# NI DOCUMENT BUNDLE: labview-pid-and-fuzzy-logic-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref start=1 end=15 -->
<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/multiloop_control.html language=enus -->
## TOPIC 00001: Multi-Loop Control

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/multiloop_control.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/multiloop_control.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Multi-Loop Control

Most of the [PID](../lvpid/pidtitle.html) VIs are polymorphic VIs for use in multiple control-loop applications. For example, you can design a multi-loop PID control application using the [PID](../lvpid/pid_vi.html) VI and DAQ functions for input and output. A DAQ analog input function returns an array of data when you configure
it for multiple channels. You can wire this array directly into the **process variable** input of the PID VI. The polymorphic type of the PID VI automatically switches from DBL to DBL Array, which calculates and returns an array of output values corresponding to the number of values in the **process variable** array. You also can switch the type of the polymorphic VI manually by right-clicking the VI icon and selecting **Select Type** from the shortcut menu.

When the polymorphic type is DBL Array, other inputs automatically change to array inputs as well. For example, the [PID](../lvpid/pid_vi.html) VI inputs **setpoint**, **PID gains**, and **output range** all become array inputs. Each of these inputs can have an array length ranging from 1 to the array length of the **process variable** input. If the array length of any of these inputs is less than the array length of the **process variable** input, the PID VI reuses the last value in the array for other calculations. For example, if you specify only one set of PID gains in the **PID gains** array, the PID VI uses these gains to calculate each **output** value corresponding to each **process variable** input value. Other polymorphic PID and Fuzzy Logic VIs operate in the same manner.

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/onesteptuning.html language=enus -->
## TOPIC 00002: Programmatically Implementing and Autotuning a PID Controller

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/onesteptuning.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/onesteptuning.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Programmatically Implementing and Autotuning a PID Controller

You can use the [PID Advanced Autotuning](../lvpid/pid_advanced_autotuning.html) VI both to implement and autotune a PID controller.

|  | Note The PID Advanced Autotuning VI incorporates the functionality of the PID Advanced VI and the PID Online Autotuning VI. You also can use the PID Online Autotuning VI to programmatically autotune a previously implemented PID controller. |
| --- | --- |

Complete the following steps to implement a tuned PID controller with the [PID Advanced Autotuning](../lvpid/pid_advanced_autotuning.html) VI.

1. Add the PID Advanced Autotuning VI to the block diagram within a control loop.
2. Wire the inputs you want to use to implement the controller. Minimally, wire the setpoint , process variable , and PID gains inputs.
3. Create a control for the autotuning parameters input and select the controller type and control specification you want to use.
4. Set the technique component of the autotuning parameters input to the autotuning technique you want to use.
5. Create a Boolean control with latched mechanical action and a default value of FALSE for the Autotune? input.
6. Run the VI.
7. Set Autotune? to TRUE to begin autotuning.

Refer to the Autotuning PID Online VI in the labview\examples\control\PID for an example of implementing autotuning with the [PID Advanced Autotuning](../lvpid/pid_advanced_autotuning.html) VI.

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/percent_to_eng.html language=enus -->
## TOPIC 00003: Converting Between Percentage of Full Scale and Engineering Units

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/percent_to_eng.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/percent_to_eng.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Converting Between Percentage of Full Scale and Engineering Units

The default setpoint, process variable, and output ranges for the [PID](../lvpid/pidtitle.html) VIs correspond to percentage of full scale. In other words, proportional gain (*K<sub>c</sub>*) relates percentage of full scale output to percentage of full scale input. This is the default behavior of many PID controllers used for process control applications. To implement PID in this way, you must scale all inputs to percentage of full scale and all controller outputs to actual engineering units, for example, volts for analog output.

You can use the [PID EGU to Percentage](../lvpid/pidegutopercent.html) VI to convert any input from real engineering units to percentage of full scale, and you can use the [PID Percentage to EGU](../lvpid/pidpercenttoegu.html) VI to convert the controller output from percentage to real engineering units.

|  | Note The PID VIs do not use the setpoint range and output range information to convert values to percentages in the PID algorithm. The controller gain relates the output in engineering units to the input in engineering units. For example, a gain value of 1 produces an output of 10 for a difference between setpoint and process variable of 10, regardless of the output range and setpoint range. |
| --- | --- |

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/pid_glossary.html language=enus -->
## TOPIC 00004: PID and Fuzzy Logic Glossary

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/pid_glossary.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/pid_glossary.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PID and Fuzzy Logic Glossary

ABCDEFGIKLMNOPQRSTW

