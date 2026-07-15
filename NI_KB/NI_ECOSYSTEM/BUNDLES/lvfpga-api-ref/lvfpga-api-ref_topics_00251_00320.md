# NI DOCUMENT BUNDLE: lvfpga-api-ref

<!--NI_BUNDLE_CHUNK bundle=lvfpga-api-ref start=251 end=320 -->
<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpatan2/xnode/nifxpmath-atan2-xnode.html language=enus -->
## TOPIC 00251: High Throughput Inverse Tangent (2 Input)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpatan2/xnode/nifxpmath-atan2-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpatan2/xnode/nifxpmath-atan2-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the arctangent of y/x in pi radians. This function supports only scalar values of the fixed-point data type. icon Dialog Box Options Parameter Description General Specifies general information about this function. Fixed-Point Configuration—Specifies the encodings, word lengths, and integer

### High Throughput Inverse Tangent (2 Input)

Computes the arctangent of **y**/**x** in pi radians.

This function supports only scalar values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpmath-atan2-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| General | Specifies general information about this function. Fixed-Point Configuration—Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type—Specifies the fixed-point configuration of the x input terminal. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. If the encoding is Signed, the maximum value is 64 bits. If the encoding is Unsigned, the maximum value is 63 bits. Integer word length—Specifies the integer word length of this terminal. If the encoding is Signed, the maximum value is 2047 bits. If the encoding is Unsigned, the maximum value is 2046 bits. As you change the value of this control, LabVIEW might change the Integer word length of the other input terminal. These changes maintain the supported fixed-point configuration of the shared internal data type. y Type—Specifies the fixed-point configuration of the y input terminal. If you wire a fixed-point data type to this terminal and that data type follows the rules for this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. If the encoding is Signed, the maximum value is 64 bits. If the encoding is Unsigned, the maximum value is 63 bits. Integer word length—Specifies the integer word length of this terminal. If the encoding is Signed, the maximum value is 2047 bits. If the encoding is Unsigned, the maximum value is 2046 bits. As you change the value of this control, LabVIEW might change the Integer word length of the other input terminal. These changes maintain the supported fixed-point configuration of the shared internal data type. atan2(y, x) Type—Specifies the fixed-point configuration of the atan2(y, x) output terminal. Signed—Specifies that this terminal is signed. atan2(y, x) always is in the range [–1, 1], so LabVIEW sets the encoding to Signed and dims this option. Unsigned—Specifies that this terminal is unsigned. atan2(y, x) always is in the range [–1, 1], so LabVIEW sets the encoding to Signed and dims this option. Word length—Specifies the word length of this terminal. The value must be between 4 and 64 bits. Integer word length—Specifies the integer word length of this terminal. LabVIEW sets this value to 2 bits and dims this option. Rounding mode—Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. Execution Mode—Specifies how this function executes. Outside single-cycle Timed Loop—Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop—Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput—Specifies the minimum number of cycles between two successive values of valid input data. Entering a low value in this control results in a high throughput rate. The maximum value of Throughput depends on the Value of the Number of internal iterations, which you specify on the CORDIC Details page. Throughput is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, this function returns a valid result on every call to the function. Therefore, the Throughput control displays 1 call / sample. The Configuration Feedback indicator displays the number of clock cycles this function takes to return a valid result. Registers—Specifies whether to add internal registers for function inputs and/or outputs. These registers will be placed outside of any embedded resources, such as block multipliers or DSP48E slices. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| CORDIC Details | Specifies options for the COordinate Rotation DIgital Computer (CORDIC) algorithm this function uses. Precision—Specifies options about the precision of the result(s) this function returns. Number of internal iterations—Specifies the number of cycles this function takes to return a valid result without considering input/output registers. Adapt to configuration—Specifies whether LabVIEW automatically determines the number of internal iterations based on the options you specify on the General page. By default, this checkbox contains a checkmark. Value—Specifies the number of cycles this function takes to return a valid result without considering input/output registers. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the number of internal iterations increases both the precision of the result and the latency of this function. Internal word length—Specifies the word length of internal calculations Adapt to configuration—Specifies whether LabVIEW automatically determines the value of the internal word length based on the options you specify on the General page and the Value of the Number of internal iterations. By default, this checkbox contains a checkmark. Value—Specifies the word length of internal calculations. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page and the Value of the Number of internal iterations. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the internal word length increases the precision of the output, the amount of FPGA resources this function requires, and the length of the combinatorial path. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| y — Specifies an input to this function. Note If you wire an unsigned value to this terminal that has a word length of 64 bits and an integer word length less than 2047 bits, LabVIEW coerces the word length to be 63 bits and displays a coercion dot on the wire. x — Specifies an input to this function. Note If you wire an unsigned value to this terminal that has a word length of 64 bits and an integer word length less than 2047 bits, LabVIEW coerces the word length to be 63 bits and displays a coercion dot on the wire. input valid — Specifies whether the next data point has arrived for processing. Wire output valid of an upstream node to input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for output, select Inside single-cycle Timed Loop in the configuration dialog box. atan2(y,x) (pi) — Returns the arctangent of y/x in pi radians, which use fewer FPGA resources than radians. To convert this value into radians, multiply atan2(y, x) by pi. output valid — Returns TRUE if this Express VI has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display output valid, select Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

#### Input Terminals Coercion

If you wire a fixed-point data type to only one input terminal, this function coerces the unwired terminal to match the configuration of the wired terminal. You can right-click the unwired terminal and select **Create»Control** or **Create»Constant**. This action creates a second fixed-point data type with the same configuration as the wired terminal.

If you wire fixed-point data types with different configurations to the input terminals, this function uses a shared, signed fixed-point data type to represent the value of both terminals internally. The maximum word length of this internal data type is 64 bits. If the configurations of the input terminals result in an internal word length greater than 64 bits, this function rounds off the fractional bits of one input terminal to achieve an internal word length of 64 bits. This function rounds off the input terminal that has the most fractional bits.

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpconvert/xnode/nifxpmath-convert-xnode.html language=enus -->
## TOPIC 00252: High Throughput To Fixed-Point

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpconvert/xnode/nifxpmath-convert-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpconvert/xnode/nifxpmath-convert-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Modifies the fixed-point configuration of x. This function supports only scalar values of the fixed-point data type. Use this function instead of the To Fixed-Pointfunction in the following situations: You want to determine whether overflow occurred during the computation or was propagated through t

### High Throughput To Fixed-Point

Modifies the fixed-point configuration of **x**.

fixed-point

To Fixed-Point

- You want to determine whether overflow occurred during the computation or was propagated through the input terminal.
- You want to insert registers after the function when you place this function inside a single-cycle Timed Loop .

[IMAGE alt='icon' src='nifxpmath-convert-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Fixed-Point Configuration | Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type—Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. y Type— Specifies the fixed-point configuration of the y input terminal. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. Overflow mode— Specifies how this function handles overflow. You can choose either Wrap (default) or Saturate. Note The Saturateoption requires more FPGA resources and a longer combinatorial path than the Wrap option does. In this situation, choosing Saturate might decrease the maximum clock rate at which this function can compile. Rounding mode— Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. |
| Execution Mode | Specifies how this function executes. Outside single-cycle Timed Loop—Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop—Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput—Displays the number of cycles between two successive values of valid input data. This number always is one cycle. Therefore, LabVIEW sets the value according to where you place this Express VI. If you select Inside single-cycle Timed Loop,LabVIEW sets the throughput to 1 cycle / sample.If you select Outside single-cycle Timed Loop,LabVIEW sets the throughput to 1 call / sample. |
| Registers | Specifies whether to add internal registers for function output terminal. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes an additional clock cycle to return a valid result. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| Optional Terminal | Specifies a setting for displaying an optional block diagram terminal. Operation overflow—Specifies that this function displays the operation overflow output terminal on the block diagram. This terminal indicates whether overflow occurred during the operation of this function. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies the fixed-point number whose configuration you want to modify. input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input valid to transfer data from the upstream node to this node. To display this handshaking terminal, select the Inside single-cycle Timed Loop option and place a checkmark in the Register outputs checkbox. These options are located in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire the ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. To displayready for output, select the Inside single-cycle Timed Loop option and place a checkmark in the Register outputs checkbox. These options are located in the configuration dialog box. y — Returns xwith the specified fixed-point configuration applied. operation overflow — Returns TRUE if the theoretical computed value exceeds the valid range of the output data type. If operation overflow returns TRUE, the Overflow mode option determines the value this function returns. LabVIEW displays the operation overflow terminal only if you place a checkmark in the Operation overflow checkbox. This checkbox is located in the Optional Terminal section of the configuration dialog box. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display this terminal, select the Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the input valid terminal is TRUE during the following cycle. To display ready for input, select the Inside single-cycle Timed Loop option and place a checkmark in the Register outputs checkbox. These options are located in the configuration dialog box. |
| --- |

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpdiv/xnode/nifxpmath-div-xnode.html language=enus -->
## TOPIC 00253: High Throughput Divide

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpdiv/xnode/nifxpmath-div-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpdiv/xnode/nifxpmath-div-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the quotient of x and y. This function rounds the result by truncating the value of the x/y output terminal towards 0. This rounding mode uses fewer FPGA resources than other rounding modes do. This function supports only scalar values of integer and fixed-point data types. icon Dialog Box

### High Throughput Divide

Computes the quotient of **x** and **y**. This function [rounds the result](/csh?context=lvfpga_lvfpgaconcepts_fpgafixedpoint) by truncating the value of the **x/y** output terminal towards 0.

This function supports only scalar values of integer and [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data types.

[IMAGE alt='icon' src='nifxpmath-div-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Fixed-Point Configuration | Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type—Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. y Type— Specifies the fixed-point configuration of the y input terminal. If you wire a fixed-point data type to this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. x/y Type— Specifies the fixed-point configuration of the x/y output terminal. Adapt to source—Specifies whether LabVIEW automatically adjusts the fixed-point configuration of the output data type to avoid overflow for nonzero values of y. . By default, this checkbox contains a checkmark and LabVIEW dims the following options. Note Because the precision of the quotient might be infinite, rounding errors always occur. Signed—SSpecifies that this terminal is signed. LabVIEW sets the encoding of this terminal based on the encoding of the input terminals and dims this option. Unsigned—Specifies that this terminal is unsigned. LabVIEW sets the encoding of this terminal based on the encoding of the input terminals and dims this option. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. Include overflow status—Specifies whether the output terminal includes the overflow status. LabVIEW propagates this status to downstream nodes. Including this status requires additional FPGA resources. By default, this checkbox does not contain a checkmark. If you place a checkmark in this checkbox, the overflow status becomes TRUE in either of the following situations: The overflow status of an input terminal is TRUE. Overflow occurs during the operation of this function. If you place a checkmark in the Adapt to source checkbox, LabVIEW sets Include overflow status depending on whether an input terminal includes this status. Overflow mode— Specifies how this function handles overflow. You can choose from the following options: Saturate (default)—Specifies that if overflow occurs, this function saturates the x/y output terminal. Note If you select Saturate and the value of y is 0, this function uses the following equations to determine the value of the x/y output terminal.x/y = max(x/y), if x ≥ 0x/y = min(x/y), if x < 0 Undefined result—Specifies that if overflow occurs, the value of the x/y output terminal is undefined. Note The Undefined result option does not require any additional FPGA resources. Conversely, the Saturate option requires additional FPGA resources and a longer combinatorial path, which might decrease the maximum clock rate at which this function can compile. |
| Execution Mode | Specifies how this function executes. Outside single-cycle Timed Loop—Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop—Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput—Specifies the minimum number of cycles between two successive values of valid input data. Entering a low value in this control results in a high throughput rate. The maximum value of Throughput depends on the Word length of the output terminal. This option is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, this function returns a valid result on every call to the function. Therefore, the Throughput control displays 1 call / sample. The Configuration Feedback indicator displays the number of clock cycles this function takes to return a valid result. |
| Registers | Specifies whether to add internal registers for function inputs and/or outputs. These registers will be placed outside of any embedded resources, such as block multipliers or DSP48E slices. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| Optional Terminal | Specifies a setting for displaying an optional block diagram terminal. Operation overflow—Specifies that this function displays the operation overflow output terminal on the block diagram. This terminal indicates whether overflow occurred during the operation of this function. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies the dividend. y — Specifies the divisor. If the value of y is 0, overflow occurs in the x/y output terminal. input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select the Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire the ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. To displayready for output, select the Inside single-cycle Timed Loop in the configuration dialog box. x/y — Returns x divided by y. operation overflow — Returns TRUE if the theoretical computed value exceeds the valid range of the output data type. If operation overflow returns TRUE, the Overflow mode option determines the value this function returns. LabVIEW displays the operation overflow terminal only if you place a checkmark in the Operation overflow checkbox. This checkbox is located in the Optional Terminal section of the configuration dialog box. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display this terminal, select the Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the input valid terminal is TRUE during the following cycle. To display ready for input, select the Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

If you place a checkmark in the **Adapt to source** checkbox, overflow still can occur in the **x/y** output terminal for non-zero values of **y** if both of the following conditions are true:

- x = –2 iwl<sub>x</sub> – 1
- y = –2 iwl<sub>y</sub> – wl<sub>y</sub>

where *wl* refers to the word length of a terminal and *iwl* refers to the integer word length of a terminal.

Complete the following steps to avoid overflow in this situation and for any non-zero value of **y**.

1. Remove the checkmark from the Adapt to source checkbox.
2. Increase both the Word length and Integer word length of the x/y terminal by at least 1 bit.

After you complete these steps, LabVIEW does not adjust the fixed-point configuration of the **x/y** terminal automatically. If you change the fixed-point configuration of the **x** or **y** terminal and still want to avoid overflow for any non-zero value of **y**, place a checkmark in the **Adapt to source checkbox** again. LabVIEW adjusts the fixed-point configuration of the **x/y** terminal automatically. Then, complete steps 1–2 above to ensure that no overflow occurs with the updated fixed-point configurations.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Divide\Divide.lvproj
- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Vector Normalization\Vector Normalization.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Vector Normalization\Vector Normalization.lvproj

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpexp/xnode/nifxpmath-exp-xnode.html language=enus -->
## TOPIC 00254: High Throughput Exponential

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpexp/xnode/nifxpmath-exp-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpexp/xnode/nifxpmath-exp-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes e raised to the power of x. The value of x must be in the range [–1, 1). This function supports only scalar values of the fixed-point data types. icon Dialog Box Options Parameter Description General Specifies general information about this function. Fixed-Point Configuration—Specifies the

### High Throughput Exponential

Computes e raised to the power of **x**. The value of **x** must be in the range [–1, 1).

This function supports only scalar values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data types.

[IMAGE alt='icon' src='nifxpmath-exp-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| General | Specifies general information about this function. Fixed-Point Configuration—Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type—Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal and that data type follows the rules for this terminal, LabVIEW dims this section and uses information from the wire. If you wire a fixed-point data type to this terminal that does not follow the rules, LabVIEW breaks the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. If the encoding is Signed, the maximum value is 1 bit. If the encoding is Unsigned, the maximum value is 0 bits. exp(x) Type— Specifies the fixed-point configuration of the exp(x) output terminal. Signed—Specifies that this terminal is signed. exp(x)) always is positive, so LabVIEW sets the encoding to Unsigned and dims this option. Unsigned—Specifies that this terminal is unsigned. exp(x)) always is positive, so LabVIEW sets the encoding to Unsigned and dims this option. Word length—Specifies the word length of this terminal. The value must be between 4 and 64 bits. Integer word length—Specifies the integer word length of this terminal. LabVIEW sets this value to 2 bits and dims this option. Rounding mode— Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. Execution Mode—Specifies how this function executes. Outside single-cycle Timed Loop—Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop—Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput—Specifies the minimum number of cycles between two successive values of valid input data. Entering a low value in this control results in a high throughput rate. The maximum value of Throughput depends on the Value of the Number of internal iterations, which you specify on the CORDIC Details page. Throughput is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, this function returns a valid result on every call to the function. Therefore, the Throughput control displays 1 call / sample. The Configuration Feedback indicator displays the number of clock cycles this function takes to return a valid result. Registers—Specifies whether to add internal registersfor function inputs and/or outputs. These registers will be placed outside of any embedded resources, such as block multipliers or DSP48E slices. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| CORDIC Details | Specifies options for the COordinate Rotation DIgital Computer (CORDIC) algorithm this function uses. Precision—Specifies options about the precision of the result(s) this function returns. Number of internal iterations—Specifies the number of cycles this function takes to return a valid result without considering input/output registers. Adapt to configuration—Specifies whether LabVIEW automatically determines the number of internal iterations based on the options you specify on the General page. By default, this checkbox contains a checkmark. Value—Specifies the number of cycles this function takes to return a valid result without considering input/output registers. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the number of internal iterations increases both the precision of the result and the latency of this function. Internal word length—Specifies the word length of internal calculations. Adapt to configuration—Specifies whether LabVIEW automatically determines the number of internal iterations based on the options you specify on the General page and the Value of the Number of internal iterations. By default, this checkbox contains a checkmark. Value—Specifies the word length of internal calculations. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page and theValue of theNumber of internal iterations. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the number of internal iterations increases both the precision of the result and the latency of this function. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies the input to this function. x must be in the range [–1, 1). input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select the Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire the ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. To displayready for output, select the Inside single-cycle Timed Loop in the configuration dialog box. exp(x) — Returns e raised to the power of x. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display this terminal, select the Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the input valid terminal is TRUE during the following cycle. To display ready for input, select the Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

#### Computing exp(x) When x is Outside the Valid Range

**x** must be in the range [–1, 1). To compute exp(**x**) when **x** is outside this range, find an integer *q* and a real number *r*, where *r* is in the range [0, ln(2)), such that **x** = *q* × ln(2) + *r*.
 You then can compute 2^*q* × exp(*r*), which is equivalent to exp(**x**). Because *r* is in the valid range of [–1, 1), you can use this function to compute exp(*r*).

#### Input Terminal Coercion

The CORDIC algorithm represents **x** internally as a fixed-point number with a 1-bit integer word length. The word length of **x** must be less than or equal to 64 bits, which means the fractional word length must be less than or equal to 63 bits. If you wire a value to **x** that has a fractional word length greater than 63 bits, this function rounds off the lower bits to achieve a fractional word length of 63 bits. For example, if you wire a fixed-point data type with a configuration of <+/–,60,–5> to **x**, this function coerces the configuration to be <+/–,58,–5>.

If you wire a fixed-point data type to **x** with a fractional word length greater than 63 bits and an integer word length less than –62 bits, this function coerces the configuration to be <+/–,1,–62> if the data type is signed. If the data type is unsigned, the coerced configuration is <+,1,–62>.

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpinterpret/xnode/nifxpmath-interpret-xnode.html language=enus -->
## TOPIC 00255: Reinterpret Number

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpinterpret/xnode/nifxpmath-interpret-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpinterpret/xnode/nifxpmath-interpret-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Shifts the decimal point of the bit pattern of x and returns y, where y has the same bit pattern as x but a different fixed-point configuration and value. This shift represents a hardware-efficient way to multiply or divide x by 2^n. Use this function instead of the High Throughput To Fixed-Point fu

### Reinterpret Number

Shifts the decimal point of the bit pattern of **x** and returns **y**, where **y** has the same bit pattern as **x** but a different fixed-point configuration and value. This shift represents a hardware-efficient way to multiply or divide **x** by 2^*n*.

Use this function instead of the [High Throughput To Fixed-Point](../../fxpconvert/xnode/nifxpmath-convert-xnode.html) function to avoid coercion or to retain the bit pattern **x** instead of the value of **x**.

The Reinterpret Number function supports only integer, array of integer, and scalar and array values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpmath-interpret-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Fixed-Point Configuration | Displays the word length and specifies the encoding and integer word length of the y output terminal. y Type— Specifies the fixed-point data type of the y output terminal. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length ofy LabVIEW dims this option and sets the value equal to the word length of x. Integer word length—Specifies the integer word length of y, which is equivalent to the number of places you want to shift the decimal point of the bit pattern of x. If you increase the integer word length of y relative to x, this function shifts the decimal point to the right. This right-shift represents a hardware-efficient way of multiplying x by 2^n, where n is the number of places the decimal point shifted. If you decrease the integer word length of y relative to x, the decimal shifts to the left, which is equivalent to dividing x by 2^n. In either situation, the bit patterns of x and y are identical. For example, if x is 2 and its data type is <+, 8, 8> and you set Integer word length to 4, this function converts the data type to <+, 8, 4>. This conversion reduces the integer word length by 4 bits, which means that y = x / 2^4 = 2 / 16 = 0.125000. The bit pattern remains unchanged: the bit pattern of x is 00000010, and the bit pattern of y is 0000.0010. Notice the decimal point of the bit pattern shifts to the left by 8–Integer word length = 8–4 = 4 places. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies the number whose bit pattern this function reinterprets. This function treats signed/unsigned n-bit integers as signed/unsigned fixed-point numbers with an n-bit word length and integer word length. For example, a signed 32-bit integer (I32) is equivalent to the fixed-point data type <+/—, 32, 32>. An unsigned 8-bit integer (U8) is equivalent to the fixed-point data type <+, 8, 8> y — Returns the reinterpreted bit pattern of x. If x is an array, y is the reinterpreted number of each element of x. |
| --- |

Parent topic:

Fixed-Point

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpln/xnode/nifxpmath-naturallogarithm-xnode.html language=enus -->
## TOPIC 00256: High Throughput Natural Logarithm

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpln/xnode/nifxpmath-naturallogarithm-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpln/xnode/nifxpmath-naturallogarithm-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the natural logarithm of x. The value of x must be in the range [1/e, 1), the encoding must be unsigned, and the integer word length must be 0 bits. This function supports only scalar values of the fixed-point data types. icon Dialog Box Options Parameter Description General Specifies gener

### High Throughput Natural Logarithm

Computes the natural logarithm of **x**. The value of **x** must be in the range [1/e, 1), the encoding must be unsigned, and the integer word length must be 0 bits.

This function supports only scalar values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data types.

[IMAGE alt='icon' src='nifxpmath-naturallogarithm-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| General | Specifies general information about this function. Fixed-Point Configuration—Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type—Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal and that data type follows the rules for this terminal, LabVIEW dims this section and uses information from the wire. If you wire a fixed-point data type to this terminal that does not follow the rules, LabVIEW breaks the wire. Signed—Specifies that this terminal is signed. The value of x must be positive, so LabVIEW sets the encoding to Unsigned and dims this option. Unsigned—Specifies that this terminal is unsigned. The value of x must be positive, so LabVIEW sets the encoding to Unsigned and dims this option. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. The value of x must be in the range [1/e, 1), so LabVIEW sets the Integer word length to 0 bits and dims this option. x does not support an integer word length of –1. ln(x) Type— Specifies the fixed-point configuration of the ln(x) output terminal. Signed—Specifies that this terminal is signed. The value of ln(x) can be either positive or negative, so LabVIEW sets the encoding to Signed and dims this option. Unsigned—Specifies that this terminal is unsigned. The value of ln(x) can be either positive or negative, so LabVIEW sets the encoding to Signed and dims this option. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. LabVIEW sets this value to 1 bit and dims this option. Rounding mode— Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. Execution Mode—Specifies how this function executes. Outside single-cycle Timed Loop—Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop—Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput—Specifies the minimum number of cycles between two successive values of valid input data. Entering a low value in this control results in a high throughput rate. The maximum value of Throughput depends on the Value of the Number of internal iterations, which you specify on the CORDIC Details page. Throughput is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, this function returns a valid result on every call to the function. Therefore, the Throughput control displays 1 call / sample. The Configuration Feedback indicator displays the number of clock cycles this function takes to return a valid result. Registers—Specifies whether to add internal registersfor function inputs and/or outputs. These registers will be placed outside of any embedded resources, such as block multipliers or DSP48E slices. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| CORDIC Details | Specifies options for the COordinate Rotation DIgital Computer (CORDIC) algorithm this function uses. Precision—Specifies options about the precision of the result(s) this function returns. Number of internal iterations—Specifies the number of cycles this function takes to return a valid result without considering input/output registers. Adapt to configuration—Specifies whether LabVIEW automatically determines the number of internal iterations based on the options you specify on the General page. By default, this checkbox contains a checkmark. Value—Specifies the number of cycles this function takes to return a valid result without considering input/output registers. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the number of internal iterations increases both the precision of the result and the latency of this function. Internal word length—Specifies the word length of internal calculations. Adapt to configuration—Specifies whether LabVIEW automatically determines the number of internal iterations based on the options you specify on the General page and the Value of the Number of internal iterations. By default, this checkbox contains a checkmark. Value—Specifies the word length of internal calculations. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page and theValue of theNumber of internal iterations. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the number of internal iterations increases both the precision of the result and the latency of this function. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies the input to this function. x must be in the range [1/e, 1) and unsigned. The integer word length must be 0 bits. input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select the Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire the ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. To displayready for output, select the Inside single-cycle Timed Loop in the configuration dialog box. ln(x) — Returns the natural logarithm of x. If x is outside the range [1/e, 1), ln(x) is undefined. undefined — Returns TRUE if ln(x) is undefined. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display output valid, select the Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the input valid terminal is TRUE during the following cycle. To display ready for input, select the Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

#### Computing ln(x) When x is Outside the Valid Range

The value of **x** must be within the range [1/e, 1). If **x** is outside the valid range, you can shift the binary point of **x** until the binary point is immediately to the left of the first nonzero bit of **x**. The resulting number *M* always is greater than or equal to 0.5, which is in the valid range [1/e, 1). Then let *E* equal the number of times you shifted the binary point to the left. You then can compute ln(*M*) + (*E* × ln(2)), which is equivalent to ln(**x**). Because *M* is in the valid range of [1/e, 1), you can use this function to compute ln(*M*).

Note

E

E

NI recommends a binary shift because this operation requires fewer FPGA resources than division does to transform **x** into *M*.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Natural Log\Natural Log.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Natural Log\Natural Log.lvproj

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpmul/xnode/nifxpmath-multiplier-xnode.html language=enus -->
## TOPIC 00257: High Throughput Multiply

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpmul/xnode/nifxpmath-multiplier-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpmul/xnode/nifxpmath-multiplier-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the product of x and y. This function supports only scalar and array values of the fixed-point data type. icon Dialog Box Options Parameter Description Fixed-Point Configuration Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this functio

### High Throughput Multiply

Computes the product of **x** and **y**.

This function supports only scalar and array values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpmath-multiplier-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Fixed-Point Configuration | Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type— Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. y Type— Specifies the fixed-point configuration of the y input terminal. If you wire a fixed-point data type to this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. x*y Type— Specifies the fixed-point configuration of the x*y output terminal. Adapt to source—Specifies whether LabVIEW automatically adjusts the fixed-point configuration of the output data type to avoid overflow and rounding errors. By default, this checkbox contains a checkmark and LabVIEW dims the following options. Note LabVIEW supports a maximum word length of 64 bits and a maximum integer word length of 2047 bits. If you place a checkmark in this checkbox and the output data type requires a word length that exceeds these maximum values, overflow and/or rounding errors might occur. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. Include overflow status—Specifies whether the output terminal includes the overflow status. LabVIEW propagates this status to downstream nodes. Including this status requires additional FPGA resources. By default, this checkbox does not contain a checkmark. If you place a checkmark in this checkbox, the overflow status becomes TRUE in either of the following situations: The overflow status of an input terminal is TRUE. Overflow occurs during the operation of this function. If you place a checkmark in the Adapt to source checkbox, LabVIEW sets Include overflow status depending on whether an input terminal includes this status. Overflow mode— Specifies how this function handles overflow. You can choose either Wrap (default) or Saturate. Note The Saturateoption requires more FPGA resources and a longer combinatorial path than the Wrap option does. In this situation, choosing Saturate might decrease the maximum clock rate at which this function can compile. Rounding mode— Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. |
| Execution Mode | Specifies how this function executes. Outside single-cycle Timed Loop— Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop— Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. |
| Pipelining Options | Specifies options for pipelining this function internally. These options affect the maximum clock rate this function can achieve. Refer to the Improving Function Performance by Pipelining section of this topic for information about this relationship. Number of pipelining stages—Specifies the number of pipelining stages this function uses internally. Increasing the number of stages increases the clock rate at which this function can compile but also increases the amount of FPGA resources this function requires. The default is 0 stages, which specifies no pipelining. The maximum is 12 stages because adding more than 12 stages does not increase the maximum clock rate at which this function can compile. Implementation resource—Specifies how to implement the multiplier. To enable this option, increase the Number of pipelining stages to be greater than 0 stages. You can choose from the following options: Auto(default)—Specifies that the compiler decides whether to use embedded block multipliers or look-up tables (LUTs) to implement the multiplier. Look-Up Table—Specifies that this function uses LUTs to implement the multiplier. Selecting this option might increase the clock rate at which this function can compile. |
| Registers | Specifies whether to add internal registers for function output terminal. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| Optional Terminal | Specifies a setting for displaying an optional block diagram terminal. Operation overflow—Specifies that this function displays the operation overflow output terminal on the block diagram. This terminal indicates whether overflow occurred during the operation of this function. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies the multiplicand. y — Specifies the multiplicand. input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node. To display this handshaking terminal, select the Inside single-cycle Timed Loop option and perform either of the following actions: Place a checkmark in either the Register inputs or Register outputs checkbox. Set the Number of pipelining stages to at least 1. These options are located in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire the ready for input output of a downstream node to this input of the current node. Note If this terminal is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. To display this terminal, select the Inside single-cycle Timed Loop option and perform either of the following actions: Place a checkmark in either the Register inputs or Register outputs checkbox. Set the Number of pipelining stages to at least 1. These options are located in the configuration dialog box. x*y — Returns the product of x and y. operation overflow — Returns TRUE if the theoretical computed value exceeds the valid range of the output data type. If operation overflow returns TRUE, the Overflow mode option determines the value this function returns. LabVIEW displays the operation overflow terminal only if you place a checkmark in the Operation overflow checkbox. This checkbox is located in the Optional Terminal section of the configuration dialog box. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. Wire this output to the input valid input of a downstream node to transfer data from the node to the downstream node. To display this terminal, select the Inside single-cycle Timed Loop option and perform either of the following actions: Place a checkmark in either the Register inputs or Register outputs checkbox. Set the Number of pipelining stages to at least 1. These options are located in the configuration dialog box. ready for input — Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the input valid terminal is TRUE during the following cycle. To display this terminal, select the Inside single-cycle Timed Loop option and perform either of the following actions: Place a checkmark in either the Register inputs or Register outputs checkbox. Set the Number of pipelining stages to at least 1. These options are located in the configuration dialog box. |
| --- |

During the cycles before **output valid** returns TRUE for the first time, this function might return different results on an FPGA target than on a host computer. The results become identical after the first time **output valid** returns TRUE.

#### Improving Function Performance by Pipelining

You can improve the timing performance of this function on an FPGA target by adjusting the **Number of pipelining stages**. The functionality of a [pipelined](/csh?context=lvfpga_lvfpgaconcepts_fpga_pipelining) multiplier is equivalent to a non-pipelined multiplier cascaded by a certain number of [registers](/csh?context=lvfpga_lvfpgaconcepts_fpga_basic_chip_terms). The number of registers is equal to the number of pipelining stages.

In general, increasing the **Number of pipelining stages** also increases the maximum clock rate this function can achieve. However, the actual clock rate depends on many factors, including the following ones:

- The FPGA target you use
- The size of the multiplier
- The rounding and overflow modes you select
- The Implementation resource you select
- Other FPGA logic besides the multiplier

The following graphs show the **Number of pipelining stages** vs. maximum clock rate estimations on Xilinx Virtex-II, Virtex-5, and Spartan-3 FPGA targets, respectively.

Note

[IMAGE alt='image' src='loc_xlsx_virtex2.gif']

In the previous figure, each line represents a multiplier of a certain size that uses a particular **Implementation resource**. For example, the **I32*I32 Block** line shows a multiplier that multiplies two 32-bit signed integers together by using an embedded block multiplier. The result is a signed 64-bit integer: <+/–,32,32> * <+/–,32,32> = <+/–,64,64>. If you use one pipelining stage on a Virtex-II FPGA target, this type of multiplier can achieve a maximum clock rate of about 51 MHz. If you use three pipelining stages, the maximum clock rate becomes about 76 MHz.

The following figures show similar information for other FPGA targets.

[IMAGE alt='image' src='loc_xlsx_spartan3.gif']

[IMAGE alt='image' src='loc_xlsx_virtex5.gif']

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Vector Normalization\Vector Normalization.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Vector Normalization\Vector Normalization.lvproj

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpmultcomplex/xnode/nifpgamultcomplex-xnode.html language=enus -->
## TOPIC 00258: High Throughput Complex Multiply

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpmultcomplex/xnode/nifpgamultcomplex-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpmultcomplex/xnode/nifpgamultcomplex-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the product of two complex numbers. The High Throughput Complex Multiply function multiplies two complex numbers x = x[r] + jx[i] and y = y[r] + jy[i], to produce a product p, as shown in the equation below. p = x*y = p[r] + jp[i] where p[r] = x[r]y[r] – x[i]y[i] and p[i] = x[r]y[i] + x[i]y

### High Throughput Complex Multiply

Computes the product of two complex numbers.

The High Throughput Complex Multiply function multiplies two complex numbers *x* = *x*<sub>r</sub> + *jx*<sub>i</sub> and *y* = *y*<sub>r</sub> + *jy*<sub>i</sub>, to produce a product *p*, as shown in the equation below.

*p* = *x***y* = *p*<sub>r</sub> + *jp*<sub>i</sub>

where *p*<sub>r</sub> = *x*<sub>r</sub>*y*<sub>r</sub> – *x*<sub>i</sub>*y*<sub>i</sub> and *p*<sub>i</sub> = *x*<sub>r</sub>*y*<sub>i</sub> + *x*<sub>i</sub>*y*<sub>r</sub>

This function supports only scalar values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifpgamultcomplex-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Fixed-Point Configuration | Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. xr/xi Type— Specifies the fixed-point configuration of the xr and xi input terminals. If you wire a fixed-point data type to these terminals, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. yr/yi Type— Specifies the fixed-point configuration of the yr and yi input terminals If you wire a fixed-point data type to these terminals, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. pr/pi Type— Specifies the fixed-point configuration of the pr and pi output terminals Adapt to source—Specifies whether LabVIEW automatically adjusts the fixed-point configuration of the output data type to avoid overflow and rounding errors. By default, this checkbox contains a checkmark and LabVIEW dims the following options. Note LabVIEW supports a maximum word length of 64 bits and a maximum integer word length of 2047 bits. If you place a checkmark in this checkbox and the output data type requires a word length that exceeds these maximum values, overflow and/or rounding errors might occur. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. Include overflow status—Specifies whether the output terminals include the overflow status. LabVIEW propagates this status to downstream nodes. Including this status requires additional FPGA resources. By default, this checkbox does not contain a checkmark. If you place a checkmark in this checkbox, the overflow status becomes TRUE in either of the following situations: The overflow status of an input terminal is TRUE. Overflow occurs during the operation of this function. Note If an overflow occurs internally during the operation of this function, LabVIEW sets the overflow bit in both pr and pi. If you place a checkmark in the Adapt to source checkbox, LabVIEW sets Include overflow status depending on whether an input terminal includes this status. Overflow mode— Specifies how this function handles overflow. You can choose either Wrap (default) or Saturate. Note The Saturate option requires more FPGA resources and a longer combinatorial path than the Wrap option does. In this situation, choosing Saturate might decrease the maximum clock rate at which this function can compile. Rounding mode— Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. The option you choose might affect the amount of resources this function requires. |
| Execution Mode | Specifies how this function executes. Outside single-cycle Timed Loop— Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop— Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. |
| Pipelining Options | Specifies options for pipelining this function internally. These options affect the maximum clock rate at which this function can compile. Refer to the Improving Function Performance by Pipelining section of this topic for information about this relationship. Number of pipelining stages—Specifies the number of pipelining stages this function uses internally. Increasing the number of stages increases the clock rate at which this function can compile but also increases the amount of FPGA resources this function requires. The default is 0 stages, which specifies no pipelining. The maximum is 11 stages Implementation resource—Specifies how to implement the multiplier. You can choose from the following options: Auto(default)—Specifies that the compiler decides whether to use embedded block multipliers or look-up tables (LUTs) to implement the multiplier. Look-Up Table—Specifies that this function uses LUTs to implement the multiplier. Selecting this option might increase the clock rate at which this function can compile. |
| Registers | Specifies whether to add internal registers for function inputs and/or outputs. These registers will be placed outside of any embedded resources, such as block multipliers or DSP48E slices. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| Optional Terminal | Specifies a setting for displaying an optional block diagram terminal. Operation overflow—Specifies that this function displays the operation overflow output terminal on the block diagram. This terminal indicates whether overflow occurred during the operation of this function. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| xr — Specifies the real part of the x multiplicand. xi — Specifies the imaginary part of the x multiplicand. yr — Specifies the real part of the y multiplicand. yi — Specifies the imaginary part of the y multiplicand. input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node. To display this handshaking terminal, select Inside single-cycle Timed Loop option and perform either of the following actions: Place a checkmark in either the Register inputs or Register outputs checkbox. Set the Number of pipelining stages to at least 1. These options are located in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input output of a downstream node to this input of the current node. Note If this terminal is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. To display this terminal, select the Inside single-cycle Timed Loop option and perform either of the following actions: Place a checkmark in either the Register inputs or Register outputs checkbox. Set the Number of pipelining stages to at least 1. These options are located in the configuration dialog box. pr — Returns the real part of the product. pi — Returns the imaginary part of the product. operation overflow — Returns TRUE if the theoretical computed value exceeds the valid range of the output data type. If operation overflow returns TRUE, the Overflow mode option determines the value this function returns. LabVIEW displays the operation overflow terminal only if you place a checkmark in the Operation overflow checkbox. This checkbox is located in the Optional Terminal section of the configuration dialog box. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. Wire this output to the input valid input of a downstream node to transfer data from the node to the downstream node. To display this terminal, select the Inside single-cycle Timed Loop option and perform either of the following actions: Place a checkmark in either the Register inputs or Register outputs checkbox. Set the Number of pipelining stages to at least 1. These options are located in the configuration dialog box. ready for input — Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the input valid terminal is TRUE during the following cycle. To display this terminal, select the Inside single-cycle Timed Loop option and perform either of the following actions: Place a checkmark in either the Register inputs or Register outputs checkbox. Set the Number of pipelining stages to at least 1. These options are located in the configuration dialog box. |
| --- |

During the cycles before **output valid** returns TRUE for the first time, this function might return different results on an FPGA target than on a host computer. The results become identical after the first time **output valid** returns TRUE.

#### Improving Function Performance by Pipelining

You can improve the timing performance of this function on an FPGA target by adjusting the **Number of pipelining stages**. The functionality of a [pipelined](/csh?context=lvfpga_lvfpgaconcepts_fpga_pipelining) multiplier is equivalent to a non-pipelined multiplier cascaded by a certain number of [registers](/csh?context=lvfpga_lvfpgaconcepts_fpga_basic_chip_terms). The number of registers is equal to the number of pipelining stages.

In general, increasing the **Number of pipelining stages** also increases the maximum clock rate at which this function can compile. However, the actual clock rate depends on many factors, including the following:

- The FPGA target you use
- The size of the multiplier
- The rounding and overflow modes you select
- The Implementation resource you select
- Other FPGA logic besides the multiplier

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxppolartorect/xnode/nifxpmath-polartorect-xnode.html language=enus -->
## TOPIC 00259: High Throughput Polar To Rectangular

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxppolartorect/xnode/nifxpmath-polartorect-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxppolartorect/xnode/nifxpmath-polartorect-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts polar coordinates to rectangular coordinates. You also can convert rectangular coordinates to polar coordinates. This function supports only the fixed-point data type. icon Dialog Box Options Option Description General Specifies general information about this function. Fixed-Point Configura

### High Throughput Polar To Rectangular

Converts polar coordinates to rectangular coordinates.

Note

convert rectangular coordinates to polar coordinates

This function supports only the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpmath-polartorect-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| General | Specifies general information about this function. Fixed-Point Configuration— Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. magnitude Type— Specifies the fixed-point configuration of the magnitude input terminal. If you wire a fixed-point data type to this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. The maximum value is 2045 bits. phase Type— Specifies the fixed-point configuration of the phase output terminal. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. x, y Type— Specifies the fixed-point configuration of the x and y output terminals. Signed—Specifies that these terminals are signed. The values can be either positive or negative, so LabVIEW sets the encoding to Signed and dims this option. Unsigned—Specifies that these terminals are unsigned. The values can be either positive or negative, so LabVIEW sets the encoding to Signed and dims this option. Word length—Specifies the word length of these terminals. LabVIEW dims this option and automatically determines this value according to the Word length of the magnitude input terminal. Integer word length—Specifies the integer word length of these terminals. LabVIEW dims this option and automatically determines this value according to the Integer word length of the magnitude input terminal. Rounding mode— Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. Execution Mode— Specifies how this function executes. Outside single-cycle Timed Loop— Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop— Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput— Specifies the minimum number of cycles between two successive values of valid input data. Entering a low value in this control results in a high throughput rate. The maximum value of Throughput depends on the Word length of the output terminal. This option is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, this function returns a valid result on every call to the function. Therefore, the Throughput control displays 1 call / sample. The Configuration Feedback indicator displays the number of clock cycles this function takes to return a valid result. Registers— Specifies whether to add internal registers for function inputs and/or outputs. These registers will be placed outside of any embedded resources, such as block multipliers or DSP48E slices. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| CORDIC Details | Specifies options for the COordinate Rotation DIgital Computer (CORDIC) algorithm this function uses. Precision— Specifies information about the internal precision of the CORDIC algorithm. Number of internal iterations—Specifies the number of cycles this function takes to return a valid result without considering input/output registers or any Gain compensation you select. Adapt to configuration—Specifies whether LabVIEW automatically determines the number of internal iterations based on the options you specify on the General page. By default, this checkbox contains a checkmark. Value—Specifies the number of cycles this function takes to return a valid result without considering input/output registers or any Gain compensation you select. By default, LabVIEW automatically determines this value and dims the control. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the number of internal iterations increases both the precision of the result and the latency of this function. Internal word length—Specifies the word length of internal calculations. Adapt to configuration—Specifies whether LabVIEW automatically determines the value of the internal word length based on the options you specify on the General page and the Value of the Number of internal iterations. By default, this checkbox contains a checkmark. Value—Specifies the word length of internal calculations. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page and the Value of the Number of internal iterations. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the internal word length increases the precision of the output, the amount of FPGA resources this function requires, and the length of the combinatorial path. Gain Compensation— Specifies whether this function uses gain compensation before returning the output terminal values. Yes—Specifies that this function returns the correct values. If you select this option, this function multiplies the internal results by the Gain reciprocal before returning these results to the output terminals. No—Specifies that this function returns incorrect values. If you select this option, this function does not multiply the internal results by the Gain reciprocal before returning these results to the output terminals. In this situation, this function uses fewer FPGA resources than if you selected Yes. To correct the values, you must multiply the outputs of this function by the Gain reciprocal that LabVIEW displays on this page. Select this option to save FPGA resources and have more control over when this multiplication happens. Gain reciprocal—Displays the value by which you must multiply the outputs of this function if you selected No gain compensation. If you selected Yes, this function performs this multiplication before returning the numeric results. In this situation, you do not need to use the Gain reciprocal value. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| magnitude — Specifies the magnitude. phase (pi) — Specifies the phase in pi radians, which use fewer FPGA resources than radians. If you have a value in radians, divide that value by pi before wiring the value to this input terminal. input valid — Specifies whether the next data point has arrived for processing. Wire output valid of an upstream node to input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for output, select Inside single-cycle Timed Loop in the configuration dialog box. x — Returns the x value of the rectangular coordinates. y — Returns the y value of the rectangular coordinates. output valid — Returns TRUE if this Express VI has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display output valid, select Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

#### Input Terminal Coercion

The CORDIC algorithm represents **phase** internally as a signed fixed-point number with a 1-bit integer word length. The word length of **phase** must be less than or equal to 64 bits. If you wire a value to **phase** that has a fractional word length greater than 63 bits, this function rounds off the lower bits to achieve a fractional word length of 63 bits. For example, if you wire a fixed-point data type with a configuration of <+/–,60,–5> to **phase**, this function coerces the configuration to be <+/–,58,–5>.

If you wire a fixed-point data type to **phase** with a fractional word length greater than 63 bits and an integer word length less than –62 bits, this function coerces the configuration to be <+/–,1,–62> if the data type is signed. If the data type is unsigned, the coerced configuration is <+,1,–62>.

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpreciprocal/xnode/nifxpmath-reciprocal-xnode.html language=enus -->
## TOPIC 00260: High Throughput Reciprocal

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpreciprocal/xnode/nifxpmath-reciprocal-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpreciprocal/xnode/nifxpmath-reciprocal-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes 1/x. This function rounds the result by truncating the value of the 1/x output terminal towards 0. This rounding mode uses fewer FPGA resources than other rounding modes do. This function supports only scalar values of the fixed-point data type. icon Dialog Box Options Option Description Fi

### High Throughput Reciprocal

Computes 1/**x**. This function [rounds the result](/csh?context=lvfpga_lvfpgaconcepts_fpgafixedpoint) by truncating the value of the **1/x** output terminal towards 0.

This function supports only scalar values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpmath-reciprocal-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Fixed-Point Configuration | Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type— Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal, LabVIEW dims this section and uses information from the wire. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. 1/x Type— Specifies the fixed-point configuration of the 1/x output terminal. Include overflow status—Specifies whether the output terminal includes the overflow status. LabVIEW propagates this status to downstream nodes. Including this status requires additional FPGA resources. By default, this checkbox does not contain a checkmark. If you place a checkmark in this checkbox, the overflow status becomes TRUE in either of the following situations: The overflow status of an input terminal is TRUE. Overflow occurs during the operation of this function. If you place a checkmark in the Adapt to source checkbox, LabVIEW sets Include overflow status depending on whether an input terminal includes this status. Word length—Specifies the word length of this terminal. Signed—Specifies that this terminal is signed. LabVIEW matches the encoding you specify in the x Type section and dims this option. Unsigned—Specifies that this terminal is unsigned. LabVIEW matches the encoding you specify in the x Type section and dims this option. Integer word length—Specifies the integer word length of this terminal. Adapt to source—Specifies whether LabVIEW automatically adjusts the fixed-point configuration of the output data type to avoid overflow for nonzero values of x. By default, this checkbox contains a checkmark and LabVIEW dims the following options. Note Because the precision of the square root might be infinite, rounding errors always occur. Overflow mode— Specifies how this function handles overflow. You can choose from the following options: Saturate (default)—Specifies that if overflow occurs, this function saturates the 1/x output terminal. Undefined result—Specifies that if overflow occurs, the value of the 1/x output terminal is undefined. Note The Undefined result option does not require any additional FPGA resources. Conversely, the Saturate option requires additional FPGA resources and a longer combinatorial path, which might decrease the maximum clock rate at which this function can compile. |
| Execution Mode | Specifies how this function executes. Outside single-cycle Timed Loop— Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop— Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput— Specifies the minimum number of cycles between two successive values of valid input data. Entering a low value in this control results in a high throughput rate. The maximum value of Throughput depends on the Word length of the output terminal. This option is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, this function returns a valid result on every call to the function. Therefore, the Throughput control displays 1 call / sample. The Configuration Feedback indicator displays the number of clock cycles this function takes to return a valid result. |
| Registers | Specifies whether to add internal registers for function inputs and/or outputs. These registers will be placed outside of any embedded resources, such as block multipliers or DSP48E slices. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| Optional Terminal | Specifies a setting for displaying an optional block diagram terminal. Operation overflow—Specifies that this function displays the operation overflow output terminal on the block diagram. This terminal indicates whether overflow occurred during the operation of this function. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies the input to this function. If the value of x is 0, overflow occurs in the 1/x output terminal. input valid — Specifies whether the next data point has arrived for processing. Wire output valid of an upstream node to input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for output, select Inside single-cycle Timed Loop in the configuration dialog box. 1/x — Returns 1/x. operation overflow — Returns TRUE if the theoretical computed value exceeds the valid range of the output data type. If operation overflow returns TRUE, the Overflow mode option determines the value this function returns. LabVIEW displays the operation overflow terminal only if you place a checkmark in the Operation overflow checkbox. This checkbox is located in the Optional Terminal section of the configuration dialog box. output valid — Returns TRUE if this Express VI has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display output valid, select Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxprecttopolar/xnode/nifxpmath-recttopolar-xnode.html language=enus -->
## TOPIC 00261: High Throughput Rectangular To Polar

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxprecttopolar/xnode/nifxpmath-recttopolar-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxprecttopolar/xnode/nifxpmath-recttopolar-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts rectangular coordinates to polar coordinates. You also can convert polar coordinates to rectangular coordinates. This function supports only scalar values of the fixed-point data type. icon Dialog Box Options Option Description General Specifies general information about this function. Fixe

### High Throughput Rectangular To Polar

Converts rectangular coordinates to polar coordinates.

Note

convert polar coordinates to rectangular coordinates

This function supports only scalar values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpmath-recttopolar-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| General | Specifies general information about this function. Fixed-Point Configuration— Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type— Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal and that data type follows the rules for this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. If the encoding is Signed, the maximum value is 64 bits. If the encoding is Unsigned, the maximum value is 63 bits. Integer word length—Specifies the integer word length of this terminal. If the encoding is Signed, the maximum value is 2047 bits. If the encoding is Unsigned, the maximum value is 2046 bits. As you change the value of this control, LabVIEW might change the Integer word length of the other input terminal. These changes maintain the supported fixed-point configuration of the shared internal data type. y Type— Specifies the fixed-point configuration of the y input terminal. If you wire a fixed-point data type to this terminal and that data type follows the rules for this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. If the encoding is Signed, the maximum value is 64 bits. If the encoding is Unsigned, the maximum value is 63 bits. Integer word length—Specifies the integer word length of this terminal. If the encoding is Signed, the maximum value is 2047 bits. If the encoding is Unsigned, the maximum value is 2046 bits. As you change the value of this control, LabVIEW might change the Integer word length of the other input terminal. These changes maintain the supported fixed-point configuration of the shared internal data type. magnitude Type— Specifies the fixed-point configuration of the magnitude output terminal. Signed—Specifies that this terminal is signed. magnitude always is positive or equal to 0, so LabVIEW sets the encoding to Unsigned and dims this option. Unsigned—Specifies that this terminal is unsigned. magnitude always is positive or equal to 0, so LabVIEW sets the encoding to Unsigned and dims this option. Word length—Specifies the word length of this terminal. LabVIEW dims this option and automatically determines the value based on the fixed-point configurations you specify in the x Type and y Type sections. Integer word length—Specifies the integer word length of this terminal. LabVIEW dims this option and automatically determines the value based on the fixed-point configurations you specify in the x Type and y Type sections. phase Type— Specifies the fixed-point configuration of the phase output terminal. Signed—Specifies that this terminal is signed. phase can be either positive or negative, so LabVIEW sets the encoding to Signed and dims this option. Unsigned—Specifies that this terminal is unsigned. phase can be either positive or negative, so LabVIEW sets the encoding to Signed and dims this option. Word length—Specifies the word length of this terminal. The value must be between 4 and 64 bits. Integer word length—Specifies the integer word length of this terminal. LabVIEW sets this value to 2 bits and dims this option. Rounding mode— Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. Execution Mode— Specifies how this function executes. Outside single-cycle Timed Loop— Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop— Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput— Specifies the minimum number of cycles between two successive values of valid input data. Entering a low value in this control results in a high throughput rate. The maximum value of Throughput depends on the Word length of the output terminal. This option is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, this function returns a valid result on every call to the function. Therefore, the Throughput control displays 1 call / sample. The Configuration Feedback indicator displays the number of clock cycles this function takes to return a valid result. Registers— Specifies whether to add internal registers for function inputs and/or outputs. These registers will be placed outside of any embedded resources, such as block multipliers or DSP48E slices. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| CORDIC Details | Specifies options for the COordinate Rotation DIgital Computer (CORDIC) algorithm this function uses. Precision— Specifies options about the precision of the result(s) this function returns. Number of internal iterations—Specifies the number of cycles this function takes to return a valid result without considering input/output registers or any Gain compensation you select. Adapt to configuration—Specifies whether LabVIEW automatically determines the number of internal iterations based on the options you specify on the General page. By default, this checkbox contains a checkmark. Value—Specifies the number of cycles this function takes to return a valid result without considering input/output registers or any Gain compensation you select. By default, LabVIEW automatically determines this value and dims the control. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the number of internal iterations increases both the precision of the result and the latency of this function. Internal word length—Specifies the word length of internal calculations. Adapt to configuration—Specifies whether LabVIEW automatically determines the value of the internal word length based on the options you specify on the General page and the Value of the Number of internal iterations. By default, this checkbox contains a checkmark. Value—Specifies the word length of internal calculations. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page and the Value of the Number of internal iterations. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the internal word length increases the precision of the output, the amount of FPGA resources this function requires, and the length of the combinatorial path. Gain Compensation—Specifies whether this function uses gain compensation before returning the output terminal values. Yes—Specifies that this function returns the correct values. If you select this option, this function multiplies the internal results by the Gain reciprocal before returning these results to the output terminals. No—Specifies that this function returns incorrect values. If you select this option, this function does not multiply the internal results by the Gain reciprocal before returning these results to the output terminals. In this situation, this function uses fewer FPGA resources than if you selected Yes. To correct the values, you must multiply the outputs of this function by the Gain reciprocal that LabVIEW displays on this page. Select this option to save FPGA resources and have more control over when this multiplication happens. Gain reciprocal—Displays the value by which you must multiply the outputs of this function if you selected No gain compensation. If you selected Yes, this function performs this multiplication before returning the numeric results. In this situation, you do not need to use the Gain reciprocal value. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies the x value of the rectangular coordinates. Note If you wire an unsigned value to this terminal that has a word length of 64 bits, LabVIEW coerces the word length to be 63 bits and displays a coercion dot on the wire. y — Specifies the y value of the rectangular coordinates. Note If you wire an unsigned value to this terminal that has a word length of 64 bits, LabVIEW coerces the word length to be 63 bits and displays a coercion dot on the wire. input valid — Specifies whether the next data point has arrived for processing. Wire output valid of an upstream node to input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for output, select Inside single-cycle Timed Loop in the configuration dialog box. magnitude — Returns the magnitude. phase (pi) — Returns the phase in pi radians, which use fewer FPGA resources than radians. To convert this value into radians, multiply phase by pi. output valid — Returns TRUE if this Express VI has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display output valid, select Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

#### Input Terminals Coercion

If you wire a fixed-point data type to only one input terminal, this function coerces the unwired terminal to match the configuration of the wired terminal. You can right-click the unwired terminal and select **Create»Control** or **Create»Constant**. This action creates a second fixed-point data type with the same configuration as the wired terminal.

If you wire fixed-point data types with different configurations to the input terminals, this function uses a shared, signed fixed-point data type to represent the value of both terminals internally. The maximum word length of this internal data type is 64 bits. If the configurations of the input terminals result in an internal word length greater than 64 bits, this function rounds off the fractional bits of one input terminal to achieve an internal word length of 64 bits. This function rounds off the input terminal that has the most fractional bits.

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpsinandcos/xnode/nifxpmath-sinandcos-xnode.html language=enus -->
## TOPIC 00262: High Throughput Sine & Cosine

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpsinandcos/xnode/nifxpmath-sinandcos-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpsinandcos/xnode/nifxpmath-sinandcos-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the sine and cosine of x. This function assumes that x is in pi radians. This function supports only scalar values of the fixed-point data type. icon Dialog Box Options Option Description General Specifies general information about this function. Fixed-Point Configuration— Specifies the enc

### High Throughput Sine & Cosine

Computes the sine and cosine of **x**. This function assumes that **x** is in pi radians.

This function supports only scalar values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpmath-sinandcos-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| General | Specifies general information about this function. Fixed-Point Configuration— Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type— Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. sin(x), cos(x) Type— Specifies the fixed-point configuration of the sin(x) and cos(x) output terminals. Signed—Specifies that these terminals are signed. The values can be either positive or negative, so LabVIEW sets the encoding to Signed and dims this option. Unsigned—Specifies that these terminals are unsigned. The values can be either positive or negative, so LabVIEW sets the encoding to Signed and dims this option. Word length—Specifies the word length of this terminal. The value must be between 4 and 64 bits. Integer word length—Specifies the integer word length of this terminal. LabVIEW sets this value to 2 bits and dims this option. Rounding mode— Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. Execution Mode— Specifies how this function executes. Outside single-cycle Timed Loop— Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop— Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput— Specifies the minimum number of cycles between two successive values of valid input data. Entering a low value in this control results in a high throughput rate. The maximum value of Throughput depends on the Word length of the output terminal. This option is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, this function returns a valid result on every call to the function. Therefore, the Throughput control displays 1 call / sample. The Configuration Feedback indicator displays the number of clock cycles this function takes to return a valid result. Registers— Specifies whether to add internal registers for function inputs and/or outputs. These registers will be placed outside of any embedded resources, such as block multipliers or DSP48E slices. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| CORDIC Details | Specifies options for the COordinate Rotation DIgital Computer (CORDIC) algorithm this function uses. Precision— Specifies options about the precision of the result(s) this function returns. Number of internal iterations—Specifies the number of cycles this function takes to return a valid result without considering input/output registers. Adapt to configuration—Specifies whether LabVIEW automatically determines the number of internal iterations based on the options you specify on the General page. By default, this checkbox contains a checkmark. Value—Specifies the number of cycles this function takes to return a valid result without considering input/output registers. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the number of internal iterations increases both the precision of the result and the latency of this function. Internal word length—Specifies the word length of internal calculations. Adapt to configuration—Specifies whether LabVIEW automatically determines the value of the internal word length based on the options you specify on the General page and the Value of the Number of internal iterations. By default, this checkbox contains a checkmark. Value—Specifies the word length of internal calculations. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page and the Value of the Number of internal iterations. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the internal word length increases the precision of the output, the amount of FPGA resources this function requires, and the length of the combinatorial path. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x (pi) — Specifies the input to this function. x must be in units of pi radians, which use fewer FPGA resources than radians. If you have a value in radians, divide that value by pi before wiring the value to this input terminal. input valid — Specifies whether the next data point has arrived for processing. Wire output valid of an upstream node to input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for output, select Inside single-cycle Timed Loop in the configuration dialog box. sin(x) — Returns the sine of x. cos(x) — Returns the cosine of x. output valid — Returns TRUE if this Express VI has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display output valid, select Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

#### Input Terminal Coercion

The CORDIC algorithm represents **x** internally as a fixed-point number with a 1-bit integer word length. The word length of **x** must be less than or equal to 64 bits, which means the fractional word length must be less than or equal to 63 bits. If you wire a value to **x** that has a fractional word length greater than 63 bits, this function rounds off the lower bits to achieve a fractional word length of 63 bits. For example, if you wire a fixed-point data type with a configuration of <+/–,60,–5> to **x**, this function coerces the configuration to be <+/–,58,–5>.

If you wire a fixed-point data type to **x** with a fractional word length greater than 63 bits and an integer word length less than –62 bits, this function coerces the configuration to be <+/–,1,–62> if the data type is signed. If the data type is unsigned, the coerced configuration is <+,1,–62>.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Sine and Cosine\Sine and Cosine.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Sine and Cosine\Sine and Cosine.lvproj

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpsinhandcosh/xnode/nifxpmath-sinhandcosh-xnode.html language=enus -->
## TOPIC 00263: High Throughput Hyperbolic Sine & Cosine

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpsinhandcosh/xnode/nifxpmath-sinhandcosh-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpsinhandcosh/xnode/nifxpmath-sinhandcosh-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the hyperbolic sine and cosine of x. The value of x must be in the range [–1, 1). This function supports only scalar values of the fixed-point data type. icon Dialog Box Options Option Description General Specifies general information about this function. Fixed-Point Configuration— Specifie

### High Throughput Hyperbolic Sine & Cosine

Computes the hyperbolic sine and cosine of **x**. The value of **x** must be in the range [–1, 1).

This function supports only scalar values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpmath-sinhandcosh-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| General | Specifies general information about this function. Fixed-Point Configuration— Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type— Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal and that data type follows the rules for this terminal, LabVIEW dims this section and uses information from the wire. If you wire a fixed-point data type to this terminal that does not follow the rules, LabVIEW breaks the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. If the encoding is Signed, the maximum value is 1 bit. If the encoding is Unsigned, the maximum value is 0 bits. sinh(x) Type— Specifies the fixed-point configuration of the sinh(x) output terminal. Signed—Specifies that this terminal is signed. sinh(x) can be either positive or negative, so LabVIEW sets the encoding to Signed and dims this option. Unsigned—Specifies that this terminal is unsigned. sinh(x) can be either positive or negative, so LabVIEW sets the encoding to Signed and dims this option. Word length—Specifies the word length of this terminal. The value must be between 4 and 64 bits. LabVIEW adjusts the word length of the cosh(x) output terminal to use one fewer bit than the word length of the sinh(x) output terminal. Integer word length—Specifies the integer word length of this terminal. LabVIEW sets this value to 2 bits and dims this option. cosh(x) Type— Specifies the fixed-point configuration of the cosh(x) output terminal. Signed—Specifies that this terminal is signed. cosh(x) always is positive, so LabVIEW sets the encoding to Unsigned and dims this option. Unsigned—Specifies that this terminal is unsigned. cosh(x) always is positive, so LabVIEW sets the encoding to Unsigned and dims this option. Word length—Specifies the word length of this terminal. The value must be between 3 and 63 bits. LabVIEW adjusts the word length of the sinh(x) output terminal to use one more bit than the word length of the cosh(x) output terminal. Integer word length—Specifies the integer word length of this terminal. LabVIEW sets this value to 1 bit and dims this option. Rounding mode— Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. Execution Mode— Specifies how this function executes. Outside single-cycle Timed Loop— Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop— Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput— Specifies the minimum number of cycles between two successive values of valid input data. Entering a low value in this control results in a high throughput rate. The maximum value of Throughput depends on the Word length of the output terminal. This option is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, this function returns a valid result on every call to the function. Therefore, the Throughput control displays 1 call / sample. The Configuration Feedback indicator displays the number of clock cycles this function takes to return a valid result. Registers— Specifies whether to add internal registers for function inputs and/or outputs. These registers will be placed outside of any embedded resources, such as block multipliers or DSP48E slices. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| CORDIC Details | Specifies options for the COordinate Rotation DIgital Computer (CORDIC) algorithm this function uses. Precision— Specifies options about the precision of the result(s) this function returns. Number of internal iterations—Specifies the number of cycles this function takes to return a valid result without considering input/output registers. Adapt to configuration—Specifies whether LabVIEW automatically determines the number of internal iterations based on the options you specify on the General page. By default, this checkbox contains a checkmark. Value—Specifies the number of cycles this function takes to return a valid result without considering input/output registers. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the number of internal iterations increases both the precision of the result and the latency of this function. Internal word length—Specifies the word length of internal calculations. Adapt to configuration—Specifies whether LabVIEW automatically determines the value of the internal word length based on the options you specify on the General page and the Value of the Number of internal iterations. By default, this checkbox contains a checkmark. Value—Specifies the word length of internal calculations. By default, LabVIEW dims this control and automatically determines this value based on the options you specify on the General page and the Value of the Number of internal iterations. To enable this control, remove the checkmark from the Adapt to configuration checkbox. Increasing the internal word length increases the precision of the output, the amount of FPGA resources this function requires, and the length of the combinatorial path. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies the input to this function. x must be in the range [–1, 1]. input valid — Specifies whether the next data point has arrived for processing. Wire output valid of an upstream node to input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for output, select Inside single-cycle Timed Loop in the configuration dialog box. sinh(x) — Returns the hyperbolic sine of x. cosh(x) — Returns the hyperbolic cosine of x. output valid — Returns TRUE if this Express VI has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display output valid, select Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

#### Computing sinh(x) and cosh(x) When x is Outside the Valid Range

**x** must be in the range [–1, 1). To compute sinh(**x**) and cosh(**x**) when **x** is outside this range, find an integer *q* and a real number *r*, where *r* is in the range [0, ln(2)), such that **x** = *q* × ln(2) + *r*. You then can make the following computations:

- 2^(q – 1)[cosh( r ) + sinh( r ) – 2^(–2q)(cosh( r ) – sinh( r ))], which is equivalent to sinh( x ).
- 2^(q – 1)[cosh( r ) + sinh( r ) + 2^(–2q)(cosh( r ) – sinh( r ))], which is equivalent to cosh( x ).

Because *r* is in the valid range of [–1, 1), you can use this function to compute sinh(*r*) and cosh(*r*).

#### Input Terminal Coercion

The CORDIC algorithm represents **x** internally as a fixed-point number with a 1-bit integer word length. The word length of **x** must be less than or equal to 64 bits, which means the fractional word length must be less than or equal to 63 bits. If you wire a value to **x** that has a fractional word length greater than 63 bits, this function rounds off the lower bits to achieve a fractional word length of 63 bits. For example, if you wire a fixed-point data type with a configuration of <+/–,60,–5> to **x**, this function coerces the configuration to be <+/–,58,–5>.

If you wire a fixed-point data type to **x** with a fractional word length greater than 63 bits and an integer word length less than –62 bits, this function coerces the configuration to be <+/–,1,–62> if the data type is signed. If the data type is unsigned, the coerced configuration is <+,1,–62>.

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpsqrt/xnode/nifxpmath-sqrt-xnode.html language=enus -->
## TOPIC 00264: High Throughput Square Root

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpsqrt/xnode/nifxpmath-sqrt-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpsqrt/xnode/nifxpmath-sqrt-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the square root of x. The encoding of x must be unsigned. This function supports only scalar values of the fixed-point data type. icon Dialog Box Options Option Description Fixed-Point Configuration Specifies the encodings, word lengths, and integer word lengths of the input and output term

### High Throughput Square Root

Computes the square root of **x**. The encoding of **x** must be unsigned.

This function supports only scalar values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpmath-sqrt-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Fixed-Point Configuration | Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type— Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal and that data type follows the rules for this terminal, LabVIEW dims this section and uses information from the wire. If you wire a fixed-point data type to this terminal that does not follow the rules, LabVIEW breaks the wire. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. Signed—Specifies that this terminal is signed. LabVIEW sets the encoding to Unsigned and dims this option. Unsigned—Specifies that this terminal is unsigned. LabVIEW sets the encoding to Unsigned and dims this option. sqrt(x) Type— Specifies the fixed-point configuration of the sqrt(x) output terminal. Include overflow status—Specifies whether the output terminal includes the overflow status. LabVIEW propagates this status to downstream nodes. Including this status requires additional FPGA resources. By default, this checkbox does not contain a checkmark. If you place a checkmark in this checkbox, the overflow status becomes TRUE in either of the following situations: The overflow status of an input terminal is TRUE. Overflow occurs during the operation of this function. If you place a checkmark in the Adapt to source checkbox, LabVIEW sets Include overflow status depending on whether an input terminal includes this status. Word length—Specifies the word length of this terminal. Signed—Specifies that this terminal is signed. sqrt(x) always is greater than or equal to 0, so LabVIEW sets the encoding to Unsigned and dims this option. Unsigned—Specifies that this terminal is unsigned. sqrt(x) always is greater than or equal to 0, so LabVIEW sets the encoding to Unsigned and dims this option. Integer word length—Specifies the integer word length of this terminal. LabVIEW sets this value based on the Integer word length you specify in the x Type section and dims this option. Adapt to source—Specifies whether LabVIEW automatically adjusts the fixed-point configuration of the output data type to avoid overflow. By default, this checkbox contains a checkmark and LabVIEW dims the following options. Note Because the precision of the square root might be infinite, rounding errors always occur. Overflow mode— Specifies how this function handles overflow. You can choose either Wrap (default) or Saturate. Note The Saturate option requires more FPGA resources and a longer combinatorial path than the Wrap option does. In this situation, choosing Saturate might decrease the maximum clock rate at which this function can compile. Rounding mode— Specifies how this function rounds the output data. You can choose Truncate (default), Round Half-Up, or Round Half-Even. The option you choose might affect the amount of resources this function requires. |
| Execution Mode | Specifies how this function executes. Outside single-cycle Timed Loop— Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop— Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput— Specifies the minimum number of cycles between two successive values of valid input data. Entering a low value in this control results in a high throughput rate. The maximum value of Throughput depends on the Word length of the output terminal. This option is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, this function returns a valid result on every call to the function. Therefore, the Throughput control displays 1 call / sample. The Configuration Feedback indicator displays the number of clock cycles this function takes to return a valid result. |
| Registers | Specifies whether to add internal registers for function inputs and/or outputs. These registers will be placed outside of any embedded resources, such as block multipliers or DSP48E slices. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register inputs—Adds internal registers after the inputs to this function. Selecting this option increases the latency of the function by one cycle. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| Optional Terminal | Specifies a setting for displaying an optional block diagram terminal. Operation overflow—Specifies that this function displays the operation overflow output terminal on the block diagram. This terminal indicates whether overflow occurred during the operation of this function. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies the input to this function. x must be unsigned. input valid — Specifies whether the next data point has arrived for processing. Wire output valid of an upstream node to input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for output, select Inside single-cycle Timed Loop in the configuration dialog box. sqrt(x) — Returns the square root of x. operation overflow — Returns TRUE if the theoretical computed value exceeds the valid range of the output data type. If operation overflow returns TRUE, the Overflow mode option determines the value this function returns. LabVIEW displays the operation overflow terminal only if you place a checkmark in the Operation overflow checkbox. This checkbox is located in the Optional Terminal section of the configuration dialog box. output valid — Returns TRUE if this Express VI has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display output valid, select Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

If you place a checkmark in the **Adapt to source** checkbox, overflow still can occur in the **sqrt(x)** output terminal if all of the following conditions are true:

- The Rounding mode is Round Half-Up or Round Half-Even .
- The Integer word length of x is an even number.
- The following relationship is true: 
 [IMAGE alt='image' src='loc_eq_htsqrt_overflow.gif'], where *fwl* refers to the fractional word length of a terminal and *iwl* refers to the integer word length of a terminal.

Complete the following steps to avoid overflow in this situation:

1. Remove the checkmark from the Adapt to source checkbox.
2. Increase the Word length of the sqrt(x) terminal.

After you complete these steps, LabVIEW does not adjust the fixed-point configuration of the **sqrt(x)** terminal automatically. If you change the fixed-point configuration of the **x** terminal and still want to avoid overflow, place a checkmark in the **Adapt to source checkbox** again. LabVIEW adjusts the fixed-point configuration of the **sqrt(x)** terminal automatically. Then, complete steps 1–2 above to ensure that no overflow occurs with the updated fixed-point configuration.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Vector Normalization\Vector Normalization.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Vector Normalization\Vector Normalization.lvproj

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpsub/xnode/nifxpmath-sub-xnode.html language=enus -->
## TOPIC 00265: High Throughput Subtract

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpsub/xnode/nifxpmath-sub-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpsub/xnode/nifxpmath-sub-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the difference between x and y. This function supports only scalar and array values of the fixed-point data type. icon Dialog Box Options Parameter Description Fixed-Point Configuration Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this

### High Throughput Subtract

Computes the difference between **x** and **y**.

This function supports only scalar and array values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpmath-sub-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Fixed-Point Configuration | Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type— Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal and that data type follows the rules for this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. y Type— Specifies the fixed-point configuration of the y input terminal. If you wire a fixed-point data type to this terminal and that data type follows the rules for this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. x-y Type— Specifies the fixed-point configuration of the x-y output terminal. Adapt to source—Specifies whether LabVIEW automatically adjusts the fixed-point configuration of the output data type to avoid overflow and rounding errors. By default, this checkbox contains a checkmark and LabVIEW dims the following options. Note LabVIEW supports a maximum word length of 64 bits and a maximum integer word length of 2047 bits. If you place a checkmark in this checkbox and the output data type requires a word length that exceeds these maximum values, overflow and/or rounding errors might occur. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. Include overflow status—Specifies whether the output terminal includes the overflow status. LabVIEW propagates this status to downstream nodes. Including this status requires additional FPGA resources. By default, this checkbox does not contain a checkmark. If you place a checkmark in this checkbox, the overflow status becomes TRUE in either of the following situations: The overflow status of an input terminal is TRUE. Overflow occurs during the operation of this function. If you place a checkmark in the Adapt to source checkbox, LabVIEW sets Include overflow status depending on whether an input terminal includes this status. Overflow mode—Specifies how this function handles overflow. You can choose either Wrap (default) or Saturate. Note The Saturateoption requires more FPGA resources and a longer combinatorial path than the Wrap option does. In this situation, choosing Saturate might decrease the maximum clock rate at which this function can compile. Rounding mode—Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose mightaffect the amount of resources this function requires. |
| Execution Mode | Specifies how this function executes. Outside single-cycle Timed Loop—Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop—Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput—Displays the number of cycles between two successive values of valid input data. This number always is one cycle. Therefore, LabVIEW sets the value according to where you place this Express VI. If you select Inside single-cycle Timed Loop,LabVIEW sets the throughput to 1 cycle / sample. If you select Outside single-cycle Timed Loop, LabVIEW sets the throughput to 1 call / sample. |
| Registers | Specifies whether to add internal registers for function output terminal. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| Optional Terminal | Specifies a setting for displaying an optional block diagram terminal. Operation overflow—Specifies that this function displays the operation overflow output terminal on the block diagram. This terminal indicates whether overflow occurred during the operation of this function. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies an input to this function. y — Specifies an input to this function. input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node. To display this handshaking terminal, select the Inside single-cycle Timed Loop option and place a checkmark in the Register outputs checkbox. These options are located in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If this terminal is FALSE during a given cycle, the output valid returns FALSE during that cycle. To display this terminal, select Inside single-cycle Timed Loop option and place a checkmark in the Register outputs checkbox. These options are located in the configuration dialog box. x-y — Returns the difference between x and y. operation overflow — Returns TRUE if the theoretical computed value exceeds the valid range of the output data type. If operation overflow returns TRUE, the Overflow mode option determines the value this function returns. LabVIEW displays the operation overflow terminal only if you place a checkmark in the Operation overflow checkbox. This checkbox is located in the Optional Terminal section of the configuration dialog box. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. Wire this output to the input valid input of a downstream node to transfer data from the node to the downstream node. To display this terminal, select the Inside single-cycle Timed Loop option and place a checkmark in the Register outputs checkbox. These options are located in the configuration dialog box. ready for input — Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the input valid terminal is TRUE during the following cycle. To display this terminal, select the Inside single-cycle Timed Loop option and place a checkmark in the Register outputs checkbox. These options are located in the configuration dialog box. |
| --- |

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nifpgainterfacerefnumconstant-vi.html language=enus -->
## TOPIC 00266: FPGA Interface Dynamic Refnum

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nifpgainterfacerefnumconstant-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nifpgainterfacerefnumconstant-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FPGA Interface Dynamic Refnum constant to specify an FPGA interface. Specify the configuration of the interface by right-clicking the constant and selecting Configure FPGA VI Reference from the shortcut menu. icon Use this function with the Dynamic FPGA Interface Cast function to create a dy

### FPGA Interface Dynamic Refnum

Use the FPGA Interface Dynamic Refnum constant to specify an FPGA interface. Specify the configuration of the interface by right-clicking the constant and selecting [Configure FPGA VI Reference](/csh?context=lvfpga_lvfpgahost_config_fpga_vi_ref) from the shortcut menu.

[IMAGE alt='icon' src='nifpgainterfacerefnumconstant-vi.png']

Use this function with the [Dynamic FPGA Interface Cast](../../../functions/dynamic-fpga-interface-cast.html) function to create a [dynamic host interface](/csh?context=lvfpga_lvfpgahosthelp_fpga_dynamic_host_interface).

Parent topic:

FPGA Interface

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirviclosefpga/nirviclosefpga-xnode.html language=enus -->
## TOPIC 00267: Close FPGA VI Reference

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirviclosefpga/nirviclosefpga-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirviclosefpga/nirviclosefpga-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the reference to the FPGA VI and, optionally, resets execution of the VI. By default, the Close FPGA VI Reference function closes the reference to the FPGA VI and resets the FPGA VI. To configure this function only to close the reference, right-click the function and select Close from the sho

### Close FPGA VI Reference

Closes the reference to the FPGA VI and, optionally, resets execution of the VI. By default, the Close FPGA VI Reference function closes the reference to the FPGA VI and resets the FPGA VI. To configure this function only to close the reference, right-click the function and select **Close** from the shortcut menu.

The Close FPGA VI Reference function also stops all DMA FIFOs on the FPGA.

[IMAGE alt='icon' src='nirviclosefpga-xnode.png']

#### Inputs/Outputs

| FPGA VI Reference In — FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

The Close FPGA VI Reference function has different options in the shortcut menu depending on where you configure the FPGA VI to execute. The following table lists the different options.

| Location of FPGA VI Execution | Shortcut Options for Close FPGA VI Reference |
| --- | --- |
| FPGA target | Close Close and Reset if Last Reference |
| Development computer | Close Close and Abort without Reference Counting |

The following table describes the options in more detail.

| Option | Description |
| --- | --- |
| Close | Closes the reference to the FPGA VI without resetting or aborting the FPGA VI. |
| Close and Reset if Last Reference | (Default) Closes the reference to the FPGA VI and resets the VI if no other references to the VI are open. Resetting the VI returns VI controls and indicators to default states, sets global variables and uninitialized shift registers to default values, and clears FIFOs. Note LabVIEW does not support this option for applications with implicit enable signals removed from single-cycle Timed Loops. |
| Close and Abort without Reference Counting | Closes the reference to the FPGA VI and aborts the FPGA VI. Aborting the FPGA VI resets values in the VI only if the VI is not in memory. A VI remains in memory if the front panel is open, the VI is a subVI of another VI, or another component references the VI. If you abort a VI and the VI is in memory, the next time you open a reference to the VI, the VI is in the same state as when you closed the reference. |

Parent topic:

FPGA Interface

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/abort-invoke-method.html language=enus -->
## TOPIC 00268: Abort (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/abort-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/abort-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts the opened and running FPGA VI on the FPGA target. This method does not reset the default values in the FPGA VI. I/O maintains its previous state upon abort. Use the Invoke Method function to implement this method. You cannot use this method if you enable the removal of implicit enable signal

### Abort (Invoke Method)

Aborts the opened and running FPGA VI on the FPGA target. This method does not reset the default values in the FPGA VI. I/O maintains its previous state upon abort.

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

Note

implicit enable signals

[IMAGE alt='image' src='fpga_method_abort.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. If an error occurred before this node runs, the node passes the error in value to error out. If an error occurs while this node runs, the node runs normally and merges error in and its own error status to produce error out. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/acknowledge-irq-invoke-method.html language=enus -->
## TOPIC 00269: Acknowledge IRQ (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/acknowledge-irq-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/acknowledge-irq-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acknowledges and resets to the default value any interrupts that occur. After a successful Wait on IRQ method, use the Acknowledge IRQ method to acknowledge the source of the interrupt. Use the Invoke Method function to implement this method. Option Description FPGA VI Reference In FPGA VI Reference

### Acknowledge IRQ (Invoke Method)

Acknowledges and resets to the default value any interrupts that occur. After a successful Wait on IRQ method, use the Acknowledge IRQ method to acknowledge the source of the interrupt.

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_ack_irq.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| IRQ Number(s) | IRQ Number(s) specifies the logical interrupt or array of logical interrupts the function acknowledges. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/download-invoke-method.html language=enus -->
## TOPIC 00270: Download (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/download-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/download-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Downloads the most recent version of the compiled FPGA VI or bitfile to the FPGA target regardless of whether the compiled FPGA VI or bitfile has changed. Use this method when you want to reinitialize the FPGA VI on the FPGA target, especially when you allow the compiler to remove implicit enable si

### Download (Invoke Method)

Downloads the most recent version of the compiled FPGA VI or bitfile to the FPGA target regardless of whether the compiled FPGA VI or bitfile has changed. Use this method when you want to reinitialize the FPGA VI on the FPGA target, especially when you allow the compiler to [remove implicit enable signals](/csh?context=lvfpga_lvfpgaconcepts_fpga_routing_congestion) from single-cycle Timed Loops. You must use the [Open FPGA VI Reference](/csh?context=lvfpga_lvfpgahosthelp_fpga_opening_vi_reference) function to open a reference to the FPGA VI before you download this FPGA VI.

Note

Run when loaded to FPGA

Run

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_download.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/fifo-acquire-read-region-invoke-method.html language=enus -->
## TOPIC 00271: FIFO.Acquire Read Region (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/fifo-acquire-read-region-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/fifo-acquire-read-region-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requests a region to read from the host memory buffer in the target device driver and returns an external data value reference to this region. This method automatically starts the DMA channel if called without a previous call to the Start method. The Acquire Read Region method is available only if t

### FIFO.Acquire Read Region (Invoke Method)

Requests a region to read from the host memory buffer in the target device driver and returns an [external data value reference](/csh?productcategories=147794&context=lvcore_lvconcepts_external_data_val_ref) to this region. This method automatically starts the DMA channel if called without a previous call to the Start method.

Note

Type

Target to Host—DMA

General FIFO Properties

Refer to [Improving Efficiency When Accessing DMA FIFOs](/csh?context=lvfpga_lvfpgahelp_fpga_zerocopy_dma) for more information about using this method.

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_fifo_acqread.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| Number of Elements | Number of Elements specifies the size in elements of the buffer region being acquired. Note NI recommends that Number of Elements be a clean integer divisor of the host FIFO size. You configure the host FIFO size using the FIFO.Configure method. For example, for a host FIFO size of 32,768 elements, and a Number of Elements of 8,192, four calls to the Acquire Read Region method read all of the data in the FIFO. In this example, subsequent calls to the Acquire Read Region method start over at the beginning of the FIFO. However, if Number of Elements is not a clean integer divisor of the host FIFO size, LabVIEW returns a partial region of data from the end of the FIFO. In this case, Elements in Region returns the actual number of elements in the region. |
| Timeout (ms) | Timeout (ms) specifies the minimum number of milliseconds the Invoke Method function waits before timing out. The Invoke Method function times out if the region is available for access but the device has not yet transferred the requested amount of data into the buffer, or if part of the region is not yet available for access. The default is 5000 milliseconds. Set this parameter to –1 if you want the Invoke Method function to wait indefinitely. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |
| Read Region Reference | Read Region Reference returns a reference to the array of elements allocated by the device driver. You must delete this external data value reference before the driver can write new data to the specified portion of the buffer. |
| Elements in Region | Elements in Region returns the total number of elements in the acquired memory region. |
| Elements Remaining | Elements Remaining returns the number of elements in the host memory buffer that are available to read. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/fifo-acquire-write-region-invoke-method.html language=enus -->
## TOPIC 00272: FIFO.Acquire Write Region (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/fifo-acquire-write-region-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/fifo-acquire-write-region-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requests a region to write to the host memory buffer in the target device driver and returns an external data value reference to this region. This method automatically starts the DMA channel if called without a previous call to the Start method. This method is available only if you have specified in

### FIFO.Acquire Write Region (Invoke Method)

Requests a region to write to the host memory buffer in the target device driver and returns an [external data value reference](/csh?productcategories=147794&context=lvcore_lvconcepts_external_data_val_ref) to this region. This method automatically starts the DMA channel if called without a previous call to the Start method.

Note

General FIFO Properties

Type

Host to Target—DMA

Refer to [Improving Efficiency When Accessing DMA FIFOs](/csh?context=lvfpga_lvfpgahelp_fpga_zerocopy_dma) for more information about using this method.

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_fifo_acqwrite.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| Number of Elements | Number of Elements specifies the size in elements of the buffer region being acquired. Note NI recommends that Number of Elements be a clean integer divisor of the host FIFO size. You configure the host FIFO size using the FIFO.Configure method. For example, for a host FIFO size of 32,768 elements, and a Number of Elements of 8,192, four calls to the Acquire Write Region method fills the FIFO buffer. In this example, subsequent calls to the Acquire Write Region method start over at the beginning of the FIFO. However, if Number of Elements is not a clean integer divisor of the host FIFO size, LabVIEW writes to a partial region of data at the end of the FIFO. In this case, Elements in Region returns the actual number of elements in the region. |
| Timeout (ms) | Timeout (ms) specifies the minimum number of milliseconds the Invoke Method function waits before timing out. The Invoke Method function times out if the region is available for access but the requested number of empty elements is not available, or if part of the region is not yet available for access. The default is 5000 milliseconds. Set this parameter to –1 if you want the Invoke Method function to wait indefinitely. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |
| Write Region Reference | Write Region Reference is the reference to the array of elements allocated by the device driver. You must delete this external data value reference before the driver can read new data from the specified portion of the buffer. |
| Elements in Region | Elements in Region returns the total number of elements in the acquired memory region. |
| Empty Elements Remaining | Empty Elements Remaining returns the number of elements in the host memory buffer that are available for writing. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/fifo-configure-invoke-method.html language=enus -->
## TOPIC 00273: FIFO.Configure (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/fifo-configure-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/fifo-configure-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the capacity, or depth, in elements of the host FIFO of the DMA channel. The new depth is implemented when the next FIFO Start, FIFO Read, or FIFO Write method executes. Before the new depth is set, LabVIEW empties all data from the host memory and FPGA FIFO. This method is optional. Use t

### FIFO.Configure (Invoke Method)

Specifies the capacity, or depth, in elements of the host FIFO of the DMA channel. The new depth is implemented when the next FIFO Start, FIFO Read, or FIFO Write method executes. Before the new depth is set, LabVIEW empties all data from the host memory and FPGA FIFO. This method is optional.

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_fifo_config.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| Requested Depth | Requested Depth specifies the number of elements that you request for the host FIFO of the DMA channel. Note On certain FPGA targets, the value wired to this parameter may not be the actual number of elements allocated for the host FIFO of the DMA channel. On these FPGA targets, the number of bytes allocated in memory is coerced to a value that is valid for the specific target and is a multiple of 4096. This coercion may increase the actual number of elements in the host FIFO of the DMA channel. In these cases, use the Actual Depth parameter to determine the number of elements allocated after coercion. Refer to the specific FPGA target hardware documentation for more information about DMA FIFO size limitations. If you do not call the FIFO.Configure method, the default is 10,000 elements or twice the size of the FPGA FIFO buffer, whichever is greater. For NI-RIO 4.0 and later, the default is 16,384 (2^14) elements or twice the size of the FPGA FIFO buffer, whichever is greater. You must pass a nonzero value. If you pass a depth of 0, LabVIEW returns an error. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |
| Actual Depth | Actual Depth returns the number of elements in the host FIFO of the DMA buffer. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/fifo-get-peer-to-peer-reader-invoke-method.html language=enus -->
## TOPIC 00274: FIFO.Get Peer To Peer Reader (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/fifo-get-peer-to-peer-reader-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/fifo-get-peer-to-peer-reader-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a reference to a peer-to-peer reader FIFO on an FPGA target. You must create a reference to a peer-to-peer reader FIFO before you create a peer-to-peer streaming session. Use the Invoke Method function to implement this method. Option Description FPGA VI Reference In FPGA VI Reference In is

### FIFO.Get Peer To Peer Reader (Invoke Method)

Returns a reference to a peer-to-peer reader FIFO on an FPGA target. You must create a reference to a peer-to-peer reader FIFO before you [create a peer-to-peer streaming session](/csh?context=lvfpga_lvfpgahelp_fpga_p2p_create_session).

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_fifo_getp2pread.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |
| Reader | Reader returns a reference to the peer-to-peer reader FIFO on the FPGA target. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/fifo-get-peer-to-peer-writer-invoke-method.html language=enus -->
## TOPIC 00275: FIFO.Get Peer To Peer Writer (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/fifo-get-peer-to-peer-writer-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/fifo-get-peer-to-peer-writer-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a reference to a peer-to-peer writer FIFO on the FPGA target. Use the Invoke Method function to implement this method. Option Description FPGA VI Reference In FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. error in error in

### FIFO.Get Peer To Peer Writer (Invoke Method)

Returns a reference to a peer-to-peer writer FIFO on the FPGA target.

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_fifo_getp2pwrite.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |
| Writer | Writer returns a reference to the peer-to-peer writer FIFO on the FPGA target. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/fifo-read-invoke-method.html language=enus -->
## TOPIC 00276: FIFO.Read (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/fifo-read-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/fifo-read-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads elements of the DMA FIFO from the host memory part of the FIFO. The Read method returns Data when the Number of Elements is available. If the Timeout period ends before the Number of Elements is available, Data is empty. The Read method is available only if the FIFO Type is Target to Host—DMA

### FIFO.Read (Invoke Method)

[Reads elements](/csh?context=lvfpga_lvfpgahosthelp_fpga_reading_dma) of the DMA FIFO from the host memory part of the FIFO. The Read method returns **Data** when the **Number of Elements** is available. If the **Timeout** period ends before the **Number of Elements** is available, **Data** is empty.

Note

Type

Target to Host—DMA

General FIFO Properties

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_fifo_read.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| Number of Elements | Number of Elements determines the number of elements you read from the DMA FIFO. |
| Timeout (ms) | Timeout (ms) specifies the minimum number of milliseconds the Invoke Method function waits before timing out. The Invoke Method function times out if the data is not available for reading by the time the number of milliseconds you specify elapse. The default is 5000 milliseconds. Set this parameter to –1 if you want the Invoke Method function to wait indefinitely. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |
| Data | Data returns the data contained in the host memory part of the DMA FIFO. The number of elements contained in Data is either the same as Number of Elements or zero if the function times out. |
| Elements Remaining | Elements Remaining returns the number of elements remaining that are available for reading.The number of elements that this method returns is less than or equal to the actual number of elements remaining in the FIFO. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/fifo-start-invoke-method.html language=enus -->
## TOPIC 00277: FIFO.Start (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/fifo-start-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/fifo-start-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins DMA data transfer between the FPGA target and the host computer. This method is optional. The FIFO Method Node configured with the Read or Write methods automatically start DMA data transfer. You might want to use this method if you want to start data transfer with the DMA FIFO before you rea

### FIFO.Start (Invoke Method)

Begins DMA data transfer between the FPGA target and the host computer. This method is optional. The FIFO Method Node configured with the **Read** or **Write** methods automatically start DMA data transfer. You might want to use this method if you want to start data transfer with the DMA FIFO before you read the first element of the FIFO.

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_fifo_start.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/fifo-stop-invoke-method.html language=enus -->
## TOPIC 00278: FIFO.Stop (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/fifo-stop-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/fifo-stop-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the DMA data transfer between the FPGA target and the host computer. This method deletes all data from the host memory and FPGA parts of the FIFO. This method is optional. Most applications do not require using the Stop method. Use the Invoke Method function to implement this method. Option De

### FIFO.Stop (Invoke Method)

Stops the DMA data transfer between the FPGA target and the host computer. This method deletes all data from the host memory and FPGA parts of the FIFO. This method is optional. Most applications do not require using the Stop method.

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_fifo_stop.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. If an error occurred before this node runs, the node passes the error in value to error out. If an error occurs while this node runs, the node runs normally and merges error in and its own error status to produce error out. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/fifo-write-invoke-method.html language=enus -->
## TOPIC 00279: FIFO.Write (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/fifo-write-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/fifo-write-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes elements to the DMA FIFO from the host VI. The Write method returns Empty Elements Remaining when the data is written or when the Timeout (ms) period ends. If a timeout occurs while writing to the FIFO, data will be lost. The FIFO accepts new data as soon as space is available in the FIFO. Th

### FIFO.Write (Invoke Method)

[Writes elements](/csh?context=lvfpga_lvfpgahosthelp_fpga_writing_dma) to the DMA FIFO from the host VI. The Write method returns **Empty Elements Remaining** when the data is written or when the **Timeout (ms)** period ends.

If a timeout occurs while writing to the FIFO, data will be lost. The FIFO accepts new data as soon as space is available in the FIFO.

Note

Host to Target—DMA

General FIFO Properties

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_fifo_write.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| Data | Data specifies the data that you want to transfer to the FPGA target. |
| Timeout (ms) | Timeout (ms) specifies the minimum number of milliseconds the Invoke Method function waits before timing out. The Invoke Method function times out if the host part of the FIFO does not contain enough space in which to write Data by the time the number of milliseconds you specify elapse. The default is 5000 milliseconds. Set this parameter to –1 if you want the Invoke Method function to wait indefinitely. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |
| Empty Elements Remaining | Empty Elements Remaining returns the number of empty elements remaining in the host memory part of the DMA FIFO. This number indicates the number of elements that can be written without blocking when performing the next write operation. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/get-fpga-vi-execution-mode-invoke-method.html language=enus -->
## TOPIC 00280: Get FPGA VI Execution Mode (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/get-fpga-vi-execution-mode-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/get-fpga-vi-execution-mode-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the FPGA VI execution mode. Use this method if you want to execute different code depending on the execution mode of the FPGA VI. Use the Invoke Method function to implement this method. Option Description FPGA VI Reference In FPGA VI Reference In is a reference to an FPGA VI. You must open

### Get FPGA VI Execution Mode (Invoke Method)

Returns the FPGA VI execution mode. Use this method if you want to execute different code depending on the execution mode of the FPGA VI.

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_get_execution.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |
| FPGA VI Execution Mode | FPGA VI Execution Mode indicates the execution mode of the FPGA VI. This output can return FPGA Target, Simulation (Simulated I/O), Simulation (Real I/O), or Third-Party Simulation. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/nirvimethod-xnode.html language=enus -->
## TOPIC 00281: Invoke Method

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/nirvimethod-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/nirvimethod-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Invokes an FPGA Interface method or action from a host VI on an FPGA VI. Use methods to do the following: download, abort, reset, and run the FPGA VI on the FPGA target, wait for and acknowledge FPGA VI interrupts, read DMA FIFOs, and write to DMA FIFOs. The methods you can choose from depend on the

### Invoke Method

Invokes an FPGA Interface method or action from a host VI on an FPGA VI. Use methods to do the following: download, abort, reset, and run the FPGA VI on the FPGA target, wait for and acknowledge FPGA VI interrupts, read DMA FIFOs, and write to DMA FIFOs. The methods you can choose from depend on the target hardware and the FPGA VI. You must wire the **FPGA VI Reference In** input to view the available methods in the shortcut menu.

To specify a method, right-click the Invoke Method function and select**Method**»***x*** from the shortcut menu, where ***x*** is the specific method. You must wire the **FPGA VI Reference In** input to view the available methods in the shortcut menu.

Note

running on a development computer

special considerations

[IMAGE alt='icon' src='nirvimethod-xnode.png']

#### Inputs/Outputs

| FPGA VI Reference In — is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA VI Reference Out — returns a reference to an FPGA VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

You can invoke the following FPGA interface methods on most FPGA targets to control the FPGA VI. You might have fewer or more methods available depending on the FPGA target. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about the FPGA interface methods you can use.

- Abort
- Acknowledge IRQ
- Download
- Get FPGA VI Execution Mode
- Reset
- Run
- Wait on IRQ
- *FIFO*–Includes the following methods you can use to read from or write to a FIFO in the FPGA VI. *FIFO* is the name of the FIFO item in the project. Except for the Get Peer To Peer Reader and Get Peer To Peer Writer methods, the following methods are available only for [Direct Memory Access (DMA) FIFOs](/csh?context=lvfpga_lvfpgaconcepts_fpga_dma_communication).
  - Configure
  - Acquire Read Region
  - Read
  - Start
  - Stop
  - Acquire Write Region
  - Write
  - Get Peer To Peer Reader
  - Get Peer To Peer Writer

Parent topic:

FPGA Interface

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/reset-invoke-method.html language=enus -->
## TOPIC 00282: Reset (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/reset-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/reset-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts and resets the FPGA VI on the FPGA target to the default state of the VI. This method sets the FPGA VI controls and indicators to their default states, sets uninitialized shift registers to their default values, clears FIFOs, and sets global variables to their default values. This method does

### Reset (Invoke Method)

Aborts and resets the FPGA VI on the FPGA target to the default state of the VI. This method sets the FPGA VI controls and indicators to their default states, sets uninitialized shift registers to their default values, clears FIFOs, and sets global variables to their default values. This method does not reset memory.

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

Note

implicit enable signals

[IMAGE alt='image' src='fpga_method_reset.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. If an error occurred before this node runs, the node passes the error in value to error out. If an error occurs while this node runs, the node runs normally and merges error in and its own error status to produce error out. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/run-invoke-method.html language=enus -->
## TOPIC 00283: Run (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/run-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/run-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs the FPGA VI on the FPGA target. If the FPGA VI is already running on the FPGA target, the Run method does nothing unless the Wait Until Done input is set to TRUE. Use the Invoke Method function to implement this method. If you enable the removal of implicit enable signals from single-cycle Time

### Run (Invoke Method)

Runs the FPGA VI on the FPGA target. If the FPGA VI is already running on the FPGA target, the Run method does nothing unless the **Wait Until Done** input is set to TRUE.

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

Note

implicit enable signals

[IMAGE alt='image' src='fpga_method_run.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| Wait Until Done (F) | Wait Until Done makes the Invoke Method function wait until the FPGA VI finishes running. If you set this parameter to TRUE, make sure the FPGA VI terminates execution on its own. The default is FALSE. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvimethod/wait-on-irq-invoke-method.html language=enus -->
## TOPIC 00284: Wait on IRQ (Invoke Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvimethod/wait-on-irq-invoke-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvimethod/wait-on-irq-invoke-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for any number of interrupt requests you included in the compiled FPGA VI running on the FPGA target. Always acknowledge interrupts after they occur using the Acknowledge IRQ method. You can use several calls to the Wait on IRQ method to implement waiting on different interrupts from different

### Wait on IRQ (Invoke Method)

Waits for any number of interrupt requests you included in the compiled FPGA VI running on the FPGA target. Always acknowledge interrupts after they occur using the Acknowledge IRQ method. You can use several calls to the Wait on IRQ method to implement waiting on different interrupts from different places in a VI. If you do so, NI recommends that you specify non-overlapping interrupts for different Wait on IRQ method calls.

Note

consumes threads

Execution Properties

Use the [Invoke Method](nirvimethod-xnode.html) function to implement this method.

[IMAGE alt='image' src='fpga_method_wait_irq.gif']

| Option | Description |
| --- | --- |
| FPGA VI Reference In | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| error in | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| IRQ Number(s) | IRQ Number(s) specifies the logical interrupt or array of logical interrupts for which the function waits. The default is 0. Typical supported values are 0 through 31 unless the target documentation specifies otherwise. |
| Timeout (ms) | Timeout (ms) specifies the time, in milliseconds, that the Invoke Method function waits before timing out. The default is 0 milliseconds. Set this parameter to –1 if you want the Invoke Method function to wait indefinitely for the number of elements. |
| FPGA VI Reference Out | FPGA VI Reference Out returns a reference to an FPGA VI. |
| error out | error out contains error information. This output provides standard error out functionality. |
| Timed Out | Timed Out returns TRUE if this method has timed out. |
| IRQs Asserted | IRQ(s) Asserted returns the asserted interrupts. If you are waiting for a single interrupt, a value of –1 indicates that the interrupt was not received. If you are waiting for multiple interrupts, an empty array indicates that no interrupts were received. |

Parent topic:

Invoke Method

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirviopenfpga/nirviopenfpga-xnode.html language=enus -->
## TOPIC 00285: Open FPGA VI Reference

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirviopenfpga/nirviopenfpga-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirviopenfpga/nirviopenfpga-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to the FPGA VI or bitfile and FPGA target you specify. Right-click the Open FPGA VI Reference function and select Configure Open FPGA VI Reference from the shortcut menu to display the Configure Open FPGA VI Reference dialog box. You must open a reference to the FPGA target before

### Open FPGA VI Reference

Opens a reference to the FPGA VI or bitfile and FPGA target you specify. Right-click the Open FPGA VI Reference function and select **Configure Open FPGA VI Reference** from the shortcut menu to display the Configure Open FPGA VI Reference dialog box.



You must open a reference to the FPGA target before you can communicate between the host VI and the FPGA VI. You can download and run only one FPGA VI at a time on a single FPGA target. If you attempt to download a second VI to the FPGA target while the first FPGA VI is still in use, LabVIEW reports an error and the download fails.

Note

interface with an FPGA bitfile even if you do not have the FPGA Module installed

[IMAGE alt='icon' src='nirviopenfpga-xnode.png']

#### Inputs/Outputs

| resource name — specifies the FPGA target on which you want to run the FPGA VI. LabVIEW automatically might determine the FPGA target on which the FPGA VI runs based on the information in the project, depending on the FPGA target. The data type of the resource name input varies by FPGA target. Note You must compile the FPGA VI before the Open FPGA VI Reference function can download or run the VI on the FPGA target. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA VI Reference Out — returns a reference to an FPGA VI. You can bind the FPGA VI Reference Out parameter to type definitions so that LabVIEW automatically propagates configuration changes to subsequent subVIs in the data flow. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Use the Open FPGA VI Reference function to do the following:

| Task | Details |
| --- | --- |
| Select the FPGA VI or bitfile with which the host VI communicates. | To determine the VI that the Open FPGA VI Reference function opens, drag the FPGA VI from the Project Explorer window onto the Open FPGA VI Reference function. You also can right-click the Open FPGA VI Reference function, select Configure Open FPGA VI Reference from the shortcut menu, and specify an FPGA VI or bitfile. Note You cannot open a reference to an FPGA VI if you do not have the LabVIEW FPGA Module installed. However, you can open a reference to a bitfile. If you double-click an Open FPGA VI Reference function that is not yet configured for an FPGA VI, the function displays the Configure Open FPGA VI Reference dialog box. If you double-click an Open FPGA VI Reference function that is configured for an FPGA VI, the function opens the front panel of the FPGA VI. If you want to open references to different FPGA VIs or bitfiles on one target, open only one reference at a time and close the reference before opening another. You can have more than one FPGA VI reference simultaneously open on a target, as long as all the references correspond to the same FPGA VI or bitfile on the same target. |
| Select the open behavior. | By default for some FPGA targets, this function opens and runs the compiled FPGA VI on the FPGA target if the FPGA VI is not already running. To open a reference to the FPGA VI without running it, remove the checkmark from the Run the FPGA VI checkbox in the Configure Open FPGA VI Reference dialog box. You then can run the FPGA VI using the Invoke Method function. Some targets do not allow you to run the FPGA VI when you open it. On some FPGA targets, you can run an FPGA VI automatically when you load the FPGA VI to the FPGA target. You can always run the FPGA VI from the host VI using the Invoke Method function. The Open FPGA VI Reference function is set to use dynamic mode by default. To open a reference that is not dynamic, remove the checkmark from the Dynamic Mode checkbox in the Configure Open FPGA VI Reference dialog box. |
| Determine where the FPGA VI executes. | The text underneath the icon for the Open FPGA VI Reference function indicates the execution mode of the FPGA VI. You can change the execution mode of the FPGA VI by right-clicking the FPGA target and selecting an option from the Select Execution Mode shortcut menu. You also can use the Execution Mode page of the FPGA Target Properties dialog box to specify the execution mode of the FPGA VI. You can use the Open FPGA VI Reference function when the execution mode of the FPGA VI is configured to FPGA target or Simulation (Simulated I/O). If you use this function when the execution mode of the FPGA VI is configured to Simulation (Real I/O), LabVIEW returns a run-time error. |

Place and wire a [Close FPGA VI Reference](../nirviclosefpga/nirviclosefpga-xnode.html) function for every Open FPGA VI Reference function in a host VI. When the Open FPGA VI Reference function first executes on the block diagram, the function checks whether the compiled FPGA VI already exists on the FPGA target. If the compiled FPGA VI is not on the FPGA target, the Open FPGA VI Reference function downloads the compiled FPGA VI to the FPGA target. If you place a checkmark in the **Run the FPGA VI** checkbox in the **Configure Open FPGA VI Reference** dialog box, the FPGA VI starts running if it is not already running.

The Open FPGA VI Reference function does not affect the FPGA VI if the FPGA VI is already downloaded and running. If you want to restart the FPGA VI, you can use the [Invoke Method](../nirvimethod/nirvimethod-xnode.html) function to abort or reset the FPGA VI and use the Invoke Method function to run the FPGA VI again.

Note

Parent topic:

FPGA Interface

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirvireadwritecontrol/nirvireadwritecontrol-xnode.html language=enus -->
## TOPIC 00286: Read/Write Control

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirvireadwritecontrol/nirvireadwritecontrol-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirvireadwritecontrol/nirvireadwritecontrol-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a value from or writes a value to a control or indicator in the FPGA VI on the FPGA target. icon Inputs/Outputs cgenclassrn.png FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. cerrcodeclst.png error in error in describes error

### Read/Write Control

Reads a value from or writes a value to a control or indicator in the FPGA VI on the FPGA target.

[IMAGE alt='icon' src='nirvireadwritecontrol-xnode.png']

#### Inputs/Outputs

| FPGA VI Reference In — is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA VI Reference Out — returns a reference to an FPGA VI. error out — error out contains error information. This output provides standard error out functionality. Unselected — |
| --- |

A host VI can control and monitor data passed through the FPGA VI front panel. You cannot access values on any wires on the FPGA VI block diagram that do not have controls or indicators unless the data is stored in a [DMA FIFO](/csh?context=lvfpga_lvfpgahosthelp_fpga_reading_dma).

First [open a reference to the FPGA target](/csh?context=lvfpga_lvfpgahosthelp_fpga_opening_vi_reference). Then wire the **FPGA VI Reference Out** output of the [Open FPGA VI Reference](../nirviopenfpga/nirviopenfpga-xnode.html) function or the **Bitfile reference out** output of the [Open Dynamic Bitfile Reference](../../../../functions/open-dynamic-bitfile-reference.html) function to the Read/Write Control function to access controls and indicators on the FPGA VI. You can [read indicators](/csh?context=lvfpga_lvfpgahosthelp_reading_fpga_vi_controls) and [write controls](/csh?context=lvfpga_lvfpgahosthelp_writing_to_fpga_vi_controls). You also can write indicators and read controls. You can expand the Read/Write Control function to read or write multiple controls and indicators. When you run the host VI, the Read/Write Control function reads and writes controls and indicators in the order they appear in the Read/Write Control function on the block diagram.

Tip

The FPGA Module creates a register map, specific to the FPGA VI, that includes a hardware register for every control and indicator. LabVIEW uses the register map internally to communicate with the FPGA VI directly with [interactive front panel communication](/csh?context=lvfpga_lvfpgaconcepts_ifp_comm) and using the host VI with [programmatic FPGA interface communication](/csh?context=lvfpga_lvfpgaconcepts_pfi_comm).

Parent topic:

FPGA Interface

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interface/nirviupcast/nirviupcast-xnode.html language=enus -->
## TOPIC 00287: Up Cast

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interface/nirviupcast/nirviupcast-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interface/nirviupcast/nirviupcast-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an FPGA VI-specific reference to a more generic reference. You then can use common code to interact with different FPGA VIs. The FPGA targets must be of the same class. You may want to use this function if you want to evaluate different algorithms in a host VI without rewriting the host VI.

### Up Cast

Converts an FPGA VI-specific reference to a more generic reference. You then can use common code to interact with different FPGA VIs. The FPGA targets must be of the same class. You may want to use this function if you want to evaluate different algorithms in a host VI without rewriting the host VI. Some FPGA targets might not support this function.

[IMAGE alt='icon' src='nirviupcast-xnode.png']

#### Inputs/Outputs

| FPGA VI Reference In — is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA VI Reference Out — returns a reference to the FPGA target. If you select Interface from the shortcut menu, FPGA VI Reference Out also returns information about the VI, including controls, indicators, data types, and the connector pane, but not including the VI filename. You can bind the FPGA VI Reference Out parameter to type definitions so that LabVIEW automatically propagates configuration changes to subsequent subVIs in the data flow. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Right-click the Up Cast function and select **Interface** from the shortcut menu to output VI information and target information. Use the **Interface** option to pass data to the [Read/Write Control](../nirvireadwritecontrol/nirvireadwritecontrol-xnode.html) function or [Invoke Method](../nirvimethod/nirvimethod-xnode.html) function. If you select the **Interface** option, the FPGA VIs and targets must meet the following requirements: the front panel windows of the FPGA VIs are the same, the control and indicator [tab order](/csh?productcategories=147794&context=lvcore_lvhowto_changingtheorderoffpanelob) matches, and you use only one clock domain on the FPGA VI block diagram.

Right-click the Up Cast function and select **Target** from the shortcut menu to output only target information. Use the **Target** option to pass data to the Invoke Method function. The default is **Target**.

Note

subVIs

Bind Reference Output to Type Definition

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/interrupt/nifpga-interrupt-vi.html language=enus -->
## TOPIC 00288: Interrupt

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/interrupt/nifpga-interrupt-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/interrupt/nifpga-interrupt-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asserts an interrupt on the interrupt line of the FPGA target. The Interrupt VI communicates to the host VI that a specific logical interrupt has occurred. The Interrupt VI is a shared resource, so multiple uses of it induce additional delay and jitter due to arbitration. To handle the interrupts in

### Interrupt

Asserts an interrupt on the interrupt line of the FPGA target.

The Interrupt VI communicates to the host VI that a specific logical interrupt has occurred. The Interrupt VI is a shared resource, so multiple uses of it induce additional delay and jitter due to arbitration. To handle the interrupts in the host VI, use the Wait on IRQ and Acknowledge IRQ methods in the [Invoke Method](../interface/nirvimethod/nirvimethod-xnode.html) function.

[IMAGE alt='icon' src='nifpga-interrupt-vi.png']

#### Inputs/Outputs

| Wait Until Cleared (F) — Wait Until Cleared specifies if this VI waits until the host VI acknowledges the logical interrupt or this VI asserts the interrupt and continues. Set this parameter to TRUE if you want the VI to wait until the host VI acknowledges it. Set this parameter to FALSE if you do not want the VI to wait. The default is FALSE. IRQ Number (0) — IRQ Number specifies which logical interrupt to assert. The default is 0. Typical supported values are 0 through 31 unless the target documentation specifies otherwise. Note To find out the supported IRQ number of a specific FPGA target, right-click the FPGA target in the Project Explorer window and select Properties from the shortcut menu. The Target Information component of the General page displays the supported IRQ number. |
| --- |

Parent topic:

Synchronization

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/ipintegrationnode/clock-and-enable-signals-page-ip-integration-node.html language=enus -->
## TOPIC 00289: Clock and Enable Signals Page (IP Integration Node)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/ipintegrationnode/clock-and-enable-signals-page-ip-integration-node.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/ipintegrationnode/clock-and-enable-signals-page-ip-integration-node.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page to specify the ports in the IP that behave as a clock or enable signal. Access this page by double-clicking the IP Integration Node and using the configuration wizard that appears. If the node is configured already, you can right-click the node and select Configure»Clock and Enable Sig

### Clock and Enable Signals Page (IP Integration Node)

Use this page to specify the ports in the IP that behave as a clock or enable signal.

Access this page by double-clicking the [IP Integration Node](ipinode-xnode/nifpgaipinode-xnode.html) and using the configuration wizard that appears. If the node is configured already, you can right-click the node and select **Configure»Clock and Enable Signals** from the shortcut menu.

This page includes the following components:

| Option | Description |
| --- | --- |
| IP Clock Signal | Contains options relating to the clock signal(s) of the IP. Clock signal name—Specifies the port in the IP that corresponds to the single-cycle Timed Loop clock. If the IP does not contain this port, select No Clock from this pull-down list. In this situation, LabVIEW assumes the IP is combinatorial, that is, does not store its state at any time. You also cannot select a Derived multiple of single-cycle Timed Loop clock. Derived multiple of single-cycle Timed Loop clock—Specifies the port in the IP that corresponds to the derived clock enable signal. If the IP does not use a derived clock signal, select No Derived Clock from this pull-down list. Use this pull-down list and the Relative clock rate control to execute IP faster than the containing single-cycle Timed Loop. Relative clock rate—Specifies the rate multiple of the Derived multiple of single-cycle Timed Loop clock relative to the Clock signal name. Relative clock rate must be an integer. LabVIEW disregards this option if you set Derived multiple of single-cycle Timed Loop clock to No Derived Clock. For example, if the clock you specify in the Clock signal name pull-down list executes at 100 MHz and the clock you specify in the Derived multiple of single-cycle Timed Loop clock pull-down list executes at 400 MHz, set Relative clock rate to 4x. Note If the IP requires a derived clock rate that is not an integer multiple of the single-cycle Timed Loop clock, use CLIP to integrate the IP into the FPGA VI. |
| IP Enable Signal(s) | Specifies the IP port(s) LabVIEW uses to enable the IP. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/ipintegrationnode/entity-architecture-and-targets-page-ip-integration-node.html language=enus -->
## TOPIC 00290: Entity, Architecture, and Targets Page (IP Integration Node)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/ipintegrationnode/entity-architecture-and-targets-page-ip-integration-node.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/ipintegrationnode/entity-architecture-and-targets-page-ip-integration-node.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page to define the top-level entity and architecture you want the IP Integration Node to synthesize and simulate. You also use this page to specify the FPGA families on which this node can compile. Access this page by double-clicking the IP Integration Node and using the configuration wizar

### Entity, Architecture, and Targets Page (IP Integration Node)

Use this page to define the top-level entity and architecture you want the [IP Integration Node](ipinode-xnode/nifpgaipinode-xnode.html) to synthesize and simulate. You also use this page to specify the FPGA families on which this node can compile.

Access this page by double-clicking the [IP Integration Node](ipinode-xnode/nifpgaipinode-xnode.html) and using the configuration wizard that appears. If the node is configured already, you can right-click the node and select **Configure»Entity, Architecture, and Targets** from the shortcut menu.

This page includes the following components:

| Option | Description |
| --- | --- |
| Top-Level Entity and Architecture | Specifies the entity/architecture pairs you want to use for IP synthesis and simulation. This table is available only if the top-level synthesis file is a .vhd file. If this file is a Xilinx IP configuration file or a netlist file, LabVIEW dims this section. Synthesis Module—Specifies the top-level entity/architecture pair to use for IP synthesis. syn entity—Specifies the top-level entity to use for IP synthesis. syn arc—Specifies the top-level architecture to use for IP synthesis. Simulation Model—Specifies the top-level entity/architecture pair to use for IP simulation. This section is available only if you selected the User-defined option in the Set Simulation Behavior dialog box for the top-level synthesis file. sim entity—Specifies the top-level entity to use for IP simulation. sim arc—Specifies the top-level architecture to use for IP simulation. |
| FPGA Family Support | Specifies the families of FPGAs on which this Node can execute. Refer to the FPGA Target Properties dialog box for information about the FPGA family to which a particular FPGA belongs. unlimited—Specifies that this IP can run on all FPGA families, including but not limited to the ones listed on this page. Select this option if the IP does not contain any family-specific code and the IP does not contain any Xilinx compilation tool-specific file types. limited—Specifies that this IP can run only on FPGAs that belong to the families you specify. If you try to compile this VI on an FPGA that belongs to an unsupported family, LabVIEW returns an error. Select this option if the IP contains code that can execute only on a particular FPGA family. all supportedl targets—Specifies the FPGA families on which you can execute the IP. If you select the Unlimited option, LabVIEW dims this list. Otherwise, you must place checkmarks in the checkboxes for the families you want the IP to support. |
| Feedback | Displays warnings, errors, and configuration information. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/ipintegrationnode/generics-and-support-file-generation-page-ip-integration-node.html language=enus -->
## TOPIC 00291: Generics and Support File Generation Page (IP Integration Node)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/ipintegrationnode/generics-and-support-file-generation-page-ip-integration-node.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/ipintegrationnode/generics-and-support-file-generation-page-ip-integration-node.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page to view and change information about generics in the IP. You also use this page to generate the files that are necessary for simulating the IP, including the simulation DLL. Access this page by double-clicking the IP Integration Node and using the configuration wizard that appears. If

### Generics and Support File Generation Page (IP Integration Node)

Use this page to view and change information about generics in the IP. You also use this page to [generate](/csh?context=lvfpga_lvfpgahelp_ipin_gen_sim) the files that are necessary for simulating the IP, including the simulation DLL.

Access this page by double-clicking the [IP Integration Node](ipinode-xnode/nifpgaipinode-xnode.html) and using the configuration wizard that appears. If the node is configured already, you can right-click the node and select **Configure»Generics and Support File Generation Model** from the shortcut menu.

This page includes the following components:

| Option | Description |
| --- | --- |
| Generics | Displays information about generics that correspond to the entity and architecture you specified on the previous page of the configuration wizard. This table is available only if the top-level synthesis file is a .vhd file. If this file is a Xilinx IP configuration file or a netlist file, LabVIEW dims this table. Value—Specifies a new value for the selected generic. Check syntax—Checks the syntax of a value you enter in the Value control. |
| Generate Support Files | Specifies options that relate to generating the support files. Note Even if you do not plan to export the FPGA VI for simulation, you must generate support files before you can continue configuring and using the IP Integration Node. skip up-to-date—Specifies whether LabVIEW updates only support files that have changed since the last update. Placing a checkmark in this checkbox can save a significant amount of regeneration time. Removing the checkmark from this checkbox increases regeneration time but can fix errors in the generated files. Generate—Generates files necessary for simulating the IP, including the simulation DLL. The amount of time required to generate these files depends on the types of synthesis files and the complexity of the IP. Progress—Displays the progress of the simulation file generation. |
| Feedback | Displays warnings, errors, and configuration information. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/ipintegrationnode/ip-terminals-page-ip-integration-node.html language=enus -->
## TOPIC 00292: IP Terminals Page (IP Integration Node)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/ipintegrationnode/ip-terminals-page-ip-integration-node.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/ipintegrationnode/ip-terminals-page-ip-integration-node.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page to specify the names and data types of block diagram terminals that correspond to VHDL ports in the IP. Access this page by double-clicking the IP Integration Node and using the configuration wizard that appears. If the node is configured already, you can right-click the node and selec

### IP Terminals Page (IP Integration Node)

Use this page to specify the names and data types of block diagram terminals that correspond to VHDL ports in the IP.

Access this page by double-clicking the [IP Integration Node](ipinode-xnode/nifpgaipinode-xnode.html) and using the configuration wizard that appears. If the node is configured already, you can right-click the node and select **Configure»IP Terminals** from the shortcut menu.

Note

Finish

This page includes the following components:

| Option | Description |
| --- | --- |
| Terminals | Displays IP ports and how LabVIEW interprets these ports. Each port becomes an input or output terminal on the IP Integration Node. To configure these terminals, select a terminal in this table and then use the buttons in the other sections of this page. Note Neither the clock signal nor the asynchronous reset signal appear in this list of terminals. The IP Integration Node assumes all ports are synchronized to the rising edge of the single-cycle Timed Loop clock. |
| Terminal Order | Contains the buttons you use to control the order of the terminals. Move Up—Moves the selected terminal higher in the list. Move Down—Moves the selected terminal lower in the list. |
| Terminal Properties | Contains settings for the selected terminal. Data type—Specifies the data type of this terminal. Click this button to specify a data type. The valid data types are integer, fixed-point, single-precision floating-point, Boolean, and Boolean array. Fixed-point encoding—Specifies the fixed-point configuration of the terminal. This section applies only if you select Fixed-point as the Data type. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Integer word length—Specifies the integer word length of the selected terminal between [–2048, 2047]. This option is valid for fixed-point terminals only. LabVIEW sets the word length of the terminal to the width of the corresponding port as specified in the IP. Hide?—Specifies whether LabVIEW hides the selected terminal. If this terminal is an input, LabVIEW sets the value of the terminal to the Default value you specify. Default value (Hex)—Specifies the value, in hexadecimal, of a hidden terminal. This component is available only if the Direction of the selected terminal is IN and you place a checkmark in the Hide this terminal checkbox. |
| Feedback | Displays warnings, errors, and configuration information. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/ipintegrationnode/ipinode-xnode/nifpgaipinode-xnode.html language=enus -->
## TOPIC 00293: IP Integration Node

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/ipintegrationnode/ipinode-xnode/nifpgaipinode-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/ipintegrationnode/ipinode-xnode/nifpgaipinode-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Integrates third-party IP into a LabVIEW FPGA VI. Before you add this node to a block diagram, ensure the necessary Xilinx compilation tools are installed on the development computer. You can place this node only inside a single-cycle Timed Loop. After you add this node to the block diagram, double-

### IP Integration Node

Integrates third-party IP into a LabVIEW FPGA VI. Before you add this node to a block diagram, ensure the necessary Xilinx compilation tools are installed on the development computer. You can place this node only inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

After you add this node to the block diagram, double-click this node to [configure it](/csh?context=lvfpga_lvfpgaconcepts_ipin_use).

[IMAGE alt='icon' src='nifpgaipinode-xnode.png']

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/ipintegrationnode/name-and-source-page-ip-integration-node.html language=enus -->
## TOPIC 00294: Name and Source Page (IP Integration Node)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/ipintegrationnode/name-and-source-page-ip-integration-node.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/ipintegrationnode/name-and-source-page-ip-integration-node.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page to define the name of the IP Integration Node and the synthesis and simulation files the node uses. Access this page by double-clicking the IP Integration Node. If the node is configured already, you can right-click the node and select Configure»Name and Source from the shortcut menu.

### Name and Source Page (IP Integration Node)

Use this page to define the name of the IP Integration Node and the [synthesis and simulation files](/csh?context=lvfpga_lvfpgaconcepts_ipin_sim) the node uses.

Access this page by double-clicking the [IP Integration Node](ipinode-xnode/nifpgaipinode-xnode.html). If the node is configured already, you can right-click the node and select **Configure»Name and Source** from the shortcut menu.

This page includes the following components:

| Option | Description |
| --- | --- |
| IP Name | Specifies the name of the IP. This name appears on the icon of the IP Integration Node. Note Do not use the same IP Name for more than one IP Integration Node. If you do use the same name for more than one IP Integration Node and generate a simulation model, LabVIEW displays a warning to prevent you from overwriting the simulation files of another node. |
| Source | Displays the synthesis files that compose the IP and the simulation behavior that corresponds to each synthesis file. Use the following buttons to manage the items in this table: Add Syn File—Prompts you for a synthesis file to add to the IP Source table. Def Sim Model—Launches the Set Simulation Behavior dialog box, which you use to change the simulation behavior of the selected synthesis file or exclude this file from simulation. Set Top—Sets the selected synthesis file as the top-level file. Remove—Removes the selected synthesis file from the IP Source table. |
| Feedback | Displays warnings, errors, and configuration information. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/ipintegrationnode/regenerate-ip-integration-node-support-files.html language=enus -->
## TOPIC 00295: Regenerate IP Integration Node Support Files

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/ipintegrationnode/regenerate-ip-integration-node-support-files.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/ipintegrationnode/regenerate-ip-integration-node-support-files.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this dialog box to regenerate support files for IP Integration Nodes in a VI hierarchy. Regenerate support files to ensure your design compiles with a specific FPGA target, especially when you upgrade LabVIEW versions, upgrade your FPGA target, or upgrade the Xilinx compilation tools. Refer to t

### Regenerate IP Integration Node Support Files

Use this dialog box to regenerate support files for IP Integration Nodes in a VI hierarchy.

Regenerate support files to ensure your design compiles with a specific FPGA target, especially when you upgrade LabVIEW versions, upgrade your FPGA target, or upgrade the Xilinx compilation tools. Refer to the [support document](https://www.ni.com/r/XilinxCompileTools) at ni.com for more information about NI hardware supported by each Xilinx compilation tool.

Select **Tools»FPGA Module»Regenerate IP Integration Node Support Files** to display this dialog box.

| Option | Description |
| --- | --- |
| Top-level VI path | Specifies a top-level VI whose hierarchy this dialog box scans for IP Integration Nodes. |
| IP Integration Nodes | Displays all IP Integration Nodes in the hierarchy of the top-level VI and whether LabVIEW updated, skipped, or failed to update each node. The status available varies depending on your specific FPGA target. |
| skip | Specifies whether LabVIEW updates only support files that have changed since the last update. Placing a checkmark in this checkbox can save a significant amount of regeneration time. Removing the checkmark from this checkbox increases regeneration time but can fix errors in the generated files. |

Note

#### Support Files

Complete either of the following tasks to restore missing support files.

- If you moved the IP Integration Node from another computer or from another location on disk, locate the support files in the original location or place them in the same location relative to the current location of the IP Integration Node.
- Return to the first page of the wizard, remove all files, and start again.

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/ipintegrationnode/reset-signals-and-behavior-page-ip-integration-node.html language=enus -->
## TOPIC 00296: Reset Signals and Behavior Page (IP Integration Node)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/ipintegrationnode/reset-signals-and-behavior-page-ip-integration-node.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/ipintegrationnode/reset-signals-and-behavior-page-ip-integration-node.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page to specify the ports in sequential IP that behave as asynchronous or synchronous reset signals. Access this page by double-clicking the IP Integration Node and using the configuration wizard that appears. If the node is configured already, you can right-click the node and select Config

### Reset Signals and Behavior Page (IP Integration Node)

Use this page to specify the ports in [sequential IP](/csh?context=lvfpga_lvfpgaconcepts_ipin_prepare_ip) that behave as asynchronous or synchronous reset signals.

Access this page by double-clicking the [IP Integration Node](ipinode-xnode/nifpgaipinode-xnode.html) and using the configuration wizard that appears. If the node is configured already, you can right-click the node and select **Configure»Reset Signals and Behavior** from the shortcut menu.

This page includes the following components:

| Option | Description |
| --- | --- |
| Reset Signals | Contains options that relate to reset signals. Synchronous reset signal(s)—Specifies the port(s) in the IP that behave as synchronous reset signals. Asynchronous reset signal—Specifies the port in the IP that behaves as an asynchronous reset signal. If the IP does not contain this port, select No Asynchronous Reset from this pull-down list. —Active logic level—Specifies the active logic level of the asynchronous reset signal. This option is available only when you specify an asynchronous reset signal for the IP. High—Specifies that the active logic level is high. Low—Specifies that the active logic level is low. sclr cycles—Specifies the number of clock cycles for which LabVIEW asserts the Synchronous reset signal(s) during a reset. If the IP has multiple synchronous reset signals that need different durations, enter the longest duration here. sclr cycles—Specifies the number of clock cycles for which LabVIEW asserts the Asynchronous reset signal during a reset. The clock is running within the reset duration. The value must be 0 for this IP to be used when the build specification is configured to allow the removal of implicit enable signals because the Asynchronous reset signal will assert and deassert before the clock starts running. The value must also be 0 if this clock is used with external clocks that might stop during reset. If an IP requires a running clock during asynchronous reset, such as for IP that use built-in FIFOs, and the design requires the removal of implicit enable signals, consider creating a local asynchronous reset, and prevent diagram access to or from the IP while this local reset is asserted. |
| Reset IP | Specifies the situation(s) in which LabVIEW resets the IP Integration Node. Before first call—Specifies that LabVIEW resets the IP Integration Node before the first call to the FPGA VI. Compile or load—Specifies that LabVIEW resets the IP only when the FPGA VI compiles or downloads to the FPGA. If you choose this option and the IP does not support asynchronous resets, the IP does not reset even if you invoke the Reset method. When the IP does reset, it might operate on garbage data, including metastable values. To mitigate these issues, ensure that your application does not depend on the values this IP returns immediately after resetting. |
| Feedback | Displays warnings, errors, and configuration information. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/ipintegrationnode/set-simulation-behavior-dialog-box-ip-integration-node.html language=enus -->
## TOPIC 00297: Set Simulation Behavior Dialog Box (IP Integration Node)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/ipintegrationnode/set-simulation-behavior-dialog-box-ip-integration-node.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/ipintegrationnode/set-simulation-behavior-dialog-box-ip-integration-node.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this dialog box to set the simulation behavior for synthesis files in the IP Integration Node. Access this dialog box by double-clicking the IP Integration Node, selecting one or more synthesis files in the IP Source table, and clicking the Set Simulation Behavior button. This dialog box include

### Set Simulation Behavior Dialog Box (IP Integration Node)

Use this dialog box to set the simulation behavior for synthesis files in the [IP Integration Node](ipinode-xnode/nifpgaipinode-xnode.html).

Access this dialog box by double-clicking the IP Integration Node, selecting one or more synthesis files in the **IP Source** table, and clicking the **Set Simulation Behavior** button.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| User-defined | Specifies that you will define one or more files, such as .vhd or .mif files, as the simulation model. NI recommends selecting this option for netlist synthesis files. The third-party tool that generates the netlist file also generates the files that define the simulation model. Ensure the code follows the guidelines for top-level synthesis and simulation files. Use the buttons to the right of this list in the following ways: Add File—Prompts you to add a file to the list. Remove File—Prompts you to remove a file from the list. Select the file and then click the Remove File button. Set as Top—Prompts you to set a file as the top-level simulation file. Select a file and then click the Set as Top button. This button is available only if you are setting simulation behavior for the top-level synthesis file as displayed on the Name and Source page. You can set only .vhd files as the top-level simulation file. |
| Post-synthesis model | Specifies that LabVIEW uses the netlist file to generate a .vhd simulation model. Select this option if you do not have the .vhd file that corresponds to the netlist synthesis file. Selecting this option greatly increases the simulation run time for netlist synthesis files. NI recommends selecting the User-defined option for netlist synthesis files. |
| Same as synthesis | Specifies that LabVIEW uses the synthesis file itself for simulation. If the synthesis file is a Xilinx IP configuration file, LabVIEW uses the .vhd simulation model that the Xilinx IP generator provides. This option is available only if the synthesis file is a Xilinx IP configuration file or a .vhd file. |
| Exclude from simulation model | Specifies that LabVIEW does not export this file for simulation. Select this option if you do not need to simulate the synthesis file or if another simulation model already includes the simulation model of a synthesis file. You cannot select this option for a top-level synthesis file. |

#### Batch Setting Simulation Behaviors

If you select multiple synthesis files before launching this dialog box, LabVIEW dims certain behaviors according to the following rules:

- LabVIEW always dims the User-defined behavior.
- LabVIEW enables the Post-synthesis model behavior only if all the files you selected are netlist files
- LabVIEW dims the Same as synthesis behavior if you selected at least one netlist file
- LabVIEW dims the Exclude from simulation model behavior if you selected the top-level synthesis file

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/linearalgebra/dotproduct/xnode/nifxpla-dotproduct-xnode.html language=enus -->
## TOPIC 00298: Dot Product

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/linearalgebra/dotproduct/xnode/nifxpla-dotproduct-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/linearalgebra/dotproduct/xnode/nifxpla-dotproduct-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the dot product of two complex vectors. This function accepts frames of data, performs computations on the input data, and returns a valid single result for each frame. This function supports only scalar and 1D fixed-size array values of the fixed-point data type. icon Dialog Box Options Pa

### Dot Product

Computes the dot product of two complex vectors.

This function supports only scalar and [1D fixed-size array](/csh?context=lvfpga_lvfpgahelp_creating_fixedsize_arrays) values of the [fixed-point](/csh?context=lvfpga_lvfpgahelp_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpla-dotproduct-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Input Vector Configuration | Specifies the encodings, word lengths, and integer word lengths of the input terminals of this function. xr/xi Type—Specifies the configuration of the real or imaginary xr/xi input terminals. If you wire a fixed-point data type to these terminals, LabVIEW dims this section and uses information from the wire. The xr/xi inputs of this function must be of the same data type and input pattern, otherwise the data type or array size of the xr input terminal takes precedent. Signed—Specifies that these terminals are signed. Unsigned—Specifies that these terminals are unsigned. Word length—Specifies the word length of these terminals. Integer word length—Specifies the integer word length of these terminals. yr/yi Type—Specifies the configuration of the real or imaginary yr/yi input terminals. If you wire a fixed-point data type to these terminals, LabVIEW dims this section and uses information from the wire. The yr/yi inputs of this function must be of the same data type and input pattern, otherwise the data type or array size of the yr input terminal takes precedent. Signed—Specifies that these terminals are signed. Unsigned—Specifies that these terminals are unsigned. Word length—Specifies the word length of these terminals. Integer word length—Specifies the integer word length of these terminals. Vector size—Specifies the size of the input vector. |
| Operation | Specifies whether to conjugate the inputs during operation and specifies the encodings, word lengths, and integer word lengths of the output terminals of this function. Conjugate X—Specifies whether to conjugate the inputs of vector X during operation. Selecting this option does not require additional FPGA resources. LabVIEW displays an icon on the block diagram based on the conjugation option you choose. By default, this checkbox does not contain a checkmark. Conjugate Y—Specifies whether to conjugate the inputs of vector Y during operation Selecting this option does not require additional FPGA resources. LabVIEW displays an icon on the block diagram based on the conjugation option you choose. By default, this checkbox does not contain a checkmark. pr/pi Type—Specifies the configuration of the real or imaginary pr/pi output terminals. Adapt to source—Specifies whether LabVIEW automatically adjusts the fixed-point configuration of the output data type to avoid overflow and rounding errors. By default, this checkbox contains a checkmark, and LabVIEW dims the following options. Note LabVIEW supports a maximum word length of 64 bits and a maximum integer word length of 1023 bits. If you place a checkmark in this checkbox and the output data type requires a word length that exceeds these maximum values, overflow and/or rounding errors might occur. Signed—Specifies that these terminals are signed. Unsigned—Specifies that these terminals are unsigned. Word length—Specifies the word length of these terminals. Integer word length—Specifies the integer word length of these terminals. Overflow mode—Specifies how this function handles overflow. You can choose either Wrap (default) or Saturate. Note The Saturate option requires more FPGA resources and a longer combinatorial path than the Wrap option does. In this situation, choosing Saturate might decrease the maximum clock rate at which this function can compile. Rounding mode—Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. |
| Implementation Details | Specifies options for implementation resources and for pipelining this function internally. These options affect the maximum clock rate at which this function can compile and may exceed available FPGA resources. Resource—Specifies how to implement the multiplier. You can choose from the following options: Auto (default)—Specifies that the compiler decides whether to use embedded block multipliers or look-up tables (LUTs) to implement the multiplier. Look-Up Table—Specifies that this function uses LUTs to implement the multiplier. Number of pipelining stages—Specifies how many pipelining stages this function uses internally. Increasing the number of stages increases the clock rate at which this function can compile but also increases the latency and the amount of FPGA resources this function requires. The degree of pipelining changes with word length and vector size. The default is Max. Min specifies a minimal number of pipelining stages. |

#### Inputs/Outputs

| xr — Specifies the real part of the x multiplicand. xi — Specifies the imaginary part of the x multiplicand. yr — Specifies the real part of the y multiplicand. yi — Specifies the imaginary part of the y multiplicand. input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node. ready for output (T) — Specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire the ready for input output of a downstream node to this input of the current node. Note If this terminal is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. pr — Returns the real part of the dot product. pi — Returns the imaginary part of the dot product. operation overflow — Returns TRUE if the theoretical computed value exceeds the valid range of the output data type. If operation overflow returns TRUE, the Overflow mode you specify in the configuration dialog box determines the value this function returns. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. After returning TRUE for the previous output frame, this indicator returns FALSE, waiting for the next frame to complete. Wire this output to the input valid input of a downstream node to transfer data from the node to the downstream node. ready for input — Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the input valid terminal is TRUE during the following cycle. |
| --- |

The real and imaginary inputs of this function must be of the same data type and input pattern, otherwise the data type or array size of the **real data in** input terminal takes precedent.

The inputs of **xr/xi** and **yr/yi** must be both scalar or both 1D fixed-size array. If the interface type of **xr/xi** and **yr/yi** differs, the input of **xr/xi** takes precedent. If both interface types are 1D fixed-size arrays, but the array sizes differ, the input with the smaller array size takes precedent regardless of whether it is **xr/xi** or **yr/yi**. If the dominating wire is a 1D fixed-size array, LabVIEW dims **Vector size** and uses the array size from the wire.

#### Improving Function Performance by Pipelining

You can improve the timing performance of this function on an FPGA target by adjusting the **Number of pipelining stages**.

In general, increasing the **Number of pipelining stages** also increases the maximum clock rate at which this function can compile. However, the actual clock rate depends on many factors, including the following:

- The FPGA target you use
- The size of the multiplier
- The rounding and overflow modes you select
- The Resource you select
- Other FPGA logic besides the multiplier

#### Handshaking

Refer to the [Scheduling Timing Using Handshaking Signals](/csh?context=lvfpga_lvfpgaconcepts_fpga_handshaking) topic for more information about handshaking.

Parent topic:

Linear Algebra

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/linearalgebra/matrixmultiply/xnode/nifxpla-matrixmultiply-xnode.html language=enus -->
## TOPIC 00299: Matrix Multiply

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/linearalgebra/matrixmultiply/xnode/nifxpla-matrixmultiply-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/linearalgebra/matrixmultiply/xnode/nifxpla-matrixmultiply-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the multiplication of two complex matrices. This function supports only scalar and 1D fixed-size array values of the fixed-point data type. icon Dialog Box Options Parameter Description Input Types Specifies the encodings, word lengths, and integer word lengths of the input terminals of thi

### Matrix Multiply

Computes the multiplication of two complex matrices.

This function supports only scalar and [1D fixed-size array](/csh?context=lvfpga_lvfpgahelp_creating_fixedsize_arrays) values of the [fixed-point](/csh?context=lvfpga_lvfpgahelp_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpla-matrixmultiply-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Input Types | Specifies the encodings, word lengths, and integer word lengths of the input terminals of this function. ar/ai Type—Specifies the real or imaginary fixed-point configuration of the ar/ai input terminals. If you wire a fixed-point data type to these terminals, LabVIEW dims this section and uses information from the wire. Signed—Specifies that these terminals are signed. Unsigned—Specifies that these terminals are unsigned. Word length—Specifies the word length of these terminals. Integer word length—Specifies the integer word length of these terminals. br/bi Type—Specifies the real or imaginary fixed-point configuration of the br/bi input terminals. If you wire a fixed-point data type to these terminals, LabVIEW dims this section and uses information from the wire. Signed—Specifies that these terminals are signed. Unsigned—Specifies that these terminals are unsigned. Word length—Specifies the word length of these terminals. Integer word length—Specifies the integer word length of these terminals. |
| Operation | Specifies whether to conjugate the inputs during operation and specifies the encodings, word lengths, and integer word lengths of the output terminals of this function. Conjugate A—Specifies whether to conjugate the inputs of matrix A during operation. Selecting this option does not require additional FPGA resources. LabVIEW displays an icon on the block diagram based on the conjugation option you choose. By default, this checkbox does not contain a checkmark. Conjugate B—Specifies whether to conjugate the inputs of matrix B during operation. Selecting this option does not require additional FPGA resources. LabVIEW displays an icon on the block diagram based on the conjugation option you choose. By default, this checkbox does not contain a checkmark cr/ci Type—Specifies the fixed-point configuration of the real or imaginary cr/ci output terminals. Adapt to source—Specifies whether LabVIEW automatically adjusts the fixed-point configuration of the output data type to avoid overflow and rounding errors. By default, this checkbox contains a checkmark, and LabVIEW dims the following options. Note LabVIEW supports a maximum word length of 64 bits and a maximum integer word length of 1023 bits. If you place a checkmark in this checkbox and the output data type requires a word length that exceeds these maximum values, overflow and/or rounding errors might occur. Signed—Specifies that these terminals are signed. Unsigned—Specifies that these terminals are unsigned. Word length—Specifies the word length of these terminals. Integer word length—Specifies the integer word length of these terminals. Overflow mode—Specifies how this function handles overflow. You can choose either Wrap (default) or Saturate. Note The Saturate option requires more FPGA resources and a longer combinatorial path than the Wrap option does. In this situation, choosing Saturate might decrease the maximum clock rate at which this function can compile. Rounding mode—Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. |
| Matrix Size | Specifies the dimensions of a given matrix. M—Specifies the row number of inputs for matrix A. L—Specifies the column number of inputs for matrix A and the row number of inputs for matrix B. N—Specifies the column number of inputs for matrix B. |
| Interface | Specifies the input and output pattern of matrix A and matrix B and the throughput of the function. Input pattern of A—Specifies that the function receives data from matrix A element by element in the matrix, by vector, by row-wise, or by column-wise. Matrix A and matrix B must both use the same input pattern. If you choose an element input pattern for the Input pattern of A, LabVIEW dims the vector input patterns for the Input pattern of B. If you choose a vector input pattern for the Input pattern of A, LabVIEW dims the element input patterns for the Input pattern of B. Row-Wise Element—Specifies that matrix A receives one element per clock cycle by row of the matrix. Column-Wise Element—Specifies that matrix A receives one element per clock cycle by column of the matrix. Row Vector—Specifies that matrix A receives one vector per clock cycle by row. Column Vector—Specifies that matrix A receives one vector per clock cycle by column. Throughput—Specifies the minimum number of clock cycles between two successive valid input matrices. LabVIEW calculates the Throughput of this function based on the values of M, L, and N as specified in Matrix Size. Selecting fewer cycles per matrix results in a higher throughput rate. Input pattern of B—Specifies that the function receives data from matrix B element by element in the matrix, by vector, by row-wise, or by column-wise. Matrix A and matrix B must both use the same input pattern. If you choose an element input pattern for the Input pattern of A, LabVIEW dims the vector input patterns for the Input pattern of B. If you choose a vector input pattern for the Input pattern of A, LabVIEW dims the element input patterns for the Input pattern of B. Row-Wise Element—Specifies that matrix B receives one element per clock cycle by row of the matrix. Column-Wise Element—Specifies that matrix B receives one element per clock cycle by column of the matrix. Row Vector—Specifies that matrix B receives one vector per clock cycle by row. Column Vector—Specifies that matrix B receives one vector per clock cycle by column. Output pattern—Specifies that the function returns data for matrix C element by element in the matrix, by vector, or by row-wise. Row-Wise Element—Specifies that matrix C returns one element per clock cycle by row. Row Vector—Specifies that matrix C returns one vector per clock cycle by row. Column Vector—Specifies that matrix C returns one vector per clock cycle by column. |
| Implementation Details | Specifies options for pipelining this function internally. These options affect the maximum clock rate at which this function can compile. Number of pipelining stages—Specifies how many pipelining stages this function uses internally. Increasing the number of stages increases the clock rate at which this function can compile but also increases the latency and the amount of FPGA resources this function requires. The degree of pipelining changes with word length and vector size. The default is Max. Min specifies a minimal number of pipelining stages. |
| Number of pipelining stages | Specifies how many pipelining stages this function uses internally. Increasing the number of stages increases the clock rate at which this function can compile but also increases the latency and the amount of FPGA resources this function requires. The degree of pipelining changes with word length and vector size. The default is Max. Min specifies a minimal number of pipelining stages. |

#### Inputs/Outputs

| ar — Specifies the real part of the a multiplicand. ai — Specifies the imaginary part of the a multiplicand. br — Specifies the real part of the b multiplicand. bi — Specifies the imaginary part of the b multiplicand. a valid — Specifies whether the next data point to a has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to the a input of this node. b valid — pecifies whether the next data point to b has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to the b input of this node. ready for output (T) — Specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire the ready for input output of a downstream node to this input of the current node. Note If this terminal returns FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. cr — Returns the real part of the matrix product of a*b. ci — Returns the imaginary part of the matrix product of a*b. operation overflow — Returns TRUE if the theoretical computed value exceeds the valid range of the output data type. If operation overflow returns TRUE, the Overflow mode you specify in the configuration dialog box determines the value this function returns. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. Wire this output to the input valid input of a downstream node to transfer data from the node to the downstream node. ready for a — Returns TRUE if this node is ready to accept new input data for the a input. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to the a input of this node during the following cycle. LabVIEW discards this data even if the a valid terminal is TRUE during the following cycle. ready for b — Returns TRUE if this node is ready to accept new input data for the b input. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to the b input of this node during the following cycle. LabVIEW discards this data even if the b valid terminal is TRUE during the following cycle. |
| --- |

Both **a valid** and **b valid** are required for matrix *A* and matrix *B* since the input cycles of matrix *A* and matrix *B* might be different.

The real and imaginary inputs of this function must be of the same data type and input pattern, otherwise the data type or array size of the real portion of the input takes precedent.

#### Improving Function Performance by Pipelining

You can improve the timing performance of this function on an FPGA target by adjusting the **Number of pipelining stages**.

In general, increasing the **Number of pipelining stages** also increases the maximum clock rate at which this function can compile. However, the actual clock rate depends on many factors, including the following:

- The FPGA target you use
- The size of the multiplier
- The rounding and overflow modes you select
- Other FPGA logic besides the multiplier

#### Handshaking

Refer to the [Scheduling Timing Using 
 
 Handshaking Signals](/csh?context=lvfpga_lvfpgaconcepts_fpga_handshaking) topic for more information about handshaking.

Parent topic:

Linear Algebra

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/linearalgebra/matrixtranspose/xnode/nifxpla-matrixtranspose-xnode.html language=enus -->
## TOPIC 00300: Matrix Transpose

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/linearalgebra/matrixtranspose/xnode/nifxpla-matrixtranspose-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/linearalgebra/matrixtranspose/xnode/nifxpla-matrixtranspose-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transposes a complex matrix. This function supports only scalar and 1D fixed-size array values of the fixed-point data type. icon Dialog Box Options Parameter Description Input Matrix Configuration Specifies the encodings, word lengths, and integer word lengths of the input terminals and the configu

### Matrix Transpose

Transposes a complex matrix.

This function supports only scalar and [1D fixed-size array](/csh?context=lvfpga_lvfpgahelp_creating_fixedsize_arrays) values of the [fixed-point](/csh?context=lvfpga_lvfpgahelp_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpla-matrixtranspose-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Input Matrix Configuration | Specifies the encodings, word lengths, and integer word lengths of the input terminals and the configuration of the input matrix of this function. Data Type—Specifies the configuration of the input terminals. If you wire a fixed-point data type to these terminals, LabVIEW dims this section and uses information from the wire. Signed—Specifies that these terminals are signed. Unsigned—Specifies that these terminals are unsigned. Word length—Specifies the word length of these terminals. Integer word length—pecifies the integer word length of these terminals. Number of rows—Specifies the row number of the input matrix. Number of columns—Specifies the column number of the input matrix. Pattern—Specifies that the function receives data by row of the matrix or by column of the matrix. If the input pattern is Row-Wise and you wire a fixed-point 1D array to the real data in or imaginary data in input terminal, LabVIEW dims Number of columns and uses the array size information from the wire. If the input pattern is Column-Wise and you wire a fixed-point 1D array to the real data in or imaginary data in input terminal, LabVIEW dims Number of rows and uses the array size information from the wire. Row-Wise—Specifies that the matrix receives data by row. Column-Wise—Specifies that the matrix receives data by column. |
| Output Matrix Configuration | Specifies whether to conjugate the input during operation and specifies the encodings, word lengths, and integer word lengths of the output terminals of this function. Conjugate—Specifies whether to conjugate the input of the matrix during operation. Selecting this option requires additional FPGA resources. LabVIEW displays an icon on the block diagram based on the conjugation option you choose. By default, this checkbox does not contain a checkmark. Data Type—Displays the configuration of the output terminals. LabVIEW dims this section and uses information from the wire. If Conjugate is deselected or the imaginary data in terminal is not wired, the output data type is the same as the input. If Conjugate is selected and the imaginary data in terminal is wired, the word length and integer word length of the output data type is 1 bit larger than that of the input, and the output encoding is signed regardless of the signed status of the input. Signed—Specifies that these terminals are signed. Unsigned—Specifies that these terminals are unsigned. Word length—Specifies the word length of these terminals. Integer word length—Specifies the integer word length of these terminals. |
| Implementation Details | Specifies how to implement the function in memory. Resource—You can choose from Look-Up Table or Block Memory when you wire a fixed-point scalar value to the real data in or the imaginary data in input terminal. If you wire a fixed-point 1D fixed-size array to the real data in or the imaginary data in input terminal, LabVIEW dims Resource and defaults to a Look-Up Table implementation. Look-Up Table (default)—Specifies that this function implements using LUTs. Block Memory—Specifies that this function uses embedded blocks of memory. Xilinx documentation describes this implementation as block RAM or BRAM. Consider choosing this option when transposing a large matrix to avoid consuming excessive FPGA resources. |

#### Inputs/Outputs

| real data in — Specifies the real part of the input to this function. The real and imaginary inputs of this function must be of the same data type and input pattern, otherwise the data type or array size of the real data in terminal takes precedent. imaginary data in — Specifies the imaginary part of the input to this function. The real and imaginary inputs of this function must be of the same data type and input pattern, otherwise the data type or array size of the real data in terminal takes precedent. input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node. ready for output (T) — Specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire the ready for input output of a downstream node to this input of the current node. Note If this terminal is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. real data out — Specifies the real part of the output of this function. imaginary data out — Specifies the imaginary part of the output of this function. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. After returning TRUE for the previous output frame, this indicator returns FALSE, waiting for the next frame to complete. Wire this output to the input valid input of a downstream node to transfer data from the node to the downstream node. ready for input — Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the input valid terminal is TRUE during the following cycle. |
| --- |

The real and imaginary inputs of this function must be of the same data type and input pattern, otherwise the data type or array size of the **real data in** terminal takes precedent.

#### Handshaking

Refer to the [Scheduling Timing Using 
 
 Handshaking Signals](/csh?context=lvfpga_lvfpgaconcepts_fpga_handshaking) topic for more information about handshaking.

Parent topic:

Linear Algebra

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/linearalgebra/normsquare/xnode/nifxpla-normsquare-xnode.html language=enus -->
## TOPIC 00301: Norm Square

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/linearalgebra/normsquare/xnode/nifxpla-normsquare-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/linearalgebra/normsquare/xnode/nifxpla-normsquare-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the norm square of a complex vector. This function accepts frames of data, performs computations on the input data, and returns a valid single result for each frame. This function supports only scalar and 1D fixed-size array values of the fixed-point data type. icon Dialog Box Options Param

### Norm Square

Computes the norm square of a complex vector.

This function supports only scalar and [1D fixed-size array](/csh?context=lvfpga_lvfpgahelp_creating_fixedsize_arrays) values of the [fixed-point](/csh?context=lvfpga_lvfpgahelp_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpla-normsquare-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Input Vector Configuration | Specifies the encodings, word lengths, and integer word lengths of the input terminals of this function. xr/xi Type—Specifies the real or imaginary fixed-point configuration of the xr/xi input terminals. If you wire a fixed-point data type to these terminals, LabVIEW dims this section and uses information from the wire. The xr/xi inputs of this function must be of the same data type and input pattern, otherwise the data type or array size of the xr input terminal takes precedent. If the dominating wire is a 1D fixed-size array, LabVIEW dims Vector size and uses the array size from the wire. Signed—Specifies that these terminals are signed. Unsigned—Specifies that these terminals are unsigned. Word length—Specifies the word length of these terminals. Integer word length—Specifies the integer word length of these terminals. Vector size—Specifies the size of the input vector. |
| Operation | Norm Square Type—Specifies the configuration of the norm square output terminal. Adapt to source—Specifies whether LabVIEW automatically adjusts the fixed-point configuration of the output data type to avoidoverflow and rounding errors.By default, this checkbox contains a checkmark, and LabVIEW dims the following options. Note LabVIEW supports a maximum word length of 64 bits and a maximum integer word length of 1023 bits. If you place a checkmark in this checkbox and the output data type requires a word length that exceeds these maximum values, overflow and/or rounding errors might occur. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. Overflow mode—Specifies how this function handles overflow. You can choose either Wrap (default) or Saturate. Note The Saturate option requires more FPGA resources and a longer combinatorial path than the Wrap option does. In this situation, choosing Saturate might decrease the maximum clock rate at which this function can compile. Rounding mode—Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. |
| Implementation Details | Specifies options for implementation resources and for pipelining this function internally. These options affect the maximum clock rate at which this function can compile and may exceed available FPGA resources. Resource—Specifies how to implement the multiplier. You can choose from the following options: Auto (default)—Specifies that the compiler decides whether to use embedded block multipliers or look-up tables (LUTs) to implement the multiplier. Look-Up Table—Specifies that this function uses LUTs to implement the multiplier. Number of pipelining stages—Specifies how many pipelining stages this function uses internally. Increasing the number of stages increases the clock rate at which this function can compile but also increases the latency and the amount of FPGA resources this function requires. The degree of pipelining changes with word length and vector size. The default is Max. Min specifies a minimal number of pipelining stages. |

#### Inputs/Outputs

| xr — Specifies the real part of the input to this function. xi — Specifies the imaginary part of the input to this function. input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node. ready for output (T) — Specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire the ready for input output of a downstream node to this input of the current node. Note If this terminal is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. norm square — Returns the norm square of input vector x. operation overflow — Returns TRUE if the theoretical computed value exceeds the valid range of the output data type. If operation overflow returns TRUE, the Overflow mode you specify in the configuration dialog box determines the value this function returns. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. After returning TRUE for the previous output frame, this indicator returns FALSE, waiting for the next frame to complete. Wire this output to the input valid input of a downstream node to transfer data from the node to the downstream node. ready for input — Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the input valid terminal is TRUE during the following cycle. |
| --- |

The **xr/xi** inputs of this function must be of the same data type and input pattern, otherwise the data type or array size of the **xr** input terminal takes precedent. If the dominating wire is a 1D fixed-size array, LabVIEW dims **Vector size** and uses the array size from the wire.

#### Improving Function Performance by Pipelining

You can improve the timing performance of this function on an FPGA target by adjusting the **Number of pipelining stages**.

In general, increasing the **Number of pipelining stages** also increases the maximum clock rate at which this function can compile. However, the actual clock rate depends on many factors, including the following:

- The FPGA target you use
- The size of the multiplier
- The rounding and overflow modes you select
- The Resource you select
- Other FPGA logic besides the multiplier

#### Handshaking

Refer to the [Scheduling Timing Using 
 
 Handshaking Signals](/csh?context=lvfpga_lvfpgaconcepts_fpga_handshaking) topic for more information about handshaking.

Parent topic:

Linear Algebra

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-handshake-vi.html language=enus -->
## TOPIC 00302: VI-Defined Handshake Configuration

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-handshake-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-handshake-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a VI-defined handshake item. Right-click the node and select Configure to configure the VI-defined handshake item. Use VI-defined handshake items to create reentrant subVIs and avoid resource conflicts. icon Inputs/Outputs igenclassrntag.png Handshake Out Handshake Out returns Handshake I

### VI-Defined Handshake Configuration

Represents a [VI-defined handshake item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant). Right-click the node and select **Configure** to configure the VI-defined handshake item. Use VI-defined handshake items to create reentrant subVIs and avoid resource conflicts.

[IMAGE alt='icon' src='nifpgalrmpalette-mergevi-handshake-vi.png']

#### Inputs/Outputs

| Handshake Out — Handshake Out returns Handshake In if Handshake In is wired. Otherwise, Handshake Out returns the handshake item that you specify in the Handshake Method Node. |
| --- |

If you use a VI-defined handshake item in a reentrant FPGA VI, LabVIEW creates a separate copy of the handshake item for each instance of the VI to avoid resource conflicts.

You can create a VI-defined handshake item with the same name as a target-scoped handshake item. You also can create VI-defined handshake items with the same name in different VIs. However, you cannot create multiple VI-defined handshake items with the same name in the same VI.

Parent topic:

Data Storage & Transfer

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-register-vi.html language=enus -->
## TOPIC 00303: VI-Defined Register Configuration

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-register-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-register-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a VI-defined register item. Right-click the node and select Configure to configure the VI-defined register item. icon Inputs/Outputs igenclassrntag.png Register Out Register Out returns the register item you specify in the FPGA Register Properties dialog box. Use the FPGA Register Propert

### VI-Defined Register Configuration

Represents a VI-defined [register item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant). Right-click the node and select **Configure** to configure the VI-defined register item.

[IMAGE alt='icon' src='nifpgalrmpalette-mergevi-register-vi.png']

#### Inputs/Outputs

| Register Out — Register Out returns the register item you specify in the FPGA Register Properties dialog box. |
| --- |

Use the **FPGA Register Properties** dialog box to initialize the register item.

Use the Read and Write methods to read from or write to the VI-defined register item.

If you use a VI-defined register item in a reentrant FPGA VI, LabVIEW creates a separate copy of the register item for each instance of the VI to avoid resource conflicts.

You can create a VI-defined register item with the same name as a target-scoped register item. You also can create VI-defined register items with the same name in different VIs. However, you cannot create VI-defined register items with the same name in the same VI.

Parent topic:

Data Storage & Transfer

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/localresourcemanager/lrm-api/nirvilrmpalette-mergevi-fifo-vi.html language=enus -->
## TOPIC 00304: VI-Defined FIFO Configuration

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/localresourcemanager/lrm-api/nirvilrmpalette-mergevi-fifo-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/localresourcemanager/lrm-api/nirvilrmpalette-mergevi-fifo-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a VI-defined FIFO. Right-click the node and select Configure to configure the VI-defined FIFO. icon Inputs/Outputs igenclassrntag.png FIFO Out FIFO Out returns the FIFO you specify in the FIFO Properties dialog box. Use the Read and Write methods to read from or write to the VI-defined FI

### VI-Defined FIFO Configuration

Represents a VI-defined FIFO. Right-click the node and select **Configure** to configure the VI-defined FIFO.

[IMAGE alt='icon' src='nirvilrmpalette-mergevi-fifo-vi.png']

#### Inputs/Outputs

| FIFO Out — FIFO Out returns the FIFO you specify in the FIFO Properties dialog box. |
| --- |

Use the [Read](/csh?context=lvfpga_lvfpga_fifo_read) and [Write](/csh?context=lvfpga_lvfpga_fifo_write) methods to read from or write to the VI-defined FIFO. FIFOs are initially empty. If you reset the FPGA VI, LabVIEW clears the FIFO.

If you use a VI-defined FIFO in a reentrant FPGA VI, LabVIEW creates a separate copy of the FIFO for each instance of the VI to avoid resource conflicts.

You can create a VI-defined FIFO with the same name as a target-scoped FIFO or DMA FIFO. You also can create VI-defined FIFOs with the same name in different VIs. However, you cannot create multiple VI-defined FIFOs with the same name in the same VI.

Parent topic:

Data Storage & Transfer

Parent topic:

FIFO

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/localresourcemanager/lrm-api/nirvilrmpalette-mergevi-memory-vi.html language=enus -->
## TOPIC 00305: VI-Defined Memory Configuration

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/localresourcemanager/lrm-api/nirvilrmpalette-mergevi-memory-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/localresourcemanager/lrm-api/nirvilrmpalette-mergevi-memory-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a VI-defined memory item. Right-click the node and select Configure to configure the VI-defined memory item. icon Inputs/Outputs igenclassrntag.png Memory Out Memory Out returns the memory you specify in the Memory Properties dialog box. Use the Memory Properties dialog box to initialize

### VI-Defined Memory Configuration

Represents a VI-defined memory item. Right-click the node and select **Configure** to configure the VI-defined memory item.

[IMAGE alt='icon' src='nirvilrmpalette-mergevi-memory-vi.png']

#### Inputs/Outputs

| Memory Out — Memory Out returns the memory you specify in the Memory Properties dialog box. |
| --- |

Use the **Memory Properties** dialog box to initialize the memory. If you reset the VI, the memory remains unchanged. You must download the VI again to reinitialize the memory.

Use the [Read](/csh?context=lvfpga_lvfpga_memory_read) and [Write](/csh?context=lvfpga_lvfpga_memory_write) methods to read from or write to the VI-defined memory item.

If you use a VI-defined memory item in a reentrant FPGA VI, LabVIEW creates a separate copy of the memory item for each instance of the VI to avoid resource conflicts.

You can create a VI-defined memory item with the same name as a target-scoped memory item. You also can create VI-defined memory items with the same name in different VIs. However, you cannot create VI-defined memory items with the same name in the same VI.

Parent topic:

Data Storage & Transfer

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/memory/memory-common/memory-properties-dialog-box.html language=enus -->
## TOPIC 00306: Memory Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/memory/memory-common/memory-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/memory/memory-common/memory-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target and select New»Memory from the shortcut menu to display this dialog box. You also can right-click a memory item in the Project Explorer window and select Properties from the shortcut menu or right-click a VI-Defined Memory Configuration node on the block diagram and select

### Memory Properties Dialog Box

Right-click an FPGA target and select **New»Memory** from the shortcut menu to display this dialog box. You also can right-click a memory item in the **Project Explorer** window and select **Properties** from the shortcut menu or right-click a [VI-Defined Memory Configuration](../../localresourcemanager/lrm-api/nirvilrmpalette-mergevi-memory-vi.html) node on the block diagram and select **Configure** from the shortcut menu to display this dialog box.

Use this dialog box to edit properties for [memory items](/csh?context=lvfpga_lvfpgaconcepts_fpga_memory_items).

This dialog box includes the following pages:

- General
- Data Type
- Interfaces
- Initial Values

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/memory/memory-common/nirvimemorypalettemergevi-vi.html language=enus -->
## TOPIC 00307: Memory Method Node

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/memory/memory-common/nirvimemorypalettemergevi-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/memory/memory-common/nirvimemorypalettemergevi-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Invokes a method on a memory block on the FPGA. The methods available depend on the type of memory you configure. You must specify a memory item before you specify a method. You can invoke the following memory methods for memory you implement as block memory or look-up tables: Write, Read You can in

### Memory Method Node

Invokes a method on a memory block on the FPGA. The methods available depend on the type of memory you configure.

You must specify a memory item before you specify a method.

You can invoke the following memory methods for memory you implement as block memory or look-up tables:

Write

Read

You can invoke the following memory methods for memory you implement as [DRAM](/csh?context=lvfpga_lvfpgaconcepts_fpga_dram_intro):

Write

Request Data

Retrieve Data

Note

two read interfaces

[A]

[B]

[IMAGE alt='icon' src='nirvimemorypalettemergevi-vi.png']

#### Inputs/Outputs

| Memory In — Memory In specifies the FPGA memory. You can wire a Memory control, Memory constant, VI-Defined Memory Configuration node, or another Memory Method Node to Memory In. Memory Out — Memory Out returns Memory In if Memory In is wired. Otherwise, Memory Out returns the memory that you specify in the Memory Method Node. |
| --- |

To use the Memory Method Node, you first must [create memory items](/csh?context=lvfpga_lvfpgahelp_fpga_creating_memory_items). You can create a memory item in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window or using a [VI-Defined Memory Configuration](../../localresourcemanager/lrm-api/nirvilrmpalette-mergevi-memory-vi.html) node. You then can right-click the Memory Method Node and select the memory item from the **Select Memory** shortcut menu.

When you wire a memory item to **Memory In**, LabVIEW renames this node to Memory Item to indicate that the node is now associated with a memory item in the project.

Tip

Project Explorer

Right-click the Memory Method Node and select **Add New Memory** from the shortcut menu to create a new memory item in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window.

Tip

Memory In

Find Item in Project

Project Explorer

If you reset the FPGA VI, the memory remains unchanged. You must download the FPGA VI again to reinitialize the memory.

#### Displaying Error-Handling Terminals

Add error terminals to monitor whether the operation you performed completed correctly. You also can add error terminals to place this node in the data flow. Right-click the Memory Method Node on the block diagram and select **Show Error Terminals** from the shortcut menu to add standard LabVIEW **error in** and **error out** parameters to the node. If **error in** includes an error, you might receive incorrect data.

Note

error in

error out

error in

error out

To use this node in the data flow without using error terminals, include the node in a [Flat Sequence](/csh?productcategories=147794&context=lvcore_glang_flat_sequence) or [Stacked Sequence](/csh?productcategories=147794&context=lvcore_glang_flat_sequence) structure.

Parent topic:

Data Storage & Transfer

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/memory/memory-common/nirvimemorypalettemergevimemorynameconstant-vi.html language=enus -->
## TOPIC 00308: Memory Constant

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/memory/memory-common/nirvimemorypalettemergevimemorynameconstant-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/memory/memory-common/nirvimemorypalettemergevimemorynameconstant-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Memory constant to specify a memory item on the block diagram. Use the Configure Memory Name Control Type dialog box to configure a Memory constant. The pull-down menu that appears when you click the arrow on the Memory constant lists only the memory items that appear in the Project Explorer

### Memory Constant

Use the Memory constant to specify a [memory item](/csh?context=lvfpga_lvfpgaconcepts_fpga_memory_items) on the block diagram.

Use the [Configure Memory Name Control Type](/csh?context=lvfpga_lvfpgadialog_fpga_mem_name_contol_db) dialog box to configure a Memory constant.

The pull-down menu that appears when you click the arrow on the Memory constant lists only the memory items that appear in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window under the same FPGA target as the active VI and that match the configuration of the constant. When you select an item from the pull-down menu, the configuration of the constant matches the configuration of the item you select from the pull-down menu.

You also can use the [Memory control](/csh?context=lvfpga_lvfpgaconcepts_fpga_name_controls) to specify a memory item on the block diagram.

Note

FPGA I/O constant

FPGA clock constant

Register constant

FIFO constant

Handshake constant

[IMAGE alt='icon' src='nirvimemorypalettemergevimemorynameconstant-vi.png']

Parent topic:

Data Storage & Transfer

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/memory/memory-common/read-memory-method.html language=enus -->
## TOPIC 00309: Read (Memory Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/memory/memory-common/read-memory-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/memory/memory-common/read-memory-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads from memory available on the FPGA target. If the memory is configured for both read and write access, you can use this method in conjunction with the Write method. If you configure the memory for dual port read access, the label includes an [A] or [B] to indicate which interface this node will

### Read (Memory Method)

Reads from memory available on the FPGA target. If the memory is configured for both read and write access, you can use this method in conjunction with the [Write](/csh?context=lvfpga_lvfpga_memory_write) method. If you configure the memory for [dual port read access](/csh?context=lvfpga_lvfpgadialog_memory_adv_code_gen), the label includes an **[A]** or **[B]** to indicate which interface this node will access.

Use the [Memory Method Node](nirvimemorypalettemergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| Memory In | Specifies the FPGA memory. You can wire a Memory control, Memory constant, VI-Defined Memory Configuration node, or another Memory Method Node to Memory In. |
| Address | Specifies the location of the data in memory on the FPGA target. The valid address range depends on the Requested number of elements you specify on the General page of the Memory Properties dialog box. For example, if you specify a Requested number of elements of 1000, the valid address range is 0–999.If Address exceeds the address range, the Read method returns an error and the output data might be invalid. Add error terminals so LabVIEW can notify you if Address exceeds the address range. |
| Memory Out | Returns Memory In if Memory In is wired. Otherwise, Memory Out returns the memory that you specify in the Memory Method Node. |
| Data | Returns the data read from memory on the FPGA target. Data is directly accessible only from within the FPGA VI. You cannot directly access the data in the memory of the FPGA target from the host VI. You must use controls, indicators, or DMA FIFOs to access data from the host VI.The Data data type is the data type you configure in the Memory Properties dialog box when you create the memory item. If you do not initialize the memory item, the data is undefined. |

You cannot use the Read method with DRAM memory. Use the [Request Data](/csh?context=lvfpga_lvfpga_fpga_mem_method_request) and [Retrieve Data](/csh?context=lvfpga_lvfpga_fpga_mem_method_retrieve) methods instead.

#### Considerations for Single-Cycle Timed Loops

Consider the following when you use this node inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop):

- You must set the read Arbitration option on the Interfaces page to Arbitrate if Multiple Requestors Only or Never Arbitrate , and you cannot use this node with the same memory item anywhere else in the FPGA VI.
 Note Selecting the **Never Arbitrate** option when simulating an FPGA application that contains memory items with multiple accessors may result in incorrect behavior. For example, if your application includes multiple writers, each writer can update the memory address specified during simulation. Additionally, if your application includes multiple readers, each reader can assess the memory address specified during simulation.
- The FPGA resource that the memory item uses affects how you read from the memory item using this node. 
 **Block Memory** 
 If you implement the memory item using block memory, the number of cycles required for the Read (Memory Method) to produce a valid **Data** value is equal to the number of cycles of read latency. The number under the icon at the top of the Read (Memory Method) node indicates the number of cycles of latency. 
 Inside the single-cycle Timed Loop, the number of Feedback Nodes or uninitialized shift registers wired to the **Data** output of the Read (Memory Method) node must be greater than or equal to the number of cycles of read latency. If you use Feedback Nodes, each Feedback Node must not display the enable terminal. If any Feedback Node displays the enable terminal or you do not wire enough Feedback Nodes or uninitialized shift registers after the Read (Memory Method), the FPGA VI fails to compile and LabVIEW returns an error. 
 Note LabVIEW supports initialization of Feedback Nodes following the Read (Memory Method) only when **Cycles of read latency** is set to 1. 
 **Look-Up Tables** 
 If you implement the memory item using look-up tables, you do not need to wire the node output directly to a Feedback Node or uninitialized shift register. You can read from the memory item during the same cycle in which you provide the **Address**.
- You can use a target-scoped or a VI-defined memory item to store data and access it from a different clock domain only if you implement the memory item using block memory. In this implementation, you can use only one writer node and one reader node for each memory item.
 Caution When you use memory items implemented using block memory in multiple clock domains, it is possible to read from and write to the same address simultaneously. Doing so can result in reading incorrect data.

Parent topic:

Memory Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/memory/memory-common/request-data-memory-method.html language=enus -->
## TOPIC 00310: Request Data (Memory Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/memory/memory-common/request-data-memory-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/memory/memory-common/request-data-memory-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queues requests for data from the DRAM memory on the FPGA target. Use this method in conjunction with the Retrieve Data method to read data from DRAM. To overcome the latency of DRAM, queue requests for data in bursts. Use the Memory Method Node to implement this method. Only DRAM memory supports th

### Request Data (Memory Method)

Queues requests for data from the DRAM memory on the FPGA target. Use this method in conjunction with the [Retrieve Data](/csh?context=lvfpga_lvfpga_fpga_mem_method_retrieve) method to read data from DRAM. To overcome the [latency of DRAM](/csh?context=lvfpga_lvfpgaconcepts_fpga_dram_intro), queue requests for data in bursts.

Use the [Memory Method Node](nirvimemorypalettemergevi-vi.html) to implement this method. Only DRAM memory supports this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| Memory In | Specifies the FPGA memory. If you leave Memory In unwired, you can specify the FPGA memory by right-clicking the Memory Method Node and selecting a memory item from the shortcut menu. Otherwise, you can wire a Memory control, Memory constant, or another Memory Method node to Memory In. |
| Address | Specifies the location of the data in memory on the FPGA target. The valid address range depends on the Requested number of elements you specify in the Memory Properties dialog box. For example, if you specify a Requested number of elements of 65536, the valid address range is 0–65535.If Address exceeds the address range, the Request Data method might access different memory than expected, causing output data from the Retrieve Method to be invalid. |
| Input Valid | Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node. To display this handshaking terminal, configure the memory as DRAM. |
| Memory Out | Returns Memory In if Memory In is wired. Otherwise, Memory Out returns the memory that you specify in the Memory Method Node. |
| Ready for Input | Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the Input Valid terminal is TRUE during the following cycle. To display this terminal, configure the memory as DRAM. |

This method specifies the order in which the Retrieve Data method returns data. You specify the maximum outstanding requests on the [General](/csh?context=lvfpga_lvfpgadialog_memory_general_page) page of the **Memory Properties** dialog box. To guarantee that you do not receive stale data, you should initialize the DRAM before using it.

Note

#### Considerations for Single-Cycle Timed Loops

You only can use this method inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

Parent topic:

Memory Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/memory/memory-common/retrieve-data-memory-method.html language=enus -->
## TOPIC 00311: Retrieve Data (Memory Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/memory/memory-common/retrieve-data-memory-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/memory/memory-common/retrieve-data-memory-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data you request with the Request Data method. Use the Memory Method Node to implement this method. Only DRAM memory supports this method. Inputs/Outputs Option Description Memory In Specifies the FPGA memory. If you leave Memory In unwired, you can specify the FPGA memory by right-clickin

### Retrieve Data (Memory Method)

Retrieves data you request with the [Request Data](/csh?context=lvfpga_lvfpga_fpga_mem_method_request) method.

Use the [Memory Method Node](nirvimemorypalettemergevi-vi.html) to implement this method. Only DRAM memory supports this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| Memory In | Specifies the FPGA memory. If you leave Memory In unwired, you can specify the FPGA memory by right-clicking the Memory Method Node and selecting a memory item from the shortcut menu. Otherwise, you can wire a Memory control, Memory constant, or another Memory Method node to Memory In. |
| Ready for Output | Specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire the Ready for Input output of a downstream node to this input of the current node. Note If this terminal is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. |
| Memory Out | Returns Memory In if Memory In is wired. Otherwise, Memory Out returns the memory that you specify in the Memory Method Node. |
| Data | Is the data retrieved from memory on the FPGA target. Data is directly accessible only from within the FPGA VI. You cannot directly access the data in the memory of the FPGA target from the host VI. You must use controls, indicators, or DMA FIFOs to access data from the host VI.The Data data type is the data type you configure in the Memory Properties dialog box when you create the memory item. If you do not initialize the memory item, the data is undefined. |
| Output Valid | Returns TRUE if this node has computed a result that downstream nodes can use. Wire this output to the Input Valid input of a downstream node to transfer data from the node to the downstream node. |

This method retrieves data in the same order that the Request Data method requests it.

Note

#### Considerations for Single-Cycle Timed Loops

You can use this method only inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

Parent topic:

Memory Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/memory/memory-common/write-memory-method.html language=enus -->
## TOPIC 00312: Write (Memory Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/memory/memory-common/write-memory-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/memory/memory-common/write-memory-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes to memory available on the FPGA target. Use the Memory Method Node to implement this method. Inputs/Outputs Option Description Memory In Specifies the FPGA memory. You can wire a Memory control, Memory constant, VI-Defined Memory Configuration node, or another Memory Method Node to Memory In.

### Write (Memory Method)

Writes to memory available on the FPGA target.

Use the [Memory Method Node](nirvimemorypalettemergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| Memory In | Specifies the FPGA memory. You can wire a Memory control, Memory constant, VI-Defined Memory Configuration node, or another Memory Method Node to Memory In. |
| Address | Specifies the location of the data in memory on the FPGA target. The valid address range depends on the Requested number of elements you specify in the Memory Properties dialog box. For example, if you specify a Requested number of elements of 65536, the valid address range is 0–65535.If Address exceeds the address range, the Memory Method Node returns an error and does not write the data. Add error terminals so LabVIEW can notify you if Address exceeds the address range. |
| Data | Is the data to write to the memory on the FPGA target. You can directly write to Data only from the FPGA VI. You cannot directly write to the data in the memory of the FPGA target from the host VI. You must use controls, indicators, or DMA FIFOs to access data from the host VI. If you do not initialize the memory item, the data is undefined. |
| Byte Enables | Specifies which bytes of data are enabled when this node writes data to memory. The least significant bit corresponds to the least significant byte of data, the second least significant bit corresponds to the second least significant byte of data, and so on. By default, Byte Enables is an integer of all ones, large enough to enable all bytes for the target.To display this terminal, configure the memory as DRAM, then right-click the node and select Show Byte Enables from the pull-down menu. Refer to your target hardware documentation for more information about the DRAM width in bytes for your target. |
| Input Valid | Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node.To display this handshaking terminal, configure the memory as DRAM. |
| Memory Out | Returns Memory In if Memory In is wired. Otherwise, Memory Out returns the memory that you specify in the Memory Method Node. |
| Ready for Input | Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the Input Valid terminal is TRUE during the following cycle. To display this terminal, configure the memory as DRAM. |

Use this method in conjunction with the [Read](/csh?context=lvfpga_lvfpga_memory_read) method when you implement the memory using block memory or LUTs. Use this method in conjunction with the [Request Data](/csh?context=lvfpga_lvfpga_fpga_mem_method_request) and [Retrieve Data](/csh?context=lvfpga_lvfpga_fpga_mem_method_retrieve) methods when you implement the memory using DRAM.

Note

#### Considerations for Single-Cycle Timed Loops

- If you use this node in a single-cycle Timed Loop , you must set the Write option on the Interfaces page to Arbitrate if Multiple Requestors Only or Never Arbitrate , and you cannot use this node with the same memory item anywhere else in the FPGA VI.
 Note Selecting the **Never Arbitrate** option when simulating an FPGA application that contains memory items with multiple accessors may result in incorrect behavior. For example, if your application includes multiple writers, each writer can update the memory address specified during simulation. Additionally, if your application includes multiple readers, each reader can assess the memory address specified during simulation.
- The Memory Method Node takes an entire clock cycle to execute.
- You can use a target-scoped or VI-defined memory item to store data and access it from a different clock domain only if you implement the memory item using block memory. In this implementation, you can use only one writer node and one reader node for each memory item.
 Caution When you use memory items implemented using block memory in multiple clock domains, it is possible to read from and write to the same address simultaneously. Doing so can result in reading incorrect data.
- If the memory is DRAM , you must use this method in a single-cycle Timed Loop.

Parent topic:

Memory Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/occurrence/nirviwaitonoccurrence-vi.html language=enus -->
## TOPIC 00313: Wait on Occurrence with Timeout in Ticks

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/occurrence/nirviwaitonoccurrence-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/occurrence/nirviwaitonoccurrence-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the Set Occurrence function to set or trigger the given occurrence. icon Inputs/Outputs ci32.png ticks timeout (-1) ticks timeout is the specified amount of time, in ticks, for the occurrence to occur. If the occurrence does not occur within the specified ticks timeout, the function return

### Wait on Occurrence with Timeout in Ticks

Waits for the [Set Occurrence](/csh?context=lvcore_glang_set_occurrence) function to set or trigger the given **occurrence**.

[IMAGE alt='icon' src='nirviwaitonoccurrence-vi.png']

#### Inputs/Outputs

| ticks timeout (-1) — ticks timeout is the specified amount of time, in ticks, for the occurrence to occur. If the occurrence does not occur within the specified ticks timeout, the function returns a value of TRUE. If ticks timeout is –1, the function does not time out. occurrence — occurrence is the occurrence refnum that links the Wait on Occurrence with Timeout in Ticks function and Set Occurrence function. ignore previous (T) — If ignore previous is TRUE (default) and another node has set the occurrence before this function began executing, the function ignores the previous occurrence and waits for another one. When ignore previous is FALSE, the function checks whether another node previously set an occurrence. If so, the function executes. However, the Wait on Occurrence function only processes one occurrence at a time and does not hold multiple previous occurrences in memory. timed out — timed out is TRUE if the occurrence does not occur within the specified ticks timeout. If ticks timeout is –1, timed out is FALSE. |
| --- |

Parent topic:

Occurrences

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/timedloop/nifpga-palettemergevi-clocknameconstant-vi.html language=enus -->
## TOPIC 00314: FPGA Clock Constant

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/timedloop/nifpga-palettemergevi-clocknameconstant-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/timedloop/nifpga-palettemergevi-clocknameconstant-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FPGA clock constant to specify an FPGA clock on the block diagram. The shortcut menu that appears when you click the arrow button on the right of the constant lists the clocks that appear in the Project Explorer window under the same FPGA target as the active VI. To use an FPGA clock that is

### FPGA Clock Constant

Use the FPGA clock constant to specify an FPGA clock on the block diagram.

The shortcut menu that appears when you click the arrow button on the right of the constant lists the clocks that appear in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window under the same FPGA target as the active VI. To use an FPGA clock that is not already in the project, first add the FPGA [base clock](/csh?context=lvfpga_lvfpgahelp_adding_fpga_base_clock), [derived clock](/csh?context=lvfpga_lvfpgahelp_creating_fpga_derived_clk), or [component-level IP (CLIP) clock](/csh?context=lvfpga_lvfpgahelp_fpga_using_clip_clock) to the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window.

You also can specify an FPGA clock by clicking inside the constant and typing the name of the clock.

When creating a reusable subVI, use the [FPGA clock control](/csh?context=lvfpga_lvfpgaconcepts_fpga_name_controls) to specify an FPGA clock on the block diagram.

Note

[IMAGE alt='icon' src='nifpga-palettemergevi-clocknameconstant-vi.png']

Parent topic:

Timed Structures

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/timedloop/timed-loop.html language=enus -->
## TOPIC 00315: Timed Loop

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/timedloop/timed-loop.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/timedloop/timed-loop.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The FPGA Module single-cycle Timed Loop differs from the standard LabVIEW Timed Loop in that the timing of the FPGA single-cycle Timed Loop corresponds exactly to the clock rate of the FPGA clock you specify. By configuring a single-cycle Timed Loop to use a clock other than the base clock of the FP

### Timed Loop

The FPGA Module single-cycle Timed Loop differs from the standard LabVIEW [Timed Loop](/csh?productcategories=147794&context=lvcore_glang_timed_loop) in that the timing of the FPGA single-cycle Timed Loop corresponds exactly to the clock rate of the FPGA clock you specify. By configuring a single-cycle Timed Loop to use a clock other than the base clock of the FPGA target, you can implement [multiple clock domains](/csh?context=lvfpga_lvfpgaconcepts_implementing_domains) in an FPGA VI. You can specify the FPGA clock that controls the single-cycle Timed Loop by wiring a value to the **Source Name** input on the Input Node of the single-cycle Timed Loop or by using the [Configure Timed Loop](/csh?productcategories=147794&context=lvcore_lvdialog_loop_configuration_db) dialog box.

You cannot use the following VIs, functions, or structures in a single-cycle Timed Loop.

Analog Period Measurement VI

Butterworth Filter VI

Discrete Delay VI

Divide function

FIFO Clear function

FPGA I/O Method Node except with some FPGA targets

FPGA I/O Property Node except with some FPGA targets

Interrupt VI

Look-Up Table 1D VI with the Interpolate data checkbox selected

Loop Timer Express VI

Multiple FPGA I/O Nodes configured for the same I/O resource if at least one node is inside the loop and at least one node is outside the loop

Non-reentrant subVIs if you use multiple instances

Notch Filter VI

PID VI

Quotient & Remainder function

Reciprocal function

Rotate 1D Array function

Sine Wave Generator VI

Single-precision floating-point operations

Square Root function

Timed Loop

Wait Express VI

Wait on Occurrence function

While Loop

The FPGA target you use might not support additional VIs or functions. Also, some targets do not support specific I/O items both inside and outside a single-cycle Timed Loop. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for more information.

The following table describes how single-cycle Timed Loops interact with other components.

| Single-Cycle Timed Loops Open in VIs under My Computer | If you place the single-cycle Timed Loop in a VI open under My Computer, the single-cycle Timed Loop displays some terminals that FPGA targets do not support. So, if you open the VI under an FPGA target, the unsupported terminals still appear. If you place the single-cycle Timed Loop in a VI open under an FPGA target, the single-cycle Timed Loop hides terminals that are not supported. So, if you open the VI under My Computer, the single-cycle Timed Loop does not display all terminals that My Computer supports. |
| --- | --- |
| Single-Cycle Timed Loops Open in VIs under an FPGA Target | When you place a single-cycle Timed Loop in an FPGA VI, only the Source Name input appears visible by default. Other than Source Name and Error, the inputs available on the Input Node of the single-cycle Timed Loop have no effect when you use the single-cycle Timed Loop in an FPGA VI. Error is the only supported output of the single-cycle Timed Loop in an FPGA VI. Note Do not add frames before or after the single-cycle Timed Loop frame to try to use the single-cycle Timed Loop as a Timed Sequence structure in an FPGA VI. The LabVIEW FPGA Module does not support Timed Sequence structures. |
| Indicators in Single-Cycle Timed Loops | You can place indicators in the single-cycle Timed Loop only if you do not have any local variables writing to the indicators. |
| FPGA I/O Nodes and Single-Cycle Timed Loops | You can use the FPGA I/O Node in the single-cycle Timed Loop if the FPGA target supports it. If the FPGA target you use supports the single-cycle Timed Loop, you can use only the Arbitrate if Multiple Requestors Only and Never Arbitrate arbitration options. If you select Arbitrate if Multiple Requestors Only, you cannot use more than one instance of the FPGA I/O Node for a specific I/O item in the FPGA VI. If you select Never Arbitrate, you can use more than one instance of the FPGA I/O Node for a specific I/O item in the FPGA VI if each instance is in a single-cycle Timed Loop executing at the same rate. |
| Flat Sequences and Single-Cycle Timed Loops | You can use the Flat Sequence or Stacked Sequence structure in the single-cycle Timed Loop. However, all sequence frames execute in one clock cycle. |
| SubVIs and Single-Cycle Timed Loops | You cannot use more than one instance of a non-reentrant or shared subVI in a single-cycle Timed Loop. You can use multiple instances of a reentrant VI inside a single-cycle Timed Loop as long as the reentrant VI does not use shared resources. |
| Wait On Occurrence Function and Single-Cycle Timed Loops | You cannot use the Wait on Occurrence function in a single-cycle Timed Loop. However, you can use the Set Occurrence function. You then can use the Wait on Occurrence function outside the single-cycle Timed Loop in a While Loop or For Loop. |
| One Clock Cycle Functions, Internal Registers, and Single-Cycle Timed Loops | You can use some functions in the single-cycle Timed Loop that take one clock cycle to execute, such as the Memory Method Node. If you use this function to read from a memory item that uses embedded block memory, the output of this function is not valid until the next iteration of the single-cycle Timed Loop. Therefore, you must wire the outputs of such functions directly to uninitialized shift registers. Note Functions such as the Memory Method Node, FFT Express VI, and FPGA I/O, have internal registers that can appear as paths in the Timing Violation Analysis window. |
| Arrays and Clusters in Single-Cycle Timed Loops | You can compile FPGA VIs with arrays and clusters wired to certain Numeric and Boolean functions inside the single-cycle Timed Loop. |
| For Loops in Single-Cycle Timed Loops | You can place a For Loop in a single-cycle Timed Loop if the For Loop contains only Array, Numeric, Boolean, or Comparison operations and uses only auto-indexed tunnels. Objects that generate or contain state, such as shift registers, Feedback Nodes, or VI calls, are not allowed in For Loops within a single-cycle Timed Loop. |
| Single-Precision Floating-Point (SGL) Data Type and Single-Cycle Timed Loops | Most functions cannot perform single-precision floating-point operations inside a single-cycle Timed Loop because they require more than one clock cycle to execute but they do not have handshaking signals. |

Parent topic:

Timed Structures

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/waveformprobe/waveform-watch-window/sampling-probe-watch-window.html language=enus -->
## TOPIC 00316: Sampling Probe Watch Window

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/waveformprobe/waveform-watch-window/sampling-probe-watch-window.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/waveformprobe/waveform-watch-window/sampling-probe-watch-window.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click a wire in a sampling source and select Sampling Probe»FPGA from the shortcut menu to display this window. In a host VI, you also can right-click a For Loop or While Loop border and select Mark as Probe Sampling Source to display this window. Use this window to manage sampling probes. Thi

### Sampling Probe Watch Window

Right-click a wire in a sampling source and select **Sampling Probe»FPGA** from the shortcut menu to display this window. In a host VI, you also can right-click a For Loop or While Loop border and select **Mark as Probe Sampling Source** to display this window.

Use this window to manage [sampling probes](/csh?context=lvfpga_lvcore_lvhowto_using_the_probe_tool).

This window includes the following components:

| Option | Description |
| --- | --- |
| Sampling Sources | Lists configured sampling sources. The waveform graph displays any sampling probes associated with the sampling signal you select. |
| Probe List | Displays all probes associated with the sampling source you select from the list of Sampling Sources. This list sorts probes in the order you create them. Probe(s)—Displays the probes in a tree diagram in the order you create them. Value—Displays the value of the probed wire at the cursor position. |
| Toolbar | Contains the following options: Remove Sampling Source—Removes the selected sampling source and all associated Sampling probes. If only one sampling source is available, Remove Sampling Source also closes the Waveform Probe Watch Window. Remove Selected Probe—Removes the selected probe. Pan—Picks up the plot and moves it around on the display. Zoom In—Zooms in on the point you click. Press and hold the <Shift> key to switch between Zoom In About Point and Zoom Out About Point. Zoom Out—Zooms out from the point you click. Press and hold the <Shift> key to switch between Zoom Out About Point and Zoom In About Point. X-Zoom—Zooms in on an area of the graph along the x-axis. Click a point you want to be the edge of the area and drag the cursor to select the area. Zoom To Fit—Autoscales all x-scales on the graph. You can use this option to clear any previous zooming actions. Previous Transition—Moves the cursor to the previous signal edge. Next Transition—Advances the cursor to the next signal edge. Add Clocks—Adds the timing source clock signal to the Probe List and displays the signal on the graph.This component is available only for Sampling probes with a single-cycle Timed Loop as the sampling source. Otherwise, LabVIEW dims this component. |
| Waveform Graph | Plots the probe signals in the Probe List. Each plot represents a different bit in the digital pattern. For For Loop and While Loop sampling sources, the graph plots the probe signals against iterations of the loop. Otherwise, the graph plots the signals over time in ns. |

Note

Note

Right-click the **Probe List** to display the shortcut menu. This menu contains additional options for customizing the **Probe List** view.

The following two options are available on the shortcut menu that appears when you right-click the data in the waveform graph subpanel of the **Sampling Probe Watch Window**.

- Copy Data —Copies the data for pasting to other controls in the same VI or other VIs. This option is also available on the shortcut menu that appears when you right-click a probe listed in the Sampling Probe Watch Window .
- Export —You can export data from the waveform graph and then import the data to the clipboard, Microsoft Excel, or DIAdem. 
 Note You must have Microsoft Excel installed to export data to Excel. You must have DIAdem installed to export data to DIAdem. Refer to the NI website atni.com/diadem to learn more about DIAdem and to download the latest version of DIAdem.

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/xilinkxip/xipin-dialog/clock-and-enable-signals-page-xilinx-ip-node-properties-dialog-box.html language=enus -->
## TOPIC 00317: Clock and Enable Signals Page (Xilinx IP Node Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/xilinkxip/xipin-dialog/clock-and-enable-signals-page-xilinx-ip-node-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/xilinkxip/xipin-dialog/clock-and-enable-signals-page-xilinx-ip-node-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page to specify the ports in the IP that behave as a clock or enable signal. Access this page by double-clicking a Xilinx IP node and using the configuration wizard that appears. If the node is on a supported target and is configured already, you can right-click the node and select Configur

### Clock and Enable Signals Page (Xilinx IP Node Properties Dialog Box)

Use this page to specify the ports in the IP that behave as a clock or enable signal.

Access this page by double-clicking a Xilinx IP node and using the configuration wizard that appears. If the node is on a supported target and is configured already, you can right-click the node and select Configure»Clock and Enable Signal(s) from the shortcut menu.

This page includes the following components:

| Option | Description |
| --- | --- |
| IP Clock Signal | Contains options relating to the clock signal(s) of the IP. Clock signal name—Specifies the port in the IP that corresponds to the single-cycle Timed Loop clock. If the IP does not contain this port, select No Clock from this pull-down list. In this situation, LabVIEW assumes the IP is combinatorial, that is, does not store its state at any time. You also cannot select a Derived multiple of single-cycle Timed Loop clock. Derived multiple of single-cycle Timed Loop clock—Specifies the port in the IP that corresponds to the derived clock enable signal. If the IP does not use a derived clock signal, select No Derived Clock from this pull-down list. Use this pull-down list and the Relative clock rate control to execute IP faster than the containing single-cycle Timed Loop. Relative clock rate— Specifies the rate multiple of the Derived multiple of single-cycle Timed Loop clock relative to the Clock signal name. Relative clock rate must be an integer. LabVIEW disregards this option if you set Derived multiple of single-cycle Timed Loop clock to No Derived Clock. For example, if the clock you specify in the Clock signal name pull-down list executes at 100 MHz and the clock you specify in the Derived multiple of single-cycle Timed Loop clock pull-down list executes at 400 MHz, set Relative clock rate to 4x. Note If the IP requires a derived clock rate that is not an integer multiple of the single-cycle Timed Loop clock, use CLIP to integrate the IP into the FPGA VI. |
| IP Enable Signal(s) | Specifies the IP port(s) LabVIEW uses to enable the IP. |
| Feedback | Displays warnings, errors, and configuration information. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/xilinkxip/xipin-dialog/configure-ip-page-xilinx-ip-node-properties-dialog-box.html language=enus -->
## TOPIC 00318: Configure IP Page (Xilinx IP Node Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/xilinkxip/xipin-dialog/configure-ip-page-xilinx-ip-node-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/xilinkxip/xipin-dialog/configure-ip-page-xilinx-ip-node-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page to view and change information about the IP. You also use this page to launch the Xilinx IP generator, which you use to configure the IP. Access this page by double-clicking a Xilinx IP node. If the node is on a supported target, you can right-click the node and select Configure»Config

### Configure IP Page (Xilinx IP Node Properties Dialog Box)

Use this page to view and change information about the IP. You also use this page to launch the Xilinx IP generator, which you use to configure the IP.

Access this page by double-clicking a Xilinx IP node. If the node is on a supported target, you can right-click the node and select **Configure»Configure IP** from the shortcut menu.

This page includes the following components:

| Option | Description |
| --- | --- |
| IP Name | Specifies the name of the IP. This name appears on the block diagram icon. Note Within a single FPGA VI, IP names must be unique. If more than one Xilinx IP node has the same name and you attempt to generate files, LabVIEW displays a warning to prevent you from overwriting the generated files of another IP. |
| Folder for Support Files | Specifies where LabVIEW saves the files generated by the Xilinx IP generator. Note If you move the FPGA VI that contains this node to another computer, you also must move the files in this folder. |
| Configure Xilinx IP | Launches the Xilinx IP generator, which you use to configure properties of the IP, view the data sheet of the IP, and generate the necessary files.(Xilinx Vivado) If the IP is migrated from a previous version of LabVIEW or moved from another target, the button name changes to Upgrade Xilinx IP. Click Upgrade Xilinx IP to upgrade the IP to work with the latest Xilinx compilation tools or to work on the new target. |
| IP Generation Progress | Displays the progress of the file generation that occurs after you click Configure Xilinx IP. |
| Feedback | Displays warnings, errors, and configuration information. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/xilinkxip/xipin-dialog/ip-terminals-page-xilinx-ip-node-properties-dialog-box.html language=enus -->
## TOPIC 00319: IP Terminals Page (Xilinx IP Node Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/xilinkxip/xipin-dialog/ip-terminals-page-xilinx-ip-node-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/xilinkxip/xipin-dialog/ip-terminals-page-xilinx-ip-node-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page to specify the names and data types of block diagram terminals that correspond to VHDL ports in the IP. Access this page by double-clicking a Xilinx IP node. If the node is on a supported target and is configured already, you can right-click the node and select Configure»IP Terminals f

### IP Terminals Page (Xilinx IP Node Properties Dialog Box)

Use this page to specify the names and data types of block diagram terminals that correspond to VHDL ports in the IP.

Access this page by double-clicking a Xilinx IP node. If the node is on a supported target and is configured already, you can right-click the node and select Configure»IP Terminals from the shortcut menu.

This page includes the following components:

| Option | Description |
| --- | --- |
| Terminals | Displays IP ports and how LabVIEW interprets these ports. Each port becomes an input or output terminal on the IP Integration Node. To configure these terminals, select a terminal in this table and then use the buttons in the other sections of this page. Note Neither the clock signal nor the asynchronous reset signal appear in this list of terminals. The IP Integration Node assumes all ports are synchronized to the rising edge of the single-cycle Timed Loop clock. |
| Terminal Order | Contains the buttons you use to control the order of the terminals. Move Up—Moves the selected terminal higher in the list. Move Down—Moves the selected terminal lower in the list. |
| Terminal Properties | Contains settings for the selected terminal. Data type—Specifies the data type of this terminal. Click this button to specify a data type. The valid data types are integer, fixed-point, single-precision floating-point, Boolean, and Boolean array. Fixed-point encoding—Specifies the fixed-point configuration of the terminal. This section applies only if you select Fixed-point as the Data type. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Integer word length—Specifies the integer word length of the selected terminal between [–2048, 2047]. This option is valid for fixed-point terminals only. LabVIEW sets the word length of the terminal to the width of the corresponding port as specified in the IP. Hide?—Specifies whether LabVIEW hides the selected terminal. If this terminal is an input, LabVIEW sets the value of the terminal to the Default value you specify. Default value (Hex)—Specifies the value, in hexadecimal, of a hidden terminal. This component is available only if the Direction of the selected terminal is IN and you place a checkmark in the Hide this terminal checkbox. |
| Feedback | Displays warnings, errors, and configuration information. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/xilinkxip/xipin-dialog/reset-signals-and-behavior-page-xilinx-ip-node-properties-dialog-box.html language=enus -->
## TOPIC 00320: Reset Signals and Behavior Page (Xilinx IP Node Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/xilinkxip/xipin-dialog/reset-signals-and-behavior-page-xilinx-ip-node-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/xilinkxip/xipin-dialog/reset-signals-and-behavior-page-xilinx-ip-node-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page to specify the ports in sequential IP that behave as asynchronous or synchronous reset signals. Access this page by double-clicking a Xilinx IP node. If the node is on a supported target and is configured already, you can right-click the node and select Configure»Reset Signals and Beha

### Reset Signals and Behavior Page (Xilinx IP Node Properties Dialog Box)

Use this page to specify the ports in sequential IP that behave as asynchronous or synchronous reset signals.

Access this page by double-clicking a Xilinx IP node. If the node is on a supported target and is configured already, you can right-click the node and select **Configure»Reset Signals and Behavior** from the shortcut menu.

This page includes the following components:

| Option | Description |
| --- | --- |
| Reset Signals | Contains options that relate to reset signals. Synchronous reset signal(s)—Specifies the port(s) in the IP that behave as synchronous reset signals. Asynchronous reset signal—Specifies the port in the IP that behaves as an asynchronous reset signal. If the IP does not contain this port, select No Asynchronous Reset from this pull-down list. Active logic level—Specifies the active logic level of the asynchronous reset signal. This option is available only when you specify an asynchronous reset signal for the IP. High—Specifies that the active logic level is high. Low—Specifies that the active logic level is low. sclr cycles—Specifies the number of clock cycles for which LabVIEW asserts the Synchronous reset signal(s) during a reset. If the IP has multiple synchronous reset signals that need different durations, enter the longest duration here. sclr cycles—Specifies the number of clock cycles for which LabVIEW asserts the Asynchronous reset signal during a reset. The clock is running within the reset duration.The value must be 0 for this IP to be used when the build specification is configured to allow the removal of implicit enable signals because the Asynchronous reset signal will assert and deassert before the clock starts running. The value must also be 0 if this clock is used with external clocks that might stop during reset. If an IP requires a running clock during asynchronous reset, such as for IP that use built-in FIFOs, and the design requires the removal of implicit enable signals, consider creating a local asynchronous reset, and prevent diagram access to or from the IP while this local reset is asserted. |
| Reset IP | Specifies the situation(s) in which LabVIEW resets the IP Integration Node. Before first call—Specifies that LabVIEW resets the IP Integration Node before the first call to the FPGA VI. Compile or load—Specifies that LabVIEW resets the IP only when the FPGA VI compiles or downloads to the FPGA. If you choose this option and the IP does not support asynchronous resets, the IP does not reset even if you invoke the Reset method. When the IP does reset, it might operate on garbage data, including metastable values. To mitigate these issues, ensure that your application does not depend on the values this IP returns immediately after resetting. |
| Feedback | Displays warnings, errors, and configuration information. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference
