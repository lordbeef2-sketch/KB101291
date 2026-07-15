# NI DOCUMENT BUNDLE: ni-dmm

<!--NI_BUNDLE_CHUNK bundle=ni-dmm start=1 end=250 -->
<!--NI_TOPIC bundle=ni-dmm path=2-wire-resistance-measurements.html language=enus -->
## TOPIC 00001: 2-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `2-wire-resistance-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/2-wire-resistance-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add inst

### 2-Wire Resistance Measurements

You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add instability to the measurement. NI recommends the Belden 83317E cable, which has excellent shielding and insulation resistance qualities and a resistance of 39 mΩ/ft. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

When considering cabling, refer to the following example:

Assume that a test system has 50 feet of copper interconnect cable hooked to a single 100 Ω resistance, such as a remote sensor device, the cable could easily introduce a resistance of ~2 Ω because Belden 83317E has a resistance of 40 mΩ/ft and 50 ft x 40 mΩ/ft = 2 Ω. The temperature coefficient of the resistance is as follows:

TC = 2Ω x 3,000 ppm/°C = 6 mΩ/°C

Relative to the 100 Ω resistance being measured:

TC = (6 mΩ/°C)/(100 Ω) = 60 ppm/°C

The error introduced by the copper not only affects the initial value of resistance measured but also introduces a temperature drift into the measurement. The drift with temperature of the copper resistance (60 ppm/°C in the example above) is much larger than the drift of the resistance ranges of the DMM (well under 10 ppm/°C). However, this drift might be perfectly acceptable to the particular measurement being made. Temperature drifts should be considered in the system error budget.

Sometimes the leads can be locally shorted, a measurement is made, and then this "offset" and its associated TC subtracted from the subsequent 2-wire resistance measurement on the resistors under test. This technique works with careful experimental measurement practice. An outline of the methodology for this technique in the context of an automated measurement system, with programmable switching available, is as follows:

1. Short the leads as close to the resistance under test as possible. If the measurement is part of an automated switching system, dedicate a switch channel to a zero value. During the measurement cycle, close the switch to the zero reference. Refer to the following figure. [IMAGE alt='image' src='GUID-671A0B9E-250B-4661-AFCD-B5BD98AFBA96-a5.svg']
2. Record the offset of this zero channel.
3. Switch to the resistance channel you want to use.
4. Measure the resistance value.
5. Subtract the offset value from the resistance value on the selected channel. The result is the resistance reading you want.

This method is subject to the following caveats:

- If the zero relay has a different contact-resistance than the rest of the relays, an error is introduced.
- If possible, you should terminate the zero channel with a cable very close in length to those cables leading to the resistance under test, matching the path length as closely as possible.
- This method does not correct for the lead resistance of the component you are testing.
- A time penalty occurs in the system and is associated with closing the zero relay and taking the additional measurement.
- The stability of the relay ON-resistance may limit this method to a repeatability of about ±20 mΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=2-wire-resistance-measurements_2.html language=enus -->
## TOPIC 00002: 2-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `2-wire-resistance-measurements_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/2-wire-resistance-measurements_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add inst

### 2-Wire Resistance Measurements

You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add instability to the measurement. NI recommends the Belden 83317E cable, which has excellent shielding and insulation resistance qualities and a resistance of 39 mΩ/ft. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

When considering cabling, refer to the following example:

Assume that a test system has 50 feet of copper interconnect cable hooked to a single 100 Ω resistance, such as a remote sensor device, the cable could easily introduce a resistance of ~2 Ω because Belden 83317E has a resistance of 40 mΩ/ft and 50 ft x 40 mΩ/ft = 2 Ω. The temperature coefficient of the resistance is as follows:

TC = 2Ω x 3,000 ppm/°C = 6 mΩ/°C

Relative to the 100 Ω resistance being measured:

TC = (6 mΩ/°C)/(100 Ω) = 60 ppm/°C

The error introduced by the copper not only affects the initial value of resistance measured but also introduces a temperature drift into the measurement. The drift with temperature of the copper resistance (60 ppm/°C in the example above) is much larger than the drift of the resistance ranges of the DMM (well under 10 ppm/°C). However, this drift might be perfectly acceptable to the particular measurement being made. Temperature drifts should be considered in the system error budget.

Sometimes the leads can be locally shorted, a measurement is made, and then this "offset" and its associated TC subtracted from the subsequent 2-wire resistance measurement on the resistors under test. This technique works with careful experimental measurement practice. An outline of the methodology for this technique in the context of an automated measurement system, with programmable switching available, is as follows:

1. Short the leads as close to the resistance under test as possible. If the measurement is part of an automated switching system, dedicate a switch channel to a zero value. During the measurement cycle, close the switch to the zero reference. Refer to the following figure. [IMAGE alt='image' src='GUID-671A0B9E-250B-4661-AFCD-B5BD98AFBA96-a5.svg']
2. Record the offset of this zero channel.
3. Switch to the resistance channel you want to use.
4. Measure the resistance value.
5. Subtract the offset value from the resistance value on the selected channel. The result is the resistance reading you want.

This method is subject to the following caveats:

- If the zero relay has a different contact-resistance than the rest of the relays, an error is introduced.
- If possible, you should terminate the zero channel with a cable very close in length to those cables leading to the resistance under test, matching the path length as closely as possible.
- This method does not correct for the lead resistance of the component you are testing.
- A time penalty occurs in the system and is associated with closing the zero relay and taking the additional measurement.
- The stability of the relay ON-resistance may limit this method to a repeatability of about ±20 mΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=2-wire-resistance-measurements_3.html language=enus -->
## TOPIC 00003: 2-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `2-wire-resistance-measurements_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/2-wire-resistance-measurements_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add inst

### 2-Wire Resistance Measurements

You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add instability to the measurement. NI recommends the Belden 83317E cable, which has excellent shielding and insulation resistance qualities and a resistance of 39 mΩ/ft. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

When considering cabling, refer to the following example:

Assume that a test system has 50 feet of copper interconnect cable hooked to a single 100 Ω resistance, such as a remote sensor device, the cable could easily introduce a resistance of ~2 Ω because Belden 83317E has a resistance of 40 mΩ/ft and 50 ft x 40 mΩ/ft = 2 Ω. The temperature coefficient of the resistance is as follows:

TC = 2Ω x 3,000 ppm/°C = 6 mΩ/°C

Relative to the 100 Ω resistance being measured:

TC = (6 mΩ/°C)/(100 Ω) = 60 ppm/°C

The error introduced by the copper not only affects the initial value of resistance measured but also introduces a temperature drift into the measurement. The drift with temperature of the copper resistance (60 ppm/°C in the example above) is much larger than the drift of the resistance ranges of the DMM (well under 10 ppm/°C). However, this drift might be perfectly acceptable to the particular measurement being made. Temperature drifts should be considered in the system error budget.

Sometimes the leads can be locally shorted, a measurement is made, and then this "offset" and its associated TC subtracted from the subsequent 2-wire resistance measurement on the resistors under test. This technique works with careful experimental measurement practice. An outline of the methodology for this technique in the context of an automated measurement system, with programmable switching available, is as follows:

1. Short the leads as close to the resistance under test as possible. If the measurement is part of an automated switching system, dedicate a switch channel to a zero value. During the measurement cycle, close the switch to the zero reference. Refer to the following figure. [IMAGE alt='image' src='GUID-671A0B9E-250B-4661-AFCD-B5BD98AFBA96-a5.svg']
2. Record the offset of this zero channel.
3. Switch to the resistance channel you want to use.
4. Measure the resistance value.
5. Subtract the offset value from the resistance value on the selected channel. The result is the resistance reading you want.

This method is subject to the following caveats:

- If the zero relay has a different contact-resistance than the rest of the relays, an error is introduced.
- If possible, you should terminate the zero channel with a cable very close in length to those cables leading to the resistance under test, matching the path length as closely as possible.
- This method does not correct for the lead resistance of the component you are testing.
- A time penalty occurs in the system and is associated with closing the zero relay and taking the additional measurement.
- The stability of the relay ON-resistance may limit this method to a repeatability of about ±20 mΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=2-wire-resistance-measurements_4.html language=enus -->
## TOPIC 00004: 2-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `2-wire-resistance-measurements_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/2-wire-resistance-measurements_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add inst

### 2-Wire Resistance Measurements

You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add instability to the measurement. NI recommends the Belden 83317E cable, which has excellent shielding and insulation resistance qualities and a resistance of 39 mΩ/ft. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

When considering cabling, refer to the following example:

Assume that a test system has 50 feet of copper interconnect cable hooked to a single 100 Ω resistance, such as a remote sensor device, the cable could easily introduce a resistance of ~2 Ω because Belden 83317E has a resistance of 40 mΩ/ft and 50 ft x 40 mΩ/ft = 2 Ω. The temperature coefficient of the resistance is as follows:

TC = 2Ω x 3,000 ppm/°C = 6 mΩ/°C

Relative to the 100 Ω resistance being measured:

TC = (6 mΩ/°C)/(100 Ω) = 60 ppm/°C

The error introduced by the copper not only affects the initial value of resistance measured but also introduces a temperature drift into the measurement. The drift with temperature of the copper resistance (60 ppm/°C in the example above) is much larger than the drift of the resistance ranges of the DMM (well under 10 ppm/°C). However, this drift might be perfectly acceptable to the particular measurement being made. Temperature drifts should be considered in the system error budget.

Sometimes the leads can be locally shorted, a measurement is made, and then this "offset" and its associated TC subtracted from the subsequent 2-wire resistance measurement on the resistors under test. This technique works with careful experimental measurement practice. An outline of the methodology for this technique in the context of an automated measurement system, with programmable switching available, is as follows:

1. Short the leads as close to the resistance under test as possible. If the measurement is part of an automated switching system, dedicate a switch channel to a zero value. During the measurement cycle, close the switch to the zero reference. Refer to the following figure. [IMAGE alt='image' src='GUID-671A0B9E-250B-4661-AFCD-B5BD98AFBA96-a5.svg']
2. Record the offset of this zero channel.
3. Switch to the resistance channel you want to use.
4. Measure the resistance value.
5. Subtract the offset value from the resistance value on the selected channel. The result is the resistance reading you want.

This method is subject to the following caveats:

- If the zero relay has a different contact-resistance than the rest of the relays, an error is introduced.
- If possible, you should terminate the zero channel with a cable very close in length to those cables leading to the resistance under test, matching the path length as closely as possible.
- This method does not correct for the lead resistance of the component you are testing.
- A time penalty occurs in the system and is associated with closing the zero relay and taking the additional measurement.
- The stability of the relay ON-resistance may limit this method to a repeatability of about ±20 mΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=2-wire-resistance-measurements_5.html language=enus -->
## TOPIC 00005: 2-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `2-wire-resistance-measurements_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/2-wire-resistance-measurements_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add inst

### 2-Wire Resistance Measurements

You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add instability to the measurement. NI recommends the Belden 83317E cable, which has excellent shielding and insulation resistance qualities and a resistance of 39 mΩ/ft. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

When considering cabling, refer to the following example:

Assume that a test system has 50 feet of copper interconnect cable hooked to a single 100 Ω resistance, such as a remote sensor device, the cable could easily introduce a resistance of ~2 Ω because Belden 83317E has a resistance of 40 mΩ/ft and 50 ft x 40 mΩ/ft = 2 Ω. The temperature coefficient of the resistance is as follows:

TC = 2Ω x 3,000 ppm/°C = 6 mΩ/°C

Relative to the 100 Ω resistance being measured:

TC = (6 mΩ/°C)/(100 Ω) = 60 ppm/°C

The error introduced by the copper not only affects the initial value of resistance measured but also introduces a temperature drift into the measurement. The drift with temperature of the copper resistance (60 ppm/°C in the example above) is much larger than the drift of the resistance ranges of the DMM (well under 10 ppm/°C). However, this drift might be perfectly acceptable to the particular measurement being made. Temperature drifts should be considered in the system error budget.

Sometimes the leads can be locally shorted, a measurement is made, and then this "offset" and its associated TC subtracted from the subsequent 2-wire resistance measurement on the resistors under test. This technique works with careful experimental measurement practice. An outline of the methodology for this technique in the context of an automated measurement system, with programmable switching available, is as follows:

1. Short the leads as close to the resistance under test as possible. If the measurement is part of an automated switching system, dedicate a switch channel to a zero value. During the measurement cycle, close the switch to the zero reference. Refer to the following figure. [IMAGE alt='image' src='GUID-671A0B9E-250B-4661-AFCD-B5BD98AFBA96-a5.svg']
2. Record the offset of this zero channel.
3. Switch to the resistance channel you want to use.
4. Measure the resistance value.
5. Subtract the offset value from the resistance value on the selected channel. The result is the resistance reading you want.

This method is subject to the following caveats:

- If the zero relay has a different contact-resistance than the rest of the relays, an error is introduced.
- If possible, you should terminate the zero channel with a cable very close in length to those cables leading to the resistance under test, matching the path length as closely as possible.
- This method does not correct for the lead resistance of the component you are testing.
- A time penalty occurs in the system and is associated with closing the zero relay and taking the additional measurement.
- The stability of the relay ON-resistance may limit this method to a repeatability of about ±20 mΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=2-wire-resistance-measurements_6.html language=enus -->
## TOPIC 00006: 2-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `2-wire-resistance-measurements_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/2-wire-resistance-measurements_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add inst

### 2-Wire Resistance Measurements

You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add instability to the measurement. NI recommends the Belden 83317E cable, which has excellent shielding and insulation resistance qualities and a resistance of 39 mΩ/ft. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

When considering cabling, refer to the following example:

Assume that a test system has 50 feet of copper interconnect cable hooked to a single 100 Ω resistance, such as a remote sensor device, the cable could easily introduce a resistance of ~2 Ω because Belden 83317E has a resistance of 40 mΩ/ft and 50 ft x 40 mΩ/ft = 2 Ω. The temperature coefficient of the resistance is as follows:

TC = 2Ω x 3,000 ppm/°C = 6 mΩ/°C

Relative to the 100 Ω resistance being measured:

TC = (6 mΩ/°C)/(100 Ω) = 60 ppm/°C

The error introduced by the copper not only affects the initial value of resistance measured but also introduces a temperature drift into the measurement. The drift with temperature of the copper resistance (60 ppm/°C in the example above) is much larger than the drift of the resistance ranges of the DMM (well under 10 ppm/°C). However, this drift might be perfectly acceptable to the particular measurement being made. Temperature drifts should be considered in the system error budget.

Sometimes the leads can be locally shorted, a measurement is made, and then this "offset" and its associated TC subtracted from the subsequent 2-wire resistance measurement on the resistors under test. This technique works with careful experimental measurement practice. An outline of the methodology for this technique in the context of an automated measurement system, with programmable switching available, is as follows:

1. Short the leads as close to the resistance under test as possible. If the measurement is part of an automated switching system, dedicate a switch channel to a zero value. During the measurement cycle, close the switch to the zero reference. Refer to the following figure. [IMAGE alt='image' src='GUID-671A0B9E-250B-4661-AFCD-B5BD98AFBA96-a5.svg']
2. Record the offset of this zero channel.
3. Switch to the resistance channel you want to use.
4. Measure the resistance value.
5. Subtract the offset value from the resistance value on the selected channel. The result is the resistance reading you want.

This method is subject to the following caveats:

- If the zero relay has a different contact-resistance than the rest of the relays, an error is introduced.
- If possible, you should terminate the zero channel with a cable very close in length to those cables leading to the resistance under test, matching the path length as closely as possible.
- This method does not correct for the lead resistance of the component you are testing.
- A time penalty occurs in the system and is associated with closing the zero relay and taking the additional measurement.
- The stability of the relay ON-resistance may limit this method to a repeatability of about ±20 mΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=2-wire-resistance-measurements_7.html language=enus -->
## TOPIC 00007: 2-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `2-wire-resistance-measurements_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/2-wire-resistance-measurements_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add inst

### 2-Wire Resistance Measurements

You can use the 2-wire method to get accurate measurements above 100 kΩ. For lower resistance values, such as 100 Ω, the interconnecting cabling can add significant resistance that can greatly affect your measurement. Copper has a temperature coefficient in the 3,000 ppm/°C range, which can add instability to the measurement. NI recommends the Belden 83317E cable, which has excellent shielding and insulation resistance qualities and a resistance of 39 mΩ/ft. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

When considering cabling, refer to the following example:

Assume that a test system has 50 feet of copper interconnect cable hooked to a single 100 Ω resistance, such as a remote sensor device, the cable could easily introduce a resistance of ~2 Ω because Belden 83317E has a resistance of 40 mΩ/ft and 50 ft x 40 mΩ/ft = 2 Ω. The temperature coefficient of the resistance is as follows:

TC = 2Ω x 3,000 ppm/°C = 6 mΩ/°C

Relative to the 100 Ω resistance being measured:

TC = (6 mΩ/°C)/(100 Ω) = 60 ppm/°C

The error introduced by the copper not only affects the initial value of resistance measured but also introduces a temperature drift into the measurement. The drift with temperature of the copper resistance (60 ppm/°C in the example above) is much larger than the drift of the resistance ranges of the DMM (well under 10 ppm/°C). However, this drift might be perfectly acceptable to the particular measurement being made. Temperature drifts should be considered in the system error budget.

Sometimes the leads can be locally shorted, a measurement is made, and then this "offset" and its associated TC subtracted from the subsequent 2-wire resistance measurement on the resistors under test. This technique works with careful experimental measurement practice. An outline of the methodology for this technique in the context of an automated measurement system, with programmable switching available, is as follows:

1. Short the leads as close to the resistance under test as possible. If the measurement is part of an automated switching system, dedicate a switch channel to a zero value. During the measurement cycle, close the switch to the zero reference. Refer to the following figure. [IMAGE alt='image' src='GUID-671A0B9E-250B-4661-AFCD-B5BD98AFBA96-a5.svg']
2. Record the offset of this zero channel.
3. Switch to the resistance channel you want to use.
4. Measure the resistance value.
5. Subtract the offset value from the resistance value on the selected channel. The result is the resistance reading you want.

This method is subject to the following caveats:

- If the zero relay has a different contact-resistance than the rest of the relays, an error is introduced.
- If possible, you should terminate the zero channel with a cable very close in length to those cables leading to the resistance under test, matching the path length as closely as possible.
- This method does not correct for the lead resistance of the component you are testing.
- A time penalty occurs in the system and is associated with closing the zero relay and taking the additional measurement.
- The stability of the relay ON-resistance may limit this method to a repeatability of about ±20 mΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=4-wire-resistance-measurements.html language=enus -->
## TOPIC 00008: 4-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `4-wire-resistance-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4-wire-resistance-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.The following figure shows a 4-wire resistance measurement, including lead resistance:In 4-wire resistance measurements, current is forced

### 4-Wire Resistance Measurements

The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.

The following figure shows a 4-wire resistance measurement, including lead resistance:

[IMAGE alt='image' src='GUID-68D5E5F3-2C62-48E6-98AD-353C73D57B8C-a5.svg']

In 4-wire resistance measurements, current is forced through the source terminals (HI, LO). The sense terminals (HI<sub>SENSE,</sub> LO<sub>SENSE</sub>) are configured for high impedance, and this configuration directs current through the resistance under test (RUT). As a result, voltage develops across RUT as well as across R<sub>LEAD1</sub> and R<sub>LEAD4</sub>. By measuring the voltage directly across RUT using the sense leads (R<sub>LEAD2,</sub> R<sub>LEAD3</sub>), the voltage drop of the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) is removed from the measurement path.

The current source in the NI DMM devices, and any of the current sources used in resistance measurements, have limited voltages that they can withstand. To avoid damage to the DMM, refer to the specifications document for your device, which lists the maximum 4-wire lead resistance, which is the maximum resistance that can occur in the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) that connect HI and LO terminals to RUT.

A maximum 4-wire lead resistance that is specified as the lesser of 10% of range or 1 kΩ implies that the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is within these limits.

For example, if you are using the 100 kΩ resistance range, 10% of this range is 10 kΩ. Therefore, the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is 1 kΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=4-wire-resistance-measurements_2.html language=enus -->
## TOPIC 00009: 4-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `4-wire-resistance-measurements_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4-wire-resistance-measurements_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.The following figure shows a 4-wire resistance measurement, including lead resistance:In 4-wire resistance measurements, current is forced

### 4-Wire Resistance Measurements

The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.

The following figure shows a 4-wire resistance measurement, including lead resistance:

[IMAGE alt='image' src='GUID-68D5E5F3-2C62-48E6-98AD-353C73D57B8C-a5.svg']

In 4-wire resistance measurements, current is forced through the source terminals (HI, LO). The sense terminals (HI<sub>SENSE,</sub> LO<sub>SENSE</sub>) are configured for high impedance, and this configuration directs current through the resistance under test (RUT). As a result, voltage develops across RUT as well as across R<sub>LEAD1</sub> and R<sub>LEAD4</sub>. By measuring the voltage directly across RUT using the sense leads (R<sub>LEAD2,</sub> R<sub>LEAD3</sub>), the voltage drop of the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) is removed from the measurement path.

The current source in the NI DMM devices, and any of the current sources used in resistance measurements, have limited voltages that they can withstand. To avoid damage to the DMM, refer to the specifications document for your device, which lists the maximum 4-wire lead resistance, which is the maximum resistance that can occur in the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) that connect HI and LO terminals to RUT.

A maximum 4-wire lead resistance that is specified as the lesser of 10% of range or 1 kΩ implies that the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is within these limits.

For example, if you are using the 100 kΩ resistance range, 10% of this range is 10 kΩ. Therefore, the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is 1 kΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=4-wire-resistance-measurements_3.html language=enus -->
## TOPIC 00010: 4-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `4-wire-resistance-measurements_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4-wire-resistance-measurements_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.The following figure shows a 4-wire resistance measurement, including lead resistance:In 4-wire resistance measurements, current is forced

### 4-Wire Resistance Measurements

The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.

The following figure shows a 4-wire resistance measurement, including lead resistance:

[IMAGE alt='image' src='GUID-68D5E5F3-2C62-48E6-98AD-353C73D57B8C-a5.svg']

In 4-wire resistance measurements, current is forced through the source terminals (HI, LO). The sense terminals (HI<sub>SENSE,</sub> LO<sub>SENSE</sub>) are configured for high impedance, and this configuration directs current through the resistance under test (RUT). As a result, voltage develops across RUT as well as across R<sub>LEAD1</sub> and R<sub>LEAD4</sub>. By measuring the voltage directly across RUT using the sense leads (R<sub>LEAD2,</sub> R<sub>LEAD3</sub>), the voltage drop of the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) is removed from the measurement path.

The current source in the NI DMM devices, and any of the current sources used in resistance measurements, have limited voltages that they can withstand. To avoid damage to the DMM, refer to the specifications document for your device, which lists the maximum 4-wire lead resistance, which is the maximum resistance that can occur in the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) that connect HI and LO terminals to RUT.

A maximum 4-wire lead resistance that is specified as the lesser of 10% of range or 1 kΩ implies that the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is within these limits.

For example, if you are using the 100 kΩ resistance range, 10% of this range is 10 kΩ. Therefore, the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is 1 kΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=4-wire-resistance-measurements_4.html language=enus -->
## TOPIC 00011: 4-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `4-wire-resistance-measurements_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4-wire-resistance-measurements_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.The following figure shows a 4-wire resistance measurement, including lead resistance:In 4-wire resistance measurements, current is forced

### 4-Wire Resistance Measurements

The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.

The following figure shows a 4-wire resistance measurement, including lead resistance:

[IMAGE alt='image' src='GUID-68D5E5F3-2C62-48E6-98AD-353C73D57B8C-a5.svg']

In 4-wire resistance measurements, current is forced through the source terminals (HI, LO). The sense terminals (HI<sub>SENSE,</sub> LO<sub>SENSE</sub>) are configured for high impedance, and this configuration directs current through the resistance under test (RUT). As a result, voltage develops across RUT as well as across R<sub>LEAD1</sub> and R<sub>LEAD4</sub>. By measuring the voltage directly across RUT using the sense leads (R<sub>LEAD2,</sub> R<sub>LEAD3</sub>), the voltage drop of the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) is removed from the measurement path.

The current source in the NI DMM devices, and any of the current sources used in resistance measurements, have limited voltages that they can withstand. To avoid damage to the DMM, refer to the specifications document for your device, which lists the maximum 4-wire lead resistance, which is the maximum resistance that can occur in the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) that connect HI and LO terminals to RUT.

A maximum 4-wire lead resistance that is specified as the lesser of 10% of range or 1 kΩ implies that the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is within these limits.

For example, if you are using the 100 kΩ resistance range, 10% of this range is 10 kΩ. Therefore, the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is 1 kΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=4-wire-resistance-measurements_5.html language=enus -->
## TOPIC 00012: 4-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `4-wire-resistance-measurements_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4-wire-resistance-measurements_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.The following figure shows a 4-wire resistance measurement, including lead resistance:In 4-wire resistance measurements, current is forced

### 4-Wire Resistance Measurements

The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.

The following figure shows a 4-wire resistance measurement, including lead resistance:

[IMAGE alt='image' src='GUID-68D5E5F3-2C62-48E6-98AD-353C73D57B8C-a5.svg']

In 4-wire resistance measurements, current is forced through the source terminals (HI, LO). The sense terminals (HI<sub>SENSE,</sub> LO<sub>SENSE</sub>) are configured for high impedance, and this configuration directs current through the resistance under test (RUT). As a result, voltage develops across RUT as well as across R<sub>LEAD1</sub> and R<sub>LEAD4</sub>. By measuring the voltage directly across RUT using the sense leads (R<sub>LEAD2,</sub> R<sub>LEAD3</sub>), the voltage drop of the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) is removed from the measurement path.

The current source in the NI DMM devices, and any of the current sources used in resistance measurements, have limited voltages that they can withstand. To avoid damage to the DMM, refer to the specifications document for your device, which lists the maximum 4-wire lead resistance, which is the maximum resistance that can occur in the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) that connect HI and LO terminals to RUT.

A maximum 4-wire lead resistance that is specified as the lesser of 10% of range or 1 kΩ implies that the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is within these limits.

For example, if you are using the 100 kΩ resistance range, 10% of this range is 10 kΩ. Therefore, the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is 1 kΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=4-wire-resistance-measurements_6.html language=enus -->
## TOPIC 00013: 4-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `4-wire-resistance-measurements_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4-wire-resistance-measurements_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.The following figure shows a 4-wire resistance measurement, including lead resistance:In 4-wire resistance measurements, current is forced

### 4-Wire Resistance Measurements

The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.

The following figure shows a 4-wire resistance measurement, including lead resistance:

[IMAGE alt='image' src='GUID-68D5E5F3-2C62-48E6-98AD-353C73D57B8C-a5.svg']

In 4-wire resistance measurements, current is forced through the source terminals (HI, LO). The sense terminals (HI<sub>SENSE,</sub> LO<sub>SENSE</sub>) are configured for high impedance, and this configuration directs current through the resistance under test (RUT). As a result, voltage develops across RUT as well as across R<sub>LEAD1</sub> and R<sub>LEAD4</sub>. By measuring the voltage directly across RUT using the sense leads (R<sub>LEAD2,</sub> R<sub>LEAD3</sub>), the voltage drop of the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) is removed from the measurement path.

The current source in the NI DMM devices, and any of the current sources used in resistance measurements, have limited voltages that they can withstand. To avoid damage to the DMM, refer to the specifications document for your device, which lists the maximum 4-wire lead resistance, which is the maximum resistance that can occur in the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) that connect HI and LO terminals to RUT.

A maximum 4-wire lead resistance that is specified as the lesser of 10% of range or 1 kΩ implies that the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is within these limits.

For example, if you are using the 100 kΩ resistance range, 10% of this range is 10 kΩ. Therefore, the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is 1 kΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=4-wire-resistance-measurements_7.html language=enus -->
## TOPIC 00014: 4-Wire Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `4-wire-resistance-measurements_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4-wire-resistance-measurements_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.The following figure shows a 4-wire resistance measurement, including lead resistance:In 4-wire resistance measurements, current is forced

### 4-Wire Resistance Measurements

The 4-wire mode requires 4-wire switching and more cabling, but it is more accurate than the 2-wire mode for precision measurements with resistances below 100 kΩ.

The following figure shows a 4-wire resistance measurement, including lead resistance:

[IMAGE alt='image' src='GUID-68D5E5F3-2C62-48E6-98AD-353C73D57B8C-a5.svg']

In 4-wire resistance measurements, current is forced through the source terminals (HI, LO). The sense terminals (HI<sub>SENSE,</sub> LO<sub>SENSE</sub>) are configured for high impedance, and this configuration directs current through the resistance under test (RUT). As a result, voltage develops across RUT as well as across R<sub>LEAD1</sub> and R<sub>LEAD4</sub>. By measuring the voltage directly across RUT using the sense leads (R<sub>LEAD2,</sub> R<sub>LEAD3</sub>), the voltage drop of the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) is removed from the measurement path.

The current source in the NI DMM devices, and any of the current sources used in resistance measurements, have limited voltages that they can withstand. To avoid damage to the DMM, refer to the specifications document for your device, which lists the maximum 4-wire lead resistance, which is the maximum resistance that can occur in the source leads (R<sub>LEAD1,</sub> R<sub>LEAD4</sub>) that connect HI and LO terminals to RUT.

A maximum 4-wire lead resistance that is specified as the lesser of 10% of range or 1 kΩ implies that the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is within these limits.

For example, if you are using the 100 kΩ resistance range, 10% of this range is 10 kΩ. Therefore, the maximum 4-wire lead resistance (R<sub>LEAD1</sub> + R<sub>LEAD4</sub>) is 1 kΩ.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=4065-dc-and-ac-current.html language=enus -->
## TOPIC 00015: DC and AC Current

- bundle_id: `ni-dmm`
- source_path: `4065-dc-and-ac-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4065-dc-and-ac-current.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4065 allows you to measure currents ranging from a few picoamps to three amperes. DC Current mode has four ranges that go from 10 mA to 3 A in decades, and AC Current mode has four ranges that go from 10 mA[rms] to 3 A[rms] in decades.Shunt ResistorsThe NI 4065 uses internal shunt resistors w

### DC and AC Current

The NI 4065 allows you to measure currents ranging from a few picoamps to three amperes. DC Current mode has four ranges that go from 10 mA to 3 A in decades, and AC Current mode has four ranges that go from 10 mA<sub>rms</sub> to 3 A<sub>rms</sub> in decades.

#### Shunt Resistors

The NI 4065 uses internal shunt resistors with temperature coefficient and power ratings selected to reduce resistor self-heating errors. For the effect of temperature changes on the accuracy of the measurements, refer to Related Documentation for the NI 4065 specifications document and the temperature coefficient. Refer to the following table for the shunt resistor values.

Tip

Parent topic:

DMM Measurements

Related concepts:

- Resistor Self-Heating

<!--NI_TOPIC bundle=ni-dmm path=4065-dmm-measurement-defaults.html language=enus -->
## TOPIC 00016: DMM Measurement Defaults

- bundle_id: `ni-dmm`
- source_path: `4065-dmm-measurement-defaults.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4065-dmm-measurement-defaults.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default measurement settings for the NI 4065. Function Aperture DC Noise Rejection DC 6½ digits 200 ms Second-Order DC 5½ digits 3.33 ms Normal DC 4½ digits^1 333 µs Normal DC Auto Range 3.33 ms Normal AC AC 6½ digits — 1 sec AC 5½ digits — Max (100 msec or (10/(minFreq

### DMM Measurement Defaults

The following table lists the default measurement settings for the NI 4065.

| Function | Aperture | DC Noise Rejection |
| --- | --- | --- |
| DC 6½ digits | 200 ms | Second-Order |
| DC 5½ digits | 3.33 ms | Normal |
| DC 4½ digits1 | 333 µs | Normal |
| DC Auto Range | 3.33 ms | Normal |
| AC | AC 6½ digits — 1 sec AC 5½ digits — Max (100 msec or (10/(minFreq))) AC 4½ digits — Max (10 msec or (5/(minFreq))) | Second-Order |
| AC Auto Range | Max (100 ms or 10/(minFreq)) | Second-Order |
| 1Settings for 3½ are equivalent to 4½. |  |  |

By default, the Aperture time and DC Noise Rejection settings for a measurement are chosen by the driver based on the configured measurement and resolution. These values are chosen to ensure accuracy for 6½–digit measurements while not sacrificing performance at lower resolutions. For more information on a particular attribute, including how to configure a non-default setting, refer to Features. For AC, 5.5 digits, the aperture is expressed as Max (AC or 10/minFreq). minFreq, or minimum frequency, is a user–programmable parameter with a default value of 20 Hz.

The same applies for other user selectable values of minFreq. For example, for a minimum frequency of 50 Hz with a 5½ digit resolution, an aperture time of 10x the period of the 50 Hz signal is required, or in this example, 200 ms.

To adjust the default aperture time, refer to Configuring Measurement Timing.

#### Default Settling Times

| Function | Settling Time |
| --- | --- |
| DC (100 mV–10 V, 100 V, 300 V) | 10 ms |
| Resistance ≤1 kΩ | 10 ms |
| Resistance 10 kΩ | 40 ms |
| Resistance 100 kΩ | 200 ms |
| Resistance 1 MΩ | 200 ms |
| Resistance ≥ 10 MΩ | 750 ms |
| AC V AC coupled | 1.5 secs |
| DC I | 10 ms |
| AC I | 1.5 secs |
| Diode | 40 ms |

To adjust the default settling times, refer to Configuring Measurement
 Timing.

Parent topic:

DMM Measurements

Related concepts:

- Features
- Configuring Measurement Timing
- DC Noise Rejection

<!--NI_TOPIC bundle=ni-dmm path=4065-dmm-measurements.html language=enus -->
## TOPIC 00017: DMM Measurements

- bundle_id: `ni-dmm`
- source_path: `4065-dmm-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4065-dmm-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections cover optimizing your measurements on the NI 4065.

### DMM Measurements

The following sections cover optimizing your measurements on the NI 4065.

- [NI 4065 DMM Measurement Cycle](ni4065-dmm-measurement-cycle.html)
- [DMM Measurement Defaults](4065-dmm-measurement-defaults.html)
- [DC Voltage](dc-voltage_7.html)
- [AC Voltage](ac-voltage_7.html)
- [DC and AC Current](4065-dc-and-ac-current.html)
- [Resistance](resistance_7.html)
- [Diode](diode_7.html)
- [Temperature Measurements](temperature-measurements_7.html)

Parent topic:

NI 4065

<!--NI_TOPIC bundle=ni-dmm path=4065-front-panel-connections.html language=enus -->
## TOPIC 00018: PXI/PCI/PCIe-4065 Front Panel Connections

- bundle_id: `ni-dmm`
- source_path: `4065-front-panel-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4065-front-panel-connections.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC Voltage AC Voltage DC Current AC Current 2-Wire Resistance 4-Wire Resistance Voltage Drop Across a Diode SCXI Communication The following table shows the pins used for SCXI communication: Pin Assignment 1–5, 7–9 SCXI Communication The NI USB-4065 does not support the ability to control SCXI swi

### PXI/PCI/PCIe-4065 Front Panel
 Connections

[IMAGE alt='image' src='GUID-55914A77-E014-4E52-912F-0E6CE55248C9-a5.svg']

Parent topic:

NI 4065

#### DC Voltage

[IMAGE alt='image' src='GUID-97AB7DF6-7C4C-428A-B56A-9992057C53FE-a5.svg']

#### AC Voltage

[IMAGE alt='image' src='GUID-E70B7331-79C2-4903-93FA-D7949F304DEF-a5.svg']

#### DC Current

[IMAGE alt='image' src='GUID-7A53197C-31C5-4F17-9B74-16DD22EA027B-a5.svg']

#### AC Current

[IMAGE alt='image' src='GUID-EDFD441E-4E8D-494E-8754-EEE9592E228B-a5.svg']

#### 2-Wire Resistance

[IMAGE alt='image' src='GUID-901DE87B-B160-4AD0-8A67-CD09BC15B511-a5.svg']

#### 4-Wire Resistance

[IMAGE alt='image' src='GUID-D0D81808-6F1B-45F0-8785-A64DBB13F774-a5.svg']

#### Voltage Drop Across a Diode

[IMAGE alt='image' src='GUID-58F5F71E-917A-48F4-B5AB-32CA8A599CC0-a5.svg']

#### SCXI Communication

[IMAGE alt='image' src='GUID-8AF1A6AB-B89D-467F-AC1E-A4191C740638-a5.svg']

The following table shows the pins used for SCXI
 communication:

| Pin | Assignment |
| --- | --- |
| 1–5, 7–9 | SCXI Communication |

Note

##### Cable Accessory

[IMAGE alt='image' src='GUID-D2759F4C-5889-43C9-B420-70071CDB9918-a5.svg']

This SH9MD-AUX
 cable allows the NI 4065 to communicate with SCXI switches. Refer to Scanning Switch
 Modules for more information.

For installation instructions for NI
 switch modules, refer to the NI Switches Help at either of the
 following locations:

- Start»All Programs»National
 Instruments»NI-SWITCH»Documentation»NI Switches Help (if you
 have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not 
 installed NI-SWITCH)

Related concepts:

- Scanning Switch Modules

#### Triggering

[IMAGE alt='image' src='GUID-8AF1A6AB-B89D-467F-AC1E-A4191C740638-a5.svg']

The following table shows the pins used for input and output triggers, which are used during synchronous scanning or handshaking:

| Pin | Assignment |
| --- | --- |
| 2 | Ground |
| 3 | AUX Trigger In |
| 6 | Measurement Complete |
| 9 | External Trigger In (Trigger/Sample Trigger) |

Note

##### Cable Accessories

For
 installation instructions for NI switch modules, refer to the NI Switches
 Help at either of the following locations:

| AUX Trigger Cable | This cable allows the NI 4065 to trigger NI switches, third-party switches, and any other external device during synchronous scanning or handshaking scanning. Note The AUX Trigger Cable only provides access to AUX I/O Connector Pins 2, 6, and 9, where Pin 2 is Ground and is present in both ends of the cable. |
| --- | --- |
| SH9MD-AUX Cable | This cable allows the NI PXI/PCI/PCIe 4065 to control SCXI switches, send measurement complete, and receive external trigger. This cable allows the NI USB 4065 to send measurement complete and receive external trigger. This functionality allows the NI 4065 to work under both synchronous scanning and handshaking scanning. Refer to Scanning Switch Modules for more information. |

- Start»Programs»National
 Instruments»NI-SWITCH»Documentation»NI Switches Help (if you
 have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not 
 installed NI-SWITCH)

#### Temperature (Thermocouple)

[IMAGE alt='image' src='GUID-A23083F8-3DEB-43F9-9F9E-00797A048FED-a5.svg']

#### Temperature (2-wire RTD)

[IMAGE alt='image' src='GUID-B3C2473F-A86F-49FF-B6E3-3629D553FD23-a5.svg']

#### Temperature (4-wire RTD)

[IMAGE alt='image' src='GUID-3927BB98-BA5F-44BB-81E3-C006491C5DC9-a5.svg']

#### Temperature (Thermistor)

[IMAGE alt='image' src='GUID-B3C2473F-A86F-49FF-B6E3-3629D553FD23-a5.svg']

<!--NI_TOPIC bundle=ni-dmm path=4065-fuse-replacement.html language=enus -->
## TOPIC 00019: Fuse Replacement

- bundle_id: `ni-dmm`
- source_path: `4065-fuse-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4065-fuse-replacement.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains how to replace the fuse in the NI 4065. For protection against fire, replace the fuse only with fuses of the same type and rating. Refer to the following table for fuse types. DMM Fuse Rating Fuse Type Manufacturer NI 4065 F 4 A H 300 V Fast-Acting ASTM F 3.15 A 250 V Fast-Acti

### Fuse Replacement

This section explains how to replace the fuse in the NI 4065.

Caution

| DMM | Fuse Rating | Fuse Type | Manufacturer |
| --- | --- | --- | --- |
| NI 4065 | F 4 A H 300 V | Fast-Acting | ASTM |
| F 3.15 A 250 V | Fast-Acting | Littelfuse |  |

Replace with the same fuse that is listed on the product. To replace the fuse,
 complete the following steps.

1. Remove all front panel connections from the NI 4065.
2. (NI PXI/PCI/PCIe-4065) Power down the chassis, and remove the device.
3. (NI USB-4065) Disconnect the USB cable from the NI USB-4065.
4. View the device at the angle shown in the figure below, and locate the fuse holder.
 NI PXI-4065 
 [IMAGE alt='image' src='GUID-132C8637-8813-4AAE-8FBD-8F4F9CF3C53D-a5.svg'] 

 1. Fuse Holder NI PCI/PCIe-4065 
 [IMAGE alt='image' src='GUID-1E24B3C0-0067-4E0E-9583-E66A101716E4-a5.svg'] 

 1. Fuse Holder NI USB-4065 [IMAGE alt='image' src='GUID-77DE497C-69CC-4012-A571-A919035A214E-a5.svg'] 

 1. Fuse Holder
5. Insert a screwdriver into the slot on the fuse holder.
6. Turn the screwdriver counterclockwise.
7. Pull out the holder, and remove the 5 x 20 mm glass fuse.
8. Verify that the fuse is blown by measuring discontinuity across the fuse using another meter.
9. Insert a new fuse into the holder, and slide the holder back into place.
10. Turn the fuse holder clockwise until it snaps shut.

Parent topic:

NI 4065

<!--NI_TOPIC bundle=ni-dmm path=40654071-input-protection.html language=enus -->
## TOPIC 00020: Input Protection

- bundle_id: `ni-dmm`
- source_path: `40654071-input-protection.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/40654071-input-protection.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The current-measuring circuit is protected with a fuse rated at F 3.15 A 250 V. The NI 4065 and NI 4071 can measure up to 3 A DC or 3 A[rms] with up to 4.2 A peak current (sine wave only). Higher currents will blow the fuse.If you apply higher current level to a range, the input protection circuitry

### Input Protection

The current-measuring circuit is protected with a fuse rated at F 3.15 A 250 V. The NI 4065 and NI 4071 can measure up to 3 A DC or 3 A<sub>rms</sub> with up to 4.2 A peak current (sine wave only). Higher currents will blow the fuse.

If you apply higher current level to a range, the input protection circuitry of the NI 4065 and NI 4071 automatically engage, and you receive an overrange warning.

Also, keep in mind that exposing the current measurement connectors to voltage sources while the DC or AC current functions are selected may trigger the input protection circuitry or even blow the fuse. Do not apply more than 150 mV to the 1 A and 3 A ranges, or more than 1 V to any of the other ranges.

For more information on fuse replacement, refer to Related Documentation for the NI Digital Multimeters Getting Started Guide.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=40654071-input-protection_2.html language=enus -->
## TOPIC 00021: Input Protection

- bundle_id: `ni-dmm`
- source_path: `40654071-input-protection_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/40654071-input-protection_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The current-measuring circuit is protected with a fuse rated at F 3.15 A 250 V. The NI 4065 and NI 4071 can measure up to 3 A DC or 3 A[rms] with up to 4.2 A peak current (sine wave only). Higher currents will blow the fuse.If you apply higher current level to a range, the input protection circuitry

### Input Protection

The current-measuring circuit is protected with a fuse rated at F 3.15 A 250 V. The NI 4065 and NI 4071 can measure up to 3 A DC or 3 A<sub>rms</sub> with up to 4.2 A peak current (sine wave only). Higher currents will blow the fuse.

If you apply higher current level to a range, the input protection circuitry of the NI 4065 and NI 4071 automatically engage, and you receive an overrange warning.

Also, keep in mind that exposing the current measurement connectors to voltage sources while the DC or AC current functions are selected may trigger the input protection circuitry or even blow the fuse. Do not apply more than 150 mV to the 1 A and 3 A ranges, or more than 1 V to any of the other ranges.

For more information on fuse replacement, refer to Related Documentation for the NI Digital Multimeters Getting Started Guide.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=4070-front-panel-connections.html language=enus -->
## TOPIC 00022: Front Panel Connections

- bundle_id: `ni-dmm`
- source_path: `4070-front-panel-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4070-front-panel-connections.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC Voltage AC Voltage DC Current AC Current 2-Wire Resistance 4-Wire Resistance Voltage Drop Across a Diode Frequency/Period Voltage Waveform Current Waveform SCXI Communication The following table shows the pins used for SCXI communication:Cable Accessory When certain NI-PXI 407x devices are insta

### Front Panel Connections

[IMAGE alt='image' src='GUID-C48DA175-628D-4B22-800C-D0133064A145-a5.svg']

Parent topic:

NI 4070

#### DC Voltage

[IMAGE alt='image' src='GUID-6A434C10-2832-4E2F-ACD3-6EE891F032F5-a5.svg']

#### AC Voltage

[IMAGE alt='image' src='GUID-C12214E2-15C8-443F-B23B-FFB83A0E7377-a5.svg']

#### DC Current

[IMAGE alt='image' src='GUID-D3833B4A-7E70-44FB-BC47-4349C404A564-a5.svg']

#### AC Current

[IMAGE alt='image' src='GUID-9E0D88D7-C5D3-4524-A66D-B4611933F15A-a5.svg']

#### 2-Wire Resistance

[IMAGE alt='image' src='GUID-EB77E92D-565F-45DF-98DB-6C2689E3E5C0-a5.svg']

#### 4-Wire Resistance

[IMAGE alt='image' src='GUID-721CF892-785A-4B46-ADA3-E0DE3F765F43-a5.svg']

#### Voltage Drop Across a Diode

[IMAGE alt='image' src='GUID-B97F1DF2-D180-4AFD-AE0B-B19AA3572714-a5.svg']

#### Frequency/Period

[IMAGE alt='image' src='GUID-C12214E2-15C8-443F-B23B-FFB83A0E7377-a5.svg']

#### Voltage Waveform

[IMAGE alt='image' src='GUID-C12214E2-15C8-443F-B23B-FFB83A0E7377-a5.svg']

#### Current Waveform

[IMAGE alt='image' src='GUID-D3833B4A-7E70-44FB-BC47-4349C404A564-a5.svg']

#### SCXI Communication

[IMAGE alt='image' src='GUID-71395A76-16B8-42E2-B092-92A897C75E5F-a5.svg']

The following table shows the pins used for SCXI communication:

##### Cable Accessory

Note

[IMAGE alt='image' src='GUID-D2759F4C-5889-43C9-B420-70071CDB9918-a5.svg']

This SH9MD-AUX cable allows the NI 4070/4071/4072 to communicate
 with SCXI switches. Refer to Scanning Switch Modules
 for more information.

For installation instructions for NI switch modules,
 refer to the NI Switches Help at either of the following
 locations:

- Start»Programs»National
 Instruments»NI-SWITCH»Documentation»NI Switches Help (if you
 have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not 
 installed NI-SWITCH)

Related concepts:

- PXI Express Compatibility
- Scanning Switch Modules

#### Triggering

[IMAGE alt='image' src='GUID-71395A76-16B8-42E2-B092-92A897C75E5F-a5.svg']

The following table shows the pins used for input and output triggers, which are used during synchronous scanning or handshaking:

| Pin | Assignment |
| --- | --- |
| Pin | Assignment |
| 2 | Ground |
| 3 | AUX Trigger In |
| 6 | Measurement Complete |
| 9 | External Trigger In (Trigger/Sample Trigger) |

##### Cable Accessories

Note

| AUX Trigger Cable | This cable allows the NI 4070/4071/4072 to trigger NI switches, third-party switches, and any other external device during synchronous scanning or handshaking scanning. Note The AUX Trigger Cable only provides access to AUX I/O Connector Pins 2, 6, and 9, where Pin 2 is Ground and is present in both ends of the cable. |
| --- | --- |
| SH9MD-AUX Cable | This cable allows the NI 4070/4071/4072 to control SCXI switches, send measurement complete, and receive external trigger. This functionality allows the NI 4070/4071/4072 to work under both synchronous scanning and handshaking scanning. Refer to Scanning Switch Modules for more information. |

For installation instructions for NI switch modules, refer to the
 NI Switches Help at either of the following locations:

- Start»Programs»National
 Instruments»NI-SWITCH»Documentation»NI Switches Help (if you
 have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not 
 installed NI-SWITCH)

#### Temperature (Thermocouple)

[IMAGE alt='image' src='GUID-2C76AC36-4319-4C59-A68A-A64693204CB4-a5.svg']

#### Temperature (2-wire RTD)

[IMAGE alt='image' src='GUID-7B5AA879-8371-49D3-A3EA-89CAF4B7DBBE-a5.svg']

#### Temperature (4-wire RTD)

[IMAGE alt='image' src='GUID-8277B097-1BE6-40CD-95BF-043F0E531079-a5.svg']

#### Temperature (Thermistor)

[IMAGE alt='image' src='GUID-7B5AA879-8371-49D3-A3EA-89CAF4B7DBBE-a5.svg']

<!--NI_TOPIC bundle=ni-dmm path=4070-fuse-replacement.html language=enus -->
## TOPIC 00023: Fuse Replacement

- bundle_id: `ni-dmm`
- source_path: `4070-fuse-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4070-fuse-replacement.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains how to replace the fuse in the NI 4070. For protection against fire, replace the fuse only with fuses of the same type and rating. Refer to the following table for fuse types. DMM Fuse Rating Fuse Type Manufacturer PCI-4070 F 1.6 A H 300 V Fast-Acting ASTM PXI-4070 F 1.25 A 250

### Fuse Replacement

This section explains how to replace the fuse in the NI 4070.

Caution

| DMM | Fuse Rating | Fuse Type | Manufacturer |
| --- | --- | --- | --- |
| PCI-4070 | F 1.6 A H 300 V | Fast-Acting | ASTM |
| PXI-4070 | F 1.25 A 250 V | Fast-Acting | Littelfuse |

Replace with the same fuse that is listed on the product. To replace the fuse, complete the
 following steps.

#### NI PXI-4070

1. Remove all front panel connections from the device.
2. Power off the chassis, and remove the device.
3. Locate the fuse hold shown in the figure below. [IMAGE alt='image' src='GUID-7AE2373D-0BB5-42A8-A2AB-4FCF0E4DB05D-a5.svg'] 

 1. Screwdriver
 2. Fuse Hole
4. Insert a screwdriver into the fuse hole. Caution Do not cover the
 fuse slot on the opposite side of the device with your hand, as doing so may
 cause injury.
5. Gently press the fuse with the screwdriver until one of the fuse clamps
 releases.
6. Locate the fuse slot shown in the figure below. [IMAGE alt='image' src='GUID-871F2DF6-3494-459D-92C1-7977367D1092-a5.svg'] 

 1. Fuse
 2. Fuse Slot
7. Pry the fuse loose from the fuse slot.
8. Verify that the fuse is blown by measuring discontinuity across the fuse using
 another meter.
9. Insert a new fuse into the fuse slot as shown in the figure below. [IMAGE alt='image' src='GUID-6BEE79F1-63DC-4EEC-A27C-DCA32EE89E87-a5.svg'] 

 1. Fuse
 2. Fuse Slot
10. Gently press the fuse with the screwdriver until both fuse clamps snap the fuse
 into place.

#### NI PCI-4070

1. Remove all front panel connections from the device.
2. Power off the computer, and remove the device.
3. Hold the device at the angle shown in the figure below, and locate the fuse holder. [IMAGE alt='image' src='GUID-3D65305E-2393-417C-A755-DDA0C700E1C6-a5.svg'] 

 1. Fuse Holder
4. Insert a screwdriver into the slot on the fuse holder.
5. Turn the screwdriver counterclockwise.
6. Pull out the fuse holder, and remove the 5 x 20 mm fuse.
7. Insert a new fuse into the holder, and slide the holder back into place.
8. Turn the fuse holder clockwise until it snaps shut.

Parent topic:

NI 4070

<!--NI_TOPIC bundle=ni-dmm path=4070728082-dc-and-ac-current.html language=enus -->
## TOPIC 00024: DC and AC Current

- bundle_id: `ni-dmm`
- source_path: `4070728082-dc-and-ac-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4070728082-dc-and-ac-current.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can measure currents ranging from a few nanoamperes to an ampere on your DMM.DC Current mode and AC Current mode have three ranges each for the NI 4080/4082 and NI 4070/4072: 20 mA, 200 mA, and 1 A for DC current; 10 mA, 100 mA, and 1 A for AC[rms] current. The AC Current mode uses the same fast

### DC and AC Current

You can measure currents ranging from a few nanoamperes to an ampere on your DMM.

DC Current mode and AC Current mode have three ranges each for the NI 4080/4082 and NI 4070/4072: 20 mA, 200 mA, and 1 A for DC current; 10 mA, 100 mA, and 1 A for AC<sub>rms</sub> current. The AC Current mode uses the same fast measurement technique as the AC Volts DC Coupled mode.

#### Shunt Resistor

For all ranges, the current you measure flows through a stable onboard 0.5 Ω precision shunt resistor with temperature coefficient and power ratings selected to reduce resistor self-heating errors. For the effect of temperature changes on the accuracy of the measurements, refer to the specifications document for your device.

Note

#### Related Topics

Resistor Self-Heating

Parent topic:

DMM Measurements

Related concepts:

- Resistor Self-Heating

<!--NI_TOPIC bundle=ni-dmm path=4070728082-dc-and-ac-current_2.html language=enus -->
## TOPIC 00025: DC and AC Current

- bundle_id: `ni-dmm`
- source_path: `4070728082-dc-and-ac-current_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4070728082-dc-and-ac-current_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can measure currents ranging from a few nanoamperes to an ampere on your DMM.DC Current mode and AC Current mode have three ranges each for the NI 4080/4082 and NI 4070/4072: 20 mA, 200 mA, and 1 A for DC current; 10 mA, 100 mA, and 1 A for AC[rms] current. The AC Current mode uses the same fast

### DC and AC Current

You can measure currents ranging from a few nanoamperes to an ampere on your DMM.

DC Current mode and AC Current mode have three ranges each for the NI 4080/4082 and NI 4070/4072: 20 mA, 200 mA, and 1 A for DC current; 10 mA, 100 mA, and 1 A for AC<sub>rms</sub> current. The AC Current mode uses the same fast measurement technique as the AC Volts DC Coupled mode.

#### Shunt Resistor

For all ranges, the current you measure flows through a stable onboard 0.5 Ω precision shunt resistor with temperature coefficient and power ratings selected to reduce resistor self-heating errors. For the effect of temperature changes on the accuracy of the measurements, refer to the specifications document for your device.

Note

#### Related Topics

Resistor Self-Heating

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=4070728082-dc-and-ac-current_3.html language=enus -->
## TOPIC 00026: DC and AC Current

- bundle_id: `ni-dmm`
- source_path: `4070728082-dc-and-ac-current_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4070728082-dc-and-ac-current_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can measure currents ranging from a few nanoamperes to an ampere on your DMM.DC Current mode and AC Current mode have three ranges each for the NI 4080/4082 and NI 4070/4072: 20 mA, 200 mA, and 1 A for DC current; 10 mA, 100 mA, and 1 A for AC[rms] current. The AC Current mode uses the same fast

### DC and AC Current

You can measure currents ranging from a few nanoamperes to an ampere on your DMM.

DC Current mode and AC Current mode have three ranges each for the NI 4080/4082 and NI 4070/4072: 20 mA, 200 mA, and 1 A for DC current; 10 mA, 100 mA, and 1 A for AC<sub>rms</sub> current. The AC Current mode uses the same fast measurement technique as the AC Volts DC Coupled mode.

#### Shunt Resistor

For all ranges, the current you measure flows through a stable onboard 0.5 Ω precision shunt resistor with temperature coefficient and power ratings selected to reduce resistor self-heating errors. For the effect of temperature changes on the accuracy of the measurements, refer to the specifications document for your device.

Note

#### Related Topics

Resistor Self-Heating

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=4070728082-dc-and-ac-current_4.html language=enus -->
## TOPIC 00027: DC and AC Current

- bundle_id: `ni-dmm`
- source_path: `4070728082-dc-and-ac-current_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4070728082-dc-and-ac-current_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can measure currents ranging from a few nanoamperes to an ampere on your DMM.DC Current mode and AC Current mode have three ranges each for the NI 4080/4082 and NI 4070/4072: 20 mA, 200 mA, and 1 A for DC current; 10 mA, 100 mA, and 1 A for AC[rms] current. The AC Current mode uses the same fast

### DC and AC Current

You can measure currents ranging from a few nanoamperes to an ampere on your DMM.

DC Current mode and AC Current mode have three ranges each for the NI 4080/4082 and NI 4070/4072: 20 mA, 200 mA, and 1 A for DC current; 10 mA, 100 mA, and 1 A for AC<sub>rms</sub> current. The AC Current mode uses the same fast measurement technique as the AC Volts DC Coupled mode.

#### Shunt Resistor

For all ranges, the current you measure flows through a stable onboard 0.5 Ω precision shunt resistor with temperature coefficient and power ratings selected to reduce resistor self-heating errors. For the effect of temperature changes on the accuracy of the measurements, refer to the specifications document for your device.

Note

#### Related Topics

Resistor Self-Heating

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=4071-dc-and-ac-current.html language=enus -->
## TOPIC 00028: DC and AC Current

- bundle_id: `ni-dmm`
- source_path: `4071-dc-and-ac-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4071-dc-and-ac-current.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4071 allows you to measure currents ranging from a few picoamps to three amperes. DC Current mode has eight ranges that go from 1 µA to 3 A in decades, and AC Current mode has six ranges that go from 100 µA[rms] to 3 A[rms] in decades. The AC Current mode uses the same fast measurement techni

### DC and AC Current

The NI 4071 allows you to measure currents ranging from a few picoamps to three amperes. DC Current mode has eight ranges that go from 1 µA to 3 A in decades, and AC Current mode has six ranges that go from 100 µA<sub>rms</sub> to 3 A<sub>rms</sub> in decades. The AC Current mode uses the same fast measurement technique as the AC Volts DC Coupled mode.

Note

#### Shunt Resistors

The NI 4071
 uses internal shunt resistors with temperature coefficient and power ratings
 selected to reduce resistor self-heating
 errors. For the effect of temperature changes on the accuracy of the measurements,
 refer to Related Documentation for the NI 4071 specifications document and the
 temperature coefficient. Refer to the following table for the shunt resistor
 values.

| Range | Shunt Resistor Value |
| --- | --- |
| 3 A | 0.05 Ω |
| 1 A | 0.05 Ω |
| 100 mA | 0.5 Ω |
| 10 mA | 5 Ω |
| 1 mA | 50 Ω |
| 100 µA | 500 Ω |
| 10 µA | 50 kΩ |
| 1 µA | 50 kΩ |

Caution

Whenever possible, switch the NI 4071 into the current measurement function before applying the current. Switching inductive current sources generally creates flyback voltages that stress the relay and, if done frequently, can shorten the reliability of the relay. Also, avoid interrupting the current by switching out of the current measurement function when currents are flowing through the circuit.

Parent topic:

DMM Measurements

Related concepts:

- Resistor Self-Heating

<!--NI_TOPIC bundle=ni-dmm path=4071-front-panel-connections.html language=enus -->
## TOPIC 00029: Front Panel Connections

- bundle_id: `ni-dmm`
- source_path: `4071-front-panel-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4071-front-panel-connections.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC Voltage AC Voltage DC Current AC Current 2-Wire Resistance 4-Wire Resistance Voltage Drop Across a Diode Frequency/Period Voltage Waveform Current Waveform SCXI Communication The following table shows the pins used for SCXI communication: Pin Assignment 1–5, 7–9 SCXI Communication Cable Accessory

### Front Panel Connections

[IMAGE alt='image' src='GUID-244CEBFE-539F-446E-A1EC-DAEB91B9E1A4-a5.svg']

Parent topic:

NI 4071

#### DC Voltage

[IMAGE alt='image' src='GUID-6E6B2F65-B6D4-4E0E-A8CE-FD423C2E2B94-a5.svg']

#### AC Voltage

[IMAGE alt='image' src='GUID-833133C8-12D1-40EC-A223-137603F7C94D-a5.svg']

#### DC Current

[IMAGE alt='image' src='GUID-D4C4A935-8DCE-48AB-93F5-FE329C5735B8-a5.svg']

#### AC Current

[IMAGE alt='image' src='GUID-41252619-02E4-47A3-9D1A-31B09BF43B4B-a5.svg']

#### 2-Wire Resistance

[IMAGE alt='image' src='GUID-8A6D6378-AACF-4373-926F-42979C945A84-a5.svg']

#### 4-Wire Resistance

[IMAGE alt='image' src='GUID-1D371393-9472-4340-898E-EECCDDD9864E-a5.svg']

#### Voltage Drop Across a Diode

[IMAGE alt='image' src='GUID-B0106A70-4BE9-430A-ADB0-CCE3D6C4329E-a5.svg']

#### Frequency/Period

[IMAGE alt='image' src='GUID-833133C8-12D1-40EC-A223-137603F7C94D-a5.svg']

#### Voltage Waveform

[IMAGE alt='image' src='GUID-833133C8-12D1-40EC-A223-137603F7C94D-a5.svg']

#### Current Waveform

[IMAGE alt='image' src='GUID-D4C4A935-8DCE-48AB-93F5-FE329C5735B8-a5.svg']

#### SCXI Communication

[IMAGE alt='image' src='GUID-3A3EE455-C789-40AA-9B31-EA865EA019B7-a5.svg']

The following table shows the pins used for SCXI communication:

| Pin | Assignment |
| --- | --- |
| 1–5, 7–9 | SCXI Communication |

##### Cable Accessory

Note

[IMAGE alt='image' src='GUID-D2759F4C-5889-43C9-B420-70071CDB9918-a5.svg']

This SH9MD-AUX cable allows the NI 4070/4071/4072 to communicate
 with SCXI switches. Refer to Scanning Switch Modules
 for more information.

For installation instructions for NI switch modules,
 refer to the NI Switches Help at either of the following
 locations:

- Start»Programs»National
 Instruments»NI-SWITCH»Documentation»NI Switches Help (if you
 have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not 
 installed NI-SWITCH)

Related concepts:

- PXI Express Compatibility
- Scanning Switch Modules

#### Triggering

[IMAGE alt='image' src='GUID-3A3EE455-C789-40AA-9B31-EA865EA019B7-a5.svg']

The following table shows the pins used for input and output triggers, which are used during synchronous scanning or handshaking:

| Pin | Assignment |
| --- | --- |
| 2 | Ground |
| 3 | AUX Trigger In |
| 6 | Measurement Complete |
| 9 | External Trigger In (Trigger/Sample Trigger) |

##### Cable Accessories

Note

| AUX Trigger Cable | This cable allows the NI 4070/4071/4072 to trigger NI switches, third-party switches, and any other external device during synchronous scanning or handshaking scanning. Note The AUX Trigger Cable only provides access to AUX I/O Connector Pins 2, 6, and 9, where Pin 2 is Ground and is present in both ends of the cable. |
| --- | --- |
| SH9MD-AUX Cable | This cable allows the NI 4070/4071/4072 to control SCXI switches, send measurement complete, and receive external trigger. This functionality allows the NI 4070/4071/4072 to work under both synchronous scanning and handshaking scanning. Refer to Scanning Switch Modules for more information. |

For installation instructions for NI switch modules, refer to the
 NI Switches Help at either of the following locations:

- Start»Programs»National
 Instruments»NI-SWITCH»Documentation»NI Switches Help (if you
 have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not 
 installed NI-SWITCH)

#### Temperature (Thermocouple)

[IMAGE alt='image' src='GUID-6691213F-BD7B-4FBC-82E4-1F6CEEFCB266-a5.svg']

#### Temperature (2-wire RTD)

[IMAGE alt='image' src='GUID-DCF27FF7-42CD-420E-9DAE-4F89288C6884-a5.svg']

#### Temperature (4-wire RTD)

[IMAGE alt='image' src='GUID-C3033B36-296E-4B84-80C9-0588D2F9A1E9-a5.svg']

#### Temperature (Thermistor)

[IMAGE alt='image' src='GUID-DCF27FF7-42CD-420E-9DAE-4F89288C6884-a5.svg']

<!--NI_TOPIC bundle=ni-dmm path=4071-fuse-replacement.html language=enus -->
## TOPIC 00030: Fuse Replacement

- bundle_id: `ni-dmm`
- source_path: `4071-fuse-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4071-fuse-replacement.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains how to replace the fuse in the NI 4071. For protection against fire, replace the fuse only with fuses of the same type and rating. Refer to the following table for fuse types. DMM Fuse Rating Fuse Type Manufacturer NI 4071 F 3.15 A 250 V Fast-Acting Littelfuse To replace the fu

### Fuse Replacement

This section explains how to replace the fuse in the NI 4071.

Caution

| DMM | Fuse Rating | Fuse Type | Manufacturer |
| --- | --- | --- | --- |
| NI 4071 | F 3.15 A 250 V | Fast-Acting | Littelfuse |

To replace the fuse, complete the following steps.

1. Remove all front panel connections from the device.
2. Power off the chassis, and remove the device.
3. Locate the fuse hold shown in the figure below. [IMAGE alt='image' src='GUID-7AE2373D-0BB5-42A8-A2AB-4FCF0E4DB05D-a5.svg'] 

 1. Screwdriver
 2. Fuse Hole
4. Insert a screwdriver into the fuse hole. Caution Do not cover the fuse slot on the opposite side of the device with your hand, as doing so may cause injury.
5. Gently press the fuse with the screwdriver until one of the fuse clamps releases.
6. Locate the fuse slot shown in the figure below. [IMAGE alt='image' src='GUID-871F2DF6-3494-459D-92C1-7977367D1092-a5.svg'] 

 1. Fuse
 2. Fuse Slot
7. Pry the fuse loose from the fuse slot.
8. Verify that the fuse is blown by measuring discontinuity across the fuse using another meter.
9. Insert a new fuse into the fuse slot as shown in the figure below. [IMAGE alt='image' src='GUID-6BEE79F1-63DC-4EEC-A27C-DCA32EE89E87-a5.svg'] 

 1. Fuse
 2. Fuse Slot
10. Gently press the fuse with the screwdriver until both fuse clamps snap the fuse into place.

#### NI PXI-4071

Parent topic:

NI 4071

<!--NI_TOPIC bundle=ni-dmm path=4072-admittance.html language=enus -->
## TOPIC 00031: Admittance

- bundle_id: `ni-dmm`
- source_path: `4072-admittance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-admittance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To simplify mathematical manipulation, calculation, and analysis, it is sometimes convenient to express the impedance as its reciprocal quantity, or admittance. Admittance is defined asY = 1/Z = I/Vand can be written asY = G + jBwhere G and B are the rectangular (real and imaginary) components, know

### Admittance

To simplify mathematical manipulation, calculation, and analysis, it is sometimes convenient to express the impedance as its reciprocal quantity, or admittance. Admittance is defined as

Y = 1/Z = I/V

and can be written as

Y = G + jB

where G and B are the rectangular (real and imaginary) components, known as conductance and susceptance respectively. The conductance G is the reciprocal of the parallel resistance, as follows:

G = 1/R<sub>P</sub>

The susceptance for capacitors is expressed as follows:

B<sub>C</sub> = 2[IMAGE alt='image' src='GUID-CC0315BF-B093-4875-ADCB-08A9AD050B4C-a5.gif']fC<sub>P</sub> = 1/X<sub>C</sub>

The susceptance for inductors is expressed as follows:

B<sub>L</sub> = 1/2[IMAGE alt='image' src='GUID-CC0315BF-B093-4875-ADCB-08A9AD050B4C-a5.gif']fL<sub>P</sub> = 1/X<sub>L</sub>

Parent topic:

Theoretical Background

<!--NI_TOPIC bundle=ni-dmm path=4072-cabling.html language=enus -->
## TOPIC 00032: Cabling

- bundle_id: `ni-dmm`
- source_path: `4072-cabling.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-cabling.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To reduce variations on the system parasitics, NI recommends using coaxial cable or shielded twisted pairs, with the shield used as the current return path and connected to the LO input of the DMM. This configuration makes the OPEN/SHORT compensation more practical and helps to reduce the noise pick

### Cabling

To reduce variations on the system parasitics, NI recommends using coaxial cable or shielded twisted pairs, with the shield used as the current return path and connected to the LO input of the DMM. This configuration makes the OPEN/SHORT compensation more practical and helps to reduce the noise pickup.

For manual probing of surface mount parts, you can use a pair of tweezers. The NI 4072 can compensate for the impedance introduced by the test fixtures. Refer to the OPEN/SHORT Compensation section for more information. Reduce the mechanical variations (for example, movement or flexing of cables, or changing fixturing) between two consecutive measurements to maintain repeatability.

Use a high-quality cable, such as Belden 83317E available at www.belden.com. NI recommends cables with Teflon, polypropylene, or polyethylene insulation. For more information about cabling requirements, refer to Interconnects and Cables. Very good performance has been achieved using up to 25 feet of this cable in both capacitance and inductance measurements by performing OPEN/SHORT compensation prior to the measurement.

Parent topic:

Measurement Considerations

Related concepts:

- OPEN/SHORT Compensation
- NI 4070

<!--NI_TOPIC bundle=ni-dmm path=4072-capacitanceinductance.html language=enus -->
## TOPIC 00033: Capacitance/Inductance

- bundle_id: `ni-dmm`
- source_path: `4072-capacitanceinductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-capacitanceinductance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4072 uses a 2-wire, multi-tone, constant current technique to measure impedance. When a multi-tone constant current source (I[src]) is applied to the device under test (DUT), the NI 4072 measures the fundamental and third harmonic of the voltage waveform.If the residual series impedance (Z[s]

### Capacitance/Inductance

The NI 4072 uses a 2-wire, multi-tone, constant current technique to measure impedance. When a multi-tone constant current source (I<sub>src</sub>) is applied to the device under test (DUT), the NI 4072 measures the fundamental and third harmonic of the voltage waveform.

[IMAGE alt='image' src='GUID-ED3A7AED-DEA3-482A-81D1-8780216530C6-a5.svg']

If the residual series impedance (Z<sub>s</sub>) and the stray parallel admittance (Y<sub>p</sub>) introduce a significant error in the measurement, the NI 4072 can measure the magnitude of the error and reduce it using compensation techniques. For more information, refer to the OPEN/SHORT Compensation section.

Refer to the NI 4072 section for the measurement ranges on the NI 4072 for the capacitance and inductance modes.

- [Theoretical Background](4072-theoretical-background.html)
- [Model](4072-model.html)
- [Test Signal](4072-test-signal.html)
- [Measurement Considerations](4072-measurement-considerations.html)
- [DC Bias](4072-dc-bias.html)
- [OPEN/SHORT Compensation](4072-openshort-compensation.html)
- [Performing Offset Nulling](performing-offset-nulling_12.html)

Parent topic:

DMM Measurements

Related concepts:

- OPEN/SHORT Compensation
- NI 4072

<!--NI_TOPIC bundle=ni-dmm path=4072-capacitors.html language=enus -->
## TOPIC 00034: Capacitors

- bundle_id: `ni-dmm`
- source_path: `4072-capacitors.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-capacitors.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A capacitor is an electronic component that is capable of storing energy as charge. Each capacitor consists of two plates of conductive material that are separated by a dielectric, which could be air, paper, plastic, oxide or any other type of insulator. The dielectric constant, or K, of an insulato

### Capacitors

A capacitor is an electronic component
 that is capable of storing energy as charge. Each capacitor consists of two plates
 of conductive material that are separated by a dielectric, which could be air,
 paper, plastic, oxide or any other type of insulator. The dielectric constant, or
 K, of an insulator represents its ability to store charge.
 The table below shows the K values for different dielectric
 materials:

| Dielectric | Dielectric Constant (K) |
| --- | --- |
| Vacuum | 1 |
| Air | 1.0001 |
| Teflon | 2.0 |
| Polypropylene | 2.1 |
| Polystyrene | 2.5 |
| Polycarbonate | 2.9 |
| Polyester | 3.2 |
| FR-4 | 3.8–5.0 |
| Glass | 4.0–8.5 |
| Mica | 6.5–8.7 |
| Ceramics | 6 to several thousand |
| Aluminum oxide | 7 |
| Tantalum oxide | 11 |

The electrical properties of insulators show variability with factors such as
 temperature, frequency, voltage, and humidity. This variability and the mechanical
 construction of the capacitor create a less than ideal device.

A better
 representation of real-world capacitors is shown in the equivalent model below,
 which aids in understanding the different parasitic elements that are present in a
 real-world component. These parasitic elements impact the capacitor impedance at
 different test frequencies.

[IMAGE alt='image' src='GUID-E69E69C9-098E-4AF9-B077-DE2B52574A33-a5.svg']

The parallel
 resistance, Rp, is usually a large value, and its effect is
 significant only when measuring capacitors with small values. The equivalent series
 resistance, Rs, although a small value, is important in
 capacitors with large values, where the impedance is small compared to
 Rs and where high power is dissipated. The series inductance,
 Ls, represents the total inductance and capacitance roll-off
 at higher frequencies.

At low frequencies, capacitance varies with frequency
 and the test signal level, due to changes in the dielectric properties. The
 following graph shows a 2.2 µF 100 V aluminum electrolytic capacitor measured at
 different frequencies. The error is referenced to the measurement using a 1
 V<sub>rms</sub> AC test signal at 1 kHz.

[IMAGE alt='image' src='GUID-AE3640B0-4BBE-42EE-8423-8CF0627C2C76-a5.gif']

These factors
 cause capacitors to have different values under varying conditions of temperature,
 frequency, and signal level.

Parent topic:

Theoretical Background

<!--NI_TOPIC bundle=ni-dmm path=4072-dc-bias.html language=enus -->
## TOPIC 00035: DC Bias

- bundle_id: `ni-dmm`
- source_path: `4072-dc-bias.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-dc-bias.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To test some polarized components, such as electrolytic and tantalum capacitors, it may be preferable to use only positive voltages. During normal operation, the AC current source swings negative 50% of the time, which results in an inverse polarization of the capacitor under test. To prevent this i

### DC Bias

To test some polarized components, such as electrolytic and tantalum capacitors, it may be preferable to use only positive voltages. During normal operation, the AC current source swings negative 50% of the time, which results in an inverse polarization of the capacitor under test. To prevent this inverse polarization, you can apply a DC bias to prevent the voltage across the part from becoming negative.

Note

The DC bias voltage is a fixed value and can only be turned on and off. The nominal voltage value is 0.45 V and can be used for the 300 pF, 1 nF, 10 nF, 100 nF, 1000 µF and 10,000 µF capacitance ranges. The default setting is OFF.

Parent topic:

Capacitance/Inductance

<!--NI_TOPIC bundle=ni-dmm path=4072-frequency-effects-of-real-world-components.html language=enus -->
## TOPIC 00036: Frequency Effects of Real-World Components

- bundle_id: `ni-dmm`
- source_path: `4072-frequency-effects-of-real-world-components.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-frequency-effects-of-real-world-components.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Due to the parasitics and materials used in the construction of real-world components, the measured capacitance or inductance value can differ from one instrument to another. When measuring capacitors with better dielectric properties, you observe much smaller reading differences between various ins

### Frequency Effects of Real-World Components

Due to the parasitics and materials used in the construction of real-world components, the measured capacitance or inductance value can differ from one instrument to another. When measuring capacitors with better dielectric properties, you observe much smaller reading differences between various instruments. This observation also applies to inductors with better magnetics.

The following table shows some examples of dielectrics with good and poor frequency characteristics:

| Dielectrics with Good Frequency Characteristics | Dielectrics with Poor Frequency Characteristics |
| --- | --- |
| Dielectrics with Good Frequency Characteristics | Dielectrics with Poor Frequency Characteristics |
| Teflon Mica Polypropylene Polycarbonate Ceramic COG | Tantalum oxide Aluminum oxide Ceramic Y5U |

Due to the amount of magnetization current required, you can see an increase in sensitivity to frequency changes and other dependency factors in inductors with cores of larger dimensions, such as those used in transformers and power inductors.

Parent topic:

Measurement Considerations

<!--NI_TOPIC bundle=ni-dmm path=4072-front-panel-connections.html language=enus -->
## TOPIC 00037: Front Panel Connections

- bundle_id: `ni-dmm`
- source_path: `4072-front-panel-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-front-panel-connections.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Capacitance Inductance DC Voltage AC Current AC Voltage DC Current 2-Wire Resistance 4-Wire Resistance Voltage Drop Across a Diode Frequency/Period Voltage Waveform Current Waveform SCXI Communication The following table shows the pins used for SCXI communication: Pin Assignment 1–5, 7–9 SCXI Commun

### Front Panel Connections

[IMAGE alt='image' src='GUID-061BCEC1-6613-4346-AA78-6480020F0391-a5.svg']

Parent topic:

NI 4072

#### Capacitance

[IMAGE alt='image' src='GUID-4BDEA910-9A52-42A7-83D4-DC7EFDAF0C9F-a5.svg']

#### Inductance

[IMAGE alt='image' src='GUID-2839272F-EEB4-44FE-86D6-D97A173DE66E-a5.svg']

#### DC Voltage

[IMAGE alt='image' src='GUID-1692A687-A9D2-4EDC-B4E6-107238819266-a5.svg']

#### AC Current

[IMAGE alt='image' src='GUID-8B57659E-512D-436F-B4DB-5E358243A18B-a5.svg']

#### AC Voltage

[IMAGE alt='image' src='GUID-9A00D618-2617-498B-96BE-6FCDD6F6D5E0-a5.svg']

#### DC Current

[IMAGE alt='image' src='GUID-0B837CD8-D07F-4BA1-8900-30712B2C4AA5-a5.svg']

#### 2-Wire Resistance

[IMAGE alt='image' src='GUID-A1BCA760-2589-49CE-A443-0E04DB51BA42-a5.svg']

#### 4-Wire Resistance

[IMAGE alt='image' src='GUID-3A94CCAA-7CA8-4CB8-BDD2-6AF6B89AE449-a5.svg']

#### Voltage Drop Across a Diode

[IMAGE alt='image' src='GUID-C0D10D8D-A5B5-4A70-A8F2-647F64723ACF-a5.svg']

#### Frequency/Period

[IMAGE alt='image' src='GUID-9A00D618-2617-498B-96BE-6FCDD6F6D5E0-a5.svg']

#### Voltage Waveform

[IMAGE alt='image' src='GUID-9A00D618-2617-498B-96BE-6FCDD6F6D5E0-a5.svg']

#### Current Waveform

[IMAGE alt='image' src='GUID-0B837CD8-D07F-4BA1-8900-30712B2C4AA5-a5.svg']

#### SCXI Communication

[IMAGE alt='image' src='GUID-EBCEED06-5FC3-453F-97C0-191A0553A0EA-a5.svg']

The following table shows the pins used for SCXI communication:

| Pin | Assignment |
| --- | --- |
| 1–5, 7–9 | SCXI Communication |

##### Cable Accessory

Note

[IMAGE alt='image' src='GUID-D2759F4C-5889-43C9-B420-70071CDB9918-a5.svg']

This SH9MD-AUX cable allows the NI 4070/4071/4072 to communicate
 with SCXI switches. Refer to Scanning Switch Modules
 for more information.

For installation instructions for NI switch modules,
 refer to the NI Switches Help at either of the following
 locations:

- Start»Programs»National
 Instruments»NI-SWITCH»Documentation»NI Switches Help (if you
 have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not 
 installed NI-SWITCH)

Related concepts:

- PXI Express Compatibility
- Scanning Switch Modules

#### Triggering

[IMAGE alt='image' src='GUID-EBCEED06-5FC3-453F-97C0-191A0553A0EA-a5.svg']

The following table shows the pins used for input and output triggers, which are used during synchronous scanning or handshaking:

| Pin | Assignment |
| --- | --- |
| 2 | Ground |
| 3 | AUX Trigger In |
| 6 | Measurement Complete |
| 9 | External Trigger In (Trigger/Sample Trigger) |

##### Cable Accessories

Note

| AUX Trigger Cable | This cable allows the NI 4070/4071/4072 to trigger NI switches, third-party switches, and any other external device during synchronous scanning or handshaking scanning. Note The AUX Trigger Cable only provides access to AUX I/O Connector Pins 2, 6, and 9, where Pin 2 is Ground and is present in both ends of the cable. |
| --- | --- |
| SH9MD-AUX Cable | This cable allows the NI 4070/4071/4072 to control SCXI switches, send measurement complete, and receive external trigger. This functionality allows the NI 4070/4071/4072 to work under both synchronous scanning and handshaking scanning. Refer to Scanning Switch Modules for more information. |

For installation instructions for NI switch modules, refer to the
 NI Switches Help at either of the following locations:

- Start»Programs»National
 Instruments»NI-SWITCH»Documentation»NI Switches Help (if you
 have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not 
 installed NI-SWITCH)

#### Temperature (Thermocouple)

[IMAGE alt='image' src='GUID-6E702787-C242-4704-AC04-0DA448220C88-a5.svg']

#### Temperature (2-wire RTD)

[IMAGE alt='image' src='GUID-FBC068F3-5BA2-4993-83B2-BAB49EBDAAA6-a5.svg']

#### Temperature (4-wire RTD)

[IMAGE alt='image' src='GUID-F5132F87-EDE5-454A-9464-B7C9EDF61C33-a5.svg']

#### Temperature (Thermistor)

[IMAGE alt='image' src='GUID-FBC068F3-5BA2-4993-83B2-BAB49EBDAAA6-a5.svg']

<!--NI_TOPIC bundle=ni-dmm path=4072-fuse-replacement.html language=enus -->
## TOPIC 00038: Fuse Replacement

- bundle_id: `ni-dmm`
- source_path: `4072-fuse-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-fuse-replacement.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains how to replace the fuse in the NI 4072. For protection against fire, replace the fuse only with fuses of the same type and rating. Refer to the following table for fuse types. DMM Fuse Rating Fuse Type Manufacturer NI 4072 F 1.25 A 250 V Fast-Acting Littelfuse To replace the fu

### Fuse Replacement

This section explains how to replace the fuse in the NI 4072.

Caution

| DMM | Fuse Rating | Fuse Type | Manufacturer |
| --- | --- | --- | --- |
| NI 4072 | F 1.25 A 250 V | Fast-Acting | Littelfuse |

To replace the fuse, complete the following steps.

1. Remove all front panel connections from the device.
2. Power off the chassis, and remove the device.
3. Locate the fuse hold shown in the figure below. [IMAGE alt='image' src='GUID-7AE2373D-0BB5-42A8-A2AB-4FCF0E4DB05D-a5.svg'] 

 1. Screwdriver
 2. Fuse Hole
4. Insert a screwdriver into the fuse hole. Caution Do not cover the fuse slot on the opposite side of the device with your hand, as doing so may cause injury.
5. Gently press the fuse with the screwdriver until one of the fuse clamps releases.
6. Locate the fuse slot shown in the figure below. [IMAGE alt='image' src='GUID-871F2DF6-3494-459D-92C1-7977367D1092-a5.svg'] 

 1. Fuse
 2. Fuse Slot
7. Pry the fuse loose from the fuse slot.
8. Verify that the fuse is blown by measuring discontinuity across the fuse using another meter.
9. Insert a new fuse into the fuse slot as shown in the figure below. [IMAGE alt='image' src='GUID-6BEE79F1-63DC-4EEC-A27C-DCA32EE89E87-a5.svg'] 

 1. Fuse
 2. Fuse Slot
10. Gently press the fuse with the screwdriver until both fuse clamps snap the fuse into place.

Parent topic:

NI 4072

<!--NI_TOPIC bundle=ni-dmm path=4072-impedance.html language=enus -->
## TOPIC 00039: Impedance

- bundle_id: `ni-dmm`
- source_path: `4072-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-impedance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Capacitive and inductive loads oppose the flow of alternating currents. This opposition is expressed as impedance at a given frequency. The effect of a real-world impedance load is observed as an attenuation of the signal and a phase shift. Because of the nature of the impedance, it is denoted as a

### Impedance

Capacitive and inductive loads oppose the flow of alternating currents. This opposition is expressed as impedance at a given frequency. The effect of a real-world impedance load is observed as an attenuation of the signal and a phase shift. Because of the nature of the impedance, it is denoted as a vector whose angle is the same as the phase angle between voltage and current, and the magnitude of the impedance is the same as the quotient between the voltage and current magnitudes, as follows:

Note

Z = V/I

Numerically, the impedance vector is represented as a complex number either in polar form (magnitude and phase) or rectangular form (real and imaginary). The following equation expresses impedance in rectangular form:

Z = R + jX

where R and X are resistance and reactance, respectively. When X = 0, the load is purely resistive; when R = 0, the load is purely reactive. For capacitors, the reactance can be expressed as follows:

X<sub>c</sub> = –1/(2[IMAGE alt='image' src='GUID-CC0315BF-B093-4875-ADCB-08A9AD050B4C-a5.gif']fC<sub>s</sub>)

For inductors, the reactance can be expressed as follows:

X<sub>L</sub> = 2[IMAGE alt='image' src='GUID-CC0315BF-B093-4875-ADCB-08A9AD050B4C-a5.gif'] fL<sub>s</sub>

Parent topic:

Theoretical Background

<!--NI_TOPIC bundle=ni-dmm path=4072-inductors.html language=enus -->
## TOPIC 00040: Inductors

- bundle_id: `ni-dmm`
- source_path: `4072-inductors.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-inductors.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: An inductor is an electronic component that is capable of storing energy as current. Each inductor consists of a conductive coil that can be wrapped without a core or around a magnetic material. The permeability of the core material is a measure of the intensity of the magnetic field that can be ind

### Inductors

An inductor is an electronic component that is capable of storing energy as current. Each inductor consists of a conductive coil that can be wrapped without a core or around a magnetic material. The permeability of the core material is a measure of the intensity of the magnetic field that can be induced in it.

The electrical properties of the cores show variability with factors such as temperature, frequency, current, and so on. This variability and the mechanical construction of the inductor create a less than ideal device.

A better representation of real-world inductors is shown in the equivalent model below, which aids in understanding the different parasitic elements that are present in a real-world component. These parasitic elements impact the inductor impedance at different test frequencies.

[IMAGE alt='image' src='GUID-AB7FDAB3-EC89-4717-AAF8-69F185D09C27-a5.svg']

The series resistance, Rs, represents the resistive losses in the conductor. The parallel capacitance, Cp, is the equivalent capacitive effect between the turns of the coil, and the parallel resistance, Rp, is the sum of all losses attributable to the core material.

Air cores require many more turns in the coil to achieve high-inductance values. Thus, air cores are often impractical for applications, due to their large size and weight. Also, air cores usually have a large winding capacitance and a series resistance with a high-inductance value.

Not all parasitics affect the value of the inductor, but some parasitics are more prominent than others, depending upon the construction of the coil, the geometry of the inductor, the gauge of the wire, and the characteristics of the core. The value of the inductor and the magnitude of each type of parasitic in relation to the other types of parasitics determine the frequency response.

The geometry of some components can increase the sensitivity of the components to external factors, and this increased sensitivity can also affect the value of the inductor. Open flux inductors are more sensitive to metallic materials that are in close proximity, because such materials modify the magnetic field. Toroidal inductors keep the flux inside the core and are less sensitive to external conductors in close proximity. Refer to the following figure to view the flux associated with these types of inductors:

[IMAGE alt='image' src='GUID-EBB6108C-EBBA-4A64-9230-ACB7EFA13550-a5.svg']

In the following graph, a 5 mH air-core inductor is measured over different frequencies. The error is referenced to the measurement with a test signal of 1 V<sub>rms</sub> at 1 kHz. This type of inductor has a high degree of winding capacitance due to the size and number of turns required for its construction. Therefore, this type of inductor measures as if there were a strong variation of inductance with frequency.

[IMAGE alt='image' src='GUID-B94BF1F0-55E2-4B53-902B-B0978F42741D-a5.gif']

Some ferrite cores are expected to vary greatly with the test signal level. In the following graph, a 100 µH ferrite-core inductor is tested at different test signal levels. The error is referenced to the measurement with a test signal of 1 mA<sub>rms</sub> at 1 kHz.

[IMAGE alt='image' src='GUID-80719574-0AB4-4F99-A7DA-4079636C491B-a5.gif']

All of these factors can combine and cause inductors to have different values under varying conditions of temperature, frequency, and signal level.

Parent topic:

Theoretical Background

<!--NI_TOPIC bundle=ni-dmm path=4072-measurement-considerations.html language=enus -->
## TOPIC 00041: Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `4072-measurement-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-measurement-considerations.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When taking capacitance and inductance measurements with the NI 4072, consider the following:

### Measurement Considerations

When taking capacitance and inductance measurements with the NI 4072, consider the following:

- [Frequency Effects of Real-World Components](4072-frequency-effects-of-real-world-components.html)
- [Temperature Effects](temperature-effects.html)
- [Cabling](4072-cabling.html)
- [Noise Pickup](4072-noise-pickup.html)

Parent topic:

Capacitance/Inductance

<!--NI_TOPIC bundle=ni-dmm path=4072-model.html language=enus -->
## TOPIC 00042: Model

- bundle_id: `ni-dmm`
- source_path: `4072-model.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-model.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: In real-world applications, devices are neither purely reactive nor purely resistive. However, they can be easily modeled either as a series or parallel combination of a resistive and a reactive load using the formulas above. In general, it is mathematically easier to manipulate parallel loads as ad

### Model

In real-world applications, devices are neither purely reactive nor purely resistive. However, they can be easily modeled either as a series or parallel combination of a resistive and a reactive load using the formulas above.

|  |  |
| --- | --- |

In general, it is mathematically easier to manipulate parallel loads as admittances and series loads as impedances.

|  |  |
| --- | --- |

You model the result as a series or parallel model based upon which resistance, R<sub>S</sub> or R<sub>P</sub>, is more significant. The parallel resistance (R<sub>P</sub>) is typically larger than the series resistance (R<sub>S</sub>). To measure small reactive values, such as high-valued capacitors and low-valued inductors, it is preferable to use the series model, because the series resistance is more significant than the parallel resistance. When measuring large reactive values, such as high-valued inductors or low-valued capacitors, it is preferable to use the parallel model.

| Type of Measurement | Range | Impedance | Model |
| --- | --- | --- | --- |
| C | >100 µF | <10 Ω | Series |
| C | 10 nF to 100 µF | 10 Ω to 10 kΩ | Series or parallel |
| C | <10 nF | >10 kΩ | Parallel |
| L | <1 mH | <10 Ω | Series |
| L | 1 mH to 1 H | 10 Ω to 1 kΩ | Series or parallel |
| L | >1 H | ≥1 kΩ | Parallel |
| Note Impedance values are calculated at the test frequency used on the NI 4072 at each specified range. |  |  |  |

Parent topic:

Capacitance/Inductance

<!--NI_TOPIC bundle=ni-dmm path=4072-noise-pickup.html language=enus -->
## TOPIC 00043: Noise Pickup

- bundle_id: `ni-dmm`
- source_path: `4072-noise-pickup.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-noise-pickup.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To minimize noise pickup, keep cables, the setup, and the DUT away from any electromagnetic noise sources such as motors, transformers, and cathode ray tubes (CRTs). Avoid frequency sources around 91 Hz, 1 kHz, 10 kHz, and the respective harmonics, because these frequencies are the frequencies of th

### Noise Pickup

To minimize noise pickup, keep cables, the setup, and the DUT away from any electromagnetic noise sources such as motors, transformers, and cathode ray tubes (CRTs). Avoid frequency sources around 91 Hz, 1 kHz, 10 kHz, and the respective harmonics, because these frequencies are the frequencies of the excitation currents used by the NI 4072. Use shielded cable (BNC connectors and coaxial cable are recommended) for cabling and for connecting the external conductor to the LO input of the DMM.

Note

Parent topic:

Measurement Considerations

Related concepts:

- Switching Capacitance and Inductance

<!--NI_TOPIC bundle=ni-dmm path=4072-openshort-compensation.html language=enus -->
## TOPIC 00044: OPEN/SHORT Compensation

- bundle_id: `ni-dmm`
- source_path: `4072-openshort-compensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-openshort-compensation.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: In most practical applications, the DMM is connected to the DUT with switches and/or fixtures. These switches and fixtures can introduce undesired errors into the measurement. Compensation minimizes the errors between the NI 4072 and the DUT.Offset CompensationCompensation consists of measuring the

### OPEN/SHORT Compensation

In most practical applications, the DMM is connected to the DUT with switches and/or fixtures. These switches and fixtures can introduce undesired errors into the measurement. Compensation minimizes the errors between the NI 4072 and the DUT.

#### Offset Compensation

Compensation consists of measuring the error and applying the measured error to the actual measurement to correct and minimize the errors introduced by the test system. The compensation functions must be set before taking any measurement at a specified function and range.

Any change in range or function defaults the compensation type to none. Therefore, you must calculate these values again. To provide maximum flexibility in the test system, the compensation values are returned by the API. You can manipulate, store, and load these values for high channel-count systems.

To perform OPEN compensation for capacitance and inductance measurements, complete the following steps:

1. Disconnect the DUT from the DMM at the DUT.
2. Configure the DMM for capacitance or inductance at the desired range.
3. Call niDMM Configure Cable Comp Type or niDMM_ConfigureCableCompType , and set the Cable Comp Type to CABLE COMP OPEN.
4. Set up an open condition, where nothing is connected to the test fixture. If the switching system in use has similar capacitance on different channels, you can dedicate one channel for open measurements. Cables and switches with low capacitance and low-path resistance are recommended.
5. In LabVIEW, call niDMM Perform Open Cable Comp or niDMM_PerformOpenCableComp while the input to the DMM is open. This VI or function returns two values: conductance and susceptance.
6. Pass the two values from the previous step into niDMM Configure Open Cable Comp Values or niDMM_ConfigureOpenCableCompValues . Passing these values subtracts the open measurement from all subsequent measurements.
7. Perform the desired measurement.

To perform SHORT compensation for capacitance and inductance measurements, complete the following steps:

1. Disconnect the DUT from the DMM at the DUT.
2. Configure the DMM for capacitance or inductance at the desired range.
3. Call niDMM Configure Cable Comp Type or niDMM_ConfigureCableCompType , and set the Cable Comp Type to CABLE COMP SHORT.
4. Set up a short condition at the end of the test fixture, using a low-impedance connection between the HI and LO terminals. If the switching system in use has similar inductance on different channels, you can dedicate one channel for short measurements. Cables and switches with low capacitance and low path resistance are recommended.
5. In LabVIEW, call niDMM Perform Short Cable Comp or niDMM_PerformShortCableComp while the input to the DMM is shorted. This VI or function returns two values: resistance and reactance.
6. Pass the two values from the previous step into niDMM Configure Short Cable Comp Values or niDMM_ConfigureShortCableCompValues . Passing these values subtracts the short measurement from all subsequent measurements.
7. Perform the desired measurement.

#### OPEN/SHORT Compensation

To perform OPEN and SHORT compensation for capacitance and inductance measurements, complete the following steps:

1. Disconnect the DUT from the DMM at the DUT.
2. Configure the DMM for capacitance or inductance at the desired range.
3. Call niDMM Configure Cable Comp Type or niDMM_ConfigureCableCompType , and set the Cable Comp Type to CABLE COMP OPEN AND SHORT.
4. Set up an open condition, where nothing is connected to the test fixture. If the switching system in use has similar inductance on different channels, you can dedicate one channel for open measurements. Cables and switches with low capacitance and low path resistance are recommended.
5. Call niDMM Perform Open Cable Comp or niDMM_PerformOpenCableComp while the input to the DMM is shorted. This VI or function returns two values: conductance and susceptance.
6. Pass the two values from the previous step into niDMM Configure Open Cable Comp Values or niDMM_ConfigureOpenCableCompValues .
7. Set up a short condition at the end of the test fixture, using a low-impedance connection between the HI and LO terminals. If the switching system in use has similar inductance on different channels, you can dedicate one channel for short measurements. Cables and switches with low capacitance and low path resistance are recommended.
8. Call niDMM Perform Short Cable Comp or niDMM_PerformShortCableComp while the input to the DMM is shorted. This VI or function returns two values: resistance and reactance.
9. Pass the two values from the previous step into niDMM Configure Short Cable Comp Values or niDMM_ConfigureShortCableCompValues .
10. NI-DMM takes the four values measured on open and short conditions to compensate all subsequent measurements.
11. Perform the desired measurement.

Note

Parent topic:

Capacitance/Inductance

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=4072-test-signal.html language=enus -->
## TOPIC 00045: Test Signal

- bundle_id: `ni-dmm`
- source_path: `4072-test-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-test-signal.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4072 uses an AC current source as excitation for capacitance and inductance measurements. The current waveform is a very stable, harmonically limited square wave. The measurement method extracts multiple-tone information contained in the test signal to find the capacitance or inductance of th

### Test Signal

The NI 4072 uses an AC current source as excitation for capacitance and inductance measurements. The current waveform is a very stable, harmonically limited square wave. The measurement method extracts multiple-tone information contained in the test signal to find the capacitance or inductance of the device under test. The frequency and level of the test signal and the tones extracted from it are shown in the following tables:

| Capacitance |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Range | Fundamental | Third Harmonic | Effective Test Signal |  |  |  |
| Frequency | Current | Frequency | Current | Frequency | Current |  |
| 300 pF | 1 kHz | 0.5 µA | 3 kHz | 0.16 µA | 3 kHz | 0.16 µA |
| 1 nF | 1 kHz | 1 µA | 3 kHz | 0.33 µA | 3 kHz | 0.33 µA |
| 10 nF |  |  |  |  |  |  |
| 100 nF | 1 kHz | 10 µA | 3 kHz | 3.3 µA | 3 kHz | 3.3 µA |
| 1 µF | 1 kHz | 100 µA | 3 kHz | 33 µA | 1 kHz | 100 µA |
| 10 µF | 1 kHz | 1 mA | 3 kHz | 330 µA | 1 kHz | 1 mA |
| 100 µF | 91 Hz | 1 mA | 273 Hz | 330 µA | 91 Hz | 1 mA |
| 1,000 µF |  |  |  |  |  |  |
| 10,000 µF |  |  |  |  |  |  |
| Inductance |  |  |  |  |  |  |
| Range | Fundamental | Third Harmonic | Effective Test Signal |  |  |  |
| Frequency | Current | Frequency | Current | Frequency | Current |  |
| 10 µH | 10 kHz | 1 mA | 30 kHz | 330 µA | 30 kHz | 330 µA |
| 100 µH |  |  |  |  |  |  |
| 1 mH | 1 kHz | 1 mA | 3 kHz | 330 µA | 3 kHz | 330 µA |
| 10 mH | 1 kHz | 10 µA | 3 kHz | 3.3 µA | 3 kHz | 3.3 µA |
| 100 mH | 91 Hz | 100 µA | 273 Hz | 33 µA | 273 Hz | 33 µA |
| 1 H | 91 Hz | 10 µA | 273 Hz | 3.3 µA | 273 Hz | 3.3 µA |
| 5 H | 91 Hz | 1 µA | 273 Hz | 0.33 µA | 273 Hz | 0.33 µA |

The digitizer measures the DUT impedance at two frequencies (tones). From these two measurements, the losses are calculated (front-end, cabling, and DUT). Using the calculated losses, the software computes the capacitance or inductance at one of the two frequencies (effective frequency).

The effective test signal is included as a reference. It is the signal that would yield a comparable capacitance or inductance value if measured with the single tone measurement technique.

Parent topic:

Capacitance/Inductance

<!--NI_TOPIC bundle=ni-dmm path=4072-theoretical-background.html language=enus -->
## TOPIC 00046: Theoretical Background

- bundle_id: `ni-dmm`
- source_path: `4072-theoretical-background.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4072-theoretical-background.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following topics include background information about capacitance and inductance measurements:

### Theoretical Background

The following topics include background information about capacitance and inductance measurements:

Parent topic:

Capacitance/Inductance

<!--NI_TOPIC bundle=ni-dmm path=407x-dmm-measurement-cycle.html language=enus -->
## TOPIC 00047: DMM Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `407x-dmm-measurement-cycle.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-dmm-measurement-cycle.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture time. Generally t

### DMM Measurement Cycle

The DMM measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture time. Generally the settle and aperture times are selected by the device driver based on the specified resolution. Settling time and aperture can be set using the niDMM Property Node. Refer to Configuring Measurement Timing for more information.

[IMAGE alt='image' src='GUID-C081233B-F9E9-459F-B325-4DC1E226E115-a5.svg']

The internal switch time is required to configure the analog circuitry of the device for the next measurement, and default settling times precede both ADC calibration and Auto Zero. All of these times are not user programmable.

During resistance measurements, the signal is measured with an applied current source. When Offset Compensated Ohms is enabled, a settle phase and current source OFF measurement phase occurs in place of the Auto Zero phase depicted above.

The AC measurement cycle contains the same phases, but the minimum signal measurement time is based on the minimum frequency required of the measurement. For example, for a minimum frequency of 50 Hz, an aperture of 4x the period of the 50 Hz signal is required, or in this example, 80 ms.

For capacitance and inductance measurements, the measurement cycle consists of applying a current source and measuring the response of its harmonics. Because the harmonics are a set frequency, the aperture time is fixed. See DMM Measurement Defaults and Capacitance/Inductance for more information.

When Auto Range is selected, the Auto Range measurement phase occurs before the Auto Zero and signal measurement phases. After the correct range is identified, the Auto Zero and signal measurements use the selected range.

Note

Parent topic:

DMM Measurements

Related concepts:

- Configuring Measurement Timing
- DMM Measurement Defaults
- Capacitance/Inductance

Related information:

- niDMM Property Node

<!--NI_TOPIC bundle=ni-dmm path=407x-dmm-measurement-cycle_2.html language=enus -->
## TOPIC 00048: DMM Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `407x-dmm-measurement-cycle_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-dmm-measurement-cycle_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture time. Generally t

### DMM Measurement Cycle

The DMM measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture time. Generally the settle and aperture times are selected by the device driver based on the specified resolution. Settling time and aperture can be set using the niDMM Property Node. Refer to Configuring Measurement Timing for more information.

[IMAGE alt='image' src='GUID-C081233B-F9E9-459F-B325-4DC1E226E115-a5.svg']

The internal switch time is required to configure the analog circuitry of the device for the next measurement, and default settling times precede both ADC calibration and Auto Zero. All of these times are not user programmable.

During resistance measurements, the signal is measured with an applied current source. When Offset Compensated Ohms is enabled, a settle phase and current source OFF measurement phase occurs in place of the Auto Zero phase depicted above.

The AC measurement cycle contains the same phases, but the minimum signal measurement time is based on the minimum frequency required of the measurement. For example, for a minimum frequency of 50 Hz, an aperture of 4x the period of the 50 Hz signal is required, or in this example, 80 ms.

For capacitance and inductance measurements, the measurement cycle consists of applying a current source and measuring the response of its harmonics. Because the harmonics are a set frequency, the aperture time is fixed. See DMM Measurement Defaults and Capacitance/Inductance for more information.

When Auto Range is selected, the Auto Range measurement phase occurs before the Auto Zero and signal measurement phases. After the correct range is identified, the Auto Zero and signal measurements use the selected range.

Note

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=407x-dmm-measurement-cycle_3.html language=enus -->
## TOPIC 00049: DMM Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `407x-dmm-measurement-cycle_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-dmm-measurement-cycle_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture time. Generally t

### DMM Measurement Cycle

The DMM measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture time. Generally the settle and aperture times are selected by the device driver based on the specified resolution. Settling time and aperture can be set using the niDMM Property Node. Refer to Configuring Measurement Timing for more information.

[IMAGE alt='image' src='GUID-C081233B-F9E9-459F-B325-4DC1E226E115-a5.svg']

The internal switch time is required to configure the analog circuitry of the device for the next measurement, and default settling times precede both ADC calibration and Auto Zero. All of these times are not user programmable.

During resistance measurements, the signal is measured with an applied current source. When Offset Compensated Ohms is enabled, a settle phase and current source OFF measurement phase occurs in place of the Auto Zero phase depicted above.

The AC measurement cycle contains the same phases, but the minimum signal measurement time is based on the minimum frequency required of the measurement. For example, for a minimum frequency of 50 Hz, an aperture of 4x the period of the 50 Hz signal is required, or in this example, 80 ms.

For capacitance and inductance measurements, the measurement cycle consists of applying a current source and measuring the response of its harmonics. Because the harmonics are a set frequency, the aperture time is fixed. See DMM Measurement Defaults and Capacitance/Inductance for more information.

When Auto Range is selected, the Auto Range measurement phase occurs before the Auto Zero and signal measurement phases. After the correct range is identified, the Auto Zero and signal measurements use the selected range.

Note

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=407x-dmm-measurement-defaults.html language=enus -->
## TOPIC 00050: DMM Measurement Defaults

- bundle_id: `ni-dmm`
- source_path: `407x-dmm-measurement-defaults.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-dmm-measurement-defaults.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default measurement settings for the NI 4070/4071/4072. Function Aperture Auto Zero ADC Calibration DC Noise Rejection DC 7½ digits^1 100 ms ON ON High-Order DC 6½ digits 100 ms ON ON High-Order DC 5½ digits 500 µs (NI 4070/4072) 500 µs^2 (NI 4071) ONCE OFF Second-Order

### DMM Measurement Defaults

The following table lists the default measurement settings for the NI 4070/4071/4072.

| Function | Aperture | Auto Zero | ADC Calibration | DC Noise Rejection |
| --- | --- | --- | --- | --- |
| DC 7½ digits1 | 100 ms | ON | ON | High-Order |
| DC 6½ digits | 100 ms | ON | ON | High-Order |
| DC 5½ digits | 500 µs (NI 4070/4072) 500 µs2 (NI 4071) | ONCE | OFF | Second-Order |
| DC 4½ digits3 | 20 µs (NI 4070/4072) 50 µs (NI 4071) | ONCE | OFF | Second-Order |
| DC Auto Range | 500 µs | ONCE | OFF | Second-Order |
| AC | Max (DC or 4/(minFreq)) | OFF | OFF | N/A |
| AC Auto Range | Max (500 µs or 4/(minFreq)) | OFF | OFF | N/A |
| Frequency | 2/(minFreq) | N/A | N/A | N/A |
| Period | 2 x (the maximum period) | N/A | N/A | N/A |
| Capacitance and Inductance | Inductance (only) at 10 kHz = 13.65 ms Inductance and capacitance at 1 kHz = 31.29 ms Inductance and capacitance at 91 Hz = 270.22 ms | N/A | N/A | N/A |
| 1The default Number of Averages for the NI 4071 is 4. 2For the NI 4071, on the 5.5 DCV 100V range, use 1.6 ms. 3Settings for 3½ digits are equivalent to 4½ digits. |  |  |  |  |

By default, the Aperture time, Auto Zero, ADC Calibration, DC Noise Rejection settings for a
 measurement are chosen by the driver based on the configured measurement and
 resolution. These values are chosen to ensure accuracy for 6½–digit or 7½–digit
 measurements while not sacrificing performance at lower resolutions. For more
 information on a particular attribute, including how to configure a non-default
 setting, refer to Features. For AC, excluding Auto Range, the aperture is expressed
 as Max (DC or 4/minFreq). minFreq, or minimum frequency, is a user–programmable
 parameter with a default value of 20 Hz. Therefore, the aperture default is
 200 ms.

The same applies for other user selectable values of minFreq. For example, on the NI 4070/4071/4072, if a minFreq of 1 kHz is selected then 4/minFreq = 4/1 kHz = 4 ms. In this case 4 ms would be used as the AC aperture for resolutions <6 digits. For resolutions >6 digits, 100 ms would be used.

To adjust the default aperture time, refer to Configuring Measurement Timing.

#### Default Settling Times

| Function | Settling Time |
| --- | --- |
| DC V (100 mV–10 V) | 1 ms |
| DC V (100 V, 300 V) (NI 4070/4072 only) | 2 ms |
| DC V (100 V, 1000 V) (NI 4071 only) | 5 ms |
| DCV Auto Range | 2 ms |
| Resistance ≤1 kΩ | 1 ms |
| Resistance 10 kΩ | 5 ms |
| Resistance 100 kΩ | 25 ms |
| Resistance 1 MΩ | 100 ms |
| Resistance ≥ 10 MΩ | 250 ms |
| Resistance Auto Range | 50 ms |
| AC V DC coupled | 3 µs |
| AC V AC coupled | 1 s |
| Frequency/Period | 500 ms |
| DC I | 100 µs |
| AC I | 3 µs |
| Diode | 10 ms |
| Inductance (NI 4072 only) | 3 µs |
| Capacitance (NI 4072 only) | 3 µs |

To adjust the default settling times, refer to Configuring Measurement
 Timing.

Parent topic:

DMM Measurements

Related concepts:

- Configuring Auto Zero
- Configuring ADC Calibration
- Configuring Measurement Timing
- Features
- Selecting DC Noise Rejection

<!--NI_TOPIC bundle=ni-dmm path=407x-dmm-measurement-defaults_2.html language=enus -->
## TOPIC 00051: DMM Measurement Defaults

- bundle_id: `ni-dmm`
- source_path: `407x-dmm-measurement-defaults_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-dmm-measurement-defaults_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default measurement settings for the NI 4070/4071/4072. Function Aperture Auto Zero ADC Calibration DC Noise Rejection DC 7½ digits^1 100 ms ON ON High-Order DC 6½ digits 100 ms ON ON High-Order DC 5½ digits 500 µs (NI 4070/4072) 500 µs^2 (NI 4071) ONCE OFF Second-Order

### DMM Measurement Defaults

The following table lists the default measurement settings for the NI 4070/4071/4072.

| Function | Aperture | Auto Zero | ADC Calibration | DC Noise Rejection |
| --- | --- | --- | --- | --- |
| DC 7½ digits1 | 100 ms | ON | ON | High-Order |
| DC 6½ digits | 100 ms | ON | ON | High-Order |
| DC 5½ digits | 500 µs (NI 4070/4072) 500 µs2 (NI 4071) | ONCE | OFF | Second-Order |
| DC 4½ digits3 | 20 µs (NI 4070/4072) 50 µs (NI 4071) | ONCE | OFF | Second-Order |
| DC Auto Range | 500 µs | ONCE | OFF | Second-Order |
| AC | Max (DC or 4/(minFreq)) | OFF | OFF | N/A |
| AC Auto Range | Max (500 µs or 4/(minFreq)) | OFF | OFF | N/A |
| Frequency | 2/(minFreq) | N/A | N/A | N/A |
| Period | 2 x (the maximum period) | N/A | N/A | N/A |
| Capacitance and Inductance | Inductance (only) at 10 kHz = 13.65 ms Inductance and capacitance at 1 kHz = 31.29 ms Inductance and capacitance at 91 Hz = 270.22 ms | N/A | N/A | N/A |
| 1The default Number of Averages for the NI 4071 is 4. 2For the NI 4071, on the 5.5 DCV 100V range, use 1.6 ms. 3Settings for 3½ digits are equivalent to 4½ digits. |  |  |  |  |

By default, the Aperture time, Auto Zero, ADC Calibration, DC Noise Rejection settings for a
 measurement are chosen by the driver based on the configured measurement and
 resolution. These values are chosen to ensure accuracy for 6½–digit or 7½–digit
 measurements while not sacrificing performance at lower resolutions. For more
 information on a particular attribute, including how to configure a non-default
 setting, refer to Features. For AC, excluding Auto Range, the aperture is expressed
 as Max (DC or 4/minFreq). minFreq, or minimum frequency, is a user–programmable
 parameter with a default value of 20 Hz. Therefore, the aperture default is
 200 ms.

The same applies for other user selectable values of minFreq. For example, on the NI 4070/4071/4072, if a minFreq of 1 kHz is selected then 4/minFreq = 4/1 kHz = 4 ms. In this case 4 ms would be used as the AC aperture for resolutions <6 digits. For resolutions >6 digits, 100 ms would be used.

To adjust the default aperture time, refer to Configuring Measurement Timing.

#### Default Settling Times

| Function | Settling Time |
| --- | --- |
| DC V (100 mV–10 V) | 1 ms |
| DC V (100 V, 300 V) (NI 4070/4072 only) | 2 ms |
| DC V (100 V, 1000 V) (NI 4071 only) | 5 ms |
| DCV Auto Range | 2 ms |
| Resistance ≤1 kΩ | 1 ms |
| Resistance 10 kΩ | 5 ms |
| Resistance 100 kΩ | 25 ms |
| Resistance 1 MΩ | 100 ms |
| Resistance ≥ 10 MΩ | 250 ms |
| Resistance Auto Range | 50 ms |
| AC V DC coupled | 3 µs |
| AC V AC coupled | 1 s |
| Frequency/Period | 500 ms |
| DC I | 100 µs |
| AC I | 3 µs |
| Diode | 10 ms |
| Inductance (NI 4072 only) | 3 µs |
| Capacitance (NI 4072 only) | 3 µs |

To adjust the default settling times, refer to Configuring Measurement
 Timing.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=407x-dmm-measurement-defaults_3.html language=enus -->
## TOPIC 00052: DMM Measurement Defaults

- bundle_id: `ni-dmm`
- source_path: `407x-dmm-measurement-defaults_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-dmm-measurement-defaults_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default measurement settings for the NI 4070/4071/4072. Function Aperture Auto Zero ADC Calibration DC Noise Rejection DC 7½ digits^1 100 ms ON ON High-Order DC 6½ digits 100 ms ON ON High-Order DC 5½ digits 500 µs (NI 4070/4072) 500 µs^2 (NI 4071) ONCE OFF Second-Order

### DMM Measurement Defaults

The following table lists the default measurement settings for the NI 4070/4071/4072.

| Function | Aperture | Auto Zero | ADC Calibration | DC Noise Rejection |
| --- | --- | --- | --- | --- |
| DC 7½ digits1 | 100 ms | ON | ON | High-Order |
| DC 6½ digits | 100 ms | ON | ON | High-Order |
| DC 5½ digits | 500 µs (NI 4070/4072) 500 µs2 (NI 4071) | ONCE | OFF | Second-Order |
| DC 4½ digits3 | 20 µs (NI 4070/4072) 50 µs (NI 4071) | ONCE | OFF | Second-Order |
| DC Auto Range | 500 µs | ONCE | OFF | Second-Order |
| AC | Max (DC or 4/(minFreq)) | OFF | OFF | N/A |
| AC Auto Range | Max (500 µs or 4/(minFreq)) | OFF | OFF | N/A |
| Frequency | 2/(minFreq) | N/A | N/A | N/A |
| Period | 2 x (the maximum period) | N/A | N/A | N/A |
| Capacitance and Inductance | Inductance (only) at 10 kHz = 13.65 ms Inductance and capacitance at 1 kHz = 31.29 ms Inductance and capacitance at 91 Hz = 270.22 ms | N/A | N/A | N/A |
| 1The default Number of Averages for the NI 4071 is 4. 2For the NI 4071, on the 5.5 DCV 100V range, use 1.6 ms. 3Settings for 3½ digits are equivalent to 4½ digits. |  |  |  |  |

By default, the Aperture time, Auto Zero, ADC Calibration, DC Noise Rejection settings for a
 measurement are chosen by the driver based on the configured measurement and
 resolution. These values are chosen to ensure accuracy for 6½–digit or 7½–digit
 measurements while not sacrificing performance at lower resolutions. For more
 information on a particular attribute, including how to configure a non-default
 setting, refer to Features. For AC, excluding Auto Range, the aperture is expressed
 as Max (DC or 4/minFreq). minFreq, or minimum frequency, is a user–programmable
 parameter with a default value of 20 Hz. Therefore, the aperture default is
 200 ms.

The same applies for other user selectable values of minFreq. For example, on the NI 4070/4071/4072, if a minFreq of 1 kHz is selected then 4/minFreq = 4/1 kHz = 4 ms. In this case 4 ms would be used as the AC aperture for resolutions <6 digits. For resolutions >6 digits, 100 ms would be used.

To adjust the default aperture time, refer to Configuring Measurement Timing.

#### Default Settling Times

| Function | Settling Time |
| --- | --- |
| DC V (100 mV–10 V) | 1 ms |
| DC V (100 V, 300 V) (NI 4070/4072 only) | 2 ms |
| DC V (100 V, 1000 V) (NI 4071 only) | 5 ms |
| DCV Auto Range | 2 ms |
| Resistance ≤1 kΩ | 1 ms |
| Resistance 10 kΩ | 5 ms |
| Resistance 100 kΩ | 25 ms |
| Resistance 1 MΩ | 100 ms |
| Resistance ≥ 10 MΩ | 250 ms |
| Resistance Auto Range | 50 ms |
| AC V DC coupled | 3 µs |
| AC V AC coupled | 1 s |
| Frequency/Period | 500 ms |
| DC I | 100 µs |
| AC I | 3 µs |
| Diode | 10 ms |
| Inductance (NI 4072 only) | 3 µs |
| Capacitance (NI 4072 only) | 3 µs |

To adjust the default settling times, refer to Configuring Measurement
 Timing.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=407x-dmm-measurements.html language=enus -->
## TOPIC 00053: DMM Measurements

- bundle_id: `ni-dmm`
- source_path: `407x-dmm-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-dmm-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections cover optimizing your measurements on the NI 4070/4071/4072.

### DMM Measurements

The following sections cover optimizing your measurements on the NI 4070/4071/4072.

Parent topic:

NI 4072

<!--NI_TOPIC bundle=ni-dmm path=407x-dmm-measurements_2.html language=enus -->
## TOPIC 00054: DMM Measurements

- bundle_id: `ni-dmm`
- source_path: `407x-dmm-measurements_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-dmm-measurements_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections cover optimizing your measurements on the NI 4070/4071/4072.

### DMM Measurements

The following sections cover optimizing your measurements on the NI 4070/4071/4072.

Parent topic:

NI 4071

<!--NI_TOPIC bundle=ni-dmm path=407x-dmm-measurements_3.html language=enus -->
## TOPIC 00055: DMM Measurements

- bundle_id: `ni-dmm`
- source_path: `407x-dmm-measurements_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-dmm-measurements_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections cover optimizing your measurements on the NI 4070/4071/4072.

### DMM Measurements

The following sections cover optimizing your measurements on the NI 4070/4071/4072.

Parent topic:

NI 4070

<!--NI_TOPIC bundle=ni-dmm path=407x-frequencyperiod.html language=enus -->
## TOPIC 00056: Frequency/Period

- bundle_id: `ni-dmm`
- source_path: `407x-frequencyperiod.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-frequencyperiod.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to 300 V[rms] (6½ digit) or 700 V[rms] (7½ digit).The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 28.8 MHz t

### Frequency/Period

The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to 300 V<sub>rms</sub> (6½ digit) or 700 V<sub>rms</sub> (7½ digit).

The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 28.8 MHz timebase.

Frequency (Hz) = timebase (Hz) x Ns / Nt

Period = 1 /Frequency (Hz)

where

timebase = 28.8 x 10<sup>6</sup> Hz

Ns = number of rising edges detected in the measurement window

Nt = number of timebase clock periods between the first and the last rising edge

To measure a signal of frequency f in Hz, the DMM needs a minimum aperture of
 (2/f) s. The resolution of the frequency measurement is
 independent of the input signal frequency and depends only on how long the DMM is
 able to look at the signal. A longer aperture enables a finer frequency
 resolution.

Frequency Resolution (ppm) = 10<sup>6</sup> (ppm) x 4 / [timebase (Hz) x aperture (s)]

where timebase = 28.8 x 10<sup>6</sup> Hz.

For example, the aperture setting of 100 ms allows you to measure a signal of a minimum frequency of 20 Hz with a resolution of 1.4 ppm.

The accuracy of the frequency measurement is directly related to the absolute accuracy of the 28.8 MHz oscillator used on the DMM. The accuracy of frequency measurement is 25 ppm including temperature and time drift. In addition, the amount of noise that couples with the signal can affect the accuracy. The DMM frequency measurement circuit has a hysteresis circuit that rejects noise up to 5% of the AC V range being used.

For example, if you are measuring TTL level signals, use the 5 V AC range (10 V<sub>pk</sub>). The frequency measurement circuit offers hysteresis of 250 mV in this case, which means you can have up to ±125 mV noise glitches superimposed on top of the signal and still be able to measure frequency accurately before it reaches the frequency measurement comparator circuit.

The minimum peak-to-peak signal amplitude required to measure frequency is 10% of the AC V range being used. In the previous example, a minimum of 500 mV (peak-to-peak) is required by the frequency measurement circuit to work correctly. Notice that for the 300 V AC range, the hysteresis is 8% of range (25 V), while the minimum peak-to-peak signal amplitude required is 17% of range (50 V).

As signals approach the 500 kHz bandwidth of the AC V path, the minimum peak-to-peak signal amplitude requirement increases by approximately a factor of three.

| AC V Range | Maximum Peak-to-PeakSignal Voltage Allowed | Minimum Peak-to-PeakSignal Amplitude Required | Hysteresis |
| --- | --- | --- | --- |
| 50 mV | 200 mV | 5 mV | 2.5 mV |
| 500 mV | 2 V | 50 mV | 25 mV |
| 5 V | 20 V | 500 mV | 250 mV |
| 50 V | 200 V | 5 V | 2.5 V |
| 300 V (6½ digit) | 450 V peak and <300 Vrms | 50 V | 25 V |
| 700 V (7½ digit) | 1000 V peak and <700 Vrms | 50 V | 25 V |

Another way to measure frequency is to perform waveform acquisitions and then to use the signal
 processing functions in the ADE to extract the frequency. This method of measuring
 frequency also allows you to extract frequency information based on amplitude and
 hysteresis.

Parent topic:

DMM Measurements

Related concepts:

- Configuring Frequency Measurements
- Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=407x-frequencyperiod_2.html language=enus -->
## TOPIC 00057: Frequency/Period

- bundle_id: `ni-dmm`
- source_path: `407x-frequencyperiod_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-frequencyperiod_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to 300 V[rms] (6½ digit) or 700 V[rms] (7½ digit).The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 28.8 MHz t

### Frequency/Period

The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to 300 V<sub>rms</sub> (6½ digit) or 700 V<sub>rms</sub> (7½ digit).

The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 28.8 MHz timebase.

Frequency (Hz) = timebase (Hz) x Ns / Nt

Period = 1 /Frequency (Hz)

where

timebase = 28.8 x 10<sup>6</sup> Hz

Ns = number of rising edges detected in the measurement window

Nt = number of timebase clock periods between the first and the last rising edge

To measure a signal of frequency f in Hz, the DMM needs a minimum aperture of
 (2/f) s. The resolution of the frequency measurement is
 independent of the input signal frequency and depends only on how long the DMM is
 able to look at the signal. A longer aperture enables a finer frequency
 resolution.

Frequency Resolution (ppm) = 10<sup>6</sup> (ppm) x 4 / [timebase (Hz) x aperture (s)]

where timebase = 28.8 x 10<sup>6</sup> Hz.

For example, the aperture setting of 100 ms allows you to measure a signal of a minimum frequency of 20 Hz with a resolution of 1.4 ppm.

The accuracy of the frequency measurement is directly related to the absolute accuracy of the 28.8 MHz oscillator used on the DMM. The accuracy of frequency measurement is 25 ppm including temperature and time drift. In addition, the amount of noise that couples with the signal can affect the accuracy. The DMM frequency measurement circuit has a hysteresis circuit that rejects noise up to 5% of the AC V range being used.

For example, if you are measuring TTL level signals, use the 5 V AC range (10 V<sub>pk</sub>). The frequency measurement circuit offers hysteresis of 250 mV in this case, which means you can have up to ±125 mV noise glitches superimposed on top of the signal and still be able to measure frequency accurately before it reaches the frequency measurement comparator circuit.

The minimum peak-to-peak signal amplitude required to measure frequency is 10% of the AC V range being used. In the previous example, a minimum of 500 mV (peak-to-peak) is required by the frequency measurement circuit to work correctly. Notice that for the 300 V AC range, the hysteresis is 8% of range (25 V), while the minimum peak-to-peak signal amplitude required is 17% of range (50 V).

As signals approach the 500 kHz bandwidth of the AC V path, the minimum peak-to-peak signal amplitude requirement increases by approximately a factor of three.

| AC V Range | Maximum Peak-to-PeakSignal Voltage Allowed | Minimum Peak-to-PeakSignal Amplitude Required | Hysteresis |
| --- | --- | --- | --- |
| 50 mV | 200 mV | 5 mV | 2.5 mV |
| 500 mV | 2 V | 50 mV | 25 mV |
| 5 V | 20 V | 500 mV | 250 mV |
| 50 V | 200 V | 5 V | 2.5 V |
| 300 V (6½ digit) | 450 V peak and <300 Vrms | 50 V | 25 V |
| 700 V (7½ digit) | 1000 V peak and <700 Vrms | 50 V | 25 V |

Another way to measure frequency is to perform waveform acquisitions and then to use the signal
 processing functions in the ADE to extract the frequency. This method of measuring
 frequency also allows you to extract frequency information based on amplitude and
 hysteresis.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=407x-frequencyperiod_3.html language=enus -->
## TOPIC 00058: Frequency/Period

- bundle_id: `ni-dmm`
- source_path: `407x-frequencyperiod_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-frequencyperiod_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to 300 V[rms] (6½ digit) or 700 V[rms] (7½ digit).The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 28.8 MHz t

### Frequency/Period

The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to 300 V<sub>rms</sub> (6½ digit) or 700 V<sub>rms</sub> (7½ digit).

The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 28.8 MHz timebase.

Frequency (Hz) = timebase (Hz) x Ns / Nt

Period = 1 /Frequency (Hz)

where

timebase = 28.8 x 10<sup>6</sup> Hz

Ns = number of rising edges detected in the measurement window

Nt = number of timebase clock periods between the first and the last rising edge

To measure a signal of frequency f in Hz, the DMM needs a minimum aperture of
 (2/f) s. The resolution of the frequency measurement is
 independent of the input signal frequency and depends only on how long the DMM is
 able to look at the signal. A longer aperture enables a finer frequency
 resolution.

Frequency Resolution (ppm) = 10<sup>6</sup> (ppm) x 4 / [timebase (Hz) x aperture (s)]

where timebase = 28.8 x 10<sup>6</sup> Hz.

For example, the aperture setting of 100 ms allows you to measure a signal of a minimum frequency of 20 Hz with a resolution of 1.4 ppm.

The accuracy of the frequency measurement is directly related to the absolute accuracy of the 28.8 MHz oscillator used on the DMM. The accuracy of frequency measurement is 25 ppm including temperature and time drift. In addition, the amount of noise that couples with the signal can affect the accuracy. The DMM frequency measurement circuit has a hysteresis circuit that rejects noise up to 5% of the AC V range being used.

For example, if you are measuring TTL level signals, use the 5 V AC range (10 V<sub>pk</sub>). The frequency measurement circuit offers hysteresis of 250 mV in this case, which means you can have up to ±125 mV noise glitches superimposed on top of the signal and still be able to measure frequency accurately before it reaches the frequency measurement comparator circuit.

The minimum peak-to-peak signal amplitude required to measure frequency is 10% of the AC V range being used. In the previous example, a minimum of 500 mV (peak-to-peak) is required by the frequency measurement circuit to work correctly. Notice that for the 300 V AC range, the hysteresis is 8% of range (25 V), while the minimum peak-to-peak signal amplitude required is 17% of range (50 V).

As signals approach the 500 kHz bandwidth of the AC V path, the minimum peak-to-peak signal amplitude requirement increases by approximately a factor of three.

| AC V Range | Maximum Peak-to-PeakSignal Voltage Allowed | Minimum Peak-to-PeakSignal Amplitude Required | Hysteresis |
| --- | --- | --- | --- |
| 50 mV | 200 mV | 5 mV | 2.5 mV |
| 500 mV | 2 V | 50 mV | 25 mV |
| 5 V | 20 V | 500 mV | 250 mV |
| 50 V | 200 V | 5 V | 2.5 V |
| 300 V (6½ digit) | 450 V peak and <300 Vrms | 50 V | 25 V |
| 700 V (7½ digit) | 1000 V peak and <700 Vrms | 50 V | 25 V |

Another way to measure frequency is to perform waveform acquisitions and then to use the signal
 processing functions in the ADE to extract the frequency. This method of measuring
 frequency also allows you to extract frequency information based on amplitude and
 hysteresis.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=407x-overrangeunderrange.html language=enus -->
## TOPIC 00059: Overrange/Underrange

- bundle_id: `ni-dmm`
- source_path: `407x-overrangeunderrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-overrangeunderrange.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the overrange and/or underrange conditions, as applicable, for the PXI/PCI‑4070, PXI‑4071, and PXI‑4072. Function Overrange1 Underrange Function Overrange^1 Underrange DC Functions:Voltage, Current, Resistance, and Diode All ranges, except 300 V and 1 A (NI 4070/4072) or 1000

### Overrange/Underrange

This section describes the overrange and/or underrange conditions, as applicable, for the PXI/PCI‑4070, PXI‑4071, and PXI‑4072.

| Function | Overrange1 | Underrange |
| --- | --- | --- |
| Function | Overrange1 | Underrange |
| DC Functions:Voltage, Current, Resistance, and Diode | All ranges, except 300 V and 1 A (NI 4070/4072) or 1000 V and 3 A (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns NaN2 (except for the 100 MΩ range on the NI 4070/4072) and the IVI overrange warning. For the 100 MΩ range on the NI 4070/4072, measurements between the 105 MΩ and 1.05 GΩ ranges have a typical accuracy of 5%, although NI-DMM returns the IVI overrange warning. For measurements above 1.05 GΩ, NI-DMM returns NaN2 and the IVI overrange warning instead of the reading. 300 V and 1 A ranges (NI 4070/4072) or 1000 V and 3 A ranges (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Not applicable |
| AC Functions:Voltage and Current | All ranges, except 300 V and 1 A (NI 4070/4072) or 700 V and 3 A (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. At significantly higher than 105%, NI-DMM returns a NaN2 and the IVI overrange warning. 300 V and 1 A ranges (NI 4070/4072) or 700 V and 3 A ranges (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Not applicable |
| Frequency/Period | Not applicable | Occurs when the signal amplitude is below 5% of the voltage range3. Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Capacitance (NI 4072 only) | Occurs above 110% of the range. Above 110%, NI-DMM returns readings (non NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Occurs below 5% of the range, except in the 300 pF range. The 300 pF range does not have underrange. Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Inductance (NI 4072 only) | Occurs above 110% of the range. Above 110%, NI-DMM returns NaN2 and the IVI overrange warning. | Can occur below ≤1% of range for the 10 mH, 100 mH, 1 H, and 5 H ranges when the signal is too weak for the measurement to occur. In such cases, NI-DMM returns 0 H and the NI-DMM underrange warning. |
| 1Refer to the NI IVI Driver Help at ni.com/docs for the IVI overrange warning code. 2NaN is a digital display value for a floating-point representation of "Not a Number," as defined by the IEEE standard for binary floating point arithmetic. NaN is typically the result of an undefined operation, such as log(-1). 3Frequency voltage range is a property with the same allowed values as for the AC voltage ranges. Refer to Frequency/Period and Frequency Voltage Range for more information. |  |  |

Parent topic:

DMM Measurement Cycle

Related concepts:

- Frequency/Period

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=407x-overrangeunderrange_2.html language=enus -->
## TOPIC 00060: Overrange/Underrange

- bundle_id: `ni-dmm`
- source_path: `407x-overrangeunderrange_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-overrangeunderrange_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the overrange and/or underrange conditions, as applicable, for the PXI/PCI‑4070, PXI‑4071, and PXI‑4072. Function Overrange1 Underrange Function Overrange^1 Underrange DC Functions:Voltage, Current, Resistance, and Diode All ranges, except 300 V and 1 A (NI 4070/4072) or 1000

### Overrange/Underrange

This section describes the overrange and/or underrange conditions, as applicable, for the PXI/PCI‑4070, PXI‑4071, and PXI‑4072.

| Function | Overrange1 | Underrange |
| --- | --- | --- |
| Function | Overrange1 | Underrange |
| DC Functions:Voltage, Current, Resistance, and Diode | All ranges, except 300 V and 1 A (NI 4070/4072) or 1000 V and 3 A (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns NaN2 (except for the 100 MΩ range on the NI 4070/4072) and the IVI overrange warning. For the 100 MΩ range on the NI 4070/4072, measurements between the 105 MΩ and 1.05 GΩ ranges have a typical accuracy of 5%, although NI-DMM returns the IVI overrange warning. For measurements above 1.05 GΩ, NI-DMM returns NaN2 and the IVI overrange warning instead of the reading. 300 V and 1 A ranges (NI 4070/4072) or 1000 V and 3 A ranges (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Not applicable |
| AC Functions:Voltage and Current | All ranges, except 300 V and 1 A (NI 4070/4072) or 700 V and 3 A (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. At significantly higher than 105%, NI-DMM returns a NaN2 and the IVI overrange warning. 300 V and 1 A ranges (NI 4070/4072) or 700 V and 3 A ranges (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Not applicable |
| Frequency/Period | Not applicable | Occurs when the signal amplitude is below 5% of the voltage range3. Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Capacitance (NI 4072 only) | Occurs above 110% of the range. Above 110%, NI-DMM returns readings (non NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Occurs below 5% of the range, except in the 300 pF range. The 300 pF range does not have underrange. Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Inductance (NI 4072 only) | Occurs above 110% of the range. Above 110%, NI-DMM returns NaN2 and the IVI overrange warning. | Can occur below ≤1% of range for the 10 mH, 100 mH, 1 H, and 5 H ranges when the signal is too weak for the measurement to occur. In such cases, NI-DMM returns 0 H and the NI-DMM underrange warning. |
| 1Refer to the NI IVI Driver Help at ni.com/docs for the IVI overrange warning code. 2NaN is a digital display value for a floating-point representation of "Not a Number," as defined by the IEEE standard for binary floating point arithmetic. NaN is typically the result of an undefined operation, such as log(-1). 3Frequency voltage range is a property with the same allowed values as for the AC voltage ranges. Refer to Frequency/Period and Frequency Voltage Range for more information. |  |  |

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=407x-overrangeunderrange_3.html language=enus -->
## TOPIC 00061: Overrange/Underrange

- bundle_id: `ni-dmm`
- source_path: `407x-overrangeunderrange_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-overrangeunderrange_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the overrange and/or underrange conditions, as applicable, for the PXI/PCI‑4070, PXI‑4071, and PXI‑4072. Function Overrange1 Underrange Function Overrange^1 Underrange DC Functions:Voltage, Current, Resistance, and Diode All ranges, except 300 V and 1 A (NI 4070/4072) or 1000

### Overrange/Underrange

This section describes the overrange and/or underrange conditions, as applicable, for the PXI/PCI‑4070, PXI‑4071, and PXI‑4072.

| Function | Overrange1 | Underrange |
| --- | --- | --- |
| Function | Overrange1 | Underrange |
| DC Functions:Voltage, Current, Resistance, and Diode | All ranges, except 300 V and 1 A (NI 4070/4072) or 1000 V and 3 A (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns NaN2 (except for the 100 MΩ range on the NI 4070/4072) and the IVI overrange warning. For the 100 MΩ range on the NI 4070/4072, measurements between the 105 MΩ and 1.05 GΩ ranges have a typical accuracy of 5%, although NI-DMM returns the IVI overrange warning. For measurements above 1.05 GΩ, NI-DMM returns NaN2 and the IVI overrange warning instead of the reading. 300 V and 1 A ranges (NI 4070/4072) or 1000 V and 3 A ranges (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Not applicable |
| AC Functions:Voltage and Current | All ranges, except 300 V and 1 A (NI 4070/4072) or 700 V and 3 A (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. At significantly higher than 105%, NI-DMM returns a NaN2 and the IVI overrange warning. 300 V and 1 A ranges (NI 4070/4072) or 700 V and 3 A ranges (NI 4071): Occurs above 105% of the range. Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Not applicable |
| Frequency/Period | Not applicable | Occurs when the signal amplitude is below 5% of the voltage range3. Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Capacitance (NI 4072 only) | Occurs above 110% of the range. Above 110%, NI-DMM returns readings (non NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Occurs below 5% of the range, except in the 300 pF range. The 300 pF range does not have underrange. Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Inductance (NI 4072 only) | Occurs above 110% of the range. Above 110%, NI-DMM returns NaN2 and the IVI overrange warning. | Can occur below ≤1% of range for the 10 mH, 100 mH, 1 H, and 5 H ranges when the signal is too weak for the measurement to occur. In such cases, NI-DMM returns 0 H and the NI-DMM underrange warning. |
| 1Refer to the NI IVI Driver Help at ni.com/docs for the IVI overrange warning code. 2NaN is a digital display value for a floating-point representation of "Not a Number," as defined by the IEEE standard for binary floating point arithmetic. NaN is typically the result of an undefined operation, such as log(-1). 3Frequency voltage range is a property with the same allowed values as for the AC voltage ranges. Refer to Frequency/Period and Frequency Voltage Range for more information. |  |  |

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=407x-self-calibration.html language=enus -->
## TOPIC 00062: Self-Calibration

- bundle_id: `ni-dmm`
- source_path: `407x-self-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-self-calibration.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every measurement instrument performs within its specifications over a finite temperature range and time. If the excursions in temperature and time exceed those specified, and you need performance close to the specifications,then you must recalibrate the instrument at the new temperature or after a

### Self-Calibration

Every measurement instrument performs within its specifications over a finite temperature range
 and time. If the excursions in temperature and time exceed those specified, and you
 need performance close to the specifications,then you must recalibrate the
 instrument at the new temperature or after a certain amount of time. The
 NI 4070/4071/4072 have a self-calibration function that allows you to perform a
 calibration at the temperature you are making your measurements.

Self-calibration fully recalibrates all ranges for DC volts and resistance.

Note

niDMM_SelfCal

Self-calibration makes the NI 4070/4071/4072 highly accurate and very stable at any operating temperature—well outside of the traditional 18 °C to 28 °C range.

The typical way of expressing accuracy is:

Accuracy = ±(X ppm of reading + Y ppm of range)

For example, if the last calibration (self or external) was performed at 23 °C, and you are using
 the 10 V range on the NI 4070/4072 and applying a 5 V signal within 18 °C to 28 °C,
 the 2–year accuracy is:

2–year Accuracy = ±(25 ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

This traditional calculation method can cause errors if the temperature is not tightly
 controlled. When a system is built of multiple traditional instrument components
 integrated together, the instruments are subject to temperature rises caused by
 inherent compromises in air circulation and other factors.

If the ambient temperature is outside of the 18 °C to 28 °C range, to calculate the measurement accuracy, you need to calibrate your instrument at the ambient temperature, or add temperature coefficient accuracy for each additional degree outside the calibration range.

Using the NI 4070/4072, assume the ambient temperature is 38 °C. The temperature coefficient
 (tempco) without self-calibration is:

Tempco = (1 ppm of reading +1 ppm of range)/°C

The 2–year accuracy at 38 °C becomes:

±[25  ppm of 5 V + 6 ppm of 10 V] + [(1 ppm of 5 V + 1 ppm of 10 V)x 10] = ±335 µV (uncertainty)

Externally recalibrating a system can be difficult and expensive and as a result generally is performed infrequently.

The NI 4070/4071/4072 incorporates a proprietary self-calibration function for DCV and
 resistance. This function is unique to the NI 4070/4071/4072in the following
 ways:

- Self-calibration corrects for all DCV gain and offset errors within the DMM using a precision, high-stability internal voltage reference, which has an outstanding temperature coefficient and time drift.
- Self-calibration also accounts for all resistance, source, and gain errors.
- In resistance, all errors are corrected to a single internal 10 kΩ aerospace grade, high-stability foil resistor, which is stable to within 0.8 ppm/°C over the full operating range.

After performing self-calibration at 38 °C, you do notneed to add any uncertainty to account for temperature change.

The 2–year accuracy after self-calibration at 38 °C becomes:

±(25  ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

| Calibration Option | Application | When |
| --- | --- | --- |
| Factory calibration | All ranges Recalibrates for time drift of onboard references Corrects for AC flatness | Every two years |
| Self-calibration | Recalibrates the measurement path and ADC for DC volts and resistance | Every 90 days or when the temperature changes more than 5 °C from last self-calibration |
| ADC calibration | Recalibrates ADC drift for all ranges | Every reading when selected |
| NONE | Add to all specification 50 ppm of reading every 90 days and 3 ppm of reading/°C typical | Extended high-speed acquisitions |

The NI 4070/4071/4072 incorporates a temperature sensor that can be read to determine how much
 temperature has drifted from the previous calibration. In addition, the previous
 self-calibration time and date can also be read. For maximum accuracy, NI recommends
 self-calibrating once every 24 hours or when the temperature changes by more than
 ±1 °C on the NI 4081 and NI 4071 and more than ±5 °C on the NI 4070/4072. Otherwise,
 NI recommends running self-calibration every 90 days.

During self-calibration, the internal circuitry is automatically disconnected from the input.
 Therefore, for the majority of applications, users do not need to
 disconnect the input signals during self-calibration. However, excessive signal
 levels (>30 VDC, >30 VAC<sub>rms</sub>, >20 kHz) at the input terminals of
 the NI 4070/4071/4072 generate a self-calibration error. Disconnecting the input
 signals during a self-calibration prevents the error from occurring. If you are
 using the NI 4070/4071/4072 as part of a switching system, you can open (disconnect)
 the connections to the NI 4070/4071/4072 input terminals, switch to a non-connected
 path, or switch to a low voltage, low frequency path. For optimum reliability, avoid
 application of current to the Amps terminals or signals of >30 V to the Volts
 Input terminals during self-calibration.

Parent topic:

NI 4072

Related concepts:

- Performing Self-Calibration
- Accuracy
- ADC Calibration

Related information:

- niDMM_SelfCal
- niDMM Self Cal

<!--NI_TOPIC bundle=ni-dmm path=407x-self-calibration_2.html language=enus -->
## TOPIC 00063: Self-Calibration

- bundle_id: `ni-dmm`
- source_path: `407x-self-calibration_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-self-calibration_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every measurement instrument performs within its specifications over a finite temperature range and time. If the excursions in temperature and time exceed those specified, and you need performance close to the specifications,then you must recalibrate the instrument at the new temperature or after a

### Self-Calibration

Every measurement instrument performs within its specifications over a finite temperature range
 and time. If the excursions in temperature and time exceed those specified, and you
 need performance close to the specifications,then you must recalibrate the
 instrument at the new temperature or after a certain amount of time. The
 NI 4070/4071/4072 have a self-calibration function that allows you to perform a
 calibration at the temperature you are making your measurements.

Self-calibration fully recalibrates all ranges for DC volts and resistance.

Note

niDMM_SelfCal

Self-calibration makes the NI 4070/4071/4072 highly accurate and very stable at any operating temperature—well outside of the traditional 18 °C to 28 °C range.

The typical way of expressing accuracy is:

Accuracy = ±(X ppm of reading + Y ppm of range)

For example, if the last calibration (self or external) was performed at 23 °C, and you are using
 the 10 V range on the NI 4070/4072 and applying a 5 V signal within 18 °C to 28 °C,
 the 2–year accuracy is:

2–year Accuracy = ±(25 ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

This traditional calculation method can cause errors if the temperature is not tightly
 controlled. When a system is built of multiple traditional instrument components
 integrated together, the instruments are subject to temperature rises caused by
 inherent compromises in air circulation and other factors.

If the ambient temperature is outside of the 18 °C to 28 °C range, to calculate the measurement accuracy, you need to calibrate your instrument at the ambient temperature, or add temperature coefficient accuracy for each additional degree outside the calibration range.

Using the NI 4070/4072, assume the ambient temperature is 38 °C. The temperature coefficient
 (tempco) without self-calibration is:

Tempco = (1 ppm of reading +1 ppm of range)/°C

The 2–year accuracy at 38 °C becomes:

±[25  ppm of 5 V + 6 ppm of 10 V] + [(1 ppm of 5 V + 1 ppm of 10 V)x 10] = ±335 µV (uncertainty)

Externally recalibrating a system can be difficult and expensive and as a result generally is performed infrequently.

The NI 4070/4071/4072 incorporates a proprietary self-calibration function for DCV and
 resistance. This function is unique to the NI 4070/4071/4072in the following
 ways:

- Self-calibration corrects for all DCV gain and offset errors within the DMM using a precision, high-stability internal voltage reference, which has an outstanding temperature coefficient and time drift.
- Self-calibration also accounts for all resistance, source, and gain errors.
- In resistance, all errors are corrected to a single internal 10 kΩ aerospace grade, high-stability foil resistor, which is stable to within 0.8 ppm/°C over the full operating range.

After performing self-calibration at 38 °C, you do notneed to add any uncertainty to account for temperature change.

The 2–year accuracy after self-calibration at 38 °C becomes:

±(25  ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

| Calibration Option | Application | When |
| --- | --- | --- |
| Factory calibration | All ranges Recalibrates for time drift of onboard references Corrects for AC flatness | Every two years |
| Self-calibration | Recalibrates the measurement path and ADC for DC volts and resistance | Every 90 days or when the temperature changes more than 5 °C from last self-calibration |
| ADC calibration | Recalibrates ADC drift for all ranges | Every reading when selected |
| NONE | Add to all specification 50 ppm of reading every 90 days and 3 ppm of reading/°C typical | Extended high-speed acquisitions |

The NI 4070/4071/4072 incorporates a temperature sensor that can be read to determine how much
 temperature has drifted from the previous calibration. In addition, the previous
 self-calibration time and date can also be read. For maximum accuracy, NI recommends
 self-calibrating once every 24 hours or when the temperature changes by more than
 ±1 °C on the NI 4081 and NI 4071 and more than ±5 °C on the NI 4070/4072. Otherwise,
 NI recommends running self-calibration every 90 days.

During self-calibration, the internal circuitry is automatically disconnected from the input.
 Therefore, for the majority of applications, users do not need to
 disconnect the input signals during self-calibration. However, excessive signal
 levels (>30 VDC, >30 VAC<sub>rms</sub>, >20 kHz) at the input terminals of
 the NI 4070/4071/4072 generate a self-calibration error. Disconnecting the input
 signals during a self-calibration prevents the error from occurring. If you are
 using the NI 4070/4071/4072 as part of a switching system, you can open (disconnect)
 the connections to the NI 4070/4071/4072 input terminals, switch to a non-connected
 path, or switch to a low voltage, low frequency path. For optimum reliability, avoid
 application of current to the Amps terminals or signals of >30 V to the Volts
 Input terminals during self-calibration.

Parent topic:

NI 4071

<!--NI_TOPIC bundle=ni-dmm path=407x-self-calibration_3.html language=enus -->
## TOPIC 00064: Self-Calibration

- bundle_id: `ni-dmm`
- source_path: `407x-self-calibration_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x-self-calibration_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every measurement instrument performs within its specifications over a finite temperature range and time. If the excursions in temperature and time exceed those specified, and you need performance close to the specifications,then you must recalibrate the instrument at the new temperature or after a

### Self-Calibration

Every measurement instrument performs within its specifications over a finite temperature range
 and time. If the excursions in temperature and time exceed those specified, and you
 need performance close to the specifications,then you must recalibrate the
 instrument at the new temperature or after a certain amount of time. The
 NI 4070/4071/4072 have a self-calibration function that allows you to perform a
 calibration at the temperature you are making your measurements.

Self-calibration fully recalibrates all ranges for DC volts and resistance.

Note

niDMM_SelfCal

Self-calibration makes the NI 4070/4071/4072 highly accurate and very stable at any operating temperature—well outside of the traditional 18 °C to 28 °C range.

The typical way of expressing accuracy is:

Accuracy = ±(X ppm of reading + Y ppm of range)

For example, if the last calibration (self or external) was performed at 23 °C, and you are using
 the 10 V range on the NI 4070/4072 and applying a 5 V signal within 18 °C to 28 °C,
 the 2–year accuracy is:

2–year Accuracy = ±(25 ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

This traditional calculation method can cause errors if the temperature is not tightly
 controlled. When a system is built of multiple traditional instrument components
 integrated together, the instruments are subject to temperature rises caused by
 inherent compromises in air circulation and other factors.

If the ambient temperature is outside of the 18 °C to 28 °C range, to calculate the measurement accuracy, you need to calibrate your instrument at the ambient temperature, or add temperature coefficient accuracy for each additional degree outside the calibration range.

Using the NI 4070/4072, assume the ambient temperature is 38 °C. The temperature coefficient
 (tempco) without self-calibration is:

Tempco = (1 ppm of reading +1 ppm of range)/°C

The 2–year accuracy at 38 °C becomes:

±[25  ppm of 5 V + 6 ppm of 10 V] + [(1 ppm of 5 V + 1 ppm of 10 V)x 10] = ±335 µV (uncertainty)

Externally recalibrating a system can be difficult and expensive and as a result generally is performed infrequently.

The NI 4070/4071/4072 incorporates a proprietary self-calibration function for DCV and
 resistance. This function is unique to the NI 4070/4071/4072in the following
 ways:

- Self-calibration corrects for all DCV gain and offset errors within the DMM using a precision, high-stability internal voltage reference, which has an outstanding temperature coefficient and time drift.
- Self-calibration also accounts for all resistance, source, and gain errors.
- In resistance, all errors are corrected to a single internal 10 kΩ aerospace grade, high-stability foil resistor, which is stable to within 0.8 ppm/°C over the full operating range.

After performing self-calibration at 38 °C, you do notneed to add any uncertainty to account for temperature change.

The 2–year accuracy after self-calibration at 38 °C becomes:

±(25  ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

| Calibration Option | Application | When |
| --- | --- | --- |
| Factory calibration | All ranges Recalibrates for time drift of onboard references Corrects for AC flatness | Every two years |
| Self-calibration | Recalibrates the measurement path and ADC for DC volts and resistance | Every 90 days or when the temperature changes more than 5 °C from last self-calibration |
| ADC calibration | Recalibrates ADC drift for all ranges | Every reading when selected |
| NONE | Add to all specification 50 ppm of reading every 90 days and 3 ppm of reading/°C typical | Extended high-speed acquisitions |

The NI 4070/4071/4072 incorporates a temperature sensor that can be read to determine how much
 temperature has drifted from the previous calibration. In addition, the previous
 self-calibration time and date can also be read. For maximum accuracy, NI recommends
 self-calibrating once every 24 hours or when the temperature changes by more than
 ±1 °C on the NI 4081 and NI 4071 and more than ±5 °C on the NI 4070/4072. Otherwise,
 NI recommends running self-calibration every 90 days.

During self-calibration, the internal circuitry is automatically disconnected from the input.
 Therefore, for the majority of applications, users do not need to
 disconnect the input signals during self-calibration. However, excessive signal
 levels (>30 VDC, >30 VAC<sub>rms</sub>, >20 kHz) at the input terminals of
 the NI 4070/4071/4072 generate a self-calibration error. Disconnecting the input
 signals during a self-calibration prevents the error from occurring. If you are
 using the NI 4070/4071/4072 as part of a switching system, you can open (disconnect)
 the connections to the NI 4070/4071/4072 input terminals, switch to a non-connected
 path, or switch to a low voltage, low frequency path. For optimum reliability, avoid
 application of current to the Amps terminals or signals of >30 V to the Volts
 Input terminals during self-calibration.

Parent topic:

NI 4070

<!--NI_TOPIC bundle=ni-dmm path=407x65-aperture-time.html language=enus -->
## TOPIC 00065: Aperture Time

- bundle_id: `ni-dmm`
- source_path: `407x65-aperture-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x65-aperture-time.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify

### Aperture Time

Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify aperture time either in seconds or in power line cycles (PLCs).

The table below lists the default conditions for aperture along with other conditions related to the measurement cycle. These defaults optimize the DMM performance to its specified accuracy.

| Function | Default Aperture |  |  |  |
| --- | --- | --- | --- | --- |
| NI 4065 | NI 4080 NI 4070 | NI 4081 NI 4071 | NI 4082 NI 4072 |  |
| DC 7½ digits | — | — | 100 ms with Number of Averages = 4 | — |
| DC 6½ digits | 200 ms | 100 ms | 100 ms | 100 ms |
| DC 5½ digits | 3.33 ms | 500 µs | 500 µs1 | 500 µs |
| DC 4½ digits | 333 µs | 20 µs | 20 µs | 20 µs |
| DC Auto Range | 3.33 ms | 500 µs | 500 µs | 500 µs |
| AC | AC 6½ digits — 1 sec AC 5½ digits — Max (100 msec or (10/(minFreq))) AC 4½ digits — Max (10 msec or (5/(minFreq))) | Max (DC or 4/(minFreq)) | Max (DC or 4/(minFreq)) | Max (DC or 4/(minFreq)) |
| AC Auto Range | Max (100 ms or 10/(minFreq)) | Max (500 µs or 4/(minFreq)) | Max (500 µs or 4/(minFreq)) | Max (500 µs or 4/(minFreq)) |
| Frequency | — | 2/(minFreq) | 2/(minFreq) | 2/(minFreq) |
| Period | — | 2 x (the maximum period) | 2 x (the maximum period) | 2 x (the maximum period) |
| Capacitance and Inductance | — | — | — | Inductance (only) at 10 kHz = 13.65 ms Inductance and capacitance at 1 kHz = 31.29 ms Inductance and capacitance at 91 Hz = 270.22 ms |
| 1For the NI 4071, on the 5.5 DCV 100V range, use 1.6 ms. |  |  |  |  |

By default, the aperture time for a measurement is chosen by the driver based on the configured measurement and resolution. These values are chosen to ensure accuracy for 6½ digit measurements while not sacrificing performance at lower resolutions. For AC, excluding Auto Range, the aperture is expressed as Max (DC or 4/minFreq) for the NI 4070/4071/4072 and 1 sec for the NI 4065. MinFreq, or minimum frequency, is a user-programmable parameter with a default value of 20 Hz.

The same applies for other user selectable values of minFreq.For example, on the NI 4070/4071/4072, if a minFreq of 1 kHz is selected, then 4/minFreq = 4/1 kHz = 4 ms. In this case, 4 ms would be used as the AC aperture for resolutions <6 digits. For resolutions >6 digits, 100 ms would be used in this example. For example, on the NI 4065, if a minFreq of 100 Hz is selected, then 5/minFreq = 5/100 Hz = 50 ms. In this case, 50 ms would be used as the AC aperture for 4.5 digits. For 5.5 digits, 10/minFreq = 10/100 Hz = 100 ms would be used in this example. For resolutions >6 digits, 1 sec would be used in this example. For settling time defaults, refer to Settling Time.

#### Number of Averages for DC
 Measurements

This function is specific for high-resolution DC
 measurements.

Note

If your application requires a long aperture
 time (>100 ms) it is recommended that Auto Zero is enabled. The offset present
 may actually drift during the measurement, so that the stored Auto Zero value is
 invalid by the time the measurement completes. To compensate for this drift, several
 shorter measurements can be taken with a new Auto Zero offset applied to each
 measurement. These measurements can then be averaged together by the
 DMM so that a single value is returned.

To configure an averaged measurement,
 set the Number of Averages property. For example, if you desire a 500 ms measurement
 aperture, you can set the aperture to 50 ms and set Number of Averages to 10. Auto
 Zero must be enabled when the Number of Averages property is greater than one. The
 DMM will take ten 50 ms measurements each with Auto Zero and return a
 single measurement.

Note

Parent topic:

DMM Measurement Cycle

Related concepts:

- Settling Time
- Configuring Measurement Timing
- Auto Zero

<!--NI_TOPIC bundle=ni-dmm path=407x65-aperture-time_2.html language=enus -->
## TOPIC 00066: Aperture Time

- bundle_id: `ni-dmm`
- source_path: `407x65-aperture-time_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x65-aperture-time_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify

### Aperture Time

Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify aperture time either in seconds or in power line cycles (PLCs).

The table below lists the default conditions for aperture along with other conditions related to the measurement cycle. These defaults optimize the DMM performance to its specified accuracy.

| Function | Default Aperture |  |  |  |
| --- | --- | --- | --- | --- |
| NI 4065 | NI 4080 NI 4070 | NI 4081 NI 4071 | NI 4082 NI 4072 |  |
| DC 7½ digits | — | — | 100 ms with Number of Averages = 4 | — |
| DC 6½ digits | 200 ms | 100 ms | 100 ms | 100 ms |
| DC 5½ digits | 3.33 ms | 500 µs | 500 µs1 | 500 µs |
| DC 4½ digits | 333 µs | 20 µs | 20 µs | 20 µs |
| DC Auto Range | 3.33 ms | 500 µs | 500 µs | 500 µs |
| AC | AC 6½ digits — 1 sec AC 5½ digits — Max (100 msec or (10/(minFreq))) AC 4½ digits — Max (10 msec or (5/(minFreq))) | Max (DC or 4/(minFreq)) | Max (DC or 4/(minFreq)) | Max (DC or 4/(minFreq)) |
| AC Auto Range | Max (100 ms or 10/(minFreq)) | Max (500 µs or 4/(minFreq)) | Max (500 µs or 4/(minFreq)) | Max (500 µs or 4/(minFreq)) |
| Frequency | — | 2/(minFreq) | 2/(minFreq) | 2/(minFreq) |
| Period | — | 2 x (the maximum period) | 2 x (the maximum period) | 2 x (the maximum period) |
| Capacitance and Inductance | — | — | — | Inductance (only) at 10 kHz = 13.65 ms Inductance and capacitance at 1 kHz = 31.29 ms Inductance and capacitance at 91 Hz = 270.22 ms |
| 1For the NI 4071, on the 5.5 DCV 100V range, use 1.6 ms. |  |  |  |  |

By default, the aperture time for a measurement is chosen by the driver based on the configured measurement and resolution. These values are chosen to ensure accuracy for 6½ digit measurements while not sacrificing performance at lower resolutions. For AC, excluding Auto Range, the aperture is expressed as Max (DC or 4/minFreq) for the NI 4070/4071/4072 and 1 sec for the NI 4065. MinFreq, or minimum frequency, is a user-programmable parameter with a default value of 20 Hz.

The same applies for other user selectable values of minFreq.For example, on the NI 4070/4071/4072, if a minFreq of 1 kHz is selected, then 4/minFreq = 4/1 kHz = 4 ms. In this case, 4 ms would be used as the AC aperture for resolutions <6 digits. For resolutions >6 digits, 100 ms would be used in this example. For example, on the NI 4065, if a minFreq of 100 Hz is selected, then 5/minFreq = 5/100 Hz = 50 ms. In this case, 50 ms would be used as the AC aperture for 4.5 digits. For 5.5 digits, 10/minFreq = 10/100 Hz = 100 ms would be used in this example. For resolutions >6 digits, 1 sec would be used in this example. For settling time defaults, refer to Settling Time.

#### Number of Averages for DC
 Measurements

This function is specific for high-resolution DC
 measurements.

Note

If your application requires a long aperture
 time (>100 ms) it is recommended that Auto Zero is enabled. The offset present
 may actually drift during the measurement, so that the stored Auto Zero value is
 invalid by the time the measurement completes. To compensate for this drift, several
 shorter measurements can be taken with a new Auto Zero offset applied to each
 measurement. These measurements can then be averaged together by the
 DMM so that a single value is returned.

To configure an averaged measurement,
 set the Number of Averages property. For example, if you desire a 500 ms measurement
 aperture, you can set the aperture to 50 ms and set Number of Averages to 10. Auto
 Zero must be enabled when the Number of Averages property is greater than one. The
 DMM will take ten 50 ms measurements each with Auto Zero and return a
 single measurement.

Note

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=407x65-aperture-time_3.html language=enus -->
## TOPIC 00067: Aperture Time

- bundle_id: `ni-dmm`
- source_path: `407x65-aperture-time_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x65-aperture-time_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify

### Aperture Time

Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify aperture time either in seconds or in power line cycles (PLCs).

The table below lists the default conditions for aperture along with other conditions related to the measurement cycle. These defaults optimize the DMM performance to its specified accuracy.

| Function | Default Aperture |  |  |  |
| --- | --- | --- | --- | --- |
| NI 4065 | NI 4080 NI 4070 | NI 4081 NI 4071 | NI 4082 NI 4072 |  |
| DC 7½ digits | — | — | 100 ms with Number of Averages = 4 | — |
| DC 6½ digits | 200 ms | 100 ms | 100 ms | 100 ms |
| DC 5½ digits | 3.33 ms | 500 µs | 500 µs1 | 500 µs |
| DC 4½ digits | 333 µs | 20 µs | 20 µs | 20 µs |
| DC Auto Range | 3.33 ms | 500 µs | 500 µs | 500 µs |
| AC | AC 6½ digits — 1 sec AC 5½ digits — Max (100 msec or (10/(minFreq))) AC 4½ digits — Max (10 msec or (5/(minFreq))) | Max (DC or 4/(minFreq)) | Max (DC or 4/(minFreq)) | Max (DC or 4/(minFreq)) |
| AC Auto Range | Max (100 ms or 10/(minFreq)) | Max (500 µs or 4/(minFreq)) | Max (500 µs or 4/(minFreq)) | Max (500 µs or 4/(minFreq)) |
| Frequency | — | 2/(minFreq) | 2/(minFreq) | 2/(minFreq) |
| Period | — | 2 x (the maximum period) | 2 x (the maximum period) | 2 x (the maximum period) |
| Capacitance and Inductance | — | — | — | Inductance (only) at 10 kHz = 13.65 ms Inductance and capacitance at 1 kHz = 31.29 ms Inductance and capacitance at 91 Hz = 270.22 ms |
| 1For the NI 4071, on the 5.5 DCV 100V range, use 1.6 ms. |  |  |  |  |

By default, the aperture time for a measurement is chosen by the driver based on the configured measurement and resolution. These values are chosen to ensure accuracy for 6½ digit measurements while not sacrificing performance at lower resolutions. For AC, excluding Auto Range, the aperture is expressed as Max (DC or 4/minFreq) for the NI 4070/4071/4072 and 1 sec for the NI 4065. MinFreq, or minimum frequency, is a user-programmable parameter with a default value of 20 Hz.

The same applies for other user selectable values of minFreq.For example, on the NI 4070/4071/4072, if a minFreq of 1 kHz is selected, then 4/minFreq = 4/1 kHz = 4 ms. In this case, 4 ms would be used as the AC aperture for resolutions <6 digits. For resolutions >6 digits, 100 ms would be used in this example. For example, on the NI 4065, if a minFreq of 100 Hz is selected, then 5/minFreq = 5/100 Hz = 50 ms. In this case, 50 ms would be used as the AC aperture for 4.5 digits. For 5.5 digits, 10/minFreq = 10/100 Hz = 100 ms would be used in this example. For resolutions >6 digits, 1 sec would be used in this example. For settling time defaults, refer to Settling Time.

#### Number of Averages for DC
 Measurements

This function is specific for high-resolution DC
 measurements.

Note

If your application requires a long aperture
 time (>100 ms) it is recommended that Auto Zero is enabled. The offset present
 may actually drift during the measurement, so that the stored Auto Zero value is
 invalid by the time the measurement completes. To compensate for this drift, several
 shorter measurements can be taken with a new Auto Zero offset applied to each
 measurement. These measurements can then be averaged together by the
 DMM so that a single value is returned.

To configure an averaged measurement,
 set the Number of Averages property. For example, if you desire a 500 ms measurement
 aperture, you can set the aperture to 50 ms and set Number of Averages to 10. Auto
 Zero must be enabled when the Number of Averages property is greater than one. The
 DMM will take ten 50 ms measurements each with Auto Zero and return a
 single measurement.

Note

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=407x65-aperture-time_4.html language=enus -->
## TOPIC 00068: Aperture Time

- bundle_id: `ni-dmm`
- source_path: `407x65-aperture-time_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/407x65-aperture-time_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify

### Aperture Time

Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify aperture time either in seconds or in power line cycles (PLCs).

The table below lists the default conditions for aperture along with other conditions related to the measurement cycle. These defaults optimize the DMM performance to its specified accuracy.

| Function | Default Aperture |  |  |  |
| --- | --- | --- | --- | --- |
| NI 4065 | NI 4080 NI 4070 | NI 4081 NI 4071 | NI 4082 NI 4072 |  |
| DC 7½ digits | — | — | 100 ms with Number of Averages = 4 | — |
| DC 6½ digits | 200 ms | 100 ms | 100 ms | 100 ms |
| DC 5½ digits | 3.33 ms | 500 µs | 500 µs1 | 500 µs |
| DC 4½ digits | 333 µs | 20 µs | 20 µs | 20 µs |
| DC Auto Range | 3.33 ms | 500 µs | 500 µs | 500 µs |
| AC | AC 6½ digits — 1 sec AC 5½ digits — Max (100 msec or (10/(minFreq))) AC 4½ digits — Max (10 msec or (5/(minFreq))) | Max (DC or 4/(minFreq)) | Max (DC or 4/(minFreq)) | Max (DC or 4/(minFreq)) |
| AC Auto Range | Max (100 ms or 10/(minFreq)) | Max (500 µs or 4/(minFreq)) | Max (500 µs or 4/(minFreq)) | Max (500 µs or 4/(minFreq)) |
| Frequency | — | 2/(minFreq) | 2/(minFreq) | 2/(minFreq) |
| Period | — | 2 x (the maximum period) | 2 x (the maximum period) | 2 x (the maximum period) |
| Capacitance and Inductance | — | — | — | Inductance (only) at 10 kHz = 13.65 ms Inductance and capacitance at 1 kHz = 31.29 ms Inductance and capacitance at 91 Hz = 270.22 ms |
| 1For the NI 4071, on the 5.5 DCV 100V range, use 1.6 ms. |  |  |  |  |

By default, the aperture time for a measurement is chosen by the driver based on the configured measurement and resolution. These values are chosen to ensure accuracy for 6½ digit measurements while not sacrificing performance at lower resolutions. For AC, excluding Auto Range, the aperture is expressed as Max (DC or 4/minFreq) for the NI 4070/4071/4072 and 1 sec for the NI 4065. MinFreq, or minimum frequency, is a user-programmable parameter with a default value of 20 Hz.

The same applies for other user selectable values of minFreq.For example, on the NI 4070/4071/4072, if a minFreq of 1 kHz is selected, then 4/minFreq = 4/1 kHz = 4 ms. In this case, 4 ms would be used as the AC aperture for resolutions <6 digits. For resolutions >6 digits, 100 ms would be used in this example. For example, on the NI 4065, if a minFreq of 100 Hz is selected, then 5/minFreq = 5/100 Hz = 50 ms. In this case, 50 ms would be used as the AC aperture for 4.5 digits. For 5.5 digits, 10/minFreq = 10/100 Hz = 100 ms would be used in this example. For resolutions >6 digits, 1 sec would be used in this example. For settling time defaults, refer to Settling Time.

#### Number of Averages for DC
 Measurements

This function is specific for high-resolution DC
 measurements.

Note

If your application requires a long aperture
 time (>100 ms) it is recommended that Auto Zero is enabled. The offset present
 may actually drift during the measurement, so that the stored Auto Zero value is
 invalid by the time the measurement completes. To compensate for this drift, several
 shorter measurements can be taken with a new Auto Zero offset applied to each
 measurement. These measurements can then be averaged together by the
 DMM so that a single value is returned.

To configure an averaged measurement,
 set the Number of Averages property. For example, if you desire a 500 ms measurement
 aperture, you can set the aperture to 50 ms and set Number of Averages to 10. Auto
 Zero must be enabled when the Number of Averages property is greater than one. The
 DMM will take ten 50 ms measurements each with Auto Zero and return a
 single measurement.

Note

Parent topic:

NI 4065 DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=4080-front-panel-connections.html language=enus -->
## TOPIC 00069: PXIe-4080 Front Panel Connections

- bundle_id: `ni-dmm`
- source_path: `4080-front-panel-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4080-front-panel-connections.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC Voltage AC Voltage DC Current AC Current 2-Wire Resistance 4-Wire Resistance Voltage Drop Across a Diode Frequency/Period Voltage Waveform Current Waveform

### PXIe-4080 Front
 Panel Connections

[IMAGE alt='image' src='GUID-300DAF7E-0BD9-49F9-94B6-D3F17E3E7EF2-a5.svg']

Parent topic:

NI PXIe-4080

#### DC Voltage

[IMAGE alt='image' src='GUID-B7776E3B-EA1B-4407-9EB4-C51DBF321CAF-a5.svg']

#### AC Voltage

[IMAGE alt='image' src='GUID-FC9EC6BB-76D4-427E-A7A7-C54292C4C315-a5.svg']

#### DC Current

[IMAGE alt='image' src='GUID-C763E64C-6C56-4496-8CB0-2AC42C623A23-a5.svg']

#### AC Current

[IMAGE alt='image' src='GUID-142CBF63-F5E2-422E-BB75-0A6CF34745A4-a5.svg']

#### 2-Wire Resistance

[IMAGE alt='image' src='GUID-BB494E3D-AE46-4176-AEEC-4639116065D4-a5.svg']

#### 4-Wire Resistance

[IMAGE alt='image' src='GUID-693012D8-A0C0-4285-A03D-3710E3AFEA8F-a5.svg']

#### Voltage Drop Across a Diode

[IMAGE alt='image' src='GUID-D3C1D634-7F73-4A0E-BA15-9279E3BF1DCA-a5.svg']

#### Frequency/Period

[IMAGE alt='image' src='GUID-F76E9756-5523-43CF-83D5-A00E7AE20E98-a5.svg']

#### Voltage Waveform

[IMAGE alt='image' src='GUID-FC9EC6BB-76D4-427E-A7A7-C54292C4C315-a5.svg']

#### Current Waveform

[IMAGE alt='image' src='GUID-C763E64C-6C56-4496-8CB0-2AC42C623A23-a5.svg']

<!--NI_TOPIC bundle=ni-dmm path=40804082-fuse-replacement.html language=enus -->
## TOPIC 00070: Fuse Replacement

- bundle_id: `ni-dmm`
- source_path: `40804082-fuse-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/40804082-fuse-replacement.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains how to replace the fuse in the NI 4080/4082. For protection against fire, replace the fuse only with fuses of the same type and rating. Refer to the following table for fuse types. DMM Fuse Rating Fuse Type NI 4080/4082 1 A 400 V Time-lag To replace the fuse, complete the follo

### Fuse Replacement

This section explains how to replace the fuse in the NI 4080/4082.

Caution

| DMM | Fuse Rating | Fuse Type |
| --- | --- | --- |
| NI 4080/4082 | 1 A 400 V | Time-lag |

To replace the fuse, complete the following steps.

1. Remove all front panel connections from the device.
2. Power off the chassis, and remove the device.
3. Locate the fuse hold shown in the image below.
4. Insert a screwdriver into the fuse hole. 
 Caution For protection against fire, replace the fuse only with fuses of the same type and rating. Refer to the following table for fuse types.
5. Gently press the fuse with the screwdriver until one of the fuse clamps releases.
6. Locate the fuse slot shown in the image below.
7. Pry the fuse loose from the fuse slot.
8. Verify that the fuse is blown by measuring discontinuity across the fuse using another meter.
9. Insert a new fuse into the fuse slot as shown in the image below.
10. Gently press the fuse with the screwdriver until both fuse clamps snap the fuse into place.

Parent topic:

NI PXIe-4082

<!--NI_TOPIC bundle=ni-dmm path=40804082-fuse-replacement_2.html language=enus -->
## TOPIC 00071: Fuse Replacement

- bundle_id: `ni-dmm`
- source_path: `40804082-fuse-replacement_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/40804082-fuse-replacement_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains how to replace the fuse in the NI 4080/4082. For protection against fire, replace the fuse only with fuses of the same type and rating. Refer to the following table for fuse types. DMM Fuse Rating Fuse Type NI 4080/4082 1 A 400 V Time-lag To replace the fuse, complete the follo

### Fuse Replacement

This section explains how to replace the fuse in the NI 4080/4082.

Caution

| DMM | Fuse Rating | Fuse Type |
| --- | --- | --- |
| NI 4080/4082 | 1 A 400 V | Time-lag |

To replace the fuse, complete the following steps.

1. Remove all front panel connections from the device.
2. Power off the chassis, and remove the device.
3. Locate the fuse hold shown in the image below.
4. Insert a screwdriver into the fuse hole. 
 Caution For protection against fire, replace the fuse only with fuses of the same type and rating. Refer to the following table for fuse types.
5. Gently press the fuse with the screwdriver until one of the fuse clamps releases.
6. Locate the fuse slot shown in the image below.
7. Pry the fuse loose from the fuse slot.
8. Verify that the fuse is blown by measuring discontinuity across the fuse using another meter.
9. Insert a new fuse into the fuse slot as shown in the image below.
10. Gently press the fuse with the screwdriver until both fuse clamps snap the fuse into place.

Parent topic:

NI PXIe-4080

<!--NI_TOPIC bundle=ni-dmm path=4081-dc-and-ac-current.html language=enus -->
## TOPIC 00072: DC and AC Current

- bundle_id: `ni-dmm`
- source_path: `4081-dc-and-ac-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4081-dc-and-ac-current.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4081 allows you to measure currents ranging from a few picoamps to three amperes. DC Current mode has eight ranges that go from 1 µA to 3 A in decades, and AC Current mode has six ranges that go from 100 µA[rms] to 3 A[rms] in decades. The AC Current mode uses the same fast measurement techni

### DC and AC Current

The NI 4081 allows you to measure currents ranging from a few picoamps to three amperes. DC
 Current mode has eight ranges that go from 1 µA to 3 A in decades, and AC Current
 mode has six ranges that go from 100 µA<sub>rms</sub> to
 3 A<sub>rms</sub> in decades. The AC Current mode uses the same fast measurement
 technique as the AC Volts DC Coupled mode.

Note

#### Shunt Resistors

The NI 4081
 uses internal shunt resistors with temperature coefficient and power ratings
 selected to reduce resistor self-heating errors. For the effect of temperature
 changes on the accuracy of the measurements, refer to the specifications document
 and the temperature coefficient. Refer to the following table for the shunt resistor
 values.

| Range | Shunt Resistor Value |
| --- | --- |
| 3 A | 0.05 Ω |
| 1 A | 0.05 Ω |
| 100 mA | 0.5 Ω |
| 10 mA | 5 Ω |
| 1 mA | 50 Ω |
| 100 µA | 500 Ω |
| 10 µA | 50 kΩ |
| 1 µA | 50 kΩ |

Tip

Whenever possible, switch the NI 4081 into the current measurement
 function before applying the current. Switching inductive current sources
 generally creates flyback voltages that stress the relay and, if done
 frequently, can shorten the reliability of the relay. Also, avoid interrupting
 the current by switching out of the current measurement function when currents
 are flowing through the circuit.

Parent topic:

DMM Measurements

Related concepts:

- Resistor Self-Heating

<!--NI_TOPIC bundle=ni-dmm path=4081-front-panel-connections.html language=enus -->
## TOPIC 00073: PXIe-4081 Front Panel Connections

- bundle_id: `ni-dmm`
- source_path: `4081-front-panel-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4081-front-panel-connections.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Measuring DC Voltage Attach the test probes for measuring DC voltage as shown in the following figure: 4 DC Voltage Connections Measuring AC Voltage Attach the test probes to measure AC voltage as shown in the following figure: 5 AC Voltage Connections Measuring AC and DC Current Attach the test pro

### PXIe-4081 Front
 Panel Connections

[IMAGE alt='image' src='GUID-EA0D1C36-07CB-49E8-A301-34484FF2B721-a5.svg']

Parent topic:

NI 4081

#### Measuring DC Voltage

Attach the test probes for measuring DC voltage as shown in the following figure:

Figure 4.

[IMAGE alt='image' src='GUID-0C5C6BCB-E8AB-4AAE-848B-DB10FC17E6ED-a5.svg']

#### Measuring AC Voltage

Attach the test probes to measure AC voltage as shown in the following figure:

Figure 5.

[IMAGE alt='image' src='GUID-4C9FCF51-CC08-4E58-8D0C-31CEA52136E4-a5.svg']

#### Measuring AC and DC Current

Attach the test probes for measuring AC current or DC current as shown in the
 following figures:

Figure 6.

[IMAGE alt='image' src='GUID-947FCC01-3334-406D-BF66-B1398C676F39-a5.svg']

Figure 7.

[IMAGE alt='image' src='GUID-5B80A234-7581-43F5-9B76-78BCE5667BA5-a5.svg']

#### Measuring Resistance

Attach the test probes for 2-wire resistance or 4-wire resistance measurements as
 shown in the following figures.

Figure 8.

[IMAGE alt='image' src='GUID-6C173AD6-E405-490A-91D5-C279E75B9730-a5.svg']

Figure 9.

[IMAGE alt='image' src='GUID-C7A5EE7C-4341-47C7-9C06-91734C3F4061-a5.svg']

Note

#### Measuring Voltage Drop Across a Diode

Attach the test probes to measure voltage drop across a diode as shown in the
 following figure:

Figure 10.

[IMAGE alt='image' src='GUID-57D8E931-F2DF-48A1-90A2-903218752685-a5.svg']

#### Measuring Frequency and Periodic Signal
 Frequency

Attach the test probes for measuring frequency and periodic signal frequencies as
 shown in the following figure:

Figure 11.

[IMAGE alt='image' src='GUID-B90149B1-5B03-4D66-850C-3FC7DABADB1E-a5.svg']

#### Acquiring Current and Voltage
 Waveforms

Attach the test probes for current waveform or voltage waveform acquisition as shown in the
 following figures:

Figure 12.

[IMAGE alt='image' src='GUID-947FCC01-3334-406D-BF66-B1398C676F39-a5.svg']

Figure 13.

[IMAGE alt='image' src='GUID-4C9FCF51-CC08-4E58-8D0C-31CEA52136E4-a5.svg']

<!--NI_TOPIC bundle=ni-dmm path=4081-fuse-replacement.html language=enus -->
## TOPIC 00074: Fuse Replacement

- bundle_id: `ni-dmm`
- source_path: `4081-fuse-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4081-fuse-replacement.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains how to replace the fuse in the NI 4081. For protection against fire, replace the fuse only with fuses of the same type and rating. Refer to the following table for fuse types. DMM Fuse Rating Fuse Type NI 4081 3.5 A 1000 V Time-Delay User-Replaceable To replace the fuse, comple

### Fuse Replacement

This section explains how to replace the fuse in the NI 4081.

Caution

| DMM | Fuse Rating | Fuse Type |
| --- | --- | --- |
| NI 4081 | 3.5 A 1000 V | Time-Delay User-Replaceable |

To replace the fuse, complete the following steps.

1. Remove all front panel connections from the device.
2. Power off the chassis, and remove the device.
3. Unscrew the shield to locate the fuse slot, as shown in the image below.
4. Use a screwdriver to pry the fuse loose from the fuse slot, as shown in the image below. Caution For protection against fire, replace the fuse only with fuses of the same type and rating. Refer to the following table for fuse types.
5. Verify that the fuse is blown by measuring discontinuity across the fuse using another meter.
6. Insert a new fuse into the fuse slot as shown in the image below.
7. Gently press the fuse with the screwdriver until both fuse clamps snap the fuse into place.

Parent topic:

NI 4081

<!--NI_TOPIC bundle=ni-dmm path=4081-input-protection.html language=enus -->
## TOPIC 00075: Input Protection

- bundle_id: `ni-dmm`
- source_path: `4081-input-protection.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4081-input-protection.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The current-measuring circuit is protected with a fuse rated at T 3.5 A 1000 V. The DMM can measure up to 3 A DC or 3 A[rms] with up to 4.2 A peak current (sine wave only). Higher currents will blow the fuse.If you apply higher current level to a range, the input protection circuitry of the DMM auto

### Input Protection

The current-measuring circuit is protected with a fuse rated at T 3.5 A 1000 V. The DMM can measure up to 3 A DC or 3 A<sub>rms</sub> with up to 4.2 A peak current (sine wave only). Higher currents will blow the fuse.

If you apply higher current level to a range, the input protection circuitry of the DMM automatically engages, and you receive an overrange warning.

Also, keep in mind that exposing the current measurement connectors to voltage sources while the DC or AC current functions are selected may trigger the input protection circuitry or even blow the fuse.

Parent topic:

DC and AC Current

Related concepts:

- Fuse Replacement

<!--NI_TOPIC bundle=ni-dmm path=4082-admittance.html language=enus -->
## TOPIC 00076: Admittance

- bundle_id: `ni-dmm`
- source_path: `4082-admittance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-admittance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To simplify mathematical manipulation, calculation, and analysis, it is sometimes convenient to express the impedance as its reciprocal quantity, or admittance. Admittance is defined asY = 1/Z = I/Vand can be written asY = G + jBwhere G and B are the rectangular (real and imaginary) components, know

### Admittance

To simplify mathematical manipulation, calculation, and analysis, it is sometimes convenient to express the impedance as its reciprocal quantity, or admittance. Admittance is defined as

Y = 1/Z = I/V

and can be written as

Y = G + jB

where G and B are the rectangular (real and imaginary) components, known as conductance and susceptance respectively. The conductance G is the reciprocal of the parallel resistance, as follows:

G = 1/R<sub>P</sub>

The susceptance for capacitors is expressed as follows:

B<sub>C</sub> = 2[IMAGE alt='image' src='GUID-CC0315BF-B093-4875-ADCB-08A9AD050B4C-a5.gif']fC<sub>P</sub> = 1/X<sub>C</sub>

The susceptance for inductors is expressed as follows:

B<sub>L</sub> = 1/2[IMAGE alt='image' src='GUID-CC0315BF-B093-4875-ADCB-08A9AD050B4C-a5.gif']fL<sub>P</sub> = 1/X<sub>L</sub>

Parent topic:

Theoretical Background

<!--NI_TOPIC bundle=ni-dmm path=4082-cabling.html language=enus -->
## TOPIC 00077: Cabling

- bundle_id: `ni-dmm`
- source_path: `4082-cabling.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-cabling.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To reduce variations on the system parasitics, NI recommends using coaxial cable or shielded twisted pairs, with the shield used as the current return path and connected to the LO input of the DMM. This configuration makes the OPEN/SHORT compensation more practical and helps to reduce the noise pick

### Cabling

To reduce variations on the system parasitics, NI recommends using coaxial cable or shielded twisted pairs, with the shield used as the current return path and connected to the LO input of the DMM. This configuration makes the OPEN/SHORT compensation more practical and helps to reduce the noise pickup.

For manual probing of surface mount parts, you can use a pair of tweezers. The NI 4082 can compensate for the impedance introduced by the test fixtures. Refer to the OPEN/SHORT Compensation section for more information. Reduce the mechanical variations (for example, movement or flexing of cables, or changing fixturing) between two consecutive measurements to maintain repeatability.

Use a high-quality cable, such as Belden 83317E available at www.belden.com. NI recommends cables with Teflon, polypropylene, or polyethylene insulation. For more information about cabling requirements, refer to Interconnects and Cables. Very good performance has been achieved using up to 25 feet of this cable in both capacitance and inductance measurements by performing OPEN/SHORT compensation prior to the measurement.

Parent topic:

Measurement Considerations

Related concepts:

- OPEN/SHORT Compensation
- NI PXIe-4082

<!--NI_TOPIC bundle=ni-dmm path=4082-capacitanceinductance.html language=enus -->
## TOPIC 00078: Capacitance/Inductance

- bundle_id: `ni-dmm`
- source_path: `4082-capacitanceinductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-capacitanceinductance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4082 uses a 2-wire, multi-tone, constant current technique to measure impedance. When a multi-tone constant current source (I[src]) is applied to the device under test (DUT), the NI 4082 measures the fundamental and third harmonic of the voltage waveform.If the residual series impedance (Z[s]

### Capacitance/Inductance

The NI 4082 uses a 2-wire, multi-tone, constant current technique to measure impedance. When a multi-tone constant current source (I<sub>src</sub>) is applied to the device under test (DUT), the NI 4082 measures the fundamental and third harmonic of the voltage waveform.

[IMAGE alt='image' src='GUID-ED3A7AED-DEA3-482A-81D1-8780216530C6-a5.svg']

If the residual series impedance (Z<sub>s</sub>) and the stray parallel admittance (Y<sub>p</sub>) introduce a significant error in the measurement, the NI 4082 can measure the magnitude of the error and reduce it using compensation techniques. For more information, refer to the OPEN/SHORT Compensation section.

Refer to the NI 4082 section for the measurement ranges on the NI 4082 for the capacitance and inductance modes.

Parent topic:

DMM Measurements

Related concepts:

- OPEN/SHORT Compensation
- NI PXIe-4082

<!--NI_TOPIC bundle=ni-dmm path=4082-capacitors.html language=enus -->
## TOPIC 00079: Capacitors

- bundle_id: `ni-dmm`
- source_path: `4082-capacitors.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-capacitors.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A capacitor is an electronic component that is capable of storing energy as charge. Each capacitor consists of two plates of conductive material that are separated by a dielectric, which could be air, paper, plastic, oxide or any other type of insulator. The dielectric constant, or K, of an insulato

### Capacitors

A capacitor is an electronic component
 that is capable of storing energy as charge. Each capacitor consists of two plates
 of conductive material that are separated by a dielectric, which could be air,
 paper, plastic, oxide or any other type of insulator. The dielectric constant, or
 K, of an insulator represents its ability to store charge.
 The table below shows the K values for different dielectric
 materials:

| Dielectric | Dielectric Constant (K) |
| --- | --- |
| Vacuum | 1 |
| Air | 1.0001 |
| Teflon | 2.0 |
| Polypropylene | 2.1 |
| Polystyrene | 2.5 |
| Polycarbonate | 2.9 |
| Polyester | 3.2 |
| FR-4 | 3.8–5.0 |
| Glass | 4.0–8.5 |
| Mica | 6.5–8.7 |
| Ceramics | 6 to several thousand |
| Aluminum oxide | 7 |
| Tantalum oxide | 11 |

The electrical properties of insulators show variability with factors such as
 temperature, frequency, voltage, and humidity. This variability and the mechanical
 construction of the capacitor create a less than ideal device.

A better
 representation of real-world capacitors is shown in the equivalent model below,
 which aids in understanding the different parasitic elements that are present in a
 real-world component. These parasitic elements impact the capacitor impedance at
 different test frequencies.

[IMAGE alt='image' src='GUID-E69E69C9-098E-4AF9-B077-DE2B52574A33-a5.svg']

The parallel
 resistance, Rp, is usually a large value, and its effect is
 significant only when measuring capacitors with small values. The equivalent series
 resistance, Rs, although a small value, is important in
 capacitors with large values, where the impedance is small compared to
 Rs and where high power is dissipated. The series inductance,
 Ls, represents the total inductance and capacitance roll-off
 at higher frequencies.

At low frequencies, capacitance varies with frequency
 and the test signal level, due to changes in the dielectric properties. The
 following graph shows a 2.2 µF 100 V aluminum electrolytic capacitor measured at
 different frequencies. The error is referenced to the measurement using a 1
 V<sub>rms</sub> AC test signal at 1 kHz.

[IMAGE alt='image' src='GUID-AE3640B0-4BBE-42EE-8423-8CF0627C2C76-a5.gif']

These factors
 cause capacitors to have different values under varying conditions of temperature,
 frequency, and signal level.

Parent topic:

Theoretical Background

<!--NI_TOPIC bundle=ni-dmm path=4082-dc-bias.html language=enus -->
## TOPIC 00080: DC Bias

- bundle_id: `ni-dmm`
- source_path: `4082-dc-bias.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-dc-bias.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To test some polarized components, such as electrolytic and tantalum capacitors, it may be preferable to use only positive voltages. During normal operation, the AC current source swings negative 50% of the time, which results in an inverse polarization of the capacitor under test. To prevent this i

### DC Bias

To test some polarized components, such as electrolytic and tantalum capacitors, it may be preferable to use only positive voltages. During normal operation, the AC current source swings negative 50% of the time, which results in an inverse polarization of the capacitor under test. To prevent this inverse polarization, you can apply a DC bias to prevent the voltage across the part from becoming negative.

Note

The DC bias voltage is a fixed value and can only be turned on and off. The nominal voltage value is 0.45 V and can be used for the 300 pF, 1 nF, 10 nF, 100 nF, 1000 µF and 10,000 µF capacitance ranges. The default setting is OFF.

Parent topic:

Capacitance/Inductance

<!--NI_TOPIC bundle=ni-dmm path=4082-frequency-effects-of-real-world-components.html language=enus -->
## TOPIC 00081: Frequency Effects of Real-World Components

- bundle_id: `ni-dmm`
- source_path: `4082-frequency-effects-of-real-world-components.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-frequency-effects-of-real-world-components.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Due to the parasitics and materials used in the construction of real-world components, the measured capacitance or inductance value can differ from one instrument to another. When measuring capacitors with better dielectric properties, you observe much smaller reading differences between various ins

### Frequency Effects of Real-World Components

Due to the parasitics and materials used in the construction of real-world components, the measured capacitance or inductance value can differ from one instrument to another. When measuring capacitors with better dielectric properties, you observe much smaller reading differences between various instruments. This observation also applies to inductors with better magnetics.

The following table shows some examples of dielectrics with good and poor frequency characteristics:

| Dielectrics with Good Frequency Characteristics | Dielectrics with Poor Frequency Characteristics |
| --- | --- |
| Teflon Mica Polypropylene Polycarbonate Ceramic COG | Tantalum oxide Aluminum oxide Ceramic Y5U |

Due to the amount of magnetization current required, you can see an increase in sensitivity to frequency changes and other dependency factors in inductors with cores of larger dimensions, such as those used in transformers and power inductors.

Parent topic:

Measurement Considerations

<!--NI_TOPIC bundle=ni-dmm path=4082-front-panel-connections.html language=enus -->
## TOPIC 00082: PXIe-4082 Front Panel Connections

- bundle_id: `ni-dmm`
- source_path: `4082-front-panel-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-front-panel-connections.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Capacitance Inductance DC Voltage AC Current AC Voltage DC Current 2-Wire Resistance 4-Wire Resistance Voltage Drop Across a Diode Frequency/Period Voltage Waveform Current Waveform

### PXIe-4082 Front
 Panel Connections

[IMAGE alt='image' src='GUID-10686DC1-519E-4E6D-9910-B86ED9CBD4D2-a5.svg']

Parent topic:

NI PXIe-4082

#### Capacitance

[IMAGE alt='image' src='GUID-E7746002-545D-48B2-AE70-0D00CCF2CAFB-a5.svg']

#### Inductance

[IMAGE alt='image' src='GUID-6F84CE5E-0B95-4C53-81FB-D66566E5AA3C-a5.svg']

#### DC Voltage

[IMAGE alt='image' src='GUID-E846B6D2-16D3-4873-903B-CFF6170B6112-a5.svg']

#### AC Current

[IMAGE alt='image' src='GUID-142CBF63-F5E2-422E-BB75-0A6CF34745A4-a5.svg']

#### AC Voltage

[IMAGE alt='image' src='GUID-120AB37A-E1DE-4ECB-8410-252EF97FB724-a5.svg']

#### DC Current

[IMAGE alt='image' src='GUID-C763E64C-6C56-4496-8CB0-2AC42C623A23-a5.svg']

#### 2-Wire Resistance

[IMAGE alt='image' src='GUID-EB776287-19E8-4539-911A-2A3BF2CADE47-a5.svg']

#### 4-Wire Resistance

[IMAGE alt='image' src='GUID-8120FB49-90ED-49FC-81A1-399F6B55DB44-a5.svg']

#### Voltage Drop Across a Diode

[IMAGE alt='image' src='GUID-8AC63386-A0EE-4264-B194-112030B1281B-a5.svg']

#### Frequency/Period

[IMAGE alt='image' src='GUID-7BB802FC-C322-4257-824F-FFF592EADD03-a5.svg']

#### Voltage Waveform

[IMAGE alt='image' src='GUID-120AB37A-E1DE-4ECB-8410-252EF97FB724-a5.svg']

#### Current Waveform

[IMAGE alt='image' src='GUID-C763E64C-6C56-4496-8CB0-2AC42C623A23-a5.svg']

<!--NI_TOPIC bundle=ni-dmm path=4082-impedance.html language=enus -->
## TOPIC 00083: Impedance

- bundle_id: `ni-dmm`
- source_path: `4082-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-impedance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Capacitive and inductive loads oppose the flow of alternating currents. This opposition is expressed as impedance at a given frequency. The effect of a real-world impedance load is observed as an attenuation of the signal and a phase shift. Because of the nature of the impedance, it is denoted as a

### Impedance

Capacitive and inductive loads oppose the flow of alternating currents. This opposition is expressed as impedance at a given frequency. The effect of a real-world impedance load is observed as an attenuation of the signal and a phase shift. Because of the nature of the impedance, it is denoted as a vector whose angle is the same as the phase angle between voltage and current, and the magnitude of the impedance is the same as the quotient between the voltage and current magnitudes, as follows:

Note

Z = V/I

Numerically, the impedance vector is represented as a complex number either in polar form (magnitude and phase) or rectangular form (real and imaginary). The following equation expresses impedance in rectangular form:

Z = R + jX

where R and X are resistance and reactance, respectively. When X = 0, the load is purely resistive; when R = 0, the load is purely reactive. For capacitors, the reactance can be expressed as follows:

X<sub>c</sub> = –1/(2[IMAGE alt='image' src='GUID-CC0315BF-B093-4875-ADCB-08A9AD050B4C-a5.gif']fC<sub>s</sub>)

For inductors, the reactance can be expressed as follows:

X<sub>L</sub> = 2[IMAGE alt='image' src='GUID-CC0315BF-B093-4875-ADCB-08A9AD050B4C-a5.gif']fL<sub>s</sub>

Parent topic:

Theoretical Background

<!--NI_TOPIC bundle=ni-dmm path=4082-inductors.html language=enus -->
## TOPIC 00084: Inductors

- bundle_id: `ni-dmm`
- source_path: `4082-inductors.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-inductors.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: An inductor is an electronic component that is capable of storing energy as current. Each inductor consists of a conductive coil that can be wrapped without a core or around a magnetic material. The permeability of the core material is a measure of the intensity of the magnetic field that can be ind

### Inductors

An inductor is an electronic component that is capable of storing energy as current. Each inductor consists of a conductive coil that can be wrapped without a core or around a magnetic material. The permeability of the core material is a measure of the intensity of the magnetic field that can be induced in it.

The electrical properties of the cores show variability with factors such as temperature, frequency, current, and so on. This variability and the mechanical construction of the inductor create a less than ideal device.

A better representation of real-world inductors is shown in the equivalent model below, which aids in understanding the different parasitic elements that are present in a real-world component. These parasitic elements impact the inductor impedance at different test frequencies.

[IMAGE alt='image' src='GUID-AB7FDAB3-EC89-4717-AAF8-69F185D09C27-a5.svg']

The series resistance, Rs, represents the resistive losses in the conductor. The parallel capacitance, Cp, is the equivalent capacitive effect between the turns of the coil, and the parallel resistance, Rp, is the sum of all losses attributable to the core material.

Air cores require many more turns in the coil to achieve high-inductance values. Thus, air cores are often impractical for applications, due to their large size and weight. Also, air cores usually have a large winding capacitance and a series resistance with a high-inductance value.

Not all parasitics affect the value of the inductor, but some parasitics are more prominent than others, depending upon the construction of the coil, the geometry of the inductor, the gauge of the wire, and the characteristics of the core. The value of the inductor and the magnitude of each type of parasitic in relation to the other types of parasitics determine the frequency response.

The geometry of some components can increase the sensitivity of the components to external factors, and this increased sensitivity can also affect the value of the inductor. Open flux inductors are more sensitive to metallic materials that are in close proximity, because such materials modify the magnetic field. Toroidal inductors keep the flux inside the core and are less sensitive to external conductors in close proximity. Refer to the following figure to view the flux associated with these types of inductors:

[IMAGE alt='image' src='GUID-EBB6108C-EBBA-4A64-9230-ACB7EFA13550-a5.svg']

In the following graph, a 5 mH air-core inductor is measured over different frequencies. The error is referenced to the measurement with a test signal of 1 V<sub>rms</sub> at 1 kHz. This type of inductor has a high degree of winding capacitance due to the size and number of turns required for its construction. Therefore, this type of inductor measures as if there were a strong variation of inductance with frequency.

[IMAGE alt='image' src='GUID-B94BF1F0-55E2-4B53-902B-B0978F42741D-a5.gif']

Some ferrite cores are expected to vary greatly with the test signal level. In the following graph, a 100 µH ferrite-core inductor is tested at different test signal levels. The error is referenced to the measurement with a test signal of 1 mA<sub>rms</sub> at 1 kHz.

[IMAGE alt='image' src='GUID-80719574-0AB4-4F99-A7DA-4079636C491B-a5.gif']

All of these factors can combine and cause inductors to have different values under varying conditions of temperature, frequency, and signal level.

Parent topic:

Theoretical Background

<!--NI_TOPIC bundle=ni-dmm path=4082-input-protection.html language=enus -->
## TOPIC 00085: Input Protection

- bundle_id: `ni-dmm`
- source_path: `4082-input-protection.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-input-protection.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The current-measuring circuit is protected with a fuse rated at 1 A 400 V. The DMM can measure up to 1 A DC or 1 A[rms] with up to 2 A peak current.If you apply higher current level to a range, the input protection circuitry of the DMM automatically engages, and you receive an overrange warning.Expo

### Input Protection

The current-measuring circuit is protected with a fuse rated at 1 A 400 V. The DMM can measure up
 to 1 A DC or 1 A<sub>rms</sub> with up to 2 A peak
 current.

If you apply higher current level to a range, the input protection circuitry of the DMM automatically engages, and you receive an overrange warning.

Exposing the current measurement connectors to voltage sources while the DC or AC current functions are selected may trigger the input protection circuitry or even blow the fuse. Do not apply more than 1 V to any of the ranges.

#### Related Topics

Fuse Replacement

Parent topic:

DC and AC Current

Related concepts:

- Fuse Replacement

<!--NI_TOPIC bundle=ni-dmm path=4082-input-protection_2.html language=enus -->
## TOPIC 00086: Input Protection

- bundle_id: `ni-dmm`
- source_path: `4082-input-protection_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-input-protection_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The current-measuring circuit is protected with a fuse rated at 1 A 400 V. The DMM can measure up to 1 A DC or 1 A[rms] with up to 2 A peak current.If you apply higher current level to a range, the input protection circuitry of the DMM automatically engages, and you receive an overrange warning.Expo

### Input Protection

The current-measuring circuit is protected with a fuse rated at 1 A 400 V. The DMM can measure up
 to 1 A DC or 1 A<sub>rms</sub> with up to 2 A peak
 current.

If you apply higher current level to a range, the input protection circuitry of the DMM automatically engages, and you receive an overrange warning.

Exposing the current measurement connectors to voltage sources while the DC or AC current functions are selected may trigger the input protection circuitry or even blow the fuse. Do not apply more than 1 V to any of the ranges.

#### Related Topics

Fuse Replacement

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=4082-input-protection_3.html language=enus -->
## TOPIC 00087: Input Protection

- bundle_id: `ni-dmm`
- source_path: `4082-input-protection_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-input-protection_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The current-measuring circuit is protected with a fuse rated at 1 A 400 V. The DMM can measure up to 1 A DC or 1 A[rms] with up to 2 A peak current.If you apply higher current level to a range, the input protection circuitry of the DMM automatically engages, and you receive an overrange warning.Expo

### Input Protection

The current-measuring circuit is protected with a fuse rated at 1 A 400 V. The DMM can measure up
 to 1 A DC or 1 A<sub>rms</sub> with up to 2 A peak
 current.

If you apply higher current level to a range, the input protection circuitry of the DMM automatically engages, and you receive an overrange warning.

Exposing the current measurement connectors to voltage sources while the DC or AC current functions are selected may trigger the input protection circuitry or even blow the fuse. Do not apply more than 1 V to any of the ranges.

#### Related Topics

Fuse Replacement

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=4082-input-protection_4.html language=enus -->
## TOPIC 00088: Input Protection

- bundle_id: `ni-dmm`
- source_path: `4082-input-protection_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-input-protection_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The current-measuring circuit is protected with a fuse rated at 1 A 400 V. The DMM can measure up to 1 A DC or 1 A[rms] with up to 2 A peak current.If you apply higher current level to a range, the input protection circuitry of the DMM automatically engages, and you receive an overrange warning.Expo

### Input Protection

The current-measuring circuit is protected with a fuse rated at 1 A 400 V. The DMM can measure up
 to 1 A DC or 1 A<sub>rms</sub> with up to 2 A peak
 current.

If you apply higher current level to a range, the input protection circuitry of the DMM automatically engages, and you receive an overrange warning.

Exposing the current measurement connectors to voltage sources while the DC or AC current functions are selected may trigger the input protection circuitry or even blow the fuse. Do not apply more than 1 V to any of the ranges.

#### Related Topics

Fuse Replacement

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=4082-measurement-considerations.html language=enus -->
## TOPIC 00089: Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `4082-measurement-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-measurement-considerations.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When taking capacitance and inductance measurements with the NI 4082, consider the following:

### Measurement Considerations

When taking capacitance and inductance measurements with the NI 4082, consider the following:

- [Frequency Effects of Real-World Components](4082-frequency-effects-of-real-world-components.html)
- [Cabling](4082-cabling.html)
- [Noise Pickup](4082-noise-pickup.html)
- [Switching Capacitance and Inductance](4082-switching-capacitance-and-inductance.html)

Parent topic:

Capacitance/Inductance

<!--NI_TOPIC bundle=ni-dmm path=4082-model.html language=enus -->
## TOPIC 00090: Model

- bundle_id: `ni-dmm`
- source_path: `4082-model.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-model.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: In real-world applications, devices are neither purely reactive nor purely resistive. However, they can be easily modeled either as a series or parallel combination of a resistive and a reactive load using the formulas above. In general, it is mathematically easier to manipulate parallel loads as ad

### Model

In real-world applications, devices are neither purely reactive nor purely resistive. However, they can be easily modeled either as a series or parallel combination of a resistive and a reactive load using the formulas above.

|  |  |
| --- | --- |

In general, it is mathematically easier to manipulate parallel loads as admittances and series loads as impedances.

|  |  |
| --- | --- |

You model the result as a series or parallel model based upon which resistance, R<sub>S</sub> or R<sub>P</sub>, is more significant. The parallel resistance (R<sub>P</sub>) is typically larger than the series resistance (R<sub>S</sub>). To measure small reactive values, such as high-valued capacitors and low-valued inductors, it is preferable to use the series model, because the series resistance is more significant than the parallel resistance. When measuring large reactive values, such as high-valued inductors or low-valued capacitors, it is preferable to use the parallel model.

| Type of Measurement | Range | Impedance | Model |
| --- | --- | --- | --- |
| C | >100 µF | <10 Ω | Series |
| C | 10 nF to 100 µF | 10 Ω to 10 kΩ | Series or parallel |
| C | <10 nF | >10 kΩ | Parallel |
| L | <1 mH | <10 Ω | Series |
| L | 1 mH to 1 H | 10 Ω to 1 kΩ | Series or parallel |
| L | >1 H | ≥1 kΩ | Parallel |
| Note Impedance values are calculated at the test frequency used on the NI 4082 at each specified range. |  |  |  |

Parent topic:

Capacitance/Inductance

<!--NI_TOPIC bundle=ni-dmm path=4082-noise-pickup.html language=enus -->
## TOPIC 00091: Noise Pickup

- bundle_id: `ni-dmm`
- source_path: `4082-noise-pickup.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-noise-pickup.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To minimize noise pickup, keep cables, the setup, and the DUT away from any electromagnetic noise sources such as motors, transformers, and cathode ray tubes (CRTs). Avoid frequency sources around 91 Hz, 1 kHz, 10 kHz, and the respective harmonics, because these frequencies are the frequencies of th

### Noise Pickup

To minimize noise pickup, keep cables, the setup, and the DUT away from any electromagnetic noise sources such as motors, transformers, and cathode ray tubes (CRTs). Avoid frequency sources around 91 Hz, 1 kHz, 10 kHz, and the respective harmonics, because these frequencies are the frequencies of the excitation currents used by the NI 4082. Use shielded cable (BNC connectors and coaxial cable are recommended) for cabling and for connecting the external conductor to the LO input of the DMM.

Note

Parent topic:

Measurement Considerations

Related concepts:

- Switching Capacitance and Inductance

<!--NI_TOPIC bundle=ni-dmm path=4082-openshort-compensation.html language=enus -->
## TOPIC 00092: OPEN/SHORT Compensation

- bundle_id: `ni-dmm`
- source_path: `4082-openshort-compensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-openshort-compensation.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: In most practical applications, the DMM is connected to the DUT with switches and/or fixtures. These switches and fixtures can introduce undesired errors into the measurement. Compensation minimizes the errors between the NI 4082 and the DUT.Offset CompensationCompensation consists of measuring the

### OPEN/SHORT Compensation

In most practical applications, the DMM is connected to the DUT with switches and/or fixtures. These switches and fixtures can introduce undesired errors into the measurement. Compensation minimizes the errors between the NI 4082 and the DUT.

#### Offset Compensation

Compensation consists of measuring the error and applying the measured error to the actual measurement to correct and minimize the errors introduced by the test system. The compensation functions must be set before taking any measurement at a specified function and range.

Any change in range or function defaults the compensation type to none. Therefore, you must calculate these values again. To provide maximum flexibility in the test system, the compensation values are returned by the API. You can manipulate, store, and load these values for high channel-count systems.

To perform OPEN compensation for capacitance and inductance measurements, complete the following steps:

1. Disconnect the DUT from the DMM at the DUT.
2. Configure the DMM for capacitance or inductance at the desired range.
3. Call niDMM Configure Cable Comp Type or niDMM_ConfigureCableCompType , and set the Cable Comp Type to CABLE COMP OPEN.
4. Set up an open condition, where nothing is connected to the test fixture. If the switching system in use has similar capacitance on different channels, you can dedicate one channel for open measurements. Cables and switches with low capacitance and low-path resistance are recommended.
5. In LabVIEW, call niDMM Perform Open Cable Comp or niDMM_PerformOpenCableComp while the input to the DMM is open. This VI or function returns two values: conductance and susceptance.
6. Pass the two values from the previous step into niDMM Configure Open Cable Comp Values or niDMM_ConfigureOpenCableCompValues . Passing these values subtracts the open measurement from all subsequent measurements.
7. Perform the desired measurement.

To perform SHORT compensation for capacitance and inductance measurements, complete the following steps:

1. Disconnect the DUT from the DMM at the DUT.
2. Configure the DMM for capacitance or inductance at the desired range.
3. Call niDMM Configure Cable Comp Type or niDMM_ConfigureCableCompType , and set the Cable Comp Type to CABLE COMP SHORT.
4. Set up a short condition at the end of the test fixture, using a low-impedance connection between the HI and LO terminals. If the switching system in use has similar inductance on different channels, you can dedicate one channel for short measurements. Cables and switches with low capacitance and low path resistance are recommended.
5. In LabVIEW, call niDMM Perform Short Cable Comp or niDMM_PerformShortCableComp while the input to the DMM is shorted. This VI or function returns two values: resistance and reactance.
6. Pass the two values from the previous step into niDMM Configure Short Cable Comp Values or niDMM_ConfigureShortCableCompValues . Passing these values subtracts the short measurement from all subsequent measurements.
7. Perform the desired measurement.

#### OPEN/SHORT Compensation

To perform OPEN and SHORT compensation for capacitance and inductance measurements, complete the following steps:

1. Disconnect the DUT from the DMM at the DUT.
2. Configure the DMM for capacitance or inductance at the desired range.
3. Call niDMM Configure Cable Comp Type or niDMM_ConfigureCableCompType , and set the Cable Comp Type to CABLE COMP OPEN AND SHORT.
4. Set up an open condition, where nothing is connected to the test fixture. If the switching system in use has similar inductance on different channels, you can dedicate one channel for open measurements. Cables and switches with low capacitance and low path resistance are recommended.
5. Call niDMM Perform Open Cable Comp or niDMM_PerformOpenCableComp while the input to the DMM is shorted. This VI or function returns two values: conductance and susceptance.
6. Pass the two values from the previous step into niDMM Configure Open Cable Comp Values or niDMM_ConfigureOpenCableCompValues .
7. Set up a short condition at the end of the test fixture, using a low-impedance connection between the HI and LO terminals. If the switching system in use has similar inductance on different channels, you can dedicate one channel for short measurements. Cables and switches with low capacitance and low path resistance are recommended.
8. Call niDMM Perform Short Cable Comp or niDMM_PerformShortCableComp while the input to the DMM is shorted. This VI or function returns two values: resistance and reactance.
9. Pass the two values from the previous step into niDMM Configure Short Cable Comp Values or niDMM_ConfigureShortCableCompValues .
10. NI-DMM takes the four values measured on open and short conditions to compensate all subsequent measurements.
11. Perform the desired measurement.

Note

Parent topic:

Capacitance/Inductance

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=4082-switching-capacitance-and-inductance.html language=enus -->
## TOPIC 00093: Switching Capacitance and Inductance

- bundle_id: `ni-dmm`
- source_path: `4082-switching-capacitance-and-inductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-switching-capacitance-and-inductance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4082 can be integrated as part of an ATE system that includes switches, cables, and other custom test fixtures. The quality of the measurement is directly related to the quality of the system setup.For information about the various NI switch modules that are available, refer to the NI Switche

### Switching Capacitance and Inductance

The NI 4082 can be integrated as part of an ATE system that includes switches, cables, and other custom test fixtures. The quality of the measurement is directly related to the quality of the system setup.

For information about the various NI switch modules that are available, refer to the NI
 Switches Help at either of the following locations:

- Start»Programs»National Instruments»NI-SWITCH»Documentation»NI Switches Help (if you have installed NI-SWITCH)
- ni.com/manuals (if you have not installed NI-SWITCH)

#### Measurement
 Considerations

Inductors and capacitors store energy. Inductors store
 currents that can damage other devices connected to them when disconnected.
 Capacitors store energy as voltage that can be harmful to some equipment or to the
 capacitors themselves.

For applications that require scanning through
 different types of measurements, NI recommends taking notice when switching channels
 that use built-in current excitation. The measurement modes in the NI 4082 that use
 current excitation are as follow:

| Type of Excitation Signal | Function Mode |
| --- | --- |
| DC Current | ResistanceRefer to the Resistance section for more information on the test current. |
| DiodeRefer to the Diode section for more information on the test current. |  |
| AC Current | CapacitanceRefer to the Capacitance and Inductance Measurement Considerations section for more information on the test signal for capacitance measurements. |
| InductanceRefer to the Capacitance and Inductance Measurement Considerations section for more information on the test signal for inductance measurements. |  |

After a measurement is completed, the front-end configuration remains
 unchanged until the next type of measurement is initiated or the DMM is reset.
 Therefore, after taking a resistance, diode, capacitance, or inductance measurement,
 the current excitation remains on until niDMM Initiate (after configuring the
 device) or niDMM Reset is called. The existing excitation current could lead to an
 unsafe condition for the setup, the device under test, or the operator.

To
 avoid such situations, review the channel assignments and configuration of your
 system, taking into account the following considerations:

- After taking a resistance measurement, turn off the DC current before switching
 to a channel for a capacitance or inductance measurement. If the resistance or
 diode DC current excitation is applied to a capacitor, the voltage can increase
 to 12 V. If this same current is switched into an inductor, you could see a
 short voltage spike of up to 12 V. You should turn off the DC current by
 resetting the device or initiating the DMM for the capacitance or inductance
 measurement before switching to the channel.
- When you use the appropriate range for capacitance measurements, the voltage
 across the capacitor does not exceed 1 V. If you have a capacitor with a value
 lower than 5% of the range, you observe an underrange condition
 and can apply a test voltage exceeding the 1 V limit (maximum of 12 V). If the
 capacitor is not built to tolerate this voltage level, you could reduce its
 life, shift its value, or damage it permanently (less likely). When performing
 in-circuit testing, you could inadvertently bias other components in the
 circuit, such as transistors or diodes.
- After you take an inductance measurement or a resistance measurement on an
 inductive load, the excitation current remains on. If the channel is opened
 immediately after you take the measurement, a voltage develops across the open
 circuit, because the inductor is still charged with current. This charge could
 produce a voltage across the open circuit that could shorten the life of the
 relays in the switch. To prevent damage to the setup, multiplexer, test fixture,
 or device under test, NI recommends performing one of the following actions
 before switching to the successive measurement:
  - If the next measurement uses a function mode that requires a current
 excitation signal, turn off the current source by resetting the device
 immediately after taking the inductance measurement before breaking the
 channel.
  - If the next measurement does not use a function mode
 that requires a current excitation signal (such as DC voltage), you can
 either reset the device or configure and initiate the next measurement
 before breaking the channel.

#### Recommendations for System Integration

To integrate the NI 4082 into an ATE system, take the following steps to maximize your success:

- Keep cables as short as possible. Longer leads are more likely to introduce noise or errors into the system.
- Use twisted pairs or coaxial cable to reduce noise pickup.
- Use strain relief ties to maintain a consistent mechanical configuration.
- Minimize contact resistance everywhere a connection is present. Contacts should be firm and must be kept clean and free from oxides.
- Verify that the contact electrodes can be opened or shorted so that it is possible to perform OPEN/SHORT compensation.
- Minimize the variation of impedance between channels. If two channels have very similar impedance (for example, same cable type and length, and same type of switch path), one channel can perform the OPEN measurement and the other channel can perform the SHORT measurement. This multi-channel compensation is not as accurate as per-channel compensation, but multi-channel compensation can reduce test time and simplify the OPEN/SHORT compensation procedure for the other measurements. The impedance levels between all channels are more likely to be similar if all channels share the majority of the measurement path, as shown below:

Note

Parent topic:

Measurement Considerations

Related concepts:

- Overrange/Underrange
- OPEN/SHORT Compensation
- Resistance
- Diode
- Measurement Considerations
- Using Switches

Related information:

- niDMM Initiate
- niDMM Reset

<!--NI_TOPIC bundle=ni-dmm path=4082-test-signal.html language=enus -->
## TOPIC 00094: Test Signal

- bundle_id: `ni-dmm`
- source_path: `4082-test-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-test-signal.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4082 uses an AC current source as excitation for capacitance and inductance measurements. The current waveform is a very stable, harmonically limited square wave. The measurement method extracts multiple-tone information contained in the test signal to find the capacitance or inductance of th

### Test Signal

The NI 4082 uses an AC current source as excitation for capacitance and inductance measurements. The current waveform is a very stable, harmonically limited square wave. The measurement method extracts multiple-tone information contained in the test signal to find the capacitance or inductance of the device under test. The frequency and level of the test signal and the tones extracted from it are shown in the following tables:

| Capacitance |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Range | Fundamental | Third Harmonic | Effective Test Signal |  |  |  |
| Frequency | Current | Frequency | Current | Frequency | Current |  |
| 300 pF | 1 kHz | 0.5 µA | 3 kHz | 0.16 µA | 3 kHz | 0.16 µA |
| 1 nF | 1 kHz | 1 µA | 3 kHz | 0.33 µA | 3 kHz | 0.33 µA |
| 10 nF |  |  |  |  |  |  |
| 100 nF | 1 kHz | 10 µA | 3 kHz | 3.3 µA | 3 kHz | 3.3 µA |
| 1 µF | 1 kHz | 100 µA | 3 kHz | 33 µA | 1 kHz | 100 µA |
| 10 µF | 1 kHz | 1 mA | 3 kHz | 330 µA | 1 kHz | 1 mA |
| 100 µF | 91 Hz | 1 mA | 273 Hz | 330 µA | 91 Hz | 1 mA |
| 1,000 µF |  |  |  |  |  |  |
| 10,000 µF |  |  |  |  |  |  |
| Inductance |  |  |  |  |  |  |
| Range | Fundamental | Third Harmonic | Effective Test Signal |  |  |  |
| Frequency | Current | Frequency | Current | Frequency | Current |  |
| 10 µH | 10 kHz | 1 mA | 30 kHz | 330 µA | 30 kHz | 330 µA |
| 100 µH |  |  |  |  |  |  |
| 1 mH | 1 kHz | 1 mA | 3 kHz | 330 µA | 3 kHz | 330 µA |
| 10 mH | 1 kHz | 10 µA | 3 kHz | 3.3 µA | 3 kHz | 3.3 µA |
| 100 mH | 91 Hz | 100 µA | 273 Hz | 33 µA | 273 Hz | 33 µA |
| 1 H | 91 Hz | 10 µA | 273 Hz | 3.3 µA | 273 Hz | 3.3 µA |
| 5 H | 91 Hz | 1 µA | 273 Hz | 0.33 µA | 273 Hz | 0.33 µA |

The digitizer measures the DUT impedance at two frequencies (tones). From these two measurements, the losses are calculated (front-end, cabling, and DUT). Using the calculated losses, the software computes the capacitance or inductance at one of the two frequencies (effective frequency).

The effective test signal is included as a reference. It is the signal that would yield a comparable capacitance or inductance value if measured with the single tone measurement technique.

Parent topic:

Capacitance/Inductance

<!--NI_TOPIC bundle=ni-dmm path=4082-theoretical-background.html language=enus -->
## TOPIC 00095: Theoretical Background

- bundle_id: `ni-dmm`
- source_path: `4082-theoretical-background.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/4082-theoretical-background.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following topics include background information about capacitance and inductance measurements:

### Theoretical Background

The following topics include background information about capacitance and inductance measurements:

- [Impedance](4082-impedance.html)
- [Admittance](4082-admittance.html)
- [Capacitors](4082-capacitors.html)
- [Inductors](4082-inductors.html)

Parent topic:

Capacitance/Inductance

<!--NI_TOPIC bundle=ni-dmm path=408x-aperture-time.html language=enus -->
## TOPIC 00096: Aperture Time

- bundle_id: `ni-dmm`
- source_path: `408x-aperture-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-aperture-time.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify

### Aperture Time

Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify aperture time either in seconds or in power line cycles (PLCs).

Refer to the table in the DMM Measurement Defaults section for default conditions for aperture, as well as other conditions related to the measurement cycle.

By default, the aperture time for a measurement is chosen by the driver based on the configured measurement and resolution. These values are chosen to ensure accuracy for high-resolution measurements while not sacrificing performance at lower resolutions. For AC, the aperture is a function of minFreq. MinFreq, or minimum frequency, is a user-programmable parameter with a default value of 20 Hz.

For settling time defaults, refer to Settling Time.

#### Number of Averages for DC
 Measurements

This function is specific for high-resolution DC
 measurements.

Note

If your application requires
 a long aperture time (>100 ms) it is recommended that Auto Zero is enabled. The
 offset present may actually drift during the measurement, so that the stored Auto
 Zero value is invalid by the time the measurement completes. To compensate for this
 drift, several shorter measurements can be taken with a new Auto Zero offset applied
 to each measurement. These measurements can then be averaged together by the
 DMM so that a single value is returned.

To configure an averaged measurement,
 set the Number of Averages property. For example, if you desire a 500 ms measurement
 aperture, you can set the aperture to 50 ms and set Number of Averages to 10. The
 DMM will take ten 50 ms measurements each with Auto Zero and return a
 single measurement.

Parent topic:

DMM Measurement Cycle

Related concepts:

- DMM Measurement Defaults
- Settling Time
- Configuring Measurement Timing
- Auto Zero

Related information:

- Number of LC Measurements To Average

<!--NI_TOPIC bundle=ni-dmm path=408x-aperture-time_2.html language=enus -->
## TOPIC 00097: Aperture Time

- bundle_id: `ni-dmm`
- source_path: `408x-aperture-time_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-aperture-time_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify

### Aperture Time

Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify aperture time either in seconds or in power line cycles (PLCs).

Refer to the table in the DMM Measurement Defaults section for default conditions for aperture, as well as other conditions related to the measurement cycle.

By default, the aperture time for a measurement is chosen by the driver based on the configured measurement and resolution. These values are chosen to ensure accuracy for high-resolution measurements while not sacrificing performance at lower resolutions. For AC, the aperture is a function of minFreq. MinFreq, or minimum frequency, is a user-programmable parameter with a default value of 20 Hz.

For settling time defaults, refer to Settling Time.

#### Number of Averages for DC
 Measurements

This function is specific for high-resolution DC
 measurements.

Note

If your application requires
 a long aperture time (>100 ms) it is recommended that Auto Zero is enabled. The
 offset present may actually drift during the measurement, so that the stored Auto
 Zero value is invalid by the time the measurement completes. To compensate for this
 drift, several shorter measurements can be taken with a new Auto Zero offset applied
 to each measurement. These measurements can then be averaged together by the
 DMM so that a single value is returned.

To configure an averaged measurement,
 set the Number of Averages property. For example, if you desire a 500 ms measurement
 aperture, you can set the aperture to 50 ms and set Number of Averages to 10. The
 DMM will take ten 50 ms measurements each with Auto Zero and return a
 single measurement.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=408x-aperture-time_3.html language=enus -->
## TOPIC 00098: Aperture Time

- bundle_id: `ni-dmm`
- source_path: `408x-aperture-time_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-aperture-time_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify

### Aperture Time

Aperture time is the period during which the ADC is reading the input signal. Resolution, measurement speed, and frequency rejection are functions of the aperture time. The larger the aperture time, the better the resolution. Select short aperture times for faster measurement speed. You can specify aperture time either in seconds or in power line cycles (PLCs).

Refer to the table in the DMM Measurement Defaults section for default conditions for aperture, as well as other conditions related to the measurement cycle.

By default, the aperture time for a measurement is chosen by the driver based on the configured measurement and resolution. These values are chosen to ensure accuracy for high-resolution measurements while not sacrificing performance at lower resolutions. For AC, the aperture is a function of minFreq. MinFreq, or minimum frequency, is a user-programmable parameter with a default value of 20 Hz.

For settling time defaults, refer to Settling Time.

#### Number of Averages for DC
 Measurements

This function is specific for high-resolution DC
 measurements.

Note

If your application requires
 a long aperture time (>100 ms) it is recommended that Auto Zero is enabled. The
 offset present may actually drift during the measurement, so that the stored Auto
 Zero value is invalid by the time the measurement completes. To compensate for this
 drift, several shorter measurements can be taken with a new Auto Zero offset applied
 to each measurement. These measurements can then be averaged together by the
 DMM so that a single value is returned.

To configure an averaged measurement,
 set the Number of Averages property. For example, if you desire a 500 ms measurement
 aperture, you can set the aperture to 50 ms and set Number of Averages to 10. The
 DMM will take ten 50 ms measurements each with Auto Zero and return a
 single measurement.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=408x-dmm-measurement-cycle.html language=enus -->
## TOPIC 00099: DMM Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `408x-dmm-measurement-cycle.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-dmm-measurement-cycle.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4080/4081/4082 measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture tim

### DMM Measurement Cycle

The NI 4080/4081/4082 measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture time. Generally the settle and aperture times are selected by the device driver based on the specified resolution. Settling time and aperture can be set using the niDMM Property Node. Refer to Configuring Measurement Timing for more information.

[IMAGE alt='image' src='GUID-C081233B-F9E9-459F-B325-4DC1E226E115-a5.svg']

The internal switch time is required to configure the analog circuitry of the NI 4080/4081/4082 for the next measurement, and default switch settling times precede both ADC calibration and Auto Zero. All of these times are not user programmable.

During resistance measurements, the signal is measured with an applied current source. When Offset Compensated Ohms is enabled, a settle phase and current source OFF measurement phase occurs in place of the Auto Zero phase depicted above.

The AC measurement cycle contains the same phases, but the minimum signal measurement time is based on the minimum frequency required of the measurement. For example, for a minimum frequency of 50 Hz, an aperture of 4x the period of the 50 Hz signal is required, or in this example, 80 ms.

(NI 4082 only) For capacitance and inductance measurements, the measurement cycle consists of applying a current source and measuring the response of its harmonics. Because the harmonics are a set frequency, the aperture time is fixed. See DMM Measurement Defaults and Capacitance/Inductance for more information.

When Auto Range is selected, the Auto Range measurement phase occurs before the Auto Zero and signal measurement phases. After the correct range is identified, the Auto Zero and signal measurements use the selected range.

Parent topic:

DMM Measurements

Related concepts:

- Configuring Measurement Timing
- DMM Measurement Defaults
- Capacitance/Inductance

Related information:

- niDMM Property Node

<!--NI_TOPIC bundle=ni-dmm path=408x-dmm-measurement-cycle_2.html language=enus -->
## TOPIC 00100: DMM Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `408x-dmm-measurement-cycle_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-dmm-measurement-cycle_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4080/4081/4082 measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture tim

### DMM Measurement Cycle

The NI 4080/4081/4082 measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture time. Generally the settle and aperture times are selected by the device driver based on the specified resolution. Settling time and aperture can be set using the niDMM Property Node. Refer to Configuring Measurement Timing for more information.

[IMAGE alt='image' src='GUID-C081233B-F9E9-459F-B325-4DC1E226E115-a5.svg']

The internal switch time is required to configure the analog circuitry of the NI 4080/4081/4082 for the next measurement, and default switch settling times precede both ADC calibration and Auto Zero. All of these times are not user programmable.

During resistance measurements, the signal is measured with an applied current source. When Offset Compensated Ohms is enabled, a settle phase and current source OFF measurement phase occurs in place of the Auto Zero phase depicted above.

The AC measurement cycle contains the same phases, but the minimum signal measurement time is based on the minimum frequency required of the measurement. For example, for a minimum frequency of 50 Hz, an aperture of 4x the period of the 50 Hz signal is required, or in this example, 80 ms.

(NI 4082 only) For capacitance and inductance measurements, the measurement cycle consists of applying a current source and measuring the response of its harmonics. Because the harmonics are a set frequency, the aperture time is fixed. See DMM Measurement Defaults and Capacitance/Inductance for more information.

When Auto Range is selected, the Auto Range measurement phase occurs before the Auto Zero and signal measurement phases. After the correct range is identified, the Auto Zero and signal measurements use the selected range.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=408x-dmm-measurement-cycle_3.html language=enus -->
## TOPIC 00101: DMM Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `408x-dmm-measurement-cycle_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-dmm-measurement-cycle_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4080/4081/4082 measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture tim

### DMM Measurement Cycle

The NI 4080/4081/4082 measurement cycle is made up of several measurement phases: switch time, settling time, signal measurement phase, Auto Zero, and ADC calibration. Refer to the figure below for relative timing of these phases. The length of the signal measurement phase is set by the aperture time. Generally the settle and aperture times are selected by the device driver based on the specified resolution. Settling time and aperture can be set using the niDMM Property Node. Refer to Configuring Measurement Timing for more information.

[IMAGE alt='image' src='GUID-C081233B-F9E9-459F-B325-4DC1E226E115-a5.svg']

The internal switch time is required to configure the analog circuitry of the NI 4080/4081/4082 for the next measurement, and default switch settling times precede both ADC calibration and Auto Zero. All of these times are not user programmable.

During resistance measurements, the signal is measured with an applied current source. When Offset Compensated Ohms is enabled, a settle phase and current source OFF measurement phase occurs in place of the Auto Zero phase depicted above.

The AC measurement cycle contains the same phases, but the minimum signal measurement time is based on the minimum frequency required of the measurement. For example, for a minimum frequency of 50 Hz, an aperture of 4x the period of the 50 Hz signal is required, or in this example, 80 ms.

(NI 4082 only) For capacitance and inductance measurements, the measurement cycle consists of applying a current source and measuring the response of its harmonics. Because the harmonics are a set frequency, the aperture time is fixed. See DMM Measurement Defaults and Capacitance/Inductance for more information.

When Auto Range is selected, the Auto Range measurement phase occurs before the Auto Zero and signal measurement phases. After the correct range is identified, the Auto Zero and signal measurements use the selected range.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=408x-dmm-measurement-defaults.html language=enus -->
## TOPIC 00102: DMM Measurement Defaults

- bundle_id: `ni-dmm`
- source_path: `408x-dmm-measurement-defaults.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-dmm-measurement-defaults.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default measurement settings for the NI 4080/4081/4082. Function Aperture Auto Zero Offset Compensated Ohms ADC Calibration DC Noise Rejection Number of Averages DCV 7½ digits 100 ms ON N/A ON High-Order 4 DCV/DCI 6½ digits 100 ms ON N/A ON High-Order 1 DCV/DCI 5½ digit

### DMM Measurement Defaults

The following table lists the default measurement settings for the NI 4080/4081/4082.

| Function | Aperture | Auto Zero | Offset Compensated Ohms | ADC Calibration | DC Noise Rejection | Number of Averages |
| --- | --- | --- | --- | --- | --- | --- |
| DCV 7½ digits | 100 ms | ON | N/A | ON | High-Order | 4 |
| DCV/DCI 6½ digits | 100 ms | ON | N/A | ON | High-Order | 1 |
| DCV/DCI 5½ digits | 500 µs | ONCE | N/A | OFF | Second-Order | 1 |
| DCV/DCI 4½1 digits | 20 µs | ONCE | N/A | OFF | Second-Order | 1 |
| Resistance 7½ digits | 100 ms | ON | OFF | ON | High-Order | 4 |
| Resistance 6½ digits | 100 ms | ON | OFF | ON | High-Order | 1 |
| Resistance 5½ digits | 500 µs | ONCE | OFF | OFF | Second-Order | 1 |
| Resistance 4½ digits1 | 20 µs | ONCE | OFF | OFF | Second-Order | 1 |
| ACV/ACI 6½ digits | Maximum of 4/minFreq or 100 ms | OFF | N/A | N/A | N/A | 1 |
| ACV/ACI 5½ digits | Maximum of 4/minFreq or 500 µs | OFF | N/A | N/A | N/A | 1 |
| ACV/ACI 4½ digits1 | Maximum of 4/minFreq or 20 µs | OFF | N/A | N/A | N/A | 1 |
| Frequency | 2/(minFreq) | N/A | N/A | N/A | N/A | 1 |
| Period | 2 x (the maximum period) | N/A | N/A | N/A | N/A | 1 |
| Capacitance and Inductance | Inductance (only) at 10 kHz = 13.65 ms Inductance and capacitance at 1 kHz = 31.29 ms Inductance and capacitance at 91 Hz = 270.22 ms | N/A | N/A | N/A | N/A | 1 |
| 1Settings for 3½ digits are equivalent to 4½ digits. |  |  |  |  |  |  |

By default, the Aperture time, Auto Zero, ADC Calibration, DC Noise Rejection settings for a measurement are chosen by the driver based on the configured measurement and resolution. These values are chosen to ensure accuracy for 6½–digit or 7½–digit measurements while not sacrificing performance at lower resolutions. For more information on a particular attribute, including how to configure a non-default setting, refer to the Features section.

To adjust the default aperture time, refer to the Configuring Measurement Timing section.

#### Default Settling Times

| Function | Settling Time |
| --- | --- |
| DC V (100 mV–10 V) | 1 ms |
| DC V ≥ 100 V | 2 ms |
| DCV Auto Range | 2 ms |
| Resistance ≤1 kΩ | 1 ms |
| Resistance 10 kΩ | 5 ms |
| Resistance 100 kΩ | 25 ms |
| Resistance 1 MΩ | 100 ms |
| Resistance ≥ 10 MΩ | 250 ms |
| Resistance Auto Range | 50 ms |
| AC V DC coupled | 3 µs |
| AC V AC coupled | 1 s |
| Frequency/Period | 500 ms |
| DC I | 100 µs |
| AC I | 3 µs |
| Diode | 10 ms |
| Inductance (NI 4082 only) | 3 µs |
| Capacitance (NI 4082 only) | 3 µs |

To adjust the default settling times, refer to the Configuring Measurement
 Timing section within the Programming with NI-DMM section.

Parent topic:

DMM Measurements

Related concepts:

- Configuring Auto Zero
- Configuring ADC Calibration
- Configuring Measurement Timing
- Features
- Selecting DC Noise Rejection

<!--NI_TOPIC bundle=ni-dmm path=408x-dmm-measurement-defaults_2.html language=enus -->
## TOPIC 00103: DMM Measurement Defaults

- bundle_id: `ni-dmm`
- source_path: `408x-dmm-measurement-defaults_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-dmm-measurement-defaults_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default measurement settings for the NI 4080/4081/4082. Function Aperture Auto Zero Offset Compensated Ohms ADC Calibration DC Noise Rejection Number of Averages DCV 7½ digits 100 ms ON N/A ON High-Order 4 DCV/DCI 6½ digits 100 ms ON N/A ON High-Order 1 DCV/DCI 5½ digit

### DMM Measurement Defaults

The following table lists the default measurement settings for the NI 4080/4081/4082.

| Function | Aperture | Auto Zero | Offset Compensated Ohms | ADC Calibration | DC Noise Rejection | Number of Averages |
| --- | --- | --- | --- | --- | --- | --- |
| DCV 7½ digits | 100 ms | ON | N/A | ON | High-Order | 4 |
| DCV/DCI 6½ digits | 100 ms | ON | N/A | ON | High-Order | 1 |
| DCV/DCI 5½ digits | 500 µs | ONCE | N/A | OFF | Second-Order | 1 |
| DCV/DCI 4½1 digits | 20 µs | ONCE | N/A | OFF | Second-Order | 1 |
| Resistance 7½ digits | 100 ms | ON | OFF | ON | High-Order | 4 |
| Resistance 6½ digits | 100 ms | ON | OFF | ON | High-Order | 1 |
| Resistance 5½ digits | 500 µs | ONCE | OFF | OFF | Second-Order | 1 |
| Resistance 4½ digits1 | 20 µs | ONCE | OFF | OFF | Second-Order | 1 |
| ACV/ACI 6½ digits | Maximum of 4/minFreq or 100 ms | OFF | N/A | N/A | N/A | 1 |
| ACV/ACI 5½ digits | Maximum of 4/minFreq or 500 µs | OFF | N/A | N/A | N/A | 1 |
| ACV/ACI 4½ digits1 | Maximum of 4/minFreq or 20 µs | OFF | N/A | N/A | N/A | 1 |
| Frequency | 2/(minFreq) | N/A | N/A | N/A | N/A | 1 |
| Period | 2 x (the maximum period) | N/A | N/A | N/A | N/A | 1 |
| Capacitance and Inductance | Inductance (only) at 10 kHz = 13.65 ms Inductance and capacitance at 1 kHz = 31.29 ms Inductance and capacitance at 91 Hz = 270.22 ms | N/A | N/A | N/A | N/A | 1 |
| 1Settings for 3½ digits are equivalent to 4½ digits. |  |  |  |  |  |  |

By default, the Aperture time, Auto Zero, ADC Calibration, DC Noise Rejection settings for a measurement are chosen by the driver based on the configured measurement and resolution. These values are chosen to ensure accuracy for 6½–digit or 7½–digit measurements while not sacrificing performance at lower resolutions. For more information on a particular attribute, including how to configure a non-default setting, refer to the Features section.

To adjust the default aperture time, refer to the Configuring Measurement Timing section.

#### Default Settling Times

| Function | Settling Time |
| --- | --- |
| DC V (100 mV–10 V) | 1 ms |
| DC V ≥ 100 V | 2 ms |
| DCV Auto Range | 2 ms |
| Resistance ≤1 kΩ | 1 ms |
| Resistance 10 kΩ | 5 ms |
| Resistance 100 kΩ | 25 ms |
| Resistance 1 MΩ | 100 ms |
| Resistance ≥ 10 MΩ | 250 ms |
| Resistance Auto Range | 50 ms |
| AC V DC coupled | 3 µs |
| AC V AC coupled | 1 s |
| Frequency/Period | 500 ms |
| DC I | 100 µs |
| AC I | 3 µs |
| Diode | 10 ms |
| Inductance (NI 4082 only) | 3 µs |
| Capacitance (NI 4082 only) | 3 µs |

To adjust the default settling times, refer to the Configuring Measurement
 Timing section within the Programming with NI-DMM section.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=408x-dmm-measurement-defaults_3.html language=enus -->
## TOPIC 00104: DMM Measurement Defaults

- bundle_id: `ni-dmm`
- source_path: `408x-dmm-measurement-defaults_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-dmm-measurement-defaults_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default measurement settings for the NI 4080/4081/4082. Function Aperture Auto Zero Offset Compensated Ohms ADC Calibration DC Noise Rejection Number of Averages DCV 7½ digits 100 ms ON N/A ON High-Order 4 DCV/DCI 6½ digits 100 ms ON N/A ON High-Order 1 DCV/DCI 5½ digit

### DMM Measurement Defaults

The following table lists the default measurement settings for the NI 4080/4081/4082.

| Function | Aperture | Auto Zero | Offset Compensated Ohms | ADC Calibration | DC Noise Rejection | Number of Averages |
| --- | --- | --- | --- | --- | --- | --- |
| DCV 7½ digits | 100 ms | ON | N/A | ON | High-Order | 4 |
| DCV/DCI 6½ digits | 100 ms | ON | N/A | ON | High-Order | 1 |
| DCV/DCI 5½ digits | 500 µs | ONCE | N/A | OFF | Second-Order | 1 |
| DCV/DCI 4½1 digits | 20 µs | ONCE | N/A | OFF | Second-Order | 1 |
| Resistance 7½ digits | 100 ms | ON | OFF | ON | High-Order | 4 |
| Resistance 6½ digits | 100 ms | ON | OFF | ON | High-Order | 1 |
| Resistance 5½ digits | 500 µs | ONCE | OFF | OFF | Second-Order | 1 |
| Resistance 4½ digits1 | 20 µs | ONCE | OFF | OFF | Second-Order | 1 |
| ACV/ACI 6½ digits | Maximum of 4/minFreq or 100 ms | OFF | N/A | N/A | N/A | 1 |
| ACV/ACI 5½ digits | Maximum of 4/minFreq or 500 µs | OFF | N/A | N/A | N/A | 1 |
| ACV/ACI 4½ digits1 | Maximum of 4/minFreq or 20 µs | OFF | N/A | N/A | N/A | 1 |
| Frequency | 2/(minFreq) | N/A | N/A | N/A | N/A | 1 |
| Period | 2 x (the maximum period) | N/A | N/A | N/A | N/A | 1 |
| Capacitance and Inductance | Inductance (only) at 10 kHz = 13.65 ms Inductance and capacitance at 1 kHz = 31.29 ms Inductance and capacitance at 91 Hz = 270.22 ms | N/A | N/A | N/A | N/A | 1 |
| 1Settings for 3½ digits are equivalent to 4½ digits. |  |  |  |  |  |  |

By default, the Aperture time, Auto Zero, ADC Calibration, DC Noise Rejection settings for a measurement are chosen by the driver based on the configured measurement and resolution. These values are chosen to ensure accuracy for 6½–digit or 7½–digit measurements while not sacrificing performance at lower resolutions. For more information on a particular attribute, including how to configure a non-default setting, refer to the Features section.

To adjust the default aperture time, refer to the Configuring Measurement Timing section.

#### Default Settling Times

| Function | Settling Time |
| --- | --- |
| DC V (100 mV–10 V) | 1 ms |
| DC V ≥ 100 V | 2 ms |
| DCV Auto Range | 2 ms |
| Resistance ≤1 kΩ | 1 ms |
| Resistance 10 kΩ | 5 ms |
| Resistance 100 kΩ | 25 ms |
| Resistance 1 MΩ | 100 ms |
| Resistance ≥ 10 MΩ | 250 ms |
| Resistance Auto Range | 50 ms |
| AC V DC coupled | 3 µs |
| AC V AC coupled | 1 s |
| Frequency/Period | 500 ms |
| DC I | 100 µs |
| AC I | 3 µs |
| Diode | 10 ms |
| Inductance (NI 4082 only) | 3 µs |
| Capacitance (NI 4082 only) | 3 µs |

To adjust the default settling times, refer to the Configuring Measurement
 Timing section within the Programming with NI-DMM section.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=408x-dmm-measurements.html language=enus -->
## TOPIC 00105: DMM Measurements

- bundle_id: `ni-dmm`
- source_path: `408x-dmm-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-dmm-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections cover optimizing your measurements on the NI 4080/4081/4082.

### DMM Measurements

The following sections cover optimizing your measurements on the NI 4080/4081/4082.

Parent topic:

NI PXIe-4082

<!--NI_TOPIC bundle=ni-dmm path=408x-dmm-measurements_2.html language=enus -->
## TOPIC 00106: DMM Measurements

- bundle_id: `ni-dmm`
- source_path: `408x-dmm-measurements_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-dmm-measurements_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections cover optimizing your measurements on the NI 4080/4081/4082.

### DMM Measurements

The following sections cover optimizing your measurements on the NI 4080/4081/4082.

- [DMM Measurement Cycle](408x-dmm-measurement-cycle_2.html)
- [DMM Measurement Defaults](408x-dmm-measurement-defaults_2.html)
- [DC Voltage](dc-voltage_2.html)
- [AC Voltage](ac-voltage_2.html)
- [DC and AC Current](4081-dc-and-ac-current.html)
- [Resistance](resistance_2.html)
- [Frequency/Period](408x-frequencyperiod_2.html)
- [Diode](diode_2.html)
- [Temperature Measurements](temperature-measurements_2.html)

Parent topic:

NI 4081

<!--NI_TOPIC bundle=ni-dmm path=408x-dmm-measurements_3.html language=enus -->
## TOPIC 00107: DMM Measurements

- bundle_id: `ni-dmm`
- source_path: `408x-dmm-measurements_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-dmm-measurements_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections cover optimizing your measurements on the NI 4080/4081/4082.

### DMM Measurements

The following sections cover optimizing your measurements on the NI 4080/4081/4082.

Parent topic:

NI PXIe-4080

<!--NI_TOPIC bundle=ni-dmm path=408x-frequencyperiod.html language=enus -->
## TOPIC 00108: Frequency/Period

- bundle_id: `ni-dmm`
- source_path: `408x-frequencyperiod.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-frequencyperiod.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to hundreds of volts.The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 108 MHz timebase.Frequency (Hz) = timeb

### Frequency/Period

The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to hundreds of volts.

The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 108 MHz timebase.

Frequency (Hz) = timebase (Hz) x Ns / Nt

Period = 1 /Frequency (Hz)

where

timebase = 108 x 10<sup>6</sup> Hz

Ns = number of rising edges detected in the measurement window

Nt = number of timebase clock periods between the first and the last rising edge

To measure a signal of frequency f in Hz, the DMM needs a minimum aperture of (2/f) s. In other words, the DMM requires an aperture that is greater than or equal to at least two periods of the input signal. Therefore, as a general rule, the aperture should be set to a value greater than or equal to 110% of (2/f) s. The resolution of the frequency/period measurement can be improved by increasing the aperture time enough to allow for an integer increase in the number of periods.

Another way to measure frequency is to perform waveform acquisitions and then to use the signal processing functions in the ADE to extract the frequency.

Parent topic:

DMM Measurements

Related concepts:

- Configuring Frequency Measurements
- Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=408x-frequencyperiod_2.html language=enus -->
## TOPIC 00109: Frequency/Period

- bundle_id: `ni-dmm`
- source_path: `408x-frequencyperiod_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-frequencyperiod_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to hundreds of volts.The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 108 MHz timebase.Frequency (Hz) = timeb

### Frequency/Period

The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to hundreds of volts.

The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 108 MHz timebase.

Frequency (Hz) = timebase (Hz) x Ns / Nt

Period = 1 /Frequency (Hz)

where

timebase = 108 x 10<sup>6</sup> Hz

Ns = number of rising edges detected in the measurement window

Nt = number of timebase clock periods between the first and the last rising edge

To measure a signal of frequency f in Hz, the DMM needs a minimum aperture of (2/f) s. In other words, the DMM requires an aperture that is greater than or equal to at least two periods of the input signal. Therefore, as a general rule, the aperture should be set to a value greater than or equal to 110% of (2/f) s. The resolution of the frequency/period measurement can be improved by increasing the aperture time enough to allow for an integer increase in the number of periods.

Another way to measure frequency is to perform waveform acquisitions and then to use the signal processing functions in the ADE to extract the frequency.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=408x-frequencyperiod_3.html language=enus -->
## TOPIC 00110: Frequency/Period

- bundle_id: `ni-dmm`
- source_path: `408x-frequencyperiod_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-frequencyperiod_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to hundreds of volts.The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 108 MHz timebase.Frequency (Hz) = timeb

### Frequency/Period

The DMM can measure periodic signal frequencies, up to 500 kHz, from a variety of signal sources, ranging from millivolts to hundreds of volts.

The DMM measures frequency by counting the number of zero-crossing rising edges of the input signal, using an onboard 108 MHz timebase.

Frequency (Hz) = timebase (Hz) x Ns / Nt

Period = 1 /Frequency (Hz)

where

timebase = 108 x 10<sup>6</sup> Hz

Ns = number of rising edges detected in the measurement window

Nt = number of timebase clock periods between the first and the last rising edge

To measure a signal of frequency f in Hz, the DMM needs a minimum aperture of (2/f) s. In other words, the DMM requires an aperture that is greater than or equal to at least two periods of the input signal. Therefore, as a general rule, the aperture should be set to a value greater than or equal to 110% of (2/f) s. The resolution of the frequency/period measurement can be improved by increasing the aperture time enough to allow for an integer increase in the number of periods.

Another way to measure frequency is to perform waveform acquisitions and then to use the signal processing functions in the ADE to extract the frequency.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=408x-overrangeunderrange.html language=enus -->
## TOPIC 00111: Overrange/Underrange

- bundle_id: `ni-dmm`
- source_path: `408x-overrangeunderrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-overrangeunderrange.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the overrange and/or underrange conditions, as applicable, for the PXIe‑4080/4081/4082. Function Overrange^1 Underrange DC Functions:Voltage, Current, Resistance, and Diode Above 105%, NI-DMM returns NaN^2 (except for the 100 MΩ range on the NI 4080/4082) and the IVI overrange

### Overrange/Underrange

This section describes the overrange and/or underrange conditions, as applicable, for the PXIe‑4080/4081/4082.

| Function | Overrange1 | Underrange |
| --- | --- | --- |
| DC Functions:Voltage, Current, Resistance, and Diode | Above 105%, NI-DMM returns NaN2 (except for the 100 MΩ range on the NI 4080/4082) and the IVI overrange warning. For the 100 MΩ range on the NI 4080/4082, measurements between 105 MΩ and 1.05 GΩ return the IVI overrange warning. For measurements above 1.05 GΩ, NI-DMM returns NaN2 and the IVI overrange warning instead of the reading. | Not applicable |
| AC Functions:Voltage and Current | Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. At significantly higher than 105%, NI-DMM returns a NaN2 and the IVI overrange warning. | Not applicable |
| Frequency/Period | Not applicable | Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Capacitance (NI 4082 only) | Above 110%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Occurs below 5% of the range, except in the 300 pF range. The 300 pF range does not have underrange. Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Inductance (NI 4082 only) | Above 110%, NI-DMM returns NaN2 and the IVI overrange warning. | Can occur below ≤1% of range for the 10 mH, 100 mH, 1 H, and 5 H ranges when the signal is too weak for the measurement to occur. In such cases, NI-DMM returns 0 H and the NI-DMM underrange warning. |
| 1Refer to the NI IVI Driver Help at ni.com/docs for the IVI overrange warning code.2 NaN is a digital display value for a floating-point representation of "Not a Number," as defined by the IEEE standard for binary floating point arithmetic. NaN is typically the result of an undefined operation, such as log(-1). |  |  |

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=408x-overrangeunderrange_2.html language=enus -->
## TOPIC 00112: Overrange/Underrange

- bundle_id: `ni-dmm`
- source_path: `408x-overrangeunderrange_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-overrangeunderrange_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the overrange and/or underrange conditions, as applicable, for the PXIe‑4080/4081/4082. Function Overrange^1 Underrange DC Functions:Voltage, Current, Resistance, and Diode Above 105%, NI-DMM returns NaN^2 (except for the 100 MΩ range on the NI 4080/4082) and the IVI overrange

### Overrange/Underrange

This section describes the overrange and/or underrange conditions, as applicable, for the PXIe‑4080/4081/4082.

| Function | Overrange1 | Underrange |
| --- | --- | --- |
| DC Functions:Voltage, Current, Resistance, and Diode | Above 105%, NI-DMM returns NaN2 (except for the 100 MΩ range on the NI 4080/4082) and the IVI overrange warning. For the 100 MΩ range on the NI 4080/4082, measurements between 105 MΩ and 1.05 GΩ return the IVI overrange warning. For measurements above 1.05 GΩ, NI-DMM returns NaN2 and the IVI overrange warning instead of the reading. | Not applicable |
| AC Functions:Voltage and Current | Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. At significantly higher than 105%, NI-DMM returns a NaN2 and the IVI overrange warning. | Not applicable |
| Frequency/Period | Not applicable | Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Capacitance (NI 4082 only) | Above 110%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Occurs below 5% of the range, except in the 300 pF range. The 300 pF range does not have underrange. Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Inductance (NI 4082 only) | Above 110%, NI-DMM returns NaN2 and the IVI overrange warning. | Can occur below ≤1% of range for the 10 mH, 100 mH, 1 H, and 5 H ranges when the signal is too weak for the measurement to occur. In such cases, NI-DMM returns 0 H and the NI-DMM underrange warning. |
| 1Refer to the NI IVI Driver Help at ni.com/docs for the IVI overrange warning code.2 NaN is a digital display value for a floating-point representation of "Not a Number," as defined by the IEEE standard for binary floating point arithmetic. NaN is typically the result of an undefined operation, such as log(-1). |  |  |

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=408x-overrangeunderrange_3.html language=enus -->
## TOPIC 00113: Overrange/Underrange

- bundle_id: `ni-dmm`
- source_path: `408x-overrangeunderrange_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-overrangeunderrange_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the overrange and/or underrange conditions, as applicable, for the PXIe‑4080/4081/4082. Function Overrange^1 Underrange DC Functions:Voltage, Current, Resistance, and Diode Above 105%, NI-DMM returns NaN^2 (except for the 100 MΩ range on the NI 4080/4082) and the IVI overrange

### Overrange/Underrange

This section describes the overrange and/or underrange conditions, as applicable, for the PXIe‑4080/4081/4082.

| Function | Overrange1 | Underrange |
| --- | --- | --- |
| DC Functions:Voltage, Current, Resistance, and Diode | Above 105%, NI-DMM returns NaN2 (except for the 100 MΩ range on the NI 4080/4082) and the IVI overrange warning. For the 100 MΩ range on the NI 4080/4082, measurements between 105 MΩ and 1.05 GΩ return the IVI overrange warning. For measurements above 1.05 GΩ, NI-DMM returns NaN2 and the IVI overrange warning instead of the reading. | Not applicable |
| AC Functions:Voltage and Current | Above 105%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. At significantly higher than 105%, NI-DMM returns a NaN2 and the IVI overrange warning. | Not applicable |
| Frequency/Period | Not applicable | Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Capacitance (NI 4082 only) | Above 110%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. | Occurs below 5% of the range, except in the 300 pF range. The 300 pF range does not have underrange. Below 5%, NI-DMM returns –Inf and the NI-DMM underrange warning. |
| Inductance (NI 4082 only) | Above 110%, NI-DMM returns NaN2 and the IVI overrange warning. | Can occur below ≤1% of range for the 10 mH, 100 mH, 1 H, and 5 H ranges when the signal is too weak for the measurement to occur. In such cases, NI-DMM returns 0 H and the NI-DMM underrange warning. |
| 1Refer to the NI IVI Driver Help at ni.com/docs for the IVI overrange warning code.2 NaN is a digital display value for a floating-point representation of "Not a Number," as defined by the IEEE standard for binary floating point arithmetic. NaN is typically the result of an undefined operation, such as log(-1). |  |  |

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=408x-self-calibration.html language=enus -->
## TOPIC 00114: Self-Calibration

- bundle_id: `ni-dmm`
- source_path: `408x-self-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-self-calibration.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every measurement instrument performs within its specifications over a finite temperature range and time. If the excursions in temperature and time exceed those specified, and you need performance close to the specifications,then you must recalibrate the instrument at the new temperature or after a

### Self-Calibration

Every measurement instrument performs within its specifications over a finite temperature range
 and time. If the excursions in temperature and time exceed those specified, and you
 need performance close to the specifications,then you must recalibrate the
 instrument at the new temperature or after a certain amount of time. The DMM has a
 self-calibration function that allows you to perform a calibration at the
 temperature you are making your measurements.

Self-calibration fully recalibrates all ranges for DC volts and resistance.

Note

niDMM_SelfCal

Self-calibration makes the DMM highly accurate and very stable at any operating temperature—well outside of the traditional 18 °C to 28 °C range.

The typical way of expressing accuracy is:

Accuracy = ±(X ppm of reading + Y ppm of range)

For example, if the last calibration (self or external) was performed at 23 °C, and you are using
 the 10 V range on the NI 4070 and applying a 5 V signal within 18 °C to 28 °C, the
 2–year accuracy is:

2–year Accuracy = ±(25 ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

This traditional calculation method can cause errors if the temperature is not tightly
 controlled. When a system is built of multiple traditional instrument components
 integrated together, the instruments are subject to temperature rises caused by
 inherent compromises in air circulation and other factors.

If the ambient temperature is outside of the 18 °C to 28 °C range, to calculate the measurement accuracy, you need to calibrate your instrument at the ambient temperature, or add temperature coefficient accuracy for each additional degree outside the calibration range.

Using the NI 4070, assume the ambient temperature is 38 °C. The temperature coefficient (tempco)
 without self-calibration is:

Tempco = (1 ppm of reading +1 ppm of range)/°C

The 2–year accuracy at 38 °C becomes:

±[25  ppm of 5 V + 6 ppm of 10 V] + [(1 ppm of 5 V + 1 ppm of 10 V)x 10] = ±335 µV (uncertainty)

Externally recalibrating a system can be difficult and expensive and as a result generally is performed infrequently.

After performing self-calibration at 38 °C, you do notneed to add any uncertainty to account for temperature change.

The 2–year accuracy after self-calibration at 38 °Becomes:

±(25  ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

Note

| Calibration Option | Application | When |
| --- | --- | --- |
| Factory calibration | All ranges Recalibrates for time drift of onboard references Corrects for AC flatness | Every two years |
| Self-calibration | Recalibrates the measurement path and ADC for DC volts and resistance | Every 24 hours or when the temperature changes more than 5 °C from last self-calibration |
| ADC calibration | Recalibrates ADC drift for all ranges | Every reading when selected |
| NONE | No recalibration | Extended high-speed acquisitions |

The NI 4080/4081/4082 incorporates a temperature sensor that can beread to determine how much
 temperature has drifted from the previous calibration. In addition, the previous
 self-calibration time and date can also be read.

During self-calibration, the internal circuitry is automatically disconnected from the input.
 Therefore, for the majority of applications, users do not need to
 disconnect the input signals during self-calibration. However, excessive signal
 levels (>30 VDC, >30 VAC<sub>rms</sub>, >20 kHz) at the input terminals of
 the NI 4080/4081/4082 generate a self-calibration error. Disconnecting the input
 signals during a self-calibration prevents the error from occurring. If you are
 using the NI 4080/4081/4082 as part of a switching system, you can open (disconnect)
 the connections to the NI 4080/4081/4082 input terminals, switch to a non-connected
 path, or switch to a low voltage, low frequency path. For optimum reliability, avoid
 application of current to the Amps terminals or signals of >30 V to the Volts
 Input terminals during self-calibration.

Parent topic:

NI PXIe-4082

Related concepts:

- Performing Self-Calibration
- Accuracy
- ADC Calibration

Related information:

- niDMM_SelfCal
- niDMM Self Cal

<!--NI_TOPIC bundle=ni-dmm path=408x-self-calibration_2.html language=enus -->
## TOPIC 00115: Self-Calibration

- bundle_id: `ni-dmm`
- source_path: `408x-self-calibration_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-self-calibration_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every measurement instrument performs within its specifications over a finite temperature range and time. If the excursions in temperature and time exceed those specified, and you need performance close to the specifications,then you must recalibrate the instrument at the new temperature or after a

### Self-Calibration

Every measurement instrument performs within its specifications over a finite temperature range
 and time. If the excursions in temperature and time exceed those specified, and you
 need performance close to the specifications,then you must recalibrate the
 instrument at the new temperature or after a certain amount of time. The DMM has a
 self-calibration function that allows you to perform a calibration at the
 temperature you are making your measurements.

Self-calibration fully recalibrates all ranges for DC volts and resistance.

Note

niDMM_SelfCal

Self-calibration makes the DMM highly accurate and very stable at any operating temperature—well outside of the traditional 18 °C to 28 °C range.

The typical way of expressing accuracy is:

Accuracy = ±(X ppm of reading + Y ppm of range)

For example, if the last calibration (self or external) was performed at 23 °C, and you are using
 the 10 V range on the NI 4070 and applying a 5 V signal within 18 °C to 28 °C, the
 2–year accuracy is:

2–year Accuracy = ±(25 ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

This traditional calculation method can cause errors if the temperature is not tightly
 controlled. When a system is built of multiple traditional instrument components
 integrated together, the instruments are subject to temperature rises caused by
 inherent compromises in air circulation and other factors.

If the ambient temperature is outside of the 18 °C to 28 °C range, to calculate the measurement accuracy, you need to calibrate your instrument at the ambient temperature, or add temperature coefficient accuracy for each additional degree outside the calibration range.

Using the NI 4070, assume the ambient temperature is 38 °C. The temperature coefficient (tempco)
 without self-calibration is:

Tempco = (1 ppm of reading +1 ppm of range)/°C

The 2–year accuracy at 38 °C becomes:

±[25  ppm of 5 V + 6 ppm of 10 V] + [(1 ppm of 5 V + 1 ppm of 10 V)x 10] = ±335 µV (uncertainty)

Externally recalibrating a system can be difficult and expensive and as a result generally is performed infrequently.

After performing self-calibration at 38 °C, you do notneed to add any uncertainty to account for temperature change.

The 2–year accuracy after self-calibration at 38 °Becomes:

±(25  ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

Note

| Calibration Option | Application | When |
| --- | --- | --- |
| Factory calibration | All ranges Recalibrates for time drift of onboard references Corrects for AC flatness | Every two years |
| Self-calibration | Recalibrates the measurement path and ADC for DC volts and resistance | Every 24 hours or when the temperature changes more than 5 °C from last self-calibration |
| ADC calibration | Recalibrates ADC drift for all ranges | Every reading when selected |
| NONE | No recalibration | Extended high-speed acquisitions |

The NI 4080/4081/4082 incorporates a temperature sensor that can beread to determine how much
 temperature has drifted from the previous calibration. In addition, the previous
 self-calibration time and date can also be read.

During self-calibration, the internal circuitry is automatically disconnected from the input.
 Therefore, for the majority of applications, users do not need to
 disconnect the input signals during self-calibration. However, excessive signal
 levels (>30 VDC, >30 VAC<sub>rms</sub>, >20 kHz) at the input terminals of
 the NI 4080/4081/4082 generate a self-calibration error. Disconnecting the input
 signals during a self-calibration prevents the error from occurring. If you are
 using the NI 4080/4081/4082 as part of a switching system, you can open (disconnect)
 the connections to the NI 4080/4081/4082 input terminals, switch to a non-connected
 path, or switch to a low voltage, low frequency path. For optimum reliability, avoid
 application of current to the Amps terminals or signals of >30 V to the Volts
 Input terminals during self-calibration.

Parent topic:

NI 4081

<!--NI_TOPIC bundle=ni-dmm path=408x-self-calibration_3.html language=enus -->
## TOPIC 00116: Self-Calibration

- bundle_id: `ni-dmm`
- source_path: `408x-self-calibration_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/408x-self-calibration_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every measurement instrument performs within its specifications over a finite temperature range and time. If the excursions in temperature and time exceed those specified, and you need performance close to the specifications,then you must recalibrate the instrument at the new temperature or after a

### Self-Calibration

Every measurement instrument performs within its specifications over a finite temperature range
 and time. If the excursions in temperature and time exceed those specified, and you
 need performance close to the specifications,then you must recalibrate the
 instrument at the new temperature or after a certain amount of time. The DMM has a
 self-calibration function that allows you to perform a calibration at the
 temperature you are making your measurements.

Self-calibration fully recalibrates all ranges for DC volts and resistance.

Note

niDMM_SelfCal

Self-calibration makes the DMM highly accurate and very stable at any operating temperature—well outside of the traditional 18 °C to 28 °C range.

The typical way of expressing accuracy is:

Accuracy = ±(X ppm of reading + Y ppm of range)

For example, if the last calibration (self or external) was performed at 23 °C, and you are using
 the 10 V range on the NI 4070 and applying a 5 V signal within 18 °C to 28 °C, the
 2–year accuracy is:

2–year Accuracy = ±(25 ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

This traditional calculation method can cause errors if the temperature is not tightly
 controlled. When a system is built of multiple traditional instrument components
 integrated together, the instruments are subject to temperature rises caused by
 inherent compromises in air circulation and other factors.

If the ambient temperature is outside of the 18 °C to 28 °C range, to calculate the measurement accuracy, you need to calibrate your instrument at the ambient temperature, or add temperature coefficient accuracy for each additional degree outside the calibration range.

Using the NI 4070, assume the ambient temperature is 38 °C. The temperature coefficient (tempco)
 without self-calibration is:

Tempco = (1 ppm of reading +1 ppm of range)/°C

The 2–year accuracy at 38 °C becomes:

±[25  ppm of 5 V + 6 ppm of 10 V] + [(1 ppm of 5 V + 1 ppm of 10 V)x 10] = ±335 µV (uncertainty)

Externally recalibrating a system can be difficult and expensive and as a result generally is performed infrequently.

After performing self-calibration at 38 °C, you do notneed to add any uncertainty to account for temperature change.

The 2–year accuracy after self-calibration at 38 °Becomes:

±(25  ppm of 5 V + 6 ppm of 10 V) = ±185 µV (uncertainty)

Note

| Calibration Option | Application | When |
| --- | --- | --- |
| Factory calibration | All ranges Recalibrates for time drift of onboard references Corrects for AC flatness | Every two years |
| Self-calibration | Recalibrates the measurement path and ADC for DC volts and resistance | Every 24 hours or when the temperature changes more than 5 °C from last self-calibration |
| ADC calibration | Recalibrates ADC drift for all ranges | Every reading when selected |
| NONE | No recalibration | Extended high-speed acquisitions |

The NI 4080/4081/4082 incorporates a temperature sensor that can beread to determine how much
 temperature has drifted from the previous calibration. In addition, the previous
 self-calibration time and date can also be read.

During self-calibration, the internal circuitry is automatically disconnected from the input.
 Therefore, for the majority of applications, users do not need to
 disconnect the input signals during self-calibration. However, excessive signal
 levels (>30 VDC, >30 VAC<sub>rms</sub>, >20 kHz) at the input terminals of
 the NI 4080/4081/4082 generate a self-calibration error. Disconnecting the input
 signals during a self-calibration prevents the error from occurring. If you are
 using the NI 4080/4081/4082 as part of a switching system, you can open (disconnect)
 the connections to the NI 4080/4081/4082 input terminals, switch to a non-connected
 path, or switch to a low voltage, low frequency path. For optimum reliability, avoid
 application of current to the Amps terminals or signals of >30 V to the Volts
 Input terminals during self-calibration.

Parent topic:

NI PXIe-4080

<!--NI_TOPIC bundle=ni-dmm path=ac-rms-noise.html language=enus -->
## TOPIC 00117: AC RMS Noise

- bundle_id: `ni-dmm`
- source_path: `ac-rms-noise.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-rms-noise.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specificall

### AC RMS Noise

Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specifically, if S is the rms value of the signal and N is the rms value of the noise, the total reading is T = √(S<sup>2</sup> + N<sup>2</sup>). In the case of noise originating in the device, factory calibration and self-calibration measure the internal noise, and the algorithm subtracts the measured noise from the result to improve accuracy. Auto Zero can be used for the same purpose. The subtraction is not linear, but takes into account the nonlinear way in which noise increases measured readings.

Note

Parent topic:

AC Voltage

Related concepts:

- Configuring Measurement Timing
- Self-Calibration

<!--NI_TOPIC bundle=ni-dmm path=ac-rms-noise_2.html language=enus -->
## TOPIC 00118: AC RMS Noise

- bundle_id: `ni-dmm`
- source_path: `ac-rms-noise_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-rms-noise_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specificall

### AC RMS Noise

Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specifically, if S is the rms value of the signal and N is the rms value of the noise, the total reading is T = √(S<sup>2</sup> + N<sup>2</sup>). In the case of noise originating in the device, factory calibration and self-calibration measure the internal noise, and the algorithm subtracts the measured noise from the result to improve accuracy. Auto Zero can be used for the same purpose. The subtraction is not linear, but takes into account the nonlinear way in which noise increases measured readings.

Note

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=ac-rms-noise_3.html language=enus -->
## TOPIC 00119: AC RMS Noise

- bundle_id: `ni-dmm`
- source_path: `ac-rms-noise_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-rms-noise_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specificall

### AC RMS Noise

Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specifically, if S is the rms value of the signal and N is the rms value of the noise, the total reading is T = √(S<sup>2</sup> + N<sup>2</sup>). In the case of noise originating in the device, factory calibration and self-calibration measure the internal noise, and the algorithm subtracts the measured noise from the result to improve accuracy. Auto Zero can be used for the same purpose. The subtraction is not linear, but takes into account the nonlinear way in which noise increases measured readings.

Note

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=ac-rms-noise_4.html language=enus -->
## TOPIC 00120: AC RMS Noise

- bundle_id: `ni-dmm`
- source_path: `ac-rms-noise_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-rms-noise_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specificall

### AC RMS Noise

Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specifically, if S is the rms value of the signal and N is the rms value of the noise, the total reading is T = √(S<sup>2</sup> + N<sup>2</sup>). In the case of noise originating in the device, factory calibration and self-calibration measure the internal noise, and the algorithm subtracts the measured noise from the result to improve accuracy. Auto Zero can be used for the same purpose. The subtraction is not linear, but takes into account the nonlinear way in which noise increases measured readings.

Note

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=ac-rms-noise_5.html language=enus -->
## TOPIC 00121: AC RMS Noise

- bundle_id: `ni-dmm`
- source_path: `ac-rms-noise_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-rms-noise_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specificall

### AC RMS Noise

Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specifically, if S is the rms value of the signal and N is the rms value of the noise, the total reading is T = √(S<sup>2</sup> + N<sup>2</sup>). In the case of noise originating in the device, factory calibration and self-calibration measure the internal noise, and the algorithm subtracts the measured noise from the result to improve accuracy. Auto Zero can be used for the same purpose. The subtraction is not linear, but takes into account the nonlinear way in which noise increases measured readings.

Note

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=ac-rms-noise_6.html language=enus -->
## TOPIC 00122: AC RMS Noise

- bundle_id: `ni-dmm`
- source_path: `ac-rms-noise_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-rms-noise_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specificall

### AC RMS Noise

Any noise added to the signal being measured can increase the apparent rms value of a signal. This applies both to external noise sources and to noise originating inside the device itself. Due to the nature of the rms computation, added noise increases the reading in a nonlinear fashion. Specifically, if S is the rms value of the signal and N is the rms value of the noise, the total reading is T = √(S<sup>2</sup> + N<sup>2</sup>). In the case of noise originating in the device, factory calibration and self-calibration measure the internal noise, and the algorithm subtracts the measured noise from the result to improve accuracy. Auto Zero can be used for the same purpose. The subtraction is not linear, but takes into account the nonlinear way in which noise increases measured readings.

Note

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=ac-voltage.html language=enus -->
## TOPIC 00123: AC Voltage

- bundle_id: `ni-dmm`
- source_path: `ac-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-voltage.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal pro

### AC Voltage

AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal processing in the analog domain. However, the NI 4070/4071/4072 and the NI 4080/4081/4082 use digital signal processing to compute the rms value from digitized samples of the AC waveform. By computing rms values (a traditionally analog problem) in the digital domain, the DMM speeds up AC measurements in two ways, as follows:

- Allows computation of fully-settled RMS values with only four cycles of the waveform
- Automatically rejects the DC component of the signal, making possible an AC Volts DC Coupled mode, which completely bypasses the slow-setting input coupling capacitor required on traditional DMMs

The result is quiet, accurate, and fast-settling AC readings.

The rms algorithm used by the DMM requires at least 4 cycles of the waveform to obtain a quiet reading. For example, it requires a measurement aperture of 4 ms to accurately measure a 1 kHz sine wave. The measurement aperture also needs to be long enough to obtain the requested resolution. For example, although a 40 µs aperture is long enough to measure the rms value of a 100 kHz sine wave, it is not long enough to obtain readings with 6½ digit accuracy. Thus, the period of the waveform being measured and the desired resolution both affect the necessary aperture. NI-DMM selects the shortest aperture to satisfy both requirements.

For aperture times for the device, refer to the Measurement Defaults table for your device.

The period of the measured waveform, rather than the period of its lowest-frequency component, determines the required minimum aperture, as shown in Figures A, B, and C. Figure A shows a 1 kHz sine wave. This signal can be measured in 4 ms because it is 4 cycles of the waveform. Figure B shows a 1.1 kHz sine wave. It can also be measured in 4 ms because it is slightly more than 4 cycles of the waveform. Figure C shows a signal that is the sum of the signals in Figures A and B. Although the minimum frequency component of this signal is 1 kHz, 4 msec is not long enough to measure the rms value of the whole signal. In this case, the signal has a period of 10 msec, so it requires a 40 msec aperture for an accurate measurement.

Figure 1.

[IMAGE alt='image' src='GUID-12457EA9-1E51-48F8-8239-C5CF8CAEA4B1-a5.svg']

Figure 2.

[IMAGE alt='image' src='GUID-8B7E0186-01D2-4F20-8921-529AAA24159E-a5.svg']

Figure 3.

[IMAGE alt='image' src='GUID-1BB2AA25-B7CA-4F8F-83CB-109D83986551-a5.svg']

Parent topic:

DMM Measurements

Related concepts:

- Configuring Measurement Timing

<!--NI_TOPIC bundle=ni-dmm path=ac-voltage_2.html language=enus -->
## TOPIC 00124: AC Voltage

- bundle_id: `ni-dmm`
- source_path: `ac-voltage_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-voltage_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal pro

### AC Voltage

AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal processing in the analog domain. However, the NI 4070/4071/4072 and the NI 4080/4081/4082 use digital signal processing to compute the rms value from digitized samples of the AC waveform. By computing rms values (a traditionally analog problem) in the digital domain, the DMM speeds up AC measurements in two ways, as follows:

- Allows computation of fully-settled RMS values with only four cycles of the waveform
- Automatically rejects the DC component of the signal, making possible an AC Volts DC Coupled mode, which completely bypasses the slow-setting input coupling capacitor required on traditional DMMs

The result is quiet, accurate, and fast-settling AC readings.

The rms algorithm used by the DMM requires at least 4 cycles of the waveform to obtain a quiet reading. For example, it requires a measurement aperture of 4 ms to accurately measure a 1 kHz sine wave. The measurement aperture also needs to be long enough to obtain the requested resolution. For example, although a 40 µs aperture is long enough to measure the rms value of a 100 kHz sine wave, it is not long enough to obtain readings with 6½ digit accuracy. Thus, the period of the waveform being measured and the desired resolution both affect the necessary aperture. NI-DMM selects the shortest aperture to satisfy both requirements.

For aperture times for the device, refer to the Measurement Defaults table for your device.

The period of the measured waveform, rather than the period of its lowest-frequency component, determines the required minimum aperture, as shown in Figures A, B, and C. Figure A shows a 1 kHz sine wave. This signal can be measured in 4 ms because it is 4 cycles of the waveform. Figure B shows a 1.1 kHz sine wave. It can also be measured in 4 ms because it is slightly more than 4 cycles of the waveform. Figure C shows a signal that is the sum of the signals in Figures A and B. Although the minimum frequency component of this signal is 1 kHz, 4 msec is not long enough to measure the rms value of the whole signal. In this case, the signal has a period of 10 msec, so it requires a 40 msec aperture for an accurate measurement.

Figure 14.

[IMAGE alt='image' src='GUID-12457EA9-1E51-48F8-8239-C5CF8CAEA4B1-a5.svg']

Figure 15.

[IMAGE alt='image' src='GUID-8B7E0186-01D2-4F20-8921-529AAA24159E-a5.svg']

Figure 16.

[IMAGE alt='image' src='GUID-1BB2AA25-B7CA-4F8F-83CB-109D83986551-a5.svg']

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=ac-voltage_3.html language=enus -->
## TOPIC 00125: AC Voltage

- bundle_id: `ni-dmm`
- source_path: `ac-voltage_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-voltage_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal pro

### AC Voltage

AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal processing in the analog domain. However, the NI 4070/4071/4072 and the NI 4080/4081/4082 use digital signal processing to compute the rms value from digitized samples of the AC waveform. By computing rms values (a traditionally analog problem) in the digital domain, the DMM speeds up AC measurements in two ways, as follows:

- Allows computation of fully-settled RMS values with only four cycles of the waveform
- Automatically rejects the DC component of the signal, making possible an AC Volts DC Coupled mode, which completely bypasses the slow-setting input coupling capacitor required on traditional DMMs

The result is quiet, accurate, and fast-settling AC readings.

The rms algorithm used by the DMM requires at least 4 cycles of the waveform to obtain a quiet reading. For example, it requires a measurement aperture of 4 ms to accurately measure a 1 kHz sine wave. The measurement aperture also needs to be long enough to obtain the requested resolution. For example, although a 40 µs aperture is long enough to measure the rms value of a 100 kHz sine wave, it is not long enough to obtain readings with 6½ digit accuracy. Thus, the period of the waveform being measured and the desired resolution both affect the necessary aperture. NI-DMM selects the shortest aperture to satisfy both requirements.

For aperture times for the device, refer to the Measurement Defaults table for your device.

The period of the measured waveform, rather than the period of its lowest-frequency component, determines the required minimum aperture, as shown in Figures A, B, and C. Figure A shows a 1 kHz sine wave. This signal can be measured in 4 ms because it is 4 cycles of the waveform. Figure B shows a 1.1 kHz sine wave. It can also be measured in 4 ms because it is slightly more than 4 cycles of the waveform. Figure C shows a signal that is the sum of the signals in Figures A and B. Although the minimum frequency component of this signal is 1 kHz, 4 msec is not long enough to measure the rms value of the whole signal. In this case, the signal has a period of 10 msec, so it requires a 40 msec aperture for an accurate measurement.

Figure 17.

[IMAGE alt='image' src='GUID-12457EA9-1E51-48F8-8239-C5CF8CAEA4B1-a5.svg']

Figure 18.

[IMAGE alt='image' src='GUID-8B7E0186-01D2-4F20-8921-529AAA24159E-a5.svg']

Figure 19.

[IMAGE alt='image' src='GUID-1BB2AA25-B7CA-4F8F-83CB-109D83986551-a5.svg']

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=ac-voltage_4.html language=enus -->
## TOPIC 00126: AC Voltage

- bundle_id: `ni-dmm`
- source_path: `ac-voltage_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-voltage_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal pro

### AC Voltage

AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal processing in the analog domain. However, the NI 4070/4071/4072 and the NI 4080/4081/4082 use digital signal processing to compute the rms value from digitized samples of the AC waveform. By computing rms values (a traditionally analog problem) in the digital domain, the DMM speeds up AC measurements in two ways, as follows:

- Allows computation of fully-settled RMS values with only four cycles of the waveform
- Automatically rejects the DC component of the signal, making possible an AC Volts DC Coupled mode, which completely bypasses the slow-setting input coupling capacitor required on traditional DMMs

The result is quiet, accurate, and fast-settling AC readings.

The rms algorithm used by the DMM requires at least 4 cycles of the waveform to obtain a quiet reading. For example, it requires a measurement aperture of 4 ms to accurately measure a 1 kHz sine wave. The measurement aperture also needs to be long enough to obtain the requested resolution. For example, although a 40 µs aperture is long enough to measure the rms value of a 100 kHz sine wave, it is not long enough to obtain readings with 6½ digit accuracy. Thus, the period of the waveform being measured and the desired resolution both affect the necessary aperture. NI-DMM selects the shortest aperture to satisfy both requirements.

For aperture times for the device, refer to the Measurement Defaults table for your device.

The period of the measured waveform, rather than the period of its lowest-frequency component, determines the required minimum aperture, as shown in Figures A, B, and C. Figure A shows a 1 kHz sine wave. This signal can be measured in 4 ms because it is 4 cycles of the waveform. Figure B shows a 1.1 kHz sine wave. It can also be measured in 4 ms because it is slightly more than 4 cycles of the waveform. Figure C shows a signal that is the sum of the signals in Figures A and B. Although the minimum frequency component of this signal is 1 kHz, 4 msec is not long enough to measure the rms value of the whole signal. In this case, the signal has a period of 10 msec, so it requires a 40 msec aperture for an accurate measurement.

Figure 20.

[IMAGE alt='image' src='GUID-12457EA9-1E51-48F8-8239-C5CF8CAEA4B1-a5.svg']

Figure 21.

[IMAGE alt='image' src='GUID-8B7E0186-01D2-4F20-8921-529AAA24159E-a5.svg']

Figure 22.

[IMAGE alt='image' src='GUID-1BB2AA25-B7CA-4F8F-83CB-109D83986551-a5.svg']

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=ac-voltage_5.html language=enus -->
## TOPIC 00127: AC Voltage

- bundle_id: `ni-dmm`
- source_path: `ac-voltage_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-voltage_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal pro

### AC Voltage

AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal processing in the analog domain. However, the NI 4070/4071/4072 and the NI 4080/4081/4082 use digital signal processing to compute the rms value from digitized samples of the AC waveform. By computing rms values (a traditionally analog problem) in the digital domain, the DMM speeds up AC measurements in two ways, as follows:

- Allows computation of fully-settled RMS values with only four cycles of the waveform
- Automatically rejects the DC component of the signal, making possible an AC Volts DC Coupled mode, which completely bypasses the slow-setting input coupling capacitor required on traditional DMMs

The result is quiet, accurate, and fast-settling AC readings.

The rms algorithm used by the DMM requires at least 4 cycles of the waveform to obtain a quiet reading. For example, it requires a measurement aperture of 4 ms to accurately measure a 1 kHz sine wave. The measurement aperture also needs to be long enough to obtain the requested resolution. For example, although a 40 µs aperture is long enough to measure the rms value of a 100 kHz sine wave, it is not long enough to obtain readings with 6½ digit accuracy. Thus, the period of the waveform being measured and the desired resolution both affect the necessary aperture. NI-DMM selects the shortest aperture to satisfy both requirements.

For aperture times for the device, refer to the Measurement Defaults table for your device.

The period of the measured waveform, rather than the period of its lowest-frequency component, determines the required minimum aperture, as shown in Figures A, B, and C. Figure A shows a 1 kHz sine wave. This signal can be measured in 4 ms because it is 4 cycles of the waveform. Figure B shows a 1.1 kHz sine wave. It can also be measured in 4 ms because it is slightly more than 4 cycles of the waveform. Figure C shows a signal that is the sum of the signals in Figures A and B. Although the minimum frequency component of this signal is 1 kHz, 4 msec is not long enough to measure the rms value of the whole signal. In this case, the signal has a period of 10 msec, so it requires a 40 msec aperture for an accurate measurement.

Figure 23.

[IMAGE alt='image' src='GUID-12457EA9-1E51-48F8-8239-C5CF8CAEA4B1-a5.svg']

Figure 24.

[IMAGE alt='image' src='GUID-8B7E0186-01D2-4F20-8921-529AAA24159E-a5.svg']

Figure 25.

[IMAGE alt='image' src='GUID-1BB2AA25-B7CA-4F8F-83CB-109D83986551-a5.svg']

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=ac-voltage_6.html language=enus -->
## TOPIC 00128: AC Voltage

- bundle_id: `ni-dmm`
- source_path: `ac-voltage_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-voltage_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal pro

### AC Voltage

AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal processing in the analog domain. However, the NI 4070/4071/4072 and the NI 4080/4081/4082 use digital signal processing to compute the rms value from digitized samples of the AC waveform. By computing rms values (a traditionally analog problem) in the digital domain, the DMM speeds up AC measurements in two ways, as follows:

- Allows computation of fully-settled RMS values with only four cycles of the waveform
- Automatically rejects the DC component of the signal, making possible an AC Volts DC Coupled mode, which completely bypasses the slow-setting input coupling capacitor required on traditional DMMs

The result is quiet, accurate, and fast-settling AC readings.

The rms algorithm used by the DMM requires at least 4 cycles of the waveform to obtain a quiet reading. For example, it requires a measurement aperture of 4 ms to accurately measure a 1 kHz sine wave. The measurement aperture also needs to be long enough to obtain the requested resolution. For example, although a 40 µs aperture is long enough to measure the rms value of a 100 kHz sine wave, it is not long enough to obtain readings with 6½ digit accuracy. Thus, the period of the waveform being measured and the desired resolution both affect the necessary aperture. NI-DMM selects the shortest aperture to satisfy both requirements.

For aperture times for the device, refer to the Measurement Defaults table for your device.

The period of the measured waveform, rather than the period of its lowest-frequency component, determines the required minimum aperture, as shown in Figures A, B, and C. Figure A shows a 1 kHz sine wave. This signal can be measured in 4 ms because it is 4 cycles of the waveform. Figure B shows a 1.1 kHz sine wave. It can also be measured in 4 ms because it is slightly more than 4 cycles of the waveform. Figure C shows a signal that is the sum of the signals in Figures A and B. Although the minimum frequency component of this signal is 1 kHz, 4 msec is not long enough to measure the rms value of the whole signal. In this case, the signal has a period of 10 msec, so it requires a 40 msec aperture for an accurate measurement.

Figure 26.

[IMAGE alt='image' src='GUID-12457EA9-1E51-48F8-8239-C5CF8CAEA4B1-a5.svg']

Figure 27.

[IMAGE alt='image' src='GUID-8B7E0186-01D2-4F20-8921-529AAA24159E-a5.svg']

Figure 28.

[IMAGE alt='image' src='GUID-1BB2AA25-B7CA-4F8F-83CB-109D83986551-a5.svg']

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=ac-voltage_7.html language=enus -->
## TOPIC 00129: AC Voltage

- bundle_id: `ni-dmm`
- source_path: `ac-voltage_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ac-voltage_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal pro

### AC Voltage

AC signals are typically characterized by their root-mean-square (rms) amplitude, which is a measure of their total energy. To compute the rms value of a waveform, take the square root of the mean value of the square of the signal level. Some DMMs, including the NI 4065, do this nonlinear signal processing in the analog domain. However, the NI 4070/4071/4072 and the NI 4080/4081/4082 use digital signal processing to compute the rms value from digitized samples of the AC waveform. By computing rms values (a traditionally analog problem) in the digital domain, the DMM speeds up AC measurements in two ways, as follows:

- Allows computation of fully-settled RMS values with only four cycles of the waveform
- Automatically rejects the DC component of the signal, making possible an AC Volts DC Coupled mode, which completely bypasses the slow-setting input coupling capacitor required on traditional DMMs

The result is quiet, accurate, and fast-settling AC readings.

The rms algorithm used by the DMM requires at least 4 cycles of the waveform to obtain a quiet reading. For example, it requires a measurement aperture of 4 ms to accurately measure a 1 kHz sine wave. The measurement aperture also needs to be long enough to obtain the requested resolution. For example, although a 40 µs aperture is long enough to measure the rms value of a 100 kHz sine wave, it is not long enough to obtain readings with 6½ digit accuracy. Thus, the period of the waveform being measured and the desired resolution both affect the necessary aperture. NI-DMM selects the shortest aperture to satisfy both requirements.

For aperture times for the device, refer to the Measurement Defaults table for your device.

The period of the measured waveform, rather than the period of its lowest-frequency component, determines the required minimum aperture, as shown in Figures A, B, and C. Figure A shows a 1 kHz sine wave. This signal can be measured in 4 ms because it is 4 cycles of the waveform. Figure B shows a 1.1 kHz sine wave. It can also be measured in 4 ms because it is slightly more than 4 cycles of the waveform. Figure C shows a signal that is the sum of the signals in Figures A and B. Although the minimum frequency component of this signal is 1 kHz, 4 msec is not long enough to measure the rms value of the whole signal. In this case, the signal has a period of 10 msec, so it requires a 40 msec aperture for an accurate measurement.

Figure 29.

[IMAGE alt='image' src='GUID-12457EA9-1E51-48F8-8239-C5CF8CAEA4B1-a5.svg']

Figure 30.

[IMAGE alt='image' src='GUID-8B7E0186-01D2-4F20-8921-529AAA24159E-a5.svg']

Figure 31.

[IMAGE alt='image' src='GUID-1BB2AA25-B7CA-4F8F-83CB-109D83986551-a5.svg']

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=accuracy.html language=enus -->
## TOPIC 00130: Accuracy

- bundle_id: `ni-dmm`
- source_path: `accuracy.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/accuracy.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A reading from a DMM can differ from the actual input. Accuracy represents the uncertainty of a given measurement and can be defined in terms of the deviation from an ideal transfer function, as follows:y = mx + bwherex is the inputm is the ideal gain of a systemb is the offsetApplying this example

### Accuracy

A reading from a DMM can differ from the actual input. Accuracy represents the uncertainty of a given measurement and can be defined in terms of the deviation from an ideal transfer function, as follows:

y = mx + b

where

x is the input

m is the ideal gain of a system

b is the offset

Applying this example to a DMM signal measurement, y is the reading obtained from the DMM with x as the input, and b is an offset error that you may be able to null before the measurement is performed. If m is 1, the output measurement is equal to the input. If m is 1.000001, then the error from the ideal is 1 ppm or 0.0001%.

The following table shows some ppm to percent conversions.

| ppm | Percent |
| --- | --- |
| 1 | 0.0001 |
| 10 | 0.001 |
| 100 | 0.01 |
| 1,000 | 0.1 |
| 10,000 | 1 |

Most high-resolution, high-accuracy DMMs describe accuracy in units of ppm (DC functions) and percentage (AC functions). Therefore, DC and AC accuracy specifications commonly appear as ±(ppm of reading + ppm of range) or ±(% of reading + % of range), respectively. The reading component is the deviation from the ideal m, and the range component is the deviation from the ideal b, which is zero. The b errors are most commonly referred to as offset errors.

Hence, accuracy is often expressed as:

(% Reading) + Offset

or

(% Reading) + (% Range)

or

±(ppm of reading + ppm of range)

Note

For example, assume a DMM set to the 10 V range is operating 90 days after calibration at 23 ºC ±5 ºC and is expecting a 7 V signal. The DC accuracy specifications for these conditions state ±(20 ppm of reading + 6 ppm of range). To determine the accuracy of the measurement under these conditions, use the following formula:

Accuracy = ±(ppm of reading + ppm of range) = ±(20 ppm of 7 V + 6 ppm of 10 V) = ±((7 V(20/1,000,000) + (10 V(6/1,000,000)) = ±200 µV

Therefore, the reading should be within ±200 µV of the actual input voltage.

Note

Self-Calibration

Parent topic:

Measurement Quality

Related concepts:

- Self-Calibration

<!--NI_TOPIC bundle=ni-dmm path=acquiring-data.html language=enus -->
## TOPIC 00131: Acquiring Data

- bundle_id: `ni-dmm`
- source_path: `acquiring-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/acquiring-data.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you have configured the acquisition, you can acquire data by calling niDMM Read or niDMM Initiate and niDMM Fetch. Read niDMM Read initiates an acquisition, reads the acquired data, stops the acquisition, and returns control to your program. niDMM Read does not return control to your program u

### Acquiring Data

After you have configured the acquisition, you can acquire data by calling niDMM Read or niDMM Initiate and niDMM Fetch.

[IMAGE alt='image' src='GUID-E6AA4FA2-7752-4678-9CC9-3FB7C0867302-a5.svg']

#### Read

niDMM Read initiates an acquisition, reads the acquired data, stops the acquisition,
 and returns control to your program. niDMM Read does not return control to your
 program until all of the requested data has been acquired. If you have not
 configured a trigger, the DMM immediately begins its acquisition and acquires a
 measurement. Refer to Single Point
 Acquisitions for information on triggering options.

You can set
 the maximum length of time ( Maximum Time) to allow the
 measurement operation to complete. If the measurement operation does not complete
 within this time interval, niDMM Read returns an error.

#### Initiate and Fetch

Use niDMM Initiate and niDMM Fetch for a more flexible method for acquiring data,
 offering several advantages over niDMM Read. With niDMM Initiate, you can perform
 other operations while the DMM acquires data. niDMM Fetch retrieves the acquired
 data.

After executing niDMM Initiate, the DMM begins acquiring data and
 sending it to your computer RAM. Meanwhile, control is returned immediately to your
 program, which frees up the computer processor for other tasks.

After niDMM
 Initiate, call niDMM Fetch; niDMM Fetch waits until the requested data has been
 acquired. niDMM Fetch transfers the acquired data from memory to your application.
 If the data is not acquired within the time specified with the timeout parameter,
 NI-DMM returns an error. If you want to stop the DMM before it finishes, use niDMM
 Abort.

Tip

Note

#### Multi Point Acquisitions

Call niDMM Read Multi Point or niDMM Initiate and niDMM Fetch Multi Point for
 multipoint acquisitions. If the measurement operation does not complete within the
 Maximum Time interval, niDMM Read Multi Point or niDMM
 Fetch Multi Point returns any acquired data along with a timeout error.

Note

#### Waveform Acquisitions

The NI 4070/4071/4072 has a digitizer that can be used to capture
 waveforms.

Use niDMM Configure Waveform Acquisition to configure the
 acquisition and niDMM Read Waveform or niDMM Initiate and niDMM Fetch Waveform to
 retrieve the waveform data.

Note

You can set the maximum length of time (
 Maximum Time) to allow the measurement operation to
 complete. If the measurement operation does not complete within this time interval,
 niDMM Read Waveform or niDMM Fetch Waveform returns any acquired data along with the
 error.

#### Combining Single Point
 Measurements, Multiple Point Measurements, and Waveform Acquisitions in the Same
 Session

You can combine multiple types of acquisitions in the same session. For example, you
 can open a session, read a single point, and then acquire a waveform. You can also
 alternate between single and multiple point measurements, and you can change the
 configuration and acquire a resistance measurement after taking a voltage
 measurement.

The Operation Mode property controls whether the DMM takes
 standard single or multi point measurements, or acquires a waveform.

The
 driver sets the value of this property when you call niDMM Config Measurement or
 niDMM Configure Waveform Acquisition. The Operation Mode property is set to IVIDMM
 MODE when niDMM Config Measurement is called. The driver takes a single point
 measurement if the Trigger Count and niDMM Sample Count properties are both set to
 1. If either of these values has been changed, either by calling niDMM Configure
 Multi Point or by setting the properties directly, the driver takes a multipoint
 measurement. The Operation Mode property is set to WAVEFORM MODE when niDMM
 Configure Waveform Acquisition is called.

If you are programming with
 properties or attributes, you should set the Operation Mode property to the correct
 value before setting other properties for that configuration.

Parent topic:

Programming Flow

Related concepts:

- Single Point Acquisitions

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=acquiring-high-frequency-waveforms.html language=enus -->
## TOPIC 00132: Acquiring High-Frequency Waveforms

- bundle_id: `ni-dmm`
- source_path: `acquiring-high-frequency-waveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/acquiring-high-frequency-waveforms.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When acquiring high-frequency waveforms, call niDMM Initiate before sending the trigger to initiate the signal. The DMM is ready to receive the trigger once you have called niDMM Initiate. This feature is supported on the NI 4080/4081/4082 and the NI 4070/4071/4072. For the NI 4070/4071/4072, the D

### Acquiring High-Frequency Waveforms

When acquiring high-frequency waveforms, call niDMM Initiate before sending the trigger to initiate the signal. The DMM is ready to receive the trigger once you have called niDMM Initiate.

This feature is supported on the NI 4080/4081/4082 and the NI 4070/4071/4072.

Note

Parent topic:

Acquiring Waveforms

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=acquiring-waveforms.html language=enus -->
## TOPIC 00133: Acquiring Waveforms

- bundle_id: `ni-dmm`
- source_path: `acquiring-waveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/acquiring-waveforms.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections provide information about acquiring waveforms:Single Waveform AcquisitionsMultiple Waveform AcquisitionsSynchronizing Waveform MeasurementsAcquiring High-Frequency WaveformsContinuous acquisitions can be performed using waveform mode only on the NI 4080/4081/4082.For more info

### Acquiring Waveforms

The following sections provide information about acquiring waveforms:

- Single Waveform Acquisitions
- Multiple Waveform Acquisitions
- Synchronizing Waveform Measurements
- Acquiring High-Frequency Waveforms

Continuous acquisitions can be performed using waveform mode only on the NI 4080/4081/4082.

For more information about optimizing waveform acquisitions, refer to Waveform Acquisitions.

Note

Parent topic:

Features

Related concepts:

- Single Waveform Acquisitions
- Multiple Waveform Acquisitions
- Synchronizing Waveform Measurements
- Acquiring High-Frequency Waveforms
- Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=adc-calibration.html language=enus -->
## TOPIC 00134: ADC Calibration

- bundle_id: `ni-dmm`
- source_path: `adc-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/adc-calibration.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or

### ADC Calibration

ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.

In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or at resolutions of 4½–5½ digits, ADC calibration is not required for satisfactory performance. When ADC calibration is enabled, every measurement cycle includes an additional phase for acquiring the value of the high-precision reference. This phase yields the most exacting precision because any ADC gain drift is normalized to the input signal, and the ADC gain drift is removed in the resulting mathematical calculation on every measurement.

The following figure represents the process of the ADC calibration cycle. During this cycle, the input is disconnected from the ADC and the precision DC reference is measured. This measurement consists of an ADC calibration Auto Zero (REF LO) and an ADC calibration HI (REF HI). The normalized value of the reference voltage is calculated from V<sub>ref</sub> = REF HI–REF LO.

[IMAGE alt='image' src='GUID-D6C9AA75-5B43-4D0D-A304-F871DADE505D-a5.svg']

Your application may demand speed over accuracy. In these instances, you can disable ADC calibration.

Note

Parent topic:

DMM Measurement Cycle

Related concepts:

- Auto Zero
- Configuring Auto Zero

<!--NI_TOPIC bundle=ni-dmm path=adc-calibration_2.html language=enus -->
## TOPIC 00135: ADC Calibration

- bundle_id: `ni-dmm`
- source_path: `adc-calibration_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/adc-calibration_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or

### ADC Calibration

ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.

In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or at resolutions of 4½–5½ digits, ADC calibration is not required for satisfactory performance. When ADC calibration is enabled, every measurement cycle includes an additional phase for acquiring the value of the high-precision reference. This phase yields the most exacting precision because any ADC gain drift is normalized to the input signal, and the ADC gain drift is removed in the resulting mathematical calculation on every measurement.

The following figure represents the process of the ADC calibration cycle. During this cycle, the input is disconnected from the ADC and the precision DC reference is measured. This measurement consists of an ADC calibration Auto Zero (REF LO) and an ADC calibration HI (REF HI). The normalized value of the reference voltage is calculated from V<sub>ref</sub> = REF HI–REF LO.

[IMAGE alt='image' src='GUID-D6C9AA75-5B43-4D0D-A304-F871DADE505D-a5.svg']

Your application may demand speed over accuracy. In these instances, you can disable ADC calibration.

Note

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=adc-calibration_3.html language=enus -->
## TOPIC 00136: ADC Calibration

- bundle_id: `ni-dmm`
- source_path: `adc-calibration_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/adc-calibration_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or

### ADC Calibration

ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.

In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or at resolutions of 4½–5½ digits, ADC calibration is not required for satisfactory performance. When ADC calibration is enabled, every measurement cycle includes an additional phase for acquiring the value of the high-precision reference. This phase yields the most exacting precision because any ADC gain drift is normalized to the input signal, and the ADC gain drift is removed in the resulting mathematical calculation on every measurement.

The following figure represents the process of the ADC calibration cycle. During this cycle, the input is disconnected from the ADC and the precision DC reference is measured. This measurement consists of an ADC calibration Auto Zero (REF LO) and an ADC calibration HI (REF HI). The normalized value of the reference voltage is calculated from V<sub>ref</sub> = REF HI–REF LO.

[IMAGE alt='image' src='GUID-D6C9AA75-5B43-4D0D-A304-F871DADE505D-a5.svg']

Your application may demand speed over accuracy. In these instances, you can disable ADC calibration.

Note

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=adc-calibration_4.html language=enus -->
## TOPIC 00137: ADC Calibration

- bundle_id: `ni-dmm`
- source_path: `adc-calibration_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/adc-calibration_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or

### ADC Calibration

ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.

In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or at resolutions of 4½–5½ digits, ADC calibration is not required for satisfactory performance. When ADC calibration is enabled, every measurement cycle includes an additional phase for acquiring the value of the high-precision reference. This phase yields the most exacting precision because any ADC gain drift is normalized to the input signal, and the ADC gain drift is removed in the resulting mathematical calculation on every measurement.

The following figure represents the process of the ADC calibration cycle. During this cycle, the input is disconnected from the ADC and the precision DC reference is measured. This measurement consists of an ADC calibration Auto Zero (REF LO) and an ADC calibration HI (REF HI). The normalized value of the reference voltage is calculated from V<sub>ref</sub> = REF HI–REF LO.

[IMAGE alt='image' src='GUID-D6C9AA75-5B43-4D0D-A304-F871DADE505D-a5.svg']

Your application may demand speed over accuracy. In these instances, you can disable ADC calibration.

Note

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=adc-calibration_5.html language=enus -->
## TOPIC 00138: ADC Calibration

- bundle_id: `ni-dmm`
- source_path: `adc-calibration_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/adc-calibration_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or

### ADC Calibration

ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.

In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or at resolutions of 4½–5½ digits, ADC calibration is not required for satisfactory performance. When ADC calibration is enabled, every measurement cycle includes an additional phase for acquiring the value of the high-precision reference. This phase yields the most exacting precision because any ADC gain drift is normalized to the input signal, and the ADC gain drift is removed in the resulting mathematical calculation on every measurement.

The following figure represents the process of the ADC calibration cycle. During this cycle, the input is disconnected from the ADC and the precision DC reference is measured. This measurement consists of an ADC calibration Auto Zero (REF LO) and an ADC calibration HI (REF HI). The normalized value of the reference voltage is calculated from V<sub>ref</sub> = REF HI–REF LO.

[IMAGE alt='image' src='GUID-D6C9AA75-5B43-4D0D-A304-F871DADE505D-a5.svg']

Your application may demand speed over accuracy. In these instances, you can disable ADC calibration.

Note

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=adc-calibration_6.html language=enus -->
## TOPIC 00139: ADC Calibration

- bundle_id: `ni-dmm`
- source_path: `adc-calibration_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/adc-calibration_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or

### ADC Calibration

ADC calibration is a method used to compensate for an internal DMM gain error and allows you to appropriately trade off measurement speed for long-term accuracy.

In DCV and resistance at 6½ or 7½ digit resolutions, NI recommends using ADC calibration for the greatest accuracy. In ACV and current, or at resolutions of 4½–5½ digits, ADC calibration is not required for satisfactory performance. When ADC calibration is enabled, every measurement cycle includes an additional phase for acquiring the value of the high-precision reference. This phase yields the most exacting precision because any ADC gain drift is normalized to the input signal, and the ADC gain drift is removed in the resulting mathematical calculation on every measurement.

The following figure represents the process of the ADC calibration cycle. During this cycle, the input is disconnected from the ADC and the precision DC reference is measured. This measurement consists of an ADC calibration Auto Zero (REF LO) and an ADC calibration HI (REF HI). The normalized value of the reference voltage is calculated from V<sub>ref</sub> = REF HI–REF LO.

[IMAGE alt='image' src='GUID-D6C9AA75-5B43-4D0D-A304-F871DADE505D-a5.svg']

Your application may demand speed over accuracy. In these instances, you can disable ADC calibration.

Note

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=analog-bandwidth.html language=enus -->
## TOPIC 00140: Analog Bandwidth

- bundle_id: `ni-dmm`
- source_path: `analog-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/analog-bandwidth.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured ampli

### Analog Bandwidth

Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured amplitude is 3 dB below the actual amplitude of the signal. This amplitude loss occurs at very low frequencies if the signal is AC coupled and at very high frequencies regardless of coupling. When the signal is DC coupled, the bandwidth of the amplifier extends all the way to the DC voltage. The following figure illustrates the effect of analog bandwidth on a high-frequency signal.

[IMAGE alt='image' src='GUID-24B519E7-FF74-48D1-8473-8B6ED3811001-a5.svg']

As indicated in the specifications, the device has a voltage measurement bandwidth of approximately 300 kHz. This specification means that only signals ≤300 kHz can be accurately acquired. Note that this number is different than the maximum sampling rate of the device (1.8 MS/s). The Nyquist Theorem implies that the maximum signal frequency that can be effectively acquired is 900 kHz. However, the bandwidth actually limits the maximum frequency to 300 kHz. Refer to sample rate for more information.

#### Bandwidth Considerations

The resistance and the capacitance present in the signal path can affect high frequency signals. The larger the capacitance and the resistance, the lower the bandwidth of the signal path. The input capacitance of the device can be found in the device specifications. Note that additional capacitance can be introduced in the cabling that is used, and any other front-end accessories such as switches. This capacitance not only impacts the performance of the waveform acquisition, but can also impact the source of the signal by loading it. Having a low-impedance source and minimal added capacitance is best for optimal operation when acquiring high frequency signals. Use short cable lengths of a low-capacitance, low resistance, and low dielectric absorption for best results.

Parent topic:

Waveform Acquisitions

Related concepts:

- Nyquist Theorem
- Sample Rate

<!--NI_TOPIC bundle=ni-dmm path=analog-bandwidth_2.html language=enus -->
## TOPIC 00141: Analog Bandwidth

- bundle_id: `ni-dmm`
- source_path: `analog-bandwidth_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/analog-bandwidth_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured ampli

### Analog Bandwidth

Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured amplitude is 3 dB below the actual amplitude of the signal. This amplitude loss occurs at very low frequencies if the signal is AC coupled and at very high frequencies regardless of coupling. When the signal is DC coupled, the bandwidth of the amplifier extends all the way to the DC voltage. The following figure illustrates the effect of analog bandwidth on a high-frequency signal.

[IMAGE alt='image' src='GUID-24B519E7-FF74-48D1-8473-8B6ED3811001-a5.svg']

As indicated in the specifications, the device has a voltage measurement bandwidth of approximately 300 kHz. This specification means that only signals ≤300 kHz can be accurately acquired. Note that this number is different than the maximum sampling rate of the device (1.8 MS/s). The Nyquist Theorem implies that the maximum signal frequency that can be effectively acquired is 900 kHz. However, the bandwidth actually limits the maximum frequency to 300 kHz. Refer to sample rate for more information.

#### Bandwidth Considerations

The resistance and the capacitance present in the signal path can affect high frequency signals. The larger the capacitance and the resistance, the lower the bandwidth of the signal path. The input capacitance of the device can be found in the device specifications. Note that additional capacitance can be introduced in the cabling that is used, and any other front-end accessories such as switches. This capacitance not only impacts the performance of the waveform acquisition, but can also impact the source of the signal by loading it. Having a low-impedance source and minimal added capacitance is best for optimal operation when acquiring high frequency signals. Use short cable lengths of a low-capacitance, low resistance, and low dielectric absorption for best results.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=analog-bandwidth_3.html language=enus -->
## TOPIC 00142: Analog Bandwidth

- bundle_id: `ni-dmm`
- source_path: `analog-bandwidth_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/analog-bandwidth_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured ampli

### Analog Bandwidth

Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured amplitude is 3 dB below the actual amplitude of the signal. This amplitude loss occurs at very low frequencies if the signal is AC coupled and at very high frequencies regardless of coupling. When the signal is DC coupled, the bandwidth of the amplifier extends all the way to the DC voltage. The following figure illustrates the effect of analog bandwidth on a high-frequency signal.

[IMAGE alt='image' src='GUID-24B519E7-FF74-48D1-8473-8B6ED3811001-a5.svg']

As indicated in the specifications, the device has a voltage measurement bandwidth of approximately 300 kHz. This specification means that only signals ≤300 kHz can be accurately acquired. Note that this number is different than the maximum sampling rate of the device (1.8 MS/s). The Nyquist Theorem implies that the maximum signal frequency that can be effectively acquired is 900 kHz. However, the bandwidth actually limits the maximum frequency to 300 kHz. Refer to sample rate for more information.

#### Bandwidth Considerations

The resistance and the capacitance present in the signal path can affect high frequency signals. The larger the capacitance and the resistance, the lower the bandwidth of the signal path. The input capacitance of the device can be found in the device specifications. Note that additional capacitance can be introduced in the cabling that is used, and any other front-end accessories such as switches. This capacitance not only impacts the performance of the waveform acquisition, but can also impact the source of the signal by loading it. Having a low-impedance source and minimal added capacitance is best for optimal operation when acquiring high frequency signals. Use short cable lengths of a low-capacitance, low resistance, and low dielectric absorption for best results.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=analog-bandwidth_4.html language=enus -->
## TOPIC 00143: Analog Bandwidth

- bundle_id: `ni-dmm`
- source_path: `analog-bandwidth_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/analog-bandwidth_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured ampli

### Analog Bandwidth

Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured amplitude is 3 dB below the actual amplitude of the signal. This amplitude loss occurs at very low frequencies if the signal is AC coupled and at very high frequencies regardless of coupling. When the signal is DC coupled, the bandwidth of the amplifier extends all the way to the DC voltage. The following figure illustrates the effect of analog bandwidth on a high-frequency signal.

[IMAGE alt='image' src='GUID-24B519E7-FF74-48D1-8473-8B6ED3811001-a5.svg']

As indicated in the specifications, the device has a voltage measurement bandwidth of approximately 300 kHz. This specification means that only signals ≤300 kHz can be accurately acquired. Note that this number is different than the maximum sampling rate of the device (1.8 MS/s). The Nyquist Theorem implies that the maximum signal frequency that can be effectively acquired is 900 kHz. However, the bandwidth actually limits the maximum frequency to 300 kHz. Refer to sample rate for more information.

#### Bandwidth Considerations

The resistance and the capacitance present in the signal path can affect high frequency signals. The larger the capacitance and the resistance, the lower the bandwidth of the signal path. The input capacitance of the device can be found in the device specifications. Note that additional capacitance can be introduced in the cabling that is used, and any other front-end accessories such as switches. This capacitance not only impacts the performance of the waveform acquisition, but can also impact the source of the signal by loading it. Having a low-impedance source and minimal added capacitance is best for optimal operation when acquiring high frequency signals. Use short cable lengths of a low-capacitance, low resistance, and low dielectric absorption for best results.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=analog-bandwidth_5.html language=enus -->
## TOPIC 00144: Analog Bandwidth

- bundle_id: `ni-dmm`
- source_path: `analog-bandwidth_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/analog-bandwidth_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured ampli

### Analog Bandwidth

Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured amplitude is 3 dB below the actual amplitude of the signal. This amplitude loss occurs at very low frequencies if the signal is AC coupled and at very high frequencies regardless of coupling. When the signal is DC coupled, the bandwidth of the amplifier extends all the way to the DC voltage. The following figure illustrates the effect of analog bandwidth on a high-frequency signal.

[IMAGE alt='image' src='GUID-24B519E7-FF74-48D1-8473-8B6ED3811001-a5.svg']

As indicated in the specifications, the device has a voltage measurement bandwidth of approximately 300 kHz. This specification means that only signals ≤300 kHz can be accurately acquired. Note that this number is different than the maximum sampling rate of the device (1.8 MS/s). The Nyquist Theorem implies that the maximum signal frequency that can be effectively acquired is 900 kHz. However, the bandwidth actually limits the maximum frequency to 300 kHz. Refer to sample rate for more information.

#### Bandwidth Considerations

The resistance and the capacitance present in the signal path can affect high frequency signals. The larger the capacitance and the resistance, the lower the bandwidth of the signal path. The input capacitance of the device can be found in the device specifications. Note that additional capacitance can be introduced in the cabling that is used, and any other front-end accessories such as switches. This capacitance not only impacts the performance of the waveform acquisition, but can also impact the source of the signal by loading it. Having a low-impedance source and minimal added capacitance is best for optimal operation when acquiring high frequency signals. Use short cable lengths of a low-capacitance, low resistance, and low dielectric absorption for best results.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=analog-bandwidth_6.html language=enus -->
## TOPIC 00145: Analog Bandwidth

- bundle_id: `ni-dmm`
- source_path: `analog-bandwidth_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/analog-bandwidth_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured ampli

### Analog Bandwidth

Analog bandwidth describes the frequency range (in Hz) in which a signal can be acquired accurately. This limitation is determined by the inherent frequency response of the input path, which causes loss of amplitude and phase information. Analog bandwidth is the frequency at which the measured amplitude is 3 dB below the actual amplitude of the signal. This amplitude loss occurs at very low frequencies if the signal is AC coupled and at very high frequencies regardless of coupling. When the signal is DC coupled, the bandwidth of the amplifier extends all the way to the DC voltage. The following figure illustrates the effect of analog bandwidth on a high-frequency signal.

[IMAGE alt='image' src='GUID-24B519E7-FF74-48D1-8473-8B6ED3811001-a5.svg']

As indicated in the specifications, the device has a voltage measurement bandwidth of approximately 300 kHz. This specification means that only signals ≤300 kHz can be accurately acquired. Note that this number is different than the maximum sampling rate of the device (1.8 MS/s). The Nyquist Theorem implies that the maximum signal frequency that can be effectively acquired is 900 kHz. However, the bandwidth actually limits the maximum frequency to 300 kHz. Refer to sample rate for more information.

#### Bandwidth Considerations

The resistance and the capacitance present in the signal path can affect high frequency signals. The larger the capacitance and the resistance, the lower the bandwidth of the signal path. The input capacitance of the device can be found in the device specifications. Note that additional capacitance can be introduced in the cabling that is used, and any other front-end accessories such as switches. This capacitance not only impacts the performance of the waveform acquisition, but can also impact the source of the signal by loading it. Having a low-impedance source and minimal added capacitance is best for optimal operation when acquiring high frequency signals. Use short cable lengths of a low-capacitance, low resistance, and low dielectric absorption for best results.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=api-ref.html language=enus -->
## TOPIC 00146: NI-DMM API References

- bundle_id: `ni-dmm`
- source_path: `api-ref.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/api-ref.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `reference`
- source_description: Access the NI-DMM API references from the following locations: 20 NI-DMM API References API Reference Installed Location LabVIEW G API Reference C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niDMM\documentation\English\dmmviref.chm C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niDMM\document

### NI-DMM API References

Access the NI-DMM API references from the following locations:

| API Reference | Installed Location |
| --- | --- |
| LabVIEW G API Reference | C:\\Program Files (x86)\\IVI Foundation\\IVI\\Drivers\\niDMM\\documentation\\English\\dmmviref.chm C:\\Program Files (x86)\\IVI Foundation\\IVI\\Drivers\\niDMM\\documentation\\English\\dmmpropref |
| C/CVI/VB API Reference | C:\\Program Files (x86)\\IVI Foundation\\IVI\\Drivers\\niDMM\\documentation\\dmmcref.chm |
| C# .NET API Reference | C:\\Program Files (x86)\\IVI Foundation\\IVI\\Drivers\\niDMM\\documentation\\English\\NINETDMMFx40.chm C:\\Program Files (x86)\\IVI Foundation\\IVI\\Drivers\\niDMM\\documentation\\English\\NINETDMMFx45Ref.chm |
| NI-ModInst API Reference | C:\\Program Files (x86)\\IVI Foundation\\IVI\\Drivers\\niModInst\\documentation\\niModInst.chm |

You can also access the NI-DMM API references on ni.com/docs.

Parent topic:

Programming with NI-DMM

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help
- NI-DMM .NET API Overview
- NI-DMM C Function Reference Help
- NI-ModInst Help

<!--NI_TOPIC bundle=ni-dmm path=auto-zero.html language=enus -->
## TOPIC 00147: Auto Zero

- bundle_id: `ni-dmm`
- source_path: `auto-zero.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/auto-zero.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Auto Zero is a method used to compensate for internal DMM offsets. For NI 4065 devices, Auto Zero is always ON. Auto Zero is an integral part of the signal measurement phase and adds no extra time to the overall measurement.When Auto Zero is enabled, the internal DMM input is connected to its input

### Auto Zero

Auto Zero is a method used to compensate for internal DMM offsets.

Note

When Auto Zero is enabled, the internal DMM input is connected to its input LO and measured. The subsequent input signal is measured, and the Auto Zero value subtracted from it. Thus, any offsets in the measurement path or ADC are subtracted from the signal, correcting for the offsets. You can disable Auto Zero before initiating or reading a measurement; it remains disabled until you enable it again.

When you disable Auto Zero, the DMM restores the Auto Zero value from the previous self-calibration.

If you find the offset to be unacceptable, you can either subtract it algorithmically in a later process, such as by shorting the inputs and recording it, or you can run self-calibration, which calculates and stores new Auto Zero offsets. To maintain stable offset performance in high resolution modes (for example, 6½ or 7½ digit resolution) you should enable Auto Zero.

You can also enable Auto Zero ONCE. Auto Zero ONCE is equivalent to Auto Zero ON if you perform a single point acquisition with the Number of Averages set to 1. If you are performing a multiple point acquisition, enabling Auto Zero ONCE will cause the DMM to perform Auto Zero only during the first measurement cycle for each acquisition. Using Auto Zero ONCE can reduce total acquisition time.

Note

NI recommends using Auto Zero ONCE only for multiple measurements taken on the same range. If you enable Auto Zero ONCE for an Auto Range measurement, Auto Zero ON is used to ensure that the correct Auto Zero value is applied to each range.

Parent topic:

DMM Measurement Cycle

Related concepts:

- Self-Calibration
- Configuring Auto Zero

<!--NI_TOPIC bundle=ni-dmm path=auto-zero_2.html language=enus -->
## TOPIC 00148: Auto Zero

- bundle_id: `ni-dmm`
- source_path: `auto-zero_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/auto-zero_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Auto Zero is a method used to compensate for internal DMM offsets. For NI 4065 devices, Auto Zero is always ON. Auto Zero is an integral part of the signal measurement phase and adds no extra time to the overall measurement.When Auto Zero is enabled, the internal DMM input is connected to its input

### Auto Zero

Auto Zero is a method used to compensate for internal DMM offsets.

Note

When Auto Zero is enabled, the internal DMM input is connected to its input LO and measured. The subsequent input signal is measured, and the Auto Zero value subtracted from it. Thus, any offsets in the measurement path or ADC are subtracted from the signal, correcting for the offsets. You can disable Auto Zero before initiating or reading a measurement; it remains disabled until you enable it again.

When you disable Auto Zero, the DMM restores the Auto Zero value from the previous self-calibration.

If you find the offset to be unacceptable, you can either subtract it algorithmically in a later process, such as by shorting the inputs and recording it, or you can run self-calibration, which calculates and stores new Auto Zero offsets. To maintain stable offset performance in high resolution modes (for example, 6½ or 7½ digit resolution) you should enable Auto Zero.

You can also enable Auto Zero ONCE. Auto Zero ONCE is equivalent to Auto Zero ON if you perform a single point acquisition with the Number of Averages set to 1. If you are performing a multiple point acquisition, enabling Auto Zero ONCE will cause the DMM to perform Auto Zero only during the first measurement cycle for each acquisition. Using Auto Zero ONCE can reduce total acquisition time.

Note

NI recommends using Auto Zero ONCE only for multiple measurements taken on the same range. If you enable Auto Zero ONCE for an Auto Range measurement, Auto Zero ON is used to ensure that the correct Auto Zero value is applied to each range.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=auto-zero_3.html language=enus -->
## TOPIC 00149: Auto Zero

- bundle_id: `ni-dmm`
- source_path: `auto-zero_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/auto-zero_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Auto Zero is a method used to compensate for internal DMM offsets. For NI 4065 devices, Auto Zero is always ON. Auto Zero is an integral part of the signal measurement phase and adds no extra time to the overall measurement.When Auto Zero is enabled, the internal DMM input is connected to its input

### Auto Zero

Auto Zero is a method used to compensate for internal DMM offsets.

Note

When Auto Zero is enabled, the internal DMM input is connected to its input LO and measured. The subsequent input signal is measured, and the Auto Zero value subtracted from it. Thus, any offsets in the measurement path or ADC are subtracted from the signal, correcting for the offsets. You can disable Auto Zero before initiating or reading a measurement; it remains disabled until you enable it again.

When you disable Auto Zero, the DMM restores the Auto Zero value from the previous self-calibration.

If you find the offset to be unacceptable, you can either subtract it algorithmically in a later process, such as by shorting the inputs and recording it, or you can run self-calibration, which calculates and stores new Auto Zero offsets. To maintain stable offset performance in high resolution modes (for example, 6½ or 7½ digit resolution) you should enable Auto Zero.

You can also enable Auto Zero ONCE. Auto Zero ONCE is equivalent to Auto Zero ON if you perform a single point acquisition with the Number of Averages set to 1. If you are performing a multiple point acquisition, enabling Auto Zero ONCE will cause the DMM to perform Auto Zero only during the first measurement cycle for each acquisition. Using Auto Zero ONCE can reduce total acquisition time.

Note

NI recommends using Auto Zero ONCE only for multiple measurements taken on the same range. If you enable Auto Zero ONCE for an Auto Range measurement, Auto Zero ON is used to ensure that the correct Auto Zero value is applied to each range.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=auto-zero_4.html language=enus -->
## TOPIC 00150: Auto Zero

- bundle_id: `ni-dmm`
- source_path: `auto-zero_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/auto-zero_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Auto Zero is a method used to compensate for internal DMM offsets. For NI 4065 devices, Auto Zero is always ON. Auto Zero is an integral part of the signal measurement phase and adds no extra time to the overall measurement.When Auto Zero is enabled, the internal DMM input is connected to its input

### Auto Zero

Auto Zero is a method used to compensate for internal DMM offsets.

Note

When Auto Zero is enabled, the internal DMM input is connected to its input LO and measured. The subsequent input signal is measured, and the Auto Zero value subtracted from it. Thus, any offsets in the measurement path or ADC are subtracted from the signal, correcting for the offsets. You can disable Auto Zero before initiating or reading a measurement; it remains disabled until you enable it again.

When you disable Auto Zero, the DMM restores the Auto Zero value from the previous self-calibration.

If you find the offset to be unacceptable, you can either subtract it algorithmically in a later process, such as by shorting the inputs and recording it, or you can run self-calibration, which calculates and stores new Auto Zero offsets. To maintain stable offset performance in high resolution modes (for example, 6½ or 7½ digit resolution) you should enable Auto Zero.

You can also enable Auto Zero ONCE. Auto Zero ONCE is equivalent to Auto Zero ON if you perform a single point acquisition with the Number of Averages set to 1. If you are performing a multiple point acquisition, enabling Auto Zero ONCE will cause the DMM to perform Auto Zero only during the first measurement cycle for each acquisition. Using Auto Zero ONCE can reduce total acquisition time.

Note

NI recommends using Auto Zero ONCE only for multiple measurements taken on the same range. If you enable Auto Zero ONCE for an Auto Range measurement, Auto Zero ON is used to ensure that the correct Auto Zero value is applied to each range.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=auto-zero_5.html language=enus -->
## TOPIC 00151: Auto Zero

- bundle_id: `ni-dmm`
- source_path: `auto-zero_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/auto-zero_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Auto Zero is a method used to compensate for internal DMM offsets. For NI 4065 devices, Auto Zero is always ON. Auto Zero is an integral part of the signal measurement phase and adds no extra time to the overall measurement.When Auto Zero is enabled, the internal DMM input is connected to its input

### Auto Zero

Auto Zero is a method used to compensate for internal DMM offsets.

Note

When Auto Zero is enabled, the internal DMM input is connected to its input LO and measured. The subsequent input signal is measured, and the Auto Zero value subtracted from it. Thus, any offsets in the measurement path or ADC are subtracted from the signal, correcting for the offsets. You can disable Auto Zero before initiating or reading a measurement; it remains disabled until you enable it again.

When you disable Auto Zero, the DMM restores the Auto Zero value from the previous self-calibration.

If you find the offset to be unacceptable, you can either subtract it algorithmically in a later process, such as by shorting the inputs and recording it, or you can run self-calibration, which calculates and stores new Auto Zero offsets. To maintain stable offset performance in high resolution modes (for example, 6½ or 7½ digit resolution) you should enable Auto Zero.

You can also enable Auto Zero ONCE. Auto Zero ONCE is equivalent to Auto Zero ON if you perform a single point acquisition with the Number of Averages set to 1. If you are performing a multiple point acquisition, enabling Auto Zero ONCE will cause the DMM to perform Auto Zero only during the first measurement cycle for each acquisition. Using Auto Zero ONCE can reduce total acquisition time.

Note

NI recommends using Auto Zero ONCE only for multiple measurements taken on the same range. If you enable Auto Zero ONCE for an Auto Range measurement, Auto Zero ON is used to ensure that the correct Auto Zero value is applied to each range.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=auto-zero_6.html language=enus -->
## TOPIC 00152: Auto Zero

- bundle_id: `ni-dmm`
- source_path: `auto-zero_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/auto-zero_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Auto Zero is a method used to compensate for internal DMM offsets. For NI 4065 devices, Auto Zero is always ON. Auto Zero is an integral part of the signal measurement phase and adds no extra time to the overall measurement.When Auto Zero is enabled, the internal DMM input is connected to its input

### Auto Zero

Auto Zero is a method used to compensate for internal DMM offsets.

Note

When Auto Zero is enabled, the internal DMM input is connected to its input LO and measured. The subsequent input signal is measured, and the Auto Zero value subtracted from it. Thus, any offsets in the measurement path or ADC are subtracted from the signal, correcting for the offsets. You can disable Auto Zero before initiating or reading a measurement; it remains disabled until you enable it again.

When you disable Auto Zero, the DMM restores the Auto Zero value from the previous self-calibration.

If you find the offset to be unacceptable, you can either subtract it algorithmically in a later process, such as by shorting the inputs and recording it, or you can run self-calibration, which calculates and stores new Auto Zero offsets. To maintain stable offset performance in high resolution modes (for example, 6½ or 7½ digit resolution) you should enable Auto Zero.

You can also enable Auto Zero ONCE. Auto Zero ONCE is equivalent to Auto Zero ON if you perform a single point acquisition with the Number of Averages set to 1. If you are performing a multiple point acquisition, enabling Auto Zero ONCE will cause the DMM to perform Auto Zero only during the first measurement cycle for each acquisition. Using Auto Zero ONCE can reduce total acquisition time.

Note

NI recommends using Auto Zero ONCE only for multiple measurements taken on the same range. If you enable Auto Zero ONCE for an Auto Range measurement, Auto Zero ON is used to ensure that the correct Auto Zero value is applied to each range.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=auto-zero_7.html language=enus -->
## TOPIC 00153: Auto Zero

- bundle_id: `ni-dmm`
- source_path: `auto-zero_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/auto-zero_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Auto Zero is a method used to compensate for internal DMM offsets. For NI 4065 devices, Auto Zero is always ON. Auto Zero is an integral part of the signal measurement phase and adds no extra time to the overall measurement.When Auto Zero is enabled, the internal DMM input is connected to its input

### Auto Zero

Auto Zero is a method used to compensate for internal DMM offsets.

Note

When Auto Zero is enabled, the internal DMM input is connected to its input LO and measured. The subsequent input signal is measured, and the Auto Zero value subtracted from it. Thus, any offsets in the measurement path or ADC are subtracted from the signal, correcting for the offsets. You can disable Auto Zero before initiating or reading a measurement; it remains disabled until you enable it again.

When you disable Auto Zero, the DMM restores the Auto Zero value from the previous self-calibration.

If you find the offset to be unacceptable, you can either subtract it algorithmically in a later process, such as by shorting the inputs and recording it, or you can run self-calibration, which calculates and stores new Auto Zero offsets. To maintain stable offset performance in high resolution modes (for example, 6½ or 7½ digit resolution) you should enable Auto Zero.

You can also enable Auto Zero ONCE. Auto Zero ONCE is equivalent to Auto Zero ON if you perform a single point acquisition with the Number of Averages set to 1. If you are performing a multiple point acquisition, enabling Auto Zero ONCE will cause the DMM to perform Auto Zero only during the first measurement cycle for each acquisition. Using Auto Zero ONCE can reduce total acquisition time.

Note

NI recommends using Auto Zero ONCE only for multiple measurements taken on the same range. If you enable Auto Zero ONCE for an Auto Range measurement, Auto Zero ON is used to ensure that the correct Auto Zero value is applied to each range.

Parent topic:

NI 4065 DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=burden-voltage.html language=enus -->
## TOPIC 00154: Burden Voltage

- bundle_id: `ni-dmm`
- source_path: `burden-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/burden-voltage.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Burden voltage is the voltage drop caused by current flowing through a current measuring device. A large burden voltage can affect the circuit being measured, corrupting the measurement. For this reason, it is desirable for burden voltage to be kept as low as possible.The following figure shows a 1.

### Burden Voltage

Burden voltage is the voltage drop caused by current flowing through a current measuring device. A large burden voltage can affect the circuit being measured, corrupting the measurement. For this reason, it is desirable for burden voltage to be kept as low as possible.

The following figure shows a 1.5 V source with a 5 Ω load. To measure the current on the circuit, an ammeter is connected in series with the circuit. In this figure, the ammeter has a 0.5 V burden voltage.

[IMAGE alt='image' src='GUID-92C0ED7F-8AA7-4F18-A912-B0BEA554A12C-a5.svg']

Without burden voltage (figure a), the calculated current is:

I<sub>actual</sub> = 1.5 V / 5 Ω

I<sub>actual</sub> = 0.3 A

With burden voltage (figure b), the current in this circuit equals:

I<sub>measured</sub> = (1.5 V-0.5 V ) / (5 Ω)

I<sub>measured</sub> = 0.2 A

In the figure above, burden voltage of the current measuring device subtracts from the voltage across the 5 Ω resistor. The result is a significant error in the measurement. In this case, the error caused by the burden voltage is 33%. Problems like this can easily crop up when using a shunt resistor to measure the current drawn by logic voltages <3.3 V common in today's digital systems.

For the maximum burden voltage per range, refer to Related Documentation for the specifications documents for the DMMs.

A more complete model of the burden voltage in a DMM is shown in the image below. In this model, you can see that the connections between the DUT and the DMM can also introduce an error into the measurement.

[IMAGE alt='image' src='GUID-EBF2E9F3-E08C-470D-9109-24639A4FB820-a5.svg']

The burden voltage listed in the specifications documents takes into account the voltage drop on the resistance of the ammeter shunt plus the contact and fuse resistances. Usually, the specifications of the DMMs list the maximum burden voltages per range. As a general rule, you should take into account the error introduced by burden voltage if the voltage drop on the source impedance and on the connecting leads is comparable to the burden voltage.

Refer to Related Documentation for the NI 4065 Specifications, the NI 4070/4072 Specifications, and the NI 4071 Specifications, which list the burden voltage specifications.

If the source impedance and leads in your system make the error introduced by the burden voltage relevant, then the measured current is equal to the following equation:

I (5 Ω + R<sub>LEAD1</sub> + R<sub>LEAD2</sub>) + V<sub>BURDEN</sub> = 1.5 V

I<sub>measured</sub> = (1.5 V - V<sub>BURDEN</sub>) / (5 Ω + R<sub>LEAD1</sub> + R <sub>LEAD2</sub>)

Recall that the DMM specifications documents list the maximum burden voltage per range. However, if you are measuring at less than full scale, then the actual burden voltage is lower. In this case, you can calculate the actual burden voltage according to the following equation:

Actual V<sub>BURDEN</sub> = V<sub>BURDEN</sub> * (I<sub>measured</sub>/I<sub>full scale</sub>),

where I<sub>full scale</sub> corresponds to the current range that you are using

Possible techniques to reduce error caused by ammeter burden voltage include the following:

- When using the current function within the DMM, keep leads to the ammeter short and use the appropriate gauge of cable to minimize voltage drops from leads.
- Sense remotely with external shunts to eliminate the need for long current-carrying cables to the DMM. Use the lowest value of shunt resistance that the measurement allows.
- Use wires in the circuit under test as resistance shunts. Measure the voltage drop across the
 wire. Then, use the Offset Compensated Ohms feature to measure the
 resistance of the wire, and calculate I = V wire /R oco .

Note

Parent topic:

Measurement Considerations

Related concepts:

- Offset Compensated Ohms

<!--NI_TOPIC bundle=ni-dmm path=chassis.html language=enus -->
## TOPIC 00155: Chassis

- bundle_id: `ni-dmm`
- source_path: `chassis.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/chassis.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section specifies the recommended chassis components and conditions for a system that includes NI DMMs.PXI Chassis RecommendationsThe NI PXI-4070/4071/4072 and NI PXI-4065 are designed to operate in any PXI-compliant chassis. Normal operating conditions for these DMMs include the following:All

### Chassis

This section specifies the recommended chassis components and conditions for a system that
 includes NI DMMs.

#### PXI Chassis Recommendations

The NI PXI-4070/4071/4072 and NI PXI-4065 are designed to operate in any PXI-compliant chassis. Normal operating conditions for these DMMs include the following:

- All PXI filler panels must be installed in empty slots.
- The PXI chassis fans that provide forced air must remain unobstructed to allow for proper cooling of the PXI chassis, devices, and controller.
- (Optional) Clean the chassis fan filters at least every six months. Some chassis include fan filters. Depending on the amount of chassis use and the ambient dust levels, filters might require more frequent cleaning. If regular maintenance of dirty or clogged filters is not possible, you can remove the filters to maintain adequate cooling.
- Temperature rise on a module within a chassis can vary with slot position. You can keep this variation to a minimum by taking the precautions listed above.

#### PXI Express Chassis

Some PXI Express chassis provide hybrid slots. A hybrid slot can accept either PXI Express modules or PXI Express compatible modules, but not standard PXI modules. To determine if your chassis contains hybrid slots, refer to your chassis documentation. For more information about hybrid slots, refer to the related Web topic PXI Express FAQ.

Refer to PXI Express Compatibility, to determine if your DMM is PXI or PXI Express compatible and for more information about PXI Express compatibility.

#### PCI Chassis Recommendations

The NI PCI-4070 and NI PCI/PCIe-4065 are designed to operate in any ATX-compliant industrial or personal computer. Normal operating conditions for these DMMs include the following:

- All covers for the industrial chassis or personal computer must be installed.
- All PCI filler panels must be installed to close off unused PCI slots. Caution For optimal electromagnetic
 compatibility (EMC) performance and input protection, you
 must install the front panel screw.
- The PCI front panel bracket on the NI PCI/PCIe-4065 and NI PCI-4070 must have a firm, direct, metal-to-metal mounting connection to ensure proper grounding. Some computer manufacturers use a securing lever made of plastic; such a lever is unacceptable for safety reasons and must be removed. The PCI devices must be screwed down. If the chassis does not meet these requirements, you must use a different computer chassis.

The cooling capability in most industrial and personal computers is less effective than the cooling capability in a PXI chassis. The NI PCI/PCIe-4065 dissipates low enough power that additional cooling is not needed in most computers. The NI PCI-4070 dissipates higher power, and NI strongly recommends that NI PCI-4070 users implement the following precautions to maximize the cooling capability of the computer:

- Install an additional 80 mm, 32 cubic ft/min (CFM) fan that forces air towards the NI PCI-4070.
 Most computer chassis contain one or two mounting locations for this type of
 fan. These fans are inexpensive and readily available at most computer supply
 stores. Note If the hard drive mounts vertically in front of the fan mounting location(s) in the computer chassis, you must move the hard drive to a horizontal 3.5 inch drive bay or to another suitable location that does not obstruct the fan mounting location(s).
- Add additional fans, such as PCI fan cards and chassis fans, to increase the air circulation inside the computer.

Parent topic:

Integration and System Considerations

Related concepts:

- PXI Express Compatibility

<!--NI_TOPIC bundle=ni-dmm path=close.html language=enus -->
## TOPIC 00156: Close

- bundle_id: `ni-dmm`
- source_path: `close.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/close.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your program finishes, terminate the session with niDMM Close.niDMM Close is essential for freeing resources, including deallocating memory, destroying threads, and freeing operating system resources. Every session that you initialize must be closed, even if an error occurs during your program.

### Close

When your program finishes, terminate the session with niDMM Close.

niDMM Close is essential for freeing resources, including deallocating memory, destroying threads, and freeing operating system resources. Every session that you initialize must be closed, even if an error occurs during your program. While debugging your application, you can abort execution before it reaches niDMM Close. While aborting execution should not cause problems, it is not recommended.

Parent topic:

Programming Flow

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=common-mode-rejection-ratio-cmrr.html language=enus -->
## TOPIC 00157: Common-Mode Rejection Ratio (CMRR)

- bundle_id: `ni-dmm`
- source_path: `common-mode-rejection-ratio-cmrr.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/common-mode-rejection-ratio-cmrr.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Common-mode rejection ratio (CMRR) describes the ability of the DMM to reject a common-mode signal and is often specified with a 1 kΩ resistance in the LO input lead, as shown in the following figure.CMRR is important because it indicates how much of the common-mode signal affects your measurement.

### Common-Mode Rejection Ratio (CMRR)

Common-mode rejection ratio (CMRR) describes the ability of the DMM to reject a common-mode signal and is often specified with a 1 kΩ resistance in the LO input lead, as shown in the following figure.

[IMAGE alt='image' src='GUID-0AC74FBD-E5FC-4683-A4C2-1480ADCA7193-a5.svg']

CMRR is important because it indicates how much of the common-mode signal affects your measurement. The CMRR is defined by the following equation:

CMRR = 20*log<sub>10</sub>(Differential Gain/Common-Mode Gain)

For example, if you are measuring a thermocouple in a noisy environment, the noise from the environment appears on both input leads. Therefore, this noise is a common-mode signal that is rejected by the CMRR of the instrument.

Parent topic:

Measurement Considerations

Related concepts:

- Normal and Common-Mode Signals

<!--NI_TOPIC bundle=ni-dmm path=configure-waveform-coupling.html language=enus -->
## TOPIC 00158: Configure Waveform Coupling

- bundle_id: `ni-dmm`
- source_path: `configure-waveform-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/configure-waveform-coupling.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the coupling for a voltage waveform acquisition by choosing one of the following:LabVIEW—Use niDMM Configure Waveform Coupling.CVI, C++, or Visual Basic—Use niDMM_ConfigureWaveformCoupling function. Values Description AC (1) Configures AC coupling of the input signal. DC (0) Configures DC

### Configure Waveform Coupling

Configure the coupling for a voltage waveform acquisition by choosing one of the following:

LabVIEW—Use niDMM Configure Waveform Coupling.CVI, C++, or Visual Basic—Use niDMM_ConfigureWaveformCoupling function.

| Values | Description |
| --- | --- |
| AC (1) | Configures AC coupling of the input signal. |
| DC (0) | Configures DC coupling of the input signal. |

Note

Parent topic:

Features

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=configuring-adc-calibration.html language=enus -->
## TOPIC 00159: Configuring ADC Calibration

- bundle_id: `ni-dmm`
- source_path: `configuring-adc-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/configuring-adc-calibration.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure ADC calibration by completing the following steps:LabVIEW Insert niDMM Configure ADC Calibration into the block diagram. Set ADC Calibration to the desired input value (refer to the following table). CVI/C++/Visual Basic Insert niDMM_ConfigureADCCalibration into the program. Set ADC Calibr

### Configuring ADC Calibration

Configure ADC calibration by completing the following steps:

- LabVIEW
  1. Insert niDMM Configure ADC Calibration into the block diagram.
  2. Set ADC Calibration to the desired input value (refer to the following table).
- CVI/C++/Visual Basic
  1. Insert niDMM_ConfigureADCCalibration into the program.
  2. Set ADC Calibration to the desired input value (refer to the following table).

| Values | Description |
| --- | --- |
| Values | Description |
| AUTO (-1) | The driver chooses the ADC calibration setting based on the configured function and resolution. |
| ON (1) | Enables ADC Calibration. |
| OFF (0) | Disables ADC Calibration. |

Note

Parent topic:

Features

Related concepts:

- ADC Calibration

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=configuring-auto-range.html language=enus -->
## TOPIC 00160: Configuring Auto Range

- bundle_id: `ni-dmm`
- source_path: `configuring-auto-range.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/configuring-auto-range.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Auto Range allows you to measure a signal when you do not know which range to select. The DMM takes a series of measurements and adjusts the range until the measurement falls within the smallest range appropriate for that measurement.Auto Range uses the configuration you specify. Refer to the Measur

### Configuring Auto Range

Auto Range allows you to measure a signal when you do not know which range to select. The DMM takes a series of measurements and adjusts the range until the measurement falls within the smallest range appropriate for that measurement.

Auto Range uses the configuration you specify. Refer to the Measurement Defaults section for your device for more information on the configuration of Auto Range measurements.

Note

- The NI 4080/4081/4082 does not support Auto Range for Frequency
 Voltage.
- For the NI 4065 and NI 4070/4071/4072, Auto Range uses the same
 configuration as 5½–digit measurements.
- The NI 4081 does not support Auto Range when the input impedance is greater
 than 10 GΩ .
- Auto Range does not adjust for the extended 200 MΩ range in 2-wire
 resistance measurements.
- On the NI 4080/4081/4082 and NI 4070/4071/4072, Auto Range is unavailable
 during diode measurements and waveform acquisitions.
- Auto Range reduces the reading rate of your measurements because the DMM
 takes an Auto Range reading before each measurement.
- The NI 4065 only supports Auto Range when the trigger and sample trigger are
 set to IMMEDIATE.
- DC current Auto Range on the NI 4081 and NI 4071 does not 
 support the 1 µA and 10 µA ranges. For low currents, the NI 4081 and NI 4071
 only Auto Ranges down to 100 µA. This behavior prevents an electromechanical
 relay from switching between these ranges (especially when high-compliance
 voltages could be present) thereby lengthening the life of the relay.
- Auto Range is not supported for inductance or capacitance measurements.
 Inductance and capacitance measurements are only 
 supported on the NI 4082 and NI 4072.

To enable Auto Range, complete the following steps:

- LabVIEW
  1. Insert niDMM Config Measurement into the block diagram.
  2. Set Range to the desired Auto Range value (refer to the following table).
- CVI/C++/Visual Basic
  1. Use niDMM_ConfigureMeasurementDigits .
  2. Set Range to the desired Auto Range value (refer to the following table).

| Values | Description |
| --- | --- |
| ON (–1) | An Auto Range measurement is performed prior to each measurement. |
| OFF (–2) | Use after a measurement that used Auto Range ON to set the DMM to the currently selected range. |
| ONCE (–3) | NI-DMM picks a range for the first point and uses that range for the remaining measurements. |

Tip

Parent topic:

Features

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=configuring-auto-zero.html language=enus -->
## TOPIC 00161: Configuring Auto Zero

- bundle_id: `ni-dmm`
- source_path: `configuring-auto-zero.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/configuring-auto-zero.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To enable, enable once, or disable Auto Zero: The NI 4065 only supports the ON setting. For NI 4065 devices, Auto Zero is always ON. Auto Zero is an integral part of the signal measurement phase and adds no extra time to the overall measurement.LabVIEW—Use niDMM Configure Auto Zero. CVI, C++, or V

### Configuring Auto Zero

To enable, enable once, or disable Auto Zero:

Note

LabVIEW—Use niDMM Configure Auto Zero.

CVI, C++, or Visual Basic—Use
 niDMM_ConfigureAutoZeroMode.

| AUTO (default) | -1 | NI-DMM chooses the Auto Zero setting based on the configured function and resolution. |
| --- | --- | --- |
| OFF | 0 | Disables Auto Zero. |
| ON | 1 | The DMM internally disconnects the input signal following each measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading. |
| ONCE | 2 | The DMM internally disconnects the input signal for the first measurement and takes a zero reading. It then subtracts the zero reading from the first reading and the following readings. |

Parent topic:

Features

Related concepts:

- Auto Zero

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=configuring-frequency-measurements.html language=enus -->
## TOPIC 00162: Configuring Frequency Measurements

- bundle_id: `ni-dmm`
- source_path: `configuring-frequency-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/configuring-frequency-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure a frequency measurement, complete the following steps:LabVIEW Use niDMM Config Measurement.Set Measurement Function to Frequency.Set Range to specify the minimum AC frequency. The DMM uses the range to calculate the aperture time.Use niDMM Configure Frequency Voltage Range. Set Frequency V

### Configuring Frequency Measurements

Configure a frequency measurement, complete the following steps:

- LabVIEW
  1. Use niDMM Config Measurement.
  2. Set Measurement Function to Frequency.
  3. Set Range to specify the minimum AC frequency. The DMM uses the range to calculate the aperture time.
  4. Use niDMM Configure Frequency Voltage Range.
  5. Set Frequency Voltage Range to the AC V range of your input signal.
- CVI/C++/Visual Basic
  1. Use niDMM_ConfigureMeasurementDigits .
  2. Set Measurement Function to NIDMM_VAL_FREQ.
  3. Set Range to specify the minimum AC frequency. The DMM uses the range to calculate the aperture time.
  4. Use niDMM_ConfigureFrequencyVoltageRange .
  5. Set Frequency Voltage Range to the AC V range of your input signal.

Note

Parent topic:

Features

Related concepts:

- Frequency/Period

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=configuring-input-resistance.html language=enus -->
## TOPIC 00163: Configuring Input Resistance

- bundle_id: `ni-dmm`
- source_path: `configuring-input-resistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/configuring-input-resistance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select the input resistance by choosing one of the following:LabVIEW—Use the Input Resistance property to set the input resistance.CVI, C++, or Visual Basic—Use niDMM_SetAttributeViReal64 to set the desired value for the NIDMM_ATTR_INPUT_RESISTANCE attribute. This feature is supported on the NI 408

### Configuring Input Resistance

Select the input resistance by choosing one of the following:

LabVIEW—Use the Input Resistance property to set the input resistance.CVI, C++, or Visual Basic—Use niDMM_SetAttributeViReal64 to set the desired value for the NIDMM_ATTR_INPUT_RESISTANCE attribute.

Note

Parent topic:

Features

Related concepts:

- Input Resistance

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=configuring-measurement-timing.html language=enus -->
## TOPIC 00164: Configuring Measurement Timing

- bundle_id: `ni-dmm`
- source_path: `configuring-measurement-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/configuring-measurement-timing.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the resolution-based DMM measurement times selected by the driver are not acceptable for your application, you can set the aperture and/or settling times for the measurement directly using properties.You can specify the aperture time in either seconds or powerline cycles. Set the Aperture Time Un

### Configuring Measurement Timing

If the resolution-based DMM measurement times selected by the driver are not acceptable for your application, you can set the aperture and/or settling times for the measurement directly using properties.

You can specify the aperture time in either seconds or powerline cycles. Set the Aperture Time Units property to the appropriate setting. If you choose powerline cycles as the unit, specify the Powerline Frequency using either niDMM Configure Powerline Frequency or the Powerline Frequency property. Set the Aperture Time property to the desired value. If the requested aperture time is less than the minimum required value, the driver uses the minimum value instead of the requested value.

Note

To configure the settling time for a measurement or a waveform acquisition, set the Settle Time property. The settling time is specified in seconds. If the requested settling time is less than the minimum required value, the driver uses the minimum value instead of the requested value.

When the aperture time is explicitly set, the absolute resolution value is ignored. The effective resolution is determined by the chosen aperture. To reset the aperture or settling time, set these properties to Auto Selection (-1). Calling niDMM Config Measurement resets the aperture time to Auto. This allows the driver to program the hardware using the requested resolution.

When you set the aperture time directly, you may also want to set the Auto Zero, ADC calibration, and DC noise rejection values. These properties default to Auto Selection (-1). When the aperture is set, the driver disables Auto Zero and ADC Calibration and uses the Normal DC Noise Rejection setting. If you desire different values, set these properties to the desired setting. Reset the values to Auto Selection when you want the driver to choose the setting for these properties.

Note

To select the measurement time:

- LabVIEW
  1. Set the Aperture Time Units property in seconds or powerline cycles.
  2. Use the Aperture Time property.
- CVI/C++/Visual Basic
  1. Use niDMM_SetAttributeViInt32 to set the desired value for the Aperture Time Units attribute.
  2. Use the niDMM_SetAttributeViReal64 function to set the desired value for the Aperture Time attribute.

#### Averaging

During single or
 multipoint measurements with long aperture times, several shorter measurements can
 be taken with a new Auto Zero offset applied to each measurement to compensate for
 drift. To specify the number of averages in a
 measurement:

- LabVIEW
  1. Enable Auto
 Zero.
  2. Set the Number Of Averages property.
- CVI/C++/Visual Basic
  1. Enable Auto
 Zero.
  2. Use the niDMM_SetAttributeViReal64 function to set the
 desired value for the NIDMM_ATTR_NUMBER_OF_AVERAGES 
 attribute.

Note

Parent topic:

Features

Related concepts:

- Aperture Time
- Configuring Auto Zero

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=configuring-offset-compensated-ohms.html language=enus -->
## TOPIC 00165: Configuring Offset Compensated Ohms

- bundle_id: `ni-dmm`
- source_path: `configuring-offset-compensated-ohms.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/configuring-offset-compensated-ohms.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, offset compensated ohms is disabled. Enable or disable offset compensated ohms by choosing one of the following:LabVIEW—Use niDMM Configure Offset Comp Ohms.CVI, C++, or Visual Basic—Use niDMM_ConfigureCompOhms. This feature is supported on the NI 4080/4081/4082 and the NI 4070/4071/407

### Configuring Offset Compensated Ohms

By default, offset compensated ohms is disabled. Enable or disable offset compensated ohms by choosing one of the following:

LabVIEW—Use niDMM Configure Offset Comp Ohms.CVI, C++, or Visual Basic—Use niDMM_ConfigureCompOhms.

Note

Parent topic:

Features

Related concepts:

- Offset Compensated Ohms

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=configuring-period-measurements.html language=enus -->
## TOPIC 00166: Configuring Period Measurements

- bundle_id: `ni-dmm`
- source_path: `configuring-period-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/configuring-period-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure a period measurement by completing the following steps: If you specify Auto Range (-1.0) for the period range, the DMM defaults to a 2 second aperture time.LabVIEW Use niDMM Config Measurement.Set Measurement Function to Period.Set Range to the maximum expected period in seconds. The DMM

### Configuring Period Measurements

Configure a period measurement by completing the following steps:

Note

- LabVIEW
  1. Use niDMM Config Measurement.
  2. Set Measurement Function to Period.
  3. Set Range to the maximum expected period in seconds. The DMM uses the range to calculate the aperture time.
  4. Use niDMM Configure Frequency Voltage Range.
  5. Set Frequency Voltage Range to the AC V range of your input signal.
- CVI/C++/Visual Basic
  1. Use niDMM_ConfigureMeasurementDigits .
  2. Set Measurement Function to NIDMM_VAL_PERIOD.
  3. Set Range to the maximum expected period in seconds. The DMM uses the range to calculate the aperture time.
  4. Use niDMM_ConfigureFrequencyVoltageRange
  5. Set Frequency Voltage Range to the AC V range of your input signal.

Parent topic:

Features

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=configuring-the-hardware-in-max.html language=enus -->
## TOPIC 00167: Configuring the Hardware in MAX

- bundle_id: `ni-dmm`
- source_path: `configuring-the-hardware-in-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/configuring-the-hardware-in-max.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Measurement & Automation Explorer (MAX) to configure your NI hardware. MAX informs other programs about which devices reside in the system and how they are configured. MAX is installed by default with NI-DMM. Launch MAX by navigating to Start»All Programs»National Instruments»Measurement & Autom

### Configuring the Hardware in MAX

Use Measurement & Automation Explorer (MAX) to configure your NI hardware. MAX informs other
 programs about which devices reside in the system and how they are configured. MAX
 is installed by default with NI-DMM.

1. Launch MAX by navigating to Start»All Programs»National Instruments»Measurement & Automation or by clicking the Measurement & Automation desktop icon.
2. In the Configuration pane, double-click Devices and Interfaces to see the list of installed devices. Installed devices appear under the name of their associated chassis.
3. Expand your Chassis tree item. MAX lists all devices installed in the chassis. Your default device names may vary.
4. Record the device identifier MAX assigns to the hardware. Use this identifier when programming your DMM.

Parent topic:

Getting Started

<!--NI_TOPIC bundle=ni-dmm path=configuring-the-hardware.html language=enus -->
## TOPIC 00168: Configuring the Hardware

- bundle_id: `ni-dmm`
- source_path: `configuring-the-hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/configuring-the-hardware.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Configuration VIs and functions set up the acquisition. NI-DMM can configure single point measurements, multipoint measurements, and waveform acquisitions. The configuration functions depend on the type of acquisition used in an application.To configure the DMM for a single point acquisition, ca

### Configuring the Hardware

The Configuration VIs and functions set up the acquisition. NI-DMM can configure single point measurements, multipoint measurements, and waveform acquisitions. The configuration functions depend on the type of acquisition used in an application.

To configure the DMM for a single point acquisition, call niDMM Config Measurement followed by calls to measurement options (such as niDMM Configure Auto Zero Mode, niDMM Configure Power Line Frequency, niDMM Configure Offset Compensated Ohms, etc).

The following table lists VIs and functions for configuring the DMM:

|  | LabVIEW VIs | C and Visual Basic Functions |
| --- | --- | --- |
| Configuration | niDMM Config Measurement | niDMM_ConfigureMeasurementDigits |
| niDMM Configure Multi Point | niDMM_ConfigureMultiPoint |  |
| niDMM Configure Waveform Acquisition | niDMM_ConfigureWaveformAcquisition |  |
| niDMM Export Attribute Configuration | niDMM_ExportAttributeConfigurationBuffer |  |
| niDMM_ExportAttributeConfigurationFile |  |  |
| niDMM Import Attribute Configuration | niDMM_ImportAttributeConfigurationBuffer |  |
| niDMM_ImportAttributeConfigurationFile |  |  |
| Measurement Options | niDMM Configure AC Bandwidth | niDMM_ConfigureACBandwidth |
| niDMM Configure ADC Calibration | niDMM_ConfigureADCCalibration |  |
| niDMM Configure Auto Zero | niDMM_ConfigureAutoZeroMode |  |
| niDMM Configure Cable Comp Type | niDMM_ConfigureCableCompType |  |
| niDMM Configure Current Source | niDMM_ConfigureCurrentSource |  |
| niDMM Configure Frequency Voltage Range | niDMM_ConfigureFrequencyVoltageRange |  |
| niDMM Configure Fixed Reference Junction | niDMM_ConfigureFixedRefJunction |  |
| niDMM Configure Offset Comp Ohms | niDMM_ConfigureOffSetCompOhms |  |
| niDMM Configure Open Cable Comp Values | niDMM_ConfigureOpenCableCompValues |  |
| niDMM Configure Powerline Frequency | niDMM_ConfigurePowerlineFrequency |  |
| niDMM Configure RTD Custom | niDMM_ConfigureRTDCustom |  |
| niDMM Configure RTD Type | niDMM_ConfigureRTDType |  |
| niDMM Configure Short Cable Comp Values | niDMM_ConfigureShortCableCompValues |  |
| niDMM Configure Thermistor Custom | niDMM_ConfigureThermistorCustom |  |
| niDMM Configure Thermistor Type | niDMM_ConfigureThermistorType |  |
| niDMM Configure Thermocouple | niDMM_ConfigureThermocouple |  |
| niDMM Configure Transducer Type | niDMM_ConfigureTransducerType |  |
| niDMM Configure Waveform Coupling | niDMM_ConfigureWaveformCoupling |  |
| Trigger | niDMM Configure Meas Complete Dest | niDMM_ConfigureMeasCompleteDest |
| niDMM Config Measurement Complete Slope | niDMM_ConfigureMeasCompleteSlope |  |
| niDMM Configure Sample Trigger Slope | niDMM_ConfigureSampleTriggerSlope |  |
| niDMM Configure Trigger | niDMM_ConfigureTrigger |  |
| niDMM Configure Trigger Slope | niDMM_ConfigureTriggerSlope |  |

#### Advanced Attributes and
 Properties

Some advanced attributes and properties are not available
 through a configuration function or VI. Set the attributes and properties directly
 using the niDMM_SetAttributeViReal64 function or a property node.
 Refer to *Using Attributes and Properties with NI-DMM* for more
 information on attribute and property programming. Refer to the following table for
 a list of those attributes and properties configurable only through the
 niDMM_SetAttributeViReal64 function or a property
 node.

| LabVIEW Property | C and Visual Basic Attribute |
| --- | --- |
| Aperture Time | NIDMM_ATTR_APERTURE_TIME |
| Aperture Time Units | NIDMM_ATTR_APERTURE_TIME_UNITS |
| DC Noise Rejection | NIDMM_ATTR_DC_NOISE_REJECTION |
| Input Resistance | NIDMM_ATTR_INPUT_RESISTANCE |
| Latency | NIDMM_ATTR_LATENCY |
| Number of Averages | NIDMM_ATTR_NUMBER_OF_AVERAGES |
| Number of LC Measurements to Average | NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE |
| Operation Mode | NIDMM_ATTR_OPERATION_MODE |
| Settle Time | NIDMM_ATTR_SETTLE_TIME |
| Shunt Value | NIDMM_ATTR_SHUNT_VALUE |

Parent topic:

Programming Flow

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=considerations-for-using-the-labview-real-time-module.html language=enus -->
## TOPIC 00169: Considerations for Using the LabVIEW Real-Time Module

- bundle_id: `ni-dmm`
- source_path: `considerations-for-using-the-labview-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/considerations-for-using-the-labview-real-time-module.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To develop an NI-DMM application in the LabVIEW Real-Time Module, follow the same steps used for developing any application in the LabVIEW Real-Time Module, with the addition of using NI-DMM VIs. Applications running NI-DMM in the LabVIEW Real-Time Module may be compromised and/or slow at 64 MB.Har

### Considerations for Using the LabVIEW Real-Time Module

To develop an NI-DMM application in the LabVIEW Real-Time Module, follow the same steps used for developing any application in the LabVIEW Real-Time Module, with the addition of using NI-DMM VIs.

Note

#### Hardware Support

You can use the following devices with the LabVIEW Real-Time Module:

- NI PXI-4082
- NI PXI-4081
- NI PXI-4080
- NI PXI-4072
- NI PXI-4071
- NI PXI-4070
- NI PXI-4065

#### Unsupported Features

When
 using NI DMMs with the LabVIEW Real-Time Module, the following features are
 not supported:

- External calibration
- Test panel
- InstrumentStudio

#### Related Documentation

- For configuration instructions for remote systems, refer to the Remote Systems Help in Measurement & Automation Explorer (MAX) by selecting Help»Help Topics»Remote Systems in MAX.
- For more information on the LabVIEW Real-Time Module, refer to the LabVIEW Real-Time Module Help at ni.com/manuals.
- For additional troubleshooting and support information, refer to the LabVIEW Real-Time Support Web site.

Parent topic:

Using NI-DMM in LabVIEW

<!--NI_TOPIC bundle=ni-dmm path=continuous-acquisitions.html language=enus -->
## TOPIC 00170: Continuous Acquisitions

- bundle_id: `ni-dmm`
- source_path: `continuous-acquisitions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/continuous-acquisitions.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Continuous acquisitions function the same way as multiple point acquisitions, except that the trigger loop or the sample trigger loop are continuous. The figure below demonstrates the sequence for continuous acquisitions.To configure a continuous acquisition, set Trigger Count or Sample Count to 0.S

### Continuous Acquisitions

Continuous acquisitions function the same way as multiple point acquisitions, except that the trigger loop or the sample trigger loop are continuous. The figure below demonstrates the sequence for continuous acquisitions.

[IMAGE alt='image' src='GUID-7766D74E-090C-47E2-A853-C7D5DE531C9A-a5.svg']

To configure a continuous acquisition, set Trigger Count or Sample Count to 0.

- Setting Sample Count to 0 causes the conditional statement "Measurements equal to Sample Count" to always evaluate to False. The DMM continues taking measurements in the inner loop.
- Setting Trigger Count to 0 causes the conditional statement "Triggers equal to Trigger Count" to always evaluate to False.

Note

To end a continuous acquisition, call niDMM Abort.

Parent topic:

Triggering

Related concepts:

- Multiple Point Acquisitions

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=creating-an-application-with-ni-dmm.html language=enus -->
## TOPIC 00171: Creating an Application with NI-DMM

- bundle_id: `ni-dmm`
- source_path: `creating-an-application-with-ni-dmm.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/creating-an-application-with-ni-dmm.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This book explains how to begin using NI-DMM with your application development environment (ADE), lists any files to include in your application, and mentions special considerations to make with each ADE.To successfully build your application, you need to have NI-DMM installed. You also need to have

### Creating an Application with NI-DMM

This book explains how to begin using NI-DMM with your application development environment (ADE), lists any files to include in your application, and mentions special considerations to make with each ADE.

To successfully build your application, you need to have NI-DMM installed. You also need to have one of the following ADEs installed:

- LabVIEW
- LabWindows/CVI
- Visual C++
- Visual Basic

Parent topic:

Getting Started

<!--NI_TOPIC bundle=ni-dmm path=crest-factor.html language=enus -->
## TOPIC 00172: Crest Factor

- bundle_id: `ni-dmm`
- source_path: `crest-factor.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/crest-factor.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Crest factor is determined by the following formula:Crest Factor = (V[peak]/V[rms])For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle wi

### Crest Factor

Crest factor is determined by the following formula:

Crest Factor = (V<sub>peak</sub>/V<sub>rms</sub>)

For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle without overloading or introducing additional error. For example, given a certain DMM with an AC accuracy of 0.03% (always specified for sine waves) with an additional error of 0.2% for crest factors between 1.414 and 5, then the total error for measuring a triangular wave (crest factor = 1.73) is 0.03% + 0.2% = 0.23%.

Historically, making AC measurements with DMMs has been very frustrating because many tradeoffs exist. Traditional methods are derated for high crest factor signals. If you do not know the crest factor, it is difficult to predict the accuracy of the measurement. Also, high-frequency, low-level signals are measured poorly by most 6½ digit DMMs because of their analog techniques. These devices employ active diode rectifiers that cannot keep up effectively as frequency increases, unless they are driven very hard (for example, high amplitudes).

The method used by the device is insensitive to crest factor error and capable of low-level measurements, limited primarily by noise. So while the specification allows for signal amplitudes of 1% of range, in practice the useful measurement range extends at least a decade lower.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=crest-factor_2.html language=enus -->
## TOPIC 00173: Crest Factor

- bundle_id: `ni-dmm`
- source_path: `crest-factor_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/crest-factor_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Crest factor is determined by the following formula:Crest Factor = (V[peak]/V[rms])For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle wi

### Crest Factor

Crest factor is determined by the following formula:

Crest Factor = (V<sub>peak</sub>/V<sub>rms</sub>)

For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle without overloading or introducing additional error. For example, given a certain DMM with an AC accuracy of 0.03% (always specified for sine waves) with an additional error of 0.2% for crest factors between 1.414 and 5, then the total error for measuring a triangular wave (crest factor = 1.73) is 0.03% + 0.2% = 0.23%.

Historically, making AC measurements with DMMs has been very frustrating because many tradeoffs exist. Traditional methods are derated for high crest factor signals. If you do not know the crest factor, it is difficult to predict the accuracy of the measurement. Also, high-frequency, low-level signals are measured poorly by most 6½ digit DMMs because of their analog techniques. These devices employ active diode rectifiers that cannot keep up effectively as frequency increases, unless they are driven very hard (for example, high amplitudes).

The method used by the device is insensitive to crest factor error and capable of low-level measurements, limited primarily by noise. So while the specification allows for signal amplitudes of 1% of range, in practice the useful measurement range extends at least a decade lower.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=crest-factor_3.html language=enus -->
## TOPIC 00174: Crest Factor

- bundle_id: `ni-dmm`
- source_path: `crest-factor_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/crest-factor_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Crest factor is determined by the following formula:Crest Factor = (V[peak]/V[rms])For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle wi

### Crest Factor

Crest factor is determined by the following formula:

Crest Factor = (V<sub>peak</sub>/V<sub>rms</sub>)

For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle without overloading or introducing additional error. For example, given a certain DMM with an AC accuracy of 0.03% (always specified for sine waves) with an additional error of 0.2% for crest factors between 1.414 and 5, then the total error for measuring a triangular wave (crest factor = 1.73) is 0.03% + 0.2% = 0.23%.

Historically, making AC measurements with DMMs has been very frustrating because many tradeoffs exist. Traditional methods are derated for high crest factor signals. If you do not know the crest factor, it is difficult to predict the accuracy of the measurement. Also, high-frequency, low-level signals are measured poorly by most 6½ digit DMMs because of their analog techniques. These devices employ active diode rectifiers that cannot keep up effectively as frequency increases, unless they are driven very hard (for example, high amplitudes).

The method used by the device is insensitive to crest factor error and capable of low-level measurements, limited primarily by noise. So while the specification allows for signal amplitudes of 1% of range, in practice the useful measurement range extends at least a decade lower.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=crest-factor_4.html language=enus -->
## TOPIC 00175: Crest Factor

- bundle_id: `ni-dmm`
- source_path: `crest-factor_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/crest-factor_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Crest factor is determined by the following formula:Crest Factor = (V[peak]/V[rms])For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle wi

### Crest Factor

Crest factor is determined by the following formula:

Crest Factor = (V<sub>peak</sub>/V<sub>rms</sub>)

For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle without overloading or introducing additional error. For example, given a certain DMM with an AC accuracy of 0.03% (always specified for sine waves) with an additional error of 0.2% for crest factors between 1.414 and 5, then the total error for measuring a triangular wave (crest factor = 1.73) is 0.03% + 0.2% = 0.23%.

Historically, making AC measurements with DMMs has been very frustrating because many tradeoffs exist. Traditional methods are derated for high crest factor signals. If you do not know the crest factor, it is difficult to predict the accuracy of the measurement. Also, high-frequency, low-level signals are measured poorly by most 6½ digit DMMs because of their analog techniques. These devices employ active diode rectifiers that cannot keep up effectively as frequency increases, unless they are driven very hard (for example, high amplitudes).

The method used by the device is insensitive to crest factor error and capable of low-level measurements, limited primarily by noise. So while the specification allows for signal amplitudes of 1% of range, in practice the useful measurement range extends at least a decade lower.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=crest-factor_5.html language=enus -->
## TOPIC 00176: Crest Factor

- bundle_id: `ni-dmm`
- source_path: `crest-factor_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/crest-factor_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Crest factor is determined by the following formula:Crest Factor = (V[peak]/V[rms])For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle wi

### Crest Factor

Crest factor is determined by the following formula:

Crest Factor = (V<sub>peak</sub>/V<sub>rms</sub>)

For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle without overloading or introducing additional error. For example, given a certain DMM with an AC accuracy of 0.03% (always specified for sine waves) with an additional error of 0.2% for crest factors between 1.414 and 5, then the total error for measuring a triangular wave (crest factor = 1.73) is 0.03% + 0.2% = 0.23%.

Historically, making AC measurements with DMMs has been very frustrating because many tradeoffs exist. Traditional methods are derated for high crest factor signals. If you do not know the crest factor, it is difficult to predict the accuracy of the measurement. Also, high-frequency, low-level signals are measured poorly by most 6½ digit DMMs because of their analog techniques. These devices employ active diode rectifiers that cannot keep up effectively as frequency increases, unless they are driven very hard (for example, high amplitudes).

The method used by the device is insensitive to crest factor error and capable of low-level measurements, limited primarily by noise. So while the specification allows for signal amplitudes of 1% of range, in practice the useful measurement range extends at least a decade lower.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=crest-factor_6.html language=enus -->
## TOPIC 00177: Crest Factor

- bundle_id: `ni-dmm`
- source_path: `crest-factor_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/crest-factor_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Crest factor is determined by the following formula:Crest Factor = (V[peak]/V[rms])For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle wi

### Crest Factor

Crest factor is determined by the following formula:

Crest Factor = (V<sub>peak</sub>/V<sub>rms</sub>)

For a sine wave, the crest factor is 1.414; for a 50% duty cycle square wave, the crest factor is 1. This specification is important because it indicates the maximum peak value of a waveform that the DMM can handle without overloading or introducing additional error. For example, given a certain DMM with an AC accuracy of 0.03% (always specified for sine waves) with an additional error of 0.2% for crest factors between 1.414 and 5, then the total error for measuring a triangular wave (crest factor = 1.73) is 0.03% + 0.2% = 0.23%.

Historically, making AC measurements with DMMs has been very frustrating because many tradeoffs exist. Traditional methods are derated for high crest factor signals. If you do not know the crest factor, it is difficult to predict the accuracy of the measurement. Also, high-frequency, low-level signals are measured poorly by most 6½ digit DMMs because of their analog techniques. These devices employ active diode rectifiers that cannot keep up effectively as frequency increases, unless they are driven very hard (for example, high amplitudes).

The method used by the device is insensitive to crest factor error and capable of low-level measurements, limited primarily by noise. So while the specification allows for signal amplitudes of 1% of range, in practice the useful measurement range extends at least a decade lower.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=current-waveforms.html language=enus -->
## TOPIC 00178: Current Waveforms

- bundle_id: `ni-dmm`
- source_path: `current-waveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/current-waveforms.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifi

### Current Waveforms

The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.

For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifications documents for the DMMs.

Apparent burden voltage is even higher when using long cable runs, which add more inductance and resistance. Minimize cable length or use a shunt resistor local to the DUT if wide bandwidth current waveform acquisition is desired. The following figure shows the burden voltage effect due to inductance:

[IMAGE alt='image' src='GUID-27919EB6-0472-4FCE-BC24-DCDAB44D6AA2-a5.svg']

For more information about burden voltage, refer to Burden Voltage.

Parent topic:

Waveform Acquisitions

Related concepts:

- Burden Voltage

<!--NI_TOPIC bundle=ni-dmm path=current-waveforms_2.html language=enus -->
## TOPIC 00179: Current Waveforms

- bundle_id: `ni-dmm`
- source_path: `current-waveforms_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/current-waveforms_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifi

### Current Waveforms

The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.

For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifications documents for the DMMs.

Apparent burden voltage is even higher when using long cable runs, which add more inductance and resistance. Minimize cable length or use a shunt resistor local to the DUT if wide bandwidth current waveform acquisition is desired. The following figure shows the burden voltage effect due to inductance:

[IMAGE alt='image' src='GUID-27919EB6-0472-4FCE-BC24-DCDAB44D6AA2-a5.svg']

For more information about burden voltage, refer to Burden Voltage.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=current-waveforms_3.html language=enus -->
## TOPIC 00180: Current Waveforms

- bundle_id: `ni-dmm`
- source_path: `current-waveforms_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/current-waveforms_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifi

### Current Waveforms

The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.

For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifications documents for the DMMs.

Apparent burden voltage is even higher when using long cable runs, which add more inductance and resistance. Minimize cable length or use a shunt resistor local to the DUT if wide bandwidth current waveform acquisition is desired. The following figure shows the burden voltage effect due to inductance:

[IMAGE alt='image' src='GUID-27919EB6-0472-4FCE-BC24-DCDAB44D6AA2-a5.svg']

For more information about burden voltage, refer to Burden Voltage.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=current-waveforms_4.html language=enus -->
## TOPIC 00181: Current Waveforms

- bundle_id: `ni-dmm`
- source_path: `current-waveforms_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/current-waveforms_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifi

### Current Waveforms

The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.

For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifications documents for the DMMs.

Apparent burden voltage is even higher when using long cable runs, which add more inductance and resistance. Minimize cable length or use a shunt resistor local to the DUT if wide bandwidth current waveform acquisition is desired. The following figure shows the burden voltage effect due to inductance:

[IMAGE alt='image' src='GUID-27919EB6-0472-4FCE-BC24-DCDAB44D6AA2-a5.svg']

For more information about burden voltage, refer to Burden Voltage.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=current-waveforms_5.html language=enus -->
## TOPIC 00182: Current Waveforms

- bundle_id: `ni-dmm`
- source_path: `current-waveforms_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/current-waveforms_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifi

### Current Waveforms

The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.

For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifications documents for the DMMs.

Apparent burden voltage is even higher when using long cable runs, which add more inductance and resistance. Minimize cable length or use a shunt resistor local to the DUT if wide bandwidth current waveform acquisition is desired. The following figure shows the burden voltage effect due to inductance:

[IMAGE alt='image' src='GUID-27919EB6-0472-4FCE-BC24-DCDAB44D6AA2-a5.svg']

For more information about burden voltage, refer to Burden Voltage.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=current-waveforms_6.html language=enus -->
## TOPIC 00183: Current Waveforms

- bundle_id: `ni-dmm`
- source_path: `current-waveforms_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/current-waveforms_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifi

### Current Waveforms

The DMM can acquire current waveforms at frequencies up to 400 kHz. At high frequencies, the apparent burden voltage could increase from that listed in the specifications due to internal inductance.

For the maximum burden voltage per range in AC current, refer to Related Documentation for the specifications documents for the DMMs.

Apparent burden voltage is even higher when using long cable runs, which add more inductance and resistance. Minimize cable length or use a shunt resistor local to the DUT if wide bandwidth current waveform acquisition is desired. The following figure shows the burden voltage effect due to inductance:

[IMAGE alt='image' src='GUID-27919EB6-0472-4FCE-BC24-DCDAB44D6AA2-a5.svg']

For more information about burden voltage, refer to Burden Voltage.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=dc-and-ac-coupling.html language=enus -->
## TOPIC 00184: DC and AC Coupling

- bundle_id: `ni-dmm`
- source_path: `dc-and-ac-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-and-ac-coupling.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM offers two different modes for measuring AC voltage:AC VoltsAC Volts DC Coupled The NI 4065 only offers the AC Volts mode for measuring AC voltage.AC Volts ModeAC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations

### DC and AC Coupling

The DMM offers two different modes for measuring AC voltage:

- AC Volts
- AC Volts DC Coupled

Note

#### AC Volts Mode

AC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations where a large DC offset must be blocked before digitization. To measure AC voltage in the presence of large DC offsets, such as ripple on a DC power supply, use AC Volts mode.

#### AC Volts DC Coupled Mode

The rms algorithm employed by the DMM is insensitive to any DC component of the signal being measured. Therefore, for applications without large DC components, such as AC powerline and audio signals, the AC coupling capacitor used to block the DC signal component is not always necessary on the DMM. This capacitor can be bypassed by using AC Volts DC Coupled mode. This mode does not have the long time constant associated with the input coupling capacitor and thus offers a very short settling time.

#### DC Coupling on AC Current Measurements

AC current measurements are always DC coupled and therefore always offer quick settling time, but these measurements are subject to overload if the DC component of the signal exceeds the limits of the chosen range.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-and-ac-coupling_2.html language=enus -->
## TOPIC 00185: DC and AC Coupling

- bundle_id: `ni-dmm`
- source_path: `dc-and-ac-coupling_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-and-ac-coupling_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM offers two different modes for measuring AC voltage:AC VoltsAC Volts DC Coupled The NI 4065 only offers the AC Volts mode for measuring AC voltage.AC Volts ModeAC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations

### DC and AC Coupling

The DMM offers two different modes for measuring AC voltage:

- AC Volts
- AC Volts DC Coupled

Note

#### AC Volts Mode

AC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations where a large DC offset must be blocked before digitization. To measure AC voltage in the presence of large DC offsets, such as ripple on a DC power supply, use AC Volts mode.

#### AC Volts DC Coupled Mode

The rms algorithm employed by the DMM is insensitive to any DC component of the signal being measured. Therefore, for applications without large DC components, such as AC powerline and audio signals, the AC coupling capacitor used to block the DC signal component is not always necessary on the DMM. This capacitor can be bypassed by using AC Volts DC Coupled mode. This mode does not have the long time constant associated with the input coupling capacitor and thus offers a very short settling time.

#### DC Coupling on AC Current Measurements

AC current measurements are always DC coupled and therefore always offer quick settling time, but these measurements are subject to overload if the DC component of the signal exceeds the limits of the chosen range.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-and-ac-coupling_3.html language=enus -->
## TOPIC 00186: DC and AC Coupling

- bundle_id: `ni-dmm`
- source_path: `dc-and-ac-coupling_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-and-ac-coupling_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM offers two different modes for measuring AC voltage:AC VoltsAC Volts DC Coupled The NI 4065 only offers the AC Volts mode for measuring AC voltage.AC Volts ModeAC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations

### DC and AC Coupling

The DMM offers two different modes for measuring AC voltage:

- AC Volts
- AC Volts DC Coupled

Note

#### AC Volts Mode

AC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations where a large DC offset must be blocked before digitization. To measure AC voltage in the presence of large DC offsets, such as ripple on a DC power supply, use AC Volts mode.

#### AC Volts DC Coupled Mode

The rms algorithm employed by the DMM is insensitive to any DC component of the signal being measured. Therefore, for applications without large DC components, such as AC powerline and audio signals, the AC coupling capacitor used to block the DC signal component is not always necessary on the DMM. This capacitor can be bypassed by using AC Volts DC Coupled mode. This mode does not have the long time constant associated with the input coupling capacitor and thus offers a very short settling time.

#### DC Coupling on AC Current Measurements

AC current measurements are always DC coupled and therefore always offer quick settling time, but these measurements are subject to overload if the DC component of the signal exceeds the limits of the chosen range.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-and-ac-coupling_4.html language=enus -->
## TOPIC 00187: DC and AC Coupling

- bundle_id: `ni-dmm`
- source_path: `dc-and-ac-coupling_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-and-ac-coupling_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM offers two different modes for measuring AC voltage:AC VoltsAC Volts DC Coupled The NI 4065 only offers the AC Volts mode for measuring AC voltage.AC Volts ModeAC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations

### DC and AC Coupling

The DMM offers two different modes for measuring AC voltage:

- AC Volts
- AC Volts DC Coupled

Note

#### AC Volts Mode

AC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations where a large DC offset must be blocked before digitization. To measure AC voltage in the presence of large DC offsets, such as ripple on a DC power supply, use AC Volts mode.

#### AC Volts DC Coupled Mode

The rms algorithm employed by the DMM is insensitive to any DC component of the signal being measured. Therefore, for applications without large DC components, such as AC powerline and audio signals, the AC coupling capacitor used to block the DC signal component is not always necessary on the DMM. This capacitor can be bypassed by using AC Volts DC Coupled mode. This mode does not have the long time constant associated with the input coupling capacitor and thus offers a very short settling time.

#### DC Coupling on AC Current Measurements

AC current measurements are always DC coupled and therefore always offer quick settling time, but these measurements are subject to overload if the DC component of the signal exceeds the limits of the chosen range.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-and-ac-coupling_5.html language=enus -->
## TOPIC 00188: DC and AC Coupling

- bundle_id: `ni-dmm`
- source_path: `dc-and-ac-coupling_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-and-ac-coupling_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM offers two different modes for measuring AC voltage:AC VoltsAC Volts DC Coupled The NI 4065 only offers the AC Volts mode for measuring AC voltage.AC Volts ModeAC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations

### DC and AC Coupling

The DMM offers two different modes for measuring AC voltage:

- AC Volts
- AC Volts DC Coupled

Note

#### AC Volts Mode

AC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations where a large DC offset must be blocked before digitization. To measure AC voltage in the presence of large DC offsets, such as ripple on a DC power supply, use AC Volts mode.

#### AC Volts DC Coupled Mode

The rms algorithm employed by the DMM is insensitive to any DC component of the signal being measured. Therefore, for applications without large DC components, such as AC powerline and audio signals, the AC coupling capacitor used to block the DC signal component is not always necessary on the DMM. This capacitor can be bypassed by using AC Volts DC Coupled mode. This mode does not have the long time constant associated with the input coupling capacitor and thus offers a very short settling time.

#### DC Coupling on AC Current Measurements

AC current measurements are always DC coupled and therefore always offer quick settling time, but these measurements are subject to overload if the DC component of the signal exceeds the limits of the chosen range.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-and-ac-coupling_6.html language=enus -->
## TOPIC 00189: DC and AC Coupling

- bundle_id: `ni-dmm`
- source_path: `dc-and-ac-coupling_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-and-ac-coupling_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM offers two different modes for measuring AC voltage:AC VoltsAC Volts DC Coupled The NI 4065 only offers the AC Volts mode for measuring AC voltage.AC Volts ModeAC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations

### DC and AC Coupling

The DMM offers two different modes for measuring AC voltage:

- AC Volts
- AC Volts DC Coupled

Note

#### AC Volts Mode

AC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations where a large DC offset must be blocked before digitization. To measure AC voltage in the presence of large DC offsets, such as ripple on a DC power supply, use AC Volts mode.

#### AC Volts DC Coupled Mode

The rms algorithm employed by the DMM is insensitive to any DC component of the signal being measured. Therefore, for applications without large DC components, such as AC powerline and audio signals, the AC coupling capacitor used to block the DC signal component is not always necessary on the DMM. This capacitor can be bypassed by using AC Volts DC Coupled mode. This mode does not have the long time constant associated with the input coupling capacitor and thus offers a very short settling time.

#### DC Coupling on AC Current Measurements

AC current measurements are always DC coupled and therefore always offer quick settling time, but these measurements are subject to overload if the DC component of the signal exceeds the limits of the chosen range.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-and-ac-coupling_7.html language=enus -->
## TOPIC 00190: DC and AC Coupling

- bundle_id: `ni-dmm`
- source_path: `dc-and-ac-coupling_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-and-ac-coupling_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM offers two different modes for measuring AC voltage:AC VoltsAC Volts DC Coupled The NI 4065 only offers the AC Volts mode for measuring AC voltage.AC Volts ModeAC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations

### DC and AC Coupling

The DMM offers two different modes for measuring AC voltage:

- AC Volts
- AC Volts DC Coupled

Note

#### AC Volts Mode

AC Volts mode uses a coupling capacitor to remove DC offsets before digitization. A coupling capacitor is available for situations where a large DC offset must be blocked before digitization. To measure AC voltage in the presence of large DC offsets, such as ripple on a DC power supply, use AC Volts mode.

#### AC Volts DC Coupled Mode

The rms algorithm employed by the DMM is insensitive to any DC component of the signal being measured. Therefore, for applications without large DC components, such as AC powerline and audio signals, the AC coupling capacitor used to block the DC signal component is not always necessary on the DMM. This capacitor can be bypassed by using AC Volts DC Coupled mode. This mode does not have the long time constant associated with the input coupling capacitor and thus offers a very short settling time.

#### DC Coupling on AC Current Measurements

AC current measurements are always DC coupled and therefore always offer quick settling time, but these measurements are subject to overload if the DC component of the signal exceeds the limits of the chosen range.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-noise-rejection-for-waveforms.html language=enus -->
## TOPIC 00191: DC Noise Rejection for Waveforms

- bundle_id: `ni-dmm`
- source_path: `dc-noise-rejection-for-waveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-noise-rejection-for-waveforms.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DC Noise Rejection feature that can reduce noise in DC measurements in DMM mode can also be used to alter the noise and frequency response of waveform acquisitions. Three settings of the DC Noise Rejection parameter are available: normal, second order, and high order. You can specify the noise r

### DC Noise Rejection for Waveforms

The DC Noise Rejection feature that can reduce noise in DC measurements in DMM mode can also be used to alter the noise and frequency response of waveform acquisitions. Three settings of the DC Noise Rejection parameter are available: normal, second order, and high order. You can specify the noise rejection settings using a property node, as for DMM-mode readings.

Only Normal DC Noise Rejection is available for sampling rates above 200,000 S/s.

#### Normal

Normal DC Noise Rejection gives rise to notches in the frequency response at multiples of the sampling rate, and the response is attenuated by 4 dB at half the sampling rate, in addition to any attenuation present at the maximum sampling rate of 1.8 MS/s. For example, with a selected sampling rate of 1 kS/s, response is down 4 dB at 500 Hz, shown in the first following graph, and is 0 at multiples of 1 kHz as shown in the second graph.

[IMAGE alt='image' src='GUID-762B3BD6-42FC-46EE-BFFC-3EBFD549D316-a5.svg']

[IMAGE alt='image' src='GUID-188A067C-9359-4963-86A5-9A59B40E56DD-a5.svg']

#### Second Order

Second order DC Noise Rejection gives rise to notches in the frequency response at even multiples of the sampling rate, and the response is attenuated by 1.9 dB at half the sampling rate, in addition to any attenuation present at the maximum sampling rate of 1.8 MS/s. For example, with a selected sampling rate of 1 kS/s, response is down 1.9 dB at 500 Hz, shown in the first following graph, and is 0 at multiples of 2 kHz as shown in the following graph.

[IMAGE alt='image' src='GUID-B494E28A-EBEF-407D-B2E9-02A6DCFC2A67-a5.svg']

[IMAGE alt='image' src='GUID-A402C93F-F7C8-468A-BA97-24C19BAE1ABC-a5.svg']

#### High Order

High order DC Noise Rejection gives rise to high attenuation to frequencies above about 4 times the sampling rate, and the response is attenuated by 0.7 dB at half the sampling rate, in addition to any attenuation present at the maximum sampling rate of 1.8 MS/s. For example, with a selected sampling rate of 1 kS/s, response is down 0.7 dB at 500 Hz, shown in the first following graph, and is very small at frequencies above 4 kHz as shown in the second following graph:

[IMAGE alt='image' src='GUID-C2B3D051-B0F1-47CC-B5A7-ECDEF1351918-a5.svg']

[IMAGE alt='image' src='GUID-5816F478-4F8F-4B0A-8FF3-06F76D2BF425-a5.svg']

#### Other Considerations

The default DC Noise Rejection setting is Normal, and it gives the lowest noise at very low frequencies. However, it does not reject out-of-band signals very well and has considerable attenuation at half the sample rate. It also yields a non-flat noise spectrum due to the notches at multiples of the sample rate. Second order DC Noise Rejection gives the lowest overall noise over a broad range of sampling rates, roughly from 500 S/s to 100 kS/s. It does a better job rejecting out-of-band signals, while reducing in-band attenuation, and it yields a flat noise spectrum. High-order DC Noise Rejection offers the flattest in-band frequency response and is useful for rejecting strong out-of-band noise signals. It also yields a flat noise spectrum. However, it yields higher overall noise than second order DC Noise Rejection.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=dc-noise-rejection-for-waveforms_2.html language=enus -->
## TOPIC 00192: DC Noise Rejection for Waveforms

- bundle_id: `ni-dmm`
- source_path: `dc-noise-rejection-for-waveforms_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-noise-rejection-for-waveforms_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DC Noise Rejection feature that can reduce noise in DC measurements in DMM mode can also be used to alter the noise and frequency response of waveform acquisitions. Three settings of the DC Noise Rejection parameter are available: normal, second order, and high order. You can specify the noise r

### DC Noise Rejection for Waveforms

The DC Noise Rejection feature that can reduce noise in DC measurements in DMM mode can also be used to alter the noise and frequency response of waveform acquisitions. Three settings of the DC Noise Rejection parameter are available: normal, second order, and high order. You can specify the noise rejection settings using a property node, as for DMM-mode readings.

Only Normal DC Noise Rejection is available for sampling rates above 200,000 S/s.

#### Normal

Normal DC Noise Rejection gives rise to notches in the frequency response at multiples of the sampling rate, and the response is attenuated by 4 dB at half the sampling rate, in addition to any attenuation present at the maximum sampling rate of 1.8 MS/s. For example, with a selected sampling rate of 1 kS/s, response is down 4 dB at 500 Hz, shown in the first following graph, and is 0 at multiples of 1 kHz as shown in the second graph.

[IMAGE alt='image' src='GUID-762B3BD6-42FC-46EE-BFFC-3EBFD549D316-a5.svg']

[IMAGE alt='image' src='GUID-188A067C-9359-4963-86A5-9A59B40E56DD-a5.svg']

#### Second Order

Second order DC Noise Rejection gives rise to notches in the frequency response at even multiples of the sampling rate, and the response is attenuated by 1.9 dB at half the sampling rate, in addition to any attenuation present at the maximum sampling rate of 1.8 MS/s. For example, with a selected sampling rate of 1 kS/s, response is down 1.9 dB at 500 Hz, shown in the first following graph, and is 0 at multiples of 2 kHz as shown in the following graph.

[IMAGE alt='image' src='GUID-B494E28A-EBEF-407D-B2E9-02A6DCFC2A67-a5.svg']

[IMAGE alt='image' src='GUID-A402C93F-F7C8-468A-BA97-24C19BAE1ABC-a5.svg']

#### High Order

High order DC Noise Rejection gives rise to high attenuation to frequencies above about 4 times the sampling rate, and the response is attenuated by 0.7 dB at half the sampling rate, in addition to any attenuation present at the maximum sampling rate of 1.8 MS/s. For example, with a selected sampling rate of 1 kS/s, response is down 0.7 dB at 500 Hz, shown in the first following graph, and is very small at frequencies above 4 kHz as shown in the second following graph:

[IMAGE alt='image' src='GUID-C2B3D051-B0F1-47CC-B5A7-ECDEF1351918-a5.svg']

[IMAGE alt='image' src='GUID-5816F478-4F8F-4B0A-8FF3-06F76D2BF425-a5.svg']

#### Other Considerations

The default DC Noise Rejection setting is Normal, and it gives the lowest noise at very low frequencies. However, it does not reject out-of-band signals very well and has considerable attenuation at half the sample rate. It also yields a non-flat noise spectrum due to the notches at multiples of the sample rate. Second order DC Noise Rejection gives the lowest overall noise over a broad range of sampling rates, roughly from 500 S/s to 100 kS/s. It does a better job rejecting out-of-band signals, while reducing in-band attenuation, and it yields a flat noise spectrum. High-order DC Noise Rejection offers the flattest in-band frequency response and is useful for rejecting strong out-of-band noise signals. It also yields a flat noise spectrum. However, it yields higher overall noise than second order DC Noise Rejection.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=dc-noise-rejection-for-waveforms_3.html language=enus -->
## TOPIC 00193: DC Noise Rejection for Waveforms

- bundle_id: `ni-dmm`
- source_path: `dc-noise-rejection-for-waveforms_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-noise-rejection-for-waveforms_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DC Noise Rejection feature that can reduce noise in DC measurements in DMM mode can also be used to alter the noise and frequency response of waveform acquisitions. Three settings of the DC Noise Rejection parameter are available: normal, second order, and high order. You can specify the noise r

### DC Noise Rejection for Waveforms

The DC Noise Rejection feature that can reduce noise in DC measurements in DMM mode can also be used to alter the noise and frequency response of waveform acquisitions. Three settings of the DC Noise Rejection parameter are available: normal, second order, and high order. You can specify the noise rejection settings using a property node, as for DMM-mode readings.

Only Normal DC Noise Rejection is available for sampling rates above 200,000 S/s.

#### Normal

Normal DC Noise Rejection gives rise to notches in the frequency response at multiples of the sampling rate, and the response is attenuated by 4 dB at half the sampling rate, in addition to any attenuation present at the maximum sampling rate of 1.8 MS/s. For example, with a selected sampling rate of 1 kS/s, response is down 4 dB at 500 Hz, shown in the first following graph, and is 0 at multiples of 1 kHz as shown in the second graph.

[IMAGE alt='image' src='GUID-762B3BD6-42FC-46EE-BFFC-3EBFD549D316-a5.svg']

[IMAGE alt='image' src='GUID-188A067C-9359-4963-86A5-9A59B40E56DD-a5.svg']

#### Second Order

Second order DC Noise Rejection gives rise to notches in the frequency response at even multiples of the sampling rate, and the response is attenuated by 1.9 dB at half the sampling rate, in addition to any attenuation present at the maximum sampling rate of 1.8 MS/s. For example, with a selected sampling rate of 1 kS/s, response is down 1.9 dB at 500 Hz, shown in the first following graph, and is 0 at multiples of 2 kHz as shown in the following graph.

[IMAGE alt='image' src='GUID-B494E28A-EBEF-407D-B2E9-02A6DCFC2A67-a5.svg']

[IMAGE alt='image' src='GUID-A402C93F-F7C8-468A-BA97-24C19BAE1ABC-a5.svg']

#### High Order

High order DC Noise Rejection gives rise to high attenuation to frequencies above about 4 times the sampling rate, and the response is attenuated by 0.7 dB at half the sampling rate, in addition to any attenuation present at the maximum sampling rate of 1.8 MS/s. For example, with a selected sampling rate of 1 kS/s, response is down 0.7 dB at 500 Hz, shown in the first following graph, and is very small at frequencies above 4 kHz as shown in the second following graph:

[IMAGE alt='image' src='GUID-C2B3D051-B0F1-47CC-B5A7-ECDEF1351918-a5.svg']

[IMAGE alt='image' src='GUID-5816F478-4F8F-4B0A-8FF3-06F76D2BF425-a5.svg']

#### Other Considerations

The default DC Noise Rejection setting is Normal, and it gives the lowest noise at very low frequencies. However, it does not reject out-of-band signals very well and has considerable attenuation at half the sample rate. It also yields a non-flat noise spectrum due to the notches at multiples of the sample rate. Second order DC Noise Rejection gives the lowest overall noise over a broad range of sampling rates, roughly from 500 S/s to 100 kS/s. It does a better job rejecting out-of-band signals, while reducing in-band attenuation, and it yields a flat noise spectrum. High-order DC Noise Rejection offers the flattest in-band frequency response and is useful for rejecting strong out-of-band noise signals. It also yields a flat noise spectrum. However, it yields higher overall noise than second order DC Noise Rejection.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=dc-noise-rejection.html language=enus -->
## TOPIC 00194: DC Noise Rejection

- bundle_id: `ni-dmm`
- source_path: `dc-noise-rejection.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-noise-rejection.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequen

### DC Noise Rejection

DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequencies. The DMM offers three different modes: normal, second-order, and high-order.

Refer to the following table for a list of the differences between the three modes:

| DC Noise Rejection Setting | Lowest Frequency for Noise Rejection | High-Frequency Noise Rejection |
| --- | --- | --- |
| Normal | 1/taperture | Good |
| Second-Order | 2/taperture | Better |
| High-Order | 4/taperture | Best |

Refer to the table in the Aperture Time section for the default aperture times and DC noise rejection settings used by the DMM.

#### Normal

When you select normal DC noise rejection, the DMM weights all samples equally. This feature emulates the behavior of most traditional DMMs, providing good rejection of frequencies at multiples of f0, where f0 = 1/t<sub>aperture</sub>. The following figure shows normal weighting, where all samples are weighted equally, and the resulting noise rejection as a function of frequency. Notice that you can obtain good rejection only very near multiples of f0. To get the fastest possible readings that give you some powerline noise rejection, set the aperture to the powerline period, such as 16.667 msec for a 60 Hz powerline frequency, and set the DC noise rejection to normal.

[IMAGE alt='image' src='GUID-477ED45A-FBF9-4A4F-8483-A304F1A6ADA3-a5.svg']

#### Second-Order

Second-order
 DC noise rejection applies a triangular weighting to the measurement samples. In
 second-order DC noise rejection, the samples taken in the middle of the aperture
 time are weighted more than samples taken at the beginning and the end of the
 measurement.

[IMAGE alt='image' src='GUID-0E770D6D-18B5-471D-A8B9-6A7C81F786B6-a5.svg']

Notice that you can obtain very good rejection near even
 multiples of f0 and that rejection increases more rapidly with
 frequency than with normal sample weighting. Also notice that the response notches
 are wider than they are with normal weighting, resulting in less sensitivity to
 slight variations in noise frequency. Use second-order DC noise rejection if you
 need better powerline noise rejection than you can get with normal DC noise
 rejection, but cannot afford to read slowly enough to take advantage of high-order
 noise rejection. For example, you could set the aperture to 33.333 msec for a 60 Hz
 powerline frequency.

#### High-Order

The following figure shows noise rejection with high order sample weighting.

[IMAGE alt='image' src='GUID-530A014E-C47D-4DBB-8A8E-834C081CED2D-a5.svg']

Note

Notice that noise rejection is good starting at around four times f0 and is excellent above about 4.5 times f0. Rejection of noise at any frequency above 4.6 times f0 exceeds 98 dB. An NI 407x or NI 408x, using high-order DC noise rejection with a 100 msec aperture, can deliver full 6½ digit accuracy on the 10 V range with over 1 V of interfering powerline noise at any frequency above 46 Hz.

The small tradeoff to using the higher-order filters is that to obtain powerline rejection, you must increase the measurement aperture by 2x (for second-order) or 4x (for high-order) versus that required for the normal setting.

Parent topic:

DC Voltage

Related concepts:

- Configuring Measurement Timing
- Aperture Time
- Selecting DC Noise Rejection

<!--NI_TOPIC bundle=ni-dmm path=dc-noise-rejection_2.html language=enus -->
## TOPIC 00195: DC Noise Rejection

- bundle_id: `ni-dmm`
- source_path: `dc-noise-rejection_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-noise-rejection_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequen

### DC Noise Rejection

DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequencies. The DMM offers three different modes: normal, second-order, and high-order.

Refer to the following table for a list of the differences between the three modes:

| DC Noise Rejection Setting | Lowest Frequency for Noise Rejection | High-Frequency Noise Rejection |
| --- | --- | --- |
| Normal | 1/taperture | Good |
| Second-Order | 2/taperture | Better |
| High-Order | 4/taperture | Best |

Refer to the table in the Aperture Time section for the default aperture times and DC noise rejection settings used by the DMM.

#### Normal

When you select normal DC noise rejection, the DMM weights all samples equally. This feature emulates the behavior of most traditional DMMs, providing good rejection of frequencies at multiples of f0, where f0 = 1/t<sub>aperture</sub>. The following figure shows normal weighting, where all samples are weighted equally, and the resulting noise rejection as a function of frequency. Notice that you can obtain good rejection only very near multiples of f0. To get the fastest possible readings that give you some powerline noise rejection, set the aperture to the powerline period, such as 16.667 msec for a 60 Hz powerline frequency, and set the DC noise rejection to normal.

[IMAGE alt='image' src='GUID-477ED45A-FBF9-4A4F-8483-A304F1A6ADA3-a5.svg']

#### Second-Order

Second-order
 DC noise rejection applies a triangular weighting to the measurement samples. In
 second-order DC noise rejection, the samples taken in the middle of the aperture
 time are weighted more than samples taken at the beginning and the end of the
 measurement.

[IMAGE alt='image' src='GUID-0E770D6D-18B5-471D-A8B9-6A7C81F786B6-a5.svg']

Notice that you can obtain very good rejection near even
 multiples of f0 and that rejection increases more rapidly with
 frequency than with normal sample weighting. Also notice that the response notches
 are wider than they are with normal weighting, resulting in less sensitivity to
 slight variations in noise frequency. Use second-order DC noise rejection if you
 need better powerline noise rejection than you can get with normal DC noise
 rejection, but cannot afford to read slowly enough to take advantage of high-order
 noise rejection. For example, you could set the aperture to 33.333 msec for a 60 Hz
 powerline frequency.

#### High-Order

The following figure shows noise rejection with high order sample weighting.

[IMAGE alt='image' src='GUID-530A014E-C47D-4DBB-8A8E-834C081CED2D-a5.svg']

Note

Notice that noise rejection is good starting at around four times f0 and is excellent above about 4.5 times f0. Rejection of noise at any frequency above 4.6 times f0 exceeds 98 dB. An NI 407x or NI 408x, using high-order DC noise rejection with a 100 msec aperture, can deliver full 6½ digit accuracy on the 10 V range with over 1 V of interfering powerline noise at any frequency above 46 Hz.

The small tradeoff to using the higher-order filters is that to obtain powerline rejection, you must increase the measurement aperture by 2x (for second-order) or 4x (for high-order) versus that required for the normal setting.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-noise-rejection_3.html language=enus -->
## TOPIC 00196: DC Noise Rejection

- bundle_id: `ni-dmm`
- source_path: `dc-noise-rejection_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-noise-rejection_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequen

### DC Noise Rejection

DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequencies. The DMM offers three different modes: normal, second-order, and high-order.

Refer to the following table for a list of the differences between the three modes:

| DC Noise Rejection Setting | Lowest Frequency for Noise Rejection | High-Frequency Noise Rejection |
| --- | --- | --- |
| Normal | 1/taperture | Good |
| Second-Order | 2/taperture | Better |
| High-Order | 4/taperture | Best |

Refer to the table in the Aperture Time section for the default aperture times and DC noise rejection settings used by the DMM.

#### Normal

When you select normal DC noise rejection, the DMM weights all samples equally. This feature emulates the behavior of most traditional DMMs, providing good rejection of frequencies at multiples of f0, where f0 = 1/t<sub>aperture</sub>. The following figure shows normal weighting, where all samples are weighted equally, and the resulting noise rejection as a function of frequency. Notice that you can obtain good rejection only very near multiples of f0. To get the fastest possible readings that give you some powerline noise rejection, set the aperture to the powerline period, such as 16.667 msec for a 60 Hz powerline frequency, and set the DC noise rejection to normal.

[IMAGE alt='image' src='GUID-477ED45A-FBF9-4A4F-8483-A304F1A6ADA3-a5.svg']

#### Second-Order

Second-order
 DC noise rejection applies a triangular weighting to the measurement samples. In
 second-order DC noise rejection, the samples taken in the middle of the aperture
 time are weighted more than samples taken at the beginning and the end of the
 measurement.

[IMAGE alt='image' src='GUID-0E770D6D-18B5-471D-A8B9-6A7C81F786B6-a5.svg']

Notice that you can obtain very good rejection near even
 multiples of f0 and that rejection increases more rapidly with
 frequency than with normal sample weighting. Also notice that the response notches
 are wider than they are with normal weighting, resulting in less sensitivity to
 slight variations in noise frequency. Use second-order DC noise rejection if you
 need better powerline noise rejection than you can get with normal DC noise
 rejection, but cannot afford to read slowly enough to take advantage of high-order
 noise rejection. For example, you could set the aperture to 33.333 msec for a 60 Hz
 powerline frequency.

#### High-Order

The following figure shows noise rejection with high order sample weighting.

[IMAGE alt='image' src='GUID-530A014E-C47D-4DBB-8A8E-834C081CED2D-a5.svg']

Note

Notice that noise rejection is good starting at around four times f0 and is excellent above about 4.5 times f0. Rejection of noise at any frequency above 4.6 times f0 exceeds 98 dB. An NI 407x or NI 408x, using high-order DC noise rejection with a 100 msec aperture, can deliver full 6½ digit accuracy on the 10 V range with over 1 V of interfering powerline noise at any frequency above 46 Hz.

The small tradeoff to using the higher-order filters is that to obtain powerline rejection, you must increase the measurement aperture by 2x (for second-order) or 4x (for high-order) versus that required for the normal setting.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-noise-rejection_4.html language=enus -->
## TOPIC 00197: DC Noise Rejection

- bundle_id: `ni-dmm`
- source_path: `dc-noise-rejection_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-noise-rejection_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequen

### DC Noise Rejection

DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequencies. The DMM offers three different modes: normal, second-order, and high-order.

Refer to the following table for a list of the differences between the three modes:

| DC Noise Rejection Setting | Lowest Frequency for Noise Rejection | High-Frequency Noise Rejection |
| --- | --- | --- |
| Normal | 1/taperture | Good |
| Second-Order | 2/taperture | Better |
| High-Order | 4/taperture | Best |

Refer to the table in the Aperture Time section for the default aperture times and DC noise rejection settings used by the DMM.

#### Normal

When you select normal DC noise rejection, the DMM weights all samples equally. This feature emulates the behavior of most traditional DMMs, providing good rejection of frequencies at multiples of f0, where f0 = 1/t<sub>aperture</sub>. The following figure shows normal weighting, where all samples are weighted equally, and the resulting noise rejection as a function of frequency. Notice that you can obtain good rejection only very near multiples of f0. To get the fastest possible readings that give you some powerline noise rejection, set the aperture to the powerline period, such as 16.667 msec for a 60 Hz powerline frequency, and set the DC noise rejection to normal.

[IMAGE alt='image' src='GUID-477ED45A-FBF9-4A4F-8483-A304F1A6ADA3-a5.svg']

#### Second-Order

Second-order
 DC noise rejection applies a triangular weighting to the measurement samples. In
 second-order DC noise rejection, the samples taken in the middle of the aperture
 time are weighted more than samples taken at the beginning and the end of the
 measurement.

[IMAGE alt='image' src='GUID-0E770D6D-18B5-471D-A8B9-6A7C81F786B6-a5.svg']

Notice that you can obtain very good rejection near even
 multiples of f0 and that rejection increases more rapidly with
 frequency than with normal sample weighting. Also notice that the response notches
 are wider than they are with normal weighting, resulting in less sensitivity to
 slight variations in noise frequency. Use second-order DC noise rejection if you
 need better powerline noise rejection than you can get with normal DC noise
 rejection, but cannot afford to read slowly enough to take advantage of high-order
 noise rejection. For example, you could set the aperture to 33.333 msec for a 60 Hz
 powerline frequency.

#### High-Order

The following figure shows noise rejection with high order sample weighting.

[IMAGE alt='image' src='GUID-530A014E-C47D-4DBB-8A8E-834C081CED2D-a5.svg']

Note

Notice that noise rejection is good starting at around four times f0 and is excellent above about 4.5 times f0. Rejection of noise at any frequency above 4.6 times f0 exceeds 98 dB. An NI 407x or NI 408x, using high-order DC noise rejection with a 100 msec aperture, can deliver full 6½ digit accuracy on the 10 V range with over 1 V of interfering powerline noise at any frequency above 46 Hz.

The small tradeoff to using the higher-order filters is that to obtain powerline rejection, you must increase the measurement aperture by 2x (for second-order) or 4x (for high-order) versus that required for the normal setting.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-noise-rejection_5.html language=enus -->
## TOPIC 00198: DC Noise Rejection

- bundle_id: `ni-dmm`
- source_path: `dc-noise-rejection_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-noise-rejection_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequen

### DC Noise Rejection

DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequencies. The DMM offers three different modes: normal, second-order, and high-order.

Refer to the following table for a list of the differences between the three modes:

| DC Noise Rejection Setting | Lowest Frequency for Noise Rejection | High-Frequency Noise Rejection |
| --- | --- | --- |
| Normal | 1/taperture | Good |
| Second-Order | 2/taperture | Better |
| High-Order | 4/taperture | Best |

Refer to the table in the Aperture Time section for the default aperture times and DC noise rejection settings used by the DMM.

#### Normal

When you select normal DC noise rejection, the DMM weights all samples equally. This feature emulates the behavior of most traditional DMMs, providing good rejection of frequencies at multiples of f0, where f0 = 1/t<sub>aperture</sub>. The following figure shows normal weighting, where all samples are weighted equally, and the resulting noise rejection as a function of frequency. Notice that you can obtain good rejection only very near multiples of f0. To get the fastest possible readings that give you some powerline noise rejection, set the aperture to the powerline period, such as 16.667 msec for a 60 Hz powerline frequency, and set the DC noise rejection to normal.

[IMAGE alt='image' src='GUID-477ED45A-FBF9-4A4F-8483-A304F1A6ADA3-a5.svg']

#### Second-Order

Second-order
 DC noise rejection applies a triangular weighting to the measurement samples. In
 second-order DC noise rejection, the samples taken in the middle of the aperture
 time are weighted more than samples taken at the beginning and the end of the
 measurement.

[IMAGE alt='image' src='GUID-0E770D6D-18B5-471D-A8B9-6A7C81F786B6-a5.svg']

Notice that you can obtain very good rejection near even
 multiples of f0 and that rejection increases more rapidly with
 frequency than with normal sample weighting. Also notice that the response notches
 are wider than they are with normal weighting, resulting in less sensitivity to
 slight variations in noise frequency. Use second-order DC noise rejection if you
 need better powerline noise rejection than you can get with normal DC noise
 rejection, but cannot afford to read slowly enough to take advantage of high-order
 noise rejection. For example, you could set the aperture to 33.333 msec for a 60 Hz
 powerline frequency.

#### High-Order

The following figure shows noise rejection with high order sample weighting.

[IMAGE alt='image' src='GUID-530A014E-C47D-4DBB-8A8E-834C081CED2D-a5.svg']

Note

Notice that noise rejection is good starting at around four times f0 and is excellent above about 4.5 times f0. Rejection of noise at any frequency above 4.6 times f0 exceeds 98 dB. An NI 407x or NI 408x, using high-order DC noise rejection with a 100 msec aperture, can deliver full 6½ digit accuracy on the 10 V range with over 1 V of interfering powerline noise at any frequency above 46 Hz.

The small tradeoff to using the higher-order filters is that to obtain powerline rejection, you must increase the measurement aperture by 2x (for second-order) or 4x (for high-order) versus that required for the normal setting.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-noise-rejection_6.html language=enus -->
## TOPIC 00199: DC Noise Rejection

- bundle_id: `ni-dmm`
- source_path: `dc-noise-rejection_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-noise-rejection_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequen

### DC Noise Rejection

DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequencies. The DMM offers three different modes: normal, second-order, and high-order.

Refer to the following table for a list of the differences between the three modes:

| DC Noise Rejection Setting | Lowest Frequency for Noise Rejection | High-Frequency Noise Rejection |
| --- | --- | --- |
| Normal | 1/taperture | Good |
| Second-Order | 2/taperture | Better |
| High-Order | 4/taperture | Best |

Refer to the table in the Aperture Time section for the default aperture times and DC noise rejection settings used by the DMM.

#### Normal

When you select normal DC noise rejection, the DMM weights all samples equally. This feature emulates the behavior of most traditional DMMs, providing good rejection of frequencies at multiples of f0, where f0 = 1/t<sub>aperture</sub>. The following figure shows normal weighting, where all samples are weighted equally, and the resulting noise rejection as a function of frequency. Notice that you can obtain good rejection only very near multiples of f0. To get the fastest possible readings that give you some powerline noise rejection, set the aperture to the powerline period, such as 16.667 msec for a 60 Hz powerline frequency, and set the DC noise rejection to normal.

[IMAGE alt='image' src='GUID-477ED45A-FBF9-4A4F-8483-A304F1A6ADA3-a5.svg']

#### Second-Order

Second-order
 DC noise rejection applies a triangular weighting to the measurement samples. In
 second-order DC noise rejection, the samples taken in the middle of the aperture
 time are weighted more than samples taken at the beginning and the end of the
 measurement.

[IMAGE alt='image' src='GUID-0E770D6D-18B5-471D-A8B9-6A7C81F786B6-a5.svg']

Notice that you can obtain very good rejection near even
 multiples of f0 and that rejection increases more rapidly with
 frequency than with normal sample weighting. Also notice that the response notches
 are wider than they are with normal weighting, resulting in less sensitivity to
 slight variations in noise frequency. Use second-order DC noise rejection if you
 need better powerline noise rejection than you can get with normal DC noise
 rejection, but cannot afford to read slowly enough to take advantage of high-order
 noise rejection. For example, you could set the aperture to 33.333 msec for a 60 Hz
 powerline frequency.

#### High-Order

The following figure shows noise rejection with high order sample weighting.

[IMAGE alt='image' src='GUID-530A014E-C47D-4DBB-8A8E-834C081CED2D-a5.svg']

Note

Notice that noise rejection is good starting at around four times f0 and is excellent above about 4.5 times f0. Rejection of noise at any frequency above 4.6 times f0 exceeds 98 dB. An NI 407x or NI 408x, using high-order DC noise rejection with a 100 msec aperture, can deliver full 6½ digit accuracy on the 10 V range with over 1 V of interfering powerline noise at any frequency above 46 Hz.

The small tradeoff to using the higher-order filters is that to obtain powerline rejection, you must increase the measurement aperture by 2x (for second-order) or 4x (for high-order) versus that required for the normal setting.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-noise-rejection_7.html language=enus -->
## TOPIC 00200: DC Noise Rejection

- bundle_id: `ni-dmm`
- source_path: `dc-noise-rejection_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-noise-rejection_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequen

### DC Noise Rejection

DC noise rejection is a configurable noise reduction feature available for DMM DC measurements. Each DC reading the DMM returns is actually an average of multiple high-speed samples. By adjusting the relative weighting of those samples, you can adjust the sensitivity to different interfering frequencies. The DMM offers three different modes: normal, second-order, and high-order.

Refer to the following table for a list of the differences between the three modes:

| DC Noise Rejection Setting | Lowest Frequency for Noise Rejection | High-Frequency Noise Rejection |
| --- | --- | --- |
| Normal | 1/taperture | Good |
| Second-Order | 2/taperture | Better |
| High-Order | 4/taperture | Best |

Refer to the table in the Aperture Time section for the default aperture times and DC noise rejection settings used by the DMM.

#### Normal

When you select normal DC noise rejection, the DMM weights all samples equally. This feature emulates the behavior of most traditional DMMs, providing good rejection of frequencies at multiples of f0, where f0 = 1/t<sub>aperture</sub>. The following figure shows normal weighting, where all samples are weighted equally, and the resulting noise rejection as a function of frequency. Notice that you can obtain good rejection only very near multiples of f0. To get the fastest possible readings that give you some powerline noise rejection, set the aperture to the powerline period, such as 16.667 msec for a 60 Hz powerline frequency, and set the DC noise rejection to normal.

[IMAGE alt='image' src='GUID-477ED45A-FBF9-4A4F-8483-A304F1A6ADA3-a5.svg']

#### Second-Order

Second-order
 DC noise rejection applies a triangular weighting to the measurement samples. In
 second-order DC noise rejection, the samples taken in the middle of the aperture
 time are weighted more than samples taken at the beginning and the end of the
 measurement.

[IMAGE alt='image' src='GUID-0E770D6D-18B5-471D-A8B9-6A7C81F786B6-a5.svg']

Notice that you can obtain very good rejection near even
 multiples of f0 and that rejection increases more rapidly with
 frequency than with normal sample weighting. Also notice that the response notches
 are wider than they are with normal weighting, resulting in less sensitivity to
 slight variations in noise frequency. Use second-order DC noise rejection if you
 need better powerline noise rejection than you can get with normal DC noise
 rejection, but cannot afford to read slowly enough to take advantage of high-order
 noise rejection. For example, you could set the aperture to 33.333 msec for a 60 Hz
 powerline frequency.

#### High-Order

The following figure shows noise rejection with high order sample weighting.

[IMAGE alt='image' src='GUID-530A014E-C47D-4DBB-8A8E-834C081CED2D-a5.svg']

Note

Notice that noise rejection is good starting at around four times f0 and is excellent above about 4.5 times f0. Rejection of noise at any frequency above 4.6 times f0 exceeds 98 dB. An NI 407x or NI 408x, using high-order DC noise rejection with a 100 msec aperture, can deliver full 6½ digit accuracy on the 10 V range with over 1 V of interfering powerline noise at any frequency above 46 Hz.

The small tradeoff to using the higher-order filters is that to obtain powerline rejection, you must increase the measurement aperture by 2x (for second-order) or 4x (for high-order) versus that required for the normal setting.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=dc-voltage.html language=enus -->
## TOPIC 00201: DC Voltage

- bundle_id: `ni-dmm`
- source_path: `dc-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-voltage.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.Selectable Input ResistanceYou can select the DCV input resistance to optimize meas

### DC Voltage

The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.

#### Selectable Input Resistance

You can select the DCV input resistance to optimize measurement performance in situations where large source resistance is present. In the following figure, S<sub>1</sub> is used to select a 10 MΩ input resistance on the 0.1 V, 1 V, and 10 V DC ranges.

[IMAGE alt='image' src='GUID-4D5C55C3-6FF5-4E1E-B94C-E4B309A11144-a5.svg']

The following figure shows an equivalent circuit after the 10 MΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2EDF6F91-3556-4AB0-9055-14967064AD30-a5.svg']

The following figure shows an equivalent circuit after the 10 GΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2584215B-11E9-4427-B783-E2E57F1A83FE-a5.svg']

Refer to the overview section for your device for information on input resistance values.

#### Input Bias Current

If the source resistance is greater than 10 kΩ, then you may need to include the effects of input bias current in addition to input resistance. For example, for 100 kΩ source resistance, a 100 pA bias current creates an offset error of 10 µV, as shown in the following figure.

[IMAGE alt='image' src='GUID-F216BD3A-750B-497E-80F7-28A1723983A8-a5.svg']

With an input resistance of >10 GΩ selected, most of the input bias current flows through the source resistance (100 kΩ), causing an offset voltage.

DMM input bias current approximately doubles for every 10 ºC of environmental temperature increase. For example, an input bias current of 25 pA at 23 ºC translates to about 50 pA at 33 ºC, 100 pA at 43 ºC, and so on. Likewise, as temperature is decreased, the current drops 50% for every 10 ºC. Thus, at 13 ºC, the input bias current is approximately 12.5 pA.

Parent topic:

DMM Measurements

Related concepts:

- Thermal Voltages

<!--NI_TOPIC bundle=ni-dmm path=dc-voltage_2.html language=enus -->
## TOPIC 00202: DC Voltage

- bundle_id: `ni-dmm`
- source_path: `dc-voltage_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-voltage_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.Selectable Input ResistanceYou can select the DCV input resistance to optimize meas

### DC Voltage

The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.

#### Selectable Input Resistance

You can select the DCV input resistance to optimize measurement performance in situations where large source resistance is present. In the following figure, S<sub>1</sub> is used to select a 10 MΩ input resistance on the 0.1 V, 1 V, and 10 V DC ranges.

[IMAGE alt='image' src='GUID-4D5C55C3-6FF5-4E1E-B94C-E4B309A11144-a5.svg']

The following figure shows an equivalent circuit after the 10 MΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2EDF6F91-3556-4AB0-9055-14967064AD30-a5.svg']

The following figure shows an equivalent circuit after the 10 GΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2584215B-11E9-4427-B783-E2E57F1A83FE-a5.svg']

Refer to the overview section for your device for information on input resistance values.

#### Input Bias Current

If the source resistance is greater than 10 kΩ, then you may need to include the effects of input bias current in addition to input resistance. For example, for 100 kΩ source resistance, a 100 pA bias current creates an offset error of 10 µV, as shown in the following figure.

[IMAGE alt='image' src='GUID-F216BD3A-750B-497E-80F7-28A1723983A8-a5.svg']

With an input resistance of >10 GΩ selected, most of the input bias current flows through the source resistance (100 kΩ), causing an offset voltage.

DMM input bias current approximately doubles for every 10 ºC of environmental temperature increase. For example, an input bias current of 25 pA at 23 ºC translates to about 50 pA at 33 ºC, 100 pA at 43 ºC, and so on. Likewise, as temperature is decreased, the current drops 50% for every 10 ºC. Thus, at 13 ºC, the input bias current is approximately 12.5 pA.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=dc-voltage_3.html language=enus -->
## TOPIC 00203: DC Voltage

- bundle_id: `ni-dmm`
- source_path: `dc-voltage_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-voltage_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.Selectable Input ResistanceYou can select the DCV input resistance to optimize meas

### DC Voltage

The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.

#### Selectable Input Resistance

You can select the DCV input resistance to optimize measurement performance in situations where large source resistance is present. In the following figure, S<sub>1</sub> is used to select a 10 MΩ input resistance on the 0.1 V, 1 V, and 10 V DC ranges.

[IMAGE alt='image' src='GUID-4D5C55C3-6FF5-4E1E-B94C-E4B309A11144-a5.svg']

The following figure shows an equivalent circuit after the 10 MΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2EDF6F91-3556-4AB0-9055-14967064AD30-a5.svg']

The following figure shows an equivalent circuit after the 10 GΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2584215B-11E9-4427-B783-E2E57F1A83FE-a5.svg']

Refer to the overview section for your device for information on input resistance values.

#### Input Bias Current

If the source resistance is greater than 10 kΩ, then you may need to include the effects of input bias current in addition to input resistance. For example, for 100 kΩ source resistance, a 100 pA bias current creates an offset error of 10 µV, as shown in the following figure.

[IMAGE alt='image' src='GUID-F216BD3A-750B-497E-80F7-28A1723983A8-a5.svg']

With an input resistance of >10 GΩ selected, most of the input bias current flows through the source resistance (100 kΩ), causing an offset voltage.

DMM input bias current approximately doubles for every 10 ºC of environmental temperature increase. For example, an input bias current of 25 pA at 23 ºC translates to about 50 pA at 33 ºC, 100 pA at 43 ºC, and so on. Likewise, as temperature is decreased, the current drops 50% for every 10 ºC. Thus, at 13 ºC, the input bias current is approximately 12.5 pA.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=dc-voltage_4.html language=enus -->
## TOPIC 00204: DC Voltage

- bundle_id: `ni-dmm`
- source_path: `dc-voltage_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-voltage_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.Selectable Input ResistanceYou can select the DCV input resistance to optimize meas

### DC Voltage

The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.

#### Selectable Input Resistance

You can select the DCV input resistance to optimize measurement performance in situations where large source resistance is present. In the following figure, S<sub>1</sub> is used to select a 10 MΩ input resistance on the 0.1 V, 1 V, and 10 V DC ranges.

[IMAGE alt='image' src='GUID-4D5C55C3-6FF5-4E1E-B94C-E4B309A11144-a5.svg']

The following figure shows an equivalent circuit after the 10 MΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2EDF6F91-3556-4AB0-9055-14967064AD30-a5.svg']

The following figure shows an equivalent circuit after the 10 GΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2584215B-11E9-4427-B783-E2E57F1A83FE-a5.svg']

Refer to the overview section for your device for information on input resistance values.

#### Input Bias Current

If the source resistance is greater than 10 kΩ, then you may need to include the effects of input bias current in addition to input resistance. For example, for 100 kΩ source resistance, a 100 pA bias current creates an offset error of 10 µV, as shown in the following figure.

[IMAGE alt='image' src='GUID-F216BD3A-750B-497E-80F7-28A1723983A8-a5.svg']

With an input resistance of >10 GΩ selected, most of the input bias current flows through the source resistance (100 kΩ), causing an offset voltage.

DMM input bias current approximately doubles for every 10 ºC of environmental temperature increase. For example, an input bias current of 25 pA at 23 ºC translates to about 50 pA at 33 ºC, 100 pA at 43 ºC, and so on. Likewise, as temperature is decreased, the current drops 50% for every 10 ºC. Thus, at 13 ºC, the input bias current is approximately 12.5 pA.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=dc-voltage_5.html language=enus -->
## TOPIC 00205: DC Voltage

- bundle_id: `ni-dmm`
- source_path: `dc-voltage_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-voltage_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.Selectable Input ResistanceYou can select the DCV input resistance to optimize meas

### DC Voltage

The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.

#### Selectable Input Resistance

You can select the DCV input resistance to optimize measurement performance in situations where large source resistance is present. In the following figure, S<sub>1</sub> is used to select a 10 MΩ input resistance on the 0.1 V, 1 V, and 10 V DC ranges.

[IMAGE alt='image' src='GUID-4D5C55C3-6FF5-4E1E-B94C-E4B309A11144-a5.svg']

The following figure shows an equivalent circuit after the 10 MΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2EDF6F91-3556-4AB0-9055-14967064AD30-a5.svg']

The following figure shows an equivalent circuit after the 10 GΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2584215B-11E9-4427-B783-E2E57F1A83FE-a5.svg']

Refer to the overview section for your device for information on input resistance values.

#### Input Bias Current

If the source resistance is greater than 10 kΩ, then you may need to include the effects of input bias current in addition to input resistance. For example, for 100 kΩ source resistance, a 100 pA bias current creates an offset error of 10 µV, as shown in the following figure.

[IMAGE alt='image' src='GUID-F216BD3A-750B-497E-80F7-28A1723983A8-a5.svg']

With an input resistance of >10 GΩ selected, most of the input bias current flows through the source resistance (100 kΩ), causing an offset voltage.

DMM input bias current approximately doubles for every 10 ºC of environmental temperature increase. For example, an input bias current of 25 pA at 23 ºC translates to about 50 pA at 33 ºC, 100 pA at 43 ºC, and so on. Likewise, as temperature is decreased, the current drops 50% for every 10 ºC. Thus, at 13 ºC, the input bias current is approximately 12.5 pA.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=dc-voltage_6.html language=enus -->
## TOPIC 00206: DC Voltage

- bundle_id: `ni-dmm`
- source_path: `dc-voltage_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-voltage_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.Selectable Input ResistanceYou can select the DCV input resistance to optimize meas

### DC Voltage

The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.

#### Selectable Input Resistance

You can select the DCV input resistance to optimize measurement performance in situations where large source resistance is present. In the following figure, S<sub>1</sub> is used to select a 10 MΩ input resistance on the 0.1 V, 1 V, and 10 V DC ranges.

[IMAGE alt='image' src='GUID-4D5C55C3-6FF5-4E1E-B94C-E4B309A11144-a5.svg']

The following figure shows an equivalent circuit after the 10 MΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2EDF6F91-3556-4AB0-9055-14967064AD30-a5.svg']

The following figure shows an equivalent circuit after the 10 GΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2584215B-11E9-4427-B783-E2E57F1A83FE-a5.svg']

Refer to the overview section for your device for information on input resistance values.

#### Input Bias Current

If the source resistance is greater than 10 kΩ, then you may need to include the effects of input bias current in addition to input resistance. For example, for 100 kΩ source resistance, a 100 pA bias current creates an offset error of 10 µV, as shown in the following figure.

[IMAGE alt='image' src='GUID-F216BD3A-750B-497E-80F7-28A1723983A8-a5.svg']

With an input resistance of >10 GΩ selected, most of the input bias current flows through the source resistance (100 kΩ), causing an offset voltage.

DMM input bias current approximately doubles for every 10 ºC of environmental temperature increase. For example, an input bias current of 25 pA at 23 ºC translates to about 50 pA at 33 ºC, 100 pA at 43 ºC, and so on. Likewise, as temperature is decreased, the current drops 50% for every 10 ºC. Thus, at 13 ºC, the input bias current is approximately 12.5 pA.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=dc-voltage_7.html language=enus -->
## TOPIC 00207: DC Voltage

- bundle_id: `ni-dmm`
- source_path: `dc-voltage_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dc-voltage_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.Selectable Input ResistanceYou can select the DCV input resistance to optimize meas

### DC Voltage

The DMM can measure signals in the sub-microvolt range. To take accurate low-voltage measurements with confidence, consider the following factors: thermal voltages, selectable input resistance, and input bias current.

#### Selectable Input Resistance

You can select the DCV input resistance to optimize measurement performance in situations where large source resistance is present. In the following figure, S<sub>1</sub> is used to select a 10 MΩ input resistance on the 0.1 V, 1 V, and 10 V DC ranges.

[IMAGE alt='image' src='GUID-4D5C55C3-6FF5-4E1E-B94C-E4B309A11144-a5.svg']

The following figure shows an equivalent circuit after the 10 MΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2EDF6F91-3556-4AB0-9055-14967064AD30-a5.svg']

The following figure shows an equivalent circuit after the 10 GΩ input resistance has been selected:

[IMAGE alt='image' src='GUID-2584215B-11E9-4427-B783-E2E57F1A83FE-a5.svg']

Refer to the overview section for your device for information on input resistance values.

#### Input Bias Current

If the source resistance is greater than 10 kΩ, then you may need to include the effects of input bias current in addition to input resistance. For example, for 100 kΩ source resistance, a 100 pA bias current creates an offset error of 10 µV, as shown in the following figure.

[IMAGE alt='image' src='GUID-F216BD3A-750B-497E-80F7-28A1723983A8-a5.svg']

With an input resistance of >10 GΩ selected, most of the input bias current flows through the source resistance (100 kΩ), causing an offset voltage.

DMM input bias current approximately doubles for every 10 ºC of environmental temperature increase. For example, an input bias current of 25 pA at 23 ºC translates to about 50 pA at 33 ºC, 100 pA at 43 ºC, and so on. Likewise, as temperature is decreased, the current drops 50% for every 10 ºC. Thus, at 13 ºC, the input bias current is approximately 12.5 pA.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=dielectric-absorption.html language=enus -->
## TOPIC 00208: Dielectric Absorption

- bundle_id: `ni-dmm`
- source_path: `dielectric-absorption.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dielectric-absorption.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Dielectric absorption caused by cable materials can increase settling time. The figure below illustrates dielectric absorption due to cable resistance and dielectric polarization capacitance where:R[DA] = Insulation resistance of cabling (10 GΩ–10^14Ω) C[DA] = Dielectric polarization capacitance (0.

### Dielectric Absorption

Dielectric absorption caused by cable materials can increase settling time. The figure below illustrates dielectric absorption due to cable resistance and dielectric polarization capacitance where:

R<sub>DA</sub> = Insulation resistance of cabling (10 GΩ–10<sup>14</sup>Ω)

C<sub>DA</sub> = Dielectric polarization capacitance (0.1–1 pF/ft)

C<sub>C</sub> = Cable capacitance (10–40 pF/ft)

[IMAGE alt='image' src='GUID-1A203146-9ED7-4E7C-8AB4-90363A75B631-a5.svg']

The RC formed by R<sub>DA</sub> and C<sub>DA</sub> results in slow settle tails that significantly lengthen settling time.

The best way to avoid dielectric absorption effects is to use a high-quality cable, such as
 Belden 83317E available. Refer to the Belden CDT
 Incorporated website for information about this
 cable.

NI recommends cables with Teflon, polypropylene, or polyethylene insulation. For more information
 about cabling requirements, refer to *Interconnects and Cables*.

Parent topic:

Measurement Considerations

Related concepts:

- NI 4070

Related information:

- Belden Inc.

<!--NI_TOPIC bundle=ni-dmm path=diode.html language=enus -->
## TOPIC 00209: Diode

- bundle_id: `ni-dmm`
- source_path: `diode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/diode.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be

### Diode

The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be measured with this setting. You can also set the current source to 1 uA, 10 uA, or 100 uA for the NI 4080/4081/4082 and NI 4070/4071/4072 and 100 uA for the NI 4065, in which case voltage up to 10 V can be measured. Refer to niDMM Configure Current Source or niDMM_ConfigureCurrentSource for more information about how to configure the current source.

Parent topic:

DMM Measurements

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=diode_2.html language=enus -->
## TOPIC 00210: Diode

- bundle_id: `ni-dmm`
- source_path: `diode_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/diode_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be

### Diode

The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be measured with this setting. You can also set the current source to 1 uA, 10 uA, or 100 uA for the NI 4080/4081/4082 and NI 4070/4071/4072 and 100 uA for the NI 4065, in which case voltage up to 10 V can be measured. Refer to niDMM Configure Current Source or niDMM_ConfigureCurrentSource for more information about how to configure the current source.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=diode_3.html language=enus -->
## TOPIC 00211: Diode

- bundle_id: `ni-dmm`
- source_path: `diode_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/diode_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be

### Diode

The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be measured with this setting. You can also set the current source to 1 uA, 10 uA, or 100 uA for the NI 4080/4081/4082 and NI 4070/4071/4072 and 100 uA for the NI 4065, in which case voltage up to 10 V can be measured. Refer to niDMM Configure Current Source or niDMM_ConfigureCurrentSource for more information about how to configure the current source.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=diode_4.html language=enus -->
## TOPIC 00212: Diode

- bundle_id: `ni-dmm`
- source_path: `diode_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/diode_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be

### Diode

The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be measured with this setting. You can also set the current source to 1 uA, 10 uA, or 100 uA for the NI 4080/4081/4082 and NI 4070/4071/4072 and 100 uA for the NI 4065, in which case voltage up to 10 V can be measured. Refer to niDMM Configure Current Source or niDMM_ConfigureCurrentSource for more information about how to configure the current source.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=diode_5.html language=enus -->
## TOPIC 00213: Diode

- bundle_id: `ni-dmm`
- source_path: `diode_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/diode_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be

### Diode

The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be measured with this setting. You can also set the current source to 1 uA, 10 uA, or 100 uA for the NI 4080/4081/4082 and NI 4070/4071/4072 and 100 uA for the NI 4065, in which case voltage up to 10 V can be measured. Refer to niDMM Configure Current Source or niDMM_ConfigureCurrentSource for more information about how to configure the current source.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=diode_6.html language=enus -->
## TOPIC 00214: Diode

- bundle_id: `ni-dmm`
- source_path: `diode_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/diode_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be

### Diode

The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be measured with this setting. You can also set the current source to 1 uA, 10 uA, or 100 uA for the NI 4080/4081/4082 and NI 4070/4071/4072 and 100 uA for the NI 4065, in which case voltage up to 10 V can be measured. Refer to niDMM Configure Current Source or niDMM_ConfigureCurrentSource for more information about how to configure the current source.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=diode_7.html language=enus -->
## TOPIC 00215: Diode

- bundle_id: `ni-dmm`
- source_path: `diode_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/diode_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be

### Diode

The DMM can excite a DUT with a constant current source and read the resulting voltage drop using a 10 V DC range. Diode mode is useful for testing p-n junctions, LEDs, and zener diodes. The default current excitation is 1 mA, and a voltage up to 4.5 V (4.0 V for NI 4071 or 3.5 V for NI 4065) can be measured with this setting. You can also set the current source to 1 uA, 10 uA, or 100 uA for the NI 4080/4081/4082 and NI 4070/4071/4072 and 100 uA for the NI 4065, in which case voltage up to 10 V can be measured. Refer to niDMM Configure Current Source or niDMM_ConfigureCurrentSource for more information about how to configure the current source.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=dmm-settling-time.html language=enus -->
## TOPIC 00216: Settling Time

- bundle_id: `ni-dmm`
- source_path: `dmm-settling-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dmm-settling-time.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices unde

### Settling Time

Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.

You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices under test (DUTs) through a multiplexing switch:

[IMAGE alt='image' src='GUID-610440AB-7B07-463D-945D-8786F509598C-a5.svg']

Whenever the external switch changes channels, the DMM input is connected to a different voltage or resistance. Each time this process happens, the DMM, interacting with the source, behaves as an RC circuit with a settling time that corresponds to:

ST = kRC

where

R = equivalent resistance of the source

C = the equivalent input capacitance seen by the DMM (C <sub>COM</sub> + C <sub>CX</sub> + C<sub>IN</sub>), where C<sub>CX</sub> = C<sub>C1</sub> or C<sub>C2</sub> or C<sub>C3</sub> (cable capacitances) depending on the channel selected

k = value related to accuracy required, as shown in the following table; increases as required accuracy increases

ST = settling time required

Note

| k | Error | Required Resolution(for full range step) |
| --- | --- | --- |
| 3 | 4.98% | — |
| 4 | 1.83% | — |
| 5 | 0.674% | — |
| 6 | 0.248% | — |
| 7 | 0.091% | — |
| 8 | 0.033% | 3½ digits |
| 9 | 0.012% | — |
| 10 | 0.0045% | 4½ digits |
| 11 | 0.0017% | — |
| 12 | 0.00061% | 5½ digits |
| 13 | 0.00023% | — |
| 14 | 0.000083% | 6½ digits |
| 15 | 0.000031% | — |
| 16 | 0.000011% | 7 digits |
| 17 | 0.000004% | 7½ digits |

Adjusting the default settling time may be important when you are measuring or scanning resistances with values above 10 kΩ, when C >500 pF, and when speed is of the utmost importance. For the input capacitance of the DMM, refer to the specifications document for your device. The cable capacitance can be significantly more than the input capacitance. Cable material dielectric absorption complicates the settling time issue.

When switching to the next measurement, consider the following example. Assume a 10 V step occurs on the 10 V range with a required resolution of 6½ digits. Referring to the previous table for 6½ digit settling, k = 14 is required. Consider next a 10 mV step on the 10 V range. The step, being 0.1% of range (10 mV/10 V = 0.1%), can only be observed to 0.1% beyond that (assuming a 6½ digit resolution). In this example, the maximum time required from the previous table corresponds to k = 7, which yields 0.091%. If the difference between channels is known to never exceed 10 mV, then you can save considerable settling time. If you cannot predict what the values are from channel to channel, consider the accuracy required in the measurement. Then assume a step size equal to the full range to identify k.

The analysis in the previous example is for fixed range operation. You can select Auto Range for the measurement, but additional delays occur as the DMM seeks the appropriate range for the measurement. NI does not recommend Auto Range for optimum speed.

Parent topic:

DMM Measurement Cycle

Related concepts:

- Using Switches
- Dielectric Absorption
- DMM Measurement Defaults
- DMM Measurement Defaults
- DMM Measurement Defaults

<!--NI_TOPIC bundle=ni-dmm path=dmm-settling-time_2.html language=enus -->
## TOPIC 00217: Settling Time

- bundle_id: `ni-dmm`
- source_path: `dmm-settling-time_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dmm-settling-time_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices unde

### Settling Time

Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.

You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices under test (DUTs) through a multiplexing switch:

[IMAGE alt='image' src='GUID-610440AB-7B07-463D-945D-8786F509598C-a5.svg']

Whenever the external switch changes channels, the DMM input is connected to a different voltage or resistance. Each time this process happens, the DMM, interacting with the source, behaves as an RC circuit with a settling time that corresponds to:

ST = kRC

where

R = equivalent resistance of the source

C = the equivalent input capacitance seen by the DMM (C <sub>COM</sub> + C <sub>CX</sub> + C<sub>IN</sub>), where C<sub>CX</sub> = C<sub>C1</sub> or C<sub>C2</sub> or C<sub>C3</sub> (cable capacitances) depending on the channel selected

k = value related to accuracy required, as shown in the following table; increases as required accuracy increases

ST = settling time required

Note

| k | Error | Required Resolution(for full range step) |
| --- | --- | --- |
| 3 | 4.98% | — |
| 4 | 1.83% | — |
| 5 | 0.674% | — |
| 6 | 0.248% | — |
| 7 | 0.091% | — |
| 8 | 0.033% | 3½ digits |
| 9 | 0.012% | — |
| 10 | 0.0045% | 4½ digits |
| 11 | 0.0017% | — |
| 12 | 0.00061% | 5½ digits |
| 13 | 0.00023% | — |
| 14 | 0.000083% | 6½ digits |
| 15 | 0.000031% | — |
| 16 | 0.000011% | 7 digits |
| 17 | 0.000004% | 7½ digits |

Adjusting the default settling time may be important when you are measuring or scanning resistances with values above 10 kΩ, when C >500 pF, and when speed is of the utmost importance. For the input capacitance of the DMM, refer to the specifications document for your device. The cable capacitance can be significantly more than the input capacitance. Cable material dielectric absorption complicates the settling time issue.

When switching to the next measurement, consider the following example. Assume a 10 V step occurs on the 10 V range with a required resolution of 6½ digits. Referring to the previous table for 6½ digit settling, k = 14 is required. Consider next a 10 mV step on the 10 V range. The step, being 0.1% of range (10 mV/10 V = 0.1%), can only be observed to 0.1% beyond that (assuming a 6½ digit resolution). In this example, the maximum time required from the previous table corresponds to k = 7, which yields 0.091%. If the difference between channels is known to never exceed 10 mV, then you can save considerable settling time. If you cannot predict what the values are from channel to channel, consider the accuracy required in the measurement. Then assume a step size equal to the full range to identify k.

The analysis in the previous example is for fixed range operation. You can select Auto Range for the measurement, but additional delays occur as the DMM seeks the appropriate range for the measurement. NI does not recommend Auto Range for optimum speed.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=dmm-settling-time_3.html language=enus -->
## TOPIC 00218: Settling Time

- bundle_id: `ni-dmm`
- source_path: `dmm-settling-time_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dmm-settling-time_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices unde

### Settling Time

Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.

You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices under test (DUTs) through a multiplexing switch:

[IMAGE alt='image' src='GUID-610440AB-7B07-463D-945D-8786F509598C-a5.svg']

Whenever the external switch changes channels, the DMM input is connected to a different voltage or resistance. Each time this process happens, the DMM, interacting with the source, behaves as an RC circuit with a settling time that corresponds to:

ST = kRC

where

R = equivalent resistance of the source

C = the equivalent input capacitance seen by the DMM (C <sub>COM</sub> + C <sub>CX</sub> + C<sub>IN</sub>), where C<sub>CX</sub> = C<sub>C1</sub> or C<sub>C2</sub> or C<sub>C3</sub> (cable capacitances) depending on the channel selected

k = value related to accuracy required, as shown in the following table; increases as required accuracy increases

ST = settling time required

Note

| k | Error | Required Resolution(for full range step) |
| --- | --- | --- |
| 3 | 4.98% | — |
| 4 | 1.83% | — |
| 5 | 0.674% | — |
| 6 | 0.248% | — |
| 7 | 0.091% | — |
| 8 | 0.033% | 3½ digits |
| 9 | 0.012% | — |
| 10 | 0.0045% | 4½ digits |
| 11 | 0.0017% | — |
| 12 | 0.00061% | 5½ digits |
| 13 | 0.00023% | — |
| 14 | 0.000083% | 6½ digits |
| 15 | 0.000031% | — |
| 16 | 0.000011% | 7 digits |
| 17 | 0.000004% | 7½ digits |

Adjusting the default settling time may be important when you are measuring or scanning resistances with values above 10 kΩ, when C >500 pF, and when speed is of the utmost importance. For the input capacitance of the DMM, refer to the specifications document for your device. The cable capacitance can be significantly more than the input capacitance. Cable material dielectric absorption complicates the settling time issue.

When switching to the next measurement, consider the following example. Assume a 10 V step occurs on the 10 V range with a required resolution of 6½ digits. Referring to the previous table for 6½ digit settling, k = 14 is required. Consider next a 10 mV step on the 10 V range. The step, being 0.1% of range (10 mV/10 V = 0.1%), can only be observed to 0.1% beyond that (assuming a 6½ digit resolution). In this example, the maximum time required from the previous table corresponds to k = 7, which yields 0.091%. If the difference between channels is known to never exceed 10 mV, then you can save considerable settling time. If you cannot predict what the values are from channel to channel, consider the accuracy required in the measurement. Then assume a step size equal to the full range to identify k.

The analysis in the previous example is for fixed range operation. You can select Auto Range for the measurement, but additional delays occur as the DMM seeks the appropriate range for the measurement. NI does not recommend Auto Range for optimum speed.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=dmm-settling-time_4.html language=enus -->
## TOPIC 00219: Settling Time

- bundle_id: `ni-dmm`
- source_path: `dmm-settling-time_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dmm-settling-time_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices unde

### Settling Time

Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.

You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices under test (DUTs) through a multiplexing switch:

[IMAGE alt='image' src='GUID-610440AB-7B07-463D-945D-8786F509598C-a5.svg']

Whenever the external switch changes channels, the DMM input is connected to a different voltage or resistance. Each time this process happens, the DMM, interacting with the source, behaves as an RC circuit with a settling time that corresponds to:

ST = kRC

where

R = equivalent resistance of the source

C = the equivalent input capacitance seen by the DMM (C <sub>COM</sub> + C <sub>CX</sub> + C<sub>IN</sub>), where C<sub>CX</sub> = C<sub>C1</sub> or C<sub>C2</sub> or C<sub>C3</sub> (cable capacitances) depending on the channel selected

k = value related to accuracy required, as shown in the following table; increases as required accuracy increases

ST = settling time required

Note

| k | Error | Required Resolution(for full range step) |
| --- | --- | --- |
| 3 | 4.98% | — |
| 4 | 1.83% | — |
| 5 | 0.674% | — |
| 6 | 0.248% | — |
| 7 | 0.091% | — |
| 8 | 0.033% | 3½ digits |
| 9 | 0.012% | — |
| 10 | 0.0045% | 4½ digits |
| 11 | 0.0017% | — |
| 12 | 0.00061% | 5½ digits |
| 13 | 0.00023% | — |
| 14 | 0.000083% | 6½ digits |
| 15 | 0.000031% | — |
| 16 | 0.000011% | 7 digits |
| 17 | 0.000004% | 7½ digits |

Adjusting the default settling time may be important when you are measuring or scanning resistances with values above 10 kΩ, when C >500 pF, and when speed is of the utmost importance. For the input capacitance of the DMM, refer to the specifications document for your device. The cable capacitance can be significantly more than the input capacitance. Cable material dielectric absorption complicates the settling time issue.

When switching to the next measurement, consider the following example. Assume a 10 V step occurs on the 10 V range with a required resolution of 6½ digits. Referring to the previous table for 6½ digit settling, k = 14 is required. Consider next a 10 mV step on the 10 V range. The step, being 0.1% of range (10 mV/10 V = 0.1%), can only be observed to 0.1% beyond that (assuming a 6½ digit resolution). In this example, the maximum time required from the previous table corresponds to k = 7, which yields 0.091%. If the difference between channels is known to never exceed 10 mV, then you can save considerable settling time. If you cannot predict what the values are from channel to channel, consider the accuracy required in the measurement. Then assume a step size equal to the full range to identify k.

The analysis in the previous example is for fixed range operation. You can select Auto Range for the measurement, but additional delays occur as the DMM seeks the appropriate range for the measurement. NI does not recommend Auto Range for optimum speed.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=dmm-settling-time_5.html language=enus -->
## TOPIC 00220: Settling Time

- bundle_id: `ni-dmm`
- source_path: `dmm-settling-time_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dmm-settling-time_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices unde

### Settling Time

Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.

You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices under test (DUTs) through a multiplexing switch:

[IMAGE alt='image' src='GUID-610440AB-7B07-463D-945D-8786F509598C-a5.svg']

Whenever the external switch changes channels, the DMM input is connected to a different voltage or resistance. Each time this process happens, the DMM, interacting with the source, behaves as an RC circuit with a settling time that corresponds to:

ST = kRC

where

R = equivalent resistance of the source

C = the equivalent input capacitance seen by the DMM (C <sub>COM</sub> + C <sub>CX</sub> + C<sub>IN</sub>), where C<sub>CX</sub> = C<sub>C1</sub> or C<sub>C2</sub> or C<sub>C3</sub> (cable capacitances) depending on the channel selected

k = value related to accuracy required, as shown in the following table; increases as required accuracy increases

ST = settling time required

Note

| k | Error | Required Resolution(for full range step) |
| --- | --- | --- |
| 3 | 4.98% | — |
| 4 | 1.83% | — |
| 5 | 0.674% | — |
| 6 | 0.248% | — |
| 7 | 0.091% | — |
| 8 | 0.033% | 3½ digits |
| 9 | 0.012% | — |
| 10 | 0.0045% | 4½ digits |
| 11 | 0.0017% | — |
| 12 | 0.00061% | 5½ digits |
| 13 | 0.00023% | — |
| 14 | 0.000083% | 6½ digits |
| 15 | 0.000031% | — |
| 16 | 0.000011% | 7 digits |
| 17 | 0.000004% | 7½ digits |

Adjusting the default settling time may be important when you are measuring or scanning resistances with values above 10 kΩ, when C >500 pF, and when speed is of the utmost importance. For the input capacitance of the DMM, refer to the specifications document for your device. The cable capacitance can be significantly more than the input capacitance. Cable material dielectric absorption complicates the settling time issue.

When switching to the next measurement, consider the following example. Assume a 10 V step occurs on the 10 V range with a required resolution of 6½ digits. Referring to the previous table for 6½ digit settling, k = 14 is required. Consider next a 10 mV step on the 10 V range. The step, being 0.1% of range (10 mV/10 V = 0.1%), can only be observed to 0.1% beyond that (assuming a 6½ digit resolution). In this example, the maximum time required from the previous table corresponds to k = 7, which yields 0.091%. If the difference between channels is known to never exceed 10 mV, then you can save considerable settling time. If you cannot predict what the values are from channel to channel, consider the accuracy required in the measurement. Then assume a step size equal to the full range to identify k.

The analysis in the previous example is for fixed range operation. You can select Auto Range for the measurement, but additional delays occur as the DMM seeks the appropriate range for the measurement. NI does not recommend Auto Range for optimum speed.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=dmm-settling-time_6.html language=enus -->
## TOPIC 00221: Settling Time

- bundle_id: `ni-dmm`
- source_path: `dmm-settling-time_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dmm-settling-time_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices unde

### Settling Time

Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.

You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices under test (DUTs) through a multiplexing switch:

[IMAGE alt='image' src='GUID-610440AB-7B07-463D-945D-8786F509598C-a5.svg']

Whenever the external switch changes channels, the DMM input is connected to a different voltage or resistance. Each time this process happens, the DMM, interacting with the source, behaves as an RC circuit with a settling time that corresponds to:

ST = kRC

where

R = equivalent resistance of the source

C = the equivalent input capacitance seen by the DMM (C <sub>COM</sub> + C <sub>CX</sub> + C<sub>IN</sub>), where C<sub>CX</sub> = C<sub>C1</sub> or C<sub>C2</sub> or C<sub>C3</sub> (cable capacitances) depending on the channel selected

k = value related to accuracy required, as shown in the following table; increases as required accuracy increases

ST = settling time required

Note

| k | Error | Required Resolution(for full range step) |
| --- | --- | --- |
| 3 | 4.98% | — |
| 4 | 1.83% | — |
| 5 | 0.674% | — |
| 6 | 0.248% | — |
| 7 | 0.091% | — |
| 8 | 0.033% | 3½ digits |
| 9 | 0.012% | — |
| 10 | 0.0045% | 4½ digits |
| 11 | 0.0017% | — |
| 12 | 0.00061% | 5½ digits |
| 13 | 0.00023% | — |
| 14 | 0.000083% | 6½ digits |
| 15 | 0.000031% | — |
| 16 | 0.000011% | 7 digits |
| 17 | 0.000004% | 7½ digits |

Adjusting the default settling time may be important when you are measuring or scanning resistances with values above 10 kΩ, when C >500 pF, and when speed is of the utmost importance. For the input capacitance of the DMM, refer to the specifications document for your device. The cable capacitance can be significantly more than the input capacitance. Cable material dielectric absorption complicates the settling time issue.

When switching to the next measurement, consider the following example. Assume a 10 V step occurs on the 10 V range with a required resolution of 6½ digits. Referring to the previous table for 6½ digit settling, k = 14 is required. Consider next a 10 mV step on the 10 V range. The step, being 0.1% of range (10 mV/10 V = 0.1%), can only be observed to 0.1% beyond that (assuming a 6½ digit resolution). In this example, the maximum time required from the previous table corresponds to k = 7, which yields 0.091%. If the difference between channels is known to never exceed 10 mV, then you can save considerable settling time. If you cannot predict what the values are from channel to channel, consider the accuracy required in the measurement. Then assume a step size equal to the full range to identify k.

The analysis in the previous example is for fixed range operation. You can select Auto Range for the measurement, but additional delays occur as the DMM seeks the appropriate range for the measurement. NI does not recommend Auto Range for optimum speed.

Parent topic:

DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=dmm-settling-time_7.html language=enus -->
## TOPIC 00222: Settling Time

- bundle_id: `ni-dmm`
- source_path: `dmm-settling-time_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/dmm-settling-time_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices unde

### Settling Time

Prior to every measurement phase, a settling time exists. Refer to the DMM Measurement Defaults section for your device for the default settling times for each function of the device.

You can modify these values to be longer or shorter. The following figure shows a DMM connected to three devices under test (DUTs) through a multiplexing switch:

[IMAGE alt='image' src='GUID-610440AB-7B07-463D-945D-8786F509598C-a5.svg']

Whenever the external switch changes channels, the DMM input is connected to a different voltage or resistance. Each time this process happens, the DMM, interacting with the source, behaves as an RC circuit with a settling time that corresponds to:

ST = kRC

where

R = equivalent resistance of the source

C = the equivalent input capacitance seen by the DMM (C <sub>COM</sub> + C <sub>CX</sub> + C<sub>IN</sub>), where C<sub>CX</sub> = C<sub>C1</sub> or C<sub>C2</sub> or C<sub>C3</sub> (cable capacitances) depending on the channel selected

k = value related to accuracy required, as shown in the following table; increases as required accuracy increases

ST = settling time required

Note

| k | Error | Required Resolution(for full range step) |
| --- | --- | --- |
| 3 | 4.98% | — |
| 4 | 1.83% | — |
| 5 | 0.674% | — |
| 6 | 0.248% | — |
| 7 | 0.091% | — |
| 8 | 0.033% | 3½ digits |
| 9 | 0.012% | — |
| 10 | 0.0045% | 4½ digits |
| 11 | 0.0017% | — |
| 12 | 0.00061% | 5½ digits |
| 13 | 0.00023% | — |
| 14 | 0.000083% | 6½ digits |
| 15 | 0.000031% | — |
| 16 | 0.000011% | 7 digits |
| 17 | 0.000004% | 7½ digits |

Adjusting the default settling time may be important when you are measuring or scanning resistances with values above 10 kΩ, when C >500 pF, and when speed is of the utmost importance. For the input capacitance of the DMM, refer to the specifications document for your device. The cable capacitance can be significantly more than the input capacitance. Cable material dielectric absorption complicates the settling time issue.

When switching to the next measurement, consider the following example. Assume a 10 V step occurs on the 10 V range with a required resolution of 6½ digits. Referring to the previous table for 6½ digit settling, k = 14 is required. Consider next a 10 mV step on the 10 V range. The step, being 0.1% of range (10 mV/10 V = 0.1%), can only be observed to 0.1% beyond that (assuming a 6½ digit resolution). In this example, the maximum time required from the previous table corresponds to k = 7, which yields 0.091%. If the difference between channels is known to never exceed 10 mV, then you can save considerable settling time. If you cannot predict what the values are from channel to channel, consider the accuracy required in the measurement. Then assume a step size equal to the full range to identify k.

The analysis in the previous example is for fixed range operation. You can select Auto Range for the measurement, but additional delays occur as the DMM seeks the appropriate range for the measurement. NI does not recommend Auto Range for optimum speed.

Parent topic:

NI 4065 DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=effective-common-mode-rejection-ratio-ecmrr.html language=enus -->
## TOPIC 00223: Effective Common-Mode Rejection Ratio (ECMRR)

- bundle_id: `ni-dmm`
- source_path: `effective-common-mode-rejection-ratio-ecmrr.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/effective-common-mode-rejection-ratio-ecmrr.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Effective common-mode rejection ratio (ECMRR) is the sum of CMRR and NMRR at a given frequency and is only valid for DC measurements. It is the effective rejection on a given noise signal that is applied to both input leads because it is rejected first by the CMRR capability of the instrument and th

### Effective Common-Mode Rejection Ratio (ECMRR)

Effective common-mode rejection ratio (ECMRR) is the sum of CMRR and NMRR at a given frequency and is only valid for DC measurements. It is the effective rejection on a given noise signal that is applied to both input leads because it is rejected first by the CMRR capability of the instrument and then again by its NMRR capability. This specification is useful at powerline frequencies, particularly for laboratory and manufacturing floor environments. An equivalent equation to represent ECMRR is as follows:

ECMRR = 20*log<sub>10</sub>(V<sub>CM</sub>/V<sub>error</sub>)

where V<sub>error</sub> is the value returned by the DMM in response to an applied common mode voltage V<sub>CM</sub>.

For example, if you are measuring 1 mVDC with a DMM that specifies an ECMRR of 130 dB at 60 Hz, and you have a common-mode interference (noise) of 100 mVrms, then the resulting measurement error is:

Measurement Error = 10<sup>(-130/20)</sup> X 100 mV = 316 nV

which is 0.03% of your measured signal instead of the 10,000% error that the 100 mV interference would otherwise imply.

Parent topic:

Measurement Considerations

<!--NI_TOPIC bundle=ni-dmm path=environment.html language=enus -->
## TOPIC 00224: Environment

- bundle_id: `ni-dmm`
- source_path: `environment.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/environment.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI DMMs use precision components whose performance can be adversely affected by operation outside the specified limits. For best performance:Ensure that the ambient temperature is between 0 ºC and 55 ºC (NI PXI-4065, NI PXI-4070/4071/4072, and NI PXIe-4080/4081/4082), 0 °C and 45 °C (NI USB-4065), o

### Environment

NI DMMs use precision components whose performance can be adversely affected by operation outside
 the specified limits.

For best performance:

- Ensure that the ambient temperature is between 0 ºC and 55 ºC (NI PXI-4065, NI PXI-4070/4071/4072, and NI PXIe-4080/4081/4082), 0 °C and 45 °C (NI USB-4065), or 0 °C and 40 °C (NI PCI/PCIe-4065 and NI PCI-4070).
- Follow standard metrology practices as you would for any ppm-level measurements.
- Use a chassis that has a well-designed cooling system, allowing the DMM to stay cool. All NI PXI chassis meet this requirement.

Operating the NI 4070/4071/4072 outside the specified operating temperatures can increase bias currents in the electronic components, increase noise, accelerate drifts, and decrease product life. Beyond the maximum specified operating temperatures, the DMM's circuits perform differently than during the factory calibration, resulting in additional measurement errors which may not be accounted for by the Tempco specifications.

Note

Operating under high humidity (>80%, >35 ºC) or dusty conditions can cause leakages between circuit components to increase and result in additional measurement errors, especially in resistance measurements above 100 kΩ.

NI used a highly accelerated life test (HALT) to verify the operation of the NI 4070/4071/4072 during severe environmental and operational stresses beyond normal shipping, storage, and operational levels.

You can operate the NI 4070/4071/4072 at temperatures below 0 ºC (down to -10 ºC) for short periods of time. The NI PXI-4070/4071/4072 operates at about 10 ºC higher than the incoming air in the PXI module. Operation above 55 ºC could induce gain errors due to the precision reference temperature control dropping out of equilibrium. You can measure the temperature of the DMM using the onboard temperature sensor.

NI designed the NI 4070/4071/4072 with robust built-in precision voltage and resistance standards. These standards and the self-calibration function improve the performance of the NI 4070/4071/4072 at the extremes, even beyond the capability of most other DMMs. Regardless, you should always ensure appropriate environmental requirements are met.

Parent topic:

Integration and System Considerations

Related concepts:

- Chassis
- USB System Considerations
- Self-Calibration

<!--NI_TOPIC bundle=ni-dmm path=examples.html language=enus -->
## TOPIC 00225: Examples

- bundle_id: `ni-dmm`
- source_path: `examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/examples.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: For NI-DMM example locations, refer to the NI-DMM Readme. The following examples are instructional tools that demonstrate some of the functionality of the DMMs that you can use or integrate into your systems. These examples are available for the following ADEs: NI LabVIEW 8.2.1 or later LabWindows/C

### Examples

For NI-DMM example locations, refer to the NI-DMM Readme.

The following examples are instructional tools that demonstrate some of the functionality of the DMMs that you can use or integrate into your systems. These examples are available for the following ADEs:

- NI LabVIEW 8.2.1 or later
- LabWindows/CVI 7.1.1 or later
- Visual C/C++ 6.0 or later
- Visual Basic 6.0 or later

For examples of using NI DMMs with NI switch modules, refer to the NI Developer Zone Web site.

Note

#### Single Measurements

These examples demonstrate how to take a specific type of measurement using the DMM. The default values for range and resolution are customized to the type of measurement. The following function calls are included in each example: niDMM Initialize, niDMM Config Measurement, niDMM Read, niDMM Close. Certain examples include additional function calls. For example, DC measurements sets the Powerline Frequency. AC measurements sets the AC Bandwidth.

Measure DC Voltage

This example acquires a single DC Voltage measurement. Specify the range and absolute resolution of the input signal and the powerline frequency of your system. The measured value displays in the Measurement indicator. A Boolean control indicates if the measured value is out of range.

Measure AC Voltage

This example acquires a single AC Voltage measurement. Specify the range, absolute resolution, and bandwidth of the input signal. The measured value displays in the Measurement indicator. A Boolean control indicates if the measured value is out of range.

Measure DC Current

This example acquires a single DC Current measurement. Specify the range and absolute resolution of the input signal and the powerline frequency of your system. The measured value displays in the Measurement indicator. A Boolean control indicates if the measured value is out of range.

Measure AC Current

This example acquires a single AC Current measurement. Specify the range, absolute resolution, and bandwidth of the input signal. The measured value displays in the Measurement indicator. A Boolean control indicates if the measured value is out of range.

Measure Resistance (2- or 4-wire)

This example acquires a single resistance measurement. Set the measurement type to either a 2-wire or 4-wire resistance measurement. Specify the range and absolute resolution of the input signal and the powerline frequency of your system. The measured value displays in the Measurement indicator. A Boolean control indicates if the measured value is out of range.

Measure Frequency (NI 4065 is not supported.)

This example acquires a single frequency or period measurement. Specify the minimum expected measurement (in Hz or seconds) and the maximum amplitude of the input signal. The measured value displays in the Measurement indicator. A Boolean control indicates if the measured value is out of range.

Diode Test

This example acquires a single diode measurement. Specify the range and absolute resolution of the input signal and the powerline frequency of your system. The current source is configurable for NI 4065 and NI 4070/4071/4072 devices. The measured value displays in the Measurement indicator. A Boolean control indicates if the measured value is out of range.

DMM Measurement

This example acquires a single measurement from an NI digital multimeter. Select the measurement function and range. Specify the resolution in digits of precision. The measured value displays in the Measurement indicator. A Boolean control indicates if the measured value is out of range.

Measure Capacitance (NI 4072 only)

This example acquires a single capacitance measurement. Specify the range of the input signal and the number of measurements to average. The measured value is displayed in the Measurement indicator. A Boolean indicator shows whether the measured value is out of range.

Measure Inductance (NI 4072 only)

This example acquires a single inductance measurement. Specify the range of the input signal and the number of measurements to average. The measured value is displayed in the Measurement indicator. A Boolean indicator shows whether the measured value is out of range.

#### Multi Point Measurements

These examples demonstrate how to use the niDMM Configure Multi Point. Only Immediate triggers are used.

Acq&Graph Multiple Samples

This example acquires multiple measurements. Select the measurement function, range, and absolute resolution. Specify the number of samples to acquire. niDMM Read is used to acquire the requested number of points. The data displays in a waveform graph.

Cont Acq&Chart Multiple Samples

This example performs a continuous acquisition. Select the measurement function, range, and absolute resolution. niDMM Initiate starts the acquisition. The requested samples are returned using niDMM Fetch Multi Point within the loop. The data displays in a waveform chart. The acquisition aborts when you click 
 Stop.

#### Triggered Acquisitions

These examples demonstrate the use of triggers during measurement acquisitions.

Acq One Sample-Ext Trig

This example acquires a single measurement when an external trigger is detected.
 Select the measurement function, range and absolute resolution. Specify the trigger
 source and a delay that elapses between the trigger and the measurement. The
 measured value displays in the Measurement indicator. A Boolean control indicates if
 the measured value is out of range.

Acq Multiple Samples-Ext Trig

This example acquires a finite number of measurements. The acquisition is initiated
 when a trigger is detected at the specified trigger source. All the points are
 acquired without a trigger. Select the measurement function, range, absolute
 resolution and power line frequency. Specify the trigger source and the number of
 samples to acquire. Read Multi Point is used to fetch the requested number of
 samples.

Acq Multiple Samples-Ext Sample Trig

This example acquires a finite number of measurements. The first measurement is
 acquired without a trigger, all remaining measurements are acquired when a trigger
 is detected at the Sample trigger source. Select the measurement function, range,
 absolute resolution and powerline frequency. Specify the sample trigger source and
 the number of samples to acquire. Read Multi Point is used to fetch the requested
 number of samples.

Cont Acq Multiple Samples-Ext Trig-Ext Sample Trig

This example acquires multiple measurements continuously. Every measurement is
 acquired when a trigger is detected at the Source according to the edge specified.
 Select the measurement function, range, absolute resolution and power line
 frequency. Specify the trigger/sample trigger source and the number of samples to
 acquire at a time. niDMM Read Multi Point is used to fetch the number of points
 available or the number of points requested (whichever is larger).

Cont Acq Multiple Samples-SW Sample Trig

This example performs a continuous acquisition. Each sample is triggered with a
 Software Trigger. Set the function, range, and resolution. Each time the Send
 Software Trigger function is called, Fetch retrieves the measurement and displays it
 in a waveform graph. The acquisition aborts when you click
 Stop.

Acq Multiple Samples-Interval Sample Trig

This example acquires multiple measurements continuously. The first measurement is
 acquired without a trigger. Each measurement thereafter is acquired when Send
 software trigger function is called. Select the measurement function, range,
 absolute resolution and power line frequency.

Note

#### Advanced Examples

These examples demonstrate some advanced features of the NI 4080/4081/4082 and
 NI 4070/4071/4072.

Improve Stability with Auto Zero (LV, CVI only)

Auto
 Zero improves the stability of a measurement by removing internal DMM
 offsets.This example acquires a DC voltage or resistance measurement and returns the
 measured value to the user.

After specifying the instrument descriptor, select the function, range, and
 resolution. Enable and disable Auto Zero and observe the difference in the
 measurement.

Eliminate V offsets with OCO (LV, CVI only)

Offset
 Compensated Ohms allows you to measure resistances in the presence of
 offset voltages. Offset Compensated Ohms is useful for resistance measurements of 10
 kΩ or less. This example acquires a 2-wire or 4-wire resistance measurement. After
 specifying the instrument descriptor, select the function, range, and resolution.
 Turning on Offset Compensated Ohms enables this feature.

Improve DC Resolution (LV, CVI only)

To remove low frequency noise from a measurement, set the aperture time to 1/
 f, where f is the noise frequency.
 Averaging multiple measurements together can further improve the resolution. This
 example acquires multiple DC voltage measurements. After specifying the instrument
 descriptor, select the function and range.

Input a stable, known voltage or short the input terminals (HI, LO). Specify 100 ms
 for the aperture time and set the number of averages to 8. Note the resolution
 available. Change the number of averages to 1 and observe the decrease in
 resolution.

Note

Improve DC Noise Rejection (LV, CVI only)

By varying
 the weighting of the samples that compose a single measurement, input noise can be
 attenuated. The DC Noise Rejection property controls the sample weighting. The signal
 frequencies removed from the measurement are related to the aperture time selected.

This example acquires DC voltage measurements. The top graph in the VI displays the
 measurements. The second graph in the VI displays a plot of the theoretical noise
 rejection versus the frequency of the input signal.

1. Connect the supplied test leads to the input and drape the leads near a power
 cord.
2. After specifying the instrument descriptor, select the 100 mV range.
3. Select an aperture time of 10 ms.
4. Set DC Noise Rejection (DCNR) to Normal.
5. Note the displayed noise.
6. Repeat with an aperture time of 16.67 ms (for 60 Hz powerline) or 20 ms (for 50
 Hz powerline).
7. Select a 100 ms aperture time and High Order DCNR.
8. Note the difference in displayed noise.

LC Cable Comp Load and Measure (NI 4072 only)

Cable compensation improves the accuracy of a capacitance or inductance measurement
 by removing the parasitic capacitance (open compensation) and parasitic inductance
 (short compensation) from the system. This example shows how to load compensation
 values from a file and pick the correct compensation value based on the current
 source frequency of the configured measurement.

LC Cable Comp Measure and Save (NI 4072 only)

Cable compensation improves the accuracy of a capacitance or inductance measurement
 by removing the parasitic capacitance (open compensation) and parasitic inductance
 (short compensation) from the system. This example shows how to take compensation
 values for all possible current source frequencies and store them for later use and
 how to pick the correct compensation value based on the current source frequency of
 the configured measurement.

LC Cable Compensation (NI 4072 only)

Cable compensation improves the accuracy of a capacitance or inductance measurement
 by removing the parasitic capacitance (open compensation) and parasitic inductance
 (short compensation) from the system. This example shows how to load or save
 compensation values from or to a file and pick the correct compensation value based
 on the current source frequency of the configured measurement.

#### Self-Calibration

This example demonstrates how to perform a self-calibration and retrieve the calibration information from the NI 4070/4071/4072. Refer to the documentation for the recommended self-calibration interval. In this example the self-calibration operation is timed to show the speed at which this operation can be performed. The calibration information stores both the date and the temperature at which the DMM was last calibrated. This information can be used along with the current temperature of the device (which is often different than the ambient temperature of the system) to determine if a self-calibration should be performed. This example times the self-calibration and displays the results. niDMM Self Cal takes approximately 60 seconds.

#### Waveform Acquisitions

These examples demonstrate the NI-DMM waveform acquisitions functions that enable you to use the NI 4070/4071/4072 as a high-voltage isolated digitizer.

Read & Graph Waveform (LV, CVI only)

This example acquires a waveform. Select the waveform acquisition function, range, sample rate, and number of points in the waveform. niDMM Read Waveform is used to acquire the requested waveform. The data is displayed in a waveform graph.

Fetch & Graph Waveform (LV, CVI only)

This example performs a waveform acquisition that employs several iterations of niDMM Fetch Waveform. Select the waveform acquisition function, range, sample rate, total number of points in the acquisition, and the number of samples to fetch at a time. The requested samples are returned using niDMM Fetch Waveform within the loop. The data retrieved in each iteration of the loop is displayed in a waveform graph. The acquisition is aborted when you press the 
 Stop button.

Triggered Waveform (LV, CVI only)

This example performs a waveform acquisition that is started by a trigger. Select the waveform acquisition function, range, sample rate and number of points in the waveform. The requested samples are returned using niDMM Fetch Waveform. The data is displayed in a waveform graph.

Waveform Demo (LV only)

This demo acquires and displays the input waveform. Enter the Instrument Descriptor and click the 
 Run button. While running, you can adjust the volts per division, and the timebase.

You can use Simulate Flag to use NI-DMM to simulate the NI 4070/4071/4072 waveform acquisition mode.

The timebase setting determines the acquisition rate of the instrument. The Acquisition rate indicator changes as you change the Timebase setting.

The subroutine of the example analyzes the acquired data to locate the first positive zero crossing of the signal. If the routine finds the zero crossing, the example displays the waveform for (10)*(Timebase seconds). If the analysis does not detect any positive zero crossings, the graph displays data from the start of the acquisition buffer.

This example and its block diagram source are available in the 
 Waveform Acquisition folder of NI-DMM examples.

#### Performance Examples

These examples demonstrate the DC Reading Rates Specifications for the NI 4070/4071/4072.

Achieving 7 Digits of Resolution (LV, CVI only)

This example demonstrates how to achieve 7 digits of resolution by averaging multiple samples together. Connect a short between the HI and LO terminals of the NI 4070/4071/4072. Specify the input descriptor of the device. Run the example. DC Voltage measurements are acquired on the selected range. The measured values are displayed in a graph. The Effective Digits of Resolution is calculated from the last 100 measurements and displayed in an indicator. The reading rate is also displayed. Click 
 STOP to end the acquisition. You can change the aperture time, number of averages, and ADC Calibration settings. Run the VI to view the resulting Effective Digits of Resolution and Readings per Second for the specified configuration. Auto Zero must be set to 
 ON when the number of averages is greater than 1.

Max DC Reading Rate at 7.5 Digits

This example demonstrates how to achieve the higher reading rate at 7½ digits of resolution with an NI 4071. Connect a short between the HI and LO terminals of the NI 4071. Specify the input descriptor of the device. Run the example. DC Voltage measurements are acquired on the selected range. The measured values are displayed on the front panel chart. The reading rate is displayed in an indicator. Click 
 STOP to end the acquisition.

To achieve the higher reading rate of 7½–digit resolution, the example configures the NI 4071 for 7½–digit measurements, turns off ADC Calibration, and directly configures Auto Zero to 
 ON, the Number of Averages to 4, and Aperture Time to 1 power-line cycle (PLC).

Maximizing DC Reading Rates (LV, CVI only)

This example demonstrates how to maximize DC reading rates for the NI 4070/4071/4072 by specifying the aperture time. Generally the DMM selects an aperture time to achieve a specified resolution, but in this example, you directly set the aperture time. The acquired measurements are then used to calculate the noise-free digits of resolution.

Most traditional DMMs specify digits of resolution based on noise "counts" on a fixed display that defines the performance of the ADC. A more conservative approach is to calculate the effective resolution based on noise-free digits. You can use the example's calculation as a guide, in addition to the actual measured values, to determine the appropriate aperture time for a given measurement setup and conditions.

1. Connect a short or very stable input signal between the HI and LO terminals of the NI 4070/4071/4072.
2. Specify the instrument descriptor of the device.
3. Choose the desired function and range.
4. Use the Recommended Aperture Time Settings table to select an aperture time.
5. Run the example.
6. Click 
 STOP to end the acquisition.

The measured value and reading rate are displayed in two indicators. The value for noise-free digits is based on the last 100 measurements and displayed in an indicator.

Use this example to find the speed-noise tradeoff that works best for your application. On the 10 V range with a shorted input, a 3.33 ms aperture time yields approximately 6½ digits of resolution at around 290 readings/s. Increasing the aperture time to 10 ms results in approximately 6.7 digits of resolution at around 100 readings/s.

By changing the aperture time to 100 ms, the resolution approaches 6.8 digits. This is the specified performance capability of the DMM before adding in other sources of noise (specified front-end noise on the most sensitive range, environmental noise, or noise from the device under test).

Try making resistance measurements with a 1 MΩ resistor and a 10 ms aperture time, but connect the resistor with the standard unshielded test leads included with the NI 4070/4071/4072. Powerline frequency noise in the environment most likely will interfere with this high impedance test setup. Because 10 ms is not a multiple of a line cycle (50 or 60 Hz), the DMM does not reject this environmental noise. This is evidenced by the value in the Noise-Free Resolution indicator. Changing the aperture time to 16.66 ms (20 ms for 50 Hz line frequency outside the US) significantly improves the effective noise-free resolution. A 100 ms aperture time yields even better results.

Parent topic:

Programming with NI-DMM

Related concepts:

- Auto Zero
- Offset Compensated Ohms
- Aperture Time
- DC Noise Rejection

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=extended-support-changes.html language=enus -->
## TOPIC 00226: Updates and Changes for NI-DMM Extended Support Versions

- bundle_id: `ni-dmm`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/extended-support-changes.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in NI-DMM versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible changes,

### Updates and Changes for NI-DMM Extended Support Versions

Browse updates and changes made in NI-DMM versions
 on extended support.

Note

Release Notes

#### NI-DMM 21.3 New
 Features and Changes

- The NI-DMM Soft Front Panel has been replaced by InstrumentStudio,
 which is automatically installed when you install the NI-DMM driver. You can access InstrumentStudio in one
 of the following ways: The deprecated NI-DMM Soft Front Panel remains available for
 download. Visit Download and Install Legacy NI-DMM Soft Front
 Panels for more information.
  - From the Windows start menu, select National Instruments»InstrumentStudio year . This launches InstrumentStudio and runs a soft front
 panel populated with devices detected on your system.
  - From Measurement & Automation Explorer (MAX) , select a device and then click
 Test Panels... . This launches
 InstrumentStudio and runs a soft front panel for the device you
 selected.
- The NI-DMM Waveform Demo application is no longer
 included with NI-DMM . It remains available for
 download as a LabVIEW example.

Related concepts:

- NI-DMM Examples

Related information:

- Download Legacy Soft Front Panel for NI-DMM

#### NI-DMM 20.0 New
 Features and Changes

NI-DMM 20.0 adds support for LabVIEW 2020 and LabVIEW NXG
 5.0.

#### NI-DMM 19.5 New
 Features and Changes

NI-DMM 19.5 adds support for LabVIEW NXG 4.0.

#### NI-DMM 19.1 New
 Features and Changes

- NI-DMM 19.1 drops support for Traditional DAQ (NI-DAQ)
 and the PCI/PXI-4060 and DAQCard-4050 (PCMCIA-4050) digital multimeters.
- NI-DMM 19.1 drops support for Express VIs in LabVIEW.
 Existing code created with earlier versions of NI-DMM and that contains Express
 VIs will continue to execute, but the Express VI cannot be reconfigured from a
 dialog box. To reconfigure an Express VI, right-click the Express VI and
 select Open Front Pane»Convert. This will convert the Express VI to code that you can
 configure on the block diagram. NI recommends converting Express VIs to code
 before using the Code Conversion Utility in LabVIEW NXG to convert code for
 LabVIEW NXG.

#### NI-DMM 19.0 New
 Features and Changes

NI-DMM 19.0 adds support for LabVIEW 2019 and LabVIEW NXG
 3.1.

#### NI-DMM 18.5 New
 Features and Changes

NI-DMM 18.5 adds support for LabVIEW NXG 3.0.

#### NI-DMM 18.1 New
 Features and Changes

- NI-DMM 18.1 adds support for InstrumentStudio.
- NI-DMM 18.1 adds support for importing and exporting
 configurations between NI-DMM sessions.

#### NI-DMM 18.0 New
 Features and Changes

- NI-DMM 18.0 adds support for LabVIEW 2018 and LabVIEW
 NXG 2.1.
- NI-DMM 18.0 adds support for .NET Framework 4.0 and
 .NET Framework 4.5.

#### NI-DMM 17.5 New
 Features and Changes

NI-DMM 17.5 adds support for LabVIEW NXG 2.0.

#### NI-DMM 17.0 New
 Features and Changes

- NI-DMM 17.0 adds support for LabVIEW 2017 (32- and
 64-bit).
- NI-DMM 17.0 adds support for LabVIEW NXG 1.0.

#### NI-DMM 16.0 New
 Features and Changes

NI-DMM 16.0 adds support for LabVIEW 2016 (32- and
 64-bit).

#### NI-DMM 15.2 New
 Features and Changes

NI-DMM 15.2 adds support for the NI PXIe-4080, NI
 PXIe-4081, and NI PXIe-4082.

#### NI-DMM 15.1 New
 Features and Changes

- NI-DMM 15.1 adds support for LabVIEW 2015 (32- and
 64-bit).
- NI-DMM 15.1 adds support for debugging an NI-DMM device while in use by another application, by
 monitoring or controlling the device in the NI-DMM Soft Front Panel . Note NI-DMM 15.1 Soft Front Panel no
 longer supports IVI device simulation.

#### NI-DMM 14.0 New
 Features and Changes

NI-DMM 14.0 adds support for LabVIEW 2014 (32- and
 64-bit).

#### NI-DMM 3.1 New
 Features and Changes

NI-DMM 14.0 adds support for LabVIEW 2013 (32- and
 64-bit).

#### NI-DMM 3.0.6 New
 Features and Changes

NI-DMM 3.0.6 adds support for LabVIEW 2012 (32- and
 64-bit).

#### NI-DMM 3.0.5 New
 Features and Changes

NI-DMM 3.0.5 adds support for LabVIEW 2011 (32- and
 64-bit).

#### NI-DMM 3.0.4 New
 Features and Changes

- NI-DMM 3.0.4 adds a fix related to code not generating
 in the Japanese versions of LabVIEW when the NI-DMM/Switch Express VI was used
 with switch devices (ID 276993).
- NI-DMM 3.0.4 adds a fix related to a loading issue
 with the NI-DMM/Switch Express VI in LabVIEW 2010 (64-bit) (ID 246480).

#### NI-DMM 3.0.3 New
 Features and Changes

- NI-DMM 3.0.3 adds support for LabVIEW 2010 (32- and
 64-bit).
- NI-DMM 3.0.3 adds a fix related to a custom installer
 built on a 32-bit OS using LabVIEW, LabWindows™/CVI™, or NI TestStand does not
 deploy NI-DMM or its dependent user applications on a 64-bit OS (ID
 228650).

#### NI-DMM 3.0.2 New
 Features and Changes

- NI-DMM 3.0.2 updates the external calibration
 procedure to accommodate a hardware change on newer NI 407x devices. NI-DMM 3.0.2 or later is required for external
 calibration beginning with NI PCI-4070 revision 189380G-01, NI PXI-4070 revision
 191485G-01, NI PXI-4071 revision 191485J-02, and NI PXI-4072 revision
 191485F-03.
- NI-DMM 3.0.2 fixes an issue with NI 407x devices that
 caused an internal hardware error when taking measurements with autorange (ID
 196451).

#### NI-DMM 3.0.1 New
 Features and Changes

NI-DMM 3.0.1 adds a fix related to offsets in AC current
 measurements for 407x devices (ID 135829).

#### NI-DMM 3.0 New
 Features and Changes

- NI-DMM 3.0.3 adds the
 niDMM_GetErrorMessage function.
- NI-DMM 3.0.3 adds support for LabVIEW 2009 (32-bit)
 and LabVIEW 2009 (64-bit).
- NI-DMM 3.0.3 adds support for temperature measurements
 in the NI-DMM/Switch Express VI.
- NI-DMM 3.0.3 adds support for temperature measurements
 in the NI-DMM Soft Front Panel .
- NI-DMM 3.0.3 adds support for 64-bit user mode.
- NI-DMM 3.0.3 adds support for C examples rewritten in
 ANSI C and makefile for 64-bit user mode.

#### NI-DMM 2.9 New
 Features and Changes

- NI-DMM 2.9 adds support for LabVIEW 8.6.
- NI-DMM 2.9 adds support for temperature measurements.
- NI-DMM 2.9 adds Japanese localization for driver, LabVIEW API, and
 documentation.
- Error and self test message strings return localized values in LabVIEW. User
 applications that check the value of these strings (or trap errors by
 comparing the error cluster) may experience a change in behavior.
- Simulation now has increased realism. Timing and error reporting are more representative
 of an actual device.
- Reset Device button in MAX has improved functionality. If you have
 selected an NI 4065/407x in the Devices and
 Interfaces configuration tree, the Reset
 Device button aborts any ongoing acquisitions before
 resetting the device to factory default.
- If you have selected an NI 4065/407x in MAX, the Test
 Panels button in MAX will launch the NI-DMM Soft Front Panel .
- Temperature has been added to function.ctl . If this type def
 is being used in the prototype for a TestStand step, the step prototype will
 need to be reloaded before the sequence can be executed.

<!--NI_TOPIC bundle=ni-dmm path=features.html language=enus -->
## TOPIC 00227: Features

- bundle_id: `ni-dmm`
- source_path: `features.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/features.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic explains how to program additional features of the DMMs. The following table is a quick overview of the additional features supported by NI digital multimeters. Click the feature for programming instructions. Features NI 4080/4081/4082 NI 4065 NI 4070/4071/4072 Performing Self-Calibration

### Features

This topic explains how to program additional features of the DMMs. The following table is a quick overview of the additional features supported by NI digital multimeters. Click the feature for programming instructions.

| Features | NI 4080/4081/4082 | NI 4065 | NI 4070/4071/4072 |
| --- | --- | --- | --- |
| Performing Self-Calibration | √ | — | √ |
| Configuring Auto Zero | √ | √ | √ |
| Configuring Auto Range | √ | √ | √ |
| Configuring Offset Compensated Ohms | √ | — | √ |
| Configuring Input Resistance | √ | √ | √ |
| Configuring ADC Calibration | √ | — | √ |
| Configuring Measurement Timing | √ | √ | √ |
| Selecting DC Noise Rejection | √ | √ | √ |
| Acquiring Waveforms | √ | — | √ |
| Configure Waveform Coupling | √ | — | √ |
| Configuring Frequency Measurements | √ | — | √ |
| Configuring Period Measurements | √ | — | √ |
| Single Point Acquisitions | √ | √ | √ |
| Multiple Point Acquisitions | √ | √ | √ |
| Generating Measurement Complete | √ | √ | √ |
| Scanning Switch Modules | √ | √ | √ |
| Simulating NI Digital Multimeters | √ | √ | √ |
| LabVIEW Trigger Routing | √ | √ | √ |
| LabWindows/CVI Trigger Routing | √ | √ | √ |

Parent topic:

Programming with NI-DMM

<!--NI_TOPIC bundle=ni-dmm path=frequency-response.html language=enus -->
## TOPIC 00228: Frequency Response

- bundle_id: `ni-dmm`
- source_path: `frequency-response.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/frequency-response.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a meas

### Frequency Response

The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a measurement of a source with a high impedance can yield lower-than-expected readings because of interaction with the input capacitance of the device. The device accurately measures the level of the signal at its input, but the signal can be smaller than expected because of the loading effect of the capacitance. In such cases, it is advisable to either allow for the error or buffer the signal being measured.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=frequency-response_2.html language=enus -->
## TOPIC 00229: Frequency Response

- bundle_id: `ni-dmm`
- source_path: `frequency-response_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/frequency-response_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a meas

### Frequency Response

The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a measurement of a source with a high impedance can yield lower-than-expected readings because of interaction with the input capacitance of the device. The device accurately measures the level of the signal at its input, but the signal can be smaller than expected because of the loading effect of the capacitance. In such cases, it is advisable to either allow for the error or buffer the signal being measured.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=frequency-response_3.html language=enus -->
## TOPIC 00230: Frequency Response

- bundle_id: `ni-dmm`
- source_path: `frequency-response_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/frequency-response_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a meas

### Frequency Response

The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a measurement of a source with a high impedance can yield lower-than-expected readings because of interaction with the input capacitance of the device. The device accurately measures the level of the signal at its input, but the signal can be smaller than expected because of the loading effect of the capacitance. In such cases, it is advisable to either allow for the error or buffer the signal being measured.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=frequency-response_4.html language=enus -->
## TOPIC 00231: Frequency Response

- bundle_id: `ni-dmm`
- source_path: `frequency-response_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/frequency-response_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a meas

### Frequency Response

The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a measurement of a source with a high impedance can yield lower-than-expected readings because of interaction with the input capacitance of the device. The device accurately measures the level of the signal at its input, but the signal can be smaller than expected because of the loading effect of the capacitance. In such cases, it is advisable to either allow for the error or buffer the signal being measured.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=frequency-response_5.html language=enus -->
## TOPIC 00232: Frequency Response

- bundle_id: `ni-dmm`
- source_path: `frequency-response_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/frequency-response_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a meas

### Frequency Response

The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a measurement of a source with a high impedance can yield lower-than-expected readings because of interaction with the input capacitance of the device. The device accurately measures the level of the signal at its input, but the signal can be smaller than expected because of the loading effect of the capacitance. In such cases, it is advisable to either allow for the error or buffer the signal being measured.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=frequency-response_6.html language=enus -->
## TOPIC 00233: Frequency Response

- bundle_id: `ni-dmm`
- source_path: `frequency-response_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/frequency-response_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a meas

### Frequency Response

The DMM uses a digital filter to ensure AC accuracy for all frequencies up to the specified limits. This filter is factory-calibrated for every AC voltage and range. However, if care is not taken, it is still possible to get frequency-dependent measurement errors with the device. For example, a measurement of a source with a high impedance can yield lower-than-expected readings because of interaction with the input capacitance of the device. The device accurately measures the level of the signal at its input, but the signal can be smaller than expected because of the loading effect of the capacitance. In such cases, it is advisable to either allow for the error or buffer the signal being measured.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=generating-a-measurement-complete-event.html language=enus -->
## TOPIC 00234: Generating a Measurement Complete Event

- bundle_id: `ni-dmm`
- source_path: `generating-a-measurement-complete-event.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/generating-a-measurement-complete-event.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can generate an event after taking a measurement. You can use this feature if you want to trigger a switch module to advance to the next entry in its scan list. The generated event is called Measurement Complete, and it can be routed to destinations including PXI trigger lines (PXI_Trign) an

### Generating a Measurement Complete Event

The DMM can generate an event after taking a measurement. You can use this feature if you want to trigger a switch module to advance to the next entry in its scan list. The generated event is called Measurement Complete, and it can be routed to destinations including PXI trigger lines (PXI_Trign) and the external 9-pin AUX connector. You can configure the destination of the event using niDMM Configure Meas Complete Dest. Refer to niDMM Configure Meas Complete Dest for all of the destination options for Measurement Complete.

For waveform acquisitions, the Measurement Complete signal is generated after the entire waveform is acquired, not after each point.

You can configure the polarity of the Measurement Complete signal using niDMM Configure Meas Complete Slope. Set Slope to Positive or Rising Edge to generate an Measurement Complete signal that pulses high. Set Slope to Negative or Falling Edge to generate an Measurement Complete signal that pulses low.

Parent topic:

Triggering

Related concepts:

- Scanning
- Scanning Switch Modules
- LabWindows/CVI Trigger Routing
- LabVIEW Trigger Routing

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=getting-started.html language=enus -->
## TOPIC 00235: Getting Started

- bundle_id: `ni-dmm`
- source_path: `getting-started.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/getting-started.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To get started using your NI-DMM device and driver software, refer to the getting started guide for your device. The getting started guide explains how to complete the following tasks: Install the software and hardware Configure the hardware in MAX Program the hardware Connect signals to the DMM for

### Getting Started

To get started using your NI-DMM device and driver software, refer to the getting started guide for your device. The getting started guide explains how to complete the following tasks:

- Install the software and hardware
- Configure the hardware in MAX
- Program the hardware
- Connect signals to the DMM for measurements
- Troubleshoot

The getting started guide for your device is printed in your hardware kit, installed with the
 driver software, and available at ni.com/docs.

Tip

<!--NI_TOPIC bundle=ni-dmm path=handling-high-dc-voltages.html language=enus -->
## TOPIC 00236: Handling High DC Voltages

- bundle_id: `ni-dmm`
- source_path: `handling-high-dc-voltages.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/handling-high-dc-voltages.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: All cables, connectors, and fixtures used in your system must have specifications to handle, with an adequate safety margin, 1000 V signals for the NI 4081 and NI 4071 and 300 V signals for the NI 4080/4082, NI 4070/4072, and NI 4065. The DMM inputs can measure sub-µV level signals with low drift,

### Handling High DC Voltages

Caution

The DMM inputs can measure sub-µV level signals with low drift, handle 300 VDC or 300 V<sub>rms</sub>(NI 4080/4082, NI 4070/4072) or 1000 VDC or 1000 V<sub>pk</sub> (NI 4081 and NI 4071) and peak VAC signals, and recover very quickly for sub-µV level measurements in a system with switching.

However, in switching systems where you are applying high voltages to a low range (e.g., 1000 V on the 10 V range), the switch receives a short-duration current transient. The current transient does not cause any degradation effect on the DMM. However, if the system switches an extreme overload to the DMM input mode with a moderate (tens of Hz) to high scanning rate over extended periods (weeks continuous or cumulative), the current transient can degrade the relay life in the switching system. For optimum switching system reliability when switching high voltages into any DMM, NI recommends selecting the range corresponding to the highest voltage expected.

Ensure that you do not exceed the voltage-hertz limit of the device. Exceeding the voltage-hertz limit is more likely to occur when measuring high-voltage/high-frequency signals. This behavior affects the internal transfer of data in the device and generates an error prompting you to reset the device and reconfigure the measurement.

Refer to the Switching Voltages section for recommendations on switching high voltages or signals with high common-mode voltage levels.

Tip

- niDMM Read (niDMM_Read)
- niDMM Read Multipoint (niDMM_ReadMultipoint)
- niDMM Fetch (niDMM_Fetch)
- niDMM Fetch Multipoint (niDMM_FetchMultipoint)

Your application can handle this error by calling the following VIs or
 functions:

1. niDMM Reset (niDMM_reset)
2. Any configuration VI or function to reconfigure the instrument to the
 required settings
3. niDMM Initiate (niDMM_Initiate), niDMM Read (niDMM_Read), or niDMM Read
 Multipoint (niDMM_ReadMultipoint) to restart the measurement

Parent topic:

DC Voltage

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=handling-high-dc-voltages_2.html language=enus -->
## TOPIC 00237: Handling High DC Voltages

- bundle_id: `ni-dmm`
- source_path: `handling-high-dc-voltages_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/handling-high-dc-voltages_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: All cables, connectors, and fixtures used in your system must have specifications to handle, with an adequate safety margin, 1000 V signals for the NI 4081 and NI 4071 and 300 V signals for the NI 4080/4082, NI 4070/4072, and NI 4065. The DMM inputs can measure sub-µV level signals with low drift,

### Handling High DC Voltages

Caution

The DMM inputs can measure sub-µV level signals with low drift, handle 300 VDC or 300 V<sub>rms</sub>(NI 4080/4082, NI 4070/4072) or 1000 VDC or 1000 V<sub>pk</sub> (NI 4081 and NI 4071) and peak VAC signals, and recover very quickly for sub-µV level measurements in a system with switching.

However, in switching systems where you are applying high voltages to a low range (e.g., 1000 V on the 10 V range), the switch receives a short-duration current transient. The current transient does not cause any degradation effect on the DMM. However, if the system switches an extreme overload to the DMM input mode with a moderate (tens of Hz) to high scanning rate over extended periods (weeks continuous or cumulative), the current transient can degrade the relay life in the switching system. For optimum switching system reliability when switching high voltages into any DMM, NI recommends selecting the range corresponding to the highest voltage expected.

Ensure that you do not exceed the voltage-hertz limit of the device. Exceeding the voltage-hertz limit is more likely to occur when measuring high-voltage/high-frequency signals. This behavior affects the internal transfer of data in the device and generates an error prompting you to reset the device and reconfigure the measurement.

Refer to the Switching Voltages section for recommendations on switching high voltages or signals with high common-mode voltage levels.

Tip

- niDMM Read (niDMM_Read)
- niDMM Read Multipoint (niDMM_ReadMultipoint)
- niDMM Fetch (niDMM_Fetch)
- niDMM Fetch Multipoint (niDMM_FetchMultipoint)

Your application can handle this error by calling the following VIs or
 functions:

1. niDMM Reset (niDMM_reset)
2. Any configuration VI or function to reconfigure the instrument to the
 required settings
3. niDMM Initiate (niDMM_Initiate), niDMM Read (niDMM_Read), or niDMM Read
 Multipoint (niDMM_ReadMultipoint) to restart the measurement

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=handling-high-dc-voltages_3.html language=enus -->
## TOPIC 00238: Handling High DC Voltages

- bundle_id: `ni-dmm`
- source_path: `handling-high-dc-voltages_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/handling-high-dc-voltages_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: All cables, connectors, and fixtures used in your system must have specifications to handle, with an adequate safety margin, 1000 V signals for the NI 4081 and NI 4071 and 300 V signals for the NI 4080/4082, NI 4070/4072, and NI 4065. The DMM inputs can measure sub-µV level signals with low drift,

### Handling High DC Voltages

Caution

The DMM inputs can measure sub-µV level signals with low drift, handle 300 VDC or 300 V<sub>rms</sub>(NI 4080/4082, NI 4070/4072) or 1000 VDC or 1000 V<sub>pk</sub> (NI 4081 and NI 4071) and peak VAC signals, and recover very quickly for sub-µV level measurements in a system with switching.

However, in switching systems where you are applying high voltages to a low range (e.g., 1000 V on the 10 V range), the switch receives a short-duration current transient. The current transient does not cause any degradation effect on the DMM. However, if the system switches an extreme overload to the DMM input mode with a moderate (tens of Hz) to high scanning rate over extended periods (weeks continuous or cumulative), the current transient can degrade the relay life in the switching system. For optimum switching system reliability when switching high voltages into any DMM, NI recommends selecting the range corresponding to the highest voltage expected.

Ensure that you do not exceed the voltage-hertz limit of the device. Exceeding the voltage-hertz limit is more likely to occur when measuring high-voltage/high-frequency signals. This behavior affects the internal transfer of data in the device and generates an error prompting you to reset the device and reconfigure the measurement.

Refer to the Switching Voltages section for recommendations on switching high voltages or signals with high common-mode voltage levels.

Tip

- niDMM Read (niDMM_Read)
- niDMM Read Multipoint (niDMM_ReadMultipoint)
- niDMM Fetch (niDMM_Fetch)
- niDMM Fetch Multipoint (niDMM_FetchMultipoint)

Your application can handle this error by calling the following VIs or
 functions:

1. niDMM Reset (niDMM_reset)
2. Any configuration VI or function to reconfigure the instrument to the
 required settings
3. niDMM Initiate (niDMM_Initiate), niDMM Read (niDMM_Read), or niDMM Read
 Multipoint (niDMM_ReadMultipoint) to restart the measurement

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=handling-high-dc-voltages_4.html language=enus -->
## TOPIC 00239: Handling High DC Voltages

- bundle_id: `ni-dmm`
- source_path: `handling-high-dc-voltages_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/handling-high-dc-voltages_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: All cables, connectors, and fixtures used in your system must have specifications to handle, with an adequate safety margin, 1000 V signals for the NI 4081 and NI 4071 and 300 V signals for the NI 4080/4082, NI 4070/4072, and NI 4065. The DMM inputs can measure sub-µV level signals with low drift,

### Handling High DC Voltages

Caution

The DMM inputs can measure sub-µV level signals with low drift, handle 300 VDC or 300 V<sub>rms</sub>(NI 4080/4082, NI 4070/4072) or 1000 VDC or 1000 V<sub>pk</sub> (NI 4081 and NI 4071) and peak VAC signals, and recover very quickly for sub-µV level measurements in a system with switching.

However, in switching systems where you are applying high voltages to a low range (e.g., 1000 V on the 10 V range), the switch receives a short-duration current transient. The current transient does not cause any degradation effect on the DMM. However, if the system switches an extreme overload to the DMM input mode with a moderate (tens of Hz) to high scanning rate over extended periods (weeks continuous or cumulative), the current transient can degrade the relay life in the switching system. For optimum switching system reliability when switching high voltages into any DMM, NI recommends selecting the range corresponding to the highest voltage expected.

Ensure that you do not exceed the voltage-hertz limit of the device. Exceeding the voltage-hertz limit is more likely to occur when measuring high-voltage/high-frequency signals. This behavior affects the internal transfer of data in the device and generates an error prompting you to reset the device and reconfigure the measurement.

Refer to the Switching Voltages section for recommendations on switching high voltages or signals with high common-mode voltage levels.

Tip

- niDMM Read (niDMM_Read)
- niDMM Read Multipoint (niDMM_ReadMultipoint)
- niDMM Fetch (niDMM_Fetch)
- niDMM Fetch Multipoint (niDMM_FetchMultipoint)

Your application can handle this error by calling the following VIs or
 functions:

1. niDMM Reset (niDMM_reset)
2. Any configuration VI or function to reconfigure the instrument to the
 required settings
3. niDMM Initiate (niDMM_Initiate), niDMM Read (niDMM_Read), or niDMM Read
 Multipoint (niDMM_ReadMultipoint) to restart the measurement

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=handling-high-dc-voltages_5.html language=enus -->
## TOPIC 00240: Handling High DC Voltages

- bundle_id: `ni-dmm`
- source_path: `handling-high-dc-voltages_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/handling-high-dc-voltages_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: All cables, connectors, and fixtures used in your system must have specifications to handle, with an adequate safety margin, 1000 V signals for the NI 4081 and NI 4071 and 300 V signals for the NI 4080/4082, NI 4070/4072, and NI 4065. The DMM inputs can measure sub-µV level signals with low drift,

### Handling High DC Voltages

Caution

The DMM inputs can measure sub-µV level signals with low drift, handle 300 VDC or 300 V<sub>rms</sub>(NI 4080/4082, NI 4070/4072) or 1000 VDC or 1000 V<sub>pk</sub> (NI 4081 and NI 4071) and peak VAC signals, and recover very quickly for sub-µV level measurements in a system with switching.

However, in switching systems where you are applying high voltages to a low range (e.g., 1000 V on the 10 V range), the switch receives a short-duration current transient. The current transient does not cause any degradation effect on the DMM. However, if the system switches an extreme overload to the DMM input mode with a moderate (tens of Hz) to high scanning rate over extended periods (weeks continuous or cumulative), the current transient can degrade the relay life in the switching system. For optimum switching system reliability when switching high voltages into any DMM, NI recommends selecting the range corresponding to the highest voltage expected.

Ensure that you do not exceed the voltage-hertz limit of the device. Exceeding the voltage-hertz limit is more likely to occur when measuring high-voltage/high-frequency signals. This behavior affects the internal transfer of data in the device and generates an error prompting you to reset the device and reconfigure the measurement.

Refer to the Switching Voltages section for recommendations on switching high voltages or signals with high common-mode voltage levels.

Tip

- niDMM Read (niDMM_Read)
- niDMM Read Multipoint (niDMM_ReadMultipoint)
- niDMM Fetch (niDMM_Fetch)
- niDMM Fetch Multipoint (niDMM_FetchMultipoint)

Your application can handle this error by calling the following VIs or
 functions:

1. niDMM Reset (niDMM_reset)
2. Any configuration VI or function to reconfigure the instrument to the
 required settings
3. niDMM Initiate (niDMM_Initiate), niDMM Read (niDMM_Read), or niDMM Read
 Multipoint (niDMM_ReadMultipoint) to restart the measurement

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=handling-high-dc-voltages_6.html language=enus -->
## TOPIC 00241: Handling High DC Voltages

- bundle_id: `ni-dmm`
- source_path: `handling-high-dc-voltages_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/handling-high-dc-voltages_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: All cables, connectors, and fixtures used in your system must have specifications to handle, with an adequate safety margin, 1000 V signals for the NI 4081 and NI 4071 and 300 V signals for the NI 4080/4082, NI 4070/4072, and NI 4065. The DMM inputs can measure sub-µV level signals with low drift,

### Handling High DC Voltages

Caution

The DMM inputs can measure sub-µV level signals with low drift, handle 300 VDC or 300 V<sub>rms</sub>(NI 4080/4082, NI 4070/4072) or 1000 VDC or 1000 V<sub>pk</sub> (NI 4081 and NI 4071) and peak VAC signals, and recover very quickly for sub-µV level measurements in a system with switching.

However, in switching systems where you are applying high voltages to a low range (e.g., 1000 V on the 10 V range), the switch receives a short-duration current transient. The current transient does not cause any degradation effect on the DMM. However, if the system switches an extreme overload to the DMM input mode with a moderate (tens of Hz) to high scanning rate over extended periods (weeks continuous or cumulative), the current transient can degrade the relay life in the switching system. For optimum switching system reliability when switching high voltages into any DMM, NI recommends selecting the range corresponding to the highest voltage expected.

Ensure that you do not exceed the voltage-hertz limit of the device. Exceeding the voltage-hertz limit is more likely to occur when measuring high-voltage/high-frequency signals. This behavior affects the internal transfer of data in the device and generates an error prompting you to reset the device and reconfigure the measurement.

Refer to the Switching Voltages section for recommendations on switching high voltages or signals with high common-mode voltage levels.

Tip

- niDMM Read (niDMM_Read)
- niDMM Read Multipoint (niDMM_ReadMultipoint)
- niDMM Fetch (niDMM_Fetch)
- niDMM Fetch Multipoint (niDMM_FetchMultipoint)

Your application can handle this error by calling the following VIs or
 functions:

1. niDMM Reset (niDMM_reset)
2. Any configuration VI or function to reconfigure the instrument to the
 required settings
3. niDMM Initiate (niDMM_Initiate), niDMM Read (niDMM_Read), or niDMM Read
 Multipoint (niDMM_ReadMultipoint) to restart the measurement

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=handling-high-dc-voltages_7.html language=enus -->
## TOPIC 00242: Handling High DC Voltages

- bundle_id: `ni-dmm`
- source_path: `handling-high-dc-voltages_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/handling-high-dc-voltages_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: All cables, connectors, and fixtures used in your system must have specifications to handle, with an adequate safety margin, 1000 V signals for the NI 4081 and NI 4071 and 300 V signals for the NI 4080/4082, NI 4070/4072, and NI 4065. The DMM inputs can measure sub-µV level signals with low drift,

### Handling High DC Voltages

Caution

The DMM inputs can measure sub-µV level signals with low drift, handle 300 VDC or 300 V<sub>rms</sub>(NI 4080/4082, NI 4070/4072) or 1000 VDC or 1000 V<sub>pk</sub> (NI 4081 and NI 4071) and peak VAC signals, and recover very quickly for sub-µV level measurements in a system with switching.

However, in switching systems where you are applying high voltages to a low range (e.g., 1000 V on the 10 V range), the switch receives a short-duration current transient. The current transient does not cause any degradation effect on the DMM. However, if the system switches an extreme overload to the DMM input mode with a moderate (tens of Hz) to high scanning rate over extended periods (weeks continuous or cumulative), the current transient can degrade the relay life in the switching system. For optimum switching system reliability when switching high voltages into any DMM, NI recommends selecting the range corresponding to the highest voltage expected.

Ensure that you do not exceed the voltage-hertz limit of the device. Exceeding the voltage-hertz limit is more likely to occur when measuring high-voltage/high-frequency signals. This behavior affects the internal transfer of data in the device and generates an error prompting you to reset the device and reconfigure the measurement.

Refer to the Switching Voltages section for recommendations on switching high voltages or signals with high common-mode voltage levels.

Tip

- niDMM Read (niDMM_Read)
- niDMM Read Multipoint (niDMM_ReadMultipoint)
- niDMM Fetch (niDMM_Fetch)
- niDMM Fetch Multipoint (niDMM_FetchMultipoint)

Your application can handle this error by calling the following VIs or
 functions:

1. niDMM Reset (niDMM_reset)
2. Any configuration VI or function to reconfigure the instrument to the
 required settings
3. niDMM Initiate (niDMM_Initiate), niDMM Read (niDMM_Read), or niDMM Read
 Multipoint (niDMM_ReadMultipoint) to restart the measurement

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=handshaking-scanning.html language=enus -->
## TOPIC 00243: Handshaking Scanning

- bundle_id: `ni-dmm`
- source_path: `handshaking-scanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/handshaking-scanning.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: With handshaking, the DMM is initiated and waiting for a trigger. The switch module is initiated, executes the first connection in the scan list, and generates a digital pulse (Scan Advanced Output). The DMM receives this signal from the switch as an input trigger, takes a measurement, and then it g

### Handshaking Scanning

With handshaking, the DMM is initiated and waiting for a trigger. The switch module is initiated, executes the first connection in the scan list, and generates a digital pulse (Scan Advanced Output). The DMM receives this signal from the switch as an input trigger, takes a measurement, and then it generates a digital pulse—Measurement Complete. When the switch receives the digital pulse, it advances to the next entry in its scan list. After the relays of the switch module have settled, the switch sends a digital pulse and triggers the DMM for a new measurement.

The following figure shows a DMM handshaking with a switch module.

[IMAGE alt='image' src='GUID-001FC5EB-4F01-43BA-9A41-5D364AA94256-a5.svg']

#### Handshaking Timing Diagram

The following figure shows the timing signals associated with the handshaking shown above.

[IMAGE alt='image' src='GUID-7F98F2DE-C0EF-479C-A5B3-0054F53B05A5-a5.svg']

where

M = measurement

WFT = wait for trigger

S&S = switch and settle

#### Hardware Connections to an External Multiplexer in Handshaking Mode

The following figure shows how to configure the hardware when performing handshaking between a DMM and an external multiplexer.

[IMAGE alt='image' src='GUID-0CC8ADB3-6C3D-4A8B-B3F1-DBA23C049F99-a5.svg']

Refer to Multiple Point Acquisitions to determine your triggering options.

Refer to Triggering for more information:

- For programming flow, refer to Single Point Acquisitions, Multi Point Acquisitions, and Continuous Acquisitions.
- For information on available trigger sources and destinations when using NI DMMs and switch
 modules, refer to Scanning Switch
 Modules.

For switch configuration information and initial programming tips, refer to the Scanning NI Switches with NI Digital Multimeters section of the NI Switches Help (Programming with NI-SWITCH»Features»Scanning»Scanning NI Switches with NI Digital Multimeters) at either of the following locations:

- Start»All Programs»National Instruments»NI-SWITCH»Documentation»NI Switches Help (if you have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not installed NI-SWITCH)

Parent topic:

Scanning

Related concepts:

- Scanning
- Multiple Point Acquisitions
- Triggering
- Single Point Acquisitions
- Continuous Acquisitions
- Scanning Switch Modules

<!--NI_TOPIC bundle=ni-dmm path=high-current-up-to-10-a-measurement-considerations.html language=enus -->
## TOPIC 00244: High-Current (Up to 10 A) Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `high-current-up-to-10-a-measurement-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/high-current-up-to-10-a-measurement-considerations.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Curren

### High-Current (Up to 10 A) Measurement Considerations

The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.

If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Current and to Related Documentation for the NI Digital Multimeters Getting Started Guide for more information about how to use the CSM-10A shunt with the DMM.

When measuring high current values, you could get errors due to resistor self-heating. The DMM uses internal shunt resistors with low temperature coefficients and good thermal resistance. Refer to the temperature coefficients in the specifications of each device for the effect of temperature changes on the accuracy of these measurements.

The NI CSM-200mA and NI CSM-10A current shunts have excellent temperature coefficients of resistance. Refer to the NI Products Web site for more information on the NI CSM-200mA and NI CSM-10A current shunts.

Check if the burden voltage can affect your measurement. Refer to Burden Voltage for an example on how to calculate the error due to burden voltage.

In applications where more than one current needs to be measured using the same DMM and the conditions require that the current cannot be interrupted across the load, use one of these two methods to measure the current:

- Use a break-before-make switch in multiplexer topology and place external shunts across the channels. Connect the shunts in series with the circuit under test and then measure the voltage drop across the shunts.
- Use make-before-break switches.

If the conditions allow interrupting the current flow through the circuit under test, it is still recommended to use external shunts. Switching currents above 1 A electromechanically can diminish the life of any switch. Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

Related concepts:

- Measuring Current
- Resistor Self-Heating
- Burden Voltage
- Switching Current

<!--NI_TOPIC bundle=ni-dmm path=high-current-up-to-10-a-measurement-considerations_2.html language=enus -->
## TOPIC 00245: High-Current (Up to 10 A) Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `high-current-up-to-10-a-measurement-considerations_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/high-current-up-to-10-a-measurement-considerations_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Curren

### High-Current (Up to 10 A) Measurement Considerations

The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.

If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Current and to Related Documentation for the NI Digital Multimeters Getting Started Guide for more information about how to use the CSM-10A shunt with the DMM.

When measuring high current values, you could get errors due to resistor self-heating. The DMM uses internal shunt resistors with low temperature coefficients and good thermal resistance. Refer to the temperature coefficients in the specifications of each device for the effect of temperature changes on the accuracy of these measurements.

The NI CSM-200mA and NI CSM-10A current shunts have excellent temperature coefficients of resistance. Refer to the NI Products Web site for more information on the NI CSM-200mA and NI CSM-10A current shunts.

Check if the burden voltage can affect your measurement. Refer to Burden Voltage for an example on how to calculate the error due to burden voltage.

In applications where more than one current needs to be measured using the same DMM and the conditions require that the current cannot be interrupted across the load, use one of these two methods to measure the current:

- Use a break-before-make switch in multiplexer topology and place external shunts across the channels. Connect the shunts in series with the circuit under test and then measure the voltage drop across the shunts.
- Use make-before-break switches.

If the conditions allow interrupting the current flow through the circuit under test, it is still recommended to use external shunts. Switching currents above 1 A electromechanically can diminish the life of any switch. Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=high-current-up-to-10-a-measurement-considerations_3.html language=enus -->
## TOPIC 00246: High-Current (Up to 10 A) Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `high-current-up-to-10-a-measurement-considerations_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/high-current-up-to-10-a-measurement-considerations_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Curren

### High-Current (Up to 10 A) Measurement Considerations

The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.

If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Current and to Related Documentation for the NI Digital Multimeters Getting Started Guide for more information about how to use the CSM-10A shunt with the DMM.

When measuring high current values, you could get errors due to resistor self-heating. The DMM uses internal shunt resistors with low temperature coefficients and good thermal resistance. Refer to the temperature coefficients in the specifications of each device for the effect of temperature changes on the accuracy of these measurements.

The NI CSM-200mA and NI CSM-10A current shunts have excellent temperature coefficients of resistance. Refer to the NI Products Web site for more information on the NI CSM-200mA and NI CSM-10A current shunts.

Check if the burden voltage can affect your measurement. Refer to Burden Voltage for an example on how to calculate the error due to burden voltage.

In applications where more than one current needs to be measured using the same DMM and the conditions require that the current cannot be interrupted across the load, use one of these two methods to measure the current:

- Use a break-before-make switch in multiplexer topology and place external shunts across the channels. Connect the shunts in series with the circuit under test and then measure the voltage drop across the shunts.
- Use make-before-break switches.

If the conditions allow interrupting the current flow through the circuit under test, it is still recommended to use external shunts. Switching currents above 1 A electromechanically can diminish the life of any switch. Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=high-current-up-to-10-a-measurement-considerations_4.html language=enus -->
## TOPIC 00247: High-Current (Up to 10 A) Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `high-current-up-to-10-a-measurement-considerations_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/high-current-up-to-10-a-measurement-considerations_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Curren

### High-Current (Up to 10 A) Measurement Considerations

The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.

If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Current and to Related Documentation for the NI Digital Multimeters Getting Started Guide for more information about how to use the CSM-10A shunt with the DMM.

When measuring high current values, you could get errors due to resistor self-heating. The DMM uses internal shunt resistors with low temperature coefficients and good thermal resistance. Refer to the temperature coefficients in the specifications of each device for the effect of temperature changes on the accuracy of these measurements.

The NI CSM-200mA and NI CSM-10A current shunts have excellent temperature coefficients of resistance. Refer to the NI Products Web site for more information on the NI CSM-200mA and NI CSM-10A current shunts.

Check if the burden voltage can affect your measurement. Refer to Burden Voltage for an example on how to calculate the error due to burden voltage.

In applications where more than one current needs to be measured using the same DMM and the conditions require that the current cannot be interrupted across the load, use one of these two methods to measure the current:

- Use a break-before-make switch in multiplexer topology and place external shunts across the channels. Connect the shunts in series with the circuit under test and then measure the voltage drop across the shunts.
- Use make-before-break switches.

If the conditions allow interrupting the current flow through the circuit under test, it is still recommended to use external shunts. Switching currents above 1 A electromechanically can diminish the life of any switch. Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=high-current-up-to-10-a-measurement-considerations_5.html language=enus -->
## TOPIC 00248: High-Current (Up to 10 A) Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `high-current-up-to-10-a-measurement-considerations_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/high-current-up-to-10-a-measurement-considerations_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Curren

### High-Current (Up to 10 A) Measurement Considerations

The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.

If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Current and to Related Documentation for the NI Digital Multimeters Getting Started Guide for more information about how to use the CSM-10A shunt with the DMM.

When measuring high current values, you could get errors due to resistor self-heating. The DMM uses internal shunt resistors with low temperature coefficients and good thermal resistance. Refer to the temperature coefficients in the specifications of each device for the effect of temperature changes on the accuracy of these measurements.

The NI CSM-200mA and NI CSM-10A current shunts have excellent temperature coefficients of resistance. Refer to the NI Products Web site for more information on the NI CSM-200mA and NI CSM-10A current shunts.

Check if the burden voltage can affect your measurement. Refer to Burden Voltage for an example on how to calculate the error due to burden voltage.

In applications where more than one current needs to be measured using the same DMM and the conditions require that the current cannot be interrupted across the load, use one of these two methods to measure the current:

- Use a break-before-make switch in multiplexer topology and place external shunts across the channels. Connect the shunts in series with the circuit under test and then measure the voltage drop across the shunts.
- Use make-before-break switches.

If the conditions allow interrupting the current flow through the circuit under test, it is still recommended to use external shunts. Switching currents above 1 A electromechanically can diminish the life of any switch. Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=high-current-up-to-10-a-measurement-considerations_6.html language=enus -->
## TOPIC 00249: High-Current (Up to 10 A) Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `high-current-up-to-10-a-measurement-considerations_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/high-current-up-to-10-a-measurement-considerations_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Curren

### High-Current (Up to 10 A) Measurement Considerations

The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.

If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Current and to Related Documentation for the NI Digital Multimeters Getting Started Guide for more information about how to use the CSM-10A shunt with the DMM.

When measuring high current values, you could get errors due to resistor self-heating. The DMM uses internal shunt resistors with low temperature coefficients and good thermal resistance. Refer to the temperature coefficients in the specifications of each device for the effect of temperature changes on the accuracy of these measurements.

The NI CSM-200mA and NI CSM-10A current shunts have excellent temperature coefficients of resistance. Refer to the NI Products Web site for more information on the NI CSM-200mA and NI CSM-10A current shunts.

Check if the burden voltage can affect your measurement. Refer to Burden Voltage for an example on how to calculate the error due to burden voltage.

In applications where more than one current needs to be measured using the same DMM and the conditions require that the current cannot be interrupted across the load, use one of these two methods to measure the current:

- Use a break-before-make switch in multiplexer topology and place external shunts across the channels. Connect the shunts in series with the circuit under test and then measure the voltage drop across the shunts.
- Use make-before-break switches.

If the conditions allow interrupting the current flow through the circuit under test, it is still recommended to use external shunts. Switching currents above 1 A electromechanically can diminish the life of any switch. Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=high-current-up-to-10-a-measurement-considerations_7.html language=enus -->
## TOPIC 00250: High-Current (Up to 10 A) Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `high-current-up-to-10-a-measurement-considerations_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/high-current-up-to-10-a-measurement-considerations_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Curren

### High-Current (Up to 10 A) Measurement Considerations

The NI 4065, NI 4071, and NI 4081 can measure currents up to 3 A. The NI 4070/4072 and NI 4080/4082 can measure currents up to 1 A.

If you need to measure currents higher than the maximum range available, you can use the CSM-10A external shunt to measure currents up to 10 A. Refer to Measuring Current and to Related Documentation for the NI Digital Multimeters Getting Started Guide for more information about how to use the CSM-10A shunt with the DMM.

When measuring high current values, you could get errors due to resistor self-heating. The DMM uses internal shunt resistors with low temperature coefficients and good thermal resistance. Refer to the temperature coefficients in the specifications of each device for the effect of temperature changes on the accuracy of these measurements.

The NI CSM-200mA and NI CSM-10A current shunts have excellent temperature coefficients of resistance. Refer to the NI Products Web site for more information on the NI CSM-200mA and NI CSM-10A current shunts.

Check if the burden voltage can affect your measurement. Refer to Burden Voltage for an example on how to calculate the error due to burden voltage.

In applications where more than one current needs to be measured using the same DMM and the conditions require that the current cannot be interrupted across the load, use one of these two methods to measure the current:

- Use a break-before-make switch in multiplexer topology and place external shunts across the channels. Connect the shunts in series with the circuit under test and then measure the voltage drop across the shunts.
- Use make-before-break switches.

If the conditions allow interrupting the current flow through the circuit under test, it is still recommended to use external shunts. Switching currents above 1 A electromechanically can diminish the life of any switch. Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current
