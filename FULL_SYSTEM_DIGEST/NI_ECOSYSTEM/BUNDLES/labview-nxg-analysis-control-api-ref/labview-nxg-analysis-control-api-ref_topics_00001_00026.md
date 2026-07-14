# NI DOCUMENT BUNDLE: labview-nxg-analysis-control-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-analysis-control-api-ref start=1 end=26 -->
<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=backlash.html language=enus -->
## TOPIC 00001: Backlash

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `backlash.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/backlash.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a backlash or deadband function. reset A Boolean or a Boolean array that determines whether to use initial output to perform the deadband computation. True Uses initial output to perform the deadband computation. False Uses the previous output to perform the deadband computation. This nod

Backlash

Implements a backlash or deadband function.

[IMAGE alt='1378' src='Backlash_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean or a Boolean array that determines whether to use initial output to perform the deadband computation.

| True | Uses initial output to perform the deadband computation. |
| --- | --- |
| False | Uses the previous output to perform the deadband computation. |

This node automatically uses initial output to perform the deadband computation on the first call.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### input

Input signal.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### deadband

Width of the deadband.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### initial output

Value that this node compares with input the first time the backlash function executes or when reset is True.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Output signal.

This output can return a double-precision, floating-point number or an array of double-precision, floating-point numbers.

#### Algorithm Definition for the Backlash Function

The following equation defines the backlash function.

y

(

t

)

=

{

y

(

t

−

1

)

if

⁢

|

u

(

t

)

−

y

(

t

−

1

)

|

≤

d

e

a

d

b

a

n

d

2

u

(

t

)

−

d

e

a

d

b

a

n

d

2

⁢

if

⁢

|

u

(

t

)

−

y

(

t

−

1

)

|

≤

d

e

a

d

b

a

n

d

2

⁢

and

⁢

u

(

t

)

⁢

>

y

(

t

−

1

)

u

(

t

)

+

d

e

a

d

b

a

n

d

2

⁢

if

⁢

|

u

(

t

)

−

y

(

t

−

1

)

|

>

d

e

a

d

b

a

n

d

2

⁢

and

⁢

u

(

t

)

⁢

≤

y

(

t

−

1

)

y

(

t

)

=

{

y

(

t

−

1

)

if

⁢

|

u

(

t

)

−

y

(

t

−

1

)

|

≤

d

e

a

d

b

a

n

d

2

u

(

t

)

−

d

e

a

d

b

a

n

d

2

⁢

if

⁢

|

u

(

t

)

−

y

(

t

−

1

)

|

≤

d

e

a

d

b

a

n

d

2

⁢

and

⁢

u

(

t

)

⁢

>

y

(

t

−

1

)

u

(

t

)

+

d

e

a

d

b

a

n

d

2

⁢

if

⁢

|

u

(

t

)

−

y

(

t

−

1

)

|

>

d

e

a

d

b

a

n

d

2

⁢

and

⁢

u

(

t

)

⁢

≤

y

(

t

−

1

)

where

- u is the input signal
- y is the output signal
- t is the current simulation time

Parent topic:

Non-Linear Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=create-gain-multimode-function.html language=enus -->
## TOPIC 00002: Create Gain

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `create-gain-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/create-gain-multimode-function.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns gain values of a controller.

Create Gain

Returns gain values of a controller.

PID Gains Nodes

Implement Proportional-Integral-Derivative (PID) control applications.

P

Returns proportional gains of a P controller.

Parent topic:

PID Gains Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=create-gain-pd-academic.html language=enus -->
## TOPIC 00003: Academic

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `create-gain-pd-academic.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/create-gain-pd-academic.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns PD gains of a PD controller in the Academic form. derivative unit Unit associated with the derivative gain. This input accepts a ring or an array of rings. Hz 0 Specifies that the derivative gain is expressed in Hz. s 1 Specifies that the derivative gain is expressed in seconds. min 2 Specif

Academic

Returns PD gains of a PD controller in the Academic form.

[IMAGE alt='1378' src='Create_Continuous_PD_Academic_Gain_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### derivative unit

Unit associated with the derivative gain.

This input accepts a ring or an array of rings.

| Hz | 0 | Specifies that the derivative gain is expressed in Hz. |
| --- | --- | --- |
| s | 1 | Specifies that the derivative gain is expressed in seconds. |
| min | 2 | Specifies that the derivative gain is expressed in minutes. |

Default value: The default value of this input changes depending on the data type you wire. If you wire a ring to this input, the default is s. If you wire an array of rings to this input, the default is Hz.

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### proportional unit

Unit associated with the proportional gain.

The relationship between the available units is K = 100/PB.

This input accepts a ring or an array of rings.

| Gain (K) | 0 | Specifies that the proportional gain is expressed in terms of proportional gain (K). |
| --- | --- | --- |
| Band (PB) | 1 | Specifies that the proportional gain is expressed in terms of proportional band (PB). |

Default value: Gain (K)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Value of the proportional component of the controller.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### derivative

Value of the derivative component of the controller.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### filter coefficient [a]

Derivative lowpass filter coefficient of the controller.

If you specify a value for filter coefficient unit, you must also specify a value for filter coefficient [a]. When filter coefficient unit is Alpha, the valid value range of filter coefficient [a] is [0, 1]. When filter coefficient unit is N, the valid value range of filter coefficient [a] is [1, 1000].

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

Default value: NaN.

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### filter coefficient unit

Unit of the derivative lowpass filter coefficients.

The relationship between the available units are as follows: N = 1/Alpha; Time Constant = 1/(2 * 
 Pi * Cutoff Frequency).

This input accepts a ring or an array of rings.

| Alpha | 0 | Specifies that the filter coefficients are expressed in Alpha. |
| --- | --- | --- |
| N | 1 | Specifies that the filter coefficients are expressed in N. |
| Cutoff Frequency | 2 | Specifies that the filter coefficients are expressed in Hz. |
| Time Constant | 3 | Specifies that the filter coefficients are expressed in seconds. |

Default value: Alpha

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### action

Action of the controller.

This input accepts a ring or an array of rings.

| Reverse | 0 | The controller is reverse-acting. |
| --- | --- | --- |
| Direct | 1 | The controller is direct-acting. |

Default value: Reverse

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### PD gains

Proportional gain and derivative gain parameters of the controller.

This output can return a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Derivative gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### filter coefficient [a]

Derivative lowpass filter coefficient of the controller.

#### Algorithm Definition

The following transfer function represents a PD controller in the Academic form:

C

i

(

s

)

=

K

c

(

1

+

T

d

s

α

i

T

d

s

+

1

)

C

i

(

s

)

=

K

c

(

1

+

T

d

s

α

i

T

d

s

+

1

)

where K<sub>c</sub> is the proportional gain, T<sub>d</sub> is the derivative time constant, and

α

i

Parent topic:

Create Gain

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=create-gain-pi-academic.html language=enus -->
## TOPIC 00004: Academic

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `create-gain-pi-academic.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/create-gain-pi-academic.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns PI gains of a PI controller in the Academic form. integral unit Unit associated with the integral gain. This input accepts a ring or an array of rings. Hz 0 Specifies that the integral gain is expressed in Hz. s 1 Specifies that the integral gain is expressed in seconds. min 2 Specifies that

