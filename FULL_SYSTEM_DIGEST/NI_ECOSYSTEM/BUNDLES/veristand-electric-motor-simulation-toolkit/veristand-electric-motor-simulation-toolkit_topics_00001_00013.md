# NI DOCUMENT BUNDLE: veristand-electric-motor-simulation-toolkit

<!--NI_BUNDLE_CHUNK bundle=veristand-electric-motor-simulation-toolkit start=1 end=13 -->
<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=ansys-motor-model-file.html language=enus -->
## TOPIC 00001: ANSYS Motor Model File

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `ansys-motor-model-file.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/ansys-motor-model-file.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: ANSYS is a company that provides engineering simulation solutions. The ANSYS motor model file is the motor model file that the ANSYS simulation software generates. The ANSYS motor model file is in the TXT file format. The TXT file contains basic motor characteristics, such as the three-phase resista

### ANSYS Motor Model File

ANSYS is a company that provides engineering simulation solutions. The ANSYS motor model file is
 the motor model file that the ANSYS simulation software generates. The ANSYS motor model
 file is in the TXT file format. The TXT file
 contains basic motor characteristics, such as the three-phase resistances and the number
 of poles. The TXT file also contains detailed motor parameters
 information, which are the analysis results of the ANSYS simulation software.

You can use the Electric Motor Simulation Toolkit to read an ANSYS motor model file if you use
 the variable parameter model for permanent magnet synchronous motors (PMSM). Refer to
 the ANSYS Incorporated website at
 www.ansys.com for more
 information about the ANSYS simulation software and the ANSYS motor model files.

Related concepts:

- Variable Parameter Model
- Supported Motor Types

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=base-value.html language=enus -->
## TOPIC 00002: Base Value

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `base-value.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/base-value.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Apart from the engineering units, electrical engineers also use per-unit to measure quantities in physics. A per-unit system expresses system quantities as fractions of a defined base unit quantity. The per-unit system scales the actual value of a physical quantity, such as current, voltage, and spe

### Base Value

Apart from the engineering units, electrical engineers also use per-unit to measure quantities in physics. A per-unit system expresses system quantities as fractions of a defined base unit quantity. The per-unit system scales the actual value of a physical quantity, such as current, voltage, and speed, with a selected constant of the same measuring unit. The ratio of the actual value to the constant is the per-unit value of the physical quantity. The selected constant, also known as base value, has the same measuring unit as the actual value.

The following equation explains the relationship between a per-unit value and a base value.

Per-unit Value

=

Real Value (any unit)

Base Value (same unit as the Real Value)

For example, suppose you have two voltages, U<sub>1</sub>=99 KV and U<sub>2</sub>=110 KV. When
 selecting 110 KV as the base value of voltages, you can express the per-unit
 value of U<sub>1</sub> and U<sub>2</sub> as follows.

U

1

=

U

1

U

2

=

99

110

=

0

.

9

U

2

=

U

2

U

2

=

110

110

=

1

.

0

The results show that the real value of U<sub>1</sub> is 0.9 times of the base value, while the
 real value of U<sub>2</sub> is the same as the base value. In other words, the per-unit value
 of U<sub>1</sub> is 0.9 and the per-unit value of U<sub>2</sub> is 1.

The per-unit system is ideal for fixed-point implementation. Per-unit helps to make the
 fixed-point model usable for various motors. All quantities are multiples of the base value
 that you select.

#### Troubleshooting Improper Base Value Error

When you use the Electric
 Motor Simulation VIs to generate FPGA data for electric motor simulation, an error occurs if
 improper base values lead to overflow. Complete the following steps
 to resolve the error.

1. Keep the value of speed base as default.
2. Gradually increase the value of current base . Keep the per-unit
 value of the maximum current within the range from 0.1 to 10. For example, suppose the
 maximum current of an electric motor is 300 A, you can select a value in the range from
 30 A to 3000 A as the current base.
3. Gradually increase the value of voltage base . Keep the per-unit
 value of the maximum voltage within the range from 0.1 to 10.
