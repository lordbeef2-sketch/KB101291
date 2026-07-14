# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6501 ordinal=6501 -->
## Property and Method Reference

Property and Method Reference


 Name         Type      Description

                         elements that it needs to compare.

Return Value

The position in the array where the data is found, with 0 being the first element of the
array, if it is found. If the data is not found, BinSearch returns – i–1, where i is the
position where key should be placed.

BlockCmpBlockCmp (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 BlockCmp(p1, p2, numBytes);

Purpose

Compares two blocks of memory to determine whether one is less than, equal to, or
greater than the other.

Parameters

 Name           Type         Description

 p1            UPtr        Pointer to a block of memory.

 p2            UPtr        Pointer to a block of memory.

 numBytes       int32     Number of bytes you want to compare.

Return Value

A negative number, zero, or a positive number if p1 is less than, equal to, or greater
than p2, respectively.

Cat4ChrsCat4Chrs (LabVIEW(LabVIEW ManagerManager Macro)Macro)

int32 Cat4Chrs(a,b,c,d);


                                                    © National Instruments 6501

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6501 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6502 ordinal=6502 -->
## Property and Method Reference

Property and Method Reference

     Purpose

       Constructs an int32 parameter from four uInt8 parameters, with the first
      parameter as the high byte and the last parameter as the low byte.

     Parameters

      Name   Type       Description

        a      uInt8    High order byte of the high word of the resulting int32.

       b      uInt8   Low order byte of the high word of the resulting int32.

        c      uInt8    High order byte of the low word of the resulting int32.

       d      uInt8   Low order byte of the low word of the resulting int32.

     Return Value

      The resulting int32.

     CPStrBufCPStrBuf (LabVIEW(LabVIEW ManagerManager Macro)Macro)

     uChar *CPStrBuf(sp);

     Purpose

       Returns the address of the first string in a concatenated list of Pascal strings, that is,
       the address of sp->str.

     Parameters

      Name    Type             Description

        sp      CPStrPtr       Pointer to a concatenated list of Pascal strings.

     Return Value

      The address of the first string of the concatenated list of Pascal strings.


6502   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6502 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6503 ordinal=6503 -->
## Property and Method Reference

Property and Method Reference

CPStrCmpCPStrCmp (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 CPStrCmp(s1p, s2p);

Purpose

Lexically compares two concatenated lists of Pascal strings to determine whether one
is less than, equal to, or greater than the other. This comparison is case sensitive. The
function compares the lists as if they were one string.

Parameters

 Name    Type             Description

 s1p     CPStrPtr       Pointer to a concatenated list of Pascal strings.

 s2p     CPStrPtr       Pointer to a concatenated list of Pascal strings.

Return Value

<0, 0, or >0 if s1p is less than, equal to, or greater than s2p, respectively. Returns <0 if
s1p is an initial substring of s2p.

CPStrIndexCPStrIndex (LabVIEW(LabVIEW ManagerManager Function)Function)

PStr CPStrIndex(s1h, index);

Purpose

Returns a pointer to the Pascal string denoted by index in a list of strings. If index is
greater than or equal to the number of strings in the list, this function returns the
pointer to the last string.

Parameters

 Name   Type               Description

 s1h    CPStrHandle     Handle to a concatenated list of Pascal strings.


                                                    © National Instruments 6503

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6503 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6504 ordinal=6504 -->
## Property and Method Reference

Property and Method Reference


      Name   Type               Description

        index   int32          Number of the string you want, with 0 as the first string.

     Return Value

      A pointer to the specified Pascal string.

      CPStrInsertCPStrInsert (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr CPStrInsert(s1h, s2, index);

     Purpose

        Inserts a new Pascal string before the index numbered Pascal string in a concatenated
          list of Pascal strings. If index is greater than or equal to the number of strings in the list,
        this function places the new string at the end of the list. The function resizes the list to
     make room for the new string.

     Parameters

      Name Type            Description

        s1h   CPStrHandle Handle to a concatenated list of Pascal strings.

        s2    PStr           Pointer to a Pascal string.

                                  Position you want the new Pascal string to have in the list of Pascal
        index int32                                      strings, with 0 as the first string.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mFullErr          2


6504   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6504 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6505 ordinal=6505 -->
## Property and Method Reference

Property and Method Reference

CPStrLenCPStrLen (LabVIEW(LabVIEW ManagerManager Macro)Macro)

int32 CPStrLen(sp);

Purpose

Returns the number of Pascal strings in a concatenated list of Pascal strings, that is,
sp->cnt. Use the CPStrSize function to get the total number of characters in the list.

Parameters

 Name    Type             Description

 sp      CPStrPtr       Pointer to a concatenated list of Pascal strings.

Return Value

The number of strings in the concatenated list of Pascal strings.

CPStrRemoveCPStrRemove (LabVIEW(LabVIEW ManagerManager Function)Function)

void CPStrRemove(s1h, index);

Purpose

Removes a Pascal string from a list of Pascal strings. If index is greater than or equal to
the number of strings in the list, this function removes the last string. The function
resizes the list after removing the string.

Parameters

 Name  Type             Description

 s1h   CPStrHandle   Handle to a concatenated list of Pascal strings.

 index  int32         Number of the string you want to remove, with 0 as the first string.


                                                    © National Instruments 6505

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6505 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6506 ordinal=6506 -->
## Property and Method Reference

Property and Method Reference

     CPStrReplaceCPStrReplace (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr CPStrReplace(s1h, s2, index);

     Purpose

       Replaces a Pascal string in a concatenated list of Pascal strings with a new Pascal
        string.

     Parameters

      Name  Type             Description

        s1h   CPStrHandle   Handle to a concatenated list of Pascal strings.

        s2    PStr             Pointer to a Pascal string.

        index  int32         Number of the string you want to replace, with 0 as the first string.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mFullErr          2

      CPStrSizeCPStrSize (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 CPStrSize(sp);

     Purpose

       Returns the number of characters in a concatenated list of Pascal strings. Use the
      CPStrLen function to get the number of Pascal strings in the concatenated list.


6506   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6506 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6507 ordinal=6507 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name    Type             Description

 sp      CPStrPtr       Pointer to a concatenated list of Pascal strings.

Return Value

The number of characters in the concatenated list of Pascal strings.

CToPStrCToPStr (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 CToPStr(cstr, pstr);

Purpose

Converts a C string to a Pascal string, even if the pointers cstr and pstr refer to the
same memory location. If the length of cstr is greater than 255 characters, this
function converts only the first 255 characters. The function assumes pstr is large
enough to contain cstr.

Parameters

 Name          Type            Description

 cstr          CStr            Pointer to a C string.

 pstr          PStr            Pointer to a Pascal string.

Return Value

The length of the string, truncated to a maximum of 255 characters.

DateCStringDateCString (LabVIEW(LabVIEW ManagerManager Function)Function)

CStr DateCString(secs, fmt);


                                                    © National Instruments 6507

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6507 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6508 ordinal=6508 -->
## Property and Method Reference

Property and Method Reference

           Note This function was formerly called DateString.

     Purpose

       Returns a pointer to a string representing the date corresponding to secs seconds after
       12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. Date formats
       vary with your system configuration.

     Parameters

      Name Type     Description

                       Seconds since 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904
        sec   uInt32                            00:00:00].

                           Indicates the format of the returned date string, using the following values:

                                         • 0—Short date format, mm/dd/yy, where mm is a number between 1 and 12
                              representing the current month, dd is the current day of the month (1
                            through 31), and yy is the last two digits of the corresponding year. For
        fmt   int32       example, 12/31/92.
                                         • 1—Long date format, dayName, MonthName, DayOfMonth, LongYear. For
                            example, Thursday, December 31,1992.
                                         • 2—Abbreviated date format, AbbrevDayName, AbbrevMonthName,
                           DayOfMonth, LongYear. For example, Thu, Dec 31,1992.


     Return Value

      The date as a C string.

     DateToSecsDateToSecs (LabVIEW(LabVIEW ManagerManager Function)Function)

     uint32 DateToSecs(dateRecordP);

     Purpose

       Converts from a time described using the DateRec data structure to the number of
      seconds since 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904


6508   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6508 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6509 ordinal=6509 -->
## Property and Method Reference

Property and Method Reference

00:00:00].

Parameters

 Name       Type         Description

                             Pointer to a DateRec structure. DateToSecs stores the converted
 dateRecordP DateRec * date in the fields of the date structure referred to by dateRecordP.
                             This parameter is a pointer.

Return Value

The corresponding number of seconds since 12:00 a.m., Friday, January 1, 1904,
Universal Time [01-01-1904 00:00:00].

FileNameCmpFileNameCmp (LabVIEW(LabVIEW ManagerManager Macro)Macro)

int32 FileNameCmp(s1, s2);

Purpose

Lexically compares two filenames to determine whether one is less than, equal to, or
greater than the other. This comparison uses the same case sensitivity as the file
system, that is, case-insensitive on Mac OS X and Windows, case-sensitive on Linux.

Parameters

 Name          Type            Description

 s1           PStr            Pointer to a Pascal string.

 s2           PStr            Pointer to a Pascal string.

Return Value

<0, 0, or >0 if s1 is less than, equal to, or greater than s2, respectively. Returns <0 if s1
is an initial substring of s2.


                                                    © National Instruments 6509

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6509 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6510 ordinal=6510 -->
## Property and Method Reference

Property and Method Reference

     FileNameIndCmpFileNameIndCmp (LabVIEW(LabVIEW ManagerManager Macro)Macro)

     int32 FileNameIndCmp(s1p, s2p);

     Purpose

        Lexically compares two filenames and determines whether one is less than, equal to,
       or greater than the other. This comparison uses the same case sensitivity as the file
       system, that is, case-insensitive on Mac OS X and Windows, case-sensitive on Linux.
       This function is similar to FileNameCmp, except you pass the function handles to the
        string data instead of pointers.

     Parameters

      Name         Type                 Description

        s1p         PStr *              Pointer to a Pascal string.

        s2p         PStr *              Pointer to a Pascal string.

     Return Value

      <0, 0, or >0 if s1p is less than, equal to, or greater than s2p, respectively. Returns <0 if
      s1p is an initial substring of s2p.

     FileNameNCmpFileNameNCmp (LabVIEW(LabVIEW ManagerManager Macro)Macro)

     int32 FileNameNCmp(s1, s2, n);

     Purpose

        Lexically compares two filenames to determine whether one is less than, equal to, or
       greater than the other, limiting the comparison to n characters. This comparison uses
       the same case sensitivity as the file system, that is, case-insensitive on Mac OS X and
      Windows, case-sensitive on Linux.


6510   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6510 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6511 ordinal=6511 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name    Type        Description

 s1      CStr        Pointer to a C string.

 s2      CStr        Pointer to a C string.

 n      uInt32    Maximum number of characters you want to compare.

Return Value

<0, 0, or >0 if s1 is less than, equal to, or greater than s2, respectively. Returns <0 if s1
is an initial substring of s2.

GetALongGetALong (LabVIEW(LabVIEW ManagerManager Macro)Macro)

int32 GetALong(p);

Purpose

Retrieves an int32 from a void pointer. This function can retrieve an int32 at any
address, even if the int32 is not long word aligned on a platform that enforces
alignment.

Parameters

 Name    Type          Description

 p       void *      Address from which you want to read an int32.

Return Value

int32 stored at the specified address.

HexCharHexChar (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 HexChar(n);


                                                    © National Instruments 6511

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6511 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6512 ordinal=6512 -->
## Property and Method Reference

Property and Method Reference

     Purpose

       Returns the ASCII character in hex that represents the specified value n, 0 ≤ n ≤ 15.

     Parameters

      Name       Type           Description

       n         int32         Decimal value between 0 and 15.

     Return Value

      The corresponding ASCII hex character. If n is out of range, the function returns the
       ASCII character corresponding to n modulo 16.

     Hi16Hi16 (LabVIEW(LabVIEW ManagerManager Macro)Macro)

     int16 Hi16(x);

     Purpose

       Returns the high order int16 of an int32.

     Parameters

      Name   Type      Description

        x      int32   int32 for which you want to determine the high int16.

     HiByteHiByte (LabVIEW(LabVIEW ManagerManager Macro)Macro)

     int8 HiByte(x);

     Purpose

       Returns the high order int8 of an int16.


6512   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6512 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6513 ordinal=6513 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name    Type       Description

 x      int16   int16 for which you want to determine the high int8.

HiNibbleHiNibble (LabVIEW(LabVIEW ManagerManager Macro)Macro)

uInt8 HiNibble(x);

Purpose

Returns the value stored in the high four bits of an uInt8.

Parameters

 Name     Type        Description

 x       uInt8    uInt8 whose high four bits you want to extract.

IsAlphaIsAlpha (LabVIEW(LabVIEW ManagerManager Function)Function)

Bool32 IsAlpha(c);

Purpose

Returns TRUE if the character c is a lowercase or uppercase letter, that is, in the set a
to z or A to Z. On Linux, this function also returns TRUE for international characters,
such as à, á, Ä, and so on.

Parameters

 Name        Type            Description

 c          uChar          Character you want to analyze.


                                                    © National Instruments 6513

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6513 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6514 ordinal=6514 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      Bool32, which can contain the following values.


        Value                 Description

       TRUE              The character is alphabetic.

       FALSE               Otherwise.

       IsDigitIsDigit (LabVIEW(LabVIEW ManagerManager Function)Function)

     Bool32 IsDigit(c);

     Purpose

       Returns TRUE if the character c is between 0 and 9.

     Parameters

      Name        Type            Description

        c          uChar          Character you want to analyze.

     Return Value

      Bool32, which can contain the following values.


        Value               Description

       TRUE               Character is a numerical digit.

       FALSE              Otherwise.

     IsLowerIsLower (LabVIEW(LabVIEW ManagerManager Function)Function)

     Bool32 IsLower(c);


6514   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6514 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6515 ordinal=6515 -->
## Property and Method Reference

Property and Method Reference

Purpose

Returns TRUE if the character c is a lowercase letter, that is, in the set a to z. This
function also returns TRUE for lowercase international characters, such as ó, ö, and so
on.

Parameters

 Name        Type            Description

 c          uChar          Character you want to analyze.

Return Value

Bool32, which can contain the following values.


 Value               Description

 TRUE               Character is a lowercase letter.

 FALSE             Otherwise.

IsUpperIsUpper (LabVIEW(LabVIEW ManagerManager Function)Function)

Bool32 IsUpper(c);

Purpose

Returns TRUE if the character c is between an uppercase letter, that is, in the set A to
Z. This function also returns TRUE for uppercase international characters, such as Ó, Ä,
and so on.

Parameters

 Name        Type            Description

 c          uChar          Character you want to analyze.


                                                    © National Instruments 6515

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6515 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6516 ordinal=6516 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      Bool32, which can contain the following values.


        Value              Description

       TRUE              Character is an uppercase letter.

       FALSE             Otherwise.

     Lo16Lo16 (LabVIEW(LabVIEW ManagerManager Macro)Macro)

     int16 Lo16(x);

     Purpose

       Returns the low order int16 of an int32.

     Parameters

      Name   Type      Description

        x      int32   int32 for which you want to determine the low int16.

     LoByteLoByte (LabVIEW(LabVIEW ManagerManager Macro)Macro)

     int8 LoByte(x);

     Purpose

       Returns the low order int8 of an int16.

     Parameters

      Name    Type       Description

        x       int16   int16 for which you want to determine the low int8.


6516   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6516 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6517 ordinal=6517 -->
## Property and Method Reference

Property and Method Reference

LongLong (LabVIEW(LabVIEW ManagerManager Macro)Macro)

int32 Long(hi, lo);

Purpose

Creates an int32 from two int16 parameters.

Parameters

 Name      Type          Description

 hi        int16        High int16 for the resulting int32.

 lo        int16      Low int16 for the resulting int32.

Return Value

The resulting int32.

LoNibbleLoNibble (LabVIEW(LabVIEW ManagerManager Macro)Macro)

uInt8 LoNibble(x);

Purpose

Returns the value stored in the low four bits of an uInt8.

Parameters

 Name     Type        Description

 x       uInt8    uInt8 whose low four bits you want to extract.

LStrBufLStrBuf (LabVIEW(LabVIEW ManagerManager Macro)Macro)

uChar *LStrBuf(s);


                                                    © National Instruments 6517

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6517 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6518 ordinal=6518 -->
## Property and Method Reference

Property and Method Reference

     Purpose

       Returns the address of the string data of a LabVIEW string, that is, the address of s-
      >str.

     Parameters

      Name        Type                  Description

         s          LStrPtr              Pointer to a LabVIEW string.

     Return Value

      The address of the string data of the LabVIEW string.

     LStrCmpLStrCmp (LabVIEW(LabVIEW ManagerManager Function)Function)

     LStrPtr LStrCmp(l1p, l2p);

     Purpose

        Lexically compares two LabVIEW strings to determine whether one is less than, equal
        to, or greater than the other. This comparison is case sensitive.

     Parameters

      Name        Type                  Description

         l1p         LStrPtr              Pointer to a LabVIEW string.

         l2p         LStrPtr              Pointer to a LabVIEW string.

     Return Value

      <0, 0, or >0 if l1p is less than, equal to, or greater than l2p, respectively. Returns <0 if
       l1p is an initial substring of l2p.


6518   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6518 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6519 ordinal=6519 -->
## Property and Method Reference

Property and Method Reference

LStrLenLStrLen (LabVIEW(LabVIEW ManagerManager Macro)Macro)

int32 LStrLen(s);

Purpose

Returns the length of a LabVIEW string, that is, s->cnt.

Parameters

 Name        Type                  Description

 s          LStrPtr              Pointer to a LabVIEW string.

Return Value

The number of characters in the LabVIEW string.

LToCStrNLToCStrN (LabVIEW(LabVIEW ManagerManager Function)Function)

uInt32 LToCStrN(ConstLStrPtr, CStr, uInt32);

Purpose

Converts a LabVIEW string to a C string, even if the pointers source and dest refer to
the same memory location. If the length of source is greater than destSize, this
function converts only the first characters that fit into the C string buffer. The function
assumes that destSize is the size of dest in bytes.

Parameters

 Name          Type                      Description

 source        ConstLStrP              Pointer to a LabVIEW string.

 dest          CStr                      Pointer to a C string.

 destSize       uInt32                    Size of the C string buffer.


                                                    © National Instruments 6519

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6519 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6520 ordinal=6520 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      The length of the string, truncated to the maximum number of characters specified by
       destSize.

      LToPStrLToPStr (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 LToPStr(lstrp, pstr);

     Purpose

       Converts a LabVIEW string to a Pascal string. If the LabVIEW string is more than
      255 characters, this function converts only the first 255 characters. The function works
      even if the pointers lstrp and pstr refer to the same memory location. The function
      assumes pstr is large enough to contain lstrp.

     Parameters

      Name        Type                  Description

          lstrp        LStrPtr              Pointer to a LabVIEW string.

         pstr        PStr                  Pointer to a Pascal string.

     Return Value

      The length of the string, truncated to a maximum of 255 characters.

     MathematicalMathematical OperationsOperations

        In addition to the support manager functions you can use for mathematical
       operations, LabVIEW supports a number of other mathematical functions. The
       following functions are implemented as defined in The C Programming Language by
       Brian W. Kernighan and Dennis M. Ritchie.

      double atan(double);

      double cos(double);


6520   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6520 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6521 ordinal=6521 -->
## Property and Method Reference

Property and Method Reference

double exp(double);

double fabs(double);

double log(double);

double sin(double);

double sqrt(double);

double tan(double);

double acos(double);

double asin(double);

double atan2(double, double);

double ceil(double);

double cosh(double);

double floor(double);

double fmod(double, double);

double frexp(double, int *);

double ldexp(double, int);

double log10(double);

double modf(double, double *);

double pow(double, double);

double sinh(double);

double tanh(double);


                                                    © National Instruments 6521

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6521 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6522 ordinal=6522 -->
## Property and Method Reference

Property and Method Reference

    MaxMax (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 Max(n,m);

     Purpose

       Returns the maximum of two int32 parameters.

     Parameters

      Name  Type     Description

         n, m   int32  int32 parameters whose maximum value you want to determine.

      MilliSecsMilliSecs (LabVIEW(LabVIEW ManagerManager Function)Function)

     uint32 MilliSecs();

     Return Value

      The time in milliseconds since an undefined system time. The actual resolution of this
       timer is system dependent.

     MinMin (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 Min(n,m);

     Purpose

       Returns the minimum of two int32 parameters.

     Parameters

      Name   Type     Description

         n, m   int32  int32 parameters whose minimum value you want to determine.


6522   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6522 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6523 ordinal=6523 -->
## Property and Method Reference

Property and Method Reference

NIGetOneErrorCodeNIGetOneErrorCode (LabVIEW(LabVIEW ManagerManager Function)Function)

LVBoolean NIGetOneErrorCode(errCode, *errText);

Purpose

Converts a numeric error code to the associated text description. This function
recognizes error codes from any installed National Instruments product.

Parameters

 Name   Type             Description

 errCode int32          Numeric error code.

                          Address at which NIGetOneErrorCode stores the error code *errText LStrHandle *
                              description. This parameter is a pointer.

Return Value

LVBoolean, which can contain the following values.


 Value   Description

 0       This function did not find the value of errCode in any of the error text files.

 1       This function found the value of errCode in one of the error text files.

OccurOccur (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr Occur(Occurrence o);

Purpose

Triggers the specified occurrence. All block diagrams that are waiting for this
occurrence stop waiting.


                                                    © National Instruments 6523

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6523 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6524 ordinal=6524 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name     Type                   Description

       o       Occurrence         Occurrence refnum you want to trigger.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1 or not a valid user event.

      OffsetOffset (LabVIEW(LabVIEW ManagerManager Macro)Macro)

     int16 Offset(type, field);

     Purpose

       Returns the offset of the specified field within the structure called type.

     Parameters

      Name      Type      Description

        type     —         Structure that contains field.

          field     —          Field whose offset you want to determine.

     Return Value

      An offset as an int16.


6524   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6524 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6525 ordinal=6525 -->
## Property and Method Reference

Property and Method Reference

PinPin (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 Pin(i, low, high);

Purpose

Returns i coerced to fall within the range from low to high inclusive.

Parameters

 Name    Type       Description

 i       int32     Value you want to coerce to the specified range.

 low     int32    Low value of the range to which you want to coerce i.

 high    int32     High value of the range to which you want to coerce i.

Return Value

i coerced to the specified range.

PostLVUserEventPostLVUserEvent (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr PostLVUserEvent(LVUserEventRef ref, void *data);

Purpose

Posts the given user event. The event and associated data are queued for all event
structures registered for the event.

Parameters

 Name Type                Description

 ref   LVUserEventRef Event refnum for the event for which you want to post data.

                           Address of the data to post. The data must match the type used to
 data  void*                             create the user event.


                                                    © National Instruments 6525

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6525 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6526 ordinal=6526 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1 or not a valid user event.

     PPStrCaseCmpPPStrCaseCmp (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 PPStrCaseCmp(s1p, s2p);

     Purpose

        Lexically compares two Pascal strings and determines whether one is less than, equal
        to, or greater than the other. This comparison ignores differences in case. This function
         is similar to PStrCaseCmp, except you pass the function handles to the string data
       instead of pointers.

     Parameters

      Name         Type                 Description

        s1p         PStr *              Pointer to a Pascal string.

        s2p         PStr *              Pointer to a Pascal string.

     Return Value

      <0, 0, or >0 if s1p is less than, equal to, or greater than s2p, respectively. Returns <0 if
      s1p is an initial substring of s2p.

     PPStrCmpPPStrCmp (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 PPStrCmp(s1p, s2p);


6526   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6526 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6527 ordinal=6527 -->
## Property and Method Reference

Property and Method Reference

Purpose

Lexically compares two Pascal strings and determines whether one is less than, equal
to, or greater than the other. This comparison is case sensitive. This function is similar
to PStrCmp, except you pass the function handles to the string data instead of
pointers.

Parameters

 Name         Type                 Description

 s1p         PStr *              Pointer to a Pascal string.

 s2p         PStr *              Pointer to a Pascal string.

Return Value

<0, 0, or >0 if s1p is less than, equal to, or greater than s2p, respectively. Returns <0 if
s1p is an initial substring of s2p.

PrintfPrintf (LabVIEW(LabVIEW ManagerManager Function)Function)
None
SPrintf, SPrintfp, PPrintf, PPrintfp, FPrintf, LStrPrintf

int32 SPrintf(CStr destCSt, CStr cfmt, ...);

int32 SPrintfp(CStr destCSt, PStr pfmt, ...);

int32 PPrintf(PStr destPSt, CStr cfmt, ...);

int32 PPrintfp(PStr destPSt, PStr pfmt, ...);

int32 FPrintf(File destFile, CStr cfmt, ...);

MgErr LStrPrintf(LStrHandle destLsh, CStr cfmt,...);


                                                    © National Instruments 6527

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6527 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6528 ordinal=6528 -->
## Property and Method Reference

Property and Method Reference

     Purpose

      These functions format data into an ASCII format to a specified destination. A format
        string describes the desired conversions. These functions take a variable number of
      arguments. Each argument follows the format string paired with a conversion
       specification embedded in the format string. The second parameter, cfmt or pfmt,
      must be cast appropriately to either type CStr or PStr.

      SPrintf and SPrintfp

     SPrintf prints to a C string, just like the C library function sprintf. sprintf
       returns the actual character count and appends a NULL byte to the end of the
       destination C string.

     SPrintfp is the same as SPrintf, except the format string is a Pascal string instead
       of a C string. As with SPrintf, SPrintfp appends a NULL byte to the end of the
       destination C string.

           If you pass NULL for destCStr, SPrintf and SPrintfp do not write data to memory.
     SPrintf and SPrintfp return the number of characters required to contain the
       resulting data, not including the terminating NULL character.

      PPrintf and PPrintfp

     PPrintf prints to a Pascal string with a maximum of 255 characters. PPrintf sets
       the length byte of the Pascal string to reflect the size of the resulting string. PPrintf
      does not append a NULL byte to the end of the string.

     PPrintfp is the same as PPrintf, except the format string is a Pascal string instead
       of a C string. As with PPrintf, PPrintfp sets the length byte of the Pascal string to
        reflect the size of the resulting string.

      FPrintf

     FPrintf prints to a file specified by the refnum in fd. FPrintf does not embed a
       length count or a terminating NULL character in the data written to the file.


6528   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6528 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6529 ordinal=6529 -->
## Property and Method Reference

Property and Method Reference

LStrPrintf

LStrPrintf prints to a LabVIEW string specified by destLsh. Because the string is a
handle that might be resized, LStrPrintf can return memory errors just as
DSSetHandleSize does.

Special Characters

These functions accept the following special characters:

Formats

These functions accept the following formats:

Conversion Specifiers

These functions use the following conversion specifiers.

Conversion Specifiers and Descriptions

 Specifier             Description

 \b                 Backspace

 \f               Form feed

                New line, which inserts the system-dependent end-of-line char(s); for
 \n                     example, CR on Mac OS X, NL on Linux, CRNL on DOS)

 \r                   Carriage return

 \s                 Space

 \t                 Tab

 %%                  Percentage character (to print %)

 %[-]                    Left-justifies what is printed; if not specified, the data is right-justified.

                        Indicates the minimum width of the field to print into. If not specified, the
                        default is 0. If less than the specified number of characters are in the data to
 [field size]
                          print, the function pads with spaces on the left if you specified -. Otherwise,
                      the function pads on the right.


                                                    © National Instruments 6529

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6529 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6530 ordinal=6530 -->
## Property and Method Reference

Property and Method Reference


         Specifier             Description

                               Sets the precision for floating-point numbers, that is, the number of
       [.precision]      characters after the decimal place. For strings, this specifies the maximum
                         number of characters to print.

                                Indicates the data size for an argument. It applies only to the d, o, u, and x
                              conversion specifiers. By default, the conversion for one of the specifiers is
       [argument size]
                           from a 16-bit integer. The flag l causes this conversion to convert the data so
                              the function assumes the data is a 32-bit integer value.

                           You can precede any of the numeric conversion characters ( x, o, d, u, b, e,
                              f) by {cc} to indicate that the number is passed by reference. cc can be
       [conversion]    iB, iW,..., cX, depending on the corresponding numeric type. If cc is
                          an asterisk ( *), the numeric type ( iB through cX) is an int16 in the
                           argument list.

       b                    Binary integer

       c                    Character

       d                   Decimal integer

         e, E                    Single-precision, floating-point number in scientific notation

       f                      Single-precision, floating-point number

       F                     Double-precision, floating-point number

         g, G                  Double-precision floating-point number in scientific notation

       H                      String handle ( LStrHandle)

       o                     Octal integer

       p                     Pascal string ( PStr)

       P                  LabVIEW string ( LStrPtr)

                               Point (passed by value) as %d,%d representing horizontal,
       q
                                   vertical coordinates

                               Point (passed by value) as hv(%d,%d) representing horizontal,
       Q
                                   vertical coordinates

                              Rectangle (passed by reference) as %d,%d,%d,%d representing top, left,
       r
                             bottom, right coordinates

                              Rectangle (passed by reference) as tlbr(%d,%d,%d,%d)
       R
                               representing top, left, bottom, right coordinates


6530   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6530 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6531 ordinal=6531 -->
## Property and Method Reference

Property and Method Reference


 Specifier             Description

 s                C String (null-terminated)

 u                  Unsigned decimal integer

 x                 Hex integer

 z                   Path

PStrBufPStrBuf (LabVIEW(LabVIEW ManagerManager Macro)Macro)

uChar *PStrBuf(s);

Purpose

Returns the address of the string data of a Pascal string, that is, the address following
the length byte.

Parameters

 Name          Type            Description

 s            PStr            Pointer to a Pascal string.

Return Value

The address of the string data of a Pascal string.

PStrCaseCmpPStrCaseCmp (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 PStrCaseCmp(s1, s2);

Purpose

Lexically compares two Pascal strings to determine whether one is less than, equal to,
or greater than the other. This comparison ignores differences in case.


                                                    © National Instruments 6531

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6531 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6532 ordinal=6532 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name          Type            Description

        s1           PStr            Pointer to a Pascal string.

        s2           PStr            Pointer to a Pascal string.

     Return Value

      <0, 0, or >0 if s1 is less than, equal to, or greater than s2, respectively. Returns <0 if s1
         is an initial substring of s2.

      PStrCatPStrCat (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 PStrCat(s1, s2);

     Purpose

      Concatenates a Pascal string, s2, to the end of another Pascal string, s1, and returns
       the result in s1. This function assumes s1 is large enough to contain the resulting
        string. If the resulting string is larger than 255 characters, the function limits the
       resulting string to 255 characters.

     Parameters

      Name          Type            Description

        s1           PStr            Pointer to a Pascal string.

        s2           PStr            Pointer to a Pascal string.

     Return Value

      The length of the resulting string.

     PStrCmpPStrCmp (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 PStrCmp(s1, s2);

6532   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6532 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6533 ordinal=6533 -->
## Property and Method Reference

Property and Method Reference

Purpose

Lexically compares two Pascal strings to determine whether one is less than, equal to,
or greater than the other. This comparison is case sensitive.

Parameters

 Name          Type            Description

 s1           PStr            Pointer to a Pascal string.

 s2           PStr            Pointer to a Pascal string.

Return Value

<0, 0, or >0 if s1 is less than, equal to, or greater than s2, respectively. Returns <0 if s1
is an initial substring of s2.

PStrCpyPStrCpy (LabVIEW(LabVIEW ManagerManager Function)Function)

PStr PStrCpy(dst, src);

Purpose

Copies the Pascal string src to the Pascal string dst. This function assumes dst is large
enough to contain src.

Parameters

 Name          Type            Description

 dst           PStr            Pointer to a Pascal string.

 src           PStr            Pointer to a Pascal string.

Return Value

A copy of the destination Pascal string pointer.


                                                    © National Instruments 6533

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6533 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6534 ordinal=6534 -->
## Property and Method Reference

Property and Method Reference

     PStrLenPStrLen (LabVIEW(LabVIEW ManagerManager Macro)Macro)

     uInt8 PStrLen(s);

     Purpose

       Returns the length of a Pascal string, that is, the value at the first byte at the specified
       address.

     Parameters

      Name          Type            Description

         s            PStr            Pointer to a Pascal string.

     PStrNCpyPStrNCpy (LabVIEW(LabVIEW ManagerManager Function)Function)

     PStr PStrNCpy(dst, src, n);

     Purpose

      Copies the Pascal string src to the Pascal string dst. If the source string is greater than
        n, this function copies only n bytes. The function assumes dst is large enough to
       contain src.

     Parameters

      Name  Type     Description

         dst    PStr    Pointer to a Pascal string.

         src    PStr    Pointer to a Pascal string.

       n     int32  Maximum number of bytes you want to copy, including the length byte.

     Return Value

      A copy of the destination Pascal string pointer.


6534   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6534 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6535 ordinal=6535 -->
## Property and Method Reference

Property and Method Reference

PToCStrPToCStr (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 PToCStr(pstr, cstr);

Purpose

Converts a Pascal string to a C string. This function works even if the pointers pstr and
cstr refer to the same memory location. The function assumes cstr is large enough to
contain pstr.

Parameters

 Name          Type            Description

 pstr          PStr            Pointer to a Pascal string.

 cstr          CStr            Pointer to a C string.

Return Value

The length of the string.

PToLStrPToLStr (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 PToLStr(pstr, lstrp);

Purpose

Converts a Pascal string to a LabVIEW string. This function works even if the pointers
pstr and lstrp refer to the same memory location. The function assumes lstrp is large
enough to contain pstr.

Parameters

 Name        Type                  Description

 pstr        PStr                  Pointer to a Pascal string.

 lstrp        LStrPtr              Pointer to a LabVIEW string.


                                                    © National Instruments 6535

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6535 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6536 ordinal=6536 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      The length of the string.

     QSortQSort (LabVIEW(LabVIEW ManagerManager Function)Function)

     void QSort(arrayp, n, elmtSize, compareProcP());

     Purpose

       Sorts an array of an arbitrary data type using the QuickSort algorithm. In addition to
       passing the array you want to sort to this routine, you also pass a comparison
      procedure that this sort routine then uses to compare elements in the array.

      The comparison routine should return a number less than zero if a is less than b, zero if
      a is equal to b, and a number greater than zero if a is greater than b.

      You should declare the comparison routine to have the following parameters and
       return type:

       int32 compareProcP(UPtr a, UPtr b);

     Parameters

      Name         Type                Description

        arrayp       UPtr               Pointer to an array of data.

       n           int32           Number of elements in the array you want to sort.

        elmtSize     int32              Size in bytes of an array element.

                                       Comparison routine you want QSort to use to compare
       compareProcP CompareProcPtr  array elements. QSort passes this routine the addresses of
                                      two elements that it needs to compare.

    RandomGenRandomGen (LabVIEW(LabVIEW ManagerManager Function)Function)

     void RandomGen(xp);


6536   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6536 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6537 ordinal=6537 -->
## Property and Method Reference

Property and Method Reference

Purpose

Generates a random number between 0 and 1 and stores it at xp.

Parameters

 Name Type         Description

                     Location to store the resulting double-precision floating-point random
 xp    float64 *                   number. This parameter is a pointer.

SecsToDateSecsToDate (LabVIEW(LabVIEW ManagerManager Function)Function)

void SecsToDate(secs, dateRecordP);

Purpose

Converts the seconds since 12:00 a.m., Friday, January 1, 1904, Universal Time
[01-01-1904 00:00:00] into a data structure containing numerical information about the
date, including the year ( 1600 through 3000), the month ( 1 through 12), the day of
the year ( 1 through 366), the day of the month ( 1 through 31), the day of the week (
1 through 7), the hour ( 0 through 23), the minute ( 0 through 59), and the second ( 0
through 59), and a value indicating whether the time specified uses daylight savings
time.

Parameters

 Name       Type         Description

                         Seconds since 12:00 a.m., Friday, January 1, 1904, Universal Time
 secs       uInt32                            [01-01-1904 00:00:00].

                             Pointer to a DateRec structure. SecsToDate stores the converted
 dateRecordP DateRec * date in the fields of the date structure referred to by dateRecordP.
                             This parameter is a pointer.

SetALongSetALong (LabVIEW(LabVIEW ManagerManager Macro)Macro)

void SetALong(p,x);

                                                    © National Instruments 6537

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6537 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6538 ordinal=6538 -->
## Property and Method Reference

Property and Method Reference

     Purpose

       Stores an int32 at the address specified by a void pointer. This function can store an
     int32 at any address, even if the int32 is not long word aligned on a platform that
       enforces alignment.

     Parameters

      Name  Type      Description

       p     void *  Address at which you want to store an int32. This parameter is a pointer.

        x     int32    Value you want to store at the specified address.

      StrCatStrCat (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 StrCat(s1, s2);

     Purpose

      Concatenates a C string, s2, to the end of another C string, s1, returning the result in
        s1. This function assumes s1 is large enough to contain the resulting string.

     Parameters

      Name            Type              Description

        s1             CStr              Pointer to a C string.

        s2             CStr              Pointer to a C string.

     Return Value

      The length of the resulting string.

     StrCmpStrCmp (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 StrCmp(s1, s2);


6538   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6538 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6539 ordinal=6539 -->
## Property and Method Reference

Property and Method Reference

Purpose

Lexically compares two strings to determine whether one is less than, equal to, or
greater than the other.

Parameters

 Name            Type              Description

 s1             CStr              Pointer to a C string.

 s2             CStr              Pointer to a C string.

Return Value

<0, 0, or >0 if s1 is less than, equal to, or greater than s2, respectively. Returns <0 if s1
is an initial substring of s2.

StrCpyStrCpy (LabVIEW(LabVIEW ManagerManager Function)Function)

CStr StrCpy(dst, src);

Purpose

Copies the C string src to the C string dst. This function assumes dst is large enough to
contain src.

Parameters

 Name            Type              Description

 dst            CStr              Pointer to a C string.

 src            CStr              Pointer to a C string.

Return Value

A copy of the destination C string pointer.


                                                    © National Instruments 6539

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6539 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6540 ordinal=6540 -->
## Property and Method Reference

Property and Method Reference

      StrLenStrLen (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 StrLen(s);

     Purpose

       Returns the length of a C string.

     Parameters

      Name            Type              Description

         s              CStr              Pointer to a C string.

     Return Value

      The number of characters in the C string, not including the NULL terminating
       character.

     StrNCaseCmpStrNCaseCmp (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 StrNCaseCmp(s1, s2, n);

     Purpose

        Lexically compares two strings to determine whether one is less than, equal to, or
       greater than the other, limiting the comparison to n characters. This comparison
       ignores differences in case.

     Parameters

      Name    Type        Description

        s1      CStr        Pointer to a C string.

        s2      CStr        Pointer to a C string.

       n      size_t    Maximum number of characters you want to compare.


6540   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6540 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6541 ordinal=6541 -->
## Property and Method Reference

Property and Method Reference

Return Value

<0, 0, or >0 if s1 is less than, equal to, or greater than s2, respectively. Returns <0 if s1
is an initial substring of s2.

StrNCmpStrNCmp (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 StrNCmp(s1, s2, n);

Purpose

Lexically compares two strings to determine whether one is less than, equal to, or
greater than the other, limiting the comparison to n characters.

Parameters

 Name    Type        Description

 s1      CStr        Pointer to a C string.

 s2      CStr        Pointer to a C string.

 n      size_t    Maximum number of characters you want to compare.

Return Value

<0, 0, or >0 if s1 is less than, equal to, or greater than s2, respectively. Returns <0 if s1
is an initial substring of s2.

StrNCpyStrNCpy (LabVIEW(LabVIEW ManagerManager Function)Function)

CStr StrNCpy(dst, src, n);

Purpose

Copies the C string src to the C string dst. If the source string is less than n characters,
the function pads the destination with NULL characters. If the source string is greater
than n, only n characters are copied. This function assumes dst is large enough to
contain src.

                                                    © National Instruments 6541

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6541 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6542 ordinal=6542 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name    Type         Description

         dst      CStr         Pointer to a C string.

         src      CStr         Pointer to a C string.

       n       size_t    Maximum number of characters you want to copy.

     Return Value

      A copy of the destination C string pointer.

     TimeCStringTimeCString (LabVIEW(LabVIEW ManagerManager Function)Function)

     CStr TimeCString(secs, fmt);

     Purpose

       Returns a pointer to a string representing the time of day corresponding to t seconds
        after 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. Date
       formats vary with your system configuration.

           Note This function was formerly called TimeString.

     Parameters

      Name Type     Description

                       Seconds since 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904
        sec   uInt32                            00:00:00].

                           Indicates the format of the returned time string, using the following values:

                                         • 0—hh:mm format, where hh is the hour (0 through 23, with 0 as midnight),
        fmt   int32      and the mm is the minute (0 through 59).
                                         • 1—hh:mm:ss format, where hh is the hour, mm is the minute (0 through 59),
                         and ss is the second (0 through 59).


6542   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6542 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6543 ordinal=6543 -->
## Property and Method Reference

Property and Method Reference

Return Value

The time as a C string.

TimeInSecsTimeInSecs (LabVIEW(LabVIEW ManagerManager Function)Function)

uint32 TimeInSecs();

Return Value

The current date and time in seconds relative to 12:00 a.m., Friday, January 1, 1904,
Universal Time [01-01-1904 00:00:00].

ToLowerToLower (LabVIEW(LabVIEW ManagerManager Function)Function)

uChar ToLower(c);

Purpose

Returns the lowercase value of c if c is an uppercase alphabetic character. Otherwise,
this function returns c unmodified. This function also works for international
characters ( Ä to ä, and so on).

Parameters

 Name        Type            Description

 c          int32          Character you want to analyze.

Return Value

The lowercase value of c.

ToUpperToUpper (LabVIEW(LabVIEW ManagerManager Function)Function)

uChar ToUpper(c);


                                                    © National Instruments 6543

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6543 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6544 ordinal=6544 -->
## Property and Method Reference

Property and Method Reference

     Purpose

       Returns the uppercase value of c if c is a lowercase alphabetic character. Otherwise,
        this function returns c unmodified. This function also works for international
       characters ( ä to Ä, and so on).

     Parameters

      Name        Type            Description

        c          int32          Character you want to analyze.

     Return Value

      The uppercase value of c.

     UnusedUnused (LabVIEW(LabVIEW ManagerManager Macro)Macro)

       void Unused(x)

     Purpose

       Indicates that a function parameter or local variable is not used by that function. This
         is useful for suppressing compiler warnings for many compilers. This macro does not
      use a semicolon.

     Parameters

      Name       Type       Description

        x       —         Unused parameter or local variable.

    WordWord (LabVIEW(LabVIEW ManagerManager Macro)Macro)

     int16 Word(hi, lo);


6544   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6544 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6545 ordinal=6545 -->
## Property and Method Reference

Property and Method Reference

Purpose

Creates an int16 from two int8 parameters.

Parameters

 Name       Type         Description

 hi         int8       High int8 for the resulting int16.

 lo         int8      Low int8 for the resulting int16.

Return Value

The resulting int16.

MathMath PlotsPlots

This section describes the properties and methods of Math Plots

© 2005–2023 National Instruments Corporation. All rights reserved. Refer to the
<National Instruments>\_Legal Information directory for information
about NI copyright, patents, trademarks, warranties, product warnings, and export
compliance.

2D2D GraphsGraphs

This section describes the properties and methods of 2D Graphs

2D2D CompassCompass

2D2D CompassCompass PropertiesProperties


 Property               Description

 Graph:Graph Legend
                   Shows the graph legend.
 Visible


                                                    © National Instruments 6545

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6545 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6546 ordinal=6546 -->
## Property and Method Reference

Property and Method Reference


        Property               Description

         Graph:Plot Legend                          Shows the plot legend.          Visible

         Graph:Plot Legend         If TRUE, resizes the plot legend to the width of the longest plot name
        Auto Size                 visible in the legend.

         Graph:Plot Legend                                Sets the number of rows in the plot legend.       Number

        Graph:X Scrollbar                                 Displays the x-axis scroll bar for the graph or chart.          Visible

         Graph:Scale Legend                          Shows the scale legend.          Visible

        Graph:Cursor Legend                                 Displays the cursor legend.
          Visible

         Graph:Plot FG Color     Specifies the foreground color of the plot area.

         Graph:Plot BG Color     Specifies the background color of the plot area.

                                  Specifies the width of the master object, excluding the label caption and        Graph:Bounds Width
                               the other palette in pixels.

                                  Specifies the height of the master object, excluding the label caption and
        Graph:Bounds Height                               the other palette in pixels.

        Format:R Scale Format  Sets the format string of the R scale.

       R Scale:Editable        Allows you to edit the value of the scale.

       R Scale:Visible        Shows the scale.

       R Scale:Style            Specifies the scale style.

       R Scale:Scale Fit          Fits the scale to the data.

       R Scale:Tick:Major Tick
                                Sets the color of the major tick mark.
         Color

       R Scale:Tick:Minor Tick
                                Sets the color of the minor tick mark.
         Color

       R Scale:Grid:Major Grid
                                Sets the color of the major grid on the scale.
         Color

       R Scale:Grid:Minor Grid
                                Sets the color of the minor grid on the scale.
         Color


6546   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6546 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6547 ordinal=6547 -->
## Property and Method Reference

Property and Method Reference


Property               Description

R                       Sets the minimum value of the scale.Scale:Range:Minimum

R                       Sets the maximum value of the scale.Scale:Range:Maximum

R                       Sets the increment value of the scale.Scale:Range:Increment

R Scale:Range:Minor                       Sets the minor increment value of the scale.Increment

R Scale:Range:Start     Sets the start value of the scale.

R Scale:Marker:Visible   Indicates whether the tick marker is visible.

R Scale:Marker:FG                         Specifies the foreground color of the tick marker.
Color

R Scale:Marker:BG                         Specifies the background color of the tick marker.
Color

R Scale:Marker:Font                         Specifies the font name of the tick marker.
Name

R Scale:Marker:Font
                         Specifies the font size of the tick marker.Size

R Scale:Marker:Font
                         Indicates whether the text is bold.Bold

R Scale:Marker:Font
                         Indicates whether the text is italic.Italic

R Scale:Marker:Font
                         Indicates whether the text is in the strikeout font.
Strike

R Scale:Marker:Font
                         Indicates whether the text is underlined.
Underline

R Scale:Name
                         Indicates whether the name label is visible.
Label:Visible

R Scale:Name Label:FG
                         Specifies the foreground color of the name label.
Color

R Scale:Name
                         Specifies the background color of the name label.
Label:BG Color


                                                    © National Instruments 6547

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6547 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6548 ordinal=6548 -->
## Property and Method Reference

Property and Method Reference


        Property               Description

       R Scale:Name                                  Specifies the font name of the name label.         Label:Font Name

       R Scale:Name                                  Specifies the font size of the name label.         Label:Font Size

       R Scale:Name                                  Indicates whether the text is bold.         Label:Font Bold

       R Scale:Name                                  Indicates whether the text is italic.         Label:Font Italic

       R Scale:Name                                  Indicates whether the text is in the strikeout font.         Label:Font Strike

       R Scale:Name                                  Indicates whether the text is underlined.
         Label:Font Underline

       R Scale:Name                               Gets and sets the justification of the text.
          Label:Justification

       R Scale:Name                                 Displays text in the scale.
         Label:Text

                               Gets and sets the active cursor and sets properties and methods on the
         Cursor:Active Cursor                                  active cursor.

        Cursor:Name           Displays text that is associated with the cursor in the plot area.

         Cursor:Color           Sets the color of the cursor, including its point, arrow, and name.

                            Draws the symbol at the focal point of the cursor in combination with
         Cursor:Style                                Point Style.

                            Draws the symbol at the focal point of the cursor in combination with
         Cursor:Point Style
                                     Style.

        Cursor:Name Visible       If TRUE, displays the cursor name in the plot area.

         Cursor:Allow Drag          If TRUE, allows you to drag the cursor.

        Cursor:Mode            Specifies the way the cursor snaps to the plots in the plot area.

         Cursor:Plot              Specifies the plot associated with the cursor.

         Cursor:Index            Specifies the array index of the point where the cursor snaps.

         Cursor:Position         Specifies the position of the cursor in terms of XY coordinates.

         Cursor:X Scale          Sets the x-scale of the cursor.


6548   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6548 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6549 ordinal=6549 -->
## Property and Method Reference

Property and Method Reference


 Property               Description

 Cursor:Y Scale          Sets the y-scale of the cursor.

                          Specifies the array that contains the indexes of the plots that the cursor Cursor:Watch Plots                      watches when the Watch All Plots property is set to FALSE.

                                      If TRUE, sets the cursor to watch all plots in the plot area. If FALSE, sets the Cursor:Watch All Plots
                        cursor to watch only the plots specified by the Watch Plots property.

 Cursor:Plot Area         Specifies the plot area associated with the cursor.

                        Sets the coordinates of the label center position relative to the cursor Cursor:Label Offset                          center.

 Cursor:Selection Color  Sets the color of the cursor row selected in the cursor legend.

 Cursor:Line Style        Specifies the style of the line that displays the active cursor.

 Cursor:Line Width       Specifies the width of the line used to display the active cursor.

 Cursor:Visible        Shows the cursor.

 Plot Specific:Active     Gets or sets the active plot. After you get or set the active plot, you then
 Plot                 can set properties or invoke methods that affect only the specified plot.

 Plot Specific:Compass                   Shows the name of the plot.
 Name

 Plot Specific:Compass
                   Shows the color of the plot. Color

 Plot Specific:Compass
                          Specifies the line style. Line Style

 Plot Specific:Compass
                        Sets the width of the plot. Line Width

 Plot Specific:Compass
                        Sets the symbol size for the compass.
 Size

 Plot Specific:Show
                   Shows the phase scale around the plot area.
 Phase Scale

 Annotation List         Returns an array of information about all annotations.

Graph:GraphGraph:Graph LegendLegend VisibleVisible

Shows the graph legend.

                                                    © National Instruments 6549

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6549 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6550 ordinal=6550 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:PlotGraph:Plot LegendLegend VisibleVisible

      Shows the plot legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6550   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6550 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6551 ordinal=6551 -->
## Property and Method Reference

Property and Method Reference

Graph:PlotGraph:Plot LegendLegend AutoAuto SizeSize

If TRUE, resizes the plot legend to the width of the longest plot name visible in the
legend.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:PlotGraph:Plot LegendLegend NumberNumber

Sets the number of rows in the plot legend.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

                                                    © National Instruments 6551

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6551 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6552 ordinal=6552 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:XGraph:X ScrollbarScrollbar VisibleVisible

       Displays the x-axis scroll bar for the graph or chart.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:ScaleGraph:Scale LegendLegend VisibleVisible

      Shows the scale legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

6552   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6552 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6553 ordinal=6553 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:CursorGraph:Cursor LegendLegend VisibleVisible

Displays the cursor legend.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:PlotGraph:Plot FGFG ColorColor

Specifies the foreground color of the plot area.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 6553

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6553 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6554 ordinal=6554 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:PlotGraph:Plot BGBG ColorColor

       Specifies the background color of the plot area.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:BoundsGraph:Bounds WidthWidth

       Specifies the width of the master object, excluding the label caption and the other
       palette in pixels.

6554   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6554 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6555 ordinal=6555 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:BoundsGraph:Bounds HeightHeight

Specifies the height of the master object, excluding the label caption and the other
palette in pixels.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6555

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6555 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6556 ordinal=6556 -->
## Property and Method Reference

Property and Method Reference

   Format:RFormat:R ScaleScale FormatFormat

       Sets the format string of the R scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:EditableScale:Editable

       Allows you to edit the value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6556   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6556 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6557 ordinal=6557 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:VisibleScale:Visible

Shows the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:StyleScale:Style

Specifies the scale style.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6557

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6557 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6558 ordinal=6558 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:ScaleScale:Scale FitFit

        Fits the scale to the data.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:Tick:MajorScale:Tick:Major TickTick ColorColor

       Sets the color of the major tick mark.

     Remarks

      The following table lists the characteristics of this property.


6558   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6558 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6559 ordinal=6559 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:Tick:MinorScale:Tick:Minor TickTick ColorColor

Sets the color of the minor tick mark.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:Grid:MajorScale:Grid:Major GridGrid ColorColor

Sets the color of the major grid on the scale.


                                                    © National Instruments 6559

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6559 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6560 ordinal=6560 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:Grid:MinorScale:Grid:Minor GridGrid ColorColor

       Sets the color of the minor grid on the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6560   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6560 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6561 ordinal=6561 -->
## Property and Method Reference

Property and Method Reference

RR Scale:Range:MinimumScale:Range:Minimum

Sets the minimum value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:Range:MaximumScale:Range:Maximum

Sets the maximum value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6561

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6561 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6562 ordinal=6562 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:Range:IncrementScale:Range:Increment

       Sets the increment value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:Range:MinorScale:Range:Minor IncrementIncrement

       Sets the minor increment value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6562   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6562 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6563 ordinal=6563 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:Range:StartScale:Range:Start

Sets the start value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:Marker:VisibleScale:Marker:Visible

Indicates whether the tick marker is visible.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6563

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6563 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6564 ordinal=6564 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:Marker:FGScale:Marker:FG ColorColor

       Specifies the foreground color of the tick marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:Marker:BGScale:Marker:BG ColorColor

       Specifies the background color of the tick marker.


6564   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6564 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6565 ordinal=6565 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:Marker:FontScale:Marker:Font NameName

Specifies the font name of the tick marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6565

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6565 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6566 ordinal=6566 -->
## Property and Method Reference

Property and Method Reference

   RR Scale:Marker:FontScale:Marker:Font SizeSize

       Specifies the font size of the tick marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:Marker:FontScale:Marker:Font BoldBold

       Indicates whether the text is bold.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6566   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6566 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6567 ordinal=6567 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:Marker:FontScale:Marker:Font ItalicItalic

Indicates whether the text is italic.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:Marker:FontScale:Marker:Font StrikeStrike

Indicates whether the text is in the strikeout font.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6567

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6567 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6568 ordinal=6568 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:Marker:FontScale:Marker:Font UnderlineUnderline

       Indicates whether the text is underlined.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:NameScale:Name Label:VisibleLabel:Visible

       Indicates whether the name label is visible.

     Remarks

      The following table lists the characteristics of this property.


6568   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6568 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6569 ordinal=6569 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:NameScale:Name Label:FGLabel:FG ColorColor

Specifies the foreground color of the name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:NameScale:Name Label:BGLabel:BG ColorColor

Specifies the background color of the name label.


                                                    © National Instruments 6569

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6569 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6570 ordinal=6570 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:NameScale:Name Label:FontLabel:Font NameName

       Specifies the font name of the name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6570   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6570 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6571 ordinal=6571 -->
## Property and Method Reference

Property and Method Reference

RR Scale:NameScale:Name Label:FontLabel:Font SizeSize

Specifies the font size of the name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:NameScale:Name Label:FontLabel:Font BoldBold

Indicates whether the text is bold.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6571

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6571 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6572 ordinal=6572 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:NameScale:Name Label:FontLabel:Font ItalicItalic

       Indicates whether the text is italic.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:NameScale:Name Label:FontLabel:Font StrikeStrike

       Indicates whether the text is in the strikeout font.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6572   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6572 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6573 ordinal=6573 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:NameScale:Name Label:FontLabel:Font UnderlineUnderline

Indicates whether the text is underlined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

RR Scale:NameScale:Name Label:JustificationLabel:Justification

Gets and sets the justification of the text.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6573

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6573 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6574 ordinal=6574 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   RR Scale:NameScale:Name Label:TextLabel:Text

       Displays text in the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:ActiveCursor:Active CursorCursor

       Gets and sets the active cursor and sets properties and methods on the active cursor.


6574   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6574 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6575 ordinal=6575 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:NameCursor:Name

Displays text that is associated with the cursor in the plot area.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6575

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6575 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6576 ordinal=6576 -->
## Property and Method Reference

Property and Method Reference

    Cursor:ColorCursor:Color

       Sets the color of the cursor, including its point, arrow, and name.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:StyleCursor:Style

      Draws the symbol at the focal point of the cursor in combination with Point Style.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6576   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6576 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6577 ordinal=6577 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:PointCursor:Point StyleStyle

Draws the symbol at the focal point of the cursor in combination with Style.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:NameCursor:Name VisibleVisible

If TRUE, displays the cursor name in the plot area.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6577

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6577 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6578 ordinal=6578 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:AllowCursor:Allow DragDrag

           If TRUE, allows you to drag the cursor.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Cursor:ModeCursor:Mode

       Specifies the way the cursor snaps to the plots in the plot area.

     Remarks

      The following table lists the characteristics of this property.


6578   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6578 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6579 ordinal=6579 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:PlotCursor:Plot

Specifies the plot associated with the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:IndexCursor:Index

Specifies the array index of the point where the cursor snaps.


                                                    © National Instruments 6579

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6579 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6580 ordinal=6580 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:PositionCursor:Position

       Specifies the position of the cursor in terms of XY coordinates.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6580   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6580 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6581 ordinal=6581 -->
## Property and Method Reference

Property and Method Reference

Cursor:XCursor:X ScaleScale

Sets the x-scale of the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:YCursor:Y ScaleScale

Sets the y-scale of the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6581

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6581 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6582 ordinal=6582 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Cursor:WatchCursor:Watch PlotsPlots

       Specifies the array that contains the indexes of the plots that the cursor watches when
       the Watch All Plots property is set to FALSE.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Cursor:WatchCursor:Watch AllAll PlotsPlots

           If TRUE, sets the cursor to watch all plots in the plot area. If FALSE, sets the cursor to
      watch only the plots specified by the Watch Plots property.

     Remarks

      The following table lists the characteristics of this property.


        Data type


6582   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6582 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6583 ordinal=6583 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:PlotCursor:Plot AreaArea

Specifies the plot area associated with the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:LabelCursor:Label OffsetOffset

Sets the coordinates of the label center position relative to the cursor center.


                                                    © National Instruments 6583

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6583 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6584 ordinal=6584 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:SelectionCursor:Selection ColorColor

       Sets the color of the cursor row selected in the cursor legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6584   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6584 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6585 ordinal=6585 -->
## Property and Method Reference

Property and Method Reference

Cursor:LineCursor:Line StyleStyle

Specifies the style of the line that displays the active cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:LineCursor:Line WidthWidth

Specifies the width of the line used to display the active cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6585

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6585 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6586 ordinal=6586 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:VisibleCursor:Visible

      Shows the cursor.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:ActiveSpecific:Active PlotPlot

       Gets or sets the active plot. After you get or set the active plot, you then can set
       properties or invoke methods that affect only the specified plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


6586   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6586 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6587 ordinal=6587 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:CompassSpecific:Compass NameName

Shows the name of the plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:CompassSpecific:Compass ColorColor

Shows the color of the plot.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 6587

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6587 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6588 ordinal=6588 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:CompassSpecific:Compass LineLine StyleStyle

       Specifies the line style.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:CompassSpecific:Compass LineLine WidthWidth

       Sets the width of the plot.


6588   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6588 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6589 ordinal=6589 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:CompassSpecific:Compass SizeSize

Sets the symbol size for the compass.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6589

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6589 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6590 ordinal=6590 -->
## Property and Method Reference

Property and Method Reference

    PlotPlot Specific:ShowSpecific:Show PhasePhase ScaleScale

      Shows the phase scale around the plot area.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   AnnotationAnnotation ListList

       Returns an array of information about all annotations.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6590   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6590 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6591 ordinal=6591 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

2D2D CompassCompass MethodsMethods


 Method            Description

 Export Image       Exports an image of the graph to the clipboard or disk.

ExportExport ImageImage

Exports an image of the graph to the clipboard or disk.

Parameters

 Name                        Data type          Required          Description

 File Type                                           Yes

 Target                                              Yes

 Path                                                Yes

 Hide Grid                                           Yes

 Always Overwrite                                    Yes

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes

 Settable when the VI is running                                                       Yes

 Loads the front panel into memory                                                    Yes

 Need to authenticate before use                                         No


                                                    © National Instruments 6591

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6591 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6592 ordinal=6592 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                                     No

    2D2D ErrorError BarBar

     2D2D ErrorError BarBar PropertiesProperties


        Property               Description

        Graph:Graph Legend                          Shows the graph legend.          Visible

         Graph:Plot Legend
                          Shows the plot legend.          Visible

         Graph:Plot Legend         If TRUE, resizes the plot legend to the width of the longest plot name
        Auto Size                 visible in the legend.

         Graph:Plot Legend                                Sets the number of rows in the plot legend.
       Number

        Graph:X Scrollbar                                 Displays the x-axis scroll bar for the graph or chart.
          Visible

         Graph:Scale Legend                          Shows the scale legend.
          Visible

        Graph:Cursor Legend                                 Displays the cursor legend.
          Visible

         Graph:Plot FG Color     Specifies the foreground color of the plot area.

         Graph:Plot BG Color     Specifies the background color of the plot area.

                                  Specifies the width of the master object, excluding the label caption and
        Graph:Bounds Width
                               the other palette in pixels.

                                  Specifies the height of the master object, excluding the label caption and
        Graph:Bounds Height
                               the other palette in pixels.

        Format:X Scale Format  Sets the format string of the X scale.

        Format:Y Scale Format  Sets the format string of the Y scale.

        X Scale:Editable        Allows you to edit the value of the scale.

                                                   If TRUE, reverses the position of the minimum and maximum values on
        X Scale:Flipped
                               the scale.


6592   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6592 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6593 ordinal=6593 -->
## Property and Method Reference

Property and Method Reference


Property               Description

X Scale:Mapping Mode  Specifies the scale mapping mode.

X Scale:Visible        Shows the scale.

X Scale:Style            Specifies the scale style.

X Scale:Scale Fit          Fits the scale to the data.

X Scale:Offset and                       Sets the offset, or initial, value for scaling data using (Deltax) xx + xo.Multiplier:Offset

X Scale:Offset and                       Sets the multiplier, or interval, for scaling data using (Deltax) xx + xo.Multiplier:Multiplier

X Scale:Tick:Major Tick                       Sets the color of the major tick mark.Color

X Scale:Tick:Minor Tick                       Sets the color of the minor tick mark.
Color

X Scale:Grid:Major Grid                       Sets the color of the major grid on the scale.
Color

X Scale:Grid:Minor Grid                       Sets the color of the minor grid on the scale.
Color

X
                       Sets the minimum value of the scale.Scale:Range:Minimum

X
                       Sets the maximum value of the scale.Scale:Range:Maximum

X
                       Sets the increment value of the scale.Scale:Range:Increment

X Scale:Range:Minor
                       Sets the minor increment value of the scale.
Increment

X Scale:Range:Start     Sets the start value of the scale.

X Scale:Marker:Visible   Indicates whether the tick marker is visible.

X Scale:Marker:FG
                         Specifies the foreground color of the tick marker.
Color

X Scale:Marker:BG
                         Specifies the background color of the tick marker.
Color

X Scale:Marker:Font
                         Specifies the font name of the tick marker.
Name

                                                    © National Instruments 6593

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6593 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6594 ordinal=6594 -->
## Property and Method Reference

Property and Method Reference


        Property               Description

        X Scale:Marker:Font                                  Specifies the font size of the tick marker.         Size

        X Scale:Marker:Font                                  Indicates whether the text is bold.        Bold

        X Scale:Marker:Font                                  Indicates whether the text is italic.            Italic

        X Scale:Marker:Font                                  Indicates whether the text is in the strikeout font.          Strike

        X Scale:Marker:Font                                  Indicates whether the text is underlined.         Underline

        X Scale:Name                                  Indicates whether the name label is visible.
          Label:Visible

        X Scale:Name Label:FG                                  Specifies the foreground color of the name label.
         Color

        X Scale:Name Label:BG                                  Specifies the background color of the name label.
         Color

        X Scale:Name
                                  Specifies the font name of the name label.         Label:Font Name

        X Scale:Name
                                  Specifies the font size of the name label.         Label:Font Size

        X Scale:Name
                                  Indicates whether the text is bold.         Label:Font Bold

        X Scale:Name                                  Indicates whether the text is italic.
         Label:Font Italic

        X Scale:Name
                                  Indicates whether the text is in the strikeout font.
         Label:Font Strike

        X Scale:Name
                                  Indicates whether the text is underlined.
         Label:Font Underline

        X Scale:Name
                               Gets and sets the justification of the text.
          Label:Justification

        X Scale:Name
                                 Displays text in the scale.
         Label:Text

        Y Scale:Editable        Allows you to edit the value of the scale.

6594   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6594 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6595 ordinal=6595 -->
## Property and Method Reference

Property and Method Reference


Property               Description

                                     If TRUE, reverses the position of the minimum and maximum values onY Scale:Filpped                      the scale.

Y Scale:Mapping Mode  Specifies the scale mapping mode.

Y Scale:Visible        Shows the scale.

Y Scale:Style            Specifies the scale style.

Y Scale:Scale Fit          Fits the scale to the data.

Y Scale:Offset and                       Sets the offset, or initial, value for scaling data using (Deltax) xx + xo.Multiplier:Offset

Y Scale:Offset and                       Sets the multiplier, or interval, for scaling data using (Deltax) xx + xo.Multiplier:Multiplier

Y Scale:Tick:Major Tick                       Sets the color of the major tick mark.
Color

Y Scale:Tick:Minor Tick                       Sets the color of the minor tick mark.
Color

Y Scale:Grid:Major Grid                       Sets the color of the major grid on the scale.
Color

Y Scale:Grid:Minor Grid
                       Sets the color of the minor grid on the scale.Color

Y
                       Sets the increment value of the scale.Scale:Range:Increment

Y
                       Sets the maximum value of the scale.Scale:Range:Maximum

Y
                       Sets the minimum value of the scale.
Scale:Range:Minimum

Y Scale:Range:Minor
                       Sets the minor increment value of the scale.
Increment

Y Scale:Range:Start     Sets the start value of the scale.

Y Scale:Marker:Visible   Indicates whether the tick marker is visible.

Y Scale:Marker:FG
                         Specifies the foreground color of the tick marker.
Color

Y Scale:Marker:BG
                         Specifies the background color of the tick marker.
Color

                                                    © National Instruments 6595

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6595 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6596 ordinal=6596 -->
## Property and Method Reference

Property and Method Reference


        Property               Description

        Y Scale:Marker:Font                                  Specifies the font name of the tick marker.      Name

        Y Scale:Marker:Font                                  Specifies the font size of the tick marker.         Size

        Y Scale:Marker:Font                                  Indicates whether the text is bold.        Bold

        Y Scale:Marker:Font                                  Indicates whether the text is italic.            Italic

        Y Scale:Marker:Font                                  Indicates whether the text is in the strikeout font.          Strike

        Y Scale:Marker:Font                                  Indicates whether the text is underlined.
         Underline

        Y Scale:Name                                  Indicates whether the name label is visible.
          Label:Visible

        Y Scale:Name Label:FG                                  Specifies the foreground color of the name label.
         Color

        Y Scale:Name Label:BG
                                  Specifies the background color of the name label.         Color

        Y Scale:Name
                                  Specifies the font name of the name label.         Label:Font Name

        Y Scale:Name
                                  Specifies the font size of the name label.         Label:Font Size

        Y Scale:Name                                  Indicates whether the text is bold.
         Label:Font Bold

        Y Scale:Name
                                  Indicates whether the text is italic.
         Label:Font Italic

        Y Scale:Name
                                  Indicates whether the text is in the strikeout font.
         Label:Font Strike

        Y Scale:Name
                                  Indicates whether the text is underlined.
         Label:Font Underline

        Y Scale:Name
                               Gets and sets the justification of the text.
          Label:Justification

        Y Scale:Name           Displays text in the scale.

6596   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6596 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6597 ordinal=6597 -->
## Property and Method Reference

Property and Method Reference


Property               Description

Label:Text

                      Gets and sets the active cursor and sets properties and methods on theCursor:Active Cursor                         active cursor.

Cursor:Name           Displays text that is associated with the cursor in the plot area.

Cursor:Color           Sets the color of the cursor, including its point, arrow, and name.

                    Draws the symbol at the focal point of the cursor in combination withCursor:Style                       Point Style.

                    Draws the symbol at the focal point of the cursor in combination withCursor:Point Style
                           Style.

Cursor:Name Visible       If TRUE, displays the cursor name in the plot area.

Cursor:Allow Drag          If TRUE, allows you to drag the cursor.

Cursor:Mode            Specifies the way the cursor snaps to the plots in the plot area.

Cursor:Plot              Specifies the plot associated with the cursor.

Cursor:Index            Specifies the array index of the point where the cursor snaps.

Cursor:Position         Specifies the position of the cursor in terms of XY coordinates.

Cursor:X Scale          Sets the x-scale of the cursor.

Cursor:Y Scale          Sets the y-scale of the cursor.

                         Specifies the array that contains the indexes of the plots that the cursorCursor:Watch Plots                     watches when the Watch All Plots property is set to FALSE.

                                     If TRUE, sets the cursor to watch all plots in the plot area. If FALSE, sets theCursor:Watch All Plots
                       cursor to watch only the plots specified by the Watch Plots property.

Cursor:Plot Area         Specifies the plot area associated with the cursor.

                       Sets the coordinates of the label center position relative to the cursor
Cursor:Label Offset
                         center.

Cursor:Selection Color  Sets the color of the cursor row selected in the cursor legend.

Cursor:Line Style        Specifies the style of the line that displays the active cursor.

Cursor:Line Width       Specifies the width of the line used to display the active cursor.

Cursor:Visible        Shows the cursor.

Plot Specific:Active     Gets or sets the active plot. After you get or set the active plot, you then


                                                    © National Instruments 6597

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6597 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6598 ordinal=6598 -->
## Property and Method Reference

Property and Method Reference


        Property               Description

         Plot                 can set properties or invoke methods that affect only the specified plot.

         Plot Specific:Error Bar                          Shows the name of the plot.      Name

         Plot Specific:Error Bar                                  Specifies the line style.
         Line Style

         Plot Specific:Error Bar                                Sets the width of the plot (0-5).         Line Width

         Plot Specific:Error Bar                                Sets the point style of the error bar.
         Point Style

         Plot Specific:Error Bar                                  Specifies the interpolation of the plot.         Interpolation

         Plot Specific:Error Bar                                Sets the color of the plot.         Color

         Plot Specific:Error Bar                                Sets the color of the point and the fill.         Point Fill Color

         Plot Specific:Error Bar                                Sets the baseline of the fill.             Fill to

         Plot Specific:Error Bar                                Sets the symbol size for the error bar.         Size

         Plot Specific:Marker     Specifies the error marker line style, as shown on the shortcut menu from
         Line Style                top-left to bottom-right.

         Plot Specific:Marker                                Sets the width of the error marker.         Line Width

         Plot Specific:Marker
                                Sets the color of the error bar line.
         Line Color

         Plot Specific:Error Bar   Sets whether the error bar displays on the Y axis only or on both X and Y
       Mode                   axes.

        Annotation List         Returns an array of information about all annotations.

   Graph:GraphGraph:Graph LegendLegend VisibleVisible

      Shows the graph legend.

6598   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6598 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6599 ordinal=6599 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:PlotGraph:Plot LegendLegend VisibleVisible

Shows the plot legend.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6599

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6599 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6600 ordinal=6600 -->
## Property and Method Reference

Property and Method Reference

    Graph:PlotGraph:Plot LegendLegend AutoAuto SizeSize

           If TRUE, resizes the plot legend to the width of the longest plot name visible in the
       legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:PlotGraph:Plot LegendLegend NumberNumber

       Sets the number of rows in the plot legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

6600   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6600 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6601 ordinal=6601 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:XGraph:X ScrollbarScrollbar VisibleVisible

Displays the x-axis scroll bar for the graph or chart.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:ScaleGraph:Scale LegendLegend VisibleVisible

Shows the scale legend.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

                                                    © National Instruments 6601

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6601 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6602 ordinal=6602 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:CursorGraph:Cursor LegendLegend VisibleVisible

       Displays the cursor legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:PlotGraph:Plot FGFG ColorColor

       Specifies the foreground color of the plot area.

     Remarks

      The following table lists the characteristics of this property.

6602   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6602 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6603 ordinal=6603 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:PlotGraph:Plot BGBG ColorColor

Specifies the background color of the plot area.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:BoundsGraph:Bounds WidthWidth

Specifies the width of the master object, excluding the label caption and the other
palette in pixels.

                                                    © National Instruments 6603

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6603 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6604 ordinal=6604 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:BoundsGraph:Bounds HeightHeight

       Specifies the height of the master object, excluding the label caption and the other
       palette in pixels.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6604   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6604 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6605 ordinal=6605 -->
## Property and Method Reference

Property and Method Reference

Format:XFormat:X ScaleScale FormatFormat

Sets the format string of the X scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Format:YFormat:Y ScaleScale FormatFormat

Sets the format string of the Y scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6605

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6605 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6606 ordinal=6606 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:EditableScale:Editable

       Allows you to edit the value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:FlippedScale:Flipped

           If TRUE, reverses the position of the minimum and maximum values on the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6606   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6606 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6607 ordinal=6607 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:MappingScale:Mapping ModeMode

Specifies the scale mapping mode.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:VisibleScale:Visible

Shows the scale.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6607

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6607 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6608 ordinal=6608 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:StyleScale:Style

       Specifies the scale style.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:ScaleScale:Scale FitFit

        Fits the scale to the data.


6608   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6608 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6609 ordinal=6609 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:OffsetScale:Offset andand Multiplier:OffsetMultiplier:Offset

Sets the offset, or initial, value for scaling data using (Deltax) xx + xo.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6609

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6609 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6610 ordinal=6610 -->
## Property and Method Reference

Property and Method Reference

   XX Scale:OffsetScale:Offset andand Multiplier:MultiplierMultiplier:Multiplier

       Sets the multiplier, or interval, for scaling data using (Deltax) xx + xo.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Tick:MajorScale:Tick:Major TickTick ColorColor

       Sets the color of the major tick mark.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6610   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6610 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6611 ordinal=6611 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Tick:MinorScale:Tick:Minor TickTick ColorColor

Sets the color of the minor tick mark.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Grid:MajorScale:Grid:Major GridGrid ColorColor

Sets the color of the major grid on the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6611

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6611 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6612 ordinal=6612 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Grid:MinorScale:Grid:Minor GridGrid ColorColor

       Sets the color of the minor grid on the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Range:MinimumScale:Range:Minimum

       Sets the minimum value of the scale.

     Remarks

      The following table lists the characteristics of this property.


6612   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6612 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6613 ordinal=6613 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Range:MaximumScale:Range:Maximum

Sets the maximum value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Range:IncrementScale:Range:Increment

Sets the increment value of the scale.


                                                    © National Instruments 6613

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6613 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6614 ordinal=6614 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Range:MinorScale:Range:Minor IncrementIncrement

       Sets the minor increment value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6614   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6614 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6615 ordinal=6615 -->
## Property and Method Reference

Property and Method Reference

XX Scale:Range:StartScale:Range:Start

Sets the start value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Marker:VisibleScale:Marker:Visible

Indicates whether the tick marker is visible.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6615

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6615 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6616 ordinal=6616 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Marker:FGScale:Marker:FG ColorColor

       Specifies the foreground color of the tick marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Marker:BGScale:Marker:BG ColorColor

       Specifies the background color of the tick marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6616   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6616 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6617 ordinal=6617 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Marker:FontScale:Marker:Font NameName

Specifies the font name of the tick marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Marker:FontScale:Marker:Font SizeSize

Specifies the font size of the tick marker.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6617

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6617 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6618 ordinal=6618 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Marker:FontScale:Marker:Font BoldBold

       Indicates whether the text is bold.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Marker:FontScale:Marker:Font ItalicItalic

       Indicates whether the text is italic.


6618   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6618 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6619 ordinal=6619 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Marker:FontScale:Marker:Font StrikeStrike

Indicates whether the text is in the strikeout font.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6619

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6619 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6620 ordinal=6620 -->
## Property and Method Reference

Property and Method Reference

   XX Scale:Marker:FontScale:Marker:Font UnderlineUnderline

       Indicates whether the text is underlined.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:NameScale:Name Label:VisibleLabel:Visible

       Indicates whether the name label is visible.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6620   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6620 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6621 ordinal=6621 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:NameScale:Name Label:FGLabel:FG ColorColor

Specifies the foreground color of the name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:NameScale:Name Label:BGLabel:BG ColorColor

Specifies the background color of the name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6621

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6621 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6622 ordinal=6622 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:NameScale:Name Label:FontLabel:Font NameName

       Specifies the font name of the name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:NameScale:Name Label:FontLabel:Font SizeSize

       Specifies the font size of the name label.

     Remarks

      The following table lists the characteristics of this property.


6622   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6622 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6623 ordinal=6623 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:NameScale:Name Label:FontLabel:Font BoldBold

Indicates whether the text is bold.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:NameScale:Name Label:FontLabel:Font ItalicItalic

Indicates whether the text is italic.


                                                    © National Instruments 6623

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6623 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6624 ordinal=6624 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:NameScale:Name Label:FontLabel:Font StrikeStrike

       Indicates whether the text is in the strikeout font.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6624   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6624 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6625 ordinal=6625 -->
## Property and Method Reference

Property and Method Reference

XX Scale:NameScale:Name Label:FontLabel:Font UnderlineUnderline

Indicates whether the text is underlined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:NameScale:Name Label:JustificationLabel:Justification

Gets and sets the justification of the text.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6625

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6625 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6626 ordinal=6626 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:NameScale:Name Label:TextLabel:Text

       Displays text in the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:EditableScale:Editable

       Allows you to edit the value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6626   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6626 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6627 ordinal=6627 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:FilppedScale:Filpped

If TRUE, reverses the position of the minimum and maximum values on the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:MappingScale:Mapping ModeMode

Specifies the scale mapping mode.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6627

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6627 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6628 ordinal=6628 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:VisibleScale:Visible

      Shows the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:StyleScale:Style

       Specifies the scale style.


6628   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6628 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6629 ordinal=6629 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:ScaleScale:Scale FitFit

Fits the scale to the data.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6629

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6629 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6630 ordinal=6630 -->
## Property and Method Reference

Property and Method Reference

   YY Scale:OffsetScale:Offset andand Multiplier:OffsetMultiplier:Offset

       Sets the offset, or initial, value for scaling data using (Deltax) xx + xo.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:OffsetScale:Offset andand Multiplier:MultiplierMultiplier:Multiplier

       Sets the multiplier, or interval, for scaling data using (Deltax) xx + xo.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6630   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6630 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6631 ordinal=6631 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Tick:MajorScale:Tick:Major TickTick ColorColor

Sets the color of the major tick mark.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Tick:MinorScale:Tick:Minor TickTick ColorColor

Sets the color of the minor tick mark.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6631

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6631 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6632 ordinal=6632 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Grid:MajorScale:Grid:Major GridGrid ColorColor

       Sets the color of the major grid on the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Grid:MinorScale:Grid:Minor GridGrid ColorColor

       Sets the color of the minor grid on the scale.

     Remarks

      The following table lists the characteristics of this property.


6632   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6632 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6633 ordinal=6633 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Range:IncrementScale:Range:Increment

Sets the increment value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Range:MaximumScale:Range:Maximum

Sets the maximum value of the scale.


                                                    © National Instruments 6633

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6633 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6634 ordinal=6634 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Range:MinimumScale:Range:Minimum

       Sets the minimum value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6634   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6634 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6635 ordinal=6635 -->
## Property and Method Reference

Property and Method Reference

YY Scale:Range:MinorScale:Range:Minor IncrementIncrement

Sets the minor increment value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Range:StartScale:Range:Start

Sets the start value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6635

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6635 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6636 ordinal=6636 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Marker:VisibleScale:Marker:Visible

       Indicates whether the tick marker is visible.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Marker:FGScale:Marker:FG ColorColor

       Specifies the foreground color of the tick marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6636   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6636 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6637 ordinal=6637 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Marker:BGScale:Marker:BG ColorColor

Specifies the background color of the tick marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Marker:FontScale:Marker:Font NameName

Specifies the font name of the tick marker.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6637

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6637 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6638 ordinal=6638 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Marker:FontScale:Marker:Font SizeSize

       Specifies the font size of the tick marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Marker:FontScale:Marker:Font BoldBold

       Indicates whether the text is bold.


6638   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6638 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6639 ordinal=6639 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Marker:FontScale:Marker:Font ItalicItalic

Indicates whether the text is italic.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6639

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6639 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6640 ordinal=6640 -->
## Property and Method Reference

Property and Method Reference

   YY Scale:Marker:FontScale:Marker:Font StrikeStrike

       Indicates whether the text is in the strikeout font.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Marker:FontScale:Marker:Font UnderlineUnderline

       Indicates whether the text is underlined.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6640   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6640 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6641 ordinal=6641 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:NameScale:Name Label:VisibleLabel:Visible

Indicates whether the name label is visible.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:NameScale:Name Label:FGLabel:FG ColorColor

Specifies the foreground color of the name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6641

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6641 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6642 ordinal=6642 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:NameScale:Name Label:BGLabel:BG ColorColor

       Specifies the background color of the name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:NameScale:Name Label:FontLabel:Font NameName

       Specifies the font name of the name label.

     Remarks

      The following table lists the characteristics of this property.


6642   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6642 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6643 ordinal=6643 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:NameScale:Name Label:FontLabel:Font SizeSize

Specifies the font size of the name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:NameScale:Name Label:FontLabel:Font BoldBold

Indicates whether the text is bold.


                                                    © National Instruments 6643

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6643 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6644 ordinal=6644 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:NameScale:Name Label:FontLabel:Font ItalicItalic

       Indicates whether the text is italic.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6644   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6644 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6645 ordinal=6645 -->
## Property and Method Reference

Property and Method Reference

YY Scale:NameScale:Name Label:FontLabel:Font StrikeStrike

Indicates whether the text is in the strikeout font.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:NameScale:Name Label:FontLabel:Font UnderlineUnderline

Indicates whether the text is underlined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6645

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6645 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6646 ordinal=6646 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:NameScale:Name Label:JustificationLabel:Justification

       Gets and sets the justification of the text.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:NameScale:Name Label:TextLabel:Text

       Displays text in the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6646   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6646 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6647 ordinal=6647 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:ActiveCursor:Active CursorCursor

Gets and sets the active cursor and sets properties and methods on the active cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:NameCursor:Name

Displays text that is associated with the cursor in the plot area.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6647

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6647 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6648 ordinal=6648 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:ColorCursor:Color

       Sets the color of the cursor, including its point, arrow, and name.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:StyleCursor:Style

      Draws the symbol at the focal point of the cursor in combination with Point Style.


6648   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6648 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6649 ordinal=6649 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:PointCursor:Point StyleStyle

Draws the symbol at the focal point of the cursor in combination with Style.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6649

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6649 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6650 ordinal=6650 -->
## Property and Method Reference

Property and Method Reference

   Cursor:NameCursor:Name VisibleVisible

           If TRUE, displays the cursor name in the plot area.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:AllowCursor:Allow DragDrag

           If TRUE, allows you to drag the cursor.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6650   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6650 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6651 ordinal=6651 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:ModeCursor:Mode

Specifies the way the cursor snaps to the plots in the plot area.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:PlotCursor:Plot

Specifies the plot associated with the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6651

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6651 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6652 ordinal=6652 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:IndexCursor:Index

       Specifies the array index of the point where the cursor snaps.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:PositionCursor:Position

       Specifies the position of the cursor in terms of XY coordinates.

     Remarks

      The following table lists the characteristics of this property.


6652   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6652 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6653 ordinal=6653 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:XCursor:X ScaleScale

Sets the x-scale of the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:YCursor:Y ScaleScale

Sets the y-scale of the cursor.


                                                    © National Instruments 6653

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6653 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6654 ordinal=6654 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Cursor:WatchCursor:Watch PlotsPlots

       Specifies the array that contains the indexes of the plots that the cursor watches when
       the Watch All Plots property is set to FALSE.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6654   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6654 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6655 ordinal=6655 -->
## Property and Method Reference

Property and Method Reference

Cursor:WatchCursor:Watch AllAll PlotsPlots

If TRUE, sets the cursor to watch all plots in the plot area. If FALSE, sets the cursor to
watch only the plots specified by the Watch Plots property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:PlotCursor:Plot AreaArea

Specifies the plot area associated with the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

                                                    © National Instruments 6655

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6655 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6656 ordinal=6656 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:LabelCursor:Label OffsetOffset

       Sets the coordinates of the label center position relative to the cursor center.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:SelectionCursor:Selection ColorColor

       Sets the color of the cursor row selected in the cursor legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

6656   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6656 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6657 ordinal=6657 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:LineCursor:Line StyleStyle

Specifies the style of the line that displays the active cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:LineCursor:Line WidthWidth

Specifies the width of the line used to display the active cursor.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 6657

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6657 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6658 ordinal=6658 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:VisibleCursor:Visible

      Shows the cursor.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:ActiveSpecific:Active PlotPlot

       Gets or sets the active plot. After you get or set the active plot, you then can set
       properties or invoke methods that affect only the specified plot.

6658   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6658 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6659 ordinal=6659 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:ErrorSpecific:Error BarBar NameName

Shows the name of the plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6659

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6659 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6660 ordinal=6660 -->
## Property and Method Reference

Property and Method Reference

    PlotPlot Specific:ErrorSpecific:Error BarBar LineLine StyleStyle

       Specifies the line style.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:ErrorSpecific:Error BarBar LineLine WidthWidth

       Sets the width of the plot (0-5).

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6660   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6660 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6661 ordinal=6661 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:ErrorSpecific:Error BarBar PointPoint StyleStyle

Sets the point style of the error bar.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:ErrorSpecific:Error BarBar InterpolationInterpolation

Specifies the interpolation of the plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6661

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6661 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6662 ordinal=6662 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:ErrorSpecific:Error BarBar ColorColor

       Sets the color of the plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:ErrorSpecific:Error BarBar PointPoint FillFill ColorColor

       Sets the color of the point and the fill.

     Remarks

      The following table lists the characteristics of this property.


6662   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6662 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6663 ordinal=6663 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:ErrorSpecific:Error BarBar FillFill toto

Sets the baseline of the fill.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:ErrorSpecific:Error BarBar SizeSize

Sets the symbol size for the error bar.


                                                    © National Instruments 6663

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6663 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6664 ordinal=6664 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:MarkerSpecific:Marker LineLine StyleStyle

       Specifies the error marker line style, as shown on the shortcut menu from top-left to
       bottom-right.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6664   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6664 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6665 ordinal=6665 -->
## Property and Method Reference

Property and Method Reference

PlotPlot Specific:MarkerSpecific:Marker LineLine WidthWidth

Sets the width of the error marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:MarkerSpecific:Marker LineLine ColorColor

Sets the color of the error bar line.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6665

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6665 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6666 ordinal=6666 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:ErrorSpecific:Error BarBar ModeMode

       Sets whether the error bar displays on the Y axis only or on both X and Y axes.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   AnnotationAnnotation ListList

       Returns an array of information about all annotations.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6666   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6666 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6667 ordinal=6667 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

2D2D ErrorError BarBar MethodsMethods


 Method            Description

 Export Image       Exports an image of the graph to the clipboard or disk.

ExportExport ImageImage

Exports an image of the graph to the clipboard or disk.

Parameters

 Name                        Data type          Required          Description

 File Type                                           Yes

 Target                                              Yes

 Path                                                Yes

 Hide Grid                                           Yes

 Always Overwrite                                    Yes

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes


                                                    © National Instruments 6667

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6667 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6668 ordinal=6668 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No

    2D2D FeatherFeather

     2D2D FeatherFeather PropertiesProperties


        Property               Description

        Graph:Graph Legend                          Shows the graph legend.          Visible

         Graph:Plot Legend                          Shows the plot legend.          Visible

         Graph:Plot Legend         If TRUE, resizes the plot legend to the width of the longest plot name
        Auto Size                 visible in the legend.

         Graph:Plot Legend                                Sets the number of rows in the plot legend.       Number

        Graph:X Scrollbar                                 Displays the x-axis scroll bar for the graph or chart.          Visible

         Graph:Scale Legend                          Shows the scale legend.          Visible

        Graph:Cursor Legend
                                 Displays the cursor legend.
          Visible

         Graph:Plot FG Color     Specifies the foreground color of the plot area.

         Graph:Plot BG Color     Specifies the background color of the plot area.

                                  Specifies the width of the master object, excluding the label caption and
        Graph:Bounds Width
                               the other palette in pixels.

                                  Specifies the height of the master object, excluding the label caption and
        Graph:Bounds Height
                               the other palette in pixels.

        Format:X Scale Format  Sets the format string of the X scale.

        Format:Y Scale Format  Sets the format string of the Y scale.


6668   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6668 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6669 ordinal=6669 -->
## Property and Method Reference

Property and Method Reference


Property               Description

X Scale:Editable        Allows you to edit the value of the scale.

                                     If TRUE, reverses the position of the minimum and maximum values onX Scale:Flipped                      the scale.

X Scale:Mapping Mode  Specifies the scale mapping mode.

X Scale:Visible        Shows the scale.

X Scale:Style            Specifies the scale style.

X Scale:Scale Fit          Fits the scale to the data.

X Scale:Offset and                       Sets the offset, or initial, value for scaling data using (Deltax) xx + xo.
Multiplier:Offset

X Scale:Offset and                       Sets the multiplier, or interval, for scaling data using (Deltax) xx + xo.Multiplier:Multiplier

X Scale:Tick:Major Tick                       Sets the color of the major tick mark.Color

X Scale:Tick:Minor Tick                       Sets the color of the minor tick mark.Color

X Scale:Grid:Major Grid                       Sets the color of the major grid on the scale.Color

X Scale:Grid:Minor Grid                       Sets the color of the minor grid on the scale.Color

X                       Sets the minimum value of the scale.Scale:Range:Minimum

X
                       Sets the maximum value of the scale.
Scale:Range:Maximum

X
                       Sets the increment value of the scale.
Scale:Range:Increment

X Scale:Range:Minor
                       Sets the minor increment value of the scale.
Increment

X Scale:Range:Start     Sets the start value of the scale.

X Scale:Marker:Visible   Indicates whether the tick marker is visible.

X Scale:Marker:FG
                         Specifies the foreground color of the tick marker.
Color


                                                    © National Instruments 6669

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6669 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6670 ordinal=6670 -->
## Property and Method Reference

Property and Method Reference


        Property               Description

        X Scale:Marker:BG                                  Specifies the background color of the tick marker.         Color

        X Scale:Marker:Font                                  Specifies the font name of the tick marker.      Name

        X Scale:Marker:Font                                  Specifies the font size of the tick marker.         Size

        X Scale:Marker:Font                                  Indicates whether the text is bold.        Bold

        X Scale:Marker:Font                                  Indicates whether the text is italic.            Italic

        X Scale:Marker:Font                                  Indicates whether the text is in the strikeout font.
          Strike

        X Scale:Marker:Font                                  Indicates whether the text is underlined.
         Underline

        X Scale:Name                                  Indicates whether the name label is visible.
          Label:Visible

        X Scale:Name Label:FG
                                  Specifies the foreground color of the name label.         Color

        X Scale:Name Label:BG
                                  Specifies the background color of the name label.         Color

        X Scale:Name
                                  Specifies the font name of the name label.         Label:Font Name

        X Scale:Name                                  Specifies the font size of the name label.
         Label:Font Size

        X Scale:Name
                                  Indicates whether the text is bold.
         Label:Font Bold

        X Scale:Name
                                  Indicates whether the text is italic.
         Label:Font Italic

        X Scale:Name
                                  Indicates whether the text is in the strikeout font.
         Label:Font Strike

        X Scale:Name
                                  Indicates whether the text is underlined.
         Label:Font Underline

        X Scale:Name          Gets and sets the justification of the text.

6670   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6670 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6671 ordinal=6671 -->
## Property and Method Reference

Property and Method Reference


Property               Description

Label:Justification

X Scale:Name                        Displays text in the scale.Label:Text

Y Scale:Editable        Allows you to edit the value of the scale.

                                     If TRUE, reverses the position of the minimum and maximum values onY Scale:Filpped                      the scale.

Y Scale:Mapping Mode  Specifies the scale mapping mode.

Y Scale:Visible        Shows the scale.

Y Scale:Style            Specifies the scale style.

Y Scale:Scale Fit          Fits the scale to the data.

Y Scale:Offset and                       Sets the offset, or initial, value for scaling data using (Deltax) xx + xo.
Multiplier:Offset

Y Scale:Offset and                       Sets the multiplier, or interval, for scaling data using (Deltax) xx + xo.
Multiplier:Multiplier

Y Scale:Tick:Major Tick                       Sets the color of the major tick mark.
Color

Y Scale:Tick:Minor Tick
                       Sets the color of the minor tick mark.Color

Y Scale:Grid:Major Grid
                       Sets the color of the major grid on the scale.Color

Y Scale:Grid:Minor Grid
                       Sets the color of the minor grid on the scale.Color

Y
                       Sets the increment value of the scale.
Scale:Range:Increment

Y
                       Sets the maximum value of the scale.
Scale:Range:Maximum

Y
                       Sets the minimum value of the scale.
Scale:Range:Minimum

Y Scale:Range:Minor
                       Sets the minor increment value of the scale.
Increment

Y Scale:Range:Start     Sets the start value of the scale.


                                                    © National Instruments 6671

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6671 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6672 ordinal=6672 -->
## Property and Method Reference

Property and Method Reference


        Property               Description

        Y Scale:Marker:Visible   Indicates whether the tick marker is visible.

        Y Scale:Marker:FG                                  Specifies the foreground color of the tick marker.         Color

        Y Scale:Marker:BG                                  Specifies the background color of the tick marker.
         Color

        Y Scale:Marker:Font                                  Specifies the font name of the tick marker.      Name

        Y Scale:Marker:Font                                  Specifies the font size of the tick marker.
         Size

        Y Scale:Marker:Font                                  Indicates whether the text is bold.        Bold

        Y Scale:Marker:Font                                  Indicates whether the text is italic.            Italic

        Y Scale:Marker:Font                                  Indicates whether the text is in the strikeout font.          Strike

        Y Scale:Marker:Font                                  Indicates whether the text is underlined.         Underline

        Y Scale:Name                                  Indicates whether the name label is visible.          Label:Visible

        Y Scale:Name Label:FG                                  Specifies the foreground color of the name label.         Color

        Y Scale:Name Label:BG                                  Specifies the background color of the name label.         Color

        Y Scale:Name
                                  Specifies the font name of the name label.
         Label:Font Name

        Y Scale:Name
                                  Specifies the font size of the name label.
         Label:Font Size

        Y Scale:Name
                                  Indicates whether the text is bold.
         Label:Font Bold

        Y Scale:Name
                                  Indicates whether the text is italic.
         Label:Font Italic

        Y Scale:Name
                                  Indicates whether the text is in the strikeout font.
         Label:Font Strike

6672   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6672 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6673 ordinal=6673 -->
## Property and Method Reference

Property and Method Reference


Property               Description

Y Scale:Name                         Indicates whether the text is underlined.Label:Font Underline

Y Scale:Name                      Gets and sets the justification of the text.Label:Justification

Y Scale:Name                        Displays text in the scale.Label:Text

                      Gets and sets the active cursor and sets properties and methods on theCursor:Active Cursor                         active cursor.

Cursor:Name           Displays text that is associated with the cursor in the plot area.

Cursor:Color           Sets the color of the cursor, including its point, arrow, and name.

                    Draws the symbol at the focal point of the cursor in combination withCursor:Style
                       Point Style.

                    Draws the symbol at the focal point of the cursor in combination withCursor:Point Style
                           Style.

Cursor:Name Visible       If TRUE, displays the cursor name in the plot area.

Cursor:Allow Drag          If TRUE, allows you to drag the cursor.

Cursor:Mode            Specifies the way the cursor snaps to the plots in the plot area.

Cursor:Plot              Specifies the plot associated with the cursor.

Cursor:Index            Specifies the array index of the point where the cursor snaps.

Cursor:Position         Specifies the position of the cursor in terms of XY coordinates.

Cursor:X Scale          Sets the x-scale of the cursor.

Cursor:Y Scale          Sets the y-scale of the cursor.

                         Specifies the array that contains the indexes of the plots that the cursor
Cursor:Watch Plots
                     watches when the Watch All Plots property is set to FALSE.

                                     If TRUE, sets the cursor to watch all plots in the plot area. If FALSE, sets the
Cursor:Watch All Plots
                       cursor to watch only the plots specified by the Watch Plots property.

Cursor:Plot Area         Specifies the plot area associated with the cursor.

                       Sets the coordinates of the label center position relative to the cursor
Cursor:Label Offset
                         center.

Cursor:Selection Color  Sets the color of the cursor row selected in the cursor legend.


                                                    © National Instruments 6673

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6673 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6674 ordinal=6674 -->
## Property and Method Reference

Property and Method Reference


        Property               Description

         Cursor:Line Style        Specifies the style of the line that displays the active cursor.

         Cursor:Line Width       Specifies the width of the line used to display the active cursor.

          Cursor:Visible        Shows the cursor.

         Plot Specific:Active     Gets or sets the active plot. After you get or set the active plot, you then
         Plot                 can set properties or invoke methods that affect only the specified plot.

         Plot Specific:Feather                          Shows the name of the plot.      Name

         Plot Specific:Feather                          Shows the color of the plot.
         Color

         Plot Specific:Feather                                  Specifies the line style.         Line Style

         Plot Specific:Feather                                Sets the width of the plot.         Line Width

         Plot Specific:Feather                                Sets the symbol size for the feather.         Size

        Annotation List         Returns an array of information about all annotations.

   Graph:GraphGraph:Graph LegendLegend VisibleVisible

      Shows the graph legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes


6674   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6674 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6675 ordinal=6675 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:PlotGraph:Plot LegendLegend VisibleVisible

Shows the plot legend.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:PlotGraph:Plot LegendLegend AutoAuto SizeSize

If TRUE, resizes the plot legend to the width of the longest plot name visible in the
legend.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 6675

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6675 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6676 ordinal=6676 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:PlotGraph:Plot LegendLegend NumberNumber

       Sets the number of rows in the plot legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:XGraph:X ScrollbarScrollbar VisibleVisible

       Displays the x-axis scroll bar for the graph or chart.


6676   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6676 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6677 ordinal=6677 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:ScaleGraph:Scale LegendLegend VisibleVisible

Shows the scale legend.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6677

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6677 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6678 ordinal=6678 -->
## Property and Method Reference

Property and Method Reference

   Graph:CursorGraph:Cursor LegendLegend VisibleVisible

       Displays the cursor legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:PlotGraph:Plot FGFG ColorColor

       Specifies the foreground color of the plot area.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6678   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6678 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6679 ordinal=6679 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:PlotGraph:Plot BGBG ColorColor

Specifies the background color of the plot area.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:BoundsGraph:Bounds WidthWidth

Specifies the width of the master object, excluding the label caption and the other
palette in pixels.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 6679

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6679 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6680 ordinal=6680 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:BoundsGraph:Bounds HeightHeight

       Specifies the height of the master object, excluding the label caption and the other
       palette in pixels.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Format:XFormat:X ScaleScale FormatFormat

       Sets the format string of the X scale.


6680   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6680 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6681 ordinal=6681 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Format:YFormat:Y ScaleScale FormatFormat

Sets the format string of the Y scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6681

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6681 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6682 ordinal=6682 -->
## Property and Method Reference

Property and Method Reference

   XX Scale:EditableScale:Editable

       Allows you to edit the value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:FlippedScale:Flipped

           If TRUE, reverses the position of the minimum and maximum values on the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6682   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6682 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6683 ordinal=6683 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:MappingScale:Mapping ModeMode

Specifies the scale mapping mode.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:VisibleScale:Visible

Shows the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6683

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6683 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6684 ordinal=6684 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:StyleScale:Style

       Specifies the scale style.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:ScaleScale:Scale FitFit

        Fits the scale to the data.

     Remarks

      The following table lists the characteristics of this property.


6684   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6684 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6685 ordinal=6685 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:OffsetScale:Offset andand Multiplier:OffsetMultiplier:Offset

Sets the offset, or initial, value for scaling data using (Deltax) xx + xo.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:OffsetScale:Offset andand Multiplier:MultiplierMultiplier:Multiplier

Sets the multiplier, or interval, for scaling data using (Deltax) xx + xo.


                                                    © National Instruments 6685

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6685 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6686 ordinal=6686 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Tick:MajorScale:Tick:Major TickTick ColorColor

       Sets the color of the major tick mark.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6686   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6686 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6687 ordinal=6687 -->
## Property and Method Reference

Property and Method Reference

XX Scale:Tick:MinorScale:Tick:Minor TickTick ColorColor

Sets the color of the minor tick mark.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Grid:MajorScale:Grid:Major GridGrid ColorColor

Sets the color of the major grid on the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6687

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6687 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6688 ordinal=6688 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Grid:MinorScale:Grid:Minor GridGrid ColorColor

       Sets the color of the minor grid on the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Range:MinimumScale:Range:Minimum

       Sets the minimum value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6688   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6688 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6689 ordinal=6689 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Range:MaximumScale:Range:Maximum

Sets the maximum value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Range:IncrementScale:Range:Increment

Sets the increment value of the scale.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6689

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6689 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6690 ordinal=6690 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Range:MinorScale:Range:Minor IncrementIncrement

       Sets the minor increment value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Range:StartScale:Range:Start

       Sets the start value of the scale.


6690   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6690 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6691 ordinal=6691 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Marker:VisibleScale:Marker:Visible

Indicates whether the tick marker is visible.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6691

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6691 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6692 ordinal=6692 -->
## Property and Method Reference

Property and Method Reference

   XX Scale:Marker:FGScale:Marker:FG ColorColor

       Specifies the foreground color of the tick marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Marker:BGScale:Marker:BG ColorColor

       Specifies the background color of the tick marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6692   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6692 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6693 ordinal=6693 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Marker:FontScale:Marker:Font NameName

Specifies the font name of the tick marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Marker:FontScale:Marker:Font SizeSize

Specifies the font size of the tick marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6693

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6693 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6694 ordinal=6694 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Marker:FontScale:Marker:Font BoldBold

       Indicates whether the text is bold.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:Marker:FontScale:Marker:Font ItalicItalic

       Indicates whether the text is italic.

     Remarks

      The following table lists the characteristics of this property.


6694   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6694 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6695 ordinal=6695 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Marker:FontScale:Marker:Font StrikeStrike

Indicates whether the text is in the strikeout font.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:Marker:FontScale:Marker:Font UnderlineUnderline

Indicates whether the text is underlined.


                                                    © National Instruments 6695

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6695 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6696 ordinal=6696 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:NameScale:Name Label:VisibleLabel:Visible

       Indicates whether the name label is visible.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6696   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6696 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6697 ordinal=6697 -->
## Property and Method Reference

Property and Method Reference

XX Scale:NameScale:Name Label:FGLabel:FG ColorColor

Specifies the foreground color of the name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:NameScale:Name Label:BGLabel:BG ColorColor

Specifies the background color of the name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6697

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6697 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6698 ordinal=6698 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:NameScale:Name Label:FontLabel:Font NameName

       Specifies the font name of the name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:NameScale:Name Label:FontLabel:Font SizeSize

       Specifies the font size of the name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6698   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6698 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6699 ordinal=6699 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:NameScale:Name Label:FontLabel:Font BoldBold

Indicates whether the text is bold.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:NameScale:Name Label:FontLabel:Font ItalicItalic

Indicates whether the text is italic.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6699

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6699 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6700 ordinal=6700 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:NameScale:Name Label:FontLabel:Font StrikeStrike

       Indicates whether the text is in the strikeout font.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   XX Scale:NameScale:Name Label:FontLabel:Font UnderlineUnderline

       Indicates whether the text is underlined.


6700   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6700 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6701 ordinal=6701 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

XX Scale:NameScale:Name Label:JustificationLabel:Justification

Gets and sets the justification of the text.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6701

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6701 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6702 ordinal=6702 -->
## Property and Method Reference

Property and Method Reference

   XX Scale:NameScale:Name Label:TextLabel:Text

       Displays text in the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:EditableScale:Editable

       Allows you to edit the value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6702   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6702 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6703 ordinal=6703 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:FilppedScale:Filpped

If TRUE, reverses the position of the minimum and maximum values on the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:MappingScale:Mapping ModeMode

Specifies the scale mapping mode.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6703

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6703 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6704 ordinal=6704 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:VisibleScale:Visible

      Shows the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:StyleScale:Style

       Specifies the scale style.

     Remarks

      The following table lists the characteristics of this property.


6704   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6704 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6705 ordinal=6705 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:ScaleScale:Scale FitFit

Fits the scale to the data.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:OffsetScale:Offset andand Multiplier:OffsetMultiplier:Offset

Sets the offset, or initial, value for scaling data using (Deltax) xx + xo.


                                                    © National Instruments 6705

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6705 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6706 ordinal=6706 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:OffsetScale:Offset andand Multiplier:MultiplierMultiplier:Multiplier

       Sets the multiplier, or interval, for scaling data using (Deltax) xx + xo.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6706   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6706 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6707 ordinal=6707 -->
## Property and Method Reference

Property and Method Reference

YY Scale:Tick:MajorScale:Tick:Major TickTick ColorColor

Sets the color of the major tick mark.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Tick:MinorScale:Tick:Minor TickTick ColorColor

Sets the color of the minor tick mark.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6707

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6707 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6708 ordinal=6708 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Grid:MajorScale:Grid:Major GridGrid ColorColor

       Sets the color of the major grid on the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Grid:MinorScale:Grid:Minor GridGrid ColorColor

       Sets the color of the minor grid on the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6708   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6708 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6709 ordinal=6709 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Range:IncrementScale:Range:Increment

Sets the increment value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Range:MaximumScale:Range:Maximum

Sets the maximum value of the scale.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6709

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6709 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6710 ordinal=6710 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Range:MinimumScale:Range:Minimum

       Sets the minimum value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Range:MinorScale:Range:Minor IncrementIncrement

       Sets the minor increment value of the scale.


6710   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6710 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6711 ordinal=6711 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Range:StartScale:Range:Start

Sets the start value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6711

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6711 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6712 ordinal=6712 -->
## Property and Method Reference

Property and Method Reference

   YY Scale:Marker:VisibleScale:Marker:Visible

       Indicates whether the tick marker is visible.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Marker:FGScale:Marker:FG ColorColor

       Specifies the foreground color of the tick marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6712   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6712 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6713 ordinal=6713 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Marker:BGScale:Marker:BG ColorColor

Specifies the background color of the tick marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Marker:FontScale:Marker:Font NameName

Specifies the font name of the tick marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6713

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6713 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6714 ordinal=6714 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Marker:FontScale:Marker:Font SizeSize

       Specifies the font size of the tick marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Marker:FontScale:Marker:Font BoldBold

       Indicates whether the text is bold.

     Remarks

      The following table lists the characteristics of this property.


6714   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6714 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6715 ordinal=6715 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Marker:FontScale:Marker:Font ItalicItalic

Indicates whether the text is italic.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:Marker:FontScale:Marker:Font StrikeStrike

Indicates whether the text is in the strikeout font.


                                                    © National Instruments 6715

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6715 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6716 ordinal=6716 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:Marker:FontScale:Marker:Font UnderlineUnderline

       Indicates whether the text is underlined.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6716   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6716 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6717 ordinal=6717 -->
## Property and Method Reference

Property and Method Reference

YY Scale:NameScale:Name Label:VisibleLabel:Visible

Indicates whether the name label is visible.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:NameScale:Name Label:FGLabel:FG ColorColor

Specifies the foreground color of the name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6717

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6717 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6718 ordinal=6718 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:NameScale:Name Label:BGLabel:BG ColorColor

       Specifies the background color of the name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:NameScale:Name Label:FontLabel:Font NameName

       Specifies the font name of the name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6718   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6718 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6719 ordinal=6719 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:NameScale:Name Label:FontLabel:Font SizeSize

Specifies the font size of the name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:NameScale:Name Label:FontLabel:Font BoldBold

Indicates whether the text is bold.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6719

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6719 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6720 ordinal=6720 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:NameScale:Name Label:FontLabel:Font ItalicItalic

       Indicates whether the text is italic.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:NameScale:Name Label:FontLabel:Font StrikeStrike

       Indicates whether the text is in the strikeout font.


6720   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6720 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6721 ordinal=6721 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

YY Scale:NameScale:Name Label:FontLabel:Font UnderlineUnderline

Indicates whether the text is underlined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6721

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6721 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6722 ordinal=6722 -->
## Property and Method Reference

Property and Method Reference

   YY Scale:NameScale:Name Label:JustificationLabel:Justification

       Gets and sets the justification of the text.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   YY Scale:NameScale:Name Label:TextLabel:Text

       Displays text in the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6722   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6722 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6723 ordinal=6723 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:ActiveCursor:Active CursorCursor

Gets and sets the active cursor and sets properties and methods on the active cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:NameCursor:Name

Displays text that is associated with the cursor in the plot area.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6723

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6723 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6724 ordinal=6724 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:ColorCursor:Color

       Sets the color of the cursor, including its point, arrow, and name.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:StyleCursor:Style

      Draws the symbol at the focal point of the cursor in combination with Point Style.

     Remarks

      The following table lists the characteristics of this property.


6724   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6724 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6725 ordinal=6725 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:PointCursor:Point StyleStyle

Draws the symbol at the focal point of the cursor in combination with Style.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:NameCursor:Name VisibleVisible

If TRUE, displays the cursor name in the plot area.


                                                    © National Instruments 6725

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6725 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6726 ordinal=6726 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:AllowCursor:Allow DragDrag

           If TRUE, allows you to drag the cursor.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6726   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6726 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6727 ordinal=6727 -->
## Property and Method Reference

Property and Method Reference

Cursor:ModeCursor:Mode

Specifies the way the cursor snaps to the plots in the plot area.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:PlotCursor:Plot

Specifies the plot associated with the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6727

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6727 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6728 ordinal=6728 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:IndexCursor:Index

       Specifies the array index of the point where the cursor snaps.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:PositionCursor:Position

       Specifies the position of the cursor in terms of XY coordinates.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6728   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6728 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6729 ordinal=6729 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:XCursor:X ScaleScale

Sets the x-scale of the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:YCursor:Y ScaleScale

Sets the y-scale of the cursor.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6729

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6729 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6730 ordinal=6730 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Cursor:WatchCursor:Watch PlotsPlots

       Specifies the array that contains the indexes of the plots that the cursor watches when
       the Watch All Plots property is set to FALSE.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Cursor:WatchCursor:Watch AllAll PlotsPlots

           If TRUE, sets the cursor to watch all plots in the plot area. If FALSE, sets the cursor to

6730   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6730 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6731 ordinal=6731 -->
## Property and Method Reference

Property and Method Reference

watch only the plots specified by the Watch Plots property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:PlotCursor:Plot AreaArea

Specifies the plot area associated with the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

                                                    © National Instruments 6731

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6731 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6732 ordinal=6732 -->
## Property and Method Reference

Property and Method Reference

    Cursor:LabelCursor:Label OffsetOffset

       Sets the coordinates of the label center position relative to the cursor center.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:SelectionCursor:Selection ColorColor

       Sets the color of the cursor row selected in the cursor legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6732   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6732 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6733 ordinal=6733 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:LineCursor:Line StyleStyle

Specifies the style of the line that displays the active cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursor:LineCursor:Line WidthWidth

Specifies the width of the line used to display the active cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6733

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6733 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6734 ordinal=6734 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursor:VisibleCursor:Visible

      Shows the cursor.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:ActiveSpecific:Active PlotPlot

       Gets or sets the active plot. After you get or set the active plot, you then can set
       properties or invoke methods that affect only the specified plot.

     Remarks

      The following table lists the characteristics of this property.

6734   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6734 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6735 ordinal=6735 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:FeatherSpecific:Feather NameName

Shows the name of the plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:FeatherSpecific:Feather ColorColor

Shows the color of the plot.


                                                    © National Instruments 6735

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6735 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6736 ordinal=6736 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:FeatherSpecific:Feather LineLine StyleStyle

       Specifies the line style.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6736   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6736 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6737 ordinal=6737 -->
## Property and Method Reference

Property and Method Reference

PlotPlot Specific:FeatherSpecific:Feather LineLine WidthWidth

Sets the width of the plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:FeatherSpecific:Feather SizeSize

Sets the symbol size for the feather.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6737

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6737 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6738 ordinal=6738 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   AnnotationAnnotation ListList

       Returns an array of information about all annotations.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     2D2D FeatherFeather MethodsMethods


       Method            Description

         Export Image       Exports an image of the graph to the clipboard or disk.

    ExportExport ImageImage

       Exports an image of the graph to the clipboard or disk.


6738   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6738 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6739 ordinal=6739 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name                        Data type          Required          Description

 File Type                                           Yes

 Target                                              Yes

 Path                                                Yes

 Hide Grid                                           Yes

 Always Overwrite                                    Yes

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes

 Settable when the VI is running                                                       Yes

 Loads the front panel into memory                                                    Yes

 Need to authenticate before use                                         No

 Loads the block diagram into memory                                     No

3D3D GraphsGraphs

This section describes the properties and methods of 3D Graphs

3D3D SurfaceSurface

3D3D SurfaceSurface PropertiesProperties


 Property                    Description

 Graph:Fast Draw            Speeds up the pan, zoom, and rotate operations of the 3D graph.

 Graph:Clip Data             Uses the clip plane to hide the part of the plot that is outside the


                                                    © National Instruments 6739

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6739 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6740 ordinal=6740 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

                                        axes.

        Graph:Background Color      Specifies the background color of the plot.

         Graph:Projection Mode      Changes the projection of the 3D graph.

        Graph:View Direction         Sets the direction for viewing the 3D graph.

        Graph:User Defined          Sets the latitude of the user-defined direction for viewing the 3D
        View:View Latitude           graph.

        Graph:User Defined          Sets the longitude of the user-defined direction for viewing the 3D
        View:View Longitude         graph.

        Graph:User Defined          Sets the distance of the user-defined direction for viewing the 3D
        View:View Distance           graph.

         Graph:Grid Plane:XY Plane                              Shows the 3D graph in the direction of the XY plane.
          Visible

         Graph:Grid Plane:YZ Plane                              Shows the 3D graph in the direction of the YZ plane.
          Visible

         Graph:Grid Plane:XZ Plane                              Shows the 3D graph in the direction of the XZ plane.
          Visible

         Graph:Grid Plane:Grid Anti-
                                  Uses anti-aliasing to show the grid lines.          aliasing

         Graph:Grid Plane:Frame
                                        Specifies the color of the grid frame.         Color

         Light:Enable Lighting        Enables the entire setting for the light.

          Light:Active Light             Sets the specified settings of the light you want to configure.

         Light:Enable Light           Enables specified settings for the light.

          Light:Light Color           Changes the specific light color.

          Light:Light Latitude          Sets the latitude of the specified light towards the target.

          Light:Light Longitude         Sets the longitude of the specified light towards the target.

          Light:Light Distance          Sets the distance of the specified light towards the target.

          Light:Light Attenuation      Changes the attenuation mode of the specified settings for the light.

          Axis:Active Axis               Sets the axis you want to configure.

        Axis:Name Label:Name       Sets the color of the axis name label.


6740   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6740 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6741 ordinal=6741 -->
## Property and Method Reference

Property and Method Reference


Property                    Description

Label Color

Axis:Name Label:Name                             Sets the font size of the axis name label.Label Size

Axis:Name Label:Name                            Configures the text that displays for the axis name label.
Label Text

Axis:Name Label:Name                             Displays the axis name label on one side of the axis.Label Normal Visible

Axis:Name Label:Name                             Displays the axis name label on the opposite side of the axis.
Label Opposite Visible

Axis:Marker:Marker Color     Sets the color of the scale marker.

Axis:Marker:Marker Size       Sets the font size of the scale marker.

Axis:Marker:Marker Normal                             Displays the scale marker on one side of the axis.Visible

Axis:Marker:Marker Opposite                             Displays the scale marker on the opposite side of the axis.Visible

Axis:Range:Range Maximum  Sets the maximum value of the scale.

Axis:Range:Range Minimum   Sets the minimum value of the scale.

                             Adjusts the scale automatically to reflect the data you wire to the 3DAxis:Range:Range Auto Scale                             graph.

Axis:Range:Range Inverted    Inverts the scale range from maximum to minimum.

Axis:Range:Range Logarithm  Shows the scale in the logarithm mapping mode.

Axis:Grid:Grid Major Color     Sets the color of the major axis grid.

Axis:Grid:Grid Major Visible    Displays the major axis grid in the 3D graph.

Axis:Grid:Grid Minor Color     Sets the color of the minor axis grid.

Axis:Grid:Grid Minor Visible    Displays the minor axis grid in the 3D graph.

Axis:Tick:Tick Major Count    Specifies the number of major tick marks that appear on the axis.

Axis:Tick:Tick Major Color     Sets the color of the major tick marks on the axis.

Axis:Tick:Tick Major Visible    Displays the major tick marks on the axis.

Axis:Tick:Tick Minor Count    Specifies the number of minor tick marks that appear on the axis.


                                                    © National Instruments 6741

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6741 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6742 ordinal=6742 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

          Axis:Tick:Tick Minor Color     Sets the color of the minor tick marks on the axis.

          Axis:Tick:Tick Minor Visible    Displays the minor tick marks on the axis.

         Value Pairs:Active Value Pair   Sets the axis to configure its value pairs.

         Value Pairs:Value Pair Label                                        Specifies how value pairs appear on the scale marker.
        Type

         Value Pairs:Value Pair Tick                                      Displays tick marks for each value pair.          Visible

         Value Pairs:Value Pair Grid                                      Displays grid lines for each value pair.
          Visible

                                            Lists the index, name, and value of the value pairs you want to         Value Pairs:Value Pair Array                                       display on the 3D graph.

         Format:Axis X Format String   Sets the formatting for the x-axis.

         Format:Axis Y Format String   Sets the formatting for the y-axis.

         Format:Axis Z Format String   Sets the formatting for the z-axis.

         Cursors:Active Cursor         Sets the cursor you want to configure.

         Cursors:General:Cursor                                   Enables you to move the cursor you configure around the 3D graph.        Enable

         Cursors:General:Cursor                                      Displays the cursor in the 3D graph.          Visible

         Cursors:General:Cursor Lock                                      Sets the style of the cursor lock.         Style

         Cursors:General:Cursor Plot
                                      Sets the cursor to snap to the specified plot.
         ID

         Cursors:General:Cursor X
                                      Sets the position of the cursor on the x-axis.
         Position

         Cursors:General:Cursor Y
                                      Sets the position of the cursor on the y-axis.
         Position

         Cursors:General:Cursor Z
                                      Sets the position of the cursor on the z-axis.
         Position

         Cursors:Point:Cursor Point
                                      Sets the color of the cursor point.
         Color


6742   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6742 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6743 ordinal=6743 -->
## Property and Method Reference

Property and Method Reference


Property                    Description

Cursors:Point:Cursor Point                               Specifies the size of the point on the cursor.Size

Cursors:Point:Cursor Point                               Specifies the symbol style of the point on the cursor.Style

Cursors:Line:Cursor Line                             Sets the color of the cursor line.Color

Cursors:Line:Cursor Line                               Specifies the width of the cursor line.Width

Cursors:Line:Cursor Line                               Specifies the style of the cursor line.Style

Cursors:Plane:Cursor Plane                             Sets the color of the cursor plane.
Color

Cursors:Plane:Cursor Plane   Specifies the level of opacity of the color you apply to the cursor
Opacity                      plane.

Cursors:Plane:Cursor Plane                             Displays the XY cursor plane on the 3D graph.
XY Visible

Cursors:Plane:Cursor Plane
                             Displays the XZ cursor plane on the 3D graph.XZ Visible

Cursors:Plane:Cursor Plane
                             Displays the YZ cursor plane on the 3D graph.YZ Visible

Cursors:Text:Cursor Name    Configures the text of the cursor name.

Cursors:Text:Cursor Text                               Specifies the color of the cursor text.Color

                               Specifies the font size of the cursor text. The text includes the cursor
Cursors:Text:Cursor Text Size
                      name and its position.

Cursors:Text:Cursor Show
                             Displays the cursor position on the 3D graph.
Position

Cursors:Text:Cursor Show
                             Displays the cursor name on the 3D graph.
Name

Cursors:Text:Cursor Text
                               Specifies the color of the cursor text background.
Background Color

Cursors:Text:Cursor Text      Specifies the level of opacity of the color you apply to the cursor text
Background Opacity         background.

                                                    © National Instruments 6743

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6743 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6744 ordinal=6744 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

         Cursors:Cursor List           Displays an array of information about all the cursors.

                                    Gets or sets the active plot. After you get or set the active plot, you
         Plot Specific:Active Plot      then can set properties or invoke methods that affect only the
                                        specified plot.

         Plot Specific:General:Plot                                     Configures the text of the plot name.      Name

         Plot Specific:General:Plot                                        Specifies the level of opacity of the color you apply to the plot.         Opacity

         Plot
         Specific:General:Coordinates  Configures the coordinate system to display the 3D plot.
        System

         Plot
         Specific:Projection:Draw XY   Displays the plot projection on the XY plane.
         Projection

         Plot
         Specific:Projection:Draw YZ   Displays the plot projection on the YZ plane.
         Projection

         Plot
         Specific:Projection:Draw XZ   Displays the plot projection on the XZ plane.
         Projection

         Plot Specific:Surface:Draw
                                      Displays the surface on the 3D graph.         Surface

         Plot Specific:Surface:Draw
                                      Displays the mesh surface on the 3D graph.       Mesh

         Plot Specific:Surface:Draw
                                      Displays the normals of the surface at regular intervals.
        Normal

         Plot Specific:Surface:Surface
                                      Sets the color map for the surface.
         Color Ramp

         Plot Specific:Surface:Surface
                                        Specifies the style of the mesh lines.
         Line Style

         Plot Specific:Surface:Surface
                                        Specifies the width of the mesh lines.
         Line Width

         Plot Specific:Surface:Surface
                                      Sets the color of the mesh lines.
         Line Color

6744   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6744 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6745 ordinal=6745 -->
## Property and Method Reference

Property and Method Reference


 Property                    Description

 Plot Specific:Surface:Surface                           Uses anti-aliasing to show the mesh lines. Line Anti-aliasing

 Plot Specific:Surface:Surface                              Sets the color mode to display the surface. Color Mode

Graph:FastGraph:Fast DrawDraw

Speeds up the pan, zoom, and rotate operations of the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:ClipGraph:Clip DataData

Uses the clip plane to hide the part of the plot that is outside the axes.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6745

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6745 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6746 ordinal=6746 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:BackgroundGraph:Background ColorColor

       Specifies the background color of the plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:ProjectionGraph:Projection ModeMode

      Changes the projection of the 3D graph.


6746   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6746 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6747 ordinal=6747 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:ViewGraph:View DirectionDirection

Sets the direction for viewing the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6747

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6747 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6748 ordinal=6748 -->
## Property and Method Reference

Property and Method Reference

   Graph:UserGraph:User DefinedDefined View:ViewView:View LatitudeLatitude

       Sets the latitude of the user-defined direction for viewing the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:UserGraph:User DefinedDefined View:ViewView:View LongitudeLongitude

       Sets the longitude of the user-defined direction for viewing the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6748   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6748 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6749 ordinal=6749 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:UserGraph:User DefinedDefined View:ViewView:View DistanceDistance

Sets the distance of the user-defined direction for viewing the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:GridGraph:Grid Plane:XYPlane:XY PlanePlane VisibleVisible

Shows the 3D graph in the direction of the XY plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6749

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6749 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6750 ordinal=6750 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:GridGraph:Grid Plane:YZPlane:YZ PlanePlane VisibleVisible

      Shows the 3D graph in the direction of the YZ plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:GridGraph:Grid Plane:XZPlane:XZ PlanePlane VisibleVisible

      Shows the 3D graph in the direction of the XZ plane.

     Remarks

      The following table lists the characteristics of this property.


6750   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6750 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6751 ordinal=6751 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:GridGraph:Grid Plane:GridPlane:Grid Anti-aliasingAnti-aliasing

Uses anti-aliasing to show the grid lines.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:GridGraph:Grid Plane:FramePlane:Frame ColorColor

Specifies the color of the grid frame.


                                                    © National Instruments 6751

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6751 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6752 ordinal=6752 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:EnableLight:Enable LightingLighting

      Enables the entire setting for the light.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6752   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6752 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6753 ordinal=6753 -->
## Property and Method Reference

Property and Method Reference

Light:ActiveLight:Active LightLight

Sets the specified settings of the light you want to configure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:EnableLight:Enable LightLight

Enables specified settings for the light.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6753

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6753 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6754 ordinal=6754 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:LightLight:Light ColorColor

      Changes the specific light color.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:LightLight:Light LatitudeLatitude

       Sets the latitude of the specified light towards the target.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6754   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6754 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6755 ordinal=6755 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:LightLight:Light LongitudeLongitude

Sets the longitude of the specified light towards the target.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:LightLight:Light DistanceDistance

Sets the distance of the specified light towards the target.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6755

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6755 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6756 ordinal=6756 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:LightLight:Light AttenuationAttenuation

      Changes the attenuation mode of the specified settings for the light.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:ActiveAxis:Active AxisAxis

       Sets the axis you want to configure.


6756   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6756 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6757 ordinal=6757 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:NameAxis:Name Label:NameLabel:Name LabelLabel ColorColor

Sets the color of the axis name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6757

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6757 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6758 ordinal=6758 -->
## Property and Method Reference

Property and Method Reference

   Axis:NameAxis:Name Label:NameLabel:Name LabelLabel SizeSize

       Sets the font size of the axis name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:NameAxis:Name Label:NameLabel:Name LabelLabel TextText

       Configures the text that displays for the axis name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6758   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6758 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6759 ordinal=6759 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:NameAxis:Name Label:NameLabel:Name LabelLabel NormalNormal VisibleVisible

Displays the axis name label on one side of the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:NameAxis:Name Label:NameLabel:Name LabelLabel OppositeOpposite
VisibleVisible

Displays the axis name label on the opposite side of the axis.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 6759

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6759 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6760 ordinal=6760 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Marker:MarkerAxis:Marker:Marker ColorColor

       Sets the color of the scale marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Marker:MarkerAxis:Marker:Marker SizeSize

       Sets the font size of the scale marker.


6760   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6760 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6761 ordinal=6761 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Marker:MarkerAxis:Marker:Marker NormalNormal VisibleVisible

Displays the scale marker on one side of the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6761

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6761 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6762 ordinal=6762 -->
## Property and Method Reference

Property and Method Reference

    Axis:Marker:MarkerAxis:Marker:Marker OppositeOpposite VisibleVisible

       Displays the scale marker on the opposite side of the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:Range:RangeAxis:Range:Range MaximumMaximum

       Sets the maximum value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6762   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6762 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6763 ordinal=6763 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Range:RangeAxis:Range:Range MinimumMinimum

Sets the minimum value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Range:RangeAxis:Range:Range AutoAuto ScaleScale

Adjusts the scale automatically to reflect the data you wire to the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6763

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6763 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6764 ordinal=6764 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:Range:RangeAxis:Range:Range InvertedInverted

       Inverts the scale range from maximum to minimum.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:Range:RangeAxis:Range:Range LogarithmLogarithm

      Shows the scale in the logarithm mapping mode.

     Remarks

      The following table lists the characteristics of this property.


6764   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6764 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6765 ordinal=6765 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Grid:GridAxis:Grid:Grid MajorMajor ColorColor

Sets the color of the major axis grid.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Grid:GridAxis:Grid:Grid MajorMajor VisibleVisible

Displays the major axis grid in the 3D graph.


                                                    © National Instruments 6765

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6765 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6766 ordinal=6766 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Grid:GridAxis:Grid:Grid MinorMinor ColorColor

       Sets the color of the minor axis grid.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6766   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6766 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6767 ordinal=6767 -->
## Property and Method Reference

Property and Method Reference

Axis:Grid:GridAxis:Grid:Grid MinorMinor VisibleVisible

Displays the minor axis grid in the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Tick:TickAxis:Tick:Tick MajorMajor CountCount

Specifies the number of major tick marks that appear on the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6767

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6767 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6768 ordinal=6768 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Tick:TickAxis:Tick:Tick MajorMajor ColorColor

       Sets the color of the major tick marks on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Tick:TickAxis:Tick:Tick MajorMajor VisibleVisible

       Displays the major tick marks on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6768   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6768 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6769 ordinal=6769 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Tick:TickAxis:Tick:Tick MinorMinor CountCount

Specifies the number of minor tick marks that appear on the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Tick:TickAxis:Tick:Tick MinorMinor ColorColor

Sets the color of the minor tick marks on the axis.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6769

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6769 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6770 ordinal=6770 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Tick:TickAxis:Tick:Tick MinorMinor VisibleVisible

       Displays the minor tick marks on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   ValueValue Pairs:ActivePairs:Active ValueValue PairPair

       Sets the axis to configure its value pairs.


6770   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6770 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6771 ordinal=6771 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:ValuePairs:Value PairPair LabelLabel TypeType

Specifies how value pairs appear on the scale marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6771

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6771 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6772 ordinal=6772 -->
## Property and Method Reference

Property and Method Reference

   ValueValue Pairs:ValuePairs:Value PairPair TickTick VisibleVisible

       Displays tick marks for each value pair.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   ValueValue Pairs:ValuePairs:Value PairPair GridGrid VisibleVisible

       Displays grid lines for each value pair.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6772   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6772 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6773 ordinal=6773 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:ValuePairs:Value PairPair ArrayArray

Lists the index, name, and value of the value pairs you want to display on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Format:AxisFormat:Axis XX FormatFormat StringString

Sets the formatting for the x-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6773

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6773 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6774 ordinal=6774 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Format:AxisFormat:Axis YY FormatFormat StringString

       Sets the formatting for the y-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Format:AxisFormat:Axis ZZ FormatFormat StringString

       Sets the formatting for the z-axis.

     Remarks

      The following table lists the characteristics of this property.


6774   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6774 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6775 ordinal=6775 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:ActiveCursors:Active CursorCursor

Sets the cursor you want to configure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor EnableEnable

Enables you to move the cursor you configure around the 3D graph.


                                                    © National Instruments 6775

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6775 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6776 ordinal=6776 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor VisibleVisible

       Displays the cursor in the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6776   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6776 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6777 ordinal=6777 -->
## Property and Method Reference

Property and Method Reference

Cursors:General:CursorCursors:General:Cursor LockLock StyleStyle

Sets the style of the cursor lock.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor PlotPlot IDID

Sets the cursor to snap to the specified plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6777

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6777 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6778 ordinal=6778 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor XX PositionPosition

       Sets the position of the cursor on the x-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor YY PositionPosition

       Sets the position of the cursor on the y-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6778   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6778 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6779 ordinal=6779 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor ZZ PositionPosition

Sets the position of the cursor on the z-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Point:CursorCursors:Point:Cursor PointPoint ColorColor

Sets the color of the cursor point.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6779

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6779 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6780 ordinal=6780 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Point:CursorCursors:Point:Cursor PointPoint SizeSize

       Specifies the size of the point on the cursor.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Point:CursorCursors:Point:Cursor PointPoint StyleStyle

       Specifies the symbol style of the point on the cursor.


6780   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6780 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6781 ordinal=6781 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Line:CursorCursors:Line:Cursor LineLine ColorColor

Sets the color of the cursor line.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6781

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6781 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6782 ordinal=6782 -->
## Property and Method Reference

Property and Method Reference

    Cursors:Line:CursorCursors:Line:Cursor LineLine WidthWidth

       Specifies the width of the cursor line.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Line:CursorCursors:Line:Cursor LineLine StyleStyle

       Specifies the style of the cursor line.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6782   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6782 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6783 ordinal=6783 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane ColorColor

Sets the color of the cursor plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane OpacityOpacity

Specifies the level of opacity of the color you apply to the cursor plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6783

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6783 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6784 ordinal=6784 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane XYXY VisibleVisible

       Displays the XY cursor plane on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane XZXZ VisibleVisible

       Displays the XZ cursor plane on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


6784   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6784 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6785 ordinal=6785 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane YZYZ VisibleVisible

Displays the YZ cursor plane on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor NameName

Configures the text of the cursor name.


                                                    © National Instruments 6785

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6785 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6786 ordinal=6786 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor TextText ColorColor

       Specifies the color of the cursor text.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6786   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6786 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6787 ordinal=6787 -->
## Property and Method Reference

Property and Method Reference

Cursors:Text:CursorCursors:Text:Cursor TextText SizeSize

Specifies the font size of the cursor text. The text includes the cursor name and its
position.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor ShowShow PositionPosition

Displays the cursor position on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

                                                    © National Instruments 6787

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6787 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6788 ordinal=6788 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor ShowShow NameName

       Displays the cursor name on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor TextText BackgroundBackground ColorColor

       Specifies the color of the cursor text background.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

6788   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6788 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6789 ordinal=6789 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor TextText BackgroundBackground
OpacityOpacity

Specifies the level of opacity of the color you apply to the cursor text background.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor ListList

Displays an array of information about all the cursors.


                                                    © National Instruments 6789

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6789 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6790 ordinal=6790 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:ActiveSpecific:Active PlotPlot

       Gets or sets the active plot. After you get or set the active plot, you then can set
       properties or invoke methods that affect only the specified plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6790   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6790 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6791 ordinal=6791 -->
## Property and Method Reference

Property and Method Reference

PlotPlot Specific:General:PlotSpecific:General:Plot NameName

Configures the text of the plot name.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:General:PlotSpecific:General:Plot OpacityOpacity

Specifies the level of opacity of the color you apply to the plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6791

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6791 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6792 ordinal=6792 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:General:CoordinatesSpecific:General:Coordinates SystemSystem

       Configures the coordinate system to display the 3D plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Projection:DrawSpecific:Projection:Draw XYXY ProjectionProjection

       Displays the plot projection on the XY plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6792   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6792 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6793 ordinal=6793 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Projection:DrawSpecific:Projection:Draw YZYZ ProjectionProjection

Displays the plot projection on the YZ plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Projection:DrawSpecific:Projection:Draw XZXZ ProjectionProjection

Displays the plot projection on the XZ plane.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6793

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6793 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6794 ordinal=6794 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Surface:DrawSpecific:Surface:Draw SurfaceSurface

       Displays the surface on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Surface:DrawSpecific:Surface:Draw MeshMesh

       Displays the mesh surface on the 3D graph.


6794   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6794 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6795 ordinal=6795 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Surface:DrawSpecific:Surface:Draw NormalNormal

Displays the normals of the surface at regular intervals.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6795

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6795 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6796 ordinal=6796 -->
## Property and Method Reference

Property and Method Reference

    PlotPlot Specific:Surface:SurfaceSpecific:Surface:Surface ColorColor RampRamp

       Sets the color map for the surface.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Surface:SurfaceSpecific:Surface:Surface LineLine StyleStyle

       Specifies the style of the mesh lines.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6796   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6796 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6797 ordinal=6797 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Surface:SurfaceSpecific:Surface:Surface LineLine WidthWidth

Specifies the width of the mesh lines.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Surface:SurfaceSpecific:Surface:Surface LineLine ColorColor

Sets the color of the mesh lines.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6797

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6797 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6798 ordinal=6798 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Surface:SurfaceSpecific:Surface:Surface LineLine Anti-Anti-
    aliasingaliasing

      Uses anti-aliasing to show the mesh lines.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Surface:SurfaceSpecific:Surface:Surface ColorColor ModeMode

       Sets the color mode to display the surface.


6798   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6798 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6799 ordinal=6799 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

3D3D SurfaceSurface MethodsMethods


 Method                    Description

 Clean Data                 Cleans up the input data by removing all the plots.

                            Resets the view direction to the default view.
 Reset to Default View
                          Views are latitude (60), longitude (45), and distance (2).

 Image to Printer           Sends the 3D graph image to the default printer.

 Image to File              Saves the 3D graph image to an image file or the clipboard.

 Get Picture Control Ref      Returns the reference number to the 3D picture control.

CleanClean DataData

Cleans up the input data by removing all the plots.


                                                    © National Instruments 6799

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6799 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6800 ordinal=6800 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


         Available in Run-Time Engine                                                         Yes

         Available in Real-Time Operating System                                              Yes

         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No

   ResetReset toto DefaultDefault ViewView

       Resets the view direction to the default view.

      Views are latitude (60), longitude (45), and distance (2).

     Remarks

      The following table lists the characteristics of this method.


         Available in Run-Time Engine                                                         Yes

         Available in Real-Time Operating System                                              Yes

         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No

   ImageImage toto PrinterPrinter

      Sends the 3D graph image to the default printer.

6800   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6800 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6801 ordinal=6801 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes

 Settable when the VI is running                                                       Yes

 Loads the front panel into memory                                                    Yes

 Need to authenticate before use                                         No

 Loads the block diagram into memory                                     No

ImageImage toto FileFile

Saves the 3D graph image to an image file or the clipboard.

Parameters

       Data Name       Required  Description        type

                          Specifies the format of the file. You can export into one of the following
                         formats:

 File                   (Windows) .emf, .bmp (default), and .eps files              Yes
 Type
                     (macOS) .pict, .bmp (default), and .eps files

                           (Linux) .bmp (default) and .eps files

                          Specifies whether to save the image to the clipboard or to disk. When you
 Target        Yes
                          set Target to File, you must specify a Path.

                      Path to the new image file. LabVIEW ignores this parameter if you set
 Path         Yes
                        Target to Clipboard. When you set Target to File, you must specify a Path.


                                                    © National Instruments 6801

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6801 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6802 ordinal=6802 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


         Available in Run-Time Engine                                                         Yes

         Available in Real-Time Operating System                                              Yes

         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No

   GetGet PicturePicture ControlControl RefRef

       Returns the reference number to the 3D picture control.

     Parameters

      Name              Data type   Required   Description

       3D Picture Control             No        The 3D picture control owned by the graph.

     Remarks

      The following table lists the characteristics of this method.


         Available in Run-Time Engine                                                         Yes

         Available in Real-Time Operating System                                              Yes

         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No


6802   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6802 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6803 ordinal=6803 -->
## Property and Method Reference

Property and Method Reference

3D3D MeshMesh

3D3D MeshMesh PropertiesProperties


 Property                    Description

 Graph:Fast Draw            Speeds up the pan, zoom, and rotate operations of the 3D graph.

                           Uses the clip plane to hide the part of the plot that is outside the Graph:Clip Data                               axes.

 Graph:Background Color      Specifies the background color of the plot.

 Graph:Projection Mode      Changes the projection of the 3D graph.

 Graph:View Direction         Sets the direction for viewing the 3D graph.

 Graph:User Defined          Sets the latitude of the user-defined direction for viewing the 3D
 View:View Latitude           graph.

 Graph:User Defined          Sets the longitude of the user-defined direction for viewing the 3D
 View:View Longitude         graph.

 Graph:User Defined          Sets the distance of the user-defined direction for viewing the 3D
 View:View Distance           graph.

 Graph:Grid Plane:XY Plane                        Shows the 3D graph in the direction of the XY plane. Visible

 Graph:Grid Plane:YZ Plane                        Shows the 3D graph in the direction of the YZ plane. Visible

 Graph:Grid Plane:XZ Plane                        Shows the 3D graph in the direction of the XZ plane. Visible

 Graph:Grid Plane:Grid Anti-
                           Uses anti-aliasing to show the grid lines.
 aliasing

 Graph:Grid Plane:Frame
                                Specifies the color of the grid frame.
 Color

 Light:Enable Lighting        Enables the entire setting for the light.

 Light:Active Light             Sets the specified settings of the light you want to configure.

 Light:Enable Light           Enables specified settings for the light.

 Light:Light Color           Changes the specific light color.

 Light:Light Latitude          Sets the latitude of the specified light towards the target.

                                                    © National Instruments 6803

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6803 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6804 ordinal=6804 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

          Light:Light Longitude         Sets the longitude of the specified light towards the target.

          Light:Light Distance          Sets the distance of the specified light towards the target.

          Light:Light Attenuation      Changes the attenuation mode of the specified settings for the light.

          Axis:Active Axis               Sets the axis you want to configure.

        Axis:Name Label:Name                                      Sets the color of the axis name label.         Label Color

        Axis:Name Label:Name                                      Sets the font size of the axis name label.         Label Size

        Axis:Name Label:Name                                     Configures the text that displays for the axis name label.         Label Text

        Axis:Name Label:Name                                      Displays the axis name label on one side of the axis.
         Label Normal Visible

        Axis:Name Label:Name                                      Displays the axis name label on the opposite side of the axis.
         Label Opposite Visible

         Axis:Marker:Marker Color     Sets the color of the scale marker.

         Axis:Marker:Marker Size       Sets the font size of the scale marker.

         Axis:Marker:Marker Normal
                                      Displays the scale marker on one side of the axis.          Visible

         Axis:Marker:Marker Opposite
                                      Displays the scale marker on the opposite side of the axis.          Visible

         Axis:Range:Range Maximum  Sets the maximum value of the scale.

         Axis:Range:Range Minimum   Sets the minimum value of the scale.

                                      Adjusts the scale automatically to reflect the data you wire to the 3D
         Axis:Range:Range Auto Scale
                                     graph.

         Axis:Range:Range Inverted    Inverts the scale range from maximum to minimum.

         Axis:Range:Range Logarithm  Shows the scale in the logarithm mapping mode.

          Axis:Grid:Grid Major Color     Sets the color of the major axis grid.

          Axis:Grid:Grid Major Visible    Displays the major axis grid in the 3D graph.

          Axis:Grid:Grid Minor Color     Sets the color of the minor axis grid.

          Axis:Grid:Grid Minor Visible    Displays the minor axis grid in the 3D graph.


6804   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6804 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6805 ordinal=6805 -->
## Property and Method Reference

Property and Method Reference


Property                    Description

Axis:Tick:Tick Major Count    Specifies the number of major tick marks that appear on the axis.

Axis:Tick:Tick Major Color     Sets the color of the major tick marks on the axis.

Axis:Tick:Tick Major Visible    Displays the major tick marks on the axis.

Axis:Tick:Tick Minor Count    Specifies the number of minor tick marks that appear on the axis.

Axis:Tick:Tick Minor Color     Sets the color of the minor tick marks on the axis.

Axis:Tick:Tick Minor Visible    Displays the minor tick marks on the axis.

Value Pairs:Active Value Pair   Sets the axis to configure its value pairs.

Value Pairs:Value Pair Label                               Specifies how value pairs appear on the scale marker.
Type

Value Pairs:Value Pair Tick                             Displays tick marks for each value pair.Visible

Value Pairs:Value Pair Grid                             Displays grid lines for each value pair.Visible

                                  Lists the index, name, and value of the value pairs you want toValue Pairs:Value Pair Array                              display on the 3D graph.

Format:Axis X Format String   Sets the formatting for the x-axis.

Format:Axis Y Format String   Sets the formatting for the y-axis.

Format:Axis Z Format String   Sets the formatting for the z-axis.

Cursors:Active Cursor         Sets the cursor you want to configure.

Cursors:General:Cursor                           Enables you to move the cursor you configure around the 3D graph.
Enable

Cursors:General:Cursor
                             Displays the cursor in the 3D graph.
Visible

Cursors:General:Cursor Lock
                             Sets the style of the cursor lock.
Style

Cursors:General:Cursor Plot
                             Sets the cursor to snap to the specified plot.
ID

Cursors:General:Cursor X
                             Sets the position of the cursor on the x-axis.
Position

Cursors:General:Cursor Y
                             Sets the position of the cursor on the y-axis.
Position

                                                    © National Instruments 6805

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6805 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6806 ordinal=6806 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

         Cursors:General:Cursor Z                                      Sets the position of the cursor on the z-axis.         Position

         Cursors:Point:Cursor Point                                      Sets the color of the cursor point.         Color

         Cursors:Point:Cursor Point                                        Specifies the size of the point on the cursor.         Size

         Cursors:Point:Cursor Point                                        Specifies the symbol style of the point on the cursor.         Style

         Cursors:Line:Cursor Line                                      Sets the color of the cursor line.         Color

         Cursors:Line:Cursor Line                                        Specifies the width of the cursor line.
        Width

         Cursors:Line:Cursor Line                                        Specifies the style of the cursor line.
         Style

         Cursors:Plane:Cursor Plane                                      Sets the color of the cursor plane.
         Color

         Cursors:Plane:Cursor Plane   Specifies the level of opacity of the color you apply to the cursor
         Opacity                      plane.

         Cursors:Plane:Cursor Plane
                                      Displays the XY cursor plane on the 3D graph.        XY Visible

         Cursors:Plane:Cursor Plane
                                      Displays the XZ cursor plane on the 3D graph.       XZ Visible

         Cursors:Plane:Cursor Plane                                      Displays the YZ cursor plane on the 3D graph.
        YZ Visible

         Cursors:Text:Cursor Name    Configures the text of the cursor name.

         Cursors:Text:Cursor Text
                                        Specifies the color of the cursor text.
         Color

                                        Specifies the font size of the cursor text. The text includes the cursor
         Cursors:Text:Cursor Text Size
                            name and its position.

         Cursors:Text:Cursor Show
                                      Displays the cursor position on the 3D graph.
         Position

         Cursors:Text:Cursor Show
                                      Displays the cursor name on the 3D graph.
      Name

6806   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6806 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6807 ordinal=6807 -->
## Property and Method Reference

Property and Method Reference


Property                    Description

Cursors:Text:Cursor Text                               Specifies the color of the cursor text background.Background Color

Cursors:Text:Cursor Text      Specifies the level of opacity of the color you apply to the cursor text
Background Opacity         background.

Cursors:Cursor List           Displays an array of information about all the cursors.

                            Gets or sets the active plot. After you get or set the active plot, you
Plot Specific:Active Plot      then can set properties or invoke methods that affect only the
                               specified plot.

Plot Specific:General:Plot                            Configures the text of the plot name.Name

Plot Specific:General:Plot                               Specifies the level of opacity of the color you apply to the plot.
Opacity

Plot
Specific:General:Coordinates  Configures the coordinate system to display the 3D plot.
System

Plot
Specific:Projection:Draw XY   Displays the plot projection on the XY plane.
Projection

Plot
Specific:Projection:Draw YZ   Displays the plot projection on the YZ plane.
Projection

Plot
Specific:Projection:Draw XZ   Displays the plot projection on the XZ plane.
Projection

Plot Specific:Mesh:Fill Color   Sets the fill color of the mesh.

Plot Specific:Mesh:Mesh Line
                               Specifies the style of the mesh lines.
Style

Plot Specific:Mesh:Mesh Line
                               Specifies the width of the mesh lines.
Width

Plot Specific:Mesh:Mesh
                             Sets the color map for the mesh lines.
Color Ramp

Plot Specific:Mesh:Mesh Line
                          Uses anti-aliasing to show the mesh lines.
Anti-aliasing


                                                    © National Instruments 6807

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6807 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6808 ordinal=6808 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

         Plot Specific:Mesh:Mesh                                      Sets the display mode to show a different mesh.       Mode

    Graph:FastGraph:Fast DrawDraw

      Speeds up the pan, zoom, and rotate operations of the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:ClipGraph:Clip DataData

      Uses the clip plane to hide the part of the plot that is outside the axes.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


6808   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6808 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6809 ordinal=6809 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:BackgroundGraph:Background ColorColor

Specifies the background color of the plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:ProjectionGraph:Projection ModeMode

Changes the projection of the 3D graph.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 6809

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6809 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6810 ordinal=6810 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:ViewGraph:View DirectionDirection

       Sets the direction for viewing the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:UserGraph:User DefinedDefined View:ViewView:View LatitudeLatitude

       Sets the latitude of the user-defined direction for viewing the 3D graph.


6810   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6810 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6811 ordinal=6811 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:UserGraph:User DefinedDefined View:ViewView:View LongitudeLongitude

Sets the longitude of the user-defined direction for viewing the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6811

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6811 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6812 ordinal=6812 -->
## Property and Method Reference

Property and Method Reference

   Graph:UserGraph:User DefinedDefined View:ViewView:View DistanceDistance

       Sets the distance of the user-defined direction for viewing the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:GridGraph:Grid Plane:XYPlane:XY PlanePlane VisibleVisible

      Shows the 3D graph in the direction of the XY plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6812   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6812 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6813 ordinal=6813 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:GridGraph:Grid Plane:YZPlane:YZ PlanePlane VisibleVisible

Shows the 3D graph in the direction of the YZ plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:GridGraph:Grid Plane:XZPlane:XZ PlanePlane VisibleVisible

Shows the 3D graph in the direction of the XZ plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6813

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6813 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6814 ordinal=6814 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:GridGraph:Grid Plane:GridPlane:Grid Anti-aliasingAnti-aliasing

      Uses anti-aliasing to show the grid lines.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:GridGraph:Grid Plane:FramePlane:Frame ColorColor

       Specifies the color of the grid frame.

     Remarks

      The following table lists the characteristics of this property.


6814   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6814 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6815 ordinal=6815 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:EnableLight:Enable LightingLighting

Enables the entire setting for the light.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:ActiveLight:Active LightLight

Sets the specified settings of the light you want to configure.


                                                    © National Instruments 6815

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6815 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6816 ordinal=6816 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:EnableLight:Enable LightLight

      Enables specified settings for the light.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6816   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6816 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6817 ordinal=6817 -->
## Property and Method Reference

Property and Method Reference

Light:LightLight:Light ColorColor

Changes the specific light color.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:LightLight:Light LatitudeLatitude

Sets the latitude of the specified light towards the target.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6817

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6817 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6818 ordinal=6818 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:LightLight:Light LongitudeLongitude

       Sets the longitude of the specified light towards the target.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:LightLight:Light DistanceDistance

       Sets the distance of the specified light towards the target.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6818   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6818 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6819 ordinal=6819 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:LightLight:Light AttenuationAttenuation

Changes the attenuation mode of the specified settings for the light.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:ActiveAxis:Active AxisAxis

Sets the axis you want to configure.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6819

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6819 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6820 ordinal=6820 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:NameAxis:Name Label:NameLabel:Name LabelLabel ColorColor

       Sets the color of the axis name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:NameAxis:Name Label:NameLabel:Name LabelLabel SizeSize

       Sets the font size of the axis name label.


6820   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6820 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6821 ordinal=6821 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:NameAxis:Name Label:NameLabel:Name LabelLabel TextText

Configures the text that displays for the axis name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6821

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6821 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6822 ordinal=6822 -->
## Property and Method Reference

Property and Method Reference

   Axis:NameAxis:Name Label:NameLabel:Name LabelLabel NormalNormal VisibleVisible

       Displays the axis name label on one side of the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:NameAxis:Name Label:NameLabel:Name LabelLabel OppositeOpposite
    VisibleVisible

       Displays the axis name label on the opposite side of the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes


6822   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6822 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6823 ordinal=6823 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Marker:MarkerAxis:Marker:Marker ColorColor

Sets the color of the scale marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Marker:MarkerAxis:Marker:Marker SizeSize

Sets the font size of the scale marker.

Remarks

The following table lists the characteristics of this property.


 Data type

                                                    © National Instruments 6823

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6823 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6824 ordinal=6824 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Marker:MarkerAxis:Marker:Marker NormalNormal VisibleVisible

       Displays the scale marker on one side of the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Marker:MarkerAxis:Marker:Marker OppositeOpposite VisibleVisible

       Displays the scale marker on the opposite side of the axis.


6824   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6824 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6825 ordinal=6825 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Range:RangeAxis:Range:Range MaximumMaximum

Sets the maximum value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6825

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6825 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6826 ordinal=6826 -->
## Property and Method Reference

Property and Method Reference

   Axis:Range:RangeAxis:Range:Range MinimumMinimum

       Sets the minimum value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:Range:RangeAxis:Range:Range AutoAuto ScaleScale

       Adjusts the scale automatically to reflect the data you wire to the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6826   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6826 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6827 ordinal=6827 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Range:RangeAxis:Range:Range InvertedInverted

Inverts the scale range from maximum to minimum.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Range:RangeAxis:Range:Range LogarithmLogarithm

Shows the scale in the logarithm mapping mode.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6827

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6827 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6828 ordinal=6828 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Grid:GridAxis:Grid:Grid MajorMajor ColorColor

       Sets the color of the major axis grid.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Grid:GridAxis:Grid:Grid MajorMajor VisibleVisible

       Displays the major axis grid in the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


6828   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6828 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6829 ordinal=6829 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Grid:GridAxis:Grid:Grid MinorMinor ColorColor

Sets the color of the minor axis grid.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Grid:GridAxis:Grid:Grid MinorMinor VisibleVisible

Displays the minor axis grid in the 3D graph.


                                                    © National Instruments 6829

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6829 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6830 ordinal=6830 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Tick:TickAxis:Tick:Tick MajorMajor CountCount

       Specifies the number of major tick marks that appear on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6830   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6830 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6831 ordinal=6831 -->
## Property and Method Reference

Property and Method Reference

Axis:Tick:TickAxis:Tick:Tick MajorMajor ColorColor

Sets the color of the major tick marks on the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Tick:TickAxis:Tick:Tick MajorMajor VisibleVisible

Displays the major tick marks on the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6831

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6831 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6832 ordinal=6832 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Tick:TickAxis:Tick:Tick MinorMinor CountCount

       Specifies the number of minor tick marks that appear on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Tick:TickAxis:Tick:Tick MinorMinor ColorColor

       Sets the color of the minor tick marks on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6832   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6832 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6833 ordinal=6833 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Tick:TickAxis:Tick:Tick MinorMinor VisibleVisible

Displays the minor tick marks on the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:ActivePairs:Active ValueValue PairPair

Sets the axis to configure its value pairs.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6833

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6833 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6834 ordinal=6834 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   ValueValue Pairs:ValuePairs:Value PairPair LabelLabel TypeType

       Specifies how value pairs appear on the scale marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   ValueValue Pairs:ValuePairs:Value PairPair TickTick VisibleVisible

       Displays tick marks for each value pair.


6834   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6834 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6835 ordinal=6835 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:ValuePairs:Value PairPair GridGrid VisibleVisible

Displays grid lines for each value pair.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6835

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6835 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6836 ordinal=6836 -->
## Property and Method Reference

Property and Method Reference

   ValueValue Pairs:ValuePairs:Value PairPair ArrayArray

        Lists the index, name, and value of the value pairs you want to display on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Format:AxisFormat:Axis XX FormatFormat StringString

       Sets the formatting for the x-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6836   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6836 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6837 ordinal=6837 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Format:AxisFormat:Axis YY FormatFormat StringString

Sets the formatting for the y-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Format:AxisFormat:Axis ZZ FormatFormat StringString

Sets the formatting for the z-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6837

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6837 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6838 ordinal=6838 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:ActiveCursors:Active CursorCursor

       Sets the cursor you want to configure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor EnableEnable

      Enables you to move the cursor you configure around the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


6838   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6838 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6839 ordinal=6839 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor VisibleVisible

Displays the cursor in the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor LockLock StyleStyle

Sets the style of the cursor lock.


                                                    © National Instruments 6839

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6839 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6840 ordinal=6840 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor PlotPlot IDID

       Sets the cursor to snap to the specified plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6840   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6840 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6841 ordinal=6841 -->
## Property and Method Reference

Property and Method Reference

Cursors:General:CursorCursors:General:Cursor XX PositionPosition

Sets the position of the cursor on the x-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor YY PositionPosition

Sets the position of the cursor on the y-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6841

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6841 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6842 ordinal=6842 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor ZZ PositionPosition

       Sets the position of the cursor on the z-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Point:CursorCursors:Point:Cursor PointPoint ColorColor

       Sets the color of the cursor point.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6842   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6842 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6843 ordinal=6843 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Point:CursorCursors:Point:Cursor PointPoint SizeSize

Specifies the size of the point on the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Point:CursorCursors:Point:Cursor PointPoint StyleStyle

Specifies the symbol style of the point on the cursor.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6843

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6843 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6844 ordinal=6844 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Line:CursorCursors:Line:Cursor LineLine ColorColor

       Sets the color of the cursor line.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Line:CursorCursors:Line:Cursor LineLine WidthWidth

       Specifies the width of the cursor line.


6844   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6844 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6845 ordinal=6845 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Line:CursorCursors:Line:Cursor LineLine StyleStyle

Specifies the style of the cursor line.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6845

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6845 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6846 ordinal=6846 -->
## Property and Method Reference

Property and Method Reference

    Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane ColorColor

       Sets the color of the cursor plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane OpacityOpacity

       Specifies the level of opacity of the color you apply to the cursor plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6846   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6846 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6847 ordinal=6847 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane XYXY VisibleVisible

Displays the XY cursor plane on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane XZXZ VisibleVisible

Displays the XZ cursor plane on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6847

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6847 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6848 ordinal=6848 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane YZYZ VisibleVisible

       Displays the YZ cursor plane on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor NameName

       Configures the text of the cursor name.

     Remarks

      The following table lists the characteristics of this property.


6848   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6848 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6849 ordinal=6849 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor TextText ColorColor

Specifies the color of the cursor text.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor TextText SizeSize

Specifies the font size of the cursor text. The text includes the cursor name and its
position.

                                                    © National Instruments 6849

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6849 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6850 ordinal=6850 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor ShowShow PositionPosition

       Displays the cursor position on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6850   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6850 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6851 ordinal=6851 -->
## Property and Method Reference

Property and Method Reference

Cursors:Text:CursorCursors:Text:Cursor ShowShow NameName

Displays the cursor name on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor TextText BackgroundBackground ColorColor

Specifies the color of the cursor text background.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6851

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6851 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6852 ordinal=6852 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor TextText BackgroundBackground
   OpacityOpacity

       Specifies the level of opacity of the color you apply to the cursor text background.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:CursorCursors:Cursor ListList

       Displays an array of information about all the cursors.

     Remarks

      The following table lists the characteristics of this property.


        Data type


6852   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6852 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6853 ordinal=6853 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:ActiveSpecific:Active PlotPlot

Gets or sets the active plot. After you get or set the active plot, you then can set
properties or invoke methods that affect only the specified plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:General:PlotSpecific:General:Plot NameName

Configures the text of the plot name.


                                                    © National Instruments 6853

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6853 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6854 ordinal=6854 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:General:PlotSpecific:General:Plot OpacityOpacity

       Specifies the level of opacity of the color you apply to the plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6854   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6854 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6855 ordinal=6855 -->
## Property and Method Reference

Property and Method Reference

PlotPlot Specific:General:CoordinatesSpecific:General:Coordinates SystemSystem

Configures the coordinate system to display the 3D plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Projection:DrawSpecific:Projection:Draw XYXY ProjectionProjection

Displays the plot projection on the XY plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6855

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6855 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6856 ordinal=6856 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Projection:DrawSpecific:Projection:Draw YZYZ ProjectionProjection

       Displays the plot projection on the YZ plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Projection:DrawSpecific:Projection:Draw XZXZ ProjectionProjection

       Displays the plot projection on the XZ plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6856   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6856 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6857 ordinal=6857 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Mesh:FillSpecific:Mesh:Fill ColorColor

Sets the fill color of the mesh.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Mesh:MeshSpecific:Mesh:Mesh LineLine StyleStyle

Specifies the style of the mesh lines.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6857

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6857 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6858 ordinal=6858 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Mesh:MeshSpecific:Mesh:Mesh LineLine WidthWidth

       Specifies the width of the mesh lines.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Mesh:MeshSpecific:Mesh:Mesh ColorColor RampRamp

       Sets the color map for the mesh lines.


6858   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6858 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6859 ordinal=6859 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Mesh:MeshSpecific:Mesh:Mesh LineLine Anti-aliasingAnti-aliasing

Uses anti-aliasing to show the mesh lines.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6859

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6859 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6860 ordinal=6860 -->
## Property and Method Reference

Property and Method Reference

    PlotPlot Specific:Mesh:MeshSpecific:Mesh:Mesh ModeMode

       Sets the display mode to show a different mesh.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     3D3D MeshMesh MethodsMethods


       Method                    Description

        Clean Data                 Cleans up the input data by removing all the plots.

                                    Resets the view direction to the default view.
         Reset to Default View
                                 Views are latitude (60), longitude (45), and distance (2).

        Image to Printer           Sends the 3D graph image to the default printer.

        Image to File              Saves the 3D graph image to an image file or the clipboard.

        Get Picture Control Ref      Returns the reference number to the 3D picture control.


6860   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6860 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6861 ordinal=6861 -->
## Property and Method Reference

Property and Method Reference

CleanClean DataData

Cleans up the input data by removing all the plots.

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes

 Settable when the VI is running                                                       Yes

 Loads the front panel into memory                                                    Yes

 Need to authenticate before use                                         No

 Loads the block diagram into memory                                     No

ResetReset toto DefaultDefault ViewView

Resets the view direction to the default view.

Views are latitude (60), longitude (45), and distance (2).

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes

 Settable when the VI is running                                                       Yes

 Loads the front panel into memory                                                    Yes

 Need to authenticate before use                                         No

 Loads the block diagram into memory                                     No


                                                    © National Instruments 6861

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6861 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6862 ordinal=6862 -->
## Property and Method Reference

Property and Method Reference

   ImageImage toto PrinterPrinter

      Sends the 3D graph image to the default printer.

     Remarks

      The following table lists the characteristics of this method.


         Available in Run-Time Engine                                                         Yes

         Available in Real-Time Operating System                                              Yes

         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No

   ImageImage toto FileFile

      Saves the 3D graph image to an image file or the clipboard.

     Parameters

               Data      Name       Required  Description
               type

                                   Specifies the format of the file. You can export into one of the following
                                 formats:

           File                   (Windows) .emf, .bmp (default), and .eps files                      Yes
        Type
                            (macOS) .pict, .bmp (default), and .eps files

                                   (Linux) .bmp (default) and .eps files

         Target        Yes        Specifies whether to save the image to the clipboard or to disk. When you


6862   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6862 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6863 ordinal=6863 -->
## Property and Method Reference

Property and Method Reference


       Data Name       Required  Description
        type

                          set Target to File, you must specify a Path.

                      Path to the new image file. LabVIEW ignores this parameter if you set Path         Yes                        Target to Clipboard. When you set Target to File, you must specify a Path.

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes

 Settable when the VI is running                                                       Yes

 Loads the front panel into memory                                                    Yes

 Need to authenticate before use                                         No

 Loads the block diagram into memory                                     No

GetGet PicturePicture ControlControl RefRef

Returns the reference number to the 3D picture control.

Parameters

 Name              Data type   Required   Description

 3D Picture Control             No        The 3D picture control owned by the graph.

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes

                                                    © National Instruments 6863

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6863 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6864 ordinal=6864 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No

    3D3D WaterfallWaterfall

     3D3D WaterfallWaterfall PropertiesProperties


        Property                    Description

         Graph:Fast Draw            Speeds up the pan, zoom, and rotate operations of the 3D graph.

                                  Uses the clip plane to hide the part of the plot that is outside the         Graph:Clip Data
                                        axes.

        Graph:Background Color      Specifies the background color of the plot.

         Graph:Projection Mode      Changes the projection of the 3D graph.

        Graph:View Direction         Sets the direction for viewing the 3D graph.

        Graph:User Defined          Sets the latitude of the user-defined direction for viewing the 3D
        View:View Latitude           graph.

        Graph:User Defined          Sets the longitude of the user-defined direction for viewing the 3D
        View:View Longitude         graph.

        Graph:User Defined          Sets the distance of the user-defined direction for viewing the 3D
        View:View Distance           graph.

         Graph:Grid Plane:XY Plane
                              Shows the 3D graph in the direction of the XY plane.
          Visible

         Graph:Grid Plane:YZ Plane
                              Shows the 3D graph in the direction of the YZ plane.
          Visible

         Graph:Grid Plane:XZ Plane
                              Shows the 3D graph in the direction of the XZ plane.
          Visible

         Graph:Grid Plane:Grid Anti-
                                  Uses anti-aliasing to show the grid lines.
          aliasing

         Graph:Grid Plane:Frame
                                        Specifies the color of the grid frame.
         Color


6864   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6864 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6865 ordinal=6865 -->
## Property and Method Reference

Property and Method Reference


Property                    Description

Light:Enable Lighting        Enables the entire setting for the light.

Light:Active Light             Sets the specified settings of the light you want to configure.

Light:Enable Light           Enables specified settings for the light.

Light:Light Color           Changes the specific light color.

Light:Light Latitude          Sets the latitude of the specified light towards the target.

Light:Light Longitude         Sets the longitude of the specified light towards the target.

Light:Light Distance          Sets the distance of the specified light towards the target.

Light:Light Attenuation      Changes the attenuation mode of the specified settings for the light.

Axis:Active Axis               Sets the axis you want to configure.

Axis:Name Label:Name                             Sets the color of the axis name label.Label Color

Axis:Name Label:Name                             Sets the font size of the axis name label.Label Size

Axis:Name Label:Name                            Configures the text that displays for the axis name label.Label Text

Axis:Name Label:Name                             Displays the axis name label on one side of the axis.Label Normal Visible

Axis:Name Label:Name                             Displays the axis name label on the opposite side of the axis.Label Opposite Visible

Axis:Marker:Marker Color     Sets the color of the scale marker.

Axis:Marker:Marker Size       Sets the font size of the scale marker.

Axis:Marker:Marker Normal
                             Displays the scale marker on one side of the axis.
Visible

Axis:Marker:Marker Opposite
                             Displays the scale marker on the opposite side of the axis.
Visible

Axis:Range:Range Maximum  Sets the maximum value of the scale.

Axis:Range:Range Minimum   Sets the minimum value of the scale.

                             Adjusts the scale automatically to reflect the data you wire to the 3D
Axis:Range:Range Auto Scale
                             graph.

Axis:Range:Range Inverted    Inverts the scale range from maximum to minimum.


                                                    © National Instruments 6865

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6865 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6866 ordinal=6866 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

         Axis:Range:Range Logarithm  Shows the scale in the logarithm mapping mode.

          Axis:Grid:Grid Major Color     Sets the color of the major axis grid.

          Axis:Grid:Grid Major Visible    Displays the major axis grid in the 3D graph.

          Axis:Grid:Grid Minor Color     Sets the color of the minor axis grid.

          Axis:Grid:Grid Minor Visible    Displays the minor axis grid in the 3D graph.

          Axis:Tick:Tick Major Count    Specifies the number of major tick marks that appear on the axis.

          Axis:Tick:Tick Major Color     Sets the color of the major tick marks on the axis.

          Axis:Tick:Tick Major Visible    Displays the major tick marks on the axis.

          Axis:Tick:Tick Minor Count    Specifies the number of minor tick marks that appear on the axis.

          Axis:Tick:Tick Minor Color     Sets the color of the minor tick marks on the axis.

          Axis:Tick:Tick Minor Visible    Displays the minor tick marks on the axis.

         Value Pairs:Active Value Pair   Sets the axis to configure its value pairs.

         Value Pairs:Value Pair Label                                        Specifies how value pairs appear on the scale marker.
        Type

         Value Pairs:Value Pair Tick                                      Displays tick marks for each value pair.
          Visible

         Value Pairs:Value Pair Grid
                                      Displays grid lines for each value pair.          Visible

                                            Lists the index, name, and value of the value pairs you want to
         Value Pairs:Value Pair Array                                       display on the 3D graph.

         Format:Axis X Format String   Sets the formatting for the x-axis.

         Format:Axis Y Format String   Sets the formatting for the y-axis.

         Format:Axis Z Format String   Sets the formatting for the z-axis.

         Cursors:Active Cursor         Sets the cursor you want to configure.

         Cursors:General:Cursor
                                   Enables you to move the cursor you configure around the 3D graph.
        Enable

         Cursors:General:Cursor
                                      Displays the cursor in the 3D graph.
          Visible

         Cursors:General:Cursor Lock  Sets the style of the cursor lock.


6866   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6866 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6867 ordinal=6867 -->
## Property and Method Reference

Property and Method Reference


Property                    Description

Style

Cursors:General:Cursor Plot                             Sets the cursor to snap to the specified plot.ID

Cursors:General:Cursor X                             Sets the position of the cursor on the x-axis.
Position

Cursors:General:Cursor Y                             Sets the position of the cursor on the y-axis.Position

Cursors:General:Cursor Z                             Sets the position of the cursor on the z-axis.
Position

Cursors:Point:Cursor Point                             Sets the color of the cursor point.Color

Cursors:Point:Cursor Point                               Specifies the size of the point on the cursor.Size

Cursors:Point:Cursor Point                               Specifies the symbol style of the point on the cursor.Style

Cursors:Line:Cursor Line                             Sets the color of the cursor line.Color

Cursors:Line:Cursor Line                               Specifies the width of the cursor line.Width

Cursors:Line:Cursor Line                               Specifies the style of the cursor line.Style

Cursors:Plane:Cursor Plane                             Sets the color of the cursor plane.Color

Cursors:Plane:Cursor Plane   Specifies the level of opacity of the color you apply to the cursor
Opacity                      plane.

Cursors:Plane:Cursor Plane
                             Displays the XY cursor plane on the 3D graph.
XY Visible

Cursors:Plane:Cursor Plane
                             Displays the XZ cursor plane on the 3D graph.
XZ Visible

Cursors:Plane:Cursor Plane
                             Displays the YZ cursor plane on the 3D graph.
YZ Visible

Cursors:Text:Cursor Name    Configures the text of the cursor name.


                                                    © National Instruments 6867

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6867 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6868 ordinal=6868 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

         Cursors:Text:Cursor Text                                        Specifies the color of the cursor text.         Color

                                        Specifies the font size of the cursor text. The text includes the cursor         Cursors:Text:Cursor Text Size                            name and its position.

         Cursors:Text:Cursor Show                                      Displays the cursor position on the 3D graph.         Position

         Cursors:Text:Cursor Show                                      Displays the cursor name on the 3D graph.      Name

         Cursors:Text:Cursor Text                                        Specifies the color of the cursor text background.        Background Color

         Cursors:Text:Cursor Text      Specifies the level of opacity of the color you apply to the cursor text
        Background Opacity         background.

         Cursors:Cursor List           Displays an array of information about all the cursors.

                                    Gets or sets the active plot. After you get or set the active plot, you
         Plot Specific:Active Plot      then can set properties or invoke methods that affect only the
                                        specified plot.

         Plot Specific:General:Plot
                                     Configures the text of the plot name.      Name

         Plot Specific:General:Plot
                                        Specifies the level of opacity of the color you apply to the plot.         Opacity

         Plot
         Specific:General:Coordinates  Configures the coordinate system to display the 3D plot.
        System

         Plot
         Specific:Projection:Draw XY   Displays the plot projection on the XY plane.
         Projection

         Plot
         Specific:Projection:Draw YZ   Displays the plot projection on the YZ plane.
         Projection

         Plot
         Specific:Projection:Draw XZ   Displays the plot projection on the XZ plane.
         Projection

         Plot
                                        Specifies the style of the waterfall lines.
          Specific:Waterfall:Waterfall

6868   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6868 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6869 ordinal=6869 -->
## Property and Method Reference

Property and Method Reference


 Property                    Description

 Line Style

 Plot
 Specific:Waterfall:Waterfall    Specifies the width of the waterfall lines.
 Line Width

 Plot
 Specific:Waterfall:Waterfall    Sets the color map for the waterfall lines.
 Color Ramp

 Plot
 Specific:Waterfall:Waterfall   Uses anti-aliasing to show the waterfall lines.
 Line Anti-aliasing

 Plot
 Specific:Waterfall:Waterfall    Sets the display mode to show a different waterfall.
 Mode

Graph:FastGraph:Fast DrawDraw

Speeds up the pan, zoom, and rotate operations of the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6869

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6869 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6870 ordinal=6870 -->
## Property and Method Reference

Property and Method Reference

    Graph:ClipGraph:Clip DataData

      Uses the clip plane to hide the part of the plot that is outside the axes.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:BackgroundGraph:Background ColorColor

       Specifies the background color of the plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6870   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6870 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6871 ordinal=6871 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:ProjectionGraph:Projection ModeMode

Changes the projection of the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:ViewGraph:View DirectionDirection

Sets the direction for viewing the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6871

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6871 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6872 ordinal=6872 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:UserGraph:User DefinedDefined View:ViewView:View LatitudeLatitude

       Sets the latitude of the user-defined direction for viewing the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:UserGraph:User DefinedDefined View:ViewView:View LongitudeLongitude

       Sets the longitude of the user-defined direction for viewing the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


6872   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6872 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6873 ordinal=6873 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:UserGraph:User DefinedDefined View:ViewView:View DistanceDistance

Sets the distance of the user-defined direction for viewing the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:GridGraph:Grid Plane:XYPlane:XY PlanePlane VisibleVisible

Shows the 3D graph in the direction of the XY plane.


                                                    © National Instruments 6873

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6873 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6874 ordinal=6874 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:GridGraph:Grid Plane:YZPlane:YZ PlanePlane VisibleVisible

      Shows the 3D graph in the direction of the YZ plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6874   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6874 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6875 ordinal=6875 -->
## Property and Method Reference

Property and Method Reference

Graph:GridGraph:Grid Plane:XZPlane:XZ PlanePlane VisibleVisible

Shows the 3D graph in the direction of the XZ plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:GridGraph:Grid Plane:GridPlane:Grid Anti-aliasingAnti-aliasing

Uses anti-aliasing to show the grid lines.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6875

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6875 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6876 ordinal=6876 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:GridGraph:Grid Plane:FramePlane:Frame ColorColor

       Specifies the color of the grid frame.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:EnableLight:Enable LightingLighting

      Enables the entire setting for the light.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6876   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6876 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6877 ordinal=6877 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:ActiveLight:Active LightLight

Sets the specified settings of the light you want to configure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:EnableLight:Enable LightLight

Enables specified settings for the light.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6877

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6877 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6878 ordinal=6878 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:LightLight:Light ColorColor

      Changes the specific light color.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:LightLight:Light LatitudeLatitude

       Sets the latitude of the specified light towards the target.


6878   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6878 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6879 ordinal=6879 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:LightLight:Light LongitudeLongitude

Sets the longitude of the specified light towards the target.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6879

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6879 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6880 ordinal=6880 -->
## Property and Method Reference

Property and Method Reference

    Light:LightLight:Light DistanceDistance

       Sets the distance of the specified light towards the target.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:LightLight:Light AttenuationAttenuation

      Changes the attenuation mode of the specified settings for the light.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6880   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6880 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6881 ordinal=6881 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:ActiveAxis:Active AxisAxis

Sets the axis you want to configure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:NameAxis:Name Label:NameLabel:Name LabelLabel ColorColor

Sets the color of the axis name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6881

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6881 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6882 ordinal=6882 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:NameAxis:Name Label:NameLabel:Name LabelLabel SizeSize

       Sets the font size of the axis name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:NameAxis:Name Label:NameLabel:Name LabelLabel TextText

       Configures the text that displays for the axis name label.

     Remarks

      The following table lists the characteristics of this property.


6882   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6882 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6883 ordinal=6883 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:NameAxis:Name Label:NameLabel:Name LabelLabel NormalNormal VisibleVisible

Displays the axis name label on one side of the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6883

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6883 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6884 ordinal=6884 -->
## Property and Method Reference

Property and Method Reference

   Axis:NameAxis:Name Label:NameLabel:Name LabelLabel OppositeOpposite
    VisibleVisible

       Displays the axis name label on the opposite side of the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Marker:MarkerAxis:Marker:Marker ColorColor

       Sets the color of the scale marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes


6884   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6884 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6885 ordinal=6885 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Marker:MarkerAxis:Marker:Marker SizeSize

Sets the font size of the scale marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Marker:MarkerAxis:Marker:Marker NormalNormal VisibleVisible

Displays the scale marker on one side of the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

                                                    © National Instruments 6885

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6885 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6886 ordinal=6886 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Marker:MarkerAxis:Marker:Marker OppositeOpposite VisibleVisible

       Displays the scale marker on the opposite side of the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:Range:RangeAxis:Range:Range MaximumMaximum

       Sets the maximum value of the scale.


6886   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6886 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6887 ordinal=6887 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Range:RangeAxis:Range:Range MinimumMinimum

Sets the minimum value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6887

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6887 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6888 ordinal=6888 -->
## Property and Method Reference

Property and Method Reference

   Axis:Range:RangeAxis:Range:Range AutoAuto ScaleScale

       Adjusts the scale automatically to reflect the data you wire to the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:Range:RangeAxis:Range:Range InvertedInverted

       Inverts the scale range from maximum to minimum.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6888   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6888 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6889 ordinal=6889 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Range:RangeAxis:Range:Range LogarithmLogarithm

Shows the scale in the logarithm mapping mode.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Grid:GridAxis:Grid:Grid MajorMajor ColorColor

Sets the color of the major axis grid.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6889

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6889 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6890 ordinal=6890 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Grid:GridAxis:Grid:Grid MajorMajor VisibleVisible

       Displays the major axis grid in the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Grid:GridAxis:Grid:Grid MinorMinor ColorColor

       Sets the color of the minor axis grid.

     Remarks

      The following table lists the characteristics of this property.


6890   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6890 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6891 ordinal=6891 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Grid:GridAxis:Grid:Grid MinorMinor VisibleVisible

Displays the minor axis grid in the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Tick:TickAxis:Tick:Tick MajorMajor CountCount

Specifies the number of major tick marks that appear on the axis.


                                                    © National Instruments 6891

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6891 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6892 ordinal=6892 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Tick:TickAxis:Tick:Tick MajorMajor ColorColor

       Sets the color of the major tick marks on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6892   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6892 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6893 ordinal=6893 -->
## Property and Method Reference

Property and Method Reference

Axis:Tick:TickAxis:Tick:Tick MajorMajor VisibleVisible

Displays the major tick marks on the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Tick:TickAxis:Tick:Tick MinorMinor CountCount

Specifies the number of minor tick marks that appear on the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6893

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6893 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6894 ordinal=6894 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Tick:TickAxis:Tick:Tick MinorMinor ColorColor

       Sets the color of the minor tick marks on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Tick:TickAxis:Tick:Tick MinorMinor VisibleVisible

       Displays the minor tick marks on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6894   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6894 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6895 ordinal=6895 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:ActivePairs:Active ValueValue PairPair

Sets the axis to configure its value pairs.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:ValuePairs:Value PairPair LabelLabel TypeType

Specifies how value pairs appear on the scale marker.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6895

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6895 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6896 ordinal=6896 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   ValueValue Pairs:ValuePairs:Value PairPair TickTick VisibleVisible

       Displays tick marks for each value pair.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   ValueValue Pairs:ValuePairs:Value PairPair GridGrid VisibleVisible

       Displays grid lines for each value pair.


6896   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6896 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6897 ordinal=6897 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:ValuePairs:Value PairPair ArrayArray

Lists the index, name, and value of the value pairs you want to display on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6897

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6897 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6898 ordinal=6898 -->
## Property and Method Reference

Property and Method Reference

    Format:AxisFormat:Axis XX FormatFormat StringString

       Sets the formatting for the x-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Format:AxisFormat:Axis YY FormatFormat StringString

       Sets the formatting for the y-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6898   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6898 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6899 ordinal=6899 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Format:AxisFormat:Axis ZZ FormatFormat StringString

Sets the formatting for the z-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:ActiveCursors:Active CursorCursor

Sets the cursor you want to configure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6899

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6899 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6900 ordinal=6900 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor EnableEnable

      Enables you to move the cursor you configure around the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor VisibleVisible

       Displays the cursor in the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


6900   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6900 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6901 ordinal=6901 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor LockLock StyleStyle

Sets the style of the cursor lock.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor PlotPlot IDID

Sets the cursor to snap to the specified plot.


                                                    © National Instruments 6901

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6901 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6902 ordinal=6902 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor XX PositionPosition

       Sets the position of the cursor on the x-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6902   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6902 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6903 ordinal=6903 -->
## Property and Method Reference

Property and Method Reference

Cursors:General:CursorCursors:General:Cursor YY PositionPosition

Sets the position of the cursor on the y-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor ZZ PositionPosition

Sets the position of the cursor on the z-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6903

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6903 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6904 ordinal=6904 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Point:CursorCursors:Point:Cursor PointPoint ColorColor

       Sets the color of the cursor point.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Point:CursorCursors:Point:Cursor PointPoint SizeSize

       Specifies the size of the point on the cursor.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6904   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6904 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6905 ordinal=6905 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Point:CursorCursors:Point:Cursor PointPoint StyleStyle

Specifies the symbol style of the point on the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Line:CursorCursors:Line:Cursor LineLine ColorColor

Sets the color of the cursor line.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6905

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6905 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6906 ordinal=6906 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Line:CursorCursors:Line:Cursor LineLine WidthWidth

       Specifies the width of the cursor line.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Line:CursorCursors:Line:Cursor LineLine StyleStyle

       Specifies the style of the cursor line.


6906   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6906 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6907 ordinal=6907 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane ColorColor

Sets the color of the cursor plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6907

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6907 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6908 ordinal=6908 -->
## Property and Method Reference

Property and Method Reference

    Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane OpacityOpacity

       Specifies the level of opacity of the color you apply to the cursor plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane XYXY VisibleVisible

       Displays the XY cursor plane on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6908   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6908 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6909 ordinal=6909 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane XZXZ VisibleVisible

Displays the XZ cursor plane on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane YZYZ VisibleVisible

Displays the YZ cursor plane on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6909

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6909 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6910 ordinal=6910 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor NameName

       Configures the text of the cursor name.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor TextText ColorColor

       Specifies the color of the cursor text.

     Remarks

      The following table lists the characteristics of this property.


6910   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6910 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6911 ordinal=6911 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor TextText SizeSize

Specifies the font size of the cursor text. The text includes the cursor name and its
position.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor ShowShow PositionPosition

Displays the cursor position on the 3D graph.

                                                    © National Instruments 6911

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6911 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6912 ordinal=6912 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor ShowShow NameName

       Displays the cursor name on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6912   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6912 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6913 ordinal=6913 -->
## Property and Method Reference

Property and Method Reference

Cursors:Text:CursorCursors:Text:Cursor TextText BackgroundBackground ColorColor

Specifies the color of the cursor text background.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor TextText BackgroundBackground
OpacityOpacity

Specifies the level of opacity of the color you apply to the cursor text background.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 6913

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6913 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6914 ordinal=6914 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:CursorCursors:Cursor ListList

       Displays an array of information about all the cursors.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:ActiveSpecific:Active PlotPlot

       Gets or sets the active plot. After you get or set the active plot, you then can set
       properties or invoke methods that affect only the specified plot.

     Remarks

      The following table lists the characteristics of this property.


6914   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6914 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6915 ordinal=6915 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:General:PlotSpecific:General:Plot NameName

Configures the text of the plot name.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:General:PlotSpecific:General:Plot OpacityOpacity

Specifies the level of opacity of the color you apply to the plot.


                                                    © National Instruments 6915

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6915 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6916 ordinal=6916 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:General:CoordinatesSpecific:General:Coordinates SystemSystem

       Configures the coordinate system to display the 3D plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6916   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6916 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6917 ordinal=6917 -->
## Property and Method Reference

Property and Method Reference

PlotPlot Specific:Projection:DrawSpecific:Projection:Draw XYXY ProjectionProjection

Displays the plot projection on the XY plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Projection:DrawSpecific:Projection:Draw YZYZ ProjectionProjection

Displays the plot projection on the YZ plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6917

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6917 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6918 ordinal=6918 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Projection:DrawSpecific:Projection:Draw XZXZ ProjectionProjection

       Displays the plot projection on the XZ plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Waterfall:WaterfallSpecific:Waterfall:Waterfall LineLine StyleStyle

       Specifies the style of the waterfall lines.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6918   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6918 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6919 ordinal=6919 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Waterfall:WaterfallSpecific:Waterfall:Waterfall LineLine WidthWidth

Specifies the width of the waterfall lines.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Waterfall:WaterfallSpecific:Waterfall:Waterfall ColorColor RampRamp

Sets the color map for the waterfall lines.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6919

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6919 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6920 ordinal=6920 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Waterfall:WaterfallSpecific:Waterfall:Waterfall LineLine Anti-Anti-
    aliasingaliasing

      Uses anti-aliasing to show the waterfall lines.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6920   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6920 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6921 ordinal=6921 -->
## Property and Method Reference

Property and Method Reference

PlotPlot Specific:Waterfall:WaterfallSpecific:Waterfall:Waterfall ModeMode

Sets the display mode to show a different waterfall.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

3D3D WaterfallWaterfall MethodsMethods


 Method                    Description

 Clean Data                 Cleans up the input data by removing all the plots.

                            Resets the view direction to the default view.
 Reset to Default View
                          Views are latitude (60), longitude (45), and distance (2).

 Image to Printer           Sends the 3D graph image to the default printer.

 Image to File              Saves the 3D graph image to an image file or the clipboard.

 Get Picture Control Ref      Returns the reference number to the 3D picture control.


                                                    © National Instruments 6921

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6921 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6922 ordinal=6922 -->
## Property and Method Reference

Property and Method Reference

   CleanClean DataData

       Cleans up the input data by removing all the plots.

     Remarks

      The following table lists the characteristics of this method.


         Available in Run-Time Engine                                                         Yes

         Available in Real-Time Operating System                                              Yes

         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No

   ResetReset toto DefaultDefault ViewView

       Resets the view direction to the default view.

      Views are latitude (60), longitude (45), and distance (2).

     Remarks

      The following table lists the characteristics of this method.


         Available in Run-Time Engine                                                         Yes

         Available in Real-Time Operating System                                              Yes

         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No


6922   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6922 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6923 ordinal=6923 -->
## Property and Method Reference

Property and Method Reference

ImageImage toto PrinterPrinter

Sends the 3D graph image to the default printer.

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes

 Settable when the VI is running                                                       Yes

 Loads the front panel into memory                                                    Yes

 Need to authenticate before use                                         No

 Loads the block diagram into memory                                     No

ImageImage toto FileFile

Saves the 3D graph image to an image file or the clipboard.

Parameters

       Data Name       Required  Description
        type

                          Specifies the format of the file. You can export into one of the following
                         formats:

 File                   (Windows) .emf, .bmp (default), and .eps files              Yes
 Type
                     (macOS) .pict, .bmp (default), and .eps files

                           (Linux) .bmp (default) and .eps files

 Target        Yes        Specifies whether to save the image to the clipboard or to disk. When you


                                                    © National Instruments 6923

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6923 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6924 ordinal=6924 -->
## Property and Method Reference

Property and Method Reference


               Data      Name       Required  Description
               type

                                   set Target to File, you must specify a Path.

                              Path to the new image file. LabVIEW ignores this parameter if you set        Path         Yes                                Target to Clipboard. When you set Target to File, you must specify a Path.

     Remarks

      The following table lists the characteristics of this method.


         Available in Run-Time Engine                                                         Yes

         Available in Real-Time Operating System                                              Yes

         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No

   GetGet PicturePicture ControlControl RefRef

       Returns the reference number to the 3D picture control.

     Parameters

      Name              Data type   Required   Description

       3D Picture Control             No        The 3D picture control owned by the graph.

     Remarks

      The following table lists the characteristics of this method.


         Available in Run-Time Engine                                                         Yes

         Available in Real-Time Operating System                                              Yes

6924   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6924 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6925 ordinal=6925 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                                       Yes

 Loads the front panel into memory                                                    Yes

 Need to authenticate before use                                         No

 Loads the block diagram into memory                                     No

3D3D RibbonRibbon

3D3D RibbonRibbon PropertiesProperties


 Property                    Description

 Graph:Fast Draw            Speeds up the pan, zoom, and rotate operations of the 3D graph.

                           Uses the clip plane to hide the part of the plot that is outside the Graph:Clip Data
                               axes.

 Graph:Background Color      Specifies the background color of the plot.

 Graph:Projection Mode      Changes the projection of the 3D graph.

 Graph:View Direction         Sets the direction for viewing the 3D graph.

 Graph:User Defined          Sets the latitude of the user-defined direction for viewing the 3D
 View:View Latitude           graph.

 Graph:User Defined          Sets the longitude of the user-defined direction for viewing the 3D
 View:View Longitude         graph.

 Graph:User Defined          Sets the distance of the user-defined direction for viewing the 3D
 View:View Distance           graph.

 Graph:Grid Plane:XY Plane
                        Shows the 3D graph in the direction of the XY plane.
 Visible

 Graph:Grid Plane:YZ Plane
                        Shows the 3D graph in the direction of the YZ plane.
 Visible

 Graph:Grid Plane:XZ Plane
                        Shows the 3D graph in the direction of the XZ plane.
 Visible

 Graph:Grid Plane:Grid Anti-
                           Uses anti-aliasing to show the grid lines.
 aliasing

 Graph:Grid Plane:Frame
                                Specifies the color of the grid frame.
 Color


                                                    © National Instruments 6925

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6925 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6926 ordinal=6926 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

         Light:Enable Lighting        Enables the entire setting for the light.

          Light:Active Light             Sets the specified settings of the light you want to configure.

         Light:Enable Light           Enables specified settings for the light.

          Light:Light Color           Changes the specific light color.

          Light:Light Latitude          Sets the latitude of the specified light towards the target.

          Light:Light Longitude         Sets the longitude of the specified light towards the target.

          Light:Light Distance          Sets the distance of the specified light towards the target.

          Light:Light Attenuation      Changes the attenuation mode of the specified settings for the light.

          Axis:Active Axis               Sets the axis you want to configure.

        Axis:Name Label:Name                                      Sets the color of the axis name label.         Label Color

        Axis:Name Label:Name                                      Sets the font size of the axis name label.         Label Size

        Axis:Name Label:Name                                     Configures the text that displays for the axis name label.         Label Text

        Axis:Name Label:Name                                      Displays the axis name label on one side of the axis.         Label Normal Visible

        Axis:Name Label:Name                                      Displays the axis name label on the opposite side of the axis.         Label Opposite Visible

         Axis:Marker:Marker Color     Sets the color of the scale marker.

         Axis:Marker:Marker Size       Sets the font size of the scale marker.

         Axis:Marker:Marker Normal
                                      Displays the scale marker on one side of the axis.
          Visible

         Axis:Marker:Marker Opposite
                                      Displays the scale marker on the opposite side of the axis.
          Visible

         Axis:Range:Range Maximum  Sets the maximum value of the scale.

         Axis:Range:Range Minimum   Sets the minimum value of the scale.

                                      Adjusts the scale automatically to reflect the data you wire to the 3D
         Axis:Range:Range Auto Scale
                                     graph.

         Axis:Range:Range Inverted    Inverts the scale range from maximum to minimum.


6926   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6926 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6927 ordinal=6927 -->
## Property and Method Reference

Property and Method Reference


Property                    Description

Axis:Range:Range Logarithm  Shows the scale in the logarithm mapping mode.

Axis:Grid:Grid Major Color     Sets the color of the major axis grid.

Axis:Grid:Grid Major Visible    Displays the major axis grid in the 3D graph.

Axis:Grid:Grid Minor Color     Sets the color of the minor axis grid.

Axis:Grid:Grid Minor Visible    Displays the minor axis grid in the 3D graph.

Axis:Tick:Tick Major Count    Specifies the number of major tick marks that appear on the axis.

Axis:Tick:Tick Major Color     Sets the color of the major tick marks on the axis.

Axis:Tick:Tick Major Visible    Displays the major tick marks on the axis.

Axis:Tick:Tick Minor Count    Specifies the number of minor tick marks that appear on the axis.

Axis:Tick:Tick Minor Color     Sets the color of the minor tick marks on the axis.

Axis:Tick:Tick Minor Visible    Displays the minor tick marks on the axis.

Value Pairs:Active Value Pair   Sets the axis to configure its value pairs.

Value Pairs:Value Pair Label                               Specifies how value pairs appear on the scale marker.
Type

Value Pairs:Value Pair Tick                             Displays tick marks for each value pair.
Visible

Value Pairs:Value Pair Grid
                             Displays grid lines for each value pair.Visible

                                  Lists the index, name, and value of the value pairs you want to
Value Pairs:Value Pair Array                              display on the 3D graph.

Format:Axis X Format String   Sets the formatting for the x-axis.

Format:Axis Y Format String   Sets the formatting for the y-axis.

Format:Axis Z Format String   Sets the formatting for the z-axis.

Cursors:Active Cursor         Sets the cursor you want to configure.

Cursors:General:Cursor
                           Enables you to move the cursor you configure around the 3D graph.
Enable

Cursors:General:Cursor
                             Displays the cursor in the 3D graph.
Visible

Cursors:General:Cursor Lock  Sets the style of the cursor lock.


                                                    © National Instruments 6927

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6927 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6928 ordinal=6928 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

         Style

         Cursors:General:Cursor Plot                                      Sets the cursor to snap to the specified plot.         ID

         Cursors:General:Cursor X                                      Sets the position of the cursor on the x-axis.
         Position

         Cursors:General:Cursor Y                                      Sets the position of the cursor on the y-axis.         Position

         Cursors:General:Cursor Z                                      Sets the position of the cursor on the z-axis.
         Position

         Cursors:Point:Cursor Point                                      Sets the color of the cursor point.         Color

         Cursors:Point:Cursor Point                                        Specifies the size of the point on the cursor.         Size

         Cursors:Point:Cursor Point                                        Specifies the symbol style of the point on the cursor.         Style

         Cursors:Line:Cursor Line                                      Sets the color of the cursor line.         Color

         Cursors:Line:Cursor Line                                        Specifies the width of the cursor line.        Width

         Cursors:Line:Cursor Line                                        Specifies the style of the cursor line.         Style

         Cursors:Plane:Cursor Plane                                      Sets the color of the cursor plane.         Color

         Cursors:Plane:Cursor Plane   Specifies the level of opacity of the color you apply to the cursor
         Opacity                      plane.

         Cursors:Plane:Cursor Plane
                                      Displays the XY cursor plane on the 3D graph.
        XY Visible

         Cursors:Plane:Cursor Plane
                                      Displays the XZ cursor plane on the 3D graph.
       XZ Visible

         Cursors:Plane:Cursor Plane
                                      Displays the YZ cursor plane on the 3D graph.
        YZ Visible

         Cursors:Text:Cursor Name    Configures the text of the cursor name.


6928   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6928 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6929 ordinal=6929 -->
## Property and Method Reference

Property and Method Reference


Property                    Description

Cursors:Text:Cursor Text                               Specifies the color of the cursor text.Color

                               Specifies the font size of the cursor text. The text includes the cursorCursors:Text:Cursor Text Size                      name and its position.

Cursors:Text:Cursor Show                             Displays the cursor position on the 3D graph.Position

Cursors:Text:Cursor Show                             Displays the cursor name on the 3D graph.Name

Cursors:Text:Cursor Text                               Specifies the color of the cursor text background.Background Color

Cursors:Text:Cursor Text      Specifies the level of opacity of the color you apply to the cursor text
Background Opacity         background.

Cursors:Cursor List           Displays an array of information about all the cursors.

                            Gets or sets the active plot. After you get or set the active plot, you
Plot Specific:Active Plot      then can set properties or invoke methods that affect only the
                               specified plot.

Plot Specific:General:Plot
                            Configures the text of the plot name.Name

Plot Specific:General:Plot
                               Specifies the level of opacity of the color you apply to the plot.Opacity

Plot
Specific:General:Coordinates  Configures the coordinate system to display the 3D plot.
System

Plot
Specific:Projection:Draw XY   Displays the plot projection on the XY plane.
Projection

Plot
Specific:Projection:Draw YZ   Displays the plot projection on the YZ plane.
Projection

Plot
Specific:Projection:Draw XZ   Displays the plot projection on the XZ plane.
Projection

Plot Specific:Ribbon:Draw
                             Displays the chromatic ribbon.
Ribbon

                                                    © National Instruments 6929

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6929 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6930 ordinal=6930 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

         Plot Specific:Ribbon:Ribbon                                      Sets the color map of the chromatic ribbon.         Color Ramp

         Plot Specific:Ribbon:Ribbon                                        Specifies the style of the outlines.         Line Style

         Plot Specific:Ribbon:Ribbon                                        Specifies the width of the outlines.         Line Width

         Plot Specific:Ribbon:Ribbon                                      Sets the color of the outlines.         Line Color

         Plot Specific:Ribbon:Ribbon                                  Uses anti-aliasing to show the outlines.         Line Anti-aliasing

         Plot Specific:Ribbon:Ribbon                                      Sets the draw direction of the ribbon towards the x- or y-axis.
       Mode

         Plot Specific:Ribbon:Ribbon                                        Specifies the width for the ribbon.
        Width

    Graph:FastGraph:Fast DrawDraw

      Speeds up the pan, zoom, and rotate operations of the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

6930   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6930 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6931 ordinal=6931 -->
## Property and Method Reference

Property and Method Reference

Graph:ClipGraph:Clip DataData

Uses the clip plane to hide the part of the plot that is outside the axes.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:BackgroundGraph:Background ColorColor

Specifies the background color of the plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6931

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6931 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6932 ordinal=6932 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:ProjectionGraph:Projection ModeMode

      Changes the projection of the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:ViewGraph:View DirectionDirection

       Sets the direction for viewing the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6932   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6932 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6933 ordinal=6933 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:UserGraph:User DefinedDefined View:ViewView:View LatitudeLatitude

Sets the latitude of the user-defined direction for viewing the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:UserGraph:User DefinedDefined View:ViewView:View LongitudeLongitude

Sets the longitude of the user-defined direction for viewing the 3D graph.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6933

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6933 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6934 ordinal=6934 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:UserGraph:User DefinedDefined View:ViewView:View DistanceDistance

       Sets the distance of the user-defined direction for viewing the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:GridGraph:Grid Plane:XYPlane:XY PlanePlane VisibleVisible

      Shows the 3D graph in the direction of the XY plane.


6934   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6934 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6935 ordinal=6935 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:GridGraph:Grid Plane:YZPlane:YZ PlanePlane VisibleVisible

Shows the 3D graph in the direction of the YZ plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6935

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6935 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6936 ordinal=6936 -->
## Property and Method Reference

Property and Method Reference

    Graph:GridGraph:Grid Plane:XZPlane:XZ PlanePlane VisibleVisible

      Shows the 3D graph in the direction of the XZ plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:GridGraph:Grid Plane:GridPlane:Grid Anti-aliasingAnti-aliasing

      Uses anti-aliasing to show the grid lines.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6936   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6936 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6937 ordinal=6937 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:GridGraph:Grid Plane:FramePlane:Frame ColorColor

Specifies the color of the grid frame.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:EnableLight:Enable LightingLighting

Enables the entire setting for the light.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6937

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6937 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6938 ordinal=6938 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:ActiveLight:Active LightLight

       Sets the specified settings of the light you want to configure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:EnableLight:Enable LightLight

      Enables specified settings for the light.

     Remarks

      The following table lists the characteristics of this property.


6938   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6938 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6939 ordinal=6939 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:LightLight:Light ColorColor

Changes the specific light color.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:LightLight:Light LatitudeLatitude

Sets the latitude of the specified light towards the target.


                                                    © National Instruments 6939

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6939 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6940 ordinal=6940 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:LightLight:Light LongitudeLongitude

       Sets the longitude of the specified light towards the target.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6940   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6940 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6941 ordinal=6941 -->
## Property and Method Reference

Property and Method Reference

Light:LightLight:Light DistanceDistance

Sets the distance of the specified light towards the target.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Light:LightLight:Light AttenuationAttenuation

Changes the attenuation mode of the specified settings for the light.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6941

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6941 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6942 ordinal=6942 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:ActiveAxis:Active AxisAxis

       Sets the axis you want to configure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:NameAxis:Name Label:NameLabel:Name LabelLabel ColorColor

       Sets the color of the axis name label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6942   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6942 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6943 ordinal=6943 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:NameAxis:Name Label:NameLabel:Name LabelLabel SizeSize

Sets the font size of the axis name label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:NameAxis:Name Label:NameLabel:Name LabelLabel TextText

Configures the text that displays for the axis name label.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6943

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6943 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6944 ordinal=6944 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:NameAxis:Name Label:NameLabel:Name LabelLabel NormalNormal VisibleVisible

       Displays the axis name label on one side of the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6944   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6944 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6945 ordinal=6945 -->
## Property and Method Reference

Property and Method Reference

Axis:NameAxis:Name Label:NameLabel:Name LabelLabel OppositeOpposite
VisibleVisible

Displays the axis name label on the opposite side of the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Marker:MarkerAxis:Marker:Marker ColorColor

Sets the color of the scale marker.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 6945

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6945 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6946 ordinal=6946 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Marker:MarkerAxis:Marker:Marker SizeSize

       Sets the font size of the scale marker.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Marker:MarkerAxis:Marker:Marker NormalNormal VisibleVisible

       Displays the scale marker on one side of the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

6946   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6946 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6947 ordinal=6947 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Marker:MarkerAxis:Marker:Marker OppositeOpposite VisibleVisible

Displays the scale marker on the opposite side of the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Range:RangeAxis:Range:Range MaximumMaximum

Sets the maximum value of the scale.


                                                    © National Instruments 6947

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6947 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6948 ordinal=6948 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:Range:RangeAxis:Range:Range MinimumMinimum

       Sets the minimum value of the scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6948   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6948 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6949 ordinal=6949 -->
## Property and Method Reference

Property and Method Reference

Axis:Range:RangeAxis:Range:Range AutoAuto ScaleScale

Adjusts the scale automatically to reflect the data you wire to the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Range:RangeAxis:Range:Range InvertedInverted

Inverts the scale range from maximum to minimum.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6949

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6949 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6950 ordinal=6950 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Axis:Range:RangeAxis:Range:Range LogarithmLogarithm

      Shows the scale in the logarithm mapping mode.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Grid:GridAxis:Grid:Grid MajorMajor ColorColor

       Sets the color of the major axis grid.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6950   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6950 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6951 ordinal=6951 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Grid:GridAxis:Grid:Grid MajorMajor VisibleVisible

Displays the major axis grid in the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Grid:GridAxis:Grid:Grid MinorMinor ColorColor

Sets the color of the minor axis grid.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6951

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6951 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6952 ordinal=6952 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Grid:GridAxis:Grid:Grid MinorMinor VisibleVisible

       Displays the minor axis grid in the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Tick:TickAxis:Tick:Tick MajorMajor CountCount

       Specifies the number of major tick marks that appear on the axis.


6952   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6952 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6953 ordinal=6953 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Tick:TickAxis:Tick:Tick MajorMajor ColorColor

Sets the color of the major tick marks on the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6953

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6953 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6954 ordinal=6954 -->
## Property and Method Reference

Property and Method Reference

    Axis:Tick:TickAxis:Tick:Tick MajorMajor VisibleVisible

       Displays the major tick marks on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Axis:Tick:TickAxis:Tick:Tick MinorMinor CountCount

       Specifies the number of minor tick marks that appear on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6954   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6954 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6955 ordinal=6955 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Tick:TickAxis:Tick:Tick MinorMinor ColorColor

Sets the color of the minor tick marks on the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axis:Tick:TickAxis:Tick:Tick MinorMinor VisibleVisible

Displays the minor tick marks on the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6955

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6955 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6956 ordinal=6956 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   ValueValue Pairs:ActivePairs:Active ValueValue PairPair

       Sets the axis to configure its value pairs.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   ValueValue Pairs:ValuePairs:Value PairPair LabelLabel TypeType

       Specifies how value pairs appear on the scale marker.

     Remarks

      The following table lists the characteristics of this property.


6956   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6956 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6957 ordinal=6957 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:ValuePairs:Value PairPair TickTick VisibleVisible

Displays tick marks for each value pair.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:ValuePairs:Value PairPair GridGrid VisibleVisible

Displays grid lines for each value pair.


                                                    © National Instruments 6957

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6957 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6958 ordinal=6958 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   ValueValue Pairs:ValuePairs:Value PairPair ArrayArray

        Lists the index, name, and value of the value pairs you want to display on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6958   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6958 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6959 ordinal=6959 -->
## Property and Method Reference

Property and Method Reference

Format:AxisFormat:Axis XX FormatFormat StringString

Sets the formatting for the x-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Format:AxisFormat:Axis YY FormatFormat StringString

Sets the formatting for the y-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6959

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6959 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6960 ordinal=6960 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Format:AxisFormat:Axis ZZ FormatFormat StringString

       Sets the formatting for the z-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:ActiveCursors:Active CursorCursor

       Sets the cursor you want to configure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6960   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6960 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6961 ordinal=6961 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor EnableEnable

Enables you to move the cursor you configure around the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor VisibleVisible

Displays the cursor in the 3D graph.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6961

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6961 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6962 ordinal=6962 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor LockLock StyleStyle

       Sets the style of the cursor lock.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor PlotPlot IDID

       Sets the cursor to snap to the specified plot.


6962   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6962 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6963 ordinal=6963 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:General:CursorCursors:General:Cursor XX PositionPosition

Sets the position of the cursor on the x-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6963

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6963 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6964 ordinal=6964 -->
## Property and Method Reference

Property and Method Reference

    Cursors:General:CursorCursors:General:Cursor YY PositionPosition

       Sets the position of the cursor on the y-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:General:CursorCursors:General:Cursor ZZ PositionPosition

       Sets the position of the cursor on the z-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6964   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6964 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6965 ordinal=6965 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Point:CursorCursors:Point:Cursor PointPoint ColorColor

Sets the color of the cursor point.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Point:CursorCursors:Point:Cursor PointPoint SizeSize

Specifies the size of the point on the cursor.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6965

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6965 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6966 ordinal=6966 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Point:CursorCursors:Point:Cursor PointPoint StyleStyle

       Specifies the symbol style of the point on the cursor.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Line:CursorCursors:Line:Cursor LineLine ColorColor

       Sets the color of the cursor line.

     Remarks

      The following table lists the characteristics of this property.


6966   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6966 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6967 ordinal=6967 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Line:CursorCursors:Line:Cursor LineLine WidthWidth

Specifies the width of the cursor line.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Line:CursorCursors:Line:Cursor LineLine StyleStyle

Specifies the style of the cursor line.


                                                    © National Instruments 6967

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6967 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6968 ordinal=6968 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane ColorColor

       Sets the color of the cursor plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6968   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6968 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6969 ordinal=6969 -->
## Property and Method Reference

Property and Method Reference

Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane OpacityOpacity

Specifies the level of opacity of the color you apply to the cursor plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane XYXY VisibleVisible

Displays the XY cursor plane on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6969

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6969 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6970 ordinal=6970 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane XZXZ VisibleVisible

       Displays the XZ cursor plane on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Plane:CursorCursors:Plane:Cursor PlanePlane YZYZ VisibleVisible

       Displays the YZ cursor plane on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

6970   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6970 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6971 ordinal=6971 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor NameName

Configures the text of the cursor name.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor TextText ColorColor

Specifies the color of the cursor text.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6971

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6971 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6972 ordinal=6972 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor TextText SizeSize

       Specifies the font size of the cursor text. The text includes the cursor name and its
       position.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor ShowShow PositionPosition

       Displays the cursor position on the 3D graph.

6972   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6972 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6973 ordinal=6973 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:Text:CursorCursors:Text:Cursor ShowShow NameName

Displays the cursor name on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6973

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6973 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6974 ordinal=6974 -->
## Property and Method Reference

Property and Method Reference

    Cursors:Text:CursorCursors:Text:Cursor TextText BackgroundBackground ColorColor

       Specifies the color of the cursor text background.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Cursors:Text:CursorCursors:Text:Cursor TextText BackgroundBackground
   OpacityOpacity

       Specifies the level of opacity of the color you apply to the cursor text background.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes


6974   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6974 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6975 ordinal=6975 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor ListList

Displays an array of information about all the cursors.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:ActiveSpecific:Active PlotPlot

Gets or sets the active plot. After you get or set the active plot, you then can set
properties or invoke methods that affect only the specified plot.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6975

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6975 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6976 ordinal=6976 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:General:PlotSpecific:General:Plot NameName

       Configures the text of the plot name.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:General:PlotSpecific:General:Plot OpacityOpacity

       Specifies the level of opacity of the color you apply to the plot.


6976   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6976 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6977 ordinal=6977 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:General:CoordinatesSpecific:General:Coordinates SystemSystem

Configures the coordinate system to display the 3D plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6977

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6977 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6978 ordinal=6978 -->
## Property and Method Reference

Property and Method Reference

    PlotPlot Specific:Projection:DrawSpecific:Projection:Draw XYXY ProjectionProjection

       Displays the plot projection on the XY plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Projection:DrawSpecific:Projection:Draw YZYZ ProjectionProjection

       Displays the plot projection on the YZ plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6978   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6978 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6979 ordinal=6979 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Projection:DrawSpecific:Projection:Draw XZXZ ProjectionProjection

Displays the plot projection on the XZ plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Ribbon:DrawSpecific:Ribbon:Draw RibbonRibbon

Displays the chromatic ribbon.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6979

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6979 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6980 ordinal=6980 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Ribbon:RibbonSpecific:Ribbon:Ribbon ColorColor RampRamp

       Sets the color map of the chromatic ribbon.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Ribbon:RibbonSpecific:Ribbon:Ribbon LineLine StyleStyle

       Specifies the style of the outlines.

     Remarks

      The following table lists the characteristics of this property.


6980   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6980 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6981 ordinal=6981 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Ribbon:RibbonSpecific:Ribbon:Ribbon LineLine WidthWidth

Specifies the width of the outlines.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Ribbon:RibbonSpecific:Ribbon:Ribbon LineLine ColorColor

Sets the color of the outlines.


                                                    © National Instruments 6981

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6981 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6982 ordinal=6982 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    PlotPlot Specific:Ribbon:RibbonSpecific:Ribbon:Ribbon LineLine Anti-Anti-
    aliasingaliasing

      Uses anti-aliasing to show the outlines.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

6982   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6982 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6983 ordinal=6983 -->
## Property and Method Reference

Property and Method Reference

PlotPlot Specific:Ribbon:RibbonSpecific:Ribbon:Ribbon ModeMode

Sets the draw direction of the ribbon towards the x- or y-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

PlotPlot Specific:Ribbon:RibbonSpecific:Ribbon:Ribbon WidthWidth

Specifies the width for the ribbon.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6983

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6983 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6984 ordinal=6984 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     3D3D RibbonRibbon MethodsMethods


       Method                    Description

        Clean Data                 Cleans up the input data by removing all the plots.

                                    Resets the view direction to the default view.
         Reset to Default View
                                 Views are latitude (60), longitude (45), and distance (2).

        Image to Printer           Sends the 3D graph image to the default printer.

        Image to File              Saves the 3D graph image to an image file or the clipboard.

        Get Picture Control Ref      Returns the reference number to the 3D picture control.

   CleanClean DataData

       Cleans up the input data by removing all the plots.

     Remarks

      The following table lists the characteristics of this method.


         Available in Run-Time Engine                                                         Yes

         Available in Real-Time Operating System                                              Yes

         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No


6984   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6984 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6985 ordinal=6985 -->
## Property and Method Reference

Property and Method Reference

ResetReset toto DefaultDefault ViewView

Resets the view direction to the default view.

Views are latitude (60), longitude (45), and distance (2).

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes

 Settable when the VI is running                                                       Yes

 Loads the front panel into memory                                                    Yes

 Need to authenticate before use                                         No

 Loads the block diagram into memory                                     No

ImageImage toto PrinterPrinter

Sends the 3D graph image to the default printer.

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes

 Settable when the VI is running                                                       Yes

 Loads the front panel into memory                                                    Yes

 Need to authenticate before use                                         No

 Loads the block diagram into memory                                     No


                                                    © National Instruments 6985

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6985 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6986 ordinal=6986 -->
## Property and Method Reference

Property and Method Reference

   ImageImage toto FileFile

      Saves the 3D graph image to an image file or the clipboard.

     Parameters

               Data      Name       Required  Description               type

                                   Specifies the format of the file. You can export into one of the following
                                 formats:

           File                   (Windows) .emf, .bmp (default), and .eps files                      Yes        Type
                            (macOS) .pict, .bmp (default), and .eps files

                                   (Linux) .bmp (default) and .eps files

                                   Specifies whether to save the image to the clipboard or to disk. When you         Target        Yes                                   set Target to File, you must specify a Path.

                              Path to the new image file. LabVIEW ignores this parameter if you set        Path         Yes                                Target to Clipboard. When you set Target to File, you must specify a Path.

     Remarks

      The following table lists the characteristics of this method.


         Available in Run-Time Engine                                                         Yes

         Available in Real-Time Operating System                                              Yes

         Settable when the VI is running                                                       Yes

        Loads the front panel into memory                                                    Yes

       Need to authenticate before use                                         No

        Loads the block diagram into memory                                     No


6986   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6986 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6987 ordinal=6987 -->
## Property and Method Reference

Property and Method Reference

GetGet PicturePicture ControlControl RefRef

Returns the reference number to the 3D picture control.

Parameters

 Name              Data type   Required   Description

 3D Picture Control             No        The 3D picture control owned by the graph.

Remarks

The following table lists the characteristics of this method.


 Available in Run-Time Engine                                                         Yes

 Available in Real-Time Operating System                                              Yes

 Settable when the VI is running                                                       Yes

 Loads the front panel into memory                                                    Yes

 Need to authenticate before use                                         No

 Loads the block diagram into memory                                     No

3D3D ContourContour

3D3D ContourContour PropertiesProperties


 Property                    Description

 Graph:Fast Draw            Speeds up the pan, zoom, and rotate operations of the 3D graph.

                           Uses the clip plane to hide the part of the plot that is outside the
 Graph:Clip Data
                               axes.

 Graph:Background Color      Specifies the background color of the plot.

 Graph:Projection Mode      Changes the projection of the 3D graph.

 Graph:View Direction         Sets the direction for viewing the 3D graph.


                                                    © National Instruments 6987

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6987 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6988 ordinal=6988 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

        Graph:User Defined          Sets the latitude of the user-defined direction for viewing the 3D
        View:View Latitude           graph.

        Graph:User Defined          Sets the longitude of the user-defined direction for viewing the 3D
        View:View Longitude         graph.

        Graph:User Defined          Sets the distance of the user-defined direction for viewing the 3D
        View:View Distance           graph.

         Graph:Grid Plane:XY Plane                              Shows the 3D graph in the direction of the XY plane.          Visible

         Graph:Grid Plane:YZ Plane                              Shows the 3D graph in the direction of the YZ plane.          Visible

         Graph:Grid Plane:XZ Plane                              Shows the 3D graph in the direction of the XZ plane.
          Visible

         Graph:Grid Plane:Grid Anti-                                  Uses anti-aliasing to show the grid lines.
          aliasing

         Graph:Grid Plane:Frame                                        Specifies the color of the grid frame.
         Color

         Light:Enable Lighting        Enables the entire setting for the light.

          Light:Active Light             Sets the specified settings of the light you want to configure.

         Light:Enable Light           Enables specified settings for the light.

          Light:Light Color           Changes the specific light color.

          Light:Light Latitude          Sets the latitude of the specified light towards the target.

          Light:Light Longitude         Sets the longitude of the specified light towards the target.

          Light:Light Distance          Sets the distance of the specified light towards the target.

          Light:Light Attenuation      Changes the attenuation mode of the specified settings for the light.

          Axis:Active Axis               Sets the axis you want to configure.

        Axis:Name Label:Name
                                      Sets the color of the axis name label.
         Label Color

        Axis:Name Label:Name
                                      Sets the font size of the axis name label.
         Label Size

        Axis:Name Label:Name
                                     Configures the text that displays for the axis name label.
         Label Text


6988   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6988 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6989 ordinal=6989 -->
## Property and Method Reference

Property and Method Reference


Property                    Description

Axis:Name Label:Name                             Displays the axis name label on one side of the axis.Label Normal Visible

Axis:Name Label:Name                             Displays the axis name label on the opposite side of the axis.Label Opposite Visible

Axis:Marker:Marker Color     Sets the color of the scale marker.

Axis:Marker:Marker Size       Sets the font size of the scale marker.

Axis:Marker:Marker Normal                             Displays the scale marker on one side of the axis.Visible

Axis:Marker:Marker Opposite                             Displays the scale marker on the opposite side of the axis.Visible

Axis:Range:Range Maximum  Sets the maximum value of the scale.

Axis:Range:Range Minimum   Sets the minimum value of the scale.

                             Adjusts the scale automatically to reflect the data you wire to the 3DAxis:Range:Range Auto Scale
                             graph.

Axis:Range:Range Inverted    Inverts the scale range from maximum to minimum.

Axis:Range:Range Logarithm  Shows the scale in the logarithm mapping mode.

Axis:Grid:Grid Major Color     Sets the color of the major axis grid.

Axis:Grid:Grid Major Visible    Displays the major axis grid in the 3D graph.

Axis:Grid:Grid Minor Color     Sets the color of the minor axis grid.

Axis:Grid:Grid Minor Visible    Displays the minor axis grid in the 3D graph.

Axis:Tick:Tick Major Count    Specifies the number of major tick marks that appear on the axis.

Axis:Tick:Tick Major Color     Sets the color of the major tick marks on the axis.

Axis:Tick:Tick Major Visible    Displays the major tick marks on the axis.

Axis:Tick:Tick Minor Count    Specifies the number of minor tick marks that appear on the axis.

Axis:Tick:Tick Minor Color     Sets the color of the minor tick marks on the axis.

Axis:Tick:Tick Minor Visible    Displays the minor tick marks on the axis.

Value Pairs:Active Value Pair   Sets the axis to configure its value pairs.

Value Pairs:Value Pair Label
                               Specifies how value pairs appear on the scale marker.
Type


                                                    © National Instruments 6989

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6989 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6990 ordinal=6990 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

         Value Pairs:Value Pair Tick                                      Displays tick marks for each value pair.          Visible

         Value Pairs:Value Pair Grid                                      Displays grid lines for each value pair.          Visible

                                            Lists the index, name, and value of the value pairs you want to         Value Pairs:Value Pair Array                                       display on the 3D graph.

         Format:Axis X Format String   Sets the formatting for the x-axis.

         Format:Axis Y Format String   Sets the formatting for the y-axis.

         Format:Axis Z Format String   Sets the formatting for the z-axis.

         Cursors:Active Cursor         Sets the cursor you want to configure.

         Cursors:General:Cursor                                   Enables you to move the cursor you configure around the 3D graph.
        Enable

         Cursors:General:Cursor                                      Displays the cursor in the 3D graph.
          Visible

         Cursors:General:Cursor Lock                                      Sets the style of the cursor lock.
         Style

         Cursors:General:Cursor Plot
                                      Sets the cursor to snap to the specified plot.         ID

         Cursors:General:Cursor X
                                      Sets the position of the cursor on the x-axis.         Position

         Cursors:General:Cursor Y
                                      Sets the position of the cursor on the y-axis.         Position

         Cursors:General:Cursor Z
                                      Sets the position of the cursor on the z-axis.
         Position

         Cursors:Point:Cursor Point
                                      Sets the color of the cursor point.
         Color

         Cursors:Point:Cursor Point
                                        Specifies the size of the point on the cursor.
         Size

         Cursors:Point:Cursor Point
                                        Specifies the symbol style of the point on the cursor.
         Style

         Cursors:Line:Cursor Line
                                      Sets the color of the cursor line.
         Color


6990   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6990 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6991 ordinal=6991 -->
## Property and Method Reference

Property and Method Reference


Property                    Description

Cursors:Line:Cursor Line                               Specifies the width of the cursor line.Width

Cursors:Line:Cursor Line                               Specifies the style of the cursor line.Style

Cursors:Plane:Cursor Plane                             Sets the color of the cursor plane.Color

Cursors:Plane:Cursor Plane   Specifies the level of opacity of the color you apply to the cursor
Opacity                      plane.

Cursors:Plane:Cursor Plane                             Displays the XY cursor plane on the 3D graph.XY Visible

Cursors:Plane:Cursor Plane                             Displays the XZ cursor plane on the 3D graph.
XZ Visible

Cursors:Plane:Cursor Plane                             Displays the YZ cursor plane on the 3D graph.
YZ Visible

Cursors:Text:Cursor Name    Configures the text of the cursor name.

Cursors:Text:Cursor Text                               Specifies the color of the cursor text.Color

                               Specifies the font size of the cursor text. The text includes the cursorCursors:Text:Cursor Text Size                      name and its position.

Cursors:Text:Cursor Show                             Displays the cursor position on the 3D graph.Position

Cursors:Text:Cursor Show                             Displays the cursor name on the 3D graph.Name

Cursors:Text:Cursor Text
                               Specifies the color of the cursor text background.
Background Color

Cursors:Text:Cursor Text      Specifies the level of opacity of the color you apply to the cursor text
Background Opacity         background.

Cursors:Cursor List           Displays an array of information about all the cursors.

                            Gets or sets the active plot. After you get or set the active plot, you
Plot Specific:Active Plot      then can set properties or invoke methods that affect only the
                               specified plot.

Plot Specific:General:Plot
                            Configures the text of the plot name.
Name

                                                    © National Instruments 6991

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6991 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6992 ordinal=6992 -->
## Property and Method Reference

Property and Method Reference


        Property                    Description

         Plot Specific:General:Plot                                        Specifies the level of opacity of the color you apply to the plot.         Opacity

         Plot
         Specific:General:Coordinates  Configures the coordinate system to display the 3D plot.
        System

         Plot
         Specific:Projection:Draw XY   Displays the plot projection on the XY plane.
         Projection

         Plot
         Specific:Projection:Draw YZ   Displays the plot projection on the YZ plane.
         Projection

         Plot
         Specific:Projection:Draw XZ   Displays the plot projection on the XZ plane.
         Projection

         Plot
         Specific:Contour:Contour     Specifies the style of the contour lines.
         Line Style

         Plot
         Specific:Contour:Contour     Specifies the width of the contour lines.
         Line Width

         Plot
         Specific:Contour:Contour     Sets the color of the contour lines.
         Line Color

         Plot
         Specific:Contour:Contour    Uses anti-aliasing to show the contour lines.
         Line Anti-aliasing

         Plot
         Specific:Contour:Contour     Sets the color map for the ramp.
         Color Ramp

         Plot
         Specific:Contour:Contour     Sets the display mode of the contour.
       Mode

         Plot
         Specific:Contour:Contour     Sets the axis to draw the contour.
         Axis Basis


6992   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6992 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6993 ordinal=6993 -->
## Property and Method Reference

Property and Method Reference


 Property                    Description

 Plot
 Specific:Contour:Contour     Configures the values of the user-defined contour line.
 Level List

 Plot
 Specific:Contour:Contour     Sets the level mode of the contour lines.
 Level Mode

 Plot
 Specific:Contour:Contour     Configures the number of contour lines.
 Levels

 Plot
 Specific:Contour:Contour     Configures the interval between the contour lines.
 Interval

Graph:FastGraph:Fast DrawDraw

Speeds up the pan, zoom, and rotate operations of the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6993

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6993 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6994 ordinal=6994 -->
## Property and Method Reference

Property and Method Reference

    Graph:ClipGraph:Clip DataData

      Uses the clip plane to hide the part of the plot that is outside the axes.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:BackgroundGraph:Background ColorColor

       Specifies the background color of the plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

6994   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6994 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6995 ordinal=6995 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:ProjectionGraph:Projection ModeMode

Changes the projection of the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:ViewGraph:View DirectionDirection

Sets the direction for viewing the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6995

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6995 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6996 ordinal=6996 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:UserGraph:User DefinedDefined View:ViewView:View LatitudeLatitude

       Sets the latitude of the user-defined direction for viewing the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

   Graph:UserGraph:User DefinedDefined View:ViewView:View LongitudeLongitude

       Sets the longitude of the user-defined direction for viewing the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


6996   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6996 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6997 ordinal=6997 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:UserGraph:User DefinedDefined View:ViewView:View DistanceDistance

Sets the distance of the user-defined direction for viewing the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:GridGraph:Grid Plane:XYPlane:XY PlanePlane VisibleVisible

Shows the 3D graph in the direction of the XY plane.


                                                    © National Instruments 6997

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6997 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6998 ordinal=6998 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:GridGraph:Grid Plane:YZPlane:YZ PlanePlane VisibleVisible

      Shows the 3D graph in the direction of the YZ plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6998   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6998 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6999 ordinal=6999 -->
## Property and Method Reference

Property and Method Reference

Graph:GridGraph:Grid Plane:XZPlane:XZ PlanePlane VisibleVisible

Shows the 3D graph in the direction of the XZ plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:GridGraph:Grid Plane:GridPlane:Grid Anti-aliasingAnti-aliasing

Uses anti-aliasing to show the grid lines.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

                                                    © National Instruments 6999

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6999 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7000 ordinal=7000 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Graph:GridGraph:Grid Plane:FramePlane:Frame ColorColor

       Specifies the color of the grid frame.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

    Light:EnableLight:Enable LightingLighting

      Enables the entire setting for the light.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

7000   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7000 -->

