# NI DOCUMENT BUNDLE: ni-9145-ethercat-expansion-chassis-configuration

<!--NI_BUNDLE_CHUNK bundle=ni-9145-ethercat-expansion-chassis-configuration start=1 end=41 -->
<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9201-9221-extensions.html language=enus -->
## TOPIC 00001: NI-9201/9221 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9201-9221-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9201-9221-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9201/9221. NI-9201/9221 Vendor Configuration ExtensionsIndex Sub Type R/W Description 0x2001 0 ARR:U32 — Scan List = 9 1 R Channels to Convert = <1..8>, default = 8 2..9 R/W Channel Code 0x2002 0 U32 R/W Fast Convert = 0/1, def

### NI-9201/9221 Vendor Configuration
 Extensions

NI-9201/9221

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | — | Scan List = 9 |
| 1 | R | Channels to Convert = <1..8>, default = 8 |  |  |
| 2..9 | R/W | Channel Code |  |  |
| 0x2002 | 0 | U32 | R/W | Fast Convert = 0/1, default = 1 (fast) |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 32 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| ... | — | — |  |  |
| 15 | R | Ch7 Offset |  |  |
| 16 | R | Ch7 Gain |  |  |
| 17 | R | External Calibration, Ch0 Offset |  |  |
| ... | — | — |  |  |

#### NI-9201/9221 Scan List

The scan list channel codes consist of two-bit fields in a 32-bit entry.

| Bits | Field |
| --- | --- |
| 31..24 | = 0 |
| 23..16 | Data Offset[t] |
| 15..8 | = 0 |
| 7..0 | Convert Flag[t+2] |

Bits <23..16> describe the data offset to store a conversion at time
 t, and bits <7..0> describe the conversion control code that
 takes effect two conversions in the future, at time t+2. For the NI-9201/9221, this conversion code is a bit flag where bit 0 represents a conversion on channel 0, through bit 7 for channel 7.

For example, the scan list entry 0x00010008 indicates this scan stores at address 1, and
 the conversion two in the future is channel 3 (bit 3 set = 8).

| Index | Sub | Type | Value |
| --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | 9 |
| 1 | 8 |  |  |
| 2 | 0x00000004 |  |  |
| 3 | 0x00010008 |  |  |
| 4 | 0x00020010 |  |  |
| 5 | 0x00030020 |  |  |
| 6 | 0x00040040 |  |  |
| 7 | 0x00050080 |  |  |
| 8 | 0x00060001 |  |  |
| 9 | 0x00070002 |  |  |

#### NI-9201/9221 Calibration Data

The NI-9201/9221 modules have eight channels with a nominal
 range of ±10.53 V and ±62.5 V,
 respectively. Each channel has an associated LSB weight, which is the number of volts per
 bit, and an offset, which is the number of volts per bit measured when the inputs are
 grounded.

Note

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | nV/LSB |
| Offset | Signed | nV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 1.

V

corrected

(

V

raw

)

=

V

raw

(

bits

)

×

{

LSB

weight

(

n

V

bits

)

×

10

−

9

(

V

n

V

)

}

−

{

Offset

(

n

V

)

×

10

−

9

(

V

n

V

)

}

V

corrected

(

V

raw

)

=

V

raw

(

bits

)

×

{

LSB

weight

(

n

V

bits

)

×

10

−

9

(

V

n

V

)

}

−

{

Offset

(

n

V

)

×

10

−

9

(

V

n

V

)

}

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9203-extensions.html language=enus -->
## TOPIC 00002: NI-9203 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9203-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9203-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9203. NI-9203 Vendor Configuration ExtensionsIndex Sub Type R/W Description 0x2001 0 ARR:U32 — Scan List = 9 1 R Channels to Convert = <1..8>, default = 82..9 R/W Channel Code 0x2002 0 U32 R/W Unipolar Channel Mask 0x2100 0 ARR

### NI-9203 Vendor Configuration
 Extensions

NI-9203

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | — | Scan List = 9 |
| 1 | R | Channels to Convert = <1..8>, default = 8 |  |  |
| 2..9 | R/W | Channel Code |  |  |
| 0x2002 | 0 | U32 | R/W | Unipolar Channel Mask |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 36 |
| 1 | R | Bipolar Offset |  |  |
| 2 | R | Ch0 Bipolar Gain |  |  |
| 3 | R | Ch1 Gain |  |  |
| ... | — | — |  |  |
| 9 | R | Ch7 Gain |  |  |
| 10 | R | Unipolar Offset |  |  |
| 11 | R | Ch0 Unipolar Gain |  |  |
| ... | — | — |  |  |
| 19 | R | R | External Calibration, Bipolar Gain |  |
| ... | — | — |  |  |

#### NI-9203 Scan List

The scan list channel codes consist of three bit fields in a 32-bit entry.

| Bits | Field |
| --- | --- |
| 31..24 | = 0 |
| 23..16 | Data Offset[t] |
| 15..4 | = 0 |
| 3 | Bipolar = 0, Unipolar = 1 |
| 2..0 | Channel Code[t+2] |

Bits <23..16> describe the data offset to store a conversion at time
 t, and bits <3..0> describe the conversion control code that will
 take effect two conversions in the future, at time t+2. On the NI-9203,
 bit 3 determines whether the result is bipolar (signed) or unipolar (unsigned), and bits
 <2..0> are the channel number reversed.

| Channel | Reversed Bits |
| --- | --- |
| 0 = 0b000 | 0b000 = 0 |
| 1 = 0b001 | 0b100 = 4 |
| 2 = 0b010 | 0b010 = 2 |
| 3 = 0b011 | 0b110 = 6 |
| 4 = 0b100 | 0b001 = 1 |
| 5 = 0b101 | 0b101 = 5 |
| 6 = 0b110 | 0b011 = 3 |
| 7 = 0b111 | 0b111 = 7 |

For example, the scan list entry 0x00010006 indicates that this scan gets stored at address
 1, and that conversion two is a bipolar channel 3 (3 reversed = 6).

| Index | Sub | Type | Value |
| --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | 9 |
| 1 | 8 |  |  |
| 2 | 0x00000002 |  |  |
| 3 | 0x00010006 |  |  |
| 4 | 0x00020001 |  |  |
| 5 | 0x00030005 |  |  |
| 6 | 0x00040003 |  |  |
| 7 | 0x00050007 |  |  |
| 8 | 0x00060000 |  |  |
| 9 | 0x00070004 |  |  |

#### NI-9203 Calibration Data

The NI-9203 has eight channels each with two modes. Each channel can have a nominal
 unipolar input range of 0 mA to 20
 mA or bipolar ±20 mA. Each channel has an associated
 LSB weight, which is the number of amps per bit, and an offset, which is the number of amps
 per bit measured when the inputs are open.

Note

The difference in offset from channel to channel is negligible.

The calibration data gives one offset and eight gains for each mode, for a total of 2
 offsets and 16 gains. All channels in a given mode use the same offset. The host can then
 take these constants and adjust the raw data into calibrated data.

The calibration data is stored in a U32 array, though each offset should be interpreted as
 a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | pA/LSB |
| Offset | Signed | pA |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 2.

I

c

o

r

r

e

c

t

e

d

(

I

r

a

w

)

=

(

I

raw

⁢

)

L

S

B

w

e

i

g

h

t

−

I

o

f

f

s

e

t

I

c

o

r

r

e

c

t

e

d

(

I

r

a

w

)

=

(

I

raw

⁢

)

L

S

B

w

e

i

g

h

t

−

I

o

f

f

s

e

t

| Term | Units | Definition |
| --- | --- | --- |
| Icorrected | pA | Calibrated current |
| Iraw | bits | Raw code from the NI-9203 |
| LSBweight | pA/bit | Amount of pA in one bit |
| Ioffset | pA | Offset at 0 mA |

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9205-9206-extensions.html language=enus -->
## TOPIC 00003: NI-9205/9206 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9205-9206-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9205-9206-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9205/9206. NI-9205/9206 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 ARR:U32 — Scan List = 33 1 R Channels to Convert = <1..32>, default = 32 2..33 R/W Channel Code 0x2100 0 ARR:U32 — Calibration = 24

### NI-9205/9206 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9205/9206.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | — | Scan List = 33 |
| 1 | R | Channels to Convert = <1..32>, default = 32 |  |  |
| 2..33 | R/W | Channel Code |  |  |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 24 |
| 1 | R | Coeff3 |  |  |
| 2 | R | Coeff2 |  |  |
| 3 | R | Coeff1 |  |  |
| 4 | R | Coeff0 |  |  |
| 5 | R | 10 V Offset |  |  |
| 6 | R | 10 V Gain |  |  |
| 7 | R | 5 V Offset |  |  |
| ... | — | — |  |  |
| 13 | R | User Calibration, Coeff 3 |  |  |
| ... | — | — |  |  |

#### NI-9205/9206 Scan List

The scan list channel codes consist of eight bit fields in a 32-bit entry.

| Bits | Field |
| --- | --- |
| 31..24 | = 0 |
| 23..16 | Data Offset[t] |
| 15..0 | Conversion Code[t+2] |

Bits <23..16> describe the data offset to store a conversion at time
 t, and bits <15..0> describe a complex conversion control code
 that takes effect two conversions in the future, at time t+2. The
 following table lists the conversion code NI-9205/9206.

| Bits | Field |
| --- | --- |
| 15..13 | 001 = Read AI |
| 12..11 | Bank: 01 = Channels <0..15> 10 = Channels <16..31> |
| 10..8 | Channel LSB = <0..7> |
| 7..6 | 00 = Cal Pos Ref5V |
| 5..4 | 00 = NRSE 11 = Cal Neg AI GND RSE or DIFF |
| 3..2 | Mode: 01 = DIFF 10 = Single-End A (Ch. <0..7>, <16..23>) 11 = Single-End B (Ch. <8..15>, <24..31>) |
| 1..0 | 00 = ±10 V 01 = ±5 V 10 = ±1 V 11 = ±200 mV |

| Index | Sub | Type | Value | Sub | Value |
| --- | --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | 33 | — | — |
| 1 | 32 | — | — |  |  |
| 2 | 0x00002A38 | 18 | 0x00103238 |  |  |
| 3 | 0x00012B38 | 19 | 0x00113338 |  |  |
| 4 | 0x00022C38 | 20 | 0x00123438 |  |  |
| 5 | 0x00032D38 | 21 | 0x00133538 |  |  |
| 6 | 0x00042E38 | 22 | 0x00143638 |  |  |
| 7 | 0x00052F38 | 23 | 0x00153738 |  |  |
| 8 | 0x0006283C | 24 | 0x0016303C |  |  |
| 9 | 0x0007293C | 25 | 0x0017313C |  |  |
| 10 | 0x00082A3C | 26 | 0x0018323C |  |  |
| 11 | 0x00092B3C | 27 | 0x0019333C |  |  |
| 12 | 0x000A2C3C | 28 | 0x001A343C |  |  |
| 13 | 0x000B2D3C | 29 | 0x001B353C |  |  |
| 14 | 0x000C2E3C | 30 | 0x001C363C |  |  |
| 15 | 0x000D2F3C | 31 | 0x001D373C |  |  |
| 16 | 0x000E3038 | 32 | 0x001E2838 |  |  |
| 17 | 0x000F3138 | 33 | 0x001F2938 |  |  |

#### NI-9205/9206 Calibration Data

The NI-9205/9206 uses a quadratic formula for conversion from 16-bit raw data to calibrated
 data.

The NI-9205/9206 EEPROM provides overall polynomial values a3-a0 along with gain and offset
 values for each voltage range. Complete the following procedure to convert 16-bit raw data
 to calibrated data.

1. Convert the 32-bit hex values to 64-bit
 floating point format for use in the calibration formula.
2. Select the 32-bit gain value for a particular
 range.
3. Select the 32-bit offset value (to be
 interpreted as a signed int) for a particular range.
4. Use the above final coefficients and complete
 the following steps in the quadratic equation to convert raw 16-bit data into scaled
 volts: where f64(x) typecasts the value to a floating point:
  1. a0 = (f64(a0) × rangeGain) + rangeOffset
  2. a1 = f64(a1) × rangeGain
  3. a2 = f64(a2) × rangeGain
  4. a3 = f64(a3) × rangeGain
5. Use the following formula with a3-a0 to obtain
 the scaled 16-bit value in volts, where x = signed un-scaled 16-bit data read from device:
 Scaled 16-bit signed data in volts = a3 × x<sup>3</sup> + a2 ×
 x<sup>2</sup> + a1 × x + a0

Refer to *NI-9201/9221 Vendor Configuration Extensions* for information about
 how to decode the raw data using only the offset and gain values.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9207-extensions.html language=enus -->
## TOPIC 00004: NI-9207 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9207-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9207-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9207. NI-9207 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 ARR:U32 — Scan List =17 1 R Channels to Convert = <1..16>, default = 16 2..17 R/W Channel Code 0x2002 0 U32 R/W Conversion Speed Control = 0

### NI-9207 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9207.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | — | Scan List =17 |
| 1 | R | Channels to Convert = <1..16>, default = 16 |  |  |
| 2..17 | R/W | Channel Code |  |  |
| 0x2002 | 0 | U32 | R/W | Conversion Speed Control = 0 or 1, default = 0 |

#### NI-9207 Conversion Speed Control

The NI-9207 converts at two pre-defined rates, as specified
 in the Speed Control field.

Note

| Speed Control | Meaning | Conversion Rate |
| --- | --- | --- |
| 0 | High Accuracy | 62.5 ms/channel (1 s total) |
| 1 | High Speed | 1.92 ms/channel (30.72 ms total) |

#### NI-9207 Scan List

The scan list is a simple, ordered list of channels to convert. The NI-9207 has a total of 16 measurable channels.

| Index | Sub | Type | Value |
| --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | 17 |
| 1 | 16 |  |  |
| 2 | 0 |  |  |
| 3 | 1 |  |  |
| ... | ... |  |  |
| 17 | 15 |  |  |