4. Repeat steps 2 and 3 until the error stops occurring.

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=constant-parameter-model.html language=enus -->
## TOPIC 00003: Constant Parameter Model

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `constant-parameter-model.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/constant-parameter-model.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the constant parameter model function to simulate an AC induction motor (ACIM) or a permanent magnet synchronous motor (PMSM). Constant Parameter Model for ACIM SimulationThe constant parameter model simulates the electromagnetic behavior of an ACIM by using the (α,β) orthogonal coordinate syste

### Constant Parameter Model

Use the constant parameter model function to simulate an AC induction motor (ACIM) or a permanent
 magnet synchronous motor (PMSM).

#### Constant Parameter Model for ACIM Simulation

The constant parameter model
 simulates the electromagnetic behavior of an ACIM by using the (α,β) orthogonal
 coordinate system.

In an (α,β) orthogonal coordinate system, the α axis
 usually coincides with the direction of the A current of the three-phase current in
 the stator. The β axis is the axis at an angle of 90 degrees from the α
 axis.

The following figure illustrates the relationship between the (α,β)
 orthogonal coordinate system and the three-phase current.

[IMAGE alt='image' src='GUID-378A6BAE-046C-4BEE-864F-5CFBF54C9310-a5.gif']

Because of the three-phase current in the stator windings, the magnetizing
 currents of the stator produce a magnetic field. The magnetic field generates a
 current in the rotor. The voltage equations for ACIM simulation with the constant
 parameter model are as follows.

V

s

α

=

R

s

I

s

α

+

d

d

t

λ

s

α

V

s

β

=

R

s

I

s

β

+

d

d

t

λ

s

β

V

r

α

=

R

r

I

r

α

+

ω

r

λ

r

β

+

d

d

t

λ

r

α

=

0

V

r

β

=

R

r

I

r

β

+

ω

r

λ

r

α

+

d

d

t

λ

r

β

=

0

Where

V<sub>sα</sub> is the stator voltage along the α
 axis,

V<sub>sβ</sub> is the stator voltage along the β
 axis,

R<sub>s</sub> is the stator resistance,

I<sub>sα</sub> is the
 stator current along the α axis,

I<sub>sβ</sub> is the stator current along
 the β axis,

λ<sub>sα</sub> is the stator flux linkage along the α
 axis,

λ<sub>sβ</sub> is the stator flux linkage along the β
 axis,

V<sub>rα</sub> is the rotor voltage along the α
 axis,

V<sub>rβ</sub> is the rotor voltage along the β
 axis,

R<sub>r</sub> is the rotor resistance,

I<sub>rα</sub> is the
 rotor current along the α axis,

I<sub>rβ</sub> is the rotor current along the
 β axis,

λ<sub>rα</sub> is the rotor flux linkage along the α
 axis,

λ<sub>rβ</sub> is the rotor flux linkage along the β
 axis,

ω<sub>r</sub> is the electrical speed, in rad/s, which equals to
 rotor speed times the number of pole pairs.

The flux linkage equations are as
 follows.

λ

sα

=

(

L

ls

+

L

m

)

I

sα

+

L

lm

I

rα

λ

s

β

=

(

L

ls

+

L

m

)

I

s

β

+

L

lm

I

r

β

λ

r

α

=

(

L

l

r

+

L

m

)

I

r

α

+

L

m

I

s

α

λ

r

β

=

(

L

l

r

+

L

m

)

I

r

β

+

L

m

I

s

β

Where

L<sub>ls</sub> is the stator leakage inductance,

L<sub>lr</sub>
 is the rotor leakage inductance,

L<sub>m</sub> is the magnetizing
 inductance.

The voltage equations calculate the derivatives of stator flux
 linkage and rotor flux linkage.

λ

s

α

(

k

)

=

V

s

α

k

-

R

s

I

s

α

k

-

1

d

t

+

λ

s

α

k

-

1

λ

s

β

(

k

)

=

V

s

β

k

-

R

s

I

s

β

k

-

1

d

t

+

λ

s

β

k

-

1

λ

r

α

(

k

)

=

-

R

r

I

r

α

k

-

1

-

ω

r

λ

r

β

k

-

1

d

t

+

λ

r

α

k

-

1

λ

r

β

(

k

)

=

-

R

r

I

r

β

k

-

1

-

ω

r

λ

r

α

k

-

1

d

t

+

λ

r

β

k

-

1

where k and k-1 are the simulation steps. For example, λ<sub>sα</sub>(k) is the
 stator flux linkage along the α axis at the k step, while λ<sub>sα</sub>(k-1) is the
 stator flux linkage along the α axis at the k-1 step.

The flux linkage
 equations calculate the current by defining λ<sub>mα</sub>, λ<sub>mβ</sub>, and
 L<sub>M</sub>.

λ

m

α

=

L

M

λ

s

α

L

I

s

+

λ

r

α

L

l

r

λ

m

β

=

L

M

λ

s

β

L

I

s

+

λ

r

β

L

l

r

L

M

=

1

L

ls

+

1

L

lr

+

1

L

M

-

1

The following equations can be derived to obtain the current in the (α,β)
 orthogonal coordinate system.

I

s

α

=

λ

s

α

-

λ

m

α

L

I

s

I

s

β

=

λ

s

β

-

λ

m

β

L

I

s

I

r

α

=

λ

r

α

-

λ

m

α

L

I

r

I

r

β

=

λ

r

β

-

λ

m

β

L

I

r

The constant parameter model calculates the electric torque of an ACIM by using
 the following equation.

T

e

=

3

2

P

2

λ

s

α

I

s

β

-

λ

s

β

I

s

α

where p is the number of poles.

#### Constant Parameter Model for PMSM Simulation

The constant parameter model
 simulates the electromagnetic behavior of a PMSM by using the d-q axes mathematical
 method.

The d-q axes are the axes in a (d,q) coordinate system. The d axis, or
 the direct axis, usually coincides with the axis of the rotor magnet pole. The q
 axis, or the quad axis, is the axis at an angle of 90 degrees from the d axis. When
 the rotor is stationary, the (d,q) coordinate system is a stationary reference
 frame. When the rotor starts rotating, the system is a rotor reference frame where
 the (d,q) coordinate system rotates at the rotor speed.

The following figure
 illustrates a (d,q) coordinate system.

[IMAGE alt='image' src='GUID-36AB9039-E027-493A-A374-666A21AA2069-a5.gif']

While the rotor is rotating, electromagnetic current is generated inside the
 electric motor. The voltage equations of the (d,q) rotor reference frame are as
 follows.

V

d

=

R

I

d

-

ω

r

λ

q

+

d

d

t

λ

d

V

q

=

R

I

q

-

ω

r

λ

d

+

d

d

t

λ

q

The flux linkage equations are as follows.

λ

d

=

L

d

I

d

+

λ

f

λ

q

=

L

q

I

q

where

ω<sub>r</sub> is electrical speed, in rad/s, which equals to rotor
 speed times the number of pole pairs

I<sub>d</sub> is the current along the d
 axis,

λ<sub>d</sub> is the flux linkage along the d axis,

λ<sub>q</sub>
 is the flux linkage along the q axis,

λ<sub>f</sub> is the flux linkage in the
 rotor magnet,

L<sub>d</sub> is the inductance along the d
 axis,

L<sub>q</sub> is the inductance along the q axis.

The
 following equation calculates the electric torque of the (d,q) rotor reference
 frame.

T

e

=

3

2

P

2

λ

d

I

q

-

λ

q

I

d

=

3

2

P

2

λ

f

I

q

+

L

d

-

L

q

I

d

I

q

where p is the number of poles.

The following discrete equations calculate
 the current for PMSM simulation with the constant parameter model.

I

d

k

=

d

t

L

d

V

d

k

-

R

I

d

k

-

1

+

ω

r

L

q

I

q

k

-

1

+

I

d

k

-

1

I

q

k

=

d

t

L

q

V

q

k

-

R

I

q

k

-

1

-

ω

r

λ

f

-

ω

r

L

d

I

d

k

-

1

+

I

q

k

-

1

where k and k-1 are the simulation steps. For example, I<sub>d</sub>(k) is the
 current along the d axis at the k step, while I<sub>d</sub>(k-1) is the current
 along the d axis at the k-1 step.

Related concepts:

- Supported Motor Types

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=creating-and-configuring-custom-devices.html language=enus -->
## TOPIC 00004: Creating and Configuring Custom Devices

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `creating-and-configuring-custom-devices.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/creating-and-configuring-custom-devices.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create an Electric Motor Simulation custom device in your VeriStand project, open the System Explorer window, navigate to Targets»Controller»Custom Devices, right-click Custom Devices, and select a custom device for electric motor simulation from the shortcut menu. Specify a RIO device and an FPG

