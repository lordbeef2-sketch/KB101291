# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9501 ordinal=9501 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

IdentifierIdentifier

Sets or gets the property identifier of the property folder.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9501

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9501 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9502 ordinal=9502 -->
## Property and Method Reference

Property and Method Reference

   LongLong NameName

       Sets or gets the long name of the property folder.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

      LibraryDataLibraryData

      LVClassPropDefFolderLVClassPropDefFolder

       LVClassPropDefFolder Properties
   LVClassPropDefFolderLVClassPropDefFolder PropertiesProperties


9502   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9502 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9503 ordinal=9503 -->
## Property and Method Reference

Property and Method Reference


 Property          Description

                  Returns the long name of the property. The long name appears in a Property LongName               Node if you choose to display long names.

                  Returns the short name of the property. The short name is the name that ShortName                  appears in a Property Node by default.

                  Gets or sets the sorting order of the LabVIEW class property definition folder.
                   Properties are normally sorted by their long name, but this property can
                   override that for LabVIEW class properties. All properties with sort keys greater
                  than or equal to zero will be sorted according to their sort key in ascending
                     order. Properties with the same sort key will then be sorted by long name. If the
 SortKey            sort key is -1, the property will be placed at the end of the property list, sorted
                 by long name. The default sort key is -1. Setting the sort key to a non-negative
               number effectively moves that property to the top of the properties list and
                   leaves the other properties unchanged. Setting the sort key to -1 effectively
                     sorts the property normally among other properties that are sorted normally.
                   Properties are always sorted within their class.

                  Returns the unique data name of the property. You then can use this data name
 UniqueDataName with the Set Property method. The data name is never localized, but the author
                    of the class may change the name.

LongNameLongName

Returns the long name of the property. The long name appears in a Property Node if
you choose to display long names.

If the long name contains a colon, LabVIEW creates a submenu. The name to the left of
the colon is the main menu item, and the name to the right of the colon is the
submenu item. LabVIEW allows for multiple submenus.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 9503

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9503 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9504 ordinal=9504 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ShortNameShortName

       Returns the short name of the property. The short name is the name that appears in a
       Property Node by default.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9504   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9504 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9505 ordinal=9505 -->
## Property and Method Reference

Property and Method Reference

SortKeySortKey

Gets or sets the sorting order of the LabVIEW class property definition folder.
Properties are normally sorted by their long name, but this property can override that
for LabVIEW class properties. All properties with sort keys greater than or equal to zero
will be sorted according to their sort key in ascending order. Properties with the same
sort key will then be sorted by long name. If the sort key is -1, the property will be
placed at the end of the property list, sorted by long name. The default sort key is -1.
Setting the sort key to a non-negative number effectively moves that property to the
top of the properties list and leaves the other properties unchanged. Setting the sort
key to -1 effectively sorts the property normally among other properties that are
sorted normally. Properties are always sorted within their class.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

UniqueDataNameUniqueDataName

Returns the unique data name of the property. You then can use this data name with
the Set Property method. The data name is never localized, but the author of the class
may change the name.


                                                    © National Instruments 9505

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9505 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9506 ordinal=9506 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

       BuildSpecificationBuildSpecification

     SceneScene

      SceneTextureSceneTexture

       SceneTexture Methods

       SceneTexture Properties
   SceneTextureSceneTexture MethodsMethods


       Method                  Description

         Transformation:Clear
                            Removes any transformations previously applied to the texture.
         Transformation

         Transformation:Get
                                 Returns the Axis and Angle that define the rotation of the object.
         Rotation

         Transformation:Get       Returns the scale factors of the object.

9506   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9506 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9507 ordinal=9507 -->
## Property and Method Reference

Property and Method Reference


 Method                  Description

 Scale

 Transformation:Get                         Returns the translation of the object. Translation

                          Rotates the texture by the specified number of radians. This method Transformation:Rotate
                        performs a relative rotation from the current orientation of the texture.

                          Scales the texture by the given scale factors. This method performs a Transformation:Scale                              relative scale from the current position of the object.

 Transformation:Set       Rotates the texture by the specified number of radians. This method
 Rotation                performs an absolute rotation from the current position of the texture.

                          Scales the texture by the specified scaling factor. This method performs Transformation:Set Scale                      an absolute scale from the current position of the texture.

 Transformation:Set       Translates the texture by the specified vector. This method performs an
 Translation              absolute translation from the initial position of the texture.

                           Translates the texture by the specified vector. This method performs a Transformation:Translate                              relative translation from the initial position of the texture.

Transformation:ClearTransformation:Clear TransformationTransformation

Removes any transformations previously applied to the texture.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

                                                    © National Instruments 9507

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9507 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9508 ordinal=9508 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                             Yes

    Transformation:GetTransformation:Get RotationRotation

       Returns the Axis and Angle that define the rotation of the object.

     Parameters

              Data      Name          Required  Description               type

                                  Returns the x, y, and z coordinates for the axis around which the
         Axis             Yes                                      rotation occurs.


        Angle           Yes      The angle in radians of the rotation around the Axis.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


9508   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9508 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9509 ordinal=9509 -->
## Property and Method Reference

Property and Method Reference

Transformation:GetTransformation:Get ScaleScale

Returns the scale factors of the object.

Parameters

 Name  Data type   Required   Description

 Scale                Yes        The x, y, and z factors that define the scale of the object.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Transformation:GetTransformation:Get TranslationTranslation

Returns the translation of the object.


                                                    © National Instruments 9509

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9509 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9510 ordinal=9510 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name        Data type   Required   Description

         Translation                Yes        The x, y, and z factors that define the translation.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Transformation:RotateTransformation:Rotate

       Rotates the texture by the specified number of radians. This method performs a
        relative rotation from the current orientation of the texture.

     Parameters

      Name   Data type    Required     Description

        Angle                  Yes          Sets the angle in radians to use in the rotation.


9510   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9510 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9511 ordinal=9511 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Transformation:ScaleTransformation:Scale

Scales the texture by the given scale factors. This method performs a relative scale
from the current position of the object.

Parameters

 Name  Data type  Required   Description

 Scale               Yes       The s and t coordinates that define the scale of a 2D texture.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No


                                                    © National Instruments 9511

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9511 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9512 ordinal=9512 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Transformation:SetTransformation:Set RotationRotation

       Rotates the texture by the specified number of radians. This method performs an
       absolute rotation from the current position of the texture.

     Parameters

      Name   Data type    Required     Description

        Angle                  Yes          Sets the angle in radians to use in the rotation.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


9512   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9512 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9513 ordinal=9513 -->
## Property and Method Reference

Property and Method Reference

Transformation:SetTransformation:Set ScaleScale

Scales the texture by the specified scaling factor. This method performs an absolute
scale from the current position of the texture.

Parameters

 Name  Data type  Required   Description

 Scale               Yes       The s and t coordinates that define the scale of a 2D texture.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Transformation:SetTransformation:Set TranslationTranslation

Translates the texture by the specified vector. This method performs an absolute
translation from the initial position of the texture.


                                                    © National Instruments 9513

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9513 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9514 ordinal=9514 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                   Data      Name              Required  Description
                   type

                                  The s and t coordinates that define the translation this method         Translation          Yes                                         applies to the texture.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Transformation:TranslateTransformation:Translate

       Translates the texture by the specified vector. This method performs a relative
       translation from the initial position of the texture.

     Parameters

                   Data
      Name              Required  Description
                   type

         Translation          Yes      The s and t coordinates that define the translation this method


9514   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9514 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9515 ordinal=9515 -->
## Property and Method Reference

Property and Method Reference


            Data Name              Required  Description
            type

                                 applies to the texture.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SceneTextureSceneTexture PropertiesProperties


 Property       Description

 Apply Mode    Reads or writes how LabVIEW applies the texture to the 3D object.

               Reads or writes the RGBA color used to blend the texture you apply to the object.
 Blend Color
              Use this property when the Apply Mode property is set to With Blending.

               Reads or writes the method used to filter the texel colors applied to the geometry.
 Filter Mode
                  Different values affect the quality and speed of the texture mapping.

 Horizontal
              Read or writes how the texture is wrapped horizontally around a 3D object.
 Wrap Mode

 Image         Reads or writes the image data for a texture you apply to an object in a 3D scene.

 Transformation Reads or writes the transformation you apply to the texture. The transformation


                                                    © National Instruments 9515

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9515 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9516 ordinal=9516 -->
## Property and Method Reference

Property and Method Reference


        Property       Description

                     must be a 4x4 2D array of single precision numbers that represents the
                         transformation matrix you want to apply to the texture.

          Vertical Wrap                     Read or writes how the texture is vertically wrapped around a 3D object.       Mode

   ApplyApply ModeMode

      Reads or writes how LabVIEW applies the texture to the 3D object.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   BlendBlend ColorColor

      Reads or writes the RGBA color used to blend the texture you apply to the object. Use
        this property when the Apply Mode property is set to With Blending.


9516   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9516 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9517 ordinal=9517 -->
## Property and Method Reference

Property and Method Reference

Elements

 Name     Description

 Red        Indicates the red value. Valid values include 0 through 1.

 Green     Indicates the green value. Valid values include 0 through 1.

 Blue       Indicates the blue value. Valid values include 0 through 1.

 Alpha      Indicates the Alpha value. Valid values include 0 through 1.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

FilterFilter ModeMode

Reads or writes the method used to filter the texel colors applied to the geometry.
Different values affect the quality and speed of the texture mapping.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9517

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9517 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9518 ordinal=9518 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    HorizontalHorizontal WrapWrap ModeMode

      Read or writes how the texture is wrapped horizontally around a 3D object.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9518   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9518 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9519 ordinal=9519 -->
## Property and Method Reference

Property and Method Reference

ImageImage

Reads or writes the image data for a texture you apply to an object in a 3D scene.

Elements

 Name     Description

 Image           Reserved for future use. Type

            Specifies the color depth of the image, which is the number of bits to use to describe
 Image           the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per pixel. Depth
          Image Depth affects how LabVIEW interprets the values of Image and Colors.

         A 1-D array of bytes that describes the color of each pixel in the image in raster order.
          The value of Image Depth determines how LabVIEW interprets the value of this input.

                   If Image Depth is 24, each pixel has three bytes to describe its color. The first byte for
          each pixel describes the red value, the second byte describes the green value, and the
             third byte describes the blue value.

                   If Image Depth is 8, each pixel has one byte to describe its color. The value of each bit
 Image     corresponds to an element in Colors, which stores 32-bit RGB values where the most-
             significant byte is zero, followed in order by red, green, and blue values. Valid values
            include 0 through 255.

                   If Image Depth is 4, the behavior is similar to when Image Depth is 8 except valid values
             in image include 0 through 15.

                   If Image Depth is 1, any value of zero in Image corresponds to element 0 in Colors. All
           other values correspond to element 1 in Colors.

         An array of bytes in which each bit describes mask information for a pixel. The first byte
            describes the first eight pixels, the second byte describes the next eight pixels, and so
            on. If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is
 Mask
           empty, LabVIEW draws all pixels without transparency. If the array does not contain a bit
             for each pixel in the image, LabVIEW draws any pixels missing from the array without
            transparency.


                                                    © National Instruments 9519

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9519 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9520 ordinal=9520 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

                An array of RGB color values that correspond to the values in image. The value of Image
                 Depth determines how LabVIEW interprets the value of this input.

                               If Image Depth is 24, LabVIEW ignores this input.
         Colors                               If Image Depth is 8, the array can have 256 elements.

                               If Image Depth is 4, the array can have 16 elements.

                               If Image Depth is 1, the array can have 2 elements.

                A cluster that contains coordinates that describe the bounding rectangle in which you
                 want to draw the image. The VI clips the image to the width and height of the rectangle.
                 The bottom and right edges of the rectangle bounds do not contain image pixels.
                    Horizontal coordinates increase to the right, and vertical coordinates increase to the
                  bottom.
         Rectangle
                                • Left—The horizontal coordinate of the left edge of the rectangle.
                                • Top—The vertical coordinate of the top edge of the rectangle.
                                • Right—The horizontal coordinate of the right edge of the rectangle.
                                • Bottom—The vertical coordinate of the bottom edge of the rectangle.


     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


9520   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9520 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9521 ordinal=9521 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

TransformationTransformation

Reads or writes the transformation you apply to the texture. The transformation must
be a 4x4 2D array of single precision numbers that represents the transformation
matrix you want to apply to the texture.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

VerticalVertical WrapWrap ModeMode

Read or writes how the texture is vertically wrapped around a 3D object.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 9521

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9521 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9522 ordinal=9522 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

     SceneNodeSceneNode

      SceneNode Properties
   SceneNodeSceneNode PropertiesProperties


        Property            Description

      Name             Reads or writes the name of the node.

   NameName

      Reads or writes the name of the node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No


9522   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9522 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9523 ordinal=9523 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

SceneLightSceneLight

SceneLight Properties
SceneLightSceneLight PropertiesProperties


 Property              Description

                    Reads or writes the RGBA color value of the ambient lighting. Ambient light
                   comes from all directions equally and scatters in all directions equally after
 Ambient Color                                   it encounters the objects in the scene, such that a source for the light
                     cannot be distinguished.

                    Reads or writes whether the light is at an infinite distance from the scene. If
 At Infinity            TRUE, all light strikes the scene in parallel. Set this property to TRUE to
                        create a directional light.

                    Reads or writes the factors of attenuation applied to the light. Attenuation
 Attenuation          mimics how the intensity of light diminishes as you increase distance from
                      the light.
                         Indicates the constant factor of attenuation (kc) you apply to the light. The Attenuation:Constant
                       constant factor of attenuation does not change as distance from the light Attenuation
                         increases.
                         Indicates the linear factor of attenuation (kl) you apply to the light. The Attenuation:Linear
                          linear factor of attenuation drops in a linear manner as distance from the Attenuation
                           light increases.
                         Indicates the quadratic factor of attenuation (kq) you apply to the light. The Attenuation:Quadratic
                       quadratic factor of attenuation drops by the square of the distance from the Attenuation
                             light.


                                                    © National Instruments 9523

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9523 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9524 ordinal=9524 -->
## Property and Method Reference

Property and Method Reference


        Property              Description

                            Reads or writes the cutoff you apply to a spotlight to restrict the width of
                              the light. The value you wire to this property is equivalent to half the angle
         Cutoff                  of the actual spotlight. For example, if you want the spotlight to emit a 40
                             degree angle of light, set this property to 20. This property accepts values 0
                                to 90 and 180, where 180 represents no cutoff.

                            Reads or writes the RGBA color of the diffuse lighting. A diffuse light
         Diffuse Color           originates at a specific point and scatters equally across the surface of any
                         3D object it encounters.

                            Reads or writes the x, y, and z coordinates that define the direction of the         Direction                                       light.

                            Reads or writes the intensity distribution of the light. The intensity of the
                                     light changes as the direction of the light and the direction of the object
        Exponent                                        differ. This property accepts values 0 to 128, where 0 means uniform
                                   distribution.

                            Reads or writes the number you assign to the light. This property accepts
         Light Number                               values 0 to 7. The default is 0.

                            Reads or writes the x, y, and z coordinates that define the position of the         Position                                     light relative to its owning object.

                            Reads or writes the RGBA color value of the specular light. The light comes
                            from a specific point and bounces off the surface of a 3D object in a
        Specular Color         direction determined by the shape of the object. When specular light
                              encounters an object, the object acts as a mirror off which the light
                             bounces.

   AmbientAmbient ColorColor

      Reads or writes the RGBA color value of the ambient lighting. Ambient light comes
      from all directions equally and scatters in all directions equally after it encounters the
       objects in the scene, such that a source for the light cannot be distinguished.

     Elements

      Name     Description

       Red        Indicates the red value. Valid values include 0 through 1.


9524   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9524 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9525 ordinal=9525 -->
## Property and Method Reference

Property and Method Reference


 Name     Description

 Green     Indicates the green value. Valid values include 0 through 1.

 Blue       Indicates the blue value. Valid values include 0 through 1.

 Alpha      Indicates the Alpha value. Valid values include 0 through 1.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

AtAt InfinityInfinity

Reads or writes whether the light is at an infinite distance from the scene. If TRUE, all
light strikes the scene in parallel. Set this property to TRUE to create a directional light.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 9525

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9525 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9526 ordinal=9526 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    AttenuationAttenuation

      Reads or writes the factors of attenuation applied to the light. Attenuation mimics how
       the intensity of light diminishes as you increase distance from the light.

       Attenuation is determined using the following equation:


      where:

     kc = constant attenuation

     kl = linear attenuation

    kq = quadratic attenuation

   d= the distance between the position of the light and the vertex

     Elements

      Name       Description
        Constant    Indicates the constant factor of attenuation (kc) you apply to the light. The constant
         Attenuation  factor of attenuation does not change as distance from the light increases.

         Linear                       Indicates the linear factor of attenuation (kl) you apply to the light. The linear factor of         Attenuation

9526   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9526 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9527 ordinal=9527 -->
## Property and Method Reference

Property and Method Reference


 Name       Description

             attenuation drops in a linear manner as distance from the light increases.
 Quadratic    Indicates the quadratic factor of attenuation (kq) you apply to the light. The quadratic
 Attenuation  factor of attenuation drops by the square of the distance from the light.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Attenuation:ConstantAttenuation:Constant AttenuationAttenuation

Indicates the constant factor of attenuation (kc) you apply to the light. The constant
factor of attenuation does not change as distance from the light increases.

This property is an element of the Scene Light:Attenuation property.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 9527

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9527 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9528 ordinal=9528 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Attenuation:LinearAttenuation:Linear AttenuationAttenuation

       Indicates the linear factor of attenuation (kl) you apply to the light. The linear factor of
       attenuation drops in a linear manner as distance from the light increases.

       This property is an element of the Scene Light:Attenuation property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9528   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9528 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9529 ordinal=9529 -->
## Property and Method Reference

Property and Method Reference

Attenuation:QuadraticAttenuation:Quadratic AttenuationAttenuation

Indicates the quadratic factor of attenuation (kq) you apply to the light. The quadratic
factor of attenuation drops by the square of the distance from the light.

This property is an element of the Scene Light:Attenuation property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

CutoffCutoff

Reads or writes the cutoff you apply to a spotlight to restrict the width of the light. The
value you wire to this property is equivalent to half the angle of the actual spotlight.
For example, if you want the spotlight to emit a 40 degree angle of light, set this
property to 20. This property accepts values 0 to 90 and 180, where 180 represents no
cutoff.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9529

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9529 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9530 ordinal=9530 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    DiffuseDiffuse ColorColor

      Reads or writes the RGBA color of the diffuse lighting. A diffuse light originates at a
        specific point and scatters equally across the surface of any 3D object it encounters.

     Elements

      Name     Description

       Red        Indicates the red value. Valid values include 0 through 1.

        Green     Indicates the green value. Valid values include 0 through 1.

        Blue       Indicates the blue value. Valid values include 0 through 1.

        Alpha      Indicates the Alpha value. Valid values include 0 through 1.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes


9530   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9530 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9531 ordinal=9531 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DirectionDirection

Reads or writes the x, y, and z coordinates that define the direction of the light.

Elements

 Name     Description

 X        The x coordinate used to define the direction of the light.

 Y        The y coordinate used to define the direction of the light.

 Z        The z coordinate used to define the direction of the light.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 9531

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9531 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9532 ordinal=9532 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                                  Yes

   ExponentExponent

      Reads or writes the intensity distribution of the light. The intensity of the light changes
       as the direction of the light and the direction of the object differ. This property accepts
       values 0 to 128, where 0 means uniform distribution.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    LightLight NumberNumber

      Reads or writes the number you assign to the light. This property accepts values 0 to 7.
      The default is 0.

     Remarks

      The following table lists the characteristics of this property.


9532   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9532 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9533 ordinal=9533 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

PositionPosition

Reads or writes the x, y, and z coordinates that define the position of the light relative
to its owning object.

Elements

 Name   Description

 X       The x coordinate of the position of the light relative to its owning object.

 Y       The y coordinate of the position of the light relative to its owning object.

 Z       The z coordinate of the position of the light relative to its owning object.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 9533

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9533 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9534 ordinal=9534 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   SpecularSpecular ColorColor

      Reads or writes the RGBA color value of the specular light. The light comes from a
        specific point and bounces off the surface of a 3D object in a direction determined by
       the shape of the object. When specular light encounters an object, the object acts as a
       mirror off which the light bounces.

     Elements

      Name     Description

       Red        Indicates the red value. Valid values include 0 through 1.

        Green     Indicates the green value. Valid values include 0 through 1.

        Blue       Indicates the blue value. Valid values include 0 through 1.

        Alpha      Indicates the Alpha value. Valid values include 0 through 1.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

9534   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9534 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9535 ordinal=9535 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

SceneObjectSceneObject

SceneObject Methods

SceneObject Properties
SceneObjectSceneObject MethodsMethods


 Method                  Description

                      Adds a clip plane to the 3D scene. If you wire the Clip Plane output, you
 Clip Plane:Add Clip Plane                      must close the reference when you no longer need it.

 Clip Plane:Clip Plane
                         Returns the number of clip planes directly owned by this object. Count

 Clip Plane:Get Clip Plane  Gets the child clip plane owned by this object at the given index.

 Clip Plane:Get State      Returns the state of the clip plane applied to an object in a 3D scene.

 Clip Plane:Remove Clip
                     Removes the given clip plane if it is owned by this object. Plane

 Clip Plane:Set State       Sets a state for the clip plane.

                       Reads or writes the light you add to a 3D scene. If you wire the Light
 Light:Add Light
                          output, you must close the reference when you no longer need it.

 Light:Get Light           Gets the child light owned by this object at the given index.

 Light:Get State           Returns the state of the light.

 Light:Light Count         Returns the number of lights directly owned by this object.

 Light:Remove Light      Removes the given light owned by this object.

 Light:Set State            Sets a state for the light.

 Object:Add Object       Reads or writes a 3D object you add to a 3D scene. If you wire the Object


                                                    © National Instruments 9535

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9535 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9536 ordinal=9536 -->
## Property and Method Reference

Property and Method Reference


       Method                  Description

                                  output, you must close the reference when you no longer need it.

                                Takes a 3D scene reference and an object name and returns the first         Object:Find Object                                   object in the scene with a matching name.

         Object:Get Object        Returns a reference to a child object identified by the index you specify.

         Object:Object Count      Returns the number of children directly under the scene object.

        Object:Remove Object   Removes a child object from the 3D object.

         Set Billboard Params      Sets or updates parameters for billboarding.

                                    Specifies the drawable attribute to apply to a 3D object. Drawable
         Set Drawable              attributes include geometries and text. You must specify a drawable
                                     attribute for the object to appear in the 3D scene.

                            Removes the texture image associated with the object. If texturing is
        Texture:Remove Texture   enabled, the object inherits the texture of its parent after this method
                                   executes.

         Texture:Set Texture      Reads or writes the texture you apply to an object in a 3D scene.

                                   Clears any transformations applied to the object and sets the         Transformation:Clear
                                  transformation property to the identity matrix.

         Transformation:Get
                                 Returns the Axis and Angle that define the rotation of the object.         Rotation

         Transformation:Get
                                 Returns the scale factors of the object.         Scale

         Transformation:Get
                                 Returns the translation of the object.         Translation

                                  Rotates the object around the given Axis by the Angle. This method
         Transformation:Rotate
                                performs a relative rotation from the current position of the object.

                                  Scales the object by the specified scaling factor. This method performs a
         Transformation:Scale
                                       relative scale from the current position of the object.

         Transformation:Set       Rotates the object around the given Axis by the Angle. This method
         Rotation                performs an absolute rotation from the current position of the object.

                                  Scales the object by the specified scaling factor. This method performs
         Transformation:Set Scale
                             an absolute scale from the current position of the object.

         Transformation:Set       Translates the object by the specified vector. This method performs an
         Translation              absolute translation from the initial position of the object.


9536   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9536 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9537 ordinal=9537 -->
## Property and Method Reference

Property and Method Reference


 Method                  Description

                           Translates the object by the specified vector. This method performs a Transformation:Translate                              relative translation from the initial position of the object.

ClipClip Plane:AddPlane:Add ClipClip PlanePlane

Adds a clip plane to the 3D scene. If you wire the Clip Plane output, you must close the
reference when you no longer need it.

Parameters

 Name     Data type  Required  Description

 Clip Plane             Yes       The refnum input for the clip plane you add to the 3D scene.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

ClipClip Plane:ClipPlane:Clip PlanePlane CountCount

Returns the number of clip planes directly owned by this object.

                                                    © National Instruments 9537

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9537 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9538 ordinal=9538 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    ClipClip Plane:GetPlane:Get ClipClip PlanePlane

       Gets the child clip plane owned by this object at the given index.

     Parameters

      Name   Data type   Required   Description

         index                Yes          Specifies the position of the object you want to select.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

9538   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9538 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9539 ordinal=9539 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

ClipClip Plane:GetPlane:Get StateState

Returns the state of the clip plane applied to an object in a 3D scene.

Parameters

              Data Name               Required  Description              type

                             The number of the clip plane. The default is 0.

 Clip Plane
                       Yes            Note The number of the clip plane is not the same Number
                                         as the clip plane index.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes


                                                    © National Instruments 9539

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9539 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9540 ordinal=9540 -->
## Property and Method Reference

Property and Method Reference

    ClipClip Plane:RemovePlane:Remove ClipClip PlanePlane

      Removes the given clip plane if it is owned by this object.

     Parameters

      Name     Data type       Required        Description

          clip                         Yes              Specifies the clip for this object.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    ClipClip Plane:SetPlane:Set StateState

       Sets a state for the clip plane.


9540   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9540 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9541 ordinal=9541 -->
## Property and Method Reference

Property and Method Reference

Parameters

             Data Name               Required  Description
              type

                                   Specifies whether to enable the clip plane state.

                                       Inherit Value (default)—The clip plane inherits the clip plane                              0
 Clip Plane                             state of a parent object.                      Yes
 State                                   Off—Disables the clip plane so it does not apply to the
                              1                                       object.

                              2 On—Enables the clip plane.


                            The number of the clip plane. The default is 0.

 Clip Plane
                      Yes            Note The number of the clip plane is not the same as Number
                                         the clip plane index.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes


                                                    © National Instruments 9541

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9541 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9542 ordinal=9542 -->
## Property and Method Reference

Property and Method Reference

    Light:AddLight:Add LightLight

      Reads or writes the light you add to a 3D scene. If you wire the Light output, you must
       close the reference when you no longer need it.

     Parameters

      Name  Data type   Required   Description

         Light                Yes        The refnum input for the light you add to the 3D scene.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Light:GetLight:Get LightLight

       Gets the child light owned by this object at the given index.


9542   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9542 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9543 ordinal=9543 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name   Data type   Required   Description

 index                Yes          Specifies the position of the object you want to select.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

Light:GetLight:Get StateState

Returns the state of the light.

Parameters

 Name         Data type  Required   Description

 Light Number               Yes       The number that identifies the light. The default is 0.


                                                    © National Instruments 9543

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9543 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9544 ordinal=9544 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    Light:LightLight:Light CountCount

       Returns the number of lights directly owned by this object.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes


9544   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9544 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9545 ordinal=9545 -->
## Property and Method Reference

Property and Method Reference

Light:RemoveLight:Remove LightLight

Removes the given light owned by this object.

Parameters

 Name    Data type     Required      Description

 light                     Yes            Specifies the light owned by this object.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Light:SetLight:Set StateState

Sets a state for the light.


                                                    © National Instruments 9545

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9545 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9546 ordinal=9546 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                   Data      Name               Required  Description
                    type

                                            Specifies whether to enable the state of the light.

                                                Inherit Value (default)—The light inherits the state of a                                      0
         Light State            Yes          parent object.
                                      1 Off—Disables the light.

                                      2 On—Enables the light.


         Light                               Yes      The number that identifies the light. The default is 0.       Number

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   Object:AddObject:Add ObjectObject

      Reads or writes a 3D object you add to a 3D scene. If you wire the Object output, you


9546   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9546 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9547 ordinal=9547 -->
## Property and Method Reference

Property and Method Reference

must close the reference when you no longer need it.

Parameters

 Name   Data type   Required   Description

 Object              Yes       The refnum output for the object you add to the 3D scene.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Object:FindObject:Find ObjectObject

Takes a 3D scene reference and an object name and returns the first object in the scene
with a matching name.

Parameters

 Name     Data type      Required       Description

 Name                     Yes         Name of the object in the 3D scene.


                                                    © National Instruments 9547

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9547 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9548 ordinal=9548 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    Object:GetObject:Get ObjectObject

       Returns a reference to a child object identified by the index you specify.

     Parameters

              Data      Name         Required  Description               type

                             The index number of the child object for which you want to obtain the
         index          Yes                                     reference. The default is 0.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes


9548   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9548 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9549 ordinal=9549 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

Object:ObjectObject:Object CountCount

Returns the number of children directly under the scene object.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

Object:RemoveObject:Remove ObjectObject

Removes a child object from the 3D object.


                                                    © National Instruments 9549

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9549 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9550 ordinal=9550 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name   Data type   Required   Description

         Object               Yes        The reference to the child object you want to remove.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    SetSet BillboardBillboard ParamsParams

       Sets or updates parameters for billboarding.

     Parameters

                Data
      Name         Required  Description
                 type

      mode       No        Specifies the rotation behavior of the billboard.


9550   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9550 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9551 ordinal=9551 -->
## Property and Method Reference

Property and Method Reference


         Data Name         Required  Description
         type


                                  The billboard rotates about the specified axis input to                             Axial                                          face the viewer.

                              Full        The billboard rotates freely to face the viewer.

                    No                                  The billboard does not rotate to face the viewer.                           Billboarding


 position                   Specifies the list of positions to put an instance of the billboard.            No
 list                    LabVIEW draws an instance of the billboard at each point in the array.


                            Specifies the vector that describes the front of the billboard when the normal      No                            billboard is not rotated.


                            Specifies the axis around which the billboard rotates if you specify
 axis         No                    Axial for the modeinput.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

                                                    © National Instruments 9551

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9551 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9552 ordinal=9552 -->
## Property and Method Reference

Property and Method Reference

    SetSet DrawableDrawable

       Specifies the drawable attribute to apply to a 3D object. Drawable attributes include
       geometries and text. You must specify a drawable attribute for the object to appear in
       the 3D scene.

     Parameters

      Name       Data type    Required    Description

        Drawable                 Yes          Refers to the drawable object in the 3D scene.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   Texture:RemoveTexture:Remove TextureTexture

      Removes the texture image associated with the object. If texturing is enabled, the
       object inherits the texture of its parent after this method executes.


9552   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9552 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9553 ordinal=9553 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Texture:SetTexture:Set TextureTexture

Reads or writes the texture you apply to an object in a 3D scene.

Parameters

 Name    Data type   Required   Description

 Texture               Yes       The refnum input for the texture you apply to the object.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

                                                    © National Instruments 9553

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9553 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9554 ordinal=9554 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Transformation:ClearTransformation:Clear

       Clears any transformations applied to the object and sets the transformation property
       to the identity matrix.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Transformation:GetTransformation:Get RotationRotation

       Returns the Axis and Angle that define the rotation of the object.


9554   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9554 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9555 ordinal=9555 -->
## Property and Method Reference

Property and Method Reference

Parameters

       Data Name          Required  Description
       type

                           Returns the x, y, and z coordinates for the axis around which the Axis             Yes                              rotation occurs.


 Angle           Yes      The angle in radians of the rotation around the Axis.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Transformation:GetTransformation:Get ScaleScale

Returns the scale factors of the object.

Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 9555

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9555 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9556 ordinal=9556 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    Transformation:GetTransformation:Get TranslationTranslation

       Returns the translation of the object.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    Transformation:RotateTransformation:Rotate

       Rotates the object around the given Axis by the Angle. This method performs a relative
       rotation from the current position of the object.

9556   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9556 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9557 ordinal=9557 -->
## Property and Method Reference

Property and Method Reference

Parameters

       Data Name          Required  Description
       type

                            Sets the x, y, and z coordinates for the axis around which the rotation Axis             Yes                             occurs.


 Angle            Yes       Sets the angle in radians to use in the rotation.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Transformation:ScaleTransformation:Scale

Scales the object by the specified scaling factor. This method performs a relative scale
from the current position of the object.


                                                    © National Instruments 9557

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9557 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9558 ordinal=9558 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name  Data type  Required  Description

         Scale              Yes       The x, y, and z factors that define the scale to apply to the object.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Transformation:SetTransformation:Set RotationRotation

       Rotates the object around the given Axis by the Angle. This method performs an
       absolute rotation from the current position of the object.

     Parameters

              Data
      Name          Required  Description
               type

                                     Sets the x, y, and z coordinates for the axis around which the rotation
         Axis             Yes
                                      occurs.


9558   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9558 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9559 ordinal=9559 -->
## Property and Method Reference

Property and Method Reference


       Data Name          Required  Description
       type

 Angle            Yes       Sets the angle in radians to use in the rotation.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Transformation:SetTransformation:Set ScaleScale

Scales the object by the specified scaling factor. This method performs an absolute
scale from the current position of the object.

Parameters

 Name  Data type  Required  Description

 Scale              Yes       The x, y, and z factors that define the scale to apply to the object.


                                                    © National Instruments 9559

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9559 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9560 ordinal=9560 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Transformation:SetTransformation:Set TranslationTranslation

       Translates the object by the specified vector. This method performs an absolute
       translation from the initial position of the object.

     Parameters

                   Data      Name              Required  Description
                   type

                                  The x, y, and z factors that define the translation this method
         Translation          Yes
                                         applies to the object.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

9560   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9560 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9561 ordinal=9561 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Transformation:TranslateTransformation:Translate

Translates the object by the specified vector. This method performs a relative
translation from the initial position of the object.

Parameters

            Data Name              Required  Description
            type

                           The x, y, and z factors that define the translation this method Translation          Yes
                                 applies to the object.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

                                                    © National Instruments 9561

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9561 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9562 ordinal=9562 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                             Yes

   SceneObjectSceneObject PropertiesProperties


        Property                     Description

          Billboard:Axis                 Returns the axis that rotates if Billboard:Mode is axial.

                                       Sets the billboard mode for the 3D graph object. If the mode is No         Billboard:Mode                                          Billboarding, the object normal is set to default.

                                 The vector that describes the direction the object is facing before
         Billboard:Normal              the object rotates. LabVIEW ignores this property if the value of
                                      Billboard:Mode is No Billboarding.

         Billboard:Positions            Returns the positions of the objects to be billboarded.

                                  Reads or writes the draw bin in which you drop and store objects.
         Blending:Bin               The bin of an object affects the order in which the object appears
                              when you render the scene.

                                  Reads or writes the blend factor you apply to the color values of         Blending:Function:Destination                                      the currently stored pixels.

                                  Reads or writes the blend factor you apply to the color values of         Blending:Function:Source                                      the incoming fragment.

        Blending:Mode              Reads or writes if the color values you apply to a 3D object blend.

       Draw Style:Face Culling Mode  Reads or writes the culling method you apply to the object.

                                  Reads or writes how you determine the front-facing polygons of       Draw Style:Frontface Mode
                                      the 3D object.

                                  Reads or writes the width of lines drawn for the 3D object. Set the
       Draw Style:Line Width                                       value to -1 to inherit the line width of a parent object.

                                  Reads or writes the method you use to draw the 3D object. You can
       Draw Style:Mode
                                   choose from the following options:

                                  Reads or writes the size of the points you use to draw the
       Draw Style:Point Size          geometry. Set the value to -1 to inherit the point size of a parent
                                          object.

                                     Returns the drawable attribute applied to a 3D object. Drawable
        Drawable                       attributes include geometries and text. You must close this
                                          reference.

9562   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9562 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9563 ordinal=9563 -->
## Property and Method Reference

Property and Method Reference


Property                     Description

                           Reads or writes the RGBA color value of the fog. The elements of
                                   this property accept values 0 to 1, where 0 represents the absenceFog:Color                                of the red, green, or blue color and 1 represents a full saturation of
                             the current color.

                           Reads or writes the density of the fog you apply to the object. Valid
Fog:Density                   values include any non-negative, floating-point number between 0
                         and 1.

                           Reads or writes the point at which fog effects end. Fog grows
Fog:End                     denser as you move away from the camera but cuts off completely
                                at the specified fog end point.

                           Reads or writes the blending factor you use to apply fog to anFog:Function
                                 object.

                           Reads or writes the point at which the fog effects you apply to theFog:Start
                               object begin.

                          The multiplier on the line stipple pattern. LabVIEW uses each bitLine Stipple:Factor
                                 factor number of times. Valid values range from 1 to 256, inclusive.

Line Stipple:Mode             Sets the mode for line stipple.

                                  Bit pattern for line stippling. This property converts a 16-bit
                            unsigned integer into binary. For example, if you input the number
Line Stipple:Pattern              5, the bit pattern is 101. The bit pattern determines if the fragment
                                        is drawn on the graph. The Line Stipple:Factor property determines
                             the size of the fragment.

                           Reads or writes the RGBA color value of the object that the ambient
Material:Ambient                                    light affects. Materials only appear in lighted scenes.

                           Reads or writes how the 3D object reacts to light. Materials only
Material:Color Mode
                           appear in lighted scenes.

                           Reads or writes the RGBA color value of the lit object based on the
Material:Diffuse               angle between the orientation of the object and the direction of
                             the light source. Materials only appear in lighted scenes.

                           Reads or writes the RGBA color value of the emissive light of the
Material:Emission               object. Emissive light emanates from the object itself instead of an
                                external light source. Materials only appear in lighted scenes.

                           Reads or writes the size of the highlight that appears on the object
Material:Shininess          when light reflects specularly off the object. Shine can be a value
                           from 0−128. Materials only appear in lighted scenes.

                                                    © National Instruments 9563

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9563 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9564 ordinal=9564 -->
## Property and Method Reference

Property and Method Reference


        Property                     Description

                                  Reads or writes the RGBA color value of the object that represents
         Material:Specular             the reflection of specular light off of the object. Materials only
                                   appear in lighted scenes.

                                     Gets or sets the polygon offset factor. Changes to this property
         PolygonOffset:Factor          cause the polygon mode to change to off if it was inherited
                                          previously.

        PolygonOffset:Mode            Gets/sets the mode for polygon offset.

                                     Gets or sets the polygon offset units. Changes to this property
         PolygonOffset:Units           cause the polygon mode to change to off if it was inherited
                                          previously.

                                 Read or writes whether the object is anti-aliased to smooth lines          Specials:Anti-aliasing
                                and edges that appear jagged.

                                 Read or writes whether the vertex normals of the object         Specials:Autonormalizing
                                       automatically normalize to enhance rendering speed.

                                  Reads or writes whether the pixels of the 3D object pass the depth
         Specials:Depth Test               test. If the object passes the depth test, the incoming depth value
                                        replaces the value in the depth buffer when you render the scene.

         Specials:Lighting            Reads or writes whether a 3D object appears lit.

                                  Reads or writes whether a color-filled object appears shaded with
         Specials:Shade Model                                 one color or multiple colors.

                                  Reads or writes whether a 3D object appears with a texture. This
         Specials:Texturing                                      property must be set to On to apply textures to an object.

         Texture                    Reads the texture that you apply to the 3D object.

         Transformation              Reads or writes the transformation you apply to the object.

                                  Reads or writes how to specify the size of the view port you use to
        View Port:Mode
                                    view the scene.

                                  Reads or writes the position and size of a viewing port through
                                   which you can view a 3D object in the 3D picture control. The x and
                                     y values specify the coordinates within the view port at which
        View Port:View Port
                                  LabVIEW renders the object. The width and height specify the
                                    width and height of the view port. If you define a view port, objects
                                do not appear beyond the specified bounds of the view port.


9564   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9564 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9565 ordinal=9565 -->
## Property and Method Reference

Property and Method Reference

Billboard:AxisBillboard:Axis

Returns the axis that rotates if Billboard:Mode is axial.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Billboard:ModeBillboard:Mode

Sets the billboard mode for the 3D graph object. If the mode is No Billboarding, the
object normal is set to default.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

                                                    © National Instruments 9565

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9565 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9566 ordinal=9566 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    Billboard:NormalBillboard:Normal

      The vector that describes the direction the object is facing before the object rotates.
      LabVIEW ignores this property if the value of Billboard:Mode is No Billboarding.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    Billboard:PositionsBillboard:Positions

       Returns the positions of the objects to be billboarded.


9566   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9566 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9567 ordinal=9567 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Blending:BinBlending:Bin

Reads or writes the draw bin in which you drop and store objects. The bin of an object
affects the order in which the object appears when you render the scene.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No


                                                    © National Instruments 9567

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9567 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9568 ordinal=9568 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Blending:Function:DestinationBlending:Function:Destination

      Reads or writes the blend factor you apply to the color values of the currently stored
        pixels.

      The following source and destination color components are described as (Rs,Gs,Bs,
      As) for source components and (Rd,Gd,Bd,Ad) for destination components.

      The components have integer values between 0 and (kR,kG,kB,kA), where kR=2mR
        1, kG=2mG 1, kB=2mB 1, and kA=2mA 1.

     (mR,mG,mB,mA) is the number of bitplanes for each red, green, blue, and alpha
       value.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9568   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9568 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9569 ordinal=9569 -->
## Property and Method Reference

Property and Method Reference

Blending:Function:SourceBlending:Function:Source

Reads or writes the blend factor you apply to the color values of the incoming
fragment.

The following source and destination color components are described as (Rs,Gs,Bs,
As) for source components and (Rd,Gd,Bd,Ad) for destination components.

The components have integer values between 0 and (kR,kG,kB,kA), where kR=2mR
1, kG=2mG 1, kB=2mB 1, and kA=2mA 1.

(mR,mG,mB,mA) is the number of bitplanes for each red, green, blue, and alpha
value.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Blending:ModeBlending:Mode

Reads or writes if the color values you apply to a 3D object blend.

                                                    © National Instruments 9569

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9569 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9570 ordinal=9570 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   DrawDraw Style:FaceStyle:Face CullingCulling ModeMode

      Reads or writes the culling method you apply to the object.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


9570   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9570 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9571 ordinal=9571 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

DrawDraw Style:FrontfaceStyle:Frontface ModeMode

Reads or writes how you determine the front-facing polygons of the 3D object.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DrawDraw Style:LineStyle:Line WidthWidth

Reads or writes the width of lines drawn for the 3D object. Set the value to -1 to inherit
the line width of a parent object.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 9571

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9571 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9572 ordinal=9572 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   DrawDraw Style:ModeStyle:Mode

      Reads or writes the method you use to draw the 3D object. You can choose from the
       following options:

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   DrawDraw Style:PointStyle:Point SizeSize

      Reads or writes the size of the points you use to draw the geometry. Set the value to -1

9572   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9572 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9573 ordinal=9573 -->
## Property and Method Reference

Property and Method Reference

to inherit the point size of a parent object.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DrawableDrawable

Returns the drawable attribute applied to a 3D object. Drawable attributes include
geometries and text. You must close this reference.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No


                                                    © National Instruments 9573

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9573 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9574 ordinal=9574 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    Fog:ColorFog:Color

      Reads or writes the RGBA color value of the fog. The elements of this property accept
       values 0 to 1, where 0 represents the absence of the red, green, or blue color and 1
       represents a full saturation of the current color.

     Elements

      Name     Description

       Red        Indicates the red value. Valid values include 0 through 1.

        Green     Indicates the green value. Valid values include 0 through 1.

        Blue       Indicates the blue value. Valid values include 0 through 1.

        Alpha      Indicates the Alpha value. Valid values include 0 through 1.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


9574   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9574 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9575 ordinal=9575 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

Fog:DensityFog:Density

Reads or writes the density of the fog you apply to the object. Valid values include any
non-negative, floating-point number between 0 and 1.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Fog:EndFog:End

Reads or writes the point at which fog effects end. Fog grows denser as you move away
from the camera but cuts off completely at the specified fog end point.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 9575

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9575 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9576 ordinal=9576 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Fog:FunctionFog:Function

      Reads or writes the blending factor you use to apply fog to an object.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9576   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9576 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9577 ordinal=9577 -->
## Property and Method Reference

Property and Method Reference

Fog:StartFog:Start

Reads or writes the point at which the fog effects you apply to the object begin.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

LineLine Stipple:FactorStipple:Factor

The multiplier on the line stipple pattern. LabVIEW uses each bit factor number of
times. Valid values range from 1 to 256, inclusive.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

                                                    © National Instruments 9577

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9577 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9578 ordinal=9578 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    LineLine Stipple:ModeStipple:Mode

       Sets the mode for line stipple.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    LineLine Stipple:PatternStipple:Pattern

        Bit pattern for line stippling. This property converts a 16-bit unsigned integer into
       binary. For example, if you input the number 5, the bit pattern is 101. The bit pattern
      determines if the fragment is drawn on the graph. The Line Stipple:Factor property
      determines the size of the fragment.


9578   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9578 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9579 ordinal=9579 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Material:AmbientMaterial:Ambient

Reads or writes the RGBA color value of the object that the ambient light affects.
Materials only appear in lighted scenes.

Elements

 Name     Description

 Red        Indicates the red value. Valid values include 0 through 1.

 Green     Indicates the green value. Valid values include 0 through 1.

 Blue       Indicates the blue value. Valid values include 0 through 1.

 Alpha      Indicates the Alpha value. Valid values include 0 through 1.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9579

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9579 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9580 ordinal=9580 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Material:ColorMaterial:Color ModeMode

      Reads or writes how the 3D object reacts to light. Materials only appear in lighted
       scenes.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9580   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9580 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9581 ordinal=9581 -->
## Property and Method Reference

Property and Method Reference

Material:DiffuseMaterial:Diffuse

Reads or writes the RGBA color value of the lit object based on the angle between the
orientation of the object and the direction of the light source. Materials only appear in
lighted scenes.

Elements

 Name     Description

 Red        Indicates the red value. Valid values include 0 through 1.

 Green     Indicates the green value. Valid values include 0 through 1.

 Blue       Indicates the blue value. Valid values include 0 through 1.

 Alpha      Indicates the Alpha value. Valid values include 0 through 1.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Material:EmissionMaterial:Emission

Reads or writes the RGBA color value of the emissive light of the object. Emissive light

                                                    © National Instruments 9581

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9581 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9582 ordinal=9582 -->
## Property and Method Reference

Property and Method Reference

      emanates from the object itself instead of an external light source. Materials only
      appear in lighted scenes.

     Elements

      Name     Description

       Red        Indicates the red value. Valid values include 0 through 1.

        Green     Indicates the green value. Valid values include 0 through 1.

        Blue       Indicates the blue value. Valid values include 0 through 1.

        Alpha      Indicates the Alpha value. Valid values include 0 through 1.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Material:ShininessMaterial:Shininess

      Reads or writes the size of the highlight that appears on the object when light reflects
       specularly off the object. Shine can be a value from 0−128. Materials only appear in
       lighted scenes.


9582   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9582 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9583 ordinal=9583 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Material:SpecularMaterial:Specular

Reads or writes the RGBA color value of the object that represents the reflection of
specular light off of the object. Materials only appear in lighted scenes.

Elements

 Name     Description

 Red        Indicates the red value. Valid values include 0 through 1.

 Green     Indicates the green value. Valid values include 0 through 1.

 Blue       Indicates the blue value. Valid values include 0 through 1.

 Alpha      Indicates the Alpha value. Valid values include 0 through 1.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9583

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9583 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9584 ordinal=9584 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    PolygonOffset:FactorPolygonOffset:Factor

       Gets or sets the polygon offset factor. Changes to this property cause the polygon
     mode to change to off if it was inherited previously.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9584   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9584 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9585 ordinal=9585 -->
## Property and Method Reference

Property and Method Reference

PolygonOffset:ModePolygonOffset:Mode

Gets/sets the mode for polygon offset.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

PolygonOffset:UnitsPolygonOffset:Units

Gets or sets the polygon offset units. Changes to this property cause the polygon mode
to change to off if it was inherited previously.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

                                                    © National Instruments 9585

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9585 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9586 ordinal=9586 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Specials:Anti-aliasingSpecials:Anti-aliasing

      Read or writes whether the object is anti-aliased to smooth lines and edges that
      appear jagged.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Specials:AutonormalizingSpecials:Autonormalizing

      Read or writes whether the vertex normals of the object automatically normalize to
      enhance rendering speed.


9586   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9586 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9587 ordinal=9587 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Specials:DepthSpecials:Depth TestTest

Reads or writes whether the pixels of the 3D object pass the depth test. If the object
passes the depth test, the incoming depth value replaces the value in the depth buffer
when you render the scene.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

                                                    © National Instruments 9587

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9587 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9588 ordinal=9588 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Specials:LightingSpecials:Lighting

      Reads or writes whether a 3D object appears lit.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Specials:ShadeSpecials:Shade ModelModel

      Reads or writes whether a color-filled object appears shaded with one color or
       multiple colors.

     Remarks

      The following table lists the characteristics of this property.


        Data type


9588   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9588 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9589 ordinal=9589 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Specials:TexturingSpecials:Texturing

Reads or writes whether a 3D object appears with a texture. This property must be set
to On to apply textures to an object.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9589

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9589 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9590 ordinal=9590 -->
## Property and Method Reference

Property and Method Reference

    TextureTexture

      Reads the texture that you apply to the 3D object.

      You must close this reference.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   TransformationTransformation

      Reads or writes the transformation you apply to the object.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes


9590   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9590 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9591 ordinal=9591 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ViewView Port:ModePort:Mode

Reads or writes how to specify the size of the view port you use to view the scene.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ViewView Port:ViewPort:View PortPort

Reads or writes the position and size of a viewing port through which you can view a
3D object in the 3D picture control. The x and y values specify the coordinates within
the view port at which LabVIEW renders the object. The width and height specify the

                                                    © National Instruments 9591

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9591 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9592 ordinal=9592 -->
## Property and Method Reference

Property and Method Reference

      width and height of the view port. If you define a view port, objects do not appear
      beyond the specified bounds of the view port.

     Elements

      Name    Description

        X       The x coordinate at which LabVIEW renders the object in the view port.

        Y       The y coordinate at which LabVIEW renders the object in the view port.

        Width    The width of the view port in pixels.

        Height   The height of the view port in pixels.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   SceneClipPlaneSceneClipPlane

       SceneClipPlane Properties
   SceneClipPlaneSceneClipPlane PropertiesProperties


9592   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9592 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9593 ordinal=9593 -->
## Property and Method Reference

Property and Method Reference


 Property  Description

          Reads or writes the number that identifies the clip plane. The range is 0−5. The default is
 Number
           0.

          Reads or writes the four coefficients of the plane equation. Plane
          <equation>Ax+By+Cz+D=0</equation>

NumberNumber

Reads or writes the number that identifies the clip plane. The range is 0−5. The default
is 0.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

PlanePlane

Reads or writes the four coefficients of the plane equation.
<equation>Ax+By+Cz+D=0</equation>


                                                    © National Instruments 9593

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9593 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9594 ordinal=9594 -->
## Property and Method Reference

Property and Method Reference

     Elements

      Name      Description

       A         The value of the A coefficient of the plane equation.

       B         The value of the B coefficient of the plane equation.

       C         The value of the C coefficient of the plane equation.

      D         The value of the D coefficient of the plane equation.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

      SceneDrawableSceneDrawable
   SceneGeometrySceneGeometry

      SceneGeometry Properties
   SceneGeometrySceneGeometry PropertiesProperties


9594   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9594 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9595 ordinal=9595 -->
## Property and Method Reference

Property and Method Reference


 Property         Description

 Texture                Reads or writes how the texture coordinates for the geometry generate. Generator Mode

 Texture         Reads or writes the values that define the s-plane to which you apply the texture.
 Generator S     The following equation defines the plane.
 Plane
                 <equation>Ax+By+Cz+D=0</equation>

 Texture         Reads or writes the values that define the t-plane to which you apply the texture.
 Generator T     The following equation defines the plane.
 Plane
                 <equation>Ax+By+Cz+D=0</equation>

TextureTexture GeneratorGenerator ModeMode

Reads or writes how the texture coordinates for the geometry generate.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9595

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9595 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9596 ordinal=9596 -->
## Property and Method Reference

Property and Method Reference

    TextureTexture GeneratorGenerator SS PlanePlane

      Reads or writes the values that define the s-plane to which you apply the texture. The
       following equation defines the plane. <equation>Ax+By+Cz+D=0</equation>

     Elements

      Name         Description

       A            The A coefficient of the plane equation.

       B            The B coefficient of the plane equation.

       C            The C coefficient of the plane equation.

      D           The D coefficient of the plane equation.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    TextureTexture GeneratorGenerator TT PlanePlane

      Reads or writes the values that define the t-plane to which you apply the texture. The


9596   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9596 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9597 ordinal=9597 -->
## Property and Method Reference

Property and Method Reference

following equation defines the plane. <equation>Ax+By+Cz+D=0</equation>

Elements

 Name         Description

 A            The A coefficient of the plane equation.

 B            The B coefficient of the plane equation.

 C            The C coefficient of the plane equation.

 D           The D coefficient of the plane equation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

SceneMeshSceneMesh

SceneMesh Methods

SceneMesh Properties
SceneMeshSceneMesh MethodsMethods

                                                    © National Instruments 9597

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9597 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9598 ordinal=9598 -->
## Property and Method Reference

Property and Method Reference


       Method     Description

        Delaunay   Generates a Delaunay triangulation mesh around an array of points. Use this method
       Mesh      on an array of 3D points in which no two points share the same x and y values.

                     Sets the parameters that describe the mesh. Use this method to define how LabVIEW         Set Mesh                     renders the 3D object to which you apply the mesh. If you do not specify a value for a        Parameters
                   parameter of this method, LabVIEW uses the current value of the parameter.

        Share                    Shares colors, normals, texture coordinates, and/or vertex arrays between meshes.         Arrays

   DelaunayDelaunay MeshMesh
   DelaunayDelaunay MeshMesh

       Generates a Delaunay triangulation mesh around an array of points. Use this method
      on an array of 3D points in which no two points share the same x and y values.

     Parameters

                 Data      Name            Required  Description                  type

                                         Specifies the array of vertices from which LabVIEW generates the         VertArray          Yes                                   Delaunay mesh.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No


9598   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9598 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9599 ordinal=9599 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SetSet MeshMesh ParametersParameters
SetSet MeshMesh ParametersParameters

Sets the parameters that describe the mesh. Use this method to define how LabVIEW
renders the 3D object to which you apply the mesh. If you do not specify a value for a
parameter of this method, LabVIEW uses the current value of the parameter.

Parameters

           Data Name           Required  Description            type

                               Specifies the mode LabVIEW uses to draw the mesh. The mode
                           determines how LabVIEW interprets the data you wire to Vertex
                               Array.

                           0         Points

                           1         Lines
 Draw                      2         Line Strip              No
 Mode
                           3         Line Loop

                           4          Triangles

                           5          Triangle Strip

                           6          Triangle Fan

                           7        Quads


                                                    © National Instruments 9599

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9599 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9600 ordinal=9600 -->
## Property and Method Reference

Property and Method Reference


                   Data      Name           Required  Description
                   type


                                  8       Quad Strip

                                  9        Polygon


         Vertex                       Sets the x, y, and z values that define the array of vertices of the                    No
         Array                     mesh.

                                  Determines the order in which LabVIEW processes the data in each of
                                    the arrays of the mesh. For example, if Indices is [3, 2, 4, 1], then V0
                                  appears at index 3 in the Vertex Array, the color of V0 appears at
                                    index 3 in the Color Array, and so on.

         Indices         No                                  Note If you set Color Binding Mode to Per
                                    Primitive, then the color refers to the entire face
                                        formed by V0, V1…VN (where N is determined by Draw
                                      Mode) instead of just the specified index.


                                        Specifies the mode used to bind color to the mesh. The mode
                                   determines how LabVIEW assigns the color you specified in Color
                                       Array.

                                  Note The Per Primitive and Overall modes differ in
                                            behavior only when Draw Mode is Points, Lines, Triangles,
                                              or Quads.
         Color
        Binding        No
       Mode                     0 Overall—One color binds uniformly to the entire mesh.
                                      Per Primitive—Different colors bind to each primitive in the
                                  1
                                    mesh.

                                  2 Per Vertex—Different colors bind to each vertex of the mesh.

                                  3 Binding Off—No colors bind to the mesh.


9600   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9600 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9601 ordinal=9601 -->
## Property and Method Reference

Property and Method Reference


           Data Name           Required  Description
            type

                               Specifies the RGBA color value for the color that Color Binding Mode Color Array      No                              applies to the 3D object.


                             Sets the binding mode for the normal vectors of the mesh. The mode
                           determines how LabVIEW assigns the normals specified by Normal
                            Array to the 3D object. Normals determine how lights in a 3D scene
                                 affect the rendering of a 3D object.
 Normal
 Binding        No        0          Overall
 Mode
                           1         Per Primitive

                           2         Per Vertex

                           3         Binding Off


 Normal                     Sets the x, y, and z values that define the array of normals that
              No Array                    Normal Binding Mode applies to the 3D object.


                             Sets the s and t coordinates that define how to apply a texture to the
 Texture                   mesh. You must assign a texture to the mesh for this array to have
 Coordinate      No       meaning. Each element of the array is a coordinate in a 2-D plane of
 Array                   domain {0..1, 0..1}, where [0,0] is the bottom-left pixel of the image,
                        and [1, 1] is the top-right pixel.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No


                                                    © National Instruments 9601

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9601 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9602 ordinal=9602 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\3D Picture Control\
        Using Meshes.vi
   ShareShare ArraysArrays
   ShareShare ArraysArrays

      Shares colors, normals, texture coordinates, and/or vertex arrays between meshes.

     Parameters

      Name           Data type   Required   Description

        Source Mesh                  Yes         Refers to the source of the scene mesh.


          Vertices                 No          Specifies whether to share vertex arrays.


         Colors                  No          Specifies whether to share colors.


        Normals                 No          Specifies whether to share normals.


9602   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9602 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9603 ordinal=9603 -->
## Property and Method Reference

Property and Method Reference


 Name           Data type   Required   Description

 Texture Coords            No          Specifies whether to share texture coordinates.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SceneMeshSceneMesh PropertiesProperties


 Property      Description

              Determines the RGBA color values that can be used by the mesh as defined by the
 Color Array
                 Indices.

 Color Binding
               Returns the mode used to bind colors of the mesh to the representation.
 Mode

 Draw Mode    Returns the mode used to draw the mesh.

 Indices        Indexes the texture coordinates for the mesh.

               Returns the x, y, and z normal components that can be used by the mesh as indexed
 Normal Array
             by the Indices.

 Normal
               Returns the binding mode of the normals of the mesh.
 Binding


                                                    © National Instruments 9603

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9603 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9604 ordinal=9604 -->
## Property and Method Reference

Property and Method Reference


        Property      Description

       Mode

         Texture                       Defines the s and t texture space coordinates that can be used by the mesh as         Coordinates                      indexed by Indices.             []

        Use Display                       Sets whether the mesh uses display lists.          List?

                      Returns an array of the vertices that can be used by the mesh, as indexed by the         Vertex Array                          Indices. Each vertex consists of an x, y, and z value.

   ColorColor ArrayArray
    ColorColor ArrayArray

      Determines the RGBA color values that can be used by the mesh as defined by the
        Indices.

     Elements

      Name     Description

       Red       Indicates the red value. Valid values include 0 through 1.

        Green     Indicates the green value. Valid values include 0 through 1.

        Blue       Indicates the blue value. Valid values include 0 through 1.

        Alpha      Indicates the Alpha value. Valid values include 0 through 1.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

9604   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9604 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9605 ordinal=9605 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ColorColor BindingBinding ModeMode
ColorColor BindingBinding ModeMode

Returns the mode used to bind colors of the mesh to the representation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9605

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9605 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9606 ordinal=9606 -->
## Property and Method Reference

Property and Method Reference

   DrawDraw ModeMode
   DrawDraw ModeMode

       Returns the mode used to draw the mesh.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   IndicesIndices
    IndicesIndices

       Indexes the texture coordinates for the mesh.

     Remarks

      The following table lists the characteristics of this property.


        Data type

9606   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9606 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9607 ordinal=9607 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

NormalNormal ArrayArray
NormalNormal ArrayArray

Returns the x, y, and z normal components that can be used by the mesh as indexed by
the Indices.

Elements

 Name         Description

 X            The x component of the normal vector.

 Y            The y component of the normal vector.

 Z            The z component of the normal vector.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes


                                                    © National Instruments 9607

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9607 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9608 ordinal=9608 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   NormalNormal BindingBinding ModeMode
   NormalNormal BindingBinding ModeMode

       Returns the binding mode of the normals of the mesh.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes


9608   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9608 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9609 ordinal=9609 -->
## Property and Method Reference

Property and Method Reference

TextureTexture CoordinatesCoordinates [][]
TextureTexture CoordinatesCoordinates [][]

Defines the s and t texture space coordinates that can be used by the mesh as indexed
by Indices.

Elements

 Name            Description

 S              The s texture space coordinate.

 T              The t texture space coordinate.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9609

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9609 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9610 ordinal=9610 -->
## Property and Method Reference

Property and Method Reference

   UseUse DisplayDisplay List?List?
   UseUse DisplayDisplay List?List?

       Sets whether the mesh uses display lists.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   VertexVertex ArrayArray
    VertexVertex ArrayArray

       Returns an array of the vertices that can be used by the mesh, as indexed by the
        Indices. Each vertex consists of an x, y, and z value.

       This property is an array of clusters. Each cluster contains the following elements.


9610   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9610 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9611 ordinal=9611 -->
## Property and Method Reference

Property and Method Reference

Elements

 Name             Description

 X               The x coordinate of the vertex.

 Y               The y coordinate of the vertex.

 Z               The z coordinate of the vertex.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

SceneHeightFieldSceneHeightField

SceneHeightField Properties
SceneHeightFieldSceneHeightField PropertiesProperties


 Property  Description

 Base     Reads or writes the height of the base of a height field. Elevations on a height field use
 Height    the base height as their 0 height. The default is 0.


                                                    © National Instruments 9611

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9611 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9612 ordinal=9612 -->
## Property and Method Reference

Property and Method Reference


        Property  Description

                 Reads or writes the color of the height field in RGBA format. This property accepts values
         Color    0 to 1, where 0 represents the absence of the current color and 1 represents a full
                    saturation of the current color.

       Column  Reads or writes the distance that uniformly separates each point on the final surface as
          Interval  you move horizontally through the height field data.

                 Reads or writes a 2D array of values that represent the height of the surface at evenly
        Data     spaced intervals. Each entry in the Data array specifies a point up to which LabVIEW
                 draws the object. Use this property to draw contoured images, such as hills or waves.

      Row     Reads or writes the distance that uniformly separates each point on the final surface as
          Interval  you move vertically through the height field data.

   BaseBase HeightHeight
   BaseBase HeightHeight

      Reads or writes the height of the base of a height field. Elevations on a height field use
       the base height as their 0 height. The default is 0.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

9612   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9612 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9613 ordinal=9613 -->
## Property and Method Reference

Property and Method Reference

ColorColor
ColorColor

Reads or writes the color of the height field in RGBA format. This property accepts
values 0 to 1, where 0 represents the absence of the current color and 1 represents a
full saturation of the current color.

Elements

 Name     Description

 Red       Indicates the red value. Valid values include 0 through 1.

 Green     Indicates the green value. Valid values include 0 through 1.

 Blue       Indicates the blue value. Valid values include 0 through 1.

 Alpha      Indicates the Alpha value. Valid values include 0 through 1.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9613

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9613 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9614 ordinal=9614 -->
## Property and Method Reference

Property and Method Reference

   ColumnColumn IntervalInterval
   ColumnColumn IntervalInterval

      Reads or writes the distance that uniformly separates each point on the final surface as
      you move horizontally through the height field data.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   DataData
   DataData

      Reads or writes a 2D array of values that represent the height of the surface at evenly
      spaced intervals. Each entry in the Data array specifies a point up to which LabVIEW
      draws the object. Use this property to draw contoured images, such as hills or waves.


9614   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9614 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9615 ordinal=9615 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

RowRow IntervalInterval
RowRow IntervalInterval

Reads or writes the distance that uniformly separates each point on the final surface as
you move vertically through the height field data.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes


                                                    © National Instruments 9615

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9615 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9616 ordinal=9616 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   SceneCylinderSceneCylinder

       SceneCylinder Properties
   SceneCylinderSceneCylinder PropertiesProperties


        Property  Description

                 Reads or writes the color of the cylinder in RGBA format. This property accepts values 0
         Color     to 1, where 0 represents the absence of the red, green, or blue color and 1 represents a
                         full saturation of the current color.

                 Reads or writes the level of detail used to render the cylinder. This property accepts
          Detail     values 0 to 1, with 0 representing very little detail and 1 representing a high level of
                       detail.

        Height   Reads or writes the height of the cylinder. The default is 0.

        Radius   Reads or writes the radius of the cylinder. The default is 0.

   ColorColor
    ColorColor

      Reads or writes the color of the cylinder in RGBA format. This property accepts values
     0 to 1, where 0 represents the absence of the red, green, or blue color and 1
       represents a full saturation of the current color.


9616   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9616 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9617 ordinal=9617 -->
## Property and Method Reference

Property and Method Reference

Elements

 Name     Description

 Red       Indicates the red value. Valid values include 0 through 1.

 Green     Indicates the green value. Valid values include 0 through 1.

 Blue       Indicates the blue value. Valid values include 0 through 1.

 Alpha      Indicates the Alpha value. Valid values include 0 through 1.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DetailDetail
DetailDetail

Reads or writes the level of detail used to render the cylinder. This property accepts
values 0 to 1, with 0 representing very little detail and 1 representing a high level of
detail.


                                                    © National Instruments 9617

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9617 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9618 ordinal=9618 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   HeightHeight
   HeightHeight

      Reads or writes the height of the cylinder. The default is 0.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No


9618   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9618 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9619 ordinal=9619 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

RadiusRadius
RadiusRadius

Reads or writes the radius of the cylinder. The default is 0.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

SceneSphereSceneSphere

SceneSphere Properties
SceneSphereSceneSphere PropertiesProperties


                                                    © National Instruments 9619

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9619 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9620 ordinal=9620 -->
## Property and Method Reference

Property and Method Reference


        Property  Description

                 Reads or writes the color of the sphere in RGBA format. This property accepts values 0 to
         Color     1, where 0 represents the absence of the current color and 1 represents a full saturation
                    of the current color.

                 Reads or writes the level of detail used to render the sphere. This property accepts
          Detail     values 0 to 1, with 0 representing very little detail and 1 representing a high level of
                       detail.

        Radius   Reads or writes the radius of the sphere. The default is 0.

   ColorColor
    ColorColor

      Reads or writes the color of the sphere in RGBA format. This property accepts values 0
       to 1, where 0 represents the absence of the current color and 1 represents a full
       saturation of the current color.

     Elements

      Name     Description

       Red       Indicates the red value. Valid values include 0 through 1.

        Green     Indicates the green value. Valid values include 0 through 1.

        Blue       Indicates the blue value. Valid values include 0 through 1.

        Alpha      Indicates the Alpha value. Valid values include 0 through 1.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

9620   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9620 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9621 ordinal=9621 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DetailDetail
DetailDetail

Reads or writes the level of detail used to render the sphere. This property accepts
values 0 to 1, with 0 representing very little detail and 1 representing a high level of
detail.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9621

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9621 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9622 ordinal=9622 -->
## Property and Method Reference

Property and Method Reference

   RadiusRadius
   RadiusRadius

      Reads or writes the radius of the sphere. The default is 0.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   SceneConeSceneCone

      SceneCone Properties
   SceneConeSceneCone PropertiesProperties


        Property  Description

                 Reads or writes the color of the cone in RGBA format. This property accepts values 0 to 1,
         Color    where 0 represents the absence of the red, green, or blue color and 1 represents a full
                    saturation of the color.


9622   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9622 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9623 ordinal=9623 -->
## Property and Method Reference

Property and Method Reference


 Property  Description

          Reads or writes the level of detail used to render the cone. This property accepts values 0
 Detail
           to 1, with 0 representing very little detail and 1 representing a high level of detail.

 Height   Reads or writes the height of the cone. The default is 0.

 Radius   Reads or writes the radius of the cone. The default is 0.

ColorColor
ColorColor

Reads or writes the color of the cone in RGBA format. This property accepts values 0 to
1, where 0 represents the absence of the red, green, or blue color and 1 represents a
full saturation of the color.

Elements

 Name     Description

 Red       Indicates the red value. Valid values include 0 through 1.

 Green     Indicates the green value. Valid values include 0 through 1.

 Blue       Indicates the blue value. Valid values include 0 through 1.

 Alpha      Indicates the Alpha value. Valid values include 0 through 1.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

                                                    © National Instruments 9623

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9623 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9624 ordinal=9624 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    DetailDetail
    DetailDetail

      Reads or writes the level of detail used to render the cone. This property accepts
       values 0 to 1, with 0 representing very little detail and 1 representing a high level of
        detail.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9624   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9624 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9625 ordinal=9625 -->
## Property and Method Reference

Property and Method Reference

HeightHeight
HeightHeight

Reads or writes the height of the cone. The default is 0.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

RadiusRadius
RadiusRadius

Reads or writes the radius of the cone. The default is 0.

Remarks

The following table lists the characteristics of this property.


 Data type

                                                    © National Instruments 9625

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9625 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9626 ordinal=9626 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   SceneBoxSceneBox

      SceneBox Properties
   SceneBoxSceneBox PropertiesProperties


        Property  Description

                 Reads or writes the color of the box in RGBA format. This property accepts values 0 to 1,
         Color    where 0 represents the absence of the red, green, or blue color and 1 represents a full
                    saturation of the color.

        Length X  Reads or writes the length of the x-axis of the box. The default is 0.

        Length Y  Reads or writes the length of the y-axis of the box. The default is 0.

        Length Z  Reads or writes the length of the z-axis of the box. The default is 0.

   ColorColor
    ColorColor

      Reads or writes the color of the box in RGBA format. This property accepts values 0 to
       1, where 0 represents the absence of the red, green, or blue color and 1 represents a


9626   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9626 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9627 ordinal=9627 -->
## Property and Method Reference

Property and Method Reference

full saturation of the color.

Elements

 Name     Description

 Red       Indicates the red value. Valid values include 0 through 1.

 Green     Indicates the green value. Valid values include 0 through 1.

 Blue       Indicates the blue value. Valid values include 0 through 1.

 Alpha      Indicates the Alpha value. Valid values include 0 through 1.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

LengthLength XX
LengthLength XX

Reads or writes the length of the x-axis of the box. The default is 0.


                                                    © National Instruments 9627

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9627 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9628 ordinal=9628 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   LengthLength YY
   LengthLength YY

      Reads or writes the length of the y-axis of the box. The default is 0.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No


9628   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9628 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9629 ordinal=9629 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

LengthLength ZZ
LengthLength ZZ

Reads or writes the length of the z-axis of the box. The default is 0.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

SceneTextSceneText

SceneText Properties
SceneTextSceneText PropertiesProperties


                                                    © National Instruments 9629

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9629 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9630 ordinal=9630 -->
## Property and Method Reference

Property and Method Reference


        Property             Description

                                 Specifies the alignment of text in a 3D scene relative to the origin of the text        Alignment                               object that contains the text.

                                 Specifies the alignment of a text object in a 3D scene relative to the vertical
         Alignment:Horizontal plane that intersects the center-point of the text object. This property is an
                           element of the Alignment property.

                                 Specifies the alignment of a text object in a 3D scene relative to the
         Alignment:Vertical     horizontal plane that intersects the center-point of the text object. This
                              property is an element of the Alignment property.

         Axis Alignment        Aligns the text object along the plane you specify.

                                 Specifies the height of text characters in a text object in object coordinates.
         Character Size        For example, set character size to 1 to create a text object equal in height to
                           a geometric object with a height of 1.

                           Reads or writes the color of the text in a text object in RGBA format. This
                              property accepts a cluster of numeric values 0 through 1, where 0
         Color
                               represents the absence of the red, green, or blue color and 1 represents a
                                        full saturation of the color.

                                 Specifies the path to a font to apply to a text object. This property accepts
        Font Path            only TrueType fonts. The path you wire to this property must have a .ttf
                                          file extension.

         Text                   Specifies the text of a text object.

                                 Specifies whether LabVIEW renders the text in a text object with the
                               characters arranged vertically or horizontally. If TRUE, LabVIEW arranges the
                               characters vertically, so that the character string aligns with the plane that
          Vertical?               intersects the center-point of the text object on the x-axis. If FALSE, LabVIEW
                              arranges the characters horizontally, so that the character string aligns with
                             the plane that intersects the center-point of the text object on the y-axis.
                          The default is FALSE.

                                 Specifies how much of the text in a text object LabVIEW renders in one line.
                                                 If you use the Vertical? property to render the text vertically, this property
                                 sets the maximum height of the text object. If you render the text
       Wrap Distance
                                  horizontally, this property sets the maximum width of the text object. If the
                              length of the text exceeds the wrap distance, LabVIEW wraps the text to a
                       new line. If you set this property to 0, LabVIEW does not wrap the text.


9630   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9630 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9631 ordinal=9631 -->
## Property and Method Reference

Property and Method Reference

AlignmentAlignment

Specifies the alignment of text in a 3D scene relative to the origin of the text object that
contains the text.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alignment:HorizontalAlignment:Horizontal

Specifies the alignment of a text object in a 3D scene relative to the vertical plane that
intersects the center-point of the text object. This property is an element of the
Alignment property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 9631

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9631 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9632 ordinal=9632 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alignment:VerticalAlignment:Vertical

       Specifies the alignment of a text object in a 3D scene relative to the horizontal plane
       that intersects the center-point of the text object. This property is an element of the
      Alignment property.

           Note The Base Line and Bottom Base Line options behave in the same
            manner as the Bottom option when you use the default font and the text
               object includes only one line of text. The Bottom Base Line option behaves in
              the same manner as the Bottom option when you use the default font and
              the text object includes more than one line of text. You must use a TrueType
               font to see the expected Base Line and Bottom Base Line behaviors.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No


9632   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9632 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9633 ordinal=9633 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

AxisAxis AlignmentAlignment

Aligns the text object along the plane you specify.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

CharacterCharacter SizeSize

Specifies the height of text characters in a text object in object coordinates. For
example, set character size to 1 to create a text object equal in height to a geometric
object with a height of 1.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 9633

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9633 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9634 ordinal=9634 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    ColorColor

      Reads or writes the color of the text in a text object in RGBA format. This property
       accepts a cluster of numeric values 0 through 1, where 0 represents the absence of the
       red, green, or blue color and 1 represents a full saturation of the color.

     Elements

      Name  Description

       Red    Indicates the saturation of the red color. Valid values include 0 through 1.

        Green  Indicates the saturation of the green color. Valid values include 0 through 1.

        Blue   Indicates the saturation of the blue color. Valid values include 0 through 1.

                 Indicates the level of transparency of the red, green, and blue colors. Valid values include 0
        Alpha
               through 1.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

9634   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9634 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9635 ordinal=9635 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

FontFont PathPath

Specifies the path to a font to apply to a text object. This property accepts only
TrueType fonts. The path you wire to this property must have a .ttf file extension.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

TextText

Specifies the text of a text object.

                                                    © National Instruments 9635

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9635 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9636 ordinal=9636 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Vertical?Vertical?

       Specifies whether LabVIEW renders the text in a text object with the characters
       arranged vertically or horizontally. If TRUE, LabVIEW arranges the characters vertically,
      so that the character string aligns with the plane that intersects the center-point of the
        text object on the x-axis. If FALSE, LabVIEW arranges the characters horizontally, so
       that the character string aligns with the plane that intersects the center-point of the
        text object on the y-axis. The default is FALSE.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes


9636   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9636 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9637 ordinal=9637 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

WrapWrap DistanceDistance

Specifies how much of the text in a text object LabVIEW renders in one line. If you use
the Vertical? property to render the text vertically, this property sets the maximum
height of the text object. If you render the text horizontally, this property sets the
maximum width of the text object. If the length of the text exceeds the wrap distance,
LabVIEW wraps the text to a new line. If you set this property to 0, LabVIEW does not
wrap the text.

      Note You cannot use this property to truncate text. If you want to cut off the
         text, use the Clip Plane:Add Clip Plane to clip the text object.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

                                                    © National Instruments 9637

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9637 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9638 ordinal=9638 -->
## Property and Method Reference

Property and Method Reference

     SceneWindowSceneWindow

      SceneWindow Methods

      SceneWindow Properties
   SceneWindowSceneWindow MethodsMethods


       Method                 Description

                                   Positions the camera to view all 3D scene objects. Use this method to        AutoFocus                                 automatically focus and render the scene in an exterior window.

                                 Creates a ray that originates at the specified point and returns an array of         Pick
                            node paths for objects that intersect that ray.

                                 Sets coordinates to render the scene in a frustum-shaped view. This         Projection:Frustum
                                  projection causes objects farther from the camera to appear smaller.

                                 Sets coordinates to render the scene in a box-shaped view. The distance
         Projection:Orthographic  of the camera from the objects does not affect the size of the objects in
                                      this view.

                                 Sets coordinates to render the scene in a frustum-shaped view, where
                             you specify an angle for the horizontal and vertical viewing fields. This         Projection:Perspective
                                  projection causes objects closer to the camera to appear larger in size.
                                  This method is similar to the Projection:Frustum method.

       Redraw               Redraws the 3D scene in the scene window.

        Render to Image         Returns an image of the scene.

        Setup Camera            Specifies the position of the camera relative to the scene.

                                Converts a point in window coordinates to points in object coordinates
        WindowToObjectCoords
                           on the near and far clip planes.

   AutoFocusAutoFocus

       Positions the camera to view all 3D scene objects. Use this method to automatically
       focus and render the scene in an exterior window.


9638   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9638 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9639 ordinal=9639 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

PickPick

Creates a ray that originates at the specified point and returns an array of node paths
for objects that intersect that ray.

Parameters

       Data Name         Required  Description
       type

                           Horizontal and vertical values that define a coordinate in the projection
 point          Yes
                         plane of the 3D scene.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

                                                    © National Instruments 9639

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9639 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9640 ordinal=9640 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    Projection:FrustumProjection:Frustum

       Sets coordinates to render the scene in a frustum-shaped view. This projection causes
       objects farther from the camera to appear smaller.

     Parameters

                Data      Name         Required  Description
                 type

          Left            Yes        Specifies the left bound of the frustum.


         Right          Yes        Specifies the right bound of the frustum.


        Bottom        Yes        Specifies the bottom bound of the frustum.


        Top            Yes        Specifies the top bound of the frustum.


        Near                       Specifies the clipping plane nearest the viewer. LabVIEW does not
         Clipping       Yes       render objects that appear closer to the viewer than the specified Near
        Plane                    Clipping Pane boundary.


9640   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9640 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9641 ordinal=9641 -->
## Property and Method Reference

Property and Method Reference


         Data Name         Required  Description
         type

 Far                        Specifies the clipping plane farthest from the viewer. LabVIEW does not
 Clipping       Yes       render objects that appear farther from the viewer than the specified
 Plane                    Far Clipping Pane boundary.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Projection:OrthographicProjection:Orthographic

Sets coordinates to render the scene in a box-shaped view. The distance of the camera
from the objects does not affect the size of the objects in this view.

Parameters

         Data
 Name         Required  Description
         type

 Left            Yes        Specifies the left bound of the box.


                                                    © National Instruments 9641

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9641 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9642 ordinal=9642 -->
## Property and Method Reference

Property and Method Reference


                Data      Name         Required  Description
                 type

         Right          Yes        Specifies the right bound of the box.


        Bottom        Yes        Specifies the bottom bound of the box.


        Top            Yes        Specifies the top bound of the box.


        Near                       Specifies the clipping plane nearest the viewer. LabVIEW does not
         Clipping       Yes       render objects that appear closer to the viewer than the specified Near
        Plane                    Clipping Pane boundary.


         Far                        Specifies the clipping plane farthest from the viewer. LabVIEW does not
         Clipping       Yes       render objects that appear farther from the viewer than the specified
        Plane                    Far Clipping Pane boundary.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


9642   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9642 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9643 ordinal=9643 -->
## Property and Method Reference

Property and Method Reference

Projection:PerspectiveProjection:Perspective

Sets coordinates to render the scene in a frustum-shaped view, where you specify an
angle for the horizontal and vertical viewing fields. This projection causes objects
closer to the camera to appear larger in size. This method is similar to the
Projection:Frustum method.

Parameters

         Data Name         Required  Description         type

 Field of
                Yes       Defines the field of view for the frustum. View

 Aspect                Yes       Defines the aspect ratio for the frustum. Ratio


 Near                       Specifies the clipping plane nearest the viewer. LabVIEW does not
 Clipping       Yes       render objects that appear closer to the viewer than the specified Near
 Plane                    Clipping Pane boundary.


 Far                        Specifies the clipping plane farthest from the viewer. LabVIEW does not
 Clipping       Yes       render objects that appear farther from the viewer than the specified
 Plane                    Far Clipping Pane boundary.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

                                                    © National Instruments 9643

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9643 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9644 ordinal=9644 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   RedrawRedraw

      Redraws the 3D scene in the scene window.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   RenderRender toto ImageImage

       Returns an image of the scene.

     Remarks

      The following table lists the characteristics of this method.


        Data type

9644   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9644 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9645 ordinal=9645 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

SetupSetup CameraCamera

Specifies the position of the camera relative to the scene.

Parameters

          Data
 Name          Required  Description          type

 Camera                   Sets the x, y, and z coordinates that define the initial position of the
                 Yes Position                 camera. The default coordinate values are [0, 0, -4].


                           Sets the x, y, and z coordinates that define the point in the scene that
 Target          Yes       the camera faces and around which a spherical camera rotates. The
                             default coordinate values are [0, 0, 0].


 Up                        Sets the x, y, and z coordinates that define the axis that the top of the
                 Yes
 Direction               camera faces. The default coordinate values are [0, 1, 0].


Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 9645

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9645 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9646 ordinal=9646 -->
## Property and Method Reference

Property and Method Reference


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   WindowToObjectCoordsWindowToObjectCoords

       Converts a point in window coordinates to points in object coordinates on the near
      and far clip planes.

     Parameters

                    Data
      Name               Required  Description                    type

                                Window coordinates of the point that you want to convert to         point                 Yes
                                          object coordinates.


        near plane                     Returns the window point converted at the near plane, or the
                              Yes
         point                             front of the rendering.


          far plane                       Returns the window point converted at the far plane, or the back
                              Yes
         point                             of the rendering.


     Remarks

      The following table lists the characteristics of this method.

9646   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9646 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9647 ordinal=9647 -->
## Property and Method Reference

Property and Method Reference


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SceneWindowSceneWindow PropertiesProperties


 Property          Description

 Automatic        Reads or writes whether LabVIEW automatically updates the projection mode
 Projection Mode   when you resize the scene window.

 Background Color  Reads or writes the RGBA color value for the background of the 3D scene.

 Camera                 Reads or writes if the scene window becomes invalid when you use the camera Controller:Auto                      controller.
 Redraw

 Camera          Reads or writes the configuration of the scene camera. Click and hold the left
 Controller:Type   mouse button and drag the cursor to operate the camera.

                 Reads or writes a matrix that contains the translation, rotation, and scale values ModelView Matrix
                      for the 3D scene that appears in the scene window.

                Read or writes the matrix that represents the transformations LabVIEW uses to
 Projection Matrix
                    project the 3D scene in the scene window.

 Scene            Reads or writes the reference number for the scene.

 Window Bounds   Reads or writes the left, right, top, and bottom bounds of the scene window.

 Window State     Reads or writes the state of the scene window.

 Window Title      Reads or writes the title of the scene window.


                                                    © National Instruments 9647

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9647 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9648 ordinal=9648 -->
## Property and Method Reference

Property and Method Reference

   AutomaticAutomatic ProjectionProjection ModeMode

      Reads or writes whether LabVIEW automatically updates the projection mode when
      you resize the scene window.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   BackgroundBackground ColorColor

      Reads or writes the RGBA color value for the background of the 3D scene.

     Elements

      Name  Description

       Red    Indicates the red value. Valid values include 0 through 1.

        Green  Indicates the green value. Valid values include 0 through 1.

        Blue   Indicates the blue value. Valid values include 0 through 1.

                 Indicates the Alpha value. Set the Alpha value on the background of a 3D scene only for
        Alpha
                blending. Setting this value does not make the background of the 3D scene transparent.

9648   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9648 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9649 ordinal=9649 -->
## Property and Method Reference

Property and Method Reference


 Name  Description

         Valid values include 0 through 1.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

CameraCamera Controller:AutoController:Auto RedrawRedraw

Reads or writes if the scene window becomes invalid when you use the camera
controller.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

                                                    © National Instruments 9649

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9649 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9650 ordinal=9650 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   CameraCamera Controller:TypeController:Type

      Reads or writes the configuration of the scene camera. Click and hold the left mouse
       button and drag the cursor to operate the camera.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ModelViewModelView MatrixMatrix

      Reads or writes a matrix that contains the translation, rotation, and scale values for the
      3D scene that appears in the scene window.


9650   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9650 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9651 ordinal=9651 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ProjectionProjection MatrixMatrix

Read or writes the matrix that represents the transformations LabVIEW uses to project
the 3D scene in the scene window.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No


                                                    © National Instruments 9651

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9651 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9652 ordinal=9652 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   SceneScene

      Reads or writes the reference number for the scene.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   WindowWindow BoundsBounds

      Reads or writes the left, right, top, and bottom bounds of the scene window.

     Elements

      Name      Description

          Left       The horizontal coordinate of the left edge of the scene window.

        Top       The vertical coordinate of the top edge of the scene window.


9652   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9652 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9653 ordinal=9653 -->
## Property and Method Reference

Property and Method Reference


 Name      Description

 Right      The horizontal coordinate of the right edge of the scene window.

 Bottom    The vertical coordinate of the bottom edge of the scene window.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

WindowWindow StateState

Reads or writes the state of the scene window.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No


                                                    © National Instruments 9653

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9653 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9654 ordinal=9654 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   WindowWindow TitleTitle

      Reads or writes the title of the scene window.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

      VariableVariable

       Variable Methods

       Variable Properties

       VariableVariable MethodsMethods


9654   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9654 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9655 ordinal=9655 -->
## Property and Method Reference

Property and Method Reference


 Method                          Description

 Disconnect From Typedefs         Disconnects the variable from the type definition.

DisconnectDisconnect FromFrom TypedefsTypedefs

Disconnects the variable from the type definition.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

VariableVariable PropertiesProperties

Use these properties to configure shared variables. You also can use the Variable
Reference property with the Variable properties to configure shared variables
programmatically. Changes you make using the Variable properties take effect after
you save the project library. These properties are similar to the options on the Variable
page of the Shared Variable Properties dialog box.


 Property                           Description

                                   Gets or sets how the Bad Status alarm for a shared variable is
 Alarming:BadStatus:Ack Type       acknowledged. To use this property, you must install the
                               LabVIEW Datalogging and Supervisory Control Module.

                                                    © National Instruments 9655

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9655 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9656 ordinal=9656 -->
## Property and Method Reference

Property and Method Reference


        Property                           Description

                                                                       If TRUE, LabVIEW enables alarm logging for the Bad Status
                                        alarm for a shared variable. The default is FALSE. To use this         Alarming:BadStatus:Allow Log                                              property, you must install the LabVIEW Datalogging and
                                           Supervisory Control Module.

                                          Gets or sets a descriptive area name for the Bad Status alarm
         Alarming:BadStatus:Area              for a shared variable. To use this property, you must install
                                           the LabVIEW Datalogging and Supervisory Control Module.

                                          Gets or sets the description of the Bad Status alarm for a
         Alarming:BadStatus:Description     shared variable. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                                                       If TRUE, LabVIEW enables the Bad Status alarm for a shared
                                                 variable. The default is FALSE. To use this property, you must         Alarming:BadStatus:Enabled                                                       install the LabVIEW Datalogging and Supervisory Control
                                         Module.

                                          Gets or sets the name of the Bad Status alarm for a shared
        Alarming:BadStatus:Name            variable. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                          Gets or sets the priority of the Bad Status alarm for a shared
         Alarming:BadStatus:Priority          variable. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                          Gets or sets how the DISCRETE alarm for a shared variable is
        Alarming:Boolean:Ack Type         acknowledged. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                          Gets or sets whether a shared variable is in alarm state when
                                           the value is either high (TRUE) or low (FALSE). To use this
        Alarming:Boolean:Alarm On
                                              property, you must install the LabVIEW Datalogging and
                                           Supervisory Control Module.

                                                                       If TRUE, LabVIEW enables alarm logging for the DISCRETE
                                        alarm for a shared variable. The default is FALSE. To use this
         Alarming:Boolean:Allow Log
                                              property, you must install the LabVIEW Datalogging and
                                           Supervisory Control Module.

                                          Gets or sets a descriptive area name for the DISCRETE alarm
         Alarming:Boolean:Area                for a shared variable. To use this property, you must install
                                           the LabVIEW Datalogging and Supervisory Control Module.

                                          Gets or sets the description of the DISCRETE alarm for a
         Alarming:Boolean:Description
                                         shared variable. To use this property, you must install the


9656   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9656 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9657 ordinal=9657 -->
## Property and Method Reference

Property and Method Reference


Property                           Description

                              LabVIEW Datalogging and Supervisory Control Module.

                                                         If TRUE, LabVIEW enables the DISCRETE alarm for a shared
                                       variable. The default is FALSE. To use this property, you mustAlarming:Boolean:Enabled                                            install the LabVIEW Datalogging and Supervisory Control
                                 Module.

                                  Gets or sets the name of the DISCRETE alarm for a shared
Alarming:Boolean:Name              variable. To use this property, you must install the LabVIEW
                                  Datalogging and Supervisory Control Module.

                                  Gets or sets the priority of the DISCRETE alarm for a shared
Alarming:Boolean:Priority            variable. To use this property, you must install the LabVIEW
                                  Datalogging and Supervisory Control Module.

                                                         If TRUE, LabVIEW enables alarming for a shared variable. The
Alarming:Enabled                    default is FALSE. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                                         If TRUE, LabVIEW sets an event for a shared variable when
                                  data changes. The default is FALSE. To use this property, youAlarming:Event On Data Change                              must install the LabVIEW Datalogging and Supervisory
                                   Control Module.

                                                         If TRUE, the value change event is generated on user input
                                       only. The default is TRUE. To use this property, you mustAlarming:Event On User Input Only
                                            install the LabVIEW Datalogging and Supervisory Control
                                 Module.

                                  Gets or sets how the HI alarm for a shared variable is
Alarming:Hi:Ack Type              acknowledged. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                                         If TRUE, LabVIEW enables alarm logging for the HI alarm for a
                                 shared variable. The default is FALSE. To use this property,
Alarming:Hi:Allow Log
                              you must install the LabVIEW Datalogging and Supervisory
                                   Control Module.

                                  Gets or sets a descriptive area name for the HI alarm for a
Alarming:Hi:Area                  shared variable. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                  Gets or sets the HI alarm deadband as a percentage of the full
Alarming:Hi:Deadband               scale range. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.


                                                    © National Instruments 9657

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9657 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9658 ordinal=9658 -->
## Property and Method Reference

Property and Method Reference


        Property                           Description

                                          Gets or sets the description of the HI alarm for a shared
         Alarming:Hi:Description              variable. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                                                       If TRUE, LabVIEW enables the HI alarm for a shared variable.
         Alarming:Hi:Enabled              The default is FALSE. To use this property, you must install
                                           the LabVIEW Datalogging and Supervisory Control Module.

                                          Gets or sets the value, in engineering units, that evokes the HI
                                        alarm condition for a shared variable. To use this property,         Alarming:Hi:Level
                                      you must install the LabVIEW Datalogging and Supervisory
                                            Control Module.

                                          Gets or sets the name of the HI alarm for a shared variable. To
        Alarming:Hi:Name                 use this property, you must install the LabVIEW Datalogging
                                     and Supervisory Control Module.

                                          Gets or sets the priority of the HI alarm for a shared variable.
         Alarming:Hi:Priority               To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                          Gets or sets how the HI_HI alarm for a shared variable is
         Alarming:HiHi:Ack Type            acknowledged. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                                                       If TRUE, LabVIEW enables alarm logging for the HI_HI alarm
                                                  for a shared variable. The default is FALSE. To use this
         Alarming:HiHi:Allow Log                                              property, you must install the LabVIEW Datalogging and
                                           Supervisory Control Module.

                                          Gets or sets a descriptive area name for the HI_HI alarm for a
         Alarming:HiHi:Area                shared variable. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                          Gets or sets the HI_HI alarm deadband as a percentage of the
        Alarming:HiHi:Deadband                full scale range. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                          Gets or sets the description of the HI_HI alarm for a shared
         Alarming:HiHi:Description            variable. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                                                       If TRUE, LabVIEW enables the HI_HI alarm for a shared
                                                 variable. The default is FALSE. To use this property, you must
         Alarming:HiHi:Enabled
                                                       install the LabVIEW Datalogging and Supervisory Control
                                         Module.


9658   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9658 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9659 ordinal=9659 -->
## Property and Method Reference

Property and Method Reference


Property                           Description

                                  Gets or sets the value, in engineering units, that evokes the
                                  HI_HI alarm condition for a shared variable. To use thisAlarming:HiHi:Level                                     property, you must install the LabVIEW Datalogging and
                                   Supervisory Control Module.

                                  Gets or sets the name of the HI_HI alarm for a shared
Alarming:HiHi:Name                  variable. To use this property, you must install the LabVIEW
                                  Datalogging and Supervisory Control Module.

                                  Gets or sets the priority of the HI_HI alarm for a shared
Alarming:HiHi:Priority                variable. To use this property, you must install the LabVIEW
                                  Datalogging and Supervisory Control Module.

                                  Gets or sets how the LO alarm for a shared variable is
Alarming:Lo:Ack Type              acknowledged. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                                         If TRUE, LabVIEW enables alarm logging for the LO alarm for a
                                 shared variable. The default is FALSE. To use this property,Alarming:Lo:Allow Log
                              you must install the LabVIEW Datalogging and Supervisory
                                   Control Module.

                                  Gets or sets a descriptive area name for the LO alarm for a
Alarming:Lo:Area                  shared variable. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                  Gets or sets the LO alarm deadband as a percentage of the
Alarming:Lo:Deadband                  full scale range. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                  Gets or sets the description of the LO alarm for a shared
Alarming:Lo:Description              variable. To use this property, you must install the LabVIEW
                                  Datalogging and Supervisory Control Module.

                                                         If TRUE, LabVIEW enables the LO alarm for a shared variable.
Alarming:Lo:Enabled             The default is FALSE. To use this property, you must install
                                  the LabVIEW Datalogging and Supervisory Control Module.

                                  Gets or sets the value, in engineering units, that evokes the
                            LO alarm condition for a shared variable. To use this property,
Alarming:Lo:Level
                              you must install the LabVIEW Datalogging and Supervisory
                                   Control Module.

                                  Gets or sets the name of the LO alarm for a shared variable.
Alarming:Lo:Name                To use this property, you must install the LabVIEW
                                  Datalogging and Supervisory Control Module.


                                                    © National Instruments 9659

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9659 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9660 ordinal=9660 -->
## Property and Method Reference

Property and Method Reference


        Property                           Description

                                          Gets or sets the priority of the LO alarm for a shared variable.
         Alarming:Lo:Priority               To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                          Gets or sets how the LO_LO alarm for a shared variable is
         Alarming:LoLo:Ack Type            acknowledged. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                                                       If TRUE, LabVIEW enables alarm logging for the LO_LO alarm
                                                  for a shared variable. The default is FALSE. To use this         Alarming:LoLo:Allow Log
                                              property, you must install the LabVIEW Datalogging and
                                           Supervisory Control Module.

                                          Gets or sets a descriptive area name for the LO_LO alarm for a
         Alarming:LoLo:Area                shared variable. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                          Gets or sets the LO_LO alarm deadband as a percentage of
        Alarming:LoLo:Deadband           the full scale range. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                          Gets or sets the description of the LO_LO alarm for a shared
         Alarming:LoLo:Description            variable. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                                                       If TRUE, LabVIEW enables the LO_LO alarm for a shared
                                                 variable. The default is FALSE. To use this property, you must
        Alarming:LoLo:Enabled                                                       install the LabVIEW Datalogging and Supervisory Control
                                         Module.

                                          Gets or sets the value, in engineering units, that evokes the
                                    LO_LO alarm condition for a shared variable. To use this
         Alarming:LoLo:Level
                                              property, you must install the LabVIEW Datalogging and
                                           Supervisory Control Module.

                                          Gets or sets the name of the LO_LO alarm for a shared
        Alarming:LoLo:Name                 variable. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                          Gets or sets the priority of the LO_LO alarm for a shared
         Alarming:LoLo:Priority                variable. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                          Gets or sets how the Rate of Change alarm for a shared
        Alarming:RateOfChange:Ack Type    variable is acknowledged. To use this property, you must
                                                       install the LabVIEW Datalogging and Supervisory Control


9660   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9660 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9661 ordinal=9661 -->
## Property and Method Reference

Property and Method Reference


Property                           Description

                                 Module.

                                                         If TRUE, LabVIEW enables alarm logging for the Rate of
                              Change alarm for a shared variable. The default is FALSE. ToAlarming:RateOfChange:Allow Log                                use this property, you must install the LabVIEW Datalogging
                             and Supervisory Control Module.

                                  Gets or sets a descriptive area name for the Rate of Change
                                alarm for a shared variable. To use this property, you mustAlarming:RateOfChange:Area                                            install the LabVIEW Datalogging and Supervisory Control
                                 Module.

                                  Gets or sets the value that a shared variable value must
                               change in the specified time to trigger the Rate of ChangeAlarming:RateOfChange:Change
                                   alarm. To use this property, you must install the LabVIEW
                                  Datalogging and Supervisory Control Module.

                                  Gets or sets the description of the Rate of Change alarm for a
Alarming:RateOfChange:Description shared variable. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                                         If TRUE, LabVIEW enables the Rate of Change alarm for a
                                 shared variable. The default is FALSE. To use this property,Alarming:RateOfChange:Enabled                              you must install the LabVIEW Datalogging and Supervisory
                                   Control Module.

                                  Gets or sets the name of the Rate of Change alarm for a
Alarming:RateOfChange:Name      shared variable. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                  Gets or sets the priority of the Rate of Change alarm for a
Alarming:RateOfChange:Priority     shared variable. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                  Gets or sets the amount of time, in milliseconds, in which a
                                 shared variable value must change at least the value of the
Alarming:RateOfChange:Time       Alarming:RateOfChange:Change property to trigger the Rate
                                      of Change alarm. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                  Gets or sets how the BIT_ARRAY alarm for a shared variable is
Alarming:U32BitField:Ack Type      acknowledged. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                  Gets or sets whether a shared variable generates an alarm
Alarming:U32BitField:Alarm On                           when any bit (1) is in alarm state or only when all bits (0) are


                                                    © National Instruments 9661

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9661 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9662 ordinal=9662 -->
## Property and Method Reference

Property and Method Reference


        Property                           Description

                                                  in alarm state. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                                                       If TRUE, LabVIEW enables alarm logging for the BIT_ARRAY
                                        alarm for a shared variable. The default is FALSE. To use this         Alarming:U32BitField:Allow Log
                                              property, you must install the LabVIEW Datalogging and
                                           Supervisory Control Module.

                                          Gets or sets a descriptive area name for the BIT_ARRAY alarm
         Alarming:U32BitField:Area            for a shared variable. To use this property, you must install
                                           the LabVIEW Datalogging and Supervisory Control Module.

                                          Gets or sets the description of the BIT_ARRAY alarm for a
         Alarming:U32BitField:Description    shared variable. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                                                       If TRUE, LabVIEW enables the BIT_ARRAY alarm for a shared
                                                 variable. The default is FALSE. To use this property, you must         Alarming:U32BitField:Enabled                                                       install the LabVIEW Datalogging and Supervisory Control
                                         Module.

                                          Gets or sets which bits of a shared variable alarm on high, 1,
                                     and which bits alarm on low, 0. To use this property, you         Alarming:U32BitField:InvertMask
                                     must install the LabVIEW Datalogging and Supervisory
                                            Control Module.

                                          Gets or sets the name of the BIT_ARRAY alarm for a shared
        Alarming:U32BitField:Name          variable. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                          Gets or sets the priority of the BIT_ARRAY alarm for a shared
         Alarming:U32BitField:Priority         variable. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                          Gets or sets which bits LabVIEW uses to calculate the alarm
         Alarming:U32BitField:Select Mask    for a shared variable. To use this property, you must install
                                           the LabVIEW Datalogging and Supervisory Control Module.

                                            Sets the data type of the variable to the data type you wire to
        Data Type (Variant)
                                                   this property.

                                          Gets or sets the description of a shared variable. To use this
         Description                          property, you must install the LabVIEW Datalogging and
                                           Supervisory Control Module.

          I/O:Alias Access Type               Gets or sets the access setting of an I/O alias. The default is


9662   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9662 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9663 ordinal=9663 -->
## Property and Method Reference

Property and Method Reference


Property                           Description

                                   Read/Write.

                                  Gets or sets the project path of the I/O variable that the I/OI/O:Alias Project Path                                         alias is bound to.

                                  Gets the index of the I/O channel that corresponds to the I/OI/O:Channel Index
                                       Variable.

I/O:Direction                      Gets the direction of an I/O variable or I/O alias.

                                                         If TRUE, LabVIEW enables the timestamp for an I/O variable.I/O:Enable Timestamp                              The default is FALSE.

I/O:Mode                          Gets whether the variable is an I/O variable or an I/O alias.

                                                         If TRUE, LabVIEW enables network publishing on the I/OI/O:Network Published                                       variable. The default is TRUE.

                                                         If TRUE, LabVIEW enables initial value setting for a shared
                                       variable. The default is FALSE. To use this property, you mustInitial Value:Enabled
                                            install the LabVIEW Datalogging and Supervisory Control
                                 Module.

                                  Gets or sets the initial value for a shared variable. To use this
Initial Value:Initial Value             property, you must install the LabVIEW Datalogging and
                                   Supervisory Control Module.

                                  Gets or sets the deadband for logging a shared variable in the
                                     Citadel historical database. To use this property, you mustLogging:Deadband                                            install the LabVIEW Datalogging and Supervisory Control
                                 Module.

                                                         If TRUE, LabVIEW enables logging for a shared variable. The
Logging:Enabled                     default is FALSE. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                                         If TRUE, LabVIEW logs data for a shared variable. The default
Logging:Log Data                          is FALSE. To use this property, you must install the LabVIEW
                                  Datalogging and Supervisory Control Module.

                                                         If TRUE, LabVIEW logs events for a shared variable. The
Logging:Log Events                  default is FALSE. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.

                                    Sets the logging string format. LabVIEW ignores this property
Logging:String Format                        if the data type of the variable is not a string. To use this
                                     property, you must install the LabVIEW Datalogging and


                                                    © National Instruments 9663

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9663 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9664 ordinal=9664 -->
## Property and Method Reference

Property and Method Reference


        Property                           Description

                                           Supervisory Control Module.

                                          Gets or sets the resolution, in seconds, for logging a shared
                                               variable value in the Citadel historical database. To use this        Logging:Time Resolution                                              property, you must install the LabVIEW Datalogging and
                                           Supervisory Control Module.

                                          Gets or sets the resolution, in engineering units, for logging
                                           the shared variable value in the Citadel historical database.         Logging:Value Resolution                                       To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

      Name                             Gets or sets the shared variable name.

                                               Specifies whether a shared variable reads, writes, or reads        Network:Access Type
                                     and writes data.

         Network:Buffer Size                Gets or sets the size of the network buffer.

                                          Gets or sets the size, in number of values, of the network
                                                   buffer. For arrays, gets or sets the number of elements in the        Network:Element Size
                                                  array. For strings, gets or sets the number of characters in the
                                                    string.

        Network:Points Per Waveform      The number of points in each waveform in the buffer.

                                               Indicates if the variable is bound to a project item or a URL. If
         Network:Project Binding           TRUE, the variable is bound to a project item. If FALSE, the
                                               variable is bound to a URL.

                                          Gets or sets the path to a shared variable in the active
         Network:Project Path             LabVIEW project to which you want to bind the shared
                                               variable you are configuring.

                                          Gets or sets the path to a shared variable inside another
        Network:URL                        project or to the data item to which you want to bind the
                                         shared variable you are configuring.

                                                                       If TRUE, LabVIEW binds a shared variable to an existing
                                         shared variable in the active project, an existing shared
        Network:Use Binding
                                               variable in another project, or an NI Publish-Subscribe
                                             Protocol data item on the network. The default is FALSE.

                                                                       If TRUE, LabVIEW enables buffering for a shared variable. The
        Network:Use Buffering
                                              default is FALSE.

         Real-Time:Array Length             Gets or sets the length of the array for a shared variable with


9664   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9664 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9665 ordinal=9665 -->
## Property and Method Reference

Property and Method Reference


Property                           Description

                               a fixed length array data type. You can only use this property
                                        in the LabVIEW development system, but you must install the
                              LabVIEW Real-Time Module to make this property available.

                                  Gets or sets the length of the real-time first-in-first-out (FIFO)
                                      buffer for a shared variable. You can only use this property inReal-Time:Buffer Length                                  the LabVIEW development system, but you must install the
                              LabVIEW Real-Time Module to make this property available.

                                  Gets or sets the number of data points for a shared variable
                                  with a Data Type of Waveform. You can only use this propertyReal-Time:Datapoints In Waveform                                        in the LabVIEW development system, but you must install the
                              LabVIEW Real-Time Module to make this property available.

                                                         If TRUE, LabVIEW enables the real-time first-in-first-out (FIFO)
                                     features for a shared variable. The default is FALSE. You can
Real-Time:Enabled                 only use this property in the LabVIEW development system,
                                 but you must install the LabVIEW Real-Time Module to make
                                         this property available.

                                                         If TRUE, LabVIEW uses the configuration you specify in the
                              Use Buffering section of the Network page of the Shared
                                     Variable Properties dialog box to configure the size and
                                 elements of a real-time first-in-first-out (FIFO) buffer for aReal-Time:Use Buffering                                 shared variable. The default is FALSE. You can only use this
                                   property in the LabVIEW development system, but you must
                                            install the LabVIEW Real-Time Module to make this property
                                       available.

                                                         If TRUE, LabVIEW coerces the shared variable data to a range
                              you specify. The default is FALSE. To use this property, youScaling:Coerce
                              must install the LabVIEW Datalogging and Supervisory
                                   Control Module.

                                                         If TRUE, LabVIEW scales the shared variable. The default is
Scaling:Enabled                   FALSE. To use this property, you must install the LabVIEW
                                  Datalogging and Supervisory Control Module.

Scaling:EngUnit                      Specifies the engineering unit for the shared variable.

                                  Gets or sets the full scale, or maximum value, that the Shared
                                     Variable Engine and Human Machine Interface (HMI)
Scaling:Engineering Max             application use for a shared variable when you use linear or
                                 square root scaling. To use this property, you must install the
                              LabVIEW Datalogging and Supervisory Control Module.


                                                    © National Instruments 9665

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9665 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9666 ordinal=9666 -->
## Property and Method Reference

Property and Method Reference


        Property                           Description

                                          Gets or sets the zero scale, or minimum value, that the
                                        Shared Variable Engine and Human Machine Interface (HMI)
         Scaling:Engineering Min             application use for a shared variable when you use linear or
                                         square root scaling. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                                                       If TRUE, LabVIEW inverts the data the server sends before
                                               storing it in a shared variable. The default is FALSE. To use          Scaling:Invert                                                   this property, you must install the LabVIEW Datalogging and
                                           Supervisory Control Module.

                                          Gets or sets the bits that the Shared Variable Engine inverts
                                            before storing them in a shared variable. To use this property,          Scaling:Invert Mask                                      you must install the LabVIEW Datalogging and Supervisory
                                            Control Module.

                                          Gets or sets the full scale, or maximum value, that the server
                                          uses for a shared variable when you use linear or square root        Scaling:Raw Max
                                                  scaling. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                          Gets or sets the zero scale, or minimum value, that the server
                                          uses for a shared variable when you use linear or square root
        Scaling:Raw Min                                                  scaling. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                          Gets or sets the bits the Shared Variable Engine uses for a
         Scaling:Select Mask                shared variable. To use this property, you must install the
                                      LabVIEW Datalogging and Supervisory Control Module.

                                          Gets or sets the type of scaling to perform on a shared
         Scaling:Type                          variable. To use this property, you must install the LabVIEW
                                           Datalogging and Supervisory Control Module.

                                                                       If TRUE, a timestamp value is recorded each time the single-
                                           process shared variable reads data. (Real-Time, Windows) To
                                         view timestamp information and add a timestamp output to
                                           the Shared Variable node, right-click the Shared Variable
         Single-Process:Enable Timestamp
                                     node and select Show Timestamp from the shortcut menu. If
                                                   this property is FALSE, the timestamp output is hidden. You
                                       can use this property only with single-process shared
                                                 variables. The default value is FALSE.

        Type                              Gets or sets the scope of a shared variable.

        Update Deadband:Enabled          Enables the update deadband for a shared variable. If TRUE,

9666   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9666 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9667 ordinal=9667 -->
## Property and Method Reference

Property and Method Reference


 Property                           Description

                               LabVIEW updates the value of a shared variable only if the
                                  percentage difference between the new value and the
                                    previous value equals or exceeds the deadband. The default
                                                is FALSE. To use this property, you must install the LabVIEW
                                   Datalogging and Supervisory Control Module.

                                   Gets or sets the deadband for updating the value of a shared
                                      variable when the value for the binding source changes. To Update Deadband:Source                                 use this property, you must install the LabVIEW Datalogging
                              and Supervisory Control Module.

                                   Gets or sets the deadband for updating the value of a shared
                                      variable when a user writes data to the variable. To use this Update Deadband:User                                      property, you must install the LabVIEW Datalogging and
                                   Supervisory Control Module.

Alarming:BadStatus:AckAlarming:BadStatus:Ack TypeType

Gets or sets how the Bad Status alarm for a shared variable is acknowledged. To use
this property, you must install the LabVIEW Datalogging and Supervisory Control
Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Ack Type option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No


                                                    © National Instruments 9667

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9667 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9668 ordinal=9668 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:BadStatus:AllowAlarming:BadStatus:Allow LogLog

           If TRUE, LabVIEW enables alarm logging for the Bad Status alarm for a shared variable.
      The default is FALSE. To use this property, you must install the LabVIEW Datalogging
      and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Log? option on the Alarming page of the Shared Variable
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9668   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9668 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9669 ordinal=9669 -->
## Property and Method Reference

Property and Method Reference

Alarming:BadStatus:AreaAlarming:BadStatus:Area

Gets or sets a descriptive area name for the Bad Status alarm for a shared variable. To
use this property, you must install the LabVIEW Datalogging and Supervisory Control
Module.

Create alarm areas to acknowledge an entire area of alarms as a single batch
operation.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Area option on the Alarming page of the Shared Variable
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:BadStatus:DescriptionAlarming:BadStatus:Description

Gets or sets the description of the Bad Status alarm for a shared variable. To use this
property, you must install the LabVIEW Datalogging and Supervisory Control Module.

                                                    © National Instruments 9669

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9669 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9670 ordinal=9670 -->
## Property and Method Reference

Property and Method Reference

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Description option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:BadStatus:EnabledAlarming:BadStatus:Enabled

           If TRUE, LabVIEW enables the Bad Status alarm for a shared variable. The default is
       FALSE. To use this property, you must install the LabVIEW Datalogging and Supervisory
       Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Enable Alarm option on the Alarming page of the Shared
       Variable Properties dialog box.


9670   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9670 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9671 ordinal=9671 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:BadStatus:NameAlarming:BadStatus:Name

Gets or sets the name of the Bad Status alarm for a shared variable. To use this
property, you must install the LabVIEW Datalogging and Supervisory Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Name option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No


                                                    © National Instruments 9671

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9671 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9672 ordinal=9672 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:BadStatus:PriorityAlarming:BadStatus:Priority

       Gets or sets the priority of the Bad Status alarm for a shared variable. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.

       Valid values are between 1 and 1000, where 1000 is the highest priority.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Priority option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

9672   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9672 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9673 ordinal=9673 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

Alarming:Boolean:AckAlarming:Boolean:Ack TypeType

Gets or sets how the DISCRETE alarm for a shared variable is acknowledged. To use
this property, you must install the LabVIEW Datalogging and Supervisory Control
Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Ack Type option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Boolean:AlarmAlarming:Boolean:Alarm OnOn

Gets or sets whether a shared variable is in alarm state when the value is either high
(TRUE) or low (FALSE). To use this property, you must install the LabVIEW Datalogging

                                                    © National Instruments 9673

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9673 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9674 ordinal=9674 -->
## Property and Method Reference

Property and Method Reference

      and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Alarm On option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:Boolean:AllowAlarming:Boolean:Allow LogLog

           If TRUE, LabVIEW enables alarm logging for the DISCRETE alarm for a shared variable.
      The default is FALSE. To use this property, you must install the LabVIEW Datalogging
      and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Log? option on the Alarming page of the Shared Variable
       Properties dialog box.


9674   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9674 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9675 ordinal=9675 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Boolean:AreaAlarming:Boolean:Area

Gets or sets a descriptive area name for the DISCRETE alarm for a shared variable. To
use this property, you must install the LabVIEW Datalogging and Supervisory Control
Module.

Create alarm areas to acknowledge an entire area of alarms as a single batch
operation.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Area option on the Alarming page of the Shared Variable
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9675

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9675 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9676 ordinal=9676 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:Boolean:DescriptionAlarming:Boolean:Description

       Gets or sets the description of the DISCRETE alarm for a shared variable. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Description option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No


9676   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9676 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9677 ordinal=9677 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Boolean:EnabledAlarming:Boolean:Enabled

If TRUE, LabVIEW enables the DISCRETE alarm for a shared variable. The default is
FALSE. To use this property, you must install the LabVIEW Datalogging and Supervisory
Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Enable Alarm option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9677

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9677 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9678 ordinal=9678 -->
## Property and Method Reference

Property and Method Reference

   Alarming:Boolean:NameAlarming:Boolean:Name

       Gets or sets the name of the DISCRETE alarm for a shared variable. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Name option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:Boolean:PriorityAlarming:Boolean:Priority

       Gets or sets the priority of the DISCRETE alarm for a shared variable. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.

       Valid values are between 1 and 1000, where 1000 is the highest priority.


9678   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9678 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9679 ordinal=9679 -->
## Property and Method Reference

Property and Method Reference

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Priority option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:EnabledAlarming:Enabled

If TRUE, LabVIEW enables alarming for a shared variable. The default is FALSE. To use
this property, you must install the LabVIEW Datalogging and Supervisory Control
Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Enable Alarming option on the Alarming page of the
Shared Variable Properties dialog box.


                                                    © National Instruments 9679

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9679 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9680 ordinal=9680 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:EventAlarming:Event OnOn DataData ChangeChange

           If TRUE, LabVIEW sets an event for a shared variable when data changes. The default is
       FALSE. To use this property, you must install the LabVIEW Datalogging and Supervisory
       Control Module.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

9680   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9680 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9681 ordinal=9681 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:EventAlarming:Event OnOn UserUser InputInput OnlyOnly

If TRUE, the value change event is generated on user input only. The default is TRUE.
To use this property, you must install the LabVIEW Datalogging and Supervisory
Control Module.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Hi:AckAlarming:Hi:Ack TypeType

Gets or sets how the HI alarm for a shared variable is acknowledged. To use this
property, you must install the LabVIEW Datalogging and Supervisory Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Ack Type option on the Alarming page of the Shared

                                                    © National Instruments 9681

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9681 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9682 ordinal=9682 -->
## Property and Method Reference

Property and Method Reference

       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:Hi:AllowAlarming:Hi:Allow LogLog

           If TRUE, LabVIEW enables alarm logging for the HI alarm for a shared variable. The
       default is FALSE. To use this property, you must install the LabVIEW Datalogging and
       Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Log? option on the Alarming page of the Shared Variable
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type


9682   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9682 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9683 ordinal=9683 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Hi:AreaAlarming:Hi:Area

Gets or sets a descriptive area name for the HI alarm for a shared variable. To use this
property, you must install the LabVIEW Datalogging and Supervisory Control Module.

Create alarm areas to acknowledge an entire area of alarms as a single batch
operation.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Area option on the Alarming page of the Shared Variable
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes


                                                    © National Instruments 9683

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9683 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9684 ordinal=9684 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:Hi:DeadbandAlarming:Hi:Deadband

       Gets or sets the HI alarm deadband as a percentage of the full scale range. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.

      A shared variable does not return to a normal state until it has left the alarm condition
       set by the value of the Alarming:Hi:Level property by at least the value of the
      deadband. If you set the deadband too high, the shared variable value might not clear
       the alarm.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Deadband/Time option on the Alarming page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No


9684   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9684 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9685 ordinal=9685 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Hi:DescriptionAlarming:Hi:Description

Gets or sets the description of the HI alarm for a shared variable. To use this property,
you must install the LabVIEW Datalogging and Supervisory Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Description option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Hi:EnabledAlarming:Hi:Enabled

If TRUE, LabVIEW enables the HI alarm for a shared variable. The default is FALSE. To
use this property, you must install the LabVIEW Datalogging and Supervisory Control

                                                    © National Instruments 9685

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9685 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9686 ordinal=9686 -->
## Property and Method Reference

Property and Method Reference

      Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Enable Alarm option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:Hi:LevelAlarming:Hi:Level

       Gets or sets the value, in engineering units, that evokes the HI alarm condition for a
      shared variable. To use this property, you must install the LabVIEW Datalogging and
       Supervisory Control Module.

      The shared variable remains in the alarm state until the shared variable value goes
      below this value minus the deadband value.

           Note You can enable alarming only for network-published shared variables.


9686   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9686 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9687 ordinal=9687 -->
## Property and Method Reference

Property and Method Reference

This property is similar to the Level/Change option on the Alarming page of the
Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Hi:NameAlarming:Hi:Name

Gets or sets the name of the HI alarm for a shared variable. To use this property, you
must install the LabVIEW Datalogging and Supervisory Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Name option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 9687

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9687 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9688 ordinal=9688 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:Hi:PriorityAlarming:Hi:Priority

       Gets or sets the priority of the HI alarm for a shared variable. To use this property, you
      must install the LabVIEW Datalogging and Supervisory Control Module.

       Valid values are between 1 and 1000, where 1000 is the highest priority.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Priority option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

9688   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9688 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9689 ordinal=9689 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:HiHi:AckAlarming:HiHi:Ack TypeType

Gets or sets how the HI_HI alarm for a shared variable is acknowledged. To use this
property, you must install the LabVIEW Datalogging and Supervisory Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Ack Type option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9689

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9689 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9690 ordinal=9690 -->
## Property and Method Reference

Property and Method Reference

    Alarming:HiHi:AllowAlarming:HiHi:Allow LogLog

           If TRUE, LabVIEW enables alarm logging for the HI_HI alarm for a shared variable. The
       default is FALSE. To use this property, you must install the LabVIEW Datalogging and
       Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Log? option on the Alarming page of the Shared Variable
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:HiHi:AreaAlarming:HiHi:Area

       Gets or sets a descriptive area name for the HI_HI alarm for a shared variable. To use
        this property, you must install the LabVIEW Datalogging and Supervisory Control
      Module.

       Create alarm areas to acknowledge an entire area of alarms as a single batch

9690   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9690 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9691 ordinal=9691 -->
## Property and Method Reference

Property and Method Reference

operation.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Area option on the Alarming page of the Shared Variable
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:HiHi:DeadbandAlarming:HiHi:Deadband

Gets or sets the HI_HI alarm deadband as a percentage of the full scale range. To use
this property, you must install the LabVIEW Datalogging and Supervisory Control
Module.

A shared variable does not return to a normal state until it has left the alarm condition
set by the value of the Alarming:HiHi:Level property by at least the value of the
deadband. If you set the deadband too high, the shared variable value might not clear
the alarm.


                                                    © National Instruments 9691

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9691 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9692 ordinal=9692 -->
## Property and Method Reference

Property and Method Reference

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Deadband/Time option on the Alarming page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:HiHi:DescriptionAlarming:HiHi:Description

       Gets or sets the description of the HI_HI alarm for a shared variable. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Description option on the Alarming page of the Shared
       Variable Properties dialog box.


9692   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9692 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9693 ordinal=9693 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:HiHi:EnabledAlarming:HiHi:Enabled

If TRUE, LabVIEW enables the HI_HI alarm for a shared variable. The default is FALSE.
To use this property, you must install the LabVIEW Datalogging and Supervisory
Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Enable Alarm option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 9693

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9693 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9694 ordinal=9694 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:HiHi:LevelAlarming:HiHi:Level

       Gets or sets the value, in engineering units, that evokes the HI_HI alarm condition for a
      shared variable. To use this property, you must install the LabVIEW Datalogging and
       Supervisory Control Module.

      The shared variable remains in the alarm state until the shared variable value goes
      below this value minus the deadband value.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Level/Change option on the Alarming page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes


9694   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9694 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9695 ordinal=9695 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:HiHi:NameAlarming:HiHi:Name

Gets or sets the name of the HI_HI alarm for a shared variable. To use this property,
you must install the LabVIEW Datalogging and Supervisory Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Name option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9695

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9695 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9696 ordinal=9696 -->
## Property and Method Reference

Property and Method Reference

    Alarming:HiHi:PriorityAlarming:HiHi:Priority

       Gets or sets the priority of the HI_HI alarm for a shared variable. To use this property,
      you must install the LabVIEW Datalogging and Supervisory Control Module.

       Valid values are between 1 and 1000, where 1000 is the highest priority.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Priority option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:Lo:AckAlarming:Lo:Ack TypeType

       Gets or sets how the LO alarm for a shared variable is acknowledged. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.


9696   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9696 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9697 ordinal=9697 -->
## Property and Method Reference

Property and Method Reference

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Ack Type option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Lo:AllowAlarming:Lo:Allow LogLog

If TRUE, LabVIEW enables alarm logging for the LO alarm for a shared variable. The
default is FALSE. To use this property, you must install the LabVIEW Datalogging and
Supervisory Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Log? option on the Alarming page of the Shared Variable
Properties dialog box.


                                                    © National Instruments 9697

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9697 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9698 ordinal=9698 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:Lo:AreaAlarming:Lo:Area

       Gets or sets a descriptive area name for the LO alarm for a shared variable. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.

       Create alarm areas to acknowledge an entire area of alarms as a single batch
       operation.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Area option on the Alarming page of the Shared Variable
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type


9698   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9698 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9699 ordinal=9699 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Lo:DeadbandAlarming:Lo:Deadband

Gets or sets the LO alarm deadband as a percentage of the full scale range. To use this
property, you must install the LabVIEW Datalogging and Supervisory Control Module.

A shared variable does not return to a normal state until it has left the alarm condition
set by the value of the Alarming:Lo:Level property by at least the value of the
deadband. If you set the deadband too high, the shared variable value might not clear
the alarm.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Deadband/Time option on the Alarming page of the
Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No


                                                    © National Instruments 9699

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9699 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9700 ordinal=9700 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:Lo:DescriptionAlarming:Lo:Description

       Gets or sets the description of the LO alarm for a shared variable. To use this property,
      you must install the LabVIEW Datalogging and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Description option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9700   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9700 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9701 ordinal=9701 -->
## Property and Method Reference

Property and Method Reference

Alarming:Lo:EnabledAlarming:Lo:Enabled

If TRUE, LabVIEW enables the LO alarm for a shared variable. The default is FALSE. To
use this property, you must install the LabVIEW Datalogging and Supervisory Control
Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Enable Alarm option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Lo:LevelAlarming:Lo:Level

Gets or sets the value, in engineering units, that evokes the LO alarm condition for a
shared variable. To use this property, you must install the LabVIEW Datalogging and
Supervisory Control Module.

The shared variable remains in the alarm state until the shared variable value exceeds

                                                    © National Instruments 9701

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9701 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9702 ordinal=9702 -->
## Property and Method Reference

Property and Method Reference

        this value plus the deadband value.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Level/Change option on the Alarming page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:Lo:NameAlarming:Lo:Name

       Gets or sets the name of the LO alarm for a shared variable. To use this property, you
      must install the LabVIEW Datalogging and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Name option on the Alarming page of the Shared
       Variable Properties dialog box.


9702   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9702 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9703 ordinal=9703 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:Lo:PriorityAlarming:Lo:Priority

Gets or sets the priority of the LO alarm for a shared variable. To use this property, you
must install the LabVIEW Datalogging and Supervisory Control Module.

Valid values are between 1 and 1000, where 1000 is the highest priority.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Priority option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

                                                    © National Instruments 9703

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9703 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9704 ordinal=9704 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:LoLo:AckAlarming:LoLo:Ack TypeType

       Gets or sets how the LO_LO alarm for a shared variable is acknowledged. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Ack Type option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


9704   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9704 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9705 ordinal=9705 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

Alarming:LoLo:AllowAlarming:LoLo:Allow LogLog

If TRUE, LabVIEW enables alarm logging for the LO_LO alarm for a shared variable. The
default is FALSE. To use this property, you must install the LabVIEW Datalogging and
Supervisory Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Log? option on the Alarming page of the Shared Variable
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:LoLo:AreaAlarming:LoLo:Area

Gets or sets a descriptive area name for the LO_LO alarm for a shared variable. To use
this property, you must install the LabVIEW Datalogging and Supervisory Control

                                                    © National Instruments 9705

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9705 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9706 ordinal=9706 -->
## Property and Method Reference

Property and Method Reference

      Module.

       Create alarm areas to acknowledge an entire area of alarms as a single batch
       operation.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Area option on the Alarming page of the Shared Variable
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:LoLo:DeadbandAlarming:LoLo:Deadband

       Gets or sets the LO_LO alarm deadband as a percentage of the full scale range. To use
        this property, you must install the LabVIEW Datalogging and Supervisory Control
      Module.

      A shared variable does not return to a normal state until it has left the alarm condition
       set by the value of the Alarming:LoLo:Level property by at least the value of the
      deadband. If you set the deadband too high, the shared variable value might not clear

9706   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9706 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9707 ordinal=9707 -->
## Property and Method Reference

Property and Method Reference

the alarm.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Deadband/Time option on the Alarming page of the
Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:LoLo:DescriptionAlarming:LoLo:Description

Gets or sets the description of the LO_LO alarm for a shared variable. To use this
property, you must install the LabVIEW Datalogging and Supervisory Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Description option on the Alarming page of the Shared
Variable Properties dialog box.


                                                    © National Instruments 9707

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9707 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9708 ordinal=9708 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:LoLo:EnabledAlarming:LoLo:Enabled

           If TRUE, LabVIEW enables the LO_LO alarm for a shared variable. The default is FALSE.
      To use this property, you must install the LabVIEW Datalogging and Supervisory
       Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Enable Alarm option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


9708   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9708 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9709 ordinal=9709 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:LoLo:LevelAlarming:LoLo:Level

Gets or sets the value, in engineering units, that evokes the LO_LO alarm condition for
a shared variable. To use this property, you must install the LabVIEW Datalogging and
Supervisory Control Module.

The shared variable remains in the alarm state until the shared variable value exceeds
this value plus the deadband value.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Level/Change option on the Alarming page of the
Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes


                                                    © National Instruments 9709

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9709 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9710 ordinal=9710 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:LoLo:NameAlarming:LoLo:Name

       Gets or sets the name of the LO_LO alarm for a shared variable. To use this property,
      you must install the LabVIEW Datalogging and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Name option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9710   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9710 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9711 ordinal=9711 -->
## Property and Method Reference

Property and Method Reference

Alarming:LoLo:PriorityAlarming:LoLo:Priority

Gets or sets the priority of the LO_LO alarm for a shared variable. To use this property,
you must install the LabVIEW Datalogging and Supervisory Control Module.

Valid values are between 1 and 1000, where 1000 is the highest priority.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Priority option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:RateOfChange:AckAlarming:RateOfChange:Ack TypeType

Gets or sets how the Rate of Change alarm for a shared variable is acknowledged. To
use this property, you must install the LabVIEW Datalogging and Supervisory Control
Module.


                                                    © National Instruments 9711

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9711 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9712 ordinal=9712 -->
## Property and Method Reference

Property and Method Reference

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Ack Type option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:RateOfChange:AllowAlarming:RateOfChange:Allow LogLog

           If TRUE, LabVIEW enables alarm logging for the Rate of Change alarm for a shared
        variable. The default is FALSE. To use this property, you must install the LabVIEW
       Datalogging and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Log? option on the Alarming page of the Shared Variable
       Properties dialog box.


9712   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9712 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9713 ordinal=9713 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:RateOfChange:AreaAlarming:RateOfChange:Area

Gets or sets a descriptive area name for the Rate of Change alarm for a shared variable.
To use this property, you must install the LabVIEW Datalogging and Supervisory
Control Module.

Create alarm areas to acknowledge an entire area of alarms as a single batch
operation.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Area option on the Alarming page of the Shared Variable
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9713

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9713 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9714 ordinal=9714 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:RateOfChange:ChangeAlarming:RateOfChange:Change

       Gets or sets the value that a shared variable value must change in the specified time to
        trigger the Rate of Change alarm. To use this property, you must install the LabVIEW
       Datalogging and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Level/Change option on the Alarming page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes


9714   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9714 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9715 ordinal=9715 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:RateOfChange:DescriptionAlarming:RateOfChange:Description

Gets or sets the description of the Rate of Change alarm for a shared variable. To use
this property, you must install the LabVIEW Datalogging and Supervisory Control
Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Description option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9715

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9715 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9716 ordinal=9716 -->
## Property and Method Reference

Property and Method Reference

   Alarming:RateOfChange:EnabledAlarming:RateOfChange:Enabled

           If TRUE, LabVIEW enables the Rate of Change alarm for a shared variable. The default is
       FALSE. To use this property, you must install the LabVIEW Datalogging and Supervisory
       Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Enable Alarm option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:RateOfChange:NameAlarming:RateOfChange:Name

       Gets or sets the name of the Rate of Change alarm for a shared variable. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.


9716   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9716 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9717 ordinal=9717 -->
## Property and Method Reference

Property and Method Reference

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Name option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:RateOfChange:PriorityAlarming:RateOfChange:Priority

Gets or sets the priority of the Rate of Change alarm for a shared variable. To use this
property, you must install the LabVIEW Datalogging and Supervisory Control Module.

Valid values are between 1 and 1000, where 1000 is the highest priority.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Priority option on the Alarming page of the Shared
Variable Properties dialog box.


                                                    © National Instruments 9717

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9717 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9718 ordinal=9718 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Alarming:RateOfChange:TimeAlarming:RateOfChange:Time

       Gets or sets the amount of time, in milliseconds, in which a shared variable value must
      change at least the value of the Alarming:RateOfChange:Change property to trigger the
       Rate of Change alarm. To use this property, you must install the LabVIEW Datalogging
      and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Deadband/Time option on the Alarming page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type


9718   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9718 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9719 ordinal=9719 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:U32BitField:AckAlarming:U32BitField:Ack TypeType

Gets or sets how the BIT_ARRAY alarm for a shared variable is acknowledged. To use
this property, you must install the LabVIEW Datalogging and Supervisory Control
Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Ack Type option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No


                                                    © National Instruments 9719

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9719 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9720 ordinal=9720 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:U32BitField:AlarmAlarming:U32BitField:Alarm OnOn

       Gets or sets whether a shared variable generates an alarm when any bit (1) is in alarm
        state or only when all bits (0) are in alarm state. To use this property, you must install
       the LabVIEW Datalogging and Supervisory Control Module.

       This option is valid only when the Alarming:U32BitField:Enabled property is TRUE.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Alarm On option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9720   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9720 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9721 ordinal=9721 -->
## Property and Method Reference

Property and Method Reference

Alarming:U32BitField:AllowAlarming:U32BitField:Allow LogLog

If TRUE, LabVIEW enables alarm logging for the BIT_ARRAY alarm for a shared variable.
The default is FALSE. To use this property, you must install the LabVIEW Datalogging
and Supervisory Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Log? option on the Alarming page of the Shared Variable
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:U32BitField:AreaAlarming:U32BitField:Area

Gets or sets a descriptive area name for the BIT_ARRAY alarm for a shared variable. To
use this property, you must install the LabVIEW Datalogging and Supervisory Control
Module.

Create alarm areas to acknowledge an entire area of alarms as a single batch

                                                    © National Instruments 9721

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9721 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9722 ordinal=9722 -->
## Property and Method Reference

Property and Method Reference

       operation.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Area option on the Alarming page of the Shared Variable
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:U32BitField:DescriptionAlarming:U32BitField:Description

       Gets or sets the description of the BIT_ARRAY alarm for a shared variable. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Description option on the Alarming page of the Shared
       Variable Properties dialog box.


9722   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9722 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9723 ordinal=9723 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:U32BitField:EnabledAlarming:U32BitField:Enabled

If TRUE, LabVIEW enables the BIT_ARRAY alarm for a shared variable. The default is
FALSE. To use this property, you must install the LabVIEW Datalogging and Supervisory
Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Enable Alarm option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 9723

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9723 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9724 ordinal=9724 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:U32BitField:InvertMaskAlarming:U32BitField:InvertMask

       Gets or sets which bits of a shared variable alarm on high, 1, and which bits alarm on
       low, 0. To use this property, you must install the LabVIEW Datalogging and Supervisory
       Control Module.

       Enter the value 1 if you want that bit to alarm when low. In bitwise terminology, the
      Shared Variable Engine performs an XOR with the invert mask value to produce the
      alarm state. LabVIEW applies the invert mask value to the scaled value after applying
      any relevant scaling masks.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Invert option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

9724   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9724 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9725 ordinal=9725 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Alarming:U32BitField:NameAlarming:U32BitField:Name

Gets or sets the name of the BIT_ARRAY alarm for a shared variable. To use this
property, you must install the LabVIEW Datalogging and Supervisory Control Module.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Name option on the Alarming page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9725

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9725 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9726 ordinal=9726 -->
## Property and Method Reference

Property and Method Reference

    Alarming:U32BitField:PriorityAlarming:U32BitField:Priority

       Gets or sets the priority of the BIT_ARRAY alarm for a shared variable. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.

       Valid values are between 1 and 1000, where 1000 is the highest priority.

           Note You can enable alarming only for network-published shared variables.

       This property is similar to the Priority option on the Alarming page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Alarming:U32BitField:SelectAlarming:U32BitField:Select MaskMask

       Gets or sets which bits LabVIEW uses to calculate the alarm for a shared variable. To
      use this property, you must install the LabVIEW Datalogging and Supervisory Control
      Module.


9726   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9726 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9727 ordinal=9727 -->
## Property and Method Reference

Property and Method Reference

LabVIEW uses bits that are 1 in the alarm calculation. Bits that are 0 do not cause an
alarm, regardless of their value. In bitwise terminology, the Shared Variable Engine
performs an AND with the select mask value to produce the alarm state. LabVIEW
applies the select mask value to the scaled value after applying any relevant scaling
masks.

      Note You can enable alarming only for network-published shared variables.

This property is similar to the Mask option on theAlarming page of the Shared Variable
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DataData TypeType (Variant)(Variant)

Sets the data type of the variable to the data type you wire to this property.

An error occurs if you attempt to set this property when the VI is running.

This property is similar to the Data Type option on the Variable page of the Shared
Variable Properties dialog box.

                                                    © National Instruments 9727

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9727 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9728 ordinal=9728 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    DescriptionDescription

       Gets or sets the description of a shared variable. To use this property, you must install
       the LabVIEW Datalogging and Supervisory Control Module.

       This property is similar to the Description option on the Description page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes


9728   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9728 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9729 ordinal=9729 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

I/O:AliasI/O:Alias AccessAccess TypeType

Gets or sets the access setting of an I/O alias. The default is Read/Write.

This property returns an error when called on a non-alias I/O variable.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

I/O:AliasI/O:Alias ProjectProject PathPath

Gets or sets the project path of the I/O variable that the I/O alias is bound to.

This property returns an error when called on a non-alias I/O variable.


                                                    © National Instruments 9729

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9729 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9730 ordinal=9730 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    I/O:ChannelI/O:Channel IndexIndex

       Gets the index of the I/O channel that corresponds to the I/O Variable.

       This property returns an error when called on an I/O Alias.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

9730   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9730 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9731 ordinal=9731 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

I/O:DirectionI/O:Direction

Gets the direction of an I/O variable or I/O alias.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

I/O:EnableI/O:Enable TimestampTimestamp

If TRUE, LabVIEW enables the timestamp for an I/O variable. The default is FALSE.

This property is similar to the Enable Timestamping option on the shared variable
properties dialog box. This property returns an error if called on an I/O alias.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9731

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9731 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9732 ordinal=9732 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   I/O:ModeI/O:Mode

       Gets whether the variable is an I/O variable or an I/O alias.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes


9732   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9732 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9733 ordinal=9733 -->
## Property and Method Reference

Property and Method Reference

I/O:NetworkI/O:Network PublishedPublished

If TRUE, LabVIEW enables network publishing on the I/O variable. The default is TRUE.

This property is similar to the Enable Network Publishing option on the Variable page
of the Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

InitialInitial Value:EnabledValue:Enabled

If TRUE, LabVIEW enables initial value setting for a shared variable. The default is
FALSE. To use this property, you must install the LabVIEW Datalogging and Supervisory
Control Module.

This property is similar to the Enable Initial Value option on the Initial Value page of
the Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 9733

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9733 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9734 ordinal=9734 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

     InitialInitial Value:InitialValue:Initial ValueValue

       Gets or sets the initial value for a shared variable. To use this property, you must install
       the LabVIEW Datalogging and Supervisory Control Module.

       This property is similar to the Initial Value option on the Initial Value page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


9734   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9734 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9735 ordinal=9735 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

Logging:DeadbandLogging:Deadband

Gets or sets the deadband for logging a shared variable in the Citadel historical
database. To use this property, you must install the LabVIEW Datalogging and
Supervisory Control Module.

Use this option to improve the performance of an application by limiting unnecessary
datalogging. LabVIEW logs a new shared variable value only if that value differs by at
least the deadband value from the value previously logged. The default value is 0%,
which logs each new value for the shared variable. This option is available only for
shared variables with a Data Type of Double or Single.

      Note You can enable logging only for network-published shared variables.

This property is similar to the Value Deadband option on the Logging page of the
Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9735

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9735 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9736 ordinal=9736 -->
## Property and Method Reference

Property and Method Reference

   Logging:EnabledLogging:Enabled

           If TRUE, LabVIEW enables logging for a shared variable. The default is FALSE. To use
        this property, you must install the LabVIEW Datalogging and Supervisory Control
      Module.

           Note You can enable logging only for network-published shared variables.

       This property is similar to the Enable Logging option on the Logging page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Logging:LogLogging:Log DataData

           If TRUE, LabVIEW logs data for a shared variable. The default is FALSE. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.


9736   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9736 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9737 ordinal=9737 -->
## Property and Method Reference

Property and Method Reference

      Note You can enable logging only for network-published shared variables.

This property is similar to the Log Data option on the Logging page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Logging:LogLogging:Log EventsEvents

If TRUE, LabVIEW logs events for a shared variable. The default is FALSE. To use this
property, you must install the LabVIEW Datalogging and Supervisory Control Module.

      Note You can enable logging only for network-published shared variables.

This property is similar to the Log Events option on the Logging page of the Shared
Variable Properties dialog box.


                                                    © National Instruments 9737

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9737 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9738 ordinal=9738 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Logging:StringLogging:String FormatFormat

       Sets the logging string format. LabVIEW ignores this property if the data type of the
       variable is not a string. To use this property, you must install the LabVIEW Datalogging
      and Supervisory Control Module.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

9738   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9738 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9739 ordinal=9739 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Logging:TimeLogging:Time ResolutionResolution

Gets or sets the resolution, in seconds, for logging a shared variable value in the
Citadel historical database. To use this property, you must install the LabVIEW
Datalogging and Supervisory Control Module.

      Note You can enable logging only for network-published shared variables.

This property is similar to the Time Resolution (sec) option on the Logging page of the
Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Logging:ValueLogging:Value ResolutionResolution

Gets or sets the resolution, in engineering units, for logging the shared variable value

                                                    © National Instruments 9739

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9739 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9740 ordinal=9740 -->
## Property and Method Reference

Property and Method Reference

        in the Citadel historical database. To use this property, you must install the LabVIEW
       Datalogging and Supervisory Control Module.

      LabVIEW writes shared variables to the Citadel historical database in compressed
       format with the specified resolution. The default value is 0.1. Enter a value of 0.0 to
       write the exact value of the shared variable to the Citadel historical database. Logging
       the exact value requires more time and disk space. This option is available only for
      shared variables with a Data Type of Double or Single.

           Note You can enable logging only for network-published shared variables.

       This property is similar to the Value Resolution option on the Logging page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   NameName

       Gets or sets the shared variable name.

      An error occurs if you attempt to set this property when the VI is running.

9740   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9740 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9741 ordinal=9741 -->
## Property and Method Reference

Property and Method Reference

This property is similar to the Name option on the Variable page of the Shared Variable
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Network:AccessNetwork:Access TypeType

Specifies whether a shared variable reads, writes, or reads and writes data.

Valid values are 0 (read only), 1 (write only), and 2 (read/write).

If you set this property to 0 (read only) or 1 (write only), you can create shared
variables that are configured only to read data or write data, respectively. When you
right-click a shared variable that is bound to a source that is read or write only, the
Change to Write and Change to Read options are disabled in the shortcut menu.

An error occurs if you attempt to set this property when the VI is running.

This property is similar to the Access Type option on the Variable page of the Shared
Variable Properties dialog box.


                                                    © National Instruments 9741

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9741 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9742 ordinal=9742 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Network:BufferNetwork:Buffer SizeSize

       Gets or sets the size of the network buffer.

      LabVIEW returns the size of the buffer in bytes. However, if the buffer data type is an
        Integer, such as an 8-bit signed integer, an 8-bit unsigned integer, a 16-bit signed
        integer, a 16-bit unsigned integer, and so on; a Boolean; a single-precision floating-
       point or double-precision floating-point; a 16-bit integer of waveforms or double
      waveforms; a 1D array of all types; or strings, LabVIEW returns the buffer size in those
       data types. For example, for a 16-bit integer, LabVIEW returns the number of 16-bit
        integers. For a 1D array, LabVIEW returns the number of arrays.

      An error occurs if you attempt to set this property when the VI is running.

      Use the Network:Element Size property to set the size of arrays or strings, and use the
       Network:Points Per Waveform property to set the size of waveforms.

       This property is similar to the Size option on the Network page of the Shared Variable
       Properties dialog box.


9742   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9742 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9743 ordinal=9743 -->
## Property and Method Reference

Property and Method Reference

LabVIEW uses the Network:Buffer Size, Network:Element Size, and Network:Points Per
Waveform properties as appropriate to calculate the network buffer size for a network-
published shared variable.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Network:ElementNetwork:Element SizeSize

Gets or sets the size, in number of values, of the network buffer. For arrays, gets or sets
the number of elements in the array. For strings, gets or sets the number of characters
in the string.

An error occurs if you attempt to set this property when the VI is running.

This property is similar to the Number of option on the Network page of the Shared
Variable Properties dialog box.

LabVIEW uses the Network:Buffer Size, Network:Element Size, and Network:Points Per
Waveform properties as appropriate to calculate the network buffer size for a network-
published shared variable.


                                                    © National Instruments 9743

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9743 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9744 ordinal=9744 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Network:PointsNetwork:Points PerPer WaveformWaveform

      The number of points in each waveform in the buffer.

      LabVIEW uses the Network:Buffer Size, Network:Element Size, and Network:Points Per
      Waveform properties as appropriate to calculate the network buffer size for a network-
       published shared variable.

      An error occurs if you attempt to set this property when the VI is running.

       This property is similar to the Waveform Size option on the Network page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

9744   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9744 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9745 ordinal=9745 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Network:ProjectNetwork:Project BindingBinding

Indicates if the variable is bound to a project item or a URL. If TRUE, the variable is
bound to a project item. If FALSE, the variable is bound to a URL.

An error occurs if you attempt to set this property when the VI is running.

This property is similar to the Enable Aliasing option on the Variable page of the
Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9745

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9745 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9746 ordinal=9746 -->
## Property and Method Reference

Property and Method Reference

    Network:ProjectNetwork:Project PathPath

       Gets or sets the path to a shared variable in the active LabVIEW project to which you
      want to bind the shared variable you are configuring.

      The project path consists of the library in which the shared variable resides and the
      shared variable name: library\project_variable.

      An error occurs if you attempt to set this property when the VI is running.

       This property is similar to the Project Path option on the Variable page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Network:URLNetwork:URL

       Gets or sets the path to a shared variable inside another project or to the data item to
      which you want to bind the shared variable you are configuring.

      The network path to shared variables in other projects consists of the computer name,

9746   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9746 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9747 ordinal=9747 -->
## Property and Method Reference

Property and Method Reference

the name of the library in which the shared variable resides, and the shared variable
name: \\computer\library\project_variable. The network path to an NI
Publish-Subscribe Protocol (NI-PSP) data item consists of the computer name, the
name of the process in which the data item resides, and the data item name:
\\computer\process\data_item.

This property is similar to the Network Path option on the Variable page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Network:UseNetwork:Use BindingBinding

If TRUE, LabVIEW binds a shared variable to an existing shared variable in the active
project, an existing shared variable in another project, or an NI Publish-Subscribe
Protocol data item on the network. The default is FALSE.

An error occurs if you attempt to set this property when the VI is running.

This property is similar to the Enable Aliasing option on the Variable page of the
Shared Variable Properties dialog box.


                                                    © National Instruments 9747

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9747 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9748 ordinal=9748 -->
## Property and Method Reference

Property and Method Reference

           Note You can bind front panel objects only to network-published shared
                variables.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Network:UseNetwork:Use BufferingBuffering

           If TRUE, LabVIEW enables buffering for a shared variable. The default is FALSE.

      An error occurs if you attempt to set this property when the VI is running.

       This property is similar to the Use Buffering option on the Network page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

9748   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9748 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9749 ordinal=9749 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Real-Time:ArrayReal-Time:Array LengthLength

Gets or sets the length of the array for a shared variable with a fixed length array data
type. You can only use this property in the LabVIEW development system, but you
must install the LabVIEW Real-Time Module to make this property available.

An error occurs if you attempt to set this property when the VI is running.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9749

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9749 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9750 ordinal=9750 -->
## Property and Method Reference

Property and Method Reference

    Real-Time:BufferReal-Time:Buffer LengthLength

       Gets or sets the length of the real-time first-in-first-out (FIFO) buffer for a shared
        variable. You can only use this property in the LabVIEW development system, but you
      must install the LabVIEW Real-Time Module to make this property available.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Real-Time:DatapointsReal-Time:Datapoints InIn WaveformWaveform

       Gets or sets the number of data points for a shared variable with a Data Type of
      Waveform. You can only use this property in the LabVIEW development system, but
      you must install the LabVIEW Real-Time Module to make this property available.

      An error occurs if you attempt to set this property when the VI is running.

     Remarks

      The following table lists the characteristics of this property.


9750   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9750 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9751 ordinal=9751 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Real-Time:EnabledReal-Time:Enabled

If TRUE, LabVIEW enables the real-time first-in-first-out (FIFO) features for a shared
variable. The default is FALSE. You can only use this property in the LabVIEW
development system, but you must install the LabVIEW Real-Time Module to make this
property available.

An error occurs if you attempt to set this property when the VI is running.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No


                                                    © National Instruments 9751

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9751 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9752 ordinal=9752 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Real-Time:UseReal-Time:Use BufferingBuffering

           If TRUE, LabVIEW uses the configuration you specify in the Use Buffering section of the
      Network page of the Shared Variable Properties dialog box to configure the size and
      elements of a real-time first-in-first-out (FIFO) buffer for a shared variable. The default
         is FALSE. You can only use this property in the LabVIEW development system, but you
      must install the LabVIEW Real-Time Module to make this property available.

      An error occurs if you attempt to set this property when the VI is running.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Scaling:CoerceScaling:Coerce

           If TRUE, LabVIEW coerces the shared variable data to a range you specify. The default is
       FALSE. To use this property, you must install the LabVIEW Datalogging and Supervisory
       Control Module.

9752   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9752 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9753 ordinal=9753 -->
## Property and Method Reference

Property and Method Reference

You can use this property for shared variables with a Scale Type of Linear.

If you scale the data for a shared variable you can write, the data must be between the
Scaling:Raw Min and Scaling:Raw Max values. If you scale the data for a shared
variable you can read, the data must be between the Scaling:Engineering Min and
Scaling:Engineering Max values.

This property is similar to the Coerce to Range option on the Scaling page of the
Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Scaling:EnabledScaling:Enabled

If TRUE, LabVIEW scales the shared variable. The default is FALSE. To use this property,
you must install the LabVIEW Datalogging and Supervisory Control Module.

      Note You can use scaling only for network-published shared variables, I/O
        variables, or I/O aliases. When the shared variable you want to scale is a
       network-published shared variable, it must also have a data source.


                                                    © National Instruments 9753

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9753 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9754 ordinal=9754 -->
## Property and Method Reference

Property and Method Reference


              Configure a network-published shared variable to have a data source by
               placing a checkmark in the Enable Aliasing checkbox on the Variable page of
              the Shared Variable Properties dialog box.

       This property is similar to the Enable Scaling option on the Scaling page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Scaling:EngUnitScaling:EngUnit

       Specifies the engineering unit for the shared variable.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


9754   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9754 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9755 ordinal=9755 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Scaling:EngineeringScaling:Engineering MaxMax

Gets or sets the full scale, or maximum value, that the Shared Variable Engine and
Human Machine Interface (HMI) application use for a shared variable when you use
linear or square root scaling. To use this property, you must install the LabVIEW
Datalogging and Supervisory Control Module.

You can use this property for shared variables with a Scale Type of Linear.

This property is similar to the Engineering Full Scale option on the Scaling page of the
Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No


                                                    © National Instruments 9755

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9755 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9756 ordinal=9756 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Scaling:EngineeringScaling:Engineering MinMin

       Gets or sets the zero scale, or minimum value, that the Shared Variable Engine and
     Human Machine Interface (HMI) application use for a shared variable when you use
        linear or square root scaling. To use this property, you must install the LabVIEW
       Datalogging and Supervisory Control Module.

      You can use this property for shared variables with a Scale Type of Linear.

       This property is similar to the Engineering Zero Scale option on the Scaling page of
       the Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Scaling:InvertScaling:Invert

           If TRUE, LabVIEW inverts the data the server sends before storing it in a shared

9756   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9756 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9757 ordinal=9757 -->
## Property and Method Reference

Property and Method Reference

variable. The default is FALSE. To use this property, you must install the LabVIEW
Datalogging and Supervisory Control Module.

You can use this property for shared variables with a Data Type of Boolean.

This property is similar to the Invert option on the Scaling page of the Shared Variable
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Scaling:InvertScaling:Invert MaskMask

Gets or sets the bits that the Shared Variable Engine inverts before storing them in a
shared variable. To use this property, you must install the LabVIEW Datalogging and
Supervisory Control Module.

The Shared Variable Engine inverts bits in the mask with value 1 but does not invert
bits with value 0. The default invert mask is 0, indicating that the Shared Variable
Engine inverts none of the bits. In bitwise logic terminology, the Shared Variable
Engine performs an XOR with this value to produce the scaled value.

You can use this property for shared variables with a Data Type of U32BitField.

                                                    © National Instruments 9757

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9757 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9758 ordinal=9758 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Scaling Invert Mask option on the Scaling page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Scaling:RawScaling:Raw MaxMax

       Gets or sets the full scale, or maximum value, that the server uses for a shared variable
     when you use linear or square root scaling. To use this property, you must install the
      LabVIEW Datalogging and Supervisory Control Module.

      You can use this property for shared variables with a Scale Type of Linear.

       This property is similar to the Raw Full Scale option on the Scaling page of the Shared
       Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type


9758   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9758 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9759 ordinal=9759 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Scaling:RawScaling:Raw MinMin

Gets or sets the zero scale, or minimum value, that the server uses for a shared
variable when you use linear or square root scaling. To use this property, you must
install the LabVIEW Datalogging and Supervisory Control Module.

You can use this property for shared variables with a Scale Type of Linear.

This property is similar to the Raw Zero Scale option on the Scaling page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No


                                                    © National Instruments 9759

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9759 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9760 ordinal=9760 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Scaling:SelectScaling:Select MaskMask

       Gets or sets the bits the Shared Variable Engine uses for a shared variable. To use this
       property, you must install the LabVIEW Datalogging and Supervisory Control Module.

      The Shared Variable Engine stores bits in the mask with value 1 in the shared variable.
      The Shared Variable Engine sets bits in the mask with value 0 to 0, regardless of the
       value received from the server. In bitwise logic terminology, the Shared Variable
      Engine performs an AND with this value to produce the scaled value.

      You can use this property for shared variables with a Data Type of U32BitField.

       This property is similar to the Scaling Select Mask option on the Scaling page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9760   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9760 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9761 ordinal=9761 -->
## Property and Method Reference

Property and Method Reference

Scaling:TypeScaling:Type

Gets or sets the type of scaling to perform on a shared variable. To use this property,
you must install the LabVIEW Datalogging and Supervisory Control Module.

Valid values are 0 (

Linear
), 1 (
Square Root
), 2 (
Bitwise
), 3 (
Invert
), and 4 (
Custom
).

Use a value of 0 or 1 for shared variables with a Data Type of Double, Single, or
Integer. Use a value of 2 for shared variables with a Data Type of U32BitField. Use a
value of 3 for shared variables with a Data Type of Boolean. Use a value of 4 to perform
custom scaling on a shared variable.

This property is similar to the Scale Type option on the Scaling page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes


                                                    © National Instruments 9761

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9761 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9762 ordinal=9762 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Single-Process:EnableSingle-Process:Enable TimestampTimestamp

           If TRUE, a timestamp value is recorded each time the single-process shared variable
       reads data. (Real-Time, Windows) To view timestamp information and add a
      timestamp output to the Shared Variable node, right-click the Shared Variable node
      and select Show Timestamp from the shortcut menu. If this property is FALSE, the
      timestamp output is hidden. You can use this property only with single-process shared
        variables. The default value is FALSE.

      An error occurs if you attempt to set this property when the VI is running.

       This property is similar to the Enable timestamp checkbox on the Variable page of the
      Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9762   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9762 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9763 ordinal=9763 -->
## Property and Method Reference

Property and Method Reference

TypeType

Gets or sets the scope of a shared variable.

An error occurs if you attempt to set this property when the VI is running.

This property is similar to the Variable Type option on the Variable page of the Shared
Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

UpdateUpdate Deadband:EnabledDeadband:Enabled

Enables the update deadband for a shared variable. If TRUE, LabVIEW updates the
value of a shared variable only if the percentage difference between the new value and
the previous value equals or exceeds the deadband. The default is FALSE. To use this
property, you must install the LabVIEW Datalogging and Supervisory Control Module.

This property is similar to the Enable Update Deadband option on the Update
Deadband page of the Shared Variable Properties dialog box.


                                                    © National Instruments 9763

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9763 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9764 ordinal=9764 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   UpdateUpdate Deadband:SourceDeadband:Source

       Gets or sets the deadband for updating the value of a shared variable when the value
        for the binding source changes. To use this property, you must install the LabVIEW
       Datalogging and Supervisory Control Module.

       This property is similar to the Source Deadband (% of range) option on the Update
      Deadband page of the Shared Variable Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No


9764   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9764 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9765 ordinal=9765 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

UpdateUpdate Deadband:UserDeadband:User

Gets or sets the deadband for updating the value of a shared variable when a user
writes data to the variable. To use this property, you must install the LabVIEW
Datalogging and Supervisory Control Module.

This property is similar to the User Deadband (% of range) option on the Update
Deadband page of the Shared Variable Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

VIVI


                                                    © National Instruments 9765

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9765 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9766 ordinal=9766 -->
## Property and Method Reference

Property and Method Reference

        VI Methods

        VI Properties

        VI Events

       VIVI MethodsMethods


       Method             Description

        Abort VI             Aborts the execution of a top-level VI.

                             Allows LabVIEW to replace overloaded nodes with more appropriate
                            implementations. For example, if you script an Add function and wire a Matrix
                               control to it, LabVIEW breaks the wire. If you call Adapt Nodes, the Add        Adapt Nodes
                              function might be replaced with a Matrix Add VI. Operator overloading will
                            not occur during scripting. You must call this method for Overloading to
                           happen.

                            Cleans up the block diagram of the VI by rearranging and resizing its objects
        Block                        and signals to improve readability. You also can select Edit»Clean Up        Diagram:Clean Up                         Diagram to clean up the block diagram.

                            Returns an image of the block diagram and scales it proportionally according
                              to the maximum width and height you wire to the method. For example, if
        Block Diagram:Get   the image of the block diagram is 200 by 200 pixels and you wire a value of 50
        Image Scaled        to maximum width and a value of 100 to maximum height, this method
                              returns an image that is 50 by 50 pixels. If you do not wire a value to
                     maximum width or maximum height, the image retains its actual size.

        Block             Removes all the broken wires on the block diagram of the VI.
        Diagram:Remove
       Bad Wires           This method is similar to selecting Edit»Remove Broken Wires.

         Clear History         Clears the revision history of the referenced VI.

         Compile:VI         Compiles the VI and optionally the entire VI hierarchy of that VI.

                            Hides the front panel of the VI and optionally hides the VI from the taskbar
                       when the VI runs as a top-level VI by changing the VI properties, such as the
         Configure Panel As   front panel transparency, run-time position, and minimization properties.
         Top-Level Hidden    This method is useful when you want to control if and when the front panel
                          opens for top-level VIs. For example, use this method to hide the front panel
                               of startup VIs of stand-alone applications that you build in LabVIEW.

9766   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9766 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9767 ordinal=9767 -->
## Property and Method Reference

Property and Method Reference


Method             Description

Control VI Apply     Apply changes made to a control VI. This method returns an error if used on
Changes            non-control VIs.

                    Gets the value of a named control or indicator as variant data. Use the VariantControl Value:Get                     to Data function to convert the data to another LabVIEW data type.

                    Gets the values of all controls or indicators in a VI as variant data. This
Control Value:Get   method returns an array of clusters that contains control and indicator
All              names and their values as variant data. Use the Variant to Data function to
                    convert the data to another LabVIEW data type.

                     Sets the value of a named control or indicator of the variant. You can wire a
Control Value:Set    value of any data type to this method. You do not have to use the To Variant
                     function to convert the data to a variant data type.

                     Creates a control or constant of the data type you specify. LabVIEW alwaysCreate from Data                     creates a control initially, even if you configure Style to create a constant orType
                       indicator. To change the type of the new object, use the Indicator property.

Create from          Creates a constant or control using a constant or control reference as a
Reference           template.

                    Returns TRUE if the button is enabled or FALSE if the button is grayed out.
Debugging:Get                     This method also returns the string for the tip strip associated with the
Debug Button                     button. For example, this method might return Step into For Loop forDisplay State
                    the Step Into button.

Debugging:Step      Single-steps through a VI to help you debug the VI. To use this method, the VI
Into              must be paused.

                      Single-steps through a VI to help you debug the VI. To use this method, the VIDebugging:Step Out                 must be paused.

Debugging:Step      Single-steps through a VI to help you debug the VI. To use this method, the VI
Over              must be paused.

Default Values:Make Changes the defaults of all controls on the front panel to be the current
Current Default       values. This method is available only in edit mode.

Default
Values:Reinitialize   Changes the current values of all controls on the front panel to their defaults.
All To Default

Detect Parallel
                     Detects parallel loops in the VI.
Loops

Disconnect From     Disconnects a VI that a LabVIEW project library owns from the owning project


                                                    © National Instruments 9767

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9767 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9768 ordinal=9768 -->
## Property and Method Reference

Property and Method Reference


       Method             Description

         Library                 library.

       Empty             Empties the front panel and block diagram of the VI.

         Find Control with    Return a reference to the control that currently has key focus. If there is not a
        Key Focus            control with key focus in the target VI, Not a Refnum is returned.

                               Specifies whether to automatically center the front panel window on the         Front Panel:Center
                          computer screen.

         Front Panel:Close    Closes the front panel window.

                            Returns an image of the front panel as a flattened pixmap. Use the Front
         Front Panel:Get      Panel:Get Image Scaled method to return an image of the front panel and
        Image               scale it proportionally according to the maximum width and height you wire
                              to the method.

                            Returns an image of the front panel and scales it proportionally according to         Front Panel:Get
                            the maximum width and height you wire to the method. This method is        Image Scaled                                similar to the Front Panel:Get Image method.

                        Opens the front panel window. If the front panel is already open, this method
         Front Panel:Open    changes the state of the front panel window to the state you wire to this
                          method.

         Front Panel:Run-     Configures the referenced VI to center its front panel every time the VI runs. If
       Time               the VI is running when you call this method, the change does not take effect
         Position:Centered    until the next time the VI runs.

         Front Panel:Run-     Configures the referenced VI to open its front panel in a custom position
       Time               every time the VI runs. If the VI is running when you call this method, the
         Position:Custom    change does not take effect until the next time the VI runs.

         Front Panel:Run-
       Time Position:Get    Returns the default position of the front panel window at run-time.
         Position

         Front Panel:Run-     Configures a VI to maximize its front panel every time the VI runs. If the VI is
       Time               running when you call this method, the change does not take effect until the
         Position:Maximized  next time the VI runs.

         Front Panel:Run-     Sets a VI to minimize its front panel every time the VI runs. If the VI is running
       Time            when you call this method, the change does not take effect until the next
         Position:Minimized  time the VI runs.

         Front Panel:Run-     Configures the VI to maintain the position of its front panel window when the
       Time                  VI runs.


9768   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9768 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9769 ordinal=9769 -->
## Property and Method Reference

Property and Method Reference


Method             Description

Position:Unchanged

                    Returns a string that describes transform metrics from the most recentGet Compile Metrics                   compile of the VI, if metric recording was enabled.

                    Returns the connector pane image, as it appears in the Context Help window,
                    as a cluster of image data so you can draw it as a picture using the DrawGet Conpane Image                     Flattened Pixmap VI or save the image to a file using the Graphics Formats
                         VIs.

                    Gets the index for the control or indicator of the given name. If the control orGet Control Index
                      indicator for which you want to get an index does not have a terminal on theby Name                    block diagram, this method returns an error.

                    Returns the access scope or inherited access scope of this VI if it is owned by a
Get Library Access   LabVIEW project library. This method provides the same information as the
Scope            method Source Scope:Get of the Project Library class without requiring a
                     reference to the owning project library.

Get ObjectRef From  Returns a reference to the object, such as the label, that contains the
BookmarkID        bookmark.

                    Returns the bookmark information for the specified VI reference. You must
                    load the VI into memory in order to read the bookmark information. ThisGet VI Bookmarks                 method returns an error if the VI is password protected or if the VI does not
                  have a block diagram.

                     This method returns the names and paths of the VI dependencies of a VI. You
Get VI                  can use this method to return a specific subset of the total set of VIDependencies                   dependencies of a VI. This method does not return non-VI dependencies,
(Names and Paths)                   such as project libraries, XControls, classes, and statecharts.

                    Returns the lock state of the VI and indicates whether the password for the VI
Lock State:Get
                           is in the password cache.

                     Sets the lock state of a VI. If interactive is FALSE (default), you can use
                  password to either unlock a password-protected VI or set the password of an
Lock State:Set
                    unprotected VI. If interactive is TRUE, LabVIEW ignores password and
                     displays a dialog box that prompts you to change the lock state.

Move Objects       Moves the objects by the offset amount of pixels.

Pause VI            Pauses or unpauses the VI execution.

Populate           Ensures that the asynchronous call pool for a VI reference contains at least
Asynchronous Call   the number of data spaces specified by the Minimum Size parameter. By
Pool                  default, when you open a reference with the Open VI Reference function,

                                                    © National Instruments 9769

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9769 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9770 ordinal=9770 -->
## Property and Method Reference

Property and Method Reference


       Method             Description

                         LabVIEW allocates one data space per CPU core on the development
                            computer.

         Print:Panel To                                Prints the panel of the VI to the specified PostScript file.         PostScript

         Print:Panel To        Prints just the front panel to the current printer. You cannot use this method
          Printer              to print a block diagram, list of controls, or polymorphic VI front panel.

                           Saves the VI information to an HTML file and saves the graphics in external
          Print:VI To HTML       files. You can use the Open URL in Default Browser VI to display the HTML file
                                 in the default Web browser.

          Print:VI To Printer    Prints the VI information to a printer.

          Print:VI To RTF      Saves the VI information to an RTF file.

                           Saves the VI information to a text file. You cannot save the icon, connector          Print:VI To Text                            pane, front panel, block diagram, subVI icons, and VI hierarchy to text.

       Remote                            Returns an array of clusters containing connection information about the         Panel:Client                                 clients viewing or controlling the VI.
        Connections

       Remote Panel:Close
        Connection To       Closes a remote front panel connection to a client.
          Client

                            Returns control of the front panel to the server and queues any requests from       Remote Panel:Lock                                 clients to control the front panel. LabVIEW ignores this method if the front
         Control                            panel is already locked.

       Remote                     If the front panel is locked, this method grants control to the next client in the
         Panel:Unlock        queue. If no clients are in the queue, the method unlocks the front panel.
         Control            LabVIEW ignores this method if the front panel is already unlocked.

                        Make the connector pane of the VI Reference match the given connector
         Replicate Conpane
                            pane.

         Revert VI            Discards changes and reloads a VI from disk.

                                Starts the VI execution, similar to the Run button. This method is different
                           than calling a VI because it uses the current values of all front panel controls
       Run VI                 for execution rather than using data passed in through parameters. This
                        method also ignores the Execution:Show Front Panel On Call property of a VI
                        and the Execution:Close After Call property.

         Save:For Previous    Saves a copy of the VI that is readable by LabVIEW version 8.0 and later. If you

9770   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9770 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9771 ordinal=9771 -->
## Property and Method Reference

Property and Method Reference


Method             Description

                   save a password-protected VI for a previous LabVIEW version, you must enter
                    the password. You can enter the password programmatically as an input on
                    the Open VI Reference function.

                   Saves a VI that is not currently running and synchronizes the VI with theSave:Instrument
                     edited version in other application instances before saving.

Save:Run-Time      Saves the run-time menu to a file specified by Path. This method works only
Menu            when the VI is running. It saves only menu items with valid tags.

Transaction:Begin                    Begins an undo transaction on a VI.
Undo

Transaction:End                  Ends an undo transaction on a VI.Undo

                        Fails the current transaction and deletes the undo information for theTransaction:Fail                      transaction.

Transaction:Get      Returns whether there is an action to redo and, if so, the text that
Redo State          corresponds to that action.

Transaction:Get      Returns whether there is an action to undo and, if so, the text that
Undo State          corresponds to that action.

Transaction:Redo    Redoes the last operation. This is similar to selecting Edit»Redo.

Transaction:Undo   Undoes the last operation. This method is similar to selecting Edit»Undo.

                    Returns the VI icon as a cluster of image data so you can draw it as a pictureVI Icon:Get As Image                    using the Draw Flattened Pixmap VI or save the image to a file using the
Data                    Graphics Formats VIs.

VI Icon:Save To File   Saves an image of the VI icon to a file.

                     Sets the image of a VI icon from a file. LabVIEW creates a user layer called VI
VI Icon:Set From File  Icon for the image and deletes any other existing icon information from the
                    Icon Editor dialog box.

                     Sets a VI icon from image data you specify. LabVIEW creates a user layer
VI Icon:Set From
                      called VI Icon for the image and deletes any other existing icon information
Image Data
                  from the Icon Editor dialog box.

                    Exports the following strings about VI and front panel objects to a tagged text
                              file: VI name and description, object caption labels, object free labels, default
VI Strings:Export     data (string, table, path, and array default data), private data (listbox item
                  names, table row and column headers, graph plot names, graph cursor
                  names, graph annotation names, and tab control page captions), and

                                                    © National Instruments 9771

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9771 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9772 ordinal=9772 -->
## Property and Method Reference

Property and Method Reference


       Method             Description

                           polymorphic VI data (instance names in the polymorphic VI and selector
                              shortcut menus).

                            Imports the following strings about VI and front panel objects from a tagged
                                 text file: VI name and description, object caption labels, object free labels,
                               default data (string, table, path, and array default data), private data (listbox
          VI Strings:Import    item names, table row and column headers, graph plot names, graph cursor
                          names, graph annotation names, and tab control page captions), and
                           polymorphic VI data (instance names in the polymorphic VI and selector
                              shortcut menus).

   AbortAbort VIVI

       Aborts the execution of a top-level VI.

       This method returns error 1000 if you call it on a subVI. Otherwise, this method is
        similar to pressing the Abort Execution button on the toolbar.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

9772   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9772 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9773 ordinal=9773 -->
## Property and Method Reference

Property and Method Reference


 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

AdaptAdapt NodesNodes

Allows LabVIEW to replace overloaded nodes with more appropriate implementations.
For example, if you script an Add function and wire a Matrix control to it, LabVIEW
breaks the wire. If you call Adapt Nodes, the Add function might be replaced with a
Matrix Add VI. Operator overloading will not occur during scripting. You must call this
method for Overloading to happen.

Parameters

            Data Name               Required  Description            type

 Nodes []           No            If wired, operator overloading will update each reference.


 Terminals                                      If wired, operator overloading will update each terminal
                  No []                                  reference.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No


                                                    © National Instruments 9773

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9773 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9774 ordinal=9774 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

        Must wait until user interface is idle                                  Yes

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

   BlockBlock Diagram:CleanDiagram:Clean UpUp

       Cleans up the block diagram of the VI by rearranging and resizing its objects and
       signals to improve readability. You also can select Edit»Clean Up Diagram to clean up
       the block diagram.

       This method is available only in edit mode.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No


9774   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9774 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9775 ordinal=9775 -->
## Property and Method Reference

Property and Method Reference


 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

BlockBlock Diagram:GetDiagram:Get ImageImage ScaledScaled

Returns an image of the block diagram and scales it proportionally according to the
maximum width and height you wire to the method. For example, if the image of the
block diagram is 200 by 200 pixels and you wire a value of 50 to maximum width and a
value of 100 to maximum height, this method returns an image that is 50 by 50 pixels.
If you do not wire a value to maximum width or maximum height, the image retains
its actual size.

You also can use the Append VI Block Diagram to Report VI to create an image of a
block diagram and append it to a report.

Parameters

          Data Name          Required  Description           type

                            Sets the color depth, or number of supported colors, of the image: 1
 Image             No          (1-bit, black and white), 4 (4-bit, 16 colors), 8 (8-bit, 256 colors), or 24
 Depth                                 (24-bit, true color). The default is 8.

                            Information about the image so you can use the Draw Flattened
                        Pixmap VI to draw it as a picture or use the Graphics Formats VIs to
                          save the image to a file. This cluster is similar to the image data
                          output of the Read JPEG File, Read PNG File, and Read BMP File VIs.

 Image                                  • image type—Reserved for future use.
             No Data                                    • image depth—Specifies the color depth of the image, which is the
                          number of bits to use to describe the color of each pixel in the
                               image. Valid values include 1, 4, 8, and 24 bits per pixel. image
                            depth affects how LabVIEW interprets the values of image and
                                   colors.


                                                    © National Instruments 9775

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9775 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9776 ordinal=9776 -->
## Property and Method Reference

Property and Method Reference


                  Data      Name          Required  Description
                  type

                                                        • image—Array of bytes that describes the color of each pixel in the
                                   image in raster order. The value of image depth determines how
                                   LabVIEW interprets the value of this output.

                                                                If image depth is 24, each pixel has three bytes to describe its
                                              color. The first byte for each pixel describes the red value, the
                                    second byte describes the green value, and the third byte
                                        describes the blue value.

                                                                If image depth is 8, each pixel has one byte to describe its color.
                                  The value of each bit corresponds to an element in colors, which
                                           stores 32-bit RGB values where the most-significant byte is zero,
                                       followed in order by red, green, and blue values.

                                                                If image depth is 4, the behavior is similar to when image depth
                                                      is 8 except valid values in image include 0 through 15.

                                                                If image depth is 1, any value of zero in image corresponds to
                                    element 0 in colors. All other values correspond to element 1 in
                                            colors.

                                  The size of the array might be larger than expected due to
                                       padding.
                                                        • mask—Array of bytes in which each bit describes mask
                                        information for a pixel. The first byte describes the first eight
                                               pixels, the second byte describes the next eight pixels, and so on.
                                                                If a bit is zero, LabVIEW draws the corresponding pixel as
                                          transparent. If the array is empty, LabVIEW draws all pixels
                                      without transparency. If the array does not contain a bit for each
                                             pixel in the image, LabVIEW draws any pixels missing from the
                                          array without transparency.
                                                        • colors—Array of RGB color values that correspond to the values in
                                     image. The value of image depth determines how LabVIEW
                                            interprets the value of this output. If image depth is 24, LabVIEW
                                         ignores this output. If image depth is 8, the array has 256
                                       elements. If image depth is 4, the array has 16 elements. If image
                                   depth is 1, the array has 2 elements.
                                                        • Rectangle—Cluster that contains coordinates that describe the
                                   bounding rectangle of the image, where the upper-left corner is at


9776   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9776 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9777 ordinal=9777 -->
## Property and Method Reference

Property and Method Reference


          Data Name          Required  Description
           type

                                         (0,0). The bottom right edges of the bounds does not include the
                               image.


 Maximum             No        Sets the maximum width of the scaled image. Width

 Maximum             No        Sets the maximum height of the scaled image. Height

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                                     Yes

 Loads the block diagram into memory                               Yes

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No


                                                    © National Instruments 9777

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9777 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9778 ordinal=9778 -->
## Property and Method Reference

Property and Method Reference

   BlockBlock Diagram:RemoveDiagram:Remove BadBad WiresWires

      Removes all the broken wires on the block diagram of the VI.

       This method is similar to selecting Edit»Remove Broken Wires.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    ClearClear HistoryHistory

       Clears the revision history of the referenced VI.

       This method is similar to the Reset button on the History window.


9778   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9778 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9779 ordinal=9779 -->
## Property and Method Reference

Property and Method Reference

Parameters

         Data Name         Required  Description
         type

 Reset                                 If TRUE, LabVIEW resets the revision number. If FALSE (default),            No Revision               LabVIEW clears the history but increments the current revision number.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                  No

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

Compile:VICompile:VI

Compiles the VI and optionally the entire VI hierarchy of that VI.


                                                    © National Instruments 9779

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9779 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9780 ordinal=9780 -->
## Property and Method Reference

Property and Method Reference

           Note This method does not show a modification, or asterisk (*) in the title
                bar, for the VI unless you included the 0x01 option flag as part of the options
              input to the Open VI Reference function when you opened the VI reference.

     Parameters

                 Data
      Name          Required  Description                  type

                               Compile Entire Hierarchy specifies whether to compile all VIs within
        Compile                   the VI hierarchy of the referenced VI. The VI hierarchy includes all VIs
         Entire                      that call the VI as well as all subVIs that the VI calls. If you set this
                   No         Hierarchy                parameter to TRUE, subVIs indicate that they were modified by
           (F)                         displaying an asterisk (*) in their title bar the next time you open them.
                               By default, this parameter is FALSE.


         Force                                  Force Compile specifies whether to compile the VI even if the VI does
        Compile       No                                  not need to be recompiled. By default, this parameter is TRUE.          (T)


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No


9780   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9780 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9781 ordinal=9781 -->
## Property and Method Reference

Property and Method Reference


 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

ConfigureConfigure PanelPanel AsAs Top-LevelTop-Level HiddenHidden

Hides the front panel of the VI and optionally hides the VI from the taskbar when the VI
runs as a top-level VI by changing the VI properties, such as the front panel
transparency, run-time position, and minimization properties. This method is useful
when you want to control if and when the front panel opens for top-level VIs. For
example, use this method to hide the front panel of startup VIs of stand-alone
applications that you build in LabVIEW.

Parameters

 Name                                        Data type     Required     Description

 hide VI in operating system taskbar? (F)                     No

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                  No


                                                    © National Instruments 9781

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9781 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9782 ordinal=9782 -->
## Property and Method Reference

Property and Method Reference


        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    ControlControl VIVI ApplyApply ChangesChanges

      Apply changes made to a control VI. This method returns an error if used on non-
       control VIs.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                             No

        Must wait until user interface is idle                                     No

         Available with control VIs                                                          Yes

         Available with global VIs                                            No

         Available with strict type definitions                                    No

         Available with polymorphic VIs                                        No


9782   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9782 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9783 ordinal=9783 -->
## Property and Method Reference

Property and Method Reference

ControlControl Value:GetValue:Get

Gets the value of a named control or indicator as variant data. Use the Variant to Data
function to convert the data to another LabVIEW data type.

      Note This method requires the VI to have a front panel. If you are using the
        Application Builder, make sure you do not remove the front panel.

For optimization purposes, LabVIEW does not keep track of data values on controls
and indicators until LabVIEW determines you want them, that is, until you call this
method or display the front panel. When you display the front panel, LabVIEW begins
keeping track of the values.

The first time you call this method on a VI whose front panel is not open, this method
returns the default values of the control or indicator rather than the actual values.
Thereafter, it returns the actual value.

Parameters

        Data Name        Required  Description         type

                         Label of the control or indicator whose value you want. LabVIEW
 Control                 searches the front panel tabbing order for the label of the object and               Yes Name                    returns the value for the first object whose label matches the string you
                         wire to this input.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

                                                    © National Instruments 9783

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9783 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9784 ordinal=9784 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

        Must wait until user interface is idle                                     No

         Available with control VIs                                                          Yes

         Available with global VIs                                                           Yes

         Available with strict type definitions                                    No

         Available with polymorphic VIs                                        No

    ControlControl Value:GetValue:Get AllAll

       Gets the values of all controls or indicators in a VI as variant data. This method returns
      an array of clusters that contains control and indicator names and their values as
       variant data. Use the Variant to Data function to convert the data to another LabVIEW
       data type.

           Note This method requires the VI to have a front panel. If you are using the
               Application Builder, make sure you do not remove the front panel.

       For optimization purposes, LabVIEW does not keep track of data values on controls
      and indicators until LabVIEW determines you want them, that is, until you call this
      method or display the front panel. When you display the front panel, LabVIEW begins
      keeping track of the values.

      The first time you call this method on a VI whose front panel is not open, this method
       returns the default values of the control or indicator rather than the actual values.
       Thereafter, it returns the actual value.


9784   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9784 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9785 ordinal=9785 -->
## Property and Method Reference

Property and Method Reference

Parameters

         Data Name         Required  Description
          type

                                           If TRUE, the method returns values for all the controls. If FALSE Controls      No                                (default), the method returns values for all the indicators.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

 Must wait until user interface is idle                                     No

 Available with control VIs                                                          Yes

 Available with global VIs                                                           Yes

 Available with strict type definitions                                    No

 Available with polymorphic VIs                                        No

ControlControl Value:SetValue:Set

Sets the value of a named control or indicator of the variant. You can wire a value of
any data type to this method. You do not have to use the To Variant function to convert
the data to a variant data type.

                                                    © National Instruments 9785

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9785 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9786 ordinal=9786 -->
## Property and Method Reference

Property and Method Reference

           Note This method requires the VI to have a front panel. If you are using the
               Application Builder, make sure you do not remove the front panel.

     Parameters

                Data      Name        Required  Description                type

                                 Label of the control or indicator whose value you want to change.
         Control               LabVIEW searches the front panel tabbing order for the label of the                       Yes      Name                    object and changes the value of the first object whose label matches the
                                      string you wire to this input.


         Value         Yes       Value to which you want to set the control or indicator.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

9786   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9786 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9787 ordinal=9787 -->
## Property and Method Reference

Property and Method Reference


 Available with polymorphic VIs                             No

CreateCreate fromfrom DataData TypeType

Creates a control or constant of the data type you specify. LabVIEW always creates a
control initially, even if you configure Style to create a constant or indicator. To change
the type of the new object, use the Indicator property.

Use the To More Specific Class function to try to cast the reference this method returns
to the specific class you want to use in the application. If the function does not return
an error, the reference matches the specific class.

Parameters

          Data Name          Required  Description           type

 Data                 Yes      The data type you want to use to create the constant. Type


                              Specifies whether you create a front panel or block diagram object. If
                        you select a front panel object, this parameter further specifies the
                                style of that object.

                          0        Probe

                          1       Diagram

                          2        Panel Control Style            Yes
                          3       3D Panel Control

                          4        Dialog Panel Control

                          5        Panel Indicator

                          6       3D Panel Indicator

                          7        Dialog Panel Indicator


                                                    © National Instruments 9787

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9787 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9788 ordinal=9788 -->
## Property and Method Reference

Property and Method Reference


                  Data      Name          Required  Description
                  type


                                 8       Power PC Control

                                 9       Power PC Indicator

                                 10        Silver Control

                                 11        Silver Indicator


                                       Specifies the position where you want to create the constant or         Position       No                                        control.

      New
         Object           Yes      The reference to the constant or control you create.
         Reference

       Make                                 Determines whether to make the name of the constant or control       Names                   No       unique. Make Names Unique does not rename the constant or control
        Unique                                                            if a constant or control with that name already exists.           (F)

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes


9788   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9788 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9789 ordinal=9789 -->
## Property and Method Reference

Property and Method Reference


 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                                 Yes

 Available with polymorphic VIs                             No

CreateCreate fromfrom ReferenceReference

Creates a constant or control using a constant or control reference as a template.

Parameters

          Data
 Name          Required  Description           type

 Source                 A reference to the object you want to duplicate on the target VI. If you
 Object           Yes       use this parameter, you do not need to wire the type descriptor and
 Reference                    style fields.


                              Specifies the position where you want to create the constant or Position       No                               control.

 New
 Object           Yes      The reference to the constant or control you create.
 Reference

 Make
                          Determines whether to make the name of the constant or control
 Names
             No       unique. Make Names Unique does not rename the constant or control
 Unique
                                              if a constant or control with that name already exists.
 (F)

Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 9789

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9789 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9790 ordinal=9790 -->
## Property and Method Reference

Property and Method Reference


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                                 Yes

         Available with polymorphic VIs                             No

   Debugging:GetDebugging:Get DebugDebug ButtonButton DisplayDisplay StateState

       Returns TRUE if the button is enabled or FALSE if the button is grayed out. This method
       also returns the string for the tip strip associated with the button. For example, this
      method might return Step into For Loop for the Step Into button.

     Parameters

                   Data
      Name               Required  Description
                   type

                                            Specifies which of the debugging buttons you want to examine.

        Button
                              Yes       0          Step Into        Type
                                     1          Step Over


9790   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9790 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9791 ordinal=9791 -->
## Property and Method Reference

Property and Method Reference


           Data Name               Required  Description
            type


                              2          Step Out


 Is                              Returns whether the specified debugging button is available to                      Yes Enabled?                             click.


                                Returns the string for the tip strip associated with the specified
 Tooltip               Yes                                 button.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No


                                                    © National Instruments 9791

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9791 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9792 ordinal=9792 -->
## Property and Method Reference

Property and Method Reference

   Debugging:StepDebugging:Step IntoInto

       Single-steps through a VI to help you debug the VI. To use this method, the VI must be
      paused.

       This method is similar to the Step Into button on the block diagram toolbar.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

   Debugging:StepDebugging:Step OutOut

       Single-steps through a VI to help you debug the VI. To use this method, the VI must be
      paused.

       This method is similar to the Step Out button on the block diagram toolbar.


9792   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9792 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9793 ordinal=9793 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

Debugging:StepDebugging:Step OverOver

Single-steps through a VI to help you debug the VI. To use this method, the VI must be
paused.

This method is similar to the Step Over button on the block diagram toolbar.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes


                                                    © National Instruments 9793

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9793 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9794 ordinal=9794 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    DefaultDefault Values:MakeValues:Make CurrentCurrent DefaultDefault

      Changes the defaults of all controls on the front panel to be the current values. This
      method is available only in edit mode.

       This method is similar to the Make Current Value Default item on the shortcut menu of
      a control and the Make Current Values Default item in the Edit menu.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No


9794   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9794 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9795 ordinal=9795 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

DefaultDefault Values:ReinitializeValues:Reinitialize AllAll ToTo DefaultDefault

Changes the current values of all controls on the front panel to their defaults.

This method is similar to the Reinitialize Values to Default item in the Edit menu.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                 No

 Available with global VIs                                            Yes

 Available with strict type definitions                         No


                                                    © National Instruments 9795

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9795 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9796 ordinal=9796 -->
## Property and Method Reference

Property and Method Reference


         Available with polymorphic VIs                             No

    DetectDetect ParallelParallel LoopsLoops

       Detects parallel loops in the VI.

     Parameters

      Name                Data type   Required    Description

         reportConflicts (T)               No           Specifies whether to report conflicts.


         analyzeAllLoops (T)              No           Specifies whether to analyze all loops.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                                 Yes

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                              Yes

       Remote access allowed                                                           Yes

        Must wait until user interface is idle                                     No

         Available with control VIs                                            No

         Available with global VIs                                            No

         Available with strict type definitions                                    No

9796   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9796 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9797 ordinal=9797 -->
## Property and Method Reference

Property and Method Reference


 Available with polymorphic VIs                                        No

DisconnectDisconnect FromFrom LibraryLibrary

Disconnects a VI that a LabVIEW project library owns from the owning project library.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

EmptyEmpty

Empties the front panel and block diagram of the VI.

Remarks

The following table lists the characteristics of this method.

                                                    © National Instruments 9797

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9797 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9798 ordinal=9798 -->
## Property and Method Reference

Property and Method Reference


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

   FindFind ControlControl withwith KeyKey FocusFocus

       Return a reference to the control that currently has key focus. If there is not a control
       with key focus in the target VI, Not a Refnum is returned.

     Parameters

      Name             Data type    Required    Description

         Control Found?                   Yes          Indicates the control that has key focus.


     Remarks

      The following table lists the characteristics of this method.


        Data type


9798   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9798 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9799 ordinal=9799 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                                 Yes

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                             No

 Must wait until user interface is idle                                     No

 Available with control VIs                                                          Yes

 Available with global VIs                                                           Yes

 Available with strict type definitions                                    No

 Available with polymorphic VIs                                        No

FrontFront Panel:CenterPanel:Center

Specifies whether to automatically center the front panel window on the computer
screen.

This method is similar to the Centered option of the Position pull-down menu on the
Window Run-Time Position page of the VI Properties dialog box.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                                  Yes


                                                    © National Instruments 9799

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9799 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9800 ordinal=9800 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

    FrontFront Panel:ClosePanel:Close

       Closes the front panel window.

      Use the Front Panel:Open method to open a front panel window.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes


9800   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9800 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9801 ordinal=9801 -->
## Property and Method Reference

Property and Method Reference


 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Server\VI
   Properties\VI Properties - Front Panel States.vi
FrontFront Panel:GetPanel:Get ImageImage

Returns an image of the front panel as a flattened pixmap. Use the Front Panel:Get
Image Scaled method to return an image of the front panel and scale it proportionally
according to the maximum width and height you wire to the method.

If a front panel is not visible, LabVIEW does not update the values in the objects on the
front panel. If you call a VI whose front panel is not visible and you use the Front
Panel:Get Image method to create an image of the front panel, the image does not
reflect any value changes that occurred when you ran the VI.

If you want the image to reflect value changes, make sure the front panel is open
before any values change. If you do not want to display the front panel but want the
image to reflect value changes, create a Property Node from any terminal on the block
diagram of the VI for which you want to create a front panel image.

You also can use the Append Front Panel Image to Report VI to create an image of a
front panel and append it to a report.

Parameters

        Data
 Name       Required  Description
        type

 Visible
 Area       No        Indicates if the front panel image includes just the objects in the visible
 Only


                                                    © National Instruments 9801

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9801 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9802 ordinal=9802 -->
## Property and Method Reference

Property and Method Reference


               Data      Name       Required  Description
               type

                                area of the front panel (TRUE) or all the front panel objects (FALSE). The
                                   default is TRUE.


                                   Indicates the color depth, or number of supported colors, of the image: 1        Image                 No          (1-bit, black and white), 4 (4-bit, 16 colors), 8 (8-bit, 256 colors), 24 (24-bit,
        Depth                                  true color), or 32 (32-bit, ARGB format). The default is 8.

                                Information about the image so you can use the Draw Flattened Pixmap
                                      VI to draw it as a picture or use the Graphics Formats VIs to save the
                            image to a file. This cluster is similar to the image data output of the Read
                           JPEG File, Read PNG File, and Read BMP File VIs.

                                                   • image type—Reserved for future use.
                                                   • image depth—Specifies the color depth of the image, which is the
                              number of bits to use to describe the color of each pixel in the image.
                                        Valid values include 1, 4, 8, and 24 bits per pixel. image depth
                                          affects how LabVIEW interprets the values of image and colors.
                                                   • image—Array of bytes that describes the color of each pixel in the
                                image in raster order. The value of image depth determines how
                                LabVIEW interprets the value of this output.

                                                           If image depth is 24, each pixel has three bytes to describe its color.        Image
                 No          The first byte for each pixel describes the red value, the second byte        Data
                                     describes the green value, and the third byte describes the blue
                                        value.

                                                           If image depth is 8, each pixel has one byte to describe its color. The
                                     value of each bit corresponds to an element in colors, which stores
                                         32-bit RGB values where the most-significant byte is zero, followed in
                                    order by red, green, and blue values.

                                                           If image depth is 4, the behavior is similar to when image depth is 8
                                    except valid values in image include 0 through 15.

                                                           If image depth is 1, any value of zero in image corresponds to
                                 element 0 in colors. All other values correspond to element 1 in
                                        colors.


9802   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9802 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9803 ordinal=9803 -->
## Property and Method Reference

Property and Method Reference


        Data Name       Required  Description
        type

                         The size of the array might be larger than expected due to padding.
                                       • mask—Array of bytes in which each bit describes mask information
                                 for a pixel. The first byte describes the first eight pixels, the second
                            byte describes the next eight pixels, and so on. If a bit is zero,
                         LabVIEW draws the corresponding pixel as transparent. If the array is
                           empty, LabVIEW draws all pixels without transparency. If the array
                          does not contain a bit for each pixel in the image, LabVIEW draws any
                                pixels missing from the array without transparency.
                                       • colors—Array of RGB color values that correspond to the values in
                           image. The value of image depth determines how LabVIEW
                                interprets the value of this output. If image depth is 24, LabVIEW
                             ignores this output. If image depth is 8, the array has 256 elements. If
                         image depth is 4, the array has 16 elements. If image depth is 1, the
                              array has 2 elements.
                                       • Rectangle—Cluster that contains coordinates that describe the
                          bounding rectangle of the image, where the upper-left corner is at
                                     (0,0). The bottom right edges of the bounds does not include the
                            image.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes


                                                    © National Instruments 9803

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9803 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9804 ordinal=9804 -->
## Property and Method Reference

Property and Method Reference


         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

    FrontFront Panel:GetPanel:Get ImageImage ScaledScaled

       Returns an image of the front panel and scales it proportionally according to the
     maximum width and height you wire to the method. This method is similar to the
       Front Panel:Get Image method.

           If a front panel is not visible, LabVIEW does not update the values in the objects on the
       front panel. If you call a VI whose front panel is not visible and you use the Front
       Panel:Get Image Scaled method to create an image of the front panel, the image does
       not reflect any value changes that occurred when you ran the VI.

           If you want the image to reflect value changes, make sure the front panel is open
       before any values change. If you do not want to display the front panel but want the
      image to reflect value changes, wire a Property Node to any terminal on the block
      diagram of the VI for which you want to create a front panel image.

      You also can use the Append Front Panel Image to Report VI to create an image of a
       front panel and append it to a report.

     Parameters

                  Data
      Name          Required  Description
                  type

                                      Indicates if the front panel image includes just the objects in the
          Visible
                   No         visible area of the front panel (TRUE) or all the front panel objects
        Area Only
                                      (FALSE). The default is TRUE.


        Image
                   No        Indicates the color depth, or number of supported colors, of the
        Depth


9804   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9804 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9805 ordinal=9805 -->
## Property and Method Reference

Property and Method Reference


          DataName          Required  Description
          type

                          image: 1 (1-bit, black and white), 4 (4-bit, 16 colors), 8 (8-bit, 256
                               colors), 24 (24-bit, true color), or 32 (32-bit, ARGB format). The default
                                    is 8.

                           Information about the image so you can use the Draw Flattened
                       Pixmap VI to draw it as a picture or use the Graphics Formats VIs to
                          save the image to a file. This cluster is similar to the image data
                         output of the Read JPEG File, Read PNG File, and Read BMP File VIs.

                                           • image type—Reserved for future use.
                                           • image depth—Specifies the color depth of the image, which is the
                         number of bits to use to describe the color of each pixel in the
                              image. Valid values include 1, 4, 8, and 24 bits per pixel. image
                            depth affects how LabVIEW interprets the values of image and
                                  colors.
                                           • image—Array of bytes that describes the color of each pixel in the
                           image in raster order. The value of image depth determines how
                           LabVIEW interprets the value of this output.

                                                  If image depth is 24, each pixel has three bytes to describe its
                                    color. The first byte for each pixel describes the red value, the
Image                       second byte describes the green value, and the third byte             No
Data                           describes the blue value.

                                                  If image depth is 8, each pixel has one byte to describe its color.
                           The value of each bit corresponds to an element in colors, which
                                 stores 32-bit RGB values where the most-significant byte is zero,
                               followed in order by red, green, and blue values.

                                                  If image depth is 4, the behavior is similar to when image depth
                                          is 8 except valid values in image include 0 through 15.

                                                  If image depth is 1, any value of zero in image corresponds to
                            element 0 in colors. All other values correspond to element 1 in
                                  colors.

                           The size of the array might be larger than expected due to
                              padding.
                                           • mask—Array of bytes in which each bit describes mask


                                                    © National Instruments 9805

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9805 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9806 ordinal=9806 -->
## Property and Method Reference

Property and Method Reference


                  Data      Name          Required  Description
                  type

                                        information for a pixel. The first byte describes the first eight
                                               pixels, the second byte describes the next eight pixels, and so on.
                                                                If a bit is zero, LabVIEW draws the corresponding pixel as
                                          transparent. If the array is empty, LabVIEW draws all pixels
                                      without transparency. If the array does not contain a bit for each
                                             pixel in the image, LabVIEW draws any pixels missing from the
                                          array without transparency.
                                                        • colors—Array of RGB color values that correspond to the values in
                                     image. The value of image depth determines how LabVIEW
                                            interprets the value of this output. If image depth is 24, LabVIEW
                                         ignores this output. If image depth is 8, the array has 256
                                       elements. If image depth is 4, the array has 16 elements. If image
                                   depth is 1, the array has 2 elements.
                                                        • Rectangle—Cluster that contains coordinates that describe the
                                   bounding rectangle of the image, where the upper-left corner is at
                                                   (0,0). The bottom right edges of the bounds does not include the
                                      image.


       Maximum                   No        Sets the maximum width of the scaled image.
        Width

       Maximum
                   No        Sets the maximum height of the scaled image.        Height

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                                  Yes


9806   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9806 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9807 ordinal=9807 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

FrontFront Panel:OpenPanel:Open

Opens the front panel window. If the front panel is already open, this method changes
the state of the front panel window to the state you wire to this method.

Use the Front Panel:Close method to close the front panel window.

You also can use the Front Panel Window:State property to set the state of a front
panel window that is already open.

Parameters

          Data Name         Required  Description          type

                                           If FALSE (default), the front panel window does not open as the active
 Activate?      No
                        window. If TRUE, the front panel window opens as the active window.


                           Sets the state in which to open the front panel window.

 State        No                                Invalid—If you set the input to this value, the method returns an
                         0
                                    error.


                                                    © National Instruments 9807

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9807 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9808 ordinal=9808 -->
## Property and Method Reference

Property and Method Reference


                 Data      Name         Required  Description
                 type


                                   Standard (default)—Opens the front panel window but does not                                1                                      minimize, maximize, or hide the window.

                                    Closed—If you set the input to this value, the method returns an                                2
                                              error.

                               Hidden—Opens the front panel window as floating but not visible.
                                                              If you set the input to this value and close all references to the
                                          front panel, the window remains open but hidden. Because the VI                                3
                                                    is open, the Getting Started window does not appear. To solve this
                                    problem, open the VI from the operating system. For example, on
                                  Windows, double-click the VI in Windows Explorer to open the VI.

                                4 Minimized—Opens the front panel window as minimized.

                                5 Maximized—Opens the front panel window as maximized.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes


9808   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9808 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9809 ordinal=9809 -->
## Property and Method Reference

Property and Method Reference


 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Server\VI
   Properties\VI Properties - Front Panel States.vi
FrontFront Panel:Run-TimePanel:Run-Time Position:CenteredPosition:Centered

Configures the referenced VI to center its front panel every time the VI runs. If the VI is
running when you call this method, the change does not take effect until the next time
the VI runs.

If you want to change the position of the VI while it is running, use the Front Panel
Window:Window Bounds property instead.

This method is similar to selecting Centered from the Position pull-down menu on the
Window Run-Time Position page of the VI Properties dialog box.

Parameters

         Data Name        Required  Description
         type

                            Specifies the monitor on which the front panel window appears, if you
                       have multiple monitors. The value 0 is the primary monitor and is the
                           default value. If you specify a value other than 0, the VI runs on that
 Monitor      No        monitor. If you specify a monitor number greater than the number of
                        monitors on the system, or if you specify a negative number, LabVIEW
                           returns an error. The monitor number corresponds to the video card you
                         plug the monitor in to.


                                                    © National Instruments 9809

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9809 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9810 ordinal=9810 -->
## Property and Method Reference

Property and Method Reference


                Data      Name        Required  Description
                type

                                    Indicates the size of the window. For single-pane front panels, Size
                                      refers to the content area of that pane, not including the scroll bars. For
                                 multi-pane front panels, Size refers to the entire front panel, including         Size        No
                              any visible scroll bars. LabVIEW returns an error if you set the width or
                                  height to 0 or set the width or height less than the minimum window
                                          size.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

    FrontFront Panel:Run-TimePanel:Run-Time Position:CustomPosition:Custom

       Configures the referenced VI to open its front panel in a custom position every time the


9810   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9810 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9811 ordinal=9811 -->
## Property and Method Reference

Property and Method Reference

VI runs. If the VI is running when you call this method, the change does not take effect
until the next time the VI runs.

If you want to change the position of the VI while it is running, use the Front Panel
Window:Window Bounds property instead.

This method is similar to selecting Custom from the Position pull-down menu on the
Window Run-Time Position page of the VI Properties dialog box.

Parameters

         Data
 Name         Required  Description         type

 Position      No        Indicates the top left coordinate of the front panel window position.


                            Indicates the size of the window. For single-pane front panels, Size
                              refers to the content area of that pane, not including the scroll bars. For
                         multi-pane front panels, Size refers to the entire front panel, including Size         No
                       any visible scroll bars. LabVIEW returns an error if you set the width or
                          height to 0 or set the width or height less than the minimum window
                                size.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

                                                    © National Instruments 9811

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9811 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9812 ordinal=9812 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

    FrontFront Panel:Run-TimePanel:Run-Time Position:GetPosition:Get PositionPosition

       Returns the default position of the front panel window at run-time.

     Parameters

                Data      Name         Required  Description                 type

                                 Returns whether the front panel is unchanged, centered, maximized,        Type        No                                 minimized, or has a custom setting.


         Position      No        Indicates the top left coordinate of the front panel window position.


                                    Indicates the size of the window. For single-pane front panels, Size
                                       refers to the content area of that pane, not including the scroll bars. For
                                 multi-pane front panels, Size refers to the entire front panel, including
         Size         No
                              any visible scroll bars. LabVIEW returns an error if you set the width or
                                  height to 0 or set the width or height less than the minimum window
                                          size.


                                     Specifies the monitor on which the front panel window appears, if you
                               have multiple monitors. The value 0 is the primary monitor and is the
        Monitor      No
                                    default value. If you specify a value other than 0, the VI runs on that
                                  monitor. If you specify a monitor number greater than the number of


9812   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9812 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9813 ordinal=9813 -->
## Property and Method Reference

Property and Method Reference


         Data Name         Required  Description
         type

                         monitors on the system, or if you specify a negative number, LabVIEW
                           returns an error. The monitor number corresponds to the video card
                       you plug the monitor in to.


 Use                         Returns the value of the Use Current Position checkbox in the Window
 Current      No                       Run-Time Position dialog box. Position

 Use                         Returns the value of the Use Current Size checkbox in the Window Run- Current      No                      Time Position dialog box. Size

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No


                                                    © National Instruments 9813

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9813 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9814 ordinal=9814 -->
## Property and Method Reference

Property and Method Reference

    FrontFront Panel:Run-TimePanel:Run-Time Position:MaximizedPosition:Maximized

       Configures a VI to maximize its front panel every time the VI runs. If the VI is running
     when you call this method, the change does not take effect until the next time the VI
       runs.

           If you want to change the position of the VI while it is running, use the Front Panel
      Window:Window Bounds property instead.

       This method is similar to selecting Maximized from the Position pull-down menu on
       the Window Run-Time Position page of the VI Properties dialog box.

     Parameters

                Data      Name        Required  Description                type

                                    Specifies the monitor on which the front panel window appears, if you
                              have multiple monitors. The value 0 is the primary monitor and is the
                                    default value. If you specify a value other than 0, the VI runs on that
        Monitor      No        monitor. If you specify a monitor number greater than the number of
                                monitors on the system, or if you specify a negative number, LabVIEW
                                   returns an error. The monitor number corresponds to the video card you
                                 plug the monitor in to.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No


9814   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9814 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9815 ordinal=9815 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

FrontFront Panel:Run-TimePanel:Run-Time Position:MinimizedPosition:Minimized

Sets a VI to minimize its front panel every time the VI runs. If the VI is running when you
call this method, the change does not take effect until the next time the VI runs.

This method is similar to selecting Minimized from the Position pull-down menu on
the Window Run-Time Position page of the VI Properties dialog box.

Parameters

         Data Name        Required  Description
         type

                            Specifies the monitor on which the front panel window appears, if you
                       have multiple monitors. The value 0 is the primary monitor and is the
                           default value. If you specify a value other than 0, the VI runs on that
 Monitor      No        monitor. If you specify a monitor number greater than the number of
                        monitors on the system, or if you specify a negative number, LabVIEW
                           returns an error. The monitor number corresponds to the video card you
                         plug the monitor in to.


Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 9815

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9815 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9816 ordinal=9816 -->
## Property and Method Reference

Property and Method Reference


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

    FrontFront Panel:Run-TimePanel:Run-Time Position:UnchangedPosition:Unchanged

       Configures the VI to maintain the position of its front panel window when the VI runs.

       This method is similar to selecting Unchanged from the Position pull-down menu on
       the Window Run-Time Position page of the VI Properties dialog box.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No


9816   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9816 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9817 ordinal=9817 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

GetGet CompileCompile MetricsMetrics

Returns a string that describes transform metrics from the most recent compile of the
VI, if metric recording was enabled.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

 Must wait until user interface is idle                                     No

 Available with control VIs                                            No

 Available with global VIs                                            No

 Available with strict type definitions                                    No

                                                    © National Instruments 9817

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9817 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9818 ordinal=9818 -->
## Property and Method Reference

Property and Method Reference


         Available with polymorphic VIs                                        No

   GetGet ConpaneConpane ImageImage

       Returns the connector pane image, as it appears in the Context Help window, as a
        cluster of image data so you can draw it as a picture using the Draw Flattened Pixmap
        VI or save the image to a file using the Graphics Formats VIs.

      The clusters returned by this method are similar to the image data output of the Read
      JPEG File, Read PNG File, and Read BMP File VIs.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

        Must wait until user interface is idle                                     No

         Available with control VIs                                            No

         Available with global VIs                                            No

         Available with strict type definitions                                    No

         Available with polymorphic VIs                                        No


9818   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9818 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9819 ordinal=9819 -->
## Property and Method Reference

Property and Method Reference

GetGet ControlControl IndexIndex byby NameName

Gets the index for the control or indicator of the given name. If the control or indicator
for which you want to get an index does not have a terminal on the block diagram, this
method returns an error.

You can use this method to specify the controls for which you get or set values with the
Get Control Values by Index or Set Control Values by Index functions.

Parameters

           Data Name             Required  Description
            type

 Control                         Specifies the name of the control or indicator for which LabVIEW                     Yes
 Name                            retrieves an index.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

 Must wait until user interface is idle                                     No

 Available with control VIs                                                          Yes

 Available with global VIs                                                           Yes

                                                    © National Instruments 9819

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9819 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9820 ordinal=9820 -->
## Property and Method Reference

Property and Method Reference


         Available with strict type definitions                                    No

         Available with polymorphic VIs                                        No

   GetGet LibraryLibrary AccessAccess ScopeScope

       Returns the access scope or inherited access scope of this VI if it is owned by a LabVIEW
       project library. This method provides the same information as the method Source
      Scope:Get of the Project Library class without requiring a reference to the owning
       project library.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

        Must wait until user interface is idle                                     No

         Available with control VIs                                                          Yes

         Available with global VIs                                                           Yes

         Available with strict type definitions                                    No

         Available with polymorphic VIs                                                     Yes


9820   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9820 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9821 ordinal=9821 -->
## Property and Method Reference

Property and Method Reference

GetGet ObjectRefObjectRef FromFrom BookmarkIDBookmarkID

Returns a reference to the object, such as the label, that contains the bookmark.

Parameters

               Data Name                  Required  Description               type

 Bookmark ID             Yes       ID of a specific bookmark in the specified VI.


 Object                            Reference to the object that contains the bookmark, such as                         Yes
 Reference                         the label.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                               Yes

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                 No

 Available with strict type definitions                         No


                                                    © National Instruments 9821

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9821 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9822 ordinal=9822 -->
## Property and Method Reference

Property and Method Reference


         Available with polymorphic VIs                             No

   GetGet VIVI BookmarksBookmarks

       Returns the bookmark information for the specified VI reference. You must load the VI
       into memory in order to read the bookmark information. This method returns an error
           if the VI is password protected or if the VI does not have a block diagram.

     Parameters

                      Data
      Name                Required  Description                       type

       Bookmark                        Array of clusters that contain the bookmark ID, the bookmark                                Yes         Information                         tag, and the full text of the label.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                 No


9822   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9822 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9823 ordinal=9823 -->
## Property and Method Reference

Property and Method Reference


 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

GetGet VIVI DependenciesDependencies (Names(Names andand Paths)Paths)

This method returns the names and paths of the VI dependencies of a VI. You can use
this method to return a specific subset of the total set of VI dependencies of a VI. This
method does not return non-VI dependencies, such as project libraries, XControls,
classes, and statecharts.

LabVIEW combines the parameter values you specify using the logical AND operator to
determine which dependencies to return. For example, you must pass TRUE to both
Static VI Refs? and Include Control VIs? in order for LabVIEW to return a static VI
reference to a custom control or indicator.

By default, this method does not load the block diagram into memory. However, if you
specify certain input values, LabVIEW loads the block diagram.

Parameters

             Data
 Name             Required  Description             type

                             Returns the fully qualified names, which include the names of
 Dependency
               No       owning project libraries, of VI dependencies. This parameter is Names
                                  similar to the This VI's SubVIs item in the View Menu.


 Dependency
               No       Returns the directory paths of VI dependencies.
 Paths


                                                 If FALSE (default), LabVIEW returns only the dependencies of the
 Whole                        current VI. If TRUE, LabVIEW returns all dependencies for the entire
               No
 Hierarchy?                       VI hierarchy. Use the TRUE case to perform hierarchy traversals
                             without having to implement recursion detection yourself.


                                                    © National Instruments 9823

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9823 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9824 ordinal=9824 -->
## Property and Method Reference

Property and Method Reference


                    Data      Name             Required  Description
                     type

                                         Specifies whether LabVIEW returns dependencies that LabVIEW
                                  does not invoke, such as those in the Disable case of a Diagram
                                       Disable structure. Also, if you wire a constant to the selector
                                       terminal of a Case structure, LabVIEW considers dependencies in
                                     non-executing cases to be commented out and does not invoke
                                   them.

       Commented
        Out            No          Only include commented out diagrams if diagram already                                   0
        Diagrams?                      loaded
                                   1 Never include commented out diagrams (default)

                                       Always include commented out diagrams—This option causes
                                    LabVIEW to load the block diagrams of VI dependencies. If a                                   2                                         block diagram requires a password not currently in the
                                    LabVIEW password cache, LabVIEW returns an error.


                                                              If TRUE, LabVIEW returns VIs referenced with Static VI Reference          Static VI                     No        functions, including the top-level VI if it contains a reference to
         Refs?                                                      itself. The default is FALSE.


                                         Specifies which VIs LabVIEW returns if the VI contains a dynamic
                                       dispatch subVI.

                                   0 No dynamic dispatch VIs (default)
       Dynamic                     No           Include nearest implementation—Returns only the VI whose
         Dispatching?                                   1  icon LabVIEW display on the node. This VI is the
                                       implementation nearest to the wired class data type.

                                          Include all overrides—Returns all VIs currently in memory to
                                   2
                                     which the node could dispatch at run time.


         Include
         Missing         No            If TRUE, LabVIEW returns names and paths for any missing
         Items?

9824   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9824 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9825 ordinal=9825 -->
## Property and Method Reference

Property and Method Reference


            DataName             Required  Description
            type

                            dependencies. LabVIEW returns dependencies as missing if they
                              are corrupt, saved in a later version of LabVIEW, or if they cannot be
                           found on disk. Since the types of missing dependencies are
                         unknown, LabVIEW returns missing dependencies regardless of
                      how you configure other parameters. The default is FALSE.


Include                                                If TRUE, LabVIEW returns subVIs, including polymorphic VIStandard        No                               instances and instantiations of generic VIs. The default is FALSE.VIs?


                                Specifies whether LabVIEW returns clone VIs of reentrant VIs that
                              are dependencies.

Include
Reentrant        No        0  Include the clone VI (default)
Clones?                           1  Include the original reentrant VI instead of the clone VI

                           2  Include both the original reentrant VI and the clone VI


Include Poly               No            If TRUE, LabVIEW returns polymorphic VIs. The default is FALSE.VIs?

Include
               No            If TRUE, LabVIEW returns global VIs. The default is FALSE.Global VIs?


Include                                     If TRUE, LabVIEW returns type definitions and strict type
               No
Control VIs?                     definitions. The default is FALSE.


Include
               No            If TRUE, LabVIEW returns generic VIs. The default is FALSE.
Generic VIs?

Include
                                                If TRUE, LabVIEW returns subVI calls that use the alternative Call
Alternate        No
                          Setup options, such as Reload for each call or Load and retain on
Call Setups?


                                                    © National Instruments 9825

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9825 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9826 ordinal=9826 -->
## Property and Method Reference

Property and Method Reference


                    Data      Name             Required  Description
                     type

                                                  first call. Because these VIs are dynamically loaded, they may or
                             may not be in memory. To include any VIs missing from memory,
                                          set the Include Missing Items to TRUE. To bring any missing items
                                         into memory in a development environment, set Load Block
                                 Diagram to TRUE. The default is FALSE.


                                                              If FALSE (default), LabVIEW returns the names of the hidden
                                       instance VIs that underlie the Express VIs and malleable VIs. If
       Keep                      TRUE, LabVIEW returns the Express VIs and malleable VIs as
         Express and                  dependencies. If you want edit-time dependencies, set Keep                     No         Malleable                    Express and Malleable VIs? to TRUE. If you want run-time
          VIs?                         dependencies, set Keep Express and Malleable VIs? to FALSE.
                                      Regardless of this setting, LabVIEW includes the subVIs of the
                                       instance VIs as dependencies of the referenced VI.


                                                              If TRUE, LabVIEW loads this VI block diagram before it evaluates
                                   whether any dependencies exist. If you open a block diagram from
        Load Block                     No       a location that is different from the location in which it is originally        Diagram?                                      saved, LabVIEW may load new subVIs into memory. This may affect
                                     the Include Alternate Call Setup VIs? option. The default is FALSE.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No


9826   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9826 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9827 ordinal=9827 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                                 Yes

 Available with polymorphic VIs                                      Yes

LockLock State:GetState:Get

Returns the lock state of the VI and indicates whether the password for the VI is in the
password cache.

Parameters

                Data Name                   Required  Description                type

 Password in                           Indicates whether the password is currently in the                     No Cache                            password cache.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

                                                    © National Instruments 9827

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9827 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9828 ordinal=9828 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

        Must wait until user interface is idle                                                Yes

         Available with control VIs                                                          Yes

         Available with global VIs                                                           Yes

         Available with strict type definitions                                    No

         Available with polymorphic VIs                                                     Yes

   LockLock State:SetState:Set

       Sets the lock state of a VI. If interactive is FALSE (default), you can use password to
       either unlock a password-protected VI or set the password of an unprotected VI. If
       interactive is TRUE, LabVIEW ignores password and displays a dialog box that prompts
      you to change the lock state.

       This method is similar to the Unlocked (no password), Locked (no password), and
      Password-protected options on the Protection page of the VI Properties dialog box.

     Parameters

                  Data      Name           Required  Description
                   type

                                       Specifies the level of editing permission of the VI.

                                  0  invalid lock state

                                  1 Not Locked—Users can see and edit the block diagram.
        Lock State        Yes
                                   Locked (No Password)—Users can see but not edit a block
                                  2
                                      diagram.

                                    Password-protected—Users cannot see or edit the block
                                  3
                                    diagram without a password.


9828   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9828 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9829 ordinal=9829 -->
## Property and Method Reference

Property and Method Reference


           Data Name           Required  Description
           type

                               Specifies whether to display a dialog box that prompts you to change Interactive      No                            the lock state. The default is FALSE.


                                              If lock state is Password-protected, password is the new password. If
 Password      No       you are changing lock state from Password-protected, password is
                            the old password. The default is an empty string.


 Put in                                    If Lock State is Password-protected, Put in Cache specifies whether              No Cache                       to place the new password in the cache. The default is FALSE.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes


                                                    © National Instruments 9829

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9829 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9830 ordinal=9830 -->
## Property and Method Reference

Property and Method Reference

   MoveMove ObjectsObjects

      Moves the objects by the offset amount of pixels.

     Parameters

                Data      Name          Required  Description                type

         Objects          Yes      The objects you want to move.


         Offset           Yes      The offset amount of pixels you want to move the objects.


                               The owner of the objects. Specify the owner if you also want to update       Owner        No                                   the owner position.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No


9830   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9830 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9831 ordinal=9831 -->
## Property and Method Reference

Property and Method Reference


 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

PausePause VIVI

Pauses or unpauses the VI execution.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

PopulatePopulate AsynchronousAsynchronous CallCall PoolPool

Ensures that the asynchronous call pool for a VI reference contains at least the number
of data spaces specified by the Minimum Size parameter. By default, when you open a

                                                    © National Instruments 9831

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9831 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9832 ordinal=9832 -->
## Property and Method Reference

Property and Method Reference

       reference with the Open VI Reference function, LabVIEW allocates one data space per
     CPU core on the development computer.

      Use this method to ensure deterministic execution of asynchronous VI calls. Set the
     Minimum Size of the call pool to the maximum number of calls that you expect to
     make to the referenced VI. This prevents LabVIEW from needing to allocate data spaces
        in the asynchronous call pool on demand, thereby avoiding the jitter of memory
        allocation.

      You cannot decrease the size of the asynchronous call pool. Use the Current Size
      output of this method to identify the current number of data spaces allocated for the
       referenced VI.

      LabVIEW deallocates the call pool when it closes the corresponding VI reference.

     Parameters

                 Data
      Name          Required  Description                  type

         Current                   Current Size returns the current number of data spaces in the
                         Yes         Size                     asynchronous call pool for the referenced VI.


                           Minimum Size determines the number of data spaces that the
       Minimum                asynchronous call pool of the referenced VI is required to have. If you                   No         Size                       wire a number to this input that is smaller than the Current Size of the
                                asynchronous call pool, the size of the call pool remains unchanged.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes


9832   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9832 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9833 ordinal=9833 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                  No

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Server\
   Asynchronous Call By Reference\Populating the
   Asynchronous Call Pool.vi
Print:PanelPrint:Panel ToTo PostScriptPostScript

Prints the panel of the VI to the specified PostScript file.

Parameters

           Data
 Name            Required  Description
           type

 PostScript
                   Yes        Specifies the path to the PostScript file.
 File


 Append?        No        Specifies whether LabVIEW appends the new information to an


                                                    © National Instruments 9833

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9833 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9834 ordinal=9834 -->
## Property and Method Reference

Property and Method Reference


                  Data      Name            Required  Description
                  type

                                          existing file. The default is FALSE.


         Entire                                      If Entire Panel? is FALSE (default), only the currently visible portion                     No         Panel?                         of the front panel prints.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    Print:PanelPrint:Panel ToTo PrinterPrinter

       Prints just the front panel to the current printer. You cannot use this method to print a
       block diagram, list of controls, or polymorphic VI front panel.

9834   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9834 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9835 ordinal=9835 -->
## Property and Method Reference

Property and Method Reference

Parameters

          Data Name            Required  Description
          type

 Entire                                     If Entire Panel? is FALSE (default), only the currently visible portion              No Panel?                        of the front panel prints.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

Print:VIPrint:VI ToTo HTMLHTML

Saves the VI information to an HTML file and saves the graphics in external files. You
can use the Open URL in Default Browser VI to display the HTML file in the default Web
browser.

                                                    © National Instruments 9835

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9835 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9836 ordinal=9836 -->
## Property and Method Reference

Property and Method Reference

       This method is similar to the HTML file option on the Destination page of the Print
       dialog box.

     Parameters

                 Data      Name          Required  Description                  type

                                 Path to the HTML file in which you want to save the VI information. The       HTML                         Yes        directory in which you want to save the file must already exist, and you
           File Path                              must wire a full path including the HTML filename.


                                      Specifies whether LabVIEW appends the new information to an existing       Append?      No                                                   file. The default is FALSE.


                                      Specifies which VI information to print and the format of the printout.
                               You can select from Custom, Standard, Using Panel, Using SubVI, and
                                 Complete. If this input is not Custom, LabVIEW ignores all custom
                                 format properties in the Application printing property class.

                                Custom (default)—Use the Property Node with the Application
                                0                                          class printing properties to specify the format

                                    Standard—Prints the VI description, icon and connector pane,                                1                                          front panel, and block diagram.

                                    Using Panel—Prints the VI description, front panel, and controls
        Format       No                                2 and indicators, including data types, names, and descriptions.
                                 LabVIEW prints the controls and indicators in tabbing order.

                                    Using SubVI—Prints the VI description, icon and connector pane,
                                and connected controls and indicators, including data types,
                                3 names, and descriptions. LabVIEW prints the controls and
                                          indicators in tabbing order. This format is similar to the format of
                                      the VI and function reference topics in the LabVIEWHelp.

                                   Complete—Prints the VI description; icon and connector pane;
                                4  front panel; controls and indicators, including data types, names,
                                and descriptions; block diagram; a list of subVIs, including icons,


9836   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9836 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9837 ordinal=9837 -->
## Property and Method Reference

Property and Method Reference


          Data Name          Required  Description
          type


                           names, and paths; revision history information; and the VI
                                 hierarchy.


                            Select the format of the graphic files.

 Image                   0       PNG (default)             No Format                         1        JPEG

                         2         GIF


                            Sets the color depth, or number of supported colors, of the image: 1
 Image             No          (1-bit, black and white), 4 (4-bit, 16 colors), 8 (8-bit, 256 colors), or 24
 Depth                                (24-bit, true color). The default is 8.


                          Path to the directory in which you want to save the graphic files. The
 Image                      directory in which you want to save the files must already exist. If not             No Directory                    specified, LabVIEW saves the image files in the same directory as the
                    HTML or RTF file.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                                  Yes


                                                    © National Instruments 9837

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9837 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9838 ordinal=9838 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                                  Yes

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

    Print:VIPrint:VI ToTo PrinterPrinter

       Prints the VI information to a printer.

           If you use this method in a stand-alone application or shared library, LabVIEW prints
       only the front panel. This method is similar to the Printer option on the Destination
      page of the Print dialog box.

     Parameters

                 Data      Name          Required  Description
                  type

                                      Specifies which VI information to print and the format of the printout.
                               You can select from Custom, Standard, Using Panel, Using SubVI, and
                                 Complete. If this input is not Custom, LabVIEW ignores all custom
                                  format properties in the Application printing property class.

        Format       No         Custom (default)—Use the Property Node with the Application                                 0
                                          class printing properties to specify the format

                                    Standard—Prints the VI description, icon and connector pane,
                                 1
                                          front panel, and block diagram.

                                 2 Using Panel—Prints the VI description, front panel, and controls


9838   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9838 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9839 ordinal=9839 -->
## Property and Method Reference

Property and Method Reference


         DataName          Required  Description
          type


                         and indicators, including data types, names, and descriptions.
                          LabVIEW prints the controls and indicators in tabbing order.

                            Using SubVI—Prints the VI description, icon and connector pane,
                         and connected controls and indicators, including data types,
                         3 names, and descriptions. LabVIEW prints the controls and
                                indicators in tabbing order. This format is similar to the format of
                             the VI and function reference topics in the LabVIEWHelp.

                           Complete—Prints the VI description; icon and connector pane;
                                 front panel; controls and indicators, including data types, names,
                         4 and descriptions; block diagram; a list of subVIs, including icons,
                          names, and paths; revision history information; and the VI
                                 hierarchy.


Scale                       Specifies whether LabVIEW scales the front panel to fit the page. The            NoPanel?                      default is TRUE.


Scale                       Specifies whether LabVIEW scales the block diagram to fit the page.            NoDiagram?               The default is TRUE.


                             Specifies whether LabVIEW prints page headers (which include thePage            No       page number, VI name, and last modification date). The default isHeaders?
                        TRUE.


                             Specifies whether LabVIEW inserts page breaks between the following
Page                        sections: connector icon and description, front panel, list of front panel
            No
Breaks?                    control details, block diagram, block diagram details, VI hierarchy, and
                                      list of subVIs. The default is FALSE.


Section                     Specifies whether to print headers for each section listed above. If
            No
Headers?               Format is Custom, Standard, or Complete, the default is TRUE.


                                                    © National Instruments 9839

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9839 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9840 ordinal=9840 -->
## Property and Method Reference

Property and Method Reference


                 Data      Name          Required  Description
                  type

                                   Otherwise, the default is FALSE.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                                  Yes

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

    Print:VIPrint:VI ToTo RTFRTF

      Saves the VI information to an RTF file.

       This method is similar to the Rich Text Format (RTF) file option on the Destination
      page of the Print dialog box.


9840   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9840 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9841 ordinal=9841 -->
## Property and Method Reference

Property and Method Reference

Parameters

          Data Name          Required  Description
          type

                          Path to the RTF file in which you want to save the VI information. The RTF File                 Yes        directory in which you want to save the file must already exist, and you Path                       must wire a full path including the RTF filename.


                             Specifies whether LabVIEW appends the new information to an existing
 Append?      No                                        file. The default is FALSE.


                             Specifies which VI information to print and the format of the printout.
                        You can select from Custom, Standard, Using Panel, Using SubVI, and
                         Complete. If this input is not Custom, LabVIEW ignores all custom
                          format properties in the Application printing property class.

                         Custom (default)—Use the Property Node with the Application                         0                                 class printing properties to specify the format

                             Standard—Prints the VI description, icon and connector pane,                         1                                 front panel, and block diagram.

                            Using Panel—Prints the VI description, front panel, and controls
                         2 and indicators, including data types, names, and descriptions.
 Format       No                          LabVIEW prints the controls and indicators in tabbing order.

                            Using SubVI—Prints the VI description, icon and connector pane,
                          and connected controls and indicators, including data types,
                         3 names, and descriptions. LabVIEW prints the controls and
                                 indicators in tabbing order. This format is similar to the format of
                              the VI and function reference topics in the LabVIEWHelp.

                            Complete—Prints the VI description; icon and connector pane;
                                 front panel; controls and indicators, including data types, names,
                         4 and descriptions; block diagram; a list of subVIs, including icons,
                           names, and paths; revision history information; and the VI
                                 hierarchy.


                                                    © National Instruments 9841

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9841 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9842 ordinal=9842 -->
## Property and Method Reference

Property and Method Reference


                 Data      Name          Required  Description
                  type

                               Format of the graphics file.
        Image                   No        Format                                0  BMP (default)—BMP is the only format supported.


                                    Sets the color depth, or number of supported colors, of the image: 1
        Image                   No          (1-bit, black and white), 4 (4-bit, 16 colors), 8 (8-bit, 256 colors), or 24        Depth                                          (24-bit, true color). The default is 8.


                                 Path to the directory in which you want to save the graphic files. The
        Image                      directory in which you want to save the files must already exist. If not                   No         Directory                    specified, LabVIEW saves the image files in the same directory as the
                          HTML or RTF file.


                                      Specifies whether to save the graphics externally and place references
                                        in the RTF file. Set this parameter to TRUE if you are creating a help file.
                              The default is FALSE. If TRUE, LabVIEW does not embed the graphics in
                                  the RTF file. Instead, LabVIEW saves the graphics as external bitmap
        Help                             files in the directory you wire to the Image Directory parameter, and                   No
        Format?                    creates a reference to each bitmap in the RTF file so you can compile
                                  the RTF file into a help file. The RTF file also includes footnotes that the
                                RTF-based help compiler uses to identify each topic in a help file. If
                                  FALSE, LabVIEW embeds each graphic in the RTF file, and does not add
                                   footnotes to the RTF file.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

9842   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9842 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9843 ordinal=9843 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                      Yes

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

Print:VIPrint:VI ToTo TextText

Saves the VI information to a text file. You cannot save the icon, connector pane, front
panel, block diagram, subVI icons, and VI hierarchy to text.

This method is similar to the Plain text file option on the Destination page of the Print
dialog box.

Parameters

          Data Name         Required  Description
          type

                         Path to the text file in which you want to save the VI information. The
 Text File
                Yes        directory in which you want to save the file must already exist, and you
 Path
                       must wire a full path including the text filename.


                             Specifies whether LabVIEW appends the new information to an existing
 Append?      No
                                       file. The default is FALSE.


                                                    © National Instruments 9843

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9843 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9844 ordinal=9844 -->
## Property and Method Reference

Property and Method Reference


                 Data      Name         Required  Description
                 type

                                     Specifies which VI information to print and the format of the printout.
                               You can select from Custom, Standard, Using Panel, Using SubVI, and
                                 Complete. If this input is not Custom, LabVIEW ignores all custom
                                 format properties in the Application printing property class.

                               Custom (default)—Use the Property Node with the Application                                0                                          class printing properties to specify the format

                                    Standard—Prints the VI description, icon and connector pane,                                1                                          front panel, and block diagram.

                                   Using Panel—Prints the VI description, front panel, and controls
                                2 and indicators, including data types, names, and descriptions.
        Format       No                                 LabVIEW prints the controls and indicators in tabbing order.

                                   Using SubVI—Prints the VI description, icon and connector pane,
                                and connected controls and indicators, including data types,
                                3 names, and descriptions. LabVIEW prints the controls and
                                         indicators in tabbing order. This format is similar to the format of
                                     the VI and function reference topics in the LabVIEWHelp.

                                   Complete—Prints the VI description; icon and connector pane;
                                          front panel; controls and indicators, including data types, names,
                                4 and descriptions; block diagram; a list of subVIs, including icons,
                                  names, and paths; revision history information; and the VI
                                         hierarchy.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes


9844   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9844 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9845 ordinal=9845 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

RemoteRemote Panel:ClientPanel:Client ConnectionsConnections

Returns an array of clusters containing connection information about the clients
viewing or controlling the VI.

LabVIEW opens a connection on the server computer when another application
instance or a related application, such as a Web browser, requests to view the front
panel of a VI in memory on the server computer.

This method can return networking error codes.

Parameters

             Data
 Name            Required  Description
             type

                              Describes the clients viewing or controlling the VI.

                               Name of the VI being viewed or controlled by the
                                    VI Name Remote                                                   client.
 Panel              Yes
 Connections               Remote    IP address of the client viewing or controlling the VI.
                         UserName LabVIEW user name of the client viewing or


                                                    © National Instruments 9845

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9845 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9846 ordinal=9846 -->
## Property and Method Reference

Property and Method Reference


                    Data      Name            Required  Description
                    type


                                                       controlling the VI.

                                        Port       Port that the Web Server on the client computer uses.

                                         An enumeration type that specifies the controlling                                        Status
                                                      status of the connection.

                                       Create    A time stamp that specifies in seconds when the
                                 Time      connection was created.

                                        Status     A time stamp that specifies in seconds when the
                                 Time        client changed to its current connection status.

                                         A time stamp that indicates when the server will
                                                    regain control of the VI or transfer control to another
                                       Control                                                             client. A value of MM/DD/YY indicates that you did                                End Time
                                                not set a time limit for the VI in the Visible VIs section
                                                      of the Web Server page of the Options dialog box.


       Remote                      Index of the client in Remote Panel Connections currently
        Panel              Yes        controlling the VI. A value of –1 indicates that no client is
         Controller                      controlling the VI and that the server is in control.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

9846   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9846 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9847 ordinal=9847 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                  No

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Remote Panels\Remote
   Panel Methods.lvproj
RemoteRemote Panel:ClosePanel:Close ConnectionConnection ToTo ClientClient

Closes a remote front panel connection to a client.

This method can return networking error codes.

Parameters

            Data
 Name              Required  Description            type

 Client                            IP address or computer name of the client whose connection you
                      Yes
 Address                     want to close.


 Client Port           Yes       Port that the Web Server on the client computer uses.


Remarks

The following table lists the characteristics of this method.

                                                    © National Instruments 9847

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9847 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9848 ordinal=9848 -->
## Property and Method Reference

Property and Method Reference


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                  No

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Remote Panels\Remote
        Panel Methods.lvproj
   RemoteRemote Panel:LockPanel:Lock ControlControl

       Returns control of the front panel to the server and queues any requests from clients
       to control the front panel. LabVIEW ignores this method if the front panel is already
       locked.

       This method is similar to the Regain Control and Lock Control shortcut menu items on
       the front panel of a running VI.


9848   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9848 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9849 ordinal=9849 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                  No

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Remote Panels\Remote
   Panel Methods.lvproj
RemoteRemote Panel:UnlockPanel:Unlock ControlControl

If the front panel is locked, this method grants control to the next client in the queue. If
no clients are in the queue, the method unlocks the front panel. LabVIEW ignores this
method if the front panel is already unlocked.

This method is similar to the Unlock Control shortcut menu item on the front panel of

                                                    © National Instruments 9849

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9849 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9850 ordinal=9850 -->
## Property and Method Reference

Property and Method Reference

      a running VI.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                  No

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Remote Panels\Remote
        Panel Methods.lvproj
    ReplicateReplicate ConpaneConpane

      Make the connector pane of the VI Reference match the given connector pane.


9850   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9850 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9851 ordinal=9851 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name      Data type    Required    Description

 Conpane                  Yes         The connector pane you want the VI to have.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                               Yes

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

RevertRevert VIVI

Discards changes and reloads a VI from disk.

This method is similar to the Revert item on the File menu.


                                                    © National Instruments 9851

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9851 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9852 ordinal=9852 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                                  Yes

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

   RunRun VIVI

        Starts the VI execution, similar to the Run button. This method is different than calling
      a VI because it uses the current values of all front panel controls for execution rather
      than using data passed in through parameters. This method also ignores the
      Execution:Show Front Panel On Call property of a VI and the Execution:Close After Call
       property.

           Note This method requires the VI to have a front panel. If you are using the
               Application Builder, make sure you do not remove the front panel.

      You cannot use this method to run a VI that is already reserved for execution by
      another VI.

9852   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9852 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9853 ordinal=9853 -->
## Property and Method Reference

Property and Method Reference

If you use the Open VI Reference function and wire the type specifier VI Refnum input,
you cannot use the reference returned by the function with this method. Instead, you
must use the Call By Reference node.

If you want to use this method with a reentrant VI, set the options parameter to 0x08
in the Open VI Reference function to prepare the VI for reentrant run.

Parameters

          Data Name          Required  Description           type

                              Specifies whether to wait until the VI completes execution before the
                           Invoke Node continues executing. The default is TRUE.

                              Tip Use the Start Asynchronous Call node instead of the
 Wait Until                      Run VI method to run target VIs asynchronously. In             No
 Done                               addition to providing a simpler interface, the Start
                                 Asynchronous Call node allows you to collect the outputs
                                       of the target VI with a corresponding Wait On
                                 Asynchronous Call node.


                           Allows you to run a VI independently of the caller without opening its
                              front panel immediately or opening another reference inside the
                              target VI. If TRUE, the referenced VI transfers ownership of the
                             reference from the calling VI to the VI that is running. This means
                        LabVIEW disposes of the reference, along with the parallel data space,
                      when the target VI goes idle, not when the VI that opened the
                             reference goes idle. The reference can still be used by the calling VI
                                until the target VI closes the reference. The calling VI does not need to
 Auto                             close the reference unless the Run VI method returns an error. If the
 Dispose       No                                calling VI does close the reference, the target VI can abort and leave
 Reference                       memory. If FALSE, LabVIEW automatically disposes of the VI reference
                      when the VI that opened it goes idle. The default is FALSE.

                           Note If Auto Dispose Ref is TRUE and the method returns
                               an error, LabVIEW does not transfer ownership of the
                                      reference to the target VI. LabVIEW will not automatically
                                    dispose of the reference when the target VI goes idle.


                                                    © National Instruments 9853

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9853 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9854 ordinal=9854 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                                  Yes

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    Save:ForSave:For PreviousPrevious

      Saves a copy of the VI that is readable by LabVIEW version 8.0 and later. If you save a
       password-protected VI for a previous LabVIEW version, you must enter the password.
      You can enter the password programmatically as an input on the Open VI Reference
       function.

       This method is similar to the LabVIEW Version option on the Save for Previous Version
       dialog box.


9854   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9854 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9855 ordinal=9855 -->
## Property and Method Reference

Property and Method Reference

Parameters

          Data Name          Required  Description
          type

 Path to
 Saved          Yes       Path to where you want to save the VI.
 File

 Warnings      No       Warnings that occurred while saving the VI.


                            Version of LabVIEW for which you want to save. Wire the version
 Target             No       number, such as 8.6 or 9.0, to the Version input. The default is the Version
                          immediately previous version.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes


                                                    © National Instruments 9855

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9855 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9856 ordinal=9856 -->
## Property and Method Reference

Property and Method Reference

   Save:InstrumentSave:Instrument

      Saves a VI that is not currently running and synchronizes the VI with the edited version
        in other application instances before saving.

       This method is similar to the Save item on the File menu.

           Note If you use this method to save a VI that is currently running, LabVIEW
               returns error 1507.

     Parameters

                Data      Name         Required  Description                 type

        Path to
        Saved       No       Designate the path of the VI file. The default is to the current location.
           File

                                                        If FALSE, change the location of the VI, including references of callers,        Save a
                  No        before saving. If TRUE, a new copy of the VI is saved to the location. The       Copy                                    default is FALSE.


        Without
                  No       Save the VI without the block diagram. The default is FALSE.        Diagram

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes


9856   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9856 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9857 ordinal=9857 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

Save:Run-TimeSave:Run-Time MenuMenu

Saves the run-time menu to a file specified by Path. This method works only when the
VI is running. It saves only menu items with valid tags.

Parameters

 Name     Data type   Required   Description

 File Path                Yes         Path to where you want to save the run-time menu.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No


                                                    © National Instruments 9857

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9857 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9858 ordinal=9858 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    Transaction:BeginTransaction:Begin UndoUndo

       Begins an undo transaction on a VI.

     Parameters

      Name      Data type         Required          Description

      Name                    No           Name of the transaction.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No


9858   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9858 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9859 ordinal=9859 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

Transaction:EndTransaction:End UndoUndo

Ends an undo transaction on a VI.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes


                                                    © National Instruments 9859

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9859 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9860 ordinal=9860 -->
## Property and Method Reference

Property and Method Reference

    Transaction:FailTransaction:Fail

        Fails the current transaction and deletes the undo information for the transaction.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    Transaction:GetTransaction:Get RedoRedo StateState

       Returns whether there is an action to redo and, if so, the text that corresponds to that
       action.


9860   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9860 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9861 ordinal=9861 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name       Data type    Required    Description

 Menu Text                  Yes         Contains the text of the item to redo or undo.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                              Yes

 Remote access allowed                                                           Yes

 Must wait until user interface is idle                                     No

 Available with control VIs                                            No

 Available with global VIs                                            No

 Available with strict type definitions                                    No

 Available with polymorphic VIs                                        No

Transaction:GetTransaction:Get UndoUndo StateState

Returns whether there is an action to undo and, if so, the text that corresponds to that
action.


                                                    © National Instruments 9861

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9861 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9862 ordinal=9862 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name       Data type    Required    Description

       Menu Text                  Yes         Contains the text of the item to redo or undo.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                              Yes

       Remote access allowed                                                           Yes

        Must wait until user interface is idle                                     No

         Available with control VIs                                            No

         Available with global VIs                                            No

         Available with strict type definitions                                    No

         Available with polymorphic VIs                                        No

   Transaction:RedoTransaction:Redo

      Redoes the last operation. This is similar to selecting Edit»Redo.

     Remarks

      The following table lists the characteristics of this method.

9862   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9862 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9863 ordinal=9863 -->
## Property and Method Reference

Property and Method Reference


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

Transaction:UndoTransaction:Undo

Undoes the last operation. This method is similar to selecting Edit»Undo.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No


                                                    © National Instruments 9863

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9863 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9864 ordinal=9864 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    VIVI Icon:GetIcon:Get AsAs ImageImage DataData

       Returns the VI icon as a cluster of image data so you can draw it as a picture using the
      Draw Flattened Pixmap VI or save the image to a file using the Graphics Formats VIs.

      You also can use the VI Icon:Save to File method to save an image of the VI icon to a
          file.

      The clusters returned by this method are similar to the image data output of the Read
      JPEG File, Read PNG File, and Read BMP File VIs.

     Parameters

                     Data      Name             Required  Description                     type

                                      Returns information about the 8-bit VI icon. The Icon Editor dialog
                                  box saves icons in both 256-color (8-bit) and monochrome (1-bit)
                                        format.

                                                            • image type—Reserved for future use.
                                                            • image depth—Specifies the color depth of the image, which is
                                          the number of bits to use to describe the color of each pixel in
         Color 256           Yes                                          the image. Valid values include 1, 4, 8, and 24 bits per pixel.
                                     image depth affects how LabVIEW interprets the values of
                                     image and colors.
                                                            • image—Array of bytes that describes the color of each pixel in
                                          the image in raster order. The value of image depth
                                         determines how LabVIEW interprets the value of this output.


9864   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9864 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9865 ordinal=9865 -->
## Property and Method Reference

Property and Method Reference


             DataName             Required  Description
             type

                                                        If image depth is 24, each pixel has three bytes to describe its
                                        color. The first byte for each pixel describes the red value, the
                               second byte describes the green value, and the third byte
                                   describes the blue value.

                                                        If image depth is 8, each pixel has one byte to describe its
                                        color. The value of each bit corresponds to an element in
                                      colors, which stores 32-bit RGB values where the most-
                                       significant byte is zero, followed in order by red, green, and
                                 blue values.

                                                        If image depth is 4, the behavior is similar to when image
                              depth is 8 except valid values in image include 0 through 15.

                                                        If image depth is 1, any value of zero in image corresponds to
                               element 0 in colors. All other values correspond to element 1
                                       in colors.

                             The size of the array might be larger than expected due to
                                 padding.
                                               • mask—Array of bytes in which each bit describes mask
                                  information for a pixel. The first byte describes the first eight
                                         pixels, the second byte describes the next eight pixels, and so
                                   on. If a bit is zero, LabVIEW draws the corresponding pixel as
                                    transparent. If the array is empty, LabVIEW draws all pixels
                                 without transparency. If the array does not contain a bit for
                               each pixel in the image, LabVIEW draws any pixels missing
                               from the array without transparency.
                                               • colors—Array of RGB color values that correspond to the
                                   values in image. The value of image depth determines how
                              LabVIEW interprets the value of this output. If image depth is
                                24, LabVIEW ignores this output. If image depth is 8, the array
                                has 256 elements. If image depth is 4, the array has 16
                                  elements. If image depth is 1, the array has 2 elements.
                                               • Rectangle—Cluster that contains coordinates that describe
                                  the bounding rectangle of the image, where the upper-left
                                  corner is at (0,0). The bottom right edges of the bounds does
                                 not include the image.


                                                    © National Instruments 9865

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9865 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9866 ordinal=9866 -->
## Property and Method Reference

Property and Method Reference


                     Data      Name             Required  Description
                     type

                                      Returns information about the 4-bit VI icon. The Icon Editor dialog
                                  box saves icons only in 256-color (8-bit) and monochrome (1-bit)
                                        format. Use the Color16 input of the VI Icon:Set From Image Data
                                method to specify the 4-bit image data you want to retrieve with
                                             this output.

                                                            • image type—Reserved for future use.
                                                            • image depth—Specifies the color depth of the image, which is
                                          the number of bits to use to describe the color of each pixel in
                                          the image. Valid values include 1, 4, 8, and 24 bits per pixel.
                                     image depth affects how LabVIEW interprets the values of
                                     image and colors.
                                                            • image—Array of bytes that describes the color of each pixel in
                                          the image in raster order. The value of image depth
                                         determines how LabVIEW interprets the value of this output.

                                                                      If image depth is 24, each pixel has three bytes to describe its
                                                  color. The first byte for each pixel describes the red value, the
                                       second byte describes the green value, and the third byte
                                            describes the blue value.
         Color 16            Yes
                                                                      If image depth is 8, each pixel has one byte to describe its
                                                  color. The value of each bit corresponds to an element in
                                               colors, which stores 32-bit RGB values where the most-
                                                 significant byte is zero, followed in order by red, green, and
                                          blue values.

                                                                      If image depth is 4, the behavior is similar to when image
                                      depth is 8 except valid values in image include 0 through 15.

                                                                      If image depth is 1, any value of zero in image corresponds to
                                       element 0 in colors. All other values correspond to element 1
                                                 in colors.

                                     The size of the array might be larger than expected due to
                                          padding.
                                                            • mask—Array of bytes in which each bit describes mask
                                           information for a pixel. The first byte describes the first eight
                                                   pixels, the second byte describes the next eight pixels, and so
                                           on. If a bit is zero, LabVIEW draws the corresponding pixel as


9866   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9866 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9867 ordinal=9867 -->
## Property and Method Reference

Property and Method Reference


             DataName             Required  Description
             type

                                    transparent. If the array is empty, LabVIEW draws all pixels
                                 without transparency. If the array does not contain a bit for
                               each pixel in the image, LabVIEW draws any pixels missing
                               from the array without transparency.
                                               • colors—Array of RGB color values that correspond to the
                                   values in image. The value of image depth determines how
                              LabVIEW interprets the value of this output. If image depth is
                                24, LabVIEW ignores this output. If image depth is 8, the array
                                has 256 elements. If image depth is 4, the array has 16
                                  elements. If image depth is 1, the array has 2 elements.
                                               • Rectangle—Cluster that contains coordinates that describe
                                  the bounding rectangle of the image, where the upper-left
                                  corner is at (0,0). The bottom right edges of the bounds does
                                 not include the image.

                             Returns information about the 1-bit VI icon. The Icon Editor dialog
                           box saves icons in both 256-color (8-bit) and monochrome (1-bit)
                               format.

                                               • image type—Reserved for future use.
                                               • image depth—Specifies the color depth of the image, which is
                                  the number of bits to use to describe the color of each pixel in
                                  the image. Valid values include 1, 4, 8, and 24 bits per pixel.
                             image depth affects how LabVIEW interprets the values of
                             image and colors.
                                               • image—Array of bytes that describes the color of each pixel in
                                  the image in raster order. The value of image depthMonochrome        Yes
                                determines how LabVIEW interprets the value of this output.

                                                        If image depth is 24, each pixel has three bytes to describe its
                                        color. The first byte for each pixel describes the red value, the
                               second byte describes the green value, and the third byte
                                   describes the blue value.

                                                        If image depth is 8, each pixel has one byte to describe its
                                        color. The value of each bit corresponds to an element in
                                      colors, which stores 32-bit RGB values where the most-
                                       significant byte is zero, followed in order by red, green, and


                                                    © National Instruments 9867

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9867 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9868 ordinal=9868 -->
## Property and Method Reference

Property and Method Reference


                     Data      Name             Required  Description
                     type

                                          blue values.

                                                                      If image depth is 4, the behavior is similar to when image
                                      depth is 8 except valid values in image include 0 through 15.

                                                                      If image depth is 1, any value of zero in image corresponds to
                                       element 0 in colors. All other values correspond to element 1
                                                 in colors.

                                     The size of the array might be larger than expected due to
                                          padding.
                                                            • mask—Array of bytes in which each bit describes mask
                                           information for a pixel. The first byte describes the first eight
                                                   pixels, the second byte describes the next eight pixels, and so
                                           on. If a bit is zero, LabVIEW draws the corresponding pixel as
                                             transparent. If the array is empty, LabVIEW draws all pixels
                                         without transparency. If the array does not contain a bit for
                                       each pixel in the image, LabVIEW draws any pixels missing
                                       from the array without transparency.
                                                            • colors—Array of RGB color values that correspond to the
                                            values in image. The value of image depth determines how
                                     LabVIEW interprets the value of this output. If image depth is
                                        24, LabVIEW ignores this output. If image depth is 8, the array
                                        has 256 elements. If image depth is 4, the array has 16
                                          elements. If image depth is 1, the array has 2 elements.
                                                            • Rectangle—Cluster that contains coordinates that describe
                                          the bounding rectangle of the image, where the upper-left
                                           corner is at (0,0). The bottom right edges of the bounds does
                                         not include the image.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes


9868   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9868 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9869 ordinal=9869 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

VIVI Icon:SaveIcon:Save ToTo FileFile

Saves an image of the VI icon to a file.

You also can use the VI Icon:Get As Image Data method to return the VI icon as a cluster
of image data.

Parameters

        Data
 Name        Required  Description
        type

 Image
               Yes       Absolute path where you want to save the image.
 File


                      Format in which to save the image.

 Image
           No        0       PNG (default) Format
                        1        JPEG


                                                    © National Instruments 9869

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9869 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9870 ordinal=9870 -->
## Property and Method Reference

Property and Method Reference


               Data      Name        Required  Description
                type


                               2         GIF

                               3       BMP


                                    Specifies the color depth of the image, which is the number of bits to use
        Image                 No        to describe the color of each pixel in the image. Valid values include 1, 4,        Depth
                         8 (default), and 24 bits per pixel.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes


9870   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9870 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9871 ordinal=9871 -->
## Property and Method Reference

Property and Method Reference

VIVI Icon:SetIcon:Set FromFrom FileFile

Sets the image of a VI icon from a file. LabVIEW creates a user layer called VI Icon for
the image and deletes any other existing icon information from the Icon Editor dialog
box.

You also can use the VI Icon:Set from Image Data method to set a VI icon from image
data you specify.

Parameters

       Data Name       Required  Description
        type

                        Absolute path to the image you want to use for the VI icon. Valid image Image
              Yes       formats include PNG, JPEG, GIF, and BMP. The BMP format is valid only on File                     Windows.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                                     Yes

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes


                                                    © National Instruments 9871

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9871 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9872 ordinal=9872 -->
## Property and Method Reference

Property and Method Reference


         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

    VIVI Icon:SetIcon:Set FromFrom ImageImage DataData

       Sets a VI icon from image data you specify. LabVIEW creates a user layer called VI Icon
        for the image and deletes any other existing icon information from the Icon Editor
       dialog box.

           If you want to use a pixmap to set the icon, use the Flatten Pixmap VI to convert the
       data to an image data cluster before using this method. If you want to use a picture to
       set the icon, use the Picture to Pixmap VI to convert the data to an image data cluster
       before using this method. Use the Create Mask VI to make a certain color in the image
       data transparent before wiring the image data to this method.

       This method converts the image data you wire to an input to the appropriate color
       depth. For example, if you wire 4-bit image data to the Color256 input, this method
       converts the image data to a color depth of 8-bit.

           If you do not wire image data to the Color16 input, LabVIEW converts the image data
      you wire to the Color256 input to a color depth of 4-bit. If you do not wire image data
       to the Monochrome input, LabVIEW converts the image data you wire to the Color16
       input, if available, to a color depth of 1-bit. Otherwise, LabVIEW converts the image
       data you wire to the Color256 input to a color depth of 1-bit.

           If the image data you wire to this method describes an image larger or smaller than 32
      × 32 pixels, the method resizes the image to 32 × 32 pixels.

      You also can use the VI Icon:Set from File method to set a VI icon from an image file.


9872   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9872 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9873 ordinal=9873 -->
## Property and Method Reference

Property and Method Reference

Parameters

             Data Name             Required  Description
              type

                                 Specifies image data to use as the 8-bit VI icon. The Icon Editor
                                dialog box saves icons in both 256-color (8-bit) and monochrome
                                      (1-bit) format.

                                                 • image type—Reserved for future use.
                                                 • image depth—Specifies the color depth of the image, which is
                                  the number of bits to use to describe the color of each pixel in
                                  the image. Valid values include 1, 4, 8, and 24 bits per pixel.
                              image depth affects how LabVIEW interprets the values of
                              image and colors.
                                                 • image—Array of bytes that describes the color of each pixel in
                                  the image in raster order. The value of image depth
                                 determines how LabVIEW interprets the value of this input.

                                                         If image depth is 24, each pixel has three bytes to describe its
                                         color. The first byte for each pixel describes the red value, the
                                second byte describes the green value, and the third byte
                                    describes the blue value.

 Color 256           Yes                  If image depth is 8, each pixel has one byte to describe its
                                         color. The value of each bit corresponds to an element in
                                       colors, which stores 32-bit RGB values where the most-
                                        significant byte is zero, followed in order by red, green, and
                                  blue values.

                                                         If image depth is 4, the behavior is similar to when image
                               depth is 8 except valid values in image include 0 through 15.

                                                         If image depth is 1, any value of zero in image corresponds to
                                element 0 in colors. All other values correspond to element 1
                                        in colors.
                                                 • mask—Array of bytes in which each bit describes mask
                                   information for a pixel. The first byte describes the first eight
                                          pixels, the second byte describes the next eight pixels, and so
                                   on. If a bit is zero, LabVIEW draws the corresponding pixel as
                                     transparent. If the array is empty, LabVIEW draws all pixels
                                  without transparency. If the array does not contain a bit for
                                each pixel in the image, LabVIEW draws any pixels missing


                                                    © National Instruments 9873

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9873 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9874 ordinal=9874 -->
## Property and Method Reference

Property and Method Reference


                     Data      Name             Required  Description
                     type

                                       from the array without transparency.
                                                            • colors—Array of RGB color values that correspond to the
                                            values in image. The value of image depth determines how
                                     LabVIEW interprets the value of this input. If image depth is
                                        24, LabVIEW ignores this input. If image depth is 8, the array
                                        has 256 elements. If image depth is 4, the array has 16
                                          elements. If image depth is 1, the array has 2 elements.
                                                            • Rectangle—Cluster that contains coordinates that describe
                                          the bounding rectangle of the image, where the upper-left
                                           corner is at (0,0). The bottom right edges of the bounds does
                                         not include the image.

                                          Specifies image data to use as the 4-bit VI icon. The Icon Editor
                                        dialog box saves icons only in 256-color (8-bit) and monochrome
                                                (1-bit) format. If you use this input to specify 4-bit image data for
                                 an icon, you can retrieve this data only by using the Color16
                                     output of the VI Icon:Get As Image Data method.

                                                            • image type—Reserved for future use.
                                                            • image depth—Specifies the color depth of the image, which is
                                          the number of bits to use to describe the color of each pixel in
                                          the image. Valid values include 1, 4, 8, and 24 bits per pixel.
                                     image depth affects how LabVIEW interprets the values of
                                     image and colors.
                                                            • image—Array of bytes that describes the color of each pixel in
         Color 16         No           the image in raster order. The value of image depth
                                         determines how LabVIEW interprets the value of this input.

                                                                      If image depth is 24, each pixel has three bytes to describe its
                                                  color. The first byte for each pixel describes the red value, the
                                       second byte describes the green value, and the third byte
                                            describes the blue value.

                                                                      If image depth is 8, each pixel has one byte to describe its
                                                  color. The value of each bit corresponds to an element in
                                               colors, which stores 32-bit RGB values where the most-
                                                 significant byte is zero, followed in order by red, green, and
                                          blue values.


9874   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9874 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9875 ordinal=9875 -->
## Property and Method Reference

Property and Method Reference


             DataName             Required  Description
             type

                                                        If image depth is 4, the behavior is similar to when image
                              depth is 8 except valid values in image include 0 through 15.

                                                        If image depth is 1, any value of zero in image corresponds to
                               element 0 in colors. All other values correspond to element 1
                                       in colors.
                                               • mask—Array of bytes in which each bit describes mask
                                  information for a pixel. The first byte describes the first eight
                                         pixels, the second byte describes the next eight pixels, and so
                                   on. If a bit is zero, LabVIEW draws the corresponding pixel as
                                    transparent. If the array is empty, LabVIEW draws all pixels
                                 without transparency. If the array does not contain a bit for
                               each pixel in the image, LabVIEW draws any pixels missing
                               from the array without transparency.
                                               • colors—Array of RGB color values that correspond to the
                                   values in image. The value of image depth determines how
                              LabVIEW interprets the value of this input. If image depth is
                                24, LabVIEW ignores this input. If image depth is 8, the array
                                has 256 elements. If image depth is 4, the array has 16
                                  elements. If image depth is 1, the array has 2 elements.
                                               • Rectangle—Cluster that contains coordinates that describe
                                  the bounding rectangle of the image, where the upper-left
                                  corner is at (0,0). The bottom right edges of the bounds does
                                 not include the image.

                                 Specifies image data to use as the 1-bit icon. The Icon Editor
                               dialog box saves icons in both 256-color (8-bit) and monochrome
                                     (1-bit) format.

                                               • image type—Reserved for future use.
                                               • image depth—Specifies the color depth of the image, which is
                                  the number of bits to use to describe the color of each pixel in
Monochrome      No                                  the image. Valid values include 1, 4, 8, and 24 bits per pixel.
                             image depth affects how LabVIEW interprets the values of
                             image and colors.
                                               • image—Array of bytes that describes the color of each pixel in
                                  the image in raster order. The value of image depth
                                determines how LabVIEW interprets the value of this input.


                                                    © National Instruments 9875

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9875 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9876 ordinal=9876 -->
## Property and Method Reference

Property and Method Reference


                     Data      Name             Required  Description
                     type

                                                                      If image depth is 24, each pixel has three bytes to describe its
                                                  color. The first byte for each pixel describes the red value, the
                                       second byte describes the green value, and the third byte
                                            describes the blue value.

                                                                      If image depth is 8, each pixel has one byte to describe its
                                                  color. The value of each bit corresponds to an element in
                                               colors, which stores 32-bit RGB values where the most-
                                                 significant byte is zero, followed in order by red, green, and
                                          blue values.

                                                                      If image depth is 4, the behavior is similar to when image
                                      depth is 8 except valid values in image include 0 through 15.

                                                                      If image depth is 1, any value of zero in image corresponds to
                                       element 0 in colors. All other values correspond to element 1
                                                 in colors.
                                                            • mask—Array of bytes in which each bit describes mask
                                           information for a pixel. The first byte describes the first eight
                                                   pixels, the second byte describes the next eight pixels, and so
                                           on. If a bit is zero, LabVIEW draws the corresponding pixel as
                                             transparent. If the array is empty, LabVIEW draws all pixels
                                         without transparency. If the array does not contain a bit for
                                       each pixel in the image, LabVIEW draws any pixels missing
                                       from the array without transparency.
                                                            • colors—Array of RGB color values that correspond to the
                                            values in image. The value of image depth determines how
                                     LabVIEW interprets the value of this input. If image depth is
                                        24, LabVIEW ignores this input. If image depth is 8, the array
                                        has 256 elements. If image depth is 4, the array has 16
                                          elements. If image depth is 1, the array has 2 elements.
                                                            • Rectangle—Cluster that contains coordinates that describe
                                          the bounding rectangle of the image, where the upper-left
                                           corner is at (0,0). The bottom right edges of the bounds does
                                         not include the image.


9876   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9876 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9877 ordinal=9877 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                                     Yes

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

VIVI Strings:ExportStrings:Export

Exports the following strings about VI and front panel objects to a tagged text file: VI
name and description, object caption labels, object free labels, default data (string,
table, path, and array default data), private data (listbox item names, table row and
column headers, graph plot names, graph cursor names, graph annotation names, and
tab control page captions), and polymorphic VI data (instance names in the
polymorphic VI and selector shortcut menus).

This method is similar to the Advanced»Export Strings item on the Tools menu.


                                                    © National Instruments 9877

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9877 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9878 ordinal=9878 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                  Data      Name           Required  Description
                   type

                                  Path to the text file where LabVIEW writes the VI strings. If you specify         String File        Yes                               an existing file, LabVIEW appends the VI strings to the end of the file.


                                       Specifies whether to display the file dialog box to select the name of          Interactive      No                                    the strings file. The default value is FALSE.


                                  Path to the log file created to list errors that occur while exporting VI        Log File        No
                                         strings to a tagged text file. The default value is no logging.


         Create                       Specifies whether control captions should be automatically created.                    No
        Captions                 The default value is FALSE.


         Export                       Specifies whether to export block diagram strings. The default value                    No        Diagram                           is FALSE.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No


9878   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9878 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9879 ordinal=9879 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

VIVI Strings:ImportStrings:Import

Imports the following strings about VI and front panel objects from a tagged text file: VI
name and description, object caption labels, object free labels, default data (string,
table, path, and array default data), private data (listbox item names, table row and
column headers, graph plot names, graph cursor names, graph annotation names, and
tab control page captions), and polymorphic VI data (instance names in the
polymorphic VI and selector shortcut menus).

This method is similar to the Advanced»Import Strings item on the Tools menu.

Parameters

           Data Name           Required  Description           type

                           Path to the VI strings file, including the filename. If you do not enter a
 String File        Yes       filename, set Interactive to TRUE so the user can set the VI strings
                             filename.


                               Specifies whether to display the file dialog box to select the name of
 Interactive      No
                            the strings file. The default value is FALSE.


                           Path to the log file created to list errors that occur while exporting VI
 Log File        No
                                strings to a tagged text file. The default value is no logging.


                                                    © National Instruments 9879

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9879 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9880 ordinal=9880 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

        Must wait until user interface is idle                                  Yes

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

       VIVI PropertiesProperties

      You can set these properties for a VI in edit mode by selecting File»VI Properties and
       other menu items. If you do not wire a refnum to the reference input of the Property
      Node, LabVIEW gets or sets the property for the current VI.


        Property              Description

        Auto Logging:Log File  Path of the datalog file in which front panel data and a time stamp are
        Path                    written.

        Auto Logging:Log at    Indicates whether to write front panel values to a datalog file after the VI
         Finish                  runs.

        Auto Logging:Print at
                                 Indicates whether to print the front panel after the VI runs.
         Finish


9880   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9880 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9881 ordinal=9881 -->
## Property and Method Reference

Property and Method Reference


Property              Description

                     Get or set the Autopreallocate arrays and strings setting on VIs. This is
                    used by the FPGA module to optimize array and string operations by forcing
                   LabVIEW to preallocate memory at compile time rather than dynamicallyAuto Preallocate
                        allocating memory at run time.Arrays and Strings
                       This property is similar to the Autopreallocate arrays and strings checkbox
                  on the Execution Page of the VI Properties dialog box.

Automatic Error                                    If TRUE, enables automatic error handling for a VI.Handling

                      Returns a reference to the block diagram of the VI. This property is not
Block Diagram                        available in stand-alone applications.

Block Diagram                    Reads or writes the size of the alignment grid squares on the block diagramWindow:Alignment
                        of the VI.Grid Size

Block Diagram
                   Opens or closes the block diagram window.Window:Open

Block Diagram        Gets or sets the vertical and horizontal coordinates in the upper left-hand
Window:Origin        corner of the block diagram.

Block Diagram                      Current state of the block diagram window.Window:State

Block Diagram
Window:Window      Gets or sets the bounds for a block diagram window.
Bounds

Callers' Names        Returns a list of all the loaded VIs that call the referenced VI.

                      Returns the complexity of the referenced VI in relation to the Compiler
                      optimizations slider on the Environment page of the Options dialog box. By
Compiled:Code
                    comparing these two values, you can determine whether LabVIEW
Complexity
                          prioritizes editor responsiveness or execution speed when compiling this
                             VI.

                      Returns the level of compiler optimizations that LabVIEW last used to
Compiled:Last        compile this VI. The value corresponds to whether the complexity of the VI
Compiled With       was greater or less than the threshold at which LabVIEW begins limiting
                      compiler optimizations to prioritize editor responsiveness.

Connector            Returns the data type of the connector pane as variant data. Connector

                                                    © National Instruments 9881

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9881 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9882 ordinal=9882 -->
## Property and Method Reference

Property and Method Reference


        Property              Description

                            panes for VIs have a VI data type. Connector panes for polymorphic VIs have
        Pane:DataType       a PolyVI data type. Connector panes for custom controls, global variables,
                          and type definitions have the data type of the control.

        Connector                              Returns a reference to the connector pane of the VI.
        Pane:Reference

                               Sets the connector pane of the VI to match the connector pane of the VI        Connector Pane:Set                                reference input.

        Contains Compiled                               Sets or returns whether the VI includes compiled code.
       Code

                                 Specifies whether a control VI is a control, a typedef, or a strict typedef. This         Control VI Type                               property is valid for control VIs only.

                                                  If TRUE, the VI opens in edit mode. If FALSE, the VI opens in run mode, and         Edit Mode On Open                              the title bar, menu bar, and toolbar do not appear.

                            Reads or writes the execution highlighting setting of the VI. This property         Execution                            works on clone VIs, unlike the Highlight? property of the TopLevelDiagram         Highlighting?
                                  object, which always only works on the original reentrant VI.

                                                  If TRUE, you can use debugging tools on the VI. For example, you can set
                                breakpoints, create probes, enable execution highlighting, and single-step         Execution:Allow                             through execution. Set this property to FALSE to disable use of debugging
        Debugging                                    tools, reduce memory requirements, and to improve performance slightly
                                    for the VI.

         Execution:Close After                                 Indicates whether to close the front panel after the VI runs.          Call

         Execution:Inline Is                              Returns TRUE if you can inline this subVI into its calling VIs.
        Allowed

         Execution:Inline
                                 Specifies whether to inline the subVI into its calling VIs.
        SubVI

         Execution:Is
                                 Indicates whether a VI can be reentrant.
         Reentrant

         Execution:Preferred
                                 Indicates the execution system in which the VI runs.
        Exec System

         Execution:Priority      Indicates the priority of the VI when it runs in parallel with other tasks.

         Execution:Reentrancy
                                 Indicates the type of reentrancy LabVIEW uses for a reentrant VI.
        Type

9882   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9882 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9883 ordinal=9883 -->
## Property and Method Reference

Property and Method Reference


Property              Description

                    Reads or writes the Retain Wire Values setting of the VI. This property worksExecution:Retain Wire                  on clone VIs, unlike the Highlight? property of the TopLevelDiagram object,Values                    which always only works on the original reentrant VI.

Execution:Run When                        Indicates whether to run the VI when it opens.
Opened

Execution:Show Front                        Indicates whether to show the front panel when the VI is called.Panel On Call

Execution:Show Front                        Indicates whether to show the front panel when the VI is loaded.
Panel On Load

Execution:State        Indicates the execution state of the VI.

Execution:Suspend     Indicates whether LabVIEW suspends the execution of the VI when calling it
On Call               as a subVI. Use this property carefully with reentrant VIs.

Expand When                    Expands to show terminals when dropped as a subVI.
Dropped As SubVI

Front Panel           Reference to the front panel of a VI.

Front Panel                    Reads or writes the size of the alignment grid squares on the front panel ofWindow:Alignment
                      the VI.Grid Size

Front Panel            Indicates whether to display shortcut menus for front panel objects while
Window:Allow         the VI runs. If you do not display default run-time shortcut menus, you can
Runtime PopUp       continue to include customized shortcut menus.

Front Panel            Sets the behavior of the front panel window. Valid values include 0
Window:Behavior       (Invalid), 1 (Default), 2 (Floating), 3 (Floating/Auto-Hide), and 4 (Modal).

Front Panel            Indicates whether the close button in the title bar is disabled and the Close
Window:Closeable     item in the File menu is disabled.

Front Panel            Indicates whether the VI has a custom title string. Write FALSE to remove
Window:Custom Title  the custom title string.

Front Panel
                        Indicates whether to highlight Boolean controls that have a shortcut key of
Window:Highlight
                       <Enter>.
Return Button

                       Writing TRUE to this value brings the front panel to the front. This property
Front Panel            applies only in the application instance of the calling VI. Writing FALSE to
Window:Is Frontmost   this value has no effect. If you read this property, it indicates whether the
                        front panel window is the front window (ignoring floating windows).

                                                    © National Instruments 9883

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9883 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9884 ordinal=9884 -->
## Property and Method Reference

Property and Method Reference


        Property              Description

         Front Panel            Indicates whether the front panel window adjusts its size in proportion with
       Window:Keep        a change in monitor resolution. The window changes size so it covers the
       Window Proportions  same percentage of the screen that it covered at its original resolution.

         Front Panel            Indicates whether the user can minimize the front panel window while the
        Window:Minimizable   VI runs.

         Front Panel         Minimum size of the front panel window in pixels. If Front Panel
       Window:Minimum     Window:Resizable is TRUE, the user cannot resize the front panel smaller
         Size                 than the width and height you wire to this property.

                          The monitor on which the front panel window appears, if you have multiple         Front Panel                               monitors. (Windows) The value 0 is the primary monitor. (OS X) The value 1        Window:Monitor                                          is the primary monitor.

         Front Panel             Specifies whether or not the user can resize the front panel during
        Window:OldResizable  execution. This property can be set on non-editable VIs.

                          The four elements in the cluster are the top, left, bottom, and right values of
                              the interior portion of the front panel, not including the scroll bars, title bar,
                       menu bar, and toolbar. The cluster elements are in global screen
                                coordinates, which are the numbers that refer to coordinates within a         Front Panel
                           computer monitor's screen (rather than an open window).        Window:Panel
       Bounds                           You can set this property only for VIs with open front panels. If you do not
                          want the VI for which you want to set this property to appear to users, use
                              the Hidden state of the Front Panel Window:State property to hide the front
                              panel of the VI.

         Front Panel            Indicates whether the user can resize the front panel window while the VI
        Window:Resizable      runs.

         Front Panel
                               Sets the VI to run transparently. Set the level of transparency using the
       Window:Run VI
                               Front Panel Window:Transparency property.
         Transparently

         Front Panel
                                 Indicates whether to display the menu bar on the front panel while the VI
       Window:Show Menu
                                 runs.
        Bar

         Front Panel
                               Current state of the front panel window.
        Window:State

         Front Panel             String that appears in the title bar. This string does not have to match the VI


9884   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9884 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9885 ordinal=9885 -->
## Property and Method Reference

Property and Method Reference


Property              Description

Window:Title          filename.

Front Panel
Window:Title Bar       Indicates whether to display a title bar on the front panel while the VI runs.
Visible

                       Sets the window transparency level of the VI. The level of transparency is a
                     percentage where 0 is opaque and 100 is invisible. This property returns an
                        error if you specify a value outside the range of 0 to 100. If you set theFront Panel                      transparency level to 100, the VI becomes invisible and uncontrollable fromWindow:Transparency
                      the front panel. You must stop the VI on the block diagram for the front
                     panel of the VI to become visible. If you set FPRunTransparently to False,
                     changing this property has no effect.

                   The four elements in the cluster are the top, left, bottom, and right values of
                      the front panel window, which includes the interior region, scroll bars, title
                         bar, menu bar, and toolbar. They are in global screen coordinates, that is,
                      the numbers refer to coordinates within a computer monitor's screenFront Panel
                         (rather than an open window).Window:Window
Bounds                    You can set this property only for VIs with open front panels. If you do not
                   want the VI for which you want to set this property to appear to users, use
                      the Hidden state of the Front Panel Window:State Property to hide the front
                     panel of the VI.

                     Path or symbolic path to an HTML file (.htm or .html) or compiled help
Help:Document Path
                               file (.chm or .hlp) to which the VI is linked.

                      Index keyword or HTML filename for a topic in the compiled help file toHelp:Document Tag
                    which the VI is linked.

Help:Document Web  URL for the web-based help topic to link to a VI from the Detailed help link
URL                     in the Context Help window.

                        Indicates whether to link to a web-based help file from the Detailed help
Help:Use Web URL
                          link in the Context Help window for a VI.

History:Always Add     Indicates whether to add a comment to the VI revision history every time
Comments At Save     the VI is saved.

History:Entire Text     Returns all the text that was added to the VI revision history.

History:Prompt for     Indicates whether to prompt for a VI revision history comment when the VI
Comments At Close     closes.


                                                    © National Instruments 9885

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9885 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9886 ordinal=9886 -->
## Property and Method Reference

Property and Method Reference


        Property              Description

         History:Prompt for     Indicates whether to prompt for a VI revision history comment when the VI
       Comments At Save      is saved.

         History:Record         Indicates whether to add comments to the VI revision history when certain
         Application           events occur, such as conversion to a new version of LabVIEW, subVI
       Comments            changes, and changes to the name or path of the VI.

         History:Revision                               Current revision number of the VI.       Number

                                 Indicates whether to use the global default history or to use the values         History:Use Defaults
                              entered in other history properties.

           Is Clone VI            Returns TRUE if the VI is a clone of a reentrant VI.

           Is In Packed Library    Returns TRUE if a packed project library contains the VI.

           Is Instance            Returns whether or not the VI is an Express VI instance.

           Is Probe              Returns TRUE if the VI is running as a probe and the probe VI is open.

           Is Running                              Returns TRUE if the VI is running interactively on the target device.          Interactively

                                 Specifies whether the execution of the VI is paused. A TRUE value indicates
           Is VI Paused?           that the VI is paused. A FALSE value indicates that the VI is not paused or
                                that it is not running.

                              Returns the name of the LabVIEW project library, XControl, or LabVIEW
         Library                 class that owns the VI. If no library, XControl, or class owns the VI, the
                               property returns Not a Refnum.

         Library:Version        Returns the version of the library that contains the VI you specify.

         Metrics:Block          Specifies whether the block diagram of the VI is in memory. The block
        Diagram Loaded      diagram can be in memory even if the window is not open.

         Metrics:Code Size     Amount of memory used for VI code in bytes.

         Metrics:Front Panel     Specifies whether the front panel of the VI is in memory. The front panel
        Loaded              can be in memory even if the window is not open.

         Metrics:Size of Block
                                 Size of the block diagram in bytes.
        Diagram

         Metrics:Size of Front
                                 Size of the front panel in bytes.
        Panel

          Metrics:Total Data    Amount of memory allocated for data in bytes.


9886   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9886 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9887 ordinal=9887 -->
## Property and Method Reference

Property and Method Reference


Property              Description

Size

                        Indicates whether changes were made to the block diagram since the VIModifications:Block                  was saved or opened, depending on which was last. If the value is zero, noDiagram Mods Bitset                    changes were made. If the value is nonzero, changes were made.

                        Indicates whether changes were made to the front panel since the VI wasModifications:Front                      saved. If the value is zero, no changes where made. If the value is nonzero,Panel Mods Bitset                    changes were made.

Modifications:VI        Indicates if changes were made to the VI since the VI was saved. If the value
Modifications Bitset     is zero, no changes were made. If the value is nonzero, changes were made.

                      Returns a reference to the application that owns the VI. Be sure and closeOwning Application                          this reference afterward.

Printing:Block                                    If TRUE, LabVIEW scales the block diagram to fit on the printed page.Diagram Scaling?

Printing:Front Panel                                    If TRUE, LabVIEW scales the front panel to fit on the printed page.Scaling?

                                    If TRUE, LabVIEW includes the date printed in the headers for the VI. UsePrinting:Header                      the Printing:Page Headers? property to set whether LabVIEW prints the
Content:Date Printed?                     headers for the VI.

                                    If TRUE, LabVIEW includes the last modified date in the headers for the VI.
Printing:Header                   Use the Printing:Page Headers? property to set whether LabVIEW prints theContent:Modify Date?                     headers for the VI.

Printing:Header            If TRUE, LabVIEW includes the page number in the headers for the VI. Use
Content:Page         the Printing:Page Headers? property to set whether LabVIEW prints the
Number?             headers for the VI.

                                    If TRUE, LabVIEW includes the VI icon in the headers for the VI. Use the
Printing:Header
                       Printing:Page Headers? property to set whether LabVIEW prints the headers
Content:VI Icon?
                          for the VI.

                                    If TRUE, LabVIEW includes the VI name in the headers for the VI. Use the
Printing:Header
                       Printing:Page Headers? property to set whether LabVIEW prints the headers
Content:VI Name?
                          for the VI.

                                    If TRUE, LabVIEW includes the VI path in the headers for the VI. Use the
Printing:Header
                       Printing:Page Headers? property to set whether LabVIEW prints the headers
Content:VI Path?
                          for the VI.

Printing:Margins       Gets or sets the page margins to use when printing the VI in inches or


                                                    © National Instruments 9887

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9887 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9888 ordinal=9888 -->
## Property and Method Reference

Property and Method Reference


        Property              Description

                                centimeters.

         Printing:Page                If TRUE, LabVIEW prints headers for the VI. Use the Printing:Header Content
        Headers?              properties in this class to customize the contents of the headers.

         Printing:Page                              Gets or sets the page orientation to use when printing the VI.
         Orientation

                       When read, this property returns the run-time menu path of the VI. When
                                  written, this property updates the run-time menu path of the VI. If the VI is        Run-Time Menu Path                              running when you write this property, it updates the menu with data from
                              the new path.

                              Returns an array of terminal bounds for the connector pane of the
        Terminal Bounds[]     referenced VI. The bounds for each terminal are represented as a cluster of
                                 integers that indicate the position of each edge of the terminal rectangle.

         Tool Bar:Show Abort   Indicates whether to display the Abort Execution button on the toolbar
        Button                while the VI runs.

         Tool Bar:Show Free     Indicates whether to display the Run Continuously button on the toolbar
       Run Button            while the VI runs.

         Tool Bar:Show Run     Indicates whether to display the Run button on the toolbar while the VI
        Button                 runs.

         Tool Bar:Visible        Indicates whether to display the toolbar while the VI runs.

          VI Clone Name      Name of the clone of a reentrant VI. Returns an error if the VI is not a clone.

                                Description of the VI that appears in the Context Help window when you
          VI Description                        move the cursor over the VI icon and in VI documentation you generate.

                      Name of the VI file. If a LabVIEW project library owns the VI, the property
          VI Name               returns the qualified name of the VI, which includes the project library
                                filename.

          VI Path               Path to the VI file.

          VI Type                 Indicates the type of VI.

   AutoAuto Logging:LogLogging:Log FileFile PathPath

      Path of the datalog file in which front panel data and a time stamp are written.


9888   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9888 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9889 ordinal=9889 -->
## Property and Method Reference

Property and Method Reference

      Note Use this property in conjunction with the Log at Finish property, which
        specifies whether to log the data. If you set the Log at Finish property without
        also setting this property, a dialog box appears at run time, prompting you to
        specify a file path.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

AutoAuto Logging:LogLogging:Log atat FinishFinish

Indicates whether to write front panel values to a datalog file after the VI runs.

This method is similar to the Log at Completion item on the Operate menu.


                                                    © National Instruments 9889

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9889 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9890 ordinal=9890 -->
## Property and Method Reference

Property and Method Reference

           Note If you set Log at Finish without having set the Log File Path property,
              the next time this VI finishes executing, a dialog box appears prompting you
               to specify the file path.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

   AutoAuto Logging:PrintLogging:Print atat FinishFinish

       Indicates whether to print the front panel after the VI runs.

       This method is similar to the Automatically print front panel every time VI completes
       execution option on the Print Options page of the VI Properties dialog box and the
       Print at Completion item in the Operate Menu.


9890   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9890 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9891 ordinal=9891 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

AutoAuto PreallocatePreallocate ArraysArrays andand StringsStrings

Get or set the Autopreallocate arrays and strings setting on VIs. This is used by the
FPGA module to optimize array and string operations by forcing LabVIEW to
preallocate memory at compile time rather than dynamically allocating memory at run
time.

This property is similar to the Autopreallocate arrays and strings checkbox on the
Execution Page of the VI Properties dialog box.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 9891

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9891 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9892 ordinal=9892 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                      No

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

   AutomaticAutomatic ErrorError HandlingHandling

           If TRUE, enables automatic error handling for a VI.

      By default, LabVIEW automatically handles any error that occurs when a VI runs by
      suspending execution, highlighting the subVI or function where the error occurred,
      and displaying an error dialog box.

       This property is similar to the Enable automatic error handling in new VIs option on
       the Block Diagram page of the Options dialog box and the Enable automatic error
      handling option on the Execution page of the VI Properties dialog box.

           Note The LabVIEW Run-Time Engine does not support automatic error
               handling.


9892   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9892 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9893 ordinal=9893 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

BlockBlock DiagramDiagram

Returns a reference to the block diagram of the VI. This property is not available in
stand-alone applications.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 9893

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9893 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9894 ordinal=9894 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                       No

        Must wait until user interface is idle                                        Yes

         Available with control VIs                                      No

         Available with global VIs                                      No

         Available with strict type definitions                              No

         Available with polymorphic VIs                                            Yes

   BlockBlock DiagramDiagram Window:AlignmentWindow:Alignment GridGrid SizeSize

      Reads or writes the size of the alignment grid squares on the block diagram of the VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                          Yes

        Loads the block diagram into memory                            No


9894   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9894 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9895 ordinal=9895 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

BlockBlock DiagramDiagram Window:OpenWindow:Open

Opens or closes the block diagram window.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                                    Yes

 Remote access allowed                                      No

 Must wait until user interface is idle                                       Yes

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No


                                                    © National Instruments 9895

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9895 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9896 ordinal=9896 -->
## Property and Method Reference

Property and Method Reference

   BlockBlock DiagramDiagram Window:OriginWindow:Origin

       Gets or sets the vertical and horizontal coordinates in the upper left-hand corner of the
       block diagram.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                      No

        Must wait until user interface is idle                                       Yes

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

   BlockBlock DiagramDiagram Window:StateWindow:State

       Current state of the block diagram window.

     Remarks

      The following table lists the characteristics of this property.

9896   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9896 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9897 ordinal=9897 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                            Yes

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

 Must wait until user interface is idle                               No

 Available with control VIs                                      No

 Available with global VIs                                      No

 Available with strict type definitions                              No

 Available with polymorphic VIs                                  No

BlockBlock DiagramDiagram Window:WindowWindow:Window BoundsBounds

Gets or sets the bounds for a block diagram window.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes


                                                    © National Instruments 9897

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9897 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9898 ordinal=9898 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                      No

        Must wait until user interface is idle                                       Yes

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

    Callers'Callers' NamesNames

       Returns a list of all the loaded VIs that call the referenced VI.

       This property is similar to the This VI's Callers item in the View Menu.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes


9898   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9898 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9899 ordinal=9899 -->
## Property and Method Reference

Property and Method Reference


 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

Compiled:CodeCompiled:Code ComplexityComplexity

Returns the complexity of the referenced VI in relation to the Compiler optimizations
slider on the Environment page of the Options dialog box. By comparing these two
values, you can determine whether LabVIEW prioritizes editor responsiveness or
execution speed when compiling this VI.

This property provides programmatic access to the Compiled Code Complexity field
on the Memory Usage page of the VI Properties dialog box.

      Note The value of this property is subject to change in future versions of
       LabVIEW.

Possible Errors

This property returns error 1000 if the referenced VI has never been compiled.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No


                                                    © National Instruments 9899

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9899 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9900 ordinal=9900 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

        Must wait until user interface is idle                               No

         Available with control VIs                                      No

         Available with global VIs                                      No

         Available with strict type definitions                              No

         Available with polymorphic VIs                                  No

   Compiled:LastCompiled:Last CompiledCompiled WithWith

       Returns the level of compiler optimizations that LabVIEW last used to compile this VI.
      The value corresponds to whether the complexity of the VI was greater or less than the
       threshold at which LabVIEW begins limiting compiler optimizations to prioritize editor
       responsiveness.

       This property provides programmatic access to the Last compiled with field on the
     Memory Usage page of the VI Properties dialog box. You can use this value to
      determine whether adjusting the complexity threshold can improve the execution
      speed of the referenced VI.

      Possible Errors

       This property returns error 1000 if the referenced VI has never been compiled.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes


9900   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9900 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9901 ordinal=9901 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

 Must wait until user interface is idle                               No

 Available with control VIs                                      No

 Available with global VIs                                      No

 Available with strict type definitions                              No

 Available with polymorphic VIs                                  No

ConnectorConnector Pane:DataTypePane:DataType

Returns the data type of the connector pane as variant data. Connector panes for VIs
have a VI data type. Connector panes for polymorphic VIs have a PolyVI data type.
Connector panes for custom controls, global variables, and type definitions have the
data type of the control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No


                                                    © National Instruments 9901

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9901 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9902 ordinal=9902 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                                 Yes

         Available with polymorphic VIs                                      Yes

   ConnectorConnector Pane:ReferencePane:Reference

       Returns a reference to the connector pane of the VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No


9902   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9902 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9903 ordinal=9903 -->
## Property and Method Reference

Property and Method Reference

ConnectorConnector Pane:SetPane:Set

Sets the connector pane of the VI to match the connector pane of the VI reference
input.

Use this property to dynamically configure a VI connector pane to match the connector
pane layout of an existing VI. The two VIs must have the same number of parameters
with identical data types and names. If they do not, the Property Node returns an
error. Use the Open VI Reference function to open references to both VIs and then wire
those references to the Property Node and the Connector Pane:Set property input.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                               Write Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                 No

 Loads the front panel into memory                                        Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                   Yes

 Must wait until user interface is idle                                        Yes

 Available with control VIs                                     No

 Available with global VIs                                      No

 Available with strict type definitions                              No

 Available with polymorphic VIs                                 No


                                                    © National Instruments 9903

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9903 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9904 ordinal=9904 -->
## Property and Method Reference

Property and Method Reference

   ContainsContains CompiledCompiled CodeCode

       Sets or returns whether the VI includes compiled code.

           If TRUE, the VI includes compiled code. If FALSE, LabVIEW separates the compiled code
      and saves it in the VI object cache.

       This property is similar to the Separate compiled code from source file option on the
       General page of the VI Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                  No

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes


9904   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9904 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9905 ordinal=9905 -->
## Property and Method Reference

Property and Method Reference

ControlControl VIVI TypeType

Specifies whether a control VI is a control, a typedef, or a strict typedef. This property is
valid for control VIs only.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

EditEdit ModeMode OnOn OpenOpen

If TRUE, the VI opens in edit mode. If FALSE, the VI opens in run mode, and the title bar,
menu bar, and toolbar do not appear.

To write this property, you must call it before you open the front panel of the VI.


                                                    © National Instruments 9905

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9905 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9906 ordinal=9906 -->
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

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

    ExecutionExecution Highlighting?Highlighting?

      Reads or writes the execution highlighting setting of the VI. This property works on
       clone VIs, unlike the Highlight? property of the TopLevelDiagram object, which always
       only works on the original reentrant VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

9906   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9906 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9907 ordinal=9907 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                          Yes

 Loads the block diagram into memory                                    Yes

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

Execution:AllowExecution:Allow DebuggingDebugging

If TRUE, you can use debugging tools on the VI. For example, you can set breakpoints,
create probes, enable execution highlighting, and single-step through execution. Set
this property to FALSE to disable use of debugging tools, reduce memory
requirements, and to improve performance slightly for the VI.

This property is similar to the Allow debugging option on the Execution page of the VI
Properties dialog box.

      Note Writing this property causes the VI to be recompiled. Writing TRUE
       causes extra code and data to be generated for the VI. This code and data
       enables LabVIEW to set breakpoints and single-step through the VI. Writing
       FALSE removes this code and data, reducing the total size of the VI.

When you debug applications and shared libraries, you cannot debug reentrant panels
that an Open VI Reference function creates. You also cannot debug reentrant panels
that are entry points to LabVIEW-built shared libraries.


                                                    © National Instruments 9907

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9907 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9908 ordinal=9908 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    Execution:CloseExecution:Close AfterAfter CallCall

       Indicates whether to close the front panel after the VI runs.

           Note Use this property in conjunction with the Show Front Panel On Call
               property.

     Remarks

      The following table lists the characteristics of this property.


9908   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9908 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9909 ordinal=9909 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

Execution:InlineExecution:Inline IsIs AllowedAllowed

Returns TRUE if you can inline this subVI into its calling VIs.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No


                                                    © National Instruments 9909

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9909 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9910 ordinal=9910 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

        Must wait until user interface is idle                               No

         Available with control VIs                                      No

         Available with global VIs                                      No

         Available with strict type definitions                              No

         Available with polymorphic VIs                                  No

    Execution:InlineExecution:Inline SubVISubVI

       Specifies whether to inline the subVI into its calling VIs.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No


9910   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9910 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9911 ordinal=9911 -->
## Property and Method Reference

Property and Method Reference


 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

Execution:IsExecution:Is ReentrantReentrant

Indicates whether a VI can be reentrant.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

Execution:PreferredExecution:Preferred ExecExec SystemSystem

Indicates the execution system in which the VI runs.


                                                    © National Instruments 9911

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9911 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9912 ordinal=9912 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    Execution:PriorityExecution:Priority

       Indicates the priority of the VI when it runs in parallel with other tasks.

       This property is similar to the Priority option on the Execution page of the VI
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type


9912   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9912 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9913 ordinal=9913 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

Execution:ReentrancyExecution:Reentrancy TypeType

Indicates the type of reentrancy LabVIEW uses for a reentrant VI.

This property is similar to options on the Execution Properties page of the VI Properties
dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No


                                                    © National Instruments 9913

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9913 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9914 ordinal=9914 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    Execution:RetainExecution:Retain WireWire ValuesValues

      Reads or writes the Retain Wire Values setting of the VI. This property works on clone
        VIs, unlike the Highlight? property of the TopLevelDiagram object, which always only
      works on the original reentrant VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                      No

        Must wait until user interface is idle                              No

9914   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9914 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9915 ordinal=9915 -->
## Property and Method Reference

Property and Method Reference


 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

Execution:RunExecution:Run WhenWhen OpenedOpened

Indicates whether to run the VI when it opens.

This property is similar to the Run when opened option on the Execution page of the
VI Properties dialog box.

      Note LabVIEW ignores this property when you load the VI using the VI
        Server. Use the Run VI method to run a VI you load using the VI Server.

      Note When a user launches a VI from a disk location other than standard NI
         installer locations, such as the LabVIEW 20XX or National
      Instruments\Shared folder, the user will be prompted to choose
       whether to run the VI or open it in edit mode.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No


                                                    © National Instruments 9915

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9915 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9916 ordinal=9916 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

   Execution:ShowExecution:Show FrontFront PanelPanel OnOn CallCall

       Indicates whether to show the front panel when the VI is called.

       This property is similar to the Show front panel when called option on the Customize
     Window Appearance dialog box and the Show front panel when called option on the
      SubVI Node Setup dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No


9916   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9916 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9917 ordinal=9917 -->
## Property and Method Reference

Property and Method Reference


 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

Execution:ShowExecution:Show FrontFront PanelPanel OnOn LoadLoad

Indicates whether to show the front panel when the VI is loaded.

This property is similar to the Show front panel when loaded option on the Customize
Window Appearance dialog box and the Open front panel when loaded option on the
SubVI Node Setup dialog box.

      Note LabVIEW ignores this property when you load the VI using the VI
        Server. Use the Front Panel:Open method to open the front panel of a VI you
       load using the VI Server.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

                                                    © National Instruments 9917

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9917 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9918 ordinal=9918 -->
## Property and Method Reference

Property and Method Reference


         Available with control VIs                                 No

         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    Execution:StateExecution:State

       Indicates the execution state of the VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes


9918   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9918 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9919 ordinal=9919 -->
## Property and Method Reference

Property and Method Reference

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Server\VI
   Properties\VI Properties - Front Panel States.vi
Execution:SuspendExecution:Suspend OnOn CallCall

Indicates whether LabVIEW suspends the execution of the VI when calling it as a subVI.
Use this property carefully with reentrant VIs.

This property is similar to the Suspend when called option on the Execution page of
the VI Properties dialog box, the Suspend when called option on the SubVI Node
Setup dialog box, and the Suspend when Called item on the Operate menu.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No


                                                    © National Instruments 9919

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9919 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9920 ordinal=9920 -->
## Property and Method Reference

Property and Method Reference


         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

   ExpandExpand WhenWhen DroppedDropped AsAs SubVISubVI

      Expands to show terminals when dropped as a subVI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

    FrontFront PanelPanel

       Reference to the front panel of a VI.


9920   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9920 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9921 ordinal=9921 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                                  Yes

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

FrontFront PanelPanel Window:AlignmentWindow:Alignment GridGrid SizeSize

Reads or writes the size of the alignment grid squares on the front panel of the VI.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No


                                                    © National Instruments 9921

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9921 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9922 ordinal=9922 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                          Yes

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

    FrontFront PanelPanel Window:AllowWindow:Allow RuntimeRuntime PopUpPopUp

       Indicates whether to display shortcut menus for front panel objects while the VI runs. If
      you do not display default run-time shortcut menus, you can continue to include
      customized shortcut menus.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

9922   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9922 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9923 ordinal=9923 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

FrontFront PanelPanel Window:BehaviorWindow:Behavior

Sets the behavior of the front panel window. Valid values include 0 (Invalid), 1
(Default), 2 (Floating), 3 (Floating/Auto-Hide), and 4 (Modal).

If you load the VI in a subpanel control, this property is read only.

This property is similar to the Window Behaviorsection in the Customize Window
Appearance dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                                       Yes


                                                    © National Instruments 9923

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9923 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9924 ordinal=9924 -->
## Property and Method Reference

Property and Method Reference


         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

    FrontFront PanelPanel Window:CloseableWindow:Closeable

       Indicates whether the close button in the title bar is disabled and the Close item in the
        File menu is disabled.

       This property prevents users from closing a VI during execution.

           If you load the VI in a subpanel control, this property is read only and always returns a
       value of FALSE.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No


9924   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9924 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9925 ordinal=9925 -->
## Property and Method Reference

Property and Method Reference


 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

FrontFront PanelPanel Window:CustomWindow:Custom TitleTitle

Indicates whether the VI has a custom title string. Write FALSE to remove the custom
title string.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                             No

 Available with polymorphic VIs                                           Yes

FrontFront PanelPanel Window:HighlightWindow:Highlight ReturnReturn ButtonButton

Indicates whether to highlight Boolean controls that have a shortcut key of <Enter>.

                                                    © National Instruments 9925

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9925 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9926 ordinal=9926 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

    FrontFront PanelPanel Window:IsWindow:Is FrontmostFrontmost

       Writing TRUE to this value brings the front panel to the front. This property applies
       only in the application instance of the calling VI. Writing FALSE to this value has no
        effect. If you read this property, it indicates whether the front panel window is the
       front window (ignoring floating windows).

     Remarks

      The following table lists the characteristics of this property.


        Data type


9926   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9926 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9927 ordinal=9927 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                                       Yes

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

FrontFront PanelPanel Window:KeepWindow:Keep WindowWindow
ProportionsProportions

Indicates whether the front panel window adjusts its size in proportion with a change
in monitor resolution. The window changes size so it covers the same percentage of
the screen that it covered at its original resolution.

This property is similar to the Maintain proportions of window for different monitor
resolutions option on the Window Size page of the VI Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 9927

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9927 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9928 ordinal=9928 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

    FrontFront PanelPanel Window:MinimizableWindow:Minimizable

       Indicates whether the user can minimize the front panel window while the VI runs.

           If you load the VI in a subpanel control, this property is read only and always returns a
       value of FALSE.

       This property is similar to the Allow user to minimize window checkbox in the
      Customize Window Appearance dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes


9928   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9928 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9929 ordinal=9929 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

FrontFront PanelPanel Window:MinimumWindow:Minimum SizeSize

Minimum size of the front panel window in pixels. If Front Panel Window:Resizable is
TRUE, the user cannot resize the front panel smaller than the width and height you
wire to this property.

You cannot size the window smaller than one pixel in either dimension. If you set a
pane to a size at which the scroll bars encroach on the content area's minimum size,
LabVIEW hides the scroll bars. When you size the pane larger, the scroll bars appear
again. For single-pane front panels, minimum size refers to the content area of that
pane, not including the scroll bars. For multi-pane front panels, minimum size refers to
the entire front panel, including any visible scroll bars.

This property is similar to the Minimum Panel Size section of the Window Size page of
the VI Properties dialog box.

Elements

 Name      Description

          The minimum width of the front panel window in pixels. This value cannot be less than
 Horizontal
              1.


                                                    © National Instruments 9929

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9929 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9930 ordinal=9930 -->
## Property and Method Reference

Property and Method Reference


      Name      Description

                 The minimum height of the front panel window in pixels. This value cannot be less than          Vertical                        1.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

    FrontFront PanelPanel Window:MonitorWindow:Monitor

      The monitor on which the front panel window appears, if you have multiple monitors.
      (Windows) The value 0 is the primary monitor. (OS X) The value 1 is the primary
       monitor.

       This property is similar to the Monitor option on the Window Run-Time Position page
       of the VI Properties dialog box.

9930   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9930 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9931 ordinal=9931 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                             No

 Available with polymorphic VIs                                           Yes

FrontFront PanelPanel Window:OldResizableWindow:OldResizable

Specifies whether or not the user can resize the front panel during execution. This
property can be set on non-editable VIs.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 9931

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9931 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9932 ordinal=9932 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

    FrontFront PanelPanel Window:PanelWindow:Panel BoundsBounds

      The four elements in the cluster are the top, left, bottom, and right values of the
        interior portion of the front panel, not including the scroll bars, title bar, menu bar, and
        toolbar. The cluster elements are in global screen coordinates, which are the numbers
       that refer to coordinates within a computer monitor's screen (rather than an open
      window).

      You can set this property only for VIs with open front panels. If you do not want the VI
        for which you want to set this property to appear to users, use the Hidden state of the
       Front Panel Window:State property to hide the front panel of the VI.

     When you read this property, LabVIEW returns the front panel bounds of the VI. If the
       front panel of the VI is not open, LabVIEW returns the front panel bounds of the VI in
       the position it was last saved. The front panel bounds adjust if you change the size or
      placement of objects in the front panel. Dynamic changes in data can occur if you alter
      bound front panel objects.

           If you load the VI in a subpanel control, this property is read only.


9932   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9932 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9933 ordinal=9933 -->
## Property and Method Reference

Property and Method Reference

Elements

 Name   Description

        The horizontal coordinate of the left edge of the interior portion of the front panel in Left          global screen coordinates.

        The vertical coordinate of the top edge of the interior portion of the front panel in global Top         screen coordinates.

        The horizontal coordinate of the right edge of the interior portion of the front panel in Right          global screen coordinates.

        The vertical coordinate of the bottom edge of the interior portion of the front panel in Bottom          global screen coordinates.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No


                                                    © National Instruments 9933

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9933 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9934 ordinal=9934 -->
## Property and Method Reference

Property and Method Reference

    FrontFront PanelPanel Window:ResizableWindow:Resizable

       Indicates whether the user can resize the front panel window while the VI runs.

           If you load the VI in a subpanel control, this property is read only and always returns a
       value of FALSE.

       This property is similar to the Allow user to resize window checkbox in the Customize
     Window Appearance dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No


9934   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9934 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9935 ordinal=9935 -->
## Property and Method Reference

Property and Method Reference

FrontFront PanelPanel Window:RunWindow:Run VIVI TransparentlyTransparently

Sets the VI to run transparently. Set the level of transparency using the Front Panel
Window:Transparency property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                           Yes

FrontFront PanelPanel Window:ShowWindow:Show MenuMenu BarBar

Indicates whether to display the menu bar on the front panel while the VI runs.

If you load the VI in a subpanel control, this property is read only and always returns a
value of FALSE.


                                                    © National Instruments 9935

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9935 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9936 ordinal=9936 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Show menu bar option on the Customize Window
      Appearance dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

    FrontFront PanelPanel Window:StateWindow:State

       Current state of the front panel window.

      A state of

      Standard
       or
      Maximized
       indicates that the front panel window is visible to the user.

9936   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9936 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9937 ordinal=9937 -->
## Property and Method Reference

Property and Method Reference

If you attempt to set this property for a front panel window that is not open, the
property returns an error.

If you load the VI in a subpanel control, this property is read only and always returns a
value of

Hidden
.

You also can use the Front Panel:Open method to set the state of the front panel
window when you display it.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                             No

 Available with polymorphic VIs                                           Yes


                                                    © National Instruments 9937

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9937 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9938 ordinal=9938 -->
## Property and Method Reference

Property and Method Reference

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\VI Server\VI
        Properties\VI Properties - Front Panel States.vi
    FrontFront PanelPanel Window:TitleWindow:Title

       String that appears in the title bar. This string does not have to match the VI filename.

       This property is similar to the Window title option on the Window Appearance page of
       the VI Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                             No

         Available with polymorphic VIs                                           Yes


9938   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9938 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9939 ordinal=9939 -->
## Property and Method Reference

Property and Method Reference

FrontFront PanelPanel Window:TitleWindow:Title BarBar VisibleVisible

Indicates whether to display a title bar on the front panel while the VI runs.

If you load the VI in a subpanel control, this property is read only and always returns a
value of FALSE.

This property is similar to the Window has title bar option on the Customize Window
Appearance dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No


                                                    © National Instruments 9939

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9939 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9940 ordinal=9940 -->
## Property and Method Reference

Property and Method Reference

    FrontFront PanelPanel Window:TransparencyWindow:Transparency

       Sets the window transparency level of the VI. The level of transparency is a percentage
      where 0 is opaque and 100 is invisible. This property returns an error if you specify a
       value outside the range of 0 to 100. If you set the transparency level to 100, the VI
      becomes invisible and uncontrollable from the front panel. You must stop the VI on the
       block diagram for the front panel of the VI to become visible. If you set
       FPRunTransparently to False, changing this property has no effect.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                           Yes

    FrontFront PanelPanel Window:WindowWindow:Window BoundsBounds

      The four elements in the cluster are the top, left, bottom, and right values of the front

9940   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9940 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9941 ordinal=9941 -->
## Property and Method Reference

Property and Method Reference

panel window, which includes the interior region, scroll bars, title bar, menu bar, and
toolbar. They are in global screen coordinates, that is, the numbers refer to
coordinates within a computer monitor's screen (rather than an open window).

You can set this property only for VIs with open front panels. If you do not want the VI
for which you want to set this property to appear to users, use the Hidden state of the
Front Panel Window:State Property to hide the front panel of the VI.

When you read this property, LabVIEW returns the window bounds of the VI. If the front
panel of the VI is not open, LabVIEW returns the window bounds of the VI in the
position it was last saved.

If you load the VI in a subpanel control, this property is read only.

Elements

 Name   Description

        The horizontal coordinate of the left edge of the front panel window in global screen Left          coordinates.

        The vertical coordinate of the top edge of the front panel window in global screen Top          coordinates.

        The horizontal coordinate of the right edge of the front panel window in global screen Right          coordinates.

        The vertical coordinate of the bottom edge of the front panel window in global screen Bottom          coordinates.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

                                                    © National Instruments 9941

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9941 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9942 ordinal=9942 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

   Help:DocumentHelp:Document PathPath

      Path or symbolic path to an HTML file (.htm or .html) or compiled help file (.chm or
      .hlp) to which the VI is linked.

           If the path is to a compiled help file, use the Document Tag property to determine the
        specific topic in that help file.

       This property is similar to the Help Path text box on the Documentation page of the VI
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No


9942   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9942 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9943 ordinal=9943 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                             No

 Available with polymorphic VIs                                           Yes

Help:DocumentHelp:Document TagTag

Index keyword or HTML filename for a topic in the compiled help file to which the VI is
linked.

Use this property only when Document Path is a path to a compiled help file (.chm or
.hlp).

For .chm files, this property can be an HTML filename or index keyword. To link to a
bookmark within an HTML file, add # followed by the name of the bookmark to the
end of the filename. For .hlp files, this property can be an index keyword.

This property is similar to the Help Tag text box on the Documentation page of the VI
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 9943

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9943 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9944 ordinal=9944 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                             No

         Available with polymorphic VIs                                           Yes

   Help:DocumentHelp:Document WebWeb URLURL

     URL for the web-based help topic to link to a VI from the Detailed help link in the
       Context Help window.

      Use the Help:Use Web URL property to indicate that you want to link a VI to a web-
      based help file from the Context Help window.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No


9944   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9944 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9945 ordinal=9945 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                             No

 Available with polymorphic VIs                                           Yes

Help:UseHelp:Use WebWeb URLURL

Indicates whether to link to a web-based help file from the Detailed help link in the
Context Help window for a VI.

Use the Help:Document Web URL property to specify the URL of the web-based help
file.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No


                                                    © National Instruments 9945

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9945 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9946 ordinal=9946 -->
## Property and Method Reference

Property and Method Reference


         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                             No

         Available with polymorphic VIs                                           Yes

    History:AlwaysHistory:Always AddAdd CommentsComments AtAt SaveSave

       Indicates whether to add a comment to the VI revision history every time the VI is
       saved.

       This property is similar to the options available in the History window.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                             No

         Available with polymorphic VIs                                           Yes


9946   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9946 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9947 ordinal=9947 -->
## Property and Method Reference

Property and Method Reference

History:EntireHistory:Entire TextText

Returns all the text that was added to the VI revision history.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

 Must wait until user interface is idle                               No

 Available with control VIs                                                  Yes

 Available with global VIs                                                   Yes

 Available with strict type definitions                              No

 Available with polymorphic VIs                                            Yes

History:PromptHistory:Prompt forfor CommentsComments AtAt CloseClose

Indicates whether to prompt for a VI revision history comment when the VI closes.

This property is similar to the options available in the History window.


                                                    © National Instruments 9947

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9947 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9948 ordinal=9948 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                             No

         Available with polymorphic VIs                                           Yes

   History:PromptHistory:Prompt forfor CommentsComments AtAt SaveSave

       Indicates whether to prompt for a VI revision history comment when the VI is saved.

       This property is similar to the options available in the History window.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

9948   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9948 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9949 ordinal=9949 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                             No

 Available with polymorphic VIs                                           Yes

History:RecordHistory:Record ApplicationApplication CommentsComments

Indicates whether to add comments to the VI revision history when certain events
occur, such as conversion to a new version of LabVIEW, subVI changes, and changes to
the name or path of the VI.

This property is similar to the Record comments generated by LabVIEW option on the
Revision History page of the VI Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

                                                    © National Instruments 9949

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9949 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9950 ordinal=9950 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                             No

         Available with polymorphic VIs                                           Yes

    History:RevisionHistory:Revision NumberNumber

       Current revision number of the VI.

     When writing this property, you can write only a value greater than the current revision
      number. If you attempt to write a revision number whose value is less than the current
       revision number, the property returns an error. Use the Clear History method to reset
       the revision history and the revision number.

       This property is similar to the Next Revision option in the History window.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes


9950   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9950 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9951 ordinal=9951 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                             No

 Available with polymorphic VIs                                           Yes

History:UseHistory:Use DefaultsDefaults

Indicates whether to use the global default history or to use the values entered in other
history properties.

This property is similar to the Use the default history settings from the Options dialog
box option in the Revision History page of the VI Properties dialog box. You can specify
the global default history in the VI Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

                                                    © National Instruments 9951

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9951 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9952 ordinal=9952 -->
## Property and Method Reference

Property and Method Reference


        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                             No

         Available with polymorphic VIs                                           Yes

     IsIs CloneClone VIVI

       Returns TRUE if the VI is a clone of a reentrant VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

        Must wait until user interface is idle                               No

         Available with control VIs                                      No

         Available with global VIs                                      No

         Available with strict type definitions                              No

         Available with polymorphic VIs                                  No


9952   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9952 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9953 ordinal=9953 -->
## Property and Method Reference

Property and Method Reference

IsIs InIn PackedPacked LibraryLibrary

Returns TRUE if a packed project library contains the VI.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

 Must wait until user interface is idle                               No

 Available with control VIs                                                  Yes

 Available with global VIs                                                   Yes

 Available with strict type definitions                              No

 Available with polymorphic VIs                                            Yes

IsIs InstanceInstance

Returns whether or not the VI is an Express VI instance.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9953

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9953 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9954 ordinal=9954 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                                 Yes

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

     IsIs ProbeProbe

       Returns TRUE if the VI is running as a probe and the probe VI is open.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No


9954   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9954 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9955 ordinal=9955 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

 Must wait until user interface is idle                               No

 Available with control VIs                                      No

 Available with global VIs                                      No

 Available with strict type definitions                              No

 Available with polymorphic VIs                                  No

IsIs RunningRunning InteractivelyInteractively

Returns TRUE if the VI is running interactively on the target device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

 Must wait until user interface is idle                               No

 Available with control VIs                                      No

 Available with global VIs                                      No


                                                    © National Instruments 9955

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9955 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9956 ordinal=9956 -->
## Property and Method Reference

Property and Method Reference


         Available with strict type definitions                              No

         Available with polymorphic VIs                                  No

     IsIs VIVI Paused?Paused?

       Specifies whether the execution of the VI is paused. A TRUE value indicates that the VI
         is paused. A FALSE value indicates that the VI is not paused or that it is not running.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

        Must wait until user interface is idle                               No

         Available with control VIs                                      No

         Available with global VIs                                      No

         Available with strict type definitions                              No

         Available with polymorphic VIs                                  No

    LibraryLibrary

       Returns the name of the LabVIEW project library, XControl, or LabVIEW class that owns

9956   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9956 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9957 ordinal=9957 -->
## Property and Method Reference

Property and Method Reference

the VI. If no library, XControl, or class owns the VI, the property returns Not a
Refnum.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

 Must wait until user interface is idle                               No

 Available with control VIs                                                  Yes

 Available with global VIs                                                   Yes

 Available with strict type definitions                                        Yes

 Available with polymorphic VIs                                            Yes

Library:VersionLibrary:Version

Returns the version of the library that contains the VI you specify.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 9957

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9957 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9958 ordinal=9958 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

        Must wait until user interface is idle                               No

         Available with control VIs                                                  Yes

         Available with global VIs                                                   Yes

         Available with strict type definitions                              No

         Available with polymorphic VIs                                            Yes

    Metrics:BlockMetrics:Block DiagramDiagram LoadedLoaded

       Specifies whether the block diagram of the VI is in memory. The block diagram can be
        in memory even if the window is not open.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

9958   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9958 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9959 ordinal=9959 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

 Must wait until user interface is idle                               No

 Available with control VIs                                      No

 Available with global VIs                                      No

 Available with strict type definitions                              No

 Available with polymorphic VIs                                  No

Metrics:CodeMetrics:Code SizeSize

Amount of memory used for VI code in bytes.

This property is similar to the Code option on the Memory Usage page of the VI
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                 No


                                                    © National Instruments 9959

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9959 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9960 ordinal=9960 -->
## Property and Method Reference

Property and Method Reference


         Available with global VIs                                 No

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    Metrics:FrontMetrics:Front PanelPanel LoadedLoaded

       Specifies whether the front panel of the VI is in memory. The front panel can be in
     memory even if the window is not open.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

        Must wait until user interface is idle                               No

         Available with control VIs                                      No

         Available with global VIs                                      No

         Available with strict type definitions                              No

         Available with polymorphic VIs                                  No


9960   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9960 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9961 ordinal=9961 -->
## Property and Method Reference

Property and Method Reference

Metrics:SizeMetrics:Size ofof BlockBlock DiagramDiagram

Size of the block diagram in bytes.

This property is similar to the Block Diagram Objects option on the Memory Usage
page of the VI Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                               Yes

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                 No

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

Metrics:SizeMetrics:Size ofof FrontFront PanelPanel

Size of the front panel in bytes.

This property is similar to the Front Panel Objects option on the Memory Usage page

                                                    © National Instruments 9961

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9961 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9962 ordinal=9962 -->
## Property and Method Reference

Property and Method Reference

       of the VI Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                             No

    Metrics:TotalMetrics:Total DataData SizeSize

     Amount of memory allocated for data in bytes.

      You cannot read this property if the VI is running.

       This property is similar to the Data option on the Memory Usage page of the VI
       Properties dialog box.


9962   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9962 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9963 ordinal=9963 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                 No

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

Modifications:BlockModifications:Block DiagramDiagram ModsMods BitsetBitset

Indicates whether changes were made to the block diagram since the VI was saved or
opened, depending on which was last. If the value is zero, no changes were made. If
the value is nonzero, changes were made.

This property is similar to the options available on the Explain Changes dialog box.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9963

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9963 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9964 ordinal=9964 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

        Must wait until user interface is idle                               No

         Available with control VIs                                      No

         Available with global VIs                                      No

         Available with strict type definitions                              No

         Available with polymorphic VIs                                  No

    Modifications:FrontModifications:Front PanelPanel ModsMods BitsetBitset

       Indicates whether changes were made to the front panel since the VI was saved. If the
       value is zero, no changes where made. If the value is nonzero, changes were made.

       This property is similar to the options available on the Explain Changes dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes


9964   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9964 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9965 ordinal=9965 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                             No

Modifications:VIModifications:VI ModificationsModifications BitsetBitset

Indicates if changes were made to the VI since the VI was saved. If the value is zero, no
changes were made. If the value is nonzero, changes were made.

This property is similar to the options available on the Explain Changes dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No


                                                    © National Instruments 9965

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9965 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9966 ordinal=9966 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

   OwningOwning ApplicationApplication

       Returns a reference to the application that owns the VI. Be sure and close this
       reference afterward.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

9966   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9966 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9967 ordinal=9967 -->
## Property and Method Reference

Property and Method Reference

Printing:BlockPrinting:Block DiagramDiagram Scaling?Scaling?

If TRUE, LabVIEW scales the block diagram to fit on the printed page.

This property is similar to the Scale printed block diagram to fit page checkbox on the
Print Options page of the VI Properties dialog box and the Scale block diagram to fit
option on the Printer page of the Print dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                                      Yes

 Available with polymorphic VIs                                 No

Printing:FrontPrinting:Front PanelPanel Scaling?Scaling?

If TRUE, LabVIEW scales the front panel to fit on the printed page.


                                                    © National Instruments 9967

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9967 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9968 ordinal=9968 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Scale printed front panel to fit page checkbox on the
       Print Options page of the VI Properties dialog box and the Scale front panel to fit
       option on the Printer page of the Print dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                                      Yes

         Available with polymorphic VIs                                 No

    Printing:HeaderPrinting:Header Content:DateContent:Date Printed?Printed?

           If TRUE, LabVIEW includes the date printed in the headers for the VI. Use the
       Printing:Page Headers? property to set whether LabVIEW prints the headers for the VI.

     Remarks

      The following table lists the characteristics of this property.


9968   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9968 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9969 ordinal=9969 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                                      Yes

 Available with polymorphic VIs                                 No

Printing:HeaderPrinting:Header Content:ModifyContent:Modify Date?Date?

If TRUE, LabVIEW includes the last modified date in the headers for the VI. Use the
Printing:Page Headers? property to set whether LabVIEW prints the headers for the VI.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes


                                                    © National Instruments 9969

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9969 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9970 ordinal=9970 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                                      Yes

         Available with polymorphic VIs                                 No

    Printing:HeaderPrinting:Header Content:PageContent:Page Number?Number?

           If TRUE, LabVIEW includes the page number in the headers for the VI. Use the
       Printing:Page Headers? property to set whether LabVIEW prints the headers for the VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

9970   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9970 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9971 ordinal=9971 -->
## Property and Method Reference

Property and Method Reference


 Available with global VIs                                                 Yes

 Available with strict type definitions                                      Yes

 Available with polymorphic VIs                                 No

Printing:HeaderPrinting:Header Content:VIContent:VI Icon?Icon?

If TRUE, LabVIEW includes the VI icon in the headers for the VI. Use the Printing:Page
Headers? property to set whether LabVIEW prints the headers for the VI.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                                      Yes

 Available with polymorphic VIs                                 No


                                                    © National Instruments 9971

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9971 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9972 ordinal=9972 -->
## Property and Method Reference

Property and Method Reference

    Printing:HeaderPrinting:Header Content:VIContent:VI Name?Name?

           If TRUE, LabVIEW includes the VI name in the headers for the VI. Use the Printing:Page
      Headers? property to set whether LabVIEW prints the headers for the VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                                      Yes

         Available with polymorphic VIs                                 No

    Printing:HeaderPrinting:Header Content:VIContent:VI Path?Path?

           If TRUE, LabVIEW includes the VI path in the headers for the VI. Use the Printing:Page
      Headers? property to set whether LabVIEW prints the headers for the VI.


9972   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9972 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9973 ordinal=9973 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                                      Yes

 Available with polymorphic VIs                                 No

Printing:MarginsPrinting:Margins

Gets or sets the page margins to use when printing the VI in inches or centimeters.

This property is similar to the Use custom page margins checkbox on the Print
Options page of the VI Properties dialog box and the Custom margins option on the
Page Setup page of the Print dialog box.

Elements

 Name                 Description

 Top                The margin to use for the top of the page in inches or centimeters.


                                                    © National Instruments 9973

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9973 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9974 ordinal=9974 -->
## Property and Method Reference

Property and Method Reference


      Name                 Description

          Left                The margin to use for the left side of the page in inches or centimeters.

        Bottom             The margin to use for the bottom of the page in inches or centimeters.

         Right               The margin to use for the right side of the page in inches or centimeters.

        Measurement System  The units of measure to use for the Top, Left, Bottom, and Right values.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                                      Yes

         Available with polymorphic VIs                                 No

    Printing:PagePrinting:Page Headers?Headers?

           If TRUE, LabVIEW prints headers for the VI. Use the Printing:Header Content properties
        in this class to customize the contents of the headers.


9974   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9974 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9975 ordinal=9975 -->
## Property and Method Reference

Property and Method Reference

This property is similar to the Print header (name, date, page number) checkbox on
the Print Options page of the VI Properties dialog box and the Print header (name,
date, page number) checkbox on the Page Setup page of the Print dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                                Yes

 Available with global VIs                                                 Yes

 Available with strict type definitions                                      Yes

 Available with polymorphic VIs                                 No

Printing:PagePrinting:Page OrientationOrientation

Gets or sets the page orientation to use when printing the VI.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9975

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9975 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9976 ordinal=9976 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                                Yes

         Available with global VIs                                                 Yes

         Available with strict type definitions                                      Yes

         Available with polymorphic VIs                                 No

   Run-TimeRun-Time MenuMenu PathPath

     When read, this property returns the run-time menu path of the VI. When written, this
       property updates the run-time menu path of the VI. If the VI is running when you write
        this property, it updates the menu with data from the new path.

      Use this property to programmatically specify the path for a run-time menu (.rtm)
          file. This is useful if you are developing multilingual applications and you want to
       switch menus for each language programmatically.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

9976   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9976 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9977 ordinal=9977 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

TerminalTerminal Bounds[]Bounds[]

Returns an array of terminal bounds for the connector pane of the referenced VI. The
bounds for each terminal are represented as a cluster of integers that indicate the
position of each edge of the terminal rectangle.

This property provides a more efficient way to obtain the terminal bounds of a
connector pane than the similar Connector Pane:Terminal Bounds[] property. The
Connector Pane:Terminal Bounds[] property causes slower run-time performance
because it requires LabVIEW to load and maintain the front panel of the associated VI
in memory, even if you close the connector pane reference with the Close Reference
function. The VI:Terminal Bounds[] property does not load the front panel of the
associated VI into memory.

Use this property to avoid the negative run-time performance impact of the Connector
Pane:Terminal Bounds[] property, such as when you need to inspect the terminal
bounds of a connector pane from a custom plug-in for the Icon Editor.

The array elements are in terminal order as defined in the Connector Pane Pattern
Reference VI for each connector pane pattern.

                                                    © National Instruments 9977

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9977 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9978 ordinal=9978 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

        Must wait until user interface is idle                               No

         Available with control VIs                                      No

         Available with global VIs                                      No

         Available with strict type definitions                              No

         Available with polymorphic VIs                                  No

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\VI Scripting\
        Connector Pane\Connector Pane Pattern Reference.vi
   ToolTool Bar:ShowBar:Show AbortAbort ButtonButton

       Indicates whether to display the Abort Execution button on the toolbar while the VI
       runs.

       This property is similar to the Show Abort button option on the Customize Window

9978   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9978 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9979 ordinal=9979 -->
## Property and Method Reference

Property and Method Reference

Appearance dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

ToolTool Bar:ShowBar:Show FreeFree RunRun ButtonButton

Indicates whether to display the Run Continuously button on the toolbar while the VI
runs.

This property is similar to the Show Run Continuously button option on the
Customize Window Appearance dialog box.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 9979

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9979 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9980 ordinal=9980 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

   ToolTool Bar:ShowBar:Show RunRun ButtonButton

       Indicates whether to display the Run button on the toolbar while the VI runs.

       This property is similar to the Show Run button option on the Customize Window
      Appearance dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes


9980   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9980 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9981 ordinal=9981 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                 No

ToolTool Bar:VisibleBar:Visible

Indicates whether to display the toolbar while the VI runs.

This property is similar to the Show toolbar when running option on the Customize
Window Appearance dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 9981

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9981 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9982 ordinal=9982 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                                  Yes

        Must wait until user interface is idle                              No

         Available with control VIs                                     No

         Available with global VIs                                     No

         Available with strict type definitions                             No

         Available with polymorphic VIs                                 No

    VIVI CloneClone NameName

     Name of the clone of a reentrant VI. Returns an error if the VI is not a clone.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

        Must wait until user interface is idle                               No

         Available with control VIs                                      No

         Available with global VIs                                      No

         Available with strict type definitions                              No

         Available with polymorphic VIs                                  No


9982   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9982 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9983 ordinal=9983 -->
## Property and Method Reference

Property and Method Reference

VIVI DescriptionDescription

Description of the VI that appears in the Context Help window when you move the
cursor over the VI icon and in VI documentation you generate.

This property is similar to the VI Description text box on the Documentation page of
the VI Properties dialog box. You can format the text in the description to appear bold
in the Context Help window.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

VIVI NameName

Name of the VI file. If a LabVIEW project library owns the VI, the property returns the

                                                    © National Instruments 9983

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9983 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9984 ordinal=9984 -->
## Property and Method Reference

Property and Method Reference

       qualified name of the VI, which includes the project library filename.

           Note To obtain only the VI filename, use the VI Path property, which returns
              the path to the VI. Then use the Strip Path function.

      You can write this property only if the VI has not been saved to disk.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

    VIVI PathPath

      Path to the VI file.

       This property is similar to the Location option on the General page of the VI Properties

9984   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9984 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9985 ordinal=9985 -->
## Property and Method Reference

Property and Method Reference

dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

 Must wait until user interface is idle                          No

 Available with control VIs                                           Yes

 Available with global VIs                                            Yes

 Available with strict type definitions                         No

 Available with polymorphic VIs                                      Yes

VIVI TypeType

Indicates the type of VI.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

                                                    © National Instruments 9985

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9985 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9986 ordinal=9986 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

        Must wait until user interface is idle                          No

         Available with control VIs                                           Yes

         Available with global VIs                                            Yes

         Available with strict type definitions                         No

         Available with polymorphic VIs                                      Yes

       VIVI EventsEvents


        Event      Description

       BD
         Selection   Occurs when the user changes the selection on the block diagram.
       Change

        Key Down  Generated when the user performs keystrokes on the keyboard.

        Key Down? Generated when the user performs keystrokes on the keyboard.

        Key        Generated at regular intervals when the user presses and holds a key anywhere on the
        Repeat      front panel.

        Key        Generated at regular intervals when the user presses and holds a key anywhere on the
        Repeat?     front panel.

        Key Up     Generated when the user releases a key on the keyboard.

                   Generated when the user opens a menu using the mouse or keyboard shortcut, for
       Menu
                   example, <Alt-F> to open the File menu. Also generated when the user presses
         Activation?
                     shortcut keys to activate a menu item, for example, <Ctrl-C> to copy text.

       Menu      Generated when the user selects an application item from the LabVIEW menu, such as
         Selection   Help»Show Context Help. Use the Menu Selection (User) event to generate an event


9986   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9986 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9987 ordinal=9987 -->
## Property and Method Reference

Property and Method Reference


 Event      Description

 (App)     when the user selects a user-defined menu item.

 Menu      Generated when the user selects a user-defined item from the LabVIEW menu. Use the
 Selection  Menu Selection (App) event to generate an event when the user selects an application
 (User)     menu item.

 Menu            Generated when the user selects an application item from the LabVIEW menu, such as Selection?           Help»Show Context Help. (App)

 Mouse            Generated when the cursor enters the bounds of the front panel.
 Enter

 Mouse            Generated when the cursor leaves the bounds of the front panel. Leave

 Panel      Generated when the user tries to interactively close the front panel of a VI by selecting
 Close       the Close item in the File menu or by clicking the close glyph on the window border.

 Panel      Generated when the user tries to interactively close the front panel on a VI by selecting
 Close?      the Close item in the File menu or by clicking the close glyph on the window border.

            Generated when the user sizes the front panel by clicking and dragging the window Panel             frame, minimizes or maximizes the front panel, or restores the front panel to its
 Resize              original size from a maximized or minimized state.

BDBD SelectionSelection ChangeChange

Occurs when the user changes the selection on the block diagram.

Event Data Fields

 Name   Description

         Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
         0            LabVIEW UI


                                                    © National Instruments 9987

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9987 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9988 ordinal=9988 -->
## Property and Method Reference

Property and Method Reference


      Name   Description

        Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time    Value of the millisecond timer when the event occurred.


         VIRef    Reference to the VI on which this event occurred.

          SelList

   KeyKey DownDown

      Generated when the user performs keystrokes on the keyboard.

       This event detects all key presses that occur anywhere on the front panel, such as
       typing text in a string control. If you want to detect a key down event only on a specific
        control, use the Key Down event in the Control class.

           Note LabVIEW only generates events for the Cluster»All Elements source
           when the cluster has keyboard focus, not when an individual element inside
              the cluster has keyboard focus.

     Event Data Fields

      Name     Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                  0            LabVIEW UI


        Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


9988   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9988 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9989 ordinal=9989 -->
## Property and Method Reference

Property and Method Reference


Name     Description

Time      Value of the millisecond timer when the event occurred.


VIRef      Reference to the VI on which this event occurred.


            Integer value that corresponds to the key pressed on the keyboard and represents a
           character from the current code page that your system uses. You also can modify the
Char          data returned by this event data field. Search for code pages on the Microsoft Web
             site for a listing of the code page tables supported by Windows.

          Enumerated type indicating the virtual key code of the key pressed. Values include
            ASCII, Shift, NumLock, F1, and so on. You also can modify the data received from this
          event data field.
VKey
              Note VKey has separate values for the <Enter> key on the alphanumeric
                  keyboard and <Enter> key on the numeric keypad.


          Scan code unique for each key on the keyboard. The values are unique for each physicalScanCode
            key, and allow you to match Key Up and Key Down events.


            Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
          platform-dependent modifiers in the PlatMods event data field. For key events, this
          event returns a Boolean indicating if the event occurred on the numeric keypad. For
Mods     mouse events, this event returns a Boolean indicating if the event was a double-click.
           For both events, a Boolean is returned if the platform-independent menu key, such as
            <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
           For filter events, you can modify the data returned by this event data field.


            Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
          dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
PlatMods  down when the event was triggered. For filter events, you can modify the data returned
          by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is
           the platform-independent menu key on Windows, but you also can use it in platform-


                                                    © National Instruments 9989

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9989 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9990 ordinal=9990 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

                 dependent programming.


                A reference to the object that has keyboard focus. When the event is for a control, it
        FocusObj  might be a sub-component, like a scale, label, and so on, rather than the control itself.
                 You also can modify the data returned by this event data field.

   KeyKey Down?Down?

      Generated when the user performs keystrokes on the keyboard.

       This event detects all key presses that occur anywhere on the front panel, such as
       typing text in a string control. If you want to detect a key down event only on a specific
        control, use the Key Down? event in the Control class.

           Note LabVIEW only generates events for the Cluster»All Elements source
           when the cluster has keyboard focus, not when an individual element inside
              the cluster has keyboard focus.

     Event Data Fields

      Name     Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                  0            LabVIEW UI


        Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


9990   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9990 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9991 ordinal=9991 -->
## Property and Method Reference

Property and Method Reference


Name     Description

Time      Value of the millisecond timer when the event occurred.


VIRef      Reference to the VI on which this event occurred.


            Integer value that corresponds to the key pressed on the keyboard and represents a
           character from the current code page that your system uses. You also can modify the
Char          data returned by this event data field. Search for code pages on the Microsoft Web
             site for a listing of the code page tables supported by Windows.

          Enumerated type indicating the virtual key code of the key pressed. Values include
            ASCII, Shift, NumLock, F1, and so on. You also can modify the data received from this
          event data field.
VKey
              Note VKey has separate values for the <Enter> key on the alphanumeric
                  keyboard and <Enter> key on the numeric keypad.


          Scan code unique for each key on the keyboard. The values are unique for each physicalScanCode
            key, and allow you to match Key Up and Key Down events.


            Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
          platform-dependent modifiers in the PlatMods event data field. For key events, this
          event returns a Boolean indicating if the event occurred on the numeric keypad. For
Mods     mouse events, this event returns a Boolean indicating if the event was a double-click.
           For both events, a Boolean is returned if the platform-independent menu key, such as
            <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
           For filter events, you can modify the data returned by this event data field.


            Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
          dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
PlatMods  down when the event was triggered. For filter events, you can modify the data returned
          by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is
           the platform-independent menu key on Windows, but you also can use it in platform-


                                                    © National Instruments 9991

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9991 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9992 ordinal=9992 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

                 dependent programming.


                A reference to the object that has keyboard focus. When the event is for a control, it
        FocusObj  might be a sub-component, like a scale, label, and so on, rather than the control itself.
                 You also can modify the data returned by this event data field.

                   Allows you to prevent LabVIEW from processing the event, bypassing the behavior
         Discard?                   normally triggered by that event. The default is FALSE.

   KeyKey RepeatRepeat

      Generated at regular intervals when the user presses and holds a key anywhere on the
       front panel.

           Note LabVIEW only generates events for the Cluster»All Elements source
           when the cluster has keyboard focus, not when an individual element inside
              the cluster has keyboard focus.

     Event Data Fields

      Name     Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                  0            LabVIEW UI


        Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time      Value of the millisecond timer when the event occurred.


9992   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9992 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9993 ordinal=9993 -->
## Property and Method Reference

Property and Method Reference


Name     Description

VIRef      Reference to the VI on which this event occurred.


            Integer value that corresponds to the key pressed on the keyboard and represents a
           character from the current code page that your system uses. You also can modify the
Char          data returned by this event data field. Search for code pages on the Microsoft Web
             site for a listing of the code page tables supported by Windows.

          Enumerated type indicating the virtual key code of the key pressed. Values include
            ASCII, Shift, NumLock, F1, and so on. You also can modify the data received from this
          event data field.
VKey
              Note VKey has separate values for the <Enter> key on the alphanumeric
                  keyboard and <Enter> key on the numeric keypad.


          Scan code unique for each key on the keyboard. The values are unique for each physicalScanCode            key, and allow you to match Key Up and Key Down events.


            Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
          platform-dependent modifiers in the PlatMods event data field. For key events, this
          event returns a Boolean indicating if the event occurred on the numeric keypad. For
Mods     mouse events, this event returns a Boolean indicating if the event was a double-click.
           For both events, a Boolean is returned if the platform-independent menu key, such as
            <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
           For filter events, you can modify the data returned by this event data field.


            Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
          dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
        down when the event was triggered. For filter events, you can modify the data returned
PlatMods
          by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is
           the platform-independent menu key on Windows, but you also can use it in platform-
          dependent programming.


                                                    © National Instruments 9993

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9993 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9994 ordinal=9994 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

                A reference to the object that has keyboard focus. When the event is for a control, it
        FocusObj  might be a sub-component, like a scale, label, and so on, rather than the control itself.
                 You also can modify the data returned by this event data field.

   KeyKey Repeat?Repeat?

      Generated at regular intervals when the user presses and holds a key anywhere on the
       front panel.

           Note LabVIEW only generates events for the Cluster»All Elements source
           when the cluster has keyboard focus, not when an individual element inside
              the cluster has keyboard focus.

     Event Data Fields

      Name     Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                  0            LabVIEW UI


        Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time      Value of the millisecond timer when the event occurred.


         VIRef      Reference to the VI on which this event occurred.


9994   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9994 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9995 ordinal=9995 -->
## Property and Method Reference

Property and Method Reference


Name     Description

            Integer value that corresponds to the key pressed on the keyboard and represents a
           character from the current code page that your system uses. You also can modify the
Char          data returned by this event data field. Search for code pages on the Microsoft Web
             site for a listing of the code page tables supported by Windows.

          Enumerated type indicating the virtual key code of the key pressed. Values include
            ASCII, Shift, NumLock, F1, and so on. You also can modify the data received from this
          event data field.
VKey
              Note VKey has separate values for the <Enter> key on the alphanumeric
                  keyboard and <Enter> key on the numeric keypad.


          Scan code unique for each key on the keyboard. The values are unique for each physical
ScanCode            key, and allow you to match Key Up and Key Down events.


            Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
          platform-dependent modifiers in the PlatMods event data field. For key events, this
          event returns a Boolean indicating if the event occurred on the numeric keypad. For
Mods     mouse events, this event returns a Boolean indicating if the event was a double-click.
           For both events, a Boolean is returned if the platform-independent menu key, such as
            <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
           For filter events, you can modify the data returned by this event data field.


            Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
          dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
        down when the event was triggered. For filter events, you can modify the data returned
PlatMods
          by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is
           the platform-independent menu key on Windows, but you also can use it in platform-
          dependent programming.


         A reference to the object that has keyboard focus. When the event is for a control, it
FocusObj  might be a sub-component, like a scale, label, and so on, rather than the control itself.
          You also can modify the data returned by this event data field.


                                                    © National Instruments 9995

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9995 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9996 ordinal=9996 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

                   Allows you to prevent LabVIEW from processing the event, bypassing the behavior         Discard?                   normally triggered by that event. The default is FALSE.

   KeyKey UpUp

      Generated when the user releases a key on the keyboard.

           Note LabVIEW only generates events for the Cluster»All Elements source
           when the cluster has keyboard focus, not when an individual element inside
              the cluster has keyboard focus.

     Event Data Fields

      Name     Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                  0            LabVIEW UI


        Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time      Value of the millisecond timer when the event occurred.


         VIRef      Reference to the VI on which this event occurred.


                 Scan code unique for each key on the keyboard. The values are unique for each physical
       ScanCode
                     key, and allow you to match Key Up and Key Down events.


9996   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9996 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9997 ordinal=9997 -->
## Property and Method Reference

Property and Method Reference


 Name     Description

            Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
           platform-dependent modifiers in the PlatMods event data field. For key events, this
           event returns a Boolean indicating if the event occurred on the numeric keypad. For
 Mods     mouse events, this event returns a Boolean indicating if the event was a double-click.
           For both events, a Boolean is returned if the platform-independent menu key, such as
             <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
           For filter events, you can modify the data returned by this event data field.


            Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
          dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
         down when the event was triggered. For filter events, you can modify the data returned PlatMods          by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is
           the platform-independent menu key on Windows, but you also can use it in platform-
          dependent programming.


          A reference to the object that has keyboard focus. When the event is for a control, it
 FocusObj  might be a sub-component, like a scale, label, and so on, rather than the control itself.
          You also can modify the data returned by this event data field.

MenuMenu Activation?Activation?

Generated when the user opens a menu using the mouse or keyboard shortcut, for
example, <Alt-F> to open the File menu. Also generated when the user presses
shortcut keys to activate a menu item, for example, <Ctrl-C> to copy text.

You can generate this event using any menu shortcut key. However, the movement and
editing keys, such as Insert, Delete, Home, End, Page Up, Page Down, and the arrow
keys do not generate this event.

The shortcut key does not have to exist in the menu in order to generate this event.
That is, all <F> keys and any <Ctrl-n> key generates the event.

LabVIEW generates this event regardless of whether the menu item being selected with


                                                    © National Instruments 9997

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9997 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9998 ordinal=9998 -->
## Property and Method Reference

Property and Method Reference

       the shortcut key is disabled or enabled.

           Note This event does not return which menu on the menu bar the user
              opens.

     Event Data Fields

      Name    Description

                 Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                 0            LabVIEW UI


        Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time     Value of the millisecond timer when the event occurred.


         VIRef     Reference to the VI on which this event occurred.


       MenuRef Reference to the LabVIEW menu from which an item was selected.

                  Allows you to prevent LabVIEW from processing the event, bypassing the behavior
         Discard?
                  normally triggered by that event. The default is FALSE.

   MenuMenu SelectionSelection (App)(App)

      Generated when the user selects an application item from the LabVIEW menu, such as
      Help»Show Context Help. Use the Menu Selection (User) event to generate an event
     when the user selects a user-defined menu item.


9998   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9998 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9999 ordinal=9999 -->
## Property and Method Reference

Property and Method Reference

      Note If you have an event structure with a Menu Selection (App) event, items
       chosen from the File»Recent Projects submenu return the item tag
      APP_RECENT_PROJECTS and items chosen from the File»Recent Files
      submenu return the item tag APP_RECENT_FILES.

Event Data Fields

 Name    Description

          Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
          0            LabVIEW UI


 Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time     Value of the millisecond timer when the event occurred.


 VIRef     Reference to the VI on which this event occurred.


 MenuRef  Reference to the LabVIEW menu from which an item was selected.


 ItemTag  Name of the menu item the user selected, such as APP_SHOW_HELP.


          Path of the LabVIEW menu item the user selected, such as
 ItemPath        APP_HELP:SHOW_APP_HELP. Components are separated by colons.


                                                    © National Instruments 9999

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9999 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10000 ordinal=10000 -->
## Property and Method Reference

Property and Method Reference

   MenuMenu SelectionSelection (User)(User)

        Generated when the user selects a user-defined item from the LabVIEW menu. Use the
      Menu Selection (App) event to generate an event when the user selects an application
      menu item.

       Event Data Fields

       Name     Description

                   Source of the event. LabVIEW UI refers to any built-in user interface event.

          Source
                   0            LabVIEW UI


         Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


         Time      Value of the millisecond timer when the event occurred.


           VIRef      Reference to the VI on which this event occurred.


         MenuRef  Reference to the LabVIEW menu from which an item was selected.


          ItemTag  Name of the LabVIEW menu item the user selected, such as APP_MY_HELP.


          ItemPath  Path of the LabVIEW menu item the user selected, such as APP_HELP:MY_HELP.


10000   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10000 -->