| A |  |
| --- | --- |
| algorithm | A prescribed set of well-defined rules or processes for the solution of a problem in a finite number of steps. |
| antecedent | The IF portion of a rule in a fuzzy system. |
| antecedent connective | An operator that specifies how to calculate the truth value of an aggregated rule antecedent. |
| anti-reset windup | A method that prevents the integral term of the PID algorithm from moving too far beyond saturation when an error persists. |
| autotuning | Automatically testing a process under control to determine the controller gains that will provide the best controller performance. |
| Autotuning Wizard | An automated graphical user interface provided in the PID Autotuning VI. The Autotuning Wizard gathers some information about the desired control from the user and then steps through the PID autotuning process. |
| B |  |
| bias | The offset added to a controller output (manipulate variable). |
| Boolean set theory | Traditional set theory based on strict membership or non-membership of elements to a set. Examples are TRUE or FALSE, ON or OFF, 1 or 0, and so on. |
| bumpless transfer | A process in which the next output always increments from the current output, regardless of the current controller output value; therefore, transfer from automatic to manual control is always bumpless. |
| C |  |
| cascade control | Control in which the output of one controller is the setpoint for another controller. |
| Center of Area (CoA) | Method of defuzzification in which the crisp output is determined by the geometrical center of area of the composite output membership functions within the range of the output linguistic variable. Also known as Center of Gravity (CoG). |
| Center of Maximum (CoM) | Method of defuzzification in which the crisp output is determined by a weighted average of the typical values of each output membership function. This method is equivalent to the Center of Area method using singleton sets. |
| Center of Sums (CoS) | Method of defuzzification in which the crisp output is determined by a weighted average of the center of area of each output membership function. |
| closed loop | A signal path which includes a forward path, a feedback path, and a summing point and which forms a closed circuit. Also called a feedback loop. |
| consequent | The THEN portion of a rule in a fuzzy system. |
| controller | Hardware and/or software used to maintain parameters of a physical process at desired values. |
| controller output | See manipulated variable. |
| crisp value | A finite single value such as a measured physical quantity, for example, x = 5.3 m. |
| cycle time | The time between samples in a discrete digital control system. |
| D |  |
| damping | The progressive reduction or suppression of oscillation in a device or system. |
| deadtime (Td) | The interval of time, expressed in minutes, between initiation of an input change or stimulus and the start of the resulting observable response. |
| defuzzification | The process of converting the degrees of membership of output linguistic variables within their linguistic terms into crisp numerical values. |
| degree of membership | A value that represents the degree of partial membership of a linguistic variable within a linguistic term. This value can range from 0 to 1. |
| degree of support | A weighting value, ranging from 0 to 1, that is applied to each rule in the rule base of a fuzzy controller. This weighting value represents the relative significance of each rule and allows for fine-tuning of the rule base. |
| derivative (control) action | Control response to the time rate of change of a variable. Also called rate action. |
| derivative kick | A sudden change in PID controller output resulting from derivative action applied to the error signal after a change in setpoint value. Derivative kick is normally avoided in PID control by applying derivative action only to the process variable and not to the error signal. |
| deviation | Any departure from a desired value or expected value or pattern. |
| downstream loop | In a cascade, the controller whose setpoint is provided by another controller. |
| E |  |
| EGU | Engineering units. Also abbreviated EU. |
| expert | A human operator of a system or process that has acquired knowledge related to controlling the process through experience. |
| F |  |
| FC | Flow controller. |
| feedback control | Control in which a measured variable is compared to its desired value to produce an actuating error signal that is acted upon in such a way as to reduce the magnitude of the error. |
| feedback loop | See closed loop. |
| fuzzification | The process of associating crisp input values with the linguistic terms of corresponding input linguistic variables.. |
| fuzzy controller | A controller that uses defined rules to control a fuzzy system based on the current values of input linguistic variables. |
| fuzzy logic | An extension of traditional Boolean set theory that allows for partial membership in a set. |
| fuzzy system | A system of input and output variables associated using fuzzy logic. |
| G |  |
| gain | For a linear system or element, the ratio of the magnitude, or amplitude, of a steady-state sinusoidal output relative to the causal input; the length of a phasor from the origin to a point of the transfer locus in a complex plane. Also called the magnitude ratio. |
| gain scheduling | The process of applying different controller gains for different regions of operation of a controller. Gain scheduling is most often used in controlling nonlinear physical processes. |
| I |  |
| implication method | A mathematical method for scaling the membership functions of an output linguistic variable based on the rule weight before performing defuzzification. |
| integral (control) action | Control action in which the output is proportional to the time integral of the input. That is, the rate of change of output is proportional to the input. |
| ISA | Instrument Society of America. The organization that sets standards for process control instrumentation in the United States. |
| K |  |
| K | Process gain. See also process gain (K). |
| Kc | Controller gain. |
| L |  |
| lag | A lowpass filter or integrating response with respect to time. |
| linearity factor | A value ranging from 0 to 1, used to specify the linearity of a calculation. A value of 1 indicates a linear operation. A value of 0.1 indicates a squared nonlinear operation. |
| linguistic term | A word or set of words that represents categories for the values of a linguistic variable. A linguistic term is defined quantitatively by the corresponding membership function. |
| linguistic variable | A word or set of words that represents an input variable or output variable of a fuzzy system. |
| load disturbance | The ability of a controller to compensate for changes in physical parameters of a controlled process while the setpoint value remains constant. |
| loop cycle time | Time interval between calls to a control algorithm. |
| M |  |
| magnitude ratio | See gain. |
| manipulated variable | A quantity or condition that is varied as a function of the actuating error signal so as to change the value of the directly controlled variable. Also called controller output. |
| Mean of Maximum (MoM) | Method of defuzzification in which the crisp output is determined by selecting a value corresponding to the maximum degree of membership of the composite output membership function. If there are multiple maximums, the mean of the corresponding values is selected. |
| membership function | A numerical function that quantitatively defines the degrees of membership of a linguistic variable within a linguistic term. |
| modified Center of Area (mCoA) | Method of defuzzification in which the crisp output is determined by the geometrical center of area of the composite output membership functions. Unlike the Center of Area method, this method allows the crisp output to realize the full range of the output variable. |
| N |  |
| noise | In process instrumentation, an unwanted component of a signal or variable. Noise may be expressed in units of the output or in percent of output span. |
| O |  |
| output limiting | Preventing a controller output (manipulated variable) from traveling beyond a desired maximum range. |
| overshoot | The maximum excursion beyond the final steady-state value of output as the result of an input change. Also called transient overshoot. |
| P |  |
| P | Proportional. |
| P controller | A controller which produces proportional control action only; that is, a controller that has only a simple gain response. |
| partial membership | In fuzzy logic, a condition in which the value of a member partially fulfills the requirements of the membership function of a set. |
| PC | Pressure controller. |
| PD | Proportional, derivative. |
| PD controller | A controller that produces proportional plus derivative (rate) control action. |
| PI | Proportional, integral. |
| PI controller | A controller that produces proportional plus integral (reset) control action. |
| PID | Proportional, integral, derivative. |
| PID control | A common control strategy in which a process variable is measured and compared to a desired set point to determine an error signal. A proportional gain (P) is applied to the error signal, an integral gain (I) is applied to the integral of the error signal, and a derivative gain (D) is applied to the derivative of the error signal. The controller output is a linear combination of the three resulting values. |
| PID controller | A controller that produces proportional plus integral (reset) plus derivative (rate) control action. |
| process gain (K) | For a linear process, the ratio of the magnitudes of the measured process response to that of the manipulated variable. |
| process variable (PV) | The measured variable (such as pressure or temperature) in a process to be controlled. |
| proportional action | Control response in which the output is proportional to the input. |
| proportional band (PB) | The change in input required to produce a full range change in output due to proportional control action. PB = 100 /Kc. |
| Q |  |
| quarter-decay ratio | A response in which the amplitude of each oscillation is one-quarter that of the previous oscillation. |
| R |  |
| ramp | The total (transient plus steady-state) time response resulting from a sudden increase in the rate of change from zero to some finite value of the input stimulus. Also called ramp response. |
| rate action | Control response to the time rate of change of a variable. Also called derivative control action. |
| reset rate | Of proportional plus integral or proportional plus integral plus derivative control action devices: for a step input, the ratio of the initial rate of change of output due to integral control action to the change in steady-state output due to proportional control action.Of integral control action devices: for a step input, the ratio of the initial rate of change of output to the input change. Also called integral action rate. |
| rule | A linguistic representation of the relationships between input and output linguistic variables based on their linguistic terms. |
| rule base | The set of rules for a fuzzy system. |
| S |  |
| selector control | The use of multiple controllers and/or multiple process variables in which the connections may change dynamically depending on process conditions. |
| setpoint (SP) | An input variable which sets the desired value of the controlled process variable. |
| singleton | A normalized membership function with an infinitely small width. A singleton is used to model a crisp value with a fuzzy set. |
| SP | See setpoint. |
| span | The algebraic difference between the upper and lower range values. |
| stochastic uncertainty | The degree of uncertainty of the occurrence of a given future nondeterministic event. |
| T |  |
| time constant (T) | In process instrumentation, the value T (in minutes) in an exponential response term, A exp (–t/T), or in one of the transform factors, such as 1 + sT. |
| transient overshoot | See overshoot. |
| trapezoidal integration | A numerical of integration in which the current value and the previous value are used to calculate the addition of the current value to the integral value. |
| W |  |
| windup area | The time during which the controller output is saturated at the maximum or minimum value. The integral action of a simple PID controller continues to increase (wind up) while the controller is in the windup area. |

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/pid_overview.html language=enus -->
## TOPIC 00005: PID Control

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/pid_overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/pid_overview.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PID Control