### Creating and Configuring Custom Devices

To create an Electric Motor Simulation custom device in your VeriStand project, open the
 System Explorer window, navigate to
 Targets»Controller»Custom Devices, right-click
 Custom Devices, and select a custom device for electric motor
 simulation from the shortcut menu. Specify a RIO device and an FPGA bitfile in the
 Configure FPGA dialog box. A new custom device appears under
 Custom Devices in the configuration tree.

The Electric Motor Simulation custom device contains the following channels and folders.

Inputs channel

Inverter Model channel

Log file channel

Outputs channel

Status channel

Waveforms channel

To view or configure a custom device, select the custom device name in the configuration tree of
 the System Explorer window. The Custom Device
 Configuration page appears to the right of the configuration tree. The
 configuration options that appear can vary depending on the different motor type or
 model type that you select.

Related information:

- Electric Motor Simulation Custom
 Devices
- Configure FPGA Dialog Box

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=fea-model.html language=enus -->
## TOPIC 00005: FEA Model

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `fea-model.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/fea-model.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The finite element analysis (FEA) model function implements high-fidelity model simulation of an electric motor. The FEA model takes real motor characteristics into account and uses the FEA method to describe the motor behaviors.In mathematics, the FEA method is a numerical technique to find approxi

### FEA Model

The finite element analysis (FEA) model function implements high-fidelity model simulation of an
 electric motor. The FEA model takes real motor characteristics into account and uses the
 FEA method to describe the motor behaviors.

In mathematics, the FEA method is a numerical technique to find approximate solutions to boundary
 value problems. This method connects many simple element equations over many small
 subdomains, named finite elements, to approximate a more complex equation over a larger
 domain.

In mechanics and computer science, the FEA method is also a method of mechanical computer
 simulation and a computational tool to perform engineering analysis. The FEA model uses
 software programs based on finite element method algorithms to divide a complex problem
 into smaller elements.

The FEA model function obtains real motor characteristics from the RTT files. Among the
 characteristics, motor parameters are analyzed using the FEA method. As part of the
 simulation process, the FEA model function looks up the motor parameters and
 characteristics in these files.

The FEA model uses the following voltage equation to calculate the current for a PMSM.

[IMAGE alt='image' src='GUID-8BA54542-7FBA-4955-9F00-3CFED03EBD4A-a5.gif']

where

V<sub>a</sub>, V<sub>b</sub>, and V<sub>c</sub> are the three-phase voltages,

R is the phase resistance,

I<sub>a</sub>, I<sub>b</sub>, and I<sub>c</sub> are the three-phase currents,

L'<sub>aa</sub>, L'<sub>bb</sub>, and L'<sub>cc</sub> are the differential
 self-inductances,

L'<sub>ab</sub>, L'<sub>ac</sub>, L'<sub>ba</sub>, L'<sub>bc</sub>, L'<sub>ca</sub>, and
 L'<sub>cb</sub> are the differential mutual inductances,

λ<sub>a</sub>, λ<sub>b</sub>, and λ<sub>c</sub> are the magnetic fluxes generated by the
 permanent magnet.

The FEA model uses the following voltage equation to calculate the current for a three-phase SRM.

[IMAGE alt='image' src='GUID-C75DEC4C-4B7C-4E0D-9EF8-7E3C89FCE7DD-a5.gif']

where

L<sub>aa</sub>, L<sub>bb</sub>, and L<sub>cc</sub> are the self-inductances,

L<sub>ab</sub>, L<sub>ac</sub>, L<sub>ba</sub>, L<sub>bc</sub>, L<sub>ca</sub>, and
 L<sub>cb</sub> are the mutual inductances.

Related concepts:

- RTT File

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=linear-model.html language=enus -->
## TOPIC 00006: Linear Model

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `linear-model.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/linear-model.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The switched reluctance motor (SRM) shows strong nonlinearity because the flux of a stator winding depends on both the phase current and the rotor position. Therefore, the linear model utilizes the piece-wise linear method to describe the flux of an SRM.In an SRM, the non-linear characteristics of t

