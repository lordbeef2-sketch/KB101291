# NI DOCUMENT BUNDLE: rfmx-pulse

<!--NI_BUNDLE_CHUNK bundle=rfmx-pulse start=1 end=10 -->
<!--NI_TOPIC bundle=rfmx-pulse path=new-features-and-changes.html language=enus -->
## TOPIC 00001: RFmx Pulse New Features and Changes

- bundle_id: `rfmx-pulse`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-pulse`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx Pulse. Discover what is new in the latest releases of RFmx Pulse.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might in

### RFmx Pulse
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx Pulse.

RFmx Pulse

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx Pulse
 2026 Q2 Changes

RFmx Pulse 2026 Q2 adds support for Python API and
 PXIe-5841 (200 MHz) bandwidth hardware.

##### New
 Features

This version of RFmx Pulse adds
 support for the following features:

- Python API.

##### New
 Hardware Support

This version of RFmx Pulse
 adds support for the following hardware:

- PXIe-5841 ( 200 MHz ) bandwidth

#### RFmx Pulse
 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx Pulse 2025 Q3.

##### New
 Features

This version of the RFmx Pulse
 adds support for the following features:

- PXIe-5860 Self-Cal Validity Check

#### RFmx Pulse 2024 Q4 New Features and
 Changes

- Support for displaying acquired pulse amplitude trace.
- Support for maximum and minimum pulse width configurations for pulse detection.
- Support for FM chirp start and stop frequency results.

##### Behavior Changes

- Uninstalling RFmx Pulse software also removes any
 previous versions of RFmx Pulse .NET runtimes that
 were leaked in .NET Global Assembly Cache directory.

#### RFmx Pulse 2024 Q3 New Features and
 Changes

- Support for Rising Edge and Falling Edge absolute time

#### RFmx Pulse 2024 Q2 New Features and
 Changes

- Support for time sidelobe measurements
- Support for displaying the amplitude trace for the ON and OFF states of a Single
 Pulse
- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI along with the appropriate
 RFmxInstr Load Options property, instead.

#### RFmx Pulse 2024 Q1 New Features and
 Changes

- Support for intra-pulse stability per pulse or burst
- Support for Pulse Measurement at multiple measurement points

#### RFmx Pulse 2023 Q4 New Features and Changes

- Support for multi-burst analysis in Pulse stability measurement
- Support for Auto reference Level
- Support for Phase vs Time and Frequency vs Time traces
- Support for Overshoot, Ripple, and Droop results in dB
- Support for Peak mode in pulse detection reference
- Support for obtaining unprocessed I/Q data utilized for RFmx measurements

#### RFmx Pulse 2023 Q3 Features
 Overview

- Support for Pulse profile measurement results
  - Time: Rise Time, Fall Time, Pulse Width and PRI
  - Level: Top level, Base level, ON level, Droop, Overshoot, Ripple
  - Phase and Frequency: Average, Deviation, and Error
- Support for FM Chirp modulation results
- Support for Pulse Stability measurements
  - Amplitude, Phase, and Total
- Support for Segmented and Single large record in Signal Acquisition methods

<!--NI_TOPIC bundle=rfmx-pulse path=pulse-metrics.html language=enus -->
## TOPIC 00002: Pulse Metrics

- bundle_id: `rfmx-pulse`
- source_path: `pulse-metrics.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse/raw/resource/enus/pulse-metrics.html
- document_id: `rfmx-pulse`
- page_type: `leaf`
- content_type: `concept`
- source_description: Pulse waveforms toggle between OFF state and ON state periodically. The following figure depicts an ideal trapezoidal pulse. The pulse parameters (metrics) are measured as per the definitions of IEEE Std 181™-2011 (IEEE Standard on Transitions, Pulses, and Related Waveforms), from the IEEE Instrumen

### Pulse Metrics

Pulse waveforms toggle between OFF state and ON state periodically. The following figure
 depicts an ideal trapezoidal pulse.

[IMAGE alt='image' src='GUID-864ACD7F-5D13-4EEE-955A-C01E527666B9-a5.png']

The pulse parameters (metrics) are measured as per the definitions of *IEEE Std
 181™-2011* (IEEE Standard on Transitions, Pulses, and Related Waveforms), from
 the IEEE Instrumentation and Measurement (I&M) Society.

Pulse metrics are categorized into two sections: time and level.

#### Pulse Time Metrics

- The transition duration from OFF state to ON state is known as Rise Time and
 the transition duration from ON state to OFF state is known as Fall Time.
 The portion of transition duration used in calculating rise and fall time is
 determined by values you set in the Pulse Upper Threshold Level (%) and
 Pulse Lower Threshold Level (%) properties.