Proportional-Integral-Derivative (PID) controllers are common feedback controllers. In PID control, you specify a process variable and a setpoint. The process variable is the system parameter you want to control, such as temperature, pressure, or flow rate, and the setpoint is the desired value for that system parameter. A PID controller determines a controller output value, for example the heater power or valve position, and applies the controller output value to the system to drive the process variable toward the setpoint value.

Use the [PID](../lvpid/pidtitle.html) VIs to develop the following control applications based on PID controllers:

- Proportional (P); proportional-integral (PI); proportional-derivative (PD); and proportional-integral-derivative (PID) algorithms
- Gain-scheduled PID
- PID autotuning
- Error-squared PID
- Lead-Lag compensation
- Setpoint profile generation
- Multi-loop cascade control
- Feedforward control

##### Related Information

[PID Algorithms](pid_algs.html)

[Designing a Control Strategy](cntrl_strat_des.html)

[Implementing PID Controllers with the PID VIs](using_pid_vis.html)

[Autotuning PID Controllers](tuning_pid.html)

[Using PID on FPGA Targets](pid_on_fpga.html)

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/pid_related_docs.html language=enus -->
## TOPIC 00006: Related Documentation

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/pid_related_docs.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/pid_related_docs.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Related Documentation

The following documents contain information that you might find helpful as you use the LabVIEW PID and Fuzzy Logic VIs:

- LabVIEW PID and Fuzzy Logic Example VIs—Refer to the labview\examples\control directory for example VIs that demonstrate common tasks using the PID and Fuzzy Logic.
- The following resources offer useful background information on the general concepts discussed in this documentation. These resources are provided for general informational purposes only and are not affiliated, sponsored, or endorsed by National Instruments. The content of these resources is not a representation of, may not correspond to, and does not imply current or future functionality in PID and Fuzzy Logic VIs or any other National Instruments product:
  - Aström, K. J. and T. Hagglund. 1984. Automatic tuning of simple regulators. In Proceedings of IFAC 9th World Congress , Budapest: 1867–72.
  - Aström, K. J., T. Hagglund, C. C. Hang, and W. K. Ho. 1993. Automatic tuning and adaptation for PID controllers: a survey. Control Engineering Practice 1, no. 4:699–714.
  - Corripio, A. B. 2000. Tuning of Industrial Control Systems . 2d ed. Raleigh, North Carolina: ISA.
  - Seborg, Dale E., Thomas F. Edgar, and Duncan A. Mellichamp. 2004. Process Dynamics and Control . 2nd ed. Hoboken, NJ: John Wiley & Sons, Inc.
  - Shinskey, F. G. 1996. Process Control Systems: Application, Design, and Tuning . 4th ed. Texas: McGraw-Hill Professional.
  - Yen, J., R. Langari, and L. A. Zadeh, eds. 1995. Industrial Applications of Fuzzy Logic and Intelligent Systems . Piscataway, NJ: IEEE Press.
  - Ziegler, J. G., and N. B. Nichols. 1942. Optimum settings for automatic controllers. Trans. ASME 64:759–68.
  - Zimmerman, H.-J. 2001. Fuzzy Set Theory – and Its Applications . 4th ed. Dordrecht, Netherlands: Springer.
  - Zimmerman, H.-J. 1987. Fuzzy Sets, Decision Making, and Expert Systems . Dordrecht, Netherlands: Springer.

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/pid_topo.html language=enus -->
## TOPIC 00007: PID Topologies

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/pid_topo.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/pid_topo.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PID Topologies

Standard PID literature provides several ways to define a PID controller. In general, PID controllers are classified using the following forms.

#### Academic Form

In the Academic form, the proportional parameter (*P*) actuates on the integral (*I*) and derivative (*D*) terms, as represented by the following equation:

[IMAGE alt='image' src='noloc_eq_pidacademic2.gif']