### Linear Model

The switched reluctance motor (SRM) shows strong nonlinearity because the flux of a stator
 winding depends on both the phase current and the rotor position. Therefore, the linear model
 utilizes the piece-wise linear method to describe the flux of an SRM.

In an SRM, the non-linear characteristics of the magnet affect the operation of the SRM. High
 levels of saturation occur cyclically as the rotor continuously moves from an unaligned
 position to an aligned position, with reference to the poles on the stator. The
 following figure depicts different rotor positions.

[IMAGE alt='image' src='GUID-EFEE7EA8-77DF-4628-98A9-1083C941392E-a5.gif']

The positions are specific to one of the phases. The aligned position means that the pole of the
 rotor and the pole of the stator are in the same line. The unaligned position means that
 the rotor of the specific phase is completely detached from the stator. The middle
 position is when the pole of the rotor has intersection with the pole of the stator. The
 flux linkage of the motor phase varies at different positions.

The SRM linear model function complies with the following equations.

Phase voltage equation:

V

=

RI

+

d

λ

d

t

=

R

I

+

∂

λ

∂

1

dI

dt

+

∂

λ

∂

θ

dθ

dt

Instant torque equation:

T

I

,

θ

=

∫

0

I

∂

λ

∂

θ

d

I

where

λ is the flux linkage,

θ is the rotor position,

R is the resistance,

I is the current,

V is the voltage,

T is the torque.

The following figure shows an analytical expression for the flux linkage of a linear model. The
 aligned and unaligned curves represent the flux changes at the aligned position and
 unaligned position. The two curves in the middle represent the flux changes at the
 middle positions.

[IMAGE alt='image' src='GUID-ACBC2C0F-3F1E-402B-A901-B0B5C55B1898-a5.gif']

In the following figure, the curves with dots show the flux linkage of a real motor at different
 rotor position. The curves without dots represent the linear model approximation.

[IMAGE alt='image' src='GUID-14633A1D-C080-496E-931A-3BBA6F1F0E3D-a5.gif']

The slope of the straight line in the figure approximates the flux curve for the unaligned position, as shown in the following equation.

λ

u

=

L

u

I

where L<sub>u</sub> is a constant that represents the equivalent inductance of the coil for the
 unaligned position. The u subscript means unaligned.

For aligned positions, when I is no greater than I<sub>s</sub>,

λ

a

=

λ

s

I

s

I

where λ<sub>a</sub> is the flux of I<sub>s</sub> at the aligned position. The a subscript means
 aligned and the s subscript means saturated.

When I is greater than I<sub>s</sub>,

λ

a

=

L

u

I

-

I

s

+

λ

s

The dependency of λ on the rotor position θ is approximated by a sine wave oscillating between
 the maximum value λ<sub>a</sub>(I) and the minimum value λ<sub>u</sub>(I), as
 illustrated in the following equation.

λ

=

1

2

λ

a

-

λ

u

cos

2

p

θ

+

1

+

λ

u

where p is the number of poles in pairs.

From the previous equations, a linear model function solves the current and torque in the
 SRM.

When I is no greater than I<sub>s</sub>,

I

k

=

V

k

d

t

+

1

2

λ

s

I

s

-

L

u

(

cos

2

p

θ

k

+

1

)

+

L

u

I

k−1

R

d

t

+

1

2

λ

s

I

s

-

L

u

(

cos

2

p

θ

k

+

1

)

+

L

u

−

p

sin

2

p

θ

k

λ

s

I

s

-

L

u

d

θ

where the k subscript indicates the variable calculated at the k step, while the k-1 subscript
 indicates the variable calculated at the k-1 step. For example,
 I<sub>k</sub> is the phase current at the k step,
 while I<sub>k-1</sub> is the phase current at the k-1 step.

T

k

=

-

p

sin

2

p

θ

k

λ

s

I

s

-

L

u

I

k

-

1

2

2

When I is greater than I<sub>s</sub>,

I

k

=

V

k

d

t

+

L

u

I

k

-

1

+

p

sin

2

p

θ

k

λ

s

-

L

u

I

s

d

θ

R

d

t

+

L

u

T

k

=

-

p

sin

2

p

θ

k

λ

s

-

L

u

I

s

I

k

-

1

-

I

s

2

Related concepts:

- Supported Motor Types

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=overview.html language=enus -->
## TOPIC 00007: VeriStand Electric Motor Simulation Toolkit Overview

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/overview.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Electric motor simulation is the process of imitating the control and operation of a real-world electric motor over time. The simulated electric motor is typically a part of the hardware-in-the-loop (HIL) simulation, which is widely used in the development and test of complex real-time embedded syst

### VeriStand Electric Motor Simulation
 Toolkit
 Overview

Electric motor simulation is the process of imitating the control and operation of a
 real-world electric motor over time. The simulated electric motor is typically a part of
 the hardware-in-the-loop (HIL) simulation, which is widely used in the development and
 test of complex real-time embedded systems. Simulating an electric motor that runs in
 the HIL system allows you to design and debug the application without depending on the
 physical electric motor.

- validate the mechanical parameters of the motor,
- test algorithms for controlling the motor behaviors,
- verify if the simulated motor works with the controller and I/O modules in the
 HIL system before you deploy and run the application on real hardware.

With the Electric Motor Simulation Toolkit, you use the palette VIs, examples, and sample
 projects to design an HIL system and model the motion of real electric motors in a
 real-world system.

You configure the motor parameters and test the control algorithms with efficiency in a
 simulated system. When you can ensure that the control algorithms work satisfactorily,
 replace the simulated motor with a real electric motor.