#### NI-9207 Calibration Data

Calibration data is set by the device driver during initialization and the calibration
 conversion is performed on the module ADC.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9208-externsions.html language=enus -->
## TOPIC 00005: NI-9208 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9208-externsions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9208-externsions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9208. NI-9208 Vendor Configuration Extensions Index Sub Type R/W Description 0x2100 0 ARR:U32 — Scan List = 17 1 R Channels to Convert = <1..16>, default = 16 2..17 R/W Channel Code 0x2002 0 U32 R/W Conversion Speed Control = 0

### NI-9208 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9208.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2100 | 0 | ARR:U32 | — | Scan List = 17 |
| 1 | R | Channels to Convert = <1..16>, default = 16 |  |  |
| 2..17 | R/W | Channel Code |  |  |
| 0x2002 | 0 | U32 | R/W | Conversion Speed Control = 0 or 1, default = 0 |

#### NI-9208 Conversion Speed Control

The NI-9208 converts at two pre-defined rates, as specified
 in the Speed Control field.

Note

| Speed Control | Meaning | Conversion Rate |
| --- | --- | --- |
| 0 | High Resolution | 62.5 ms/channel (1 s total) |
| 1 | High Speed | 1.92 ms/channel (30.72 ms total) |

#### NI-9208 Scan List

The scan list is a simple, ordered list of channels to convert. The NI-9208 has a total of 16 measurable channels.

| Index | Sub | Type | Value |
| --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | 17 |
| 1 | 16 |  |  |
| 2 | 0 |  |  |
| 3 | 1 |  |  |
| ... | ... |  |  |
| 17 | 15 |  |  |

#### NI-9208 Calibration Data

Calibration data is set by the device driver during initialization and the calibration
 conversion is performed on the module ADC.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9209-extensions.html language=enus -->
## TOPIC 00006: NI-9209 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9209-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9209-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9209. NI-9209 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 ARR:U32 - Scan List = 33 1 R Channels to Convert = <1..32>, default = 32 2..33 R/W Channel Code 0x2002 0 U32 R/W Conversion Speed Control = 0

### NI-9209 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9209.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | - | Scan List = 33 |
| 1 | R | Channels to Convert = <1..32>, default = 32 |  |  |
| 2..33 | R/W | Channel Code |  |  |
| 0x2002 | 0 | U32 | R/W | Conversion Speed Control = 0 or 1, default = 0 |

#### NI-9209 Conversion Speed Control

The NI-9209 converts at two pre-defined rates, as specified in the Speed Control field.

| Speed Control | Meaning | Conversion Rate |
| --- | --- | --- |
| 0 | High Resolution | 52 ms/channel |
| 1 | High Speed | 2 ms/channel |

#### NI-9209 Scan List

The scan list channel codes consist of eight bit fields in a 32-bit entry.

| Bits | Field |
| --- | --- |
| 31..6 | Reserved |
| 5 | Mode: 0 = DIFF 1 = RSE |
| 4..0 | Channel number = <0..31> |

| Index | Sub | Type | Value |
| --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | 33 |
| 1 | 32 |  |  |
| 2 | 0x20 \| 0x00 |  |  |
| 3 | 0x20 \| 0x01 |  |  |
| ... | ... |  |  |
| 33 | 0x20 \| 0x1F |  |  |

#### NI-9209 Calibration Data

Calibration data is set up by driver during initialization, and the calibration conversion
 is performed on the module ADC itself. The calibration tables are not required.

Use the following equation to scale the calibrated ADC codes into voltages for the NI-9209:

Figure 3.

V

c

o

r

r

e

c

t

e

d

⁢

(

R

r

a

w

)

=

V

r

a

w

(

bits

)

×

1.2398514

(

µ

V

bits

)

×

10

−

6

(

V

µ

V

)

V

c

o

r

r

e

c

t

e

d

⁢

(

R

r

a

w

)

=

V

r

a

w

(

bits

)

×

1.2398514

(

µ

V

bits

)

×

10

−

6

(

V

µ

V

)

where V<sub>corrected</sub> represents the calibrated voltage value and V<sub>raw</sub>
 represents the data returned by the NI-9209 in bits.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9211-extensions.html language=enus -->
## TOPIC 00007: NI-9211 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9211-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9211-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9211. NI-9211 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 ARR:U32 — Scan List = 7 1 R Channels to Convert = <1..6>, default = 6 2..7 R/W Channel Number NI-9211 Scan List The scan list is a simple, or

### NI-9211 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9211.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | — | Scan List = 7 |
| 1 | R | Channels to Convert = <1..6>, default = 6 |  |  |
| 2..7 | R/W | Channel Number |  |  |

#### NI-9211 Scan List

The scan list is a simple, ordered list of channels to convert. The NI-9211 has a total of
 six measurable channels.

- <0..3>: four input channels (always
 measured in a ±80 mV range)
- 4: one cold junction channel (always measured
 in a ±2.5 V range)
- 5: one auto zero channel (always measured in a
 ±80 mV range)

| Index | Sub | Type | Value |
| --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | 7 |
| 1 | 6 |  |  |
| 2 | 0 |  |  |
| 3 | 1 |  |  |
| ... | ... |  |  |
| 7 | 5 |  |  |

#### NI-9211 Calibration Data

Calibration data is set by the device driver during initialization and the calibration
 conversion is performed on the module ADC.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9212-extensions.html language=enus -->
## TOPIC 00008: NI-9212 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9212-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9212-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9212. NI-9212 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R/W Conversion Speed Control = 2, 8, 9 or 15, default = 15 0x2003 0 ARR:U32 R Open Thermocouple Status (also as 8-bit PDO) NI-9212 Conver

### NI-9212 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9212.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R/W | Conversion Speed Control = 2, 8, 9 or 15, default = 15 |
| 0x2003 | 0 | ARR:U32 | R | Open Thermocouple Status (also as 8-bit PDO) |

#### NI-9212 Conversion Speed
 Control

The NI-9212 converts at four pre-defined rates, as specified
 in the Speed Control field.

Note

| Speed Control | Meaning | Conversion Rate |
| --- | --- | --- |
| 2 (0x02) | High Speed | 10.39 ms/module |
| 8 (0x08) | Best 60 Hz Rejection | 138 ms/module |
| 9 (0x09) | Best 50 Hz Rejection | 117.49 ms/module |
| 15 (0x0F) | High Resolution | 548.2 ms/module |

#### NI-9212 Status

The following table lists the error/status field definitions.

| Bits | Field |
| --- | --- |
| 31..8 | Reserved |
| 7..0 | The latest detected open thermocouple status. Each channel takes one bit. |

#### NI-9212 Calibration Data

Calibration data is set up by the driver during initialization. The calibration conversion
 is performed on the module ADC itself. The third-party user does not need to check the index
 0x2100 to calibrate the data manually.

Use the following equation to calculate raw voltage for the cold-junction compensation
 (CJC):

Figure 18.

V

CJCvoltage

=