The [algorithms](pid_algs.html) implemented by the [PID](../lvpid/pidtitle.html) VIs are based on the Academic form with time expressed in minutes.

#### Parallel Form

In the Parallel form, the three parameters *P*, *I*, and *D* are independent of each other and control each interaction. This form also is referred to as non-interacting PID. The Parallel form is represented by the following equation:

[IMAGE alt='image' src='noloc_eq_pidparallel2.gif']

#### Series Form

In the Series form, the parameters are coupled and in series with each component, as represented by the following equation:

[IMAGE alt='image' src='noloc_eq_pidseries2.gif']

#### Converting Topologies

You can use the [PID Structure Conversion](../lvpid/pid_structure_conversion.html) VI to convert a PID controller from one topology, or form, to another.

[IMAGE alt='image' src='add.gif'] Add

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/pidrelay_alg.html language=enus -->
## TOPIC 00008: PID Relay Autotuning Technique

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/pidrelay_alg.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/pidrelay_alg.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PID Relay Autotuning Technique

The PID Relay [autotuning technique](autotun_techniques.html), which is used by the [Autotuning Wizard](pid_autowiz.html) and the PID Relay instance of the [PID Online Autotuning](../lvpid/pid_online_autotuning.html) VI, uses the setpoint relay experiment to determining the information needed to tune the controller.

The following image illustrates the autotuning procedure excited by the setpoint relay experiment, which connects a relay and an extra feedback signal with the setpoint. The setpoint relay steps the setpoint up or down, exciting the autotuning procedure and allowing the controller to respond to the change and tune the system for an acceptable response. The [PID Autotuning](../lvpid/pid_with_autotuning.html) VI and the PID Relay instance of the [PID Online Autotuning](../lvpid/pid_online_autotuning.html) polymorphic VI directly implement this process. The existing controller remains in the loop.

[IMAGE alt='image' src='loc_eps_process.gif']

For most systems, the nonlinear relay characteristic generates a limiting cycle, from which the autotuning algorithm identifies the relevant information needed for PID tuning. If the existing controller is proportional only, the autotuning algorithm identifies the ultimate gain *K<sub>u</sub>* and ultimate period *T<sub>u</sub>*. If the existing model is PI or PID, the autotuning algorithm identifies the dead time [IMAGE alt='image' src='tau.gif'] and time constant *T<sub>P</sub>*, which are two parameters in the integral-plus-deadtime model.

[IMAGE alt='image' src='noloc_eq_int_plus_deadt.gif']

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/select_defuzz.html language=enus -->
## TOPIC 00009: Selecting a Defuzzification Method

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/select_defuzz.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/select_defuzz.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Selecting a Defuzzification Method

In decision support systems, the choice of the [defuzzification method](defuzz_methods.html) depends on the context of the decision you want to calculate with the fuzzy controller. For quantitative decisions like project prioritization, apply the [Center of Maximum (CoM)](center_of_max.html) method. For qualitative decisions, such as an evaluation of credit worthiness, [Mean of Maximum (MoM)](mean_of_max.html) is the correct method.

An important aspect of a defuzzification method is the continuity of the output signal. Consider a fuzzy system with a complete rule base and overlapping membership functions. A defuzzification method is continuous if an arbitrary small change of an input value never causes an abrupt change in the output signal.

In this respect, the defuzzification methods CoM and [Center of Area (CoA)](center_of_area.html) are continuous because, assuming overlapping output membership functions, the best compromise does not jump to a different value with a small change to the inputs. The defuzzification method MoM, however, is discontinuous because an arbitrary small change in the input values of the fuzzy system can cause the output value to switch to another, more plausible result.

Using CoA or CoM as the defuzzification method results in continuous [controller characteristic](fuzzy_io.html) functions, especially within those intervals of the input values in which two or more rules are active simultaneously. This behavior results from the averaging character of the defuzzification methods.

The following table compares the different defuzzification methods based on various assessment criteria.

| Assessment Criteria | Method |  |  |  |
| --- | --- | --- | --- | --- |
| Center of Area(CoA)andModified Center of Area(mCoA) | Center of Sums(CoS) | Center of Maximum(CoM) | Mean of Maximum(MoM) |  |
| Linguistic Characteristic | Best Compromise | Best Compromise | Best Compromise | Most Plausible Result |
| Fit with Intuition | Implausible with varying membership function shapes and strong overlapping membership functions | Implausible with varying membership function shapes and strong overlapping membership functions | Good | Good |
| Continuity | Yes | Yes | Yes | No |
| Computational Effort | Very High | Medium | Low | Very Low |
| Application Field | Closed-Loop Control, Decision Support, Data Analysis | Closed-Loop Control, Decision Support, Data Analysis | Closed-Loop Control, Decision Support, Data Analysis | Pattern Recognition, Decision Support, Data Analysis |

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/setpoint_ramp_gen.html language=enus -->
## TOPIC 00010: Setpoint Profile Generation

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/setpoint_ramp_gen.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/setpoint_ramp_gen.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Setpoint Profile Generation