You can further replace the control algorithms with a real controller, such as an
 electronic control unit (ECU).

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=rtt-file.html language=enus -->
## TOPIC 00008: RTT File

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `rtt-file.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/rtt-file.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RTT file, or the JMAG-RT motor model, is a third-party product provided by the JSOL company. The file, with an extension of .rtt, contains basic motor characteristics, such as the motor type, connection type, and number of poles. The RTT file also contains detailed motor parameters information, w

### RTT File

An RTT file, or the JMAG-RT motor model, is a third-party product provided by the JSOL company.
 The file, with an extension of .rtt, contains basic motor
 characteristics, such as the motor type, connection type, and number of poles. The RTT
 file also contains detailed motor parameters information, which are the analysis results
 of the JMAG-RT software.

You can use the Electric Motor Simulation Toolkit to read an RTT file for the FEA model or the
 variable parameter model. You can either download RTT files from the JSOL website at
 www.jmag-international.com or create an RTT file by using the JMAG-RT software.

Related concepts:

- Variable Parameter Model
- FEA Model

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=supported-motor-types.html language=enus -->
## TOPIC 00009: Supported Motor Types

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `supported-motor-types.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/supported-motor-types.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Electric Motor Simulation Toolkit allows you to simulate the following types of electric motors. AC induction motors (ACIM) Permanent magnet synchronous motors (PMSM) Switched reluctance motors (SRM) ACIMAn ACIM is a type of electric motor that has a stationary stator outside and a rotor which s

### Supported Motor Types

The Electric Motor Simulation Toolkit allows you to simulate the following types of electric
 motors.

- AC induction motors (ACIM)
- Permanent magnet synchronous motors (PMSM)
- Switched reluctance motors (SRM)

#### ACIM

An ACIM is a type of electric motor
 that has a stationary stator outside and a rotor which spins inside. By supplying
 alternating current to the stator, the ACIM uses the electromagnet of the stator to
 generate current in the rotor and produce torque. The stator is a hollow metal
 cylinder with slots for coils of wires. The rotor consists of metal bars which have
 end rings at both ends to form short circuits. The following figure illustrates a
 typical ACIM.

[IMAGE alt='image' src='GUID-0D4506BA-7218-418E-B000-A516D8BB16D4-a5.gif']

#### PMSM

A PMSM is a type of electric motor
 that utilizes permanent magnets in the rotor. The poles of a PMSM indicates how many
 even numbers of magnet poles that the rotor has. The following figure is an example
 of a typical PMSM. This motor has four permanent magnets on the rotor, as shown in
 the figure.

[IMAGE alt='image' src='GUID-FB6E50DF-5B2C-4D4F-BD4B-17E5E19D7B1E-a5.gif']

#### SRM

An SRM is a type of electric motor
 that produces torque from a slight misalignment of poles on the rotor with poles on
 the stator. The rotor tends to align itself with the stator to maximize the
 inductance of the stator, while the stator is consequently energized to force the
 rotor to rotate. The phase of the SRM indicates the number of pole pairs in the
 stator. For example, the following figure illustrates a three-phase SRM. The stator
 of this motor has three pairs of poles.

[IMAGE alt='image' src='GUID-525C264D-4FA7-4117-9027-CAEE145E7C92-a5.gif']

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=temperature-correction.html language=enus -->
## TOPIC 00010: Temperature Correction

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `temperature-correction.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/temperature-correction.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Temperature correction is a functionality that simulates the changes of resistance, magnet flux, or torque in an electric motor according to temperature variations. In a permanent magnet synchronous motor (PMSM), when the magnet temperature and the coil temperature change, the resistance and the mag

### Temperature Correction

Temperature correction is a functionality that simulates the changes of resistance, magnet flux,
 or torque in an electric motor according to temperature variations. In a permanent
 magnet synchronous motor (PMSM), when the magnet temperature and the coil temperature
 change, the resistance and the magnet flux change accordingly. Magnet temperature
 variations also affect the electromagnetic torque. In an AC induction motor (ACIM), when
 the rotor temperature and the stator temperature change, the rotor resistance and the
 stator resistance change accordingly.

The Electric Motor Simulation Toolkit provides the temperature correction functionality
 for ACIM simulation with the constant parameter model and PMSM simulation with the FEA
 and the variable parameter models.

To perform the temperature correction functionality, you must obtain motor parameters for
 temperature correction. By using the Electric Motor Simulation VIs, you can either
 manually specify the temperature correction parameters, or obtain the temperature
 correction parameters from an RTT file.

The following equation calculates the PMSM coil resistance, the ACIM stator resistance, and the
 ACIM rotor resistance after temperature correction:

R

'

=

R

1

+

k

T

-

T

b

a

s

e

where

R' is the resistance after temperature correction,

R is the resistance under the base temperature before temperature correction,

k is the temperature correction coefficient,

T<sub>base</sub> is the base temperature.

The following equation calculates the PMSM magnet flux after temperature correction:

F

'

=

F

1

+

k

m

T

m

-

T

m

-

b

a

s

e

where

F' is the magnet flux after temperature correction,

F is the magnet flux under the magnet base temperature before temperature correction,

k<sub>m</sub> is the magnet temperature correction coefficient,

T<sub>m</sub> is the real-time magnet temperature,

T<sub>m-base</sub> is the magnet base temperature.

Related concepts:

- Constant Parameter Model
- Variable Parameter Model
- FEA Model
- RTT File

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=three-phase-inverter.html language=enus -->
## TOPIC 00011: Three-Phase Inverter

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `three-phase-inverter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/three-phase-inverter.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An inverter is an electrical device that converts direct current (DC) to alternating current (AC). A three-phase inverter is a commonly-used inverter for powering a variable-speed motor like the permanent magnet synchronous motor (PMSM). The three-phase inverter consists of three single-phase branch