(

78.125

⁢

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

Bit

CJC

V

CJCvoltage

=

(

78.125

⁢

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

Bit

CJC

where V<sub>CJCvoltage</sub> represents raw CJC voltage and Bit<sub>CJC</sub> represents
 binary bits for the CJC

Use the following equation to calculate raw voltage for the thermocouple (TC):

Figure 5.

V

TCvoltage

=

(

78.125

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

Bit

TC

V

TCvoltage

=

(

78.125

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

Bit

TC

where V<sub>TCvoltage</sub> represents raw TC voltage and Bit<sub>TC</sub> represents
 binary bits for the TC

After calculating the CJC and the TC voltage, use the NI-9212 Getting Started example,
 which is located in the LabVIEW\examples\CompactRIO\Module Specific
 directory, to calculate the resistance of the TC and the CJC temperature in degrees Celsius.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9213-extensions.html language=enus -->
## TOPIC 00009: NI-9213 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9213-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9213-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9213. NI-9213 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 ARR:U32 — Scan List = 16 1 R Channels to Convert = <1..18>, default = 18 2..19 R/W Channel Code 0x2002 0 U32 R/W Channel Speed Control = 2 or

### NI-9213 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9213.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | — | Scan List = 16 |
| 1 | R | Channels to Convert = <1..18>, default = 18 |  |  |
| 2..19 | R/W | Channel Code |  |  |
| 0x2002 | 0 | U32 | R/W | Channel Speed Control = 2 or 15, default = 2 |
| 0x2003 | 0 | U32 | R | Common Mode Range Error Detection Status (also as 8-bit PDO) |

#### NI-9213 Conversion Speed Control

The NI-9213 converts at two pre-defined rates, as specified
 by the Speed Control field.

Note

| Speed Control | Meaning | Conversion Rate |
| --- | --- | --- |
| 2 (0x02) | High Accuracy | 55 ms/channel (.99 s total) |
| 15 (0x0F) | High Speed | 740 µs/channel (12.32 ms total) |

#### NI-9213 Common Mode Error/Status

The following tables define the error/status field for the NI-9213.

| Bits | Field |
| --- | --- |
| 31..16 | Reserved |
| 15..0 | The most recently detected open thermocouple status. Each channel takes one bit. |

| Bits | Field |
| --- | --- |
| 31..16 | Reserved |
| 15..0 | The most recently detected common mode voltage error. Each channel takes one bit. |

#### NI-9213 Scan List

The scan list is a simple list of channels to convert, in order. The NI-9213 has eighteen
 total channels that can be measured:

- <0..15>: 16 thermocouple channels (always
 measured in a ±78.125 mV range)
- 16: one cold junction channel (always measured
 in a ±2.5 V range)
- 17: one auto-zero channel (always measured in a
 ±78.125 mV range)

| Index | Sub | Type | Value |
| --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | 19 |
| 1 | 18 |  |  |
| 2 | 0 |  |  |
| 3 | 1 |  |  |
| ... | ... |  |  |
| 18 | 16 |  |  |
| 19 | 17 |  |  |

#### NI-9213 Calibration Data

Calibration data is set up by the driver during initialization. The calibration conversion
 is performed on the module ADC itself. The third-party user does not need to check the index
 0x2100 to calibrate the data manually.

Use the following equation to calculate raw voltage for the cold-junction compensation
 (CJC):

Figure 6.

V

CJCvoltage

=

(

78.125

⁢

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

Bit

CJC

V

CJCvoltage

=

(

78.125

⁢

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

Bit

CJC

where V<sub>CJCvoltage</sub> represents raw CJC voltage and Bit<sub>CJC</sub> represents
 binary bits for the CJC.

Use the following equation to calculate raw voltage for the thermocouple (TC):

Figure 7.

V

TCvoltage

=

(

78.125

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

(

Bit

TC

−

Bit

autozero

)

V

TCvoltage

=

(

78.125

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

(

Bit

TC

−

Bit

autozero

)

- V TCvoltage represents raw TC voltage
- Bit TC represents binary bits for the TC
- Bit autozero represents binary bits returned by the autozero channel

Use the following equation to calculate the resistance of the thermistor:

Figure 8.

R

=

(

10000

×

32

×

V

CJCvoltage

)

÷

(

2.5

−

32

×

V

CJCvoltage

)

R

=

(

10000

×

32

×

V

CJCvoltage

)

÷

(

2.5

−

32

×

V

CJCvoltage

)

where R represents the resistance of the thermistor and V<sub>CJCvoltage</sub> = raw CJC
 voltage.

Use the following equation to calculate the CJC temperature:

Figure 9.

T

=

{

1

÷

[

A

+

B

(

In

(

R

)

)

+

C

(

In

(

R

)

)

3

]

}

−

(

273.15

+

Offset

)

T

=

{

1

÷

[

A

+

B

(

In

(

R

)

)

+

C

(

In

(

R

)

)

3

]

}

−

(

273.15

+

Offset

)

- T represents the temperature in degrees Celsius
- R represents the resistance of the thermistor
- A is 1.2873851 × 10 -3
- B is 2.3575235× 10 -4
- C is 9.4978060 × 10 -8
- Offset represents the offset constant, which the constant is the typical temperature
 gradient between the CJC sensor and the TC cold junction

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9214-extensions.html language=enus -->
## TOPIC 00010: NI-9214 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9214-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9214-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9214. NI-9214 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 ARR:U32 — Scan List = 21 1 R Channels to Convert = <1..20>, default = 20 2..21 R/W Channel Code 0x2002 0 U32 R/W Conversion Speed Control/Ope

### NI-9214 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9214.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | — | Scan List = 21 |
| 1 | R | Channels to Convert = <1..20>, default = 20 |  |  |
| 2..21 | R/W | Channel Code |  |  |
| 0x2002 | 0 | U32 | R/W | Conversion Speed Control/Open Thermocouple Detection |
| 0x2003 | 0 | U32 | R | Common Mode Range Error Detection Status (also as 8-bit PDO) |

#### NI-9214 Conversion Speed Control/Open
 Thermocouple Detection (0x2002)

The NI-9214 converts at two pre-defined rates, as specified
 in the Speed Control field. The conversion rate assumes that 20 channels are in the scan
 list. The NI-9214 can also enable/disable open thermocouple
 detection.

| Bits | Field |
| --- | --- |
| 31..5 | Reserved |
| 4 | Open Thermocouple Detection: 0x10: Enable 0x00: Disable |
| 3..0 | Conversion Speed Control: 0x02: High Accuracy, 52 ms/channel (1.04 s total) 0x0F: High Speed, 735 µs/channel (14.7 ms total) |

#### NI-9214 Common Mode Error/Status
 (0x2003)

The following tables describe the error/status field for the NI-9214.

| Bits | Field |
| --- | --- |
| 31..6 | Reserved |
| 15..0 | The most recently detected open thermocouple status. Each channel takes one bit. |

| Bits | Field |
| --- | --- |
| 31..6 | Reserved |
| 15..0 | The most recently detected common mode voltage error. Each channel takes one bit. |

#### NI-9214 Scan List

The scan list is a simple list of channels to convert, in order. The NI-9214 has 20 total channels that can be measured:

- 0..15: 16 thermocouple channels (always
 measured in a ±78.125 mV range)
- 16: One auto-zero channel (always measured in a
 ±78.125 mV range)
- 17: Cold junction channel 0 (always measured in
 a ±2.5 V range)
- 18: Cold junction channel 1 (always measured in
 a ±2.5 V range)
- 19: Cold junction channel 2 (always measured in
 a ±2.5 V range)

| Index | Sub | Type | Value |
| --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | 21 |
| 1 | 20 |  |  |
| 2 | 0 |  |  |
| 3 | 1 |  |  |
| ... | — |  |  |
| 20 | 18 |  |  |
| 21 | 19 |  |  |

#### NI-9214 Calibration Data

Calibration data is set up by the driver during initialization. The calibration conversion
 is performed on the module ADC itself. The third-party user does not need to check the index
 0x2100 to calibrate the data manually.

Use the following equation to calculate raw voltage for the cold-junction compensation
 (CJC):

Figure 10.

V

CJCvoltage

=

(

78.125

⁢

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

Bit

CJC

V

CJCvoltage

=

(

78.125

⁢

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

Bit

CJC

where V<sub>CJCvoltage</sub> represents raw CJC voltage and Bit<sub>CJC</sub> represents
 binary bits for the CJC.

Use the following equation to calculate raw voltage for the thermocouple (TC):

Figure 11.

V

TCvoltage

=

(

78.125

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

Bit

TC

V

TCvoltage

=

(

78.125

⁢

mV

⁢

+

78.125

⁢

mV

)

2

24

×

Bit

TC

where V<sub>TCvoltage</sub> represents raw TC voltage and Bit<sub>TC</sub> represents
 binary bits for the TC.

After calculating the CJC and TC voltage, use the NI-9214 Getting Started example located
 in the LabVIEW\examples\CompactRIO\Module Specific directory to
 calculate the resistance of the thermistor and the CJC temperature in degrees Celsius.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9215-extensions.html language=enus -->
## TOPIC 00011: NI-9215 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9215-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9215-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9215. NI-9215 Vendor Configuration Extensions Index Sub Type R/W Description 0x2100 0 ARR:U32 — Calibration = 16 1 R Ch0 Offset 2 R Ch0 Gain ... — — 7 R Ch3 Offset 8 R Ch3 Gain 9 R External Calibration, Ch0 Offset ... — — NI-92

### NI-9215 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9215.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 16 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| ... | — | — |  |  |
| 7 | R | Ch3 Offset |  |  |
| 8 | R | Ch3 Gain |  |  |
| 9 | R | External Calibration, Ch0 Offset |  |  |
| ... | — | — |  |  |

#### NI-9215 Calibration Data

The NI-9215 has four channels with a nominal range of ±10.4 V. Each channel has an associated LSB weight, which is
 the number of volts per bit, and an offset, which is the number of volts per bit measured
 when the inputs are grounded.

Note

The NI-9215 EEPROM stores these two constants for each
 channel. The host can then take these constants and adjust the raw data into calibrated
 data.

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | nV/LSB |
| Offset | Signed | nV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 12.

V

c

o

r

r

e

c

t

e

d

(

V

r

a

w

)

=

V

raw

(

bits

)

×

{

LSB

w

e

i

g

h

t

(

nV

bits

)

×

10

−

9

(

V

nV

)

}

−

{

Offset

(

nV

)

×

10

−

9

(

V

nV

)

}

V

c

o

r

r

e

c

t

e

d

(

V

r

a

w

)

=

V

raw

(

bits

)

×

{

LSB

w

e

i

g

h

t

(

nV

bits

)

×

10

−

9

(

V

nV

)

}

−

{

Offset

(

nV

)

×

10

−

9

(

V

nV

)

}

where V<sub>corrected</sub> represents the calibrated voltage value and V<sub>raw</sub>
 represents data returned by the NI-9215 in bits.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9216-9226-extensions.html language=enus -->
## TOPIC 00012: NI-9216/9226 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9216-9226-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9216-9226-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9216/9226. NI-9216/9226 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 ARR:U32 - Scan List = 9 1 R Channels to Convert = <1..8>, default = 8 2..9 R/W Channel Code 0x2002 0 U32 R/W Conversion Speed Contr

### NI-9216/9226 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9216/9226.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | - | Scan List = 9 |
| 1 | R | Channels to Convert = <1..8>, default = 8 |  |  |
| 2..9 | R/W | Channel Code |  |  |
| 0x2002 | 0 | U32 | R/W | Conversion Speed Control = 2 or 31, default = 31 |
| 0x2100 | 0 | ARR:U32 | - | Calibration = 32 |
| 1 | - | Ch0 Offset |  |  |
| 2 | - | Ch0 Gain |  |  |
| 3 | - | Ch1 Offset |  |  |
| ... | - | - |  |  |
| 16 | R | Ch7 Gain |  |  |
| 17 | - | External Ch0 Offset |  |  |
| ... | - | - |  |  |

#### NI-9216/9226 Conversion Speed
 Control

The NI-9216/9226 converts at two pre-defined rates, as specified in the Speed Control
 field.

Note

| Speed Control | Meaning | Conversion Rate |
| --- | --- | --- |
| 31 (0x1F) | High Accuracy | 200 ms/channel (1600 ms total) |
| 2 (0x02) | High Speed | 2.5 ms/channel (20 ms total) |

#### NI-9216/9226 Scan List

The scan list channel codes consist of eight bit fields in a 32-bit entry.

| Bits | Field |
| --- | --- |
| 31..16 | Reserved |
| 15..8 | Data Offset[t] |
| 7..0 | Convert Code [t+1] |

Bits <15..8> describe the data offset to store a conversion at time
 t, and bits <7..0> describe the conversion control codes that
 take effect one conversion in the future, at time t+1. The conversion
 code is listed in the following table.

| Bits | Field |
| --- | --- |
| 7..3 | Reserved |
| 2..0 | Channel number |

For example, the scan list entry 0x0000000102 indicates this scan stores at address 1, and
 the next conversion is channel 2.

| Index | Sub | Type | Value |
| --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | 9 |
| 1 | 8 |  |  |
| 2 | 0x0000 \| 0x01 |  |  |
| 3 | 0x0100 \| 0x02 |  |  |
| ... | ... |  |  |
| 9 | 0x0700 \| 0x00 |  |  |

#### NI-9216/9226 Calibration Data

The NI-9216/9226 has eight RTD channels that can measure 100 Ω/1000 Ω RTD in 3-wire and 4-wire mode. There is a 1 mA excitation current source per channel for NI-9216 and 0.1 mA excitation
 current source per channel for NI-9226. The resistance range
 specified in the manual is 0 Ω to 400 Ω for NI-9216 and 0
 Ω to 4000 Ω for NI-9226. This range is tested and covers the temperature range of -200 ºC to 850 ºC for the
 standard platinum RTD. The channel does not read negative resistance.

Each channel has an associated LSB weight, which is the number of ohms per bit, and an
 offset, which is the number of ohms per bit measured when the inputs are grounded.

Note

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | pΩ/LSB |
| Offset | Signed | mΩ |

Use the calibration coefficients with the following equation to generate corrected data:

Figure 13.

R

c

o

r

r

e

c

t

e

d

⁢

(

R

r

a

w

)

=

R

r

a

w

(

bits

)

×

{

LSB

weight

(

p

Ω

bits

)

×

10

−

12

(

Ω

p

Ω

)

}

−

Offset

(

µ

Ω

)

×

10

−

6

(

Ω

µ

Ω

)

R

c

o

r

r

e

c

t

e

d

⁢

(

R

r

a

w

)

=

R

r

a

w

(

bits

)

×

{

LSB

weight

(

p

Ω

bits

)

×

10

−

12

(

Ω

p

Ω

)

}

−

Offset

(

µ

Ω

)

×

10

−

6

(

Ω

µ

Ω

)

where R<sub>raw</sub> represents data returned by the NI-9216/9226 in bits and R<sub>corrected</sub> represents calibrated resistance
 reading.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9217-extensions.html language=enus -->
## TOPIC 00013: NI-9217 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9217-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9217-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9217. NI-9217 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 ARR:U32 - Scan List = 5 1 R Channels to Convert = <1..4>, default = 4 2..5 R/W Channel Code 0x2002 0 U32 R/W Conversion Speed Control = 2 or

### NI-9217 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9217.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | - | Scan List = 5 |
| 1 | R | Channels to Convert = <1..4>, default = 4 |  |  |
| 2..5 | R/W | Channel Code |  |  |
| 0x2002 | 0 | U32 | R/W | Conversion Speed Control = 2 or 31, default = 31 |
| 0x2100 | 0 | ARR:U32 | - | Calibration = 16 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | - | - |  |  |
| 8 | R | Ch3 Gain |  |  |
| 9 | R | External Ch0 Offset |  |  |
| ... | - | - |  |  |

#### NI-9217 Conversion Speed Control

The NI-9217 converts at two pre-defined rates, as specified in the Speed Control field.

Note

| Speed Control | Meaning | Conversion Rate |
| --- | --- | --- |
| 31 (0x1F) | High Accuracy | 200 ms/channel (800 ms total) |
| 2 (0x02) | High Speed | 2.5 ms/channel (10 ms total) |

#### NI-9217 Scan List

The scan list channel codes consist of eight bit fields in a 32-bit entry.

| Bits | Field |
| --- | --- |
| 31..16 | Reserved |
| 15..8 | Data Offset[t] |
| 7..0 | Convert Code [t+1] |

Bits <15..8> describe the data offset to store a conversion at time
 t, and bits <7..0> describe the conversion control codes that
 take effect one conversion in the future, at time t+1. The conversion
 code is listed in the following table.

| Bits | Field |
| --- | --- |
| 7..3 | Conversion rate: 0b11111 = 31, High-Accuracy 0b00010 = 2, High-Speed |
| 2..1 | Channel number |
| 0 | Reserved |

Note

For example, the scan list entry 0x00000001FC indicates this scan stores at address 1, and
 the next conversion is channel 2 at high accuracy.

| Index | Sub | Type | Value |
| --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | 5 |
| 1 | 4 |  |  |
| 2 | 0x0000 \| 0xF8 \| 0x02 |  |  |
| 3 | 0x0100 \| 0xF8 \| 0x04 |  |  |
| 4 | 0x0200 \| 0xF8 \| 0x06 |  |  |
| 5 | 0x0300 \| 0xF8 \| 0x00 |  |  |

#### NI-9217 Calibration Data

The NI-9217 has four RTD channels that can measure 100 Ω RTD in 3-wire and 4-wire mode. There is a 1 mA excitation current source per channel and the module range
 is -500 Ω to 500 Ω. The
 resistance range specified in the manual is 0 Ω to 400 Ω. This range is tested and covers the temperature range of
 -200 ºC to 850 ºC for the
 standard platinum RTD. The channel does not read negative resistance.

Each channel has an associated LSB weight, which is the number of ohms per bit, and an
 offset, which is the number of ohms per bit measured when the inputs are grounded.

Note

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | pΩ/LSB |
| Offset | Signed | mΩ |

Use the calibration coefficients with the following equation to generate corrected data:

Figure 14.

R

c

o

r

r

e

c

t

e

d

⁢

(

R

r

a

w

)

=

R

r

a

w

(

bits

)

×

{

LSB

weight

(

p

Ω

bits

)

×

10

−

12

(

Ω

p

Ω

)

}

−

Offset

(

µ

Ω

)

×

10

−

6

(

Ω

µ

Ω

)

R

c

o

r

r

e

c

t

e

d

⁢

(

R

r

a

w

)

=

R

r

a

w

(

bits

)

×

{

LSB

weight

(

p

Ω

bits

)

×

10

−

12

(

Ω

p

Ω

)

}

−

Offset

(

µ

Ω

)

×

10

−

6

(

Ω

µ

Ω

)

where R<sub>raw</sub> represents data returned by the NI-9217 in bits and R<sub>corrected</sub> represents calibrated resistance reading.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9218-extensions.html language=enus -->
## TOPIC 00014: NI-9218 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9218-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9218-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9218. NI-9218 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R/W Configure Module, default = 0x00010106 0x2100 0 ARR:U32 — Calibration = 48 1 R Ch0 60 V Gain 2 R Ch0 16 V Offset 3 R Ch0 16 V Gain 4

### NI-9218 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9218.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R/W | Configure Module, default = 0x00010106 |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 48 |
| 1 | R | Ch0 60 V Gain |  |  |
| 2 | R | Ch0 16 V Offset |  |  |
| 3 | R | Ch0 16 V Gain |  |  |
| 4 | R | Ch0 60 mV Offset |  |  |
| 5 | R | Ch0 60 mV Gain |  |  |
| 6 | R | Ch0 5 V Offset |  |  |
| 7 | R | Ch0 5 V Gain |  |  |
| 8 | R | Ch0 20 mA Offset |  |  |
| 9 | R | Ch0 20 mA Gain |  |  |
| 10 | R | Ch0 22 mV/V Offset |  |  |
| 11 | R | Ch0 22 mV/V Gain |  |  |
| 12 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

#### NI-9218 Configuration Mode

This module is set to maximum speed and configured for full-bridge mode for all channels by
 default.

| Bits | Field | Description |
| --- | --- | --- |
| 31..22 | Reserved | — |
| 21 | Offset Cal Enable <ch1> | Controls the offset calibration mode. Offset calibration mode disconnects both signal input pins and forces the channel inputs to zero volts, enabling measurement of the channel offset voltage. A logic 1 in any bit enables offset calibration for the channel, while a logic 0 disables the offset calibration. |
| 20 | Shunt Cal Enable <ch1> | Controls the shunt calibration switch for each of the two channels. A logic 1 in any bit closes the switch for the respective channel, while a logic 0 opens the switch. |
| 19..16 | Module Mode Setting <ch1> | Saves the module mode calibration information for the channel. |
| 15..14 | Reserved | — |
| 13 | Offset Cal Enable <ch0> | Controls the offset calibration mode. Offset calibration mode disconnects both signal input pins and forces the channel inputs to zero volts, enabling measurement of the channel offset voltage. A logic 1 in any bit enables offset calibration for the channel, while a logic 0 disables the offset calibration. |
| 12 | Shunt Cal Enable <ch0> | Controls the shunt calibration switch for each of the two channels. A logic 1 in any bit closes the switch for the respective channel, while a logic 0 opens the switch. |
| 11..8 | Module Mode Setting <ch0> | Saves the module mode calibration information for the channel. |
| 7 | Reserved | — |
| 6..2 | Clock Divisor | The NI-9218 divides the clock source by this value and uses it as the oversample clock of the converter. The data rate is equal to 1/256 times this oversample clock frequency. |
| 1..0 | Clock Source | — |

This module has the following modes for each channel.

| Mode | Index |
| --- | --- |
| 16 V | 1 |
| 5 V | 2 |
| 16 V with Power Sensor | 3 |
| 60 V | 4 |
| 65 mV | 5 |
| 65 mV with Power Sensor | 6 |
| 20 mA | 7 |
| 20 mA with Power Sensor | 8 |
| 22 mV/V Bridge, 2 V Ex. | 9 |
| 22 mV/V Bridge, 3.3 V Ex. | 10 |

#### NI-9218 Example Data Rates

Example data rates use a 13.1072 MHz clock source.

| Data Rate | Clock Divisor | Clock Source | Oversample Clock Rate |
| --- | --- | --- | --- |
| 51.2 kS/s | 1 | 10 | 13.1072 MHz |
| 25.6 kS/s | 2 | 10 | 6.5536 MHz |
| 17.067 kS/s | 3 | 10 | 4.3691 MHz |
| ... | ... | ... | ... |
| 1.652 kS/s | 31 | 10 | 422.8129 kHz |

#### NI-9218 Calibration Data

The NI-9218 has two channels. Each channel has an associated
 LSB weight, which is the number of volts per bit, and an offset, which is the number of
 volts per bit measured when the inputs are grounded.

Note

The following table shows the scan list format for each mode.

| Coefficient | Representation | Units |
| --- | --- | --- |
| 60 V LSB Weight | Unsigned | pV/LSB |
| 60 V Offset | Signed | nV |
| 16 V LSB Weight | Unsigned | pV/LSB |
| 16 V Offset | Signed | nV |
| 65 mV LSB Weight | Unsigned | fV/LSB |
| 65 mV Offset | Signed | nV |
| 5 V LSB Weight | Unsigned | pV/LSB |
| 5 V Offset | Signed | nV |
| 20 mA LSB Weight | Unsigned | fA/LSB |
| 20 mA Offset | Signed | nV |
| 22 mV/V LSB Weight | Unsigned | fV/V/LSB |
| 22 mV/V Offset | Signed | nV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 15.

y

=

m

x

−

b

y

=

m

x

−

b

- y represents the calibrated data for the voltage, current, or bridge
- m represents the ADC data
- x represents raw data for the voltage, current, or bridge
- b represents the offset value

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9219-extensions.html language=enus -->
## TOPIC 00015: NI-9219 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9219-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9219-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9219. NI-9219 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 ARR:U32 — Command List = 33 1 R Command Count = <1..32>, default = 32 2..33 R/W Configuration Command 0x2002 1 ARR:U32 R Error Status 0x2005

### NI-9219 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9219.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | ARR:U32 | — | Command List = 33 |
| 1 | R | Command Count = <1..32>, default = 32 |  |  |
| 2..33 | R/W | Configuration Command |  |  |
| 0x2002 | 1 | ARR:U32 | R | Error Status |
| 0x2005 | 0 | U32 | R/W | ADC Format |
| 0x2100 | 0 | ARR:U32 |  | Calibration = 168 |
| 1 | R | Ch0 60 V Offset |  |  |
| 2 | R | Ch0 60 V Gain |  |  |
| 3 | R | Ch0 15 V Offset |  |  |
| ... | — | — |  |  |
| 42 | R | Ch0 Full-Bridge 7.8 mV/V Gain |  |  |
| 43 | R | Ch1 60 V Offset |  |  |
| ... | — | — |  |  |
| 0x2101 | 0 | ARR:U32 |  | External Calibration = 168 |
| 1 | — | R | Ch0 60 V Offset |  |
| ... | ... | ... | ... | ... |

#### NI-9219 ADC Format

The NI-9219 converts at different rates, and can specify different data formatting styles.
 This is determined by both the ADC Format field and corresponding fields in the setup
 commands. The following table describes the ADC Format field.

| Bits | Field |
| --- | --- |
| 31..24 | Reserved |
| 23..16 | Conversion speed in multiples of 10 mS |
| 15..8 | Reserved |
| 7..0 | ADC Data Formatting |

Standard values for ADC Format are:

- 0x0001000F, High Speed
- 0x000B000F, Best 60
 Hz rejection
- 0x000D000F, Best 50
 Hz rejection
- 0x0032000F, High Resolution

#### NI-9219 Error Status

Caution

When a channel over-current condition occurs on any of the channels of the NI-9219 (such as, configure channels in 4-wire resistance mode
 and do not connect a resistor to the channel), the firmware sets a bit in the lower nibble
 indicating the presence of this condition (LSB = ch0).

Errors are internally acknowledged on the cycle after the error is reported.

#### NI-9219 Calibration Data

The NI-9219 has four channels which each have 21 different
 operating modes and ranges. Each channel has an associated LSB weight, which is the number
 of volts per bit, and an offset, which is the number of volts per bit measured when the
 inputs are grounded.

Note

The following table lists the operating modes and ranges, in the order they are defined in
 the calibration table for each channel.

| Entry Number | Mode | Range |
| --- | --- | --- |
| 1 | Voltage | ±60 V |
| 2 | ±15 V |  |
| 3 | ±4 V |  |
| 4 | ±1 V |  |
| 5 | ±125 mV |  |
| 6 | Current | ±25 mA |
| 7 | 4-Wire Resistance | 10 kΩ |
| 8 | 1 kΩ |  |
| 9 | 2-Wire Resistance | 10 kΩ |
| 10 | 1 kΩ |  |
| 11 | Thermocouple | — |
| 12 | 4-Wire RTD | Pt1000 |
| 13 | Pt100 |  |
| 14 | 3-Wire RTD | Pt1000 |
| 15 | Pt100 |  |
| 16 | Quarter-Bridge | 350 Ω |
| 17 | 120 Ω |  |
| 18 | Half-Bridge | ±500 mV/V |
| 19 | Reserved | — |
| 20 | Full-Bridge | ±62.5 mV/V |
| 21 | ±7.8 mV/V |  |

The calibration data is stored in a U32 array, though each offset field should be
 interpreted as a signed value.

| Coefficient | Representation |
| --- | --- |
| LSB Weight | Unsigned |
| Offset | Signed |

The NI-9219 returns calibrated 24-bit (padded to 32-bits) AI
 data for all modes and ranges.

Use the following formula to convert raw data into engineering units.

Figure 16.

y

=

m

x

+

b

y

=

m

x

+

b

where b represents offset based on range of the device: such as, -60 for ±60 V voltage measurement range and m represents gain
 full-range/(2<sup>24</sup>): such as, 120/(2<sup>24</sup>) for ±60 V voltage measurement range.

#### NI-9219 Configuration Commands

There are eight configuration commands for the NI-9219.
 Eight configuration commands must be sent for each of the four channels, even if you are
 only using a subset of the four channels. Each of the eight configuration commands is 1
 Byte. Each configuration command is followed by a data Byte, then by a CRC value, which is 1
 Byte. Therefore, 3 Bytes × 8 commands × 4 channels = 96 command bytes (held in 32 entries in
 the object dictionary).

Data in the object dictionary is held in LSB format, so the value 0x12345678 is represented
 in memory as the series of bytes 0x78, 0x56, 0x34, 0x12. The following table shows the
 command word format.

| Bits | Field |
| --- | --- |
| 31..24 | Reserved |
| 23..16 | CRC |
| 15..8 | Configuration Data |
| 7..0 | Configuration Command |

NI-9219 CRC Calculation

```text
U8 crcShiftReg = 0;
   for ( x = 0 ; x < 8 ; ++x )
   {
      dataBool = ((0x80>>x) & configCommand) != 0;
      shiftBool = (0x01 & crcShiftReg) != 0;
      crcShiftReg /= 2;
      if (dataBool != shiftBool)
         crcShiftReg ^= 0x8C;
   }
   for ( x = 0 ; x < 8 ; ++x )
   {
dataBool = ((0x80>>x) & configData) != 0;
      shiftBool = (0x01 & crcShiftReg) != 0;
      crcShiftReg /= 2; 
      if (dataBool != shiftBool) 
         crcShiftReg ^= 0x8C;
   }
   crcShiftReg = crcShiftReg << 1;
   return crcShiftReg;
```

NI-9219 Configuration Command

You must configure the conversion time, mode, range, and calibration gain/offset values for
 each channel on the NI-9219, regardless of whether you are
 using that channel.

Note

| Bits | Field | Description |
| --- | --- | --- |
| 7..6 | Channel Number, <0..3> | — |
| 5 | 0 | — |
| 4..0 | Configuration Type | Configuration Type values: |
| Conversion Time | 0x1F |  |
| Mode & Range | 0x01 |  |
| Calibration Offset 2 (LSB) | 0x06 |  |
| Calibration Offset 1 | 0x05 |  |
| Calibration Offset 0 (MSB) | 0x04 |  |
| Calibration Gain 2 (LSB) | 0x0A |  |
| Calibration Gain 1 | 0x09 |  |
| Calibration Gain 0 (MSB) | 0x08 |  |

NI-9219 Configuration Data

| Configuration Value | Maximum Frequency | Conversion Time | Description |
| --- | --- | --- | --- |
| 0x01 | 100 Hz/50 Hz (TC) | 10 ms/20 ms (TC) | High Speed |
| 0x08 | 9.09 Hz/8.33 Hz (TC) | 110 ms/120 ms (TC) | Best 60 Hz Rejection |
| 0x09 | 7.69 Hz/7.14 Hz (TC) | 130 ms/140 ms (TC) | Best 50 Hz Rejection |
| 0x0F | 2 Hz/1.96 Hz (TC) | 500 ms/510 ms (TC) | High Resolution |

Note

10 ms

| Configuration Value | Mode | Range |
| --- | --- | --- |
| 0x00 | Voltage | 60 V |
| 0x01 | 15 V |  |
| 0x02 | 3.75 V |  |
| 0x03 | 1 V |  |
| 0x04 | 125 mV |  |
| 0x05 | Current | 25 mA |
| 0x06 | Resistance | 10K 4w |
| 0x07 | 1K 4w |  |
| 0x08 | 10K 2w |  |
| 0x09 | 1K 2w |  |
| 0x0A | TC | TC |
| 0x0B | RTD | Pt1000 4w |
| 0x0C | Pt100 4w |  |
| 0x0D | Pt1000 3w |  |
| 0x0E | Pt100 3w |  |
| 0x0F | Quarter-Bridge | 350 Ω |
| 0x10 | 120 Ω |  |
| 0x11 | Half-Bridge | 1 V/V |
| 0x13 | Full-Bridge CJC | 62.5 mV/V |
| 0x14 | 7.8 mV/V |  |
| 0x17 | CJC range |  |

NI-9219 Example Command Words Sequence

Note

Configuration 1: All Channels <ai0..ai3> for Voltage AI, ±15 V Range, High-Speed Mode (100 Hz Maximum Sample
 Rate).

| Command Byte Value | Description |
| --- | --- |
| 0x01 | Mode and Range Configuration Byte - Channel 0 |
| 0x01 | Data Byte |
| 0x46 | CRC value |
| 0x1F | Conversion Time - Channel 0 |
| 0x01 | Data Byte |
| 0xC6 | CRC value |
| 0x04 | Calibration Offset MSB - Channel 0 |
| 0x7F | Data Byte |
| 0x54 | CRC value |
| 0x05 | Calibration Offset Byte 2 - Channel 0 |
| 0xFF | Data Byte |
| 0xB6 | CRC value |
| 0x06 | Calibration Offset LSB - Channel 0 |
| 0x85 | Data Byte |
| 0x56 | CRC value |
| 0x08 | Calibration Gain MSB - Channel 0 |
| 0x6C | Data Byte |
| 0x1E | CRC value |
| 0x09 | Calibration Gain Byte 2 - Channel 0 |
| 0xAA | Data Byte |
| 0x4E | CRC value |
| 0x0A | Calibration Gain LSB - Channel 0 |
| 0xC1 | Data Byte |
| 0x32 | CRC value |
| 0x41 | Mode and Range Configuration Byte - Channel 1 |
| 0x01 | Data Byte |
| 0x64 | CRC value |
| 0x5F | Conversion Time - Channel 1 |
| 0x01 | Data Byte |
| 0xE4 | CRC value |
| 0x44 | Calibration Offset MSB - Channel 1 |
| 0x7F | Data Byte |
| 0x76 | CRC value |
| 0x45 | Calibration Offset Byte 2 - Channel 1 |
| 0xFF | Data Byte |
| 0x94 | CRC value |
| 0x46 | Calibration Offset LSB - Channel 1 |
| 0x86 | Data Byte |
| 0xE0 | CRC value |
| 0x48 | Calibration Gain MSB - Channel 1 |
| 0x6C | Data Byte |
| 0x3C | CRC value |
| 0x49 | Calibration Gain Byte 2 - Channel 1 |
| 0x76 | Data Byte |
| 0x50 | CRC value |
| 0x4A | Calibration Gain LSB - Channel 1 |
| 0x3C | Data Byte |
| 0xF6 | CRC value |
| 0x81 | Mode and Range Configuration Byte - Channel 2 |
| 0x01 | Data Byte |
| 0xCE | CRC value |
| 0x9F | Conversion Time - Channel 2 |
| 0x01 | Data Byte |
| 0x4E | CRC value |
| 0x84 | Calibration Offset MSB - Channel 2 |
| 0x7F | Data Byte |
| 0xDC | CRC value |
| 0x85 | Calibration Offset Byte 2 - Channel 2 |
| 0xFF | Data Byte |
| 0x3E | CRC value |
| 0x86 | Calibration Offset LSB - Channel 2 |
| 0xC8 | Data Byte |
| 0xC2 | CRC value |
| 0x88 | Calibration Gain MSB - Channel 2 |
| 0x6C | Data Byte |
| 0x96 | CRC value |
| 0x89 | Calibration Gain Byte 2 - Channel 2 |
| 0xB0 | Data Byte |
| 0xF4 | CRC value |
| 0x8A | Calibration Gain LSB - Channel 2 |
| 0x90 | Data Byte |
| 0x5E | CRC value |
| 0xC1 | Mode and Range Configuration Byte - Channel 3 |
| 0x01 | Data Byte |
| 0xEC | CRC value |
| 0xDF | Conversion Time - Channel 3 |
| 0x01 | Data Byte |
| 0x6C | CRC value |
| 0xC4 | Calibration Offset MSB - Channel 3 |
| 0x7F | Data Byte |
| 0xFE | CRC value |
| 0xC5 | Calibration Offset Byte 2 - Channel 3 |
| 0xFF | Data Byte |
| 0x1C | CRC value |
| 0xC6 | Calibration Offset LSB - Channel 3 |
| 0xD3 | Data Byte |
| 0xCA | CRC value |
| 0xC8 | Calibration Gain MSB - Channel 3 |
| 0x6C | Data Byte |
| 0xB4 | CRC value |
| 0xC9 | Calibration Gain Byte 2 - Channel 3 |
| 0xD8 | Data Byte |
| 0x56 | CRC value |
| 0xCA | Calibration Gain LSB - Channel 3 |
| 0x65 | Data Byte |
| 0xA0 | CRC value |

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9220-extensions.html language=enus -->
## TOPIC 00016: NI-9220 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9220-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9220-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9220. NI-9220 Vendor Configuration Extensions Index Sub Type R/W Description 0x2100 0 ARR:U32 — Calibration = 64 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset ... — — 32 R Ch16 Gain 33 R User Calibration Ch0 Offset ... — — NI-9220

### NI-9220 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9220.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 64 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 32 | R | Ch16 Gain |  |  |
| 33 | R | User Calibration Ch0 Offset |  |  |
| ... | — | — |  |  |

#### NI-9220 Calibration Data

The NI-9220 has 16 channels with a nominal range of ±10.5 V. Each channel has an associated LSB weight, which is
 the number of volts per bit, and an offset, which is the number of volts per bit measured
 when the inputs are grounded.

Note

The NI-9220 EEPROM stores these two constants for each channel. The host can then take
 these constants and adjust the raw data into calibrated data.

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | pV/LSB |
| Offset | Signed | nV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 17.

V

c

o

r

r

e

c

t

e

d

(

V

r

a

w

)

=

V

r

a

w

(

bits

)

×

{

LSB

w

e

i

g

h

t

(

pV

bits

)

×

10

−

12

(

V

pV

)

}

−

Offset

(

nV

)

×

10

−

9

(

V

nV

)

V

c

o

r

r

e

c

t

e

d

(

V

r

a

w

)

=

V

r

a

w

(

bits

)

×

{

LSB

w

e

i

g

h

t

(

pV

bits

)

×

10

−

12

(

V

pV

)

}

−

Offset

(

nV

)

×

10

−

9

(

V

nV

)

where V<sub>corrected</sub> represents the calibrated voltage value and V<sub>raw</sub>
 represents the raw data returned by the NI-9220 in bits.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9222-9223-extensions.html language=enus -->
## TOPIC 00017: NI-9222/9223 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9222-9223-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9222-9223-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9222/9223. NI-9222/9223 Vendor Configuration Extensions Index Sub Type R/W Description 0x2100 0 ARR:U32 — Calibration = 16 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset ... — — 8 R Ch3 Gain 9 R User Calibration Ch0 Offset ... — —

### NI-9222/9223 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9222/9223.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 16 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 8 | R | Ch3 Gain |  |  |
| 9 | R | User Calibration Ch0 Offset |  |  |
| ... | — | — |  |  |

#### NI-9222/9223 Calibration Data

The NI-9222/9223 has four channels with a nominal range of
 ±10.6 V. Each channel has an associated LSB weight, which
 is the number of volts per bit, and an offset, which is the number of volts per bit measured
 when the inputs are grounded.

Note

The NI-9222/9223 EEPROM stores these two constants for each
 channel. The host can then take these constants and adjust the raw data into calibrated
 data.

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | nV/LSB |
| Offset | Signed | nV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 18.

V

corrected

(

V

raw

)

=

V

r

a

w

(

bits

)

×

{

LSB

weight

(

nV

bits

)

×

10

−

9

(

V

nV

)

}

−

Offset

(

n

V

)

×

10

−

9

(

V

nV

)

V

corrected

(

V

raw

)

=

V

r

a

w

(

bits

)

×

{

LSB

weight

(

nV

bits

)

×

10

−

9

(

V

nV

)

}

−

Offset

(

n

V

)

×

10

−

9

(

V

nV

)

where V<sub>corrected</sub> represents the calibrated voltage value and V<sub>raw</sub>
 represents the raw data returned by the NI-9222/9223 in bits.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9225-extensions.html language=enus -->
## TOPIC 00018: NI-9225 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9225-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9225-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9225. NI-9225 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R/W Configure ADC, default = 0x0A 0x2100 0 ARR:U32 — Calibration = 12 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset ... — — 6 R Ch2 Gain 7 R

### NI-9225 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9225.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R/W | Configure ADC, default = 0x0A |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 12 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 6 | R | Ch2 Gain |  |  |
| 7 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

As a DSA module, the NI-9225 does not
 synchronize to other modules and free-runs at its own fixed rate.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9227-extensions.html language=enus -->
## TOPIC 00019: NI-9227 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9227-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9227-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9227. NI-9227 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R/W Configure ADC, default = 0x0A 0x2100 0 ARR:U32 — Calibration = 16 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset ... — — 8 R Ch3 Gain 9 R

### NI-9227 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9227.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R/W | Configure ADC, default = 0x0A |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 16 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 8 | R | Ch3 Gain |  |  |
| 9 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

As a DSA module, the NI-9227 does not synchronize to other modules and free-runs at its own
 fixed rate.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9229-9239-extensions.html language=enus -->
## TOPIC 00020: NI-9229/9239 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9229-9239-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9229-9239-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9229/9239. NI-9229/9239 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R/W Configure ADC, default = 0x06 0x2100 0 ARR:U32 — Calibration = 16 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset ... — — 8 R Ch

### NI-9229/9239 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9229/9239.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R/W | Configure ADC, default = 0x06 |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 16 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 8 | R | Ch3 Gain |  |  |
| 9 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

As a DSA module, the NI-9229/9239 does not synchronize to
 other modules and free-runs at its own fixed rate.

Note

NI-9229/9239

#### NI-9229/9239 Calibration Data

The NI-9229/9239 have four channels with nominal ranges of
 ±10 V and ±60 V
 respectively. Each channel has an associated LSB weight, which is the number of volts per
 bit, and an offset, which is the number of volts per bit measured when the inputs are
 grounded.

Note

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | pV/LSB |
| Offset | Signed | nV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 19.

V

corrected

=

Raw

×

(

LSB

weight

×

10

−

12

)

−

Offset

×

10

−

9

V

corrected

=

Raw

×

(

LSB

weight

×

10

−

12

)

−

Offset

×

10

−

9

where Raw represents raw data returned by the NI-9229/9239
 and V<sub>corrected</sub> represents the corrected voltage value.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9234-extensions.html language=enus -->
## TOPIC 00021: NI-9234 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9234-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9234-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9234. NI-9234 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R/W Configure Module, default = 0x06 0x2100 0 ARR:U32 — Calibration = 16 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch0 Offset ... — — 8 R Ch3 Gain

### NI-9234 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9234.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R/W | Configure Module, default = 0x06 |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 16 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch0 Offset |  |  |
| ... | — | — |  |  |
| 8 | R | Ch3 Gain |  |  |
| 9 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

As a DSA module, the NI-9234 does not synchronize to other
 modules and free-runs at its own fixed rate.

#### NI-9234 Configure Module

The NI-9234 has multiple configuration fields. Configuration
 bits <15..8> control the channel mode, while bits <7..0> set the conversion
 rate.

| Bits | Field | Description |
| --- | --- | --- |
| 15 | Ch3 IEPE | IEPE Enable 3: When set, the relays of the corresponding channel are switched to IEPE operation. IEPE operations switches the AC/DC relay to AC mode and enables the IEPE relay to send the current to the IEPE sensor. |
| 14 | Ch3 AC/~DC | AC/~DC 3: Controls the AC/DC relay when IEPE is not selected. If IEPE is enabled, then these bits have no meaning as AC mode is always selected with an IEPE operation. |
| 13 | Ch2 IEPE | IEPE Enable 2: When set, the realys of the corresponding channel are switched to IEPE operation. IEPE operations switches the AC/DC relay to AC mode and enables the IEPE relay to send the current to the IEPE sensor. |
| 12 | Ch2 AC/~DC | AC/~DC 2: Controls the AC/DC relay when IEPE is not selected. If IEPE is enabled, these bits have no meaning as AC mode is always selected with an IEPE operation. |
| 11 | Ch1 IEPE | IEPE Enable 1: When set, the relays of the corresponding channel are switched to IEPE operation. IEPE operations switches the AC/DC relay to AC mode and enables the IEPE relay to send the current to the IEPE sensor. |
| 10 | Ch1 AC/~DC | AC/~DC 1: Controls the AC/DC relay when IEPE is not selected. If IEPE is enabled, then these bits have no meaning as AC mode is always selected with an IEPE operation. |
| 9 | Ch0 IEPE | IEPE Enable 0: When set, the relays of the corresponding channel are switched to IEPE operation. IEPE operations switches the AC/DC relay to AC mode and enables the IEPE relay to send the current to the IEPE sensor. |
| 8 | Ch0 AC/~DC | AC/~DC 0: Controls the AC/DC relay when IEPE is not selected. If IEPE is enabled, then these bits have no meaning as AC mode is always selected with an IEPE operation. |
| 7 | Reserved | — |
| 6..2 | Clock Divisor | Clock Divisor: The NI-9234 divides the clock source (internal or external) by this value and uses it as the oversample clock of the converter. The data rate is equal to 1/256 times this oversample clock frequency. Valid values for Clock Divisor are from 1 to 31, and the final divided clock must be between 100 KHz and 12.8 MHz. |
| 1..0 | Clock Source | 0b00 = 0: The OCLK pin is used as the oversample clock source. 0b01 = 1: The 12.8 MHz internal clock is used as the clock source and this 12.8 MHz is driven onto the OCLK pin. 0b10 = 2: The internal clock is used but not driven onto OCLK pin. This is the required clock setting. 0b11 = 3: Reserved. |

#### NI-9234 Example Data Rates

The example data rates use a 12.8 MHz clock source.

| Data Rate | Clock Divisor | Clock Source | Rate Byte | Oversample Clock Rate |
| --- | --- | --- | --- | --- |
| 50.000 kS/s | 00001 | 10 | 0x06 | 12.80 MHz |
| 25.000 kS/s | 00010 | 10 | 0x0A | 6.40 MHz |
| 16.667 kS/s | 00011 | 10 | 0x0E | 4.27 MHz |
| 12.500 kS/s | 00100 | 10 | 0x12 | 3.20 MHz |
| 10.000 kS/s | 00101 | 10 | 0x16 | 2.56 MHz |
| 6.250 kS/s | 01000 | 10 | 0x22 | 1.60 MHz |
| 5.000 kS/s | 01010 | 10 | 0x2A | 1.28 MHz |

#### NI-9234 Calibration Data

The NI-9234 has four channels with a nominal range of ±5 V. Each channel has an associated AC or DC input mode; an
 optional IEPE excitation; an associated LSB weight, which is the number of volts per bit;
 and an offset, which is the volts per bit measured with the inputs grounded.

Note

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | pV/LSB |
| Offset | Signed | nV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 20.

V

corrected

(

V

raw

)

=

V

raw

(

bits

)

×

{

LSB

weight

(

pV

bits

)

×

10

−

12

(

V

pV

)

}

−

Offset

(

pV

)

×

−

9

10

(

V

nV

)

V

corrected

(

V

raw

)

=

V

raw

(

bits

)

×

{

LSB

weight

(

pV

bits

)

×

10

−

12

(

V

pV

)

}

−

Offset

(

pV

)

×

−

9

10

(

V

nV

)

where V<sub>raw</sub> represents data returned by the NI-9234 in bits and V<sub>corrected</sub> represents the corrected voltage value.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9235-extensions.html language=enus -->
## TOPIC 00022: NI-9235 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9235-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9235-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9235. NI-9235 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R/W Configure ADC, default = 0xCE00 0x2100 0 ARR:U32 - Calibration = 48 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch0 Shunt 4 R Ch1 Offset ... — —

### NI-9235 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9235.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R/W | Configure ADC, default = 0xCE00 |
| 0x2100 | 0 | ARR:U32 | - | Calibration = 48 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch0 Shunt |  |  |
| 4 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 24 | R | Ch7 Shunt |  |  |
| 25 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

The NI-9235 is a DSA module and as such does not synchronize
 with other modules but free-runs at its own fixed rate.

#### Configure ADC

The NI-9235 (like the other DSA modules) can convert at various rates, controlled by the
 fields in the ADC conversion command.

| Bits | Field | Description |
| --- | --- | --- |
| 15..10 | Clock Divisor | The clock source (internal or external) is divided by one half of this value and used as the oversample clock converter. Valid values are from 2 to 63, but the final divided clock must be between 502 kHz and 5.12 MHz. This means that only values from 5 to 51 (representing the divisors 2.5 to 25.5) are valid when using the 12.8 MHz internal clock source. |
| 9..8 | Clock Source | 0b00 = 0: The OCLK pin is used as the oversample clock source. 0b01 = 1: The 12.8 MHz internal clock is used as the clock source and this 12.8 MHz is driven onto the OCLK pin. 0b10 = 2: The internal clock is used but not driven onto OCLK pin. This is the required clock setting. 0b11 = 3: Reserved. |
| 7..0 | Shunt Cal Enable <ch7..ch0> | Controls the shunt calibration switch for each of the eight channels. A logic 1 in any bit closes the switch for the respective channel, while a logic 0 opens the switch. Refer to the following table for example data rates using a 12.8 MHz clock source (and using 0x00 in the shunt cal enable bits). |

| Data Rate | Clock Divisor | Clock Source | Configure ADC | Oversample Clock Rate |
| --- | --- | --- | --- | --- |
| 10.000 kS/s | 000101 | 10 | 0x1600 | 5.12 MHz |
| 8.333 kS/s | 000110 | 10 | 0x1A00 | 4.27 MHz |
| 7.143 kS/s | 000111 | 10 | 0x1E00 | 3.66 MHz |
| 2.500 kS/s | 010100 | 10 | 0x5200 | 1.28 MHz |
| 1.613 kS/s | 011111 | 10 | 0x7E00 | 825.8 kHz |
| 1.250 kS/s | 101000 | 10 | 0xA200 | 640.0 kHz |
| 0.980 kS/s | 110011 | 10 | 0xCE00 | 502.0 kHz |

#### NI-9235 Calibration Data

The NI-9235 has eight input channels for measuring strain.
 Each channel has an associated LSB weight, which is the number of volts per bit, and an
 offset, which is the number of volts per bit measured when the inputs are grounded.

Note

There is also a shunt measurement value which is not used during normal operation. The
 calibration data is stored in an U32 array, though each offset field (subindex 1, 4, 7,
 etc.) should be interpreted as a signed value.

| Coefficient | Representation |
| --- | --- |
| LSB Weight | Unsigned |
| Offset | Signed |
| Shunt | Signed |

The calibration coefficients are used with the following equation to generate corrected
 data.

Figure 21.

Nominal

(

V

V

)

=

Binary

Data

×

LSB

Weight

×

1

e

−

13

−

Offset

×

1

e

−

7

Nominal

(

V

V

)

=

Binary

Data

×

LSB

Weight

×

1

e

−

13

−

Offset

×

1

e

−

7

The resultant calibrated reading is a ratio between the bridge input voltage and the
 excitation voltage, termed V<sub>r</sub>. However, typical quarter-bridge measurements are
 denominated in strain, which require not only conversion in the strain equation, but also
 the acquisition and use of an unstrained measurement. The strain equation is:

Figure 22.

strain

(

e

)

=

−

4

(

V

r

−

st

−

V

r

−

unst

)

GF

⋅

[

(

1

+

2

)

⋅

(

V

r

−

st

−

V

r

−

u

n

s

t

)

]

strain

(

e

)

=

−

4

(

V

r

−

st

−

V

r

−

unst

)

GF

⋅

[

(

1

+

2

)

⋅

(

V

r

−

st

−

V

r

−

u

n

s

t

)

]

where V<sub>r – st</sub> and V<sub>r – unst</sub> are the strained and unstrained readings,
 respectively from the module.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9236-extensions.html language=enus -->
## TOPIC 00023: NI-9236 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9236-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9236-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9236. NI-9236 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R/W Configure ADC, default = 0xCE00 0x2100 0 ARR:U32 ... Calibration = 48 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch0 Shunt 4 R Ch1 Offset ... —

### NI-9236 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9236.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R/W | Configure ADC, default = 0xCE00 |
| 0x2100 | 0 | ARR:U32 | ... | Calibration = 48 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch0 Shunt |  |  |
| 4 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 24 | R | Ch7 Shunt |  |  |
| 25 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

The NI-9236 is a DSA module and as such it does not
 synchronize with other modules but free-runs at its own fixed rate.

#### Configure ADC

The NI-9236 (like the other DSA modules) can convert at various rates, controlled by the
 fields in the ADC conversion command.

| Bits | Field | Description |
| --- | --- | --- |
| 15..10 | Clock Divisor | The clock source (internal or external) is divided by one half of this value and used as the oversample clock of the converter. Valid values are from 2 to 63, but the final divided clock must be between 502 kHz and 5.12 MHz. This means that only values from 5 to 51 (representing the divisors 2.5 to 25.5) are valid when using the 12.8 MHz internal clock source. |
| 9..8 | Clock Source | 0b00 = 0: The OCLK pin is used as the oversample clock source. 0b01 = 1: The 12.8 MHz internal clock is used as the clock source and this 12.8 MHz is driven onto the OCLK pin. 0b10 = 2: The internal clock is used but not driven onto OCLK pin. This is the required clock setting. 0b11 = 3: Reserved. |
| 7..0 | Shunt Cal Enable <ch7..ch0> | Controls the shunt calibration switch for each of the eight channels. A logic 1 in any bit closes the switch for the respective channel, while a logic 0 opens the switch. |

| Data Rate | Clock Divisor | Clock Source | Configure ADC | Oversample Clock Rate |
| --- | --- | --- | --- | --- |
| 10.000 kS/s | 000101 | 10 | 0x1600 | 5.12 MHz |
| 8.333 kS/s | 000110 | 10 | 0x1A00 | 4.27 MHz |
| 7.143 kS/s | 000111 | 10 | 0x1E00 | 3.66 MHz |
| 2.500 kS/s | 010100 | 10 | 0x5200 | 1.28 MHz |
| 1.613 kS/s | 011111 | 10 | 0x7E00 | 825.8 kHz |
| 1.250 kS/s | 101000 | 10 | 0xA200 | 640.0 kHz |
| 0.980 kS/s | 110011 | 10 | 0xCE00 | 502.0 kHz |

#### NI-9236 Calibration Data

The NI-9236 has eight input channels for measuring strain. Each channel has an associated
 LSB weight, which is the number of volts per bit, and an offset, which is the number of
 volts per bit measured when the inputs are grounded.

Note

There is also a shunt measurement value which is not used during normal operation. The
 calibration data is stored in an U32 array, though each offset field (subindex 1, 4, 7, etc)
 should be interpreted as a signed value.

| Coefficient | Representation |
| --- | --- |
| LSB Weight | Unsigned |
| Offset | Signed |
| Shunt | Signed |

The calibration coefficients are used with the following equation to generate corrected
 data.

Figure 23.

Nominal

(

V

V

)

=

Binary

Data

×

LSB

Weight

×

1

e

−

13

−

Offset

×

1

e

−

7

Nominal

(

V

V

)

=

Binary

Data

×

LSB

Weight

×

1

e

−

13

−

Offset

×

1

e

−

7

The resultant calibrated reading is a ratio between the bridge input voltage and the
 excitation voltage, termed V<sub>r</sub>. However, typical quarter-bridge measurements are
 denominated in strain, which require not only conversion in the strain equation, but also
 the acquisition and use of an unstrained measurement. The strain equation is:

Figure 24.

strain

(

e

)

=

−

4

(

V

r

_

st

−

V

r

_

unst

)

GF

⋅

[

(

1

+

2

)

⋅

(

V

r

_

st

−

V

r

_

unst

)

]

strain

(

e

)

=

−

4

(

V

r

_

st

−

V

r

_

unst

)

GF

⋅

[

(

1

+

2

)

⋅

(

V

r

_

st

−

V

r

_

unst

)

]

where V<sub>r_st</sub> and V<sub>r_unst</sub> are the strained and unstrained readings,
 respectively from the module.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9237-extensions.html language=enus -->
## TOPIC 00024: NI-9237 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9237-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9237-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9237. NI-9237 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R/W Configure Module, default = 0x00060000 0x2100 0 ARR:U16 — Calibration = 16 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset ... — — 8 R Ch3

### NI-9237 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9237.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R/W | Configure Module, default = 0x00060000 |
| 0x2100 | 0 | ARR:U16 | — | Calibration = 16 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 8 | R | Ch3 Gain |  |  |
| 9 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

As a DSA module, the NI-9237 does not synchronize to other
 modules and free-runs at its own fixed rate.

#### NI-9237 Configure Module

This module is set to maximum speed and configured for full-bridge mode for all channels by
 default.

| Bits | Field | Description |
| --- | --- | --- |
| 31..23 | Reserved | — |
| 22..18 | Clock Divisor | The NI-9237 divides the clock source (internal or external) by this value and uses it as the oversample clock of the converter. The data rate is equal to 1/256 times this oversample clock frequency. The final data rate must be between 391 kS/s and 52.734 kS/s. This means that while all values from 1 to 31 are within the specified operating range when using the 12.8 MHz internal clock source, for external clock sources of more than 13.5 MHz or less than 3.1 MHz the valid divisors are limited to those that provide data rates within the specified range. |
| 17..16 | Clock Source | — |
| 15..12 | Shunt Cal Enable <ch3..ch0> | Controls the shunt calibration switch for each of the four channels. A logic 1 in any bit closes the switch for the respective channel, while a logic 0 opens the switch. |
| 11..8 | Half-Bridge Enable <ch3..ch0> | Controls the half-bridge completion option for each channel. Enabling half-bridge completion for a channel disconnects the negative signal input pin from the rest of the circuit, and uses an internal voltage equal to the midpoint of the excitation voltage as the negative input to the rest of the circuit. A logic 1 in any bit enables half-bridge completion for the respective channel, while a logic 0 disables it. |
| 7 | Reserved | — |
| 6..4 | Excitation | Sets the excitation voltage setting. All channels share the same excitation voltage. 0b000 = 0: 2.5 V, The OCLK pin is used as the oversample clock source. 0b001 = 1: 3.3 V, The 12.8 MHz internal clock is used as the clock source and this 12.8 MHz is driven onto the OCLK pin. 0b010 = 2: 5.0 V, The internal clock is used but not driven onto OCLK pin. Currently, this is the required clock setting. 0b011 = 3: 10.0 V, Reserved. 0b1xx = 4..7: External Excitation. |
| 3..0 | Offset Cal Enable <ch3..ch0> | Controls the offset calibration mode. Offset calibration mode disconnects both signal input pins and forces the channel inputs to zero volts, enabling measurement of the channel offset voltage. A logic 1 in any bit enables offset calibration for the respective channel, while a logic 0 disables it. |

#### NI-9237 Example Data Rates

Example data rates use a 12.8 MHz clock source.

| Data Rate | Clock Divisor | Clock Source | Rate Byte | Oversample Clock Rate |
| --- | --- | --- | --- | --- |
| 50.000 kS/s | 00001 | 10 | 0x06 | 12.80 MHz |
| 25.000 kS/s | 00010 | 10 | 0x0A | 6.40 MHz |
| 16.667 kS/s | 00011 | 10 | 0x0E | 4.27 MHz |
| 12.500 kS/s | 00100 | 10 | 0x12 | 3.20 MHz |
| 10.000 kS/s | 00101 | 10 | 0x16 | 2.56 MHz |
| 6.250 kS/s | 01000 | 10 | 0x22 | 1.60 MHz |
| 5.000 kS/s | 01010 | 10 | 0x2A | 1.28 MHz |
| 3.333 kS/s | 01111 | 10 | 0x3E | 853.3 KHz |
| 2.500 kS/s | 10100 | 10 | 0x52 | 640.0 KHz |
| 2.000 kS/s | 11001 | 10 | 0x66 | 512.0 KHz |

#### NI-9237 Calibration Data

The NI-9237 has four channels. Each channel has an
 associated LSB weight, which is the number of volts per bit, and an offset, which is the
 number of volts per bit measured when the inputs are grounded.

Note

The calibration data is stored in a U16 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | 0.1 pV/LSB |
| Offset | Signed | 10 nV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 25.

V

corrected

(

V

raw

)

=

V

raw

(

bits

)

×

{

LSB

weight

(

pV

bits

)

×

10

−

13

(

V

pV

)

}

−

Offset

(

nV

)

×

−

8

10

(

V

nV

)

V

corrected

(

V

raw

)

=

V

raw

(

bits

)

×

{

LSB

weight

(

pV

bits

)

×

10

−

13

(

V

pV

)

}

−

Offset

(

nV

)

×

−

8

10

(

V

nV

)

where V<sub>raw</sub> represents data returned by the NI-9237 in bits and V<sub>corrected</sub> represents the corrected voltage value.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9242-9244-extensions.html language=enus -->
## TOPIC 00025: NI-9242/9244 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9242-9244-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9242-9244-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9242/9244. NI-9242/9244 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R/W Configure ADC, default = 0x6 0x2100 0 ARR:U16 — Calibration = 16 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset ... — — 8 R Ch3

### NI-9242/9244 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9242/9244.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R/W | Configure ADC, default = 0x6 |
| 0x2100 | 0 | ARR:U16 | — | Calibration = 16 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 8 | R | Ch3 Gain |  |  |
| 9 | R | User Calibration Ch0 Offset |  |  |
| ... | — | — |  |  |

As a DSA module, the NI-9242/9244 does not synchronize to
 other modules and free-runs at its own fixed rate.

#### NI-9242/9244 Configure ADC

The NI-9242/9244 converts at various rates, controlled by
 the field in the ADC conversion command.

| Bits | Field | Description |
| --- | --- | --- |
| 7 | Reserved | — |
| 6..2 | Clock Divisor | The NI-9242/9244 divides the clock source by this value and uses it as the oversample clock of the converter. The data rate is equal to 1/256 times this oversample clock frequency. Valid values for Clock Divisor are from 1 to 31. |
| 1..0 | Clock Source = 2 | 0b00 = 0: The OCLK pin is used as the oversample clock source. 0b01 = 1: The 12.8 MHz internal clock is used as the clock source and this 12.8 MHz is driven onto the OCLK pin. 0b10 = 2: The internal clock is used but not driven onto OCLK pin. Currently, this is the required clock setting. 0b11 = 3: Reserved. |

#### NI-9242/9244 Example Data Rates

The following table lists the example data rates for the NI-9242/9244. These example data rates use a 12.8 MHz
 clock source.

| Data Rate | Clock Divisor | Clock Source | Rate Byte | Oversample Clock Rate |
| --- | --- | --- | --- | --- |
| 50.000 kS/s | 00001 | 10 | 0x06 | 12.80 MHz |
| 25.000 kS/s | 00010 | 10 | 0x0A | 6.40 MHz |
| 12.500 kS/s | 00100 | 10 | 0x12 | 3.20 MHz |
| 10.000 kS/s | 00101 | 10 | 0x16 | 2.56 MHz |
| 6.250 kS/s | 01000 | 10 | 0x22 | 1.60 MHz |
| 5.000 kS/s | 01010 | 10 | 0x2A | 1.28 MHz |
| 3.333 kS/s | 01111 | 10 | 0x3E | 853 KHz |
| 3.125 kS/s | 10000 | 10 | 0x42 | 800 KHz |
| 2.500 kS/s | 10100 | 10 | 0x52 | 640 KHz |
| 2.000 kS/s | 11001 | 10 | 0x66 | 512 KHz |

#### NI-9242/9244 Calibration Data

The NI-9242/9244 have four channels with nominal ranges of
 ±500 V and ±997.5 V
 respectively. Calibration data is set up by the driver during initialization. The
 calibration conversion is performed on the module ADC itself, by applying the gain and
 offset constants in the following equation. You do not need to check the index 0x2100 to
 calibrate the data manually.

Figure 26.

y

⁢

=

m

x

−

b

y

⁢

=

m

x

−

b

- y represents the calibrated ADC codes
- m represents the gain value
- x represents ADC data
- b represents the offset value

Use the following equation to scale the calibrated ADC codes into voltages for NI-9242.

Figure 27.

V

corrected

=

V

raw

(

bits

)

×

59605

(

nV

bits

)

×

10

−

9

(

V

nV

)

V

corrected

=

V

raw

(

bits

)

×

59605

(

nV

bits

)

×

10

−

9

(

V

nV

)

Use the following equation to scale the calibrated ADC codes into voltages for NI-9244.

Figure 28.

V

corrected

=

V

raw

(

bits

)

×

118911

(

nV

bits

)

×

10

−

9

(

V

nV

)

V

corrected

=

V

raw

(

bits

)

×

118911

(

nV

bits

)

×

10

−

9

(

V

nV

)

where V<sub>corrected</sub> represents the calibrated voltage value and V<sub>raw</sub>
 represents the data returned by the NI-9242/9244 in bits.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9263-extensions.html language=enus -->
## TOPIC 00026: NI-9263 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9263-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9263-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9263. NI-9263 Vendor Configuration Extensions Index Sub Type R/W Description 0x2100 0 ARR:U32 — Calibration = 16 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset ... — — 8 R Ch3 Gain 9 R External Ch0 Offset ... — — NI-9263 Calibratio

### NI-9263 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9263.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 16 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 8 | R | Ch3 Gain |  |  |
| 9 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

#### NI-9263 Calibration Data

The NI-9263 has four channels with a nominal range of ±10.7 V. Each channel has an associated LSB weight, which is
 the number of volts per bit, and an offset, which is the number of volts per bit measured
 when the inputs are grounded.

Note

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | nV/LSB |
| Offset | Signed | nV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 33.

V

desired

(

Code

)

=

Code

×

LSB

weight

(

nV

bits

)

×

10

−

9

(

V

nV

)

+

Offset

(

nV

)

×

−

9

10

(

V

nV

)

V

desired

(

Code

)

=

Code

×

LSB

weight

(

nV

bits

)

×

10

−

9

(

V

nV

)

+

Offset

(

nV

)

×

−

9

10

(

V

nV

)

where Code represents the code returned by the NI-9263 and
 V<sub>desired</sub> represents the corrected voltage value.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9264-extensions.html language=enus -->
## TOPIC 00027: NI-9264 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9264-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9264-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9264. NI-9264 Vendor Configuration Extensions Index Sub Type R/W Description 0x2100 0 ARR:U32 — Calibration = 64 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset ... — — 32 R Ch16 33 R External Ch0 Offset ... — — NI-9264 Calibration

### NI-9264 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9264.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 64 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 32 | R | Ch16 |  |  |
| 33 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

#### NI-9264 Calibration Data

The NI-9264 has 16 channels with a nominal range of ±10.5 V. Each channel has an associated LSB weight, which is
 the number of volts per bit, and an offset, which is the number of volts per bit measured
 when the inputs are grounded.

Note

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | pV/LSB |
| Offset | Signed | nV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 33.

V

desired

(

Code

)

=

Code

×

LSB

weight

(

nV

bits

)

×

10

−

9

(

V

nV

)

+

Offset

(

nV

)

×

10

−

9

(

V

nV

)

V

desired

(

Code

)

=

Code

×

LSB

weight

(

nV

bits

)

×

10

−

9

(

V

nV

)

+

Offset

(

nV

)

×

10

−

9

(

V

nV

)

where Code represents the code returned by the NI-9264 and
 V<sub>desired</sub> represents the corrected voltage value.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9265-extensions.html language=enus -->
## TOPIC 00028: NI-9265 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9265-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9265-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9265. NI-9265 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R Error Status, sent as 8-bit PDO 0x2100 0 ARR:U32 — Calibration = 16 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset ... — — 8 R Ch3 Gain 9 R

### NI-9265 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9265.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R | Error Status, sent as 8-bit PDO |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 16 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 8 | R | Ch3 Gain |  |  |
| 9 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

#### NI-9265 Error Status

Each channel has open loop detection circuitry that reports an error whenever the load is
 disconnected and the current is set to a value higher than 0
 mA. On the cycle after the error is reported, it is (internally) automatically
 acknowledged.

#### NI-9265 Calibration Data

The NI-9265 has four channels with a nominal range of 0 mA to 20.675 mA. Each channel
 has an associated LSB weight, which is the number of amps per bit, and an offset, which is
 the number of amps per bit measured when the inputs are grounded.

Note

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | pA/LSB |
| Offset | Signed | pA |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 31.

I

desired

(

Code

)

=

C

o

d

e

×

LSB

w

e

i

g

h

t

(

pA

bits

)

×

10

−

12

(

A

pA

)

+

Offset

(

pA

)

×

10

−

12

(

A

pA

)

I

desired

(

Code

)

=

C

o

d

e

×

LSB

w

e

i

g

h

t

(

pA

bits

)

×

10

−

12

(

A

pA

)

+

Offset

(

pA

)

×

10

−

12

(

A

pA

)

where Code represents the code returned by the NI-9265 and
 I<sub>desired</sub> represents the corrected current value.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9266-extensions.html language=enus -->
## TOPIC 00029: NI-9266 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9266-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9266-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9266. NI-9266 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R Error Status, sent as 8-bit PDO 0x2100 0 ARR:U32 — Calibration = 32 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset 4 R Ch1 Gain ... — — 15

### NI-9266 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9266.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R | Error Status, sent as 8-bit PDO |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 32 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| 4 | R | Ch1 Gain |  |  |
| ... | — | — |  |  |
| 15 | R | Ch7 Offset |  |  |
| 16 | R | Ch7 Gain |  |  |
| 17 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

#### NI-9266 Error Status

Each channel has open loop detection circuitry that reports an error whenever the load is
 disconnected and the current is set to a value higher than 0
 mA. On the cycle after the error is reported, it is (internally) automatically
 acknowledged.

#### NI-9266 Calibration Data

The NI-9266 has eight channels with a nominal range of 0 mA to 20.8896 mA. Each channel
 has an associated LSB weight, which is the number of amps per bit, and an offset, which is
 the number of amps per bit measured when the inputs are grounded.

Note

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | pA/LSB |
| Offset | Signed | pA |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 32.

I

desired

(

Code

)

=

C

o

d

e

×

LSB

w

e

i

g

h

t

(

pA

bits

)

×

10

−

12

(

A

pA

)

+

Offset

(

pA

)

×

10

−

12

(

A

pA

)

I

desired

(

Code

)

=

C

o

d

e

×

LSB

w

e

i

g

h

t

(

pA

bits

)

×

10

−

12

(

A

pA

)

+

Offset

(

pA

)

×

10

−

12

(

A

pA

)

where Code represents the code returned by the NI-9266 and
 I<sub>desired</sub> represents the corrected current value.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9269-extensions.html language=enus -->
## TOPIC 00030: NI-9269 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9269-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9269-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9269. NI-9269 Vendor Configuration Extensions Index Sub Type R/W Description 0x2100 0 ARR:U32 — Calibration = 16 1 R Ch0 Offset 2 R Ch0 Gain 3 R Ch1 Offset ... — — 8 R Ch3 Gain 9 R External Ch0 Offset ... — — NI-9269 Calibratio

### NI-9269 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9269.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2100 | 0 | ARR:U32 | — | Calibration = 16 |
| 1 | R | Ch0 Offset |  |  |
| 2 | R | Ch0 Gain |  |  |
| 3 | R | Ch1 Offset |  |  |
| ... | — | — |  |  |
| 8 | R | Ch3 Gain |  |  |
| 9 | R | External Ch0 Offset |  |  |
| ... | — | — |  |  |

#### NI-9269 Calibration Data

The NI-9269 has four channels with a nominal range of ±10.7 V. Each channel has an associated LSB weight, which is
 the number of volts per bit, and an offset, which is the number of volts per bit measured
 when the inputs are grounded.

Note

The calibration data is stored in a U32 array, though each offset field (subindex 1, 3, 5,
 and so on) should be interpreted as a signed value.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | nV/LSB |
| Offset | Signed | nV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 33.

V

desired

(

Code

)

=

Code

×

LSB

weight

(

nV

bits

)

×

10

−

9

(

V

nV

)

+

Offset

(

nV

)

×

10

−

9

(

V

nV

)

V

desired

(

Code

)

=

Code

×

LSB

weight

(

nV

bits

)

×

10

−

9

(

V

nV

)

+

Offset

(

nV

)

×

10

−

9

(

V

nV

)

where Code represents the code returned by the NI-9269 and
 V<sub>desired</sub> represents the corrected current value.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9381-extensions.html language=enus -->
## TOPIC 00031: NI-9381 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9381-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9381-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9381. NI-9381 Vendor Configuration Extensions Index Sub Type R/W Description 0x2100 0 U32 R/W Digital Channel Direction Control, default = 0 0 ARR:U16 — Calibration = 64 1 R AI0 Offset 2 R AI0 Gain ... — — 15 R AI7 Offset 16 R

### NI-9381
 Vendor Configuration Extensions

The following table lists the vendor configuration extensions for the NI-9381.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2100 | 0 | U32 | R/W | Digital Channel Direction Control, default = 0 |
| 0 | ARR:U16 | — | Calibration = 64 |  |
| 1 | R | AI0 Offset |  |  |
| 2 | R | AI0 Gain |  |  |
| ... | — | — |  |  |
| 15 | R | AI7 Offset |  |  |
| 16 | R | AI7 Gain |  |  |
| 17 | R | AO0 Offset |  |  |
| 18 | R | AO0 Gain |  |  |
| ... | — | — |  |  |
| 31 | R | AO7 Offset |  |  |
| 32 | R | AO7 Gain |  |  |
| 33 | R | External AI0 Offset |  |  |
| ... | — | — |  |  |

#### NI-9381 Calibration Data

The NI-9381 has either input channels or output channels
 with a nominal range of 0 V to 5
 V. Each channel has an associated LSB weight, which is the number of volts per bit,
 and an offset, which is the number of volts per bit measured when the inputs are grounded.

Note

The NI-9381 EEPROM stores two constants for each channel.
 The host takes the constants and adjusts the raw data in calibrated data. The calibration
 data is stored in a U16 array.

| Coefficient | Representation | Units |
| --- | --- | --- |
| LSB Weight | Unsigned | 100 nV/LSB |
| Offset | Signed | 10 µV |

Use the calibration coefficients with the following equation to generate corrected data.

Figure 34.

V

corrected

=

Raw

⁢

×

(

LSB

weight

×

10

−

7

)

+

Offset

×

10

−

5

V

corrected

=

Raw

⁢

×

(

LSB

weight

×

10

−

7

)

+

Offset

×

10

−

5

where Raw represents raw data returned by the NI-9381 and V<sub>corrected</sub> represents
 the corrected voltage value

#### NI-9381 Digital Channel Direction
 Control

| Bits | Field |
| --- | --- |
| 3 | 0: data bit as input 1: data bit as output |
| 2 |  |
| 1 |  |
| 0 |  |

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9401-extensions.html language=enus -->
## TOPIC 00032: NI-9401 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9401-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9401-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9401. NI-9401 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 U32 R/W Nibble direction control, default = 0 NI-9401 Direction Control NI-9401 Scan List Format Bits Field 1 0: data bits <3..0> as input 1:

### NI-9401 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9401.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | U32 | R/W | Nibble direction control, default = 0 |

#### NI-9401 Direction Control

| Bits | Field |
| --- | --- |
| 1 | 0: data bits <3..0> as input 1: data bits <7..4> as output |
| 0 |  |

Note

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9402-extensions.html language=enus -->
## TOPIC 00033: NI-9402 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9402-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9402-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9402. NI-9402 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 U32 R/W Line direction control, default = 0 NI-9402 Direction Control NI-9402 Scan List Format Bits Field 3 0: data bit as input 1: data bit

### NI-9402 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9402.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | U32 | R/W | Line direction control, default = 0 |

#### NI-9402 Direction Control

| Bits | Field |
| --- | --- |
| 3 | 0: data bit as input 1: data bit as output |
| 2 |  |
| 1 |  |
| 0 |  |

Note

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9403-extensions.html language=enus -->
## TOPIC 00034: NI-9403 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9403-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9403-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9403. NI-9403 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 U32 R/W I/O direction control, default = 0 NI-9403 Direction Control The direction control field has one bit for each I/O pin, with bit 0 mat

### NI-9403 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9403.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | U32 | R/W | I/O direction control, default = 0 |

#### NI-9403 Direction Control

The direction control field has one bit for each I/O pin, with bit 0 matching channel 0,
 and so forth. 0 in the direction control indicates that I/O is an input; 1 indicates an
 output.

Note

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9476-extensions.html language=enus -->
## TOPIC 00035: NI-9476 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9476-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9476-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9476. NI-9476 Vendor Configuration Extensions Index Sub Type R/W Description 0x2002 0 U32 R Error Status, sent as 8-bit PDO NI-9476 Error Status If a channel over-current occurs on any of the 32 channels, the corresponding bit

### NI-9476 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9476.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2002 | 0 | U32 | R | Error Status, sent as 8-bit PDO |

#### NI-9476 Error Status

If a channel over-current occurs on any of the 32 channels, the corresponding bit in error
 status field is set to inform the user.

Errors are automatically internally acknowledged on the cycle after the error is reported.

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=9478-extensions.html language=enus -->
## TOPIC 00036: NI-9478 Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `9478-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/9478-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the vendor configuration extensions for the NI-9478. NI-9478 Vendor Configuration Extensions Index Sub Type R/W Description 0x2001 0 U32 R/W Current Limit Select 0x2002 1 U32 R Error Status A, sent as 16-bit PDO 2 U32 R Error Status B, sent as 16-bit PDO 0x2003 1 U32 R Erro

### NI-9478 Vendor Configuration
 Extensions

The following table lists the vendor configuration extensions for the NI-9478.

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2001 | 0 | U32 | R/W | Current Limit Select |
| 0x2002 | 1 | U32 | R | Error Status A, sent as 16-bit PDO |
| 2 | U32 | R | Error Status B, sent as 16-bit PDO |  |
| 0x2003 | 1 | U32 | R | Error Overtemp, sent as 8-bit PDO |
| 0x2004 | 1 | U8 | R/W | Limit A |
| 2 | U8 | R/W | Limit B |  |
| 0x2005 | 0 | U8 | R/W | Refresh Period |

#### Current Limits and Selection

Each of the 15 channels has 2 bits represented in index 0x2001 Current Limit Select, with channel 0 controlled by bits 0 and 1.

#### NI-9478 Direction Control

| Bits | Field |
| --- | --- |
| 31..30 | 0: Limit A 1: Limit B 2: No Limit 3: (no charge) |
| 29..28 |  |
| ... |  |
| 1..0 |  |

The current limits are set in index 0x2002 sub-indices1 (Limit A) and 2 (Limit B). The
 current limits are 8-bit unsigned integers in increments of 20
 mA (1 = 20 mA, 2 = 40
 mA, and so on).

#### Error Status and Overtemp

The two error status fields each hold 16 bits of data (one bit per channel, with bit 0 for channel 0). The error status bits in 0x2002.1 are for Limit A reporting. Bits 0x2002.2 are for Limit B reporting.

Errors are reported for at least one cycle and are automatically cleared by the module when appropriate.

The Error Overtemperature field has seven bits to ignore and one bit (bit 0) that when set indicates that the module in an over-temperature condition.

| Bits | Field |
| --- | --- |
| 7..1 | Reserved |
| 0 | Overtemp |

#### Refresh Period

During the Refresh Period, output values that may have experienced an over-current condition are re-enabled. An eight byte value in 10 μs is listed in the following table.

| Value | Description |
| --- | --- |
| 0 | Infinity (no refresh) |
| 1 | Invalid value |
| 2..255 | 20 μs to 2,550 μs refresh period |

Parent topic:

Vendor Extensions to the Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=951x-extensions.html language=enus -->
## TOPIC 00037: NI-951x Vendor Configuration Extensions

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `951x-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/951x-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the NI 951x C Series Modules Object Dictionary, available on ni.com/docs, for NI-951xC Series drive interface module object dictionary entries.

### NI-951x Vendor Configuration
 Extensions

Refer to the *NI 951x C Series Modules Object Dictionary*, available on
 ni.com/docs, for NI-951*x*C Series drive interface module object dictionary entries.

Parent topic:

Vendor Extensions to the Object Dictionary

Related information:

- NI 951x C Series Modules Object Dictionary

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=ecat-configuration-guide.html language=enus -->
## TOPIC 00038: EtherCAT® Expansion Chassis Vendor Configurations Guide

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `ecat-configuration-guide.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/ecat-configuration-guide.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `concept`
- source_description: This document contains information about accessing all of the functionality of the C Series modules using vendor extensions to the object dictionary on the EtherCAT expansion chassis. Looking For Something Else? For information not found in this guide, browse Related Information.

### EtherCAT® Expansion Chassis Vendor
 Configurations Guide

This document contains information about accessing all of the functionality of the C Series modules using vendor extensions to the object dictionary on the EtherCAT expansion chassis.

#### Looking For Something Else?

For information
 not found in this guide, browse *Related Information*.

Related information:

- NI-9144 Getting Started
- NI-9144 Features
- NI-9144 Specifications
- NI-9145 Getting Started
- NI-9145 Specifications

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=modules-no-config.html language=enus -->
## TOPIC 00039: C Series Modules with No Configurable Options

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `modules-no-config.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/modules-no-config.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following C Series modules are supported with no configurable options. NI-9344 NI-9375 NI-9411 NI-9421 NI-9422 NI-9423 NI-9425 NI-9426 NI-9435 NI-9436 NI-9437 NI-9472 NI-9474 NI-9475 NI-9477 NI-9481 NI-9482 NI-9485

### C Series Modules with No Configurable Options

The following C Series modules are supported with no configurable options.

- NI-9344
- NI-9375
- NI-9411
- NI-9421
- NI-9422
- NI-9423
- NI-9425
- NI-9426
- NI-9435
- NI-9436
- NI-9437
- NI-9472
- NI-9474
- NI-9475
- NI-9477
- NI-9481
- NI-9482
- NI-9485

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=third-party-master.html language=enus -->
## TOPIC 00040: Using the Chassis with an EtherCAT Third-Party Master

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `third-party-master.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/third-party-master.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: When using a third-party master, you can access all of the functionality of the C Series modules using vendor extensions to the object dictionary. Each module installed in the chassis has its own object dictionary that you can use to configure the module. If your master software supports ADS over Et

### Using the Chassis with an EtherCAT
 Third-Party Master

When using a third-party master, you can access all of the functionality of the C Series modules using vendor extensions to the object
 dictionary. Each module installed in the chassis has its own object dictionary that you can
 use to configure the module.

If your master software supports ADS over EtherCAT (AoE) services, you can address the module directly. If your master software does not support AoE services, you can still configure your module using NI vendor extensions and CAN over EtherCAT (CoE).

#### Using AoE/SDO

AoE protocol allows you to specify the destination port or address of the SDO request. An
 address of 0 indicates the chassis. Addresses 1 through 8 route the SDO request to the
 object dictionary of the module in the addressed slot. If no module is installed in the
 addressed slot, the request fails. SDOInfo and SDO requests work with module object
 dictionaries over AoE similar to the chassis main object dictionary.

Tip

#### Using CoE/SDO

CoE protocol does not have a destination port or address. When using CoE protocol, the
 chassis provides an object dictionary entry that allows addressing support. Prior to sending
 an SDOInfo or SDO request, the application writes an address of 1 through 8 to the object
 dictionary index 0x5FFF, subindex 0. Once the address is written, SDO transactions are sent
 to the object dictionary of the module in the addressed slot. If no module is installed in
 the addressed slot, the request fails.

After the module-specific SDOInfo and SDO requests are complete, the application writes 0
 to the module object dictionary index 0x5FFF, subindex 0 to return control to the chassis
 main object dictionary.

<!--NI_TOPIC bundle=ni-9145-ethercat-expansion-chassis-configuration path=vendor-extensions.html language=enus -->
## TOPIC 00041: Vendor Extensions to the Object Dictionary

- bundle_id: `ni-9145-ethercat-expansion-chassis-configuration`
- source_path: `vendor-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-9145-ethercat-expansion-chassis-configuration/raw/resource/enus/vendor-extensions.html
- document_id: `ni-9145-ethercat-expansion-chassis-configuration`
- page_type: `leaf`
- content_type: `reference`
- source_description: Most object dictionary entries are defined by the EtherCAT and CANOpen specifications for modular slave devices. The chassis and the C Series modules have vendor extensions to those specifications. Refer to the NI 951x C Series Modules Object Dictionary, available on ni.com/docs, for NI-951xC Series

### Vendor Extensions to the Object Dictionary

Most object dictionary entries are defined by the EtherCAT and CANOpen specifications for
 modular slave devices. The chassis and the C Series modules
 have vendor extensions to those specifications.

Note

NI 951x C Series Modules Object
 Dictionary

ni.com/docs

x

C Series

Note

The following tabled list common C Series module vendor extensions.

Note

C Series

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x3001 | 0 | ARR:U32 | — | Timing overrides. Provides additional control over the timing of the chassis. |
| — | 1 | — | R/W | Minimum free-run cycle time in nanoseconds. Set to 0 to operate at the minimum cycle. Set to 1,000,000 for a 1 mS cycle (1 kHz). |
| — | 2 | — | R/W | Disables multiple scans. Setting the field to 1 disables multiple-scan ability, regardless of whether a module has enough time during the cycle to acquire more than one set of data. This is useful when analyzing the module acquisition timing. |
| 0x5FFF | 0 | U32 | R/W | Slot address override. Enter the slot number of the module to address CoE requests to the object dictionary of the module. Set to 0 to cancel the slot address override. |

| Index | Sub | Type | R/W | Description |
| --- | --- | --- | --- | --- |
| 0x2000 | 0 | U32 | R | C Series Vendor ID (For C Series modules, equals 0x1093) |
| 0x2001 | 0..N | ARR: | R/W | Scan or command list Channel direction control Mode selection |
| 0x2002 | 0 | U32 | R/W | Error status Unipolar/bipolar control Module configuration command Module conversion rate control |
| 0x2003 | 0 | U32 | R/W | Error acknowledgment or status |
| 0x2005 | 0 | U8 | R/W | Refresh period Conversion format |
| 0x2100 | 0..N | ARR: | R | Calibration data |
| 0x3002 | 0 | U32 | R | Number of scans. This index reports the number of conversions the module makes during the cycle. If disable multiple scans is selected, the number of scans is always 1. |
| 0x4000 … 0x47FF | — | — | R/W | Safe data values that mirror the PDO data in 0x6000…0x67FF. |
| 0x4800 … 0x4FFF | — | — | R/W | Safe control values that mirror the SDO data in 0x2000…0x27FF. |

- [NI-9201/9221 Vendor Configuration Extensions](9201-9221-extensions.html)
- [NI-9203 Vendor Configuration Extensions](9203-extensions.html)
- [NI-9205/9206 Vendor Configuration Extensions](9205-9206-extensions.html)
- [NI-9207 Vendor Configuration Extensions](9207-extensions.html)
- [NI-9208 Vendor Configuration Extensions](9208-externsions.html)
- [NI-9209 Vendor Configuration Extensions](9209-extensions.html)
- [NI-9211 Vendor Configuration Extensions](9211-extensions.html)
- [NI-9212 Vendor Configuration Extensions](9212-extensions.html)
- [NI-9213 Vendor Configuration Extensions](9213-extensions.html)
- [NI-9214 Vendor Configuration Extensions](9214-extensions.html)
- [NI-9215 Vendor Configuration Extensions](9215-extensions.html)
- [NI-9216/9226 Vendor Configuration Extensions](9216-9226-extensions.html)
- [NI-9217 Vendor Configuration Extensions](9217-extensions.html)
- [NI-9218 Vendor Configuration Extensions](9218-extensions.html)
- [NI-9219 Vendor Configuration Extensions](9219-extensions.html)
- [NI-9220 Vendor Configuration Extensions](9220-extensions.html)
- [NI-9222/9223 Vendor Configuration Extensions](9222-9223-extensions.html)
- [NI-9225 Vendor Configuration Extensions](9225-extensions.html)
- [NI-9227 Vendor Configuration Extensions](9227-extensions.html)
- [NI-9229/9239 Vendor Configuration Extensions](9229-9239-extensions.html)
- [NI-9234 Vendor Configuration Extensions](9234-extensions.html)
- [NI-9235 Vendor Configuration Extensions](9235-extensions.html)
- [NI-9236 Vendor Configuration Extensions](9236-extensions.html)
- [NI-9237 Vendor Configuration Extensions](9237-extensions.html)
- [NI-9242/9244 Vendor Configuration Extensions](9242-9244-extensions.html)
- [NI-9263 Vendor Configuration Extensions](9263-extensions.html)
- [NI-9264 Vendor Configuration Extensions](9264-extensions.html)
- [NI-9265 Vendor Configuration Extensions](9265-extensions.html)
- [NI-9266 Vendor Configuration Extensions](9266-extensions.html)
- [NI-9269 Vendor Configuration Extensions](9269-extensions.html)
- [NI-9381 Vendor Configuration Extensions](9381-extensions.html)
- [NI-9401 Vendor Configuration Extensions](9401-extensions.html)
- [NI-9402 Vendor Configuration Extensions](9402-extensions.html)
- [NI-9403 Vendor Configuration Extensions](9403-extensions.html)
- [NI-9476 Vendor Configuration Extensions](9476-extensions.html)
- [NI-9478 Vendor Configuration Extensions](9478-extensions.html)
- [NI-951x Vendor Configuration Extensions](951x-extensions.html)

Related information:

- NI 951x C Series Modules Object Dictionary