You can use the [PID Setpoint Profile](../lvpid/pid_setpoint_profile.html) VI inside a control loop to generate a profile of setpoint values over time for a ramp and soak type PID application. For example, you might want to ramp the setpoint temperature of an oven control system over time, and then hold, or soak, the setpoint at a certain temperature for another period of time. You can use the PID Setpoint Profile VI to implement any arbitrary combination of ramp, hold, and step functions.

Specify the setpoint profile as an array of pairs of time and setpoint values with the time values in ascending order.

#### Ramp Setpoint Profile

You can specify a ramp setpoint profile with two setpoint profile array values, as shown in the following image.

[IMAGE alt='image' src='loc_fp_rampspprof.gif']

#### Ramp and Hold Setpoint Profile

A ramp and hold setpoint profile also can have two successive array values with the same setpoint value, as shown in the following image.

[IMAGE alt='image' src='loc_fp_rampholdspprof.gif']

#### Step Setpoint Profile

A step setpoint profile can have two successive array values with the same time value but different setpoint values, as shown in the following image.

[IMAGE alt='image' src='loc_fp_rampstepspprof.gif']

The [PID Setpoint Profile](../lvpid/pid_setpoint_profile.html) VI returns a single **setpoint** value determined from the current elapsed time. The first call to the VI initializes the current time in the setpoint profile to 0. On subsequent calls, the VI determines the current time from the previous time and the **dt** input value. If you reinitialize the current time to 0 by passing a value of TRUE to the **reinitialize?** input, you can repeat the specified setpoint profile.

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/tuning_pid.html language=enus -->
## TOPIC 00011: Autotuning PID Controllers (PID and Fuzzy Logic)

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/tuning_pid.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/tuning_pid.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Autotuning PID Controllers (PID and Fuzzy Logic)

Often, many PID controllers are poorly tuned. As a result, some controllers are too aggressive and some controllers are too sluggish. Tuning a controller involves adjusting the parameters of the system to get the desired, or optimal, response. However, manually tuning PID controllers can be difficult when you do not know the process dynamics or disturbances. In this case, you can use autotuning to automatically test different parameter values and determine the best response.

Choose from the following VIs that integrate autotuning based on your specific application needs and your knowledge of tuning theory.

| Use Case | VI Name |
| --- | --- |
| Autotuning that runs with minimal user input or knowledge of tuning algorithms. Single VI implements a controller for a system and allows tuning. | PID Advanced Autotuning VI |
| Autotuning that runs with minimal user input or knowledge of tuning algorithms. Single VI implements a controller for a system with significant deadtime and allows tuning. How-To: Programmatically Implementing and Autotuning a PID Controller | PID Autotuning (Temperature) VI |
| Controlling the autotuning technique used to identify the system. Other PID VIs automatically determine the technique. Tuning system parameters, then passing the output parameters to the PID Advanced VI to implement that controller. How-To: Programmatically Autotuning a Previously Implemented PID Controller | PID Online Autotuning VI |
| Generating PID parameters for a system given an input/output signal. This technique is useful when you have insufficient information about the system and you want to develop initial parameters based on system response. Provides access to multiple methods for determining PID parameters. Other PID VIs automatically determine the method. | PID Autotuning Design VI |
| Performing interactive autotuning in a dialog box that you use to configure the process. Not supported on RT or FPGA hardware targets. How-To: Implementing Autotuning with the Autotuning Wizard | PID Autotuning VI |
| PID applications with high-speed control and/or high channel count on an FPGA target. Implements a fixed-point PID algorithm. | PID (FPGA) VI |

##### Related Information

[Updating PID Parameters After Autotuning](update_autotun_params.html)

[Logging Parameter Values After Autotuning](datalog_params.html)

[Online Autotuning Techniques](autotun_techniques.html)

[Autotuning Methods for Testing PID Parameters](autotun_methods.html)

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/twosteptuning.html language=enus -->
## TOPIC 00012: Programmatically Autotuning a Previously Implemented PID Controller

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/twosteptuning.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/twosteptuning.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Programmatically Autotuning a Previously Implemented PID Controller

You can use the [PID Online Autotuning](../lvpid/pid_online_autotuning.html) VI to tune a controller you implement or previously implemented with the [PID Advanced](../lvpid/pidadvanced.html) VI.