- The duration for which the pulse remains in the ON state is known as the
 pulse width. The Pulse Width Threshold Level (%) property determines the
 pulse portion for pulse width calculation.

#### Pulse Level
 Metrics

Pulse level measures amplitude levels in different regions of the
 pulse.

Non-ideal pulses have characteristics such as overshoot, droop, and
 ripple. The following figure depicts a non-ideal pulse.

[IMAGE alt='image' src='GUID-6D919295-1305-4A75-864C-A4F55134CF11-a5.png']

Overshoot

Overshoot is the ratio of the height of the local peak after a rising
 edge to the pulse amplitude.

[IMAGE alt='image' src='GUID-7DAC6D83-9435-4889-84CD-8F70282C9B8E-a5.png']

Overshoot is calculated (either as a percentage or in dB) based on the value you set
 to the Pulse Amplitude Deviation Unit property. If you set the Pulse Amplitude
 Deviation Unit property to Percentage, then the overshoot
 value is calculated either in volts or watts based on the value you set in the Pulse
 Amplitude Level Domain property. The calculation is as follows:

[IMAGE alt='image' src='GUID-C65596E0-9D3C-4EBD-9DFC-64D158C71F12-a5.png']

where,

L<sub>OV</sub> is the peak level after rising
 edge

L<sub>100%</sub> is the ON level

L<sub>0%</sub> is the OFF
 level

Droop

Droop is the rate at which the pulse top levels decays from
 the beginning to the end during the ON duration.

[IMAGE alt='image' src='GUID-FE22F739-3458-460F-8D22-4BE2B9BE64DF-a5.png']

For droop estimation, center 50% of the pulse ON duration samples are used. A
 best-fit linear line is applied on this region. The first point of intersection
 between the best fit line and the pulse is determined.

Droop is calculated (either as a percentage or in dB) based on the value you set to the Pulse
 Amplitude Deviation Unit property. If you set the Pulse Amplitude Deviation Unit
 property to Percentage, then the droop value is calculated
 either in volts or watts based on the value you set in the Pulse Amplitude Level
 Domain property. The calculation is as follows:

[IMAGE alt='image' src='GUID-D4CF2A3B-9F4A-4459-8C0F-7D55DD781B5B-a5.png']

L<sub>rise</sub> is the first point of intersection between the best-fit line and the
 pulse on the rising edge

L<sub>fall</sub> is the first point of intersection
 between the best-fit line and the pulse on the falling edge

L<sub>100%</sub>
 is the ON level

L<sub>0%</sub> is the OFF level

Ripple

Ripple is
 the difference between the maximum and minimum deviation from the pulse top
 reference.

[IMAGE alt='image' src='GUID-F19B1CCE-5447-4E39-80E6-BEA783296149-a5.png']

Ripple is calculated (either as a percentage or in dB) based on the value you set to
 the Pulse Amplitude Deviation Unit property. If you set the Pulse Amplitude
 Deviation Unit property to Percentage, then the ripple value
 is calculated either in volts or watts based on the value you set in the Pulse
 Amplitude Level Domain property. The calculation is as follows:

[IMAGE alt='image' src='GUID-013D2360-5EAF-4CA6-8DA8-593E2D60624A-a5.png']

where,

L<sub>rip+</sub> is the maximum deviation from the pulse top above ON
 level

L<sub>rip-</sub> is the maximum deviation from the pulse top below ON
 level

L<sub>top+</sub> is the distance between L<sub>rip+</sub> and its
 projection on the linear best-fit line (calculated in the droop estimation)

L<sub>top-</sub> is the distance between L<sub>rip-</sub> and its
 projection on the linear best-fit line (calculated in the droop
 estimation)

L<sub>100%</sub> is the ON level

L<sub>0%</sub> is the
 OFF level

<!--NI_TOPIC bundle=rfmx-pulse path=pulse-stability.html language=enus -->
## TOPIC 00003: Pulse Stability Overview

