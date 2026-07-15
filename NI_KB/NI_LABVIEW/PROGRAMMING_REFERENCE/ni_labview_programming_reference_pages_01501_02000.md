# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1501 ordinal=1501 -->
## Functions

Functions

OpenOpen ConfigConfig DataData

Opens a reference to the configuration data found in a platform-independent
configuration file.

Format the content of an .ini file correctly when you use this VI.


Inputs/Outputs

   •      configuration file path —

    configuration file path is the path to the platform-independent configuration file.

   •      create file if necessary (T) —

    create file if necessary (T) configures the VI to create the file specified in configuration file path
       if the file does not exist. You must set create file if necessary (T) to the default value of TRUE for
    the VI to create the file.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum —

    refnum is the reference number of the configuration data.

   •        file created? —

      file created? returns TRUE if the configuration file operation creates a file.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1501

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1501 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1502 ordinal=1502 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Configuration
        (INI)\Configuration (INI) File.lvproj

     ReadRead KeyKey

      Reads a value associated with a key in a specified section from the configuration data
        identified by refnum. If the key does not exist, the VI returns the default value. This VI
       supports multibyte characters in strings. Wire data to the default value input to
      determine the polymorphic instance to use or manually select the instance.


            • Read Key (Boolean) VI
            • Read Key (Double) VI
            • Read Key (I32) VI
            • Read Key (Path) VI
            • Read Key (String) VI
            • Read Key (U32) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Configuration
        (INI)\Configuration (INI) File.lvproj
   ReadRead KeyKey (Boolean)(Boolean) VIVI

      Reads a value associated with a key in a specified section from the configuration data
        identified by refnum. If the key does not exist, the VI returns the default value. This VI
       supports multibyte characters in strings. Wire data to the default value input to
      determine the polymorphic instance to use or manually select the instance.

1502   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1502 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1503 ordinal=1503 -->
## Functions

Functions


Inputs/Outputs

   •      section —

    section is the name of the section from which to read the specified key.

   •     refnum —

    refnum is the reference number of the configuration data.

   •      key —

    key is the name of the key to read.

   •       default value —

    default value is the value to return if the VI does not find the key in the specified section or if an
     error occurs.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the reference number of the configuration data.

   •      found? —

    found? is TRUE if the VI found the key in the specified section.

   •      value —

    value is the value of the key.

   •       error out —


                                                    © National Instruments 1503

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1503 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1504 ordinal=1504 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Configuration
        (INI)\Configuration (INI) File.lvproj
   ReadRead KeyKey (Double)(Double) VIVI

      Reads a value associated with a key in a specified section from the configuration data
        identified by refnum. If the key does not exist, the VI returns the default value. This VI
       supports multibyte characters in strings. Wire data to the default value input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      section —

            section is the name of the section from which to read the specified key.

               •     refnum —

          refnum is the reference number of the configuration data.

               •      key —

           key is the name of the key to read.

               •       default value —


1504   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1504 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1505 ordinal=1505 -->
## Functions

Functions


    default value is the value to return if the VI does not find the key in the specified section or if an
     error occurs.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the reference number of the configuration data.

   •      found? —

    found? is TRUE if the VI found the key in the specified section.

   •      value —

    value is the value of the key.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Configuration
   (INI)\Configuration (INI) File.lvproj
ReadRead KeyKey (I32)(I32) VIVI

Reads a value associated with a key in a specified section from the configuration data
identified by refnum. If the key does not exist, the VI returns the default value. This VI
supports multibyte characters in strings. Wire data to the default value input to
determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1505

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1505 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1506 ordinal=1506 -->
## Functions

Functions


      Inputs/Outputs

               •      section —

            section is the name of the section from which to read the specified key.

               •     refnum —

          refnum is the reference number of the configuration data.

               •      key —

           key is the name of the key to read.

               •       default value —

             default value is the value to return if the VI does not find the key in the specified section or if an
             error occurs.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is the reference number of the configuration data.

               •      found? —

           found? is TRUE if the VI found the key in the specified section.

               •      value —

            value is the value of the key.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1506   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1506 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1507 ordinal=1507 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Configuration
   (INI)\Configuration (INI) File.lvproj
ReadRead KeyKey (Path)(Path) VIVI

Reads a value associated with a key in a specified section from the configuration data
identified by refnum. If the key does not exist, the VI returns the default value. This VI
supports multibyte characters in strings. Wire data to the default value input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      section —

    section is the name of the section from which to read the specified key.

   •     refnum —

    refnum is the reference number of the configuration data.

   •      key —

    key is the name of the key to read.

   •       default value —

    default value is the value to return if the VI does not find the key in the specified section or if an
     error occurs.

   •       error in (no error) —


                                                    © National Instruments 1507

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1507 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1508 ordinal=1508 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is the reference number of the configuration data.

               •      found? —

           found? is TRUE if the VI found the key in the specified section.

               •      value —

            value is the value of the key.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Configuration
        (INI)\Configuration (INI) File.lvproj
   ReadRead KeyKey (String)(String) VIVI

      Reads a value associated with a key in a specified section from the configuration data
        identified by refnum. If the key does not exist, the VI returns the default value. This VI
       supports multibyte characters in strings. Wire data to the default value input to
      determine the polymorphic instance to use or manually select the instance.


1508   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1508 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1509 ordinal=1509 -->
## Functions

Functions

Inputs/Outputs

   •      section —

    section is the name of the section from which to read the specified key.

   •     refnum —

    refnum is the reference number of the configuration data.

   •      key —

    key is the name of the key to read.

   •       default value —

    default value is the value to return if the VI does not find the key in the specified section or if an
     error occurs.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      read raw string? (F) —

    read raw string? specifies whether the string was written without escaping unprintable and
    backslash (\) characters.

       If FALSE (default), the VI replaces any unprintable characters in the string, such as <ESC>, with a
    backslash and two Hex characters (\xx). If TRUE, the VI does not convert the unprintable
    characters in the string.

   •     refnum out —

    refnum out is the reference number of the configuration data.

   •      found? —

    found? is TRUE if the VI found the key in the specified section.

   •      value —

    value is the value of the key.

   •       error out —

                                                    © National Instruments 1509

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1509 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1510 ordinal=1510 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Configuration
        (INI)\Configuration (INI) File.lvproj
   ReadRead KeyKey (U32)(U32) VIVI

      Reads a value associated with a key in a specified section from the configuration data
        identified by refnum. If the key does not exist, the VI returns the default value. This VI
       supports multibyte characters in strings. Wire data to the default value input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      section —

            section is the name of the section from which to read the specified key.

               •     refnum —

          refnum is the reference number of the configuration data.

               •      key —

           key is the name of the key to read.

               •       default value —


1510   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1510 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1511 ordinal=1511 -->
## Functions

Functions


    default value is the value to return if the VI does not find the key in the specified section or if an
     error occurs.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the reference number of the configuration data.

   •      found? —

    found? is TRUE if the VI found the key in the specified section.

   •      value —

    value is the value of the key.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Configuration
   (INI)\Configuration (INI) File.lvproj

WriteWrite KeyKey

Writes a value to a key in a specified section of the configuration data identified by
refnum. This VI modifies data in memory. To write data to disk, use the Close Config
Data VI. Wire data to the value input to determine the polymorphic instance to use or
manually select the instance.

Format the content of an .ini file correctly when you use this VI.


                                                    © National Instruments 1511

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1511 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1512 ordinal=1512 -->
## Functions

Functions


            • Write Key (Boolean) VI
            • Write Key (Double) VI
            • Write Key (I32) VI
            • Write Key (Path) VI
            • Write Key (String) VI
            • Write Key (U32) VI

           If key exists, the VI replaces the existing value. If key does not exist, the VI adds the
       key/value pair to the end of the specified section. If section does not exist, the VI adds
       section, with the key/value pair, to the end of the configuration data.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Configuration
        (INI)\Configuration (INI) File.lvproj
    WriteWrite KeyKey (Boolean)(Boolean) VIVI

       Writes a value to a key in a specified section of the configuration data identified by
      refnum. This VI modifies data in memory. To write data to disk, use the Close Config
      Data VI. Wire data to the value input to determine the polymorphic instance to use or
      manually select the instance.

      Format the content of an .ini file correctly when you use this VI.


1512   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1512 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1513 ordinal=1513 -->
## Functions

Functions

Inputs/Outputs

   •      section —

    section is the name of the section in which to write the specified key.

   •     refnum —

    refnum is the reference number of the configuration data.

   •      key —

    key is the name of the key to write.

   •      value —

    value is the value to write to the key.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the reference number of the configuration data.

   •      found? —

    found? is TRUE if the VI found the key in the specified section.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If key exists, the VI replaces the existing value. If key does not exist, the VI adds the
key/value pair to the end of the specified section. If section does not exist, the VI adds
section, with the key/value pair, to the end of the configuration data.

Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 1513

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1513 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1514 ordinal=1514 -->
## Functions

Functions

            • labview\examples\File IO\Configuration
        (INI)\Configuration (INI) File.lvproj
    WriteWrite KeyKey (Double)(Double) VIVI

       Writes a value to a key in a specified section of the configuration data identified by
      refnum. This VI modifies data in memory. To write data to disk, use the Close Config
      Data VI. Wire data to the value input to determine the polymorphic instance to use or
      manually select the instance.

      Format the content of an .ini file correctly when you use this VI.


      Inputs/Outputs

               •      use system decimal point (T) —

           use system decimal point specifies whether to use the localized decimal separator. The default
                is TRUE.

               •      section —

            section is the name of the section in which to write the specified key.

               •     refnum —

          refnum is the reference number of the configuration data.

               •      key —

           key is the name of the key to write.

               •      value —


1514   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1514 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1515 ordinal=1515 -->
## Functions

Functions


    value is the value of the key to write.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       precision (6) —

    precision is the number of digits after the decimal point. The default is 6.

   •      format (fractional) —

    format is the format of the number.

              Fractional    0
               (default)
    1       Engineering
    2        Exponential

   •     refnum out —

    refnum out is the reference number of the configuration data.

   •      found? —

    found? is TRUE if the VI found the key in the specified section.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If key exists, the VI replaces the existing value. If key does not exist, the VI adds the
key/value pair to the end of the specified section. If section does not exist, the VI adds
section, with the key/value pair, to the end of the configuration data.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Configuration

                                                    © National Instruments 1515

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1515 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1516 ordinal=1516 -->
## Functions

Functions

        (INI)\Configuration (INI) File.lvproj
    WriteWrite KeyKey (I32)(I32) VIVI

       Writes a value to a key in a specified section of the configuration data identified by
      refnum. This VI modifies data in memory. To write data to disk, use the Close Config
      Data VI. Wire data to the value input to determine the polymorphic instance to use or
      manually select the instance.

      Format the content of an .ini file correctly when you use this VI.


      Inputs/Outputs

               •      section —

            section is the name of the section in which to write the specified key.

               •     refnum —

          refnum is the reference number of the configuration data.

               •      key —

           key is the name of the key to write.

               •      value —

            value is the value of the key to write.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —


1516   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1516 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1517 ordinal=1517 -->
## Functions

Functions


    refnum out is the reference number of the configuration data.

   •      found? —

    found? is TRUE if the VI found the key in the specified section.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If key exists, the VI replaces the existing value. If key does not exist, the VI adds the
key/value pair to the end of the specified section. If section does not exist, the VI adds
section, with the key/value pair, to the end of the configuration data.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Configuration
   (INI)\Configuration (INI) File.lvproj
WriteWrite KeyKey (Path)(Path) VIVI

Writes a value to a key in a specified section of the configuration data identified by
refnum. This VI modifies data in memory. To write data to disk, use the Close Config
Data VI. Wire data to the value input to determine the polymorphic instance to use or
manually select the instance.

Format the content of an .ini file correctly when you use this VI.


                                                    © National Instruments 1517

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1517 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1518 ordinal=1518 -->
## Functions

Functions

      Inputs/Outputs

               •      section —

            section is the name of the section in which to write the specified key.

               •     refnum —

          refnum is the reference number of the configuration data.

               •      key —

           key is the name of the key to write.

               •      value —

            value is the value of the key to write.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is the reference number of the configuration data.

               •      found? —

           found? is TRUE if the VI found the key in the specified section.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If key exists, the VI replaces the existing value. If key does not exist, the VI adds the
       key/value pair to the end of the specified section. If section does not exist, the VI adds
       section, with the key/value pair, to the end of the configuration data.

     Examples

       Refer to the following example files included with LabVIEW.


1518   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1518 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1519 ordinal=1519 -->
## Functions

Functions

  • labview\examples\File IO\Configuration
   (INI)\Configuration (INI) File.lvproj
WriteWrite KeyKey (String)(String) VIVI

Writes a value to a key in a specified section of the configuration data identified by
refnum. This VI modifies data in memory. To write data to disk, use the Close Config
Data VI. Wire data to the value input to determine the polymorphic instance to use or
manually select the instance.

Format the content of an .ini file correctly when you use this VI.


Inputs/Outputs

   •      section —

    section is the name of the section in which to write the specified key.

   •     refnum —

    refnum is the reference number of the configuration data.

   •      key —

    key is the name of the key to write.

   •      value —

    value is the value of the key to write.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 1519

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1519 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1520 ordinal=1520 -->
## Functions

Functions

               •      write raw string? (F) —

            write raw string? specifies whether to write the string without escaping unprintable and
            backslash (\) characters.

                    If FALSE (default), the VI converts any backslashes (\) to double backslashes (\\) and replaces
           any remaining unprintable characters in the string, such as <ESC>, with a backslash and two
          Hex characters (\xx). If TRUE, the VI does not convert the unprintable characters in the string.

               •     refnum out —

          refnum out is the reference number of the configuration data.

               •      found? —

           found? is TRUE if the VI found the key in the specified section.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If key exists, the VI replaces the existing value. If key does not exist, the VI adds the
       key/value pair to the end of the specified section. If section does not exist, the VI adds
       section, with the key/value pair, to the end of the configuration data.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Configuration
        (INI)\Configuration (INI) File.lvproj
    WriteWrite KeyKey (U32)(U32) VIVI

       Writes a value to a key in a specified section of the configuration data identified by
      refnum. This VI modifies data in memory. To write data to disk, use the Close Config
      Data VI. Wire data to the value input to determine the polymorphic instance to use or
      manually select the instance.


1520   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1520 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1521 ordinal=1521 -->
## Functions

Functions

Format the content of an .ini file correctly when you use this VI.


Inputs/Outputs

   •      section —

    section is the name of the section in which to write the specified key.

   •     refnum —

    refnum is the reference number of the configuration data.

   •      key —

    key is the name of the key to write.

   •      value —

    value is the value of the key to write.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the reference number of the configuration data.

   •      found? —

    found? is TRUE if the VI found the key in the specified section.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1521

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1521 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1522 ordinal=1522 -->
## Functions

Functions

           If key exists, the VI replaces the existing value. If key does not exist, the VI adds the
       key/value pair to the end of the specified section. If section does not exist, the VI adds
       section, with the key/value pair, to the end of the configuration data.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Configuration
        (INI)\Configuration (INI) File.lvproj

     RemoveRemove KeyKey

      Removes a key in a specified section from the configuration data identified by refnum.


      Inputs/Outputs

               •      section —

            section is the name of the section from which to remove the specified key.

               •     refnum —

          refnum is the reference number of the configuration data.

               •      key —

           key is the name of the key to remove.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —


1522   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1522 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1523 ordinal=1523 -->
## Functions

Functions


    refnum out is the reference number of the configuration data.

   •      found? —

    found? is TRUE if the VI found the key in the specified section.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


RemoveRemove SectionSection

Removes a section from the configuration data identified by refnum.


Inputs/Outputs

   •      section —

    section is the name of the section to remove.

   •     refnum —

    refnum is the reference number of the configuration data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the reference number of the configuration data.

   •      section exists? —

    section exists? is TRUE if the VI found the specified section.


                                                    © National Instruments 1523

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1523 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1524 ordinal=1524 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      CloseClose ConfigConfig DataData

       Writes data to the platform-independent configuration file identified by refnum and
      then closes the reference to that file.


      Inputs/Outputs

               •     refnum —

          refnum is the reference number of the configuration data.

               •      write file if changed (T) —

            write file if changed (T) configures the VI to write the configuration data to the platform-
           independent configuration file you specify with the Open Config Data VI. You must set write file
                   if changed (T) to the default value of TRUE for the VI to write the configuration data. If the value
                is FALSE, the VI does not write the configuration data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

                    If an error occurs before this node executes, the node only closes the reference passed to it.

               •        file path —

                file path is the path to the configuration file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1524   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1524 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1525 ordinal=1525 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Configuration
   (INI)\Configuration (INI) File.lvproj

GetGet KeyKey NamesNames

Gets the names of all keys in the specified section from the configuration data
identified by refnum.

Format the content of an .ini file correctly when you use this VI.


Inputs/Outputs

   •      section —

    section is the name of the section from which to get the key names.

   •     refnum —

    refnum is the reference number of the configuration data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the reference number of the configuration data.

   •      section exists? —


                                                    © National Instruments 1525

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1525 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1526 ordinal=1526 -->
## Functions

Functions


            section exists? is TRUE if the VI found the specified section.

               •      key names —

           key names contains the names of all keys in the section, in the order in which they appear in the
                  file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      GetGet SectionSection NamesNames

       Gets the names of all sections from the configuration data identified by refnum.

      Format the content of an .ini file correctly when you use this VI.


      Inputs/Outputs

               •     refnum —

          refnum is the reference number of the configuration data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is the reference number of the configuration data.

               •      section names —

            section names contains the names of all sections in refnum.

               •       error out —

1526   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1526 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1527 ordinal=1527 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


NotNot AA ConfigConfig DataData RefnumRefnum

Determines whether a configuration data refnum is valid.

This VI considers a configuration data refnum to be invalid if you do not open the
reference with the Open Config Data VI, the file referenced does not exist, or the
reference is already closed when passed to this VI.


Inputs/Outputs

   •     refnum —

    refnum is the reference number of the configuration data.

   •      not a config data refnum —

    not a config data refnum is TRUE if refnum is not a valid configuration data refnum.

TDMTDM StreamingStreaming

Use the TDM Streaming VIs and functions to read and write waveforms and waveform
properties to binary measurement files (.tdms).

      Note Some functions on this palette do not work with real-time operating
       systems.

The VIs and functions on this palette can return TDM streaming error codes.


                                                    © National Instruments 1527

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1527 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1528 ordinal=1528 -->
## Functions

Functions


         Palette                     Description
        Object

                  Opens a .tdms file for reading or writing. You also can use this function to create a new      TDMS Open                              file or replace an existing file. Use the TDMS Close function to close the reference to         Function                     the file.

      TDMS Write  Streams data to the specified .tdms file. The data subset to write is determined by the
         Function    values you identify in the group name in and channel name(s) in inputs.

                   Reads the specified .tdms file and returns data in a format specified by the data type      TDMS Read                       input. If data has scaling information, this VI automatically scales the data. Use the         Function
                   count and offset inputs to read a specified subset of the data.

      TDMS Close                     Closes the .tdms file you opened with the TDMS Open function.         Function

      TDMS List                     Provides a list of group and channel names contained within the .tdms file specified in        Contents                     the .tdms file input.
         Function

                      Sets the properties of the specified .tdms file, channel group, or channel. If you wire
                     the group name and channel name inputs with values, the function writes the
                      properties at the channel level. Wiring only the group name input with a value writes
      TDMS Set                     the properties at the channel group level. If both group name and channel name         Properties                      inputs contain no values, the properties become file-specific. If you wire the channel
         Function                name input with a value, you must also wire a value to the group name input. You
                  must close the reference to the .tdms file or flush data to the .tdms file for changes to
                     take effect.

                     Returns the properties of the specified .tdms file, channel group, or channel. If you
                     wire the group name and channel name inputs with values, the function searches for
      TDMS Get    properties at the channel level. Wiring only the group name input with a value
         Properties   searches for properties at the channel group level. If both group name and channel
         Function   name inputs contain no values, the function searches for properties at the root level
                       of the .tdms file. If you wire the channel name input with a value, you must also wire a
                     value to the group name input.

                      Writes all buffers of the .tdms file data to the file identified by the tdms file input. Data
      TDMS Flush  written to a .tdms file often resides in a buffer until the buffer fills up or until you close
         Function    the file. This function forces the operating system to write any buffer data to the .tdms
                               file.

      TDMS File   Opens the .tdms file specified in the file in input and presents the file data in the
        Viewer     TDMS File Viewer dialog box.


1528   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1528 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1529 ordinal=1529 -->
## Functions

Functions


 Palette             Description
 Object

 TDMS            Defragments the .tdms file data specified in the file path input. Use this function to Defragment             clean up your .tdms data when it becomes cluttered, and increase performance. Function

            Use the Advanced TDMS VIs and functions to perform advanced file I/O operations,
            such as asynchronous reads and writes, on .tdms files. You can use these VIs and
 Advanced    functions to read data from an existing .tdms file, write data to a new .tdms file, or
 TDMS       replace subsets of data in an existing .tdms file. You also can use these VIs and
              functions to convert the file format version of a .tdms file or to create scaling
             information for unscaled data.


Unsupported Functions on Real-Time Operating Systems

The following functions on this palette do not work with real-time operating systems,
such as Phar Lap ETS, VxWorks, and NI Linux Real-Time:

  • TDMS Advanced Asynchronous Read
  • TDMS Advanced Asynchronous Read (Data Ref)
  • TDMS Advanced Asynchronous Write
  • TDMS Advanced Asynchronous Write (Data Ref)
  • TDMS Configure Asynchronous Reads
  • TDMS Configure Asynchronous Reads (Data Ref)
  • TDMS Configure Asynchronous Writes
  • TDMS Configure Asynchronous Writes (Data Ref)
  • TDMS File Viewer
  • TDMS Generate Random Data
  • TDMS Get Asynchronous Read Status
  • TDMS Get Asynchronous Read Status (Data Ref)
  • TDMS Get Asynchronous Write Status
  • TDMS Get Asynchronous Write Status (Data Ref)
  • TDMS Reserve File Size
  • TDMS Start Asynchronous Reads
  • TDMS Stop Asynchronous Reads


                                                    © National Instruments 1529

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1529 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1530 ordinal=1530 -->
## Functions

Functions

     TDMSTDMS OpenOpen FunctionFunction

      Opens a .tdms file for reading or writing. You also can use this function to create a new
          file or replace an existing file. Use the TDMS Close function to close the reference to the
          file.


      Inputs/Outputs

               •      create index file? (T) —

            create index file? specifies whether LabVIEW automatically generates a .tdms_index file for
            the corresponding .tdms file. This index file enables LabVIEW to speed up random access to the
         .tdms file. If you have limited disk space, wire a FALSE value to this input to prevent LabVIEW
           from generating the .tdms_index file. The default is TRUE.

           LabVIEW ignores this input if you open a .tdms file that already has a .tdms_index file.
            Wiring a FALSE value to this input does not remove this file. LabVIEW might update this file
            during the TDMS application to ensure this file is up-to-date. To remove this file, you can
           manually delete it from the disk or programmatically delete it by using the Delete function.

               Note If you use multiple TDMS Open functions, which have different values for the
                     create index file? input, to open the same .tdms file, LabVIEW uses the create index
                          file? input of the first TDMS Open function to determine whether to generate the
                .tdms_index file or not. LabVIEW ignores the create index file? input of all
                   subsequent TDMS Open functions.

          The .tdms_index file is optional in TDMS applications. When you distribute a TDMS
             application or .tdms file to another computer, you do not need to include the corresponding
         .tdms_index file. You can use this function to create a new .tdms_index file for your TDMS
             application if necessary.

               •        file format version (2.0) —


1530   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1530 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1531 ordinal=1531 -->
## Functions

Functions


   file format version specifies the file format version for the .tdms file.

  Refer to the following support document at ni.com for more information about the .tdms file
  format.

  0           1.0
               2.0  1                (default)

•        file path —

   file path specifies the absolute path to the file you want to open. If you use this function to
  create a new file, the file extension of the filename you specify in file path must be .tdms.
  Otherwise, this function automatically appends .tdms to the filename you specify. If you use
   this function to open or update an existing file, you do not have to ensure that the file extension
   is .tdms.

•      operation (0:open) —

  operation specifies the operation to perform.

  0 open (default)—Opens a .tdms file to write to.
  1 open or create—Creates a new .tdms file or opens an existing .tdms file to configure.
  2 create or replace—Creates a new .tdms file or replaces an existing .tdms file.
  3 create—Creates a new .tdms file.
  4 open (read-only)—Opens a read-only version of the .tdms file.

•      byte order (2:little-endian) —

  byte order specifies the byte order, or endian format, of the data in the .tdms file. Byte order
  specifies whether LabVIEW represents numeric values in memory from most significant byte to
  least significant byte or vice versa.

  The byte order input is valid only if you use this function to create a new .tdms file. If you use
   this function to read an existing .tdms file, LabVIEW reads data in the byte order of that file and
  represents the data in the native byte order of the host computer. If you use this function to
  update an existing .tdms file, LabVIEW writes data in the byte order of that file.

   big-endian, network order—Specifies that the most significant byte occupies the lowest
  0
   memory address.


                                                   © National Instruments 1531

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1531 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1532 ordinal=1532 -->
## Functions

Functions


           1 native, host order—Specifies that this function uses the byte order of the host computer.
               little-endian (default)—Specifies that the least significant byte occupies the lowest memory           2              address.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      disable buffering? (T) —

            disable buffering? (Windows) specifies whether LabVIEW opens, creates, or replaces a .tdms
                 file without system buffering. The default is TRUE, which means this function disables system
             buffering and enables buffering in the TDMS disk cache.

             Disabling system buffering can speed up data transfers in certain situations. If you have a small
          amount of data to transfer, you might not notice a difference if you disable system buffering. To
            read or write a data file to a Redundant Array of Independent Disks (RAID), consider opening the
                 file without system buffering to speed up data transfers. To read the same set of data repeatedly
           from the computer, consider enabling system buffering.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Standard Read and Write\
        TDMS Read Events Data.vi
            • labview\examples\File IO\TDMS\Concurrent Access to TDMS
        File.vi


1532   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1532 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1533 ordinal=1533 -->
## Functions

Functions

TDMSTDMS WriteWrite FunctionFunction

Streams data to the specified .tdms file. The data subset to write is determined by the
values you identify in the group name in and channel name(s) in inputs.


Inputs/Outputs

   •      data layout (0:decimated) —

    data layout specifies the arrangement of the data that you want to stream to a .tdms file. You
    must use the same data layout for each channel under the same group.


     decimated (default)—Specifies that the input data prioritizes channels before samples. This
     arrangement first lists all samples from the first channel, then all samples from the second
      channel, and so on through the last channel. The following table shows a typical example of
     the

     decimated
     data layout.

    0
     Channel 0—Sample 1
     Channel 0—Sample 2
          ...
     Channel 0—Sample N
     Channel 1—Sample 1
     Channel 1—Sample 2
          ...


                                                    © National Instruments 1533

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1533 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1534 ordinal=1534 -->
## Functions

Functions


            Channel 1—Sample N
            Channel 2—Sample 1
            Channel 2—Sample 2
                         ...
            Channel 2—Sample N


              interleaved—Specifies that the input data prioritizes samples before channels. This
            arrangement lists the first sample from every channel, then the second sample from every
              channel, and so on through the last sample from every channel. The following table shows a
               typical example of the

              interleaved
             data layout.

            Channel 0—Sample 1
           1 Channel 1—Sample 1
            Channel 2—Sample 1
            Channel 0—Sample 2
            Channel 1—Sample 2
            Channel 2—Sample 2
                         ...
            Channel 0—Sample N
            Channel 1—Sample N
            Channel 2—Sample N


               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Open function to open the refnum.

               •      group name in (Untitled) —

           group name in specifies the channel group on which to perform the operation. The default is
          Untitled.

               •      channel name(s) in (Untitled) —


1534   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1534 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1535 ordinal=1535 -->
## Functions

Functions


  channel name(s) in indicates the channels on which to perform the operation. If you do not wire
  data to this input, LabVIEW names the channels automatically. If you wire waveform data to the
  data input, LabVIEW uses waveform names. The data type that the channel name(s) in input
  accepts can be a string or a 1D array of strings. The data type varies according to the data you
  wire to the data input.

                                                          1D Array of
  String          String or 1D Array of Strings                                                                             Strings

              1D array of:                                                      Digital waveform
                             • Signed or unsigned integers
                             •  Floating-point numbers                                    Digital table
                             • Timestamps
                             • Booleans                                    1D array of analog
                                                                 waveforms
                   Note  Analog                                                            2D array of:
  waveform
                                          If data layout is decimated and you wire a 1D
                                                                                                                • Signed or                           array of strings to channel name(s) in, this VI uses  1D array of                                                                         unsigned                         the first element of the 1D array as the channel  alphanumeric                                                                                    integers                      name.   strings that do                                                                                                                •  Floating-
  not contain null                                                                               point                                          If data layout is interleaved and you wire a string  characters                                                                  numbers                           to channel name(s) in, this VI uses this string as
                                                                                                                • Timestamps                         the channel name of the first element in the 1D
                                                                                                                • Booleans                           array and uses Untitled, Untitled1,
                                                                                                                • Alphanumeric                       Untitled2...as the channel names of the rest
                                                                                        strings that                          elements.
                                                                do not
                                                                              contain null
                                                                                 characters

   If the data input contains compressed digital data, you must enter the name of the compression
  channel as the first entry in the channel name(s) in array.

•      data —

  data is the data to write to the .tdms file.

  This input accepts the following data types:

      • Analog waveform or a 1D array of analog waveforms
      •  Digital waveform

                                                   © National Instruments 1535

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1535 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1536 ordinal=1536 -->
## Functions

Functions


                   Caution When you write analog or digital waveforms to a new channel,
                      LabVIEW includes the timestamp information in the waveforms. However, when
                      you append analog or digital waveforms to an existing channel, LabVIEW might
                          discard the timestamp information in the new waveforms.

                     •  Digital table
                     • Dynamic data
                     • 1D or 2D array of:
        ◦ Signed or unsigned integers
        ◦  Floating-point numbers, including the following specific data types:
         ▪  Single-precision and double-precision floating-point numbers
         ▪ Complex single-precision and double-precision floating-point numbers
         ▪ (Windows) Extended-precision floating-point numbers
        ◦ Timestamps
        ◦ Booleans
        ◦ Alphanumeric strings that do not contain null characters
               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •      group name out —

           group name out returns the name of the channel group on which you performed the operation.

               •      channel name(s) out —

           channel name(s) out returns the channel name on which you performed the operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.


1536   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1536 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1537 ordinal=1537 -->
## Functions

Functions

  • labview\examples\File IO\TDMS\Standard Read and Write\
   TDMS Write Events Data.vi
  • labview\examples\File IO\TDMS\Standard Read and Write\
   TDMS Write Time Domain Data.vi
  • labview\examples\File IO\TDMS\Standard Read and Write\
   TDMS Write Triggered Data.vi
  • labview\examples\File IO\TDMS\Concurrent Access to TDMS
   File.vi

TDMSTDMS ReadRead FunctionFunction

Reads the specified .tdms file and returns data in a format specified by the data type
input. If data has scaling information, this VI automatically scales the data. Use the
count and offset inputs to read a specified subset of the data.


Inputs/Outputs

   •      count (-1: all) —

    count specifies the maximum number of data elements to read from the .tdms file for each
    channel. The default is –1, all available elements.

   •       offset (0) —

     offset specifies the number of data elements into the .tdms file at which the function begins
    reading the .tdms file. The default is 0.

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Open function to open the refnum.

   •      group name in —

                                                    © National Instruments 1537

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1537 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1538 ordinal=1538 -->
## Functions

Functions


           group name in specifies the channel group on which to perform the operation.

                    If you do not wire data to this input, the following behavior occurs:

                     • LabVIEW reads data from the current group in the file. The current group is either the first
               group in the file when you run this function for the first time or the nth group at the nth
                 cycle when you run this function continuously for multiple cycles.
                     • The order that the TDMS Read function reads groups is the same order that the TDMS List
                Contents function returns groups.
                     •  After LabVIEW reaches the last group, if the TDMS Read function attempts to run, LabVIEW
                 returns an end of file error.

               Note The TDMS List Contents function and the TDMS Get Properties function will
                       reset the current group to the first group in the file. Resetting the current group to the
                             first group in the file impacts the group read by the next TDMS Read function when
                  you do not wire the group name in input.

               •      channel name(s) in —

           channel name(s) in indicates the channel to perform the operation on. If you do not wire data to
              this input, LabVIEW reads data from all channels under the same group. If you wire waveform
            data to the data type input, LabVIEW uses waveform names. The data type that the channel
           name(s) in input accepts can be a string or a 1D array of strings. The data type varies according
             to the data you wire to the data type input.

             String                               1D Array of Strings

                                                                   Digital waveform

           Analog waveform                                 Digital table

          1D array of:                            1D array of analog waveforms

                     • Signed or unsigned integers            2D array of:
                     •  Floating-point numbers
                     • Timestamps                                              • Signed or unsigned integers
                     • Booleans                                                  •  Floating-point numbers
                     • Alphanumeric strings that do not contain       • Timestamps
                  null characters                                          • Booleans
                                                                                       • Alphanumeric strings that do not contain
                                                                     null characters


1538   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1538 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1539 ordinal=1539 -->
## Functions

Functions


   If you load a complete file or group that contains compressed digital data, LabVIEW
  automatically inserts the compression channel name in the channel name(s) in array. If you load
  a subset of a file or group that contains compressed digital data, you must enter the name of the
  compression channel as the first entry in the channel name(s) in array.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      data type —

  data type is the type of data that you want data to contain.

  This input accepts the following data types:
      • Analog waveform or a 1D array of analog waveforms
      •  Digital waveform
      •  Digital table
      • Dynamic data
      • 1D or 2D array of:
   ◦ Signed or unsigned integers
   ◦  Floating-point numbers, including the following specific data types:
     ▪  Single-precision and double-precision floating-point numbers
     ▪ Complex single-precision and double-precision floating-point numbers
     ▪ (Windows) Extended-precision floating-point numbers
   ◦ Timestamps
   ◦ Booleans
   ◦ Alphanumeric strings that do not contain null characters
•      return channels in file order? (F) —

  return channels in file order? specifies whether this function returns data channels in the same
  order as they exist in the .tdms file. If the value is TRUE or if you do not specify the channel
  name(s) in input, this function returns data channels in the same order as they exist in the
  .tdms file. If the value is FALSE, this function returns data channels in the same order as you
  specify in the channel name(s) in input. The default is FALSE.

•     tdms file out —

  tdms file out returns a TDMS file reference to the .tdms file on which you performed the
  operation.

•      group name out —


                                                   © National Instruments 1539

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1539 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1540 ordinal=1540 -->
## Functions

Functions


           group name out returns the name of the channel group on which you performed the operation.

               •      channel name(s) out —

           channel name(s) out returns the channel name on which you performed the operation.

               •      data —

           data contains the data read from the file in the specified data type. It can consist of any data
            type depending on which data type you specify in data type and how count is set.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     end of file? —

          end of file? indicates if the end of the file has been reached.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Standard Read and Write\
        TDMS Read Events Data.vi
            • labview\examples\File IO\TDMS\Concurrent Access to TDMS
        File.vi

     TDMSTDMS CloseClose FunctionFunction

       Closes the .tdms file you opened with the TDMS Open function.


      Inputs/Outputs

               •     tdms file —


1540   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1540 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1541 ordinal=1541 -->
## Functions

Functions


   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Open function to open the refnum.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •        file path out —

      file path out returns the path of the .tdms file on which you performed the operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


(VxWorks) LabVIEW loads the shared TDMS component into memory when you open a
TDMS file. LabVIEW unloads this component from memory when you close all TDMS
files. On the VxWorks operating system, unloading the TDMS component from memory
will leak approximately 1.8 kilobytes of memory due to a known issue of VxWorks. You
can follow the guidelines below to avoid memory leak in your application.

  • Avoid opening and closing TDMS files unnecessarily on VxWorks.
  • Open an additional TDMS file at the beginning of the application and keep it open
    until the application completes all TDMS reading and writing. This workaround will
   keep the TDMS component in memory while you frequently open and close other
   TDMS files.
  • Set the TDMS component as a startup component on your RT target. To do this,
   add tdms.out; to the StartupDLLs section of ni-rt.ini, which is located in
   the root directory of your target (c:\ni-rt.ini), then restart the target. This
    will prevent the TDMS component from being unloaded from memory when you
    close TDMS files.

For information on how to access files such as ni-rt.ini on your RT target, refer to
the KnowledgeBase on ni.com.


                                                    © National Instruments 1541

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1541 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1542 ordinal=1542 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Standard Read and Write\
        TDMS Read Events Data.vi
            • labview\examples\File IO\TDMS\Concurrent Access to TDMS
        File.vi

     TDMSTDMS ListList ContentsContents FunctionFunction

       Provides a list of group and channel names contained within the .tdms file specified in
       the .tdms file input.


      Inputs/Outputs

               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Open function to open the refnum.

               •      group name —

           group name indicates the channel group to analyze. If this input is not wired, the function
           performs the operation on all channel and group names.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •      group names —

1542   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1542 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1543 ordinal=1543 -->
## Functions

Functions


    group names lists the names of the channel groups in the specified .tdms file.

   •      group/channel names —

    group/channel names lists the names of the channel groups and their associated channels in
    the specified .tdms file.

       If the group name input is wired, group/channel names returns the channel names within the
     specified group.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


TDMSTDMS SetSet PropertiesProperties FunctionFunction

Sets the properties of the specified .tdms file, channel group, or channel. If you wire
the group name and channel name inputs with values, the function writes the
properties at the channel level. Wiring only the group name input with a value writes
the properties at the channel group level. If both group name and channel name
inputs contain no values, the properties become file-specific. If you wire the channel
name input with a value, you must also wire a value to the group name input. You
must close the reference to the .tdms file or flush data to the .tdms file for changes to
take effect.


Inputs/Outputs

   •      property values —

    property values specifies the property values of the specified channel group, channel, or .tdms
      file. This input accepts the following data types:

         • Signed or unsigned integers
         •  Floating-point numbers, including the following specific data types:

                                                    © National Instruments 1543

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1543 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1544 ordinal=1544 -->
## Functions

Functions

        ◦  Single-precision and double-precision floating-point numbers
        ◦ Complex single-precision and double-precision floating-point numbers
        ◦ (Windows) Extended-precision floating-point numbers
                     • Timestamps
                     • Booleans
                     • Alphanumeric strings that do not contain null characters
                     •  Variants that contain any of the data types specified above

                    If you want to set more than one property using the same function, you can wire a 1D array of
           any of the previously specified data types to the property values input. Each value in the array
            corresponds to a single property. However, a single property cannot hold an array of values.

               •      property names —

            property names specifies the property names of the specified channel group, channel, or
         .tdms file.

               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Open function to open the refnum.

               •      group name —

           group name specifies the channel group to perform the operation on. If you wire a value to the
           channel name input, you must also wire a value to this input.

               •      channel name —

           channel name specifies the channel to perform the operation on. If you wire a value to this
             input, you must also wire a value to the group name input.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •      group name out —


1544   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1544 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1545 ordinal=1545 -->
## Functions

Functions


    group name out returns the name of the channel group on which you performed the operation.

   •      channel name out —

    channel name out returns the name of the channel on which you performed the operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This section lists all properties that you might encounter when you use a .tdms file.
The first table lists all properties you might find in a .tdms file. The second table lists
all properties that do not exist in a .tdms file but which you can use to perform
certain actions. You can write these properties as waveform attributes to a .tdms file.
However, some of these properties might not appear as waveform attributes when you
read the waveform data from the .tdms file. The Available as a Waveform Attribute?
column provides information about whether a property is available as a waveform
attribute. If the data type of a property is not valid, LabVIEW treats the property as a
customized property and the property will not perform as described in the table.

You can use the TDMS Get Properties function to obtain the values of these properties.
Use the TDMS Set Properties function to change the values of these properties.

The following table lists all properties you might find in a .tdms file.


                                                      Available  Available
                                                          in File    as a
 Property Name                Data Type  Access                       Description
                                              Format   Waveform
                                                    Versions  Attribute?

                                                                                Specifies the object name,
                                         Read/                      such as the root name, group
 name                             String               2.0       Yes                                               write                     name, or channel name, in a
                                                        .tdms file.

                                                                               Indicates the index of a
                                    32-bit                                                                column in a 2D array. This
                                signed     Read   1.0 and NI_ArrayColumn                                 No         property appears in a .tdms                                   integer     only    2.0
                                                                                                        file only if you write a 2D                              numeric
                                                                              array of data to the file.

                                                    © National Instruments 1545

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1545 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1546 ordinal=1546 -->
## Functions

Functions


                                                               Available  Available
                                                                  in File    as a        Property Name                Data Type  Access                       Description                                                    Format   Waveform
                                                            Versions  Attribute?

                                             64-bit                                                                               Represents the number of
                                      unsigned   Read   1.0 and       NI_ChannelLength                                         Yes        values in a channel of a                                            integer     only    2.0                                                              .tdms file.                                     numeric

                                                                               Represents the data type of a
                                                                                  channel. The value is an
                                                                                        integer that corresponds to a
                                                                        LabVIEW type code.

                                                                   Note A .tdms file
                                                                                       uses a different
                                                                                        type code than
                                                                                         the LabVIEW type
                                                                                 code for the
                                                                                               following data
                                                                                                 types:

                                                                                                                                             •  String: 0x20
                                             16-bit                                                                                                                                             • Boolean:
                                      unsigned   Read   1.0 and                                                                                          0x21       NI_DataType                                                Yes                                            integer     only    2.0                                                                                                                                             • Time
                                     numeric                                                                                            stamp:
                                                                                          0x44
                                                                                                                                             •  Fixed-point
                                                                                     number:
                                                                                          0x4F
                                                                                                                                             •  Single-
                                                                                                           precision,
                                                                                                                floating-
                                                                                                  point
                                                                               number
                                                                                               with units:
                                                                                          0x19
                                                                                                                                             • Complex
                                                                                                              single-


1546   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1546 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1547 ordinal=1547 -->
## Functions

Functions


                                                      Available  Available
                                                         in File    as aProperty Name                Data Type  Access                       Description                                             Format   Waveform
                                                    Versions  Attribute?


                                                                                                 precision,
                                                                                                      floating-
                                                                                         point
                                                                              number:
                                                                                  0x08000c
                                                                                                                                • Complex
                                                                                     double-
                                                                                                 precision,
                                                                                                      floating-
                                                                                         point
                                                                              number:
                                                                                0x10000d
                                                                                                                                • DAQmx raw
                                                                                              data:
                                                                                 0xFFFFFFFF

                                                                                 For the full list of
                                                             TDMS data type
                                                                                  codes, refer to the
                                                                             Data Type Values
                                                                                     section in TDMS
                                                                                                   File Format
                                                                                          Internal Structure.


                                                                               Indicates whether a digital
                                                                              table is compressed or not. A
                                                                          value of 1 indicates that the
                                      Read   1.0 and
NI_DigitalCompression    Boolean                 No          digital table is compressed. If                                            only    2.0
                                                                        the digital table is not
                                                                    compressed, this property
                                                                  does not appear.

                                    32-bit
                               signed     Read   1.0 and                Indicates the index of a row
NI_DigitalLine                                 No                                   integer     only    2.0                     in a digital table.
                             numeric

                                                    © National Instruments 1547

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1547 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1548 ordinal=1548 -->
## Functions

Functions


                                                               Available  Available
                                                                  in File    as a        Property Name                Data Type  Access                       Description                                                    Format   Waveform
                                                            Versions  Attribute?

                                             32-bit
                                        signed     Read   1.0 and                Indicates the number of rows
       NI_DigitalNumberOfLines                        No                                            integer     only    2.0                     in a digital table.
                                     numeric

                                                                                         Specifies the number of
                                                                                       scales to use when you read
                                                                               data from a .tdms file. For
                                                                              example, if a .tdms file has
                                             32-bit                                                                                                   five scales and you set the                                      unsigned   Read/
       NI_Number_Of_Scales                             2.0      No         value of                                            integer      write
                                                              NI_Number_Of_Scales                                     numeric
                                                                                     to 4, LabVIEW applies only
                                                                                the first four scales to the
                                                                               data when you read the
                                                              .tdms file.

                                                                                         Specifies the scaling
                                                                                  information for the data in a
                                                              .tdms file. You can create
                                                                   more than one scale in a
                                                              .tdms file.
       NI_Scale[n]_config, where
    nrepresents the order of the                Read/                        Note National                                     N/A                  2.0      No
         scale and configrepresents the               write                                 Instruments
         configuration of the scale.                                                recommends you
                                                                                    use the TDMS
                                                                                           Create Scaling
                                                                                          Information VI to
                                                                                               create scales.


                                                                                         Specifies whether LabVIEW
                                                                                       scales data when reading the
                                                                               data from a .tdms file. If the
                                                 Read/       NI_Scaling_Status          String               2.0      No         value is unscaled and the                                                        write
                                                              .tdms file contains one or
                                                                   more scales, LabVIEW scales
                                                                                the data. If the value is


1548   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1548 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1549 ordinal=1549 -->
## Functions

Functions


                                                      Available  Available
                                                         in File    as aProperty Name                Data Type  Access                       Description                                             Format   Waveform
                                                    Versions  Attribute?

                                                            scaled, LabVIEW does not
                                                                              scale the data. For DAQmx
                                                                       data channels, LabVIEW
                                                                    cannot return unscaled data
                                                                  even when
                                                       NI_Scaling_Status is
                                                           unscaled.

                                         Read/   1.0 and                Specifies the unit of the
unit_string                   String                   No                                               write   2.0                  channel data in a .tdms file.

                                                                       Represents the increment
                                         Read/   1.0 andwf_increment               Double                  No       between two consecutive                                               write   2.0
                                                                   samples on the x-axis.

                                                                       Represents the number of
                                    32-bit                                samples in the first data
                               signed     Read/   1.0 and             chunk of the waveform you
wf_samples                                     No                                   integer      write   2.0                    write to a .tdms file. The
                             numeric                                  value must be greater than
                                                                                 zero.

                                                                   Frequency-domain data and
                                      Read   1.0 and              histogram results use this
wf_start_offset           Double                  No                                            only    2.0                   value as the first value on the
                                                                                   x-axis.

                                                                       Represents the time at which
                                                                        the waveform was acquired
                                                                          or generated. This property
                                      Read   1.0 and
wf_start_time             Timestamp               No        can be zero if the time                                            only    2.0
                                                                         information is relative or the
                                                               waveform is not in time
                                                                   domain.

                                                                               Indicates whether LabVIEW
                                      Read   1.0 and                interprets the x-axis data inwf_time_pref                  String                   No
                                            only    2.0                   absolute time or relative
                                                                             time.

wf_xname                       String      Read   1.0 and   No         Indicates the name of the


                                                    © National Instruments 1549

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1549 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1550 ordinal=1550 -->
## Functions

Functions


                                                               Available  Available
                                                                  in File    as a        Property Name                Data Type  Access                       Description                                                    Format   Waveform
                                                            Versions  Attribute?
                                                     only    2.0                    x-axis of the waveform.

                                             Read   1.0 and                Indicates the unit text of the
       wf_xunit_string             String                   No                                                     only    2.0                     x-axis.

        In addition to the properties in the table above, a .tdms file might also contain other
      waveform attributes.

      The following table lists all properties that do not exist in a .tdms file, but you can use
      them to perform certain actions.


                                                                        Available  Available
                                        Data                        in File    as a        Property Name                              Unit    Access                       Description
                                      Type                   Format   Waveform
                                                                     Versions  Attribute?

                                                                                 You can use the
                                                                    NI_DiskCacheSiz
                                                                                   improve the .tdms d
                                                                                    performance by alloca
                                                                           amount of cache size
                                                                                         the data. LabVIEW wri
                                                                                        data in bytes per file. T
                                                                                                                           is valid only when the
                                                32-bit                                            buffering? input of the
                                         unsigned         Read/                        function is TRUE. The       NI_DiskCacheSize                       Byte             2.0       Yes
                                               integer             write                            for this property is app
                                        numeric                                  MB. Wire a different va
                                                                                       property values input
                                                                                           Set Properties functio
                                                                                         the cache size. A great
                                                                                         the NI_DiskCacheS
                                                                                          property usually can i
                                                                                                  writing performance;
                                                                                                greater value also requ
                                                                                 computer resources.


1550   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1550 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1551 ordinal=1551 -->
## Functions

Functions


                                                               Available  Available
                                Data                        in File    as aProperty Name                              Unit    Access                       Description                              Type                   Format   Waveform
                                                             Versions  Attribute?

                                                                         You can use the
                                                              NI_DiskGapSize p
                                                                           improve the .tdms d
                                                                            performance when rea
                                                                                  discontinuous data. T
                                                                                             valid only when the di
                                                                                     buffering? input of the
                                                                                     function is TRUE. The
                                                              NI_DiskGapSize p
                                                                                    multiple of the sector
                                                                                             local hard disk. The de
                                                                                               for this property is 10.
                                                                        gap in the .tdms file
                                                                                 the value of the
                                                              NI_DiskGapSize p
                                                              TDMS Read function c
                                                                                data from the file at on
                                       32-bit                                         data gap in the .tdms
                                 unsigned         Read/                      than the value of the
NI_DiskGapSize                         Byte             2.0       Yes                                     integer             write                  NI_DiskGapSize p
                                numeric                              TDMS Read function re
                                                                                   piece of data one at a
                                                                                     function finishes read
                                                                                Wire a value to the pro
                                                                                   input of the TDMS Set
                                                                                     function to change the

                                                                   Note Obtain
                                                                                        optimal read
                                                                                                  writing perfo
                                                                                                         trial-and-err
                                                                              The same co
                                                                                   might not re
                                                                         same optima
                                                                                    performance
                                                                                                       different com
                                                                                   might need t


                                                    © National Instruments 1551

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1551 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1552 ordinal=1552 -->
## Functions

Functions


                                                                        Available  Available
                                        Data                        in File    as a        Property Name                              Unit    Access                       Description                                      Type                   Format   Waveform
                                                                     Versions  Attribute?


                                                                                                   property val
                                                                                              deploy an ap
                                                                                          from one com
                                                                                                       another.


                                                64-bit                                     You can use the
                                           signed           Read                  NI_InMemoryFile
       NI_InMemoryFileSize                   Byte             2.0       Yes                                               integer            only                         property to return the
                                        numeric                              .tdms file in memory

                                                                                 You can use the
                                                                    NI_InMemoryWrit
                                                                                          property to allocate th
                                                                                                        in memory for writing
                                                                                                 default value for this p
                                                                               MB. The value range fo
                                                64-bit                                          property is [1 KB, 1 GB
                                           signed           Read/                        value for this property       NI_InMemoryWriteBlockSize           Byte             2.0       Yes                                               integer             write                      improve the in-memo
                                        numeric                                     performance by alloca
                                                                                                 blocks; however, a gre
                                                                                               also requires more com
                                                                                                resources. You must se
                                                                                          property before the w
                                                                                                begins. Otherwise, Lab
                                                                              an error.

                                                                                 You can use the
                                                                    NI_MinimumBuffe
                                                                                          property to improve th
                                                                                        data writing performa
                                                32-bit
                                                                                               to a file less often. This
                                         unsigned Data    Read/   1.0 and
       NI_MinimumBufferSize                                             Yes        reduce the size of a .t                                               integer   sample  write   2.0
                                                                                                   controlling the numbe                                        numeric
                                                                                        data is written to disk.
                                                                    NI_MinimumBuffe
                                                                                          property is valid only i
                                                                                             layout input of the TD

1552   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1552 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1553 ordinal=1553 -->
## Functions

Functions


                                                               Available  Available
                                Data                        in File    as aProperty Name                              Unit    Access                       Description                              Type                   Format   Waveform
                                                             Versions  Attribute?

                                                                                     function is decimated
                                                                                 the value of the
                                                              NI_MinimumBuffe
                                                                                  property is zero. If you
                                                                                          at the group level, this
                                                                                          sets the value of unde
                                                                               channels whose value
                                                                                          set the value at the file
                                                                                     function also sets the
                                                                                  underlying groups and
                                                                    whose value is zero. U
                                                                                  property and the
                                                              NI_DiskCacheSiz
                                                                                              affects file buffering w

                                                                         You can use the TDMS
                                                                                      Properties function to
                                                                             groups and channels i
                                                                                                                  files. Wire
                                                              NI_UpdateGroupN
                                                                               property names input
                                                                                      to rename a group and
                                                              NI_UpdateChanne
                                                                               property names input
NI_UpdateChannelName                                                       Write   1.0 and               to rename a channel. W                                      String    N/A                       Yes
                                                     only    2.0                 group or channel namNI_UpdateGroupName
                                                                               property values input
                                                                           group or channel nam
                                                                       want to replace to the
                                                                                    or channel name inpu
                                                                             groups or channels yo
                                                                         group name or chann
                                                                               not exist, LabVIEW cre
                                                                             groups or channels wi
                                                                         names.


                                                    © National Instruments 1553

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1553 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1554 ordinal=1554 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Standard Read and Write\
        TDMS Write Time Domain Data.vi

     TDMSTDMS GetGet PropertiesProperties FunctionFunction

       Returns the properties of the specified .tdms file, channel group, or channel. If you
       wire the group name and channel name inputs with values, the function searches for
       properties at the channel level. Wiring only the group name input with a value
       searches for properties at the channel group level. If both group name and channel
     name inputs contain no values, the function searches for properties at the root level of
       the .tdms file. If you wire the channel name input with a value, you must also wire a
       value to the group name input.


      Inputs/Outputs

               •      data type —

           data type controls the data type of the property values or property value output.

             This input accepts the following data types:

           Data Type                                                                 Default Value
           Signed or unsigned integer                                            0
             Single-precision or double-precision floating-point number                 0
          Complex single-precision or double-precision floating-point number         0+0i
           (Windows) Extended-precision floating-point number                      0
           Alphanumeric string that does not contain null characters                 Empty string


1554   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1554 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1555 ordinal=1555 -->
## Functions

Functions


  Data Type                                                                 Default Value
  Timestamp                                                                 00:00:00.000
  Boolean                                                           FALSE
  Variant that contains any of the data types specified above                 Empty variant

  To return more than one property using the same function, you can wire a 1D array of any of the
  previously specified data types to the data type input. Each value in the array corresponds to a
  single property. However, a single property cannot hold an array of values.

•      property name —

  property name specifies the name of the property whose values you want to get. If you do not
  wire this input, this function returns the property names and their property values for the
  specified group name, channel name, or the entire .tdms file. If you wire this input, the
  property value output replaces property values and returns the value of the specified property;
  the found output replaces property names and returns TRUE. If the specified property does not
   exist in the .tdms file, the property value output returns the default value of the specified data
  type and the found output returns FALSE.

•     tdms file —

  tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
  the TDMS Open function to open the refnum.

•      group name —

  group name specifies the channel group to perform the operation on. If you wire a value to the
  channel name input, you must also wire a value to this input.

•      channel name —

  channel name specifies the channel to perform the operation on. If you wire a value to this
  input, you must also wire a value to the group name input.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     tdms file out —

  tdms file out returns a TDMS file reference to the .tdms file on which you performed the
  operation.


                                                   © National Instruments 1555

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1555 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1556 ordinal=1556 -->
## Functions

Functions

               •      group name out —

           group name out returns the name of the channel group on which you performed the operation.

               •      channel name out —

           channel name out returns the name of the channel on which you performed the operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      property values —

            property values returns the property values of the specified channel group, channel, or .tdms
                  file. This output is available only if the property name input is not wired.

          The data type of this parameter is determined by the data type input.
               •      property value —

            property value replaces the property values output and returns the property value of the
             specified property. This output is available only if the property name input is wired.

          The data type of this parameter is determined by the data type input.
               •      property names —

            property names returns the property names of the specified channel group, channel, or .tdms
                  file. This output is available only if the property name input is not wired.

               •      found — found replaces the property names output and indicates whether the specified
            property exists in the .tdms file or not. This output is available only if the property name input
                is wired.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Concurrent Access to TDMS
        File.vi

     TDMSTDMS FlushFlush FunctionFunction

       Writes all buffers of the .tdms file data to the file identified by the tdms file input. Data

1556   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1556 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1557 ordinal=1557 -->
## Functions

Functions

written to a .tdms file often resides in a buffer until the buffer fills up or until you close
the file. This function forces the operating system to write any buffer data to the .tdms
file.

      Note Flushing data too frequently might negatively impact the writing
       performance of your application.


Inputs/Outputs

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Open function to open the refnum.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Flush Written TDMS Data.vi


                                                    © National Instruments 1557

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1557 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1558 ordinal=1558 -->
## Functions

Functions

     TDMSTDMS FileFile ViewerViewer

      Opens the .tdms file specified in the file in input and presents the file data in the TDMS
        File Viewer dialog box.


      Inputs/Outputs

               •        file in —

                file in is the absolute path to the file you want to open.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •        file out —

                file out returns file in unchanged.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Standard Read and Write\
        TDMS Write Events Data.vi
            • labview\examples\File IO\TDMS\Standard Read and Write\
        TDMS Write Triggered Data.vi

     TDMSTDMS DefragmentDefragment FunctionFunction

      Defragments the .tdms file data specified in the file path input. Use this function to

1558   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1558 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1559 ordinal=1559 -->
## Functions

Functions

clean up your .tdms data when it becomes cluttered, and increase performance.


Inputs/Outputs

   •        file path —

      file path is the path to the .tdms file you want to defragment.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


AdvancedAdvanced TDMSTDMS

Use the Advanced TDMS VIs and functions to perform advanced file I/O operations,
such as asynchronous reads and writes, on .tdms files. You can use these VIs and
functions to read data from an existing .tdms file, write data to a new .tdms file, or
replace subsets of data in an existing .tdms file. You also can use these VIs and
functions to convert the file format version of a .tdms file or to create scaling
information for unscaled data.

      Note Use the standard TDMS VIs and functions when the features of the
       Advanced TDMS VIs and functions are not necessary. Incorrect use of the
       Advanced TDMS VIs and functions might result in a corrupt .tdms file. If you
        disable buffering when using the Advanced TDMS VIs and functions, the data
         size you read or write must be a multiple of the sector size of the hard disk.

The VIs and functions on this palette can return TDM streaming error codes.


                                                    © National Instruments 1559

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1559 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1560 ordinal=1560 -->
## Functions

Functions


         Palette                       Description        Object

                    Opens a .tdms file for reading or writing in the byte order of the host computer. You
      TDMS                         also can use this function to create a new file or replace an existing file. Unlike the        Advanced                 TDMS Open function, the TDMS Advanced Open function does not create a       Open                       .tdms_index file. If you use this function to open an existing .tdms file that has a         Function                       corresponding .tdms_index file, this function removes the .tdms_index file.

      TDMS
        Advanced      Closes the .tdms file that you opened with the TDMS Advanced Open function and
         Close          releases extra disk space that the TDMS Reserve File Size function reserves.
         Function

      TDMS Set
                        Defines the channel information of the raw data that you want to write to the        Channel                         specified .tdms file. The channel information includes the data layout, name of the         Information
                       group, names of the channels, data type, and number of samples.         Function

                        Creates scaling information for unscaled data in a .tdms file. This VI writes the
                         scaling information to the .tdms file. You must manually select the polymorphic      TDMS Create
                        instance to use.         Scaling
         Information                     To call this VI with TDMS Advanced functions, only call the TDMS Set Channel
                       Information function after any calls to this VI.

      TDMS Delete
                        Deletes data from a channel or multiple channels in a group.
        Data Function

      TDMS Set
                       Configures the offset at which the TDMS Advanced Asynchronous Write or TDMS
        Next Write
                     Advanced Synchronous Write function starts overwriting the existing data in a .tdms
         Position
                                  file.
         Function

      TDMS Set
        Next Read     Configures the offset at which the TDMS Advanced Asynchronous Read function
         Position        starts reading data from a .tdms file.
         Function

      TDMS Reserve  Pre-allocates disk space for writing and prevents fragmentation on a file-system
           File Size         level. If you are running this function on Windows with User Account Control


1560   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1560 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1561 ordinal=1561 -->
## Functions

Functions


 Palette                Description
 Object

               enabled, you must run LabVIEW or the application with administrator privileges to Function               avoid a run-time error.

               Converts the file format version of a .tdms file from 1.0 to 2.0 or vice versa. This VI
 TDMS Convert  overwrites the .tdms file with the new file format version you specify in the target
 Format        version input. This VI also changes the byte order of the .tdms file to native, host
                 order.

 TDMS
 Advanced     Use the TDMS Advanced Synchronous I/O functions to synchronously read data
 Synchronous  from or write data to .tdms files.
 I/O

 TDMS
 Advanced     Use the TDMS Advanced Asynchronous I/O functions to asynchronously read data
 Asynchronous from or write data to .tdms files.
 I/O

             Use the TDMS Advanced Data Reference I/O functions to interact with data that is
            owned by a component external to LabVIEW, such as the direct memory access TDMS
              (DMA) buffer of a device driver that controls a data-streaming device. You can use Advanced               these functions to asynchronously write data from the DMA buffer of a device driver Data
                to .tdms files without needing to copy the data into a LabVIEW array first. You also Reference I/O              can use these functions to asynchronously read data from .tdms files and place the
               data directly into the DMA buffer.


 TDMS In      Use the TDMS In Memory functions to open, close, read from, and write to .tdms
 Memory         files in memory.

TDMSTDMS AdvancedAdvanced OpenOpen FunctionFunction

Opens a .tdms file for reading or writing in the byte order of the host computer. You
also can use this function to create a new file or replace an existing file. Unlike the
TDMS Open function, the TDMS Advanced Open function does not create a
.tdms_index file. If you use this function to open an existing .tdms file that has a

                                                    © National Instruments 1561

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1561 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1562 ordinal=1562 -->
## Functions

Functions

       corresponding .tdms_index file, this function removes the .tdms_index file.


      Inputs/Outputs

               •        file path —

                file path specifies the absolute path to the file you want to open. If you use this function to
             create a new file, the file extension of the filename you specify in file path must be .tdms.
            Otherwise, this function automatically appends .tdms to the filename you specify. If you use
              this function to open or update an existing file, you do not have to ensure that the file extension
                is .tdms.

               •      operation (0:open) —

            operation specifies the operation to perform.

           0 open (default)—Opens a .tdms file to write to.
           1 open or create—Creates a new .tdms file or opens an existing .tdms file to configure.
           2 create or replace—Creates a new .tdms file or replaces an existing .tdms file.
           3 create—Creates a new .tdms file.
           4 open (read-only)—Opens a read-only version of the .tdms file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      disable buffering? (T) —

            disable buffering? (Windows) specifies whether LabVIEW opens, creates, or replaces a .tdms
                 file without system buffering. The default is TRUE, which means this function disables system
              buffering. If the value is TRUE, the size of data to read or write must be a multiple of the sector
             size of the hard disk.

             Disabling system buffering can speed up data transfers in certain situations. If you have a small
          amount of data to transfer, you might not notice a difference if you disable buffering. To read or


1562   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1562 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1563 ordinal=1563 -->
## Functions

Functions


    write a data file to a Redundant Array of Independent Disks (RAID), consider opening the file
    without buffering to speed up data transfers. To read the same set of data repeatedly from the
    computer, consider enabling buffering.

   •      enable asynchronous? (T) —

    enable asynchronous? (Windows) specifies whether to enable asynchronous reads or writes for
    the .tdms file. Set the value to TRUE if you want to use the TDMS Advanced Asynchronous I/O
    or TDMS Advanced Data Reference I/O functions. Set the value to FALSE if you want to use the
   TDMS Advanced Synchronous I/O functions. The default is TRUE.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •      sector size —

    sector size returns the sector size of the hard disk. (macOS/Linux/RT targets) sector size is not
    supported and returns a value of zero.

          Note Traditionally, the sector size of hard disks is 512 bytes. In recent years, the
              sector size is 4096 bytes for large hard disks and RAID arrays.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The byte order, or endian format, specifies whether LabVIEW represents numeric
values in memory from most significant byte to least significant byte or vice versa.

      Note Use this function to open a .tdms file with a file format version of 2.0.
       To open a version 1.0 file, use the TDMS Open function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Advanced Read and Write\

                                                    © National Instruments 1563

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1563 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1564 ordinal=1564 -->
## Functions

Functions

        Asynchronous Read and Write\TDMS Advanced Asynchronous
        Write.vi
            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Basic
        Asynchronous Read.vi
   TDMSTDMS AdvancedAdvanced CloseClose FunctionFunction

       Closes the .tdms file that you opened with the TDMS Advanced Open function and
       releases extra disk space that the TDMS Reserve File Size function reserves.


      Inputs/Outputs

               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Advanced Open function to open the refnum.

               •      truncate file? (F) —

            truncate file? specifies whether to truncate the .tdms file when closing this file. If the value is
           TRUE, this function truncates the file at the current writing position. If the value is FALSE, this
             function does not truncate the file and only releases extra disk space that the TDMS Reserve File
             Size function reserves. The default is FALSE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (10 s) —

           timeout specifies the maximum time, in seconds, that this function waits for pending
           asynchronous writes to complete before closing the .tdms file. If you do not wire data to the
           timeout input, this function sets the value to 10. This input is valid only if the enable


1564   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1564 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1565 ordinal=1565 -->
## Functions

Functions


    asynchronous? input of the TDMS Advanced Open function is TRUE.

   •        file path out —

      file path out returns the path of the .tdms file on which you performed the operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Advanced Read and Write\
   Asynchronous Read and Write\TDMS Advanced Asynchronous
   Write.vi
  • labview\examples\File IO\TDMS\Advanced Read and Write\
   Asynchronous Read and Write\TDMS Advanced Basic
   Asynchronous Read.vi
TDMSTDMS SetSet ChannelChannel InformationInformation FunctionFunction

Defines the channel information of the raw data that you want to write to the specified
.tdms file. The channel information includes the data layout, name of the group,
names of the channels, data type, and number of samples.

      Note If you use this function multiple times in an application, the order in
       which you use this function determines the order of channels and groups
        that you write to a .tdms file.


                                                    © National Instruments 1565

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1565 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1566 ordinal=1566 -->
## Functions

Functions


      Inputs/Outputs

               •      data layout (0:non-interleaved) —

           data layout specifies the arrangement of the data that you want to stream to a .tdms file. You
          must use the same data layout for each channel under the same group.


             non-interleaved (default)—Specifies that the input data prioritizes channels before samples.
              This arrangement first lists all samples from the first channel, then all samples from the second
              channel, and so on through the last channel. The following table shows a typical example of
             the non-interleaved data layout.

            Channel 0—Sample 1
            Channel 0—Sample 2
                         ...
            Channel 0—Sample N           0
            Channel 1—Sample 1
            Channel 1—Sample 2
                         ...
            Channel 1—Sample N
            Channel 2—Sample 1
            Channel 2—Sample 2
                         ...
            Channel 2—Sample N


              interleaved—Specifies that the input data prioritizes samples before channels. This
            arrangement lists the first sample from every channel, then the second sample from every
           1
              channel, and so on through the last sample from every channel. The following table shows a
               typical example of the interleaved data layout.


1566   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1566 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1567 ordinal=1567 -->
## Functions

Functions


   Channel 0—Sample 1
   Channel 1—Sample 1
   Channel 2—Sample 1
   Channel 0—Sample 2
   Channel 1—Sample 2
   Channel 2—Sample 2
      ...
   Channel 0—Sample N
   Channel 1—Sample N
   Channel 2—Sample N


•     tdms file —

  tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
  the TDMS Advanced Open function to open the refnum.

•      group name (Untitled) —

  group name specifies the group name for the channel. If you do not wire data to this input or if
  you wire an empty string to this input, this function uses Untitled as the group name.

•      channel name(s) —

  channel name(s) specifies the names for the channels.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      data type —

  data type specifies the type of data on which you want to perform the operation. This input
  accepts integers, floating-point numbers, Booleans, and timestamps.

        Note You can wire the following floating-point numbers to this input:
                      •  Single-precision and double-precision floating-point numbers
                      • Complex single-precision and double-precision floating-point numbers
                      • (Windows) Extended-precision floating-point numbers


                                                   © National Instruments 1567

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1567 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1568 ordinal=1568 -->
## Functions

Functions

               •      samples per channel —

           samples per channel specifies the number of data samples that each channel contains.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following use cases demonstrate how the TDMS Set Channel Information function
       arranges raw data according to the data layout input.

      Single Group, Single Channel (Non-Interleaved)


      The data layout in the file is consecutive samples per channel. In the previous figure, a
       single 16-bit numeric or I16 sample follows another I16 sample, which follows another
       I16 sample, and so on. You can write as many I16 samples as you want. For example,
      you can write one million I16 samples or two million I16 samples at a time.

      Single Group, Multiple Channels (Non-Interleaved)


1568   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1568 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1569 ordinal=1569 -->
## Functions

Functions

The data layout is 8 consecutive samples per channel. In the previous figure, the data
layout is eight I16 samples for the ch0 channel, eight I16 samples for the ch1 channel,
and so on.

Single Group, Multiple Channels (Interleaved)


In the previous figure, the data layout is an I16 sample for the ch0 channel followed by
an I16 sample for the ch1 channel. This pair repeats in the file. The total file size or the
NI_ChannelLength property determines how often the pair repeats.

Multiple Group, Multiple Channels (Non-Interleaved)


The data layout is 8 consecutive samples per channel per group or device. In the
previous figure, the data layout contains eight I16 samples for the ch0 channel for
device1, eight I16 samples for the ch1 channel for device1, eight I16 samples for
the ch0 channel for device2, eight I16 samples for the ch1 channel for device2,
and so on.


                                                    © National Instruments 1569

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1569 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1570 ordinal=1570 -->
## Functions

Functions

      Multiple Group, Multiple Channels (Interleaved)


        In the previous figure, the data layout is 8 pairs of an I16 sample for the ch0 channel
      and an I16 sample for the ch1 channel of device1. Following the 8 pairs is 8 pairs of
      an I16 sample for the ch0 channel and an I16 sample for the ch1 channel of
      device2. This pattern repeats in the file.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Append Multiple
        Headers.vi
   TDMSTDMS CreateCreate ScalingScaling InformationInformation

       Creates scaling information for unscaled data in a .tdms file. This VI writes the scaling
       information to the .tdms file. You must manually select the polymorphic instance to
       use.

      To call this VI with TDMS Advanced functions, only call the TDMS Set Channel
       Information function after any calls to this VI.

      Use the TDMS File Viewer VI to retrieve the scaling information from a .tdms file.

           Note This VI does not scale strings or complex floating-point numbers.


1570   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1570 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1571 ordinal=1571 -->
## Functions

Functions


  • TDMS Create Scaling Information (Linear) VI
  • TDMS Create Scaling Information (Polynomial) VI
  • TDMS Create Scaling Information (Thermocouple) VI
  • TDMS Create Scaling Information (RTD) VI
  • TDMS Create Scaling Information (Table) VI
  • TDMS Create Scaling Information (Strain) VI
  • TDMS Create Scaling Information (Thermistor) VI
  • TDMS Create Scaling Information (Reciprocal) VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Scale TDMS Data.vi
TDMSTDMS CreateCreate ScalingScaling InformationInformation (Linear)(Linear) VIVI

Creates scaling information for unscaled data in a .tdms file. This VI writes the scaling
information to the .tdms file. You must manually select the polymorphic instance to
use.

To call this VI with TDMS Advanced functions, only call the TDMS Set Channel
Information function after any calls to this VI.

Use the TDMS File Viewer VI to retrieve the scaling information from a .tdms file.

      Note This VI does not scale strings or complex floating-point numbers.


                                                    © National Instruments 1571

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1571 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1572 ordinal=1572 -->
## Functions

Functions

      Inputs/Outputs

               •       linear scale —

             linear scale specifies the linear scaling information. A linear scale uses the equation y=mx+b,
           where xis a pre-scaled value, and yis a scaled value.

                     •      slope —

                slope specifies the slope, or min the equation, for the scale. The default is 0.

                     •      y intercept —

               y intercept specifies the yintercept, or bin the equation, for the scale. The default is 0.

                     •      input source —

                input source specifies the ID of the child scale. If the current scale has a child scale, you can
                wire the scale ID of the child scale to this input. The default is –1, which specifies that the
                 current scale does not have a child scale.


               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Open function to open the refnum. group name and channel name take precedence
            over this input. If you specify a value for either group name or channel name, this VI applies the
             scaling information to either the group or the channel, respectively. If you do not specify a value
              for them, this VI applies the scaling information to the .tdms data.

               •      group name —

           group name specifies the group name for the .tdms data. This input takes precedence over
          tdms file but has a lower priority than channel name.

               •      channel name —

           channel name specifies the channel name for the .tdms data. This input takes precedence over
           group name and tdms file. If you do not specify a value for channel name, this VI applies the
             scaling information to the group. If you do not specify a value for group name either, this VI
             applies the scaling information to the .tdms data.

               •       error in (no error) —


1572   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1572 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1573 ordinal=1573 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •      group name out —

    group name out returns the name of the channel group on which you performed the operation.

   •      channel name out —

    channel name out returns the name of the channel on which you performed the operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •       scale ID —

    scale ID returns the ID of the resulting scale.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Scale TDMS Data.vi
TDMSTDMS CreateCreate ScalingScaling InformationInformation
(Polynomial)(Polynomial) VIVI

Creates scaling information for unscaled data in a .tdms file. This VI writes the scaling
information to the .tdms file. You must manually select the polymorphic instance to
use.

To call this VI with TDMS Advanced functions, only call the TDMS Set Channel

                                                    © National Instruments 1573

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1573 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1574 ordinal=1574 -->
## Functions

Functions

       Information function after any calls to this VI.

      Use the TDMS File Viewer VI to retrieve the scaling information from a .tdms file.

           Note This VI does not scale strings or complex floating-point numbers.


      Inputs/Outputs

               •      polynomial scale —

           polynomial scale specifies the polynomial scaling information. A polynomial scale uses an nth-
            order polynomial equation.

                     •       coefficients —

                  coefficients specifies the coefficients for the scale that converts pre-scaled values to scaled
                  values. Each element of the array corresponds to a term of the equation.

                For example, if index three of the array is 9, the fourth term of the equation is 9x3.

                     •      input source —

                input source specifies the ID of the child scale. If the current scale has a child scale, you can
                wire the scale ID of the child scale to this input. The default is –1, which specifies that the
                 current scale does not have a child scale.


               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Open function to open the refnum. group name and channel name take precedence
            over this input. If you specify a value for either group name or channel name, this VI applies the
             scaling information to either the group or the channel, respectively. If you do not specify a value
              for them, this VI applies the scaling information to the .tdms data.


1574   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1574 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1575 ordinal=1575 -->
## Functions

Functions

   •      group name —

    group name specifies the group name for the .tdms data. This input takes precedence over
   tdms file but has a lower priority than channel name.

   •      channel name —

    channel name specifies the channel name for the .tdms data. This input takes precedence over
    group name and tdms file. If you do not specify a value for channel name, this VI applies the
     scaling information to the group. If you do not specify a value for group name either, this VI
    applies the scaling information to the .tdms data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •      group name out —

    group name out returns the name of the channel group on which you performed the operation.

   •      channel name out —

    channel name out returns the name of the channel on which you performed the operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •       scale ID —

    scale ID returns the ID of the resulting scale.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Scale TDMS Data.vi

                                                    © National Instruments 1575

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1575 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1576 ordinal=1576 -->
## Functions

Functions

   TDMSTDMS CreateCreate ScalingScaling InformationInformation
   (Thermocouple)(Thermocouple) VIVI

       Creates scaling information for unscaled data in a .tdms file. This VI writes the scaling
       information to the .tdms file. You must manually select the polymorphic instance to
       use.

      To call this VI with TDMS Advanced functions, only call the TDMS Set Channel
       Information function after any calls to this VI.

      Use the TDMS File Viewer VI to retrieve the scaling information from a .tdms file.

           Note This VI does not scale strings or complex floating-point numbers.


      Inputs/Outputs

               •      thermocouple scale —

           thermocouple scale specifies the thermocouple scaling information, which scales the .tdms
            data from microvolts to degrees Celsius.

                    If the data is not in microvolts, first convert the data to microvolts with an additional scale. For
            example, you can use the TDMS Create Scaling Information (Linear) instance VI to convert the
             data.

                     •      thermocouple type —

               thermocouple type specifies the type of thermocouple connected to the channel.
              Thermocouple types differ in composition and measurement range.


1576   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1576 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1577 ordinal=1577 -->
## Functions

Functions


      10047    B—Specifies the B-type thermocouple.
      10055    E—Specifies the E-type thermocouple.
      10072    J (default)—Specifies the J-type thermocouple.
      10073    K—Specifies the K-type thermocouple.
      10077    N—Specifies the N-type thermocouple.
      10082    R—Specifies the R-type thermocouple.
      10085    S—Specifies the S-type thermocouple.
      10086    T—Specifies the T-type thermocouple.

      •      input source —

      input source specifies the ID of the child scale. If the current scale has a child scale, you can
      wire the scale ID of the child scale to this input. The default is –1, which specifies that the
       current scale does not have a child scale.


•     tdms file —

  tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
  the TDMS Open function to open the refnum. group name and channel name take precedence
  over this input. If you specify a value for either group name or channel name, this VI applies the
  scaling information to either the group or the channel, respectively. If you do not specify a value
  for them, this VI applies the scaling information to the .tdms data.

•      group name —

  group name specifies the group name for the .tdms data. This input takes precedence over
  tdms file but has a lower priority than channel name.

•      channel name —

  channel name specifies the channel name for the .tdms data. This input takes precedence over
  group name and tdms file. If you do not specify a value for channel name, this VI applies the
  scaling information to the group. If you do not specify a value for group name either, this VI
  applies the scaling information to the .tdms data.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     tdms file out —

                                                   © National Instruments 1577

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1577 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1578 ordinal=1578 -->
## Functions

Functions


          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •      group name out —

           group name out returns the name of the channel group on which you performed the operation.

               •      channel name out —

           channel name out returns the name of the channel on which you performed the operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •       scale ID —

             scale ID returns the ID of the resulting scale.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Scale TDMS Data.vi
   TDMSTDMS CreateCreate ScalingScaling InformationInformation (RTD)(RTD) VIVI

       Creates scaling information for unscaled data in a .tdms file. This VI writes the scaling
       information to the .tdms file. You must manually select the polymorphic instance to
       use.

      To call this VI with TDMS Advanced functions, only call the TDMS Set Channel
       Information function after any calls to this VI.

      Use the TDMS File Viewer VI to retrieve the scaling information from a .tdms file.

           Note This VI does not scale strings or complex floating-point numbers.


1578   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1578 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1579 ordinal=1579 -->
## Functions

Functions


Inputs/Outputs

   •     RTD scale —

   RTD scale specifies the resistance temperature detector (RTD) scaling information, which scales
    the .tdms data in degrees Celsius.

         •      current excitation —

        current excitation specifies, in amperes, the amount of excitation that the sensor requires.
         Refer to the sensor documentation to determine this value.

         •      r0 nominal resistance —

         r0 nominal resistance specifies the sensor resistance, in ohms, at 0 degrees Celsius. The
        Callendar-Van Dusen equation requires this value. Refer to the sensor documentation to
        determine this value.

         •      a —

       a specifies the acoefficient for the Callendar-Van Dusen equation. Refer to the sensor
        documentation to determine this value.

         •     b —

       b specifies the bcoefficient for the Callendar-Van Dusen equation. Refer to the sensor
        documentation to determine this value.

         •      c —

        c specifies the ccoefficient for the Callendar-Van Dusen equation. Refer to the sensor
        documentation to determine this value.

         •      lead wire resistance —


                                                    © National Instruments 1579

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1579 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1580 ordinal=1580 -->
## Functions

Functions


                lead wire resistance specifies the amount of resistance in ohms in the lead wires. Ideally,
                   this value is the same for all leads.

                     •       resistance configuration —

                 resistance configuration specifies the number of wires to use for resistance measurements.

               2 2-Wire (default)—Specifies the 2-wire mode.
               3 3-Wire—Specifies the 3-wire mode.
               4 4-Wire—Specifies the 4-wire mode.

                     •      input source —

                input source specifies the ID of the child scale. If the current scale has a child scale, you can
                wire the scale ID of the child scale to this input. The default is –1, which specifies that the
                 current scale does not have a child scale.


               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Open function to open the refnum. group name and channel name take precedence
            over this input. If you specify a value for either group name or channel name, this VI applies the
             scaling information to either the group or the channel, respectively. If you do not specify a value
              for them, this VI applies the scaling information to the .tdms data.

               •      group name —

           group name specifies the group name for the .tdms data. This input takes precedence over
          tdms file but has a lower priority than channel name.

               •      channel name —

           channel name specifies the channel name for the .tdms data. This input takes precedence over
           group name and tdms file. If you do not specify a value for channel name, this VI applies the
             scaling information to the group. If you do not specify a value for group name either, this VI
             applies the scaling information to the .tdms data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


1580   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1580 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1581 ordinal=1581 -->
## Functions

Functions


    standard error in functionality.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •      group name out —

    group name out returns the name of the channel group on which you performed the operation.

   •      channel name out —

    channel name out returns the name of the channel on which you performed the operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •       scale ID —

    scale ID returns the ID of the resulting scale.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Scale TDMS Data.vi
TDMSTDMS CreateCreate ScalingScaling InformationInformation (Table)(Table) VIVI

Creates scaling information for unscaled data in a .tdms file. This VI writes the scaling
information to the .tdms file. You must manually select the polymorphic instance to
use.

To call this VI with TDMS Advanced functions, only call the TDMS Set Channel
Information function after any calls to this VI.

Use the TDMS File Viewer VI to retrieve the scaling information from a .tdms file.

                                                    © National Instruments 1581

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1581 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1582 ordinal=1582 -->
## Functions

Functions

           Note This VI does not scale strings or complex floating-point numbers.


      Inputs/Outputs

               •       table scale —

            table scale specifies the table scaling information. A table scale maps an array of pre-scaled
            values to an array of corresponding scaled values.

                     •      scaled values —

                scaled values specifies the scaled values that map to the values in pre-scaled values.

                     •      pre-scaled values —

                pre-scaled values specifies the pre-scaled values that map to the values in scaled values.

                     •      input source —

                input source specifies the ID of the child scale. If the current scale has a child scale, you can
                wire the scale ID of the child scale to this input. The default is –1, which specifies that the
                 current scale does not have a child scale.


               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Open function to open the refnum. group name and channel name take precedence
            over this input. If you specify a value for either group name or channel name, this VI applies the
             scaling information to either the group or the channel, respectively. If you do not specify a value
              for them, this VI applies the scaling information to the .tdms data.

               •      group name —

           group name specifies the group name for the .tdms data. This input takes precedence over


1582   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1582 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1583 ordinal=1583 -->
## Functions

Functions


   tdms file but has a lower priority than channel name.

   •      channel name —

    channel name specifies the channel name for the .tdms data. This input takes precedence over
    group name and tdms file. If you do not specify a value for channel name, this VI applies the
     scaling information to the group. If you do not specify a value for group name either, this VI
    applies the scaling information to the .tdms data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •      group name out —

    group name out returns the name of the channel group on which you performed the operation.

   •      channel name out —

    channel name out returns the name of the channel on which you performed the operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •       scale ID —

    scale ID returns the ID of the resulting scale.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Scale TDMS Data.vi


                                                    © National Instruments 1583

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1583 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1584 ordinal=1584 -->
## Functions

Functions

   TDMSTDMS CreateCreate ScalingScaling InformationInformation (Strain)(Strain) VIVI

       Creates scaling information for unscaled data in a .tdms file. This VI writes the scaling
       information to the .tdms file. You must manually select the polymorphic instance to
       use.

      To call this VI with TDMS Advanced functions, only call the TDMS Set Channel
       Information function after any calls to this VI.

      Use the TDMS File Viewer VI to retrieve the scaling information from a .tdms file.

           Note This VI does not scale strings or complex floating-point numbers.


      Inputs/Outputs

               •       strain scale —

             strain scale specifies the strain scaling information, which scales the .tdms data in strains.
             Strain is the amount of deformation of a body due to an applied force. Specifically, strain is the
              fractional change in length.

                     •      configuration —

                 configuration specifies the bridge configuration for the strain gages.

               10183                Full Bridge I (default)
               10184                Full Bridge II
               10185                Full Bridge III
               10188              Half Bridge I
               10189              Half Bridge II


1584   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1584 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1585 ordinal=1585 -->
## Functions

Functions


  10271             Quarter Bridge I
  10272             Quarter Bridge II

•      Poisson ratio —

  Poisson ratio specifies the ratio of lateral strain to axial strain in the material you are
  measuring.

•      gage resistance —

  gage resistance specifies the resistance, in ohms, of the gages in an unstrained position.
  Each gage in the bridge must have the same nominal gage resistance. The resistance across
  arms of the bridge that do not have strain gages also must be the same as the nominal gage
  resistance. Refer to the sensor documentation to determine this value.

•      lead wire resistance —

  lead wire resistance specifies the amount of resistance in ohms in the lead wires. Ideally,
   this value is the same for all leads.

•        initial bridge voltage —

   initial bridge voltage specifies in volts the output voltage of the bridge in the unloaded
  condition. This VI subtracts this value from any measurements before applying scaling
  equations. Perform a voltage measurement on the bridge with no strain applied to
  determine this value.

•      gage factor —

  gage factor specifies the sensitivity of the strain gages and relates the change in electrical
  resistance to the change in strain. Each gage in the bridge must have the same gage factor.
  Refer to the sensor documentation to determine this value.

•      voltage excitation —

  voltage excitation specifies in volts the amount of excitation that the sensor requires. Refer
  to the sensor documentation to determine this value.

•      input source —

  input source specifies the ID of the child scale. If the current scale has a child scale, you can


                                                © National Instruments 1585

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1585 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1586 ordinal=1586 -->
## Functions

Functions


                wire the scale ID of the child scale to this input. The default is –1, which specifies that the
                 current scale does not have a child scale.


               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Open function to open the refnum. group name and channel name take precedence
            over this input. If you specify a value for either group name or channel name, this VI applies the
             scaling information to either the group or the channel, respectively. If you do not specify a value
              for them, this VI applies the scaling information to the .tdms data.

               •      group name —

           group name specifies the group name for the .tdms data. This input takes precedence over
          tdms file but has a lower priority than channel name.

               •      channel name —

           channel name specifies the channel name for the .tdms data. This input takes precedence over
           group name and tdms file. If you do not specify a value for channel name, this VI applies the
             scaling information to the group. If you do not specify a value for group name either, this VI
             applies the scaling information to the .tdms data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •      group name out —

           group name out returns the name of the channel group on which you performed the operation.

               •      channel name out —

           channel name out returns the name of the channel on which you performed the operation.

               •       error out —

1586   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1586 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1587 ordinal=1587 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

   •       scale ID —

    scale ID returns the ID of the resulting scale.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Scale TDMS Data.vi
TDMSTDMS CreateCreate ScalingScaling InformationInformation
(Thermistor)(Thermistor) VIVI

Creates scaling information for unscaled data in a .tdms file. This VI writes the scaling
information to the .tdms file. You must manually select the polymorphic instance to
use.

To call this VI with TDMS Advanced functions, only call the TDMS Set Channel
Information function after any calls to this VI.

Use the TDMS File Viewer VI to retrieve the scaling information from a .tdms file.

      Note This VI does not scale strings or complex floating-point numbers.


                                                    © National Instruments 1587

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1587 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1588 ordinal=1588 -->
## Functions

Functions

      Inputs/Outputs

               •      thermistor scale —

            thermistor scale specifies the thermistor scaling information, which scales the .tdms data in
              Kelvin.

                     •       resistance configuration —

                 resistance configuration specifies the number of wires to use for resistance measurements.

               2 2-Wire (default)—Specifies the 2-wire mode.
               3 3-Wire—Specifies the 3-wire mode.
               4 4-Wire—Specifies the 4-wire mode.

                     •       excitation type —

                 excitation type specifies the type of excitation for the scale.

               10122      Voltage (default)—Voltage excitation.
               10334      Current—Current excitation.

                     •       excitation value —

                 excitation value specifies the amount of excitation that the sensor requires. When
                 excitation type is Current, the unit of excitation value is amperes. When excitation type is
                 Voltage, the unit of excitation value is volts. Refer to the sensor documentation to
               determine this value.

                     •      r1 reference resistance —

                 r1 reference resistance specifies, in ohms, the value of the reference resistor.

                     •      lead wire resistance —

                lead wire resistance specifies the amount of resistance in ohms in the lead wires. Ideally,
                   this value is the same for all leads.

                     •      a —

              a specifies the aconstant for the Steinhart-Hart thermistor equation. Refer to the sensor


1588   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1588 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1589 ordinal=1589 -->
## Functions

Functions


      documentation to determine the value for this constant.

      •     b —

     b specifies the bconstant for the Steinhart-Hart thermistor equation. Refer to the sensor
      documentation to determine the value for this constant.

      •      c —

      c specifies the cconstant for the Steinhart-Hart thermistor equation. Refer to the sensor
      documentation to determine the value for this constant.

      •      input source —

      input source specifies the ID of the child scale. If the current scale has a child scale, you can
      wire the scale ID of the child scale to this input. The default is –1, which specifies that the
       current scale does not have a child scale.


•     tdms file —

  tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
  the TDMS Open function to open the refnum. group name and channel name take precedence
  over this input. If you specify a value for either group name or channel name, this VI applies the
  scaling information to either the group or the channel, respectively. If you do not specify a value
  for them, this VI applies the scaling information to the .tdms data.

•      group name —

  group name specifies the group name for the .tdms data. This input takes precedence over
  tdms file but has a lower priority than channel name.

•      channel name —

  channel name specifies the channel name for the .tdms data. This input takes precedence over
  group name and tdms file. If you do not specify a value for channel name, this VI applies the
  scaling information to the group. If you do not specify a value for group name either, this VI
  applies the scaling information to the .tdms data.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides


                                                   © National Instruments 1589

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1589 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1590 ordinal=1590 -->
## Functions

Functions


            standard error in functionality.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •      group name out —

           group name out returns the name of the channel group on which you performed the operation.

               •      channel name out —

           channel name out returns the name of the channel on which you performed the operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •       scale ID —

             scale ID returns the ID of the resulting scale.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Scale TDMS Data.vi
   TDMSTDMS CreateCreate ScalingScaling InformationInformation
    (Reciprocal)(Reciprocal) VIVI

       Creates scaling information for unscaled data in a .tdms file. This VI writes the scaling
       information to the .tdms file. You must manually select the polymorphic instance to
       use.

      To call this VI with TDMS Advanced functions, only call the TDMS Set Channel
       Information function after any calls to this VI.

1590   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1590 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1591 ordinal=1591 -->
## Functions

Functions

Use the TDMS File Viewer VI to retrieve the scaling information from a .tdms file.

      Note This VI does not scale strings or complex floating-point numbers.


Inputs/Outputs

   •       reciprocal scale —

    reciprocal scale specifies the reciprocal scaling information. A reciprocal scale divides the
   number 1 by an input value. If the input value is zero, this VI uses zero as the reciprocal.

         •      input source —

        input source specifies the ID of the child scale. If the current scale has a child scale, you can
        wire the scale ID of the child scale to this input. The default is –1, which specifies that the
         current scale does not have a child scale.


   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Open function to open the refnum. group name and channel name take precedence
    over this input. If you specify a value for either group name or channel name, this VI applies the
     scaling information to either the group or the channel, respectively. If you do not specify a value
     for them, this VI applies the scaling information to the .tdms data.

   •      group name —

    group name specifies the group name for the .tdms data. This input takes precedence over
   tdms file but has a lower priority than channel name.

   •      channel name —

    channel name specifies the channel name for the .tdms data. This input takes precedence over


                                                    © National Instruments 1591

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1591 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1592 ordinal=1592 -->
## Functions

Functions


           group name and tdms file. If you do not specify a value for channel name, this VI applies the
             scaling information to the group. If you do not specify a value for group name either, this VI
             applies the scaling information to the .tdms data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •      group name out —

           group name out returns the name of the channel group on which you performed the operation.

               •      channel name out —

           channel name out returns the name of the channel on which you performed the operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •       scale ID —

             scale ID returns the ID of the resulting scale.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Scale TDMS Data.vi
   TDMSTDMS DeleteDelete DataData FunctionFunction

       Deletes data from a channel or multiple channels in a group.


1592   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1592 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1593 ordinal=1593 -->
## Functions

Functions

      Note This function does not support digital data or DAQmx raw data.


Inputs/Outputs

   •      count (-1: all) —

    count specifies the number of data samples to delete from the .tdms file for each channel. The
     default is -1, which means this function deletes all data samples from the position you specify in
    from.

       If the value of count is out of range for a channel, this function automatically sets count to the
   number of data samples in that channel.

   •      from (0: start) —

    from specifies from where to delete data samples from the .tdms file for each channel.

    0 start (default)—Specifies to delete data samples from the beginning of each channel.
    1 end—Specifies to delete data samples from the end of each channel.

   •        file path —

      file path is the absolute path to the file you want to open.

   •      group name in —

    group name in specifies the channel group on which to perform the operation.

   •      channel name(s) in —

    channel name(s) in specifies the channel to perform the operation on. If you do not wire data to
     this input, LabVIEW performs the operation on all channels under the same group.

   •       error in (no error) —


                                                    © National Instruments 1593

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1593 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1594 ordinal=1594 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      keep empty group/channel? (T) —

           keep empty group/channel? specifies whether to keep the group or channels in the .tdms file
                    if the group or channels are empty after this function deletes data samples. The default is TRUE,
           which means this function keeps the empty group or channels.

               •        file path out —

                file path out returns the path of the .tdms file on which you performed the operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When the data you wire contains waveform data, LabVIEW sets the following channel
       properties and waveform attributes:

            •  If the waveform attribute NI_ExpXDimension represents time or if this attribute
         does not exist, LabVIEW sets the following values:
     ◦ wf_start_offset = wf_start_offset + count * wf_increment
     ◦  If the waveform attribute NI_ExpTimeStamp exists, LabVIEW sets
          NI_ExpTimeStamp = NI_ExpTimeStamp + count * 1/wf_increment
            •  If the waveform attribute NI_ExpXDimension represents frequency, LabVIEW
           sets the following values:
     ◦ wf_start_offset = wf_start_offset + count * 1/wf_increment
     ◦  If the waveform attribute NI_ExpTimeStamp exists, LabVIEW sets
          NI_ExpTimeStamp = NI_ExpTimeStamp + count * 1/wf_increment
            • After this function deletes data, if the number of data samples in the .tdms file is
            less than the value of the channel property wf_samples, LabVIEW sets the value
           of wf_samples to equal the number of data samples in the .tdms file.

     Examples

       Refer to the following example files included with LabVIEW.


1594   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1594 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1595 ordinal=1595 -->
## Functions

Functions

  • labview\examples\File IO\TDMS\TDMS Delete Data from
   Channels.vi
TDMSTDMS SetSet NextNext WriteWrite PositionPosition FunctionFunction

Configures the offset at which the TDMS Advanced Asynchronous Write or TDMS
Advanced Synchronous Write function starts overwriting the existing data in a .tdms
file.

      Note Overwriting existing data from the middle of a file might result in a
        corrupt final file. National Instruments recommends that you truncate the file
      when you finish writing, or make sure you overwrite the entire remainder of
       the file. Use the truncate file? input of the TDMS Advanced Close function to
        truncate a .tdms file.


Inputs/Outputs

   •      channel name in —

    channel name in specifies the channel on which to perform the operation.

   •      group name in —

    group name in specifies the group on which to perform the operation.

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Advanced Open function to open the refnum.

   •       offset (0) —


                                                    © National Instruments 1595

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1595 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1596 ordinal=1596 -->
## Functions

Functions


             offset specifies how far in the raw data from the location specified by from to set the file
             position. The default is 0. If the disable buffering? input of the TDMS Advanced Open function is
           TRUE, the next write position you set must be a multiple of the sector size of the hard disk.

               •      from (0:start) —

           from specifies where to set the file position in the raw data based on the offset.

               start (default)—Sets the file position offset samples from the beginning of the raw data in the
           0 .tdms file. If the value of from is 0, the value of offset must be equal to or greater than 0,
            which sets the file position at the beginning of the raw data.
            end—Sets the file position offset samples from the end of the raw data in the .tdms file. If the
           1 value of from is 1, the value of offset must be equal to or less than 0, which sets the file
              position at the end of the raw data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Overwrite.vi
            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Ring Buffer.vi


1596   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1596 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1597 ordinal=1597 -->
## Functions

Functions

TDMSTDMS SetSet NextNext ReadRead PositionPosition FunctionFunction

Configures the offset at which the TDMS Advanced Asynchronous Read function starts
reading data from a .tdms file.


Inputs/Outputs

   •      channel name in —

    channel name in specifies the channel on which to perform the operation.

   •      group name in —

    group name in specifies the group on which to perform the operation.

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Advanced Open function to open the refnum.

   •       offset (0) —

     offset specifies how far in the raw data from the location specified by from to set the file
     position. The default is 0. If the disable buffering? input of the TDMS Advanced Open function is
    TRUE, the next read position you set must be a multiple of the sector size of the hard disk.

   •      from (0: start) —

    from specifies where to set the file position in the raw data based on the offset.

      start (default)—Sets the file position offset samples from the beginning of the raw data in the
    0 .tdms file. If the value of from is 0, the value of offset must be equal to or greater than 0,
     which sets the file position at the beginning of the raw data.
    1 end—Sets the file position offset samples from the end of the raw data in the .tdms file. If the


                                                    © National Instruments 1597

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1597 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1598 ordinal=1598 -->
## Functions

Functions


              value of from is 1, the value of offset must be equal to or less than 0, which sets the file
              position at the end of the raw data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Finite
        Asynchronous Read.vi
            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Prefetched
        Asynchronous Read.vi
            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Synchronous Read and Write\TDMS Advanced Synchronous
        Read.vi
   TDMSTDMS ReserveReserve FileFile SizeSize FunctionFunction

       Pre-allocates disk space for writing and prevents fragmentation on a file-system level.
           If you are running this function on Windows with User Account Control enabled, you
      must run LabVIEW or the application with administrator privileges to avoid a run-time
        error.


1598   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1598 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1599 ordinal=1599 -->
## Functions

Functions

      Note

            If you are using this function to build an application, National Instruments
      recommends that you embed an application manifest to the application. The
       requested execution level in the manifest file must be
      requireAdministrator.

      When a .tdms file is in use by this function, no other processes can access this
           file.


Inputs/Outputs

   •     append? (T) —

    append? specifies whether to append the new size that this function reserves to an existing file.
       If the value is FALSE, this function changes the file size of tdms file to the reserved size. If the
    value is TRUE, this function extends the file size of tdms file with the reserved size. The default is
    TRUE.

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Advanced Open function to open the refnum.

   •      reserve size —

    reserve size specifies the size to reserve in samples.

    You can calculate the actual size, in bytes, that this function reserves by multiplying the value of
    reserve size by the number of bytes of data type. For example, if the value of reserve size is 512
    and data type is an unsigned 16-bit integer, then you can calculate the actual size that this
    function reserves as follows: 512×(16÷8) = 1024 bytes.

    For large files of several terabytes, the operating system may take a significant amount of time to


                                                    © National Instruments 1599

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1599 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1600 ordinal=1600 -->
## Functions

Functions


             pre-allocate disk space. Insert a delay in your application after the TDMS Reserve File Size
             function to ensure the file size is fully reserved. For multiple files on separate RAID volumes, if
           you reserve the file size in a loop, insert a single delay after the loop to avoid serializing the
             delays. NI recommends a time delay of 500 ms/TB.

               Note If the disable buffering? input of the TDMS Advanced Open function is TRUE,
                     the actual reserved size in bytes must be a multiple of the sector size of the hard disk.
                  Use the TDMS Advanced Open function to obtain the sector size of the hard disk.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data type —

           data type specifies the type of data on which you want to perform the operation. This input
            accepts integers, floating-point numbers, Booleans, and timestamps.

               Note You can wire the following floating-point numbers to this input:
                                     •  Single-precision and double-precision floating-point numbers
                                     • Complex single-precision and double-precision floating-point numbers
                                     • Extended-precision floating-point numbers

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Append Multiple
        Headers.vi

1600   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1600 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1601 ordinal=1601 -->
## Functions

Functions

TDMSTDMS ConvertConvert FormatFormat

Converts the file format version of a .tdms file from 1.0 to 2.0 or vice versa. This VI
overwrites the .tdms file with the new file format version you specify in the target
version input. This VI also changes the byte order of the .tdms file to native, host
order.


Inputs/Outputs

   •        file path —

      file path specifies the path to the .tdms file you want to convert.

   •       target version —

    target version specifies the file format version to which you want to convert the .tdms file.

    0                           1.0
    1                           2.0

   •     new property name —

   new property name specifies a new name for the name property of a group or channel in the
   .tdms file. For example, if a group has a name property with a value TDMSDataGroup, and if
    you wire a value group name to this input and run this VI, the original name property of this
    group changes to group name, which has a value TDMSDataGroup. This VI creates a new
   name property for this group, and uses the group name that you specified when creating this
   .tdms file as the property value. This input is valid only when target version is 2.0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •        file path out —


                                                    © National Instruments 1601

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1601 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1602 ordinal=1602 -->
## Functions

Functions


                file path out returns the path of the .tdms file on which you performed the operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When converting a .tdms file from file format version 1.0 to 2.0, this VI makes the
       following changes to the properties of the .tdms file.

            •  If the .tdms file does not have a name property, this VI adds a name property for
            this file and uses the filename as the value of the name property.
            •  If the groups or channels of the .tdms file have name properties, this VI keeps the
          property values in the version 2.0 file. However, this VI changes the object paths of
          these groups and channels. For example, if you use the TDMS Write function to
           write .tdms data to a version 1.0 file without wiring a value to the group name in
           input, the TDMS Write function automatically names the group as Untitled.
         Even if you later use the TDMS Set Properties function to create a name property
            for this group and assign a different value than Untitled, you still need to access
            this group from Untitled. You cannot access this group from the new name
          property value. However, if you use the TDMS Convert Format VI to convert this
        .tdms file to version 2.0, you no longer can access this group from Untitled.
         You must access this group from the name property value that you specified
             earlier.

               Tip To access groups or channels from the original names that you
                   specified for version 1.0, wire a value to the new property name input to
                change the name property to a new property name.

            •  If the name property of the groups or channels has duplicate values, this VI
         appends a numeric suffix to the duplicate values. For example, if a .tdms file has a
         group of three channels with the same channel name TDMSDataChannel, this VI
         changes the values of the name property in the second and third groups to
        TDMSDataChannel 1 and TDMSDataChannel 2, respectively. This VI does
          not change the property value of the first channel and keeps the value as
        TDMSDataChannel.


1602   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1602 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1603 ordinal=1603 -->
## Functions

Functions

TDMSTDMS AdvancedAdvanced SynchronousSynchronous I/OI/O

Use the TDMS Advanced Synchronous I/O functions to synchronously read data from
or write data to .tdms files.


 Palette Object                  Description

 TDMS Advanced Synchronous
                                 Writes data to the specified .tdms file synchronously. Write Function

 TDMS Advanced Synchronous   Reads the specified .tdms file and returns data in a format
 Read Function                   specified by the data type input.

TDMSTDMS AdvancedAdvanced SynchronousSynchronous WriteWrite
FunctionFunction

Writes data to the specified .tdms file synchronously.


Inputs/Outputs

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Advanced Open function to open the refnum.

   •      data —

    data specifies the data to write to the .tdms file. This input accepts a 1D or 2D array of integers,
     floating-point numbers, Booleans, and timestamps. If the disable buffering? input of the TDMS
    Advanced Open function is TRUE, the size of data must be a multiple of the sector size and the


                                                    © National Instruments 1603

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1603 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1604 ordinal=1604 -->
## Functions

Functions


             array size must be less than 67,076,096 bytes on x86 systems, 67,051,520 bytes on IA-64 systems,
            or 33,525,760 bytes on x64 systems.

             Refer to the Microsoft Developer Network Web site at msdn.microsoft.com for more
            information about calculating the maximum array size.

               Note

                   You can wire the following floating-point numbers to this input:

                                     •  Single-precision and double-precision floating-point numbers
                                     • Complex single-precision and double-precision floating-point numbers
                                     • (Windows) Extended-precision floating-point numbers

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Synchronous Read and Write\TDMS Advanced Synchronous
        Write.vi
   TDMSTDMS AdvancedAdvanced SynchronousSynchronous ReadRead FunctionFunction

      Reads the specified .tdms file and returns data in a format specified by the data type

1604   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1604 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1605 ordinal=1605 -->
## Functions

Functions

input.


Inputs/Outputs

   •      count (-1) —

    count specifies the maximum number of data elements you want to read. The default is -1,
    which specifies that this function reads all data elements. If the disable buffering? input of the
   TDMS Advanced Open function is TRUE, the value of (count * the length of data type) must be a
    multiple of the sector size.

    You can calculate the size, in bytes, that this function reads by multiplying the value of count by
    the number of bytes of data type. For example, if the value of count is 512 and data type is an
    unsigned 16-bit integer, then you can calculate the size that this function reads as follows:
    512×(16÷8) = 1024 bytes.

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Advanced Open function to open the refnum.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      data type —

    data type specifies the type of data on which you want to perform the operation. This input
    accepts integers, floating-point numbers, Booleans, and timestamps.

          Note You can wire the following floating-point numbers to this input:
                         •  Single-precision and double-precision floating-point numbers
                         • Complex single-precision and double-precision floating-point numbers
                         • (Windows) Extended-precision floating-point numbers

   •     tdms file out —


                                                    © National Instruments 1605

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1605 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1606 ordinal=1606 -->
## Functions

Functions


          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •      data —

           data returns the data this function reads from the .tdms file in the specified data type.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      read process finished? —

           read process finished? indicates whether the reading process finished or not.

                 Tip Use this Boolean value as one of the stop conditions for a While Loop. For
                    example, you can put the TDMS Advanced Synchronous Read function in the While
                  Loop to read data infinitely until the value of read process finished? becomes TRUE.
                      This value becomes TRUE when the TDMS Advanced Synchronous Read function
                    reaches the end of a .tdms file.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Synchronous Read and Write\TDMS Advanced Synchronous
        Read.vi
   TDMSTDMS AdvancedAdvanced AsynchronousAsynchronous I/OI/O

      Use the TDMS Advanced Asynchronous I/O functions to asynchronously read data from
       or write data to .tdms files.

           Note To use the TDMS Advanced Asynchronous I/O functions, you must set
              the enable asynchronous? input of the TDMS Advanced Open function to
             TRUE.

1606   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1606 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1607 ordinal=1607 -->
## Functions

Functions


Palette               DescriptionObject

TDMS
                Allocates buffers and configures the timeout value for asynchronous writes. TheConfigure             timeout value applies to all subsequent asynchronous writes. You must use thisAsynchronous               function to configure the asynchronous writes before using the TDMS AdvancedWrites             Asynchronous Write function.Function

TDMS               Writes data to the specified .tdms file asynchronously. This function can initiateAdvanced               multiple asynchronous writes that take place in the background. You can use theAsynchronous
           TDMS Get Asynchronous Write Status function to query the number of pendingWrite              asynchronous writes.Function

TDMS Get
Asynchronous  Retrieves the number of pending asynchronous writes issued by the TDMS
Write Status   Advanced Asynchronous Write function.
Function

              Generates random data that you can use to test the performance of the AdvancedTDMS           TDMS VIs and functions. Use this VI in benchmarking tests to simulate the
Generate              production of data from a data acquisition device. Wire data to the data type inputRandom Data               to determine the polymorphic instance to use or manually select the instance.

TDMS                Allocates buffers and configures the timeout value for asynchronous reads. TheConfigure
             timeout value applies to all subsequent asynchronous reads. You must use this
Asynchronous
               function to configure the asynchronous reads before using the TDMS Advanced
Reads
             Asynchronous Read function.
Function

TDMS Start     Starts an asynchronous read process. You cannot configure or start an
Asynchronous asynchronous read process unless the previous process has completed or stopped.
Reads        You can stop an asynchronous read process by using the TDMS Stop Asynchronous
Function      Reads function.

TDMS Stop    Stops issuing new asynchronous reads. This function does not discard completed
Asynchronous asynchronous reads or cancel pending asynchronous reads. After you use this
Reads         function to stop asynchronous reads, you still can use the TDMS Advanced
Function      Asynchronous Read function to read the completed asynchronous reads.


                                                    © National Instruments 1607

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1607 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1608 ordinal=1608 -->
## Functions

Functions


         Palette                       Description
        Object

      TDMS Get
        Asynchronous  Retrieves the number of buffers that contain data available for the TDMS Advanced
       Read Status   Asynchronous Read function to read.
         Function

      TDMS                     Reads the specified .tdms file and returns data in a format specified by the data        Advanced                      type input. This function returns data that was previously read into the buffers        Asynchronous                       configured in the TDMS Configure Asynchronous Reads function. This function can
       Read                       execute multiple asynchronous reads simultaneously in the background.         Function

   TDMSTDMS ConfigureConfigure AsynchronousAsynchronous WritesWrites
   FunctionFunction

       Allocates buffers and configures the timeout value for asynchronous writes. The
      timeout value applies to all subsequent asynchronous writes. You must use this
       function to configure the asynchronous writes before using the TDMS Advanced
      Asynchronous Write function.


      Inputs/Outputs

               •     max write size —

         max write size specifies the maximum size, in samples, to allocate for each asynchronous write.
             This input is valid only if pre-allocate? is TRUE.

           You can calculate the actual maximum size, in bytes, that this function pre-allocates by
             multiplying the value of max write size by the number of bytes of data type. For example, if the
            value of max write size is 512 and data type is an unsigned 16-bit integer, then you can calculate


1608   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1608 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1609 ordinal=1609 -->
## Functions

Functions


  the actual maximum size that this function pre-allocates as follows: 512×(16÷8) = 1024 bytes.

        Note If the disable buffering? input of the TDMS Advanced Open function is TRUE,
           the actual maximum size in bytes must be a multiple of the sector size of the hard
            disk. Use the TDMS Advanced Open function to obtain the sector size of the hard disk.

•       pre-allocate? (F) —

  pre-allocate? specifies whether to pre-allocate buffers to return to LabVIEW in exchange for the
  data buffers you pass to the TDMS Advanced Asynchronous Write function. The default is FALSE.

  Set the value to TRUE to avoid run-time buffer allocations. If pre-allocate? is TRUE, you must
  wire a supported data type to this function.

•     tdms file —

  tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
  the TDMS Advanced Open function to open the refnum.

•     max asynchronous writes (4) —

  max asynchronous writes specifies the maximum number of asynchronous writes that can run
  simultaneously in the background. After the number of pending asynchronous writes reaches
  the maximum value, the TDMS Advanced Asynchronous Write function waits for a pending
  asynchronous write to complete before issuing another asynchronous write. The value must be
  greater than zero. The default is 4.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      data type —

  data type specifies the data type of the pre-allocated buffers. These pre-allocated buffers are
  returned to LabVIEW in exchange for the data buffers you pass to the TDMS Advanced
  Asynchronous Write function. This input accepts integers, floating-point numbers, Booleans,
  and timestamps. You must wire a supported data type to this input if pre-allocate? is TRUE.
  LabVIEW ignores this input if pre-allocate? is FALSE.

•      timeout (5 s) —


                                                   © National Instruments 1609

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1609 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1610 ordinal=1610 -->
## Functions

Functions


           timeout specifies the timeout value, in seconds, for the TDMS Advanced Asynchronous Write
             function. When the number of pending asynchronous writes reaches the maximum value, the
         TDMS Advanced Asynchronous Write function waits as long as the timeout value for a pending
           asynchronous write to complete before issuing another asynchronous write. If you do not wire
            data to this input, this function sets the value to 5.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Append Multiple
        Headers.vi
            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Asynchronous
        Write.vi
   TDMSTDMS AdvancedAdvanced AsynchronousAsynchronous WriteWrite
   FunctionFunction

       Writes data to the specified .tdms file asynchronously. This function can initiate
       multiple asynchronous writes that take place in the background. You can use the TDMS
      Get Asynchronous Write Status function to query the number of pending
      asynchronous writes.


1610   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1610 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1611 ordinal=1611 -->
## Functions

Functions


Inputs/Outputs

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Advanced Open function to open the refnum.

   •      data —

    data specifies the data to write to the .tdms file. This input accepts a 1D or 2D array of integers,
     floating-point numbers, Booleans, and timestamps. If the disable buffering? input of the TDMS
    Advanced Open function is TRUE, the size of data must be a multiple of the sector size and the
    array size must be less than 67,076,096 bytes on x86 systems, 67,051,520 bytes on IA-64 systems,
    or 33,525,760 bytes on x64 systems.

    Refer to the Microsoft Developer Network Web site at msdn.microsoft.com for more
    information about calculating the maximum array size.

          Note You can wire the following floating-point numbers to this input:
                         •  Single-precision and double-precision floating-point numbers
                         • Complex single-precision and double-precision floating-point numbers
                         • Extended-precision floating-point numbers

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1611

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1611 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1612 ordinal=1612 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Asynchronous
        Write.vi
   TDMSTDMS GetGet AsynchronousAsynchronous WriteWrite StatusStatus
   FunctionFunction

       Retrieves the number of pending asynchronous writes issued by the TDMS Advanced
      Asynchronous Write function.

            Tip Use this function when you monitor an application that issues a series of
             asynchronous writes over a long period of time. By querying the number of
             pending writes and keeping track of the highest value this function returns,
            you can choose an appropriate value for the max asynchronous writes input
               of the TDMS Configure Asynchronous Writes function.


      Inputs/Outputs

               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Advanced Open function to open the refnum.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     tdms file out —

1612   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1612 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1613 ordinal=1613 -->
## Functions

Functions


   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •     number of pending writes —

   number of pending writes returns the number of pending asynchronous writes issued by the
   TDMS Advanced Asynchronous Write function.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Advanced Read and Write\
   Asynchronous Read and Write\TDMS Advanced Ring Buffer.vi
TDMSTDMS GenerateGenerate RandomRandom DataData

Generates random data that you can use to test the performance of the Advanced
TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
of data from a data acquisition device. Wire data to the data type input to determine
the polymorphic instance to use or manually select the instance.


  • TDMS Generate Random Data (U8) VI
  • TDMS Generate Random Data (I8) VI
  • TDMS Generate Random Data (U16) VI
  • TDMS Generate Random Data (I16) VI
  • TDMS Generate Random Data (U32) VI
  • TDMS Generate Random Data (I32) VI
  • TDMS Generate Random Data (U64) VI
  • TDMS Generate Random Data (I64) VI

                                                    © National Instruments 1613

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1613 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1614 ordinal=1614 -->
## Functions

Functions

            • TDMS Generate Random Data (SGL) VI
            • TDMS Generate Random Data (DBL) VI
            • TDMS Generate Random Data (CSG) VI
            • TDMS Generate Random Data (CDB) VI
   TDMSTDMS GenerateGenerate RandomRandom DataData (U8)(U8) VIVI

       Generates random data that you can use to test the performance of the Advanced
     TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
       of data from a data acquisition device. Wire data to the data type input to determine
       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      data type —

           data type specifies the data type of the random data you want to generate.

               •     number of samples —

          number of samples specifies the number of data samples you want to generate.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data —

           data returns the random data with the specified data type.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1614   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1614 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1615 ordinal=1615 -->
## Functions

Functions

TDMSTDMS GenerateGenerate RandomRandom DataData (I8)(I8) VIVI

Generates random data that you can use to test the performance of the Advanced
TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
of data from a data acquisition device. Wire data to the data type input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      data type —

    data type specifies the data type of the random data you want to generate.

   •     number of samples —

   number of samples specifies the number of data samples you want to generate.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      data —

    data returns the random data with the specified data type.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

TDMSTDMS GenerateGenerate RandomRandom DataData (U16)(U16) VIVI

Generates random data that you can use to test the performance of the Advanced
TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
of data from a data acquisition device. Wire data to the data type input to determine

                                                    © National Instruments 1615

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1615 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1616 ordinal=1616 -->
## Functions

Functions

       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      data type —

           data type specifies the data type of the random data you want to generate.

               •     number of samples —

          number of samples specifies the number of data samples you want to generate.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data —

           data returns the random data with the specified data type.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   TDMSTDMS GenerateGenerate RandomRandom DataData (I16)(I16) VIVI

       Generates random data that you can use to test the performance of the Advanced
     TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
       of data from a data acquisition device. Wire data to the data type input to determine
       the polymorphic instance to use or manually select the instance.


1616   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1616 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1617 ordinal=1617 -->
## Functions

Functions

Inputs/Outputs

   •      data type —

    data type specifies the data type of the random data you want to generate.

   •     number of samples —

   number of samples specifies the number of data samples you want to generate.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      data —

    data returns the random data with the specified data type.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

TDMSTDMS GenerateGenerate RandomRandom DataData (U32)(U32) VIVI

Generates random data that you can use to test the performance of the Advanced
TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
of data from a data acquisition device. Wire data to the data type input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      data type —

    data type specifies the data type of the random data you want to generate.

   •     number of samples —

                                                    © National Instruments 1617

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1617 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1618 ordinal=1618 -->
## Functions

Functions


          number of samples specifies the number of data samples you want to generate.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data —

           data returns the random data with the specified data type.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   TDMSTDMS GenerateGenerate RandomRandom DataData (I32)(I32) VIVI

       Generates random data that you can use to test the performance of the Advanced
     TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
       of data from a data acquisition device. Wire data to the data type input to determine
       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      data type —

           data type specifies the data type of the random data you want to generate.

               •     number of samples —

          number of samples specifies the number of data samples you want to generate.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


1618   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1618 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1619 ordinal=1619 -->
## Functions

Functions


    standard error in functionality.

   •      data —

    data returns the random data with the specified data type.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

TDMSTDMS GenerateGenerate RandomRandom DataData (U64)(U64) VIVI

Generates random data that you can use to test the performance of the Advanced
TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
of data from a data acquisition device. Wire data to the data type input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      data type —

    data type specifies the data type of the random data you want to generate.

   •     number of samples —

   number of samples specifies the number of data samples you want to generate.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      data —

    data returns the random data with the specified data type.


                                                    © National Instruments 1619

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1619 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1620 ordinal=1620 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   TDMSTDMS GenerateGenerate RandomRandom DataData (I64)(I64) VIVI

       Generates random data that you can use to test the performance of the Advanced
     TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
       of data from a data acquisition device. Wire data to the data type input to determine
       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      data type —

           data type specifies the data type of the random data you want to generate.

               •     number of samples —

          number of samples specifies the number of data samples you want to generate.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data —

           data returns the random data with the specified data type.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1620   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1620 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1621 ordinal=1621 -->
## Functions

Functions

TDMSTDMS GenerateGenerate RandomRandom DataData (SGL)(SGL) VIVI

Generates random data that you can use to test the performance of the Advanced
TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
of data from a data acquisition device. Wire data to the data type input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      data type —

    data type specifies the data type of the random data you want to generate.

   •     number of samples —

   number of samples specifies the number of data samples you want to generate.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      data —

    data returns the random data with the specified data type.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

TDMSTDMS GenerateGenerate RandomRandom DataData (DBL)(DBL) VIVI

Generates random data that you can use to test the performance of the Advanced
TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
of data from a data acquisition device. Wire data to the data type input to determine

                                                    © National Instruments 1621

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1621 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1622 ordinal=1622 -->
## Functions

Functions

       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      data type —

           data type specifies the data type of the random data you want to generate.

               •     number of samples —

          number of samples specifies the number of data samples you want to generate.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data —

           data returns the random data with the specified data type.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   TDMSTDMS GenerateGenerate RandomRandom DataData (CSG)(CSG) VIVI

       Generates random data that you can use to test the performance of the Advanced
     TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
       of data from a data acquisition device. Wire data to the data type input to determine
       the polymorphic instance to use or manually select the instance.


1622   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1622 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1623 ordinal=1623 -->
## Functions

Functions

Inputs/Outputs

   •      data type —

    data type specifies the data type of the random data you want to generate.

   •     number of samples —

   number of samples specifies the number of data samples you want to generate.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      data —

    data returns the random data with the specified data type.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

TDMSTDMS GenerateGenerate RandomRandom DataData (CDB)(CDB) VIVI

Generates random data that you can use to test the performance of the Advanced
TDMS VIs and functions. Use this VI in benchmarking tests to simulate the production
of data from a data acquisition device. Wire data to the data type input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      data type —

    data type specifies the data type of the random data you want to generate.

   •     number of samples —

                                                    © National Instruments 1623

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1623 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1624 ordinal=1624 -->
## Functions

Functions


          number of samples specifies the number of data samples you want to generate.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data —

           data returns the random data with the specified data type.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   TDMSTDMS ConfigureConfigure AsynchronousAsynchronous ReadsReads
   FunctionFunction

       Allocates buffers and configures the timeout value for asynchronous reads. The
      timeout value applies to all subsequent asynchronous reads. You must use this
       function to configure the asynchronous reads before using the TDMS Advanced
      Asynchronous Read function.

           Note Before using this function, ensure that no asynchronous reads are
              pending.


      Inputs/Outputs

               •     tdms file —


1624   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1624 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1625 ordinal=1625 -->
## Functions

Functions


  tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
  the TDMS Advanced Open function to open the refnum.

•     number of buffers (4) —

  number of buffers specifies the number of buffers to allocate for asynchronous reads. The value
  must be greater than zero. The default is 4.

•       buffer size —

  buffer size specifies the buffer size in samples of data. If the disable buffering? input of the
  TDMS Advanced Open function is TRUE, the value of (buffer size * the length of data type) must
  be a multiple of the sector size.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      data type —

  data type specifies the type of data on which you want to perform the operation. This input
  accepts integers, floating-point numbers, Booleans, and timestamps.

        Note You can wire the following floating-point numbers to this input:
                      •  Single-precision and double-precision floating-point numbers
                      • Complex single-precision and double-precision floating-point numbers
                      • Extended-precision floating-point numbers

•      timeout (5 s) —

  timeout specifies the timeout value, in seconds, for the asynchronous read. If you do not wire
  data to this input, this function sets the value to 5.

•     tdms file out —

  tdms file out returns a TDMS file reference to the .tdms file on which you performed the
  operation.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 1625

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1625 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1626 ordinal=1626 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Basic
        Asynchronous Read.vi
            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Prefetched
        Asynchronous Read.vi
   TDMSTDMS StartStart AsynchronousAsynchronous ReadsReads FunctionFunction

        Starts an asynchronous read process. You cannot configure or start an asynchronous
       read process unless the previous process has completed or stopped. You can stop an
      asynchronous read process by using the TDMS Stop Asynchronous Reads function.


      Inputs/Outputs

               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Advanced Open function to open the refnum.

               •       total count (-1) —

              total count specifies the total number of values of the data type you want to read from a .tdms
                  file. The default is –1, which specifies that LabVIEW keeps initiating asynchronous reads until this
             function reaches the end of the .tdms file or you stop initiating asynchronous reads by using
            the TDMS Stop Asynchronous Reads function.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


1626   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1626 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1627 ordinal=1627 -->
## Functions

Functions


    standard error in functionality.

   •      data type —

    data type specifies the type of data on which you want to perform the operation. This input
    accepts integers, floating-point numbers, Booleans, and timestamps.

          Note You can wire the following floating-point numbers to this input:
                         •  Single-precision and double-precision floating-point numbers
                         • Complex single-precision and double-precision floating-point numbers
                         • Extended-precision floating-point numbers

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Advanced Read and Write\
   Asynchronous Read and Write\TDMS Advanced Basic
   Asynchronous Read.vi
  • labview\examples\File IO\TDMS\Advanced Read and Write\
   Asynchronous Read and Write\TDMS Advanced Prefetched
   Asynchronous Read.vi
TDMSTDMS StopStop AsynchronousAsynchronous ReadsReads FunctionFunction

Stops issuing new asynchronous reads. This function does not discard completed
asynchronous reads or cancel pending asynchronous reads. After you use this function
to stop asynchronous reads, you still can use the TDMS Advanced Asynchronous Read


                                                    © National Instruments 1627

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1627 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1628 ordinal=1628 -->
## Functions

Functions

       function to read the completed asynchronous reads.


      Inputs/Outputs

               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Advanced Open function to open the refnum.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Prefetched
        Asynchronous Read.vi


1628   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1628 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1629 ordinal=1629 -->
## Functions

Functions

TDMSTDMS GetGet AsynchronousAsynchronous ReadRead StatusStatus
FunctionFunction

Retrieves the number of buffers that contain data available for the TDMS Advanced
Asynchronous Read function to read.


Inputs/Outputs

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Advanced Open function to open the refnum.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •     number of buffers available —

   number of buffers available returns the number of buffers that contain data for the TDMS
    Advanced Asynchronous Read function to read.

   •        all buffers full? —

     all buffers full? indicates whether all the buffers are full of data for the TDMS Advanced
    Asynchronous Read function to read.

    This output also can be TRUE even when the number of buffers available output of this function
      is not equal to the number of buffers input of the TDMS Configure Asynchronous Reads function
    under the following conditions:

                                                    © National Instruments 1629

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1629 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1630 ordinal=1630 -->
## Functions

Functions

                     • The TDMS Advanced Asynchronous Read function reaches the end of a .tdms file.
                     • The TDMS Advanced Asynchronous Read function finishes reading the total count of data
                 that you specify in the TDMS Start Asynchronous Reads function.

                 Tip Use this Boolean value as one of the stop conditions for a While Loop. For
                    example, you can put the TDMS Get Asynchronous Read Status function in the While
                  Loop and wire the all buffers full? output to the Stop if True conditional terminal of
                     the While Loop. You then can start asynchronous reads by using the TDMS Start
                   Asynchronous Reads function and wait for the all buffers full? value to become TRUE.
                When this value becomes TRUE, you can use the TDMS Advanced Asynchronous Read
                      function to read the data from the buffers.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Finite
        Asynchronous Read.vi
            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Prefetched
        Asynchronous Read.vi
   TDMSTDMS AdvancedAdvanced AsynchronousAsynchronous ReadRead
   FunctionFunction

      Reads the specified .tdms file and returns data in a format specified by the data type
       input. This function returns data that was previously read into the buffers configured
        in the TDMS Configure Asynchronous Reads function. This function can execute
       multiple asynchronous reads simultaneously in the background.


1630   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1630 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1631 ordinal=1631 -->
## Functions

Functions


Inputs/Outputs

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Advanced Open function to open the refnum.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      data type —

    data type specifies the type of data on which you want to perform the operation. This input
    accepts integers, floating-point numbers, Booleans, and timestamps.

          Note You can wire the following floating-point numbers to this input:
                         •  Single-precision and double-precision floating-point numbers
                         • Complex single-precision and double-precision floating-point numbers
                         • Extended-precision floating-point numbers

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •      data —

    data returns the data this function reads from the .tdms file in the specified data type.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      read process finished? —

    read process finished? indicates whether the reading process is finished or not.


                                                    © National Instruments 1631

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1631 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1632 ordinal=1632 -->
## Functions

Functions


                 Tip

                  Use this Boolean value as one of the stop conditions for a While Loop. For example,
                  you can place the TDMS Advanced Asynchronous Read function in the While Loop to
                    read data indefinitely until the value of read process finished? returns TRUE. This
                     value returns TRUE when one of the following conditions occurs:

                                     • The TDMS Advanced Asynchronous Read function reaches the end of a .tdms
                                        file.
                                     • The TDMS Advanced Asynchronous Read function finishes reading total count
                             of data that you specify for the TDMS Start Asynchronous Reads function.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Basic
        Asynchronous Read.vi
            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Finite
        Asynchronous Read.vi
            • labview\examples\File IO\TDMS\Advanced Read and Write\
        Asynchronous Read and Write\TDMS Advanced Prefetched
        Asynchronous Read.vi
   TDMSTDMS AdvancedAdvanced DataData ReferenceReference I/OI/O

      Use the TDMS Advanced Data Reference I/O functions to interact with data that is
     owned by a component external to LabVIEW, such as the direct memory access (DMA)
       buffer of a device driver that controls a data-streaming device. You can use these
       functions to asynchronously write data from the DMA buffer of a device driver to .tdms
         files without needing to copy the data into a LabVIEW array first. You also can use these
       functions to asynchronously read data from .tdms files and place the data directly into
       the DMA buffer.


1632   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1632 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1633 ordinal=1633 -->
## Functions

Functions

     Note To use the TDMS Advanced Data Reference I/O functions, you must set
       the enable asynchronous? input of the TDMS Advanced Open function to
      TRUE.


Palette               DescriptionObject

TDMS               Configures the maximum number of asynchronous writes and the timeout value.Configure             The timeout value applies to all subsequent asynchronous writes. You must useAsynchronous                 this function to configure the asynchronous writes before using the TDMS Advanced
Writes (Data             Asynchronous Write (Data Ref) function.Ref) Function

TDMS               Writes data referenced by the data reference input to the specified .tdms fileAdvanced               asynchronously. The data reference input typically refers to a portion of data
Asynchronous            owned by a component external to LabVIEW, such as a region of a DMA buffer thatWrite (Data               contains data you want to write to the .tdms file.
Ref) Function

TDMS Get
Asynchronous              Returns the number of pending asynchronous writes issued by the TDMS AdvancedWrite Status
             Asynchronous Write (Data Ref) function.(Data Ref)
Function

TDMS         Configures the maximum number of asynchronous reads, total amount of data to
Configure      read, and the timeout value for the asynchronous reads. The timeout value applies
Asynchronous  to all subsequent asynchronous reads. You must use this function to configure the
Reads (Data   asynchronous reads before using the TDMS Advanced Asynchronous Read (Data
Ref) Function  Ref) function.

TDMS
             Reads data from the specified .tdms file asynchronously and stores the data in the
Advanced
           memory of a component external to LabVIEW. Use the data reference input of this
Asynchronous
               function to specify the location of the external memory, such as a region of a DMA
Read (Data
                buffer owned by a device driver.
Ref) Function

TDMS Get
              Returns the number of pending asynchronous reads issued by the TDMS Advanced
Asynchronous
             Asynchronous Read (Data Ref) function.
Read Status


                                                    © National Instruments 1633

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1633 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1634 ordinal=1634 -->
## Functions

Functions


         Palette                       Description
        Object

         (Data Ref)
         Function

   TDMSTDMS ConfigureConfigure AsynchronousAsynchronous WritesWrites (Data(Data
    Ref)Ref) FunctionFunction

       Configures the maximum number of asynchronous writes and the timeout value. The
      timeout value applies to all subsequent asynchronous writes. You must use this
       function to configure the asynchronous writes before using the TDMS Advanced
      Asynchronous Write (Data Ref) function.


      Inputs/Outputs

               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Advanced Open function to open the refnum.

               •     max asynchronous writes (4) —

         max asynchronous writes specifies the maximum number of asynchronous writes that can run
            simultaneously in the background. After the number of pending asynchronous writes reaches
            the maximum value, the TDMS Advanced Asynchronous Write (Data Ref) function waits for a
           pending asynchronous write to complete before issuing another asynchronous write. The value
          must be greater than zero. The default is 4.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (5 s) —

1634   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1634 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1635 ordinal=1635 -->
## Functions

Functions


    timeout specifies the timeout value, in seconds, for the TDMS Advanced Asynchronous Write
    (Data Ref) function. When the number of pending asynchronous writes reaches the maximum
     value, the TDMS Advanced Asynchronous Write (Data Ref) function waits as long as the timeout
    value for a pending asynchronous write to complete before issuing another asynchronous write.
       If you do not wire data to this input, this function sets the value to 5.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

TDMSTDMS AdvancedAdvanced AsynchronousAsynchronous WriteWrite (Data(Data
Ref)Ref) FunctionFunction

Writes data referenced by the data reference input to the specified .tdms file
asynchronously. The data reference input typically refers to a portion of data owned
by a component external to LabVIEW, such as a region of a DMA buffer that contains
data you want to write to the .tdms file.


Inputs/Outputs

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Advanced Open function to open the refnum.

   •      data reference —


                                                    © National Instruments 1635

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1635 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1636 ordinal=1636 -->
## Functions

Functions


           data reference specifies the external data value reference that points to the external data you
          want to write to the .tdms file. This input accepts an external data value reference containing a
          1D or 2D array of integers, floating-point numbers, Booleans, or timestamps. If the disable
             buffering? input of the TDMS Advanced Open function is TRUE, the size of data that you wire to
            the data reference input must be a multiple of the sector size.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      auto delete reference? (T) —

           auto delete reference? specifies whether you want LabVIEW to delete the data reference
            automatically after the asynchronous operation completes. Deleting the data reference notifies
            the owner of the external memory that LabVIEW no longer needs access to the external memory.
          The default is TRUE. Set this value to FALSE when you want to continue using the reference after
            the asynchronous operation completes. For example, you might want to modify the data in
           LabVIEW before deleting the reference. If you set the value to FALSE, you must use the Delete
           Data Value Reference function to delete the data reference.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       This function can issue additional asynchronous writes while executing previously-
       issued asynchronous writes in the background. When the number of asynchronous
       writes in the background reaches the maximum value, this function waits until a
       previously-issued asynchronous write completes before issuing an additional
      asynchronous write. If the previously-issued asynchronous write does not complete
       within the timeout value, this function returns error code –2546. Use the TDMS
       Configure Asynchronous Writes (Data Ref) function to configure the maximum number
       of asynchronous writes and the timeout value.

      Use the TDMS Get Asynchronous Write Status (Data Ref) function to query the number
       of pending asynchronous writes.

1636   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1636 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1637 ordinal=1637 -->
## Functions

Functions

TDMSTDMS GetGet AsynchronousAsynchronous WriteWrite StatusStatus (Data(Data
Ref)Ref) FunctionFunction

Returns the number of pending asynchronous writes issued by the TDMS Advanced
Asynchronous Write (Data Ref) function.

      Tip Use this function when you monitor an application that issues a series of
       asynchronous writes over a long period of time. By querying the number of
       pending writes and keeping track of the highest value this function returns,
       you can choose an appropriate value for the max asynchronous writes input
        of the TDMS Configure Asynchronous Writes (Data Ref) function.


Inputs/Outputs

   •     tdms file —

   tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
    the TDMS Advanced Open function to open the refnum.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •     number of pending writes —

   number of pending writes returns the number of asynchronous writes that have not completed.
    You can use this information to monitor a write-to-disk operation.


                                                    © National Instruments 1637

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1637 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1638 ordinal=1638 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   TDMSTDMS ConfigureConfigure AsynchronousAsynchronous ReadsReads (Data(Data
    Ref)Ref) FunctionFunction

       Configures the maximum number of asynchronous reads, total amount of data to read,
      and the timeout value for the asynchronous reads. The timeout value applies to all
      subsequent asynchronous reads. You must use this function to configure the
      asynchronous reads before using the TDMS Advanced Asynchronous Read (Data Ref)
       function.

           Note Before using this function, ensure that no asynchronous reads are
              pending.


      Inputs/Outputs

               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Advanced Open function to open the refnum.

               •     max asynchronous reads (4) —

         max asynchronous reads specifies the maximum number of asynchronous reads that can run
            simultaneously in the background. After the number of pending asynchronous reads reaches the
         maximum value, the TDMS Advanced Asynchronous Read (Data Ref) function waits for a pending
           asynchronous read to complete before issuing another asynchronous read. The value must be
             greater than zero. The default is 4.


1638   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1638 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1639 ordinal=1639 -->
## Functions

Functions

   •       total size (in bytes) (-1) —

     total size specifies the total size, in bytes, of the data to read from the .tdms file. The default is
     –1, which specifies that the TDMS Advanced Asynchronous Read (Data Ref) function keeps
     issuing asynchronous reads until this function reaches the end of the .tdms file. Use this input
     in conjunction with the read process finished? output of the TDMS Advanced Asynchronous
    Read (Data Ref) function to control an asynchronous reading process.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (5 s) —

    timeout specifies the timeout value, in seconds, for the TDMS Advanced Asynchronous Read
    (Data Ref) function. When the number of pending asynchronous reads reaches the maximum
     value, the TDMS Advanced Asynchronous Read (Data Ref) function waits as long as the timeout
    value for a pending asynchronous read to complete before issuing another asynchronous read. If
    you do not wire data to this input, this function sets the value to 5.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

TDMSTDMS AdvancedAdvanced AsynchronousAsynchronous ReadRead (Data(Data
Ref)Ref) FunctionFunction

Reads data from the specified .tdms file asynchronously and stores the data in the
memory of a component external to LabVIEW. Use the data reference input of this
function to specify the location of the external memory, such as a region of a DMA
buffer owned by a device driver.


                                                    © National Instruments 1639

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1639 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1640 ordinal=1640 -->
## Functions

Functions


      Inputs/Outputs

               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Advanced Open function to open the refnum.

               •      data reference —

           data reference specifies the external data value reference that points to the region of an external
             buffer in which you want LabVIEW to store the data this function reads from the .tdms file. This
            input accepts an external data value reference containing a 1D or 2D array of integers, floating-
            point numbers, Booleans, or timestamps. If the disable buffering? input of the TDMS Advanced
          Open function is TRUE, the size of data that you wire to the data reference input must be a
            multiple of the sector size.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      auto delete reference? (T) —

           auto delete reference? specifies whether you want LabVIEW to delete the data reference
            automatically after the asynchronous operation completes. Deleting the data reference notifies
            the owner of the external memory that LabVIEW no longer needs access to the external memory.
          The default is TRUE. Set this value to FALSE when you want to continue using the reference after
            the asynchronous operation completes. For example, you might want to modify the data in
           LabVIEW before deleting the reference. If you set the value to FALSE, you must use the Delete
           Data Value Reference function to delete the data reference.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1640   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1640 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1641 ordinal=1641 -->
## Functions

Functions

   •      read process finished? —

    read process finished? indicates whether the reading process is finished or not.

           Tip Use this Boolean value as one of the stop conditions for a While Loop. For
            example, you can place the TDMS Advanced Asynchronous Read (Data Ref) function
               in the While Loop to read data indefinitely until the value of read process finished?
              returns TRUE. This value returns TRUE when one of the following conditions occurs:
                         • The TDMS Advanced Asynchronous Read (Data Ref) function reaches the end
                     of a .tdms file.
                         • The TDMS Advanced Asynchronous Read (Data Ref) function finishes reading
                   the total size of data that you specify for the TDMS Configure Asynchronous
                 Reads (Data Ref) function.


This function can issue additional asynchronous reads while executing previously-
issued asynchronous reads in the background. When the number of asynchronous
reads in the background reaches the maximum value, this function waits until a
previously-issued asynchronous read completes before issuing an additional
asynchronous read. If the previously-issued asynchronous read does not complete
within the timeout value, this function returns error code –2546. Use the TDMS
Configure Asynchronous Reads (Data Ref) function to configure the maximum number
of asynchronous reads and the timeout value.

Use the TDMS Get Asynchronous Read Status (Data Ref) function to query the number
of pending asynchronous reads.
TDMSTDMS GetGet AsynchronousAsynchronous ReadRead StatusStatus (Data(Data
Ref)Ref) FunctionFunction

Returns the number of pending asynchronous reads issued by the TDMS Advanced
Asynchronous Read (Data Ref) function.

      Tip Use this function when you monitor an application that issues a series of
       asynchronous reads over a long period of time. By querying the number of
       pending reads and keeping track of the highest value this function returns,


                                                    © National Instruments 1641

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1641 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1642 ordinal=1642 -->
## Functions

Functions


            you can choose an appropriate value for the max asynchronous reads input
               of the TDMS Configure Asynchronous Reads (Data Ref) function.


      Inputs/Outputs

               •     tdms file —

          tdms file specifies a reference number to the .tdms file on which to perform the operation. Use
            the TDMS Advanced Open function to open the refnum.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     tdms file out —

          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •     number of pending reads —

          number of pending reads returns the number of asynchronous reads that have not completed.
           You can use this information to monitor a read-from-disk operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   TDMSTDMS InIn MemoryMemory

      Use the TDMS In Memory functions to open, close, read from, and write to .tdms files in
      memory.


1642   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1642 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1643 ordinal=1643 -->
## Functions

Functions


 Palette Object    Description

 TDMS In Memory  Creates an empty .tdms file in memory for reading or writing. You also can use
 Open Function    this function to create a file in memory from a byte array or file on disk.

 TDMS In Memory                Reads a .tdms file in memory and returns data as an unsigned 8-bit integer array Read Bytes                  data type.
 Function

                  Closes the .tdms file in memory that you opened with the TDMS In Memory Open TDMS In Memory                    function. This function also writes the .tdms file to disk, if specified by the file Close Function                 path input.

TDMSTDMS InIn MemoryMemory OpenOpen FunctionFunction

Creates an empty .tdms file in memory for reading or writing. You also can use this
function to create a file in memory from a byte array or file on disk.

Use the TDMS In Memory Close function to close the reference to this file.


Inputs/Outputs

   •      byte array or file path —

    byte array or file path specifies the byte array or file path from which to create a .tdms file in
    memory. The byte order of the byte array or file on disk, if specified, determines the byte order
     of the .tdms file in memory this function creates.

       If you do not specify byte array or file path, this function creates an empty .tdms file in
   memory that uses the byte order of the host computer.
   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     tdms file out —

                                                    © National Instruments 1643

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1643 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1644 ordinal=1644 -->
## Functions

Functions


          tdms file out returns a TDMS file reference to the .tdms file on which you performed the
             operation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Advanced Read and Write\
        TDMS In Memory Write and Read.vi
            • labview\examples\File IO\TDMS\Advanced Read and Write\In
        Memory Network Read and Write\TDMS In Memory Network Read
        and Write.lvproj
   TDMSTDMS InIn MemoryMemory ReadRead BytesBytes FunctionFunction

      Reads a .tdms file in memory and returns data as an unsigned 8-bit integer array data
       type.


      Inputs/Outputs

               •      byte count (-1: all) —

            byte count specifies the maximum number of bytes to read from the .tdms file in memory. The
             default is -1, which means this function reads all available bytes.

                    If the value of byte count is out of range, this function automatically sets byte count to equal the
          number of bytes in the file minus offset.
               •       offset (0) —

1644   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1644 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1645 ordinal=1645 -->
## Functions

Functions


     offset specifies the number of bytes into the .tdms file at which the function begins reading the
   .tdms file. The default is 0.

   •     tdms file —

   tdms file specifies a reference number to the .tdms file in memory on which to perform the
    operation. Use the TDMS In Memory Open function to open the refnum.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     tdms file out —

   tdms file out returns a TDMS file reference to the .tdms file on which you performed the
    operation.

   •      data —

    data returns the data read from the .tdms file in memory as an unsigned 8-bit integer array
    data type.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Advanced Read and Write\
   TDMS In Memory Write and Read.vi
  • labview\examples\File IO\TDMS\Advanced Read and Write\In
   Memory Network Read and Write\TDMS In Memory Network Read
   and Write.lvproj


                                                    © National Instruments 1645

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1645 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1646 ordinal=1646 -->
## Functions

Functions

   TDMSTDMS InIn MemoryMemory CloseClose FunctionFunction

       Closes the .tdms file in memory that you opened with the TDMS In Memory Open
       function. This function also writes the .tdms file to disk, if specified by the file path
       input.


      Inputs/Outputs

               •      overwrite (F) —

            overwrite specifies whether to overwrite the file you specify in file path with the .tdms file in
          memory. The default is FALSE, which means that this VI does not overwrite the file.

               •        file path —

                file path specifies the absolute path to the file on disk that you want to write the .tdms file in
          memory.

               •     tdms file —

          tdms file specifies a reference number to the .tdms file in memory on which to perform the
             operation. Use the TDMS In Memory Open function to open the refnum.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

1646   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1646 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1647 ordinal=1647 -->
## Functions

Functions

  • labview\examples\File IO\TDMS\Advanced Read and Write\
   TDMS In Memory Write and Read.vi
  • labview\examples\File IO\TDMS\Advanced Read and Write\In
   Memory Network Read and Write\TDMS In Memory Network Read
   and Write.lvproj

Storage/DataPluginStorage/DataPlugin

Use the Storage/DataPlugin VIs to read measurement data from a variety of file
formats, write data to .tdm or .tdms files, or manage DataPlugins installed on the local
computer. You must download appropriate DataPlugins and register them on the local
computer before you can access the corresponding file formats. Refer to the National
Instruments website at ni.com/dataplugins to download DataPlugins.

      Note If you build an installer for a stand-alone application or shared library
        that uses the Storage/DataPlugin VIs, you must include the NI USI installer. To
        include the NI USI installer, on the Additional Installers page of the Installer
        Properties dialog box, remove the checkmark from the Automatically select
      recommended installers checkbox and place a checkmark in the NI USI
       checkbox.

The VIs on this palette can return storage error codes.


 Palette
             Description
 Object

           Opens an NI TDM (.tdm) file for reading or writing. You also can use this VI to create a
 Open Data
          new file or replace an existing file. Use the Close Data Storage VI to close the reference
 Storage
              to the file.

            Adds a channel group or channel to a file you specify. You also can use this VI to
 Write Data
              define properties for the channel group or channel that you want to add.

             Returns an array of refnums that represent channel groups or channels in the file. If
 Read Data   you select Channel as the Object type to read in the configuration dialog box, this VI
             reads waveforms associated with the channel. You also can use this VI to return

                                                    © National Instruments 1647

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1647 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1648 ordinal=1648 -->
## Functions

Functions


         Palette                     Description
        Object

                    channel groups or channels that meet query conditions you specify.

                     Closes a data file. You must use this Express VI to close a data file after you finish         Close Data                     reading from or writing to the file. Memory leakage might occur if you do not close the         Storage
                     data file.

                      Defines the properties of an existing file, channel group, or channel. If you configure
                         this VI before you wire a refnum to storage refnum, the configuration might change         Set                   depending on the refnum you wire. For example, if you configure this VI for a channel         Properties                  and then wire a channel group refnum, the VI returns broken wires on the block
                   diagram because the same properties are not available for a channel group.

                   Reads property values from a file, channel group, or channel. If you configure this VI
                     before you wire a refnum to storage refnum, the configuration might change        Get                   depending on the refnum you wire. For example, if you configure this VI for a channel         Properties
                  and then wire a channel group refnum, the VI returns broken wires on the block
                   diagram because the same properties are not available for a channel group.

                  Removes a channel group or channel you specify. If you choose to delete a channel
                     group, this VI deletes all channels associated with that channel group. Wire data to         Delete Data
                     the storage refnum input to determine the polymorphic instance to use or manually
                        select the instance.


        Data File    Opens the data file specified in the file path input and presents the data in the Data
        Viewer        File Viewer dialog box.

        Convert to
      TDM or      Converts the specified file to the .tdm or .tdms file format.
      TDMS

       Manage     Use the Manage DataPlugins VIs to list, export, register, or unregister DataPlugins
         DataPlugins  installed on the local computer.


        Advanced   Use the Advanced Storage VIs to read, write, and query data when object types or
         Storage      property names are determined at run time.


1648   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1648 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1649 ordinal=1649 -->
## Functions

Functions

OpenOpen DataData StorageStorage

Opens an NI TDM (.tdm) file for reading or writing. You also can use this VI to create a
new file or replace an existing file. Use the Close Data Storage VI to close the reference
to the file.

      Note You must download appropriate DataPlugins and register them on the
        local computer before you can access the corresponding data files. Refer to
       the National Instruments website at ni.com/dataplugins to download
        DataPlugins.


Dialog Box Options

 Option      Description

               Specifies the format of the file you want to access. If you wire a value to the
             DataPlugin name block diagram input of this Express VI, LabVIEW ignores the
             DataPlugin option. If you wire an empty string to the DataPlugin name block
             diagram input, LabVIEW automatically detects the storage format of the data file.

             Contains the following options:

                       • auto-detect the storage format—Automatically detects the storage format of the
 DataPlugin      data file you specify in the File location option or the file path block diagram
                   input.
                       • TDM Streaming (high performance)—Opens or replaces an existing .tdms file or
                   creates a new .tdms file. This storage format has a higher performance
               compared to the TDM with XML Header storage format.
                       • TDM with XML Header (medium performance)—Opens or replaces an existing
                 .tdm file or creates a new .tdm file.
                       • CSV—Opens an existing data file with comma-separated values (CSV).
                       • DAT—Opens an existing .dat file.


                                                    © National Instruments 1649

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1649 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1650 ordinal=1650 -->
## Functions

Functions


        Option      Description

                                   • LVM—Opens an existing text-based measurement file (.lvm).

                         Tip Click the Install/Update DataPlugins button on this dialog box to
                          download more DataPlugins from ni.com and install more storage
                              formats to this list.


                     Contains the following option:
        DataPlugin
        parameters      •  File location—
             (if not
        wired)            Specifies the location of the file you want to open.


                        Specifies the operation to perform.

                     Contains the following options:

                                   • open—Opens an existing file.
                                   • open or create—Opens an existing file or creates a new file if one does not exist.
                                   • create or replace—Creates a new file or replaces a file if it exists and you give
                          permission. This Express VI replaces a file by opening the file and setting its end        Overwrite
                            of file to 0.        options (if
                                   • create—Creates a new file.        not wired)
                                   • open (read only)—Opens an existing file for read only.

                      Note Only TDM and TDMS files support all the options listed above. If the
                              DataPlugin you specify in the DataPlugin list is not a .tdms or .tdm file,
                           LabVIEW uses the open (read only) option by default to open the data file.
                           To write to the data file, you can wire a create or create or replace control
                                to the function (open:0) block diagram input.


          Install/      Launches the Install/Update DataPlugins dialog box which allows you to search,
        Update        install, and update DataPlugins from the National Instruments website at ni.com/
        DataPlugins  dataplugins.


1650   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1650 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1651 ordinal=1651 -->
## Functions

Functions

Inputs/Outputs

   •        file path —

     Specifies the full path of the file you want to open.

   •      function (open:0) —

     Specifies the operation to perform.

   •      DataPlugin name —

     Specifies the name of the DataPlugin, which determines the storage format of the data file. To
    open an external data file, you first must install the correct National Instruments DataPlugins.
    Refer to the National Instruments website at ni.com/dataplugins to download DataPlugins. If
    you do not wire data to this input, LabVIEW uses the value that you specify in the DataPlugin
    dialog box option. If you wire data to this input, LabVIEW ignores the value of the DataPlugin
    option. If you wire an empty string to this input, LabVIEW automatically detects the storage
    format of the data file.

   •      additional parameters —

     Specifies additional parameters for the input DataPlugin.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage refnum (file) —

    Generates a refnum to the file this Express VI opened.

   •      DataPlugin name out —

    Returns DataPlugin name unchanged. If you do not wire data to the DataPlugin name input,
    DataPlugin name out returns the value that you specify in the DataPlugin dialog box option. If
    you wire an empty string to the DataPlugin name input, DataPlugin name out returns the
    storage format that LabVIEW automatically detects.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1651

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1651 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1652 ordinal=1652 -->
## Functions

Functions

       WriteWrite DataData

      Adds a channel group or channel to a file you specify. You also can use this VI to define
       properties for the channel group or channel that you want to add.

      You also can use the Write To Measurement File Express VI to write data to a .tdm,
      .tdms, or .lvm file.


      Dialog Box Options

        Option     Description

                    Contains the following options:

                                 • Object type—

                          Specifies the type of object to add to the file.

                        Contains the following options:
           ◦ Channel group—Adds a channel group to the file.
           ◦ Channel—Adds a channel to the file.
                                 • Always create new channel group/channel—
         Settings
                          Specifies whether to append existing channel groups or channels of the same
                     name. If you do not want to append existing channel groups or channels, place a
                     checkmark in this checkbox.

                   When a channel name is repeated, LabVIEW appends an integer to the end of the
                    names to enforce unique channel names. For example, if you provide the channel
                    names sine, sine, square, square, and sine, LabVIEW updates these names
                         to sine, sine 1, square, square 1, and sine 2, respectively.

         Properties Contains the following options:


1652   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1652 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1653 ordinal=1653 -->
## Functions

Functions


Option     Description

                    • TDM Properties—Use the TDM Properties tab to edit predefined properties and
                create user-defined properties for .tdm and .tdms files. Click the Insert button
                to add a new property to configure. Click the Delete button to remove the selected
                 property. For predefined properties, you can edit only the Source and Value
               columns.
       ◦ Source—Use the Source column to specify the input source of the property
                     information. The Source column contains the following options:
         ▪ Terminal—Select this option if you want to specify the property
                        information on the block diagram.
         ▪ Ignore—Select this option if you do not want to write any of the property
                        information on the specified row to the file.
         ▪ Value—Select this option if you want to specify the property information
                    on the TDM Properties tab.
       ◦ Name—Use the Name column to specify the property name. The property
               name cannot contain any spaces or special characters. LabVIEW automatically
                    replaces spaces and special characters with an underscore. This column
                    contains the following predefined property names:
         ▪ Name—Specifies the name of the object you select in Object type.
         ▪ Description—Specifies the description of the object you select in Object
                         type.
         ▪ Channel group—Specifies the channel group object for the data channel.
                         This property appears only if you select Channel in Object type.
         ▪ Unit—Specifies the unit of the channel values. This property appears only
                                        if you select Channel in Object type.
         ▪ Waveform length—Specifies the number of samples in the waveform.
                         This property appears only if you select Channel in Object type
         ▪ Waveform x dimension—Specifies the name of the xdimension of the
                      waveform. This property appears only if you select Channel in Object
                         type.
         ▪ Waveform x unit—Specifies the unit of the xdimension of the waveform.
                         This property appears only if you select Channel in Object type.
         ▪ Waveform timestamp—Specifies the time stamp of the first sample in the
                      waveform. This property appears only if you select Channel in Object
                         type.
         ▪ Waveform offset—Specifies the starting point in the waveform. This
                        property appears only if you select Channel in Object type.
         ▪ Waveform increment—Specifies the time interval between every two
                        adjacent samples in the waveform. This property appears only if you
                          select Channel in Object type.


                                                    © National Instruments 1653

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1653 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1654 ordinal=1654 -->
## Functions

Functions


        Option     Description

             ▪ Waveform time mode—Specifies the time mode of the waveform. You
                              can specify either an absolute or relative time mode. This property
                               appears only if you select Channel in Object type.
           ◦ Value—Use the Value column to specify the property value. The format of
                           Value is determined by your selection in the Data Type column. The value in
                                 this column is not used if you selected the Terminal option in the Source
                          column.
           ◦ Data Type—Use the Data Type column to specify the data type of the Value
                          column. The Data Type column contains the following options:
             ▪ STR—Select this option to specify Value as a string.
             ▪ DBL—Select this option to specify Value as a double-precision, floating-
                                 point number.
             ▪ TIME—Select this option to specify Value as a timestamp value.
             ▪ I32—Select this option to specify Value as a long integer number.
           ◦  Insert—Inserts a new input at the top of the list.
           ◦ Delete—Deletes the selected input from the list.
                                 • DAQmx—Use the DAQmx Properties tab to select and edit DAQmx property names
                            for .tdm and .tdms files.

                   Options in this section are available only if you select Channel as the Object type.
                    Contains the following options:

                                 • Show terminals for data channel—

                         Displays terminals for Signal, append/replace (append data values), and index on        Measured
                        the block diagram.        data
        channel                                 • Append/replace data values—Contains the following options:
           ◦ Append—Appends new values to the end of existing values.
           ◦ Replace at index—Replaces all existing values with new values.
           ◦ Replace all—Replaces values at the index you wire to index on the block
                            diagram.


      Inputs/Outputs

               •      storage refnum (file) —

             Specifies the reference number for the .tdm and .tdms file you want to access. You must wire a


1654   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1654 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1655 ordinal=1655 -->
## Functions

Functions


   file refnum to this input.

•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      index —

  Specifies where to replace values in the waveform. The default is 0.

•     append / replace (append data values) —

  Specifies whether you want to append new values to the end of existing values, replace all
  existing values with new values, or replace values at the index you wire to the index input. This
  input appears only if you place a checkmark in the Show terminals for data channel check box
  in the configuration dialog box.

•      Signal —

  Specifies the signal to add to the an existing channel. This input appears only if you specify
  Channel as the Object type in the configuration dialog box.

        Note The Storage/DataPlugin VIs do not support strings that contain binary data.
          You must first convert the string to an unsigned byte array using the String to Byte
           Array function. If you do not convert the string, the Write Data Express VI writes only
           the portion of the string before the first NULL character.

•      storage refnum (file) out —

  Returns a reference number for the .tdm and .tdms file this Express VI accesses. You can wire
   this refnum to another VI to complete another operation on the same file.

•       error out —

  error out contains error information. This output provides standard error out functionality.

•      storage refnum (channel) —

  Returns an array of refnums that represent the channel groups or channels in the file. If you
  select a property from the configuration dialog box and wire a value to compare to the
  Comparison input, this refnum returns the channel groups or channels that meet the query
  condition. If you do not specify a value to compare, this refnum returns all channel groups or


                                                   © National Instruments 1655

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1655 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1656 ordinal=1656 -->
## Functions

Functions


            channels.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\DataPlugins\TDM\TDM Event Data\
        TDM Event Data.lvproj

     ReadRead DataData

       Returns an array of refnums that represent channel groups or channels in the file. If
      you select Channel as the Object type to read in the configuration dialog box, this VI
       reads waveforms associated with the channel. You also can use this VI to return
      channel groups or channels that meet query conditions you specify.

      Use the Set Properties Express VI to define properties and the Get Properties Express VI
       to return properties for the channel groups or channels this Express VI returns.

      You also can use the Read From Measurement File Express VI to read data from a .tdm,
      .tdms, or .lvm file.


      Dialog Box Options

        Option    Description

                   Contains the following options:
       Read
         Settings       • Object type to read—


1656   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1656 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1657 ordinal=1657 -->
## Functions

Functions


Option    Description

                Specifies the type of object to return.

               Contains the following options:
       ◦ Channel group—Returns channel groups in the file.
       ◦ Channel—Returns channels in the channel group or file.

           Contains the following options:

                   • Property to compare—

                Specifies the property to compare when performing the query. If you select a
               property from this list, a corresponding input and the Comparison input appear on
               the block diagram. This Express VI compares the value you wire to the property to
               the channels or channel groups the storage refnum identifies and returns channels
               or channel groups that meet the comparison condition.

       ◦ query all data—Returns all data.
       ◦ Name—Name of the channel group or channel.
       ◦ Description—Description of the channel group or channel.
Query    ◦ Unit—Name of a unit. This property is available only when you select Channel
                   as the Data type.
       ◦ Data type—Data type of the channel. This property is available only when you
                     select Channel as the Object type to read.
       ◦ Minimum—Minimum value of the channel. This property is available only
               when you select Channel as the Object type to read.
       ◦ Maximum—Maximum value of the channel. This property is available only
               when you select Channel as the Object type to read.
                   • Include only channels from the wired channel group—

                Specifies whether to query all channels in the file or only channels in the channel
               group. In order to place a checkmark in this checkbox, the incoming refnum must
             be a channel group.

           Contains the following options:

                   • Show terminals—Measured
data
               Displays a terminal for Signal on the block diagram.
channels
                   • Output data channel as—Specifies the data type of the output. This option is


                                                    © National Instruments 1657

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1657 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1658 ordinal=1658 -->
## Functions

Functions


        Option    Description

                         available only if you select Channel as the Object type to read and you place a
                     checkmark in the Show terminals checkbox. Contains the following options:
           ◦ Dynamic data type—Returns the output signals formatted as dynamic data.
           ◦ Array of waveforms—Returns the output signals formatted as a 1D array of
                          waveforms.
           ◦ Array of strings—Returns the output signals formatted as a 2D array of strings.
           ◦ Array of doubles—Returns the output signals formatted as a 2D array of
                             double-precision, floating-point numbers.
           ◦ Array of singles—Returns the output signals formatted as a 2D array of single-
                               precision, floating-point numbers.
           ◦ Array of I32—Returns the output signals formatted as a 2D array of 32-bit
                           signed integers.
           ◦ Array of I16—Returns the output signals formatted as a 2D array of 16-bit
                           signed integers.
           ◦ Array of U8—Returns the output signals formatted as a 2D array of 8-bit
                          unsigned integers.
           ◦ Array of time stamps—Returns the output signals formatted as a 2D array of
                          time stamp values.


      Inputs/Outputs

               •      storage refnum (file) —

             Specifies the reference number for the data object you want to access. After you wire a file
           refnum to this input, the label changes from storage refnum to storage refnum (file). After you
            wire a channel group refnum to this input, the label changes from storage refnum to storage
          refnum (channel group). After you wire a channel refnum to this input, the label changes from
            storage refnum to storage refnum (channel).

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      index —

             Specifies where this Express VI starts reading values from a channel. This input appears only if
           you select Channel as the Object type and if you place a checkmark in the Show terminals for
           data channel check box in the configuration dialog box.


1658   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1658 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1659 ordinal=1659 -->
## Functions

Functions

   •      count —

     Specifies the number of values for this Express VI to read from a channel. This input appears only
       if you select Channel as the Object type and if you place a checkmark in the Show terminals for
    data channel check box in the configuration dialog box.

   •      storage refnum (file) out —

    Returns a reference number for the data object this Express VI accesses. You can wire this refnum
    to another VI to complete another operation on the same object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      storage refnums (channel) —

    Returns an array of refnums that represent the channel groups or channels in the file. If you
     select a property from the configuration dialog box and wire a value to compare to the
    Comparison input, this refnum returns the channel groups or channels that meet the query
    condition. If you do not specify a value to compare, this refnum returns all channel groups or
    channels.

   •      Signal —

    Returns a signal formatted according to the data type you specified in the configuration dialog
    box. This output appears only if you select Channel as the Object type and if you place a
    checkmark in the Show terminals for data channel check box in the configuration dialog box.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\DataPlugins\TDM\TDM Event Data\
   TDM Event Data.lvproj

CloseClose DataData StorageStorage

Closes a data file. You must use this Express VI to close a data file after you finish
reading from or writing to the file. Memory leakage might occur if you do not close the
data file.


                                                    © National Instruments 1659

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1659 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1660 ordinal=1660 -->
## Functions

Functions


      Dialog Box Options
      Inputs/Outputs

               •      storage refnum —
             Specifies the reference number for the data object you want to access. After you wire a file
           refnum to this input, the label changes from storage refnum to storage refnum (file). After you
            wire a channel group refnum to this input, the label changes from storage refnum to storage
          refnum (channel group). After you wire a channel refnum to this input, the label changes from
            storage refnum to storage refnum (channel).
               •       error in (no error) —
            Describes error conditions that occur before this node runs.
               •        file path —
            Returns the path that corresponds to storage refnum.
               •       error out —
            Contains error information. This output provides standard error out functionality.

      SetSet PropertiesProperties

       Defines the properties of an existing file, channel group, or channel. If you configure
        this VI before you wire a refnum to storage refnum, the configuration might change
      depending on the refnum you wire. For example, if you configure this VI for a channel
      and then wire a channel group refnum, the VI returns broken wires on the block
      diagram because the same properties are not available for a channel group.


1660   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1660 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1661 ordinal=1661 -->
## Functions

Functions

Dialog Box Options

 Option     Description

            Contains the following options:

                     • Object type—

                  Specifies the type of object to add to the file. Settings
        ◦ File—Sets properties for a file.
        ◦ Channel group—Sets properties for a channel group.
        ◦ Channel—Sets properties for a channel.

            Contains the following options:

                     • TDM Properties—Use the TDM Properties tab to edit predefined properties and
                 create user-defined properties for .tdm and .tdms files. Click the Insert button
                 to add a new property to configure. Click the Delete button to remove the selected
                 property. For predefined properties, you can edit only the Source and Value
                columns.
        ◦ Source—Use the Source column to specify the input source of the property
                     information. The Source column contains the following options:
         ▪ Terminal—Select this option if you want to specify the property
                         information on the block diagram.
         ▪ Ignore—Select this option if you do not want to write any of the property
                         information on the specified row to the file.
         ▪ Value—Select this option if you want to specify the property information
 Properties            on the TDM Properties tab.
        ◦ Name—Use the Name column to specify the property name. The property
                name cannot contain any spaces or special characters. LabVIEW automatically
                     replaces spaces and special characters with an underscore. This column
                     contains the following predefined property names:
         ▪ Name—Specifies the name of the object you select in Object type.
         ▪ Description—Specifies the description of the object you select in Object
                          type.
         ▪  Title—Specifies the title of the data set in the .tdm or .tdms file. This
                         property appears only if you select File in Object type.
         ▪ Author—Specifies the author of the data set in the .tdm or .tdms file.
                          This property appears only if you select File in Object type.
         ▪ Time stamp—Specifies the time and date information when you last
                       saved the data set in the .tdm or .tdms file. This property appears only


                                                    © National Instruments 1661

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1661 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1662 ordinal=1662 -->
## Functions

Functions


        Option     Description

                                                       if you select File in Object type.
             ▪ Unit—Specifies the unit of the channel values. This property appears only
                                                       if you select Channel in Object type.
             ▪ Waveform length—Specifies the number of samples in the waveform.
                                  This property appears only if you select Channel in Object type
             ▪ Waveform x dimension—Specifies the name of the xdimension of the
                              waveform. This property appears only if you select Channel in Object
                                  type.
             ▪ Waveform x unit—Specifies the unit of the xdimension of the waveform.
                                  This property appears only if you select Channel in Object type.
             ▪ Waveform timestamp—Specifies the time stamp of the first sample in the
                              waveform. This property appears only if you select Channel in Object
                                  type.
             ▪ Waveform offset—Specifies the starting point in the waveform. This
                                property appears only if you select Channel in Object type.
             ▪ Waveform increment—Specifies the time interval between every two
                                adjacent samples in the waveform. This property appears only if you
                                    select Channel in Object type.
             ▪ Waveform time mode—Specifies the time mode of the waveform. You
                              can specify either an absolute or relative time mode. This property
                               appears only if you select Channel in Object type.
           ◦ Value—Use the Value column to specify the property value. The format of
                           Value is determined by your selection in the Data Type column. The value in
                                 this column is not used if you selected the Terminal option in the Source
                          column.
           ◦ Data Type—Use the Data Type column to specify the data type of the Value
                          column. The Data Type column contains the following options:
             ▪ STR—Select this option to specify Value as a string.
             ▪ DBL—Select this option to specify Value as a double-precision, floating-
                                 point number.
             ▪ TIME—Select this option to specify Value as a timestamp value.
             ▪ I32—Select this option to specify Value as a long integer number.
           ◦  Insert—Inserts a new input at the top of the list.
           ◦ Delete—Deletes the selected input from the list.
                                 • DAQmx—Use the DAQmx Properties tab to select and edit DAQmx property names
                            for .tdm and .tdms files.

        Measured
                   Options in this section are available only if you select Channel as the Object type.
        data
                    Contains the following options:
        channel

1662   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1662 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1663 ordinal=1663 -->
## Functions

Functions


 Option     Description

                     • Show terminals for data channel—

                 Displays terminals for Signal, append/replace (append data values), and index on
                the block diagram.

                     • Append/replace data values—Contains the following options:
        ◦ Append—Appends new values to the end of existing values.
        ◦ Replace at index—Replaces all existing values with new values.
        ◦ Replace all—Replaces values at the index you wire to index on the block
                    diagram.


Inputs/Outputs

   •      storage refnum (channel) —

     Specifies the reference number for the data object you want to access. After you wire a file
    refnum to this input, the label changes from storage refnum to storage refnum (file). After you
    wire a channel group refnum to this input, the label changes from storage refnum to storage
    refnum (channel group). After you wire a channel refnum to this input, the label changes from
    storage refnum to storage refnum (channel).

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      index —

     Specifies where to replace values in the waveform. The default is 0.

   •     append / replace (append data values) —

     Specifies whether you want to append new values to the end of existing values, replace all
     existing values with new values, or replace values at the index you wire to the index input. This
    input appears only if you place a checkmark in the Show terminals for data channel check box
     in the configuration dialog box.

   •     Name —

     Specifies the name of the object you select in Object type.


                                                    © National Instruments 1663

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1663 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1664 ordinal=1664 -->
## Functions

Functions

               •      Description —

             Specifies the description of the object you select in Object type.

               •      Unit —

             Specifies the unit of the channel values. This property appears only if you select Channel in
            Object type.

               •      Signal —

             Specifies the signal to add to the an existing channel. This input appears only if you specify
           Channel as the Object type in the configuration dialog box.

               Note The Storage/DataPlugin VIs do not support strings that contain binary data.
                   You must first convert the string to an unsigned byte array using the String to Byte
                      Array function. If you do not convert the string, the Write Data Express VI writes only
                     the portion of the string before the first NULL character.

               •      storage refnum (channel) out —

            Returns a reference number for the data object this Express VI accesses. You can wire this refnum
             to another VI to complete another operation on the same object.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      GetGet PropertiesProperties

      Reads property values from a file, channel group, or channel. If you configure this VI
       before you wire a refnum to storage refnum, the configuration might change
      depending on the refnum you wire. For example, if you configure this VI for a channel
      and then wire a channel group refnum, the VI returns broken wires on the block
      diagram because the same properties are not available for a channel group.


1664   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1664 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1665 ordinal=1665 -->
## Functions

Functions


Dialog Box Options

 Option     Description

            Contains the following options:

                     • Object type—

                  Specifies the type of data for which you want to get properties. Settings
        ◦ File—Reads properties from a file.
        ◦ Channel group—Reads properties from a channel group.
        ◦ Channel—Reads properties from a channel.

            Contains the following options:

                     • TDM Properties—Use the TDM Properties tab to edit predefined properties and
                 create user-defined properties for .tdm and .tdms files. Click the Insert button
                 to add a new property to configure. Click the Delete button to remove the selected
                 property. For predefined properties, you can edit only the Source and Value
                columns.
        ◦ Source—Use the Source column to specify the input source of the property
                     information. The Source column contains the following options:
         ▪ Terminal—Select this option if you want to specify the property
                         information on the block diagram.
 Properties         ▪ Ignore—Select this option if you do not want to write any of the property
                         information on the specified row to the file.
        ◦ Name—Use the Name column to specify the property name. The property
                name cannot contain any spaces or special characters. LabVIEW automatically
                     replaces spaces and special characters with an underscore. This column
                     contains the following predefined property names:
         ▪ Name—Specifies the name of the object you select in Object type.
         ▪ Description—Specifies the description of the object you select in Object
                          type.
         ▪  Title—Specifies the title of the data set in the .tdm or .tdms file. This


                                                    © National Instruments 1665

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1665 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1666 ordinal=1666 -->
## Functions

Functions


        Option     Description

                                property appears only if you select File in Object type.
             ▪ Author—Specifies the author of the data set in the .tdm or .tdms file.
                                  This property appears only if you select File in Object type.
             ▪ Time stamp—Specifies the time and date information when you last
                              saved the data set in the .tdm or .tdms file. This property appears only
                                                       if you select File in Object type.
             ▪ Channel groups—Specifies the channel group objects for the data set in
                                the .tdm or .tdms file. This property appears only if you select File in
                               Object type.
             ▪  File—Specifies the file object for the channel group. This property
                               appears only if you select Channel group in Object type.
             ▪ Channels—Specifies the channel objects for the channel group. This
                                property appears only if you select Channel group in Object type.
             ▪ Channel group—Specifies the channel group object for the data channel.
                                  This property appears only if you select Channel in Object type.
             ▪ Unit—Specifies the unit of the channel values. This property appears only
                                                       if you select Channel in Object type.
             ▪ Data type—Specifies the data type of the channel values. This property
                               appears only if you select Channel in Object type.
             ▪ Minimum—Specifies the lowest channel value. This property appears
                                 only if you select Channel in Object type.
             ▪ Maximum—Specifies the highest channel value. This property appears
                                 only if you select Channel in Object type.
             ▪ Waveform length—Specifies the number of samples in the waveform.
                                  This property appears only if you select Channel in Object type
             ▪ Waveform x dimension—Specifies the name of the xdimension of the
                              waveform. This property appears only if you select Channel in Object
                                  type.
             ▪ Waveform x unit—Specifies the unit of the xdimension of the waveform.
                                  This property appears only if you select Channel in Object type.
             ▪ Waveform timestamp—Specifies the time stamp of the first sample in the
                              waveform. This property appears only if you select Channel in Object
                                  type.
             ▪ Waveform offset—Specifies the starting point in the waveform. This
                                property appears only if you select Channel in Object type.
             ▪ Waveform increment—Specifies the time interval between every two
                                adjacent samples in the waveform. This property appears only if you
                                    select Channel in Object type.
             ▪ Waveform time mode—Specifies the time mode of the waveform. You


1666   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1666 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1667 ordinal=1667 -->
## Functions

Functions


Option     Description

                      can specify either an absolute or relative time mode. This property
                       appears only if you select Channel in Object type.
       ◦ Value—Use the Value column to specify the property value. The format of
                   Value is determined by your selection in the Data Type column. The value in
                       this column is not used if you selected the Terminal option in the Source
                  column.
       ◦ Data Type—Use the Data Type column to specify the data type of the Value
                  column. The Data Type column contains the following options:
         ▪ STR—Select this option to specify Value as a string.
         ▪ DBL—Select this option to specify Value as a double-precision, floating-
                        point number.
         ▪ TIME—Select this option to specify Value as a timestamp value.
         ▪ I32—Select this option to specify Value as a long integer number.
       ◦  Insert—Inserts a new input at the top of the list.
       ◦ Delete—Deletes the selected input from the list.
                    • DAQmx—Use the DAQmx Properties tab to select and edit DAQmx property names
                  for .tdm and .tdms files.

           Contains the following options:

                    • Show terminals for data channel—

                Displays terminals for Signal, index, and count on the block diagram.

                    • Output data channel as—

                 Specifies the data type of the output. This option is available only if you select
              Channel as the Object type and if you place a checkmark in the Show terminals
Measured       for data channel check box.
data
       ◦ Dynamic data type—Returns the output signal formatted as dynamic data.channel
       ◦ Waveform—Returns the output signal formatted as a waveform.
       ◦ Array of strings—Returns the output signal formatted as a 1D array of strings.
       ◦ Array of doubles—Returns the output signal formatted as a 1D array of
                     double-precision, floating-point numbers.
       ◦ Array of singles—Returns the output signal formatted as a 1D array of single-
                      precision, floating-point numbers.
       ◦ Array of I32—Returns the output signal formatted as a 1D array of 32-bit
                   signed integers.
       ◦ Array of I16—Returns the output signal formatted as a 1D array of 16-bit


                                                    © National Instruments 1667

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1667 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1668 ordinal=1668 -->
## Functions

Functions


        Option     Description

                            signed integers.
           ◦ Array of U8—Returns the output signal formatted as a 1D array of 8-bit
                           unsigned integers.
           ◦ Array of time stamps—Returns the output signal as a 1D array of time stamp
                               values.


      Inputs/Outputs

               •      storage refnum (channel) —

             Specifies the reference number for the data object you want to access. After you wire a file
           refnum to this input, the label changes from storage refnum to storage refnum (file). After you
            wire a channel group refnum to this input, the label changes from storage refnum to storage
          refnum (channel group). After you wire a channel refnum to this input, the label changes from
            storage refnum to storage refnum (channel).

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      index —

             Specifies where this Express VI starts reading values from a channel. This input appears only if
           you select Channel as the Object type and if you place a checkmark in the Show terminals for
           data channel check box in the configuration dialog box.

               •      count —

             Specifies the number of values for this Express VI to read from a channel. This input appears only
                    if you select Channel as the Object type and if you place a checkmark in the Show terminals for
           data channel check box in the configuration dialog box.

               •      storage refnum (channel) out —

            Returns a reference number for the data object this Express VI accesses. You can wire this refnum
             to another VI to complete another operation on the same object.

               •       error out —


1668   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1668 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1669 ordinal=1669 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

   •     Name —

     Specifies the name of the object you select in Object type.

   •      Unit —

     Specifies the unit of the channel values. This property appears only if you select Channel in
    Object type.

   •      Signal —

    Returns a signal formatted according to the data type you specified in the configuration dialog
    box. This output appears only if you select Channel as the Object type and if you place a
    checkmark in the Show terminals for data channel check box in the configuration dialog box.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\DataPlugins\TDM\TDM Channel
   Groups\TDM Channel Groups.lvproj

DeleteDelete DataData

Removes a channel group or channel you specify. If you choose to delete a channel
group, this VI deletes all channels associated with that channel group. Wire data to the
storage refnum input to determine the polymorphic instance to use or manually select
the instance.

      Note This VI does not delete data in .tdms files.


  • Delete Channel VI


                                                    © National Instruments 1669

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1669 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1670 ordinal=1670 -->
## Functions

Functions

            • Delete Channel Group VI
    DeleteDelete ChannelChannel VIVI

      Removes a channel group or channel you specify. If you choose to delete a channel
       group, this VI deletes all channels associated with that channel group. Wire data to the
       storage refnum input to determine the polymorphic instance to use or manually select
       the instance.

           Note This VI does not delete data in .tdms files.


      Inputs/Outputs

               •      storage refnum (channel) —

            storage refnum (channel) specifies the channel to remove.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    DeleteDelete ChannelChannel GroupGroup VIVI

      Removes a channel group or channel you specify. If you choose to delete a channel
       group, this VI deletes all channels associated with that channel group. Wire data to the
       storage refnum input to determine the polymorphic instance to use or manually select
       the instance.


1670   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1670 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1671 ordinal=1671 -->
## Functions

Functions

      Note This VI does not delete data in .tdms files.


Inputs/Outputs

   •      storage refnum (channel group) —

    storage refnum (channel group) specifies the channel group to remove.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


DataData FileFile ViewerViewer

Opens the data file specified in the file path input and presents the data in the Data
File Viewer dialog box.


Inputs/Outputs

   •        file path —

      file path is the absolute path to the file you want to open.

   •      DataPlugin name —

    DataPlugin name specifies the name of the DataPlugin that determines the storage format of


                                                    © National Instruments 1671

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1671 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1672 ordinal=1672 -->
## Functions

Functions


            the data file. Use the List DataPlugins VI to obtain the names of all DataPlugins installed on the
              local computer. If you do not wire data to this input or if you wire an empty string to this input,
              this VI automatically detects the storage format of the data file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •        file path out —

                file path out returns file path unchanged.

               •      DataPlugin name out —

            DataPlugin name out returns DataPlugin name unchanged. If you do not wire the DataPlugin
         name input or if you wire an empty string to this input, DataPlugin name out returns the
            DataPlugin name that this VI detects automatically.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      ConvertConvert toto TDMTDM oror TDMSTDMS

       Converts the specified file to the .tdm or .tdms file format.


      Inputs/Outputs

               •      DataPlugin name —

            DataPlugin name specifies the name of the DataPlugin that determines the storage format of
            the data file. Use the List DataPlugins VI to obtain the names of all DataPlugins installed on the


1672   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1672 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1673 ordinal=1673 -->
## Functions

Functions


  local computer. If you do not wire data to this input or if you wire an empty string to this input,
   this VI automatically detects the storage format of the data file.

•      source file path —

  source file path specifies the path to the data file you want to convert.

•       target file path —

  target file path specifies the path to the new .tdm or .tdms file you want to create.

•       target file operation (3:create) —

  target file operation specifies the operation to perform.

    open  0   —Opens a file to configure.
    open or create  1   —Opens an existing file or creates a new file to configure.
    create or replace  2    —Creates a new file or replaces an existing file.
    create  3    (Default)—Creates a new file.
    open (read only)  4   —Opens a read-only version of the file.

•       target file format (TDMS) —

  target file format specifies the target file format to which you want to convert the data file.

   TDM
  0    —Converts the data file to a .tdm file.
   TDMS
  1     (Default)—Converts the data file to a .tdms file.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      data chunk size (1E+7) —


                                                   © National Instruments 1673

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1673 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1674 ordinal=1674 -->
## Functions

Functions


           data chunk size specifies the number of values to read into memory at a time until this VI
              finishes reading all values. If you have enough system memory, use a higher number than the
             default value to achieve better performance. The default is 1E+7.

               •      DataPlugin name out —

            DataPlugin name out returns DataPlugin name unchanged. If you do not wire the DataPlugin
         name input or if you wire an empty string to this input, DataPlugin name out returns the
            DataPlugin name that this VI detects automatically.

               •      source file path out —

            source file path out returns source file path unchanged.

               •       target file path out —

             target file path out returns target file path unchanged.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     ManageManage DataPluginsDataPlugins

      Use the Manage DataPlugins VIs to list, export, register, or unregister DataPlugins
        installed on the local computer.

           Note DataPlugins are shared between different National Instruments
              products and applications on the local computer. Registering or unregistering
             a DataPlugin might affect these products or applications.

      The VIs on this palette can return storage error codes.


1674   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1674 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1675 ordinal=1675 -->
## Functions

Functions


 Palette             Description
 Object

                Lists all DataPlugins existing on the National Instruments website at ni.com/ List             dataplugins or registered on the local computer. You also can use this VI to search for DataPlugins            a DataPlugin that exists on the local computer or the National Instruments website.


 Export             Exports a DataPlugin that exists on the local computer to a .uri file. DataPlugin


 Register      Registers or installs a DataPlugin to the local computer. You must manually select the
 DataPlugin  polymorphic instance to use.


 Unregister   Unregisters a DataPlugin from the local computer. This VI does not delete the
 DataPlugin  corresponding DataPlugin .uri file or installer from the computer.

ListList DataPluginsDataPlugins

Lists all DataPlugins existing on the National Instruments website at ni.com/
dataplugins or registered on the local computer. You also can use this VI to search for a
DataPlugin that exists on the local computer or the National Instruments website.

      Note Use the Register DataPlugin VI to register or install DataPlugins on the
        local computer.


Inputs/Outputs

   •      DataPlugin name —


                                                    © National Instruments 1675

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1675 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1676 ordinal=1676 -->
## Functions

Functions


            DataPlugin name specifies the name of the DataPlugin you want to search for. If you do not wire
            data to this input or if you wire an empty string to this input, this VI lists all DataPlugins
             registered on the local computer or exist on the National Instruments website.

               •        file extension —

                file extension specifies the file extension of a DataPlugin.

               •      source —

            source specifies the source location where you want to search for the DataPlugins.

           0 local machine (default)—Lists or searches DataPlugins installed on the local computer.
            web—Lists or searches DataPlugins from the National Instruments website at ni.com/           1
              dataplugins.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      DataPlugin information —

            DataPlugin information returns information about each DataPlugin.

                     •     name —

            name returns the name of the DataPlugin.

                     •      version —

                version returns the version information of the DataPlugin.

                     •      type —

               type returns the type of the DataPlugin. This information indicates the programming
               language in which the DataPlugin was created.

                     •      read-only? —

                read-only? indicates whether the DataPlugin is a read-only DataPlugin.


1676   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1676 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1677 ordinal=1677 -->
## Functions

Functions


         •      extensions —

        extensions returns the file extensions you can use with this DataPlugin.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\DataPlugins\General\Manage
   DataPlugins.vi
ExportExport DataPluginDataPlugin

Exports a DataPlugin that exists on the local computer to a .uri file.

      Note You can export only DataPlugins with a type of VBS or VBCrypt. Use the
         List DataPlugins VI to view the type of a DataPlugin.


Inputs/Outputs

   •      DataPlugin URI path (*.uri) —

    DataPlugin URI path (*.uri) specifies the path to which you want to export the DataPlugin.

   •      DataPlugin name —


                                                    © National Instruments 1677

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1677 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1678 ordinal=1678 -->
## Functions

Functions


            DataPlugin name specifies the name of the DataPlugin you want to export.

               •      encrypt? (F) —

            encrypt? specifies whether to encrypt the .uri file when you export the DataPlugin. The
             default is FALSE. This VI ignores this input if you export a DataPlugin with a type of VBCrypt.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      DataPlugin URI path out —

            DataPlugin URI path out returns DataPlugin URI path (*.uri) unchanged.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\DataPlugins\General\Manage
        DataPlugins.vi
    RegisterRegister DataPluginDataPlugin

       Registers or installs a DataPlugin to the local computer. You must manually select the
      polymorphic instance to use.

           Note DataPlugins are shared between different National Instruments
              products and applications on the local computer. Installing/registering or
               uninstalling/unregistering a DataPlugin might affect these products or
                applications.


1678   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1678 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1679 ordinal=1679 -->
## Functions

Functions


  • Register DataPlugin by URI VI
  •  Install DataPlugin by Name VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\DataPlugins\General\Manage
   DataPlugins.vi
  • labview\examples\File IO\DataPlugins\ATML\DataPlugins -
   ATML.lvproj
RegisterRegister DataPluginDataPlugin byby URIURI VIVI

Registers or installs a DataPlugin to the local computer. You must manually select the
polymorphic instance to use.

      Note DataPlugins are shared between different National Instruments
       products and applications on the local computer. Installing/registering or
        uninstalling/unregistering a DataPlugin might affect these products or
        applications.


Inputs/Outputs

   •      DataPlugin URI path (*.uri) —

    DataPlugin URI path (*.uri) specifies the path to the DataPlugin .uri file. You can download
    DataPlugin .uri files from the National Instruments website at ni.com/dataplugins.

   •       error in (no error) —

                                                    © National Instruments 1679

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1679 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1680 ordinal=1680 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      DataPlugin URI path out —

            DataPlugin URI path out returns DataPlugin URI path (*.uri) unchanged.

               •      DataPlugin information —

            DataPlugin information returns information about the DataPlugin that this VI registers on the
              local computer.

                     •     name —

            name returns the name of the DataPlugin.

                     •      version —

                version returns the version information of the DataPlugin.

                     •      type —

               type returns the type of the DataPlugin. This information indicates the programming
               language in which the DataPlugin was created.

                     •      read-only? —

                read-only? indicates whether the DataPlugin is a read-only DataPlugin.

                     •      extensions —

                extensions returns the file extensions you can use with this DataPlugin.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.


1680   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1680 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1681 ordinal=1681 -->
## Functions

Functions

  • labview\examples\File IO\DataPlugins\General\Manage
   DataPlugins.vi
  • labview\examples\File IO\DataPlugins\ATML\DataPlugins -
   ATML.lvproj
InstallInstall DataPluginDataPlugin byby NameName VIVI

Registers or installs a DataPlugin to the local computer. You must manually select the
polymorphic instance to use.

      Note DataPlugins are shared between different National Instruments
       products and applications on the local computer. Installing/registering or
        uninstalling/unregistering a DataPlugin might affect these products or
        applications.


Inputs/Outputs

   •      DataPlugin name —

    DataPlugin name specifies the name of the DataPlugin. You can find the DataPlugin names on
    the National Instruments website at ni.com/dataplugins or use the List DataPlugins VI to list all
    the DataPlugins existing on the website.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      DataPlugin name out —

    DataPlugin name out returns a duplicate of DataPlugin name.

   •      DataPlugin information —


                                                    © National Instruments 1681

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1681 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1682 ordinal=1682 -->
## Functions

Functions


            DataPlugin information returns information about the DataPlugin that this VI installs on the
              local computer.

                     •     name —

            name returns the name of the DataPlugin.

                     •      version —

                version returns the version information of the DataPlugin.

                     •      Type —

               type returns the type of the DataPlugin. This information indicates the programming
               language in which the DataPlugin was created.

                     •      read-only? —

                read-only? indicates whether the DataPlugin is a read-only DataPlugin.

                     •      extensions —

                extensions returns the file extensions you can use with this DataPlugin.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\DataPlugins\General\Manage
        DataPlugins.vi
            • labview\examples\File IO\DataPlugins\ATML\DataPlugins -
        ATML.lvproj


1682   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1682 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1683 ordinal=1683 -->
## Functions

Functions

UnregisterUnregister DataPluginDataPlugin

Unregisters a DataPlugin from the local computer. This VI does not delete the
corresponding DataPlugin .uri file or installer from the computer.

      Note DataPlugins are shared between different National Instruments
       products and applications on the local computer. Registering or unregistering
       a DataPlugin might affect these products or applications.


Inputs/Outputs

   •      DataPlugin name —

    DataPlugin name specifies the name of the DataPlugin you want to unregister.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\DataPlugins\General\Manage
   DataPlugins.vi


                                                    © National Instruments 1683

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1683 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1684 ordinal=1684 -->
## Functions

Functions

      AdvancedAdvanced StorageStorage

      Use the Advanced Storage VIs to read, write, and query data when object types or
       property names are determined at run time.

      The VIs on this palette can return storage error codes.


         Palette                     Description        Object

        Get Object                     Returns information about the object you specify.          Info

        Get
         Property     Retrieves the properties of a data file, channel group, or channel.
          Info

         Set          Defines a property for a file, channel group, or channel. Wire data to the Value input to
         Property    determine the polymorphic instance to use or manually select the instance.


        Get         Returns the value of a property for a file, channel group, or channel. You must
         Property    manually select the polymorphic instance you want to use.


                   Merges two arrays of storage reference numbers into one larger array of refnums. This
        Merge
                        VI works properly only if the two sets of storage refnums are from the same data file.
         Storage
                    Wire data to either of the storage refnums inputs to determine the polymorphic
       Refnums
                      instance to use or manually select the instance.


         Create       Creates a query expression to use with the Execute Query Expression VI to search for
        Query       objects that meet the condition you specify. Wire data to the value input to determine
         Expression  the polymorphic instance to use or manually select the instance.


1684   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1684 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1685 ordinal=1685 -->
## Functions

Functions


 Palette             Description
 Object

 Merge            Merges two query expressions. You can use the Create Query Expression VI to create Query            query expressions that you want to merge. Expressions

 Execute
 Query       Returns data objects that meet the query expression.
 Expression

 Refnum to             Returns the ID for a data object. ID


 ID to        Returns a refnum for an object you specify. Wire data to the storage refnum input to
 Refnum     determine the polymorphic instance to use.

GetGet ObjectObject InfoInfo

Returns information about the object you specify.


Inputs/Outputs

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage read-only —

                                                    © National Instruments 1685

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1685 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1686 ordinal=1686 -->
## Functions

Functions


            storage read-only specifies if the data storage is read only.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •      object type —

            object type returns the data object type (file, channel group, or channel).

               •      storage location —

            storage location returns the file path to the data storage.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      DataPlugin name —

            DataPlugin name returns the DataPlugin name that the data object contains.

   GetGet PropertyProperty InfoInfo

       Retrieves the properties of a data file, channel group, or channel.


      Inputs/Outputs

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


1686   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1686 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1687 ordinal=1687 -->
## Functions

Functions

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.

   •      properties —

    properties returns the properties of the data file, channel group, or channel.

         •      object type —

        object type returns the type of the storage object that you wire to storage refnum.

         •      property name —

        property name returns the name of the property. Use the Set Property VI to create property
        names.

         •      data type —

        data type returns the data type of the storage object.


   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet PropertyProperty

Defines a property for a file, channel group, or channel. Wire data to the Value input to
determine the polymorphic instance to use or manually select the instance.


  • Set Property (String) VI
  • Set Property (DBL) VI
  • Set Property (SGL) VI
  • Set Property (I32) VI
  • Set Property (I16) VI
  • Set Property (U8) VI

                                                    © National Instruments 1687

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1687 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1688 ordinal=1688 -->
## Functions

Functions

            • Set Property (Enum) VI
            • Set Property (Time Stamp) VI
            • Set Property (Storage Refnum) VI
            • Set Property (Storage Refnums) VI
    SetSet PropertyProperty (String)(String) VIVI

       Defines a property for a file, channel group, or channel. Wire data to the Value input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Create if not found (no:F) —

            Create if not found specifies whether the VI creates a new property with the values you set if the
            property specified in Property name does not exist. The default is FALSE, which means the VI
           does not create a property and returns an error if the specified property does not exist.

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      Property name —

            Property name specifies the name of the property. Use the Get Property Info VI to obtain the
            Property name.

               •      Value —

            Value specifies the value of the property.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


1688   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1688 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1689 ordinal=1689 -->
## Functions

Functions

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet PropertyProperty (DBL)(DBL) VIVI

Defines a property for a file, channel group, or channel. Wire data to the Value input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Create if not found (no:F) —

    Create if not found specifies whether the VI creates a new property with the values you set if the
    property specified in Property name does not exist. The default is FALSE, which means the VI
    does not create a property and returns an error if the specified property does not exist.

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •      Property name —

    Property name specifies the name of the property. Use the Get Property Info VI to obtain the
    Property name.

   •      Value —

    Value specifies the value of the property.

   •       error in (no error) —


                                                    © National Instruments 1689

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1689 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1690 ordinal=1690 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet PropertyProperty (SGL)(SGL) VIVI

       Defines a property for a file, channel group, or channel. Wire data to the Value input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Create if not found (no:F) —

            Create if not found specifies whether the VI creates a new property with the values you set if the
            property specified in Property name does not exist. The default is FALSE, which means the VI
           does not create a property and returns an error if the specified property does not exist.

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      Property name —

            Property name specifies the name of the property. Use the Get Property Info VI to obtain the
            Property name.

               •      Value —


1690   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1690 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1691 ordinal=1691 -->
## Functions

Functions


    Value specifies the value of the property.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet PropertyProperty (I32)(I32) VIVI

Defines a property for a file, channel group, or channel. Wire data to the Value input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Create if not found (no:F) —

    Create if not found specifies whether the VI creates a new property with the values you set if the
    property specified in Property name does not exist. The default is FALSE, which means the VI
    does not create a property and returns an error if the specified property does not exist.

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •      Property name —


                                                    © National Instruments 1691

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1691 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1692 ordinal=1692 -->
## Functions

Functions


            Property name specifies the name of the property. Use the Get Property Info VI to obtain the
            Property name.

               •      Value —

            Value specifies the value of the property.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet PropertyProperty (I16)(I16) VIVI

       Defines a property for a file, channel group, or channel. Wire data to the Value input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Create if not found (no:F) —

            Create if not found specifies whether the VI creates a new property with the values you set if the
            property specified in Property name does not exist. The default is FALSE, which means the VI
           does not create a property and returns an error if the specified property does not exist.

               •      storage refnum —


1692   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1692 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1693 ordinal=1693 -->
## Functions

Functions


    storage refnum specifies the reference number for the data object you want to access.

   •      Property name —

    Property name specifies the name of the property. Use the Get Property Info VI to obtain the
    Property name.

   •      Value —

    Value specifies the value of the property.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet PropertyProperty (U8)(U8) VIVI

Defines a property for a file, channel group, or channel. Wire data to the Value input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Create if not found (no:F) —

    Create if not found specifies whether the VI creates a new property with the values you set if the


                                                    © National Instruments 1693

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1693 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1694 ordinal=1694 -->
## Functions

Functions


            property specified in Property name does not exist. The default is FALSE, which means the VI
           does not create a property and returns an error if the specified property does not exist.

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      Property name —

            Property name specifies the name of the property. Use the Get Property Info VI to obtain the
            Property name.

               •      Value —

            Value specifies the value of the property.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet PropertyProperty (Enum)(Enum) VIVI

       Defines a property for a file, channel group, or channel. Wire data to the Value input to
      determine the polymorphic instance to use or manually select the instance.


1694   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1694 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1695 ordinal=1695 -->
## Functions

Functions

Inputs/Outputs

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •      Property name —

    Property name specifies the name of the property. Use the Get Property Info VI to obtain the
    Property name.

   •      Value —

    Value specifies the numeric value of the enum.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     Enum values —

   enum values specifies the valid string values for the enum.

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet PropertyProperty (Time(Time Stamp)Stamp) VIVI

Defines a property for a file, channel group, or channel. Wire data to the Value input to
determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1695

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1695 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1696 ordinal=1696 -->
## Functions

Functions


      Inputs/Outputs

               •      Create if not found (no:F) —

            Create if not found specifies whether the VI creates a new property with the values you set if the
            property specified in Property name does not exist. The default is FALSE, which means the VI
           does not create a property and returns an error if the specified property does not exist.

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      Property name —

            Property name specifies the name of the property. Use the Get Property Info VI to obtain the
            Property name.

               •      Value —

            Value specifies the value of the property.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet PropertyProperty (Storage(Storage Refnum)Refnum) VIVI

       Defines a property for a file, channel group, or channel. Wire data to the Value input to

1696   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1696 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1697 ordinal=1697 -->
## Functions

Functions

determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •      Property name —

    Property name specifies the name of the property. Use the Get Property Info VI to obtain the
    Property name.

   •      Value —

    Value specifies the value of the property.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet PropertyProperty (Storage(Storage Refnums)Refnums) VIVI

Defines a property for a file, channel group, or channel. Wire data to the Value input to
determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1697

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1697 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1698 ordinal=1698 -->
## Functions

Functions


      Inputs/Outputs

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      Property name —

            Property name specifies the name of the property. Use the Get Property Info VI to obtain the
            Property name.

               •      Value —

            Value specifies the value of the property.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   GetGet PropertyProperty

       Returns the value of a property for a file, channel group, or channel. You must
      manually select the polymorphic instance you want to use.


1698   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1698 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1699 ordinal=1699 -->
## Functions

Functions

  • Get Property (String) VI
  • Get Property (DBL) VI
  • Get Property (SGL) VI
  • Get Property (I32) VI
  • Get Property (I16) VI
  • Get Property (U8) VI
  • Get Property (Enum) VI
  • Get Property (Time Stamp) VI
  • Get Property (Storage Refnum) VI
  • Get Property (Storage Refnums) VI
GetGet PropertyProperty (String)(String) VIVI

Returns the value of a property for a file, channel group, or channel. You must
manually select the polymorphic instance you want to use.


Inputs/Outputs

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •      Property name —

    Property name specifies the name of the property. Use the Get Property Info VI to obtain the
    Property name.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.


                                                    © National Instruments 1699

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1699 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1700 ordinal=1700 -->
## Functions

Functions

               •      Value —

            Value returns the value of the property.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   GetGet PropertyProperty (DBL)(DBL) VIVI

       Returns the value of a property for a file, channel group, or channel. You must
      manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      Property name —

            Property name specifies the name of the property. Use the Get Property Info VI to obtain the
            Property name.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •      Value —

            Value returns the value of the property.


1700   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1700 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1701 ordinal=1701 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetGet PropertyProperty (SGL)(SGL) VIVI

Returns the value of a property for a file, channel group, or channel. You must
manually select the polymorphic instance you want to use.


Inputs/Outputs

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •      Property name —

    Property name specifies the name of the property. Use the Get Property Info VI to obtain the
    Property name.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.

   •      Value —

    Value returns the value of the property.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1701

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1701 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1702 ordinal=1702 -->
## Functions

Functions

   GetGet PropertyProperty (I32)(I32) VIVI

       Returns the value of a property for a file, channel group, or channel. You must
      manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      Property name —

            Property name specifies the name of the property. Use the Get Property Info VI to obtain the
            Property name.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •      Value —

            Value returns the value of the property.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1702   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1702 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1703 ordinal=1703 -->
## Functions

Functions

GetGet PropertyProperty (I16)(I16) VIVI

Returns the value of a property for a file, channel group, or channel. You must
manually select the polymorphic instance you want to use.


Inputs/Outputs

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •      Property name —

    Property name specifies the name of the property. Use the Get Property Info VI to obtain the
    Property name.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.

   •      Value —

    Value returns the value of the property.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1703

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1703 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1704 ordinal=1704 -->
## Functions

Functions

   GetGet PropertyProperty (U8)(U8) VIVI

       Returns the value of a property for a file, channel group, or channel. You must
      manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      Property name —

            Property name specifies the name of the property. Use the Get Property Info VI to obtain the
            Property name.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •      Value —

            Value returns the Value of the property.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1704   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1704 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1705 ordinal=1705 -->
## Functions

Functions

GetGet PropertyProperty (Enum)(Enum) VIVI

Returns the value of a property for a file, channel group, or channel. You must
manually select the polymorphic instance you want to use.


Inputs/Outputs

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •      Property name —

    Property name specifies the name of the property. Use the Get Property Info VI to obtain the
    Property name.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.

   •       String —

     string returns the string value of the enum.

   •      Value —

    Value returns the numeric value of the enum.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1705

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1705 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1706 ordinal=1706 -->
## Functions

Functions

   GetGet PropertyProperty (Time(Time Stamp)Stamp) VIVI

       Returns the value of a property for a file, channel group, or channel. You must
      manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      Property name —

            Property name specifies the name of the property. Use the Get Property Info VI to obtain the
            Property name.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •      Value —

            Value returns the value of the property.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1706   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1706 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1707 ordinal=1707 -->
## Functions

Functions

GetGet PropertyProperty (Storage(Storage Refnum)Refnum) VIVI

Returns the value of a property for a file, channel group, or channel. You must
manually select the polymorphic instance you want to use.


Inputs/Outputs

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •      Property name —

    Property name specifies the name of the property. Use the Get Property Info VI to obtain the
    Property name.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.

   •      Value —

    Value returns the value of the property.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1707

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1707 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1708 ordinal=1708 -->
## Functions

Functions

   GetGet PropertyProperty (Storage(Storage Refnums)Refnums) VIVI

       Returns the value of a property for a file, channel group, or channel. You must
      manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      Property name —

            Property name specifies the name of the property. Use the Get Property Info VI to obtain the
            Property name.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •      Value —

            Value returns the value of the property.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1708   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1708 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1709 ordinal=1709 -->
## Functions

Functions

MergeMerge StorageStorage RefnumsRefnums

Merges two arrays of storage reference numbers into one larger array of refnums. This
VI works properly only if the two sets of storage refnums are from the same data file.
Wire data to either of the storage refnums inputs to determine the polymorphic
instance to use or manually select the instance.


  • Merge Storage Refnums (Channel) VI
  • Merge Storage Refnums (Channel group) VI
MergeMerge StorageStorage RefnumsRefnums (Channel)(Channel) VIVI

Merges two arrays of storage reference numbers into one larger array of refnums. This
VI works properly only if the two sets of storage refnums are from the same data file.
Wire data to either of the storage refnums inputs to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •      storage refnums (channel) 1 —

    storage refnums (channel) 1 specifies the channels to merge. Wire the storage refnums output
     of the Read Data VI to this input.

   •      storage refnums (channel) 2 —

    storage refnums (channel) 2 specifies the channels to merge. Wire the storage refnums output
     of the Read Data VI to this input.

   •      operation —

                                                    © National Instruments 1709

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1709 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1710 ordinal=1710 -->
## Functions

Functions


            operation specifies the condition that joins storage refnums (channel) 1 and storage refnums
            (channel) 2.

          AND
           0 —Combines all channels that are included in both storage refnums (channel) 1 and storage
            refnums (channel) 2.
          OR
           1           —Combines all channels from storage refnums (channel) 1 and storage refnums (channel) 2.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnums (channel) —

            storage refnums (channel) returns the channels that meet the operation condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   MergeMerge StorageStorage RefnumsRefnums (Channel(Channel group)group) VIVI

      Merges two arrays of storage reference numbers into one larger array of refnums. This
        VI works properly only if the two sets of storage refnums are from the same data file.
       Wire data to either of the storage refnums inputs to determine the polymorphic
       instance to use or manually select the instance.


      Inputs/Outputs

               •      storage refnums (channel group) 2 —


1710   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1710 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1711 ordinal=1711 -->
## Functions

Functions


    storage refnums (channel group) 2 specifies the channel groups to merge. Wire the storage
    refnums output of the Read Data VI to this input.

   •      storage refnums (channel group) 1 —

    storage refnums (channel group) 1 specifies the channel groups to merge. Wire the storage
    refnums output of the Read Data VI to this input.

   •      operation —

    operation specifies the condition that joins storage refnums (channel group) 1 and storage
    refnums (channel group) 2.

    AND—Combines all channel groups that are included in both storage refnums (channel group)    0
     1 and storage refnums (channel group) 2.
    OR—Combines all channel groups from storage refnums (channel group) 1 and storage    1
     refnums (channel group) 2.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage refnums (channel group) —

    storage refnums (channel group) returns the channel groups that meet the operation
    condition.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

CreateCreate QueryQuery ExpressionExpression

Creates a query expression to use with the Execute Query Expression VI to search for
objects that meet the condition you specify. Wire data to the value input to determine
the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1711

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1711 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1712 ordinal=1712 -->
## Functions

Functions


            • Create Query Expression (String) VI
            • Create Query Expression (I32) VI
            • Create Query Expression (DBL) VI
            • Create Query Expression (Time Stamp) VI
    CreateCreate QueryQuery ExpressionExpression (String)(String) VIVI

       Creates a query expression to use with the Execute Query Expression VI to search for
       objects that meet the condition you specify. Wire data to the value input to determine
       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      property name —

            property name specifies the name of the property. Use the Get Property Info VI to obtain the
            property name.

               •      comparison operator (=) —

           comparison operator (=) specifies the comparison condition.

           0                           =
           1                                  !=
           2                           >
           3                           <
           4                           >=
           5                           <=

               •      value —


1712   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1712 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1713 ordinal=1713 -->
## Functions

Functions


    value specifies the value you want to compare.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      query expression —

    query expression returns a query expression based on what you wired to the inputs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

CreateCreate QueryQuery ExpressionExpression (I32)(I32) VIVI

Creates a query expression to use with the Execute Query Expression VI to search for
objects that meet the condition you specify. Wire data to the value input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      property name —

    property name specifies the name of the property. Use the Get Property Info VI to obtain the
    property name.

   •      comparison operator (=) —

    comparison operator (=) specifies the comparison condition.

    0                           =


                                                    © National Instruments 1713

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1713 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1714 ordinal=1714 -->
## Functions

Functions


           1                                  !=
           2                           >
           3                           <
           4                           >=
           5                           <=

               •      value —

            value specifies the value you want to compare.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      query expression —

           query expression returns a query expression based on what you wired to the inputs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    CreateCreate QueryQuery ExpressionExpression (DBL)(DBL) VIVI

       Creates a query expression to use with the Execute Query Expression VI to search for
       objects that meet the condition you specify. Wire data to the value input to determine
       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      property name —

            property name specifies the name of the property. Use the Get Property Info VI to obtain the


1714   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1714 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1715 ordinal=1715 -->
## Functions

Functions


    property name.

   •      comparison operator (=) —

    comparison operator (=) specifies the comparison condition.

    0                           =
    1                                  !=
    2                           >
    3                           <
    4                           >=
    5                           <=

   •      value —

    value specifies the value you want to compare.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      query expression —

    query expression returns a query expression based on what you wired to the inputs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

CreateCreate QueryQuery ExpressionExpression (Time(Time Stamp)Stamp) VIVI

Creates a query expression to use with the Execute Query Expression VI to search for
objects that meet the condition you specify. Wire data to the value input to determine
the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1715

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1715 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1716 ordinal=1716 -->
## Functions

Functions


      Inputs/Outputs

               •      property name —

            property name specifies the name of the property. Use the Get Property Info VI to obtain the
            property name.

               •      comparison operator (=) —

           comparison operator (=) specifies the comparison condition.

           0                           =
           1                                  !=
           2                           >
           3                           <
           4                           >=
           5                           <=

               •      value —

            value specifies the value you want to compare.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      query expression —

           query expression returns a query expression based on what you wired to the inputs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1716   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1716 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1717 ordinal=1717 -->
## Functions

Functions

MergeMerge QueryQuery ExpressionsExpressions

Merges two query expressions. You can use the Create Query Expression VI to create
query expressions that you want to merge.


Inputs/Outputs

   •      query expression 1 —

    query expression 1 specifies a query expression you want to merge.

   •      query expression 2 —

    query expression 2 specifies a query expression you want to merge.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     combined query expression —

    combined query expression returns a query expression that merges query expression 1 and
    query expression 2. You can wire this output to the Execute Query Expression VI to obtain the
    objects that meet the combined query conditions.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ExecuteExecute QueryQuery ExpressionExpression

Returns data objects that meet the query expression.


                                                    © National Instruments 1717

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1717 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1718 ordinal=1718 -->
## Functions

Functions


      Inputs/Outputs

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      object type —

            object type specifies the object type of the storage refnums that this VI returns. Use the Get
            Object Info VI to obtain the object type from a storage refnum.

               •      query expression —

           query expression specifies the query condition. Use the Create Query Expression VI to obtain the
           query expression.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      storage refnum out —

            storage refnum out returns a reference number for the data object this VI accesses.

               •      storage refnums —

            storage refnums returns the data objects that meet the query conditions.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   RefnumRefnum toto IDID

       Returns the ID for a data object.


1718   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1718 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1719 ordinal=1719 -->
## Functions

Functions


Inputs/Outputs

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      storage refnum out —

    storage refnum out returns a reference number for the data object this VI accesses.

   •      object ID —

    object ID returns the object ID, which is a unique string that identifies the object in the file. The
    object ID is persistent, so you can reuse it after closing a file and opening the file again.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

IDID toto RefnumRefnum

Returns a refnum for an object you specify. Wire data to the storage refnum input to
determine the polymorphic instance to use.


  • GetObjectFromID_Storage VI
  • GetObjectFromID_Object VI


                                                    © National Instruments 1719

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1719 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1720 ordinal=1720 -->
## Functions

Functions

   GetObjectFromID_StorageGetObjectFromID_Storage VIVI

       Returns a refnum for an object you specify. Wire data to the storage refnum input to
      determine the polymorphic instance to use.


      Inputs/Outputs

               •      storage refnum —

            storage refnum specifies the reference number for the data object you want to access.

               •      object ID —

            object ID specifies the ID of the object you want to access. The object ID is a unique string that
              identifies the object in the file. Use the Refnum to ID VI to obtain the object ID.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     new storage refnum —

         new storage refnum returns a refnum for the object.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   GetObjectFromID_ObjectGetObjectFromID_Object VIVI

       Returns a refnum for an object you specify. Wire data to the storage refnum input to
      determine the polymorphic instance to use.


1720   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1720 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1721 ordinal=1721 -->
## Functions

Functions


Inputs/Outputs

   •      storage refnum —

    storage refnum specifies the reference number for the data object you want to access.

   •      Object id —

    object ID specifies the ID of the object you want to access. The object ID is a unique string that
     identifies the object in the file. Use the Refnum to ID VI to obtain the object ID.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     new storage refnum —

   new storage refnum returns a refnum for the object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ZipZip

Use the Zip VIs to create new zip files, to add files to zip files, to unzip zip files, and to
close zip files.


 Palette
         Description
 Object

 New
 Zip     Creates a new empty zip file in the path that target specifies. The new file overwrites an
 File


                                                    © National Instruments 1721

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1721 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1722 ordinal=1722 -->
## Functions

Functions


         Palette                 Description
        Object

                   existing file or produces a confirmation dialog based on the value of the confirm
                 overwrite? control.


       Add               Adds the file source file path specifies to a zip file. The destination path in zip control           File to                   specifies the zipped path information.
         Zip

         Close
         Zip     Closes the zip file zip file in specifies.
           File

                Unzips the contents of Zip file to the Target directory. Set Preview only? to TRUE to
        Unzip   preview the list of files in Zip file before you unzip the zip file. This VI cannot unzip a zip file
                  that is password protected.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Zip\Create Zip File.vi

     NewNew ZipZip FileFile

       Creates a new empty zip file in the path that target specifies. The new file overwrites
      an existing file or produces a confirmation dialog based on the value of the confirm
       overwrite? control.


      Inputs/Outputs

               •       target —

             target specifies the path to the new or existing zip file. The VI deletes and rewrites the file if it


1722   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1722 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1723 ordinal=1723 -->
## Functions

Functions


    already exists. You cannot append data to a zip file.

   •      confirm overwrite? (F) —

    confirm overwrite? specifies to overwrite the existing zip file. The default is FALSE. If you set
    confirm overwrite? to TRUE, the VI prompts you to confirm deleting the existing zip file.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       zip file out —

     zip file out returns the open zip file. zip file out is analogous to a refnum or task ID.

   •      cancelled —

    cancelled returns TRUE only if a user cancels an overwrite confirmation dialog box.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Zip\Create Zip File.vi

AddAdd FileFile toto ZipZip

Adds the file source file path specifies to a zip file. The destination path in zip control
specifies the zipped path information.


                                                    © National Instruments 1723

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1723 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1724 ordinal=1724 -->
## Functions

Functions

      Inputs/Outputs

               •       zip file in —

             zip file in specifies the open zip file.

               •      source file path —

            source file path specifies the path to file to add to the zip file.

               •      destination path in zip —

            destination path in zip specifies the filename and the path to apply to the source file when the
              VI encodes the file into the zip file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       zip file out —

             zip file out returns the open zip file. zip file out is analogous to a refnum or task ID.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Zip\Create Zip File.vi

      CloseClose ZipZip FileFile

       Closes the zip file zip file in specifies.


1724   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1724 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1725 ordinal=1725 -->
## Functions

Functions

Inputs/Outputs

   •       zip file in —

     zip file in specifies the open zip file.

   •     comments —

   comments includes text to include in the zip file.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Zip\Create Zip File.vi

UnzipUnzip

Unzips the contents of Zip file to the Target directory. Set Preview only? to TRUE to
preview the list of files in Zip file before you unzip the zip file. This VI cannot unzip a zip
file that is password protected.


Inputs/Outputs

   •      Zip file —

                                                    © National Instruments 1725

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1725 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1726 ordinal=1726 -->
## Functions

Functions


            Zip file specifies the path to the zip file that you want to unzip.

               •      Preview only? —

           Preview only? specifies whether to display the files in Zip file without unzipping the zip file. If
           TRUE, this VI does not unzip Zip file and Preview displays a list of the files in the zip file. The
             default is FALSE.

               •      Target directory (same as Zip file if empty) —

            Target directory specifies the directory path to which the VI unzips the files in Zip file. The
             default is the directory path that contains the zip file.

                    If you specify a path that includes a filename, the VI strips the filename from the path and unzips
                files to the resulting directory.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Unzipped files —

           Unzipped files lists the files that the VI unzips.

               •      Preview —

           Preview lists the paths to the files in Zip file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    XMLXML

      Use the XML VIs and functions to manipulate XML data.


1726   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1726 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1727 ordinal=1727 -->
## Functions

Functions


 Palette Object  Description

 LabVIEW      Use the LabVIEW Schema VIs and functions to manipulate LabVIEW data in XML
 Schema        format.


              Use the XML Parser VIs and nodes to process XML documents using the XML parser.
 XML Parser              The XML parser in LabVIEW is the Xerces 2.7 parser which uses a document object
             model (DOM).


LabVIEWLabVIEW SchemaSchema

Use the LabVIEW Schema VIs and functions to manipulate LabVIEW data in XML format.


 Palette           Description
 Object

 Flatten           Converts any data type you wire to anything and converts it to an XML string according
 To XML            to the LabVIEW XML schema. Function

 Unflatten
 From XML Converts an XML string to a LabVIEW data type according to the LabVIEW XML schema.
 Function

            Writes a text string of XML data with accompanying header tags to a text file. Wire data
 Write to
            to the XML Input input to determine the polymorphic instance to use or manually select
 XML File
           the instance. All XML data must follow the standard LabVIEW XML schema.


          Reads and parses tags from a LabVIEW XML file. When you place this VI on the block
 Read
           diagram, the polymorphic VI selector is visible. Use this selector to choose which
 From XML
           polymorphic instance to use. All XML data must follow the standard LabVIEW XML
 File
          schema.


                                                    © National Instruments 1727

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1727 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1728 ordinal=1728 -->
## Functions

Functions


         Palette                   Description
        Object

        Escape                   Converts special characters to XML syntax according to the LabVIEW XML schema.       XML


        Unescape Converts the XML syntax for special characters back to the special characters according
       XML       to the LabVIEW XML schema.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\XML\Flatten and Unflatten XML\
        Flatten and Unflatten XML.lvproj
    FlattenFlatten ToTo XMLXML FunctionFunction

       Converts any data type you wire to anything and converts it to an XML string according
       to the LabVIEW XML schema.

           If anything contains the characters <, >, or &, the function converts those characters to
      &lt;, &gt;, or &amp;, respectively. Use the Escape XML VI to convert other
       characters, such as ", to XML syntax.


      Inputs/Outputs

               •      anything —

           anything is any LabVIEW data you want to convert. This parameter is polymorphic.

               •     xml string —


1728   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1728 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1729 ordinal=1729 -->
## Functions

Functions


    xml string is the resulting XML string that represents the LabVIEW data type.

   When converting decimal values, this function uses only the period (.) as a decimal separator.
    The function does not use localized decimal separators.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\XML\Flatten and Unflatten XML\
   Flatten and Unflatten XML.lvproj
UnflattenUnflatten FromFrom XMLXML FunctionFunction

Converts an XML string to a LabVIEW data type according to the LabVIEW XML schema.

If xml string contains the characters &lt;, &gt;, or &amp;, the function converts
those characters to <, >, or &, respectively. Use the Unescape XML VI to convert other
characters, such as ".


Inputs/Outputs

   •     xml string —

    xml string is the XML string that includes the data you want to convert.

    xml string must conform to the LabVIEW XML schema, including the case and order of tags in the
    schema. If xml string does not conform to the schema, the function returns an error and value
    contains the default value for the data type wired to type. If the VI containing the function
    previously completed execution, value contains the value from the previous execution.

     In xml string, this function accepts only the period (.) as a decimal separator. The function does
    not recognize localized decimal separators. This restriction prevents errors when you use XML
     strings on operating systems with different settings for the decimal separator.


                                                    © National Instruments 1729

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1729 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1730 ordinal=1730 -->
## Functions

Functions

               •      type —

           type is the data type to which you want to convert xml string.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      value —

            value is the data type you specified in type and the data in xml string.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    WriteWrite toto XMLXML FileFile

       Writes a text string of XML data with accompanying header tags to a text file. Wire data
       to the XML Input input to determine the polymorphic instance to use or manually
        select the instance. All XML data must follow the standard LabVIEW XML schema.


            • Write to XML File(string) VI
            • Write to XML File(array) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\XML\Flatten and Unflatten XML\
        Flatten and Unflatten XML.lvproj


1730   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1730 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1731 ordinal=1731 -->
## Functions

Functions

WriteWrite toto XMLXML File(string)File(string) VIVI

Writes a text string of XML data with accompanying header tags to a text file. Wire data
to the XML Input input to determine the polymorphic instance to use or manually
select the instance. All XML data must follow the standard LabVIEW XML schema.


Inputs/Outputs

   •     XML File Path —

   XML File Path is the path and filename to which you want to write XML data.

    The filename must have a .xml extension. When you specify an empty path, a dialog box
    prompts the user to specify an XML file.

   •     XML Input —

   XML Input contains XML data to write to the file.

   •     XML Encoding —

   XML Encoding specifies the encoding scheme for the XML file. LabVIEW supports ANSI and
    Multibyte encoding schemes.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Standalone? (T) —

    Standalone? specifies the value for the standalone attribute in the XML declaration.
    Standalone? determines whether the document exists entirely on its own (TRUE), or depends on
    other files (FALSE).

   •     XML File Path(duplicate) —


                                                    © National Instruments 1731

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1731 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1732 ordinal=1732 -->
## Functions

Functions


         XML File Path(duplicate) is the path of the file to which the VI writes data.

           You can use this output to determine the file path that you selected through a dialog box. XML
              File Path(duplicate) has a value of <Not A Path> if you cancelled the dialog box.

               •     XML String —

         XML String contains the XML data that the VI writes to the specified file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\XML\Flatten and Unflatten XML\
        Flatten and Unflatten XML.lvproj
    WriteWrite toto XMLXML File(array)File(array) VIVI

       Writes a text string of XML data with accompanying header tags to a text file. Wire data
       to the XML Input input to determine the polymorphic instance to use or manually
        select the instance. All XML data must follow the standard LabVIEW XML schema.


      Inputs/Outputs

               •     XML File Path —

         XML File Path is the path of the file to which the VI writes data.


1732   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1732 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1733 ordinal=1733 -->
## Functions

Functions


    The filename must have a .xml extension. When you specify an empty path, a dialog box
    prompts the user to specify an XML file.

   •     XML Input —

   XML Input allows you to write multiple nodes of XML data to an XML file.

   •     XML Encoding —

   XML Encoding specifies the encoding scheme for the XML file. LabVIEW supports ANSI and
    Multibyte encoding schemes.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Standalone? (T) —

    Standalone? specifies the value for the standalone attribute in the XML declaration.
    Standalone? determines whether the document exists entirely on its own (TRUE), or depends on
    other files (FALSE).

   •     XML File Path —

   XML File Path is the path and filename to which you want to write XML data.

    You can use this output to determine the file path that you selected through a dialog box. XML
     File Path has a value of <Not A Path> if you cancelled the dialog box.

   •     XML String —

   XML String contains the XML data that the VI writes to the specified file.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 1733

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1733 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1734 ordinal=1734 -->
## Functions

Functions

            • labview\examples\File IO\XML\Flatten and Unflatten XML\
        Flatten and Unflatten XML.lvproj
   ReadRead FromFrom XMLXML FileFile

      Reads and parses tags from a LabVIEW XML file. When you place this VI on the block
       diagram, the polymorphic VI selector is visible. Use this selector to choose which
      polymorphic instance to use. All XML data must follow the standard LabVIEW XML
      schema.


            • Read From XML File(array) VI
            • Read From XML File(string) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\XML\Flatten and Unflatten XML\
        Flatten and Unflatten XML.lvproj
   ReadRead FromFrom XMLXML File(array)File(array) VIVI

      Reads and parses tags from a LabVIEW XML file. When you place this VI on the block
       diagram, the polymorphic VI selector is visible. Use this selector to choose which
      polymorphic instance to use. All XML data must follow the standard LabVIEW XML
      schema.


1734   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1734 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1735 ordinal=1735 -->
## Functions

Functions

Inputs/Outputs

   •     XML File Path —

   XML File Path is the path and filename from which you want to read XML data.

   When you specify an empty path, a dialog box prompts the user to specify an XML file.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     XML File Path(duplicate) —

   XML File Path(duplicate) is the path of the file from which the VI reads data.

    You can use this output to determine the file path that you selected through a dialog box. XML
     File Path(duplicate) has a value of <Not A Path> if you cancelled the dialog box.

   •     XML Elements —

   XML Elements returns the top-level XML tags found between the end of the </Version> and
    </LVData> tags in an array of strings. You then can index the array and use the Unflatten From
   XML function.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\XML\Flatten and Unflatten XML\
   Flatten and Unflatten XML.lvproj
ReadRead FromFrom XMLXML File(string)File(string) VIVI

Reads and parses tags from a LabVIEW XML file. When you place this VI on the block
diagram, the polymorphic VI selector is visible. Use this selector to choose which

                                                    © National Instruments 1735

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1735 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1736 ordinal=1736 -->
## Functions

Functions

      polymorphic instance to use. All XML data must follow the standard LabVIEW XML
      schema.


      Inputs/Outputs

               •     XML File Path —

         XML File Path is the path and filename from which you want to read XML data.

         When you specify an empty path, a dialog box prompts the user to specify an XML file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     XML File Path(duplicate) —

         XML File Path(duplicate) is the path of the file from which the VI reads data.

           You can use this output to determine the file path that you selected through a dialog box. XML
              File Path(duplicate) has a value of <Not A Path> if you cancelled the dialog box.

               •     XML Elements —

         XML Elements returns the top-level XML tags found between the end of the </Version> and
            </LVData> tags in a single string. You then can wire this output to the Unflatten From XML
             function.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\XML\Flatten and Unflatten XML\

1736   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1736 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1737 ordinal=1737 -->
## Functions

Functions

   Flatten and Unflatten XML.lvproj
EscapeEscape XMLXML

Converts special characters to XML syntax according to the LabVIEW XML schema.

The Flatten To XML function converts the characters <, >, or & to &lt;, &gt;, or
&amp;, respectively, but you must use this VI to convert other characters, such as ", to
XML syntax.


Inputs/Outputs

   •     XML String In —

   XML String In is the XML string for which you want to convert special characters.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     XML String Out —

   XML String Out is the XML string with special characters converted.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

UnescapeUnescape XMLXML

Converts the XML syntax for special characters back to the special characters
according to the LabVIEW XML schema.


                                                    © National Instruments 1737

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1737 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1738 ordinal=1738 -->
## Functions

Functions

      The Unflatten From XML function converts the characters &lt;, &gt;, or &amp; to <,
       >, or &, respectively, but you must use this VI to convert other characters, such as
      &quot;.


      Inputs/Outputs

               •     XML String In —

         XML String In is the XML string that contains the XML-formatted characters you want to convert.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     XML String Out —

         XML String Out is the XML string with special characters.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     XMLXML ParserParser

      Use the XML Parser VIs and nodes to process XML documents using the XML parser.

      The XML parser in LabVIEW is the Xerces 2.7 parser which uses a document object
      model (DOM).

      The VIs and nodes on this palette can return XML Parser error codes.


1738   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1738 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1739 ordinal=1739 -->
## Functions

Functions


Palette          Description
Object

         Returns an XML parser session in LabVIEW. Use this VI each time you create a new XMLNew          parser session.


         Gets (reads) and/or sets (writes) properties of an XML reference. The node operates in the
Property same way as a standard Property Node.
Node
(XML)    National Instruments recommends that you use the Close VI to close all the references
           after using the XML parser classes.


Invoke         Invokes a method or action on an XML reference. The node operates in the same way as aNode
         standard Invoke Node.(XML)


          Closes a reference for all XML parser classes. You can use this polymorphic VI to close
Close    refnums from the NamedNodeMap class, the NodeList class, the Implementation class,
          or the Node class. The Node class encompasses all other XML classes.


Get First         Returns the first node within node in that matches the XPath expression. If this VI does
Matched         not find a match, node result is not a valid refnum.Node

Get All
Matched  Returns all the nodes within node in that match the XPath expression.
Nodes

Get Next
Non-
         Returns the first sibling of the node in that is not of type Text_Node.
Text
Sibling

Get First
Non-
         Returns the first child of the node in that is not of type Text_Node.
Text
Child


                                                    © National Instruments 1739

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1739 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1740 ordinal=1740 -->
## Functions

Functions


         Palette                  Description
        Object

        Get
       Node                  Returns the combined values of Text_Node children that the node in node owns.         Text
        Content

               Opens an XML file and allows you to configure the XML parser to validate the file against a
               schema or Document Type Definition (DTD).
        Load
                   National Instruments recommends that you use the Close VI to close all the references
                     after using the XML parser classes.


        Save     Saves an XML document.

   NewNew

       Returns an XML parser session in LabVIEW. Use this VI each time you create a new XML
       parser session.


      Inputs/Outputs

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •    DOM document out —

        DOM document out returns a reference to the new XML parser session.

               •       error out —


1740   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1740 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1741 ordinal=1741 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

PropertyProperty NodeNode (XML)(XML)

Gets (reads) and/or sets (writes) properties of an XML reference. The node operates in
the same way as a standard Property Node.

National Instruments recommends that you use the Close VI to close all the references
after using the XML parser classes.


Inputs/Outputs

   •      reference —
    reference is the refnum associated with an XML parser object that is already open.
   •       error in (no error) —
    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.
   •      reference out —
    reference out returns reference unchanged.
   •       error out —
    error out contains error information. This output provides standard error out functionality.
   •      Property —
    property 1..n are examples of properties you want to get (read).

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\XML\Parse XML\Generate XML
   String with Parser API.vi


                                                    © National Instruments 1741

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1741 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1742 ordinal=1742 -->
## Functions

Functions

   InvokeInvoke NodeNode (XML)(XML)

       Invokes a method or action on an XML reference. The node operates in the same way
       as a standard Invoke Node.


      Inputs/Outputs

               •      reference —
            reference is the refnum associated with an XML parser object that is already open.
               •       error in (no error) —
             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.
               •     Method —
            input 1..n are example input parameters of a method.
               •      reference out —
            reference out returns reference unchanged.
               •       error out —
             error out contains error information. This output provides standard error out functionality.
               •     Method —
            return value is an example return value of a method.
               •     param —

           output 1..n are example output parameters of a method.

   CloseClose

       Closes a reference for all XML parser classes. You can use this polymorphic VI to close
      refnums from the NamedNodeMap class, the NodeList class, the Implementation
        class, or the Node class. The Node class encompasses all other XML classes.


1742   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1742 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1743 ordinal=1743 -->
## Functions

Functions

  • Close Reference(NNMap) VI
  • Close Reference(NdList) VI
  • Close Reference(Impl) VI
  • Close Reference(Node) VI
CloseClose Reference(NNMap)Reference(NNMap) VIVI

Closes a reference for all XML parser classes. You can use this polymorphic VI to close
refnums from the NamedNodeMap class, the NodeList class, the Implementation
class, or the Node class. The Node class encompasses all other XML classes.


Inputs/Outputs

   •     named node map —

   named node map is the XML Parser NamedNodeMap class refnum that you want to close.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

CloseClose Reference(NdList)Reference(NdList) VIVI

Closes a reference for all XML parser classes. You can use this polymorphic VI to close
refnums from the NamedNodeMap class, the NodeList class, the Implementation
class, or the Node class. The Node class encompasses all other XML classes.


                                                    © National Instruments 1743

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1743 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1744 ordinal=1744 -->
## Functions

Functions


      Inputs/Outputs

               •     node list —

          node list is the XML Parser NodeList class refnum that you want to close.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   CloseClose Reference(Impl)Reference(Impl) VIVI

       Closes a reference for all XML parser classes. You can use this polymorphic VI to close
      refnums from the NamedNodeMap class, the NodeList class, the Implementation
        class, or the Node class. The Node class encompasses all other XML classes.


      Inputs/Outputs

               •      implementation —

           implementation is the XML Parser Implementation class refnum that you want to close.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following


1744   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1744 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1745 ordinal=1745 -->
## Functions

Functions


    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

CloseClose Reference(Node)Reference(Node) VIVI

Closes a reference for all XML parser classes. You can use this polymorphic VI to close
refnums from the NamedNodeMap class, the NodeList class, the Implementation
class, or the Node class. The Node class encompasses all other XML classes.


Inputs/Outputs

   •     node —

   node is the XML Parser Node class refnum that you want to close.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1745

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1745 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1746 ordinal=1746 -->
## Functions

Functions

   GetGet FirstFirst MatchedMatched NodeNode

       Returns the first node within node in that matches the XPath expression. If this VI does
       not find a match, node result is not a valid refnum.


      Inputs/Outputs

               •     node in —

          node in is a reference to an instance of XML Parser class Node. This VI uses node in as the context
          node to evaluate the XPath expression.

               •      XPath expression —

           XPath expression specifies the expression this VI uses to query node in for a match. Use XPath
            syntax to define the XPath expression.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     node out —

          node out contains the same reference as node in.

               •     node result —

          node result returns a reference to the first node that matches XPath expression. If this VI does
            not find a match, node result is not a valid refnum. You can use the Not a Number/Path/Refnum?
             function to establish whether this VI finds a match.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1746   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1746 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1747 ordinal=1747 -->
## Functions

Functions

GetGet AllAll MatchedMatched NodesNodes

Returns all the nodes within node in that match the XPath expression.


Inputs/Outputs

   •     node in —

   node in is a reference to an instance of XML Parser class Node. This VI uses node in as the context
    node to evaluate the XPath expression.

   •      XPath expression —

    XPath expression specifies the expression this VI uses to query node in for a match. Use XPath
    syntax to define the XPath expression.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     node out —

   node out contains the same reference as node in.

   •     node result array —

   node result array returns an array of references to each node that matches XPath expression. If
     this VI does not find a match, node result array is empty.

       If you use a For Loop to process each node from node result array, consider using shift registers
    instead of tunnels for other data you pass through the loop. Doing so avoids surprising behaviors
     in case node result array is empty.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1747

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1747 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1748 ordinal=1748 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\XML\Parse XML\Parse XML String
        for Multiple Nodes.vi
   GetGet NextNext Non-TextNon-Text SiblingSibling

       Returns the first sibling of the node in that is not of type Text_Node.


      Inputs/Outputs

               •     node in —

          node in is a reference to an instance of XML Parser class Node.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     node out —

          node out contains the same reference as node in.

               •       sibling node —

             sibling node contains a reference to the sibling.

               •      found sibling node? —

           found sibling node? indicates whether the VI located a non-Text_Node sibling.

               •       error out —


1748   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1748 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1749 ordinal=1749 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

GetGet FirstFirst Non-TextNon-Text ChildChild

Returns the first child of the node in that is not of type Text_Node.


Inputs/Outputs

   •     node in —

   node in is a reference to an instance of XML Parser class Node.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     node out —

   node out contains the same reference as node in.

   •       child node —

     child node contains a reference to the child.

   •      found child node? —

    found child node? indicates whether the VI located a non-Text_Node child.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1749

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1749 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1750 ordinal=1750 -->
## Functions

Functions

   GetGet NodeNode TextText ContentContent

       Returns the combined values of Text_Node children that the node in node owns.


      Inputs/Outputs

               •     node in —

          node in is a reference to an instance of XML Parser class Node.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     node out —

          node out contains the same reference as node in.

               •     node text —

          node text contains the combined values of the Text_Node children.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   LoadLoad

      Opens an XML file and allows you to configure the XML parser to validate the file
       against a schema or Document Type Definition (DTD).

       National Instruments recommends that you use the Close VI to close all the references
        after using the XML parser classes.


1750   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1750 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1751 ordinal=1751 -->
## Functions

Functions

The VI contains information about errors that the XML parser encounters while parsing
the document.


  • Load XML File VI
  • Load XML String VI
LoadLoad XMLXML FileFile VIVI

Opens an XML file and allows you to configure the XML parser to validate the file
against a schema or Document Type Definition (DTD).

National Instruments recommends that you use the Close VI to close all the references
after using the XML parser classes.

The VI contains information about errors that the XML parser encounters while parsing
the document.


Inputs/Outputs

   •       validate on load (Auto) —

    validate on load specifies the validation scheme that the XML parser uses. The default is Auto,
    which turns on validation only if the parser detects an internal or external DTD subset.

    You also can select Always, which turns on validation, or Never, which turns off validation.

   •      preserve whitespace (True) —


                                                    © National Instruments 1751

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1751 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1752 ordinal=1752 -->
## Functions

Functions


            preserve whitespace specifies whether a validating parser includes ignorable whitespaces as
             Text Nodes. The default is TRUE.

                    If you select FALSE, the parser discards ignorable whitespaces and does not add Text Nodes to
            the DOM tree. If you select FALSE, you must provide a valid DTD definition for the Preserve
           Whitespace option to correctly discard ignorable whitespaces. If the XML document is invalid or
           has no schema, the Preserve Whitespace option is ignored.

               •      path to XML document —

           path to XML document contains the location of the XML document you want to load into the
          XML parser.

               Note The XML document must include an XML prolog with a valid encoding value. If
                     the encoding value is incorrect or missing, this function might fail to parse the XML
                   document.

               •      process namespaces (False) —

            process namespaces disables namespace processing for the XML parser when set to FALSE, the
              default. When set to TRUE, the XML parser enforces the constraints and rules that the
          NameSpace specification contains.

               •      process schema (False) —

            process schema disables schema processing for the XML parser when set to FALSE, the default. If
           you set the control to TRUE, you must set process namespaces to TRUE.

               •      load external DTD (True) —

            load external DTD specifies whether the XML parser can load external DTDs. The default is TRUE.

           LabVIEW loads the schema specified in the metadata of the XML file. If you set validate on load
             to Always or Auto, the parser ignores this input and always loads the DTD.

              In the XML file, specify the external schema you want to use in one of the following metadata
              attributes:
                     • xsi:schemaLocation—Use this attribute if you define the targetNamespace attribute in the
               metadata of the XML file.
                     • xsi:noNamespaceSchemaLocation—Use this attribute if you do not define the
               targetNamespace attribute in the metadata of the XML file.
             Refer to TestConfiguration.xml in the examples\File IO\XML\Parse XML\
         support directory for an example of specifying a schema in an XML file.

1752   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1752 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1753 ordinal=1753 -->
## Functions

Functions

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     schema full checking (False) —

   schema full checking specifies whether the XML parser runs full or partial schema constraint
    checking. The default is FALSE, which configures the XML parser to run partial constraint
    checking.

   •    DOM document out —

   DOM document out returns a reference to the new XML parser session.

   •      parse errors —

    parse errors contains information on errors the XML parser found when it parsed the document,
    including problems the parser encountered when validating the document against the schema.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

LoadLoad XMLXML StringString VIVI

Opens an XML file and allows you to configure the XML parser to validate the file
against a schema or Document Type Definition (DTD).

National Instruments recommends that you use the Close VI to close all the references
after using the XML parser classes.

The VI contains information about errors that the XML parser encounters while parsing
the document.


                                                    © National Instruments 1753

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1753 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1754 ordinal=1754 -->
## Functions

Functions


      Inputs/Outputs

               •       validate on load (Auto) —

             validate on load specifies the validation scheme that the XML parser uses. The default is Auto,
           which turns on validation only if the parser detects an internal or external DTD subset.

           You also can select Always, which turns on validation, or Never, which turns off validation.

               •      preserve whitespace (True) —

            preserve whitespace specifies whether a validating parser includes ignorable whitespaces as
             Text Nodes. The default is TRUE.

                    If you select FALSE, the parser discards ignorable whitespaces and does not add Text Nodes to
            the DOM tree. If you select FALSE, you must provide a valid DTD definition for the Preserve
           Whitespace option to correctly discard ignorable whitespaces. If the XML document is invalid or
           has no schema, the Preserve Whitespace option is ignored.

               •     XML string —

         XML string is the XML string that includes the data you want to parse.

               Note The XML string must include an XML prolog with a valid encoding value. If the
                   encoding value is incorrect or missing, this function might fail to parse the XML string.

               •      process namespaces (False) —

            process namespaces disables namespace processing for the XML parser when set to FALSE, the
              default. When set to TRUE, the XML parser enforces the constraints and rules that the
          NameSpace specification contains.

               •      process schema (False) —

            process schema disables schema processing for the XML parser when set to FALSE, the default. If
           you set the control to TRUE, you must set process namespaces to TRUE.


1754   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1754 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1755 ordinal=1755 -->
## Functions

Functions

•      load external DTD (True) —

  load external DTD specifies whether the XML parser can load external DTDs. The default is TRUE.

  LabVIEW loads the schema specified in the metadata of the XML file. If you set validate on load
  to Always or Auto, the parser ignores this input and always loads the DTD.

  In the XML file, specify the external schema you want to use in one of the following metadata
  attributes:

      • xsi:schemaLocation—Use this attribute if you define the targetNamespace attribute in the
      metadata of the XML file.
      • xsi:noNamespaceSchemaLocation—Use this attribute if you do not define the
      targetNamespace attribute in the metadata of the XML file.

  Refer to TestConfiguration.xml in the examples\File IO\XML\Parse XML\
  support directory for an example of specifying a schema in an XML file.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     schema full checking (False) —

  schema full checking specifies whether the XML parser runs full or partial schema constraint
  checking. The default is FALSE, which configures the XML parser to run partial constraint
  checking.

•    DOM document out —

 DOM document out returns a reference to the new XML parser session.

•      parse errors —

  parse errors contains information on errors the XML parser found when it parsed the document,
  including problems the parser encountered when validating the document against the schema.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 1755

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1755 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1756 ordinal=1756 -->
## Functions

Functions

   SaveSave

      Saves an XML document.


      Inputs/Outputs

               •    DOM document in —

        DOM document in contains a reference to the XML parser session you want to save.

               •     XML file path —

         XML file path specifies the path where you want to save the file.

               •      overwrite file (True) —

            overwrite file specifies whether you want the VI to overwrite an existing file with the same
          name. The default is TRUE, which overwrites an existing file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •    DOM document out —

        DOM document out contains the same reference as DOM document in.

               •     XML file path out —

         XML file path out contains the path where the VI saved the file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1756   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1756 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1757 ordinal=1757 -->
## Functions

Functions

WaveformWaveform FileFile I/OI/O

Use the Waveform File I/O VIs to write waveform data to and read waveform data from
files.

The VIs on this palette can return waveform error codes.


 Palette              Description Object

              Creates a new file or appends to an existing file, writes the specified number of
 Write              records to the file, then closes the file and checks for errors. Each record is an array of Waveforms             waveforms. Wire data to the Waveform input to determine the polymorphic instance
 to File               to use or manually select the instance.


 Read       Opens a file created with the Write Waveforms to File VI and reads one record of the
 Waveforms    file. Each record might contain one or more separate waveforms. To retrieve all
 from File     records in the file, call this VI in a loop until the end of the file is reached.

 Export
 Waveforms   Converts a waveform to a text string and writes the string to a new byte stream file or
 to          appends the string to an existing file. Wire data to the waveforms input to determine
 Spreadsheet the polymorphic instance to use or manually select the instance.
 File

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Write Waveforms to
   File.vi


                                                    © National Instruments 1757

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1757 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1758 ordinal=1758 -->
## Functions

Functions

     AdvancedAdvanced FileFile FunctionsFunctions

      Use the Advanced File VIs and functions to manipulate files, directories, and paths.


         Palette                       Description
        Object

        Get File                      Returns the position of the current file mark of the file identified by refnum relative         Position                        to the beginning of the file.         Function

        Get File Size                      Gets the file size of file. This function does not work for files inside an LLB.
         Function

        Get                      Returns the owner, group, and permissions of the file or directory specified by path.
         Permissions                        This function does not work for files inside an LLB.         Function

        Get Type and                     Reads the type and creator of the file specified by path. type and creator are four-         Creator                        character strings. This function does not work for files inside an LLB.
         Function

         Preallocated                     Reads binary data from a file and places the data into an array that you have already
       Read from                        allocated without incurring a copy of the data. Unlike the Read from Binary File         Binary File
                         function, this function avoids run-time memory allocations.         Function

           File Dialog     Displays a dialog box with which you can specify the path to a file or directory.

         Set File
                    Moves the position of the current file mark of the file identified by refnum to the
         Position
                        position indicated by offset (in bytes) according to the mode in from.
         Function

         Set File Size   Sets the file size of file by setting the end-of-file marker to size bytes from the
         Function      beginning of the file. This function does not work for files inside an LLB.

         Set
                       Sets the owner, group, and permissions of the file or directory specified by path.
         Permissions
                        This function does not work for files inside an LLB.
         Function

         Set Type and  Sets the type and creator of the file specified by path. type and creator are four-


1758   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1758 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1759 ordinal=1759 -->
## Functions

Functions


Palette              Description
Object

Creator        character strings. This function does not work for files inside an LLB. Only macOS
Function      supports setting the type and creator of files.

            Opens a path to a file or directory in (Windows) Windows Explorer, (macOS) the
Show in File   Finder, or (Linux) a file system browser depending on the current platform. If you
System        specify a path to a file that is inside an LLB or a packed project library, this VI opens
              the path to the LLB or the packed project library.


             Checks if a filename is valid on different platforms. This VI checks filenames against
Is Name       only desktop platforms that support LabVIEW, which are Windows, macOS, and
Multiplatform  Linux. You can choose to check the filename against all possible platforms or
               against the current platform.


Create File              Creates a file and appends an incrementing number suffix to the filename if the file
with               already exists at a specified path. If the file does not exist, this VI creates the fileIncrementing              without appending an incrementing number suffix to the filename.
Suffix

            Moves the file or directory that you specify in source path to the location that you
Move          specify in target path. If you move a directory, this function moves all the contents
Function       of the directory recursively to the new location. You cannot use this function to
           move files into or out of an LLB.

              Copies the file or directory that you specify in source path to the location that you
Copy          specify in target path. If you copy a directory, this function copies all its contents
Function       recursively to the new location. You cannot use this function to copy files into or out
               of an LLB.

Delete         Deletes the file or directory specified by path. This function does not work for files
Function       inside an LLB.

Flush File      Writes all buffers of the file identified by refnum to disk and updates the directory
Function      entry of the file associated with refnum.

Deny Access   Reopens the instance of the file specified by refnum to temporarily change what
Function      read or write access is denied to other refnums, VIs, or applications.

              Returns information about the file or directory specified by path, including its size,
File/Directory
                   its last modification date, whether it is a directory, whether it is a shortcut, and the
Info Function
              resolved path if the file or directory is a shortcut. This function does not work for


                                                    © National Instruments 1759

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1759 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1760 ordinal=1760 -->
## Functions

Functions


         Palette                       Description
        Object

                              files inside an LLB.

                      Returns information about the volume containing the file or directory specified by        Get Volume                       path, including the total storage space provided by the volume and the amount free          Info Function
                          in bytes.

         Create Folder                       Creates the appropriate folder specified by path.         Function

                      Returns two arrays of strings listing the names of all files and folders found in path,           List Folder
                             filtering both arrays based upon pattern and filtering the filenames array based         Function                   upon the specified datalog type.

        Check if File                     Checks whether a file or folder exists on disk at a specified path. This VI works with         or Folder
                      standard files and folders as well as files in LLB files.          Exists

         Recursive File                            Lists the contents of a folder or LLB.           List

        Path To
         String        Converts path into a string describing a path in the standard format of the platform.
         Function

         String To                      Converts a string, describing a path in the standard format for the current platform,        Path
                        to a path.         Function

        Path to Array
         of Strings     Converts a path into an array of strings and indicates whether the path is relative.
         Function

         Array of
         Strings to
                      Converts an array of strings into a relative or absolute path.
        Path
         Function

       Refnum to
        Path          Returns the path associated with the specified refnum.
         Function

        Path Type     Returns the type of the specified path, indicating whether it is an absolute, relative,
         Function      or <Not A Path>.


1760   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1760 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1761 ordinal=1761 -->
## Functions

Functions


 Palette               Description
 Object

             Compares Path 1 to Path 2 and returns a relative path between the two paths, the Compare           common path between the two paths, and a Boolean that indicates whether the Two Paths               paths are on the same path hierarchy level.


 Get File               Returns the file extension, without the period (.), of a file you specify.
 Extension


 File         Computes the message digest on the contents of a file. You must manually select
 Checksum     the polymorphic instance you want to use.


 Generate               Returns a unique file path to the temporary directory. This VI only returns a path. It Temporary
             does not create the temporary file. File Path


             Use the Datalog functions to open and close datalog files, read from and write to
 Datalog       datalog files, get and set datalog file positions, and get and set the number of
               datalog records.


 Packed             Use the Packed Library VIs to get and return data from a packed project library.
 Library

 Create
 Directory      Creates a directory and any parent directories it requires to exist.
 Recursive

 Create File
 and
               Creates a file at a specified path and any folders within that path that do not exist.
 Containing
 Folders

GetGet FileFile PositionPosition FunctionFunction

Returns the position of the current file mark of the file identified by refnum relative to
the beginning of the file.


                                                    © National Instruments 1761

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1761 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1762 ordinal=1762 -->
## Functions

Functions


      Inputs/Outputs

               •     refnum —

          refnum is the file refnum associated with the file whose file mark you want to move.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out returns refnum unchanged.

               •       offset (in bytes) —

             offset (in bytes) indicates the new location of the file mark relative to the beginning of the file
             (zero-based).

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      GetGet FileFile SizeSize FunctionFunction

       Gets the file size of file. This function does not work for files inside an LLB.


      Inputs/Outputs

               •        file —

                file can be a refnum or file path.


1762   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1762 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1763 ordinal=1763 -->
## Functions

Functions

       If it is a file path, this node opens the file specified by the file path.
   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the refnum of the file that the function read. You can wire this output to another
      file function, depending on what you want to do with the file. The default is to close the file if it is
    referenced by a file path. If file is a refnum or if you wire refnum out to another function,
    LabVIEW assumes that the file is still in use until you close it.

   •       size (in bytes) —

     size (in bytes) is the size of the file in bytes.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


GetGet PermissionsPermissions FunctionFunction

Returns the owner, group, and permissions of the file or directory specified by path.
This function does not work for files inside an LLB.


Inputs/Outputs

   •      path —

    path specifies the file or directory whose access rights you want to change.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 1763

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1763 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1764 ordinal=1764 -->
## Functions

Functions


            standard error in functionality.

               •      permissions —

            permissions contains the current permissions setting for the file or directory after this function
             executes.

               •      path out —

           path out returns path unchanged.

               •     owner —

          owner contains the current owner setting for the file or directory after this function executes.

               •      group —

           group contains the current group setting for the file or directory after this function executes.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Refer to Setting Permissions for more information about the permissions parameter.

      (Windows) This function returns empty strings for owner and group because Windows
      does not support owners and groups.

      (macOS) If path refers to a file, this function returns empty strings for owner and group
      because macOS does not support owners or groups for files.

      GetGet TypeType andand CreatorCreator FunctionFunction

      Reads the type and creator of the file specified by path. type and creator are four-
       character strings. This function does not work for files inside an LLB.

           If the specified file has a name ending with characters that LabVIEW recognizes, such
       as .vi for the LVIN file type and .llb for the LVAR file type, this function returns that
       type in type and LBVW in creator. If the specified file is not a known LabVIEW file type,
        this function returns ???? in type and creator.

1764   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1764 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1765 ordinal=1765 -->
## Functions

Functions


Inputs/Outputs

   •      path —

    path specifies the file or directory whose type or creator you want to read.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      path out —

    path out returns path unchanged.

   •      type —

    type contains the current type of the file after this function executes.

       If no error occurs, this function returns the type of the specified file in type. If an error occurs,
    error indicates the type of error and type is an empty string.
   •       creator —

    creator contains the current creator of the file after this function executes.

       If no error occurs, this function returns the creator of the specified file in creator. If an error
    occurs, error indicates the type of error and creator is an empty string.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


type can return the values for LabVIEW files listed in the table below.


 LabVIEW File Type                                      type Value

 Control                                             LVCC

 .log                                               LVDL

                                                    © National Instruments 1765

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1765 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1766 ordinal=1766 -->
## Functions

Functions


       LabVIEW File Type                                      type Value

        LabVIEW Class                                          CLIB

        LabVIEW Project                                          LVPJ

         Library                                                LIBR

        LLB                                                LVAR

         Palette                                     LMNU

        Template Control                                     sVCC

        Template VI                                              sVIN

         Xcontrol                                             LVXC

          VI                                                       LVIN

      The type parameter can also return some platform-specific strings.

      PreallocatedPreallocated ReadRead fromfrom BinaryBinary FileFile FunctionFunction

      Reads binary data from a file and places the data into an array that you have already
       allocated without incurring a copy of the data. Unlike the Read from Binary File
       function, this function avoids run-time memory allocations.

      The performance of this function depends on the array you preallocate.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •     refnum in —

          refnum in specifies the file refnum associated with the file you want to read.

               •      data in —


1766   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1766 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1767 ordinal=1767 -->
## Functions

Functions


  data in specifies the array in which to place data. This function attempts to read as many data
  elements as the array holds. Refer to the support table for information about the arrays and data
  types this function supports.

•      byte order (0:big-endian, network order) —

  byte order sets the endian form of the resulting data. Byte order, or endian form, indicates
  whether integers are represented in memory from most-significant byte to least-significant byte
  or vice versa. The function must read the data in the same byte order that the data was written.

        Note This function requires that you set the byte order parameter to match the
           native byte order of the host computer running LabVIEW. If the computer is big
           endian, choose either native, host order or big-endian, network order> endian form.
                  If the computer is little endian, choose either native, host order or little-endian
          endian form.


   big-endian, network order (default)—The most-significant byte occupies the lowest memory
  0 address. This endian form is used on PowerPC platforms such as VxWorks. This endian-form
    also is used when reading data written on a different platform.
    native, host order—Uses the byte-ordering format of the host computer. This endian form
  1    increases read and write speed.
   little-endian—The least-significant byte occupies the lowest memory address. This endian
  2   form is used on Windows, macOS, and Linux.

•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     refnum out —

  refnum out is the refnum of the file that the function read. You can wire this output to another
   file function.

•      data out —

  data out contains the data read from the file. This output does not resize to include only valid
  data. If LabVIEW reaches the end of the file before the data in array is full, then the array contains
  some invalid elements. Use the num elements read output to determine the exact amount of
  valid data in data out. If LabVIEW does not reach the end of the file before the data in array is
   full, LabVIEW leaves the file pointer where the read finished so that the next read starts where


                                                   © National Instruments 1767

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1767 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1768 ordinal=1768 -->
## Functions

Functions


            the last read left off.

               •    num elements read —

        num elements read returns the total number of elements in the data in array replaced with data
           from the file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following block diagram shows an example of how this function works with a pre-
       allocated array. Each time the Preallocated Read from Binary File function executes,
      LabVIEW places the data from file in the same array.


      Preallocated Read from Binary File Support

       This function provides different levels of support for arrays you wire to place data from
          file:

          Fully supported. Because the function does not require a new allocation, it is
       probably faster than the Read from Binary File function.

         Supported. Because the function requires a new allocation and copy, it is probably
       slower than the Read from Binary File function.

        Not accepted by the function.

      The following table describes support when the array you wire to data in is a particular
       array or array slice that contains a particular data type.

1768   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1768 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1769 ordinal=1769 -->
## Functions

Functions


                                               Contiguous Array   Noncontiguous Array Data Type                                 Array                                                         Slice                 Slice1

 Integers

 Single-precision, floating-point numeric

 Double-precision, floating-point numeric

 Extended-precision, floating-point numeric²

 Complex single-precision, floating-point
 numeric

 Complex double-precision, floating-point
 numeric

 Complex extended-precision, floating-point
 numeric²

 Fixed-point numeric²

 Boolean

 String

 All other data types

      Note

          1. LabVIEW must make a memory copy of a noncontiguous array slice.
            Therefore, the Preallocated Read from Binary File function is not faster
          than the Read from Binary File function if you wire a noncontiguous array
             slice to data in.
          2. The Preallocated Read from Binary File function accepts extended
            precision, complex extended precision, and fixed-point data. However,
             this function allocates memory for a new copy with these data types, like
           the Read from Binary File function, because it cannot put the data in an
            existing allocation.


This function also fully supports each of the data types from the table as scalar values
that are not contained in arrays.


                                                    © National Instruments 1769

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1769 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1770 ordinal=1770 -->
## Functions

Functions

        FileFile DialogDialog

       Displays a dialog box with which you can specify the path to a file or directory.

      You can use this dialog box to select existing files or directories or to select a location
      and name for a new file or directory.

      (macOS) This VI does not recognize macOS-specific means of specifying the default
       application for a file. However, you can use the pattern input to specify a file type for
         files that include an extension to the filename.


      Dialog Box Options

        Option    Description

                The user can select one or more files. When you de-select this option, the options for the
                   types of files or folders the user can select appear dimmed.

                               •  files or folders—
                      Contains the following options:
         Limit    ◦ File—The user can select only a file.
         selection   ◦ Folder—The user can select only a folder.
         to single   ◦  File or folder—The user can select either a file or a folder.
        item            • new or existing—
                      Contains the following options:
           ◦ Existing—The user can select only an existing file or folder.
           ◦ New—The user only can enter the name of a new file or folder.
           ◦ New or existing—The user can select an existing file or folder or create a new
                                      file or folder.

        Allow
         selection  Specifies that you can select a file from an LLB or a packed library. If this checkbox does
         of files in

1770   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1770 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1771 ordinal=1771 -->
## Functions

Functions


 Option    Description

          not contain a checkmark, you can select an LLB or a packed library but you cannot
            select a file in an LLB or a packed library.

               Note To select an LLB or packed library using the File Dialog Express VI, you LLBs and
                  can remove the checkmark from the Allow selection of files in LLBs and packed
                 packed project libraries checkbox and select the LLB or packed library from project
                   the file dialog box. You also can place a checkmark in the Allow selection of libraries
                         files in LLBs and packed project libraries checkbox, select the Files or
                    Folders option button, choose an LLB or packed library from the file dialog
                    box, and select the second folder icon from the file list in the second file
                    dialog box that appears.


Inputs/Outputs

   •      button label —

    Label to display on the OK or Current Directory button in the file dialog box. If you configure the
    Express VI to allow the user to select directories, use this input to specify a label for the Current
    Directory button. If the configuration does not allow the user to select directories, use this input
    to specify a label for the OK button.

    For example, if you select Files only in the configure dialog box, the user must select an existing
      file to which to append data, so you might want to wire Append to button label.

       If button label is longer than the width of the button, the file dialog box does not display the
     entire label. For example, in an English version of Windows, the button is approximately 11
    characters wide.

   •      pattern (all files) —

     Restricts the files displayed in the dialog box to those whose name matches pattern (all files).
    pattern (all files) does not restrict the directories displayed.

    The pattern matching in this VI is similar to the matching used in matching wildcards in Windows
    and Linux filenames. If you specify characters other than the question mark character (?) or the
     asterisk character (*), the VI displays only files or directories that contain those characters. You
    can use the question mark character (?) to match any single character. You can use the asterisk
    character (*) to match any sequence of zero or more characters.


                                                    © National Instruments 1771

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1771 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1772 ordinal=1772 -->
## Functions

Functions


            For example, a pattern (all files) of *.vi;test*.llb returns matches for any file with a .vi
            extension and any file whose filename begins with test and has a .llb extension.

           To match multiple patterns, use a semicolon ( ; ) to separate the patterns. White space, such as
             blanks, tabs, and carriage returns, are taken literally. Avoid using white spaces unless they are
             part of the extension pattern. For example, if you use *.html;*.doc, the dialog box displays
                all files that end with .html and .doc. If you use *.html; *.doc, the dialog box displays
            only files that end with .html.

               •       start path —

            Path of the directory whose contents LabVIEW initially displays in the dialog box.

                    If start path is valid, but does not refer to an existing directory, LabVIEW strips names from the
          end of the path until the path is a valid directory path or an empty path. If start path is invalid or
            unwired, the last directory viewed in a file dialog box initially appears in the dialog box.

               •       default name —

         Name you want to appear as the initial file or directory name in the dialog box.

          The default is an empty string.

               •       error in —

            Describes error conditions that occur before this node runs.

               •     prompt —

          Custom message that appears as the title of the file dialog box. (Windows and Linux) The default
             dialog box title is Choose or Enter Path of File. (macOS) The default dialog box title is Select File
            or Create New File.

               •      pattern label —

            Label to display in the file dialog box next to the custom pattern.

                    If you do not wire this input or it contains an empty string, the default label next to any custom
            pattern is Custom Pattern. If you do not wire a string to pattern, LabVIEW ignores this input.

               •       error out —

            Contains error information. This output provides standard error out functionality.


1772   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1772 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1773 ordinal=1773 -->
## Functions

Functions

   •      selected path —

     Full path to the file or directory selected using this dialog box.

       If you cancel the dialog box, this VI sets selected path to <Not A Path>. This output is
     available if you place a checkmark in the Limit selection to single item checkbox in the
    Configure File Dialog dialog box.

   •       exists —

      Is TRUE if selected path specifies an existing file or directory.

   •      cancelled —

      Is TRUE if you cancel the dialog box.

   •      selected paths —

    Contains the full path names to the files or directories selected using this dialog box. This output
      is available if you do not place a checkmark in the Limit selection to single item in the
    Configure File Dialog dialog box.


Components

Specifies that you can select a file from an LLB or a packed library. If this checkbox
does not contain a checkmark, you can select an LLB or a packed library but you
cannot select a file in an LLB or a packed library.

The user can select one or more files. When you de-select this option, the options for
the types of files or folders the user can select appear dimmed.

Contains the following options:

  • Existing—The user can select only an existing file or folder.
  • New—The user only can enter the name of a new file or folder.
  • New or existing—The user can select an existing file or folder or create a new file or
    folder.

Contains the following options:

  • File—The user can select only a file.

                                                    © National Instruments 1773

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1773 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1774 ordinal=1774 -->
## Functions

Functions

            • Folder—The user can select only a folder.
            • File or folder—The user can select either a file or a folder.

      SetSet FileFile PositionPosition FunctionFunction

      Moves the position of the current file mark of the file identified by refnum to the
       position indicated by offset (in bytes) according to the mode in from.


      Inputs/Outputs

               •     refnum —

          refnum is the file refnum associated with the file whose file mark you want to move.

               •       offset (in bytes) (0) —

             offset (in bytes) specifies how far from the location specified by from to set the file mark.

               •      from (0:start) —

            from, together with offset (in bytes), specifies where to set the file mark. If you wire offset (in
             bytes), from defaults to 0, and the offset is relative to the beginning of the file. If you do not wire
             offset (in bytes), offset (in bytes) defaults to 0, from defaults to 2, and the operation starts at the
             current file mark.

             start—Sets the file mark offset (in bytes) bytes from the beginning of the file. If from is 0, offset
           0
                (in bytes) should be positive or 0, which sets the file mark at the beginning of the file.
            end—Sets the file mark offset (in bytes) bytes from the end of the file. If from is 1, offset (in
           1
              bytes) should be negative or 0, which sets the file mark at the end of the file.
           2 current—Sets the file mark offset (in bytes) bytes from the current file mark.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

1774   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1774 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1775 ordinal=1775 -->
## Functions

Functions


    refnum out returns refnum.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SetSet FileFile SizeSize FunctionFunction

Sets the file size of file by setting the end-of-file marker to size bytes from the
beginning of the file. This function does not work for files inside an LLB.


Inputs/Outputs

   •        file —

      file can be a refnum or file path.

       If it is a file path, this node opens the file specified by the file path.
   •       size (in bytes) —

     size (in bytes) is the size of the file in bytes.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the refnum of the file that the function read. You can wire this output to another
      file function, depending on what you want to do with the file. The default is to close the file if it is
    referenced by a file path. If file is a refnum or if you wire refnum out to another function,
    LabVIEW assumes that the file is still in use until you close it.

   •       error out —


                                                    © National Instruments 1775

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1775 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1776 ordinal=1776 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


      SetSet PermissionsPermissions FunctionFunction

       Sets the owner, group, and permissions of the file or directory specified by path. This
       function does not work for files inside an LLB.


      Inputs/Outputs

               •      permissions —

            permissions specifies the new permissions setting for the file or directory.

             Refer to Setting Permissions for more information about how to define the permissions you
          want to set.
               •      path —

           path specifies the file or directory whose access rights you want to change.

               •     new owner —

         new owner specifies the new owner for the file or directory.

                    If new owner is an empty string, the VI does not set the owner.
               •     new group —

         new group specifies the new group for the file or directory.

                    If new group is an empty string, the VI does not set the group.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      path out —


1776   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1776 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1777 ordinal=1777 -->
## Functions

Functions


    path out returns path unchanged.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If you do not specify new owner, new group, or permissions, this function returns the
current settings unchanged.

(Windows) This function ignores new owner and new group because Windows does
not support owners and groups.

(macOS) If path refers to a file, this function ignores new owner and new group
because macOS does not support owners or groups for files.

SetSet TypeType andand CreatorCreator FunctionFunction

Sets the type and creator of the file specified by path. type and creator are four-
character strings. This function does not work for files inside an LLB. Only macOS
supports setting the type and creator of files.


Inputs/Outputs

   •      path —

    path specifies the file or directory whose type or creator you want to read.

   •      type (no change) —

    type is the type of the specified file.

       If type is a string other than four characters, an error occurs.
   •       creator (no change) —


                                                    © National Instruments 1777

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1777 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1778 ordinal=1778 -->
## Functions

Functions


            creator is the creator of the specified file.

                    If creator is a string other than four characters, an error occurs.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      path out —

           path out returns path unchanged.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     ShowShow inin FileFile SystemSystem

      Opens a path to a file or directory in (Windows) Windows Explorer, (macOS) the Finder,
       or (Linux) a file system browser depending on the current platform. If you specify a
      path to a file that is inside an LLB or a packed project library, this VI opens the path to
       the LLB or the packed project library.


      Inputs/Outputs

               •        file or directory path —

                file or directory path specifies the path to a file or directory.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —


1778   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1778 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1779 ordinal=1779 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


IsIs NameName MultiplatformMultiplatform

Checks if a filename is valid on different platforms. This VI checks filenames against
only desktop platforms that support LabVIEW, which are Windows, macOS, and Linux.
You can choose to check the filename against all possible platforms or against the
current platform.


Inputs/Outputs

   •      filename —

    filename specifies the filename to check.

   •      filename must be valid on all platforms (F) —

    filename must be valid on all platforms specifies whether to check if the specified filename is
     valid on all possible platforms. If this input is TRUE, the VI checks the filename against all
    possible platforms. If this input is FALSE, the VI checks the filename against only the current
    platform. The default is FALSE.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      suggested filename —

    suggested filename returns the filename that you specified if the filename is valid. If the
     specified filename is invalid, this output transforms the specified filename into a valid filename
    by replacing invalid characters with hyphens or removing ending periods.

   •      filename had conflict —


                                                    © National Instruments 1779

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1779 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1780 ordinal=1780 -->
## Functions

Functions


            filename had conflict returns whether the specified filename is valid on any possible platform or
            the current platform. If filename must be valid on all platforms is TRUE, this output returns
          TRUE if the specified filename is invalid on any possible platform. If filename must be valid on
                all platforms is FALSE, this output returns TRUE if the specified filename is invalid on the current
             platform.

               •      filename not crossplatform —

            filename not crossplatform returns whether the specified filename is invalid on any possible
             platform. This output returns TRUE if the specified filename is invalid on any possible platform.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     problem description —

          problem description returns the problem details if the specified filename is invalid on any
             possible platform. This output lists reasons why the specified filename is considered invalid on
          one or multiple platforms.


       This VI checks if a filename is valid on different platforms according to the following
        rules:

            • (Windows) The following characters are invalid: \, /, :, *, ?, ", <, >, and |.
            • (Windows) Filenames cannot end with a period (.).
            • (macOS) The colon (:) is an invalid character.
            • (Linux) The slash (/) is an invalid character.

      The Is Name Multiplatform does not support multibyte characters. To check if a
       filename with multibyte characters is valid, use Is Name Multiplatform_Allow
     Multibyte.vi located in labview\vi.lib\Utility\Multibyte.

      CreateCreate FileFile withwith IncrementingIncrementing SuffixSuffix

       Creates a file and appends an incrementing number suffix to the filename if the file
       already exists at a specified path. If the file does not exist, this VI creates the file
       without appending an incrementing number suffix to the filename.


1780   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1780 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1781 ordinal=1781 -->
## Functions

Functions


Inputs/Outputs

   •      format string (" (%d)") —

    format string specifies how to convert the file path into a string. format string must contain
     exactly one decimal format code (%d). The default is " (%d)".

   •        file path —

      file path specifies the path to the file you want to create. You must specify an absolute path. If
    you specify an empty or relative path, this VI returns an error.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      disable buffering (F) —

    disable buffering specifies if the file opens without buffering. The default is FALSE.

       If you want to read or write a data file to a Redundant Array of Independent Disks (RAID),
    consider opening the file without buffering to speed up data transfers. To disable buffering, wire
    a TRUE value to the disable buffering input.

          Note If you have a small amount of data to transfer, you might not notice a
              difference if you disable buffering.

   (macOS and Linux) LabVIEW ignores this input.

   •     refnum out —

    refnum out returns the reference number of the file this VI creates.

   •      actual path —

    actual path returns the path to the file this VI creates.


                                                    © National Instruments 1781

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1781 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1782 ordinal=1782 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following table displays examples of how this VI uses format string to convert file
      path and to return actual path.


        Format                    File Path  Actual Path   Description         String

                                   The %d in format string specifies that the VI appends an
         " (%d)"   C:\test.txt  C:\test (1).txt incrementing number starting with 1 to the filename before the
                                        period (.).

                                   The 4 in format string specifies that the suffix after the filename       "%4d"   C:\test.txt  C:\test  1.txt
                                  and before the period (.) has a width of 4.

     MoveMove FunctionFunction

      Moves the file or directory that you specify in source path to the location that you
       specify in target path. If you move a directory, this function moves all the contents of
       the directory recursively to the new location. You cannot use this function to move files
       into or out of an LLB.


      Inputs/Outputs

               •     prompt (Choose or enter target path for move) —

          prompt is the message that appears above the list of files and directories, or folder, in the file
             dialog box.

               •      source path —

            source path specifies an absolute path to the file or directory on which you want to operate.


1782   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1782 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1783 ordinal=1783 -->
## Functions

Functions

   If you specify an empty or relative path, this function returns an error.
•       target path (use dialog) —

  target path is the new absolute path for the file or folder on which you want to operate,
  including the new file or folder name.

  You must have write permission for the file or directory that you specify in target path;
  otherwise, this function does not move the file or directory and returns an error.

         Tip Use the Set Permissions function to set the permissions for a file or directory.

  You must ensure the target path exists before running this function. If the last component of the
  target path does not exist, this function renames the file or folder you specified in the source
  path to this component name and moves the file or folder to the target location. See the
  examples below for details. If target path is empty (default), the function displays a dialog box
  from which you can select a file or folder. If you specify an empty or relative path, this function
  returns an error.

  Example: moving the source folder on C drive to the dest folder on D drive.

  Input/
         Value      Notes  Output
  source
       C:\source —  path
  target
       D:\dest  —  path
  new  D:\dest\  If the dest folder in target path exists, this function moves the source
  path  source     folder to the dest folder.
                                   If the dest folder in target path does not exist, this function renames the
  new       D:\dest  source folder to dest and then moves all the source folder contents to  path
                     the dest folder.

  Example: moving the test.txt file under C:\source to the dest folder on D drive.

  Input/
         Value        Notes
  Output
  source C:\source\
             —
  path  test.txt
  target
       D:\dest  —  path
  new  D:\dest\     If the dest folder in target path exists, this function moves the


                                                   © National Instruments 1783

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1783 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1784 ordinal=1784 -->
## Functions

Functions


            Input/                   Value        Notes
           Output
           path  test.txt  test.txt file to the dest folder.
         new                           If the dest folder in target path does not exist, this function renames the
               D:\dest
           path            test.txt file to dest and then moves this file to D drive.

               •      overwrite (F) —

            overwrite determines whether the function replaces existing files or folders in the target path. If
           you overwrite a folder that contains unique files, LabVIEW moves those files to the new folder.
          (macOS and Linux) LabVIEW does not overwrite read-only files, even if you set this parameter to
           TRUE.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     new path —

         new path specifies the new location of the file or directory. If the operation is unsuccessful, this
             function sets new path to <Not A Path>.

               •      cancelled —

            cancelled is TRUE if you cancel the file dialog box.

            Otherwise, cancelled is FALSE, even if this function returns an error.
               •       error out —

             error out contains error information. This output provides standard error out functionality.


     CopyCopy FunctionFunction

      Copies the file or directory that you specify in source path to the location that you
       specify in target path. If you copy a directory, this function copies all its contents
       recursively to the new location. You cannot use this function to copy files into or out of
      an LLB.


1784   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1784 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1785 ordinal=1785 -->
## Functions

Functions


Inputs/Outputs

   •     prompt (Choose or enter target path for copy) —

    prompt is the message that appears above the list of files and directories, or folder, in the file
    dialog box.

   •      source path —

    source path specifies an absolute path to the file or directory on which you want to operate. If
    you specify an empty or relative path, this function returns an error.

   •       target path (use dialog) —

    target path is the new absolute path for the file or folder on which you want to operate,
    including the new file or folder name.

       If target path is empty (default), the function displays a dialog box from which you can select a
      file or folder. If you specify an empty or relative path, this function returns an error. cancelled is
   TRUE if you cancel the dialog box.

   •      overwrite (F) —

    overwrite determines whether the function replaces existing files or folders in the target path. If
    you overwrite a folder that contains unique files, LabVIEW moves those files to the new folder.
   (macOS and Linux) LabVIEW does not overwrite read-only files, even if you set this parameter to
    TRUE.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     new path —

   new path specifies the new location of the file or directory.

       If the operation is unsuccessful, this function sets new path to <Not A Path>.

   •      cancelled —

                                                    © National Instruments 1785

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1785 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1786 ordinal=1786 -->
## Functions

Functions


            cancelled is TRUE if you cancel the file dialog box.

            Otherwise, cancelled is FALSE, even if this function returns an error.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       This function copies the original file or directory and renames the copy with the name
       that you specify in the last element of the target path. If target path is the path to an
        existing file, this function returns a Duplicate Path error. If target path is the path to an
        existing directory, the function places the new file or directory inside the existing
       directory using the original file or directory name.

       For example, if you copy the directory c:\app to d:\app2, the function creates a
     new directory d:\app2 with the same contents as c:\app. The second time you
      copy the directory, the function creates a new subdirectory d:\app2\app and places
       the contents of app there. The third time you copy the directory, the function returns a
       Duplicate Path error.

       This function also returns an error if the target path is an invalid path, such as if the
       specified parent directory is not valid.

           Note This function does not automatically append file extensions, such as
            .txt, to filenames when it copies or moves files. You must explicitly include
              the extension as a part of the new filename that you specify in target path.

           If you do not have write permission for the file or directory that you specify in target
       path, this function does not copy the file or directory and returns an error. Use the Set
       Permissions function to set the permissions for a file or directory.

      DeleteDelete FunctionFunction

       Deletes the file or directory specified by path. This function does not work for files
       inside an LLB.


1786   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1786 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1787 ordinal=1787 -->
## Functions

Functions


Inputs/Outputs

   •     prompt (Delete) —

    prompt is the message that appears above the list of files and directories, or folder, in the file
    dialog box.

   •      path (use dialog) —

    path specifies the absolute path to the file or directory you want to delete. If path is empty
     (default), the function displays a dialog box from which you can select a file or directory. If you
     specify an empty or relative path, this function returns an error. cancelled is TRUE if you cancel
    the dialog box.

   •       entire hierarchy (F) —

    entire hierarchy determines whether this function deletes all contents in the folder. The default
      is FALSE. If entire hierarchy is TRUE, this function deletes all files and folders within the
     specified path.

   •      confirm (F) —

       If confirm is TRUE, the function displays a dialog box and asks you to confirm the delete
    operation. The default is FALSE.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      deleted path —

    deleted path is the path of the deleted file or folder.deleted path returns <Not A Path> if an
     error occurred.

   •      cancelled —

    cancelled is TRUE if you cancel the file dialog box. Otherwise, cancelled is FALSE, even if this


                                                    © National Instruments 1787

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1787 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1788 ordinal=1788 -->
## Functions

Functions


             function returns an error.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If path specifies a directory that is not empty or if you do not have write permission for
       the file or directory specified by path and its parent directory, this function does not
      remove the directory and returns an error. Set entire hierarchy to TRUE to set the
       function to delete non-empty directories. Use the Set Permissions function to set the
       permissions for a file or directory.

      FlushFlush FileFile FunctionFunction

       Writes all buffers of the file identified by refnum to disk and updates the directory
       entry of the file associated with refnum.

      The file remains open, and refnum remains valid. Data written to a file often resides in
      a buffer until the buffer fills up or until you close the file. This function forces the
       operating system to write any buffer data to the file.


      Inputs/Outputs

               •     refnum —

          refnum is the file refnum associated with the file you want to flush.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out returns refnum unchanged.


1788   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1788 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1789 ordinal=1789 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


DenyDeny AccessAccess FunctionFunction

Reopens the instance of the file specified by refnum to temporarily change what read
or write access is denied to other refnums, VIs, or applications.


Inputs/Outputs

   •     refnum —

    refnum is the file refnum associated with the file you want to deny access to.

   •     deny mode (0:deny read/write) —

    deny mode specifies what read or write access is denied.

    0 deny read/write—Deny both read and write access to the file (default).
    1 deny write-only—Permit read access but deny write access to the file.
    2 deny none—Permit both read and write access to the file.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out returns refnum.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1789

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1789 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1790 ordinal=1790 -->
## Functions

Functions

       This function temporarily overrides permissions for a specific instance of the file. This
       function does not modify permissions for the file itself. When you grant access to an
       instance of a file, LabVIEW removes the override caused by denying access to the file so
       that the file permissions and the deny mode associated with refnum determine
      whether other refnums, VIs, or applications can read from or write to that instance of
       the file. After the file refnum is closed, the permissions for that instance of the file are
      no longer overridden.

           Note You cannot deny access to a datalog file.

       File/DirectoryFile/Directory InfoInfo FunctionFunction

       Returns information about the file or directory specified by path, including its size, its
        last modification date, whether it is a directory, whether it is a shortcut, and the
       resolved path if the file or directory is a shortcut. This function does not work for files
       inside an LLB.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      path —

           path specifies the absolute path to the file or directory whose attributes you want to determine.

                    If you wire an empty path to path, directory returns TRUE.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       directory —


1790   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1790 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1791 ordinal=1791 -->
## Functions

Functions


    directory is TRUE if the path points to a directory and FALSE otherwise.

       If you wire an empty path constant to path, directory returns TRUE.
   •      path out —

    path out returns path unchanged.

   •       size —

     size indicates the size of the file or directory specified by path.

       If path specifies a directory, size indicates the number of items in the directory. (Windows) If
    path is an empty path, size indicates the number of drives on the computer. (macOS and Linux)
       If path is an empty path, size indicates the number of volumes on the computer. Otherwise, size
     indicates the length in bytes of the specified file, whether the file is a datalog file or a byte
    stream file.
   •       last mod —

     last mod indicates the date and time at which the file or directory was last modified. The
   number is a time zone-independent number of seconds that have elapsed since 12:00 a.m.,
     Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00].

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      resolved path —

    resolved path returns the path to the shortcut target.

   •      shortcut —

    shortcut is TRUE if the path points to a shortcut and FALSE otherwise.


GetGet VolumeVolume InfoInfo FunctionFunction

Returns information about the volume containing the file or directory specified by
path, including the total storage space provided by the volume and the amount free in
bytes.


                                                    © National Instruments 1791

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1791 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1792 ordinal=1792 -->
## Functions

Functions


      Inputs/Outputs

               •      path —

           path specifies the absolute path to the file or directory whose volume attributes you want to
            determine.

                    If you specify an empty or relative path, this function returns an error.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     volume path —

          volume path is a new path that specifies the volume on which the specified file or directory
              resides.

               •      path out —

           path out returns path unchanged.

               •       size (bytes) —

             size (bytes) indicates the amount of storage, in bytes, provided by the specified volume.

               •       free (bytes) —

             free (bytes) indicates the amount of storage, in bytes, available on the specified volume.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      sector size (bytes) —

            sector size (bytes) indicates the size, in bytes, of the smallest physical storage unit on disk. If you
          open a file without buffering, you must make the size of the data in that file a multiple of the


1792   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1792 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1793 ordinal=1793 -->
## Functions

Functions


    given sector size.


The volume where the file is located determines the sector size.

CreateCreate FolderFolder FunctionFunction

Creates the appropriate folder specified by path.

This function creates all folders that do not already exist in the specified path. If a file
or folder already exists at the specified location, the function returns an error instead
of overwriting the existing file or folder.


Inputs/Outputs

   •     prompt (Create Folder) —

    prompt (Create Folder) is the message that appears above the list of files and directories, or
     folder, in the file dialog box.

   •      path (use dialog) —

    path is the absolute path to the folder you want to create.

       If you do not wire data to path, the function displays a dialog box from which you can select a
     folder. If you specify an empty or relative path, this function returns an error.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      created path —

    created path specifies the new location of the folder.


                                                    © National Instruments 1793

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1793 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1794 ordinal=1794 -->
## Functions

Functions


                    If the operation is unsuccessful, this function sets created path to <Not A Path>.

               •      cancelled —

            cancelled is TRUE if you cancel the file dialog box. Otherwise, cancelled is FALSE, even if this
             function returns an error.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


        ListList FolderFolder FunctionFunction

       Returns two arrays of strings listing the names of all files and folders found in path,
        filtering both arrays based upon pattern and filtering the filenames array based upon
       the specified datalog type.


      Inputs/Outputs

               •      datalog type —

            datalog type can be any data type and restricts the filenames returned to only datalog files
            containing records of the specified data type. Datalog records contain a time stamp cluster and a
              cluster of the front panel data.

               •      path —

           path identifies the folder whose contents you want to determine. If this is not an existing folder,
              this function sets filenames and folder names to empty arrays and returns an error. If path
            points to a VI library (*.llb), filenames returns the contents of the VI library and folder names
             returns an empty array.

               •       error in —


1794   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1794 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1795 ordinal=1795 -->
## Functions

Functions


  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      pattern —

  pattern restricts the files and directories returned to those whose names match pattern.

  The pattern matching in this function is similar to the matching used in matching wildcards in
  Windows and Linux filenames and is not like the regular expression matching performed by the
  Match Pattern function and the Match Regular Expression function. If you specify characters
  other than the question mark character (?) or the asterisk character (*), the function displays
  only files or directories that contain those characters. You can use the question mark character
   (?) to match any single character. You can use the asterisk character (*) to match any sequence of
  zero or more characters.

   If pattern is an empty string, the VI returns all files and directories.

•      path out —

  path out returns path unchanged.

•      filenames —

  filenames contains the names of the files found in the specified directory. This function does not
  return the names of files found in folders within the directory. This function sorts the returned
  filenames alphabetically.

•       folder names —

  folder names contains the names of the folders found in the specified directory. This function
  sorts the folder names alphabetically. If path is an empty path, folder names contains the names
  of the drives on the computer.

•       error out —

  error out contains error information. This output provides standard error out functionality.


    Note Front panel controls might not update while the function lists files and
      folders found in the specified directory. The controls update when the
      function finishes listing the files and folders.


                                                   © National Instruments 1795

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1795 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1796 ordinal=1796 -->
## Functions

Functions

      CheckCheck ifif FileFile oror FolderFolder ExistsExists

      Checks whether a file or folder exists on disk at a specified path. This VI works with
       standard files and folders as well as files in LLB files.


      Inputs/Outputs

               •      path —

           path specifies the path to the file or folder you want LabVIEW to look for.

                    If you use this VI to check the validity of a network path, make sure that you connect to the
           network first.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     dup path —

          dup path returns path unchanged.

               •        file or folder exists? —

                file or folder exists? is TRUE if the file or folder you specify in path exists on disk and FALSE if the
                 file or folder you specify in path does not exist on disk. If you wire an empty path to path, file or
             folder exists? returns TRUE because the empty path refers to the list of drives mapped to the
            computer. (macOS) The empty path refers to the mounted volumes. (Linux) The empty path
              refers to the root directory.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1796   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1796 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1797 ordinal=1797 -->
## Functions

Functions

RecursiveRecursive FileFile ListList

Lists the contents of a folder or LLB.


Inputs/Outputs

   •      Folder Path —

    Folder Path specifies the path to the folder or LLB whose contents you want LabVIEW to return.

          Note This VI does not support shortcuts and symbolic links to folders or LLB files.
             Specify a path to the target folder or LLB instead of its shortcut or symbolic link.

   •      Treat LLBs as Folders? —

    Treat LLBs as Folders? specifies whether to list LLBs as files or folders. If Treat LLBs as Folders?
      is TRUE, this VI includes LLBs in the list of folders. If Treat LLBs as Folders? is FALSE, this VI
    includes LLBs in the list of files. The default is FALSE.

       If Folder Path specifies the path to an LLB, this VI ignores this input and returns all files,
    including LLBs, in All Files in Dir.

   •      Continue Recursing on Error? (F) —

    Continue Recursing on Error? specifies whether to continue recursing directories if an error
    occurs. If Continue Recursing on Error? is TRUE, the VI continues recursing directory contents
     after the error occurs. If Continue Recursing on Error? is FALSE, the VI stops recursing directory
    content when the error occurs.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      pattern —


                                                    © National Instruments 1797

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1797 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1798 ordinal=1798 -->
## Functions

Functions


            pattern specifies the pattern for files for which you want to search in Folder Path.

           You can use the question mark character (?) to match any single character. You can use the
              asterisk character (*) to match any sequence of zero or more characters. For example, if you
          want this VI to find a list of the VIs in a folder, specify *.vi for pattern.

               •      Folders to Exclude —

            Folders to Exclude specifies folder names you want to exclude during the recursion. Any folder
           you exclude does not appear in the All Folders array. This input is case insensitive.

               •        All Folders —

               All Folders returns a list of all subfolders, and shortcuts to folders in Folder Path.

               •     dup Folder Path —

          dup Folder Path returns Folder Path unchanged.

               •        All Files in Dir —

               All Files in Dir returns a list of all files in Folder Path. If Treat LLBs as Folders? is set to TRUE, the
                  list of files includes LLBs. The list also includes shortcuts to files.

               •     Number of Files —

         Number of Files returns the number of files in the All Files in Dir array.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      PathPath ToTo StringString FunctionFunction

       Converts path into a string describing a path in the standard format of the platform.

      The connector pane displays the default data types for this polymorphic function.


1798   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1798 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1799 ordinal=1799 -->
## Functions

Functions

Inputs/Outputs

   •      path —

    path is the path, array of paths, cluster of paths, or array of clusters of paths you want to convert
    to a string.

       If path is <Not A Path>, the function sets string to <Not A Path>.
   •       string —

     string is the path descriptor(s) represented by path in the standard format for the current
    platform. string is of the same data type structure as path.


StringString ToTo PathPath FunctionFunction

Converts a string, describing a path in the standard format for the current platform, to
a path.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •       string —

     string can be a string or any data structure that contains only strings, such as an array or clusters
     of strings.

   •      path —

    path is the platform-independent representation of the path described by string.

       If string is not a valid path descriptor on the current platform, the function sets path to <Not a
    Path>. path is of the same data type structure as string.

          Note If string is <Not a Path>, the function returns a path to <Not a Path>. If
           you attempt to use the path, LabVIEW cannot find the file and throws an error.


                                                    © National Instruments 1799

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1799 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1800 ordinal=1800 -->
## Functions

Functions

      PathPath toto ArrayArray ofof StringsStrings FunctionFunction

       Converts a path into an array of strings and indicates whether the path is relative.


      Inputs/Outputs

               •      path —

           path is the path you want to convert to an array of strings.

                    If path is <Not A Path>, the array of strings is empty and relative is FALSE.
               •       relative —

             relative indicates whether the path you converted is a relative path or an absolute path.

                    If TRUE, it is a relative path. If FALSE, it is an absolute path.
               •      array of strings —

            array of strings contains the components of the path.

          The first element is the first step of the path hierarchy. For file systems that support multiple
            volumes, the first element is the volume name. If path is a network path, the first element of
            array of strings includes the name of the server in addition to the first step of the path hierarchy.
          The last element of array of strings is the file or directory specified by the path.

       ArrayArray ofof StringsStrings toto PathPath FunctionFunction

       Converts an array of strings into a relative or absolute path.

           If you have an empty string in the array, the directory location before the empty string
         is deleted in the path output. This behavior is similar to moving up a level in directory
       hierarchy.


1800   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1800 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1801 ordinal=1801 -->
## Functions

Functions

Inputs/Outputs

   •       relative —

     relative indicates whether you want to create a relative path or an absolute path.

       If TRUE, the function creates a relative path. If FALSE (default), the function creates an absolute
    path. If FALSE and the path specified is not valid as an absolute path (for example, the path
   means go up a level), the function sets path to <Not A Path>.

   •      array of strings —

    array of strings contains the names of the components of the path you want to build.

    The first element is the highest level of the path hierarchy (the volume name, for file systems
    that support multiple volumes), and the last element is the last element of the hierarchy. An
    element that contains an empty string tells LabVIEW to go up a level in the hierarchy.

          Note Each string in the array of strings must represent a single element of the
            complete path. Partial paths, such as test\subtest, are not valid as array
            elements because they might produce invalid paths on platforms that use different
              directory separators.

   •      path —

    path is the resulting path.


Suppose the path to the VI containing this function is c:\dir1\main.vi. To use this
function to build a relative path to another VI such as c:\dir1\dir2\called.vi,
wire TRUE to relative. In array of strings, enter dir2 as the first element and
called.vi as the second element. The function returns a relative path of dir2\
called.vi. You can use the Build Path function to append the relative path to the
output of the Current VI's Path function.

To build an absolute path to c:\dir1\dir2\called.vi, wire FALSE to relative. In
array of strings, enter c as the first element, dir1 as the second element, dir2 as
the third element, and called.vi as the fourth element. The function returns an
absolute path of c:\dir1\dir2\called.vi.


                                                    © National Instruments 1801

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1801 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1802 ordinal=1802 -->
## Functions

Functions

     RefnumRefnum toto PathPath FunctionFunction

       Returns the path associated with the specified refnum.


      Inputs/Outputs

               •     refnum —

          refnum is the refnum of an open file whose associated path you want to determine.

                    If refnum is not a valid refnum, this function sets path to <Not A Path>, meaning refnum is
            not associated with any open file. You can wire only file refnums to refnum. You cannot wire
             configuration file refnums to refnum.
               •      path —

           path is the corresponding path to refnum.


      PathPath TypeType FunctionFunction

       Returns the type of the specified path, indicating whether it is an absolute, relative, or
      <Not A Path>.

       This function does not verify that the path exists on the computer. It checks only the
       syntax of the path. Use the File/Directory Info function to verify that a file or directory
        exists on the computer.


      Inputs/Outputs

               •      path —

           path specifies the path whose syntax you want to check.

               •      type —

1802   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1802 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1803 ordinal=1803 -->
## Functions

Functions


    type indicates the type of the specified path.

   UNC file paths are absolute file paths. Use two leading backslashes (\\) to represent UNC file
    paths. type returns <Not A Path> only when you wire the Not A Path constant to this
     function.

    0     Absolute path
    1      Relative path
    2    <Not A Path>


CompareCompare TwoTwo PathsPaths

Compares Path 1 to Path 2 and returns a relative path between the two paths, the
common path between the two paths, and a Boolean that indicates whether the paths
are on the same path hierarchy level.

For example, if Path 1 is C:\folder\sub\test.txt and Path 2 is C:\folder\
sub2\dir\test2.doc, Relative Path from 1 to 2 returns ..\..\sub2\dir\
test2.doc. Common Path returns C:\folder, and Path 2 Relative to Path 1
returns FALSE because you have to go up two levels in the path hierarchy to get to the
common path between Path 1 and Path 2.


Inputs/Outputs

   •      Path 1 —

    Path 1 specifies the first path.

   •      Path 2 —

    Path 2 specifies the second path.

   •       error in (no error) —


                                                    © National Instruments 1803

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1803 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1804 ordinal=1804 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       Relative Path from 1 to 2 —

             Relative Path from 1 to 2 returns the relative path you have to take on disk to get from Path 1 to
           Path 2.

               •    Common Path —

        Common Path returns the part of the absolute path that Path 1 shares with Path 2.

               •      Path 2 Relative to Path 1? —

           Path 2 Relative to Path 1? is TRUE if Path 1 is on the same directory level as Path 2. Otherwise,
              this output is FALSE.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      GetGet FileFile ExtensionExtension

       Returns the file extension, without the period (.), of a file you specify.


      Inputs/Outputs

               •        file —

                file specifies the path to the file whose extension you want LabVIEW to return.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


1804   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1804 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1805 ordinal=1805 -->
## Functions

Functions

   •     dup file —

   dup file returns file unchanged.

   •      lowercase file extension —

    lowercase file extension returns the extension of the file, without the period (.). LabVIEW always
    returns a lowercase file extension, even if file contains uppercase letters.

   •      filename without extension —

    filename without extension returns the name of the file you specify in file without the directory
    path, period (.), or file extension. Unlike lowercase file extension, filename without extension
    matches the case of the original filename.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      unmodified file extension —

    unmodified file extension returns the extension of the file you specify in file, without the period
       (.). Unlike lowercase file extension, unmodified file extension matches the case of the original
      file extension.


FileFile ChecksumChecksum

Computes the message digest on the contents of a file. You must manually select the
polymorphic instance you want to use.


  • SHA-256 File Checksum VI
  • SHA-224 File Checksum VI
  • SHA-512 File Checksum VI
  • SHA-384 File Checksum VI
  • SHA-512-256 File Checksum VI
  • SHA-512-224 File Checksum VI
  • SHA3-224 File Checksum VI


                                                    © National Instruments 1805

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1805 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1806 ordinal=1806 -->
## Functions

Functions

            • SHA3-256 File Checksum VI
            • SHA3-384 File Checksum VI
            • SHA3-512 File Checksum VI
   SHA-256SHA-256 FileFile ChecksumChecksum VIVI

      Computes the message digest on the contents of a file. You must manually select the
      polymorphic instance you want to use.


      Inputs/Outputs

               •      path —

           path specifies the path to the file for which you want to compute the message digest.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       digest —

             digest returns the SHA-256 message digest of the contents of the file as a hexadecimal string.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   SHA-224SHA-224 FileFile ChecksumChecksum VIVI

      Computes the message digest on the contents of a file. You must manually select the
      polymorphic instance you want to use.


1806   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1806 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1807 ordinal=1807 -->
## Functions

Functions


Inputs/Outputs

   •      path —

    path specifies the path to the file for which you want to compute the message digest.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       digest —

    digest returns the SHA-224 message digest of the contents of the file as a hexadecimal string.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SHA-512SHA-512 FileFile ChecksumChecksum VIVI

Computes the message digest on the contents of a file. You must manually select the
polymorphic instance you want to use.


Inputs/Outputs

   •      path —

    path specifies the path to the file for which you want to compute the message digest.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 1807

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1807 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1808 ordinal=1808 -->
## Functions

Functions


            standard error in functionality.

               •       digest —

             digest returns the SHA-512 message digest of the contents of the file as a hexadecimal string.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   SHA-384SHA-384 FileFile ChecksumChecksum VIVI

      Computes the message digest on the contents of a file. You must manually select the
      polymorphic instance you want to use.


      Inputs/Outputs

               •      path —

           path specifies the path to the file for which you want to compute the message digest.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       digest —

             digest returns the SHA-384 message digest of the contents of the file as a hexadecimal string.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1808   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1808 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1809 ordinal=1809 -->
## Functions

Functions

SHA-512-256SHA-512-256 FileFile ChecksumChecksum VIVI

Computes the message digest on the contents of a file. You must manually select the
polymorphic instance you want to use.


Inputs/Outputs

   •      path —

    path specifies the path to the file for which you want to compute the message digest.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       digest —

    digest returns the SHA-512/256 message digest of the contents of the file as a hexadecimal
     string.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SHA-512-224SHA-512-224 FileFile ChecksumChecksum VIVI

Computes the message digest on the contents of a file. You must manually select the
polymorphic instance you want to use.


                                                    © National Instruments 1809

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1809 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1810 ordinal=1810 -->
## Functions

Functions

      Inputs/Outputs

               •      path —

           path specifies the path to the file for which you want to compute the message digest.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       digest —

             digest returns the SHA-512/224 message digest of the contents of the file as a hexadecimal
               string.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   SHA3-224SHA3-224 FileFile ChecksumChecksum VIVI

      Computes the message digest on the contents of a file. You must manually select the
      polymorphic instance you want to use.


      Inputs/Outputs

               •      path —

           path specifies the path to the file for which you want to compute the message digest.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       digest —


1810   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1810 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1811 ordinal=1811 -->
## Functions

Functions


    digest returns the SHA3-224 message digest of the contents of the file as a hexadecimal string.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SHA3-256SHA3-256 FileFile ChecksumChecksum VIVI

Computes the message digest on the contents of a file. You must manually select the
polymorphic instance you want to use.


Inputs/Outputs

   •      path —

    path specifies the path to the file for which you want to compute the message digest.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       digest —

    digest returns the SHA3-256 message digest of the contents of the file as a hexadecimal string.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SHA3-384SHA3-384 FileFile ChecksumChecksum VIVI

Computes the message digest on the contents of a file. You must manually select the


                                                    © National Instruments 1811

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1811 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1812 ordinal=1812 -->
## Functions

Functions

      polymorphic instance you want to use.


      Inputs/Outputs

               •      path —

           path specifies the path to the file for which you want to compute the message digest.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       digest —

             digest returns the SHA3-384 message digest of the contents of the file as a hexadecimal string.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   SHA3-512SHA3-512 FileFile ChecksumChecksum VIVI

      Computes the message digest on the contents of a file. You must manually select the
      polymorphic instance you want to use.


      Inputs/Outputs

               •      path —

           path specifies the path to the file for which you want to compute the message digest.

               •       error in —

1812   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1812 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1813 ordinal=1813 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       digest —

    digest returns the SHA3-512 message digest of the contents of the file as a hexadecimal string.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


GenerateGenerate TemporaryTemporary FileFile PathPath

Returns a unique file path to the temporary directory. This VI only returns a path. It
does not create the temporary file.


Inputs/Outputs

   •      Temporary File Extension (tmp) —

    Temporary File Extension (tmp) specifies the file extension.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Unique Temporary File Path —

    Unique Temporary File Path returns a unique path to a non-existent file in the temporary
     directory. You can use this path with other VIs when you want to create a file in the temporary
     directory.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1813

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1813 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1814 ordinal=1814 -->
## Functions

Functions

      DatalogDatalog

      Use the Datalog functions to open and close datalog files, read from and write to
       datalog files, get and set datalog file positions, and get and set the number of datalog
       records.


         Palette
                       Description        Object

        Open/Create/                    Opens an existing datalog file, creates a new datalog file, or replaces an existing
        Replace                       datalog file, programmatically or interactively using a file dialog box. This function         Datalog                     does not work for files inside an LLB.
         Function

         Close File      Closes an open file specified by refnum and returns the path to the file associated
         Function      with the refnum.

                     Reads records from an open datalog file specified by refnum and returns it in       Read Datalog
                         record(s). Reading begins at the current datalog position. Use the Set Datalog         Function                        Position function to move the current datalog position of the file.

         Set Datalog                    Moves the current datalog position of the file identified by refnum to the datalog         Position                        position indicated by offset (in records) according to the mode in from.
         Function

         Set Number
         of Records     Sets the size in records of the datalog file identified by refnum.
         Function

         Write Datalog  Writes record(s) to an open datalog file specified by refnum. Sets the current
         Function      datalog position to the end of the file before writing.

        Get Datalog
         Position       Returns the current datalog position of the datalog file specified by refnum.
         Function

        Get Number
         of Records     Returns the size in records of the datalog file identified by refnum.
         Function


1814   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1814 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1815 ordinal=1815 -->
## Functions

Functions

Open/Create/ReplaceOpen/Create/Replace DatalogDatalog FunctionFunction

Opens an existing datalog file, creates a new datalog file, or replaces an existing
datalog file, programmatically or interactively using a file dialog box. This function
does not work for files inside an LLB.

You can optionally specify a dialog prompt or default filename. Use this function with
the intermediate Write Datalog or Read Datalog functions. Use the Close File function
to close the reference to the file.


Inputs/Outputs

   •      record type —

    record type can be any data type. Wire a cluster matching the record data type and cluster order
    to this input when creating datalog files.

   •     prompt —

    prompt is the message that appears above the list of files and directories or folder in the file
    dialog box.

   •      datalog path (use dialog) —

    datalog path is the absolute path to the file.

       If you do not wire datalog path, the function displays a dialog box from which you can select a
      file. If you specify an empty or relative path, this function returns an error.

   •      operation (0:open) —

    operation is the operation to perform. Error 43 occurs if you cancel the dialog box.


                                                    © National Instruments 1815

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1815 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1816 ordinal=1816 -->
## Functions

Functions


           0 open (default)—Opens an existing file. Error 7 occurs if the file cannot be found.
           1 replace—Replaces an existing file by opening the file and setting its end of file to 0.
           2 create—Creates a new file. Error 10 occurs if the file already exists.
           3 open or create—Opens an existing file or creates a new file if one does not exist.
             replace or create—Creates a new file or replaces a file if it exists. This VI replaces a file by           4
            opening the file and setting its end of file to 0.
             replace or create with confirmation—Creates a new file or replaces a file if it exists and you           5              give permission. This VI replaces a file by opening the file and setting its end of file to 0.

               •      access (0:read/write) —

            access specifies how you plan to access the file.

                       read/write           0                         (default)
           1         read-only
           2         write-only

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is the reference number of the open file.

          The value is Not A Refnum if the file cannot be opened.

               •      cancelled —

            cancelled is TRUE if you cancel the file dialog box or if you do not select the replacement in an
            advisory dialog box.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1816   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1816 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1817 ordinal=1817 -->
## Functions

Functions

CloseClose FileFile FunctionFunction

Closes an open file specified by refnum and returns the path to the file associated with
the refnum.

Error I/O operates uniquely in this function, which closes the file regardless of whether
an error occurred in a preceding operation. This ensures that files are closed correctly.


Inputs/Outputs

   •     refnum —

    refnum is the file refnum associated with the file you want to close.

   •       error in —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      path —

    path is the corresponding path to refnum.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Datalog\Datalog File.lvproj


                                                    © National Instruments 1817

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1817 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1818 ordinal=1818 -->
## Functions

Functions

   ReadRead DatalogDatalog FunctionFunction

      Reads records from an open datalog file specified by refnum and returns it in
       record(s). Reading begins at the current datalog position. Use the Set Datalog Position
       function to move the current datalog position of the file.


      Inputs/Outputs

               •     refnum —

          refnum is the file refnum associated with the file you want to read. If you want to read more than
          one element at a time, wire the count parameter.

               •      count (1) —

           count is the number of datalog records to read.

          The function returns count data elements in record(s), or if it reaches the end of the file, it
             returns all the complete data elements read thus far and an end-of-file error. By default, the
             function returns a single data element. If count is –1, the function reads the entire file. If count is
              less than –1, the function returns an error.

                    If count calls for an array of elements and the record(s) data type is an array, the function
            automatically returns a cluster of arrays or cluster array because LabVIEW does not allow arrays
             of arrays.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out returns refnum.

               •       record(s) —


1818   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1818 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1819 ordinal=1819 -->
## Functions

Functions


    record(s) contains the datalog records read from the file.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet DatalogDatalog PositionPosition FunctionFunction

Moves the current datalog position of the file identified by refnum to the datalog
position indicated by offset (in records) according to the mode in from.

The Write Datalog function changes the current datalog position to the end of the file.
You cannot use this function to write to a different position in the file.


Inputs/Outputs

   •     refnum —

    refnum is the file refnum associated with the datalog file whose datalog position you want to
     set.

   •       offset (in records) (0) —

     offset (in records) specifies how many records from the location specified by from to set the
    datalog position.

   •      from (0:start) —

    from, together with offset (in records), specifies where to set the datalog position. If you wire
     offset (in records), from defaults to 0, and the offset is relative to the beginning of the file. If you
   do not wire offset (in records), offset (in records) defaults to 0, from defaults to 2, and the
    operation starts at the current datalog position.


                                                    © National Instruments 1819

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1819 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1820 ordinal=1820 -->
## Functions

Functions


             start—Sets the datalog position offset (in records) from the beginning of the file. If from is 0,           0
               offset (in records) should be positive.
            end—Sets the datalog position offset (in records) from the end of the file. If from is 1, offset (in           1              records) should be negative.
           2 current—Sets the datalog position offset (in records) from the current datalog position.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out returns refnum.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet NumberNumber ofof RecordsRecords FunctionFunction

       Sets the size in records of the datalog file identified by refnum.

      LabVIEW reduces the number of records in a datalog file by deleting the last records in
       the file until the records equal the number you enter. The number of records you enter
      must be smaller than the number of records the datalog file holds. This function is not
      a permanent limit, but an operation that affects the records already in the datalog file
      one time. For example, if a datalog file contains 10 records and you set the number of
       records to 5, then LabVIEW deletes the last 5 records. However, if you add 5 records,
       the file then contains 10 records.


      Inputs/Outputs

               •     refnum —

1820   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1820 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1821 ordinal=1821 -->
## Functions

Functions


    refnum identifies the datalog file whose size you want to set.

   •      # of records —

    # of records is the size in records of the datalog file you want to set.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out returns refnum.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

WriteWrite DatalogDatalog FunctionFunction

Writes record(s) to an open datalog file specified by refnum. Sets the current datalog
position to the end of the file before writing.


Inputs/Outputs

   •     refnum —

    refnum is the file refnum associated with the file to which you want to write.

   •       record(s) —

    record(s) contains the datalog records to write to the datalog file.

    record(s) must be either a data type that matches the record type specified when you open or
    create the file or an array of such record types. In the former case, this function writes record(s)

                                                    © National Instruments 1821

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1821 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1822 ordinal=1822 -->
## Functions

Functions

            as a single record in the datalog file. If necessary, the function coerces numeric data to the
            representation of the record type of this parameter. In the latter case, this function writes each
            record in the array separately in the datalog file in row-major order.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out returns refnum.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   GetGet DatalogDatalog PositionPosition FunctionFunction

       Returns the current datalog position of the datalog file specified by refnum.


      Inputs/Outputs

               •     refnum —

          refnum is the file refnum associated with the datalog file whose datalog position you want to
              get.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out returns refnum.

               •       offset (in records) —

1822   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1822 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1823 ordinal=1823 -->
## Functions

Functions


     offset (in records) returns the current datalog position in records.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetGet NumberNumber ofof RecordsRecords FunctionFunction

Returns the size in records of the datalog file identified by refnum.


Inputs/Outputs

   •     refnum —

    refnum identifies the datalog file whose size you want to get.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out returns refnum.

   •      # of records —

    # of records is the number of records in the datalog file.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1823

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1823 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1824 ordinal=1824 -->
## Functions

Functions

      PackedPacked LibraryLibrary

      Use the Packed Library VIs to get and return data from a packed project library.


         Palette Object      Description

        Get Exported File    Returns the qualified names and paths of the exported files in a packed
           List                  project library.

        Get Exported File                            Returns the path of an exported file in a packed project library.        Path

                            Returns the path to a packed project library for the VI you specify in vi
        Packed Library Path                              reference.

   GetGet ExportedExported FileFile ListList

       Returns the qualified names and paths of the exported files in a packed project library.


      Inputs/Outputs

               •      packed library path —

           packed library path specifies the path to the packed library.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       qualified names —


1824   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1824 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1825 ordinal=1825 -->
## Functions

Functions


    qualified names returns an array of strings with the qualified names of the exported files in the
    packed library.

   •      paths —

    paths returns an array with the paths to the exported files in the packed library.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetGet ExportedExported FileFile PathPath

Returns the path of an exported file in a packed project library.


Inputs/Outputs

   •      packed library path —

    packed library path specifies the path to the packed library.

   •       qualified name —

    qualified name specifies the qualified name of the exported file in the packed library.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      path —

    path returns the path to the exported file in the packed library.

   •       error out —


                                                    © National Instruments 1825

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1825 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1826 ordinal=1826 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.

   PackedPacked LibraryLibrary PathPath

       Returns the path to a packed project library for the VI you specify in vi reference.


      Inputs/Outputs

               •        vi reference —

              vi reference specifies the reference to a VI in a packed library.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •        vi reference out —

              vi reference out returns vi reference unchanged.

               •      packed library path —

           packed library path returns a path to the packed library that contains the VI you specify in vi
             reference. If the referenced VI is not in a packed library, packed library path returns an empty
             path.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      CreateCreate DirectoryDirectory RecursiveRecursive

       Creates a directory and any parent directories it requires to exist.

1826   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1826 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1827 ordinal=1827 -->
## Functions

Functions


Inputs/Outputs

   •       directory —

    directory specifies the path to the directory to create. If you specify a directory that already
     exists, this VI does nothing.

   •     maximum path length —

   maximum path length specifies the maximum number of characters allowed in the path. The
     default is 252.

   •      permissions —

    permissions specifies the permissions setting for the file or directory. The default is 111101101,
    which is rwx r-x r-x in common file notation, and means the current user has permission to read,
     write, and execute files in this directory; the current user's group members have permission only
    to read and execute; all system users have permission only to read and execute.

    Refer to Setting Permissions for more information about how to define the permissions you
    want to set.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       directory copy —

    directory copy returns directory unchanged.

   •       directories created —

     directories created returns the path to the directory and paths to any parent directories this VI
     creates.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1827

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1827 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1828 ordinal=1828 -->
## Functions

Functions

      CreateCreate FileFile andand ContainingContaining FoldersFolders

       Creates a file at a specified path and any folders within that path that do not exist.


      Inputs/Outputs

               •        file path —

                file path specifies the path to the file you want to create. You must specify an absolute path. If
           you specify an empty or relative path, this VI returns an error.

               •      access —

            access specifies how to access the file.

          The default is write-only.

           0         read/write
           1         read-only
           2         write-only

               •      permissions —

            permissions specifies the permissions setting for the file or directory. The default is 111101101,
           which is rwx r-x r-x in common file notation, and means the current user has permission to read,
              write, and execute files in this directory; the current user's group members have permission only
             to read and execute; all system users have permission only to read and execute.

             Refer to Setting Permissions for more information about how to define the permissions you
          want to set.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      disable buffering (F) —

1828   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1828 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1829 ordinal=1829 -->
## Functions

Functions


    disable buffering specifies if the file opens without buffering. The default is FALSE.

       If you want to read or write a data file to a Redundant Array of Independent Disks (RAID),
    consider opening the file without buffering to speed up data transfers. To disable buffering, wire
    a TRUE value to the disable buffering input.

          Note If you have a small amount of data to transfer, you might not notice a
              difference if you disable buffering.

   (macOS and Linux) LabVIEW ignores this input.

   •     refnum out —

    refnum out returns the reference number of the file this VI creates.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ContiguousContiguous andand NoncontiguousNoncontiguous ArrayArray SlicesSlices

To optimize performance, LabVIEW sometimes creates array slices from the arrays you
wire to certain Array functions. An array slice is an array created from another array,
and it contains some of the elements from the original array. LabVIEW expresses an
array slice as a (sub)array  in the Context Help window when you move the cursor
over the wire for the resulting array. For example, (1-D (sub)array of) indicates that
the function creates an array slice, while (1-D array of) indicates the resulting array
contains all of the resulting elements.

      Note The Context Help window only differentiates between arrays and
        array slices if you allow debugging for the VI on the Execution page of the VI
        Properties dialog box.

If LabVIEW creates an array slice, it may create a contiguous array slice, which stores
data adjacently, or a noncontiguous array slice, which stores data nonadjacently. If you
wire an array slice to the Preallocated Read from Binary File function, you might need
to know whether the array slice is contiguous or noncontiguous, because the function

                                                    © National Instruments 1829

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1829 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1830 ordinal=1830 -->
## Functions

Functions

       provides different levels of support that depend on the array you use.

      Determining Whether LabVIEW Creates a Contiguous or Noncontiguous
      Array Slice

       Array functions in LabVIEW access data in row-major order. If you arrange the elements
       of an array in row-major order, then LabVIEW represents that array in memory
       contiguously. LabVIEW represents the following 2D array in memory contiguously as a
      1D line from 0 to 15:

           If you wire the previous array to the Index Array function and set the index (row) input
       to 0, LabVIEW may return an array or a contiguous array slice. The array slice is
       contiguous because LabVIEW represents the values in adjacent memory offsets 0, 1, 2,
        3.

           If you wire the previous array to the Index Array function and set the index (col) input
       to 0, LabVIEW may return an array or a noncontiguous array slice. The array slice is
      noncontiguous because LabVIEW represents the values in nonadjacent memory offsets
        0, 4, 8, 12.

      The following functions might return an array slice. If one of these functions returns an
       array slice, use the following guidelines to determine whether LabVIEW creates a
       contiguous or noncontiguous array slice:

            • Array Subset—If LabVIEW represents the output from this function contiguously in
         memory, it creates a contiguous array slice.
            • Reverse 1D Array—If you wire an array to this function, it creates a noncontiguous
           array slice. If you wire an already reversed array slice to this function, it creates a
          contiguous array slice.
            • Split 1D Array—If you wire an array to this function, it creates a contiguous array
             slice. If you wire a noncontiguous array slice to this function, the resulting array
             slice is either contiguous or noncontiguous based on how LabVIEW represents the
           array slice in memory.
            • Transpose 2D Array—This function creates a noncontiguous array slice unless you
          wire an already transposed array to the function.
            • Cluster to Array—This function creates a contiguous array slice.
            • Index Array—This function creates a contiguous array slice unless you specify to
          index the array column-wise.

1830   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1830 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1831 ordinal=1831 -->
## Functions

Functions

  • Decimate 1D Array—This function creates a noncontiguous array slice.

SettingSetting PermissionsPermissions

The Set Permissions function includes a permissions input that allows you to control
access to files and directories that you create. To define the permissions you want to
set, you can wire the permissions output of the Get Permissions function to the
permissions input of the Set Permissions function, or you can wire a constant or a
control.

The following illustration shows the format of the permissions parameter.


The 9 bits that the permissions parameter uses are divided into three sets: user, group,
and others. Each set is divided into three permission categories: read, write, and
execute. Read determines if members of a set can read a file or directory. Write
determines if members of a set can write data to a file or directory. Execute determines
if members of a set can execute the file. A 1 in the bit grants permission.

For example, the following illustration shows how to grant a user permission to read
from, write to, and execute a file, and deny permission from the other two sets.


This structure is based on the Linux permission bits that govern read, write, and
execute permissions for users, groups, and others.

(Windows) Use of the permissions parameter is very limited on non-Linux operating
systems. You can use permissions to change only write permissions for users (bit 7);
the operating system ignores all other changes to the bits. Wire the binary value 0 to
permissions to deny user write permissions. The operating system grants read and
write permissions by default when you create any new file or directory but does not
allow you to change read permissions or set permissions for groups or others. Execute

                                                    © National Instruments 1831

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1831 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1832 ordinal=1832 -->
## Functions

Functions

       permissions do not apply to non-Linux operating systems. Therefore, wiring 0 to
      permissions modifies only user write permissions for the new file or directory.
      (Windows) The operating system also ignores permissions when creating new
        directories. You can use permissions only when creating a new file.

      (macOS) The read, write, and execute categories correspond to the See Files, Make
      Changes, and See Folders access rights, respectively.

      You can enter the value for permissions in any numeric format. For example, you can
      change the numeric format to octal format to shorten the binary number with which
      you set the file or directory permissions. Octal format shortens each three-bit group
       within the parameter to a single octal value. (Windows) For example, to make a file
       writable, enter the octal value 200, which corresponds to the binary representation
     10000000. (Linux) To grant users read, write, and execute permissions, enter the
       octal value 700, which corresponds to the binary value 111000000.

    UNCUNC FilenameFilename SupportSupport ofof FileFile I/OI/O VIsVIs onon WindowsWindows

     UNC filenames provide the primary means for specifying the location of a file or
       directory in a networked environment. In LabVIEW, you can enter and view UNC
       filenames in path controls, indicators, and constants in a file dialog box. UNC
       filenames use the following path form.

     \\<machine>\<share name>\<dir>\...\<file or dir>

      where <machine> is the name of the computer that you want to access on the
       network, <share name> is the name of a shared drive on that machine, <dir>\...
       consists of the name of the directory and subdirectories in which you want to store the
          file, and <file> consists of the name that you want to call the file.

     TimingTiming

      Use the Timing VIs and Functions to manipulate the speed at which an operation
       executes and to retrieve time and date information from the computer clock.


1832   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1832 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1833 ordinal=1833 -->
## Functions

Functions


Palette            Description
Object

Tick Count
(ms)       Returns the value of the millisecond timer.
Function

           Returns the relative current time in seconds. Use the difference between twoHigh            successive values to measure the elapsed time between the calls. Use this VI toResolution          measure time spans with much higher resolution than you can obtain from the TickRelative          Count (ms) function. The time resolution of this VI may vary with different operatingSeconds
           systems and CPU types.

           Waits the specified number of milliseconds and returns the value of the millisecondWait (ms)             timer. (Windows) The actual wait time may be up to 1 ms shorter than the requestedFunction
            wait time.

           Waits until the value of the millisecond timer becomes a multiple of the specifiedWait Until
           millisecond multiple. Use this function to synchronize activities. You can call thisNext ms            function in a loop to control the loop execution rate. However, it is possible that theMultiple
                first loop period might be short. Wiring a value of 0 to the milliseconds multiple inputFunction            forces the current thread to yield control of the CPU.

Stall Data
           Delays the data flow of the wire for a specified period of time.Flow

Get Date/   Converts a timestamp value or a numeric value to a date and time string in the time
Time      zone configured for the computer. The function interprets timestamp and numeric
String      values as the time-zone-independent number of seconds that have elapsed since 12:00
Function    a.m., Friday, January 1, 1904, Universal Time.

Get Date/
Time In    Returns a timestamp of the current time. LabVIEW calculates this timestamp using the
Seconds   number of seconds elapsed since 12:00 a.m., Friday, January 1, 1904, Universal Time.
Function

Date/Time
To
            Creates a timestamp from a set of individual values that specify a date and time.
Seconds
Function

Seconds    Converts a timestamp value or a numeric value to a cluster of time values. This
To Date/    function loses fractional seconds of precision when converting the timestamp. If you
Time       convert date time rec back into a time stamp, the timestamp may not display the


                                                    © National Instruments 1833

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1833 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1834 ordinal=1834 -->
## Functions

Functions


         Palette                    Description
        Object

         Function    exactly correct value.

        To Time
       Stamp     Converts a number to a timestamp.
         Function

       Time                       Inserts a time delay into the calling VI.        Delay

        Elapsed                      Indicates the amount of time that has elapsed since the specified start time.       Time


                    Waits the specified number of seconds with higher resolution than you can obtain with
                    the Wait (ms) function. For example, use this VI in applications that require waiting
                    with sub-millisecond resolution between steps. The resolution of the timer this VI uses        High
                      varies with different operating systems and CPU types.         Resolution
         Polling                    Unlike the Wait (ms) function, if the number of seconds you specify is 0, this VI does not
        Wait                      force the current thread to yield control of the CPU. Use this VI with caution if you are
                   concerned about high CPU loads: this VI may use polling to achieve high timing
                     resolution for all or a portion of the wait time.

        Format
        Date/Time  Displays a timestamp value or a numeric value as time in the format you specify using
         String      time format codes.
         Function

       Time
       Stamp     Use the time stamp constant to pass a time and date value to the block diagram.
        Constant

      TickTick CountCount (ms)(ms) FunctionFunction

       Returns the value of the millisecond timer.

      The base reference time (millisecond zero) is undefined. That is, you cannot convert
       millisecond timer value to a real-world time or date. Be careful when you use this
       function in comparisons because the value of the millisecond timer wraps from


1834   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1834 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1835 ordinal=1835 -->
## Functions

Functions

(2^32)–1 to 0.


Inputs/Outputs

   •      millisecond timer value —

    millisecond timer value returns the value of the millisecond timer.

HighHigh ResolutionResolution RelativeRelative SecondsSeconds

Returns the relative current time in seconds. Use the difference between two
successive values to measure the elapsed time between the calls. Use this VI to
measure time spans with much higher resolution than you can obtain from the Tick
Count (ms) function. The time resolution of this VI may vary with different operating
systems and CPU types.

      Note The operating system clock this VI uses is not tied to any absolute time
        reference and may drift over time when compared to absolute time sources.
       Avoid using this VI across long periods of time.


Inputs/Outputs

   •       relative seconds —

     relative seconds returns the value of the second timer in seconds.

WaitWait (ms)(ms) FunctionFunction

Waits the specified number of milliseconds and returns the value of the millisecond

                                                    © National Instruments 1835

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1835 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1836 ordinal=1836 -->
## Functions

Functions

        timer. (Windows) The actual wait time may be up to 1 ms shorter than the requested
       wait time.

       This function makes asynchronous system calls, but the nodes on the block diagram
       execute synchronously. Therefore, this function does not complete execution until the
       specified time has elapsed.


      Inputs/Outputs

               •      milliseconds to wait —

            milliseconds to wait specifies the number of milliseconds to wait. This function does not wait
            longer than 0x7ffffff or 2,147,483,647 ms or about 25 days. To wait for a longer period, execute
            the function multiple times or use the High Resolution Polling Wait function. Wiring a value of 0
             to this parameter forces the current thread to yield control of the CPU.

               •      millisecond timer value —

            millisecond timer value returns the value of the millisecond timer after the wait.


     When LabVIEW calls a VI for example, if millisecond timer value is 112 ms and
       milliseconds to wait is 10 ms, the VI finishes when millisecond timer value is greater
      than or equal to 122 ms.

      Use the Wait For Front Panel Activity function to eliminate the need for continually
       polling the front panel to determine if the value of a front panel object changes.

      Timer resolution is system dependent and might be less accurate than one
       millisecond, depending on your platform. Use the Wait Until Next ms Multiple function
       or the High Resolution Polling Wait VI to improve resolution.

           Note The Wait (ms) function behaves differently on Windows and the
            LabVIEW Real-Time Module. (Windows) The Wait (ms) function waits at least
              the value specified by the following formula: milliseconds to wait minus 1


1836   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1836 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1837 ordinal=1837 -->
## Functions

Functions


       ms. For example, if milliseconds to wait is 3 ms, the Wait (ms) function waits
        at least 2 ms. If milliseconds to wait is 1 ms, the Wait (ms) function may
        return without waiting at all. (Real-Time Module) The Wait (ms) function
        waits at least the value specified in the milliseconds to wait input.

WaitWait UntilUntil NextNext msms MultipleMultiple FunctionFunction

Waits until the value of the millisecond timer becomes a multiple of the specified
millisecond multiple. Use this function to synchronize activities. You can call this
function in a loop to control the loop execution rate. However, it is possible that the
first loop period might be short. Wiring a value of 0 to the milliseconds multiple input
forces the current thread to yield control of the CPU.

This function makes asynchronous system calls, but the nodes themselves function
synchronously. Therefore, it does not complete execution until the specified time has
elapsed.


Inputs/Outputs

   •      millisecond multiple —

    millisecond multiple is the input that specifies how many milliseconds lapse when the VI runs.
    Wiring a value of 0 to this parameter forces the current thread to yield control of the CPU.

   •      millisecond timer value —

    millisecond timer value returns the value of the millisecond timer after the wait.


When LabVIEW calls a VI for example, if millisecond multiple is 10 ms and millisecond
timer value is 112 ms, the VI waits 8 more milliseconds until the millisecond timer
value is 120 ms, a multiple of 10.


                                                    © National Instruments 1837

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1837 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1838 ordinal=1838 -->
## Functions

Functions

       StallStall DataData FlowFlow

       Delays the data flow of the wire for a specified period of time.


      Inputs/Outputs

               •      milliseconds to wait —

            milliseconds to wait specifies the number of milliseconds that this VI waits to continue the data
              flow.

               •      value in —

            value in specifies the input value before the delay occurs. This input accepts any data type.

               •      millisecond timer value —

            millisecond timer value returns the LabVIEW system time when the delay finishes.

               •      value out —

            value out returns the value in value in.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Malleable VIs\Basics\Malleable VIs
        Basics.lvproj

     GetGet Date/TimeDate/Time StringString FunctionFunction

       Converts a timestamp value or a numeric value to a date and time string in the time
      zone configured for the computer. The function interprets timestamp and numeric
       values as the time-zone-independent number of seconds that have elapsed since


1838   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1838 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1839 ordinal=1839 -->
## Functions

Functions

12:00 a.m., Friday, January 1, 1904, Universal Time.


Inputs/Outputs

   •      date format (0) —

    date format selects the appearance of the date string.

    Date formats vary with your system configuration. To use a different date format, use the Format
    Date/Time String function.

    0  short—1/21/94
    1   long—Friday, January 21, 1994
    2   abbreviated—Fri, Jan 21, 1994

   •      time stamp —

    time stamp can be a timestamp or a numeric. If numeric, this number is the time-zone-
    independent number of seconds that have elapsed since 12:00 a.m., Friday, January 1, 1904,
    Universal Time [01-01-1904 00:00:00]. The default is the current date and time.

       If year is before 1904, time stamp is negative.

   •     want seconds? (F) —

    want seconds? controls the display of seconds in the time string.

   •      date string —

    date string is the string returned by the function according to the specified date format.

   •      time string —

    time string returns the string formatted according to the configured time zone for your
    computer. want seconds? controls whether the string includes seconds.


                                                    © National Instruments 1839

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1839 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1840 ordinal=1840 -->
## Functions

Functions

     GetGet Date/TimeDate/Time InIn SecondsSeconds FunctionFunction

       Returns a timestamp of the current time. LabVIEW calculates this timestamp using the
      number of seconds elapsed since 12:00 a.m., Friday, January 1, 1904, Universal Time.

      Use the To Double Precision Float function to convert the timestamp value to a lower
       precision, floating-point number.


      Inputs/Outputs

               •      current time —

            current time returns a timestamp of the LabVIEW system time. LabVIEW calculates this
           timestamp using the number of seconds elapsed since 12:00 a.m., Friday, January 1, 1904,
             Universal Time [01-01-1904 00:00:00].


      Timer resolution is system dependent and might be less accurate than one
       millisecond, depending on your platform. When you perform timing, use the Tick
      Count (ms) function to improve resolution.

     Date/TimeDate/Time ToTo SecondsSeconds FunctionFunction

       Creates a timestamp from a set of individual values that specify a date and time.

      Use the To Double Precision Float function to convert the timestamp value to a lower
       precision, floating-point number. The number is measured as the number of seconds
       that have elapsed since 12:00 a.m., Friday, January 1, 1904, Universal Time, assuming
     DST is set to 1.


1840   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1840 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1841 ordinal=1841 -->
## Functions

Functions

Inputs/Outputs

   •      date time rec —

    date time rec is the date and time to convert. If is UTC is TRUE, date time rec is in Universal
    Time. If is UTC is FALSE, date time rec is in the configured time zone for the computer.

         •       fractional second —

         fractional second must be greater than or equal to 0 and less than 1.

         •      second —

        second can be from 0 to 59.

         •      minute —

       minute can be from 0 to 59.

         •      hour —

       hour can be from 0 to 23.

         •     day of month —

       day of month can be from 1 to 31.

         •     month —

       month can be from 1 to 12.

         •      year —

        year can be from 1600 to 3000.

         •     day of week —

       day of week can be from 1 to 7, which correspond to Sunday and Saturday, respectively.

             Note This function ignores day of week when building the timestamp.

         •     day of year —


                                                    © National Instruments 1841

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1841 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1842 ordinal=1842 -->
## Functions

Functions


              day of year can be from 1 to 366.

                   Note This function ignores day of year when building the timestamp.

                     •     DST —

             DST indicates whether the time is standard (0) or daylight savings time (1). You also can set
             DST to -1 to have the VI determine the correct time automatically each time you run the VI.
                           If is UTC is TRUE, the function ignores the DST setting and uses Universal Time.


               •        is UTC (F) —

                is UTC specifies if date time rec is in Universal Time or in the configured time zone for the
            computer. If TRUE, date time rec is in Universal Time. The default is FALSE.

               •      time stamp —

           time stamp is the time that represents the date and time specified by the individual values in
           date time rec.

                    If year and month are out of range, the results are unpredictable.

     SecondsSeconds ToTo Date/TimeDate/Time FunctionFunction

       Converts a timestamp value or a numeric value to a cluster of time values. This
       function loses fractional seconds of precision when converting the timestamp. If you
       convert date time rec back into a time stamp, the timestamp may not display the
       exactly correct value.


      Inputs/Outputs

               •      time stamp —


1842   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1842 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1843 ordinal=1843 -->
## Functions

Functions


  time stamp can be a timestamp or a numeric. If numeric, this number is the time-zone-
  independent number of seconds that have elapsed since 12:00 a.m., Friday, January 1, 1904,
  Universal Time [01-01-1904 00:00:00]. The default is the current date and time.

   If year is before 1904, time stamp is negative.
•      to UTC (F) —

  to UTC specifies if date time rec is in Universal Time or in the configured time zone for the
  computer. If TRUE, date time rec is in Universal Time.

  The default is FALSE.
•      date time rec —

  date time rec returns the date and time. If to UTC is TRUE, date time rec is in Universal Time. If
  to UTC is FALSE, date time rec is in the configured time zone for the computer.

      •       fractional second —

       fractional second is the fractions of a second since the start of the second. Values must be
       greater than or equal to 0 and less than 1.

      •      second —

      second is the number of complete seconds since the start of the minute. Values can be 0 to
       59.

      •      minute —

      minute is the number of complete minutes since the start of the hour. Values can be 0 to 59.

      •      hour —

      hour is the number of complete hours since midnight. Values can be 0 to 23.

      •     day of month —

     day of month can be 1 to 31.

      •     month —

     month can be 1 to 12.

      •      year —


                                                   © National Instruments 1843

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1843 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1844 ordinal=1844 -->
## Functions

Functions


                year can be from 1600 to 3000.

                     •     day of week —

              day of week can be 1 to 7, which correspond to Sunday and Saturday, respectively.

                     •     day of year —

              day of year can be 1 to 366.

                     •     DST —

                     is DST returns a value for standard (0) or daylight saving time (1). If to UTC is TRUE, is DST is
                standard (0).


     ToTo TimeTime StampStamp FunctionFunction

       Converts a number to a timestamp.


      Inputs/Outputs

               •     number —

          number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
           so on, that represents the amount of seconds from the epoch time of 12 a.m., January 1, 1904
            [01-01-1904 00:00:00].

               •      time stamp —

           time stamp is a time-zone-independent number of seconds that have elapsed since 12:00 a.m.,
              Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00].


1844   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1844 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1845 ordinal=1845 -->
## Functions

Functions

TimeTime DelayDelay

Inserts a time delay into the calling VI.


Dialog Box Options

 Option              Description

 Time delay           Specifies how many seconds to delay running the calling VI. The default is
 (seconds)             1.000.


Inputs/Outputs

   •      Delay Time (s) —

     Specifies how many seconds to wait. The value you wire to this input overrides the value you set
     in the configuration dialog box.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •       error out —

    Contains error information. This output provides standard error out functionality.


Components

Specifies how many seconds to delay running the calling VI. The default is 1.000.

TickTick CountCount

Returns the value of a free running counter in the units specified. The output and
internal counter are both of the configured width.

                                                    © National Instruments 1845

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1845 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1846 ordinal=1846 -->
## Functions

Functions

           If you do not have the FPGA, Real-Time, or DSP modules, you can use the Tick Count
       (ms) function instead.


      Dialog Box Options

        Option   Description

                  Unit of time the VI uses for the counter.

                    Note (Windows) The Windows operating system supports only millisecond
                             resolution. If you select a µSec or Tick resolution under Windows, the VI does
                          not provide exact timing and instead provides an approximation that averages
                            to the requested time over the course of the timing interval. Windows does not        Counter
                         support resolutions under one millisecond and rounds them up to one         Units
                            millisecond.

                              • Ticks—Sets the counter units to a single clock cycle, the length of which is
                    determined by the clock rate for which the VI is compiled.
                              • µSec—Sets the counter units to microseconds.
                              • mSec—Sets the counter units to milliseconds.


         Size of                   Specifies the maximum time a timer can track. To save space on the FPGA, use the         Internal                  smallest Size of Internal Counter possible for the FPGA VI.
        Counter

      Inputs/Outputs

               •      Tick Count(Ticks) —

            Returns the value of a free running counter at the time the VI wakes up. A free running counter
               rolls over when the counter reaches the maximum of Size of Internal Counter specified in the
             configuration dialog box.


1846   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1846 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1847 ordinal=1847 -->
## Functions

Functions

Components

Specifies the maximum time a timer can track. To save space on the FPGA, use the
smallest Size of Internal Counter possible for the FPGA VI.

Unit of time the VI uses for the counter.

WaitWait

Delays for a certain time interval before the output data dependence becomes valid.

(Real-Time Module) The Wait Express VI waits the specified count time and then
returns the value of a free running counter. When the Wait Express VI executes, it sleeps
and blocks the execution of other code running in the same thread.


Dialog Box Options

 Option   Description

          Unit of time the VI uses for the counter.

              Note (Windows) The Windows operating system supports only millisecond
                     resolution. If you select a µSec or Tick resolution under Windows, the VI does
                  not provide exact timing and instead provides an approximation that averages
                   to the requested time over the course of the timing interval. Windows does not Counter
                  support resolutions under one millisecond and rounds them up to one Units
                    millisecond.

                  • Ticks—Sets the counter units to a single clock cycle, the length of which is
             determined by the clock rate for which the VI is compiled.
                  • µSec—Sets the counter units to microseconds.
                  • mSec—Sets the counter units to milliseconds.


                                                    © National Instruments 1847

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1847 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1848 ordinal=1848 -->
## Functions

Functions


        Option   Description

         Size of                   Specifies the maximum time a timer can track. To save space on the FPGA, use the
         Internal                  smallest Size of Internal Counter possible for the FPGA VI.        Counter

      Inputs/Outputs

               •      Count(Ticks) —

          The time spent in the component.

               •      Tick Count(Ticks) —

            Returns the value of a free running counter at the time the VI wakes up. A free running counter
               rolls over when the counter reaches the maximum of Size of Internal Counter specified in the
             configuration dialog box.


           If you do not have the FPGA, Real-Time, or DSP modules, you can use the Wait (ms)
       function instead.

           Note (Real-Time Module, Windows) When the Wait Express VI runs inside a
             timed structure or a VI set to time-critical priority, it blocks the execution of
                   all other code in the same timed structure or VI because timed structures and
                 time-critical VIs are single-threaded. In all other cases, the Wait Express VI
               sleeps while other code in the calling VI runs in parallel on separate threads.

     Components

       Specifies the maximum time a timer can track. To save space on the FPGA, use the
       smallest Size of Internal Counter possible for the FPGA VI.

       Unit of time the VI uses for the counter.

     ElapsedElapsed TimeTime

       Indicates the amount of time that has elapsed since the specified start time.


1848   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1848 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1849 ordinal=1849 -->
## Functions

Functions


Dialog Box Options

 Option                  Description

                           Specifies how much time must elapse before the Time has Elapsed
 Elapsed time (seconds)                       Boolean is set to TRUE. The default is 1.000.


 Automatically reset                         Resets the elapsed time marker. after time target

Inputs/Outputs

   •      Reset —

    Controls the initialization of the internal state of the VI. The default is FALSE.

   •     Time Target (s) —

     Specifies how much time must elapse before the Time has Elapsed Boolean is set to TRUE. The
     default is 1.

   •      Auto Reset —

    Resets the start time to the value in Present (s) when the Express VI reaches the Time Target (s).

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Set Start Time (s) —


                                                    © National Instruments 1849

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1849 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1850 ordinal=1850 -->
## Functions

Functions


           Uses the current time or a time offset from 12:00 a.m., Friday, January 1, 1904 [01-01-1904
             00:00:00] as the start time instead of the time this VI first ran.

                    If the value is 0, the Express VI uses the current time as the start time. The Express VI uses any
            other value as the number of seconds offset from 12:00 a.m., Friday, January 1, 1904 [01-01-1904
              00:00:00]. For example if the value is 1, the Express VI measures the elapsed time since 12:00:01
             a.m., Friday, January 1, 1904 [01-01-1904 00:00:01]. You can wire this input to the Present (s)
           output of another Elapsed Time Express VI to get this value.

               •      Present (s) —

             Displays the present time in seconds since 12:00 a.m., Friday, January 1, 1904, Universal Time
            [01-01-1904 00:00:00].

               •       Start Time Text —

                    If Automatically reset after time target is FALSE, displays (in text format) the date and time the
              VI first ran or the time you wire to the Set Start Time (s) input. Otherwise displays the date and
           time of the last reset.

               •      Present Text —

             Displays the present date and time in text format.

               •     Time has Elapsed —

             Indicates if the Elapsed Time (s) is greater than the start time plus Time Target (s).

               •      Get Start Time (s) —

                    If Automatically reset after time target is FALSE, displays the date and time the VI first ran or the
           time you wire to the Set Start Time (s) input. Otherwise displays the date and time of the last
              reset.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Elapsed Time (s) —

             Displays the amount of time in seconds that has elapsed since the start time and the Present (s)
             time.

               •      Elapsed Time Text —


1850   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1850 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1851 ordinal=1851 -->
## Functions

Functions


    Displays the amount of time in seconds that has elapsed since the start time.


Components

Specifies how much time must elapse before the Time has Elapsed Boolean is set to
TRUE. The default is 1.000.

Resets the elapsed time marker.

HighHigh ResolutionResolution PollingPolling WaitWait

Waits the specified number of seconds with higher resolution than you can obtain with
the Wait (ms) function. For example, use this VI in applications that require waiting
with sub-millisecond resolution between steps. The resolution of the timer this VI uses
varies with different operating systems and CPU types.

Unlike the Wait (ms) function, if the number of seconds you specify is 0, this VI does
not force the current thread to yield control of the CPU. Use this VI with caution if you
are concerned about high CPU loads: this VI may use polling to achieve high timing
resolution for all or a portion of the wait time.


Inputs/Outputs

   •      seconds to wait —

    seconds to wait specifies the number of seconds to wait.

       If seconds to wait is equal to or less than 0, the VI does not wait at all. If seconds to wait is 0, this
     VI also does not force the current thread to yield control of the CPU.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 1851

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1851 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1852 ordinal=1852 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     FormatFormat Date/TimeDate/Time StringString FunctionFunction

       Displays a timestamp value or a numeric value as time in the format you specify using
      time format codes.


      Inputs/Outputs

               •      time format string (%c) —

           time format string specifies the format of the output string.

          Time format codes (beginning with %) not recognized by the function as a format code return the
             character literally. The default code is %c, which corresponds to the date/time representation
            appropriate for the configured time zone for the computer. If time format string is an empty
               string, the function uses the default.
               •      time stamp —

           time stamp can be a timestamp or a numeric. If numeric, this number is the time-zone-
           independent number of seconds that have elapsed since 12:00 a.m., Friday, January 1, 1904,
             Universal Time [01-01-1904 00:00:00]. The default is the current date and time.

                    If year is before 1904, time stamp is negative.
               •     UTC format —

         UTC format specifies if the output string is in Universal Time or in the configured time zone for
            the computer. If TRUE, date/time string is in Universal Time.

          The default is FALSE.
               •      date/time string —

            date/time string is the formatted date/time string.


1852   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1852 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1853 ordinal=1853 -->
## Functions

Functions

This function calculates date/time string by copying time format string and replacing
each of the time format codes with the corresponding values. For example, the time
format string %y%m%d displays timestamp in the format yymmdd. The time format
string %y%m%d displays the date January 30, 2014 as 140130.

The following list describes some of the caveats to consider when you use this
function:

  • LabVIEW returns abbreviated weekday and month names as numeric values for
   systems that do not support abbreviated names, such as Chinese and Korean.
  • The %c, %u, %x, %X, %z, and %Z format codes depend on operating system locale
    support. The output of these codes is platform dependent. Interpretation of the
    Daylight Saving Time rule also can vary by platform.
  • The %p format code only takes effect at locales that use the 12-hour time system.
  • Time format codes have leading zeros as necessary to ensure a constant field
    width. An optional # modifier before the format code letter removes the leading
    zeros from the following format codes: %#d, %#H, %#I, %#j, %#m, %#M,
   %#s, %#S, %#U, %#w, %#W, %#X, %#y, %#Y. The # modifier does not
   modify the behavior of any other format codes.

Related Information

Time Format Codes

TimeTime StampStamp ConstantConstant

Use the time stamp constant to pass a time and date value to the block diagram.

The default value is zero seconds since 12:00 a.m., Friday, January 1, 1904, Universal
Time [01-01-1904 00:00:00]. To change the time and date, right-click the constant and
select Data Operations»Set Time and Date from the shortcut menu to display the Set
Time and Date dialog box. You also can right-click the constant and select Data
Operations»Set Time to Now from the shortcut menu to set the time and date value to
the current time and date.

      Note If you convert a time stamp to a variant, the variant indicator displays
       the current value of the time stamp that you wired to it.

                                                    © National Instruments 1853

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1853 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1854 ordinal=1854 -->
## Functions

Functions


     DialogDialog && UserUser InterfaceInterface

      Use the Dialog & User Interface VIs and functions to create dialog boxes to prompt
       users with instructions.


         Palette                   Description        Object

       One
        Button                   Displays a dialog box that contains a message and a single button.         Dialog
         Function

       Two
        Button                   Displays a dialog box that contains a message and two buttons.         Dialog
         Function

        Three
        Button    Displays a dialog box that contains a message and three buttons.
         Dialog

        Simple                    Indicates whether an error occurred. If an error occurred, this VI returns a description of         Error
                  the error and optionally displays a dialog box.
        Handler

        General
                    Indicates whether an error occurred. If an error occurred, this VI returns a description of
         Error
                  the error and optionally displays a dialog box.
        Handler


                   Resets the error status to no error, code to 0, and source to an empty string. Use this VI
         Clear
               when you want to ignore an error. By default, this VI ignores all errors. Wire an error code
         Errors
                   value to specific error code to clear if you only want to ignore a specific error.


1854   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1854 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1855 ordinal=1855 -->
## Functions

Functions


Palette          Description
Object

Error     Use the Error Ring to quickly select and pass NI or custom error codes throughout your
Ring        VI.

Merge         Merges error I/O clusters from different VIs and functions.Errors

Error     Converts an error or warning code to an error cluster. This VI is useful when you receive a
Cluster    return value from a shared library call or when you return user-defined error codes.
From
Error     Passing error code 0 means that no error occurred and the VI does not modify the error
Code      cluster.


Find           Tests the error status of one or more low-level functions or subVIs that produce aFirst
         numeric error code as output.Error


Error     Use the error cluster constant to pass an error cluster value to the block diagram. Set this
Cluster   value by clicking inside the constant with the Operating tool and specifying values for
Constant  the status, code, and source elements.


Multiple  Use the Multiple Errors VIs to convert an error cluster into different formats or to
Errors    manipulate the attributes of an error cluster.


Prompt
          Displays a standard dialog box that prompts users to enter information, such as a user
User for
        name and password.
Input

Display
Message  Displays a standard dialog box that contains an alert or a message for users.
to User

Write to
System   Writes a message to the nierrlog system log for storage and subsequent viewing.
Log

Wait For  Pauses the execution of the calling VI block diagram in run mode until the function


                                                    © National Instruments 1855

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1855 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1856 ordinal=1856 -->
## Functions

Functions


         Palette                   Description
        Object

         Front
        Panel                   detects front panel activity in the front panel you want to monitor.          Activity
         Function

        Generate
         Front     Programmatically generates front panel activity so any VI execution halted by the Wait
        Panel    on Front Panel Activity function continues executing. No actual changes occur on the
          Activity   front panel.
         Function

         Color
        Box      Use the color box constant to supply a constant color value to the block diagram.
        Constant

         Listbox
       Symbol                Use the listbox symbol ring constant to assign symbols to items in a listbox control.
        Ring
        Constant

        Events   Use the Events functions to register events dynamically and to create user events.


                Use the Menu functions to modify the menus in LabVIEW applications. Use the functions       Menu
                   located on the top row of the palette to handle menu selections.


                Use the Cursor VIs to change the appearance of the cursor on the front panel of a VI. For
                  example, if the VI is acquiring or analyzing data and can accept no user input, you might
         Cursor   want to change the cursor to an hourglass or watch cursor. After the VI finishes acquiring
                   or analyzing data and can accept user input, you can change the cursor back to the
                    default cursor.


        Help     Use the Help VI and functions to link from VIs to HTML files or compiled help files.


1856   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1856 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1857 ordinal=1857 -->
## Functions

Functions

OneOne ButtonButton DialogDialog FunctionFunction

Displays a dialog box that contains a message and a single button.


Inputs/Outputs

   •     message —

    message is the text to display in the dialog box. The dialog box expands when you add more
     text. This function automatically wraps the text based on the size of the dialog box. The dialog
    box can display as much text as your computer screen can display. If you want a scrollbar to
   show when the size of the dialog box exceeds your desired size, use the Three Button Dialog VI.
    With this VI, you can convert a three button dialog box to a one or two button dialog box by
    wiring an empty string to a button text input to hide that button.

   •      button name ("OK") —

    button name is the name displayed in the dialog box button. The default is OK.

   •      true —

    true returns a value of TRUE when this dialog box closes, regardless of whether you close the
    dialog by using the dialog box button or by using the close window button. You may use this
    output to provide execution ordering control for downstream functions.

TwoTwo ButtonButton DialogDialog FunctionFunction

Displays a dialog box that contains a message and two buttons.


Inputs/Outputs

   •     message —


                                                    © National Instruments 1857

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1857 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1858 ordinal=1858 -->
## Functions

Functions


          message is the text to display in the dialog box. The dialog box expands when you add more
               text. This function automatically wraps the text based on the size of the dialog box. The dialog
           box can display as much text as your computer screen can display. If you want a scrollbar to
          show when the size of the dialog box exceeds your desired size, use the Three Button Dialog VI.
           With this VI, you can convert a three button dialog box to a one or two button dialog box by
             wiring an empty string to a button text input to hide that button.

               •     T button name ("OK") —

          T button name is the name displayed on one of the dialog box buttons. The default is OK.

               •      F button name ("Cancel") —

           F button name is the name displayed on one of the dialog box buttons. The default is Cancel.

               •     T button? —

          T button? returns a value of TRUE if you click the dialog box button named T button name. If
           you click the dialog box button named F button name or click the close window button, T
           button? returns a value of FALSE.

     ThreeThree ButtonButton DialogDialog

       Displays a dialog box that contains a message and three buttons.


      Inputs/Outputs

               •       Justify Message (Left) —

             Justify Message sets the justification of the text that is displayed.


1858   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1858 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1859 ordinal=1859 -->
## Functions

Functions


  0  Left—Justifies the text to the left.
  1  Center—Centers the text.
  2  Right—Justifies the text to the right.

•     Window Title ("") —

  Window Title is the text to display in the title bar of the dialog box.

•     message —

  message is the text to display in the dialog box. The dialog box has a maximum size based on
  your computer screen resolution and system font size. If the text exceeds the maximum size of
  the dialog box, a vertical scrollbar appears on the right side. Scroll to display the text beyond the
  maximum size.

•       Left Button Text ("Yes") —

  Left Button Text is the text to display on the left button. The default is Yes.

•      Center Button Text ("No") —

  Center Button Text is the text to display on the center button. The default is No.

•      Right Button Text ("Cancel") —

  Right Button Text is the text to display on the right button. The default is Cancel.

•      Keyboard Shortcuts (Left is <Enter>) —

  Keyboard Shortcuts specifies keyboard shortcuts for each button in the dialog box.

  For example, you can specify a shortcut of <F1> for a Help button in the dialog box. The default is
  a shortcut of <Enter> for the left button and no shortcuts for the center and right buttons.

      •       Left Button Key Shortcut —

       Left Button Key Shortcut specifies a keyboard shortcut for the left button.

             •      Control —


                                                   © National Instruments 1859

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1859 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1860 ordinal=1860 -->
## Functions

Functions


                                 If Control is TRUE, the keyboard shortcut includes the <Ctrl> key.

                           •       Shift —

                                 If Shift is TRUE, the keyboard shortcut includes the <Shift> key.

                           •     Key —

                  Key is the name of the shortcut key.

                  Key must match a key name on the Key Navigation page of the Properties dialog box.


                     •      Center Button Key Shortcut —

               Center Button Key Shortcut specifies a keyboard shortcut for the center button.

                           •      Control —

                                 If Control is TRUE, the keyboard shortcut includes the <Ctrl> key.

                           •       Shift —

                                 If Shift is TRUE, the keyboard shortcut includes the <Shift> key.

                           •     Key —

                  Key is the name of the shortcut key.

                  Key must match a key name on the Key Navigation page of the Properties dialog box.


                     •      Right Button Key Shortcut —

                Right Button Key Shortcut specifies a keyboard shortcut for the right button.

                           •      Control —

                                 If Control is TRUE, the keyboard shortcut includes the <Ctrl> key.


1860   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1860 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1861 ordinal=1861 -->
## Functions

Functions


                •       Shift —

                     If Shift is TRUE, the keyboard shortcut includes the <Shift> key.

                •     Key —

           Key is the name of the shortcut key.

           Key must match a key name on the Key Navigation page of the Properties dialog box.


   •      Allow user to close window? (TRUE) —

       If Allow user to close window? is TRUE (default), the operating system window close button
    appears in the dialog box, and the user can close the dialog box without clicking the left, center,
    or right buttons.

     In most operating systems, the window close button appears in the upper right corner of the
    window.

   •     Which Button? —

    Which Button? indicates which button the user clicked.

    0 Left Button
    1 Center Button
    2 Right Button
    Window Close—The user closed the dialog box without clicking the left, center, or right    3
      buttons.


If you wire an empty string to a button text input, this VI hides that button. This allows
you to convert a three button dialog box to a one or two button dialog box. For
example, you could use this functionality to hide a Help button when no help is
available. If you wire an empty string to all three button text inputs, this VI displays a
dialog box with a single default OK button.


                                                    © National Instruments 1861

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1861 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1862 ordinal=1862 -->
## Functions

Functions

     SimpleSimple ErrorError HandlerHandler

       Indicates whether an error occurred. If an error occurred, this VI returns a description
       of the error and optionally displays a dialog box.

       This VI calls the General Error Handler VI and has the same basic functionality as
       General Error Handler but with fewer options.


      Inputs/Outputs

               •       error code (no error:0) —

             error code is a numeric error code.

                    If error in indicates an error, the VI ignores error code. If not, the VI tests it. A nonzero value
              signifies an error.

               •       error source (" ") —

             error source is an optional string you can use to describe the source of error code.

               •      type of dialog (OK msg:1) —

           type of dialog determines what type of dialog box to display, if any.

            Regardless of its value, the VI outputs the error information and message describing the error.

           no dialog—Displays no dialog box. This is useful if you want to have programmatic control over
           0
             handling errors.
          OK message (default)—Displays a dialog box with a single Continue button. After the user
           1
            acknowledges the dialog box, the VI returns control to the main VI.
             continue or stop message—Displays a dialog box with buttons, which the user can use to
           2
               either continue or stop. If the user selects Stop, the VI calls the Stop function to halt execution.
          OK message + warnings—Displays a dialog box with any warnings and a single Continue
           3
              button. After the user acknowledges the dialog box, the VI returns control to the main VI.


1862   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1862 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1863 ordinal=1863 -->
## Functions

Functions


     continue/stop + warnings—Displays a dialog box with any warnings and buttons, which the
    4 user can use to either continue or stop. If the user selects Stop, the VI calls the Stop function to
      halt execution.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs.

    This input contains status, code, and source, which provide standard error in cluster element
     functionality.

   •       error? —

    error? returns TRUE if an error occurs. If this VI finds an error, it sets the parameters in the error
     cluster.

   •      code out —

    code out is the error code indicated by error in or error code.

   •      source out —

    source out indicates the source of the error.

    The source out string is a more descriptive string than the source string in the error in input.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •     message —

    message describes the error code that occurred, the source of the error, and a description of the
     error.

       If the VI does not return a description of the error, you can take several actions to find the error
    code description. If more than one description exists for the same error code, the VI displays all
    the descriptions, separated by or.

GeneralGeneral ErrorError HandlerHandler

Indicates whether an error occurred. If an error occurred, this VI returns a description

                                                    © National Instruments 1863

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1863 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1864 ordinal=1864 -->
## Functions

Functions

       of the error and optionally displays a dialog box.


      Inputs/Outputs

               •      [user-defined descriptions] —

            [user-defined descriptions] is an array of descriptions of user-defined codes.

                    If an incoming error matches one in user-defined codes, the VI returns the corresponding
             description from user-defined descriptions in message.

               •      [user-defined codes] —

            [user-defined codes] is an array of numeric error codes you can use to define error codes and
           messages for your own VIs.

          The VI searches this array after searching an internal database of error codes. Error codes -8999
           through -8000, 5000 through 9999, and 500,000 through 599,999 are reserved for you to define
            your own error messages.

               •       [error code] (0) —

             [error code] is a numeric error code.

                    If error in indicates an error, the VI ignores error code. If not, the VI tests it. A nonzero value
              signifies an error.

               •       [error source] (" ") —

             [error source] is an optional string you can use to describe the source of error code.

               •      search ni.com link visible?(T) —


1864   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1864 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1865 ordinal=1865 -->
## Functions

Functions


  search ni.com link visible? determines whether the Search ni.com for error hyperlink
  appears in the dialog box. Set to TRUE to display the hyperlink. Clicking the hyperlink opens
  search results for the error code on ni.com in the default web browser. The hyperlink appears
  only for LabVIEW-defined error codes in the development environment. The default is TRUE.

•      type of dialog (OK msg:1) —

  type of dialog determines what type of dialog box to display, if any.

  Regardless of its value, the VI outputs the error information and message describing the error.

   no dialog—Displays no dialog box. This is useful if you want to have programmatic control over
  0   handling errors.
  OK message (default)—Displays a dialog box with a single Continue button. After the user  1   acknowledges the dialog box, the VI returns control to the main VI.
   continue or stop message—Displays a dialog box with buttons, which the user can use to  2    either continue or stop. If the user selects Stop, the VI calls the Stop function to halt execution.
  OK message + warnings—Displays a dialog box with any warnings and a single Continue  3    button. After the user acknowledges the dialog box, the VI returns control to the main VI.
   continue/stop + warnings—Displays a dialog box with any warnings and buttons, which the
  4 user can use to either continue or stop. If the user selects Stop, the VI calls the Stop function to
    halt execution.

•       error in (no error) —

  error in describes error conditions that occur before this node runs.

  This input contains status, code, and source, which provide standard error in cluster element
  functionality.

•      [exception action] (none:0) —

  [exception action] is a way for you to create exceptions to error handling.

  The VI performs the exception action if the error code and error source match the exception
  code and exception source. If you use the default value for an exception source, only the
  exception code must match for the VI to perform the exception action.

   No exception (default)—Performs no error exception handling, even if you wire an exception
  0
   code or an exception source.
  1 Cancel error on match—Treats what is normally an error as no error. If the VI cancels an error,


                                                   © National Instruments 1865

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1865 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1866 ordinal=1866 -->
## Functions

Functions


              error? is FALSE, code out is 0, and source out is an empty string.
             Set error on match—Upgrades a warning to an error. This parameter sets an error if the VI
              detects no error, as described in the status and error code parameters, but the code value of
           2 error in matches exception code and the error source value matches exception source. If the VI
               sets an error, error? is TRUE, code out is the code value from error in, and source out is the
             source value from error in.

               •      [exception code] —

            [exception code] is the error code that you want to treat as an exception. The default is 0.

               •      [exception source] —

            [exception source] is the error message that you want to use to test for an exception. The default
                is an empty string.

               •       error? —

             error? returns TRUE if an error occurs. If this VI finds an error, it sets the parameters in the error
               cluster.

               •      code out —

           code out is the error code indicated by error in or error code.

               •      source out —

            source out indicates the source of the error.

          The source out string is a more descriptive string than the source string in the error in input.

               •     message —

          message describes the error code that occurred, the source of the error, and a description of the
               error.

                    If the VI does not return a description of the error, you can take several actions to find the error
           code description. If more than one description exists for the same error code, the VI displays all
            the descriptions, separated by or.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1866   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1866 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1867 ordinal=1867 -->
## Functions

Functions

ClearClear ErrorsErrors

Resets the error status to no error, code to 0, and source to an empty string. Use this VI
when you want to ignore an error. By default, this VI ignores all errors. Wire an error
code value to specific error code to clear if you only want to ignore a specific error.


Inputs/Outputs

   •       specific error code to clear (0: all) —

     specific error code to clear ignores only the specific error code wired to this input. The default
    value is 0, which means the VI will ignore all errors.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

    The default is no error. If you do not wire a value to specific error code to clear, this node
    does not pass the error in input to the error out output.

   •       specific error cleared? —

     specific error cleared? indicates whether the error referenced by specific error code to clear has
    been cleared.

   •       error out —

    error out contains error information. This output provides standard error out functionality. error
    out returns no error by default. If you wire a value to specific error code to clear and error in
    contains errors that do not match the error code you wired, error out will return an error.

ErrorError RingRing

Use the Error Ring to quickly select and pass NI or custom error codes throughout your
VI.


                                                    © National Instruments 1867

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1867 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1868 ordinal=1868 -->
## Functions

Functions

      You can configure the ring to return a built-in error message or you can create a
      custom error message for a one-time use. By default, the source string of the error
        cluster contains the call chain from the top-level VI to the current VI.

           Note To reduce unnecessary execution time in your VIs, place Error Rings
               inside a case structure that executes only when the error condition the Error
              Ring reports is met.

       (Real-Time Module) Exclude the call chain to reduce jitter in real-time applications. You
      cannot use the Error Ring in VIs that run on RT targets.


      Inputs/Outputs

               •       error out —


      The following is a configured Error Ring.


      The configured Error Ring has the following parts.


        Section    Description

                    Toggles between error and warning.

                     Indicates if the error includes the call chain.

                     Description of the error. Right-click the Error Ring and select Visible Items»Error
                   Explanation Text from the shortcut menu to show or hide the error description.

        6:LabVIEW        Note You can include format specifiers, such as %s and %T, in the
                               description. Refer to Defining a Custom Error Code from the Error Ring for
                       more details.


1868   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1868 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1869 ordinal=1869 -->
## Functions

Functions


 Section    Description

           Launches the Select Error dialog box.

After you select the error, you can change the type (Error or Warning) and whether to
include the call chain by clicking the icons on the ring. You also can toggle the error
type and call chain options by right-clicking the Error Ring and selecting Generate
Error, Generate Warning, Include Call Chain, or Exclude Call Chain from the shortcut
menu.

MergeMerge ErrorsErrors

Merges error I/O clusters from different VIs and functions.

By default, this function looks for errors beginning with the error in 0 parameter and
reports the first error found. If the function finds no errors, it looks for warnings and
returns the first warning found. If the function finds no warnings, it returns no error.
Use exception control to treat what is normally an error as no error or to treat a
warning as an error.

To configure the function to return an error cluster that combines all the specified
errors/warnings, right-click the function and select Retain All Errors.


Inputs/Outputs

   •       error in —

    error in 0 describes the first error condition to check for errors.

   •       error in —

    error in 1 describes the second error condition to check for errors.

   •       error out —


                                                    © National Instruments 1869

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1869 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1870 ordinal=1870 -->
## Functions

Functions


             error out returns the first error/warning in the specified inputs or an error cluster that combines
                all the specified errors/warnings.


     When you place this function on the block diagram, it has two inputs available. You
      can add additional inputs to the node by right-clicking an input and selecting Add
       Input from the shortcut menu or by resizing the node. To remove inputs, right-click an
       input and select Remove Input from the shortcut menu or use resizing handles to
        resize the node.

      ErrorError ClusterCluster FromFrom ErrorError CodeCode

       Converts an error or warning code to an error cluster. This VI is useful when you receive
      a return value from a shared library call or when you return user-defined error codes.

       Passing error code 0 means that no error occurred and the VI does not modify the
       error cluster.


      Inputs/Outputs

               •        is warning? (False) —

                    If is warning? is TRUE, status returns FALSE to indicate that a warning occurred. The default is
            FALSE.

               •     show call chain? (False) —

                    If show call chain? is TRUE, source includes the chain of callers from the VI that produced the
             error or warning to the top-level VI. The default is FALSE, which indicates to include only the
              calling VI.

             This VI uses the Call Chain function to obtain the chain of callers.

               •       error code (0) —


1870   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1870 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1871 ordinal=1871 -->
## Functions

Functions


    error code is the code you want to convert to an error cluster. The default is 0, which indicates
    that no error occurred.

   •       error message ("") —

    error message is the error description to appear in the error out cluster.

    LabVIEW displays the description in error message when the General Error Handler VI receives
     this error out cluster. If error message is empty, LabVIEW uses error code to determine the error
    description from existing LabVIEW error codes.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. With the following exception, this output provides
    standard error out functionality.

       If the value of error in is no error, this VI contains error information that corresponds to the
    error code input.

FindFind FirstFirst ErrorError

Tests the error status of one or more low-level functions or subVIs that produce a
numeric error code as output.


Inputs/Outputs

   •       error codes —

    error codes is an array of the numeric error codes assembled from local subVIs or functions. If
    there is no error indicated in the error in cluster, the VI tests these codes in ascending order for
    nonzero values. If the VI finds a nonzero value, error out reflects the error status of that input.


                                                    © National Instruments 1871

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1871 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1872 ordinal=1872 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      source messages —

            source messages contains the source message you want to appear in the error out cluster if the
              VI finds an error in error codes. Place each message on a separate line in a string constant or
              control. Use of this input is optional.

               •       error? —

             error? is TRUE if the error in cluster or any of the error codes reflects an error.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If this VI finds an error, it sets the parameters in the error out cluster. You can wire this
        cluster to the Simple Error Handler or General Error Handler to identify the error and
       describe it to the user.

      ErrorError ClusterCluster ConstantConstant

      Use the error cluster constant to pass an error cluster value to the block diagram. Set
        this value by clicking inside the constant with the Operating tool and specifying values
        for the status, code, and source elements.


      MultipleMultiple ErrorsErrors

      Use the Multiple Errors VIs to convert an error cluster into different formats or to
      manipulate the attributes of an error cluster.


1872   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1872 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1873 ordinal=1873 -->
## Functions

Functions


 Palette Object  Description

 Error Cluster to  Converts a cluster of errors into an array of encoded errors. This VI returns an
 Array of Errors  empty array if the error cluster does not include any errors.

 Convert to
 Legacy Error    Converts an error cluster from JSON encoded format to legacy format.
 Cluster

 Convert to
 Encoded Error  Converts an error cluster from legacy format to JSON encoded format.
 Cluster

               Updates the value of an attribute stored in an error cluster. If the specified
 Write Error      attribute name is not found, this VI adds the attribute with the specified value to
 Cluster         the error cluster.
 Attribute
                For a single cluster that stores multiple errors, this VI updates only the first error.

 Remove Error
 Cluster        Removes an attribute from an error cluster.
 Attribute

 List Error                Returns the names of all attributes stored in an error cluster. For a single cluster
 Cluster                 that stores multiple errors, this VI lists only the attribute names of the first error. Attributes

 Read Error                Returns the value of an attribute stored in an error cluster. If the attribute is not Cluster
                found, this VI returns an empty string.
 Attribute

ErrorError ClusterCluster toto ArrayArray ofof ErrorsErrors

Converts a cluster of errors into an array of encoded errors. This VI returns an empty
array if the error cluster does not include any errors.

To create a cluster of errors from multiple VIs or functions, use the Merge Errors
function.


                                                    © National Instruments 1873

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1873 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1874 ordinal=1874 -->
## Functions

Functions


      Inputs/Outputs

               •       error —

             error specifies an error cluster that you use to check for errors or warnings.

               •      array of errors —

            array of errors returns an array of all the error clusters, encoded in either JSON or legacy format.


      ConvertConvert toto LegacyLegacy ErrorError ClusterCluster

       Converts an error cluster from JSON encoded format to legacy format.


      Inputs/Outputs

               •       error in —

             error in specifies an error cluster that you use to check for errors or warnings.

               •       error out —

             error out returns the error from error in, encoded in legacy format.


      ConvertConvert toto EncodedEncoded ErrorError ClusterCluster

       Converts an error cluster from legacy format to JSON encoded format.


1874   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1874 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1875 ordinal=1875 -->
## Functions

Functions

Inputs/Outputs

   •       error in —

    error in specifies an error cluster that you use to check for errors or warnings.

   •       error out —

    error out returns the error from error in, encoded in JSON format.


WriteWrite ErrorError ClusterCluster AttributeAttribute

Updates the value of an attribute stored in an error cluster. If the specified attribute
name is not found, this VI adds the attribute with the specified value to the error
cluster.

For a single cluster that stores multiple errors, this VI updates only the first error.


Inputs/Outputs

   •       error in —

    error in specifies an error cluster that you use to check for errors or warnings.

   •       attribute name —

     attribute name specifies the name of the attribute that you want to update.

   •     JSON value —

   JSON value specifies the value, in JSON format, to set for the attribute.

   •       error out —

    error out returns an error cluster with the value of the specified attribute updated or with the
     specified attribute added.

   •      created? —

                                                    © National Instruments 1875

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1875 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1876 ordinal=1876 -->
## Functions

Functions


            created? returns TRUE if the VI added the specified attribute and value to the error cluster. This
           output returns FALSE if the VI found the specified attribute name in the error cluster and
           updated the value.


     RemoveRemove ErrorError ClusterCluster AttributeAttribute

      Removes an attribute from an error cluster.


      Inputs/Outputs

               •       error in —

             error in specifies an error cluster that you use to check for errors or warnings.

               •       attribute name —

             attribute name specifies the name of the attribute that you want to remove.

               •       error out —

             error out returns an error cluster with the attribute removed. If the attribute is not found, this
           output returns the same error as error in.

               •      deleted? —

            deleted? indicates if the attribute is removed.


        ListList ErrorError ClusterCluster AttributesAttributes

       Returns the names of all attributes stored in an error cluster. For a single cluster that
       stores multiple errors, this VI lists only the attribute names of the first error.


1876   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1876 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1877 ordinal=1877 -->
## Functions

Functions

Inputs/Outputs

   •       error —

    error specifies an error cluster that you use to check for errors or warnings.

   •       attribute names —

     attribute names returns the names of all attributes stored in the error cluster.


ReadRead ErrorError ClusterCluster AttributeAttribute

Returns the value of an attribute stored in an error cluster. If the attribute is not found,
this VI returns an empty string.


Inputs/Outputs

   •       error —

    error specifies an error cluster that you use to check for errors or warnings.

   •       attribute name —

     attribute name specifies the name of the attribute that you want to read.

   •     JSON object string —

   JSON object string returns the JSON objects stored in the error cluster.

   •      value string —

    value string returns the value of the attribute.

   •      found? —

    found? indicates if the attribute is found.


                                                    © National Instruments 1877

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1877 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1878 ordinal=1878 -->
## Functions

Functions

     PromptPrompt UserUser forfor InputInput

       Displays a standard dialog box that prompts users to enter information, such as a user
     name and password.


      Dialog Box Options

        Option   Description

        Message
         to       Contains the text to display in the dialog box.
         Display

                  Contains the following options:

                              •  First button name—

                        Specifies the text that appears on the first button. By default, the text on the first
                     button is OK.

        Buttons      • Second button name—
         to
         Display       Specifies the text that appears on the second button. By default, the text on the
                    second button is Cancel. This option is available only when you place a checkmark
                          in the Display second button checkbox.

                              • Display second button—

                        Specifies whether a second button is displayed in the dialog box.


                    Specifies the name and data type of the controls that appear in the dialog box. The
                   Inputs you list here are returned as outputs on the block diagram.
         Inputs                  Input Name is the name of the control and instructs users what to enter into the control.
                  Input Data Type is the type of control you want to use in the dialog box. You can choose
                from the following options: Number, Checkbox, or Text Entry Box.


1878   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1878 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1879 ordinal=1879 -->
## Functions

Functions


 Option   Description

          Contains the following options:

                  • Delete—

 Edit          Deletes the selected input.
 Inputs
                  • Insert—

                Inserts a new row in the Inputs list above the selected row.


 Window
          Contains the text to display in the title bar of the dialog box. Title

Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Enable —

    Enables or disables the Express VI. The default is ON or TRUE.

   •     OK —

    Returns TRUE when you click the first button in the dialog box and FALSE when you click the
    second button.

   •       error out —

    Contains error information. This output provides standard error out functionality.


      Note The behavior of this VI changes depending upon the target. If the
        current target does not or might not have a host computer connected, the
        configuration dialog box displays warnings next to options that are invalid
       without a host. If you configure this VI to prompt for input and run the VI on a
        target with no user interface, such as the Real-Time Module with no host
       computer connected, this VI returns an error.

                                                    © National Instruments 1879

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1879 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1880 ordinal=1880 -->
## Functions

Functions

     Components

        Inserts a new row in the Inputs list above the selected row.

       Deletes the selected input.

       Specifies whether a second button is displayed in the dialog box.

       Contains the text to display in the title bar of the dialog box.

       Specifies the text that appears on the second button. By default, the text on the second
       button is Cancel. This option is available only when you place a checkmark in the
       Display second button checkbox.

       Specifies the text that appears on the first button. By default, the text on the first
       button is OK.

       Contains the text to display in the dialog box.

       Specifies the name and data type of the controls that appear in the dialog box. The
       Inputs you list here are returned as outputs on the block diagram.

      DisplayDisplay MessageMessage toto UserUser

       Displays a standard dialog box that contains an alert or a message for users.


      Dialog Box Options

        Option   Description

        Message
         to       Contains the text to display in the dialog box.
         Display

        Buttons  Contains the following options:


1880   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1880 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1881 ordinal=1881 -->
## Functions

Functions


 Option   Description

                  •  First button name—

                Specifies the text that appears on the first button. By default, the text on the first
              button is OK.

                  • Second button name—
 to
 Display       Specifies the text that appears on the second button. By default, the text on the
             second button is Cancel. This option is available only when you place a checkmark
                 in the Display second button checkbox.

                  • Display second button—

                Specifies whether a second button is displayed in the dialog box.


Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Enable —

    Enables or disables the Express VI. The default is ON or TRUE.

   •      Message —

    Contains the text to display in the dialog box.

   •     OK? —

    Returns TRUE when you click the first button in the dialog box and FALSE when you click the
    second button.

   •       error out —

    Contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1881

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1881 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1882 ordinal=1882 -->
## Functions

Functions

     Components

       Specifies whether a second button is displayed in the dialog box.

       Specifies the text that appears on the first button. By default, the text on the first
       button is OK.

       Contains the text to display in the dialog box.

       Specifies the text that appears on the second button. By default, the text on the second
       button is Cancel. This option is available only when you place a checkmark in the
       Display second button checkbox.

      WriteWrite toto SystemSystem LogLog

       Writes a message to the nierrlog system log for storage and subsequent viewing.


      Inputs/Outputs

               •     message —

          message is the text to write to the system log.

               •       severity (Error) —

             severity specifies how the system log classifies the message.

           0 Error—Specifies the message as an error.
           1 Warning—Specifies the message as a warning.
           2 Informational—Specifies the message as informational text.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


1882   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1882 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1883 ordinal=1883 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


You can view the messages this VI writes using the system log viewer for your
operating system.

(Windows) Open the Application page of the Windows Event Viewer.

(macOS) Use Console to view the system log.

(Linux) Use a system log viewer appropriate to your distribution.

(NI Linux Real-Time) Open the System Log Viewer page of NI Web-based Configuration
& Monitoring.

(Phar Lap ETS, VxWorks) Open the console. The messages display alongside other
console output.

WaitWait ForFor FrontFront PanelPanel ActivityActivity FunctionFunction

Pauses the execution of the calling VI block diagram in run mode until the function
detects front panel activity in the front panel you want to monitor.


Inputs/Outputs

   •     do not wait! (False) —

       If do not wait! is TRUE, the VI runs without pausing execution.

   •       front panel (this VI's panel) —

    front panel is a reference to the VI you want to monitor for front panel activity.

    You can wire a VI, front panel, or control reference to this input. If you wire a control reference,


                                                    © National Instruments 1883

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1883 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1884 ordinal=1884 -->
## Functions

Functions


            the function monitors the activity of the front panel containing the control. If you do not specify
           a reference, the function monitors the front panel activity of the VI in which you place the
             function.

           You must wire a reference to a VI or object in a local application instance. You cannot wire a
             reference to a VI or object in a remote application instance.

               •      timeout ms (-1 never timeout) —

           timeout ms specifies the time, in milliseconds, that the function waits before it lets the VI
            continue execution. The default value is –1, which indicates to wait indefinitely.

               •      millisecond timer value —

            millisecond timer value returns the value of the millisecond timer.


       This function is similar to the Occurrences functions. Use this function if you want a
       block diagram to execute only after a user changes the value of a front panel object,
      such as when the user clicks a button, turns a knob, or enters data. This function
       activates that block diagram if the function detects user activity on the front panel. Use
        this function to eliminate the need for continually polling the front panel to determine
           if the value of a front panel object changes. You also can use this function to monitor
        activity on a remote front panel.

           Note You cannot use this function to handle front panel events such as
           mouse clicks or keystrokes programmatically. Use the Event structure to
             handle front panel events programmatically.

       Continual polling can cause a VI to run millions of times and use up system resources
       before a user interacts with the front panel. If you use this function, the loop runs only
       twice to respond to user input—once to engage the function and a second time when
       the user changes the value of a front panel object.

      The VI in the following example pauses at the Wait For Front Panel Activity Node until a
       user enters a user name or password or clicks the OK button.


1884   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1884 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1885 ordinal=1885 -->
## Functions

Functions


The OK button wired to the While Loop passes the user name and password to the
Validate Password VI and to the do not wait! parameter of the Wait For Front Panel
Activity function. If the button were not wired to the function, clicking the OK button
would execute the subdiagram in the While Loop including the Wait For Front Panel
Activity function, which defaults to wait on front panel activity when executed. The
user would have to click the OK button twice to send the user name and password to
the Validate Password VI—one time to wake up the VI and execute the loop and a
second time to wake up the VI and send the user name and password out of the loop
to the Validate Password VI.

GenerateGenerate FrontFront PanelPanel ActivityActivity FunctionFunction

Programmatically generates front panel activity so any VI execution halted by the Wait
on Front Panel Activity function continues executing. No actual changes occur on the
front panel.


Inputs/Outputs

   •       front panel (this VI's panel) —


                                                    © National Instruments 1885

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1885 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1886 ordinal=1886 -->
## Functions

Functions


             front panel specifies which VI the function generates front panel activity for. If you do not specify
           a reference to a VI, the function generates front panel activity of the VI in which you place the
             function.

           You must wire a reference to a VI in a local application instance. You cannot wire a reference to a
              VI in a remote application instance.

     ColorColor BoxBox ConstantConstant

      Use the color box constant to supply a constant color value to the block diagram.

      Use the color picker to set the color in the color box constant.

      You cannot change the value of the color box constant while the VI runs. You can assign
      a label to this constant.


      ListboxListbox SymbolSymbol RingRing ConstantConstant

      Use the listbox symbol ring constant to assign symbols to items in a listbox control.

      You typically wire the listbox symbol ring constant to the Item Symbols property in a
       Property Node for a listbox.


     EventsEvents

      Use the Events functions to register events dynamically and to create user events.


1886   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1886 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1887 ordinal=1887 -->
## Functions

Functions


 Palette            Description
 Object

 Register    Dynamically registers events. The events for which you can register depend on the type
 For         of the reference you wire to each event source input. Wire the event reg refnum out
 Events     output to an Event structure or to another Register For Events function.

            Waits until an event occurs, then executes the appropriate case to handle that event.
          The Event structure has one or more subdiagrams, or event cases, exactly one of which
 Event      executes when the structure executes to handle an event. This structure can time out
 Structure  while waiting for notification of an event. Wire a value to the Timeout terminal at the
           top left of the Event structure to specify the number of milliseconds the Event structure
            waits for an event. The default is -1, which indicates never to time out.

 Unregister
 For            Unregisters all events associated with an event registration refnum. Events
 Function

 Flush      Discards the least recent notify events from one or more event queues. If the event
 Event     queue that you want to discard includes filter events, this function stops at the first
 Queue       filter event in the queue and discards only the events that occurred previous to the
 Function   stop.

            Returns a reference to a user event. LabVIEW uses the user event data type you wire to
 Create           determine the event name and data type of the event. Wire the user event out output User            to a Register For Events function to register for the event. Wire the user event out
 Event           output to a Generate User Event function to send the event and associated data to all Function           Event structures registered for the event.

 Generate
 User       Broadcasts the user event you wire to the user event input and sends the user event
 Event     and associated event data to each Event structure registered to handle the event.
 Function

 Destroy
 User       Releases a user event reference by destroying its associated user event refnum. Any
 Event      Event structures registered for this user event no longer receive the event.
 Function

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Dialog and User Interface\Events\

                                                    © National Instruments 1887

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1887 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1888 ordinal=1888 -->
## Functions

Functions

        Events.lvproj
            • labview\examples\Structures\Event Structure\Event
        Structure.lvproj

       RegisterRegister ForFor EventsEvents

       Dynamically registers events. The events for which you can register depend on the
       type of the reference you wire to each event source input. Wire the event reg refnum
      out output to an Event structure or to another Register For Events function.


      Inputs/Outputs

               •      event registration refnum —

           event registration refnum is a reference to an existing event registration a Register For Events
             function created.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      event source —

           event source 1..n is a reference to an application, VI, control, or user event. References must be
             to local objects. You cannot wire a reference to a remote object.

                    If you wire an array or cluster of refnums to this input, LabVIEW registers all elements of the array
            or cluster for the event.
               •      event registration refnum —

           event reg refnum out returns the reference to a new or existing event registration.

               •       error out —

1888   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1888 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1889 ordinal=1889 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


When using dynamic registration, make sure you have a Register For Events function
for each Event structure.

Each event source input is a reference to an application, VI, control, or user event.
Each kind of event source can produce a variety of events. To specify which event you
want LabVIEW to begin detecting for a particular event source, right-click the data
item for the event source and select the event to detect. After this function executes,
LabVIEW detects, or registers, every repetition of that event that occurs. LabVIEW
stores these events in a queue so that an Event structure can handle the events later in
the VI.

You can wire the event reg refnum out terminal of the Register For Events function to
the dynamic event terminals on the Event structure border, to the Unregister For
Events function, or to the top left input of another Register For Events function. If you
wire the top left input of the Register For Events function, the function modifies the
existing registration information associated with that refnum instead of registering the
event again.

Registered events stay registered until you explicitly unregister them or until the VI that
registered the events finishes running or you abort the VI. If the VI which registered for
events was a subVI, events are unregistered when that VI's top-level VI finishes
execution or is aborted. If you use the Run VI method to execute a subVI that registered
for events, events are unregistered when the subVI finishes execution or is aborted.

      Note LabVIEW does not include an event registration refnum on the Controls
        palette because the event registration refnum is strictly typed and a generic
        version does not exist. You can create an event registration refnum by
        configuring a Register For Events function or right-clicking the function and
        creating a control or indicator from the shortcut menu. You also can select
       the part of the application that includes the event registration refnum and
        selecting Edit»Create SubVI to create a subVI from the selection. If you later
       modify the Register For Events function and change the type of the event
        registration refnum, you must recreate the control or indicator to match.


                                                    © National Instruments 1889

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1889 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1890 ordinal=1890 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Dialog and User Interface\Events\Dynamic
        Event Generation.vi

       UnregisterUnregister ForFor EventsEvents FunctionFunction

       Unregisters all events associated with an event registration refnum.

      Event structures that use this event registration refnum no longer receive any dynamic
       events. National Instruments recommends that you unregister for events when you no
       longer need to handle them. If you do not unregister for events, LabVIEW continues to
       generate and queue the events as long as the VI runs, even if no Event structure is
       waiting to handle them, which consumes memory and can hang the VI if you enable
       front panel locking for the events.


      Inputs/Outputs

               •      event registration refnum —

           event registration refnum is a reference to an existing event registration a Register For Events
             function created.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1890   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1890 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1891 ordinal=1891 -->
## Functions

Functions

FlushFlush EventEvent QueueQueue FunctionFunction

Discards the least recent notify events from one or more event queues. If the event
queue that you want to discard includes filter events, this function stops at the first
filter event in the queue and discards only the events that occurred previous to the
stop.


Inputs/Outputs

   •      oldest event time —

    oldest event time is the event timestamp, in milliseconds, when you want to start keeping
    events. This function discards all events previous to the event time you specify. This millisecond
    timer can accept the value returned by the Tick Count (ms) function.

   •      event registration refnum —

    event registration refnum is a reference to an event registration refnum associated with the
    queue you want to flush.

   •      include static events? (T) —

    include static events? specifies whether you want to include the enqueued static events
    associated with an Event structure in the flush operation. The default is TRUE if you place the
    Flush Event Queue function in an event case of an Event structure. Otherwise, the default is
    FALSE.

          Note If you wire include static events?, you must place this function inside the Event
              structure that handles the static events you want to include or omit from the flush
              operation.

   •      event type or object —

                                                    © National Instruments 1891

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1891 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1892 ordinal=1892 -->
## Functions

Functions


           event type or object specifies which notify events you want to discard within the criteria set by
            oldest event time and keep most recent.

             Refer to the Details section for more information about how to specify which events you want to
             discard.
               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      keep most recent —

           keep most recent specifies the number of most recent events to keep in the event queue. If you
            wire the event type or object parameter, keep most recent affects only the events of the type
           you specify. If you flush more than one event queue, keep most recent includes the total
          number of events to keep from all specified event queues.

               Note If you leave both oldest event time and keep most recent unwired, the
                      function discards all events in all queues that meet any criteria set by event type or
                      object. If you wire both oldest event time and keep most recent, this function keeps
                            all events starting at the event time you specify and all events within the number of
                  most recent events you specify.

               •      event reg refnum out —

           event reg refnum out returns the event registration refnum associated with the flushed event
           queue.

               •     number of events discarded —

          number of events discarded returns the total number of discarded events.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       For applications where events occur in rapid succession but the application only needs
       the most recent events, such as Mouse Move or Panel Resize events, you can discard
       the older events so the application can respond to the newer event data more quickly.

      The following examples show how you can wire data to the event type or object

1892   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1892 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1893 ordinal=1893 -->
## Functions

Functions

parameter to specify the way the Flush Event Queue function discards events.

Example 1: Discarding More than One Event Type

If you want to discard more than one event type, such as Mouse Down and Mouse Up,
you can wire an array or cluster of event type enums to the event type or object input,
as shown in the following example.


Flush Event Queue discards both the Mouse Down and the Mouse Up events regardless
of the event source. However, because a constant value of 1 is wired to the keep most
recent parameter, the function keeps one of the most recent Mouse Down or Mouse Up
events in the event queue. Furthermore, the function keeps only one event total rather
than one event for each event type.

Example 2: Discarding Events Generated by Specific Objects

You can wire a VI Server reference that points to an object that generates an event, a
user event refnum, and any refnum with associated events to the event type or object
input to discard only the events generated by a specific objects. To discard events from
multiple objects, use an array or cluster of refnums, as shown in the following
example.


Flush Event Queue discards any type of event generated by the objects linked to the


                                                    © National Instruments 1893

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1893 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1894 ordinal=1894 -->
## Functions

Functions

       references that are bundled in the cluster.

     Example 3: Discarding Specific Events Generated by Specific Objects

           If you want to discard an event only when a specific object generates that event, you
      can bundle an enum that contains the event type you want to discard with a refnum
       that points to the object that generates that event. You also can create a cluster or
       array of event type enum/object pairs to discard multiple events associated with
       multiple objects, as shown in the following example.


            •  —The function discards the Mouse Up or Mouse Down events only when the
         Boolean generates those events.
            •  —The function discards the Mouse Move event only when the 2D Picture control
          generates that event.
            •  — Because the event is not paired with a specific object, the function discards
          the Key Up event when any event source generates that event.
      CreateCreate UserUser EventEvent FunctionFunction

       Returns a reference to a user event. LabVIEW uses the user event data type you wire to
      determine the event name and data type of the event. Wire the user event out output
       to a Register For Events function to register for the event. Wire the user event out
      output to a Generate User Event function to send the event and associated data to all
      Event structures registered for the event.


1894   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1894 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1895 ordinal=1895 -->
## Functions

Functions

Inputs/Outputs

   •      user event data type —

    user event data type is a cluster of elements or an individual element whose data type and label
    define the data type and name of the user event.

          Note LabVIEW uses owned labels to identify data the user event carries, so label
            each element of the input with a descriptive owned label. If you do not add a label,
             the user event will not appear in the Event Data Node of an Event structure when
            added.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      user event out —

    user event out returns the strictly typed user event refnum.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The user event data type is a cluster of elements or an individual element. If you wire
a cluster to the user event data type input, LabVIEW uses the type name of the cluster
as the name of the user event. The names and data types of the cluster elements
define the event data the user event carries. If you wire an individual data element to
the user event data type input, LabVIEW uses the type name of the element as the
name of the user event and as the name of the single data item it carries, which is the
same data type as the element. The actual value you wire to the function is not
important because LabVIEW uses only the name and data type to define the user
event. The user event out output is a strictly typed refnum that includes the user
event name and event data type.

You can wire the user event out output to the Generate User Event function and the
Destroy User Event function. Wire the user event out output to the Register For Events
function to dynamically register for notification when the user event occurs. When you
handle a user event in an Event structure, the name of the user event appears in the

                                                    © National Instruments 1895

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1895 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1896 ordinal=1896 -->
## Functions

Functions

       event selector label at the top of the Event structure, and the user event data fields
      appear in the Event Data Node inside the left border of the event case.

           Note If you obtain a user event reference in one application instance, you
             cannot use that user event reference in another application instance. If you
              attempt to use a user event reference in another application instance,
            LabVIEW returns error 1500.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Dialog and User Interface\Events\User
        Event Generation.vi

      GenerateGenerate UserUser EventEvent FunctionFunction

       Broadcasts the user event you wire to the user event input and sends the user event
      and associated event data to each Event structure registered to handle the event.


      Inputs/Outputs

               •       priority (normal) —

              priority specifies the priority of the user event. If you specify high priority, the Generate
            User Event function enqueues the user event and associated event data into the event queue in
             front of any previously generated normal priority events. The default is normal priority.

           0   high priority
           1   normal priority (default)

               •      user event —


1896   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1896 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1897 ordinal=1897 -->
## Functions

Functions


    user event is a user event refnum the Create User Event function created.

   •      event data —

    event data is the type of data you defined in the user event data type input of the Create User
    Event function.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      user event out —

    user event out returns the strictly typed user event refnum.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The user event input accepts a user event refnum the Create User Event function
created. The data type of the event data input must match the data type of the user
event. For example, if the data type of the user event input is a string, the data type of
the event data input must also be a string. The event data is the type of data you
defined in the user event data type input of the Create User Event function. If the
event is not registered, the Generate User Event function has no effect.

DestroyDestroy UserUser EventEvent FunctionFunction

Releases a user event reference by destroying its associated user event refnum. Any
Event structures registered for this user event no longer receive the event.


Inputs/Outputs

   •      user event —


                                                    © National Instruments 1897

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1897 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1898 ordinal=1898 -->
## Functions

Functions


            user event is a user event refnum the Create User Event function created.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    MenuMenu

      Use the Menu functions to modify the menus in LabVIEW applications. Use the
       functions located on the top row of the palette to handle menu selections.

       (Real-Time Module) You cannot use these functions in VIs that run on RT targets.


         Palette Object          Description

         Current VI's Menubar                                Returns the menu reference refnum of the current VI.
         Function

        Get Menu Selection      Returns the item tag of the last selected menu item, optionally waiting ms
         Function              timeout milliseconds.

        Enable Menu Tracking
                               Enables or disables tracking of menu bar selections.
         Function

          Insert Menu Items        Inserts menu items specified by item names or item tags into a menu or a
         Function            submenu within the menu.

         Delete Menu Items
                                 Deletes menu items from the menu or a submenu within the menu.
         Function

         Set Menu Item Info
                                 Sets the attributes of a menu item.
         Function


1898   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1898 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1899 ordinal=1899 -->
## Functions

Functions


 Palette Object          Description

 Get Menu Item Info                        Returns the attributes of a menu item or menu bar. Function

 Get Menu Short Cut Info                        Returns the menu item that is accessible through a given shortcut. Function

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Dialog and User Interface\Menu\
   Customizing the Menubar

CurrentCurrent VI'sVI's MenubarMenubar FunctionFunction

Returns the menu reference refnum of the current VI.

Use the menu reference refnum in conjunction with other Menu functions to
programmatically modify the run-time menu of a VI.

(Real-Time Module) You cannot use this function in VIs that run on RT targets.


Inputs/Outputs

   •     menu reference —

   menu reference refers to the menu bar of the current VI.


GetGet MenuMenu SelectionSelection FunctionFunction

Returns the item tag of the last selected menu item, optionally waiting ms timeout
milliseconds.


                                                    © National Instruments 1899

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1899 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1900 ordinal=1900 -->
## Functions

Functions

           If you use this function with an Event structure configured to handle the same menu
       item, the Event structure takes precedence and LabVIEW ignores the Get Menu
       Selection function. In any given VI, use the Event structure or the Get Menu Selection
       function.

       (Real-Time Module) You cannot use this function in VIs that run on RT targets.


      Inputs/Outputs

               •     menu reference —

         menu reference is the reference to a menu bar in a VI.

           You can obtain this refnum with the Current VI's Menubar function.
               •     ms timeout (200) —

         ms timeout is the maximum amount of time this function checks for a menu selection.

          The default is 200 ms. –1 indicates never to time out.
               •      block menu (F) —

                    If block menu is TRUE, LabVIEW disables menu tracking after reading an item tag.

              After you process the menu selection, you must use the Enable Menu Tracking function to enable
         menu tracking. The default is FALSE.
               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timed out —

                    If timed out is TRUE, a user selection was not made within the time specified by ms timeout.

               •     menu reference out —

         menu reference out returns menu reference unchanged.


1900   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1900 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1901 ordinal=1901 -->
## Functions

Functions

   •      item tag —

    item tag is the menu item that was selected.

    Wire this value to a Case structure selector terminal to handle the menu selection. When you
    create a case to handle each menu item, enter application item tags in the case selector label to
    handle application menu items.
   •      item path —

    item path describes the position of the item in the menu hierarchy, which is in the format of a
      list of menu tags separated by a colon (:).

    For example, if you choose the Open menu item from the File menu, the item path is
   File:Open.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Dialog and User Interface\Menu\
   Customizing the Menubar\Customizing the Menubar.vi

EnableEnable MenuMenu TrackingTracking FunctionFunction

Enables or disables tracking of menu bar selections.

If you use the Get Menu Selection function to block a menu, you must use this function
to enable the menu.

(Real-Time Module) You cannot use this function in VIs that run on RT targets.


                                                    © National Instruments 1901

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1901 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1902 ordinal=1902 -->
## Functions

Functions

      Inputs/Outputs

               •     menu reference —

         menu reference is the reference to a menu bar in a VI.

           You can obtain this refnum with the Current VI's Menubar function.
               •      enable (T) —

           enable allows you to perform menu tracking if enable is TRUE (default). If enable is FALSE, menu
             tracking is disabled.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     menu reference out —

         menu reference out returns menu reference unchanged.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       InsertInsert MenuMenu ItemsItems FunctionFunction

        Inserts menu items specified by item names or item tags into a menu or a submenu
       within the menu.

       (Real-Time Module) You cannot use this function in VIs that run on RT targets.


      Inputs/Outputs

               •     menu tag —

1902   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1902 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1903 ordinal=1903 -->
## Functions

Functions


  menu tag specifies the submenu in which to insert the items.

   If you do not specify menu tag, the function inserts the items at the top level of the menu.
•     menu reference —

  menu reference is the reference to a menu bar in a VI or to a shortcut menu of a control. You can
  obtain this refnum with the Current VI's Menubar function or with the MenuRef event data field
  of menu events.

•      item names —

  item names identifies the items to insert in the menu. item names is the string that appears in
  the menu. You can wire either item names or item tags, in which case both names and tags have
  the same values. If you want to insert only one item, wire a string to item names.

•      item tags —

  item tags identifies the items to insert in the menu. item tags is the string that is returned if the
  menu item is selected. You can wire either item names or item tags, in which case both names
  and tags have the same values. If you want to insert only one item, wire a string to item tags.

  Use application item tags to insert application menu items.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       after item —

  after item specifies the position where the items are inserted. after item can be a tag (string) of
  an existing item or a position index (zero based integer) in the menu. To insert at the beginning
  of the menu, wire a number less than 0 to after item. To insert at the end of the menu, wire a
  number larger than the number of items in the menu. You can insert application items using
  application tags. You can insert a separator using the application tag APP_SEPARATOR. The
  function always ensures that the tags of all the inserted menu items are unique to the menu
  hierarchy by appending numbers to the supplied tags, if necessary.

•     menu reference out —

  menu reference out returns menu reference unchanged.

•      item tags out —


                                                   © National Instruments 1903

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1903 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1904 ordinal=1904 -->
## Functions

Functions


           item tags out returns the actual tags of the inserted items. If the function does not find menu
            tag or after item (tag), the function returns an error.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Dialog and User Interface\Menu\
        Customizing the Menubar\Customizing the Menubar.vi

      DeleteDelete MenuMenu ItemsItems FunctionFunction

       Deletes menu items from the menu or a submenu within the menu.

       (Real-Time Module) You cannot use this function in VIs that run on RT targets.


      Inputs/Outputs

               •     menu reference —

         menu reference is the reference to a menu bar in a VI or to a shortcut menu of a control.

           You can obtain this refnum with the Current VI's Menubar function or with the MenuRef event
            data field of menu events.

               •     menu tag —

         menu tag specifies the submenu from which to delete items.

                    If you do not specify menu tag, the function deletes all items from the menu.


1904   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1904 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1905 ordinal=1905 -->
## Functions

Functions

   •      items —

    items can be a tag (string) of an existing item, an array of tags of existing items, a position index
    (zero-based integer) of an item in the menu, or an array of position indexes of items in the menu.

    The default is to delete all the items in the menu or submenu specified by menu tag. If any of the
     specified items have a submenu, the function deletes the submenu and all its contents. Use
    application item tags for menus or shortcut menus to delete application menu items. Because
    separators do not have unique tags, you can delete them using their positional indexes.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     menu reference out —

   menu reference out returns menu reference unchanged.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Dialog and User Interface\Menu\
   Customizing the Menubar\Customizing the Menubar.vi

SetSet MenuMenu ItemItem InfoInfo FunctionFunction

Sets the attributes of a menu item.

Unwired attributes remain unchanged.

(Real-Time Module) You cannot use this function in VIs that run on RT targets.


                                                    © National Instruments 1905

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1905 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1906 ordinal=1906 -->
## Functions

Functions


      Inputs/Outputs

               •      item tag —

           item tag identifies the menu item you want to set attributes for.

                    If item tag is not valid, the function returns an error. Use application item tags to set attributes
              for application menu items.
               •     menu reference —

         menu reference is the reference to a menu bar in a VI or to a shortcut menu of a control.

           You can obtain this refnum with the Current VI's Menubar function or with the MenuRef event
            data field of menu events.
               •      item name —

           item name is the string that appears in the menu.

               •      enabled —

                    If enabled is FALSE, the menu item is grayed out.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      checked —

                    If checked is TRUE, the menu item has a checkmark next to it.

               •      short cut —

            short cut is the keyboard equivalent of selecting the menu item with a mouse.

                     •      include Shift key? —


1906   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1906 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1907 ordinal=1907 -->
## Functions

Functions


              If include Shift key? is TRUE, the shortcut includes the <Shift> key, in addition to the
        shortcut key.

         •      include Ctrl key? —

              If include Ctrl key? is TRUE, the shortcut includes the <Ctrl> key, in addition to the shortcut
         key. You can set include Ctrl key? to FALSE only if you select a function key, such as <F1>,
         <F2>, and so on, as the shortcut key.

       (macOS) The key included is <Command>. (Linux) The key included is <Alt>.
         •      shortcut key —

        shortcut key describes the key associated with the shortcut.


   •     menu reference out —

   menu reference out returns menu reference unchanged.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


GetGet MenuMenu ItemItem InfoInfo FunctionFunction

Returns the attributes of a menu item or menu bar.

(Real-Time Module) You cannot use this function in VIs that run on RT targets.


Inputs/Outputs

   •      item tag —


                                                    © National Instruments 1907

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1907 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1908 ordinal=1908 -->
## Functions

Functions


           item tag identifies the item whose attributes you want to return.

          The default is to return the menu bar attributes.

           Use application item tags to return application menu item attributes.

               •     menu reference —

         menu reference is the reference to a menu bar in a VI or to a shortcut menu of a control.

           You can obtain this refnum with the Current VI's Menubar function or with the MenuRef event
            data field of menu events.
               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     submenu tags —

          submenu tags are the submenu item tags if the item has a submenu.

               •     menu reference out —

         menu reference out returns menu reference unchanged.

               •      item name —

           item name is the string that appears in the menu.

               •      enabled —

                    If enabled is FALSE, the menu item is grayed out.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      checked —

                    If checked is TRUE, the menu item has a checkmark next to it.

               •      short cut —

            short cut is the keyboard equivalent of selecting this menu item with a mouse.


1908   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1908 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1909 ordinal=1909 -->
## Functions

Functions


         •      include Shift key? —

              If include Shift key? is TRUE, the shortcut includes the <Shift> key, in addition to the
        shortcut key.

         •      include Ctrl key? —

              If include Ctrl key? is TRUE, the shortcut includes the <Ctrl> key, in addition to the shortcut
         key. You can set include Ctrl key? to FALSE only if you select a function key, such as <F1>,
         <F2>, and so on, as the shortcut key. On macOS, the key included is <Command>. On Linux,
        the key included is <Alt>.

         •      shortcut key —

        shortcut key describes the key associated with the shortcut.


GetGet MenuMenu ShortShort CutCut InfoInfo FunctionFunction

Returns the menu item that is accessible through a given shortcut.

(Real-Time Module) You cannot use this function in VIs that run on RT targets.


Inputs/Outputs

   •     menu reference —

   menu reference is the reference to a menu bar in a VI.

    You can obtain this refnum with the Current VI's Menubar function.
   •      short cut —

    short cut is the keyboard equivalent of selecting the menu item with a mouse.

         •      include Shift key? —


                                                    © National Instruments 1909

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1909 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1910 ordinal=1910 -->
## Functions

Functions


                           If include Shift key? is TRUE, the shortcut includes the <Shift> key, in addition to the
                shortcut key.

                     •      include Ctrl key? —

                           If include Ctrl key? is TRUE, the shortcut includes the <Ctrl> key, in addition to the shortcut
                 key. You can set include Ctrl key? to FALSE only if you select a function key, such as <F1>,
                 <F2>, and so on, as the shortcut key. (macOS) The key included is <Command>. (Linux) The
               key included is <Alt>.

                     •      shortcut key —

                shortcut key describes the key associated with the shortcut.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     menu reference out —

         menu reference out returns menu reference unchanged.

               •      item tag —

           item tag is the tag of the menu item that matches the shortcut.

               •      item path —

           item path describes the position of the item in the menu hierarchy, which is in the format of a
                  list of menu tags separated by a colon (:).

            For example, on Windows, if you do not change the default shortcuts and you pass in <Ctrl-O>
           from the menu bar reference of a VI, item path returns File:Open.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1910   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1910 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1911 ordinal=1911 -->
## Functions

Functions

CursorCursor

Use the Cursor VIs to change the appearance of the cursor on the front panel of a VI.
For example, if the VI is acquiring or analyzing data and can accept no user input, you
might want to change the cursor to an hourglass or watch cursor. After the VI finishes
acquiring or analyzing data and can accept user input, you can change the cursor back
to the default cursor.

(Real-Time Module) You cannot use these VIs in VIs that run on RT targets.


 Palette             Description
 Object

 Create
 Cursor      Returns a reference to a cursor in a cursor file.
 From File

           Changes the appearance of the cursor on the front panel of a VI. Wire data to the icon Set Cursor             input to determine the polymorphic instance to use or manually select the instance.


 Destroy     Closes a reference to a cursor and changes the cursor to the default cursor in any VIs
 Cursor      using the reference.


           Changes the appearance of the cursor on the front panel of a VI to the system busy
 Set Busy
              cursor. You also can use this VI to disable the mouse and keyboard on the front panel.


           Changes the appearance of the cursor on the front panel of a VI from a busy cursor to
 Unset Busy
            the default LabVIEW cursor and enables the mouse on the front panel.


Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 1911

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1911 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1912 ordinal=1912 -->
## Functions

Functions

            • labview\examples\Dialog and User Interface\Cursor\
        Cursor.lvproj

      CreateCreate CursorCursor FromFrom FileFile

       Returns a reference to a cursor in a cursor file.

           If a VI that you want to distribute as a stand-alone application or as a shared library
       uses a cursor from a cursor file, you must distribute the cursor file with the application
       or shared library.

       (Real-Time Module) You cannot use this VI in VIs that run on RT targets.


      Inputs/Outputs

               •      cursor file —

            cursor file is the path to the file that contains the cursor for which you want a reference.

                    If the file does not exist or if the file is not a valid cursor file, LabVIEW returns error code 7.

           (Windows) The file must have a .ani or .cur extension.

           (macOS) The file must be a resource file. You also must wire the ID of the cursor you want to use
             to the cursor resource ID input. If the cursor image is larger than 16 × 16 pixels, the VI crops the
           image to that size.

             (Linux) The file must have a .png extension. You cannot use animated cursors. Cursors are
          monochrome, and the shape of the cursor is determined by the how you set the transparency
           around the .png file.

               •      cursor resource ID —

           (macOS) cursor resource ID is the ID for a cursor in the resource file wired to cursor file.

                    If the cursor is animated, cursor resource ID must be less than 128. If the cursor is not


1912   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1912 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1913 ordinal=1913 -->
## Functions

Functions


  animated, cursor resource ID must be equal to or greater than 128.

•      hotspot —

  hotspot contains the coordinates of the cursor hot spot starting from the upper left corner. You
  cannot set the hot spot for animated cursors.

  National Instruments recommends that you set the hot spot only on Linux. Windows and macOS
  cursors already have hot spots, but you must set the hot spot for cursors on Linux.

      •      x —

      x is the horizontal coordinate of the hot spot, which increases to the right. The default is –1,
      which means the VI sets the horizontal coordinate of the hot spot to the horizontal
      coordinate of the default hot spot for the cursor.

      •      y —

      y is the vertical coordinate of the hot spot, which increases to the bottom. The default is –1,
      which means the VI sets the vertical coordinate of the hot spot to the vertical coordinate of
      the default hot spot for the cursor.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      cursor ID —

  cursor ID is a reference to the cursor in the cursor file. If a reference to the cursor already exists,
  the VI returns the existing reference.

  Wire this reference to the Set Cursor or Set Busy VIs to change the appearance of the cursor on
  the front panel of the VI.

  Use the Destroy Cursor VI to close the cursor reference after you set the cursor.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 1913

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1913 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1914 ordinal=1914 -->
## Functions

Functions

      SetSet CursorCursor

      Changes the appearance of the cursor on the front panel of a VI. Wire data to the icon
       input to determine the polymorphic instance to use or manually select the instance.

       (Real-Time Module) You cannot use this VI in VIs that run on RT targets.


            • Set Cursor (Icon Pict) VI
            • Set Cursor (Cursor ID) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Dialog and User Interface\Cursor\Change
        Cursor Icon.vi
    SetSet CursorCursor (Icon(Icon Pict)Pict) VIVI

      Changes the appearance of the cursor on the front panel of a VI. Wire data to the icon
       input to determine the polymorphic instance to use or manually select the instance.

       (Real-Time Module) You cannot use this VI in VIs that run on RT targets.


      Inputs/Outputs

               •      icon —

            icon is the system or LabVIEW cursor you want to use on the front panel of the VI.


1914   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1914 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1915 ordinal=1915 -->
## Functions

Functions


  Uses the default LabVIEW cursor. For example, if automatic tool selection is enabled and you
0 move the cursor over a ring control, LabVIEW uses the cursor of the Operating tool. If you
  move the cursor over a string control, LabVIEW uses the cursor of the Labeling tool.
    (Windows) LabVIEW uses this system cursor. (macOS and Linux) LabVIEW uses the system
1
  cursor that corresponds to this Windows cursor.
     (Windows) LabVIEW uses this system cursor. (macOS and Linux) LabVIEW uses the system
2
  cursor that corresponds to this Windows cursor.
    (Windows) LabVIEW uses this system cursor. (macOS and Linux) LabVIEW uses the system
3
  cursor that corresponds to this Windows cursor.
     (Windows) LabVIEW uses this system cursor. (macOS and Linux) LabVIEW uses the system
4
  cursor that corresponds to this Windows cursor.
     (Windows) LabVIEW uses this system cursor. (macOS and Linux) LabVIEW uses the system
5
  cursor that corresponds to this Windows cursor.
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30


                                                 © National Instruments 1915

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1915 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1916 ordinal=1916 -->
## Functions

Functions


           31
           32

               •       VI reference (current VI) —

             VI reference is a reference to the VI for which you want to change the cursor. The default is a
             reference to the current VI.

           You can use the Open VI Reference function to obtain a reference to another VI.

             This input is useful if multiple front panels are open, but you want to change the cursor in only
          one front panel. If the front panel of the VI for which you want to change the cursor is not open,
              this VI returns an error.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      previous cursor ID —

            previous cursor ID is a reference to the cursor on the front panel before this VI ran.

            Wire this output to another instance of the Set Cursor VI to change the cursor back to the
            previous cursor.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Dialog and User Interface\Cursor\Change
        Cursor Icon.vi
    SetSet CursorCursor (Cursor(Cursor ID)ID) VIVI

      Changes the appearance of the cursor on the front panel of a VI. Wire data to the icon

1916   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1916 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1917 ordinal=1917 -->
## Functions

Functions

input to determine the polymorphic instance to use or manually select the instance.

(Real-Time Module) You cannot use this VI in VIs that run on RT targets.


Inputs/Outputs

   •      cursor ID —

    cursor ID is a reference to the cursor you want to use on the front panel of the VI.

    Use the Create Cursor From File VI to obtain a reference to a cursor.

       If the cursor reference is invalid, LabVIEW changes the cursor to the default LabVIEW cursor and
    returns control of the cursor to LabVIEW.

   •       VI reference (current VI) —

     VI reference is a reference to the VI for which you want to change the cursor. The default is a
    reference to the current VI.

    You can use the Open VI Reference function to obtain a reference to another VI.

    This input is useful if multiple front panels are open, but you want to change the cursor in only
    one front panel. If the front panel of the VI for which you want to change the cursor is not open,
     this VI returns an error.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      previous cursor ID —

    previous cursor ID is a reference to the cursor on the front panel before this VI ran.

    Wire this output to another instance of the Set Cursor VI to change the cursor back to the
    previous cursor.

   •       error out —


                                                    © National Instruments 1917

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1917 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1918 ordinal=1918 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Dialog and User Interface\Cursor\Change
        Cursor Icon.vi

      DestroyDestroy CursorCursor

       Closes a reference to a cursor and changes the cursor to the default cursor in any VIs
       using the reference.

       (Real-Time Module) You cannot use this VI in VIs that run on RT targets.


      Inputs/Outputs

               •      cursor ID —

            cursor ID is the cursor reference you want to close.

           Use the Create Cursor From File VI to create this reference.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1918   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1918 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1919 ordinal=1919 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Dialog and User Interface\Cursor\Change
   Cursor Icon.vi

SetSet BusyBusy

Changes the appearance of the cursor on the front panel of a VI to the system busy
cursor. You also can use this VI to disable the mouse and keyboard on the front panel.

Use the Unset Busy VI to change the cursor back to the default LabVIEW cursor and to
enable the mouse and keyboard again. Using the Set Busy VI is similar to using the Set
Cursor VI and wiring 1 to the icon input.

(Real-Time Module) You cannot use this VI in VIs that run on RT targets.


Inputs/Outputs

   •      cursor ID —

    cursor ID is a reference to the cursor you want to use on the front panel of the VI. The default is
    the system busy cursor.

    Use the Create Cursor From File VI to obtain a reference to a cursor.

       If the cursor reference is invalid, LabVIEW changes the cursor to the default LabVIEW cursor and
    returns control of the cursor to LabVIEW.

   •       VI reference (current VI) —

     VI reference is a reference to the VI for which you want to change the cursor. The default is a
    reference to the current VI.


                                                    © National Instruments 1919

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1919 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1920 ordinal=1920 -->
## Functions

Functions


           You can use the Open VI Reference function to obtain a reference to another VI.

             This input is useful if multiple front panels are open, but you want to change the cursor in only
          one front panel. If the front panel of the VI for which you want to change the cursor is not open,
              this VI returns an error.

               •      disable click? (T) —

                    If disable click? is TRUE (default), the VI disables the mouse and keyboard on the front panel.

           You must use the Unset Busy VI to enable the mouse and keyboard again.

                    If you disable the mouse and keyboard on the front panel, the user still can click the Abort
            Execution button on the toolbar.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      previous cursor ID —

            previous cursor ID is a reference to the cursor on the front panel before this VI ran.

            Wire this output to the Set Cursor VI to change the cursor back to the previous cursor.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Dialog and User Interface\Cursor\Set
        Busy Cursor.vi

      UnsetUnset BusyBusy

      Changes the appearance of the cursor on the front panel of a VI from a busy cursor to
       the default LabVIEW cursor and enables the mouse on the front panel.

1920   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1920 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1921 ordinal=1921 -->
## Functions

Functions

Use this VI only after you use the Set Busy VI.

(Real-Time Module) You cannot use this VI in VIs that run on RT targets.


Inputs/Outputs

   •       VI reference (current VI) —

     VI reference is a reference to the VI for which you want to change the cursor. The default is a
    reference to the current VI.

    You can use the Open VI Reference function to obtain a reference to another VI.

    This input is useful if multiple front panels are open, but you want to change the cursor in only
    one front panel. If the front panel of the VI for which you want to change the cursor is not open,
     this VI returns an error.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Dialog and User Interface\Cursor\Set
   Busy Cursor.vi


                                                    © National Instruments 1921

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1921 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1922 ordinal=1922 -->
## Functions

Functions

     HelpHelp

      Use the Help VI and functions to link from VIs to HTML files or compiled help files.

       (Real-Time Module) You cannot use the objects on this palette in VIs that run on RT
        targets.


         Palette                  Description        Object

         Control
        Help                   Modifies the Context Help window by showing, hiding, or by repositioning the window.       Window
         Function

        Get Help
       Window                  Returns the status and the position of the Context Help window.         Status
         Function

         Control
         Online    Controls a compiled help file by displaying the table of contents, jumping to a specific
        Help      topic in the file, or closing the help file.
         Function

       Open     Displays a URL or HTML file in the default Web browser. If the URL or path you wire to this
       URL in    VI contains a space character, the VI encodes the space as %20 before displaying the URL
         Default   or HTML file in the Web browser. Wire data to the URL input to determine the
        Browser  polymorphic instance to use or manually select the instance.


      ControlControl HelpHelp WindowWindow FunctionFunction

       Modifies the Context Help window by showing, hiding, or by repositioning the window.

       (Real-Time Module) You cannot use this function in VIs that run on RT targets.


1922   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1922 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1923 ordinal=1923 -->
## Functions

Functions


Inputs/Outputs

   •     Show —

       If Show is TRUE, LabVIEW displays the Context Help window. If FALSE, LabVIEW hides the
    Context Help window. The default is to maintain the current visibility of the Context Help
    window.

   •     Top Left Corner —

    Top Left Corner indicates the new position of the Context Help window and contains numbers
    that represent points offset from the upper left corner of the screen.

         •      Horizontal —

        Horizontal is the number of points to place the Context Help window to the right of the
        upper left corner of the screen.

         •       Vertical —

         Vertical is the number of points to place the Context Help window below the upper left
        corner of the screen.


GetGet HelpHelp WindowWindow StatusStatus FunctionFunction

Returns the status and the position of the Context Help window.

(Real-Time Module) You cannot use this function in VIs that run on RT targets.


Inputs/Outputs

   •     Show —


                                                    © National Instruments 1923

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1923 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1924 ordinal=1924 -->
## Functions

Functions


                    If Show is TRUE, the Context Help window is visible.

                    If FALSE, the Context Help window is not visible.
               •     Top Left Corner —

          Top Left Corner indicates the position of the Context Help window and contains numbers that
            represent points offset from the upper left corner of the screen.

                     •      Horizontal —

                Horizontal is the number of points that the Context Help window is to the right of the upper
                      left corner of the screen.

                     •       Vertical —

                  Vertical is the number of points that the Context Help window is below the upper left corner
                  of the screen.


      ControlControl OnlineOnline HelpHelp FunctionFunction

       Controls a compiled help file by displaying the table of contents, jumping to a specific
       topic in the file, or closing the help file.

      You can create a compiled help file and use this function to link from a VI to the help
          file. You also can use this function to display an HTML file in the default browser.

       (Real-Time Module) You cannot use this function in VIs that run on RT targets.


      Inputs/Outputs

               •      Operation —

           Operation is the operation to perform on the help file.


1924   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1924 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1925 ordinal=1925 -->
## Functions

Functions


   Contents—Displays the table of contents of the help file. If you use this function to control a
  0 .chm file, setting this input to 0 displays the table of contents, index, or search tab, depending
   on which tab was visible the last time you closed the .chm file.
   Key—Displays a specific topic in the help file using a keyword in the help file index or using the  1   name of an individual HTML file in the compiled help file.
  2 Close—Closes the help file.

•       String to search for —

  String to search for is the index keyword or HTML filename for the topic in the help file that you
  want to display.

  The default is an empty string. LabVIEW ignores this string if Operation is 0 or 2.

   If this string contains an index keyword, the string must match the index keyword as it appears in
  the help file index. To jump to a topic with a multi-level index keyword, enter the first-level index
  keyword, a colon, and the second-level index keyword. Do not separate the elements with
  spaces. For example, a error codes:GPIB string jumps to a topic with a first-level index
  keyword of error codes and a second-level index keyword of GPIB.

   If Path to the help file contains a path to an HTML Help (.chm) file, this string can contain the
  filename (.htm or .html) of an individual HTML file in the HTML Help project.

•      Path to the help file —

  Path to the help file is the path or symbolic path to the compiled help file you want to control.

  The help file can have a .chm or .hlp extension. (macOS and Linux) If this input contains a
  path to a .chm file and the file does not exist, LabVIEW ignores this input. However, if String to
  search for contains an HTML filename and that HTML file is in the help\html\help.chm
  directory where help.chm is the filename you wire to this input, LabVIEW displays that HTML
   file in the default browser. If this input contains a path to a .chm file and String to search for
  contains an index keyword, this function does not display an HTML file.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 1925

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1925 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1926 ordinal=1926 -->
## Functions

Functions

     OpenOpen URLURL inin DefaultDefault BrowserBrowser

       Displays a URL or HTML file in the default Web browser. If the URL or path you wire to
        this VI contains a space character, the VI encodes the space as %20 before displaying
       the URL or HTML file in the Web browser. Wire data to the URL input to determine the
      polymorphic instance to use or manually select the instance.

       (Real-Time Module) You cannot use this VI in VIs that run on RT targets.


            • Open URL in Default Browser (string) VI
            • Open URL in Default Browser (path) VI
   OpenOpen URLURL inin DefaultDefault BrowserBrowser (string)(string) VIVI

       Displays a URL or HTML file in the default Web browser. If the URL or path you wire to
        this VI contains a space character, the VI encodes the space as %20 before displaying
       the URL or HTML file in the Web browser. Wire data to the URL input to determine the
      polymorphic instance to use or manually select the instance.

       (Real-Time Module) You cannot use this VI in VIs that run on RT targets.


      Inputs/Outputs

               •     URL —

         URL is the URL you want to display in the default Web browser.

            For example, wire http://www.site.com/report.html to this input to display the HTML
                 file report.html on the Web Server www.site.com in the browser.

               •       error in (no error) —


1926   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1926 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1927 ordinal=1927 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     URL out —

   URL out is the URL displayed in the Web browser.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

OpenOpen URLURL inin DefaultDefault BrowserBrowser (path)(path) VIVI

Displays a URL or HTML file in the default Web browser. If the URL or path you wire to
this VI contains a space character, the VI encodes the space as %20 before displaying
the URL or HTML file in the Web browser. Wire data to the URL input to determine the
polymorphic instance to use or manually select the instance.

(Real-Time Module) You cannot use this VI in VIs that run on RT targets.


Inputs/Outputs

   •      path —

    path is the path to the HTML file you want to display in the default Web browser.

       If the path is relative, the VI interprets the path as relative to the application directory, such as
    the labview directory or the directory containing the stand-alone application.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     URL out —


                                                    © National Instruments 1927

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1927 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1928 ordinal=1928 -->
## Functions

Functions


         URL out is the URL displayed in the Web browser.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     SynchronizationSynchronization

      Use the Synchronization VIs and functions to synchronize tasks executing in parallel
      and to pass data between parallel tasks.


         Palette                      Description
        Object

                   Use the Notifier Operations functions to suspend the execution of a block diagram          Notifier
                         until you receive data from another section of the block diagram or from another VI        Operations                     running in the same application instance.


       Queue      Use the Queue Operations functions to create a queue for communicating data
        Operations  between sections of a block diagram or from another VI.


                   Use the Semaphore VIs to limit the number of tasks that can simultaneously operate
                  on a shared (protected) resource. A protected resource or critical section of code
       Semaphore
                    might include writing to global variables or communicating with external
                      instruments.


                   Use the Rendezvous VIs to synchronize two or more separate, parallel tasks at
                         specific points of execution. Each task that reaches the rendezvous waits until the
        Rendezvous
                       specified number of tasks are waiting, at which point all tasks proceed with
                       execution.


1928   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1928 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1929 ordinal=1929 -->
## Functions

Functions


 Palette              Description
 Object

 Occurrences Use the Occurrences functions to control separate, synchronous activities.

               Indicates that a subVI or section of a block diagram is running for the first time. The First Call?                 First Call? function returns TRUE only the first time you call it after you click the Run Function              button.

             Passes through the values of the input wires after the upstream code executes.
 Synchronize
 Data Flow   Use this VI to synchronize multiple parallel code paths at a single point of data flow to
             ensure a certain execution order.


NotifierNotifier OperationsOperations

Use the Notifier Operations functions to suspend the execution of a block diagram
until you receive data from another section of the block diagram or from another VI
running in the same application instance.

You cannot use notifiers to communicate with VIs on other computers. For example,
you cannot use notifiers to communicate across a network or the VI Server.

Unlike the Queue Operations functions, the Notifier Operations functions do not buffer
sent messages. If no nodes are waiting on a message when it is sent, the data is lost if
another message is sent. Notifiers behave like single-element, bounded, lossy queues.

When using a Notifier Operation function in a While Loop, the stop condition should be
connected to the execution of the function.


 Palette Object       Description

 Obtain Notifier
                     Returns a reference to a notifier.
 Function


                                                    © National Instruments 1929

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1929 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1930 ordinal=1930 -->
## Functions

Functions


         Palette Object       Description

       Send Notification                          Sends a message to all functions waiting on a notifier.         Function

        Cancel Notification   Erases any message currently in a notifier and returns the cancelled
         Function           message.

        Get Notifier Status    Returns information about the current state of a notifier, such as the last
         Function            uncancelled notification sent to the notifier.

         Release Notifier                             Releases a reference to a notifier.         Function

        Wait on Notification                             Waits until a notifier receives a message.         Function

        Wait on Notification
        from Multiple        Waits until at least one of the notifiers you specify receives a message.
         Function

                         Use the Advanced Notifier Waiting functions to prevent dropped messages        Advanced Notifier                         and other problems when you use the functions repeatedly with different         Waiting
                                    notifiers.


      ObtainObtain NotifierNotifier FunctionFunction

       Returns a reference to a notifier.

      Use this reference when calling other Notifier Operations functions.


      Inputs/Outputs

               •     name (unnamed) —

         name contains the name of the notifier that you want to obtain or create.

          The default is an empty string to create an unnamed notifier.

1930   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1930 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1931 ordinal=1931 -->
## Functions

Functions

   •      element data type —

    element data type is the type of data that you want the notifier to contain.

    You can wire any data type to this input.
   •      create if not found? (T) —

    create if not found? specifies whether you want to create a new notifier if one with the same
   name as name does not exist.

       If TRUE (default), the function creates a notifier if one with the same name does not exist.
   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       notifier out —

     notifier out is a reference to the existing named notifier or the new notifier created by this
     function.

   •      created new? —

    created new? is TRUE if the function created a new notifier.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use named notifiers to pass data between two sections of a block diagram or between
two VIs. If you do not wire name, the function creates a new, unnamed notifier
reference. If you wire name, the function first searches for an existing notifier with the
same name and returns a new reference to the existing notifier. If a notifier with the
same name does not already exist and create if not found? is TRUE, the function
creates a new, named notifier reference.

If you use the Obtain Notifier function to return a reference to a named notifier inside a
loop, LabVIEW creates a new reference to the named notifier each time the loop
iterates. If you use Obtain Notifier in a tight loop, LabVIEW slowly increases how much
memory it uses because each new reference uses an additional four bytes. These bytes
are released automatically when the VI stops running. However, in a long-running


                                                    © National Instruments 1931

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1931 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1932 ordinal=1932 -->
## Functions

Functions

       application it may appear as if LabVIEW is leaking memory since the memory usage
      keeps increasing. To prevent this unintended memory allocation, use the Release
        Notifier function in the loop to release the notifier reference for each iteration.

       This function might return error codes 1, 2, 1094, 1100, or 1492.

           Note If you obtain a notifier reference in one application instance, you
             cannot use that notifier reference in another application instance. If you
              attempt to use a notifier reference in another application instance, LabVIEW
               returns error 1492.

     SendSend NotificationNotification FunctionFunction

      Sends a message to all functions waiting on a notifier.

         All Wait on Notification and Wait on Notification from Multiple functions currently
       waiting on the notifier stop waiting and continue to execute.


      Inputs/Outputs

               •       notifier —

              notifier is a reference to a notifier.

           Use the Obtain Notifier function to obtain a notifier reference.
               •       notification —

             notification is the message to send.

             This data type changes to match the subtype of notifier.
               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       notifier out —


1932   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1932 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1933 ordinal=1933 -->
## Functions

Functions


     notifier out returns notifier unchanged.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Synchronization\Notifier\Simple
   Notifier.vi

CancelCancel NotificationNotification FunctionFunction

Erases any message currently in a notifier and returns the cancelled message.


Inputs/Outputs

   •       notifier —

     notifier is a reference to a notifier.

    Use the Obtain Notifier function to obtain a notifier reference.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       notifier out —

     notifier out returns notifier unchanged.

   •      canceled notification —


                                                    © National Instruments 1933

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1933 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1934 ordinal=1934 -->
## Functions

Functions


            cancelled notification contains the last notification sent to the notifier.

             This data type changes to match the subtype of notifier.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If any Wait on Notification or Wait on Notification from Multiple functions received the
      message before the call to this function, those functions continue to execute. This
       function does not recall or reset any wait functions. After you cancel a notification, any
      subsequent wait functions wait until the notifier receives another message. Canceling
      a notification before the notifier has a message does not result in an error.

      GetGet NotifierNotifier StatusStatus FunctionFunction

       Returns information about the current state of a notifier, such as the last uncancelled
        notification sent to the notifier.


      Inputs/Outputs

               •       notifier —

              notifier is a reference to a notifier.

           Use the Obtain Notifier function to obtain a notifier reference.
               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       notifier name —


1934   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1934 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1935 ordinal=1935 -->
## Functions

Functions


     notifier name specifies the name of the notifier.

   •       notifier out —

     notifier out returns notifier unchanged.

   •       latest notification —

     latest notification is the most recent uncancelled notification sent to the notifier.

       If no notification is available, the function returns the zero value for the element data type you
    wired in the Obtain Notifier function.

    This data type changes to match the subtype of notifier.

   •      # waiting —

    # waiting is the number of functions currently waiting on the notifier.

    These functions include Wait on Notification and Wait on Notification from Multiple.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


ReleaseRelease NotifierNotifier FunctionFunction

Releases a reference to a notifier.


Inputs/Outputs

   •       notifier —

     notifier is a reference to a notifier.

    Use the Obtain Notifier function to obtain a notifier reference.
   •       force destroy? (F) —


                                                    © National Instruments 1935

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1935 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1936 ordinal=1936 -->
## Functions

Functions


             force destroy? indicates whether to destroy the notifier.

                    If FALSE (default) and you want to destroy the notifier, call the Release Notifier function a
          number of times equal to the number of times you obtained a reference to the notifier or stop all
              VIs using the notifier reference. If TRUE, the function destroys the notifier and you do not have to
               call the function multiple times or stop all VIs using the notifier reference.
               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       notifier name —

              notifier name specifies the name of the notifier.

               •       last notification —

              last notification is the last uncancelled notification sent to the notifier.

                    If no notification is available, the function returns the zero value for the element data type you
            wired in the Obtain Notifier function.

             This data type changes to match the subtype of notifier.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      You can use the Obtain Notifier function to obtain a reference to the same notifier with
       the same name multiple times. To destroy a notifier, call the Release Notifier function a
      number of times equal to the number of times you obtained a reference to the notifier
       or stop all VIs using the notifier reference.

           If force destroy? is TRUE, this function releases all references to the notifier and
       destroys the notifier.

      Any Wait on Notification or Wait on Notification from Multiple functions waiting on the
        notifier time out and return error code 1122.


1936   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1936 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1937 ordinal=1937 -->
## Functions

Functions

WaitWait onon NotificationNotification FunctionFunction

Waits until a notifier receives a message.

When the notifier receives a message, this function continues to execute. Use the Send
Notification function to send the message. If a notifier reference becomes invalid such
as when another function closes it, the function stops waiting and returns error code
1122. If the notifier does not contain a message, this function waits until the notifier
receives a message.


Inputs/Outputs

   •       notifier —

     notifier is a reference to a notifier.

    Use the Obtain Notifier function to obtain a notifier reference.
   •      ignore previous (F) —

    ignore previous indicates whether to ignore messages that LabVIEW sends to the notifier before
       it calls this function.

       If TRUE and the notifier contains a message before you call this function, this function waits until
    the notifier receives another message. If FALSE (default) and the notifier contains a message
    before you call this function, this function continues to execute.
   •      timeout in ms (-1) —

    timeout in ms specifies the time, in milliseconds, that the function waits for the notifier to
    receive a message.

    The default is –1, which indicates never to time out.

       If the function waits timeout in ms and the notifier does not receive a message, timed out? is
    TRUE.

   •       error in (no error) —


                                                    © National Instruments 1937

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1937 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1938 ordinal=1938 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       notifier out —

              notifier out returns notifier unchanged.

               •       notification —

             notification is the last message the notifier receives.

             This data type changes to match the subtype of notifier.
               •      timed out? —

           timed out? is TRUE if the notifier does not receive a message before the function times out or if
          an error occurs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Each unique instance of this function remembers the timestamp of the last message it
        receives.

           If ignore previous is FALSE, each instance of the Wait on Notification function waits if
       the message in the notifier has a time stamp for the same time that the instance of the
       function last executed. If the message is new, then the function returns the message.

     When ignore previous is TRUE, the Wait on Notification function always waits for a
     new message, even if the message currently in the notifier is one it has never seen
       before.

           If you experience deadlock when you use this function repeatedly with different
        notifiers, use the Wait on Notification with Notifier History function to store
      timestamps for each individual notifier. This function prevents deadlock.

       This function does not remove the message from the notifier. Although a specific
       instance of the function returns a message only once, other instances of the function
       or to the Wait on Notification from Multiple function repeat the message until you call
       the Send Notification function with a new message.

1938   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1938 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1939 ordinal=1939 -->
## Functions

Functions

WaitWait onon NotificationNotification fromfrom MultipleMultiple FunctionFunction

Waits until at least one of the notifiers you specify receives a message.

When one of the notifiers receives a message, this function continues to execute. Use
the Send Notification function to send the message. If a notifier reference becomes
invalid, such as when another function closes it, this function stops waiting and
returns error code 1122. If the notifier does not contain a message, this function waits
until the notifier receives a message.


Inputs/Outputs

   •       notifiers —

     notifiers is an array of notifier references.

    Use the Obtain Notifier function to obtain a notifier reference.
   •      ignore previous (F) —

    ignore previous indicates whether to ignore messages that LabVIEW sends to the notifier before
       it calls this function.

       If TRUE and the notifier contains a message before you call this function, this function waits until
    the notifier receives another message. If FALSE (default) and the notifier contains a message
    before you call this function, this function continues to execute.
   •      timeout in ms (-1) —

    timeout in ms specifies the time, in milliseconds, that the function waits for the notifier to
    receive a message.

    The default is –1, which indicates never to time out.

       If the function waits timeout in ms and the notifier does not receive a message, timed out? is
    TRUE.

   •       error in (no error) —


                                                    © National Instruments 1939

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1939 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1940 ordinal=1940 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       notifiers out —

              notifiers out returns an array of the notifier references from which messages were received.

               •       notifications —

             notifications is an array of the last messages the notifiers receive.

             This data type changes to match the subtype of notifiers, unless the subtype is an array. If the
           subtype is an array, the data type becomes a cluster of arrays.
               •      timed out? —

           timed out? is TRUE if the notifier does not receive a message before the function times out or if
          an error occurs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Use the Wait on Notification function for a single notifier reference.

      Each unique instance of this function remembers the time stamp of the last message it
        receives. If this function receives only one message, the function stops remembering
      which message the time stamp refers to, and the only item filled in the notifiers array is
       the first element.

           If you experience deadlock when you use this function repeatedly with different
        notifiers, use the Wait on Notification from Multiple with Notifier History function to
       store time stamps for each individual notifier. This function prevents deadlock.

           If ignore previous is FALSE, each instance of the Wait on Notification from Multiple
       function determines if one or more notifier has a message newer than the time stamp
      most recently received by this function. If one or more of the notifiers has new
      messages, all messages are returned.

     When ignore previous is TRUE, this function always waits for a new message, even if
       the message currently in the notifier is one it has never seen before.

1940   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1940 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1941 ordinal=1941 -->
## Functions

Functions

This function does not remove the message from the notifier. Although a specific
instance of the function returns a message only once, other instances of the function
or to the Wait on Notification function repeat the message until you call the Send
Notification function with a new message.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Synchronization\Notifier\Wait on
   Multiple Notifiers.vi

AdvancedAdvanced NotifierNotifier WaitingWaiting

Use the Advanced Notifier Waiting functions to prevent dropped messages and other
problems when you use the functions repeatedly with different notifiers.


 Palette Object          Description

 Wait on Notification     Waits until a notifier receives a message. This function tracks the most
 with Notifier History     recent message and timestamp for each individual notifier when you use
 Function                  this function repeatedly with different notifiers.

 Wait on Notification                        Waits until a notifier within an array receives a message. This function from Multiple with
                          tracks the most recent message and timestamp for each individual
 Notifier History
                             notifier within an array.
 Function

WaitWait onon NotificationNotification withwith NotifierNotifier HistoryHistory
FunctionFunction

Waits until a notifier receives a message. This function tracks the most recent message
and timestamp for each individual notifier when you use this function repeatedly with
different notifiers.

                                                    © National Instruments 1941

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1941 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1942 ordinal=1942 -->
## Functions

Functions


      Inputs/Outputs

               •       notifier —

              notifier is a reference to a notifier.

           Use the Obtain Notifier function to obtain a notifier reference.
               •      ignore previous (F) —

            ignore previous indicates whether to ignore messages that LabVIEW sends to the notifier before
                   it calls this function.

                    If TRUE and the notifier contains a message before you call this function, this function waits until
            the notifier receives another message. If FALSE (default) and the notifier contains a message
            before you call this function, this function continues to execute.
               •      timeout in ms (-1) —

           timeout in ms specifies the time, in milliseconds, that the function waits for the notifier to
             receive a message.

          The default is –1, which indicates never to time out.

                    If the function waits timeout in ms and the notifier does not receive a message, timed out? is
           TRUE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       notifier out —

              notifier out returns notifier unchanged.

               •       notification —

             notification is the last message the notifier receives.

             This data type changes to match the subtype of notifier.
               •      timed out? —

1942   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1942 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1943 ordinal=1943 -->
## Functions

Functions


    timed out? is TRUE if the notifier does not receive a message before the function times out or if
    an error occurs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Each unique instance of this function remembers the timestamp of the most recent
message that each individual notifier receives.

Maintaining notifier history prevents dropped messages and other problems when you
use this function repeatedly with different notifiers. When the notifier receives a
message, this function continues to execute. Use the Send Notification function to
send the message. If a notifier reference becomes invalid when another function closes
it, the function stops waiting and returns error code 1122. If the notifier does not
contain a message, this function waits until the notifier receives a message.

Maintaining notifier history also causes this function to run slower than the Wait on
Notification function. The Wait on Notification function does not maintain notifier
history and might experience deadlock when you use it repeatedly with different
notifiers.

Use the Wait on Notification from Multiple with Notifier History function to handle an
array of notifier references.

If ignore previous is FALSE, each instance of the Wait on Notification with Notifier
History function waits if it has not received notification. The function also waits if the
timestamp of the current message is the same as when the instance of the function
last executed. If the message is new, then the function returns the message.

If ignore previous is TRUE, the Wait on Notification with Notifier History function
always waits for a new message, even if the message currently in the notifier is one the
function has never seen before.

This function does not remove the message from the notifier. Although a single
instance of the function returns a message only once, other instances of the function
or the Wait on Notification from Multiple function repeat the message until you call the


                                                    © National Instruments 1943

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1943 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1944 ordinal=1944 -->
## Functions

Functions

      Send Notification function with a new message.
   WaitWait onon NotificationNotification fromfrom MultipleMultiple withwith
    NotifierNotifier HistoryHistory FunctionFunction

       Waits until a notifier within an array receives a message. This function tracks the most
       recent message and timestamp for each individual notifier within an array.


      Inputs/Outputs

               •       notifiers —

              notifiers is an array of notifier references.

           Use the Obtain Notifier function to obtain a notifier reference.
               •      ignore previous (F) —

            ignore previous indicates whether to ignore messages that LabVIEW sends to the notifier before
                   it calls this function.

                    If TRUE and the notifier contains a message before you call this function, this function waits until
            the notifier receives another message. If FALSE (default) and the notifier contains a message
            before you call this function, this function continues to execute.
               •      timeout in ms (-1) —

           timeout in ms specifies the time, in milliseconds, that the function waits for the notifier to
             receive a message.

          The default is –1, which indicates never to time out.

                    If the function waits timeout in ms and the notifier does not receive a message, timed out? is
           TRUE.

               •       error in (no error) —


1944   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1944 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1945 ordinal=1945 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       notifiers out —

     notifiers out returns an array of the notifier references from which messages were received.

   •       notifications —

     notifications is an array of the last messages the notifiers receive.

    This data type changes to match the subtype of notifiers, unless the subtype is an array. If the
    subtype is an array, the data type becomes a cluster of arrays.
   •      timed out? —

    timed out? is TRUE if the notifier does not receive a message before the function times out or if
    an error occurs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Each unique instance of this function remembers the time stamp of the most recent
message for each individual notifier.

Maintaining notifier history prevents dropped messages and other problems when you
use this function repeatedly with different notifiers. When one of the notifiers in the
array receives a message, this function continues to execute. Use the Send Notification
function to send the message. If a notifier reference becomes invalid, such as when
another function closes it, this function stops waiting and returns error code 1122. If
the notifier does not contain a message, this function waits until a notifier within the
array receives a message.

Maintaining notifier history also causes this function to run slower than the Wait on
Notification from Multiple function, which does not maintain notifier history and might
experience deadlock when you use it repeatedly with different notifiers.

Use the Wait on Notification with Notifier History function for a single notifier
reference.


                                                    © National Instruments 1945

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1945 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1946 ordinal=1946 -->
## Functions

Functions

           If ignore previous is FALSE, each instance of the Wait on Notification from Multiple
       with Notifier History function waits if it has not received notification. If one or more of
       the notifiers have messages newer than the time stamp most recently received by this
       function, the function returns all messages. Otherwise, the function waits.

     When ignore previous is TRUE, this function always waits for a new message, even if
       the message currently in the notifier is one it has never seen before.

       This function does not remove the message from the notifier. Although a specific
       instance of the function returns a message only once, other instances of the function
       or the Wait on Notification function repeat the message until you call the Send
       Notification function with a new message.

    QueueQueue OperationsOperations

      Use the Queue Operations functions to create a queue for communicating data
      between sections of a block diagram or from another VI.

       Unlike the Notifier Operations functions, the Queue Operations functions buffer data.


         Palette                    Description        Object

        Obtain
       Queue     Returns a reference to a queue.
         Function

       Enqueue
        Element   Adds an element to the back of a queue.
         Function

        Preview
       Queue     Returns the element at the front of the queue without removing the element from the
        Element   queue.
         Function

        Get       Returns information about the current state of a queue, such as the number of elements
       Queue     currently in the queue.


1946   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1946 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1947 ordinal=1947 -->
## Functions

Functions


 Palette            Description
 Object

 Status
 Function

 Release
 Queue     Releases a reference to a queue.
 Function

          Adds an element to a queue. If no space is available in the queue, this function removes Lossy          an element from the front of the queue and discards the element to make space. Unlike Enqueue
           the Enqueue Element function, this function does not wait for room in the queue to Element         become available. Use the Obtain Queue function to set the maximum size of the Function           queue.

 Enqueue
 Element
 At          Adds an element to the front of a queue. Opposite
 End
 Function

 Dequeue
 Element   Removes an element from the front of a queue and returns the element.
 Function

 Flush
 Queue    Removes all elements from a queue and returns the elements as an array.
 Function

ObtainObtain QueueQueue FunctionFunction

Returns a reference to a queue.

Use this reference when calling other Queue Operations functions.


                                                    © National Instruments 1947

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1947 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1948 ordinal=1948 -->
## Functions

Functions

      Inputs/Outputs

               •     max queue size (-1, unlimited) —

         max queue size is the maximum number of elements you want the queue to hold.

          The default is –1, specifying that the queue can hold an unlimited number of elements.

                    If a queue reaches max queue size, the Enqueue Element or Enqueue Element at Opposite End
             functions wait until the Dequeue Element or Flush Queue functions remove elements from the
           queue.

                    If a queue with the same name exists, LabVIEW ignores this input and uses the size from the
              existing queue.

               Note (Real-Time Module) max queue size preallocates the specified number of
                   elements in the queue of scalar data types when running on an RT target.

               Note When not running on an RT target, max queue size only limits the number of
                   elements in the queue and does not preallocate the queue. To preallocate memory
                        for a queue, enqueue that number of elements and then flush the queue. The space
                    remains allocated for further use of the queue. Refer to the Details section for more
                     information on memory allocation for queues.

               •     name (unnamed) —

         name contains the name of the queue that you want to obtain or create.

          The default is an empty string to create an unnamed queue.
               •      element data type —

           element data type is the type of data that you want the queue to contain.

           You can wire any data type to this input.
               •      create if not found? (T) —

            create if not found? specifies whether you want to create a new queue if one with the same
         name as name does not exist.

                    If TRUE (default), the function creates a queue if one with the same name does not exist.
               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


1948   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1948 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1949 ordinal=1949 -->
## Functions

Functions


    standard error in functionality.

   •     queue out —

    queue out is a reference to the existing queue or the new queue created by this function.

   •      created new? —

    created new? is TRUE if the function created a new queue.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


When you enqueue and dequeue resizable data types, such as paths, strings and
arrays, you do not affect the memory used by queues. Queues transfer data, but do not
generate copies of the data. Use the Lossy Enqueue Element function if you are
concerned that elements waiting to enter an already-full queue might cause jitter in a
deterministic loop.

Use named queues to pass data between two sections of a block diagram or between
two VIs in the same application instance. If you do not wire name, the function creates
a new, unnamed queue reference. If you wire name, the function searches for an
existing queue with the same name and returns a new reference to the existing queue.
If a queue with the same name does not already exist and create if not found? is TRUE,
the function creates a new, named queue reference.

If you use the Obtain Queue function to return a reference to a named queue inside a
loop, LabVIEW creates a new reference to the named queue each time the loop
iterates. If you use Obtain Queue in a tight loop, LabVIEW slowly increases how much
memory it uses because each new reference uses an additional four bytes. These bytes
are released automatically when the VI stops running. However, in a long-running
application it may appear as if LabVIEW is leaking memory since the memory usage
keeps increasing. To prevent this unintended memory allocation, use the Release
Queue function in the loop to release the queue reference for each iteration.

This function might return error codes 1, 2, 1094, 1100, 1491, or 1548.


                                                    © National Instruments 1949

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1949 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1950 ordinal=1950 -->
## Functions

Functions

           Note

             You cannot use queues or named queues to communicate across application
               instances. If you attempt to communicate with a named queue in another
               application instance, LabVIEW does not return an error but you might not
               receive the expected results.

                       If you obtain a queue reference in one application instance, you cannot use
               that queue reference in another application instance. If you attempt to use a
            queue reference in another application instance, LabVIEW returns error 1491.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Synchronization\Queue\Queue Overflow and
        Underflow.vi

     EnqueueEnqueue ElementElement FunctionFunction

      Adds an element to the back of a queue.


      Inputs/Outputs

               •     queue —

          queue is a reference to a queue.

           Use the Obtain Queue function to obtain a queue reference.
               •      element —

           element is the element you want to add to the back of the queue.

             This data type changes to match the subtype of queue.

1950   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1950 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1951 ordinal=1951 -->
## Functions

Functions

   •      timeout in ms (-1) —

    timeout in ms specifies the time, in milliseconds, that the function waits for available space in
    the queue if the queue is full.

    The default is –1, indicating never to time out.

       If the function waits timeout in ms and the queue remains full, timed out? is TRUE.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     queue out —

    queue out returns the reference to the queue unchanged.

   •      timed out? —

    timed out? returns TRUE if space in the queue did not become available before the function
    times out. timed out? also returns TRUE if this function encounters an error.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If the queue is full, the function waits timeout in ms before timing out. If space
becomes available in the queue during the wait, the function inserts the element and
timed out? is FALSE. If queue becomes invalid such as when you release the queue
reference, the function stops waiting and returns error code 1122. Use the Obtain
Queue function to set the maximum size of the queue.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Synchronization\Queue\Queue Overflow and
   Underflow.vi


                                                    © National Instruments 1951

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1951 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1952 ordinal=1952 -->
## Functions

Functions

      PreviewPreview QueueQueue ElementElement FunctionFunction

       Returns the element at the front of the queue without removing the element from the
      queue.


      Inputs/Outputs

               •     queue —

          queue is a reference to a queue.

           Use the Obtain Queue function to obtain a queue reference.
               •      timeout in ms (-1) —

           timeout in ms specifies the time, in milliseconds, that the function waits for an element to
          become available in the queue if the queue is empty.

          The default is –1, indicating never to time out.

                    If the function waits timeout in ms and the queue remains empty, timed out? is TRUE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     queue out —

          queue out returns the reference to the queue unchanged.

               •      element —

           element is the element at the front of the queue.

             This data type changes to match the subtype of queue.
               •      timed out? —

           timed out? returns TRUE if an element did not become available in the queue before the


1952   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1952 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1953 ordinal=1953 -->
## Functions

Functions


    function timed out. timed out? also returns TRUE if this function encounters an error.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use the Dequeue Element function to return the element at the front of the queue and
remove it from the queue. If the queue is empty, the function waits timeout in ms
before timing out. If an element becomes available in the queue during the wait, the
function returns the element and timed out? is FALSE. If queue becomes invalid (for
example, the queue reference is released), the function stops waiting and returns error
code 1122.

GetGet QueueQueue StatusStatus FunctionFunction

Returns information about the current state of a queue, such as the number of
elements currently in the queue.

You also can use this function to verify that queue is a valid queue refnum. If queue is
not a valid queue refnum, the function returns error code 1.


Inputs/Outputs

   •     queue —

    queue is a reference to a queue.

    Use the Obtain Queue function to obtain a queue reference.
   •      return elements? (F) —


                                                    © National Instruments 1953

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1953 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1954 ordinal=1954 -->
## Functions

Functions


            return elements? indicates whether to return the elements in the queue.

                    If FALSE (default), the function does not return the elements in the queue.
               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     max queue size —

         max queue size is the maximum number of elements the queue can contain. If max queue size
                is –1, the queue can contain any number of elements.

               Note max queue size only limits the number of elements in the queue. It does not
                      preallocate that number of elements in the queue.

               •     queue name —

          queue name is the name of the queue.

               •     queue out —

          queue out returns the reference to the queue unchanged.

               •      # pending remove —

           # pending remove is the number of Dequeue Element or Preview Queue Element functions
             currently waiting to remove an element from the queue.

             Refer to the Dequeue Element and Preview Queue Element functions for more information.
               •      # pending insert —

           # pending insert is the number of functions currently waiting to insert an element in the queue.

           Use the Enqueue Element or Enqueue Element at Opposite End functions to insert an element in
            the queue.

                    If the max queue size is –1, # pending insert is 0.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      # elements in queue —

1954   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1954 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1955 ordinal=1955 -->
## Functions

Functions


    # elements in queue returns the current number of elements in the queue.

   •      elements —

    elements returns all the elements currently in the queue, but does not remove them from the
    queue.

       If return elements? is FALSE, this array is empty. This data type changes to match the subtype of
    queue.

ReleaseRelease QueueQueue FunctionFunction

Releases a reference to a queue.


Inputs/Outputs

   •     queue —

    queue is a reference to a queue.

    Use the Obtain Queue function to obtain a queue reference.
   •       force destroy? (F) —

    force destroy? indicates whether to destroy the queue.

       If FALSE (default) and you want to destroy the queue, either call the Release Queue function a
   number of times equal to the number of times you obtained a reference to the queue or stop all
     VIs using the queue reference. If TRUE, the function destroys the queue and you do not have to
     call the function multiple times or stop all VIs using the queue reference. Destroying the queue
     invalidates all references to the queue.
   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •     queue name —

                                                    © National Instruments 1955

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1955 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1956 ordinal=1956 -->
## Functions

Functions


          queue name is the name of the queue.

               •      remaining elements —

           remaining elements is the array of elements that were in the queue before the function released
            the queue.

          The first element in the array is the element from the front of the queue and the last element in
            the array is the element from the back of the queue.

             This data type changes to match the subtype of queue.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      You can use the Obtain Queue function to obtain a reference to the same queue with
       the same name multiple times. To destroy a queue, call the Release Queue function a
      number of times equal to the number of times you obtained a reference to the queue
       or stop all VIs using the queue reference.

           If force destroy? is TRUE, this function releases all references to the queue and
       destroys the queue.

      Any Enqueue Element, Enqueue Element at Opposite End, Preview Queue Element,
      and Dequeue Element functions waiting on the queue time out and return error code
       1122.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Synchronization\Queue\Queue Overflow and
        Underflow.vi

      LossyLossy EnqueueEnqueue ElementElement FunctionFunction

      Adds an element to a queue. If no space is available in the queue, this function
      removes an element from the front of the queue and discards the element to make

1956   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1956 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1957 ordinal=1957 -->
## Functions

Functions

space. Unlike the Enqueue Element function, this function does not wait for room in
the queue to become available. Use the Obtain Queue function to set the maximum
size of the queue.


Inputs/Outputs

   •     queue —

    queue is a reference to a queue. Use the Obtain Queue function to obtain a queue reference.

   •      element —

    element is the element you want to add to the back of the queue. This data type changes to
    match the subtype of queue.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     queue out —

    queue out is a reference to the existing queue.

   •      overflow element —

    overflow element is the element LabVIEW removed from the front of the queue if the queue was
      full.

   •      overflow? —

    overflow? returns TRUE if the queue was full and LabVIEW removed an element to create space.
    overflow? returns FALSE if the queue accepted the element and did not remove an element to
   make space.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1957

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1957 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1958 ordinal=1958 -->
## Functions

Functions

     EnqueueEnqueue ElementElement AtAt OppositeOpposite EndEnd FunctionFunction

      Adds an element to the front of a queue.


      Inputs/Outputs

               •     queue —

          queue is a reference to a queue.

           Use the Obtain Queue function to obtain a queue reference.
               •      element —

           element is the element you want to add to the front of the queue.

             This data type changes to match the subtype of queue.
               •      timeout in ms (-1) —

           timeout in ms specifies the time, in milliseconds, that the function waits for available space in
            the queue if the queue is full.

          The default is –1, indicating never to time out.

                    If the function waits timeout in ms and the queue remains full, timed out? is TRUE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     queue out —

          queue out returns the reference to the queue unchanged.

               •      timed out? —

           timed out? returns TRUE if space in the queue did not become available before the function
            times out. timed out? also returns TRUE if this function encounters an error.


1958   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1958 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1959 ordinal=1959 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This function is similar to the Enqueue Element function. If the queue is full, the
function waits timeout in ms before continuing. If queue becomes invalid (for
example, the queue reference is released), the function stops waiting and returns error
code 1122.

Queues typically use a first-in-first-out flow of data. In rare situations, you might want
to interrupt this normal flow of data by adding an element to the front of the queue.
After you add an element to the front of a queue, the next Dequeue Element function
you call removes the element you added to the front. For example, you could use this
function if you want to use the queue as a stack structure or add high-priority
elements to the front of the queue.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Synchronization\Queue\Queue Stack Maze
   Solver.vi

DequeueDequeue ElementElement FunctionFunction

Removes an element from the front of a queue and returns the element.

If the queue is empty, the function waits timeout in ms before timing out. If an
element becomes available in the queue during the wait, the function removes and
returns the element and timed out? is FALSE. If queue becomes invalid (for example,
the queue reference is released), the function stops waiting and returns error code
1122.


                                                    © National Instruments 1959

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1959 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1960 ordinal=1960 -->
## Functions

Functions

      Inputs/Outputs

               •     queue —

          queue is a reference to a queue.

           Use the Obtain Queue function to obtain a queue reference.

               •      timeout in ms (-1) —

           timeout in ms specifies the time, in milliseconds, that the function waits for an element to
          become available in the queue if the queue is empty.

          The default is –1, indicating never to time out.

                    If the function waits timeout in ms and the queue remains empty, timed out? is TRUE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     queue out —

          queue out returns the reference to the queue unchanged.

               •      element —

           element is the element at the front of the queue.

             This data type changes to match the subtype of queue.

               •      timed out? —

           timed out? returns TRUE if an element did not become available in the queue before the
             function timed out. timed out? also returns TRUE if this function encounters an error.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

1960   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1960 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1961 ordinal=1961 -->
## Functions

Functions

  • labview\examples\Synchronization\Queue\Queue Overflow and
   Underflow.vi

FlushFlush QueueQueue FunctionFunction

Removes all elements from a queue and returns the elements as an array.

This function does not release the queue reference. Use the Release Queue function to
release the reference.


Inputs/Outputs

   •     queue —

    queue is a reference to a queue.

    Use the Obtain Queue function to obtain a queue reference.
   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     queue out —

    queue out returns the reference to the queue unchanged.

   •      remaining elements —

    remaining elements is an array of elements removed from the queue.

    The first element in the array is the element from the front of the queue and the last element in
    the array is the element from the back of the queue.

    This data type changes to match the subtype of queue.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1961

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1961 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1962 ordinal=1962 -->
## Functions

Functions

     SemaphoreSemaphore

      Use the Semaphore VIs to limit the number of tasks that can simultaneously operate
      on a shared (protected) resource. A protected resource or critical section of code might
       include writing to global variables or communicating with external instruments.

      You can use the Semaphore VIs to synchronize two or more separate, parallel tasks so
       that only one task at a time executes a critical section of code protected by a common
      semaphore. In particular, use these VIs when you want certain VIs or parts of a block
      diagram to wait until another VI or part of a block diagram is finished with the
       execution of a critical section.


         Palette Object   Description

        Obtain                         Obtains a reference to an existing semaphore or creates a new semaphore and       Semaphore
                          returns a reference to that semaphore.         Reference

         Acquire                         Acquires access to a semaphore.       Semaphore


         Release         Releases access to a semaphore. If the Acquire Semaphore VI is waiting for the
       Semaphore     semaphore this VI releases, it stops waiting and continues execution.

         Release
       Semaphore      Releases a reference to a semaphore.
         Reference

        Get Semaphore
                         Returns current status information of a semaphore.
         Status

        Not A
                         Returns TRUE if semaphore is not a valid semaphore refnum.
       Semaphore


1962   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1962 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1963 ordinal=1963 -->
## Functions

Functions

ObtainObtain SemaphoreSemaphore ReferenceReference

Obtains a reference to an existing semaphore or creates a new semaphore and returns
a reference to that semaphore.

Use this VI in conjunction with the other Semaphore VIs to implement a semaphore in
LabVIEW.


Inputs/Outputs

   •     name (unnamed) —

   name contains the name of the semaphore you want to look up or create.

    The default is an empty string to create an unnamed semaphore. If you wire name, LabVIEW
    searches for an existing semaphore with the same name and returns a unique reference to the
     existing semaphore. If a semaphore with the same name does not already exist and create if not
    found is TRUE, LabVIEW creates a new, named semaphore and returns a unique reference to that
    semaphore.

   •       size (1) —

     size specifies how many tasks can acquire the semaphore at the same time. If a named
    semaphore already exists, wiring a value to this parameter does not resize the semaphore.

     size must be greater than or equal to 1. The default is 1.

   •      create if not found (T) —

    create if not found specifies whether you want to create a new semaphore if one with that name
    does not exist.

    The default is TRUE, which specifies that LabVIEW creates a semaphore if the semaphore does
    not exist. If create if not found is FALSE and LabVIEW cannot find a semaphore with the name
    you specify, LabVIEW returns error code 1534.

   •       error in (no error) —


                                                    © National Instruments 1963

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1963 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1964 ordinal=1964 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     semaphore —

          semaphore is a reference to an existing or newly created semaphore.

                    If you use this VI to obtain multiple references to the same named semaphore, each reference
          number is unique.

               •      created new —

            created new is TRUE if the VI created a new semaphore.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      You cannot use semaphores to communicate between LabVIEW application instances.
           If you obtain a reference to a semaphore in one application instance, you cannot use
       that semaphore reference in another application instance.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Synchronization\Semaphore\Simple
        Semaphore.vi

      AcquireAcquire SemaphoreSemaphore

       Acquires access to a semaphore.

      Use this VI in conjunction with the other Semaphore VIs to implement a semaphore in
      LabVIEW.


1964   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1964 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1965 ordinal=1965 -->
## Functions

Functions

Inputs/Outputs

   •     semaphore —

    semaphore is a reference to a semaphore.

   •     ms timeout (-1) —

   ms timeout specifies how many milliseconds the function should wait for the semaphore to
   become available.

    The default is -1, indicating never to time out.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •     semaphore out —

    semaphore out has the same value as semaphore.

   •      timed out —

    timed out is TRUE if the semaphore did not become available before the function timed out or if
    an error occurred.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If the semaphore is already acquired by the maximum number of tasks, the VI waits ms
timeout milliseconds before timing out. If the semaphore becomes available during
the wait, timed out is FALSE. If the semaphore does not become available or
semaphore is not valid, timed out is TRUE. The count on a semaphore is incremented
each time Acquire Semaphore executes, even if the task acquiring the semaphore has
already acquired it once.


                                                    © National Instruments 1965

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1965 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1966 ordinal=1966 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Synchronization\Semaphore\Simple
        Semaphore.vi

      ReleaseRelease SemaphoreSemaphore

       Releases access to a semaphore. If the Acquire Semaphore VI is waiting for the
      semaphore this VI releases, it stops waiting and continues execution.

      Use this VI in conjunction with the other Semaphore VIs to implement a semaphore in
      LabVIEW.


      Inputs/Outputs

               •     semaphore —

          semaphore is a reference to a semaphore.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •     semaphore out —

          semaphore out has the same value as semaphore.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1966   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1966 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1967 ordinal=1967 -->
## Functions

Functions

If the semaphore is currently unacquired, this VI returns error code 1111.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Synchronization\Semaphore\Simple
   Semaphore.vi

ReleaseRelease SemaphoreSemaphore ReferenceReference

Releases a reference to a semaphore.

Use this VI in conjunction with the other Semaphore VIs to implement a semaphore in
LabVIEW.


Inputs/Outputs

   •     semaphore —

    semaphore is a reference to a semaphore.

   •       force destroy? (F) —

    force destroy? specifies whether to destroy the semaphore.

       If FALSE (default), LabVIEW destroys the semaphore only if no other references to the semaphore
     exist. If TRUE, LabVIEW releases all references to the semaphore and destroys the semaphore.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •     semaphore name —


                                                    © National Instruments 1967

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1967 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1968 ordinal=1968 -->
## Functions

Functions


          semaphore name is the name of the semaphore.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


         All Acquire Semaphore VIs that are currently waiting on this reference to the
      semaphore time out immediately and return an error. This does not affect any Acquire
      Semaphore VIs that are waiting on a different reference to the same semaphore.
      However, if force destroy? is TRUE, all Acquire Semaphore VIs, including those that are
       waiting on a different reference to the semaphore, time out immediately and return an
        error.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Synchronization\Semaphore\Simple
        Semaphore.vi

      GetGet SemaphoreSemaphore StatusStatus

       Returns current status information of a semaphore.

      Use this VI in conjunction with the other Semaphore VIs to implement a semaphore in
      LabVIEW.


      Inputs/Outputs

               •     semaphore —


1968   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1968 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1969 ordinal=1969 -->
## Functions

Functions


    semaphore is a reference to a semaphore.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     name —

   name contains the name of the semaphore.

   •     semaphore out —

    semaphore out has the same value as semaphore.

   •      # available —

    # available contains the number of tasks that can acquire the semaphore at the current time.
    This number is always less than or equal to size.

   •      # waiting —

    # waiting is the number of Acquire Semaphore functions currently waiting to acquire the
    semaphore.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •       size —

     size contains the maximum number of tasks that can acquire the semaphore at a time.


NotNot AA SemaphoreSemaphore

Returns TRUE if semaphore is not a valid semaphore refnum.

Use this VI in conjunction with the other Semaphore VIs to implement a semaphore in
LabVIEW.


                                                    © National Instruments 1969

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1969 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1970 ordinal=1970 -->
## Functions

Functions


      Inputs/Outputs

               •     semaphore —

          semaphore is a reference to a semaphore.

               •      not a semaphore —

           not a semaphore is TRUE if semaphore is not a valid semaphore reference.

     RendezvousRendezvous

      Use the Rendezvous VIs to synchronize two or more separate, parallel tasks at specific
       points of execution. Each task that reaches the rendezvous waits until the specified
      number of tasks are waiting, at which point all tasks proceed with execution.


         Palette Object       Description

                           Looks up an existing rendezvous or creates a new rendezvous and returns a         Create Rendezvous
                            refnum.


        Wait at Rendezvous   Waits until a sufficient number of tasks have arrived at the rendezvous.


         Resize Rendezvous   Changes the size of rendezvous by size change and returns new size.


         Destroy Rendezvous  Destroys the specified rendezvous.


        Get Rendezvous
                             Returns current status information of a rendezvous.
         Status


        Not A Rendezvous    Returns TRUE if rendezvous is not a valid rendezvous refnum.


1970   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1970 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1971 ordinal=1971 -->
## Functions

Functions

CreateCreate RendezvousRendezvous

Looks up an existing rendezvous or creates a new rendezvous and returns a refnum.

You can use this refnum when calling other Rendezvous VIs.


Inputs/Outputs

   •     name (unnamed) —

   name contains the name of the rendezvous that you are looking up or creating.

    The default is an empty string to create an unnamed rendezvous. LabVIEW does not
    automatically release named rendezvous.

          Note A named rendezvous exists only as long as the top-level VI that first created the
          named rendezvous continues running. For example, if Application.vi has a
             subVI Subtask.vi, any named rendezvous created by Subtask.vi is cleaned up
          when Application.vi stops executing. You can use the same named rendezvous
               in any VI—even those not in the hierarchy of Application.vi—but the
            rendezvous ceases to exist when the Application.vi hierarchy shuts down.

   •       size (2) —

     size specifies how many tasks initially meet at the rendezvous to continue execution.

    The default is 2. If a named rendezvous already exists, wiring a value to size does not resize the
    rendezvous. Use the Resize Rendezvous to resize a named rendezvous.

   •      return existing (F) —

    return existing (F) specifies whether the rendezvous must already exist for this function to
    succeed.

    The default is FALSE, specifying that a rendezvous should be created if it does not exist. If return
     existing (F) is TRUE and a rendezvous with that name does not exist, the function returns an
     error.


                                                    © National Instruments 1971

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1971 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1972 ordinal=1972 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      rendezvous —

           rendezvous is a reference to an existing or newly created rendezvous.

               •      created new —

            created new is TRUE if the VI created a new rendezvous.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If name is specified, the VI first searches for an existing rendezvous with the same
     name and returns its refnum if it exists. If a named rendezvous with the same name
      does not already exist and return existing is FALSE, the VI creates a new rendezvous
      and returns its refnum. created new is TRUE if the VI creates a new rendezvous.

           Note You cannot use a rendezvous to communicate between LabVIEW
               application instance. If you create a rendezvous reference in one application
               instance, you cannot use that rendezvous reference in another application
               instance.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Synchronization\Rendezvous\Simple
        Rendezvous.vi

      WaitWait atat RendezvousRendezvous

       Waits until a sufficient number of tasks have arrived at the rendezvous.


1972   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1972 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1973 ordinal=1973 -->
## Functions

Functions


Inputs/Outputs

   •      rendezvous —

    rendezvous is a reference associated with a rendezvous.

   •     ms timeout (-1) —

   ms timeout specifies how many milliseconds the function should wait for other tasks to arrive at
    the rendezvous.

    The default is –1, indicating never to time out.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      rendezvous out —

    rendezvous out has the same value as rendezvous.

   •      timed out —

    timed out is TRUE if not enough tasks arrived before the function timed out or if an error
    occurred.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If the number of tasks, including the new one, waiting at rendezvous is less than the
rendezvous size, the VI waits ms timeout milliseconds before timing out. If enough
tasks arrive at the rendezvous during the wait, timed out is FALSE. If enough tasks do
not arrive or rendezvous is not valid, timed out is TRUE.

ResizeResize RendezvousRendezvous

Changes the size of rendezvous by size change and returns new size.

                                                    © National Instruments 1973

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1973 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1974 ordinal=1974 -->
## Functions

Functions


      Inputs/Outputs

               •      rendezvous —

           rendezvous is a reference associated with a rendezvous.

               •       size change (0) —

             size change specifies how many more tasks want to meet at the rendezvous.

          A negative size decreases the number of tasks. The default is 0 for no change in size.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      rendezvous out —

           rendezvous out has the same value as rendezvous.

               •     new size —

         new size is the new number of tasks meeting at the rendezvous.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      DestroyDestroy RendezvousRendezvous

       Destroys the specified rendezvous.

         All Wait at Rendezvous VIs that are currently waiting on this rendezvous time out
      immediately and return an error.


1974   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1974 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1975 ordinal=1975 -->
## Functions

Functions


Inputs/Outputs

   •      rendezvous —

    rendezvous is a reference associated with a rendezvous.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      rendezvous name —

    rendezvous name is the name of rendezvous.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Synchronization\Rendezvous\Simple
   Rendezvous.vi

GetGet RendezvousRendezvous StatusStatus

Returns current status information of a rendezvous.


                                                    © National Instruments 1975

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1975 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1976 ordinal=1976 -->
## Functions

Functions

      Inputs/Outputs

               •      rendezvous —

           rendezvous is a reference associated with a rendezvous.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     name —

         name contains the name of the rendezvous.

               •      rendezvous out —

           rendezvous out has the same value as rendezvous.

               •      # waiting —

           # waiting is the number of Wait at Rendezvous functions currently waiting at the rendezvous.

               •       size —

             size is the number of tasks meeting at the rendezvous.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      NotNot AA RendezvousRendezvous

       Returns TRUE if rendezvous is not a valid rendezvous refnum.


      Inputs/Outputs

               •      rendezvous —


1976   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1976 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1977 ordinal=1977 -->
## Functions

Functions


    rendezvous is a reference associated with a rendezvous.

   •      not a rendezvous —

    not a rendezvous is TRUE if rendezvous is not a valid rendezvous reference.

OccurrencesOccurrences

Use the Occurrences functions to control separate, synchronous activities.

In particular, use these functions when you want one VI or part of a block diagram to
wait until another VI or part of a block diagram finishes a task without forcing LabVIEW
to poll.

You can perform the same task using global variables, with one loop polling the global
variable until its value changes. However, global variables use more overhead because
the loop that waits uses execution time. With occurrences, the second loop becomes
idle and does not use processor time. When the first loop sets the occurrence, LabVIEW
activates the second loop and any other block diagrams that wait for the specified
occurrence.


 Palette Object         Description

 Generate Occurrence   Generates an occurrence that you can pass to the Wait on Occurrence and
 Function              Set Occurrence functions.

 Wait on Occurrence
                       Waits for the Set Occurrence function to set the given occurrence.
 Function

 Set Occurrence         Sets the specified occurrence. All nodes that are waiting for this occurrence
 Function              stop waiting.

Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 1977

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1977 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1978 ordinal=1978 -->
## Functions

Functions

            • labview\examples\Synchronization\Occurrence\Simple
        Occurrence.vi

      GenerateGenerate OccurrenceOccurrence FunctionFunction

       Generates an occurrence that you can pass to the Wait on Occurrence and Set
      Occurrence functions.

           Note National Instruments encourages you to use the Notifier Operations
               functions in place of occurrences for most operations.


      Inputs/Outputs

               •      occurrence —

            occurrence is the occurrence refnum that links Wait on Occurrence and Set Occurrence.


        Ordinarily, only one Generate Occurrence function is wired to any set of Wait on
      Occurrence and Set Occurrence functions. You can wire a Generate Occurrence
       function to any number of Wait on Occurrence and Set Occurrence functions. You do
       not have to have the same number of Wait on Occurrence and Set Occurrence
       functions.

       Unlike other Synchronization VIs, each Generate Occurrence function on a block
      diagram represents a single, unique occurrence. In this way, the Generate Occurrence
       function is similar to a constant. When a VI is running, every time a Generate
      Occurrence function executes, the function produces the same value. For example, if
      you place a Generate Occurrence function inside of a loop, the value produced by the
      Generate Occurrence function is the same for every iteration of the loop. If you place a
      Generate Occurrence function on the block diagram of a reentrant VI, the Generate
      Occurrence function produces a different value for each caller.


1978   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1978 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1979 ordinal=1979 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Synchronization\Occurrence\Simple
   Occurrence.vi

WaitWait onon OccurrenceOccurrence FunctionFunction

Waits for the Set Occurrence function to set the given occurrence.

      Note National Instruments encourages you to use the Notifier Operations
        functions in place of occurrences for most operations.


Inputs/Outputs

   •     ms timeout (-1) —

   ms timeout is the specified amount of time, in milliseconds, for occurrence to occur.

       If occurrence does not occur within the specified ms timeout, the function returns a value of
    TRUE. If ms timeout is –1 (default), the function does not time out unless the occurrence wired
    to this function is invalid. If occurrence is invalid, the function immediately returns TRUE for
    timed out, even if ms timeout is equal to –1 (default).

   •      occurrence —

    occurrence is the occurrence refnum that links Wait on Occurrence and Set Occurrence.

   •      ignore previous (T) —

       If ignore previous is TRUE (default) and another node has set the occurrence before this
    function began executing, the function ignores the previous occurrence and waits for another
    one.


                                                    © National Instruments 1979

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1979 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1980 ordinal=1980 -->
## Functions

Functions


         When ignore previous is FALSE, the function checks whether another node previously set an
            occurrence. If so, the function executes. However, the Wait on Occurrence function only
            processes one occurrence at a time and does not hold multiple previous occurrences in memory.

               •      timed out —

           timed out is TRUE if occurrence does not occur within the specified ms timeout or if occurrence
                is invalid, even if ms timeout is equal to –1.

                    If ms timeout is –1 and occurrence is valid, timed out is FALSE.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Synchronization\Occurrence\Simple
        Occurrence.vi

      SetSet OccurrenceOccurrence FunctionFunction

       Sets the specified occurrence. All nodes that are waiting for this occurrence stop
       waiting.

           Note National Instruments encourages you to use the Notifier Operations
               functions in place of occurrences for most operations.


      Inputs/Outputs

               •      occurrence —

            occurrence is the occurrence refnum that links Wait on Occurrence and Set Occurrence.


1980   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1980 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1981 ordinal=1981 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Synchronization\Occurrence\Simple
   Occurrence.vi

FirstFirst Call?Call? FunctionFunction

Indicates that a subVI or section of a block diagram is running for the first time. The
First Call? function returns TRUE only the first time you call it after you click the Run
button.

You can place the First Call? function in multiple locations within a VI. The function
returns TRUE the first time the section of the block diagram in which it is placed runs.


Inputs/Outputs

   •        First Call?: T/F —

     First Call? is TRUE if the subVI is running for the first time since you ran the entire VI.


This function is useful if you want to run a subVI or a section of a block diagram within
a loop or Case structure only once when the VI runs.

First Call? returns TRUE the first time the VI runs after the first top-level caller starts
running, such as when the Run button is clicked or the Run VI method executes. If a
second top-level caller calls the VI while the first top-level caller is still running, First
Call? does not return TRUE a second time. After all the top-level callers become idle
and a top-level caller starts again, First Call? returns TRUE the first time the VI runs
after the idle state. Reentrant VIs have an instance per data space. Therefore, a shared
reentrant VI returns TRUE for each data space instance the first time its top-level caller
calls it.


                                                    © National Instruments 1981

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1981 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1982 ordinal=1982 -->
## Functions

Functions

     SynchronizeSynchronize DataData FlowFlow

       Passes through the values of the input wires after the upstream code executes.

      Use this VI to synchronize multiple parallel code paths at a single point of data flow to
      ensure a certain execution order.


      Inputs/Outputs

               •      input 1 —

            input 1 specifies the value of the first wire.

             This input accepts any data type. The default data type is a variant.

               •      input 2 —

            input 2 specifies the value of the second wire.

             This input accepts any data type. The default data type is a variant.

               •      input 3 —

            input 3 specifies the value of the third wire.

             This input accepts any data type. The default data type is a variant.

               •      input 4 —

            input 4 specifies the value of the fourth wire.

             This input accepts any data type. The default data type is a variant.

               •      output 1 —

           output 1 returns the value of input 1.

               •      output 2 —


1982   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1982 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1983 ordinal=1983 -->
## Functions

Functions


    output 2 returns the value of input 2.

   •      output 3 —

    output 3 returns the value of input 3.

   •      output 4 —

    output 4 returns the value of input 4.

GraphicsGraphics && SoundSound

Use the Graphics & Sound VIs to create custom displays, import and export data from
graphics files, and play sounds.


 Palette            Description
 Object

 3D Graph           Use the 3D Graph Properties VIs to create 3D data displays. Properties

 Picture           Use the Picture Plots VIs to create graphical representations of data.
 Plots


           Use the Picture Functions VIs to create visual representations of data. Many of these
 Picture     picture VIs use clusters to define points and rectangles. The VIs related to drawing text
 Functions  use clusters and enumerations to describe the font choice and the positioning of the
               text.


 Graphics   Use the Graphics Formats VIs to retrieve or store image data in BMP, JPEG, or PNG
 Formats   image files.


                                                    © National Instruments 1983

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1983 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1984 ordinal=1984 -->
## Functions

Functions


         Palette                    Description
        Object

       Beep      Causes the system to issue an audible tone. (Windows Vista 64-bit) This VI might not
        (Windows) work correctly if use system alert? is FALSE.


       Sound     Use the Sound VIs to play sounds.


       3D Picture  Use the 3D Picture Control VIs to display graphical representations of objects in 3D
         Control     scenes.


    3D3D GraphGraph PropertiesProperties

      Use the 3D Graph Properties VIs to create 3D data displays.

           Note The 3D Graph Properties VIs are available on Windows only, because
              the ActiveX 3D graph is an ActiveX control, which is available only on
             Windows.


         Palette
                    Description
        Object

                      Plots a simple surface from z matrix. The x and y vectors cause the surface to shift in
       3D Surface  relation to the x and y planes. This VI accepts one 2D array and the two optional 1D
                       arrays.


       3D
                      Plots a surface in terms of x, y, and z surfaces. The VI has three 2D array or matrix inputs
         Parametric
                     that specify each of the x, y, and z planes.
         Surface


1984   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1984 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1985 ordinal=1985 -->
## Functions

Functions


 Palette            Description
 Object

            Describes a line in terms of x, y, and z points. This VI has three 1D array or vector inputs 3D Curve             that specify each point in the plot.


 Basic       Adjusts various properties of the plot, including the transparency, plot style, and
 Properties  coordinate system.


 Axes
             Adjusts the properties of the x-, y-, and z-axes, including scaling and inverting. Properties

 Grid
          Shows or hides the xy, xz, yz grids. Properties

 Projection             Adjusts the types of projections associated with the plot. Properties

 Convert            Converts LabVIEW colors to or from colors used by ActiveX.
 OLE Color


 Set Plots    Sets the number of plots that are available for a 3D graph control.


3D3D SurfaceSurface

Plots a simple surface from z matrix. The x and y vectors cause the surface to shift in
relation to the x and y planes. This VI accepts one 2D array and the two optional 1D
arrays.


                                                    © National Instruments 1985

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1985 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1986 ordinal=1986 -->
## Functions

Functions

      Inputs/Outputs

               •     3D graph —

          3D graph accepts the reference to the 3D control.

               •      x vector —

           x vector is a 1D array that describes the surface from z matrix in relation to the x plane.

               •      y vector —

           y vector is a 1D array that describes the surface from the z matrix in relation to the y plane.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array of data that determines the surface in relation to the z plane.

          The x and y vectors shift or skew the set of data in the z matrix.

               •       plot number (1) —

             plot number is the index into the list of plots from the properties of the 3D control.

          Add new plots by right-clicking the control and adjusting the properties. The default is the first
             plot from the list.

               •     3D graph out —

          3D graph out passes the reference to the 3D control out so that you can use it with other VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      x vector and y vector correspond to the two indexes for the z matrix 2D array. If the
      number of elements in x vector does not match the width of z matrix in the first
       dimension, and the number of elements in y vector does not match the width of z
       matrix in the second dimension, both x vector and y vector are ignored.

1986   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1986 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1987 ordinal=1987 -->
## Functions

Functions

The values of x vector and y vector specify where the corresponding point in the z
matrix should be located. The default values for x vector and y vector are 0, 1, 2, 3, and
so on. The first point in z matrix (index 0,0) is located at (x vector[0], y vector[0]), or
(0,0). If you change x vector to –1, 1, 2, 3, and so on, the first point in z matrix moves to
(–1,0).

3D3D ParametricParametric SurfaceSurface

Plots a surface in terms of x, y, and z surfaces. The VI has three 2D array or matrix
inputs that specify each of the x, y, and z planes.


Inputs/Outputs

   •     3D graph —

   3D graph accepts the reference to the 3D control.

   •      x matrix —

    x matrix is a 2D array of data that determines the surface in relation to the x plane.

   •      y matrix —

    y matrix is a 2D array of data that determines the surface in relation to the y plane.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      z matrix —

    z matrix is a 2D array of data that determines the surface in relation to the z plane.

    The x and y vectors shift or skew the set of data in the z matrix.


                                                    © National Instruments 1987

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1987 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1988 ordinal=1988 -->
## Functions

Functions

               •       plot number (1) —

             plot number is the index into the list of plots from the properties of the 3D control.

          Add new plots by right-clicking the control and adjusting the properties. The default is the first
             plot from the list.

               •     3D graph out —

          3D graph out passes the reference to the 3D control out so that you can use it with other VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     3D3D CurveCurve

       Describes a line in terms of x, y, and z points. This VI has three 1D array or vector inputs
       that specify each point in the plot.


      Inputs/Outputs

               •     3D graph —

          3D graph accepts the reference to the 3D control.

               •      x vector —

           x vector is a 1D array of data that contains the x coordinates of the curve.

               •      y vector —

           y vector is a 1D array of data that contains the y coordinates of the curve.

               •       error in (no error) —


1988   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1988 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1989 ordinal=1989 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      z vector —

    z vector is a 1D array of data that contains the z coordinates of the line or curve.

    The x and y vectors shift or skew the set of data in the z vector.

   •       plot number (1) —

    plot number is the index into the list of plots from the properties of the 3D control.

   Add new plots by right-clicking the control and adjusting the properties. The default is the first
     plot from the list.

   •     3D graph out —

   3D graph out passes the reference to the 3D control out so that you can use it with other VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D (ActiveX)\3D Curve Graph
   (ActiveX).vi

BasicBasic PropertiesProperties

Adjusts various properties of the plot, including the transparency, plot style, and
coordinate system.


                                                    © National Instruments 1989

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1989 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1990 ordinal=1990 -->
## Functions

Functions


      Inputs/Outputs

               •     3D graph —

          3D graph accepts the reference to the 3D control.

               •       plot style —

             plot style changes the way the data is plotted. The default is a surface plot.

               •       fast draw —

              fast draw determines if the surface is redrawn while it is rotated and zoomed or if it is displayed
            as points of data.

               •      transparency —

            transparency is a value from 0 to 100 that changes the transparency of the plot.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      coordinate system —

            coordinate system can be cwCartesian, cwCylindrical, or cwSpherical.

          The default is cwCartesian.

               •       plot number (1) —

             plot number is the index into the list of plots from the properties of the 3D control.

          Add new plots by right-clicking the control and adjusting the properties. The default is the first
             plot from the list.

               •     3D graph out —


1990   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1990 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1991 ordinal=1991 -->
## Functions

Functions


   3D graph out passes the reference to the 3D control out so that you can use it with other VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


AxesAxes PropertiesProperties

Adjusts the properties of the x-, y-, and z-axes, including scaling and inverting.


Inputs/Outputs

   •       invert x —

    invert x reverses the plot along the x plane.

   •       invert y —

    invert y reverses the plot along the y plane.

   •       invert z —

    invert z reverses the plot along the z plane.

   •     3D graph —

   3D graph accepts the reference to the 3D control.

   •      auto scale x —

    auto scale x enables autoscaling for the x plane.

   •      auto scale y —

                                                    © National Instruments 1991

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1991 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1992 ordinal=1992 -->
## Functions

Functions


           auto scale y enables autoscaling for the y plane.

               •      auto scale z —

           auto scale z enables autoscaling for the z plane.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       plot number (1) —

             plot number is the index into the list of plots from the properties of the 3D control.

          Add new plots by right-clicking the control and adjusting the properties. The default is the first
             plot from the list.

               •     3D graph out —

          3D graph out passes the reference to the 3D control out so that you can use it with other VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      GridGrid PropertiesProperties

      Shows or hides the xy, xz, yz grids.


      Inputs/Outputs

               •       grid smoothing —


1992   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1992 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1993 ordinal=1993 -->
## Functions

Functions


    grid smoothing allows the grids to be drawn with smooth lines.

   •     3D graph —

   3D graph accepts the reference to the 3D control.

   •      xy grid —

    xy grid shows the xy grid.

   •      xz grid —

    xz grid shows the xz grid.

   •      yz grid —

    yz grid shows the yz grid.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     3D graph out —

   3D graph out passes the reference to the 3D control out so that you can use it with other VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


ProjectionProjection PropertiesProperties

Adjusts the types of projections associated with the plot.

The plot can be projected onto the xy plane, xz plane, or yz plane.


                                                    © National Instruments 1993

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1993 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1994 ordinal=1994 -->
## Functions

Functions


      Inputs/Outputs

               •      coordinate system —

            coordinate system can be cwCartesian, cwCylindrical, or cwSpherical.

          The default is cwCartesian.

               •     3D graph —

          3D graph accepts the reference to the 3D control.

               •      xy projection —

           xy projection projects an image of the plot onto the xy plane.

               •      xz projection —

            xz projection projects an image of the plot onto the xz plane.

               •      yz projection —

            yz projection projects an image of the plot onto the yz plane.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     show projections only —

          show projections only allows only the projections to be shown.

               •       plot number (1) —

             plot number is the index into the list of plots from the properties of the 3D control.


1994   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1994 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1995 ordinal=1995 -->
## Functions

Functions


   Add new plots by right-clicking the control and adjusting the properties. The default is the first
     plot from the list.

   •     3D graph out —

   3D graph out passes the reference to the 3D control out so that you can use it with other VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


ConvertConvert OLEOLE ColorColor

Converts LabVIEW colors to or from colors used by ActiveX.

You can use the property page for the 3D graph to set all of the colors. Color conversion
is necessary for use with ActiveX Property Nodes.


Inputs/Outputs

   •       color in —

    color in is the color you want to convert.

   •       color out —

    color out is the converted color.


SetSet PlotsPlots

Sets the number of plots that are available for a 3D graph control.


                                                    © National Instruments 1995

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1995 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1996 ordinal=1996 -->
## Functions

Functions


      Inputs/Outputs

               •     3D graph —

          3D graph accepts the reference to the 3D control.

               •      # of plots(1) —

           # of plots sets the number of plots for a 3D control. It removes all of the plots that are currently
              in the graph and adds the number of plots. The default is one plot for a control.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     3D graph out —

          3D graph out passes the reference to the 3D control out so that you can use it with other VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

      PicturePicture PlotsPlots

      Use the Picture Plots VIs to create graphical representations of data.


         Palette
                        Description
        Object

         Polar Plot
                      Takes a picture and polar data and appends a picture that represents a polar graph
        with Point
                         of the data. This VI can represent polar data as points or lines between points.
        Options


1996   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1996 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1997 ordinal=1997 -->
## Functions

Functions


Palette               Description
Object

              Takes a picture and the data for a Smith plot and appends a picture that representsSmith Plot               the Smith plot of the data.


Smith Multi    Takes a picture and an array of Smith plots and appends a picture that represents
Plot           the superimposed Smith plots of the data.


Normalize     Takes data for a Smith plot and normalizes it, meaning that the data is scaled
Smith Plot      relative to a known value.


              Takes a picture and an array of points and appends a picture that represents an XYPlot XY
              graph of the data.


              Takes a picture and an array of plots and appends a picture of an XY graph of thePlot Multi-XY              data with the plots overlaid on the same graph.


Plot           Takes uniformly distributed data and a picture and creates a new picture that
Waveform      represents a waveform graph of the data.


              Takes a picture and an array of plots and appends a picture that represents theRadar Plot
               radar plot of the data.


Draw Legend   Takes a picture and adds a legend to the picture.


Calc Scale     Takes a specification for a Cartesian style scale and calculates the coordinates and
Specs          labels to use for the scale.


Draw Scale    Draws a scale onto a picture.


                                                    © National Instruments 1997

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1997 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1998 ordinal=1998 -->
## Functions

Functions


         Palette                        Description
        Object

                     Uses pixel and data ranges to determine scale factors such that (a * data value) + b       Map Setup                                is the pixel value that corresponds to that data value.


       Map Value to   Uses the domain value and the cluster returned by the Map Setup VI to determine a
          Pixel            pixel value corresponding to that domain value.


       Map Pixel to   Uses the pixel value and the cluster returned by the Map Setup VI to determine the
         Value        domain value corresponding to that pixel value.


       PolarPolar PlotPlot withwith PointPoint OptionsOptions

      Takes a picture and polar data and appends a picture that represents a polar graph of
       the data. This VI can represent polar data as points or lines between points.


      Inputs/Outputs

               •       [user-specified font] —

             [user-specified font] specifies the specific font characteristics for the text to draw.

          The VI ignores this input unless desired font is User-specified Font.

                     •      Font Name: —


1998   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1998 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1999 ordinal=1999 -->
## Functions

Functions


      Font Name specifies the font to use for the text.

          If you misspell the font name or specify a font that is not installed on the computer, the
      operating system selects a font.

      •       Size —

       Size specifies the size of the font in points.

      •       Strikeout? —

       Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
       strikeout.

      •        Italic? —

        Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

      •      Underline? —

      Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
       underlined.

      •      Outline? —

      Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

      •     Shadow? —

     Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

      •      Bold? —

      Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


•      desired font(Application) —

  desired font specifies the text font.

  0     User-specified Font
  1     Application Font


                                                   © National Instruments 1999

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1999 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2000 ordinal=2000 -->
## Functions

Functions


                    (default)
           2    System Font
           3     Dialog Font

               •       picture —

             picture is the picture to which you want to add the scale. The default is an empty picture.

               •      data array [mag, phase (deg)] —

           data array is an array of points, where each point is a cluster containing a magnitude and a
           phase in degrees that specifies the format and precision for the scale.

                     •      magnitude —

              magnitude is the straight line distance from the point to the center of the circle.

                     •      phase —

              phase is the angle (measured in degrees) between the positive x-axis and a straight line
               from the center of the circle to the point.


               •      top left point(0, 0) —

           top left point specifies in coordinates where to place the top-left corner of the image in the new
             picture.

                     •      x —

               x is the horizontal coordinate that increases to the right.

                     •      y —

               y is the vertical coordinate that increases to the bottom.


               •      dimensions (w,h) —

           dimensions specifies the top left point of the drawn bitmap.

                     •      width —


2000   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2000 -->