|  | Note You must use the PID Advanced VI to implement the controller. You can implement PID controllers with various PID VIs, but PID Advanced is the only VI that supports putting the controller under manual control, which is necessary for using the PID Online Autotuning VI. You also can use the PID Advanced Autotuning VI to implement and autotune a PID controller from a single VI. |
| --- | --- |

Complete the following steps autotune a previously implemented PID controller.

1. If you have not already done so, implement a PID controller using the PID Advanced VI.
2. Put the controller in manual mode by setting the auto? input of the PID Advanced VI to FALSE.
3. Add the PID Online Autotuning VI to the block diagram within the control loop but to the left of the PID Advanced VI.
4. Manually select the polymorphic instance of the PID Online Autotuning VI.
5. Without deleting the controls, constants, or shift registers that contain the values, delete the wires to the setpoint , process variable , and PID gains inputs of the PID Advanced VI.
6. Wire the values to the Setpoint in , Process Variable , and PID gains in inputs of the PID Online Autotuning VI.
7. Create a Boolean control with latched mechanical action and a default value of FALSE, and wire the control to the Autotune? input of the PID Online Autotuning VI.
8. Wire the setpoint out , Process Variable Out , and PID gains out outputs of the PID Online Autotuning VI to the setpoint , process variable , and PID gains inputs of the PID Advanced VI.
9. (Optional) If you are specifying a value for the dt (s) input, wire the same value to both VIs.
10. Run the VI.
11. Set Autotune? to TRUE to begin autotuning.

Refer to the Autotuning PID Online and Inline VI in the labview\examples\control\PID for an example of implementing autotuning with the [PID Online Autotuning](../lvpid/pid_online_autotuning.html) VI and the [PID Advanced](../lvpid/pidadvanced.html) VI.

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/update_autotun_params.html language=enus -->
## TOPIC 00013: Updating PID Parameters After Autotuning

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/update_autotun_params.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/update_autotun_params.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Updating PID Parameters After Autotuning

The PID [autotuning](tuning_pid.html) VIs, including [PID Autotuning](../lvpid/pid_with_autotuning.html), [PID Advanced Autotuning](../lvpid/pid_advanced_autotuning.html), and [PID Online Autotuning](../lvpid/pid_online_autotuning.html), calculate new parameters for a PID controller that result in the best response. When autotuning, you must write your code to apply the new PID controller parameters (the PID gains) when the autotuning is complete.

You can use the following methods to update PID parameters after autotuning.

|  | Note In both of the following methods, you must manually save the PID gains so that you can use the PID gains out values the next time you run the control application. Ensure that the PID gains control shows the current updated parameters, select Operate»Make Current Values Default, and save the VI. If you do not want to manually save the VI after each run, you can use a datalog file to save PID gains values. |
| --- | --- |

#### Using Shift Registers to Update PID Parameters

The following block diagram shows a simple implementation of using shift registers to update PID parameters in the [PID Autotuning](../lvpid/pid_with_autotuning.html) VI.
The shift register on the left stores the initial value of the PID gains. **PID gains out** then passes an updated value to the right-hand shift register terminal when each control loop iteration completes. This method is simple, but limited in that the user cannot change **PID gains** manually while the control loop runs.

[IMAGE alt='image' src='loc_bd_autotuningshiftregister.gif']

#### Using Local Variables to Update PID Parameters

In place of shift registers, you can use a local variable to store updated PID gains values. In the following block diagram, [PID Autotuning](../lvpid/pid_with_autotuning.html) VI reads the **PID gains** control on each iteration of the While Loop, and a local variable updates the control only when **tuning complete?** is TRUE. This method allows for manual control of the **PID gains** while the control loop executes.

[IMAGE alt='image' src='loc_bd_autotun_update_locvar.gif']

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/using_pid_vis.html language=enus -->
## TOPIC 00014: Implementing PID Controllers with the PID VIs

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/using_pid_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/using_pid_vis.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Implementing PID Controllers with the PID VIs

The [PID](../lvpid/pidtitle.html) VIs are all variations of the basic [PID](../lvpid/pid_vi.html) VI, and each variation provides additional functionality as described in the following table. You can use these VIs interchangeably because they use consistent inputs and outputs where possible. Refer to the help topic for the VI you want to use for specific information about the VI.