- bundle_id: `rfmx-pulse`
- source_path: `pulse-stability.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse/raw/resource/enus/pulse-stability.html
- document_id: `rfmx-pulse`
- page_type: `leaf`
- content_type: `concept`
- source_description: Pulse Stability is a measurement to characterize the amplitude and phase variation of successive pulses over time. A stability value for each individual pulse is the deviation of the pulse amplitude or phase from a reference value, measured at a selected point, you set in the Pulse Meas Point Refere

### Pulse Stability Overview

Pulse Stability is a measurement to characterize the amplitude and phase variation of
 successive pulses over time.

A stability value for each individual pulse is the deviation of the pulse amplitude or phase
 from a reference value, measured at a selected point, you set in the Pulse Meas Point
 Reference property within the pulse.

The reference value is the mean of the amplitude/phase over a range of pulses within burst
 and then averaged across all bursts. It must be measured over the most stable part within the
 burst to remove initial settling effects. You must configure the Pulse Stability Ref Offset
 property to ignore the number of starting pulses for reference value calculation.

For the average stability results the deviation measured values are mean squared over a range
 of pulses and then converted to dB. You must configure the Pulse Stability Meas Offset
 property to ignore the number of initial pulses for statistical average value calculation.

With multiple burst of pulses, at first, the deviation values are position averaged for each
 pulse position across all bursts. Positional average increases the sensitivity of measurement
 by suppressing the variation that occur over the multiple bursts. The resultant positional
 average deviation values are mean squared to get average stability results.

Additionally, you can perform carrier frequency offset (CFO) compensation on the measured
 phase values before the stability calculation.

<!--NI_TOPIC bundle=rfmx-pulse path=pulse-time-sidelobe.html language=enus -->
## TOPIC 00004: Pulse Time Sidelobe

- bundle_id: `rfmx-pulse`
- source_path: `pulse-time-sidelobe.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse/raw/resource/enus/pulse-time-sidelobe.html
- document_id: `rfmx-pulse`
- page_type: `leaf`
- content_type: `concept`
- source_description: The pulse time sidelobe is a result of the pulse compression technique, which cross-correlates the measured pulse and the reference pulse waveform. This technique generates an output that comprises of the main compressed pulse, which is characterized by a high peak value called the mainlobe. The mai

### Pulse Time Sidelobe

The *pulse time sidelobe* is a result of the pulse compression technique, which
 cross-correlates the measured pulse and the reference pulse waveform. This technique
 generates an output that comprises of the main compressed pulse, which is characterized
 by a high peak value called the *mainlobe*. The mainlobe is surrounded by
 artifacts called *time sidelobes*.

Figure 1.

[IMAGE alt='image' src='GUID-B59D14C7-343E-49F0-A3B9-EF141C21EA28-a5.svg']

If both the measured and reference pulses are identical, the pulse time sidelobe exhibits
 a narrower mainlobe with a peak correlation value of 1. In practice, the measured pulse
 typically differs from the ideal reference pulse due to artifacts and gains introduced
 by the device under test (DUT). Consequently, there is an increase in the sidelobe
 levels and a decrease in the peak correlation value.

You can apply the window function to the reference pulse to reduce the sidelobe levels at
 the correlated output. By default, either a rectangular window or no windowing is
 applied.

C

o

r

r

e

l

a

t

o

r

o

u

t

p

u

t

,

P

c

o

r

r

k

=

|

∑

n

=

1

N

I

Q

m

e

a

s

t

n

+

k

×

I

Q

r

e

f

*

t

n

|

2

where:

- k is the sample offset within the measured pulse
- IQ meas (t n ) for n=1 to N → measured pulse
- IQ ref (t m ) for m=1 to M → reference pulse

Both the measured pulse and the reference pulse are sampled at the same sample
 rate. If you provide a reference pulse with a different sample rate, the reference pulse
 is automatically resampled to match the measured pulse sample rate.

Since the cross correlation is equivalent to the Linear Time-Invariant (LTI) operation, you can
 efficiently implement the cross correlation in the frequency domain using the Fast
 Fourier Transform (FFT) operation.

peak

P

e

a

k

c

o

r

r

e

l

a

t

e

d

o

u

t

p

u

t

p

o

w

e

r

,

P

c

o

r

r

k

p

e

a

k

=

|

∑

n

=

1

N

I

Q

m

e

a

s

t

n

+

k

p

e

a

k

×

I

Q

r

e

f

*

t

n

|

2

To find the peak correlation value, normalize the peak correlated output power
 by both the reference pulse power and the measured pulse power. This value
 ranges between 0 (no correlation) and 1 (perfectly correlated).

P

e

a

k

⁢

c

o

r

r

e

l

a

t

i

o

n

⁢

P

p

e

a

k

=

|

∑

n

=

1

N

I

Q

m

e

a

s

t

n

+

k

p

e

a

k

×

I

Q

r

e

f

*

t

n

|

2

∑

n

=

1

N

|

I

Q

m

e

a

s

t

n

|

2

×

∑

m

=

1

M

|

I

Q

r

e

f

t

m

|

2

To determine the magnitude of the correlated output, normalize
 the peak correlated output power by the reference pulse power and the
 correlation interval and then convert the value to the dBm scale.

C

o

r

r

e

l

a

t

e

d

m

a

g

n

i

t

u

d

e

,

P

c

o

r

r

,

d

B

m

=

10

+

10

l

o

g

|

∑

n

=

1

N

I

Q

m

e

a

s

t

n

+

k

p

e

a

k

×

I

Q

r

e

f

*

t

n

|

2

K

×

∑

m

=

1

M

|

I