Academic

Returns PI gains of a PI controller in the Academic form.

[IMAGE alt='1378' src='Create_Continuous_PI_Academic_Gain_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### integral unit

Unit associated with the integral gain.

This input accepts a ring or an array of rings.

| Hz | 0 | Specifies that the integral gain is expressed in Hz. |
| --- | --- | --- |
| s | 1 | Specifies that the integral gain is expressed in seconds. |
| min | 2 | Specifies that the integral gain is expressed in minutes. |

Default value: The default value of this input changes depending on the data type you wire. If you wire a ring to this input, the default is s. If you wire an array of rings to this input, the default is Hz.

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### proportional unit

Unit associated with the proportional gain.

The relationship between the available units is K = 100/PB.

This input accepts a ring or an array of rings.

| Gain (K) | 0 | Specifies that the proportional gain is expressed in terms of proportional gain (K). |
| --- | --- | --- |
| Band (PB) | 1 | Specifies that the proportional gain is expressed in terms of proportional band (PB). |

Default value: Gain (K)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Value of the proportional component of the controller.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### integral

Value of the integral component of the controller.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### action

Action of the controller.

This input accepts a ring or an array of rings.

| Reverse | 0 | The controller is reverse-acting. |
| --- | --- | --- |
| Direct | 1 | The controller is direct-acting. |

Default value: Reverse

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### PI gains

Proportional gain and integral gain parameters of the controller.

This output can return a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Integral gain of the controller.

#### Algorithm Definition

The following transfer function represents a PI controller in the Academic form:

C

i

(

s

)

=

K

c

(

1

+

1

T

i

s

)

C

i

(

s

)

=

K

c

(

1

+

1

T

i

s

)

where K<sub>c</sub> is the proportional gain and T<sub>i</sub> is the integral time constant.

Parent topic:

Create Gain

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=create-gain-pi-parallel.html language=enus -->
## TOPIC 00005: Parallel

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `create-gain-pi-parallel.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/create-gain-pi-parallel.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns PI gains of a PI controller in the Parallel form. integral unit Unit associated with the integral gain. This input accepts a ring or an array of rings. Hz 0 Specifies that the integral gain is expressed in Hz. s 1 Specifies that the integral gain is expressed in seconds. min 2 Specifies that

Parallel

Returns PI gains of a PI controller in the Parallel form.

[IMAGE alt='1378' src='Create_Continuous_PI_Parallel_Gain_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### integral unit

Unit associated with the integral gain.

This input accepts a ring or an array of rings.

| Hz | 0 | Specifies that the integral gain is expressed in Hz. |
| --- | --- | --- |
| s | 1 | Specifies that the integral gain is expressed in seconds. |
| min | 2 | Specifies that the integral gain is expressed in minutes. |

Default value: The default value of this input changes depending on the data type you wire. If you wire a ring to this input, the default is s. If you wire an array of rings to this input, the default is Hz.

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### proportional unit

Unit associated with the proportional gain.

The relationship between the available units is K = 100/PB.

This input accepts a ring or an array of rings.

| Gain (K) | 0 | Specifies that the proportional gain is expressed in terms of proportional gain (K). |
| --- | --- | --- |
| Band (PB) | 1 | Specifies that the proportional gain is expressed in terms of proportional band (PB). |

Default value: Gain (K)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Value of the proportional component of the controller.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### integral

Value of the integral component of the controller.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### action

Action of the controller.

This input accepts a ring or an array of rings.

| Reverse | 0 | The controller is reverse-acting. |
| --- | --- | --- |
| Direct | 1 | The controller is direct-acting. |

Default value: Reverse

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### PI gains

Proportional gain and integral gain parameters of the controller.

This output can return a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Integral gain of the controller.

#### Algorithm Definition

The following transfer function represents a PI controller in the Parallel form:

C

p

(

s

)

=

K

p

′

+

K

i

′

s

C

p

(

s

)

=

K

p

′

+

K

i

′

s

where

K

p

′

K

i

′

Parent topic:

Create Gain

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=create-gain-schedule-pi.html language=enus -->
## TOPIC 00006: PI

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `create-gain-schedule-pi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/create-gain-schedule-pi.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns gain scheduling values of the parameters for a PI controller. PI gains Proportional gain and integral gain parameters of the controller. This input accepts a cluster or an array of clusters. proportional Proportional gain of the controller. integral Integral time constant of the controller,

PI

Returns gain scheduling values of the parameters for a PI controller.

[IMAGE alt='1378' src='Create_PI_Gain_Schedule_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### PI gains

Proportional gain and integral gain parameters of the controller.

This input accepts a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### integral

Integral time constant of the controller, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### maximum

Maximum value of the range of the gain scheduling values.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### PI gain schedule

Gain scheduling values for the controller parameters.

This output can return a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### PI gains

Proportional gain and integral gain parameters of the controller.

This output can return a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Integral gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### maximum

Maximum value of the range of the gain scheduling values.

Parent topic:

Create Gain Schedule

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=dead-zone.html language=enus -->
## TOPIC 00007: Dead Zone

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `dead-zone.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/dead-zone.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a dead zone function by providing a region of zero output. input Input signal. This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers. start of dead zone Low end of the dead zone. This input accepts a double-precision, floating

Dead Zone

Implements a dead zone function by providing a region of zero output.

[IMAGE alt='1378' src='Dead_Zone_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### input

Input signal.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### start of dead zone

Low end of the dead zone.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### end of dead zone

High end of the dead zone.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Output signal.

This output can return a double-precision, floating-point number or an array of double-precision, floating-point numbers.

#### Algorithm Definition for the Dead Zone Function

The following equation defines the dead zone function.

y

=

{

0

if

⁢

s

≤

u

≤

e

u

−

s

⁢

if

⁢

u

<

s

u

−

e

⁢

if

⁢

u

>

e

y

=

{

0

if

⁢

s

≤

u

≤

e

u

−

s

⁢

if

⁢

u

<

s

u

−

e

⁢

if

⁢

u

>

e

where

- u is the input signal
- y is the output signal
- s is the low end of the dead zone
- e is the high end of the dead zone

Parent topic:

Non-Linear Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=dual-gain-schedule.html language=enus -->
## TOPIC 00008: Dual Gain Schedule

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `dual-gain-schedule.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/dual-gain-schedule.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects a set of gains from a gain schedule for either rising or falling values. gain scheduling value Current input value to use to select gains from the gain schedule. This input accepts a floating-point, double-precision number or an array of floating-point, double-precision numbers. gain schedul

Dual Gain Schedule

Selects a set of gains from a gain schedule for either rising or falling values.

[IMAGE alt='1378' src='PID_Dual_Direction_Gain_Schedule_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gain scheduling value

Current input value to use to select gains from the gain schedule.

This input accepts a floating-point, double-precision number or an array of floating-point, double-precision numbers.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### gain schedule for rising value

Gain values for the control parameters and maximum value of the rising gain scheduling values.

This node uses the first set of gain values for all the gain scheduling values less than the corresponding maximum value.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### gain

Proportional gain, integral gain, derivative gain, or filter coefficient parameter of the controller.

This input accepts a double-precision, floating-point number or a cluster. The data type and cluster elements change according to the controller type. This node supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### maximum

Maximum value of the range of the gain scheduling values.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### gain schedule for falling value

Gain values for the control parameters and maximum value of the falling gain scheduling values.

This node uses the first set of gain values for all the gain scheduling values less than the corresponding maximum value.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### gain

Proportional gain, integral gain, derivative gain, or filter coefficient parameter of the controller.

This input accepts a double-precision, floating-point number or a cluster. The data type and cluster elements change according to the controller type. This node supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### maximum

Maximum value of the range of the gain scheduling values.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### gain schedule option

Gain scheduling values from which to select a set of gains.

This input accepts a ring or an array of rings.

| rising gain schedule | 0 | Specifies that the node selects a set of gains from gain schedule for rising value. |
| --- | --- | --- |
| falling gain schedule | 1 | Specifies that the node selects a set of gains from gain schedule for falling value. |

Default value: rising gain schedule

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### gain out

Current gains from the gain schedule.

This output can return the following data types:

- Double-precision, floating-point number
- Array of double-precision, floating-point numbers
- Cluster
- Array of clusters

The data type and cluster elements change according to the controller type. This node
 supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### gains out

Current gains from the gain schedule.

This output can return the following data types:

- Double-precision, floating-point number
- Array of double-precision, floating-point numbers
- Cluster
- Array of clusters

The data type and cluster elements change according to the controller type. This node supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### index

Index of the element in the gain schedule corresponding to gains out.

This output can return a 32-bit signed integer or an array of 32-bit signed integers.

#### Programming Patterns

You can call the Create Gain Schedule node to obtain the gain schedule for a controller before using this node.

#### Cluster Elements for Different Controller Types

The following table shows the elements the input and output gain clusters contain for different controller types.

| Controller Type | Gain Cluster Elements |
| --- | --- |
| P | proportional gain |
| PD | proportional gain, derivative gain, and derivative lowpass filter coefficient |
| PI | proportional gain and integral gain |
| PID | proportional gain, integral gain, derivative gain, and derivative lowpass filter coefficient |

Parent topic:

PID Gains Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=friction.html language=enus -->
## TOPIC 00009: Friction

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `friction.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/friction.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a discontinuity at zero with linear behavior elsewhere. input Input signal. This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers. gain Slope of the friction element. This input accepts a double-precision, floating-point numbe

Friction

Implements a discontinuity at zero with linear behavior elsewhere.

[IMAGE alt='1378' src='Friction_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### input

Input signal.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gain

Slope of the friction element.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### offset

Offset of the friction element.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Output signal.

This output can return a double-precision, floating-point number or an array of double-precision, floating-point numbers.

#### Algorithm for Computing the Output Signal

The node uses the following equation to implement a discontinuity at zero with linear behavior elsewhere.

y

=

{

0

if

⁢

u

=

0

u

*

gain

+

offset

⁢

if

⁢

u

>

0

u

*

gain

−

offset

⁢

if

⁢

u

<

0

y

=

{

0

if

⁢

u

=

0

u

*

gain

+

offset

⁢

if

⁢

u

>

0

u

*

gain

−

offset

⁢

if

⁢

u

<

0

where y is the output signal and u is the input signal.

Parent topic:

Non-Linear Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=gain-schedule.html language=enus -->
## TOPIC 00010: Gain Schedule

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `gain-schedule.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/gain-schedule.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects a set of gains from a gain schedule. gain scheduling value Current input value to use to select gains from the gain schedule. This input accepts a floating-point, double-precision number or an array of floating-point, double-precision numbers. gain schedule Gain values for the control parame

Gain Schedule

Selects a set of gains from a gain schedule.

[IMAGE alt='1378' src='PID_Gain_Schedule_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gain scheduling value

Current input value to use to select gains from the gain schedule.

This input accepts a floating-point, double-precision number or an array of floating-point, double-precision numbers.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### gain schedule

Gain values for the control parameters and maximum value of the gain scheduling values.

This node uses the first set of gain values for all the gain scheduling values less than the corresponding maximum value.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### gain

Proportional gain, integral gain, derivative gain, or filter coefficient parameter of the controller.

This input accepts a double-precision, floating-point number or a cluster. The data type and cluster elements change according to the controller type. This node supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### maximum

Maximum value of the range of the gain scheduling values.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### gain out

Current gains from the gain schedule.

This output can return the following data types:

- Double-precision, floating-point number
- Array of double-precision, floating-point numbers
- Cluster
- Array of clusters

The data type and cluster elements change according to the controller type. This node
 supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### gains out

Current gains from the gain schedule.

This output can return the following data types:

- Double-precision, floating-point number
- Array of double-precision, floating-point numbers
- Cluster
- Array of clusters

The data type and cluster elements change according to the controller type. This node supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### index

Index of the element in the gain schedule corresponding to gains out.

This output can return a 32-bit signed integer or an array of 32-bit signed integers.

#### Programming Patterns

You can call the Create Gain Schedule node to obtain the gain schedule for a controller before using this node.

#### Cluster Elements for Different Controller Types

The following table shows the elements the input and output gain clusters contain for different controller types.

| Controller Type | Gain Cluster Elements |
| --- | --- |
| P | proportional gain |
| PD | proportional gain, derivative gain, and derivative lowpass filter coefficient |
| PI | proportional gain and integral gain |
| PID | proportional gain, integral gain, derivative gain, and derivative lowpass filter coefficient |

Parent topic:

PID Gains Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=insert-gain-schedule.html language=enus -->
## TOPIC 00011: Insert Gain Schedule

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `insert-gain-schedule.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/insert-gain-schedule.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a gain schedule element to a gain schedule so that the maximum value of the inserted element is greater than the preceding maximum value in the gain schedule. gain schedule in Gain values for the control parameters and maximum value of the gain scheduling values. gain Proportional gain, inte

Insert Gain Schedule

Inserts a gain schedule element to a gain schedule so that the maximum value of the inserted element is greater than the preceding maximum value in the gain schedule.

[IMAGE alt='1378' src='Insert_PID_Gain.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### gain schedule in

Gain values for the control parameters and maximum value of the gain scheduling values.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### gain

Proportional gain, integral gain, derivative gain, or filter coefficient parameter of the controller.

This input accepts a double-precision, floating-point number or a cluster. The data type and cluster elements change according to the controller type. This node supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### maximum

Maximum value of the range of the gain scheduling values.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### gain schedule element

Gain scheduling values to insert to the gain schedule.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### gain

Proportional gain, integral gain, derivative gain, or filter coefficient parameter of the controller.

This input accepts a double-precision, floating-point number or a cluster. The data type and cluster elements change according to the controller type. This node supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### maximum

Maximum value of the range of the gain scheduling values.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### gain schedule out

Output gain schedule.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### gain

Proportional gain, integral gain, derivative gain, or filter coefficient parameter of the controller.

This output can return a double-precision, floating-point number or a cluster. The data type and cluster elements change according to the controller type. This node supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### maximum

Maximum value of the range of the gain scheduling values.

#### Programming Patterns

You can call the Create Gain Schedule node to obtain the gain schedule for a controller before using this node.

#### Cluster Elements for Different Controller Types

The following table shows the elements the input and output gain clusters contain for different controller types.

| Controller Type | Gain Cluster Elements |
| --- | --- |
| P | proportional gain |
| PD | proportional gain, derivative gain, and derivative lowpass filter coefficient |
| PI | proportional gain and integral gain |
| PID | proportional gain, integral gain, derivative gain, and derivative lowpass filter coefficient |

Parent topic:

PID Gains Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=lead-lag.html language=enus -->
## TOPIC 00012: Lead Lag

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `lead-lag.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/lead-lag.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a PID controller with a lead or lag function, which is generally used as a dynamic compensator in feedforward control schemes. reset A Boolean or a Boolean array that specifies the initialization of the internal state of the node. True Initializes the output to the current input value. Fa

Lead Lag

Implements a PID controller with a lead or lag function, which is generally used as a dynamic compensator in feedforward control schemes.

[IMAGE alt='1378' src='Lead-Lag_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean or a Boolean array that specifies the initialization of the internal state of the node.

| True | Initializes the output to the current input value. |
| --- | --- |
| False | Does not initialize the output to the current input value. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### input

Input signal.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### tuning parameters

Tuning parameters to adjust the controller.

This input accepts a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gain

DC gain. Setting gain to a negative value produces an inverting amplifier with an additional 180-degree phase shift.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### lag time

Phase lag in seconds. A value of zero turns off the lag.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### lead time

Phase lead in seconds. A value of zero turns off the lead. Large lead time values might result in a wild oscillation of the output.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time or interval, in seconds, at which this node is called.

dt must be greater than zero.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

This output can return a double-precision, floating-point number or an array of double-precision, floating-point numbers.

Parent topic:

Control Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=pid-design-ziegler-nichols.html language=enus -->
## TOPIC 00013: Ziegler-Nichols

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `pid-design-ziegler-nichols.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/pid-design-ziegler-nichols.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements autotuning using the Ziegler-Nichols tuning method. Ziegler-Nichols speed Desired response performance of the PID parameters. Fast 0 Specifies a fast response performance. Faster response generally results in a smaller rise time. Normal 1 Specifies a normal response performance. Slow 2 Sp

Ziegler-Nichols

Implements autotuning using the Ziegler-Nichols tuning method.

[IMAGE alt='1378' src='PID_Autotuning_Design_(Ziegler-Nichols).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### Ziegler-Nichols speed

Desired response performance of the PID parameters.

| Fast | 0 | Specifies a fast response performance. Faster response generally results in a smaller rise time. |
| --- | --- | --- |
| Normal | 1 | Specifies a normal response performance. |
| Slow | 2 | Specifies a slow response performance. Slower response generally results in less overshoot. |

Default value: Fast

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### type of controller

Parameters to return as PID gains.

| P | 0 | Returns only the proportional parameters. |
| --- | --- | --- |
| PI | 1 | Returns the proportional and integral parameters. |
| PID | 2 | Returns the proportional, integral, and derivative parameters. |

Default value: P

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### stimulus signal

Stimulus signal for the system.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### response signal

Response signal of the system.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### closed-loop?

A Boolean that specifies whether the system is a closed-loop system.

| True | The system is a closed-loop system. The node estimates open-loop parameter values based on the closed-loop values the node identifies from the input signals. |
| --- | --- |
| False | The system is not a closed-loop system. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### controller gain

Initial value for the controller gain.

This node uses this input to calculate integral of PID gains.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time or interval, in seconds, at which this node is called.

dt must be greater than zero.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### PID gains

Proportional gain, integral gain, derivative gain, and filter coefficient parameters of the controller.

This output can return a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Integral gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Derivative gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### filter coefficient [a]

Derivative lowpass filter coefficient of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### stimulus operating point

Stimulus offset for the plant.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### response operating point

Response offset for the plant.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### plant parameters

Gain, time constant, and dead time of the plant.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Plant Gain (K)

Process gain (K).

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Time Constant (T)

Time constant (T), in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Dead Time (L)

Dead time (L), in seconds.

Parent topic:

PID Design

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=pid-gains-nodes.html language=enus -->
## TOPIC 00014: PID Gains Nodes

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `pid-gains-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/pid-gains-nodes.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implement Proportional-Integral-Derivative (PID) control applications.

PID Gains Nodes

Implement Proportional-Integral-Derivative (PID) control applications.

Control Nodes

Convert Gain

Converts gains in the Academic, Parallel, or Series form to the form you specify.

Create Gain

Returns gain values of a controller.

Create Gain Schedule

Returns gain scheduling values of controller parameters.

Dual Gain Schedule

Selects a set of gains from a gain schedule for either rising or falling values.

Gain Schedule

Selects a set of gains from a gain schedule.

Insert Gain Schedule

Inserts a gain schedule element to a gain schedule so that the maximum value of the inserted element is greater than the preceding maximum value in the gain schedule.

Measures of Integral of Error

Measures the performance of a control system by calculating the integral of the controller error.

PID Design

Implements autotuning.

Sort Gain Schedule

Returns a sorted version of a gain schedule with maximum values arranged in ascending order.

Parent topic:

Control Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=pid-multimode-function.html language=enus -->
## TOPIC 00015: PID

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `pid-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/pid-multimode-function.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a Proportional-Integral-Derivative (PID) controller.

PID

Implements a Proportional-Integral-Derivative (PID) controller.

Control Nodes

P

Implements a P controller.

Parent topic:

Control Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=pid-p.html language=enus -->
## TOPIC 00016: P

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `pid-p.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/pid-p.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a P controller. feedforward input Value of the feedforward control. This input accepts an array of double-precision, floating-point numbers if setpoint is an array. manual control Settings for the manual control mode. This input accepts an array of clusters if setpoint is an array. manual

P

Implements a P controller.

[IMAGE alt='1378' src='P_Continuous_Academic_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### feedforward input

Value of the feedforward control.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### manual control

Settings for the manual control mode.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### manual

A Boolean that specifies whether to use the manual control mode.

| True | Uses the manual control mode. |
| --- | --- |
| False | Uses the automatic control mode. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### manual input

Value of the control output when you use the manual control mode.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal parameters, such as the integrated error, of the controller.

| True | Resets the internal parameters. |
| --- | --- |
| False | Does not reset the internal parameters. |

Set reset to True if your application must stop and restart the control loop without restarting the entire application.

This input accepts an array of Booleans if setpoint is an array.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint value, or desired value, of the process variable.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### process variable

Measured value of the process variable.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional gain

Proportional gain of the controller.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### output range

Range for the control output value.

If the control output value is outside output range, this node coerces the value to fall within the range and returns the coerced value as the control output value.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output high

Maximum control output value.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output low

Minimum control output value.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time, or interval in seconds, at which this node is called.

dt

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional weighting [beta]

Relative emphasis of setpoint tracking to disturbance rejection.

The valid value range is [0, 1]. Use the default value for most applications.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### error

Difference between the setpoint and the process variable.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### actions

Values of the proportional action, the integral action, and the derivative action in the PID algorithm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Value of the proportional action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Value of the integral action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Value of the derivative action.

#### Algorithm Definition

The following transfer function represents a P controller:

C

(

s

)

=

K

p

C

(

s

)

=

K

p

where K<sub>p</sub> is the proportional gain.

Parent topic:

PID

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=pid-pd-parallel.html language=enus -->
## TOPIC 00017: Parallel

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `pid-pd-parallel.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/pid-pd-parallel.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a PD controller in the Parallel form. feedforward input Value of the feedforward control. This input accepts an array of double-precision, floating-point numbers if setpoint is an array. manual control Settings for the manual control mode. This input accepts an array of clusters if setpoi

Parallel

Implements a PD controller in the Parallel form.

[IMAGE alt='1378' src='PD_Continuous_Parallel_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### feedforward input

Value of the feedforward control.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### manual control

Settings for the manual control mode.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### manual

A Boolean that specifies whether to use the manual control mode.

| True | Uses the manual control mode. |
| --- | --- |
| False | Uses the automatic control mode. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### manual input

Value of the control output when you use the manual control mode.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal parameters, such as the integrated error, of the controller.

| True | Resets the internal parameters. |
| --- | --- |
| False | Does not reset the internal parameters. |

Set reset to True if your application must stop and restart the control loop without restarting the entire application.

This input accepts an array of Booleans if setpoint is an array.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint value, or desired value, of the process variable.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### process variable

Measured value of the process variable.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### PD gains

Proportional gain and derivative gain parameters of the controller.

This input accepts a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### derivative

Derivative gain of the controller, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### filter coefficient [a]

Derivative lowpass filter coefficient of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### output range

Range for the control output value.

If the control output value is outside output range, this node coerces the value to fall within the range and returns the coerced value as the control output value.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output high

Maximum control output value.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output low

Minimum control output value.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time, or interval in seconds, at which this node is called.

dt

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### setpoint weighting

Corrections to apply to the error values of the controller.

setpoint weighting

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional weighting [beta]

Relative emphasis of setpoint tracking to disturbance rejection.

The valid value range is [0, 1]. Use the default value for most applications.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### derivative weighting [gamma]

An amount by which to weight the error applied to the derivative action.

The valid value range is [0, 1]. Use the default value to avoid the derivative kick.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### error

Difference between the setpoint and the process variable.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### actions

Values of the proportional action, the integral action, and the derivative action in the PID algorithm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Value of the proportional action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Value of the integral action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Value of the derivative action.

#### Algorithm Definition

The following transfer function represents a PD controller in the Parallel form:

C

p

(

s

)

=

K

p

′

+

K

d

′

s

α

p

K

d

′

s

+

1

C

p

(

s

)

=

K

p

′

+

K

d

′

s

α

p

K

d

′

s

+

1

where

K

p

′

K

d

′

α

p

Parent topic:

PID

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=pid-pi-academic.html language=enus -->
## TOPIC 00018: Academic

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `pid-pi-academic.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/pid-pi-academic.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a PI controller in the Academic form. feedforward input Value of the feedforward control. This input accepts an array of double-precision, floating-point numbers if setpoint is an array. manual control Settings for the manual control mode. This input accepts an array of clusters if setpoi

Academic

Implements a PI controller in the Academic form.

[IMAGE alt='1378' src='PI_Continuous_Academic_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### feedforward input

Value of the feedforward control.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### manual control

Settings for the manual control mode.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### manual

A Boolean that specifies whether to use the manual control mode.

| True | Uses the manual control mode. |
| --- | --- |
| False | Uses the automatic control mode. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### manual input

Value of the control output when you use the manual control mode.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal parameters, such as the integrated error, of the controller.

| True | Resets the internal parameters. |
| --- | --- |
| False | Does not reset the internal parameters. |

Set reset to True if your application must stop and restart the control loop without restarting the entire application.

This input accepts an array of Booleans if setpoint is an array.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint value, or desired value, of the process variable.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### process variable

Measured value of the process variable.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### PI gains

Proportional gain and integral gain parameters of the controller.

This input accepts a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### integral

Integral time constant of the controller, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### output range

Range for the control output value.

If the control output value is outside output range, this node coerces the value to fall within the range and returns the coerced value as the control output value. This node implements integrator anti-windup when the control output is saturated at the specified minimum or maximum value.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output high

Maximum control output value.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output low

Minimum control output value.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time, or interval in seconds, at which this node is called.

dt

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional weighting [beta]

Relative emphasis of setpoint tracking to disturbance rejection.

The valid value range is [0, 1]. Use the default value for most applications.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### error

Difference between the setpoint and the process variable.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### actions

Values of the proportional action, the integral action, and the derivative action in the PID algorithm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Value of the proportional action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Value of the integral action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Value of the derivative action.

#### Algorithm Definition

The following transfer function represents a PI controller in the Academic form:

C

i

(

s

)

=

K

c

(

1

+

1

T

i

s

)

C

i

(

s

)

=

K

c

(

1

+

1

T

i

s

)

where K<sub>c</sub> is the proportional gain and T<sub>i</sub> is the integral time constant.

Parent topic:

PID

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=pid-pi-parallel.html language=enus -->
## TOPIC 00019: Parallel

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `pid-pi-parallel.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/pid-pi-parallel.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a PI controller in the Parallel form. feedforward input Value of the feedforward control. This input accepts an array of double-precision, floating-point numbers if setpoint is an array. manual control Settings for the manual control mode. This input accepts an array of clusters if setpoi

Parallel

Implements a PI controller in the Parallel form.

[IMAGE alt='1378' src='PI_Continuous_Parallel_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### feedforward input

Value of the feedforward control.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### manual control

Settings for the manual control mode.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### manual

A Boolean that specifies whether to use the manual control mode.

| True | Uses the manual control mode. |
| --- | --- |
| False | Uses the automatic control mode. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### manual input

Value of the control output when you use the manual control mode.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal parameters, such as the integrated error, of the controller.

| True | Resets the internal parameters. |
| --- | --- |
| False | Does not reset the internal parameters. |

Set reset to True if your application must stop and restart the control loop without restarting the entire application.

This input accepts an array of Booleans if setpoint is an array.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint value, or desired value, of the process variable.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### process variable

Measured value of the process variable.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### PI gains

Proportional gain and integral gain parameters of the controller.

This input accepts a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### integral

Integral gain of the controller, in Hz.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### output range

Range for the control output value.

If the control output value is outside output range, this node coerces the value to fall within the range and returns the coerced value as the control output value. This node implements integrator anti-windup when the control output is saturated at the specified minimum or maximum value.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output high

Maximum control output value.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output low

Minimum control output value.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time, or interval in seconds, at which this node is called.

dt

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional weighting [beta]

Relative emphasis of setpoint tracking to disturbance rejection.

The valid value range is [0, 1]. Use the default value for most applications.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### error

Difference between the setpoint and the process variable.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### actions

Values of the proportional action, the integral action, and the derivative action in the PID algorithm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Value of the proportional action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Value of the integral action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Value of the derivative action.

#### Algorithm Definition

The following transfer function represents a PI controller in the Parallel form:

C

p

(

s

)

=

K

p

′

+

K

i

′

s

C

p

(

s

)

=

K

p

′

+

K

i

′

s

where

K

p

′

K

i

′

Parent topic:

PID

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=pid-pid-academic.html language=enus -->
## TOPIC 00020: Academic

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `pid-pid-academic.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/pid-pid-academic.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a PID controller in the Academic form. feedforward input Value of the feedforward control. This input accepts an array of double-precision, floating-point numbers if setpoint is an array. manual control Settings for the manual control mode. This input accepts an array of clusters if setpo

Academic

Implements a PID controller in the Academic form.

[IMAGE alt='1378' src='PID_Continuous_Academic_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### feedforward input

Value of the feedforward control.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### manual control

Settings for the manual control mode.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### manual

A Boolean that specifies whether to use the manual control mode.

| True | Uses the manual control mode. |
| --- | --- |
| False | Uses the automatic control mode. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### manual input

Value of the control output when you use the manual control mode.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal parameters, such as the integrated error, of the controller.

| True | Resets the internal parameters. |
| --- | --- |
| False | Does not reset the internal parameters. |

Set reset to True if your application must stop and restart the control loop without restarting the entire application.

This input accepts an array of Booleans if setpoint is an array.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint value, or desired value, of the process variable.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### process variable

Measured value of the process variable.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### PID gains

Proportional gain, integral gain, derivative gain, and filter coefficient parameters of the controller.

This input accepts a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### integral

Integral time constant of the controller, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### derivative

Derivative time constant of the controller, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### filter coefficient [a]

Derivative lowpass filter coefficient of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### output range

Range for the control output value.

If the control output value is outside output range, this node coerces the value to fall within the range and returns the coerced value as the control output value. This node implements integrator anti-windup when the control output is saturated at the specified minimum or maximum value.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output high

Maximum control output value.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output low

Minimum control output value.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time, or interval in seconds, at which this node is called.

dt

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### setpoint weighting

Corrections to apply to the error values of the controller.

setpoint weighting

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional weighting [beta]

Relative emphasis of setpoint tracking to disturbance rejection.

The valid value range is [0, 1]. Use the default value for most applications.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### derivative weighting [gamma]

An amount by which to weight the error applied to the derivative action.

The valid value range is [0, 1]. Use the default value to avoid the derivative kick.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### error

Difference between the setpoint and the process variable.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### actions

Values of the proportional action, the integral action, and the derivative action in the PID algorithm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Value of the proportional action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Value of the integral action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Value of the derivative action.

#### Algorithm Definition

The following transfer function represents a PID controller in the Academic form:

C

i

(

s

)

=

K

c

(

1

+

1

T

i

s

+

T

d

s

α

i

T

d

s

+

1

)

C

i

(

s

)

=

K

c

(

1

+

1

T

i

s

+

T

d

s

α

i

T

d

s

+

1

)

where

- K 
 c is the proportional gain
- T 
 i is the integral time constant
- T 
 d is the derivative time constant
- α
 i is the derivative filter coefficient

Parent topic:

PID

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=pid-pid-parallel.html language=enus -->
## TOPIC 00021: Parallel

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `pid-pid-parallel.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/pid-pid-parallel.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a PID controller in the Parallel form. feedforward input Value of the feedforward control. This input accepts an array of double-precision, floating-point numbers if setpoint is an array. manual control Settings for the manual control mode. This input accepts an array of clusters if setpo

Parallel

Implements a PID controller in the Parallel form.

[IMAGE alt='1378' src='PID_Continuous_Parallel_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### feedforward input

Value of the feedforward control.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### manual control

Settings for the manual control mode.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### manual

A Boolean that specifies whether to use the manual control mode.

| True | Uses the manual control mode. |
| --- | --- |
| False | Uses the automatic control mode. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### manual input

Value of the control output when you use the manual control mode.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal parameters, such as the integrated error, of the controller.

| True | Resets the internal parameters. |
| --- | --- |
| False | Does not reset the internal parameters. |

Set reset to True if your application must stop and restart the control loop without restarting the entire application.

This input accepts an array of Booleans if setpoint is an array.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint value, or desired value, of the process variable.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### process variable

Measured value of the process variable.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### PID gains

Proportional gain, integral gain, derivative gain, and filter coefficient parameters of the controller.

This input accepts a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### integral

Integral gain of the controller, in Hz.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### derivative

Derivative gain of the controller, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### filter coefficient [a]

Derivative lowpass filter coefficient of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### output range

Range for the control output value.

If the control output value is outside output range, this node coerces the value to fall within the range and returns the coerced value as the control output value. This node implements integrator anti-windup when the control output is saturated at the specified minimum or maximum value.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output high

Maximum control output value.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output low

Minimum control output value.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time, or interval in seconds, at which this node is called.

dt

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### setpoint weighting

Corrections to apply to the error values of the controller.

setpoint weighting

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional weighting [beta]

Relative emphasis of setpoint tracking to disturbance rejection.

The valid value range is [0, 1]. Use the default value for most applications.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### derivative weighting [gamma]

An amount by which to weight the error applied to the derivative action.

The valid value range is [0, 1]. Use the default value to avoid the derivative kick.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### error

Difference between the setpoint and the process variable.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### actions

Values of the proportional action, the integral action, and the derivative action in the PID algorithm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Value of the proportional action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Value of the integral action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Value of the derivative action.

#### Algorithm Definition

The following transfer function represents a PID controller in the Parallel form:

C

p

(

s

)

=

K

p

′

+

K

i

′

s

+

K

d

′

s

α

p

K

d

′

s

+

1

C

p

(

s

)

=

K

p

′

+

K

i

′

s

+

K

d

′

s

α

p

K

d

′

s

+

1

where

- K
 p
 ′ is the proportional gain
- K
 i
 ′ is the integral gain
- K
 d
 ′ is the derivative gain
- α
 p is the derivative filter coefficient

Parent topic:

PID

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=pid-pid-series.html language=enus -->
## TOPIC 00022: Series

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `pid-pid-series.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/pid-pid-series.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a PID controller in the Series form. feedforward input Value of the feedforward control. This input accepts an array of double-precision, floating-point numbers if setpoint is an array. manual control Settings for the manual control mode. This input accepts an array of clusters if setpoin

Series

Implements a PID controller in the Series form.

[IMAGE alt='1378' src='PID_Continuous_Series_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### feedforward input

Value of the feedforward control.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### manual control

Settings for the manual control mode.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### manual

A Boolean that specifies whether to use the manual control mode.

| True | Uses the manual control mode. |
| --- | --- |
| False | Uses the automatic control mode. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### manual input

Value of the control output when you use the manual control mode.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal parameters, such as the integrated error, of the controller.

| True | Resets the internal parameters. |
| --- | --- |
| False | Does not reset the internal parameters. |

Set reset to True if your application must stop and restart the control loop without restarting the entire application.

This input accepts an array of Booleans if setpoint is an array.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint value, or desired value, of the process variable.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### process variable

Measured value of the process variable.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### PID gains

Proportional gain, integral gain, derivative gain, and filter coefficient parameters of the controller.

This input accepts a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### integral

Integral time constant of the controller, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### derivative

Derivative time constant of the controller, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### filter coefficient [a]

Derivative lowpass filter coefficient of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### output range

Range for the control output value.

If the control output value is outside output range, this node coerces the value to fall within the range and returns the coerced value as the control output value. This node implements integrator anti-windup when the control output is saturated at the specified minimum or maximum value.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output high

Maximum control output value.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output low

Minimum control output value.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time, or interval in seconds, at which this node is called.

dt

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### setpoint weighting

Corrections to apply to the error values of the controller.

setpoint weighting

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional weighting [beta]

Relative emphasis of setpoint tracking to disturbance rejection.

The valid value range is [0, 1]. Use the default value for most applications.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### derivative weighting [gamma]

An amount by which to weight the error applied to the derivative action.

The valid value range is [0, 1]. Use the default value to avoid the derivative kick.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### error

Difference between the setpoint and the process variable.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### actions

Values of the proportional action, the integral action, and the derivative action in the PID algorithm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Value of the proportional action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Value of the integral action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Value of the derivative action.

#### Algorithm Definition

The following transfer function represents a PID controller in the Series form:

C

s

(

s

)

=

K

c

′

(

1

+

1

T

I

′

s

)

(

T

D

′

s

+

1

α

s

T

D

′

s

+

1

)

C

s

(

s

)

=

K

c

′

(

1

+

1

T

I

′

s

)

(

T

D

′

s

+

1

α

s

T

D

′

s

+

1

)

where

- K
 c
 ′ is the proportional gain
- T
 I
 ′ is the integral time constant
- T
 D
 ′ is the derivative time constant
- α
 s is the derivative filter coefficient

Parent topic:

PID

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=profile-generation-nodes.html language=enus -->
## TOPIC 00023: Profile Generation Nodes

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `profile-generation-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/profile-generation-nodes.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generate a profile of setpoint values.

Profile Generation Nodes

Generate a profile of setpoint values.

Control Nodes

Setpoint Profile

Generates setpoint values over time in a control loop for ramp and soak types of control applications.

Step Signal

Generates the point-by-point value of a step signal.

Parent topic:

Control Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=setpoint-profile.html language=enus -->
## TOPIC 00024: Setpoint Profile

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `setpoint-profile.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/setpoint-profile.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates setpoint values over time in a control loop for ramp and soak types of control applications. reset A Boolean that specifies the initialization of the internal state of the node. True Initializes the output to setpoint profile at time t = 0. False Does not initialize the internal state of t

Setpoint Profile

Generates setpoint values over time in a control loop for ramp and soak types of control applications.

[IMAGE alt='1378' src='Setpoint_Profile.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies the initialization of the internal state of the node.

| True | Initializes the output to setpoint profile at time t = 0. |
| --- | --- |
| False | Does not initialize the internal state of the node. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/c1dnclst.png']

##### setpoint profile

An array of time and setpoint value pairs that define the profile of the setpoint as a function of time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### time (s)

Time values in the setpoint profile. Specify time (s) in ascending order.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint values in the setpoint profile.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time or interval, in seconds, at which this node is called.

dt must be greater than zero.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### setpoint

Setpoint value this node calculates from setpoint profile and from the elapsed time since the first call or reinitialization of this node.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### profile complete?

A Boolean that indicates whether the elapsed time is greater than or equal to the last defined time value in setpoint profile.

| True | The elapsed time is greater than or equal to the last defined time value in setpoint profile. |
| --- | --- |
| False | The elapsed time is less than the last defined time value in setpoint profile. |

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### elapsed time

Elapsed time, in seconds, since the first call of the node or since the reinitialization of the node.

Parent topic:

Profile Generation Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=sort-gain-schedule.html language=enus -->
## TOPIC 00025: Sort Gain Schedule

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `sort-gain-schedule.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/sort-gain-schedule.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a sorted version of a gain schedule with maximum values arranged in ascending order. gain schedule in Gain values for the control parameters and maximum value of the gain scheduling values. gain Proportional gain, integral gain, derivative gain, or filter coefficient parameter of the control

Sort Gain Schedule

Returns a sorted version of a gain schedule with maximum values arranged in ascending order.

[IMAGE alt='1378' src='Sort_PID_Gain.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### gain schedule in

Gain values for the control parameters and maximum value of the gain scheduling values.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### gain

Proportional gain, integral gain, derivative gain, or filter coefficient parameter of the controller.

This input accepts a double-precision, floating-point number or a cluster. The data type and cluster elements change according to the controller type. This node supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### maximum

Maximum value of the range of the gain scheduling values.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### gain schedule out

Output gain schedule.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### gain

Proportional gain, integral gain, derivative gain, or filter coefficient parameter of the controller.

This output can return a double-precision, floating-point number or a cluster. The data type and cluster elements change according to the controller type. This node supports the following controller types:

- P (Proportional)
- PI (Proportional-Integral)
- PD (Proportional-Derivative)
- PID (Proportional-Integral-Derivative)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### maximum

Maximum value of the range of the gain scheduling values.

#### Programming Patterns

You can call the Create Gain Schedule node to obtain the gain schedule for a controller before using this node.

#### Cluster Elements for Different Controller Types

The following table shows the elements the input and output gain clusters contain for different controller types.

| Controller Type | Gain Cluster Elements |
| --- | --- |
| P | proportional gain |
| PD | proportional gain, derivative gain, and derivative lowpass filter coefficient |
| PI | proportional gain and integral gain |
| PID | proportional gain, integral gain, derivative gain, and derivative lowpass filter coefficient |

Parent topic:

PID Gains Nodes

<!--NI_TOPIC bundle=labview-nxg-analysis-control-api-ref path=step-signal.html language=enus -->
## TOPIC 00026: Step Signal

- bundle_id: `labview-nxg-analysis-control-api-ref`
- source_path: `step-signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-analysis-control-api-ref/raw/resource/enus/step-signal.html
- document_id: `labview-nxg-analysis-control-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates the point-by-point value of a step signal. reset A Boolean that specifies the initialization of the internal state of the node. True Initializes the internal state of the node by returning the output at time t = 0. False Does not initialize the internal state of the node. Default value: Fa

Step Signal

Generates the point-by-point value of a step signal.

[IMAGE alt='1378' src='Step_Signal_(Scalar_DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies the initialization of the internal state of the node.

| True | Initializes the internal state of the node by returning the output at time t = 0. |
| --- | --- |
| False | Does not initialize the internal state of the node. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### amplitude

Amplitude of the step signal.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### offset

Lower limit of the step signal.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### step time

Simulation time, in seconds, at which the output changes from offset to offset + amplitude.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time or interval, in seconds, at which this node is called.

dt must be greater than zero.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### step output

Point-by-point value of the step signal.

#### Algorithm Definition for the Step Signal

The following equations define the step signal:

y

=

{

u

⁢

if

⁢

t

<

step

⁢

time

u

+

a

⁢

if

⁢

t

≥

step

⁢

time

y

=

{

u

⁢

if

⁢

t

<

step

⁢

time

u

+

a

⁢

if

⁢

t

≥

step

⁢

time

where

- y is the step signal
- u is the lower limit of the step signal
- a is the amplitude of the step signal
- t is the current simulation time

Parent topic:

Profile Generation Nodes