| Use Case | VI Name |
| --- | --- |
| Simple systems, or when an efficient algorithm is required. Implements the basic PID algorithm | PID VI |
| Complex systems that require options for manual or automatic operation, setpoint weighting, filtering of derivative action, and so on. Implements the advanced PID algorithm and provides extra input parameters to expand on the functionality of the PID VI. | PID Advanced VI |
| Complex systems that require the same advanced options as the PID Advanced VI and the ability to autotune parameters. | PID Advanced Autotuning VI |
| Systems that contain significant dead time. | PID Autotuning (Temperature) VI |
| Systems that require lead/lag function. | PID Lead-Lag VI |

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

##### Related Information

[Fault Protection](fault_protection.html)

[Multi-Loop Control](multiloop_control.html)

[Setpoint Profile Generation](setpoint_ramp_gen.html)

[Gain Scheduling](gain_schedule.html)

[Control Output Rate Limiting](cntrl_out_limit.html)

[Lead/Lag](lead_lag.html)

[Converting Between Percentage of Full Scale and Engineering Units](percent_to_eng.html)

[Filtering Control Inputs](filter_control_inputs.html)

<!--NI_TOPIC bundle=labview-pid-and-fuzzy-logic-toolkit-api-ref path=lvpidmain/ziegnichforms.html language=enus -->
## TOPIC 00015: Ziegler-Nichols Autotuning Method

- bundle_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- source_path: `lvpidmain/ziegnichforms.html`
- source_url: https://docs-be.ni.com/bundle/labview-pid-and-fuzzy-logic-toolkit-api-ref/raw/resource/enus/lvpidmain/ziegnichforms.html
- document_id: `labview-pid-and-fuzzy-logic-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Ziegler-Nichols Autotuning Method

Ziegler and Nichols developed heuristic methods for determining the parameters of a PID controller. The Autotuning Wizard and PID VIs that use the [PID Relay autotuning technique](pidrelay_alg.html) use this method.

When using the Ziegler-Nichols autotuning method, select one of the following three types of desired loop response performance: **fast** (1/4 damping ratio), **normal** (some overshoot), and **slow** (little overshoot). The following tables show the tuning formulas for each type of loop performance.

|  | Note During tuning, the process remains under closed-loop PID control. You do not need to switch off the existing controller and perform the experiment under open-loop conditions. In the setpoint relay experiment, the setpoint signal mirrors the setpoint for the PID controller. |
| --- | --- |

##### Ziegler-Nichols Closed Loop/Frequency Response Method

The following tables show the tuning formulas for different types of loop performance under proportional-only control, where *K<sub>u</sub>* is the controller gain and *T<sub>u</sub>* is the period of oscillation.

| Fast Performance |  |  |  |
| --- | --- | --- | --- |
| Controller | Kc | Ti | Td |
| P | 0.5Ku | — | — |
| PI | 0.4Ku | 0.8Tu | — |
| PID | 0.6Ku | 0.5Tu | 0.12Tu |

| Normal Performance |  |  |  |
| --- | --- | --- | --- |
| Controller | Kc | Ti | Td |
| P | 0.2Ku | — | — |
| PI | 0.18Ku | 0.8Tu | — |
| PID | 0.25Ku | 0.5Tu | 0.12Tu |

| Slow Performance |  |  |  |
| --- | --- | --- | --- |
| Controller | Kc | Ti | Td |
| P | 0.13Ku | — | — |
| PI | 0.13Ku | 0.8Tu | — |
| PID | 0.15Ku | 0.5Tu | 0.12Tu |

##### Ziegler-Nichols Open Loop/Step Response Method

The following tables shows the tuning formulas for different types of loop performance under PI or PID control, where *T<sub>P</sub>* is the time constant and [IMAGE alt='image' src='tau.gif'] is the dead time.

| Fast Performance |  |  |  |
| --- | --- | --- | --- |
| Controller | Kc | Ti | Td |
| P | TP/ | — | — |
| PI | 0.9TP/ | 3.33 | — |
| PID | 1.1TP/ | 2.0 | 0.5 |

| Normal Performance |  |  |  |
| --- | --- | --- | --- |
| Controller | Kc | Ti | Td |
| P | 0.44TP/ | — | — |
| PI | 0.4TP/ | 5.33 | — |
| PID | 0.53TP/ | 4.0 | 0.8 |

| Slow Performance |  |  |  |
| --- | --- | --- | --- |
| Controller | Kc | Ti | Td |
| P | 0.26TP/ | — | — |
| PI | 0.24TP/ | 5.33 | — |
| PID | 0.32TP/ | 4.0 | 0.8 |

|  | Note The previous tables provides proportional gain (Kc) values. The following equation describes the relationship between proportional gain and proportional band (PB): Kc = 100/PB |
| --- | --- |