Q

r

e

f

t

m

|

2

where:

- K is the correlation interval

Figure 2.

[IMAGE alt='image' src='GUID-4A128199-E795-4C91-B56B-FF4EFAE2770E-a5.svg']

<!--NI_TOPIC bundle=rfmx-pulse path=rfmxpulse-overview.html language=enus -->
## TOPIC 00005: RFmx Pulse Overview

- bundle_id: `rfmx-pulse`
- source_path: `rfmxpulse-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse/raw/resource/enus/rfmxpulse-overview.html
- document_id: `rfmx-pulse`
- page_type: `leaf`
- content_type: `concept`
- source_description: This user manual contains an introduction to RFmx Pulse measurement and related conceptual information.

### RFmx Pulse Overview

This user manual contains an introduction to RFmx Pulse
 measurement and related conceptual information.

<!--NI_TOPIC bundle=rfmx-pulse path=scalar-stability-results.html language=enus -->
## TOPIC 00006: Scalar Stability Results

- bundle_id: `rfmx-pulse`
- source_path: `scalar-stability-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse/raw/resource/enus/scalar-stability-results.html
- document_id: `rfmx-pulse`
- page_type: `leaf`
- content_type: `concept`
- source_description: Multiburst Disabled Individual pulse stability resultsAverage pulse stability results Multiburst Enabled ∅ → P h a s e A → A m p l i t u d e P → B u r s t L e n g t h B → N u m b e r o f B u r s t s A m p l i t u d e D e v i a t i o n a t p o s i t

### Scalar Stability Results

#### Multiburst Disabled

[IMAGE alt='image' src='GUID-42BC2F67-BAF7-4F75-995A-B68ACDB770E2-a5.png']

[IMAGE alt='image' src='GUID-625F72BA-5765-491C-BE0D-6D3F7DF79128-a5.png']

Individual pulse stability results

[IMAGE alt='image' src='GUID-D4DE929E-5714-4FBE-BB08-6F6BE1A5870E-a5.png']

Average
 pulse stability results

[IMAGE alt='image' src='GUID-5960FBFC-3F9F-4528-B636-92865D167113-a5.png']

#### Multiburst Enabled

[IMAGE alt='image' src='GUID-882FF366-636E-4DFB-B994-F71BD1D0F787-a5.png']

∅

→

P

h

a

s

e

A

→

A

m

p

l

i

t

u

d

e

P

→

B

u

r

s

t

L

e

n

g

t

h

B

→

N

u

m

b

e

r

o

f

B

u

r

s

t

s

A

m

p

l

i

t

u

d

e

D

e

v

i

a

t

i

o

n

a

t

p

o

s

i

t

i

o

n

"

p

"

i

n

b

u

r

s

t

"

b

"

,

δ

A

b

,

p

=

[

A

b

,

p

A

-

-

1

]

A

-

=

reference

⁢

mean

⁢

amplitude

⁢

value

A

-

=

1

B

(

P

-

r

)

.

∑

b

=

1

B

∑

p

=

r

P

A

b

,

p

r

⁢

=

′

Reference

⁢

⁢

Offset

′

P

h

a

s

e

D

e

v

i

a

t

i

o

n

a

t

p

o

s

i

t

i

o

n

"

p

"

i

n

b

u

r

s

t

"

b

"

,

δ

∅

b

,

p

=

[

ϕ

b

,

p

-

ϕ

-

]

ϕ

-

=

reference

⁢

mean

⁢

phase

⁢

value

,

ϕ

-

=

1

B

(

P

-

r

)

.

∑

b

=

1

B

∑

p

=

r

P

ϕ

b

,

p

r

⁢

=

′

Reference

⁢

⁢

Offset

′

Individual pulse stability results

A

m

p

l

i

t

u

d

e

S

t

a

b

i

l

i

t

y

b

,

p

d

B

=

10

.

l

o

g

|

δA

b

,

p

|

2

P

h

a

s

e

S

t

a

b

i

l

i

t

y

b

,

p

d

B

=

10

.

l

o

g

|

δ

∅

b

,

p

|

2

T

o

t

a

l

S

t

a

b

i

l

i

t

y

b

,

p

d

B

=

10

.

l

o

g

|

δ

A

b

,

p

|

2

+

|

δ

∅

b

,

p

|

2

Average pulse stability results

P

o

s

i

t

i

o

n

a

l

a

v

e

r

a

g

e

o

f

a

m

p

l

i

t

u

d

e

d

e

v

i

a

t

i

o

n

a

t

p

o

s

i

t

i

o

n

"

p

"

,

δ

A

p

=

1

B

∑

b

=

1

B

δ

A

b

,

p

P

o

s

i

t

i

o

n

a

l

a

v

e

r

a

g

e

o