### Three-Phase Inverter

An inverter is an electrical device that converts direct current (DC) to alternating current (AC). A three-phase inverter is a commonly-used inverter for powering a variable-speed motor like the permanent magnet synchronous motor (PMSM). The three-phase inverter consists of three single-phase branches which connect to three load terminals. Each single-phase branch contains two power switches. The following figure illustrates the circuit diagram of a three-phase inverter. In this circuit, the three resistances represent the load. In real applications, the load can be an electric motor.

[IMAGE alt='image' src='GUID-AA3305D2-3899-4337-B706-E35C26FEF786-a5.gif']

where

S<sub>au</sub> is the phase A upper switch,

S<sub>al</sub> is the phase A lower switch,

S<sub>bu</sub> is the phase B upper switch,

S<sub>bl</sub> is the phase B lower switch,

S<sub>cu</sub> is the phase C upper switch,

S<sub>cl</sub> is the phase C lower switch,

V<sub>ab</sub>, V<sub>bc</sub>, and V<sub>ca</sub> are the line-to-line voltages,

V<sub>a</sub>, V<sub>b</sub>, and V<sub>c</sub> are the phase voltages.

The Electric Motor Simulation Toolkit allows you to simulate an ideal three-phase inverter or an
 advanced three-phase inverter. In the ideal three-phase inverter model, the switches are
 simple on-off switches. When the switch is on, no voltage drop happens on the switch.
 When the switch is off, no current flows through the switch. In the advanced three-phase
 inverter model, the switches are insulated gate bipolar transistors (IGBT) with diodes.
 The advanced three-phase inverter model simulates the transient behavior of the
 inverter. By using the advanced three-phase inverter model, you can specify the forward
 voltage drops of the switches and insert fault to the inverter at run time.

#### Ideal Three-Phase Inverter Model

The ideal three-phase inverter model
 assumes that the switch state changes between on and off instantaneously. The two
 switches in the same single-phase branch are complementary. The following table
 lists the phase voltages and line-to-line voltages of the ideal three-phase inverter
 model. V<sub>DC</sub> is the DC voltage that connects to the inverter. In the
 Switch State column, 1 indicates that the switch is on,
 while 0 indicates that the switch is off.

| Switch State |  |  | Phase Voltage (V) |  |  | Line-to-Line Voltage (V) |  |  |
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

The Electric Motor Simulation Toolkit only calculates the phase voltages. The
 following equations demonstrate the relationship between the line-to-line voltages
 and the phase voltages.

V

a

b

=

V

a

-

V

b

V

b

c

=

V

b

-

V

c

V

c

a

=

V

c

-

V

a

#### Advanced Three-Phase Inverter Model

The advanced three-phase inverter
 model regards the IGBT-with-diode switch as a small inductance (L) when the switch
 is on. When the switch is off, the model regards the switch as a small capacitance
 (C). A conductance (G) in parallel with a dependent current source (J) represents a
 switch. The following figure illustrates how the advanced three-phase inverter model
 simulates the switch.

[IMAGE alt='image' src='GUID-7FA07553-3F83-49CD-AFE3-AC27A37FF3F7-a5.gif']

The advanced three-phase inverter model regards the conductance as a constant to
 simplify the calculation process. The following equations show the relationship
 between the conductance and the simulation time interval (dt).

