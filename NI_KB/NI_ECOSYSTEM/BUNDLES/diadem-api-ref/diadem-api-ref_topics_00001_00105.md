# NI DOCUMENT BUNDLE: diadem-api-ref

<!--NI_BUNDLE_CHUNK bundle=diadem-api-ref start=1 end=105 -->
<!--NI_TOPIC bundle=diadem-api-ref path=comoff/textfileencoding.htm language=enus -->
## TOPIC 00001: Command: TextFileEncoding

- bundle_id: `diadem-api-ref`
- source_path: `comoff/textfileencoding.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/comoff/textfileencoding.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Command: TextFileEncoding

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();)  [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

### Command: TextFileEncoding

Specifies the character encoding of a file. The function uses the Byte Order Mark (BOM) of the file to specify the character encoding.

ReturnValue

#### Input Parameters

| FileName | Specifies the filename. String variable Note In many commands, you can use the wildcard * for any number of characters, and the wildcard ? for one character. |
| --- | --- |
| String variable |  |
|  | Note In many commands, you can use the wildcard * for any number of characters, and the wildcard ? for one character. |

#### Return Parameters

| ReturnValue | The return value is an Integer variable type. Contains the character encoding 4 eTextFileAttributeANSI Encoded in ANSI. 8 eTextFileAttributeUnicode Encoded in Unicode. 16 eTextFileAttributeUTF8 Encoded in UTF8. Examples The following example specifies the character encoding of a file: VBScriptPython Copy script Dim intMyEncode intMyEncode = TextFileEncoding(ScriptReadPath & "NewText.txt") Select Case intMyEncode Case eTextFileAttributeANSI Call MsgBoxDisp("ANSI") Case eTextFileAttributeUnicode Call MsgBoxDisp("Unicode") Case eTextFileAttributeUTF8 Call MsgBoxDisp("UTF8") Case Else Call MsgBoxDisp("Error occured") End Select Copy scriptintMyEncode = dd.TextFileEncoding(dd.ScriptReadPath + "NewText.txt") select_variable_0 = intMyEncode if (select_variable_0 == eTextFileAttributeANSI) : dd.MsgBoxDisp("ANSI") elif (select_variable_0 == eTextFileAttributeUnicode) : dd.MsgBoxDisp("Unicode") elif (select_variable_0 == eTextFileAttributeUTF8) : dd.MsgBoxDisp("UTF8") else: dd.MsgBoxDisp("Error occured") Related FunctionsCommand: TextFileEOL \| Function: FR \| Function: TextFileEOF \| Function: TextFileError \| Function: TextFileErrorTxt \| Function: TextFileSeek |  |
| --- | --- | --- |
| 4 | eTextFileAttributeANSI | Encoded in ANSI. |
| 8 | eTextFileAttributeUnicode | Encoded in Unicode. |
| 16 | eTextFileAttributeUTF8 | Encoded in UTF8. |
| VBScript | Python |  |

<!--NI_TOPIC bundle=diadem-api-ref path=comoff/textfileeol.htm language=enus -->
## TOPIC 00002: Command: TextFileEOL

- bundle_id: `diadem-api-ref`
- source_path: `comoff/textfileeol.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/comoff/textfileeol.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Command: TextFileEOL

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();)  [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

### Command: TextFileEOL

Specifies the end-of-line character of a text file. The function checks the end-of-line character of the first line. By transferring the end-of-line character to the [TextFileOpen](../comoff/textfileopen.htm) function, you can speed up the opening of a text file.

ReturnValue

TextFileAttribute

#### Input Parameters

| FileName | Specifies the filename. String variable Note In many commands, you can use the wildcard * for any number of characters, and the wildcard ? for one character. |  |
| --- | --- | --- |
| String variable |  |  |
|  | Note In many commands, you can use the wildcard * for any number of characters, and the wildcard ? for one character. |  |
| TextFileAttribute | Specifies how DIAdem creates or opens a text file. You can connect various attributes with logic operators. Integer variable -2147483648 <= TextFileAttribute <= 2147483647 0 eTextFileAttributeRead Opens a text file in read-only mode. 1 eTextFileAttributeWrite Opens a text file in read and write mode. When opening a file, DIAdem skips to the end of the file and appends the texts to be written. 4 eTextFileAttributeANSI Encodes a text file in ANSI. 8 eTextFileAttributeUnicode Encodes a text file in Unicode. 16 eTextFileAttributeUTF8 Encodes a text file in UTF8. This attribute is only available when the text file is read. 32 eTextFileAttributeWriteBuffer Opens a text file in write mode. When writing, DIAdem uses a buffer in order to accelerate the writing. The buffer increases the risk that not all data is saved on the hard disk if the program crashes. 32768 eTextFileAttributeCreate Generates a text file and overwrites any file of the same name in the specified folder without requesting confirmation. 1048576 eTextFileAttributeExclusive Opens a text file with exclusive read and write rights. 2097152 eTextFileAttributeDenyWrite Opens a text file as read-only. 4194304 eTextFileAttributeDenyRead Stops other applications from reading a text file at the same time as DIAdem. 8388608 eTextFileAttributeDenyNone Allows other applications to access a text file simultaneously with DIAdem. 16777216 eTextFileAttributenoAutoClose Specifies that DIAdem does not automatically close a text file at the end of a script. 33554432 eTextFileAttributeLogDIAdemMsg Specifies that DIAdem writes its Logfile into the specified text file. |  |
| Integer variable |  |  |
| -2147483648 <= TextFileAttribute <= 2147483647 |  |  |
| 0 | eTextFileAttributeRead | Opens a text file in read-only mode. |
| 1 | eTextFileAttributeWrite | Opens a text file in read and write mode. When opening a file, DIAdem skips to the end of the file and appends the texts to be written. |
| 4 | eTextFileAttributeANSI | Encodes a text file in ANSI. |
| 8 | eTextFileAttributeUnicode | Encodes a text file in Unicode. |
| 16 | eTextFileAttributeUTF8 | Encodes a text file in UTF8. This attribute is only available when the text file is read. |
| 32 | eTextFileAttributeWriteBuffer | Opens a text file in write mode. When writing, DIAdem uses a buffer in order to accelerate the writing. The buffer increases the risk that not all data is saved on the hard disk if the program crashes. |
| Opens a text file in write mode. When writing, DIAdem uses a buffer in order to accelerate the writing. The buffer increases the risk that not all data is saved on the hard disk if the program crashes. |  |  |
| 32768 | eTextFileAttributeCreate | Generates a text file and overwrites any file of the same name in the specified folder without requesting confirmation. |
| 1048576 | eTextFileAttributeExclusive | Opens a text file with exclusive read and write rights. |
| 2097152 | eTextFileAttributeDenyWrite | Opens a text file as read-only. |
| 4194304 | eTextFileAttributeDenyRead | Stops other applications from reading a text file at the same time as DIAdem. |
| 8388608 | eTextFileAttributeDenyNone | Allows other applications to access a text file simultaneously with DIAdem. |
| 16777216 | eTextFileAttributenoAutoClose | Specifies that DIAdem does not automatically close a text file at the end of a script. |
| 33554432 | eTextFileAttributeLogDIAdemMsg | Specifies that DIAdem writes its Logfile into the specified text file. |

#### Return Parameters

| ReturnValue | Specifies the line end character. TextFileLineEnd type return value. Enumeration variable Enumeration variable with the following selection terms Script Term Interface Term, Explanation "Auto" Automatic "CR" CR (carriage return) "LF" LF (line feed) "CRLF" CRLF (carriage return with line feed) "LFCR" LFCR (line feed with carriage return) |
| --- | --- |
| Enumeration variable |  |
| Enumeration variable with the following selection terms Script Term Interface Term, Explanation "Auto" Automatic "CR" CR (carriage return) "LF" LF (line feed) "CRLF" CRLF (carriage return with line feed) "LFCR" LFCR (line feed with carriage return) |  |
| Script Term | Interface Term, Explanation |
| "Auto" | Automatic |
| "CR" | CR (carriage return) |
| "LF" | LF (line feed) |
| "CRLF" | CRLF (carriage return with line feed) |
| "LFCR" | LFCR (line feed with carriage return) |

#### Examples

The following example specifies the end of line character of a file.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strFile, intLineCount, intMyHandle, strEOL, strMyText, intMyError
strFile = ScriptReadPath & "NewText.txt"
strEOL = TextFileEOL(strFile, eTextFileAttributeRead)
intMyHandle = TextFileOpen(strFile, eTextFileAttributeRead, strEOL)
intLineCount = 0
Do
  strMyText = TextFileReadLn(intMyHandle)
  If (Not IsNull(strMyText)) then
    intLineCount = intLineCount+1
    Call MsgBoxDisp(strMyText,"MB_OK")
  End If  
Loop until (IsNull(strMyText))
intMyError = TextFileClose(intMyHandle)
```

[Copy script](javascript:void(0);)

```text
strFile = dd.ScriptReadPath + "NewText.txt" 
strEOL = dd.TextFileEOL(strFile, eTextFileAttributeRead) 
intMyHandle = dd.TextFileOpen(strFile, eTextFileAttributeRead, strEOL) 
intLineCount = 0 
while True: 
    strMyText = dd.TextFileReadLn(intMyHandle) 
    if (not strMyText == None): 
        intLineCount = intLineCount+1 
        dd.MsgBoxDisp(strMyText,"MBOK") 
if (strMyText == None):
        break 
intMyError = dd.TextFileClose(intMyHandle) 
```

#### Related Functions

[Command: TextFileEncoding](../comoff/textfileencoding.htm) | [Function: FR](../functions/functions/fr.htm) | [Function: TextFileEOF](../functions/functions/textfileeof.htm) | [Function: TextFileError](../functions/functions/textfileerror.htm) | [Function: TextFileErrorTxt](../functions/functions/textfileerrortxt.htm) | [Function: TextFileSeek](../functions/functions/textfileseek.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=comoff/textfileopen.htm language=enus -->
## TOPIC 00003: Command: TextFileOpen

- bundle_id: `diadem-api-ref`
- source_path: `comoff/textfileopen.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/comoff/textfileopen.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Command: TextFileOpen

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();)  [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

### Command: TextFileOpen

Opens or creates a text file.

ReturnValue

TextFileAttribute

TextFileLineEnd

#### Input Parameters

| FileName | Specifies the file name. String variable Note In many commands, you can use the * wildcard for any number of characters, and the ? wildcard for one character. |  |
| --- | --- | --- |
| String variable |  |  |
|  | Note In many commands, you can use the * wildcard for any number of characters, and the ? wildcard for one character. |  |
| TextFileAttribute | Specifies how DIAdem creates or opens a text file. You can connect various attributes with logic operators. Integer variable -2147483648 <= TextFileAttribute <= 2147483647 0 eTextFileAttributeRead Opens a text file in read-only mode. 1 eTextFileAttributeWrite Opens a text file in read and write mode. When opening a file, DIAdem skips to the end of the file and appends the texts to be written. 4 eTextFileAttributeANSI Encodes a text file in ANSI. 8 eTextFileAttributeUnicode Encodes a text file in Unicode. 16 eTextFileAttributeUTF8 Encodes a text file in UTF8. This attribute is only available when the text file is read. 32 eTextFileAttributeWriteBuffer Opens a text file in write mode. When writing, DIAdem uses a buffer in order to accelerate the writing. The buffer increases the risk that not all data is saved on the hard disk if the program crashes. 32768 eTextFileAttributeCreate Generates a text file and overwrites any file of the same name in the specified folder without requesting confirmation. 1048576 eTextFileAttributeExclusive Opens a text file with exclusive read and write rights. 2097152 eTextFileAttributeDenyWrite Opens a text file as read-only. 4194304 eTextFileAttributeDenyRead Stops other applications from reading a text file at the same time as DIAdem. 8388608 eTextFileAttributeDenyNone Allows other applications to access a text file simultaneously with DIAdem. 16777216 eTextFileAttributenoAutoClose Specifies that DIAdem does not automatically close a text file at the end of a script. 33554432 eTextFileAttributeLogDIAdemMsg Specifies that DIAdem writes its Logfile into the specified text file. |  |
| Integer variable |  |  |
| -2147483648 <= TextFileAttribute <= 2147483647 |  |  |
| 0 | eTextFileAttributeRead | Opens a text file in read-only mode. |
| 1 | eTextFileAttributeWrite | Opens a text file in read and write mode. When opening a file, DIAdem skips to the end of the file and appends the texts to be written. |
| 4 | eTextFileAttributeANSI | Encodes a text file in ANSI. |
| 8 | eTextFileAttributeUnicode | Encodes a text file in Unicode. |
| 16 | eTextFileAttributeUTF8 | Encodes a text file in UTF8. This attribute is only available when the text file is read. |
| 32 | eTextFileAttributeWriteBuffer | Opens a text file in write mode. When writing, DIAdem uses a buffer in order to accelerate the writing. The buffer increases the risk that not all data is saved on the hard disk if the program crashes. |
| Opens a text file in write mode. When writing, DIAdem uses a buffer in order to accelerate the writing. The buffer increases the risk that not all data is saved on the hard disk if the program crashes. |  |  |
| 32768 | eTextFileAttributeCreate | Generates a text file and overwrites any file of the same name in the specified folder without requesting confirmation. |
| 1048576 | eTextFileAttributeExclusive | Opens a text file with exclusive read and write rights. |
| 2097152 | eTextFileAttributeDenyWrite | Opens a text file as read-only. |
| 4194304 | eTextFileAttributeDenyRead | Stops other applications from reading a text file at the same time as DIAdem. |
| 8388608 | eTextFileAttributeDenyNone | Allows other applications to access a text file simultaneously with DIAdem. |
| 16777216 | eTextFileAttributenoAutoClose | Specifies that DIAdem does not automatically close a text file at the end of a script. |
| 33554432 | eTextFileAttributeLogDIAdemMsg | Specifies that DIAdem writes its Logfile into the specified text file. |
| [TextFileLineEnd] | Specifies the line end character. Enumeration variable Enumeration variable with the following selection terms Script Term Interface Term, Explanation "Auto" Automatic "CR" CR (carriage return) "LF" LF (line feed) "CRLF" CRLF (carriage return with line feed) "LFCR" LFCR (line feed with carriage return) |  |
| Enumeration variable |  |  |
| Enumeration variable with the following selection terms Script Term Interface Term, Explanation "Auto" Automatic "CR" CR (carriage return) "LF" LF (line feed) "CRLF" CRLF (carriage return with line feed) "LFCR" LFCR (line feed with carriage return) |  |  |
| Script Term | Interface Term, Explanation |  |
| "Auto" | Automatic |  |
| "CR" | CR (carriage return) |  |
| "LF" | LF (line feed) |  |
| "CRLF" | CRLF (carriage return with line feed) |  |
| "LFCR" | LFCR (line feed with carriage return) |  |

#### Return Parameters

| ReturnValue | Contains the file handle as a numeric value. If an error occurs when the text file is being opened or created, the function returns the value -1. The return value is a TextFileHandle type. Integer variable -2147483648 <= TextFileHandle <= 2147483647 |
| --- | --- |
| Integer variable |  |
| -2147483648 <= TextFileHandle <= 2147483647 |  |

You can open a text file faster if you specify the character encoding with the [TextFileEOL](../comoff/textfileeol.htm) function and transfer it to the TextFileOpen function.

#### Examples

The following example creates a text file in ANSI code and writes twenty lines in this file. DIAdem saves the file in the DIAdem script folder.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim LineNo, intMyHandle, intMyText, intMyError 
intMyHandle = TextFileOpen(ScriptReadPath & "NewText.txt", eTextFileAttributeCreate OR eTextFileAttributeWrite OR eTextFileAttributeANSI) 
For LineNo = 1 To 20
  intMyText= TextfileWriteLn(intMyHandle, "Line " & LineNo)
Next
intMyError = TextFileClose(intMyHandle)
```

[Copy script](javascript:void(0);)

```text
intMyHandle = dd.TextFileOpen(dd.ScriptReadPath + "NewText.txt", eTextFileAttributeCreate or eTextFileAttributeWrite or eTextFileAttributeANSI) 
for LineNo in range( 1, 20 + 1): 
    intMyText= dd.TextfileWriteLn(intMyHandle, "Line " + LineNo) 
intMyError = dd.TextFileClose(intMyHandle) 
```

The following example reads a text file in ANSI code.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strFile, intLineCount, intMyHandle, strEOL, strMyText, intMyError
strFile = ScriptReadPath & "NewText.txt"
strEOL = TextFileEOL(strFile)
intMyHandle = TextFileOpen(strFile, eTextFileAttributeRead, strEOL)
intLineCount = 0
Do
  strMyText = TextFileReadLn(intMyHandle)
  If (Not IsNull(strMyText)) then
    intLineCount = intLineCount+1
    Call MsgBoxDisp(strMyText,"MB_OK")
  End If  
Loop until (IsNull(strMyText))
intMyError = TextFileClose(intMyHandle)
```

[Copy script](javascript:void(0);)

```text
strFile = dd.ScriptReadPath + "NewText.txt" 
strEOL = dd.TextFileEOL(strFile) 
intMyHandle = dd.TextFileOpen(strFile, eTextFileAttributeRead, strEOL) 
intLineCount = 0 
while True: 
    strMyText = dd.TextFileReadLn(intMyHandle) 
    if (not strMyText == None): 
        intLineCount = intLineCount+1 
        dd.MsgBoxDisp(strMyText,"MBOK") 
if (strMyText == None):
        break 
intMyError = dd.TextFileClose(intMyHandle) 
```

|  | Note If you open a file with the filename extension .Lst, DIAdem opens this file for the Serial evaluation. DIAdem automatically accesses the files that have the same name as the script file, but have the filename extension .Lst. Therefore, you must open this file with the TfDenyNone attribute. |
| --- | --- |

#### Related Topics

[Command: ExecuteExclusiveBegin](../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/abs.htm language=enus -->
## TOPIC 00004: Function: Abs

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/abs.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/abs.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Abs

### Function: Abs

Calculates the absolute value of a number.

```text
ReturnValue = Abs(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns positive numeric values. |
| --- | --- |

#### Examples

The following example calculates the absolute value of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Abs(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Abs(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/and.htm language=enus -->
## TOPIC 00005: Function: And

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/and.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/and.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: And

### Function: And

Calculates the And operation of two values.

```text
ReturnValue = Value1 And Value2
```

#### Parameters

| Value1 | Specifies a Boolean value, a Boolean variable, or a data channel. |
| --- | --- |
| Value2 | Specifies a Boolean value, a Boolean variable, or a data channel. |

#### Result

| ReturnValue | Returns Boolean values. Value1 Value2Result TRUEandTRUETRUE TRUEand1TRUE 23and17TRUE FALSEandTRUEFALSE FALSEandFALSEFALSE FALSEand0FALSE FALSEand-100 FALSE 0and00 0andTRUE0 0and230 |  |  |
| --- | --- | --- | --- |
| Value1 |  | Value2 | Result |
| TRUE | and | TRUE | TRUE |
| TRUE | and | 1 | TRUE |
| 23 | and | 17 | TRUE |
| FALSE | and | TRUE | FALSE |
| FALSE | and | FALSE | FALSE |
| FALSE | and | 0 | FALSE |
| FALSE | and | -100 | FALSE |
| 0 | and | 0 | 0 |
| 0 | and | TRUE | 0 |
| 0 | and | 23 | 0 |

#### Examples

The following example checks rowwise whether the two data channels contain values. If both data channels have a value in the same row, the result in the new channel Group2/Result is the value 1, and if either of the two data channels has the value 0 in the same row, the result is the value 0.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= (Ch(""Group1/Input""))And(Ch(""Group1/Reference""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= (Ch(""Group1/Input""))and(Ch(""Group1/Reference""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note If you use the And function without the Calculate command in your script, DIAdem uses the VBS operator And, which compares two integer values bitwise. |
| --- | --- |

|  | The first and the second physical quantity must be the same. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: CTNV](../../comoff/ctnv.htm) | [Function: IIf](../../comoff/iif.htm) | [Function: NOT](../functions/not.htm) | [Function: OR](../functions/or.htm) | [Function: VIT](../functions/vit.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/andb.htm language=enus -->
## TOPIC 00006: Function: AndB

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/andb.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/andb.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: AndB

### Function: AndB

Calculates the number that results from the identical bits of two numbers. The AndB function converts the decimal numbers into binary numbers, determines the identical bits, and reconverts this binary number into a decimal number.

```text
ReturnValue = AndB(Value1, Value2)
```

#### Input Parameters

| Value1 | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |
| Value2 | Specifies a numeric value, a variable, or a data channel. |

|  | Note If you specify numbers with decimal places for the parameters Value1 and Value2, DIAdem rounds the numbers to integers. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. If two numbers contain no identical bits, the function returns the result 0. If the input value is NoValue, the AndB function returns the value NoValue. |
| --- | --- |

#### Examples

The following example calculates the identical bits of the two decimal numbers 10 and 12 and saves the corresponding decimal number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = AndB(10,12)   'intMyResult = 8
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.AndB(10,12) #intMyResult = 8
```

The following example calculates the identical bits of the values in each line of two data channels, and saves the decimal numbers in the new data channel Group2/Result.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= AndB (Ch(""Group1/Input""),Ch(""Group1/Reference""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= AndB (Ch(""Group1/Input""),Ch(""Group1/Reference""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note You also can use VBS function And to calculate the identical bits of two numbers. |
| --- | --- |

|  | The first and the second physical quantity must be the same. The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ClrB](../functions/clrb.htm) | [Function: GetB](../functions/getb.htm) | [Function: NotB](../functions/notb.htm) | [Function: OrB](../functions/orb.htm) | [Function: SetB](../functions/setb.htm) | [Function: ShL](../functions/shl.htm) | [Function: ShR](../functions/shr.htm) | [Function: XOrB](../functions/xorb.htm) | [Variable: ApplicationLegacyBinaryOperations](/csh?topicname=varoff/applicationlegacybinaryoperations.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/arccos.htm language=enus -->
## TOPIC 00007: Function: ArcCos

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/arccos.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/arccos.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ArcCos

### Function: ArcCos

Valid names: ArcCos, ACos

Calculates the arc cosine of a number.

```text
ReturnValue = ArcCos(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel that contains the cosine values.Value range from -1 to +1. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns an angle in radians from 0 to Pi. |
| --- | --- |

#### Examples

The following example calculates from the arc cosine of a number the corresponding angle value in degrees.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = Deg(ACos(-0.9143))    'dblMyResult = 156.10651
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.Deg(dd.ACos(-0.9143)) #dblMyResult = 156.10651
```

The following example calculates the arc cosine of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= ACos(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= ACos(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must be dimensionless. The result quantity has the physical quantity Plane angle.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/arccot.htm language=enus -->
## TOPIC 00008: Function: ArcCot

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/arccot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/arccot.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ArcCot

### Function: ArcCot

Valid names: ArcCot, ACot

Calculates the arccotangent of a number.

```text
ReturnValue = ArcTan(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel that contains the cotangent values. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns an angle in radians from -Pi/2 to Pi/2. |
| --- | --- |

#### Examples

The following example calculates the arccotangent of a number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = ACot(1.9143)    'dblMyResult = 0.481394161422127
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.ACot(1.9143) #dblMyResult = 0.481394161422127
```

The following example calculates the arc tangent of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= ACot(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= ACot(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must be dimensionless. The result quantity has the physical quantity Plane angle.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/arcsin.htm language=enus -->
## TOPIC 00009: Function: ArcSin

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/arcsin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/arcsin.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ArcSin

### Function: ArcSin

Valid names: ArcSin, ASin

Calculates the arc sine of a number.

```text
ReturnValue = ArcSin(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel that contains the sine values.Value range from -1 to +1. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns an angle in radians from -Pi/2 to Pi/2. |
| --- | --- |

#### Examples

The following example calculates the corresponding angle value in degrees from the arc sine of a number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = Deg(ASin(0.9143))    'dblMyResult = 66.1065125606145
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.Deg(dd.ASin(0.9143)) #dblMyResult = 66.1065125606145
```

The following example calculates the arc sine of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= ASin(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= ASin(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must be dimensionless. The result quantity has the physical quantity Plane angle.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/arctan.htm language=enus -->
## TOPIC 00010: Function: ArcTan

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/arctan.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/arctan.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ArcTan

### Function: ArcTan

Valid names: ArcTan, ATan

Calculates the arc tangent of a number.

```text
ReturnValue = ArcTan(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel that contains the tangent values. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns an angle in radians from -Pi/2 to Pi/2. |
| --- | --- |

#### Examples

The following example calculates the arc tangent of a number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = ATan(1.9143)    'dblMyResult = 1.0894
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.ATan(1.9143) #dblMyResult = 1.0894
```

The following example calculates the arc tangent of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= ATan(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= ATan(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note You also can use the VBS function Atn to calculate the arc tangent of a number. |
| --- | --- |

|  | The input quantity must be dimensionless. The result quantity has the physical quantity Plane angle.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/arctanh.htm language=enus -->
## TOPIC 00011: Function: ArcTanH

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/arctanh.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/arctanh.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ArcTanH

### Function: ArcTanH

Valid names: ArcTanH, ATanH

Calculates the hyperbolic arcustangens of a number.

```text
ReturnValue = ArcTanH(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel.Value range from -1 to +1. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns numeric values. |
| --- | --- |

#### Examples

The following example calculates the hyperbolic arc tangent of a number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = ATanH(0.9143)    'dblMyResult = 1.5531
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.ATanH(0.9143) #dblMyResult = 1.5531
```

The following example calculates the hyperbolic arc tangent of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= ATanH(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= ATanH(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must be dimensionless. The physical result quantity is also dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/atan2.htm language=enus -->
## TOPIC 00012: Function: ATan2

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/atan2.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/atan2.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ATan2

### Function: ATan2

Calculates the arc tangent from two numbers. Specify the adjacent leg and the opposite leg to assign the result to any of the four quadrants and handle 0°, 90°, and 270°, which are special cases.

```text
ReturnValue = ATan2(Opposite, Adjacent)
```

#### Input Parameters

| Opposite | Specifies a numeric value, a variable, or a data channel that contains the opposite leg. |
| --- | --- |
| Adjacent | Specifies a numeric value, a variable, or a data channel that contains the adjacent leg. |

#### Return Parameters

| ReturnValue | Returns an angle in radians from -Pi to Pi. |
| --- | --- |

#### Examples

The following example calculates the arc tangent of two numbers.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = ATan2(12.9143,17.209)    'dblMyResult = 0.64378
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.ATan2(12.9143,17.209) #dblMyResult = 0.64378
```

The following example calculates the arc tangent of the values in the data channels Group1/Input and Group1/Input2 and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= ATan2(Ch(""Group1/Input""),Ch(""Group1/Input2""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= ATan2(Ch(""Group1/Input""),Ch(""Group1/Input2""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The first and second physical input quantity must be the same. The result quantity has the physical quantity Plane angle.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/atank.htm language=enus -->
## TOPIC 00013: Function: ATanK

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/atank.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/atank.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ATanK

### Function: ATanK

Possible spellings: ATanK, ATK

Calculates the arc tangent from two numbers. Specify the adjacent leg and the opposite leg to assign the result to any of the four quadrants and handle 0°, 90°, and 270°, which are special cases.

```text
ReturnValue = ATanK(Opposite, Adjacent)
```

#### Input Parameters

| Opposite | Specifies a numeric value, a variable, or a data channel that contains the opposite leg. |
| --- | --- |
| Adjacent | Specifies a numeric value, a variable, or a data channel that contains the adjacent leg. |

#### Return Parameters

| ReturnValue | Returns an angle in radians from 0 to 2*Pi. |
| --- | --- |

#### Examples

The following example calculates the arc tangent of two numbers.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = ATanK(12.9143,17.209)    'dblMyResult = 0.64378
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.ATanK(12.9143,17.209) #dblMyResult = 0.64378
```

The following example calculates the arc tangent of the values in the data channels Group1/Input and Group1/Input2 and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= ATanK(Ch(""Group1/Input""),Ch(""Group1/Input2""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= ATanK(Ch(""Group1/Input""),Ch(""Group1/Input2""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The first and second physical input quantity must be the same. The result quantity has the physical quantity Plane angle.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/calc_functions_units.htm language=enus -->
## TOPIC 00014: Input and Result Quantities in Quantity-Sized Calculations

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/calc_functions_units.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/calc_functions_units.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > Input and Result Quantities in Quantity-Sized Calculations

### Input and Result Quantities in Quantity-Sized Calculations

To calculate quantity-based in DIAdem, click the **Calculate Quantity-Based** button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the selected [physical quantities](/csh?topicname=genshell/genshell/genunitcatalog_basics.htm) can be used in the same calculation. If DIAdem cannot execute the calculation due to inappropriate physical quantities, DIAdem displays an error message. Refer to the Help page [Calculating Quantity-Based and Non-Quantity-Based in DIAdem](/csh?topicname=genshell/genshell/calc_unitbased.htm) for the conditions and rules for quantity-based calculations.

Additional rules apply for the Calculator and the Calculate command. Refer to the Help page of the [Calculate](../../comoff/calculate.htm) command for further information.

Some functions need dimensionless input quantities or return dimensionless result quantities. These physical quantities all have the exponent 0 for all base units. 1, %, and dB are examples of dimensionless physical sizes. If you do not specify a result quantity, DIAdem uses the unit 1 as the result unit for these functions.

For most VBS functions the physical input quantity is arbitrary and the physical result quantity dimensionless. The following functions however need a special physical input quantity or return special physical result quantities:

#### Numeric Functions

| +, -, Abs, Frac, MaxV, MinV, Random, Rnd, Round, Trunc, | The physical input quantities and the result quantities are the same. |
| --- | --- |
| *, -, ^, Sqr, Sqrt | DIAdem specifies the physical result quantity with the physical dimensions of the input quantities. |
| Exp, Eex, Fak, Lg, Ln, Log, | The input quantity must be dimensionless. The physical result quantity is also dimensionless. |
| Mod | The first physical input quantity is arbitrary. The second input quantity must be dimensionless. The first physical input quantity and the result quantity are the same. |
| Sign, SND, Rtp, Rtt | The physical input quantity is arbitrary. The physical result quantity is dimensionless. |

#### Trigonometric Functions

| ArcCos, ArcCot, ArcSin, ArcTan, | The input quantity must be dimensionless. The result quantity has the physical quantity Plane angle. |
| --- | --- |
| ArcTanH, Cos | The input quantity must be dimensionless. The physical result quantity is also dimensionless. |
| ATanK | The first and second physical input quantity must be the same. The result quantity has the physical quantity Plane angle. |
| Deg | The input quantity must have the unit rad. The result quantity has the physical quantity Plane angle. |
| Rad | The input quantity must have the unit deg. The result quantity has the physical quantity Plane angle. |
| Cos, CosH, Cot, Sin, SinH, Tan, TanH | The input quantity must have the physical quantity Plane angle. The physical result quantity is dimensionless. |

#### Boolean Functions

| AND, NOT, OR, =, >, >=, <, <=, <> | The first and the second physical quantity must be the same. The physical result quantity is dimensionless. |
| --- | --- |

#### Bit Functions

| AndB, OrB, XorB | The first and the second physical quantity must be the same. The physical input quantities and the result quantities are the same. |
| --- | --- |
| ClrB, GetB, NotB, SetB, ShL, ShR, | The first physical input quantity is arbitrary. The second input quantity must be dimensionless. The first physical input quantity and the result quantity are the same. |

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/cch.htm language=enus -->
## TOPIC 00015: Function: CCh

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/cch.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/cch.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: CCh

### Function: CCh

Calculates the characteristic values of a data channel.

```text
ReturnValue = CCh(Channel,StatValueIndex)
```

#### Input Parameters

| ChannelName | Specifies the data channel. |
| --- | --- |
| StatValueIndex | Specifies the index of the characteristic value to be calculated. |
| Index Characteristic value 0 Mean value 1 Minimum 2 Maximum 3 Range 4 Total |  |
| Index | Characteristic value |
| 0 | Mean value |
| 1 | Minimum |
| 2 | Maximum |
| 3 | Range |
| 4 | Total |

#### Return Parameters

| ReturnValue | Returns characteristic values of a data channel. |
| --- | --- |

#### Examples

The following example determines the maximum value of the Group1/Input data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = CCh("Group1/Input",2)
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.CCh("Group1/Input",2) 
```

|  | Note Refer to Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

#### Related Functions

[Command: ChnFind](../../comoff/chnfind.htm) | [Command: ChnFindReverse](../../comoff/chnfindreverse.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: Find](../functions/find.htm) | [Function: FindReverse](../functions/findreverse.htm) | [Function: PNo](../functions/pno.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/ceil.htm language=enus -->
## TOPIC 00016: Function: Ceil

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/ceil.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/ceil.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > [Numeric Functions](../functions/functions_num_overview.htm) > Function: Ceil

### Function: Ceil

Specifies the integer part of a number, where the function rounds up the transferred value to obtain an integer number. For negative numbers the function returns integer numbers that are greater than or equal to the Value argument.

```text
ReturnValue = Ceil(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. |
| --- | --- |

#### Examples

The following example rounds up some values:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBox(Ceil(2.6))  '=> 3
Call MsgBox(Ceil(2.1))  '=> 3
Call MsgBox(Ceil(-2.1)) '=> -2
Call MsgBox(Ceil(-2.6)) '=> -2
```

[Copy script](javascript:void(0);)

```text
print(dd.Ceil(2.6)) #=> 3
print(dd.Ceil(2.1)) #=> 3
print(dd.Ceil(-2.1)) #=> -2
print(dd.Ceil(-2.6)) #=> -2
```

The following example rounds up the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Ceil (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Ceil (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Topics

[Floor](../functions/floor.htm) | [Int](/csh?topicname=vbs/methods/vbs_method_int_globalobj.htm) | [Round](../functions/round.htm) | [Trunc](../functions/trunc.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/char.htm language=enus -->
## TOPIC 00017: Function: Char

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/char.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/char.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Char

### Function: Char

Determines the character that corresponds to the entered ASCII code.

```text
ReturnValue = Char(ASCIIcode)
```

#### Input Parameters

| ASCIIcode | Specifies an integer value.Value range from 1 to 255. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns a text character. |
| --- | --- |

#### Examples

The following example determines the character that corresponds to the ASCII code 65.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strMyResult
strMyResult = Char(65)    'strMyResult = A
```

[Copy script](javascript:void(0);)

```text
strMyResult = Char(65) #strMyResult = A
```

#### Related Functions

[Command: TTD](../../comoff/ttd.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: FileNameSplit](../functions/namesplit.htm) | [Function: Idx](../functions/idx.htm) | [Function: Len](../functions/len.htm) | [Function: PU](../functions/pu.htm) | [Function: Str](../functions/str.htm) | [Function: Textaddition (+)](../functions/tadd.htm) | [Function: TTR (Text to Real)](../functions/ttr.htm) | [Function: Val](../functions/val.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/clrb.htm language=enus -->
## TOPIC 00018: Function: ClrB

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/clrb.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/clrb.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ClrB

### Function: ClrB

Deletes a specific bit from the binary display of a decimal number. The ClrB function converts a decimal number to a binary number, deletes the specified bit, and reconverts the new binary number to a decimal number.

```text
ReturnValue = ClrB(Value, BitIndex)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |
| BitIndex | Specifies a numeric value, a variable, or a data channel for the index of the bit you want to delete. Value range 0 to 31 |

|  | Note If you enter numbers with decimal places for the values Value and Index, DIAdem rounds the numbers to integers. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. If the specified bit already has the value 0, its value remains 0. If the input value is NoValue, the ClrB function returns the value NoValue. |
| --- | --- |

#### Examples

The following example deletes the second bit of the binary display of the decimal number 10.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = ClrB(10,1)    'intMyResult = 8
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.ClrB(10,1) #intMyResult = 8
```

The following example deletes the bits indexed by the Group1/Reference data channel from the values in the Group1/Input data channel, and saves the new decimal numbers in the new data channel Group2/Result. DIAdem skips values of the Group1/Reference index channel that are higher than 31.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= ClrB (Ch(""Group1/Input""),Ch(""Group1/Reference""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= ClrB (Ch(""Group1/Input""),Ch(""Group1/Reference""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The first physical input quantity is arbitrary. The second input quantity must be dimensionless. The first physical input quantity and the result quantity are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: AndB](../functions/andb.htm) | [Function: GetB](../functions/getb.htm) | [Function: NotB](../functions/notb.htm) | [Function: OrB](../functions/orb.htm) | [Function: SetB](../functions/setb.htm) | [Function: ShL](../functions/shl.htm) | [Function: ShR](../functions/shr.htm) | [Function: XOrB](../functions/xorb.htm) | [Variable: ApplicationLegacyBinaryOperations](/csh?topicname=varoff/applicationlegacybinaryoperations.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/cos.htm language=enus -->
## TOPIC 00019: Function: Cos

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/cos.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/cos.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Cos

### Function: Cos

Calculates the cosine of a number.

```text
ReturnValue = Cos(Value) 
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel that contains the angles in radians. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns numeric values ranging from -1 to +1. |
| --- | --- |

#### Examples

The following example calculates the cosine of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Cos(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Cos(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must be dimensionless. The physical result quantity is also dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/cosh.htm language=enus -->
## TOPIC 00020: Function: CosH

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/cosh.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/cosh.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: CosH

### Function: CosH

Calculates the hyperbolic cosine of a number.

```text
ReturnValue = CosH(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel that contains the angles in radians. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns numeric values. |
| --- | --- |

#### Examples

The following example calculates the hyperbolic cosine of a number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = CosH(1.9143)    'dblMyResult = 3.46482
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.CosH(1.9143) #dblMyResult = 3.46482
```

The following example calculates the hyperbolic cosine of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= CosH(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= CosH(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must have the physical quantity Plane angle. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/cot.htm language=enus -->
## TOPIC 00021: Function: Cot

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/cot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/cot.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Cot

### Function: Cot

Calculates the cotangent of a number.

```text
ReturnValue = Cot(Value) 
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel that contains the angles in radians. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns numeric values. |
| --- | --- |

#### Examples

The following example calculates the cotangent of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Cot(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Cot(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must have the physical quantity Plane angle. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/datafilesize.htm language=enus -->
## TOPIC 00022: Function: DataFileSize

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/datafilesize.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/datafilesize.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: DataFileSize

### Function: DataFileSize

Determines the size in bytes of a DIAdem file that is a .tdm, .tdms, or .dat type and the associated binary files that contain the bulk data.

```text
ReturnValue = DataFileSize(FileName)
```

#### Input Parameters

| FileName | Specifies a filename with path and extension.In the filename and extension, you can use ? as a wildcard for a single character and * for several characters.If you do not specify a path, DIAdem searches for the file in the DIAdem folder. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns an integer value. If DIAdem cannot uniquely determine or find the file, the function returns the value 0. |
| --- | --- |

#### Examples

The following example determines the size of a TDM file and the associated binary file.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = DataFileSize(DataReadPath & "Drive.tdm")
intMyResult = DataFileSize(ProgramDrv & "Example\Data\Course.tdm")
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.DataFileSize(dd.DataReadPath + "Drive.tdm") 
intMyResult = dd.DataFileSize(dd.ProgramDrv + "Example\\Data\\Course.tdm") 
```

#### Related Functions

[Command: ChnValExpand](../../comoff/chnvalexpand.htm) | [Command: DataFileCopy](../../comoff/datafilecopy.htm) | [Command: DataFileDelete](../../comoff/datafiledelete.htm) | [Command: DataFileLoad](../../comoff/datafileload.htm) | [Command: DataFileLoadRed](../../comoff/datafileloadred.htm) | [Command: DataFileLoadSel](../../comoff/datafileloadsel.htm) | [Command: DataFileLstGet](../../comoff/datafilelstget.htm) | [Command: DataFileMove](../../comoff/datafilemove.htm) | [Command: DataFileRename](../../comoff/datafilerename.htm) | [Command: DataFileSave](../../comoff/datafilesave.htm) | [Command: DataFileSaveSel](../../comoff/datafilesavesel.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: FileDlgShow](../../comoff/filedlgshow.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: PathDlgShow](../../comoff/pathdlgshow.htm) | [Commands and Variables for Working with Data](../../cmdvarlist/cmdvarlist/cmdlist_data.htm) | [Commands and Variables for Working with Files and Folders](../../cmdvarlist/cmdvarlist/cmdlist_files.htm) | [DIAdem Library Paths](../../cmdvarlist/cmdvarlist/cmdlist_librarypath.htm) | [DIAdem Path Variables](../../cmdvarlist/cmdvarlist/cmdlist_path.htm) | [DIAdem User Paths](../../cmdvarlist/cmdvarlist/cmdlist_userpath.htm) | [Function: FileAttrCheck](../functions/fileattrcheck.htm) | [Function: FileDateGet](../functions/filedateget.htm) | [Function: FileSize](../functions/filesize.htm) | [Function: FilEx](../functions/filex.htm) | [Function: FolderAttrCheck](../functions/folderattrcheck.htm) | [Function: FolderDateGet](../functions/folderdateget.htm) | [Function: FolderExist](../functions/folderexist.htm) | [Function: FolderSize](../functions/foldersize.htm) | [Variable: FileExportFilter](/csh?topicname=varoff/fileexportfilter.htm) | [Variable: FileFilter](/csh?topicname=varoff/filefilter.htm) | [Variable: FileImportFilter](/csh?topicname=varoff/fileimportfilter.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/deg.htm language=enus -->
## TOPIC 00023: Function: Deg

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/deg.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/deg.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Deg

### Function: Deg

Converts an angle from radians to degrees.

```text
ReturnValue = Deg(Angle) 
```

#### Input Parameters

| Angle | Specifies a numeric value or a variable in radians, or a data channel that contains radians. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns angles in degrees. |
| --- | --- |

#### Examples

The following example converts the value Pi/3 to its angle value.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = Deg(Pi/3)    'intMyResult = 60
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.Deg(Pi/3) #intMyResult = 60
```

The following example converts the values in the Group1/Input data channel from radians into degrees and saves the results in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Deg (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Deg (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note Use the Rad function to convert angle values from degree to radians. |
| --- | --- |

|  | The input quantity must have the unit rad. The result quantity has the physical quantity Plane angle.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/eex.htm language=enus -->
## TOPIC 00024: Function: Eex

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/eex.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/eex.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Eex

### Function: Eex

Exponentiates a number to the base 10.

```text
ReturnValue = Eex(Exponent) 
```

#### Input Parameters

| Exponent | Specifies a numeric value or a variable as an exponent, or a data channel that contains exponents. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns positive values. |
| --- | --- |

#### Examples

The following example calculates the third power of 10.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = Eex(3)    'intMyResult = 1000
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.Eex(3) #intMyResult = 1000
```

The following example exponentiates the values of the Group1/Input data channel to the base 10 and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Eex (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Eex (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must be dimensionless. The physical result quantity is also dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/exp.htm language=enus -->
## TOPIC 00025: Function: Exp

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/exp.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/exp.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Exp

### Function: Exp

Exponentiates a number to the base e (Euler number).

```text
ReturnValue = Exp(Exponent)
```

#### Input Parameters

| Exponent | Specifies a numeric value or a variable as an exponent, or a data channel that contains exponents. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns positive values. |
| --- | --- |

#### Examples

The following example exponentiates the values of the Group1/Input data channel to the base e (Euler number) and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Exp (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Exp (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note DIAdem only uses the DIAdem function Exp if you use the FormulaCalc command otherwise DIAdem uses the VBS function Exp. |
| --- | --- |

|  | The input quantity must be dimensionless. The physical result quantity is also dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/fak.htm language=enus -->
## TOPIC 00026: Function: Fak

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/fak.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/fak.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Fak

### Function: Fak

Calculates the factorial of a number.

```text
ReturnValue = Fak(Value)
```

#### Input Parameters

| Value | Specifies an integer value, a variable, or a data channel that contains integer values. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. |
| --- | --- |

#### Examples

The following example calculates the factorial of the number 6.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = Fak(6)    'intMyResult = 720
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.Fak(6) #intMyResult = 720
```

The following example calculates the factorial of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Fak (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Fak (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must be dimensionless. The physical result quantity is also dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/fcno.htm language=enus -->
## TOPIC 00027: Function: FCNo

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/fcno.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/fcno.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FCNo

### Function: FCNo

Determines the number of a channel from an external file header in a [DAT file](/csh?topicname=header/header/headerdse_allgemein.htm).

```text
ReturnValue = FCNo(ChnName, [ChannelStart]) 
```

#### Input Parameters

| ChnName | Specifies a channel name. |
| --- | --- |
| [ChannelName] | Specifies the channel number where DIAdem starts searching for the channel in the file header. |

#### Return Parameters

| ReturnValue | Returns the channel number of the channel you want. If DIAdem does not find a channel with the given name, the FCNo function delivers the value 0. |
| --- | --- |

|  | Note To use the FCNo function, you must register the external file header. Use the HDLoad command to register external file headers in a script. Select File»DAT Files»Import via Header in DIAdem NAVIGATOR to open an overview of the external file headers in your computer. You can load, save, generate, and edit external file headers in this dialog box. |
| --- | --- |

#### Examples

The following example uses the HdLoad command to load the Auto1.dat file header, which contains the data channels Time, Deviation, Frequency, and Amplitude. The FCNo function determines the channel number of the Frequency data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
Call HdLoad ("Auto1.dat")
intMyResult = FCNo("Frequency")    'intMyResult = 3
intMyResult = FCNo("Frequency",4)  'intMyResult = 0
```

[Copy script](javascript:void(0);)

```text
dd.HdLoad ("Auto1.dat") 
intMyResult = dd.FCNo("Frequency") #intMyResult = 3
intMyResult = dd.FCNo("Frequency",4) #intMyResult = 0
```

#### Related Functions

[Command: ChnFind](../../comoff/chnfind.htm) | [Command: ChnFindReverse](../../comoff/chnfindreverse.htm) | [Function: CCh](../functions/cch.htm) | [Function: Find](../functions/find.htm) | [Function: FindReverse](../functions/findreverse.htm) | [Function: PNo](../functions/pno.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/fileattrcheck.htm language=enus -->
## TOPIC 00028: Function: FileAttrCheck

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/fileattrcheck.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/fileattrcheck.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FileAttrCheck

### Function: FileAttrCheck

Checks the attributes of a file.

```text
ReturnValue = FileAttrCheck(FileName, Attribute) 
```

#### Input Parameters

| FileName | Specifies a file with path and extension.In the filename and extension, you can use ? as a wildcard for a single character and * for several characters.If you do not specify a path, DIAdem searches for the file in the DIAdem folder. |
| --- | --- |
| Attributes | Specifies the attribute to be checked. |
| Value Meaning "faReadOnly" The file is write-protected. "faArchive" The file has been modified. "faHidden" The file is hidden. "faSystem" The file is a system file for the operating system. "faOffline" The file has been moved from an archiving system to an offline memory. |  |
| Value | Meaning |
| "faReadOnly" | The file is write-protected. |
| "faArchive" | The file has been modified. |
| "faHidden" | The file is hidden. |
| "faSystem" | The file is a system file for the operating system. |
| "faOffline" | The file has been moved from an archiving system to an offline memory. |

#### Return Parameters

| ReturnValue | Returns a Boolean value. If DIAdem does not find the given file, the function returns the result FALSE. |
| --- | --- |

#### Examples

The following example checks whether the report file Example.dat in the library folder is write-protected.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim blnMyResult
blnMyResult = FileAttrCheck(LayoutLibrPath & "Example.tdr","faReadOnly")
```

[Copy script](javascript:void(0);)

```text
blnMyResult = dd.FileAttrCheck(dd.LayoutLibrPath + "Example.tdr","faReadOnly") 
```

#### Related Functions

[Command: ChnValExpand](../../comoff/chnvalexpand.htm) | [Command: DataFileCopy](../../comoff/datafilecopy.htm) | [Command: DataFileDelete](../../comoff/datafiledelete.htm) | [Command: DataFileLoad](../../comoff/datafileload.htm) | [Command: DataFileLoadRed](../../comoff/datafileloadred.htm) | [Command: DataFileLoadSel](../../comoff/datafileloadsel.htm) | [Command: DataFileLstGet](../../comoff/datafilelstget.htm) | [Command: DataFileMove](../../comoff/datafilemove.htm) | [Command: DataFileRename](../../comoff/datafilerename.htm) | [Command: DataFileSave](../../comoff/datafilesave.htm) | [Command: DataFileSaveSel](../../comoff/datafilesavesel.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: FileDlgShow](../../comoff/filedlgshow.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: PathDlgShow](../../comoff/pathdlgshow.htm) | [Commands and Variables for Working with Data](../../cmdvarlist/cmdvarlist/cmdlist_data.htm) | [Commands and Variables for Working with Files and Folders](../../cmdvarlist/cmdvarlist/cmdlist_files.htm) | [DIAdem Library Paths](../../cmdvarlist/cmdvarlist/cmdlist_librarypath.htm) | [DIAdem Path Variables](../../cmdvarlist/cmdvarlist/cmdlist_path.htm) | [DIAdem User Paths](../../cmdvarlist/cmdvarlist/cmdlist_userpath.htm) | [Function: DataFileSize](../functions/datafilesize.htm) | [Function: FileDateGet](../functions/filedateget.htm) | [Function: FileSize](../functions/filesize.htm) | [Function: FilEx](../functions/filex.htm) | [Function: FolderAttrCheck](../functions/folderattrcheck.htm) | [Function: FolderDateGet](../functions/folderdateget.htm) | [Function: FolderExist](../functions/folderexist.htm) | [Function: FolderSize](../functions/foldersize.htm) | [Variable: FileExportFilter](/csh?topicname=varoff/fileexportfilter.htm) | [Variable: FileFilter](/csh?topicname=varoff/filefilter.htm) | [Variable: FileImportFilter](/csh?topicname=varoff/fileimportfilter.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/filedateget.htm language=enus -->
## TOPIC 00029: Function: FileDateGet

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/filedateget.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/filedateget.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FileDateGet

### Function: FileDateGet

Determines what time DIAdem created a file, or the last time DIAdem saved or opened the file.

```text
ReturnValue = FileDateGet(FileName, TimeAttribute) 
```

#### Input Parameters

| FileName | Specifies a file with path and extension.In the filename and extension, you can use ? as a wildcard for a single character and * for several characters.If you do not specify a path, DIAdem searches for the file in the DIAdem folder. |
| --- | --- |
| TimeAttribute | Specifies the time attribute you want: |
| Value Meaning fdCreateTime of creation fdModifyTime of the last modification fdAccessTime of the last access |  |
| Value | Meaning |
| fdCreate | Time of creation |
| fdModify | Time of the last modification |
| fdAccess | Time of the last access |

#### Return Parameters

| ReturnValue | Returns a text with the specified time. The time format depends on the language of the operating system. To select the time format for a language that does not correspond to the language of the operating system, first execute the ApplicationSetLocale command. The function returns an empty text if DIAdem does not find the given file. |
| --- | --- |

#### Examples

The following example determines what time DIAdem created the file Data?.tdm.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strMyResult
strMyResult = FileDateGet(DataWritePath & "Data?.tdm","fdCreate")
```

[Copy script](javascript:void(0);)

```text
strMyResult = dd.FileDateGet(dd.DataWritePath + "Data?.tdm","fdCreate") 
```

The following example determines what time DIAdem last saved the report file Example.tdr.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strMyResult
strMyResult = FileDateGet(LayoutLibrPath & "Example.tdr","fdModify")
```

[Copy script](javascript:void(0);)

```text
strMyResult = dd.FileDateGet(dd.LayoutLibrPath + "Example.tdr","fdModify") 
```

#### Related Functions

[Command: ChnValExpand](../../comoff/chnvalexpand.htm) | [Command: DataFileCopy](../../comoff/datafilecopy.htm) | [Command: DataFileDelete](../../comoff/datafiledelete.htm) | [Command: DataFileLoad](../../comoff/datafileload.htm) | [Command: DataFileLoadRed](../../comoff/datafileloadred.htm) | [Command: DataFileLoadSel](../../comoff/datafileloadsel.htm) | [Command: DataFileLstGet](../../comoff/datafilelstget.htm) | [Command: DataFileMove](../../comoff/datafilemove.htm) | [Command: DataFileRename](../../comoff/datafilerename.htm) | [Command: DataFileSave](../../comoff/datafilesave.htm) | [Command: DataFileSaveSel](../../comoff/datafilesavesel.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: FileDlgShow](../../comoff/filedlgshow.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: PathDlgShow](../../comoff/pathdlgshow.htm) | [Commands and Variables for Working with Data](../../cmdvarlist/cmdvarlist/cmdlist_data.htm) | [Commands and Variables for Working with Files and Folders](../../cmdvarlist/cmdvarlist/cmdlist_files.htm) | [DIAdem Library Paths](../../cmdvarlist/cmdvarlist/cmdlist_librarypath.htm) | [DIAdem Path Variables](../../cmdvarlist/cmdvarlist/cmdlist_path.htm) | [DIAdem User Paths](../../cmdvarlist/cmdvarlist/cmdlist_userpath.htm) | [Function: DataFileSize](../functions/datafilesize.htm) | [Function: FileAttrCheck](../functions/fileattrcheck.htm) | [Function: FileSize](../functions/filesize.htm) | [Function: FilEx](../functions/filex.htm) | [Function: FolderAttrCheck](../functions/folderattrcheck.htm) | [Function: FolderDateGet](../functions/folderdateget.htm) | [Function: FolderExist](../functions/folderexist.htm) | [Function: FolderSize](../functions/foldersize.htm) | [Variable: FileExportFilter](/csh?topicname=varoff/fileexportfilter.htm) | [Variable: FileFilter](/csh?topicname=varoff/filefilter.htm) | [Variable: FileImportFilter](/csh?topicname=varoff/fileimportfilter.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/filesize.htm language=enus -->
## TOPIC 00030: Function: FileSize

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/filesize.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/filesize.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FileSize

### Function: FileSize

Determines the size of a file in bytes.

```text
ReturnValue = FileSize(FileName)
```

#### Input Parameters

| FileName | Specifies a file with path and extension. In the filename and extension, you can use ? as a wildcard for a single character and * for several characters.If you do not specify a path, DIAdem searches for the file in the DIAdem folder. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns an integer value. If DIAdem cannot uniquely determine or find the file, the function returns the value 0. |
| --- | --- |

#### Examples

The following example determines the size of files.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = FileSize(DataLibrPath & "Example.tdm")
intMyResult = FileSize(LayoutLibrPath & "Example.tdr")
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.FileSize(dd.DataLibrPath + "Example.tdm") 
intMyResult = dd.FileSize(dd.LayoutLibrPath + "Example.tdr") 
```

#### Related Functions

[Command: ChnValExpand](../../comoff/chnvalexpand.htm) | [Command: DataFileCopy](../../comoff/datafilecopy.htm) | [Command: DataFileDelete](../../comoff/datafiledelete.htm) | [Command: DataFileLoad](../../comoff/datafileload.htm) | [Command: DataFileLoadRed](../../comoff/datafileloadred.htm) | [Command: DataFileLoadSel](../../comoff/datafileloadsel.htm) | [Command: DataFileLstGet](../../comoff/datafilelstget.htm) | [Command: DataFileMove](../../comoff/datafilemove.htm) | [Command: DataFileRename](../../comoff/datafilerename.htm) | [Command: DataFileSave](../../comoff/datafilesave.htm) | [Command: DataFileSaveSel](../../comoff/datafilesavesel.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: FileDlgShow](../../comoff/filedlgshow.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: PathDlgShow](../../comoff/pathdlgshow.htm) | [Commands and Variables for Working with Data](../../cmdvarlist/cmdvarlist/cmdlist_data.htm) | [Commands and Variables for Working with Files and Folders](../../cmdvarlist/cmdvarlist/cmdlist_files.htm) | [DIAdem Library Paths](../../cmdvarlist/cmdvarlist/cmdlist_librarypath.htm) | [DIAdem Path Variables](../../cmdvarlist/cmdvarlist/cmdlist_path.htm) | [DIAdem User Paths](../../cmdvarlist/cmdvarlist/cmdlist_userpath.htm) | [Function: DataFileSize](../functions/datafilesize.htm) | [Function: FileAttrCheck](../functions/fileattrcheck.htm) | [Function: FileDateGet](../functions/filedateget.htm) | [Function: FilEx](../functions/filex.htm) | [Function: FolderAttrCheck](../functions/folderattrcheck.htm) | [Function: FolderDateGet](../functions/folderdateget.htm) | [Function: FolderExist](../functions/folderexist.htm) | [Function: FolderSize](../functions/foldersize.htm) | [Variable: FileExportFilter](/csh?topicname=varoff/fileexportfilter.htm) | [Variable: FileFilter](/csh?topicname=varoff/filefilter.htm) | [Variable: FileImportFilter](/csh?topicname=varoff/fileimportfilter.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/filex.htm language=enus -->
## TOPIC 00031: Function: FilEx

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/filex.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/filex.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FilEx

### Function: FilEx

Valid names: FileExist, FilEx

Checks whether a file exists in a folder.

```text
ReturnValue = FilEx(FileName)
```

#### Input Parameters

| FileName | Specifies a file with path and extension.In the filename and extension, you can use ? as a wildcard for a single character and * for several characters.If you do not specify a path, DIAdem searches for the file in the DIAdem folder. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns a Boolean value. TRUEFile exists in the specified folder. FALSEFile does not exist in the specified folder. |
| --- | --- |
| TRUE | File exists in the specified folder. |
| FALSE | File does not exist in the specified folder. |

#### Examples

The following example checks whether the Diadem.exe file is in the DIAdem folder.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim blnMyResult
blnMyResult = FileExist("diadem.exe")    'blnMyResult = TRUE
```

[Copy script](javascript:void(0);)

```text
blnMyResult = dd.FileExist("diadem.exe") #blnMyResult = TRUE
```

The following example checks whether the library folder contains any [DAT files](/csh?topicname=header/header/headerdse_allgemein.htm).

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim blnMyResult
blnMyResult = FilEx(DataLibrPath & "*.dat")    'blnMyResult = TRUE 
```

[Copy script](javascript:void(0);)

```text
blnMyResult = dd.FilEx(dd.DataLibrPath + "*.dat") #blnMyResult = TRUE
```

The following example checks, whether any [TDM files](/csh?topicname=genshell/genshell/genshell_directories.htm) are in the [NAVIGATOR-user folder](/csh?topicname=tdmdatamodel/tdmdatamodel/tdm_datamodel.htm). If the FilEx function returns the value TRUE, DIAdem opens the dialog box for loading data files. If the FileEx function returns the value FALSE, a message box displays an error message.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If FilEx(DataReadPath & "*.tdm") Then
  Call FileNameGet("NAVIGATOR","FileRead","*.TDM")
  FileImportFilter = FileDlgFilter
  Call DataFileLoad(FileDlgFileName, FileImportFilter)
Else
  MsgBoxDisp("No TDM file found")
End If
```

[Copy script](javascript:void(0);)

```text
if dd.FilEx(dd.DataReadPath + "*.tdm") : 
    dd.FileNameGet("NAVIGATOR","FileRead","*.TDM") 
    dd.FileImportFilter = dd.FileDlgFilter 
    dd.DataFileLoad(dd.FileDlgFileName, dd.FileImportFilter) 
else: 
    dd.MsgBoxDisp("No TDM file found") 
```

#### Related Functions

[Command: ChnValExpand](../../comoff/chnvalexpand.htm) | [Command: DataFileCopy](../../comoff/datafilecopy.htm) | [Command: DataFileDelete](../../comoff/datafiledelete.htm) | [Command: DataFileLoad](../../comoff/datafileload.htm) | [Command: DataFileLoadRed](../../comoff/datafileloadred.htm) | [Command: DataFileLoadSel](../../comoff/datafileloadsel.htm) | [Command: DataFileLstGet](../../comoff/datafilelstget.htm) | [Command: DataFileMove](../../comoff/datafilemove.htm) | [Command: DataFileRename](../../comoff/datafilerename.htm) | [Command: DataFileSave](../../comoff/datafilesave.htm) | [Command: DataFileSaveSel](../../comoff/datafilesavesel.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: FileDlgShow](../../comoff/filedlgshow.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: PathDlgShow](../../comoff/pathdlgshow.htm) | [Commands and Variables for Working with Data](../../cmdvarlist/cmdvarlist/cmdlist_data.htm) | [Commands and Variables for Working with Files and Folders](../../cmdvarlist/cmdvarlist/cmdlist_files.htm) | [DIAdem Library Paths](../../cmdvarlist/cmdvarlist/cmdlist_librarypath.htm) | [DIAdem Path Variables](../../cmdvarlist/cmdvarlist/cmdlist_path.htm) | [DIAdem User Paths](../../cmdvarlist/cmdvarlist/cmdlist_userpath.htm) | [Function: DataFileSize](../functions/datafilesize.htm) | [Function: FileAttrCheck](../functions/fileattrcheck.htm) | [Function: FileDateGet](../functions/filedateget.htm) | [Function: FileSize](../functions/filesize.htm) | [Function: FolderAttrCheck](../functions/folderattrcheck.htm) | [Function: FolderDateGet](../functions/folderdateget.htm) | [Function: FolderExist](../functions/folderexist.htm) | [Function: FolderSize](../functions/foldersize.htm) | [Variable: FileExportFilter](/csh?topicname=varoff/fileexportfilter.htm) | [Variable: FileFilter](/csh?topicname=varoff/filefilter.htm) | [Variable: FileImportFilter](/csh?topicname=varoff/fileimportfilter.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/find.htm language=enus -->
## TOPIC 00032: Function: Find

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/find.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/find.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Find

### Function: Find

Determines the first row in a data channel that meets a specified condition. The Find function searches a data channel from the beginning to the end.

```text
ReturnValue = Find(Condition[,ChannelLine]) 
```

#### Input Parameters

| Condition | Specifies the condition to check. |
| --- | --- |
| [ChannelLine] | Specifies the row number at which DIAdem begins checking the data channel. |

#### Return Parameters

| ReturnValue | Returns the first row number that satisfies the given condition. The Find function returns the result 0, if no rows of the data channel satisfy the condition. |
| --- | --- |

#### Examples

The following example searches the Group1/Input data channel of which the absolute value for the contents is higher than 10. DIAdem starts checking from row 250 of the data channel and continues to the end of the channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = Find("Ch(""Group1/Input"")>10",250)
```

[Copy script](javascript:void(0);)

```text
intMyResult= dd.Find("Ch(""Group1/Input"")>10",250) 
```

|  | Note In the VBS syntax in the Calculator, use the ChnFind function instead of the Find function, to access the entire VBS functionality and user commands. |
| --- | --- |

#### Related Functions

[Command: ChnFind](../../comoff/chnfind.htm) | [Command: ChnFindReverse](../../comoff/chnfindreverse.htm) | [Function: CCh](../functions/cch.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: FindReverse](../functions/findreverse.htm) | [Function: PNo](../functions/pno.htm)

#### Examples

[Searching for Outliers with the ChnEvent Function](/csh?topicname=exploff/examples/exp_analysis_av2.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/findreverse.htm language=enus -->
## TOPIC 00033: Function: FindReverse

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/findreverse.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/findreverse.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FindReverse

### Function: FindReverse

Determines the first row in a data channel that meets a specified condition. The ReverseFind function searches a data channel from the end to the beginning.

```text
ReturnValue = FindReverse(Condition[,ChannelLine]) 
```

#### Input Parameters

| Condition | Specifies the condition to check. |
| --- | --- |
| [ChannelLine] | Specifies the row number at which DIAdem begins checking the data channel, back to the beginning. |

#### Return Parameters

| ReturnValue | Returns the first row number that satisfies the given condition. The function returns the result 0, if no rows of the data channel satisfy the condition. |
| --- | --- |

#### Examples

The following example searches the Group1/Input data channel of which the absolute value for the contents is higher than 10. DIAdem checks from row 1000 up to the beginning of the data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = FindReverse("Ch(""Group1/Input"")>10",1000)
```

[Copy script](javascript:void(0);)

```text
intMyResult= dd.FindReverse("Ch(""Group1/Input"")>10",1000) 
```

|  | Note In the VBS syntax in the Calculator, use the ChnFindReverse function instead of the FindReverse function, to access the entire VBS functionality and user commands. |
| --- | --- |

#### Related Functions

[Command: ChnFind](../../comoff/chnfind.htm) | [Command: ChnFindReverse](../../comoff/chnfindreverse.htm) | [Function: CCh](../functions/cch.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: Find](../functions/find.htm) | [Function: PNo](../functions/pno.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/floor.htm language=enus -->
## TOPIC 00034: Function: Floor

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/floor.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/floor.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Floor

### Function: Floor

Specifies the integer part of a number, where the function rounds down the transferred value to obtain an integer number. For negative numbers the function returns integer numbers that are smaller than or equal to the Value argument.

```text
ReturnValue = Floor(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. |
| --- | --- |

#### Examples

The following example rounds down some values:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBox(Floor(2.6))  '=> 2
Call MsgBox(Floor(2.1))  '=> 2
Call MsgBox(Floor(-2.1)) '=> -3
Call MsgBox(Floor(-2.6)) '=> -3
```

[Copy script](javascript:void(0);)

```text
print(dd.Floor(2.6)) #=> 2
print(dd.Floor(2.1)) #=> 2
print(dd.Floor(-2.1)) #=> -3
print(dd.Floor(-2.6)) #=> -3
```

The following example rounds down the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Floor (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Floor (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Topics

[Ceil](../functions/ceil.htm) | [Int](/csh?topicname=vbs/methods/vbs_method_int_globalobj.htm) | [Round](../functions/round.htm) | [Trunc](../functions/trunc.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/folderattrcheck.htm language=enus -->
## TOPIC 00035: Function: FolderAttrCheck

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/folderattrcheck.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/folderattrcheck.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FolderAttrCheck

### Function: FolderAttrCheck

Checks the attributes of a folder.

```text
ReturnValue = FolderAttrCheck(FolderName, Attribute)
```

#### Input Parameters

| FolderName | Specifies a folder with path.If you do not specify a path, DIAdem searches for the folder in the DIAdem folder. |
| --- | --- |
| Attributes | Specifies the attribute to be checked. |
| Value Meaning faReadOnly The folder is write-protected. faArchive The contents of the folder have been modified. faHidden The folder is hidden. faSystem The folder is a system folder. |  |
| Value | Meaning |
| faReadOnly | The folder is write-protected. |
| faArchive | The contents of the folder have been modified. |
| faHidden | The folder is hidden. |
| faSystem | The folder is a system folder. |

#### Return Parameters

| ReturnValue | Returns a Boolean value. If DIAdem does not find the given folder, the function returns the result FALSE. |
| --- | --- |

#### Example

The following example checks whether the DIAdem library folder is write-protected.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim blnMyResult
blnMyResult = FolderAttrCheck("libr","faReadOnly")
```

[Copy script](javascript:void(0);)

```text
blnMyResult = dd.FolderAttrCheck("libr","faReadOnly") 
```

The following example checks, whether the C:\MyFolder data folder is write-protected. If the FolderAttrCheck function returns the value FALSE, a message box appears with an error message. If the FolderAttrCheck function returns the value FALSE, DIAdem opens the dialog box for saving data files.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If FolderAttrCheck("C:\MyFolder","faReadOnly") then
  MsgBoxDisp("Folder is readonly!")
Else
  Call FileNameGet("NAVIGATOR", "FileWrite")
  Call DataFileSave(FileDlgFileName)
End If
```

[Copy script](javascript:void(0);)

```text
if dd.FolderAttrCheck("C:\\MyFolder","faReadOnly") : 
    dd.MsgBoxDisp("Folder is readonly!") 
else: 
    dd.FileNameGet("NAVIGATOR", "FileWrite") 
    dd.DataFileSave(dd.FileDlgFileName) 
```

#### Related Functions

[Command: ChnValExpand](../../comoff/chnvalexpand.htm) | [Command: DataFileCopy](../../comoff/datafilecopy.htm) | [Command: DataFileDelete](../../comoff/datafiledelete.htm) | [Command: DataFileLoad](../../comoff/datafileload.htm) | [Command: DataFileLoadRed](../../comoff/datafileloadred.htm) | [Command: DataFileLoadSel](../../comoff/datafileloadsel.htm) | [Command: DataFileLstGet](../../comoff/datafilelstget.htm) | [Command: DataFileMove](../../comoff/datafilemove.htm) | [Command: DataFileRename](../../comoff/datafilerename.htm) | [Command: DataFileSave](../../comoff/datafilesave.htm) | [Command: DataFileSaveSel](../../comoff/datafilesavesel.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: FileDlgShow](../../comoff/filedlgshow.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: PathDlgShow](../../comoff/pathdlgshow.htm) | [Commands and Variables for Working with Data](../../cmdvarlist/cmdvarlist/cmdlist_data.htm) | [Commands and Variables for Working with Files and Folders](../../cmdvarlist/cmdvarlist/cmdlist_files.htm) | [DIAdem Library Paths](../../cmdvarlist/cmdvarlist/cmdlist_librarypath.htm) | [DIAdem Path Variables](../../cmdvarlist/cmdvarlist/cmdlist_path.htm) | [DIAdem User Paths](../../cmdvarlist/cmdvarlist/cmdlist_userpath.htm) | [Function: DataFileSize](../functions/datafilesize.htm) | [Function: FileAttrCheck](../functions/fileattrcheck.htm) | [Function: FileDateGet](../functions/filedateget.htm) | [Function: FileSize](../functions/filesize.htm) | [Function: FilEx](../functions/filex.htm) | [Function: FolderDateGet](../functions/folderdateget.htm) | [Function: FolderExist](../functions/folderexist.htm) | [Function: FolderSize](../functions/foldersize.htm) | [Variable: FileExportFilter](/csh?topicname=varoff/fileexportfilter.htm) | [Variable: FileFilter](/csh?topicname=varoff/filefilter.htm) | [Variable: FileImportFilter](/csh?topicname=varoff/fileimportfilter.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/folderdateget.htm language=enus -->
## TOPIC 00036: Function: FolderDateGet

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/folderdateget.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/folderdateget.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FolderDateGet

### Function: FolderDateGet

Determines what time DIAdem created a folder, or the last time DIAdem modified or opened the folder.

```text
ReturnValue = FolderDateGet(FolderName, TimeAttribute)
```

#### Input Parameters

| FolderName | Specifies a folder with path. |
| --- | --- |
| TimeAttribute | Specifies the time attribute you want: |
| Value Meaning fdCreateTime of creation fdModifyTime of the last modification fdAccessTime of the last access |  |
| Value | Meaning |
| fdCreate | Time of creation |
| fdModify | Time of the last modification |
| fdAccess | Time of the last access |

#### Return Parameters

| ReturnValue | Returns a text with the time in the form dd.mm.yyyy hh:nn:ss. |
| --- | --- |

#### Examples

The following example determines the last access date for the demo data folder.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strMyResult
strMyResult = FolderDateGet(DataReadPath,"fdModify")
```

[Copy script](javascript:void(0);)

```text
strMyResult = dd.FolderDateGet(dd.DataReadPath,"fdModify") 
```

#### Related Functions

[Command: ChnValExpand](../../comoff/chnvalexpand.htm) | [Command: DataFileCopy](../../comoff/datafilecopy.htm) | [Command: DataFileDelete](../../comoff/datafiledelete.htm) | [Command: DataFileLoad](../../comoff/datafileload.htm) | [Command: DataFileLoadRed](../../comoff/datafileloadred.htm) | [Command: DataFileLoadSel](../../comoff/datafileloadsel.htm) | [Command: DataFileLstGet](../../comoff/datafilelstget.htm) | [Command: DataFileMove](../../comoff/datafilemove.htm) | [Command: DataFileRename](../../comoff/datafilerename.htm) | [Command: DataFileSave](../../comoff/datafilesave.htm) | [Command: DataFileSaveSel](../../comoff/datafilesavesel.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: FileDlgShow](../../comoff/filedlgshow.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: PathDlgShow](../../comoff/pathdlgshow.htm) | [Commands and Variables for Working with Data](../../cmdvarlist/cmdvarlist/cmdlist_data.htm) | [Commands and Variables for Working with Files and Folders](../../cmdvarlist/cmdvarlist/cmdlist_files.htm) | [DIAdem Library Paths](../../cmdvarlist/cmdvarlist/cmdlist_librarypath.htm) | [DIAdem Path Variables](../../cmdvarlist/cmdvarlist/cmdlist_path.htm) | [DIAdem User Paths](../../cmdvarlist/cmdvarlist/cmdlist_userpath.htm) | [Function: DataFileSize](../functions/datafilesize.htm) | [Function: FileAttrCheck](../functions/fileattrcheck.htm) | [Function: FileDateGet](../functions/filedateget.htm) | [Function: FileSize](../functions/filesize.htm) | [Function: FilEx](../functions/filex.htm) | [Function: FolderAttrCheck](../functions/folderattrcheck.htm) | [Function: FolderExist](../functions/folderexist.htm) | [Function: FolderSize](../functions/foldersize.htm) | [Variable: FileExportFilter](/csh?topicname=varoff/fileexportfilter.htm) | [Variable: FileFilter](/csh?topicname=varoff/filefilter.htm) | [Variable: FileImportFilter](/csh?topicname=varoff/fileimportfilter.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/folderexist.htm language=enus -->
## TOPIC 00037: Function: FolderExist

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/folderexist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/folderexist.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FolderExist

### Function: FolderExist

Checks whether a folder exists.

```text
ReturnValue = FolderExist(FolderName)
```

#### Input Parameters

| FolderName | Specifies a folder with path.If you do not specify a complete path, DIAdem searches for the folder in the DIAdem folder. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns a Boolean value. TRUEFolder exists in the specified path. FALSEFolder does not exist in the specified path. |
| --- | --- |
| TRUE | Folder exists in the specified path. |
| FALSE | Folder does not exist in the specified path. |

#### Examples

The following example checks whether the C:\MyFolder data folder exists. If the FolderExist function returns the value TRUE, DIAdem opens the dialog box for loading data files. If the FolderExist function returns the value FALSE, a message box appears with an error message.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If FolderExist("C:\MyFolder") then
  Call FileNameGet("NAVIGATOR","FileRead","*.TDM")
  FileImportFilter = FileDlgFilter
  Call DataFileLoad(FileDlgFileName,FileImportFilter,"Load")
Else
  MsgBoxDisp("Folder not found")
End If
```

[Copy script](javascript:void(0);)

```text
if dd.FolderExist("C:\\MyFolder") : 
    dd.FileNameGet("NAVIGATOR","FileRead","*.TDM") 
    dd.FileImportFilter = dd.FileDlgFilter 
    dd.DataFileLoad(dd.FileDlgFileName,dd.FileImportFilter,"Load") 
else: 
    dd.MsgBoxDisp("Folder not found") 
```

The following example checks whether the library folder exists. DIAdem searches for the folder in the DIAdem folder because the specified path is not complete.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim blnMyResult
blnMyResult = FolderExist("libr")    'blnMyResult = TRUE
```

[Copy script](javascript:void(0);)

```text
blnMyResult = dd.FolderExist("libr") #blnMyResult = TRUE
```

#### Related Functions

[Command: ChnValExpand](../../comoff/chnvalexpand.htm) | [Command: DataFileCopy](../../comoff/datafilecopy.htm) | [Command: DataFileDelete](../../comoff/datafiledelete.htm) | [Command: DataFileLoad](../../comoff/datafileload.htm) | [Command: DataFileLoadRed](../../comoff/datafileloadred.htm) | [Command: DataFileLoadSel](../../comoff/datafileloadsel.htm) | [Command: DataFileLstGet](../../comoff/datafilelstget.htm) | [Command: DataFileMove](../../comoff/datafilemove.htm) | [Command: DataFileRename](../../comoff/datafilerename.htm) | [Command: DataFileSave](../../comoff/datafilesave.htm) | [Command: DataFileSaveSel](../../comoff/datafilesavesel.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: FileDlgShow](../../comoff/filedlgshow.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: FolderAttrClear](../../comoff/folderattrclear.htm) | [Command: FolderAttrSet](../../comoff/folderattrset.htm) | [Command: FolderCopy](../../comoff/foldercopy.htm) | [Command: FolderCreate](../../comoff/foldercreate.htm) | [Command: FolderDelete](../../comoff/folderdelete.htm) | [Command: FolderMove](../../comoff/foldermove.htm) | [Command: FolderRename](../../comoff/folderrename.htm) | [Command: FolderUnzip](../../comoff/folderunzip.htm) | [Command: FolderZip](../../comoff/folderzip.htm) | [Command: PathAddTrailingBackslash](../../comoff/pathaddtrailingbackslash.htm) | [Command: PathDlgShow](../../comoff/pathdlgshow.htm) | [Commands and Variables for Working with Data](../../cmdvarlist/cmdvarlist/cmdlist_data.htm) | [Commands and Variables for Working with Files and Folders](../../cmdvarlist/cmdvarlist/cmdlist_files.htm) | [DIAdem Library Paths](../../cmdvarlist/cmdvarlist/cmdlist_librarypath.htm) | [DIAdem Path Variables](../../cmdvarlist/cmdvarlist/cmdlist_path.htm) | [DIAdem User Paths](../../cmdvarlist/cmdvarlist/cmdlist_userpath.htm) | [Function: DataFileSize](../functions/datafilesize.htm) | [Function: FileAttrCheck](../functions/fileattrcheck.htm) | [Function: FileDateGet](../functions/filedateget.htm) | [Function: FileSize](../functions/filesize.htm) | [Function: FilEx](../functions/filex.htm) | [Function: FolderAttrCheck](../functions/folderattrcheck.htm) | [Function: FolderDateGet](../functions/folderdateget.htm) | [Function: FolderSize](../functions/foldersize.htm) | [Variable: FileExportFilter](/csh?topicname=varoff/fileexportfilter.htm) | [Variable: FileFilter](/csh?topicname=varoff/filefilter.htm) | [Variable: FileImportFilter](/csh?topicname=varoff/fileimportfilter.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/foldersize.htm language=enus -->
## TOPIC 00038: Function: FolderSize

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/foldersize.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/foldersize.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FolderSize

### Function: FolderSize

Determines the size of a folder, subfolders included, in bytes.

```text
ReturnValue = FolderSize(FolderName)
```

#### Input Parameters

| FolderName | Specifies a folder with path.If you do not specify a path, DIAdem searches for the folder in the DIAdem folder. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns an integer value. If DIAdem cannot uniquely determine or find the folder, the function returns the value 0. |
| --- | --- |

#### Examples

The following example determines the amount of memory that the files in the demo folder of DIAdem take up.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = FolderSize(DataReadPath)
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.FolderSize(dd.DataReadPath) 
```

#### Related Functions

[Command: ChnValExpand](../../comoff/chnvalexpand.htm) | [Command: DataFileCopy](../../comoff/datafilecopy.htm) | [Command: DataFileDelete](../../comoff/datafiledelete.htm) | [Command: DataFileLoad](../../comoff/datafileload.htm) | [Command: DataFileLoadRed](../../comoff/datafileloadred.htm) | [Command: DataFileLoadSel](../../comoff/datafileloadsel.htm) | [Command: DataFileLstGet](../../comoff/datafilelstget.htm) | [Command: DataFileMove](../../comoff/datafilemove.htm) | [Command: DataFileRename](../../comoff/datafilerename.htm) | [Command: DataFileSave](../../comoff/datafilesave.htm) | [Command: DataFileSaveSel](../../comoff/datafilesavesel.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: DataFileSelDlg](../../comoff/datafileseldlg.htm) | [Command: FileDlgShow](../../comoff/filedlgshow.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: FileNameGet](../../comoff/filenameget.htm) | [Command: PathDlgShow](../../comoff/pathdlgshow.htm) | [Commands and Variables for Working with Data](../../cmdvarlist/cmdvarlist/cmdlist_data.htm) | [Commands and Variables for Working with Files and Folders](../../cmdvarlist/cmdvarlist/cmdlist_files.htm) | [DIAdem Library Paths](../../cmdvarlist/cmdvarlist/cmdlist_librarypath.htm) | [DIAdem Path Variables](../../cmdvarlist/cmdvarlist/cmdlist_path.htm) | [DIAdem User Paths](../../cmdvarlist/cmdvarlist/cmdlist_userpath.htm) | [Function: DataFileSize](../functions/datafilesize.htm) | [Function: FileAttrCheck](../functions/fileattrcheck.htm) | [Function: FileDateGet](../functions/filedateget.htm) | [Function: FileSize](../functions/filesize.htm) | [Function: FilEx](../functions/filex.htm) | [Function: FolderAttrCheck](../functions/folderattrcheck.htm) | [Function: FolderDateGet](../functions/folderdateget.htm) | [Function: FolderExist](../functions/folderexist.htm) | [Variable: FileExportFilter](/csh?topicname=varoff/fileexportfilter.htm) | [Variable: FileFilter](/csh?topicname=varoff/filefilter.htm) | [Variable: FileImportFilter](/csh?topicname=varoff/fileimportfilter.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/fr.htm language=enus -->
## TOPIC 00039: Function: FR

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/fr.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/fr.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FR

### Function: FR

Reads a line from a text file.

```text
ReturnValue = FR(FileName, LineNo)
```

#### Input Parameters

| FileName | Specifies a text file with path and extension. If you do not specify a path, DIAdem searches for the text file in the DIAdem folder. |
| --- | --- |
| LineNo | Specifies the number of the line that DIAdem reads out. |

#### Return Parameters

| ReturnValue | Returns a text. If the given text line is a comment line, DIAdem returns an empty text. DIAdem discards any comments in a text line and returns the remainder of the text line as the result. The FR function only recognizes a comment by the characters { and (*. If the line number you enter for the LineNo parameter is higher than the number of lines in the text file, the FR function returns the value EOF. |
| --- | --- |

#### Examples

The following examples read out lines from a fictitious ANSI text file Test.txt. The file is located in the DIAdem SCRIPT read path.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
***************
This is an 
example
text {only for demonstration
```

[Copy script](javascript:void(0);)

```text
*************** 
This is an 
example 
text {only for demonstration 
```

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strMyResult
strMyResult = FR(ScriptReadPath & "test.txt",1)    'strMyResult = ***************
strMyResult = FR(ScriptReadPath & "test.txt",4)    'strMyResult = text
strMyResult = FR(ScriptReadPath & "test.txt",7)    'strMyResult = EOF
```

[Copy script](javascript:void(0);)

```text
strMyResult = dd.FR(dd.ScriptReadPath + "test.txt",1) #strMyResult = ***************
strMyResult = dd.FR(dd.ScriptReadPath + "test.txt",4) #strMyResult = text
strMyResult = dd.FR(dd.ScriptReadPath + "test.txt",7) #strMyResult = EOF
```

|  | Note The FR function does not support Unicode files. Use the TextFileReadLn function to read text files. These functions also support long text and Unicode characters. Use the TextFileWriteLn function to write to text files. |
| --- | --- |

#### Related Functions

[Command: DataFileDelete](../../comoff/datafiledelete.htm) | [Command: DataFileLstGet](../../comoff/datafilelstget.htm) | [Command: DataFileMove](../../comoff/datafilemove.htm) | [Command: DataFileRename](../../comoff/datafilerename.htm) | [Command: DirLstWrite](../../comoff/dirlstwrite.htm) | [Command: FileAttrClear](../../comoff/fileattrclear.htm) | [Command: FileAttrSet](../../comoff/fileattrset.htm) | [Command: FileClose](../../comoff/fileclose.htm) | [Command: FileCloseAll](../../comoff/filecloseall.htm) | [Command: FileCopy](../../comoff/filecopy.htm) | [Command: FileDateSet](../../comoff/filedateset.htm) | [Command: FileDelete](../../comoff/filedelete.htm) | [Command: FileMove](../../comoff/filemove.htm) | [Command: FileOpen](../../comoff/fileopen.htm) | [Command: FileRename](../../comoff/filerename.htm) | [Command: TextFileEncoding](../../comoff/textfileencoding.htm) | [Command: TextFileEOL](../../comoff/textfileeol.htm) | [Function: DataFileSize](../functions/datafilesize.htm) | [Function: TextFileEOF](../functions/textfileeof.htm) | [Function: TextFileError](../functions/textfileerror.htm) | [Function: TextFileErrorTxt](../functions/textfileerrortxt.htm) | [Function: TextFileSeek](../functions/textfileseek.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/frac.htm language=enus -->
## TOPIC 00040: Function: Frac

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/frac.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/frac.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Frac

### Function: Frac

Determines the decimal places of a number.

```text
ReturnValue = Frac(Value) 
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns the decimal places as numeric values. For invalid values the value is NoValue. |
| --- | --- |

#### Examples

The following example determines the decimal places of the number Pi.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = Frac(Pi)    'intMyResult = 0.14159265358979
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.Frac(Pi) #intMyResult = 0.14159265358979
```

The following example determines the decimal places of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Frac (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Frac (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note Use the Trunc function to determine the integer part of a number. |
| --- | --- |

|  | The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/functions_bit_overview.htm language=enus -->
## TOPIC 00041: Bit Functions

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/functions_bit_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/functions_bit_overview.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > Bit Functions

### Bit Functions

The subordinate topics contained in the tree on the contents tab of the Help describe the DIAdem bit functions. You can use these functions to set, check, negate, or shift bits, for example.

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/functions_boolesch_overview.htm language=enus -->
## TOPIC 00042: Boolean Functions

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/functions_boolesch_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/functions_boolesch_overview.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > Boolean Functions

### Boolean Functions

The subordinate topics contained in the tree on the contents tab of the Help describe the Boolean DIAdem functions. You can use these functions to negate values and for logical AND or OR operations.

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/functions_channels_overview.htm language=enus -->
## TOPIC 00043: Channel Functions

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/functions_channels_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/functions_channels_overview.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > Channel Functions

### Channel Functions

The subordinate topics contained in the tree on the contents tab of the Help describe the DIAdem channel functions. You can use these functions to determine characteristic channel values.

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/functions_comvar_overview.htm language=enus -->
## TOPIC 00044: Command and Variable Functions

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/functions_comvar_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/functions_comvar_overview.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > Command and Variable Functions

### Command and Variable Functions

The subordinate topics contained in the tree on the contents tab of the Help describe the DIAdem command and variable functions. You can use these functions to determine the type of a variable or of a command, or to read out the environment variables of the operating system.

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/functions_directoryfile_overview.htm language=enus -->
## TOPIC 00045: Folder and File Functions

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/functions_directoryfile_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/functions_directoryfile_overview.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > Folder and File Functions

### Folder and File Functions

The subordinate topics contained in the tree on the contents tab of the Help describe the DIAdem folder and file functions. You can use these functions to determine whether folders and files exist and how big they are.

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/functions_num_overview.htm language=enus -->
## TOPIC 00046: Numeric Functions

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/functions_num_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/functions_num_overview.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > Numeric Functions

### Numeric Functions

The subordinate topics contained in the tree on the contents tab of the Help describe the numeric functions in DIAdem. You can use these functions, for example, to calculate the root, the square, and the logarithm of a number, or to determine random numbers.

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/functions_text_overview.htm language=enus -->
## TOPIC 00047: Text Functions

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/functions_text_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/functions_text_overview.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > Text Functions

### Text Functions

The subordinate topics contained in the tree on the contents tab of the Help describe the DIAdem text functions. You can use these functions, for example, to determine the index of a text or the position of a character in a text, or to delete characters from a text.

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/functions_textfile_overview.htm language=enus -->
## TOPIC 00048: Text File Functions

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/functions_textfile_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/functions_textfile_overview.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > Text File Functions

### Text File Functions

The subordinate topics contained in the tree on the contents tab of the Help describe the DIAdem text file functions. You can use these functions, for example, to open, to close, or to read out functions.

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/functions_trigonom_overview.htm language=enus -->
## TOPIC 00049: Trigonometric Functions

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/functions_trigonom_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/functions_trigonom_overview.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > Trigonometric Functions

### Trigonometric Functions

The subordinate topics contained in the tree on the contents tab of the Help describe the trigonometric DIAdem functions. You can use these functions,for example, to calculate the sine or the cosine of a number.

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/getb.htm language=enus -->
## TOPIC 00050: Function: GetB

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/getb.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/getb.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: GetB

### Function: GetB

Checks a bit you specify in the binary representation of a decimal number. The GetB function converts the decimal number into a dual number.

```text
ReturnValue = GetB(Value,BitIndex)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |
| BitIndex | Specifies a numeric value, a variable, or a data channel for the index of the bit you want to check.Value range 0 to 31 |

|  | Note If you enter numbers with decimal places for the parameters Value and BitIndex, DIAdem rounds the numbers to integers.From DIAdem 2014, the function no longer calculates the sum of the BitIndex input parameter. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns Boolean values. If the input value is NoValue, the GetB function returns the value NoValue. If the input parameter BitIndex is outside the value range, the function returns the value 0. |
| --- | --- |

#### Examples

The following example checks the second bit of the binary representation of the decimal number 10.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim blnMyResult
blnMyResult = GetB(10,1)    'blnMyResult = TRUE
```

[Copy script](javascript:void(0);)

```text
blnMyResult = dd.GetB(10,1) #blnMyResult = TRUE
```

The following example checks the bits from the values in the Group1/Input data channel, indexed by the Group1/Reference data channel, and saves the result in the new data channel Group2/Result. DIAdem skips values of the Group1/Reference index channel that are higher than 31.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= GetB (Ch(""Group1/Input""),Ch(""Group1/Reference""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= GetB (Ch(""Group1/Input""),Ch(""Group1/Reference""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The first physical input quantity is arbitrary. The second input quantity must be dimensionless. The first physical input quantity and the result quantity are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: AndB](../functions/andb.htm) | [Function: ClrB](../functions/clrb.htm) | [Function: NotB](../functions/notb.htm) | [Function: OrB](../functions/orb.htm) | [Function: SetB](../functions/setb.htm) | [Function: ShL](../functions/shl.htm) | [Function: ShR](../functions/shr.htm) | [Function: XOrB](../functions/xorb.htm) | [Variable: ApplicationLegacyBinaryOperations](/csh?topicname=varoff/applicationlegacybinaryoperations.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/getenv.htm language=enus -->
## TOPIC 00051: Function: GetEnv

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/getenv.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/getenv.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: GetEnv

### Function: GetEnv

Reads out an environment variable of the operating system.

```text
ReturnValue = GetEnv(VariableName)
```

#### Input Parameters

| VariableName | Specifies an environment variable. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns the content of the environment variable as text. |
| --- | --- |

#### Examples

The following example reads out the path environment variable of the operating system.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strMyResult
strMyResult = GetEnv("path")
```

[Copy script](javascript:void(0);)

```text
strMyResult = dd.GetEnv("path") 
```

|  | Note Select the Windows menu Start»Control Panel»System»Advanced»Environment Variables to check which environment variables your Windows operating system uses. |
| --- | --- |

#### Related Functions

[Command: AddUserCommandToEvent](../../comoff/addusercommandtoevent.htm) | [Command: RemoveUserCommandFromEvent](../../comoff/removeusercommandfromevent.htm) | [Command: VEnumIdx](../../comoff/venumidx.htm) | [Function: IdentifierType](../functions/identifiertype.htm) | [Function: MaxOrd](../functions/maxord.htm) | [Function: Ord](../functions/ord.htm) | [Function: ScriptEvaluate](../functions/scriptevaluate.htm) | [Function: VEnum](../functions/venum.htm) | [Function: VIT](../functions/vit.htm) | [Function: VSA](../functions/vsa.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/identifiertype.htm language=enus -->
## TOPIC 00052: Function: IdentifierType

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/identifiertype.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/identifiertype.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: IdentifierType

### Function: IdentifierType

Determines the type of a [variable](/csh?topicname=genas/genauto/genauto_variables.htm) or a command.

```text
ReturnValue = IdentifierType(CmdVarName) 
```

#### Input Parameters

| CmdVarName | Specifies a variable or a command. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns an integer value for the variable or command type: Value Meaning 0Unknown type 1DIAdem command registered by default 2DIAdem command registered with GPI 3User command 4DIAdem variable registered by default 5DIAdem variable registered with GPI 6DIAdem user variable 7Calculator function |
| --- | --- |
| Value | Meaning |
| 0 | Unknown type |
| 1 | DIAdem command registered by default |
| 2 | DIAdem command registered with GPI |
| 3 | User command |
| 4 | DIAdem variable registered by default |
| 5 | DIAdem variable registered with GPI |
| 6 | DIAdem user variable |
| 7 | Calculator function |

#### Examples

The following example determines the type of the [O1](/csh?topicname=varoff/o1.htm) variable.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = IdentifierType("O1")             'intMyResult = 4
```

[Copy script](javascript:void(0);)

```text
intMyResult= dd.IdentifierType("O1") #intMyResult = 4
```

The following example determines the type of the [Calculate](../../comoff/calculate.htm) command.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = IdentifierType("Calculate")    'intMyResult = 1
```

[Copy script](javascript:void(0);)

```text
intMyResult= dd.IdentifierType("Calculate") #intMyResult = 1
```

#### Related Functions

[Command: AddUserCommandToEvent](../../comoff/addusercommandtoevent.htm) | [Command: RemoveUserCommandFromEvent](../../comoff/removeusercommandfromevent.htm) | [Command: VEnumIdx](../../comoff/venumidx.htm) | [Function: GetEnv](../functions/getenv.htm) | [Function: MaxOrd](../functions/maxord.htm) | [Function: Ord](../functions/ord.htm) | [Function: ScriptEvaluate](../functions/scriptevaluate.htm) | [Function: VEnum](../functions/venum.htm) | [Function: VIT](../functions/vit.htm) | [Function: VSA](../functions/vsa.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/idx.htm language=enus -->
## TOPIC 00053: Function: Idx

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/idx.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/idx.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Idx

### Function: Idx

Determines the index of a text in a DIAdem vector variable.

```text
ReturnValue = Idx(String, VariableName [:Start])
```

#### Input Parameters

| String | Specifies the text to search for. |
| --- | --- |
| VariableName | Specifies the name of the DIAdem vector variable to search. |
| [Start] | Specifies the index where DIAdem starts searching in the vector variable. |

#### Return Parameters

| ReturnValue | Returns the index of the first vector element that contains the text you specify, as a numeric value. The Idx function first searches for vector elements identical to the text you specify. If the function does not find any identical vector elements, it searches for the text at the beginning of the texts in the vector elements. The function returns the result 0 if DIAdem cannot find any text or text element identical to the text you specify. |
| --- | --- |

#### Examples

The following example determines the index of a text in the DIAdem vector variable TV, which you can fill with text in the [DIAdem Calculator](/csh?topicname=dlgcalculator/dlgcalculator/dlgformulacalc_dialog.htm).

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
TV(1) = "DIAdem"
TV(2) = "is a" 
TV(3) = "very"
TV(4) = "useful"
TV(5) = "software"
TV(6) = "use"
TV(7) = "it"
Dim intMyResult
intMyResult = Idx("DIAdem","TV")       'intMyResult = 1
intMyResult = Idx("software","TV:3")   'intMyResult = 5
intMyResult = Idx("use","TV")          'intMyResult = 6
intMyResult = Idx("ware","TV")         'intMyResult = 0
```

[Copy script](javascript:void(0);)

```text
TV[1] = "DIAdem" 
TV[2] = "is a" 
TV[3] = "very" 
TV[4] = "useful" 
TV[5] = "software" 
TV[6] = "use" 
TV[7] = "it" 
intMyResult = dd.Idx("DIAdem","TV") #intMyResult = 1
intMyResult = dd.Idx("software","TV:3") #intMyResult = 5
intMyResult = dd.Idx("use","TV") #intMyResult = 6
intMyResult = dd.Idx("ware","TV") #intMyResult = 0
```

|  | Note You cannot use the Idx function to search in enumeration variables and dynamic enumeration variables for enumeration terms and dynamic enumeration terms. Use the Ord function to search enumeration variables and dynamic enumeration variables. |
| --- | --- |

#### Related Functions

[Command: TTD](../../comoff/ttd.htm) | [Function: Char](../functions/char.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: FileNameSplit](../functions/namesplit.htm) | [Function: Len](../functions/len.htm) | [Function: PU](../functions/pu.htm) | [Function: Str](../functions/str.htm) | [Function: Textaddition (+)](../functions/tadd.htm) | [Function: TTR (Text to Real)](../functions/ttr.htm) | [Function: Val](../functions/val.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/len.htm language=enus -->
## TOPIC 00054: Function: Len

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/len.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/len.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Len

### Function: Len

Determines the text length.

```text
ReturnValue = Len(String) 
```

#### Input Parameters

| String | Specifies a text or a text variable. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns the number of characters as an integer value. DIAdem counts blanks at the beginning, at the end, and within the text. |
| --- | --- |

#### Examples

The following example determines the number of characters in a text.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("L1= Len(""DIAdem  "")")    'L1 = 8 
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("L1= Len(""DIAdem  "")") #L1 = 8
```

|  | Note DIAdem only uses the DIAdem function Len if you use the FormulaCalc command otherwise DIAdem uses the VBS function Len. |
| --- | --- |

#### Related Functions

[Command: TTD](../../comoff/ttd.htm) | [Function: Char](../functions/char.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: FileNameSplit](../functions/namesplit.htm) | [Function: Idx](../functions/idx.htm) | [Function: PU](../functions/pu.htm) | [Function: Str](../functions/str.htm) | [Function: Textaddition (+)](../functions/tadd.htm) | [Function: TTR (Text to Real)](../functions/ttr.htm) | [Function: Val](../functions/val.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/ln.htm language=enus -->
## TOPIC 00055: Function: Ln

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/ln.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/ln.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Ln

### Function: Ln

Calculates the logarithm with a base of e (Eularian number).

```text
ReturnValue = Ln(Value) 
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns numeric values. |
| --- | --- |

#### Examples

The following example calculates the natural logarithm of the number Pi.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = Ln(Pi)    'intMyResult = 1.1447298858494
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.Ln(Pi) #intMyResult = 1.1447298858494
```

The following example calculates the natural logarithm of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Ln (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Ln (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must be dimensionless. The physical result quantity is also dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/log.htm language=enus -->
## TOPIC 00056: Function: Lg

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/log.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/log.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Lg

### Function: Lg

Calculates the logarithm with a base of 10. DIAdem uses the DIAdem function Lg only if you use the [FormulaCalc](../../comoff/formulacalc.htm) command in your script, otherwise DIAdem uses the VBS function [Log](/csh?topicname=vbs/methods/vbs_method_log_globalobj.htm).

```text
ReturnValue = Lg(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns numeric values. |
| --- | --- |

#### Examples

The following example calculates the decadic logarithm of the number 1000.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = Lg(1000)    'intMyResult = 3 
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.Lg(1000) #intMyResult = 3
```

The following example calculates the decadic logarithm of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Lg (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Lg (Ch(""Group1/Input""))") 
```

|  | Note You must use the commands Calculate or FormulaCalc in scripts in order to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must be dimensionless. The physical result quantity is also dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/maxord.htm language=enus -->
## TOPIC 00057: Function: MaxOrd

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/maxord.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/maxord.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: MaxOrd

### Function: MaxOrd

Determines the greatest index of enumeration and dynamic enumeration terms in [enumeration variables](/csh?topicname=genas/genauto/genauto_enumeration_list.htm) or [dynamic enumeration variables](/csh?topicname=genas/genauto/genauto_dynamic_enumeration_list.htm).

```text
ReturnValue = MaxOrd(VariableName)
```

#### Input Parameters

| VariableName | Specifies an enumeration variable or a dynamic enumeration variable.The property variables of the object-oriented script interface are constants and not enumeration variables or dynamic enumeration list variables. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns an integer for the index of the last enumeration or dynamic enumeration term. The first enumeration or dynamic enumeration term has the index 0. |
| --- | --- |

#### Examples

The following example determines the index of the last color in the [ColorLst](/csh?topicname=varoff/colorlst.htm) variable.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = MaxOrd("ColorLst")
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.MaxOrd("ColorLst") 
```

The following example shows all the colors of the ColorLst variable in a message box.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intNo
For intNo = 1 To MaxOrd("Colorlst")
 Call MsgBoxDisp ("Color No " & intNo & " is " & VEnum("ColorLst",intNo))
Next
```

[Copy script](javascript:void(0);)

```text
for intNo in range( 1, dd.MaxOrd("Colorlst") + 1): 
    dd.MsgBoxDisp ("Color No " + intNo + " is " + dd.VEnum("ColorLst",intNo)) 
```

#### Related Functions

[Command: AddUserCommandToEvent](../../comoff/addusercommandtoevent.htm) | [Command: RemoveUserCommandFromEvent](../../comoff/removeusercommandfromevent.htm) | [Command: VEnumIdx](../../comoff/venumidx.htm) | [Function: GetEnv](../functions/getenv.htm) | [Function: IdentifierType](../functions/identifiertype.htm) | [Function: Ord](../functions/ord.htm) | [Function: ScriptEvaluate](../functions/scriptevaluate.htm) | [Function: VEnum](../functions/venum.htm) | [Function: VIT](../functions/vit.htm) | [Function: VSA](../functions/vsa.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/maxv.htm language=enus -->
## TOPIC 00058: Function: MaxV

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/maxv.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/maxv.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: MaxV

### Function: MaxV

Determines the greater of two numbers.

```text
ReturnValue = MaxV(Value1,Value2)
```

#### Input Parameters

| Value1 | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |
| Value2 | Specifies a numeric value, a variable, or a data channel. |

#### Return Parameters

| ReturnValue | Returns numeric values. |
| --- | --- |

|  | Note Use the command ValMax instead of the function MaxV if you are not calculating quantity-based because the ValMax command is faster. |
| --- | --- |

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Command: ValEqual](../../comoff/valequal.htm) | [Command: ValEqualGT](../../comoff/valequalgt.htm) | [Command: ValEqualLT](../../comoff/valequallt.htm) | [Command: ValGT](../../comoff/valgt.htm) | [Command: ValLT](../../comoff/vallt.htm) | [Command: ValMax](../../comoff/valmax.htm) | [Command: ValMin](../../comoff/valmin.htm) | [Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MinV](../functions/minv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/minv.htm language=enus -->
## TOPIC 00059: Function: MinV

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/minv.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/minv.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: MinV

### Function: MinV

Determines the smaller of two numbers.

```text
ReturnValue = MinV(Value1,Value2)
```

#### Input Parameters

| Value1 | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |
| Value2 | Specifies a numeric value, a variable, or a data channel. |

#### Return Parameters

| ReturnValue | Returns numeric values. |
| --- | --- |

|  | Note Use the command ValMin instead of the function MinV if you are not calculating quantity-based because the ValMin command is faster. |
| --- | --- |

|  | The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Command: ValEqual](../../comoff/valequal.htm) | [Command: ValEqualGT](../../comoff/valequalgt.htm) | [Command: ValEqualLT](../../comoff/valequallt.htm) | [Command: ValGT](../../comoff/valgt.htm) | [Command: ValLT](../../comoff/vallt.htm) | [Command: ValMax](../../comoff/valmax.htm) | [Command: ValMin](../../comoff/valmin.htm) | [Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/mod.htm language=enus -->
## TOPIC 00060: Function: Mod

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/mod.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/mod.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Mod

### Function: Mod

Divides two numeric values as integers and returns the remainder. DIAdem only uses the DIAdem function Mod if you use the [FormulaCalc](../../comoff/formulacalc.htm) command in your script, otherwise DIAdem uses the VBS function [Mod](/csh?topicname=vbs/general/vbs_operators.htm), which rounds the input parameters to integers, divides the numbers,and returns the divider rest.

```text
ReturnValue = Dividend Mod Divisor
```

#### Input Parameters

| Dividend | Specifies a numeric value, a variable, or a data channel for the dividend. |
| --- | --- |
| Divisor | Specifies a numeric value, a variable, or a data channel for the divisor. |

#### Return Parameters

Returns the remainder as a numeric value.

#### Examples

The following example divides the values in each line of the Group1/Input and Group1/Reference data channels, and saves the remainders in the Group2/Result data channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call FormulaCalc ("Ch('Group2/Result'):= Ch('Group1/Input') Mod Ch('Group1/Reference')")
```

[Copy script](javascript:void(0);)

```text
dd.FormulaCalc ("Ch('Group2/Result'):= Ch('Group1/Input') Mod Ch('Group1/Reference')") 
```

The following example shows the differences between the DIAdem Mod function and the VBS Mod function:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call FormulaCalc  ("R1 := (e)Mod(Pi)")   '=> R1 = 2.71828182845905
Call Calculate ("R1 =  (e)Mod(Pi)")   '=> R1 = 0
```

[Copy script](javascript:void(0);)

```text
dd.FormulaCalc  ("R1 := (e)Mod(Pi)") #=> R1 = 2.71828182845905
dd.Calculate ("R1 =  (e)Mod(Pi)") #=> R1 = 0
```

|  | Note You must use the commands Calculate or FormulaCalc in scripts in order to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The first physical input quantity is arbitrary. The second input quantity must be dimensionless. The first physical input quantity and the result quantity are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/namesplit.htm language=enus -->
## TOPIC 00061: Function: FileNameSplit

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/namesplit.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/namesplit.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: FileNameSplit

### Function: FileNameSplit

Valid names: NameSplit

Extracts information from a text.

```text
ReturnValue = NameSplit(String, Type)
```

#### Input Parameters

| String | Specifies a text or a text variable that contains a filename with extension and path. |
| --- | --- |
| Type | Specifies the wildcard for the file information you want to extract: |
| Value Meaning PPath NFilename EFilename extension |  |
| Value | Meaning |
| P | Path |
| N | Filename |
| E | Filename extension |

#### Return Parameters

| ReturnValue | Returns the filename, the path, or the extension as text. The function returns an empty text if the specified text does not contain the information you want. |
| --- | --- |

#### Examples

The following examples extract various information from a file.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strMyResult
strMyResult = NameSplit("C:\Folder\Test.txt","P")    'strMyResult = C:\Folder\
strMyResult = NameSplit("C:\Folder\Test.txt","N")    'strMyResult = Test
strMyResult = NameSplit("C:\Folder\Test.txt","E")    'strMyResult = txt
strMyResult = NameSplit("C:\Folder\Test","E")       'strMyResult = ""
```

[Copy script](javascript:void(0);)

```text
strMyResult = dd.NameSplit("C 
\\Folder\\Test.txt","P")    'strMyResult = C:\\Folder\ 
strMyResult = dd.NameSplit("C:\\Folder\\Test.txt","N") #strMyResult = Test
strMyResult = dd.NameSplit("C:\\Folder\\Test.txt","E") #strMyResult = txt
strMyResult = dd.NameSplit("C:\\Folder\\Test","E") #strMyResult = ""
```

#### Related Functions

[Command: TTD](../../comoff/ttd.htm) | [Function: Char](../functions/char.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: Idx](../functions/idx.htm) | [Function: Len](../functions/len.htm) | [Function: PU](../functions/pu.htm) | [Function: Str](../functions/str.htm) | [Function: Textaddition (+)](../functions/tadd.htm) | [Function: TTR (Text to Real)](../functions/ttr.htm) | [Function: Val](../functions/val.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/not.htm language=enus -->
## TOPIC 00062: Function: NOT

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/not.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/not.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: NOT

### Function: NOT

Computes the logical negation.

```text
ReturnValue = NOT Value
```

#### Input Parameters

| Value | Specifies a Boolean value, a Boolean variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns Boolean values. TRUEFor the value FALSE FALSEFor the value TRUE 1For the value zero |
| --- | --- |
| TRUE | For the value FALSE |
| FALSE | For the value TRUE |
| 1 | For the value zero |

#### Examples

The following example checks the Group1/Input data channel for values. The result in the Group2/Result data channel returns the value 0 for every value, and returns the value 0 for the value 1.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= NOT (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= not (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note DIAdem only uses the DIAdem function Not if you use the FormulaCalc command otherwise DIAdem uses the VBS function Not. |
| --- | --- |

|  | The first and the second physical quantity must be the same. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: And](../functions/and.htm) | [Function: CTNV](../../comoff/ctnv.htm) | [Function: IIf](../../comoff/iif.htm) | [Function: OR](../functions/or.htm) | [Function: VIT](../functions/vit.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/notb.htm language=enus -->
## TOPIC 00063: Function: NotB

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/notb.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/notb.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: NotB

### Function: NotB

Negates the bits of the one-byte long binary representation of a decimal number. The NotB function converts the decimal numbers to one-byte long binary numbers, negates each bit, and reconverts the new binary number to a decimal number.

```text
ReturnValue = NotB(Value,ByteLength)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |
| ByteLength | Specifies a numeric value, a variable, or a data channel for the byte length.Value range 1 to 4 |

|  | Note If you enter numbers with decimal places for the parameters Value and ByteLength, DIAdem rounds the numbers to integers.From DIAdem 2014, the function no longer calculates the sum of the ByteLength input parameter. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. If the input value is NoValue, the NotB function returns the value NoValue. If the input parameter ByteLength is outside the value range, the function returns the value 0. |
| --- | --- |

#### Examples

The following example negates the one-byte long binary representation of the decimal number 10.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = NotB(10,1)    'intMyResult = 245
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.NotB(10,1) #intMyResult = 245
```

The following example switches the bits of the values in the Group1/Input data channel within the byte length given by the Group1/Reference data channel and saves the result in the new data channel Group2/Result.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= NotB (Ch(""Group1/Input""),Ch(""Group1/Reference""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= NotB (Ch(""Group1/Input""),Ch(""Group1/Reference""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The first physical input quantity is arbitrary. The second input quantity must be dimensionless. The first physical input quantity and the result quantity are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: AndB](../functions/andb.htm) | [Function: ClrB](../functions/clrb.htm) | [Function: GetB](../functions/getb.htm) | [Function: OrB](../functions/orb.htm) | [Function: SetB](../functions/setb.htm) | [Function: ShL](../functions/shl.htm) | [Function: ShR](../functions/shr.htm) | [Function: XOrB](../functions/xorb.htm) | [Variable: ApplicationLegacyBinaryOperations](/csh?topicname=varoff/applicationlegacybinaryoperations.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/or.htm language=enus -->
## TOPIC 00064: Function: OR

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/or.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/or.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: OR

### Function: OR

Executes the OR operation on two values.

```text
ReturnValue = Value1 OR Value2
```

#### Input Parameters

| Value1 | Specifies a Boolean value, a Boolean variable, or a data channel. |
| --- | --- |
| Value2 | Specifies a Boolean value, a Boolean variable, or a data channel. |

#### Return Parameters

| ReturnValue | Returns Boolean values. Value1 Value2Result TRUEorTRUETRUE TRUEorFALSETRUE FALSEor1TRUE FALSEor17TRUE TRUEor-100TRUE TRUEor0TRUE 0or1 TRUE FALSEorFALSEFALSE 0or00 0orFALSE0 |  |  |
| --- | --- | --- | --- |
| Value1 |  | Value2 | Result |
| TRUE | or | TRUE | TRUE |
| TRUE | or | FALSE | TRUE |
| FALSE | or | 1 | TRUE |
| FALSE | or | 17 | TRUE |
| TRUE | or | -100 | TRUE |
| TRUE | or | 0 | TRUE |
| 0 | or | 1 | TRUE |
| FALSE | or | FALSE | FALSE |
| 0 | or | 0 | 0 |
| 0 | or | FALSE | 0 |

#### Examples

The following example checks rowwise whether the two data channels contain values. If one of the two data channels has a value in the same row, the result in the new channel Group2/Result returns the value 1, and if both data channels have the value 0 in the same row, the result returns the value 0.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= (Ch(""Group1/Input"")) OR (Ch(""Group1/Reference""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= (Ch(""Group1/Input"")) or (Ch(""Group1/Reference""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note If you use the Or function without the Calculate command in your script, DIAdem uses the VBS operator Or, which computes two integer values bitwise. |
| --- | --- |

|  | The first and the second physical quantity must be the same. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: And](../functions/and.htm) | [Function: CTNV](../../comoff/ctnv.htm) | [Function: IIf](../../comoff/iif.htm) | [Function: NOT](../functions/not.htm) | [Function: VIT](../functions/vit.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/orb.htm language=enus -->
## TOPIC 00065: Function: OrB

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/orb.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/orb.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: OrB

### Function: OrB

Calculates the number resulting from the shared bits of two numbers. The OrB function converts the decimal numbers into binary numbers, determines the shared bits, and reconverts this binary number into a decimal number.

```text
ReturnValue = OrB(Value1, Value2)
```

#### Input Parameters

| Value1 | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |
| Value2 | Specifies a numeric value, a variable, or a data channel. |

|  | Note If you specify numbers with decimal places for the parameters Value1 and Value2, DIAdem rounds the numbers to integers. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. If the input value is NoValue, the OrB function returns the value NoValue. |
| --- | --- |

#### Examples

The following example calculates the shared bits of the two decimal numbers 12 and 16 and saves the corresponding decimal number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = OrB(16,12)    'intMyResult = 28
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.OrB(16,12) #intMyResult = 28
```

The following example calculates the shared bits of the values of two data channels rowwise and saves the decimal numbers in the data channel Group2/Result.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= OrB (Ch(""Group1/Input""),Ch(""Group1/Reference""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= OrB (Ch(""Group1/Input""),Ch(""Group1/Reference""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note You can also calculate the shared bits of two numbers with the VBS function Or. |
| --- | --- |

|  | The first and the second physical quantity must be the same. The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: AndB](../functions/andb.htm) | [Function: ClrB](../functions/clrb.htm) | [Function: GetB](../functions/getb.htm) | [Function: NotB](../functions/notb.htm) | [Function: SetB](../functions/setb.htm) | [Function: ShL](../functions/shl.htm) | [Function: ShR](../functions/shr.htm) | [Function: XOrB](../functions/xorb.htm) | [Variable: ApplicationLegacyBinaryOperations](/csh?topicname=varoff/applicationlegacybinaryoperations.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/ord.htm language=enus -->
## TOPIC 00066: Function: Ord

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/ord.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/ord.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Ord

### Function: Ord

Determines the ordinal number in the ASCII character set for the first character of a text, and determines the index of the current enumeration or dynamic enumeration term for [enumeration variables](/csh?topicname=genas/genauto/genauto_enumeration_list.htm) or [dynamic enumeration variables](/csh?topicname=genas/genauto/genauto_dynamic_enumeration_list.htm).

```text
ReturnValue = Ord(String [,Flag])
```

#### Input Parameters

| String | Specifies a text, or an enumeration or a dynamic enumeration variable. |
| --- | --- |
| [Flag] | Specifies the evaluation of the string. |
| Value Meaning 0 DIAdem checks in the standard setting whether the string is a text or a variable.If the string is a text, DIAdem evaluates the text.If the string is a variable, DIAdem evaluates the current content of the variable. 1 DIAdem evaluates the string as a text. |  |
| Value | Meaning |
| 0 | DIAdem checks in the standard setting whether the string is a text or a variable.If the string is a text, DIAdem evaluates the text.If the string is a variable, DIAdem evaluates the current content of the variable. |
| 1 | DIAdem evaluates the string as a text. |

#### Return Parameters

| ReturnValue | Returns an integer for the ASCII ordinal number of the first character in a string, or for the index of the current enumeration or dynamic enumeration term. The index of the first enumeration or dynamic enumeration term has the value 0. |
| --- | --- |

#### Examples

The following example determines the index of the term "TIF" in the variable [ExType](/csh?topicname=varoff/extype.htm).

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyValue
ExType = "TIF"
intMyValue = Ord("ExType")       'intMyValue = 3
```

[Copy script](javascript:void(0);)

```text
ExType = "TIF" 
intMyValue = dd.Ord("ExType") #intMyValue = 3
```

The following example evaluates a variable as a text and returns the ASCII code of the first letter E.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult 
ExType = "TIF"
intMyResult  = Ord("ExType",1)       'intMyResult  = 69
```

[Copy script](javascript:void(0);)

```text
ExType = "TIF" 
intMyResult  = dd.Ord("ExType",1) #intMyResult  = 69
```

|  | Note If you specify the variable name without quotation marks, DIAdem evaluates the current enumeration or dynamic enumeration term as a text. In this case the second example returns the value 84 as the result for the letter T. |
| --- | --- |

#### Related Functions

[Command: AddUserCommandToEvent](../../comoff/addusercommandtoevent.htm) | [Command: RemoveUserCommandFromEvent](../../comoff/removeusercommandfromevent.htm) | [Command: VEnumIdx](../../comoff/venumidx.htm) | [Function: GetEnv](../functions/getenv.htm) | [Function: IdentifierType](../functions/identifiertype.htm) | [Function: MaxOrd](../functions/maxord.htm) | [Function: ScriptEvaluate](../functions/scriptevaluate.htm) | [Function: VEnum](../functions/venum.htm) | [Function: VIT](../functions/vit.htm) | [Function: VSA](../functions/vsa.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/pno.htm language=enus -->
## TOPIC 00067: Function: PNo

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/pno.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/pno.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: PNo

### Function: PNo

Determines the row in a numeric channel or a text channel, of which the contents are closest to a specified value or text.

```text
ReturnValue = PNo(Channel,Value)
```

#### Input Parameters

| ChannelName | Specifies the channel. |
| --- | --- |
| Value | Specifies the value or text to search for. |

#### Return Parameters

| ReturnValue | Returns the number of the first row with contents that are closest to the specified value or text. |
| --- | --- |

#### Examples

The following example searches in the numeric channel Group1/Input for the row with contents closest to the value 77.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = PNo("Group1/Input",77)
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.PNo("Group1/Input",77) 
```

The following example searches in the text channel Group1/Input for the row with contents that are closest to the text test.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = PNo("Group1/Input","test")
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.PNo("Group1/Input","test") 
```

#### Related Functions

[Command: ChnFind](../../comoff/chnfind.htm) | [Command: ChnFindReverse](../../comoff/chnfindreverse.htm) | [Function: CCh](../functions/cch.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: Find](../functions/find.htm) | [Function: FindReverse](../functions/findreverse.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/potenz.htm language=enus -->
## TOPIC 00068: Function: ^

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/potenz.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/potenz.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ^

### Function: ^

Calculates the power of one number to another.

```text
ReturnValue = Base ^ Exponent
```

#### Input Parameters

| Base | Specifies a numeric value, a variable, or a data channel as the base. |
| --- | --- |
| Exponent | Specifies a numeric value, a variable, or a data channel as the exponent. |

#### Return Parameters

| ReturnValue | Returns numeric values. |
| --- | --- |

#### Examples

The following example exponentiates the values of the Group1/Input data channel to the base 2 and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= 2 ^ Ch(""Group1/Input"")")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= 2 ^ Ch(""Group1/Input"")") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note If you use the ^ operator in your script without the Calculate command, DIAdem applies the VBS exponential operator ^. |
| --- | --- |

#### Related Functions

[Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/pu.htm language=enus -->
## TOPIC 00069: Function: PU

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/pu.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/pu.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: PU

### Function: PU

Formats the contents of a text variable.

```text
ReturnValue = PU(TextVarName1, TextVarName2)
```

#### Input Parameters

| TextVarName1 | Specifies a text variable that contains either the text to be formatted or the name of a DIAdem variable. Separate the individual values with the @ character. |
| --- | --- |
| TextVarName2 | Specifies the text variable with the format instructions. You can format texts flush left with the wildcard L and flush right with the wildcard R. |

#### Return Parameters

Returns a formatted text.

#### Examples

The following example formats the contents of the text variable strValue according to the format instructions in the text variable strFormat.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strValue, strFormat, strMyResult
strValue = "123.654@789.345"
strFormat = "dddd.d ddd.ddd"
strMyResult = PU(strValue,strFormat)      'strMyResult = 123.7 789.345
```

[Copy script](javascript:void(0);)

```text
strValue = "123.654@789.345" 
strFormat = "ddd+nbsp;dddd" 
strMyResult = PU(strValue,strFormat) #strMyResult = 123.7 789.345
```

The following example refers to three variables to be formatted, in the strValue variable.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
L1 = 1
Dim strValue, strFormat, strMyResult
strValue = "CN(L1)@ChD(1,L1)@CL(L1)"
strFormat = "LLLL ddd.d dddd"
strMyResult = PU(strValue,strFormat)    'Time 123.5 1024
```

[Copy script](javascript:void(0);)

```text
L1 = 1 
strValue = "CN(L1)@ChD(1,L1)@CL(L1)" 
strFormat = "LLLL+nbsp;dd+nbsp;dddd" 
strMyResult = PU(strValue,strFormat) #Time 123.5 1024
```

|  | Note If you transfer variable names to text variables, you must use DIAdem variables. |
| --- | --- |

|  | Note Use the Str function to convert a numeric value into a text or to format a text. |
| --- | --- |

#### Related Functions

[Command: TTD](../../comoff/ttd.htm) | [Function: Char](../functions/char.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: FileNameSplit](../functions/namesplit.htm) | [Function: Idx](../functions/idx.htm) | [Function: Len](../functions/len.htm) | [Function: Str](../functions/str.htm) | [Function: Textaddition (+)](../functions/tadd.htm) | [Function: TTR (Text to Real)](../functions/ttr.htm) | [Function: Val](../functions/val.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/rad.htm language=enus -->
## TOPIC 00070: Function: Rad

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/rad.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/rad.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Rad

### Function: Rad

Converts an angle from degrees to radians.

```text
ReturnValue = Rad(Angle) 
```

#### Input Parameters

| Angle | Specifies a numeric value or a variable as an angle value, or a data channel that contains angle values. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns angle values with the unit radians. |
| --- | --- |

#### Examples

The following example converts the angle value 45° into radians.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = Rad(45)    'intMyResult = 0.785398163397448
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.Rad(45) #intMyResult = 0.785398163397448
```

The following example converts the angle values of the Group1/Input data channel to radians and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Rad (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Rad (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note Use the Deg function to convert angle values from radians to degrees. |
| --- | --- |

|  | The input quantity must have the unit deg. The result quantity has the physical quantity Plane angle.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/random.htm language=enus -->
## TOPIC 00071: Function: Random

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/random.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/random.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Random

### Function: Random

Determines random numbers in the value range from zero up to a specified value.

```text
ReturnValue = Random(Limit)
```

#### Input Parameters

| Limit | Specifies a numeric value, a variable, or a data channel, to limit the value range. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns random numeric values. |
| --- | --- |

#### Examples

The following example determines a random number between 0 and 5.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = Random(5) 
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.Random(5) 
```

The following example determines for each value of the Group1/Input data channel a random value between 0 and the channel value, and saves the random numbers in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Random (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Random (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/rnd.htm language=enus -->
## TOPIC 00072: Function: Rnd

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/rnd.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/rnd.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Rnd

### Function: Rnd

Determines random numbers in the value range from zero up to a specified value. DIAdem uses the DIAdem function Rnd only if you use the [FormulaCalc](../../comoff/formulacalc.htm) command in your script otherwise DIAdem uses the VBS function [Rnd](/csh?topicname=vbs/methods/vbs_method_rnd_globalobj.htm).Use the [Random](../functions/random.htm) function in scripts.

```text
ReturnValue = Rnd([Limit])
```

#### Input Parameters

| Limit | Specifies a numeric value, a variable, or a data channel, to limit the value range. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns random numeric values. |
| --- | --- |

#### Examples

The following example determines for each value of the Group1/Input data channel a random value between 0 and the channel value, and saves the random numbers in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call FormulaCalc ("Ch('Group2/Result'):= Rnd(Ch('Group1/Input'))")
```

[Copy script](javascript:void(0);)

```text
dd.FormulaCalc ("Ch('Group2/Result'):= Rnd(Ch('Group1/Input'))") 
```

|  | Note You must use the commands Calculate or FormulaCalc in scripts in order to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/round.htm language=enus -->
## TOPIC 00073: Function: Round

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/round.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/round.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Round

### Function: Round

Rounds off a number to the nearest integer. DIAdem uses the DIAdem function Round only if you use the [FormulaCalc](../../comoff/formulacalc.htm) command in your script otherwise DIAdem uses the VBS function [Round](/csh?topicname=vbs/methods/vbs_method_round_globalobj.htm).

```text
ReturnValue = Round(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. |
| --- | --- |

#### Examples

The following example rounds off the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call FormulaCalc ("Ch('Group2/Result'):= Round ('Group1/Input')")
```

[Copy script](javascript:void(0);)

```text
dd.FormulaCalc ("Ch('Group2/Result'):= Round ('Group1/Input')") 
```

|  | Note You must use the commands Calculate or FormulaCalc in scripts in order to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/rtp.htm language=enus -->
## TOPIC 00074: Function: RTP (Real To Part of Date)

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/rtp.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/rtp.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: RTP (Real To Part of Date)

### Function: RTP (Real To Part of Date)

Converts a number in DIAdem double time format into a text in time format and determines from the calculated date partial date information based on the variable [ApplicationTimebaseHighResolution](/csh?topicname=varoff/applicationtimebasehighresolution.htm).

```text
ReturnValue = RTP(Value,Text)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel containing the elapsed seconds. You can also specify a variant value with the subtype Date such as the functions CDate or Now return.Note If you save time values in DIAdem that are VBS VBDate subtype variables, the high resolution is lost. VBS only offers time values for this data type which provides only a limited resolution. |
| --- | --- |
|  | Note If you save time values in DIAdem that are VBS VBDate subtype variables, the high resolution is lost. VBS only offers time values for this data type which provides only a limited resolution. |
| Text | Specifies the wildcard of the time format for the date information you want to extract, such as the day or year. |

#### Return Parameters

| ReturnValue | Returns the date information you want. The RTP function returns the result 0 for negative values. |
| --- | --- |

#### Example

The following example converts the values of the Group1/Input data channel into time format, determines the months, and saves this result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= RTP (Ch(""Group1/Input""), ""M"")")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= RTP (Ch(""Group1/Input""), ""M"")") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The physical input quantity is arbitrary. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/rtt.htm language=enus -->
## TOPIC 00075: Function: RTT (Real to Text)

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/rtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/rtt.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: RTT (Real to Text)

### Function: RTT (Real to Text)

Converts a number that exists in the DIAdem double time format into a text. The interpretation of the number depends on the variable [ApplicationTimebaseHighResolution](/csh?topicname=varoff/applicationtimebasehighresolution.htm).

```text
ReturnValue = RTT(Value[,Format])
```

#### Input Parameters

| Value | Specifies a numeric value or a variable in DIAdem double time format.Note If you specify Variant values with the Date subtype, such as those returned by the CDate or Now functions, these values are automatically converted to DIAdem time format and lose their high resolution. |
| --- | --- |
|  | Note If you specify Variant values with the Date subtype, such as those returned by the CDate or Now functions, these values are automatically converted to DIAdem time format and lose their high resolution. |
| [Format] | Specifies a format definition for the time format. |

#### Return Parameters

| ReturnValue | Returns the date as text. |
| --- | --- |

The [TTR](../functions/ttr.htm) function converts a text in time format into a number in DIAdem double time format.

#### Examples

The following example converts a positive number into time format.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strMyResult
strMyResult = RTT(14*3600)
```

[Copy script](javascript:void(0);)

```text
strMyResult = dd.RTT(14*3600) 
```

The following example formats the current date.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBox(RTT(Now,"#YYYY/MM/DD"))
```

[Copy script](javascript:void(0);)

```text
print(dd.RTT(Now,"#YYYY/MM/DD")) 
```

|  | The first physical input quantity is arbitrary. The second input quantity must be dimensionless. The first physical input quantity and the result quantity are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Command: ChnConvertNumericToTime](../../comoff/chnconvertnumerictotime.htm) | [Command: ChnConvertTimeToNumeric](../../comoff/chnconverttimetonumeric.htm) | [Command: ConvertTimeType](../../comoff/converttimetype.htm) | [Command: TTD](../../comoff/ttd.htm) | [Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: TTR (Text to Real)](../functions/ttr.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/scriptevaluate.htm language=enus -->
## TOPIC 00076: Function: ScriptEvaluate

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/scriptevaluate.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/scriptevaluate.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ScriptEvaluate

### Function: ScriptEvaluate

Determines the contents of a [user command](/csh?topicname=genshell/genshell/genshell_user_commands.htm) in the DIAdem Calculator.

```text
ReturnValue = ScriptEvaluate(UserCmdName)
```

#### Input Parameters

| UserCmdName | Specifies a user command registered in DIAdem. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns the current contents of the user command as a text. |
| --- | --- |

#### Examples (Calculator)

The following example assumes that you have registered the script in DIAdem with the user command MyCommand.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Function MyCommand(MyPar)
  MyCommand = "Value: " & MyPar
End Function
```

[Copy script](javascript:void(0);)

```text
def MyCommand(MyPar): 
    MyCommand = "Value: " + MyPar 
    return MyCommand
```

The following example line determines the contents of the user command MyCommand.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
T1 = ScriptEvaluate("MyCommand(45.3)")    'T1 = Value: 45.3
```

[Copy script](javascript:void(0);)

```text
T1 = dd.ScriptEvaluate("MyCommand(45.3)") #T1 = Value: 45.3
```

|  | Note You cannot use the ScriptEvaluate function in scripts. |
| --- | --- |

|  | Note Refer to Using User Commands for information on how to define your own commands. |
| --- | --- |

#### Related Functions

[Command: AddUserCommandToEvent](../../comoff/addusercommandtoevent.htm) | [Command: RemoveUserCommandFromEvent](../../comoff/removeusercommandfromevent.htm) | [Command: VEnumIdx](../../comoff/venumidx.htm) | [Function: GetEnv](../functions/getenv.htm) | [Function: IdentifierType](../functions/identifiertype.htm) | [Function: MaxOrd](../functions/maxord.htm) | [Function: Ord](../functions/ord.htm) | [Function: VEnum](../functions/venum.htm) | [Function: VIT](../functions/vit.htm) | [Function: VSA](../functions/vsa.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/setb.htm language=enus -->
## TOPIC 00077: Function: SetB

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/setb.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/setb.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: SetB

### Function: SetB

Sets a specific bit in the binary representation of a decimal number. The SetB function converts a decimal number to a binary number, sets the specified bit, and reconverts the new binary number to a decimal number.

```text
ReturnValue = SetB(Value,BitIndex)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |
| BitIndex | Specifies a numeric value, a variable, or a data channel for the index of the bit you want to check.Value range 0 to 31 |

|  | Note If you enter numbers with decimal places for the parameters Value and BitIndex, DIAdem rounds the numbers to integers.From DIAdem 2014, the function no longer calculates the sum of the BitIndex input parameter. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. If the indexed bit is already set, which means it has the value 1, its value remains 1. If the input value is NoValue, the SetB function returns the value NoValue. If the input parameter BitIndex is outside the value range, the function returns the value of the input parameter Value. |
| --- | --- |

#### Examples

The following example sets the seventh bit in the binary representation of the decimal number 10.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = SetB(10,6)    'intMyResult = 74
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.SetB(10,6) #intMyResult = 74
```

The following example sets the bits, indexed by the Group1/Reference data channel, of the values in the Group1/Input data channel, and saves the new decimal numbers in the new data channel Group2/Result. DIAdem skips values of the Group1/Reference index channel that are higher than 31.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= SetB (Ch(""Group1/Input""),Ch(""Group1/Reference""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= SetB (Ch(""Group1/Input""),Ch(""Group1/Reference""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The first physical input quantity is arbitrary. The second input quantity must be dimensionless. The first physical input quantity and the result quantity are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: AndB](../functions/andb.htm) | [Function: ClrB](../functions/clrb.htm) | [Function: GetB](../functions/getb.htm) | [Function: NotB](../functions/notb.htm) | [Function: OrB](../functions/orb.htm) | [Function: ShL](../functions/shl.htm) | [Function: ShR](../functions/shr.htm) | [Function: XOrB](../functions/xorb.htm) | [Variable: ApplicationLegacyBinaryOperations](/csh?topicname=varoff/applicationlegacybinaryoperations.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/shl.htm language=enus -->
## TOPIC 00078: Function: ShL

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/shl.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/shl.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ShL

### Function: ShL

Shifts the bits in the binary representation of a decimal number to the left by a specific number of places. The ShL function converts the decimal number into a binary number, inserts on the right as many zeros as you specify, and reconverts the binary number into a decimal number.

```text
ReturnValue = ShL(Value, Digits)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |
| Digits | Specifies a numeric value, a variable, or a data channel for the number of places you want to shift.Value range 0 to 31 |

|  | Note If you enter numbers with decimal places for the parameters Value and Digits, DIAdem rounds off the numbers to integers.From DIAdem 2014, the function no longer calculates the sum of the Digits input parameter. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. If the input value is NoValue, the ShLB function returns the value NoValue. If the input parameter Digits is outside the value range, the function returns the value 0. |
| --- | --- |

#### Examples

The following example adds two zeros to the binary representation of the decimal number 13 and saves the new decimal number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = ShL(13,2)    'intMyResult = 52
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.ShL(13,2) #intMyResult = 52
```

The following example adds bits on the right of the binary representation of the values in the Group1/Input data channel. The number of places added is specified in the Group1/Reference data channel. The example saves the new decimal numbers in the data channel Group2/Result.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= ShL (Ch(""Group1/Input""),Ch(""Group1/Reference""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= ShL (Ch(""Group1/Input""),Ch(""Group1/Reference""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The first physical input quantity is arbitrary. The second input quantity must be dimensionless. The first physical input quantity and the result quantity are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: AndB](../functions/andb.htm) | [Function: ClrB](../functions/clrb.htm) | [Function: GetB](../functions/getb.htm) | [Function: NotB](../functions/notb.htm) | [Function: OrB](../functions/orb.htm) | [Function: SetB](../functions/setb.htm) | [Function: ShR](../functions/shr.htm) | [Function: XOrB](../functions/xorb.htm) | [Variable: ApplicationLegacyBinaryOperations](/csh?topicname=varoff/applicationlegacybinaryoperations.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/shr.htm language=enus -->
## TOPIC 00079: Function: ShR

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/shr.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/shr.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: ShR

### Function: ShR

Shifts the bits in the binary representation of a decimal number a specific number of places to the right. The ShR function converts the decimal number into a binary number, deletes the specified number of places on the right of the binary number, and reconverts the new binary number into a decimal number.

```text
ReturnValue = ShR(Value,Digits)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |
| Digits | Specifies a numeric value, a variable, or a data channel for the number of places you want to delete.Value range 0 to 31 |

|  | Note If you enter numbers with decimal places for the parameters Value and BitIndex, DIAdem rounds the numbers to integers.From DIAdem 2014, the function no longer calculates the sum of the Digits input parameter. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. If the input value is NoValue, the ShRB function returns the value NoValue. If the input parameter Digits is outside the value range, the function returns the value 0. |
| --- | --- |

#### Examples

The following example deletes the last two bits of the binary representation of the decimal number 13 and saves the new decimal number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = ShR(13,2)   'intMyResult = 3
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.ShR(13,2) #intMyResult = 3
```

The following example deletes bits on the right of the binary representation of the values in the Group1/Input data channel. The number of places deleted is specified in the Group1/Reference data channel. The example saves the new decimal numbers in the data channel Group2/Result.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= ShR (Ch(""Group1/Input""),Ch(""Group1/Reference""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= ShR (Ch(""Group1/Input""),Ch(""Group1/Reference""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The first physical input quantity is arbitrary. The second input quantity must be dimensionless. The first physical input quantity and the result quantity are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: AndB](../functions/andb.htm) | [Function: ClrB](../functions/clrb.htm) | [Function: GetB](../functions/getb.htm) | [Function: NotB](../functions/notb.htm) | [Function: OrB](../functions/orb.htm) | [Function: SetB](../functions/setb.htm) | [Function: ShL](../functions/shl.htm) | [Function: XOrB](../functions/xorb.htm) | [Variable: ApplicationLegacyBinaryOperations](/csh?topicname=varoff/applicationlegacybinaryoperations.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/sign.htm language=enus -->
## TOPIC 00080: Function: Sign

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/sign.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/sign.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Sign

### Function: Sign

Specifies the sign of a number.

```text
ReturnValue = Sign(Value) 
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Receives the sign of number. The value is -1 for negative values, 0 for the value 0, and 1 for positive values. For invalid values the value is NoValue. |
| --- | --- |

#### Examples

The following example determines the sign for the value -Pi.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim lngMyResult
lngMyResult = Sign(-Pi)    'lngMyResult = -1
```

[Copy script](javascript:void(0);)

```text
lngMyResult = Sign(-Pi) #lngMyResult = -1
```

The following example determines the signs of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Sign(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Sign(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The physical input quantity is arbitrary. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/sin.htm language=enus -->
## TOPIC 00081: Function: Sin

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/sin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/sin.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Sin

### Function: Sin

Calculates the sine of a number.

```text
ReturnValue = Sin(Value) 
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel that contains the angles in radians. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns numeric values ranging from -1 to +1. |
| --- | --- |

#### Examples

The following example calculates the sine of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Sin(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Sin(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note DIAdem only uses the DIAdem function Sin if you use the FormulaCalc command otherwise DIAdem uses the VBS function Sin. |
| --- | --- |

|  | The input quantity must have the physical quantity Plane angle. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/sinh.htm language=enus -->
## TOPIC 00082: Function: SinH

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/sinh.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/sinh.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: SinH

### Function: SinH

Calculates the hyperbolic sine of a number.

```text
ReturnValue = SinH(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel that contains the angles in radians. |
| --- | --- |

#### Output Parameters

| ReturnValue | Returns numeric values. |
| --- | --- |

#### Examples

The following example calculates the hyperbolic sine of a number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = SinH(1.9143)    'dblMyResult = 3.31737229713868  
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.SinH(1.9143) #dblMyResult = 3.31737229713868
```

The following example calculates the hyperbolic sine of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= SinH(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= SinH(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must have the physical quantity Plane angle. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: Tan](../functions/tan.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/snd.htm language=enus -->
## TOPIC 00083: Function: SND

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/snd.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/snd.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: SND

### Function: SND

Calculates the function value of the standard normal distribution for a number.

```text
ReturnValue = SND(Value) 
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns function values of the standard normal distribution. |
| --- | --- |

#### Examples

The following example determines the function value of the standard normal distribution for the value 0.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = SND(0)    'intMyResult = 0.5
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.SND(0) #intMyResult = 0.5
```

The following example determines the function values of the standard normal distribution for the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= SND (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= SND (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The physical input quantity is arbitrary. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/sqr.htm language=enus -->
## TOPIC 00084: Function: Sqr

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/sqr.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/sqr.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Sqr

### Function: Sqr

Calculates the square of a number. DIAdem uses the DIAdem function Sqr if you use the [FormulaCalc](../../comoff/formulacalc.htm) command in your script, otherwise DIAdem uses the VBS function [Sqr](/csh?topicname=vbs/methods/vbs_method_sqr_globalobj.htm), which calculates the square root.

```text
ReturnValue = SQR(Value) 
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns positive values. |
| --- | --- |

The following example squares the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call FormulaCalc ("Ch('Group2/Result'):= SQR ('Group1/Input')")
```

[Copy script](javascript:void(0);)

```text
dd.FormulaCalc ("Ch('Group2/Result'):= SQR ('Group1/Input')") 
```

|  | Note You must use the commands Calculate or FormulaCalc in scripts in order to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | DIAdem specifies the physical result quantity with the physical dimensions of the input quantities.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/sqrt.htm language=enus -->
## TOPIC 00085: Function: Sqrt

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/sqrt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/sqrt.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Sqrt

### Function: Sqrt

Calculates the square root of a number.

```text
ReturnValue = Sqrt(Value)
```

#### Input Parameters

| Value | Specifies a positive numeric value, a variable that contains a positive value, or a data channel that contains positive values. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns positive numeric values. |
| --- | --- |

#### Examples

The following example calculates the square root of a number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = Sqrt(6.5109)    'intMyResult = 2.55164652724471
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.Sqrt(6.5109) #intMyResult = 2.55164652724471
```

The following example calculates the square root of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Sqrt (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Sqrt (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note You also can use the VBS function Sqr to calculate the square root of a value or of a variable in a script. |
| --- | --- |

|  | DIAdem specifies the physical result quantity with the physical dimensions of the input quantities.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Trunc](../functions/trunc.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/str.htm language=enus -->
## TOPIC 00086: Function: Str

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/str.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/str.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Str

### Function: Str

Converts a numeric value into a text or formats a text.

```text
ReturnValue = Str(String, [Format])
```

#### Input Parameters

| String | Specifies a numeric value, a text, or a variable. |  |
| --- | --- | --- |
| [Format] | Specifies the output format of the string. String Format Example Numeric valueNumeric variable Display format according to the format instructions d.dd — Decimal with two places after the decimal point TextText variable L for text flush to the leftR for text flush to the right R:10 — Flush to the right and ten characters longL:5 — Flush to the left and five characters long Time valuesVariant value with the subtype Date Display format according to the format instructions for time values #MM/DD/YYYY hh:nn — Date with hours and minutes specification. |  |
| String | Format | Example |
| Numeric valueNumeric variable | Display format according to the format instructions | d.dd — Decimal with two places after the decimal point |
| TextText variable | L for text flush to the leftR for text flush to the right | R:10 — Flush to the right and ten characters longL:5 — Flush to the left and five characters long |
| Time valuesVariant value with the subtype Date | Display format according to the format instructions for time values | #MM/DD/YYYY hh:nn — Date with hours and minutes specification. |

#### Return Parameters

| ReturnValue | Returns a formatted text. If you specify a format that has less places after the decimal point than the number to be converted, DIAdem rounds off the result. |
| --- | --- |

#### Examples

The following example formats and converts a numeric value with a place after the decimal point.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sMyResult
sMyResult = Str(123.456,"d.d")  'sMyResult = "123.5"
```

[Copy script](javascript:void(0);)

```text
sMyResult = dd.Str(123.456,"d.d") #sMyResult = "123.5"
```

The following example formats a text flush right and fills the rest of the specified places with blanks.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sMyResult
sMyResult = Str("DIAdem", "R:10")    'sMyResult = "    DIAdem"
```

[Copy script](javascript:void(0);)

```text
sMyResult = dd.Str("DIAdem", "R:10") #sMyResult = "    DIAdem"
```

The following example formats a text with leading zeros.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(Str(2.34,"0dd.dd")) ' => "02.34"
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.Str(2.34,"0dd")) # => "02.34"
```

The first example determines the current calendar week and the second example formats the current date.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strCurrWeek, strMyDate
strCurrWeek = Str(TTR(CurrDate),"#k")  
strMyDate   = Str((Now),"#YYYY, DD.T")
```

[Copy script](javascript:void(0);)

```text
strCurrWeek = dd.Str(dd.TTR(dd.CurrDate),"#k")   
strMyDate   = dd.Str((Now),"#YYYY, DD.T") 
```

|  | Note Some variables, for example CurrTime, CurrDate, and CurrDateTime, return time values as text. You can use the TTR function to convert these texts to numeric values. |
| --- | --- |

|  | Note Use the PU function to format the contents of a text or of a text variable. |
| --- | --- |

#### Related Functions

[Command: TTD](../../comoff/ttd.htm) | [Function: Char](../functions/char.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: FileNameSplit](../functions/namesplit.htm) | [Function: Idx](../functions/idx.htm) | [Function: Len](../functions/len.htm) | [Function: PU](../functions/pu.htm) | [Function: Textaddition (+)](../functions/tadd.htm) | [Function: TTR (Text to Real)](../functions/ttr.htm) | [Function: Val](../functions/val.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/tadd.htm language=enus -->
## TOPIC 00087: Function: Textaddition (+)

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/tadd.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/tadd.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

[Calculator Functions](../functions_general.htm) > [Text Functions](../functions/functions_text_overview.htm) > Function: Textaddition (+)

### Function: Textaddition (+)

Links texts together to form a new text.

```text
ReturnValue = String1 + String2
```

#### Input Parameters

| String1 | Specifies a text or the name of a text variable. |
| --- | --- |
| String2 | Specifies a text or the name of a text variable. |

#### Return Parameters

| ReturnValue | Returns a text. |
| --- | --- |

#### Examples

The following example links the contents of two text variables.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
T1 = "DIA"
T2 = "dem"
Call Calculate ("T1 = T1 + T2")    'T1 = DIAdem
```

[Copy script](javascript:void(0);)

```text
T1 = "DIA" 
T2 = "dem" 
dd.Calculate ("T1 = T1 + T2") #T1 = DIAdem
```

|  | Note Use the VBS link operator & to link texts in scripts. |
| --- | --- |

#### Related Functions

[Command: TTD](../../comoff/ttd.htm) | [Function: Char](../functions/char.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: FileNameSplit](../functions/namesplit.htm) | [Function: Idx](../functions/idx.htm) | [Function: Len](../functions/len.htm) | [Function: PU](../functions/pu.htm) | [Function: Str](../functions/str.htm) | [Function: TTR (Text to Real)](../functions/ttr.htm) | [Function: Val](../functions/val.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/tan.htm language=enus -->
## TOPIC 00088: Function: Tan

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/tan.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/tan.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Tan

### Function: Tan

Calculates the tangent of a number.

```text
ReturnValue = Tan(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel that contains the angles in radians. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns numeric values. |
| --- | --- |

#### Examples

The following example calculates the tangent of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Tan(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Tan(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note DIAdem only uses the DIAdem function Tan if you use the FormulaCalc command in your script otherwise DIAdem uses the VBS function Tan. |
| --- | --- |

|  | The input quantity must have the physical quantity Plane angle. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: TanH](../functions/tanh.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/tanh.htm language=enus -->
## TOPIC 00089: Function: TanH

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/tanh.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/tanh.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: TanH

### Function: TanH

Calculates the hyperbolic tangent of a number.

```text
ReturnValue = TanH(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel that contains the angles in radians. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns numeric values. |
| --- | --- |

#### Examples

The following example calculates the hyperbolic tangent of a number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = TanH(1.9143)    'intMyResult = 0.957445
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.TanH(1.9143) #intMyResult = 0.957445
```

The following example calculates the hyperbolic tangent of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= TanH(Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= TanH(Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | The input quantity must have the physical quantity Plane angle. The physical result quantity is dimensionless.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ArcCos](../functions/arccos.htm) | [Function: ArcCot](../functions/arccot.htm) | [Function: ArcSin](../functions/arcsin.htm) | [Function: ArcTan](../functions/arctan.htm) | [Function: ArcTanH](../functions/arctanh.htm) | [Function: ATan2](../functions/atan2.htm) | [Function: ATanK](../functions/atank.htm) | [Function: Cos](../functions/cos.htm) | [Function: CosH](../functions/cosh.htm) | [Function: Cot](../functions/cot.htm) | [Function: Sin](../functions/sin.htm) | [Function: SinH](../functions/sinh.htm) | [Function: Tan](../functions/tan.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/textfileclose.htm language=enus -->
## TOPIC 00090: Function: TextFileClose

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/textfileclose.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/textfileclose.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: TextFileClose

### Function: TextFileClose

Closes a text file.

```text
ReturnValue = TextFileClose(TextFileHandle)
```

#### Input Parameters

| TextFileHandle | Specifies the handle of the text file.Use the return value of the TextFileOpen function. If you enter -1, DIAdem closes all text files opened with the TextFileOpen command.If you do not specify a path, DIAdem searches for the text file in the DIAdem folder. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns a numeric value. If an error occurs when the text file closes, the function returns the value -1. |
| --- | --- |

#### Examples

The following example creates a text file in ANSI code, writes twenty lines in this file, and closes it.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim LineNo, intMyHandle, intMyText, intMyError
intMyHandle = TextFileOpen("NewText.txt",eTextFileAttributeCreate OR eTextFileAttributeWrite OR eTextFileAttributeANSI) 
For LineNo = 1 To 20
  intMyText= TextfileWriteLn(intMyHandle, "Line " & LineNo)
Next
intMyError = TextFileClose(intMyHandle)
```

[Copy script](javascript:void(0);)

```text
intMyHandle = dd.TextFileOpen("NewText.txt",eTextFileAttributeCreate or eTextFileAttributeWrite or eTextFileAttributeANSI) 
for LineNo in range( 1, 20 + 1): 
    intMyText= dd.TextfileWriteLn(intMyHandle, "Line " + LineNo) 
intMyError = dd.TextFileClose(intMyHandle) 
```

#### Related Functions

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm) | [Command: TextFileEncoding](../../comoff/textfileencoding.htm) | [Command: TextFileEOL](../../comoff/textfileeol.htm) | [Function: FR](../functions/fr.htm) | [Function: TextFileEOF](../functions/textfileeof.htm) | [Function: TextFileError](../functions/textfileerror.htm) | [Function: TextFileErrorTxt](../functions/textfileerrortxt.htm) | [Function: TextFileSeek](../functions/textfileseek.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/textfileeof.htm language=enus -->
## TOPIC 00091: Function: TextFileEOF

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/textfileeof.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/textfileeof.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: TextFileEOF

### Function: TextFileEOF

Checks whether DIAdem has reached the end of a file when reading a text file linewise.

```text
ReturnValue = TextFileEOF(TextFileHandle)
```

#### Input Parameters

| TextFileHandle | Specifies the handle of the text file.Use the return value of the TextFileOpen function. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns a Boolean value. |
| --- | --- |

#### Examples

The following example opens the text file NewText.txt and reads the file linewise to the end. DIAdem displays each line of text in a message box.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyHandle, strMyText, intMyError
intMyHandle = TextFileOpen("NewText.txt", eTextFileAttributeRead)
Do While Not TextFileEOF(intMyHandle)
  strMyText = TextFileReadLn(intMyHandle)
  Call MsgBoxDisp(strMyText,"MB_OK")
Loop
intMyError = TextFileClose(intMyHandle)
```

[Copy script](javascript:void(0);)

```text
intMyHandle = dd.TextFileOpen("NewText.txt", eTextFileAttributeRead) 
while Do : 
    strMyText = dd.TextFileReadLn(intMyHandle) 
    dd.MsgBoxDisp(strMyText,"MB_OK") 
intMyError = dd.TextFileClose(intMyHandle) 
```

#### Related Functions

[Command: TextFileEncoding](../../comoff/textfileencoding.htm) | [Command: TextFileEOL](../../comoff/textfileeol.htm) | [Function: FR](../functions/fr.htm) | [Function: TextFileError](../functions/textfileerror.htm) | [Function: TextFileErrorTxt](../functions/textfileerrortxt.htm) | [Function: TextFileSeek](../functions/textfileseek.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/textfileerror.htm language=enus -->
## TOPIC 00092: Function: TextFileError

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/textfileerror.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/textfileerror.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: TextFileError

### Function: TextFileError

Checks whether an error occurs when you open, write, or read a text file.

```text
ReturnValue = TextFileError(TextFileHandle)
```

#### Input Parameters

| TextFileHandle | Specifies the handle of the text file.Use the return value of the TextFileOpen function. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns a numeric value. If an error occurs, the function returns the value -1. |
| --- | --- |

#### Examples

The following example attempts to open the text file OldText.txt. However, DIAdem does not find this text file in the DIAdem folder and the [TextFileOpen](../../comoff/textfileopen.htm) function returns an error. The example then jumps into the subroutine for dealing with errors and displays the error number and the associated error text.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyHandle, intMyError
intMyHandle = TextFileOpen("OldText.txt",eTextFileAttributeRead)
If intMyHandle = -1 Then
  Call MsgError(intMyHandle)
Else
  Call MsgBoxDisp( "Text file can be read.",_
                   "MB_OK","MsgTypeInformation",,5) 
  intMyError = TextFileClose(intMyHandle)
End If

Sub MsgError(FileNo)
 Call MsgboxDisp("Error number: " & TextFileError(FileNo) & VbCrLf & _
 "error message: " & TextFileErrorTxT(FileNo)) 'Show error number and error message
End Sub
```

[Copy script](javascript:void(0);)

```text
intMyHandle = dd.TextFileOpen("OldText.txt",eTextFileAttributeRead) 
if intMyHandle == -1 : 
    MsgError(intMyHandle) 
else: 
    dd.MsgBoxDisp( "Text file can be read.","MB_OK","MsgTypeInformation",None ,5) 
    intMyError = dd.TextFileClose(intMyHandle) 
def MsgError(FileNo): 
    dd.MsgboxDisp("Error number: " + TextFileError(FileNo) + "\r\n" + "error message: " + TextFileErrorTxT(FileNo)) #Show error number and error message
```

#### Related Functions

[Command: TextFileEncoding](../../comoff/textfileencoding.htm) | [Command: TextFileEOL](../../comoff/textfileeol.htm) | [Function: FR](../functions/fr.htm) | [Function: TextFileEOF](../functions/textfileeof.htm) | [Function: TextFileErrorTxt](../functions/textfileerrortxt.htm) | [Function: TextFileSeek](../functions/textfileseek.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/textfileerrortxt.htm language=enus -->
## TOPIC 00093: Function: TextFileErrorTxt

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/textfileerrortxt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/textfileerrortxt.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: TextFileErrorTxt

### Function: TextFileErrorTxt

Displays an error text if an error occurs when you open, write, or read a text file.

```text
ReturnValue = TextFileErrorTxt(TextFileHandle)
```

#### Input Parameters

| TextFileHandle | Specifies the handle of the text file.Use the return value of the TextFileOpen function. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns an error text. |
| --- | --- |

#### Examples

The following example attempts to open the text file OldText.txt. However, DIAdem does not find this text file in the DIAdem folder and the [TextFileOpen](../../comoff/textfileopen.htm) function returns an error. The example then jumps into the subroutine for dealing with errors and displays the error number and the associated error text.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyHandle, intMyError
intMyHandle = TextFileOpen("OldText.txt",eTextFileAttributeRead)
If intMyHandle = -1 Then
  Call MsgError(intMyHandle)
Else
  Call MsgBoxDisp( "Text file can be read.",_
                   "MB_OK","MsgTypeInformation",,5) 
  intMyError = TextFileClose(intMyHandle)
End If

Sub MsgError(FileNo)
 Call MsgboxDisp("Error number: " & TextFileError(FileNo) & VbCrLf & _
 "error message: " & TextFileErrorTxT(FileNo)) 'Show error number and error message
End Sub
```

[Copy script](javascript:void(0);)

```text
intMyHandle = dd.TextFileOpen("OldText.txt",eTextFileAttributeRead) 
if intMyHandle == -1 : 
    MsgError(intMyHandle) 
else: 
    dd.MsgBoxDisp( "Text file can be read.","MB_OK","MsgTypeInformation",None ,5) 
    intMyError = dd.TextFileClose(intMyHandle) 
def MsgError(FileNo): 
    dd.MsgboxDisp("Error number: " + TextFileError(FileNo) + "\r\n" + "error message: " + TextFileErrorTxT(FileNo)) #Show error number and error message
```

#### Related Functions

[Command: TextFileEncoding](../../comoff/textfileencoding.htm) | [Command: TextFileEOL](../../comoff/textfileeol.htm) | [Function: FR](../functions/fr.htm) | [Function: TextFileEOF](../functions/textfileeof.htm) | [Function: TextFileError](../functions/textfileerror.htm) | [Function: TextFileSeek](../functions/textfileseek.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/textfilereadln.htm language=enus -->
## TOPIC 00094: Function: TextFileReadLn

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/textfilereadln.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/textfilereadln.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: TextFileReadLn

### Function: TextFileReadLn

Reads a text file line up to the end of line identifier. DIAdem starts to read from the first line. After DIAdem reads the line, DIAdem positions the bookmark in the next line. The next time you call the TextFileReadLn function, DIAdem automatically reads the next row. If you want to jump to a specific row in a text file, use the [TextFileSeek](../functions/textfileseek.htm) function.

```text
ReturnValue = TextFileReadLn(TextFileHandle)
```

#### Input Parameters

| TextFileHandle | Specifies the handle of the text file.Use the return value of the TextFileOpen function. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns the read text line without the line end identifier. When DIAdem reaches the file end, the function returns NULL. |
| --- | --- |

#### Examples

The following example opens the text file NewText.txt and reads the file linewise to the end. The function checks for the value NULL to detect the file end.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strFile, intLineCount, intMyHandle, strEOL, strMyText, intMyError
strFile = ScriptReadPath & "NewText.txt"
strEOL = TextFileEOL(strFile)
intMyHandle = TextFileOpen(strFile, eTextFileAttributeRead, strEOL)
intLineCount = 0
Do
  strMyText = TextFileReadLn(intMyHandle)
  If (Not IsNull(strMyText)) then
    intLineCount = intLineCount+1
    Call MsgBoxDisp(strMyText,"MB_OK")
  End If  
Loop until (IsNull(strMyText))
intMyError = TextFileClose(intMyHandle)
```

[Copy script](javascript:void(0);)

```text
strFile = dd.ScriptReadPath + "NewText.txt" 
strEOL = dd.TextFileEOL(strFile) 
intMyHandle = dd.TextFileOpen(strFile, eTextFileAttributeRead, strEOL) 
intLineCount = 0 
while True: 
    strMyText = dd.TextFileReadLn(intMyHandle) 
    if (not strMyText == None) : 
        intLineCount = intLineCount+1 
        dd.MsgBoxDisp(strMyText,"MB_OK") 
if (strMyText == None):
        break 
intMyError = dd.TextFileClose(intMyHandle) 
```

#### Related Functions

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm) | [Command: TextFileEncoding](../../comoff/textfileencoding.htm) | [Command: TextFileEOL](../../comoff/textfileeol.htm) | [Function: FR](../functions/fr.htm) | [Function: TextFileEOF](../functions/textfileeof.htm) | [Function: TextFileError](../functions/textfileerror.htm) | [Function: TextFileErrorTxt](../functions/textfileerrortxt.htm) | [Function: TextFileSeek](../functions/textfileseek.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/textfileseek.htm language=enus -->
## TOPIC 00095: Function: TextFileSeek

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/textfileseek.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/textfileseek.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: TextFileSeek

### Function: TextFileSeek

Jumps to a specific row in a text file. 
Using TextFileSeek can lead to greater runtimes for large files. If you want to read a text file line by line, use the [TextFileReadln](../functions/textfilereadln.htm) function. After DIAdem reads the line, DIAdem positions the bookmark in the next line. The next time you call the TextFileReadLn function, DIAdem automatically reads the next row.

```text
ReturnValue = TextFileSeek(TextFileHandle, LineNo)
```

#### Input Parameters

| TextFileHandle | Specifies the handle of the text file.Use the return value of the TextFileOpen function. |
| --- | --- |
| LineNo | Specifies the line number. |

#### Return Parameters

| ReturnValue | Returns a numeric value. If an error occurs, the function returns either the value -1 or a value that does is not the same as the specified line number. |
| --- | --- |

#### Examples

The following example opens the text file NewText.txt, skips to the tenth row, and reads the file linewise to the end. DIAdem displays each line of text in a message box.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim GotoLine, intMyHandle, intMyText, strMyText, intMyError
intMyHandle = TextFileOpen("NewText.txt",eTextFileAttributeRead)
GotoLine = 10
intMyError = TextFileSeek(intMyHandle, GotoLine)
If intMyError = Gotoline then
    strMyText = TextFileReadLn(intMyHandle)
    Call MsgBoxDisp(strMyText,"MB_OK")
End If
intMyError = TextFileClose(intMyHandle)
```

[Copy script](javascript:void(0);)

```text
intMyHandle = dd.TextFileOpen("NewText.txt",eTextFileAttributeRead) 
GotoLine = 10 
intMyError = dd.TextFileSeek(intMyHandle, GotoLine) 
if intMyError == Gotoline : 
    strMyText = dd.TextFileReadLn(intMyHandle) 
    dd.MsgBoxDisp(strMyText,"MB_OK") 
intMyError = dd.TextFileClose(intMyHandle) 
```

#### Related Functions

[Command: TextFileEncoding](../../comoff/textfileencoding.htm) | [Command: TextFileEOL](../../comoff/textfileeol.htm) | [Function: FR](../functions/fr.htm) | [Function: TextFileEOF](../functions/textfileeof.htm) | [Function: TextFileError](../functions/textfileerror.htm) | [Function: TextFileErrorTxt](../functions/textfileerrortxt.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/textfilewriteln.htm language=enus -->
## TOPIC 00096: Function: TextFileWriteLn

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/textfilewriteln.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/textfilewriteln.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: TextFileWriteLn

### Function: TextFileWriteLn

Writes a text line into a text file.

```text
ReturnValue = TextFileWriteLn(TextFileHandle, Text)
```

#### Input Parameters

| TextFileHandle | Specifies the handle of the text file.Use the return value of the TextFileOpen function. |
| --- | --- |
| Text | Specifies a text that DIAdem inserts into the text file. |

#### Return Parameters

| ReturnValue | Returns a numeric value. If an error occurs when the text is written, the function returns the value -1. |
| --- | --- |

#### Examples

The following example creates a text file in ANSI code and writes twenty lines in this file.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim LineNo, intMyHandle, intMyText, intMyError
intMyHandle = TextFileOpen("NewText.txt",eTextFileAttributeCreate OR eTextFileAttributeWrite OR eTextFileAttributeANSI) 
For LineNo = 1 To 20
  intMyText= TextfileWriteLn(intMyHandle, "Line " & LineNo)
Next
intMyError = TextFileClose(intMyHandle)
```

[Copy script](javascript:void(0);)

```text
intMyHandle = dd.TextFileOpen("NewText.txt",eTextFileAttributeCreate or eTextFileAttributeWrite or eTextFileAttributeANSI) 
for LineNo in range( 1, 20 + 1): 
    intMyText= dd.TextfileWriteLn(intMyHandle, "Line " + LineNo) 
intMyError = dd.TextFileClose(intMyHandle) 
```

#### Related Functions

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm) | [Command: TextFileEncoding](../../comoff/textfileencoding.htm) | [Command: TextFileEOL](../../comoff/textfileeol.htm) | [Function: FR](../functions/fr.htm) | [Function: TextFileEOF](../functions/textfileeof.htm) | [Function: TextFileError](../functions/textfileerror.htm) | [Function: TextFileErrorTxt](../functions/textfileerrortxt.htm) | [Function: TextFileSeek](../functions/textfileseek.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/trunc.htm language=enus -->
## TOPIC 00097: Function: Trunc

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/trunc.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/trunc.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Trunc

### Function: Trunc

Determines the integer part of a number.

```text
ReturnValue = Trunc(Value)
```

#### Input Parameters

| Value | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. For invalid values the value is NoValue. |
| --- | --- |

#### Examples

The following example determines the integer part of a real number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = Trunc(-75.5109)    'intMyResult = -75
```

[Copy script](javascript:void(0);)

```text
intMyResult= dd.Trunc(-75.5109) #intMyResult = -75
```

The following example determines the integer parts of the values in the Group1/Input data channel and saves the result in the Group2/Result data channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= Trunc (Ch(""Group1/Input""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= Trunc (Ch(""Group1/Input""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note Use the Frac function to determine the decimal places of a number. |
| --- | --- |

|  | The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: VU](../functions/vu.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/ttr.htm language=enus -->
## TOPIC 00098: Function: TTR (Text to Real)

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/ttr.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/ttr.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: TTR (Text to Real)

### Function: TTR (Text to Real)

Converts a text in time format into a number in DIAdem double time format. The value depends on the variable [ApplicationTimebaseHighResolution](/csh?topicname=varoff/applicationtimebasehighresolution.htm).

Use the command [TTD](../../comoff/ttd.htm) instead of the TTR function in order to convert a text in time format into a VBS date.

|  | Note If you save time values in DIAdem that are VBS VBDate subtype variables, the high resolution is lost. VBS only offers time values for this data type which provides only a limited resolution. |
| --- | --- |

```text
ReturnValue = TTR(String [,Format])
```

#### Input Parameters

| String | Specifies a text or a variable that contains the date in DIAdem time format. The text must not contain written or abbreviated weekdays, months, or calendar weeks. If the day or month is single-digit, it must contain leading zeros, for example, 01/02/2011. |
| --- | --- |
| [Format] | Specifies the time format for the text according to the format instructions.If you do not specify a time format, DIAdem applies the default format specified under Settings»DIAdem Settings. |

#### Return Parameters

| ReturnValue | Returns a Double value. |
| --- | --- |

The [RTT](../functions/rtt.htm) function converts a number that exists in the DIAdem double time format into a text.

#### Examples

The following example converts a date into a number.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dMyResult
dMyResult = TTR("09/11/1989","dd/mm/yyyy")
```

[Copy script](javascript:void(0);)

```text
dMyResult = dd.TTR("09/11/1989","dd/mm/yyyy") 
```

The following example determines the calendar week for the current date.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strCurrWeek
strCurrWeek = Str(TTR(CurrDate),"#k")
```

[Copy script](javascript:void(0);)

```text
strCurrWeek = dd.Str(dd.TTR(dd.CurrDate),"#k") 
```

#### Related Functions

[Command: ChnConvertNumericToTime](../../comoff/chnconvertnumerictotime.htm) | [Command: ChnConvertTimeToNumeric](../../comoff/chnconverttimetonumeric.htm) | [Command: ConvertTimeType](../../comoff/converttimetype.htm) | [Command: TTD](../../comoff/ttd.htm) | [Command: TTD](../../comoff/ttd.htm) | [Function: Char](../functions/char.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: FileNameSplit](../functions/namesplit.htm) | [Function: Idx](../functions/idx.htm) | [Function: Len](../functions/len.htm) | [Function: PU](../functions/pu.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Str](../functions/str.htm) | [Function: Textaddition (+)](../functions/tadd.htm) | [Function: Val](../functions/val.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/val.htm language=enus -->
## TOPIC 00099: Function: Val

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/val.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/val.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: Val

### Function: Val

Determines a number in a text.

```text
ReturnValue = Val(String,[ErrorValue])
```

#### Input Parameters

| String | Specifies a text or a text variable. |
| --- | --- |
| [ErrorValue] | Specifies the numeric value that DIAdem returns if a conversion error occurs. If you do not specify ErrorValue, DIAdem displays an error message when a conversion error occurs. |

#### Output Parameters

| ReturnValue | Returns the first number, which is contained in the text, as a numeric value. If the text does not contain a number and if the second parameter is not set, DIAdem outputs an error message. |
| --- | --- |

#### Examples

The following examples determines the first number in a text.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dblMyResult
dblMyResult = Val("3dimension")               'dblMyResult = 3
dblMyResult = Val("-3*2")                     'dblMyResult = -3
dblMyResult = Val("Points,5.12,7.03,11.7")    'dblMyResult = 5.12
dblMyresult = Val("OnlyText",0)               'dblMyresult = 0; No error message
```

[Copy script](javascript:void(0);)

```text
dblMyResult = dd.Val("3dimension") #dblMyResult = 3
dblMyResult = dd.Val("-3*2") #dblMyResult = -3
dblMyResult = dd.Val("Points,5.12,7.03,11.7") #dblMyResult = 5.12
dblMyresult = dd.Val("OnlyText",0) #dblMyresult = 0; No error message
```

|  | Note Use the Val function instead of the VBS functions CDbl and CLng, to convert texts into numbers and to process these numbers in DIAdem. The VBS functions use the language set on your computer. The Val function always uses a point as the decimal character, which is customary in DIAdem. |
| --- | --- |

#### Related Functions

[Command: TTD](../../comoff/ttd.htm) | [Function: Char](../functions/char.htm) | [Function: FCNo](../functions/fcno.htm) | [Function: FileNameSplit](../functions/namesplit.htm) | [Function: Idx](../functions/idx.htm) | [Function: Len](../functions/len.htm) | [Function: PU](../functions/pu.htm) | [Function: Str](../functions/str.htm) | [Function: Textaddition (+)](../functions/tadd.htm) | [Function: TTR (Text to Real)](../functions/ttr.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/venum.htm language=enus -->
## TOPIC 00100: Function: VEnum

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/venum.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/venum.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: VEnum

### Function: VEnum

Determines an enumeration or dynamic enumeration term in a script from a [enumeration variable](/csh?topicname=genas/genauto/genauto_enumeration_list.htm) or [dynamic enumeration variable](/csh?topicname=genas/genauto/genauto_dynamic_enumeration_list.htm).

```text
ReturnValue = VEnum(VariableName, Index)
```

#### Input Parameters

| VariableName | Specifies an enumeration variable or a dynamic enumeration variable.The property variables of the object-oriented script interface are constants and not enumeration variables or dynamic enumeration list variables. |
| --- | --- |
| Index | Specifies the index of an enumeration term or a dynamic enumeration term.Value range 0 to MaxOrd |

#### Return Parameters

| ReturnValue | Returns the enumeration term or dynamic enumeration term as text. If you enter an index that does not exist in the variable, DIAdem returns an empty text. |
| --- | --- |

#### Examples

The following example determines the fifth color in the [ColorLst](/csh?topicname=varoff/colorlst.htm) variable.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim strMyResult
strMyResult = VEnum("ColorLst",4)    'strMyResult = "blue"
```

[Copy script](javascript:void(0);)

```text
strMyResult= dd.VEnum("ColorLst",4) #strMyResult = "blue"
```

The following example shows all the colors of the ColorLst variable in a message box.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intNo
For intNo = 1 To MaxOrd("Colorlst")
  Call MsgBoxDisp ("Color No " & intNo & " is " & VEnum("ColorLst",intNo))
Next
```

[Copy script](javascript:void(0);)

```text
for intNo in range( 1, dd.MaxOrd("Colorlst") + 1): 
    dd.MsgBoxDisp ("Color No " + intNo + " is " + dd.VEnum("ColorLst",intNo)) 
```

#### Related Functions

[Command: AddUserCommandToEvent](../../comoff/addusercommandtoevent.htm) | [Command: RemoveUserCommandFromEvent](../../comoff/removeusercommandfromevent.htm) | [Command: VEnumIdx](../../comoff/venumidx.htm) | [Function: GetEnv](../functions/getenv.htm) | [Function: IdentifierType](../functions/identifiertype.htm) | [Function: MaxOrd](../functions/maxord.htm) | [Function: Ord](../functions/ord.htm) | [Function: ScriptEvaluate](../functions/scriptevaluate.htm) | [Function: VIT](../functions/vit.htm) | [Function: VSA](../functions/vsa.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/vit.htm language=enus -->
## TOPIC 00101: Function: VIT

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/vit.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/vit.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: VIT

### Function: VIT

Determines whether a user variable is enabled in DIAdem.

```text
ReturnValue = VIT(VariableName)
```

#### Input Parameters

| VariableName | Specifies a user variable. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns a Boolean value. |
| --- | --- |

#### Examples

The following example determines whether the user variable MyTest_ is enabled.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim blnMyResult
blnMyResult = VIT("MyTest_")
```

[Copy script](javascript:void(0);)

```text
blnMyResult = dd.VIT("MyTest_") 
```

|  | Note Use the commands GlobalDim and GlobalReDim to define global variables. You also can define global variables in user command files. Declare the variable in the global range outside a function and register this user command file. |
| --- | --- |

#### Related Functions

[Command: AddUserCommandToEvent](../../comoff/addusercommandtoevent.htm) | [Command: RemoveUserCommandFromEvent](../../comoff/removeusercommandfromevent.htm) | [Command: VEnumIdx](../../comoff/venumidx.htm) | [Function: GetEnv](../functions/getenv.htm) | [Function: IdentifierType](../functions/identifiertype.htm) | [Function: MaxOrd](../functions/maxord.htm) | [Function: Ord](../functions/ord.htm) | [Function: ScriptEvaluate](../functions/scriptevaluate.htm) | [Function: VEnum](../functions/venum.htm) | [Function: VSA](../functions/vsa.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/vsa.htm language=enus -->
## TOPIC 00102: Function: VSA

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/vsa.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/vsa.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: VSA

### Function: VSA

Determines whether a user variable file is enabled.

```text
ReturnValue = VSA(UserVarFile)
```

#### Input Parameters

| UserVarFile | Specifies a user variable file. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns a Boolean value. |
| --- | --- |

|  | Note The user variable file must be located in the SCRIPT user path. |
| --- | --- |

#### Examples

The following example determines whether the user variable file MyVar.vas is enabled.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim blnMyResult
blnMyResult = VSA("MyVar")
```

[Copy script](javascript:void(0);)

```text

```

|  | Note Use the commands GlobalDim and GlobalReDim to define global variables. You also can define global variables in user command files. Declare the variable in the global range outside a function and register this user command file. |
| --- | --- |

#### Related Functions

[Command: AddUserCommandToEvent](../../comoff/addusercommandtoevent.htm) | [Command: RemoveUserCommandFromEvent](../../comoff/removeusercommandfromevent.htm) | [Command: VEnumIdx](../../comoff/venumidx.htm) | [Function: GetEnv](../functions/getenv.htm) | [Function: IdentifierType](../functions/identifiertype.htm) | [Function: MaxOrd](../functions/maxord.htm) | [Function: Ord](../functions/ord.htm) | [Function: ScriptEvaluate](../functions/scriptevaluate.htm) | [Function: VEnum](../functions/venum.htm) | [Function: VIT](../functions/vit.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/vu.htm language=enus -->
## TOPIC 00103: Function: VU

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/vu.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/vu.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: VU

### Function: VU

Connects a value and a unit.

```text
ReturnValue = VU(Value, [Unit])
```

#### Input Parameters

| Value | Specifies a numeric value or a variable. |
| --- | --- |
| [Unit] | Specifies a unit. If you do not specify the unit, DIAdem uses the unit "1". |

#### Return Parameters

DIAdem saves the result unit in a quantity-based calculation of the [Calculate](../../comoff/calculate.htm) command in the [CalculateResultUnit](/csh?topicname=varoff/calculateresultunit.htm) variable. Refer to the [Calculate](../../comoff/chncalculate.htm) command for rules for input units and result units.

#### Examples

The following example calculates the quotient from "10 m/s" and "2 ms" and displays the result value and the result unit as a message.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
CalcQuantityBased = TRUE
Call Calculate("R1=VU(10, ""m/s"") / VU(2, ""ms"")")
Call MsgBoxDisp("Result: Value " & R1 & " with unit " & CalculateResultUnit)
```

[Copy script](javascript:void(0);)

```text
CalcQuantityBased = True 
dd.Calculate("R1=VU(10, ""m/s"") / VU(2, ""ms"")") 
dd.MsgBoxDisp("Result: Value " + dd.R1 + " with unit " + dd.CalculateResultUnit) 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

#### Related Functions

[Function: ^](../functions/potenz.htm) | [Function: Abs](../functions/abs.htm) | [Function: Ceil](../functions/ceil.htm) | [Function: Deg](../functions/deg.htm) | [Function: Eex](../functions/eex.htm) | [Function: Exp](../functions/exp.htm) | [Function: Fak](../functions/fak.htm) | [Function: Floor](../functions/floor.htm) | [Function: Frac](../functions/frac.htm) | [Function: Lg](../functions/log.htm) | [Function: Ln](../functions/ln.htm) | [Function: MaxV](../functions/maxv.htm) | [Function: MinV](../functions/minv.htm) | [Function: Mod](../functions/mod.htm) | [Function: Rad](../functions/rad.htm) | [Function: Random](../functions/random.htm) | [Function: Rnd](../functions/rnd.htm) | [Function: Round](../functions/round.htm) | [Function: RTP (Real To Part of Date)](../functions/rtp.htm) | [Function: RTT (Real to Text)](../functions/rtt.htm) | [Function: Sign](../functions/sign.htm) | [Function: SND](../functions/snd.htm) | [Function: Sqr](../functions/sqr.htm) | [Function: Sqrt](../functions/sqrt.htm) | [Function: Trunc](../functions/trunc.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions/xorb.htm language=enus -->
## TOPIC 00104: Function: XOrB

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions/xorb.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions/xorb.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Function: XOrB

### Function: XOrB

Determines the number resulting from the unequal bits of two numbers. The XOrB function converts the decimal numbers into binary numbers, determines the bits that the two numbers do not have in common, and reconverts this binary number into a decimal number.

```text
ReturnValue = XOrB(Value1, Value2)
```

#### Input Parameters

| Value1 | Specifies a numeric value, a variable, or a data channel. |
| --- | --- |
| Value2 | Specifies a numeric value, a variable, or a data channel. |

|  | Note If you specify numbers with decimal places for the parameters Value1 and Value2, DIAdem rounds the numbers to integers. |
| --- | --- |

#### Return Parameters

| ReturnValue | Returns integer values. If the input value is NoValue, the XOrB function returns the value NoValue. |
| --- | --- |

#### Examples

The following example determines the unequal bits of the decimal numbers 10 (dual: 1010) and 12 (dual: 1100).

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim intMyResult
intMyResult = XOrB(10,12)    'intMyResult = 6 (dual:0110)
```

[Copy script](javascript:void(0);)

```text
intMyResult = dd.XOrB(10,12) #intMyResult = 6 (dual:0110)
```

The following example determines the unequal bits of the values in each line of two data channels, and saves the decimal numbers in the new data channel Group2/Result.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Calculate ("Ch(""Group2/Result"")= XOrB (Ch(""Group1/Input""),Ch(""Group1/Reference""))")
```

[Copy script](javascript:void(0);)

```text
dd.Calculate ("Ch(""Group2/Result"")= XOrB (Ch(""Group1/Input""),Ch(""Group1/Reference""))") 
```

|  | Note You must use the Calculate command in scripts to calculate data channels with formulas. Compute the data channels according to the syntax in the Calculator. Refer to the procedures Executing Channel Calculations in the Calculator and Assigning a Value to a Variable in the Calculator for more information about the Calculator. |
| --- | --- |

|  | Note You can also determine the unequal bits of two numbers with the VBS function XOr. |
| --- | --- |

|  | The first and the second physical quantity must be the same. The physical input quantities and the result quantities are the same.The Input and Result Quantities for Quantity-Based Calculations page contains an overview of the input quantities and result quantities of all functions. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Related Functions

[Function: AndB](../functions/andb.htm) | [Function: ClrB](../functions/clrb.htm) | [Function: GetB](../functions/getb.htm) | [Function: NotB](../functions/notb.htm) | [Function: OrB](../functions/orb.htm) | [Function: SetB](../functions/setb.htm) | [Function: ShL](../functions/shl.htm) | [Function: ShR](../functions/shr.htm) | [Variable: ApplicationLegacyBinaryOperations](/csh?topicname=varoff/applicationlegacybinaryoperations.htm)

<!--NI_TOPIC bundle=diadem-api-ref path=functions/functions_general.htm language=enus -->
## TOPIC 00105: Calculator Functions

- bundle_id: `diadem-api-ref`
- source_path: `functions/functions_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem-api-ref/raw/resource/enus/functions/functions_general.htm
- document_id: `diadem-api-ref`
- page_type: `leaf`
- content_type: ``

Calculator Functions

### Calculator Functions

The following topics describe the functions of the DIAdem calculator.