f

p

h

a

s

e

d

e

v

i

a

t

i

o

n

a

t

p

o

s

i

t

i

o

n

"

p

"

,

δ

∅

p

=

1

B

∑

b

=

1

B

δ

∅

b

,

p

A

v

e

r

a

g

e

A

m

p

l

i

t

u

d

e

S

t

a

b

i

l

i

t

y

d

B

=

10

.

l

o

g

1

P

-

m

∑

p

=

m

P

|

δ

A

p

|

2

A

v

e

r

a

g

e

P

h

a

s

e

S

t

a

b

i

l

i

t

y

d

B

=

10

.

l

o

g

1

P

-

m

∑

p

=

m

P

|

δ

∅

p

|

2

A

v

e

r

a

g

e

T

o

t

a

l

S

t

a

b

i

l

i

t

y

d

B

=

10

.

l

o

g

1

P

-

m

∑

p

=

m

P

|

δ

A

p

|

2

+

|

δ

∅

p

|

2

where

,

m

⁢

=

′

Measurement

⁢

Offset

′

<!--NI_TOPIC bundle=rfmx-pulse path=stability-traces.html language=enus -->
## TOPIC 00007: Stability Trace

- bundle_id: `rfmx-pulse`
- source_path: `stability-traces.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse/raw/resource/enus/stability-traces.html
- document_id: `rfmx-pulse`
- page_type: `leaf`
- content_type: `concept`
- source_description: Stability Trace The stability trace of the selected pulse is calculated from the stability value for each sample within the pulse ON region with respect to the reference value. Pulse-to-Pulse stability Trace The pulse-to-pulse stability trace is calculated from the deviation between two neighboring

### Stability Trace

#### Stability Trace

The stability trace of the selected pulse is calculated from the stability value for
 each sample within the pulse ON region with respect to the reference
 value.

[IMAGE alt='image' src='GUID-27F6A0F2-10D1-41F9-A736-A18A97396389-a5.png']

[IMAGE alt='image' src='GUID-7CD49DD3-5E00-47FF-B0BE-9371A810ED13-a5.png']

#### Pulse-to-Pulse stability Trace

The pulse-to-pulse stability trace is calculated from the deviation between two
 neighboring pulses for the value you set in the 'Measurement Point' within the
 pulse.

[IMAGE alt='image' src='GUID-BCF47E5F-11B7-4DAA-A02F-78C09BF711AE-a5.png']

[IMAGE alt='image' src='GUID-2A643471-1259-42D1-8F14-48FD06ECEB2B-a5.png']

#### Burst Selected Position Stability Trace

The
 burst selected position stability trace is determined by computing the position
 average of the deviation values for the selected pulse position across all bursts,
 in relation to the reference value.

[IMAGE alt='image' src='GUID-988BF33C-B48A-441A-878A-61BEE736BB4B-a5.png']

∅

→

P

h

a

s

e

A

→

A

m

p

l

i

t

u

d

e

k

t

h

→

s

a

m

p

l

e

i

n

p

u

l

s

e

O

N

r

e

g

i

o

n

B

→

N

u

m

b

e

r

o

f

B

u

r

s

t

s

P

→

B

u

r

s

t

L

e

n

g

t

h

S

e

l

e

c

t

e

d

P

o

s

i

t

i

o

n

→

P

o

s

1

A

m

p

l

i

t

u

d

e

D

e

v

i

a

t

i

o

n

a

t

p

o

s

i

t

i

o

n

"

s

e

l

"

i

n

b

u

r

s

t

"

b

"

,

δ

A

b

,

s

e

l

[

k

]

=

[

A

b

,

s

e

l

[

k

]

A

-

[

k

]

-

1

]

A

-

[

k

]

=

reference

⁢

mean

⁢

amplitude

⁢

at

⁢

kth

⁢

sample

,

A

-

[

k

]

=

1

B

(

P

-

r

)

.

∑

b

=

1

B

∑

p

=

r

P

A

b

,

p

[

k

]

r

⁢

=

′

Reference

⁢

⁢

Offset

′

P

h

a

s

e

D

e

v

i

a

t

i

o

n

a

t

p

o

s

i

t

i

o

n

"

s

e

l

"

i

n

b

u

r

s

t

"

b

"

,

δ

∅

b

,

s

e

l

[

k

]

=

[

ϕ

b

,

s

e

l

[

k

]

-

ϕ

-

[

k

]

ϕ

-

[

k

]

=

reference

⁢

mean

⁢

amplitude

⁢

at

⁢

kth

⁢

sample

,

ϕ

-

[

k

]

=

1

B

(

P

-

r

)

.

∑

b

=

1

B

∑

p

=

r

P

ϕ

b

,

p

[

k

]

P

o

s

i

t

i

o

n

a

l

a

v

e

r

a

g

e

o

f

a

m

p

l

i

t

u

d

e

d

e

v

i

a

t

i

o

n

,

δ

A

s

e

l

[

k

]

=

1

B

∑

b

=

1

B

δ

A

b

,

s

e

l

[

k

]

P

o

s

i

t

i

o

n

a

l

a

v

e

r

a

g

e

o

f

p

h

a

s

e

d

e

v

i

a

t

i

o

n

,

δ

∅

s

e

l

[

k

]

=

1

B

∑

b

=

1

B

δ

∅

b

,

s

e

l

[

k

]

A

m

p

l

i

t

u

d

e

S

t

a

b

i

l

i

t

y

d

B

=

10

.

l

o

g

|

δ

A

s

e

l

[

k

]

|

2

P

h

a

s

e

S

t

a

b

i

l

i

t

y

d

B

=

10

.

l

o

g

|

δ

∅

s

e

l

[

k

]

|

2

T

o

t

a

l

S

t

a

b

i

l

i

t

y

d

B

=

10

.

l

o

g

|

δ

A

s

e

l

[

k

]

|

2

+

|

δ

∅

s

e

l

[

k

]

|

2

#### Multiple Measurement Points
 Stability Trace

Pulse stability measurements can be performed on single or multiple selected
 measurement points within a pulse. The stability is calculated for the same
 measurement points in all consecutive pulses in an acquired burst.

The multiple measurement points over pulse ON region can be configured using the
 Pulse Multi Meas Points Window Start (%), Pulse Multi Meas Points Window Stop (%),
 and Pulse Multi Meas Points Window Step Size (%) properties.

The multiple measurement points stability trace is computed by averaging the
 deviation values of each measurement point across the pulses.

[IMAGE alt='image' src='GUID-B7FD5B3F-6031-4DAD-81DE-9FDF7EDE4DE1-a5.png']

A

m

p

l

i

t

u

d

e

D

e

v

i

a

t

i

o

n

o

f

k

t

h

m

e

a

s

u

r

e

m

e

n

t

p

o

i

n

t

i

n

n

t

h

p

u

l

s

e

,

δ

A

n

(

k

)

=

[

A

n

(

k

)

A

-

(

k

)

-

1

]

A

n

(

k

)

is

⁢

the

⁢

measured

⁢

amplitude

⁢

value

⁢

of

⁢

the

⁢

kth

⁢

measurement

⁢

point

⁢

in

⁢

the

⁢

nth

⁢

pulse

A

-

(

k

)

is

⁢

the

⁢

reference

⁢

mean

⁢

amplitude

⁢

value

⁢

of

⁢

the

⁢

kth

⁢

measurement

⁢

point

A

-

(

k

)

=

1

N

-

r

.

∑

n

=

r

N

A

n

(

k

)

P

h

a

s

e

D

e

v

i

a

t

i

o

n

o

f

k

t

h

m

e

a

s

u

r

e

m

e

n

t

p

o

i

n

t

i

n

n

t

h

p

u

l

s

e

,

δ

∅

n

(

k

)

=

[

ϕ

n

(

k

)

-

ϕ

-

(

k

)

]

ϕ

n

(

k

)

is

⁢

the

⁢

measured

⁢

phase

⁢

value

⁢

of

⁢

the

⁢

kth

⁢

measurement

⁢

point

⁢

in

⁢

the

⁢

nth

⁢

pulse

ϕ

-

(

k

)

is

⁢

the

⁢

reference

⁢

mean

⁢

phase

⁢

value

⁢

of

⁢

the

⁢

kth

⁢

measurement

⁢

point

ϕ

-

(

k

)

=

1

N

-

r

.

∑

n

=

r

N

ϕ

n

(

k

)

A

v

e

r

a

g

e

A

m

p

l

i

t

u

d

e

S

t

a

b

i

l

i

t

y

k

(

d

B

)

=

10

.

l

o

g

1

N

-

m

∑

n

=

m

N

δ

A

n

(

k

)

2

A

v

e

r

a

g

e

P

h

a

s

e

S

t

a

b

i

l

i

t

y

k

(

d

B

)

=

10

.

l

o

g

1

N

-

m

∑

n

=

m

N

δ

∅

n

(

k

)

2

where,

m is the measurement offset

r is the reference offset

N is the total number of pulses

When multiburst is enabled, the deviation values are first positional averaged for
 each pulse position across all bursts and then averaged across the pulses.

#### Intrapulse Stability Trace

The intrapulse stability is a measure of amplitude variation and phase variation
 values within a pulse. The selected multiple measurement points within a pulse
 are compared with a reference value for the pulse. The intrapulse stability is
 available as amplitude, phase, and total stability for either the selected pulse
 (when multiburst is disabled) or selected position (when multiburst is
 enabled).

The intrapulse stability trace of the selected pulse is computed as the deviation
 between the measured amplitude and phase values of multiple measurement points
 and the computed reference value of the pulse.

A

m

p

l

i

t

u

d

e

D

e

v

i

a

t

i

o

n

o

f

k

t

h

m

e

a

s

u

r

e

m

e

n

t

p

o

i

n

t

i

n

s

e

l

e

c

t

e

d

p

u

l

s

e

,

δ

A

s

e

l

e

c

t

e

d

(

k

)

=

[

A

s

e

l

e

c

t

e

d

(

k

)

A

-

s

e

l

e

c

t

e

d

-

1

]

A

s

e

l

e

c

t

e

d

(

k

)

is

⁢

the

⁢

measured

⁢

amplitude

⁢

value

⁢

of

⁢

kth

⁢

measurement

⁢

point

⁢

in

⁢

selected

⁢

pulse

A

-

s

e

l

e

c

t

e

d

⁢

is

⁢

the

⁢

reference

⁢

mean

⁢

amplitude

⁢

value

⁢

of

⁢

the

⁢

selected

⁢

pulse

A

-

s

e

l

e

c

t

e

d

=

1

M

.

∑

k

=

M

P

a

t

w

i

n

d

o

w

s

t

a

r

t

M

P

a

t

w

i

n

d

o

w

s

t

o

p

A

s

e

l

e

c

t

e

d

(

k

)

M

⁢

is

⁢

the

⁢

total

⁢

number

⁢

of

⁢

measurement

⁢

points

⁢

between

⁢

the

⁢

window

⁢

start

⁢

and

⁢

window

⁢

stop

P

h

a

s

e

D

e

v

i

a

t

i

o

n

o

f

k

t

h

m

e

a

s

u

r

e

m

e

n

t

p

o

i

n

t

i

n

s

e

l

e

c

t

e

d

p

u

l

s

e

,

δ

∅

s

e

l

e

c

t

e

d

(

k

)

=

[

ϕ

s

e

l

e

c

t

e

d

(

k

)

-

ϕ

-

s

e

l

e

c

t

e

d

-

]

ϕ

s

e

l

e

c

t

e

d

(

k

)

is

⁢

the

⁢

measured

⁢

phase

⁢

value

⁢

of

⁢

the

⁢

kth

⁢

measurement

⁢

point

⁢

in

⁢

the

⁢

selected

⁢

pulse

ϕ

-

s

e

l

e

c

t

e

d

⁢

is

⁢

the

⁢

reference

⁢

mean

⁢

phase

⁢

value

⁢

of

⁢

the

⁢

selected

⁢

pulse

ϕ

-

s

e

l

e

c

t

e

d

=

1

M

.

∑

k

=

M

P

a

t

w

i

n

d

o

w

s

t

a

r

t

M

P

a

t

w

i

n

d

o

w

s

t

o

p

ϕ

s

e

l

e

c

t

e

d

(

k

)

M

⁢

is

⁢

the

⁢

total

⁢

number

⁢

of

⁢

measurement

⁢

points

⁢

between

⁢

the

⁢

window

⁢

start

⁢

and

⁢

window

⁢

stop

A

m

p

l

i

t

u

d

e

S

t

a

b

i

l

i

t

y

k

d

B

=

10

.

l

o

g

δ

A

s

e

l

e

c

t

e

d

(

k

)

2

P

h

a

s

e

S

t

a

b

i

l

i

t

y

k

d

B

=

10

.

l

o

g

δ

∅

s

e

l

e

c

t

e

d

(

k

)

2

T

o

t

a

l

S

t

a

b

i

l

i

t

y

k

d

B

=

10

.

l

o

g

δ

A

s

e

l

e

c

t

e

d

(

k

)

2

+

δ

∅

s

e

l

e

c

t

e

d

(

k

)

2

When multiburst is enabled, the deviation values are
 positional averaged across all bursts for the selected position.

#### Burst Intrapulse Stability Trace

The burst intrapulse stability trace is returned as average amplitude, average phase, and average
 total stability. This trace is computed by averaging the deviation values of each
 measurement point across the pulses.

A

m

p

l

i

t

u

d

e

D

e

v

i

a

t

i

o

n

o

f

k

t

h

m

e

a

s

u

r

e

m

e

n

t

p

o

i

n

t

i

n

n

t

h

p

u

l

s

e

,

δ

A

n

(

k

)

=

[

A

n

(

k

)

A

-

n

-

1

]

A

-

n

⁢

is

⁢

the

⁢

reference

⁢

mean

⁢

amplitude

⁢

value

⁢

of

⁢

the

⁢

nth

⁢

pulse

A

-

n

=

1

M

.

∑

k

=

M

P

a

t

w

i

n

d

o

w

s

t

a

r

t

M

P

a

t

w

i

n

d

o

w

s

t

o

p

A

n

(

k

)

M

⁢

is

⁢

the

⁢

total

⁢

number

⁢

of

⁢

measurement

⁢

points

⁢

between

⁢

window

⁢

start

⁢

and

⁢

stop

P

h

a

s

e

D

e

v

i

a

t

i

o

n

o

f

k

t

h

m

e

a

s

u

r

e

m

e

n

t

p

o

i

n

t

i

n

n

t

h

p

u

l

s

e

,

δ

∅

n

(

k

)

=

[

ϕ

n

(

k

)

-

ϕ

-

n

]

ϕ

-

n

⁢

is

⁢

the

⁢

reference

⁢

mean

⁢

phase

⁢

value

⁢

of

⁢

the

⁢

nth

⁢

pulse

ϕ

-

(

k

)

=

1

M

.

∑

k

=

M

P

a

t

w

i

n

d

o

w

s

t

a

r

t

M

P

a

t

w

i

n

d

o

w

s

t

o

p

ϕ

n

(

k

)

M

⁢

is

⁢

the

⁢

total

⁢

number

⁢

of

⁢

measurement

⁢

points

⁢

between

⁢

the

⁢

window

⁢

start

⁢

and

⁢

window

⁢

stop

A

v

e

r

a

g

e

A

m

p

l

i

t

u

d

e

S

t

a

b

i

l

i

t

y

k

(

d

B

)

=

10

.

l

o

g

1

N

-

m

∑

n

=

m

N

δ

A

n

(

k

)

2

A

v

e

r

a

g

e

P

h

a

s

e

S

t

a

b

i

l

i

t

y

k

(

d

B

)

=

10

.

l

o

g

1

N

-

m

∑

n

=

m

N

δ

∅

n

(

k

)

2

A

v

e

r

a

g

e

T

o

t

a

l

S

t

a

b

i

l

i

t

y

k

(

d

B

)

=

10

.

l

o

g

1

N

-

m

∑

n

=

m

N

δ

A

n

(

k

)

2

+

δ

∅

n

(

k

)

2

where,

m is the measurement offset

N is the total number of pulses

When multiburst is enabled, the deviation values are first positional
 averaged across all bursts and then an average is computed across the pulses in a
 positional average burst.

<!--NI_TOPIC bundle=rfmx-pulse path=supported-hw.html language=enus -->
## TOPIC 00008: Supported Hardware

- bundle_id: `rfmx-pulse`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse/raw/resource/enus/supported-hw.html
- document_id: `rfmx-pulse`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx Pulse Supported Hardware RFmx Pulse Hardware Earliest Driver Version Support (Windows 11) PXIe-5668 2022 Q3 PXIe-5831 2022 Q3 PXIe-5840 2022 Q3 PXIe-5841 (1 GHz Bandwidth) 2022 Q3 PXIe-5841 (200 MHz Bandwidth) 2026 Q2 PXIe-5842 2022 Q4 PXIe-5860 2024 Q3

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx Pulse Hardware | Earliest Driver Version Support (Windows 11) |
| --- | --- |
| PXIe-5668 | 2022 Q3 |
| PXIe-5831 | 2022 Q3 |
| PXIe-5840 | 2022 Q3 |
| PXIe-5841 (1 GHz Bandwidth) | 2022 Q3 |
| PXIe-5841 (200 MHz Bandwidth) | 2026 Q2 |
| PXIe-5842 | 2022 Q4 |
| PXIe-5860 | 2024 Q3 |

Note

RFmx Pulse

NI-RFSA Properties

NI-RFSA LabVIEW VI
 Reference

For more information about your hardware and functionality, refer to the *NI-RFSA
 User Manual*.

<!--NI_TOPIC bundle=rfmx-pulse path=system-requirements.html language=enus -->
## TOPIC 00009: RFmx Pulse System Requirements

- bundle_id: `rfmx-pulse`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse/raw/resource/enus/system-requirements.html
- document_id: `rfmx-pulse`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Pulse has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory may be requir

### RFmx Pulse System Requirements

RFmx Pulse has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-pulse path=user-manual-welcome.html language=enus -->
## TOPIC 00010: RFmx Pulse User Manual

- bundle_id: `rfmx-pulse`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-pulse`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx Pulse User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx Pulse
 User Manual

The RFmx Pulse User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx Pulse
- License Setup and Activation
- RFmx Pulse Release Notes
- Getting Started with RFmx
- RFmx Pulse LabVIEW Reference
- RFmx Pulse .NET Reference
- RFmx Pulse C Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET Reference
- RFmx Instr C Reference