G

=

d

t

L

G

=

C

d

t

d

t

=

L

c

The following equation determines the current source. The subscript k and k-1
 denote the simulation steps.

J

k

=

-

-

I

k

-

1

i

f

s

k

=

1

G

V

k

-

1

i

f

s

k

=

0

where

I<sub>k-1</sub> is the current on the switch at the k-1
 step,

V<sub>k-1</sub> is the voltage on the switch at the k-1
 step,

s<sub>k</sub>=1 denotes that the switch is on at the k
 step,

s<sub>k</sub>=0 denotes that the switch is off at the k
 step.

The following equation determines the state of the IGBT-with-diode
 switch.

s

k

=

g

k

+

s

k

-

1

I

k

-

1

≤

0

+

s

k

-

1

V

k

-

1

<

0

where

s

#### Inserting Fault to the
 Inverter

The advanced three-phase inverter model allows you to simulate the behavior of an
 inverter when the switch has faults. The model provides four types of faults and
 only supports one fault at a time. The four fault types are as follows.

IGBT open fault

Diode open fault

IGBT and diode open fault

IGBT or diode short fault

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00012: VeriStand Electric Motor Simulation Toolkit User Manual

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The VeriStand Electric Motor Simulation Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse R

### VeriStand Electric Motor Simulation
 Toolkit
 User Manual

The VeriStand Electric Motor Simulation
 Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System
 Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit path=variable-parameter-model.html language=enus -->
## TOPIC 00013: Variable Parameter Model

- bundle_id: `veristand-electric-motor-simulation-toolkit`
- source_path: `variable-parameter-model.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit/raw/resource/enus/variable-parameter-model.html
- document_id: `veristand-electric-motor-simulation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the variable parameter model function to implement medium-fidelity model simulation of a permanent magnet synchronous motor (PMSM). Like the constant parameter model, the variable parameter model uses the voltage equations, flux linkage equations, and torque equation of the (d,q) rotor reference

### Variable Parameter Model

Use the variable parameter model function to implement medium-fidelity model simulation of a
 permanent magnet synchronous motor (PMSM). Like the constant parameter model, the
 variable parameter model uses the voltage equations, flux linkage equations, and torque
 equation of the (d,q) rotor reference frame. Unlike the constant parameter model, the
 motor inductance in the variable parameter model is a variable due to magnet saturation.
 The variable parameter model can obtain real motor characteristics from an RTT file, an
 ANSYS motor model file, or an external model.

The variable parameter model uses the following discrete equations to calculate the current for a
 PMSM.

I

d

k

=

V

d

k

+

ω

r

L

q

k

-

1

I

q

k

-

1

d

t

+

I

d

k

-

1

L

d

k

-

1

-

λ

f

k

-

1

-

λ

f

k

-

2

R

d

t

+

2

L

d

k

-

1

-

L

d

k

-

2

I

q

k

=

V

q

k

+

ω

r

L

d

k

-

1

I

d

k

-

1

+

λ

f

k

-

1

d

t

+

I

q

k

-

1

L

q

k

-

1

R

d

t

+

2

L

q

k

-

1

-

L

q

k

-

2

where

ω<sub>r</sub> is electrical speed, in rad/s, which equals to rotor speed times the number
 of pole,

R is the resistance,

V<sub>d</sub> is the voltage along the d axis,

V<sub>q</sub> is the voltage along the q axis,

λ<sub>d</sub> is the flux linkage along the d axis,

λ<sub>q</sub> is the flux linkage along the q axis,

λ<sub>f</sub> is the flux linkage in the rotor magnet,

λ<sub>f</sub> is the flux linkage in the rotor magnet,

L<sub>d</sub> is the inductance along the d axis,

L<sub>q</sub> is the inductance along the q axis,

k, k-1, and k-2 are the simulation steps.

For example, I<sub>d</sub>(k) is the current along the d axis at the k step. I<sub>d</sub>(k-1)
 is the current along the d axis at the k-1 step. L<sub>q</sub>(k-2) is the inductance
 along the q axis at the k-2 step.

#### External Model

An external model is a
 model function you create by using the Electric Motor Simulation Toolkit. You can
 import the external model to get motor characteristics for simulating a PMSM with
 the variable parameter model. Motor characteristics include number of poles,
 resistance, temperature correction parameters, direct inductance table, quad
 inductance table, flux table, and so on.

Related concepts:

- Supported Motor Types
- Constant Parameter Model
- RTT File
- ANSYS Motor Model File
- Temperature Correction
