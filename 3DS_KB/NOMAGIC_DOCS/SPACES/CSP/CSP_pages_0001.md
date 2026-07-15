# NOMAGIC DOCUMENTATION SPACE: CATIA Software Producer

<!--NOMAGIC_SPACE key=CSP chunk=1 -->

<!--NOMAGIC_PAGE id=258048985 space=CSP version=3 -->
## PAGE 00001: CATIA Software Producer

- page_id: `258048985`
- space_key: `CSP`
- source_url: https://docs.nomagic.com/spaces/CSP/pages/258048985/CATIA+Software+Producer
- version_number: 3
- version_date: `2025-09-25T13:23:42.947+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

##### **[Latest documentation](https://help.3ds.com/HelpDS.aspx?P=19&V=2026&L=English&F=CatEspMagicUserMap/catesp-c-ov.htm&contextscope=all)**

The CATIA Software Producer allows you to generate and build code from a UML or SysML v1 model. You can generate code, for example, from the UML Class structure, UML State Machine, or SysML v1 Blocks.

#### Key concepts and capabilities

CATIA Software Producer offers the following generation capabilities:

- Generating C code from UML and SysML v1 models.
- Generating C++ code from UML and SysML v1 models.
- Generating Java code from UML classes.
- Generating target dependent middleware code for AUTOSAR classic and adaptive.
- Generating and compiling code for FMU.
- Generating and compiling code to produce an executable for Windows, Linux, or a custom target.
- Generating code from a model persisted as a file, or in TeamworkCloud, or the 3D EXPERIENCE Platform.
- Generating code with traceability information, establishing the relation from the model items to the code.
- Code revers from C++ to UML.

For more information about the Software Production Engineering application, see [Software Production Engineering](https://help.3ds.com/2024x/english/dsdoc/CatEspUserMap/catesp-c-ov.htm?contextscope=cloud&id=bb196d4c58f14192a3a2c4c1fbefb4c6).

#### Prerequisites

- The CATIA Software Producer Client plugin is installed in your modeling tool. Learn more about how to [CONFLUENCE_PAGE title='Downloading installation files' space='IL'] .

When you launch any operation for the first time in your project, a dialog will open to configure the local workspace path, which will host generated resources.

[IMAGE alt='' src='']

#### Configuring the code generator

##### The principle

The generated code is composed of multiple layers as shown on the schemas below.

When the user configures code generators, the generated files will contain the following part:

[IMAGE alt='' src='']

When the user configures application generators, the generated files will contain the following part:

[IMAGE alt='' src='']

To configure the code generator, you have to create a Code Generation Configuration Diagram.

[IMAGE alt='' src='']

[IMAGE alt='' src='']

###### Click the image to enlarge.

Code generation supported so far is C, C++, and Java. You can select them in the diagram palette.

[IMAGE alt='' src='']

A code generation configuration is composed of:

- Elements
- Local Path . A patch to your workspace.
- (optional)
- Store Execution Summary in Model: set to false by default. Set to true, if you want an execution object to be created in your project (under the configuration element), so that you can view the execution summary of your configuration in the Code Generation Result Table.

[IMAGE alt='' src='']

[IMAGE alt='' src='']

Application production supported so far is FMU, AUTOSAR, Linux, Windows, and Custom Target.

[IMAGE alt='' src='']

An application production is composed of:

- code generation configurations: their generated files are used to produce the application
- top level element: only for FMU Production and AUTOSAR Generation configurations
- local workspace path
- store execution summary in model: by default set to false ; if set to true, an execution object will be created in your project (under the configuration element), so that you can view the execution summary of your configuration in the Code Generation Result Table.
- generate code: by default set to true.
  - If set to true, the associated code generation configuration(s) will be launched and their results will be taken as inputs of the final operation.
  - If set to false, the inputs of the final operation are the current files stored under the folders referenced by the configurations.
- parameters specifics to the selected operation:
  - in the example below: platform, include_souce, C_standard, Cpp_standar, debug [ATTACHMENT filename='fmu_example.png']
- (optional)

##### Code generation on the platform or locally

The code generation can be launched on the platform or locally.

The local code generation is available for:

- Code Generation configurations (C Code Generation, Cpp Code Generation, Java Code Generation, and Component Tester)
- Component Tester configuration in generation mode (default mode)

If you want to generate the code on the platform, you need to specify parameters of the configuration.

To launch the code generation on the platform

1. In the Containment tree or on the diagram pane, right-click the needed configuration.
2. From the shortcut menu, select Specification.
3. In the Specification window, go to the Code Generation Configuration option group.
4. Set the Execute On Cloud option to true .
5. Click OK .

[IMAGE alt='' src='']

Before starting to work on code generation on the platform, first, you have to **connect to 3DEXPERIENCE** by entering the URL of the Software Producer cloud server. After that, you will be able to log in with your regular identifiers. You must have the Software Production Engineer Role. It will give you permission to use the service.

For information about how to authenticate with the **3D**EXPERIENCE platform, see [CONFLUENCE_PAGE title='Authentication with 3DEXPERIENCE platform' space='MT']Authentication with **3D**EXPERIENCE platform.

##### Specifying elements and configurations

You can specify “elements” or “topLevelElement” in two ways:

- Drag and drop the element from the Containment tree to the desired configuration in the diagram [ATTACHMENT filename='drag_drop_to_set_element.png']
- Open the Specification window of the configuration and edit the Element property.

You can specify “codeGenerationConfigurations” in two ways:

- On the diagram, drag and drop the Code Generation Configuration to the application Production configuration. [ATTACHMENT filename='configuration_drag_drop_production.png']
- Open the Specification window of the configuration and edit the Code Generation Configuration property.

#### Validating

You can check if your model is compatible with the code generation via the standard validation menu.

To run the validation

1. In the Containment tree, right-click the code configuration.
2. In the shortcut menu, select one of the following:
  1. Click **Validate,**and in the open **Validation**dialog, choose either all possible constraints or only **Code Generation Constraints**.
  2. Click **Validate Element** to run validation for a selected element only.

[IMAGE alt='' src='']

You can also use the Validate Diagram command, which you can find in the configuration diagram toolbar:

[IMAGE alt='' src='']

The results are displayed in the **Validation Results** window if there are any errors or warnings.

[IMAGE alt='' src='']

The operation logs are displayed in the usual Software Producer logs window.

If you do not want to run the validation for code generation when calling the validation menu, you can choose to ignore a selected validation suite and/or validation rule.

To ignore a validation suite or a validation rule

1. In the modeling tool's main menu, click Options > Project .
2. In the open Project Options dialog > Validation , specify the Ignored Validation Suites and/or Ignored Validation Rules .

Show Validation Report

false

Project Options

CATIA Software Producer Client

[IMAGE alt='' src='']

Validation is actually an SPO (Software Production Operation) launched in dry-run mode (no file generation, no credit consumption).

#### Executing Operations

To execute the code generator, you can run the generation from the following locations:

- Main menu
- Code generation diagram
- Containment tree

##### Execution from the main menu

[IMAGE alt='' src='']

You can do one of the following:

- launch the default action Execute Operation that will launch the operations
  - if Activate Smart Launch Mode is set to true in the environment options ( Environment options dialog > CATIA Software Producer Client General Properties ), operations will be launched only if a change was made in the model. By default, the property is set to false.

- launch the Clean & Execute Operation that will delete your previously generated local files and cloud assets, then launch all the operations.
  - for the deletion of the local files: if files previously generated by this configuration are found, a dialog will be prompted to the user to confirm the deletion of local files. If you do not want to see this message again, cancel the selection of the **Show this message next time** check box. If you want to see this message again, there is a dedicated Environment option to turn the message showing on (see ). [ATTACHMENT filename='delete_local_folders.png']
  - for the deletion of cloud assets: it will be done without asking for the confirmation of the user.

##### Execution from a code generation diagram

Do one of the following:

- On the diagram pane, right-click a configuration element, and from the shortcut menu, choose **Software Code Generation** > **Execute Operation**: 
[IMAGE alt='' src='']
- On the diagram pane, select a configuration element, and in the diagram toolbar, click **Execute Selected Configuration**: 
[IMAGE alt='' src='']

###### Execution from Containment tree

- In the Containment tree, right-click a configuration element, and from the shortcut menu, select **Software Code Generation** > **Execute Operation** > **Execute Operation**: 
[IMAGE alt='' src='']
- In the Containment tree, right-click an input element, and from the shortcut menu, select **Software Code Generation** > **Execute with...**: 
[IMAGE alt='' src='']

The operation logs are displayed in the**Software Producer Logs** window.

##### Limitation

Currently, when a code generation is launched after renaming a class, the newly generated files reflect the new class names. However, the old files (corresponding to the previous class names) are not automatically deleted. This can lead to "outdated" files remaining in the output directory.

This limitation will be addressed in 2026x.

#### Test Environment Generation

The Component Tester is an operation designed to support software development by providing a ready-to-use environment. This solution allows multiple ways to execute the application for testing purposes.

The Component Tester is generated by the Component Tester Generator. Based on the specified generation parameters, it can be used to:

- Facilitate application development following code generation from a UML architecture
- Support testing activities during software development

[IMAGE alt='' src='']

When you define the Component Tester parameters, you can generate the code. All files will be available in the .

From the **Files** tab, you can open the Tester with VS Code for further actions with the generated code.

Opening files with VS Code works only if you set the value of the configuration parameter "ide" to "vscode" and have VS Code installed on your machine.

[IMAGE alt='' src='']

#### Cpp Code Reverse

The goal of the Cpp Code Reverse operation is to create the UML components from the existing C++ files.

For working with the code reverse, first, you need to specify the CppCodeReverse configuration.

To specify the code reverse configuration

1. In the model, create a package for storing the configuration.
2. In the package, create the Code Generation Configuration diagram.
3. In the diagram, create the Cpp Code Reverse element.
4. In the Containment tree, under the Model, create a package that will be used as a target package for the created UML elements.
5. Drag the target package onto the Cpp Code Reverse element on the diagram pane to assign it as a target package.
6. Double-click the Cpp Code Reverse element to open the Specification window.
7. Specify the needed options.

[IMAGE alt='' src='']

| Option name | Default value | Description |
| --- | --- | --- |
| Create Strategy | Create element according to code | The creation strategy defines if the elements newly added to the code file should be created in the model. If you do not want the new elements to be created after executing the code reverse, choose Ignore new element from code strategy. |
| Delete Strategy | Delete element according to code | The deletion strategy defines if the elements deleted from the code file should also be deleted from the model. If you do not want the elements to be deleted after executing the code reverse, choose Ignore deleted element from code strategy. |
| Update Strategy | Update attribute according to code | The update strategy defines if the attribute changes in the code file should be applied in the model. If you do not want the attribute changes to be applied after executing the code reverse, choose Ignore attribute changes from code strategy. |
| Define Symbols | NA | Define the symbols to be expanded by the preprocessor when parsing files. |
| Dry Run | false | If this option is set to true, the operation will not modify the model after the execution. It only shows changes in the Software Producer Logs that would be made. |
| Include Directories | NA | Include directories used by the parser for searching "#include" files. |
| Verbose | false | If this option is set to true, every model creation, modification, and deletion is logged in the Software Producer Logs. |
| Name | Cpp code reverse element name | The name of the Cpp code reverse element. |
| Target Package | Target package name | The elements, created after code reverse execution, will be stored in this package. |
| Reverse Local Path | <sop.local.workspace.path>/<configuration.name> | Define the path where the C++ source files are stored. By default, the path points to the location where the project is stored. |

###### Code reverse example

You can find a sample model, Contact Book - Cpp Reverse, located in *<installation_directory>\samples\CATIA Software Producer*.

The files containing the C++ code and used in the sample are located in *<installation_directory>\samples\CATIA Software Producer\Contact Book - Cpp Reverse\Contact Book*.

You can use the files to try out the code reverse functionalities. Try deleting UML elements from the sample project and executing the CppCodeReverse configuration while changing various strategies. Also, try modifying the code files.

##### C++ to UML reverse process

The C++ to UML code reverse operation supports C++ files based on the latest C++ version: C++14, C++17, C++20. It does not imply that each new concept of a specific version is supported, but it reading the file should be available. Only header files are analyzed: .h and .hpp.

###### Supported elements

| Icon | Meaning |
| --- | --- |
|  | Supported / Partially supported. |
|  | Not supported. |

| Element | Status | Description |
| --- | --- | --- |
| Class |  | A declaration of a class in C++, used to define a custom type with members and methods. |
| Class member function declaration |  | Declaration of a member function inside a class, without its complete definition. |
| Class member function definition |  | The full definition of a member function, including its body, usually outside the class. |
| Class member variable |  | Variable defined within a class, representing an object's state or property. |
| Namespace declaration |  | A declaration of a namespace to organize classes and functions under a common name scope. |
| #include preprocessor directive |  | Preprocessor directive used to include header files or libraries. |
| Class constructor |  | A special function is called when an object is created, used to initialize its members. |
| Class destructor |  | A special function is called when an object is destroyed, used to release resources. |
| Global function declaration |  | Declaration of a function defined outside any class. |
| Global function definition |  | Full definition of a global function, including its body. |
| Alias (typedef & using) |  | Declaration of a type alias using typedef or using to simplify complex types. |
| #define preprocessor directive |  | Preprocessor directive that defines a macro or symbolic constant. |
| Global variable |  | Variable defined outside of any class or function, accessible globally in the program. |
| Union |  | A special data type that allows storing different types of data in the same memory location. |
| Struct |  | A declaration of a structure in C++, used to group multiple variables under the same type. |
| Enum |  | Declaration of an enumerated type, used to define a set of named constants. |
| @port |  | An annotation used to identify that a variable will be translated into a UML Port. |
| @getter:<var> |  | An annotation used to identify that an operation is a getter of a variable. |
| @setter:<var> |  | An annotation used to identify that an operation is a setter of a Port. |
| @agregation |  | Not supported. |
| @member |  | Not supported. |
| @association |  | Not supported. |
| @classifierBehavior |  | Not supported. |

###### Comment handling

| Function | Description |
| --- | --- |
| @generated_from, @generated_brief,@reverse_ignore | For any element of the code, any comment except lines containing “@generated_from”, “@generated_brief”, and “@reverse_ignore” annotations are expected to be taken into account. |
| Documentation in the model | Comments found in the C++ source code will be handled in the UML model. Once processed, the comment will be written in the UML item Documentation/Comments property. Only Doxygen documentation is processed.Example - The documentation in the Model |
| Comment styles | Doxygen comments delimiters (/** */, /*! */, ///, //!) are supported.Example - Comment styles |
| Supported C++ items | Supported C++ items for comments retrieval are class, struct, enum, union, typedef, attribute, function, and arguments. |
| Comment mapping | Only the last previous comment is taken into account. If there are several comment blocks before an item in C++ code, only the last is taken into account. example - Comment mapping |
| Doxygen command patterns | The supported Doxygen command patterns are @ and \ Example - Command patterns |
| Comment with Doxygen syntax handling rules | Comments with Doxygen syntax will be handled with the following rules:@param and \param commands will be retrieved, and their value will be set in the argument documentation attribute@brief command will be retrieved@return or @returns will be retrieved and its value will be set into the operation documentation of the return argument.Example |
| Other commands | Other commands (such as @author) will be added to the Item documentation as is.Example |
| @param[in\|out\|inout] | @param[in\|out\|inout]: direction set by @param command will be taken into account to set direction in the UML argument. |

###### Code reverse behavior specification

The behavior of the code reverse depending on the Cpp element is described in the following table.

| Function / Element | Description | Example |
| --- | --- | --- |
| Namespace declaration | The inline namespace (Since C++11) is ignored during parsing. |  |
| A package with the stereotype “C++ Namespace” is expected to be created with the name of the namespace for any declared namespace in the code. |  |  |
| “unique namespace name” attribute of “C++ Namespace” stereotype of the created package will have the name of the namespace. | Namespace declarationNamespace declaration since C++17 |  |
| If a class is defined in a namespace, the UML class will be created under the package corresponding to the namespace. | Class declaration with namespace |  |
| Class | A UML class is created for each declared Cpp class. | Class declaration |
| Inheritance | If a class inherits from another class, a generalization relation is created from the class to the other class. |  |
| The visibility of the inheritance is used in the created generalization relation.See: www.geeksforgeeks.org/visibility-modes-in-c-with-examples/ | Class declaration with generalization |  |
| Nested Class | A declaration of a class/struct or union appearing within another class is known as a nested class. https://en.cppreference.com/w/cpp/language/nested_types |  |
| A UML class will be generated under the parent class for the Cpp nested class. |  |  |
| Abstract Class | A Class is abstract when all functions are defined as virtual. See virtual operation. |  |
| Global functions and variables | A “global” Class is created without any name and with the “C++ Global” stereotype when code contains functions and variables declared outside any class (global functions and global variables). |  |
| The “global” Class is created under the root package. |  |  |
| Class constructor | An operation with the stereotype “C++ Constructor” will be generated for any constructor declared in the code of the class. | Constructor |
| The Initializer List of a constructor is replicated in the “Initialization list” field of the “C++ Constructor” stereotype applied to the operation. | Constructor with Initialization list |  |
| The “explicit” specifier of a constructor is replicated in the “Explicit” field of the “C++ Constructor” stereotype applied to the operation. | Constructor with explicit specifier |  |
| Class destructor | An operation with the stereotype “C++ Destructor” will be generated for any destructor declared in the code of the class. |  |
| Variable (Class Member Variable and Global Variable) | A property is generated in the UML class for each member variable of the Cpp class. |  |
| Properties created from the reverse code analysis will keep the order in which they are read. |  |  |
| Visibility of the property is configured according to the declaration in the code for that variable. |  |  |
| The type of the variable is used to configure the type of the property. | Property |  |
| The default value of the property is a string set as defined in the code. | Property |  |
| Pointer and reference declaration | “Type Modifier” attribute of the property will be set to “*” for a variable declared as a pointer. | Pointer and reference |
| “Type Modifier” attribute of the property will be set to “&” for a variable declared as a reference. |  |  |
| “Type Modifier” attribute of the property will be set to “&&” for a variable declared as a rvalue reference. |  |  |
| “Type Modifier” attribute of the property will be set to “**” for a variable declared as a double pointer. |  |  |
| “Type Modifier” attribute of the property will be set to “*&” for a variable declared as a reference to a pointer. |  |  |
| List & Vector declaration | Multiplicity attribute of the property will be set to “*” for a variable declared as a list or a vector. | List declaration class MyClass{ std::list myList; }; UML: [class] MyClass \|-[property] myList:bool, multiplicity=*]]>List declaration class MyClass{ std::vector myVector; }; UML: [class] MyClass \|-[property] myVector:bool, multiplicity=*]]> |
| Array declaration | For a variable declared as an array, the corresponding property will be created with the stereotype “C++ Attributes,” and the “Array” attribute is set with the size of the array. | Array declaration class MyClass{ std::array myArray; }; UML: [class] MyClass \|-[property] myArray:int [[C++ Attributes:Array=2]]]]> |
| Const | For a variable declared as const, the corresponding property will be created with the “Is Read Only” attribute set to true. | Const declaration |
| Static | For a variable declared with the storage class “static”, the corresponding property will be created with “Is Static” attribute set to true. | Static declaration |
| Mutable | For a variable declared with the storage class “mutable”, the corresponding property will be created with the stereotype “C++ Attributes” and the “Mutable” attribute is set to true. | Mutable declaration |
| Bit field | For a variable declared using a bit field pattern, the corresponding property will be created with the stereotype “C++ Attributes,” and the “Bit Field” attribute is set with the size of the bit field. | Bitfield declaration |
| Extern | For a variable declared with the storage class “extern”, the corresponding property will be created with the stereotype “C++ Extern”. |  |
| Function Declaration (Class Member Function & Global Function) | An operation is generated in the UML class for each member function of the Cpp class. |  |
| Visibility of the operation is configured according to the declaration in the code for that variable. | Function |  |
| Virtual | For a function declared as virtual, the corresponding operation will be created with the stereotype “C++ Operation,” and the “Virtual” attribute is set to true. |  |
| Volatile | For a function declared as volatile, the corresponding operation will be created with the stereotype “C++ Operation,” and the “Volatile” attribute is set to true. |  |
| Static | For a function declared with the storage class “static”, the corresponding operation will be created with the “Is Static” attribute set to true. | Static declaration |
| Const | For a function declared as const, the corresponding operation will be created with the “Is Query” attribute set to true. |  |
| Operator | For a function having the name “operator<overloaded_operator>”, an operation will be created with the C++ Operator” stereotype. <overloaded_operator> can have the following values: |  |
| Function Argument | For a function declaring a returned value, a parameter will be generated with direction set as “return”. |  |
| For each argument of a function, a parameter will be generated with direction set as “in” or “inout”. | Operation with arguments |  |
| The type of the argument is used to configure the type of the parameter. | Operation with arguments |  |
| Pointer and reference declaration | “Type Modifier” attribute of a parameter will be set to “*” for an argument declared as a pointer. |  |
| “Type Modifier” attribute of parameter will be set to “&” for an argument declared as a reference. | Pointer and reference |  |
| List declaration | Multiplicity attribute of parameter will be set to “*” for an argument declared as a list. | class MyClass{ void myFct(std::list myList); }; UML: [class] MyClass \|-[operation] myFct:void \|-[parameter] myList: type=bool, direction=in, multiplicity=*]]> |
| Array declaration | For an argument declared as an array, the corresponding parameter will be created with the stereotype “C++ Attributes,” and the “Array” attribute is set with the size of the array. | class MyClass{ void myFct(std::array myArray); }; UML: [class] MyClass \|-[operation] myFct:void \|-[parameter] myArray: type=int [[C++ Attributes:Array=2]]]]> |
| Const | For an argument declared as const, the corresponding parameter will be created with direction set to “in” |  |
| Variable length parameter list | For a variable length function, the latest parameter will be created with the name “…” without any type |  |
| Function Definition (Class Member Function & Global Function) | For the implementation body of a function, an opaque behavior will be generated, the language attribute will be set to “C++”, and the body attribute will be filled with the body of the function. This opaque behavior will be referenced by the operation with the “Method” attribute. | Operation with behavior |
| Standard Data Types | When a model element (eg, property, parameter) references a type, the reference is mapped to standard types for the following types: |  |
| Structure | A UML class with the stereotype “C++ Struct” will be created for each declared struct. |  |
| A property will be created for each field of the struct. | Structure definition |  |
| Enumeration | An enumeration will be generated for an enum in the code. |  |
| An enumeration literal with the stereotype “C++LiteralValue” will be generated for each field of the enum. |  |  |
| A value attribute of “C++LiteralValue” will be configured with the value of the field, if any. |  |  |
| Since C++11, an enum can be defined using enum class. Such a pattern will be supported when detecting enums in code. |  |  |
| Union | A UML class with the stereotype “C++ Union” will be created for each declared union. |  |
| A property will be created for each field of the union. | Union definition |  |
| Alias (Typedef and Using) | For an alias to another type (via typedef or using), a Data Type will be generated and a generalization relation will be created between this Data Type and the Data Type source of the alias. | typedef declarationUsing declaration |
| typedef of an array | For an alias to another type (via typedef or using) declaring an array, a Data Type will be generated with the “C++ Attributes” and “Array” attribute is set with the size of the array and a generalization relation will be created between this Data Type and the Data Type source of alias. |  |
| typedef of a struct | For an alias (via typedef or using) declaring a struct, a class will be generated (same as for a Union). |  |
| For an alias (via typedef or using) declaring a struct, if the struct is anonymous, the created class will have the name of the alias with the suffix “Struct”. | Structure definition \|-[class] <> [[C++ Struct]] \|-[property]data1:type=C++ ANSI profile::datatypes::unsigned int]]> |  |
| typedef of an enum | For an alias (via typedef or using), declaring an enum, an enumeration will be generated (same as for Enumeration) |  |
| For an alias (via typedef or using) declaring an enum, if the enum is anonymous, the created enumeration will have the name of the alias with the suffix “Enum”. | enum definition |  |
| typedef of a union | For an alias (via typedef or using), declaring a union, a class will be generated (same as for Union) |  |
| For an alias (via typedef or using) declaring a union, if the unionenum is anonymous, the created class will have the name of the alias with the suffix “Union”. | Union definition \|-[class] <>[[C++ Union]] \|-[property]data1:type=C++ ANSI profile::datatypes::int \|-[property]data1:type=C++ ANSI profile::datatypes::float \|-[property]data1:type= UML Standard Profile::MagicDraw Profile::datatypes::char ]]> |  |

###### Limitations

In the following table, you can see functionalities that are not yet supported in the code reverse.

| Icon | Meaning |
| --- | --- |
|  | Not yet supported. |

| Function | Status | Description |
| --- | --- | --- |
| Friend class |  | If a class is declared a friend to another one, a usage relation with the “C++ Friend” stereotype is expected to be generated. |
| #Include preprocessor directive |  | If a file contains one or multiple class definitions and contains #include directives to other files containing class definitions, a usage relation is created for the corresponding UML classes and the targeted classes with the stereotype “C++ Include”. |
|  | If the #include directive is declared using <>, the “header include” attribute will be configured with the value “System Include“ |  |
|  | If the #include directive is declared using “ “, the “header include” attribute will be configured with the value “User Include“ |  |
| Variable supported by an association |  | If the annotation @association is defined before the declaration of a variable and this variable is a pointer, a directed association relation will be created from the class to the type of the variable, and the role on the target will have the name of the variable. |
| Flow Property variable |  | If the annotation @port:<port_name> is defined before the declaration of a variable, a Property will be generated in an Interface referenced by a Port. A Port and an Interface will be created for each port_name. The <port_name> will be part of the prefix of the variable. |
| Function pointer |  | For a variable declared as a function pointer, the corresponding property will be created with the stereotype “C++ FunctionPtr,” and the signature attribute will be set with the signature definition. |
| Multiple declarations |  | For a variable declared with a complex collection of storage classes or declarations, the Type Modifier attribute will be used to register the complete declaration. “$” char replaces the type name.const on pointer not yet supported: const int* const |
| Friend |  | For a function declared as a friend in a class, a usage relation with the “C++ Friend” stereotype is created between the operation in the class declaring it and the current class. |
| Exception |  | For a function declared with the suffix noexcept (since C++11), the corresponding operation will be created with the stereotype “C++ Operation” and the “Throw exception” attribute is set to “none”. |
|  | For a function declared with the suffix noexcept (<condition>) (since C++11), the corresponding operation will be created with the stereotype “C++ Operation”, and the “Throw exception” attribute is set to “none”, and the condition will be configured somewhere. |  |
|  | For a function declaring an exception without any argument (C++98 and C++03 only), the corresponding operation will be created with the stereotype “C++ Operation” and the “Throw exception” attribute is set to “any”. |  |
|  | For a function declaring an exception with arguments (C++98 and C++03 only), the corresponding operation will be created with the stereotype “C++ Operation”, “Throw exception” attribute is set to “any”, and “Raised exception” attribute is set with the value of the exception arguments. |  |
| @getter |  | For a function having annotation @getter before its declaration, the corresponding operation will be created with the stereotype “getter”, and “getter/setter for attribute” will be configured with the corresponding property. |
| @setter |  | For a function having annotation @setter before its declaration, the corresponding operation will be created with the stereotype “getter” and “getter/setter for attribute” will be configured with the corresponding property. |
| “C++ Parameter” and “volatile” attribute set to “true” |  | For a return type declared with the modifier volatile, the corresponding return parameter will be created with the stereotype “C++ Parameter” and “volatile” attribute set to “true” |
| #define preprocessor directive |  | A macro can be defined via a property with Is Read Only=true, but the C++ profile needs to be extended with a new stereotype “C++ Macro” to distinguish it from a regular const.Another alternative is to use the notes to attach a const to a Class. |
| Templates |  | Not supported. |

#### Software Governance

To commit elements from the modeling tool, you need to:

- Associate a SCM repository to the model element
  - Using Connected Software Connectors
  - With a local configuration
- Create an SCM Configuration element
- Configure an SCM branch
  - Using Software Logical Items of Connected Software
  - With a local configuration

##### SCM Repository association

###### Associating repository using Connected Software Connectors

To associate the SCM repository

1. In the Containment tree, right-click Model.
2. In the shortcut menu, click Software Code Generation > Associate SCM Repository .
3. In the open Associate SCM Repository dialog, choose the needed repository,
4. Click OK .

[IMAGE alt='' src=''][IMAGE alt='' src='']

After you click **OK** in the **Associate SCM Repository** dialog, the repository information will be associated to the model via the «Connector» stereotype from the Embedded Software Profile:

- repositoryHost: root url of the targeted Git server (ex: : https://gitlab.com)
- repositoryPath: relative path of the repository (ex: SJA/cubesat-control)
- repositoryToken: associate the access token to the repository (example: glpat-6_y_4y8hMDNDxWyaATi4)

To remove the association of the SCM repository

1. In the Containment tree, right-click Model.
2. In the shortcut menu, click Software Code Generation > Associate SCM Repository .
3. In the open Associate SCM Repository dialog, click the selected repository for which you want to remove the association.
4. Click OK .

When you click **OK**, the association will be removed and the branches will be detached from elements if there were any.

###### Local Configuration

If Connected Software is not used, it is still possible to attach a repository to the model element.

To do so, associate the «Connector» stereotype from Embedded Software Profile to the model element and configure it as following:

- repositoryHost: root url of the targeted Git server (ex: : https://gitlab.com)
- repositoryPath: relative path of the repository (ex: SJA/cubesat-control)
- repositoryToken: associate the access token to the repository (example: glpat-6_y_4y8hMDNDxWyaATi4)

##### SCM Configuration creation

It is necessary to associate a repository before attaching a branch from the configuration dialog.

From the diagram palette, the you can create a SCM Configuration that will contain a reminder of the repository path of the model: you cannot edit the repository here. If you need to change the repository, see.

[IMAGE alt='' src='']

To use the SCM Configuration, you have to drag and drop the SCM configuration on the code configuration or application configuration that you wants to execute and commit:

[IMAGE alt='' src='']

##### SCM Branch Configuration

This is the branch to which you are going to commit the code.

It is necessary to associate a repository before attaching a branch from the configuration dialog.

###### With Software Logical Items of Connected Software

- you can edit the branch in the **Specification**window by clicking the three dots in the branch value field:

[IMAGE alt='' src=''][IMAGE alt='' src='']

- When you click OK in the Associate Branch of Repository dialog, the branch information will be associated to the configuration via the «SoftwareLogicalItem» stereotype from Embedded Software Profile:

- 
  - 
    - branchName: the branch name to target (example: “main”)
    - SoftwareLogicalItemId: ID of the logical Item linked to the branch (from Connected Software)

If if you remove the repository association, the branches will also be detached from elements if there were any. See.

###### Local Configuration

The you can edit it in the branch:

- branchName: the branch name to target (example: “main”)

##### Code persistency

Code generation is executed via the regular mechanism.

The code will be committed after a successful execution of code generation.

[IMAGE alt='' src='']

At execution phase, mandatory parameters are checked, if they are not present or are invalid, the operation is canceled and a message is printed (see an example below).

[IMAGE alt='' src='']

The mandatory parameters are:

- the repository path: must be present
- the repository token: must be present
- the repository host: must be present and must reference a valid URL (syntax check only)
- the commit message: must be present
- the commit author: must be present
- the branch name: must be present

#### Local workspace of the software producer

Under the local workspace, you can find the generated files, if you have selected the download option and left the default location (as seen above) in the configurations. You can also find some other files under an “etc” folder:

- <Local_workspace_path>

1You can change the root of the local workspace path in the project options.

2By default, a backup of your downloaded files is saved in this folder so that in case something wrong happens with the download of new files, you can still reach your previous files. You can disable this option in the **Project Options**

3SPO Report files are rotated by size and date so that you might see multiple report files here.

4Log files are rotated by size and date so that you might see multiple log files here.

#### Views

##### Files tab

The**Files**tab lists the existing configurations in the model and displays as children the files contained in the directory referenced by the configuration.This behavior is available for the code generation configuration and the reverse code configurations.

Configurations are greyed if they have no content (no files yet).

[IMAGE alt='' src='']

In the **Files**tab, double-click a file to see its content in a.

You can select any file in the **Files**tab, and open the Specification of an element that was used to generate the file, or navigate to that element in the Containment tree. Right-click the file and from the shortcut menu, choose **Select in Containment Tree**. If there is more than one element in the file, you will be offered to choose the needed element.

[IMAGE alt='' src='']

You can activate the filter mode in the **File** tab to display the files impacted by the element which you select in the Containent tree.

To display files related with the selected element

- In the Files tab toolbar, click Filter on Selection .

[IMAGE alt='' src='']

From the **Files**tab, you can open the generated filesin the default editor configured for that file type on your machine. If no default application is associated with the file type, you will be prompted to choose one.

[IMAGE alt='' src='']

##### Code viewer

The code viewer opens when you double click a file in the **Files**tab. The code viewer is read-only.

In the open code viewer, you can see the highlighted markers where the selected element is used in the file.

To view the markers

1. In the Files tab, right-click the needed file.
2. In the shortcut menu, click Select in Containment Tree .

[IMAGE alt='' src='']

You can also navigate from the code viewer to the element in the **Containment**tree from which the code was generated.

To navigate to the element in the **Containment**tree

1. In the open code viewer, hover over the id near the *@generated_from*.
2. In the displayed tooltip, click the element name.

[IMAGE alt='' src='']

##### Software Producer Logs

In the Software Producer Log panel, you can see the messages of the running SPO.

[IMAGE alt='' src='']

In the following table, the actions to enhance the navigation in this window are explained:

| Icon | Name | Description |
| --- | --- | --- |
|  | Scroll to the Start | Scrolls to the tip of the panel. |
|  | Scroll to the End | Scrolls to the bottom of the panel. |
|  | Lock Position | By default, when some new logs are printed, the scrollbar goes down. If the user wants to prevent the panel to be scrolled automatically to the bottom, he can click on this button. |
|  | Clear | Clears the panel. |
|  | Show Log File | Opens the file where the logs are written (each project has its own log file). |
|  | Show Timestamp | Adds a timestamp as a prefix to the messages. |
|  | Show Additional Messages | Shows more messages related to the SOP client. |
|  | Level combo box | Shows the messages of the selected level, hide the others. By default, All levels is selected to display all types of messages. Other available types are: Info, Error, Warning. |
|  | Find | Highlights the search results and navigate to them |

A log file for general Software Producer messages not related to a specific project is stored next to the modeling tool log file.

At the bottom right corner of the modeling tool, in the progress bar, you can see whether the generation is running. After the generation is completed, the notification is displayed in case of failure or always if the verbose mode is activated (**Environment Options**> **CATIA Software Producer Client General Properties** > **Notifications** section).

##### Validation Results

When an operation produces a report, the plugin reads it and opens it in a **Validation Result** window if any element has a diagnostic associated.

[IMAGE alt='' src='']

A diagnostic is associated with a rule consisting of a severity, message, and source.

You can navigate to the source in the Containment tree. If you need to show more details concerning the rule or open the full report, right-click the appropriate lines of the table.

You can turn off the **Validation Results** window's opening after the operation produces a report.

To turn the validation report off

1. In the modeling tool main menu, click Options and select Project .
2. Set the **Show Validation Report**property to *false*.

When you execute a configuration, before calling the operation the plugin checks the UML Completeness Constraints. If a mandatory property is missing (“elements” in the example below), a validation warning and a notification will be displayed informing which tag value(s) are missing.

[IMAGE alt='' src='']

##### Diagrams and Containment tree

The following commands are available from the diagrams toolbar or from the shortcut menu of the supported elements in the Containment tree:

| Button | Description |
| --- | --- |
| Show in File Explorer | Open a location in your file system wherein the Software Production Operation results file is stored. |
| Execute Selected Configuration | Runs the code generation for the selected configuration. |

#### Code Generation Result Table

When the option "storeExecutionSummaryInModel" is set to true in the configuration, the results of the execution of the configuration is saved as an object under the configuration inside the model.

[IMAGE alt='' src='']

You can have an overview of all of these execution objects in the **Code Generation Result Table**.

To create a table

1. In the Containment tree, right-click a package.
2. From the shortcut menu, select Create Diagram .
3. Search for Code Generation Result Table and click it.

[IMAGE alt='' src='']

[IMAGE alt='' src='']

In the Containment tree on the above image, you can see under the configurations that new objects were created:

- Configuration Execution: for example, "fmu" execution at 2024-08-23T12:47:14.008"
- Operation Instance: for example, "FMU Middleware Generation"

Those objects are displayed in the **Code Generation Result Table**. Among other information you can see the duration of each operation and the total duration on the execution, same as for the status.

If you click the Open Logs in the Logs column, you will see the logs of the selected operation.

[IMAGE alt='' src='']

If you click the location in the Local Result Path column, your file explorer is opened at the specified location.

#### Options

##### Project Options

You can specify **Project Options** for the CATIA Software Producer Client.

[IMAGE alt='' src='']

| Option name | Default value | Description |
| --- | --- | --- |
| Workspace path | <project_directory>\<project_name> | Local workspace path for this project. Bu default, it is next to the project file, and named after it. It is used by default in the local path property of the configurations, represented by the variable <sop.lokal.worspace.path>. |
| Backup property | true | If set to true, then before each generation, the code will be backed-up in the etc/backup folder of the local workspace. |
| Show validation report | true | If set to true, then each time a report will be generated by an operation, the Validation Results Window will be displayed. |

##### Environment Options

You can specify **Environment Options** for the CATIA Software Producer Client and CATIA Software Producer Client General Properties.

A workspace is automatically created on our cloud servers for each of your projects using the widget. This workspace gathers the assets needed for the generation. A cloud workspace is automatically deleted after 30 days of inactivity. You can also delete it manually in the**Environment Options**dialog. If you delete the workspace, all the components will have to be regenerated on the cloud on your next session because you will not be able to push any files to a workspace through the plugin.

To monitor the CATIA Software Producer Client workspaces, you must login to the platform first.

[IMAGE alt='' src='']

| Option name | Default value | Description |
| --- | --- | --- |
| Enable Software Governance | true | Enable Software Governance to manage generated code in SCM repositories. |
| Activate Smart Launch Mode | false | Activate Smart Launch Mode to execute the operations only when a change is detected. |
| Activate Verbose Mode | false | Activate Verbose Mode to get more notifications during the generation process, |
| Show next time the question to clean lock files | true | If set to false, deletion of local files previously generated by the configuration will be done (in the clean and full generated mode) without asking for it in a dialog to the user. |

#### Additional Information

You can switch projects (or even shut down your computer, saving your work first) while waiting for the generation result as it is running on the cloud and as the widget keeps the IDs of the cloud assets in the record files located in <local workspace path>\etc\operations\spoRecordFile.json (you will have access to it if you need it, for example, for the debugging purpose). When you come back, another dialog will tell you that operations were running while you were away and will propose you inspect the result and download it.

**Sample models**

The following sample models are available in *<modeling tool instalation directory>\samples\CATIA Software Producer\*

- SysML Flashlight Tempo.mdzip
- UML Lock Manager.mdzip
- Contact Book - Cpp Reverse.mdzip

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3><strong><a href="https://help.3ds.com/HelpDS.aspx?P=19&amp;V=2026&amp;L=English&amp;F=CatEspMagicUserMap/catesp-c-ov.htm&amp;contextscope=all">Latest documentation</a></strong></h3><p>The CATIA Software Producer allows you to generate and build code from a UML or SysML v1 model. You can generate code, for example, from the UML Class structure,  UML State Machine, or SysML v1 Blocks. </p><h2>Key concepts and capabilities</h2><p>CATIA Software Producer offers the following generation capabilities:</p><ul><li data-uuid="2ed3bd05-3732-46b8-a3e5-3423b88a5edd">Generating C code from UML and SysML v1 models.</li><li data-uuid="ac3ff4ec-4044-415c-a407-1b317898c00b">Generating C++ code from UML and SysML v1 models.</li><li data-uuid="54dfa66b-56f3-44c7-ad9a-38daed355803">Generating Java code from UML classes.</li><li data-uuid="2ee0d5c5-6d28-4325-9bc1-10d7a7debd31">Generating target dependent middleware code for AUTOSAR classic and adaptive.</li><li data-uuid="f6e46964-56a6-44a9-a75e-1d8cf05d1efc">Generating and compiling code for FMU.</li><li data-uuid="0a399dcd-9ead-423f-a3d4-f86b4cb43d6a">Generating and compiling code to produce an executable for Windows, Linux, or a custom target.</li><li data-uuid="ed4dccbf-b5c2-4415-8ba8-b73fb5d10714">Generating code from a model persisted as a file, or in TeamworkCloud, or the <strong>3D</strong>EXPERIENCE Platform.</li><li data-uuid="d1a7a253-21e8-45e3-a65d-63cc8d95e103">Generating code with traceability information, establishing the relation from the model items to the code.</li><li data-uuid="0c7c264f-0170-43b1-8440-4e63a837c83c">Code revers from C++ to UML.</li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="74dac8af-7f67-49a3-81d1-4cd204eaddc5"><ac:rich-text-body><p>For more information about the Software Production Engineering application, see <a href="https://help.3ds.com/2024x/english/dsdoc/CatEspUserMap/catesp-c-ov.htm?contextscope=cloud&amp;id=bb196d4c58f14192a3a2c4c1fbefb4c6">Software Production Engineering</a>.</p></ac:rich-text-body></ac:structured-macro><h2><span>Prerequisites</span></h2><ul><li data-uuid="1bab0c33-0b6d-497f-8acd-61a793f096c7">The CATIA Software Producer Client plugin is installed in your modeling tool. Learn more about how to <ac:link><ri:page ri:space-key="IL" ri:content-title="Downloading installation files" /><ac:plain-text-link-body><![CDATA[download the installation files]]></ac:plain-text-link-body></ac:link>.</li></ul><p><span>When you launch any operation for the first time in your project, a dialog will open to configure the local workspace path, which will host generated resources.</span></p><p><ac:image><ri:attachment ri:filename="local_workspace.png" /></ac:image></p><h2>Configuring the code generator</h2><h3>The principle </h3><p>The generated code is composed of multiple layers as shown on the schemas below.</p><p>When the user configures code generators, the generated files will contain the following part:</p><p><ac:image ac:align="center"><ri:attachment ri:filename="principle_lauers_I.png" /></ac:image></p><p><br /></p><p>When the user configures application generators, the generated files will contain the following part:</p><p><ac:image ac:align="center"><ri:attachment ri:filename="principle_lauers_II.png" /></ac:image></p><p><br /></p><p>To configure the code generator, you have to create a Code Generation Configuration Diagram.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="to_generate_code.png" /></ac:image></p><p><ac:image ac:align="center" ac:width="1100"><ri:attachment ri:filename="to_generate_code_diagram_example.png" /></ac:image></p><h6 style="text-align: center;">Click the image to enlarge.</h6><p>Code generation supported so far is C, C++, and Java. You can select them in the diagram palette.</p><p><ac:image><ri:attachment ri:filename="diagram_palette_C_C_Java.png" /></ac:image></p><p>A code generation configuration is composed of:</p><ul><li data-uuid="015c1af5-6bd8-4197-9b32-f4e56407376d"><strong>Elements</strong></li><li data-uuid="43045b59-27f6-418c-87cc-4f99d78c93f5"><strong>Local Path</strong>. A patch to your workspace.</li><li data-uuid="fe3a0c2c-9508-4b58-af9d-9ae0653ceb31"><strong><ac:link ac:anchor="SCM Configuration" /></strong> (optional)</li><li data-uuid="448d1734-d482-4b07-a276-9e9d7736ae1e"><strong>Store Execution Summary in Model:</strong> set to false by default. Set to true, if you want an execution object to be created in your project (under the configuration element), so that you can view the execution summary of your configuration in the Code Generation Result Table.</li></ul><p> <ac:image><ri:attachment ri:filename="cc_element_for_generation.png" /></ac:image></p><p><ac:image><ri:attachment ri:filename="cc_specification.png" /></ac:image></p><p>Application production supported so far is FMU, AUTOSAR, Linux, Windows, and Custom Target.</p><p><ac:image><ri:attachment ri:filename="supported_application_production.png" /></ac:image></p><p><br /></p><p>An application production is composed of:</p><ul><li data-uuid="eb9c1e78-4b47-4514-8180-b21c115cabce">code generation configurations: their generated files are used to produce the application</li><li data-uuid="45ab48ca-c441-455d-b831-86ce54a18149">top level element: only for FMU Production and AUTOSAR Generation configurations</li><li data-uuid="43d41587-0b1f-4acb-a26a-cea0c7b6b633">local workspace path<p><br /></p></li><li data-uuid="b86b0f98-a542-4a3e-9464-48e1aefc53a6"><p>store execution summary in model: by default set to false ; if set to true, an execution object will be created in your project (under the configuration element), so that you can view the execution summary of your configuration in the Code Generation Result Table.</p></li><li data-uuid="198e930b-cf11-45f2-b7f9-4eee96779215"><p><span>generate code: by default set to true.</span></p><ul><li>If set to true, the associated code generation configuration(s) will be launched and their results will be taken as inputs of the final operation.</li><li>If set to false, the inputs of the final operation are the current files stored under the folders referenced by the configurations.</li></ul></li><li data-uuid="4b24a01d-9f37-4eb1-a139-04b779ab4598">parameters specifics to the selected operation:<ul><li>in the example below: platform, include_souce, C_standard, Cpp_standar, debug<br /><ac:image><ri:attachment ri:filename="fmu_example.png" /></ac:image></li></ul></li><li data-uuid="4b284703-8d7e-4f62-be0d-58d6fa6c18ab"><ac:link ac:anchor="SCM Configuration" /> (optional)</li></ul><h3>Code generation on the platform or locally</h3><p>The code generation can be launched on the platform or locally.</p><p>The local code generation is available for:</p><ul style="text-align: left;"><li data-uuid="16be16d3-4fad-4f4e-a200-dfce35cdca39">Code Generation configurations (C Code Generation, Cpp Code Generation, Java Code Generation, and Component Tester)</li><li data-uuid="5bbf28be-30f8-4d83-9fd0-f382a4d9c593">Component Tester configuration in generation mode (default mode)</li></ul><p><br /></p><p>If you want to generate the code on the platform, you need to specify parameters of the configuration.</p><p><br /></p><p>To launch the code generation on the platform</p><hr /><ol><li data-uuid="e6d04bc6-4405-4cbd-9053-5aa2510c15b1">In the Containment tree or on the diagram pane, right-click the needed configuration.</li><li data-uuid="2601e253-1b19-4c0c-bfbf-107f2cac5194">From the shortcut menu, select Specification.</li><li data-uuid="5ad017b9-640f-4d3c-8bba-9356c9a6598a">In the <strong>Specification </strong>window, go to the Code Generation Configuration option group.</li><li data-uuid="34324ab8-b30e-46ef-bd75-3a8deca130e7">Set the <strong>Execute On Cloud</strong> option to <em>true</em>.</li><li data-uuid="99c9f29f-a577-4d80-87ae-cf1397489d91">Click <strong>OK</strong>.</li></ol><p><ac:image><ri:attachment ri:filename="execute_on_cloud.png" /></ac:image></p><p>Before starting to work on code generation on the platform, first, you have to <strong>connect to 3DEXPERIENCE</strong> by entering the URL of the Software Producer cloud server. After that, you will be able to log in with your regular identifiers. <span>You must have the Software Production Engineer Role. It will give you permission to use the service.</span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="cf5eca55-cadf-4839-a9b7-d5e12478fc8b"><ac:rich-text-body><p>For information about how to authenticate with the <strong>3D</strong>EXPERIENCE platform, see <ac:link><ri:page ri:space-key="MT" ri:content-title="Authentication with 3DEXPERIENCE platform" /><ac:link-body>Authentication with <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><h3>Specifying elements and configurations</h3><p>You can specify “elements” or “topLevelElement” in two ways:</p><ul><li data-uuid="90b7204a-68cf-4d2e-9eb4-3026df7836d1">Drag and drop the element from the Containment tree to the desired configuration in the diagram<br /><ac:image><ri:attachment ri:filename="drag_drop_to_set_element.png" /></ac:image></li><li data-uuid="5b9ed14b-d87c-403b-b564-5769ec8db703">Open the Specification window of the configuration and edit the Element property.</li></ul><p>You can specify “codeGenerationConfigurations” in two ways:</p><ul><li data-uuid="a2c5d61b-9ebf-48e8-a142-99c0130aefbe">On the diagram, drag and drop the Code Generation Configuration to the application Production configuration.<br /><ac:image><ri:attachment ri:filename="configuration_drag_drop_production.png" /></ac:image></li><li data-uuid="98c05975-e414-4734-8098-29d3a88f32be">Open the Specification window of the configuration and edit the Code Generation Configuration property.</li></ul><h2>Validating</h2><p>You can check if your model is compatible with the code generation via the standard validation menu.</p><p><br /></p><p>To run the validation</p><hr /><ol><li data-uuid="52ec56c1-bc37-4ce9-bfde-6d0740ce0ab8">In the Containment tree, right-click the <span>code configuration.</span></li><li data-uuid="c5afa5cb-62a1-4256-aee2-d2b7faf1e608"><span>In the shortcut menu, select one of the following:</span><ol><li><span>Click <strong>Validate, </strong>and in the open <strong>Validation </strong>dialog, choose either all possible constraints or only <strong>Code Generation Constraints</strong>.</span></li><li><span>Click <strong>Validate Element</strong> to run validation for a selected element only.</span></li></ol></li></ol><p style="text-align: left;"><span><ac:image><ri:attachment ri:filename="start_validation_containment.png" /></ac:image></span></p><p style="text-align: left;"><br /></p><p style="text-align: left;"><span>You can also use the Validate Diagram command, which you can find in the configuration diagram toolbar:</span></p><p style="text-align: left;"><span><ac:image><ri:attachment ri:filename="start_validation_toolbar.png" /></ac:image></span></p><p style="margin-left: 0.0in;"><span style="color:var(--ds-text,#172b4d);">The results are displayed in the <strong>Validation Results</strong> window if there are any errors or warnings. </span></p><p style="margin-left: 0.0in;"><span style="color:var(--ds-text,#172b4d);"><ac:image><ri:attachment ri:filename="validation_results_window.png" /></ac:image></span></p><p><span>The operation logs are displayed in the usual Software Producer logs window.</span></p><p>If you do not want to run the validation for code generation when calling the validation menu, you can choose to ignore a selected validation suite and/or validation rule. </p><p><br /></p><p>To ignore a validation suite or a validation rule</p><hr /><ol><li data-uuid="d1024f0b-b754-47af-8d9a-c7a04580a879">In the modeling tool's main menu, click <strong>Options </strong>&gt; <strong>Project</strong>.</li><li data-uuid="909f6841-f202-4601-a1c1-563f965c173f">In the open <strong>Project Options</strong> dialog &gt; <strong>Validation</strong>, specify the <strong>Ignored Validation Suites</strong> and/or <strong>Ignored Validation Rules</strong>.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bb2ebccd-661c-4b44-ab39-7224077841f1"><ac:rich-text-body>The validation will still be triggered during code generation. If you want to hide the validation results at this point, set the <strong>Show Validation Report</strong> property to <em>false</em> in the <strong>Project Options</strong> &gt; <strong>CATIA Software Producer Client</strong> (see <ac:link ac:anchor="Validation Results" />.). </ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="validation_project_options.png" /></ac:image></p><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5adc8d88-6d27-49d7-9c2e-7a72de6cd363"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">Validation is actually an SPO (Software Production Operation) launched in dry-run mode (no file generation, no credit consumption).</span></p></ac:rich-text-body></ac:structured-macro><p style="margin-left: 0.0in;"><br /></p><h2>Executing Operations</h2><p>To execute the code generator, you can run the generation from the following locations:</p><ul><li data-uuid="d6a78739-d62b-4474-bdc0-589efbf0de44"><span>Main menu</span></li><li data-uuid="f0363b9b-f399-4eba-9d9a-557b06330867"><span>Code generation diagram</span></li><li data-uuid="43c29dd0-d9d3-4e5b-8212-3316ff6c8649"><span>Containment tree</span></li></ul><h3><span>Execution from the main menu</span></h3><p><span><ac:image><ri:attachment ri:filename="execution_main_menu.png" /></ac:image></span></p><p><span>You can do one of the following:</span></p><ul><li data-uuid="3a17a0b9-c055-4b29-8daf-59581f7b8c09">launch the default action <strong>Execute Operation</strong> that will launch the operations<ul><li>if <strong>Activate Smart Launch Mode</strong> is set to true in the environment options (<strong>Environment </strong>options dialog &gt; <strong>CATIA Software Producer Client General Properties</strong>), operations will be launched only if a change was made in the model. By default, the property is set to false.</li></ul></li></ul><ul><li data-uuid="645d05de-f782-4c46-afd0-453fa247e66f">launch the <strong>Clean &amp; Execute Operation</strong> that will delete your previously generated local files and cloud assets, then launch all the operations.<ul><li>for the deletion of the local files: if files previously generated by this configuration are found, a dialog will be prompted to the user to confirm the deletion of local files. <br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2531679e-8cff-4972-9d05-2b9de4156812"><ac:rich-text-body><p>If you do not want to see this message again,  cancel the selection of the <strong>Show this message next time</strong> check box. If you want to see this message again, there is a dedicated Environment option to turn the message showing on (see <ac:link ac:anchor="Additional Information" />).</p></ac:rich-text-body></ac:structured-macro><br /><ac:image><ri:attachment ri:filename="delete_local_folders.png" /></ac:image></li><li>for the deletion of cloud assets: it will be done without asking for the confirmation of the user. </li></ul></li></ul><h3>Execution from a code generation diagram</h3><p>Do one of the following:</p><ul><li data-uuid="ff490fa6-fa26-4d8a-85a6-7e0735c135be"><span style="color:var(--ds-text,#172b4d);">On the diagram pane, right-click a configuration element, and from the shortcut menu, choose <strong>Software Code Generation</strong> &gt; <strong>Execute Operation</strong>:<br /><ac:image><ri:attachment ri:filename="execute_operation_element_shortcut_menu.png" /></ac:image><br /></span></li><li data-uuid="e2c9df5f-7df0-46bc-bb0e-89b2f1af982c"><span style="color:var(--ds-text,#172b4d);">On the diagram pane, select a configuration element, and in the diagram toolbar, click <strong>Execute Selected Configuration</strong>:<br /><ac:image><ri:attachment ri:filename="execution_from_diagram_toolbar.png" /></ac:image><br /></span></li></ul><h4>Execution from Containment tree</h4><ul><li data-uuid="f6e8978d-4cce-44c5-a91b-b58a4c0cf178"><span style="color:var(--ds-text,#172b4d);">In the Containment tree, right-click a configuration element, and from the shortcut menu, select <strong>Software Code Generation</strong> &gt; <strong>Execute Operation</strong> &gt; <strong>Execute Operation</strong>:<br /><ac:image><ri:attachment ri:filename="execute_operation_containment_tree.png" /></ac:image><br /></span></li><li data-uuid="8c54675e-c32f-400b-89cd-9a8b9f1c6ff3"><span style="color:var(--ds-text,#172b4d);">In the Containment tree, right-click an input element, and from the shortcut menu, select <strong>Software Code Generation</strong> &gt; <strong>Execute with...</strong>:<br /><ac:image><ri:attachment ri:filename="execute_containment_tree_imput_element.png" /></ac:image><br /></span></li></ul><p>The operation logs are displayed in the<strong> Software Producer Logs</strong> window.</p><h3 style="margin-left: 40.0px;">Limitation</h3><p style="margin-left: 40.0px;text-align: left;">Currently, when a code generation is launched after renaming a class, the newly generated files reflect the new class names. However, the old files (corresponding to the previous class names) are not automatically deleted. This can lead to &quot;outdated&quot; files remaining in the output directory.</p><p style="margin-left: 40.0px;text-align: left;">This limitation will be addressed in 2026x. </p><h2>Test Environment Generation</h2><p><span>The Component Tester is an operation designed to support software development by providing a ready-to-use environment. This solution allows multiple ways to execute the application for testing purposes.</span></p><p>The Component Tester is generated by the Component Tester Generator. Based on the specified generation parameters, it can be used to:</p><ul><li data-uuid="cac79ca6-c859-4720-abb9-f300d164392d">Facilitate application development following code generation from a UML architecture</li><li data-uuid="c63f6ecf-e3bd-4c0b-8e57-7deb7368f503">Support testing activities during software development</li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="component_tester_example.png" /></ac:image></p><p>When you define the Component Tester parameters, you can generate the code. All files will be available in the <ac:link ac:anchor="Files tab" />.</p><p>From the <strong>Files</strong> tab, you can open the Tester with VS Code for further actions with the generated code. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="79614162-8ee6-4cb0-959a-1f106544972e"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">Opening files with VS Code works only if you set the value of the configuration parameter &quot;ide&quot; to &quot;vscode&quot; and have VS Code installed on your machine.</span></p></ac:rich-text-body></ac:structured-macro><p><br /><ac:image><ri:attachment ri:filename="open_with_vscode.png" /></ac:image></p><h2>Cpp Code Reverse</h2><p>The goal of the Cpp Code Reverse operation is to create the <span>UML components from the existing C++ files.</span></p><p>For working with the code reverse, first, you need to specify the CppCodeReverse configuration.</p><p><br /></p><p>To specify the code reverse configuration</p><hr /><ol><li data-uuid="1fdbb354-83f3-4826-97ed-0324c53a179e">In the model, create a package for storing the configuration.</li><li data-uuid="83145127-adc3-407c-a847-d5191a0a2e96">In the package, create the Code Generation Configuration diagram.</li><li data-uuid="0f587196-3fc4-4bb0-954d-9f39580c9653">In the diagram, create the Cpp Code Reverse element.</li><li data-uuid="925262da-fb78-45b4-a15f-35623f609d86">In the <strong>Containment </strong>tree, under the Model, create a package that will be used as a target package for the created UML elements.</li><li data-uuid="bd0ab304-17f8-4291-a1f8-3ee46f32954d">Drag the target package onto the Cpp Code Reverse element on the diagram pane to assign it as a target package.</li><li data-uuid="4bb3b21a-b5e1-4fec-b0f5-75cd1bc34bf7">Double-click the Cpp Code Reverse element to open the <strong>Specification </strong>window.</li><li data-uuid="8422634f-0ec6-4011-a4a7-4ddca34ae3e2">Specify the needed options.</li></ol><p><span><ac:image><ri:attachment ri:filename="code_reverse_configuration.png" /></ac:image></span></p><table class="relative-table" style="width: 92.2438%;"><colgroup class=""><col class="" style="width: 9.9156%;" /><col class="" style="width: 24.0979%;" /><col class="" style="width: 65.9865%;" /></colgroup><tbody class=""><tr class=""><th>Option name</th><th>Default value</th><th>Description</th></tr><tr class=""><td>Create Strategy</td><td>Create element according to code</td><td>The creation strategy defines if the elements newly added to the code file should be created in the model. If you do not want the new elements to be created after executing the code reverse, choose <strong>Ignore new element from code</strong> strategy.</td></tr><tr class=""><td>Delete Strategy</td><td>Delete element according to code</td><td>The deletion strategy defines if the elements deleted from the code file should also be deleted from the model. If you do not want the elements to be deleted after executing the code reverse, choose <strong>Ignore deleted element from code</strong> strategy.</td></tr><tr class=""><td>Update Strategy</td><td>Update attribute according to code</td><td>The update strategy defines if the attribute changes in the code file should be applied in the model. If you do not want the attribute changes to be applied after executing the code reverse, choose <strong>Ignore attribute changes from code</strong> strategy.</td></tr><tr class=""><td>Define Symbols</td><td>NA</td><td>Define the symbols to be expanded by the preprocessor when parsing files. </td></tr><tr class=""><td>Dry Run</td><td>false</td><td>If this option is set to <em>true</em>, the operation will not modify the model after the execution. It only shows changes in the Software Producer Logs that would be made. </td></tr><tr class=""><td>Include Directories</td><td>NA</td><td>Include directories used by the parser for searching &quot;#include&quot; files.</td></tr><tr class=""><td>Verbose</td><td>false</td><td>If this option is set to <em>true</em>, every model creation, modification, and deletion is logged in the Software Producer Logs.</td></tr><tr class=""><td>Name</td><td>Cpp code reverse element name</td><td>The name of the Cpp code reverse element.</td></tr><tr class=""><td>Target Package</td><td>Target package name</td><td>The elements, created after code reverse execution, will be stored in this package.</td></tr><tr class=""><td>Reverse Local Path</td><td>&lt;sop.local.workspace.path&gt;/&lt;<a href="http://configuration.name">configuration.name</a>&gt;</td><td>Define the path where the C++ source files are stored. By default, the path points to the location where the project is stored.</td></tr></tbody></table><h4 style="margin-left: 40.0px;">Code reverse example</h4><p style="margin-left: 40.0px;">You can find a sample model, Contact Book - Cpp Reverse, located in <em>&lt;installation_directory&gt;\samples\CATIA Software Producer</em>.</p><p style="margin-left: 40.0px;">The files containing the C++ code and used in the sample are located in <em>&lt;installation_directory&gt;\samples\CATIA Software Producer\Contact Book - Cpp Reverse\Contact Book</em>.</p><p style="margin-left: 40.0px;">You can use the files to try out the code reverse functionalities. Try deleting UML elements from the sample project and executing the CppCodeReverse configuration while changing various strategies. Also, try modifying the code files.</p><h3>C++ to UML reverse process</h3><p>The C++ to UML code reverse operation supports C++ files based on the latest C++ version: C++14, C++17, C++20. It does not imply that each new concept of a specific version is supported, but it reading the file should be available. Only header files are analyzed: .h and .hpp.</p><h4>Supported elements</h4><table style="margin-left: 0.0px;"><thead class=""><tr class=""><th style="text-align: left;vertical-align: middle;">Icon</th><th style="text-align: left;vertical-align: middle;">Meaning</th></tr></thead><tbody class=""><tr class=""><td style="text-align: center;"><ac:emoticon ac:name="tick" /> </td><td>Supported / Partially supported.</td></tr><tr class=""><td style="text-align: center;"><ac:emoticon ac:name="cross" /> </td><td>Not supported.</td></tr></tbody></table><table><tbody class=""><tr class=""><th><p>Element</p></th><th><p>Status</p></th><th><p>Description</p></th></tr><tr class=""><th><p>Class</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>A declaration of a class in C++, used to define a custom type with members and methods.</p></td></tr><tr class=""><th><p>Class member function declaration</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>Declaration of a member function inside a class, without its complete definition.</p></td></tr><tr class=""><th><p>Class member function definition</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>The full definition of a member function, including its body, usually outside the class.</p></td></tr><tr class=""><th><p>Class member variable</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>Variable defined within a class, representing an object's state or property.</p></td></tr><tr class=""><th><p>Namespace declaration</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>A declaration of a <strong>namespace</strong> to organize classes and functions under a common name scope.</p></td></tr><tr class=""><th><p>#include preprocessor directive</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="cross" /></p></td><td><p>Preprocessor directive used to include header files or libraries.</p></td></tr><tr class=""><th><p>Class constructor</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>A special function is called when an object is created, used to initialize its members.</p></td></tr><tr class=""><th><p>Class destructor</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>A special function is called when an object is destroyed, used to release resources.</p></td></tr><tr class=""><th><p>Global function declaration</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>Declaration of a function defined outside any class.</p></td></tr><tr class=""><th><p>Global function definition</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>Full definition of a global function, including its body.</p></td></tr><tr class=""><th><p>Alias (typedef &amp; using)</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>Declaration of a type alias using typedef or using to simplify complex types.</p></td></tr><tr class=""><th><p>#define preprocessor directive</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="cross" /></p></td><td><p>Preprocessor directive that defines a macro or symbolic constant.</p></td></tr><tr class=""><th><p>Global variable</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>Variable defined outside of any class or function, accessible globally in the program.</p></td></tr><tr class=""><th><p>Union</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>A special data type that allows storing different types of data in the same memory location.</p></td></tr><tr class=""><th><p>Struct</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>A declaration of a structure in C++, used to group multiple variables under the same type.</p></td></tr><tr class=""><th><p>Enum</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="tick" /></p></td><td><p>Declaration of an enumerated type, used to define a set of named constants.</p></td></tr><tr class=""><th><p>@port</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="cross" /></p></td><td><p>An annotation used to identify that a variable will be translated into a UML Port.</p></td></tr><tr class=""><th><p>@getter:&lt;var&gt;</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="cross" /></p></td><td><p>An annotation used to identify that an operation is a getter of a variable.</p></td></tr><tr class=""><th><p>@setter:&lt;var&gt;</p></th><td style="text-align: center;"><p><ac:emoticon ac:name="cross" /></p></td><td><p>An annotation used to identify that an operation is a setter of a Port.</p></td></tr><tr class=""><th><p>@agregation</p></th><td style="text-align: center;"><p><strong><ac:emoticon ac:name="cross" /></strong></p></td><td><p><span style="color:var(--ds-text,#333333);">Not supported.</span></p></td></tr><tr class=""><th><p>@member</p></th><td style="text-align: center;"><p><strong><ac:emoticon ac:name="cross" /></strong></p></td><td><p><span style="color:var(--ds-text,#333333);">Not supported.</span></p></td></tr><tr class=""><th><p>@association</p></th><td style="text-align: center;"><p><strong><ac:emoticon ac:name="cross" /></strong></p></td><td><p><span style="color:var(--ds-text,#333333);">Not supported.</span></p></td></tr><tr class=""><th><p>@classifierBehavior</p></th><td style="text-align: center;"><p><strong><ac:emoticon ac:name="cross" /></strong></p></td><td><p><span style="color:var(--ds-text,#333333);">Not supported.</span></p></td></tr></tbody></table><p><br /></p><h4>Comment handling</h4><table class="relative-table" style="width: 90.0277%;"><colgroup class=""><col class="" style="width: 14.9034%;" /><col class="" style="width: 85.0966%;" /></colgroup><tbody class=""><tr class=""><th>Function</th><th>Description</th></tr><tr class=""><th><p>@generated_from, @generated_brief,<br /><span>@reverse_ignore</span></p></th><td><div class="content-wrapper"><p>For any element of the code, any comment except lines containing “@generated_from”, “@generated_brief”, and “@reverse_ignore” annotations are expected to be taken into account.</p></div></td></tr><tr class=""><th>Documentation in the model</th><td><div class="content-wrapper"><p>Comments found in the C++ source code will be handled in the UML model. Once processed, the comment will be written in the UML item Documentation/Comments property. Only Doxygen documentation is processed.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2339cdae-480e-47a4-9de6-a8ec512e9ec2"><ac:parameter ac:name="title">Example - The documentation in the Model</ac:parameter><ac:plain-text-body><![CDATA[C++:
class test {
	public:
	/**
	This is 'a' attribute
	It helps to store the value as an int
	and it is public 
	*/
	int a;
}
UML:
[class] test
|-[property]a:int, documentation:” 	This is 'a' attribute
	It helps to store the value as an int
	and it is public 
”]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th>Comment styles</th><td><div class="content-wrapper"><p>Doxygen comments delimiters (/** */, /*! */, ///, //!) are supported.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="39857c8e-5175-40f7-a79f-1497248365e3"><ac:parameter ac:name="title">Example - Comment styles</ac:parameter><ac:plain-text-body><![CDATA[/** block comment */
/*! block comment */
/// one line comment
//! one line comment]]></ac:plain-text-body></ac:structured-macro><p><br /></p></div></td></tr><tr class=""><th>Supported C++ items</th><td><p>Supported C++ items for comments retrieval are <strong>class</strong>, struct, enum, union, typedef, <strong>attribute</strong>, <strong>function</strong>, and <strong>arguments.</strong></p></td></tr><tr class=""><th>Comment mapping</th><td><div class="content-wrapper"><p>Only the last previous comment is taken into account. <span>If there are several comment blocks before an item in C++ code, only the last is taken into account.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="70787206-101b-4d94-9053-5846480d13dd"><ac:parameter ac:name="title"> example - Comment mapping</ac:parameter><ac:plain-text-body><![CDATA[C++:
int myFirstProperty
//comment1
//comment2
/** @brief my comment */
int myProperty;
uml:
[property]myproperty:int, documentation: ”my comment”

]]></ac:plain-text-body></ac:structured-macro><p><br /></p></div></td></tr><tr class=""><th>Doxygen command patterns</th><td><div class="content-wrapper"><p>The supported Doxygen command patterns are @ and \ </p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1b099702-31bb-4811-900c-26ed862de0a1"><ac:parameter ac:name="title">Example - Command patterns</ac:parameter><ac:plain-text-body><![CDATA[C++:
/** @brief documentation*/
int myProperty;
uml:
[property]myproperty:int, documentation: ”documentation”]]></ac:plain-text-body></ac:structured-macro><p><br /></p></div></td></tr><tr class=""><th>Comment with Doxygen syntax handling rules</th><td><div class="content-wrapper"><p>Comments with Doxygen syntax will be handled with the following rules:</p><ul><li data-uuid="92f171c8-d86a-497f-991f-59ec8cc750cf">@param and \param commands will be retrieved, and their value will be set in the argument documentation attribute</li><li data-uuid="93242ff4-46ba-498d-81f0-2a1f70d6bbbe">@brief command will be retrieved</li><li data-uuid="b1b32809-63e6-4707-a14f-6f585df0300b">@return or @returns will be retrieved and its value will be set into the operation documentation of the return argument.</li></ul><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="68d337de-7952-4711-b978-e47a30d30caa"><ac:parameter ac:name="title">Example</ac:parameter><ac:plain-text-body><![CDATA[C++:
/** 
 * @brief documentation of function
 * @param[in] param the first parameter
 * @return the return type
 */
int func(int param);
uml:
+class
|-[operation] func, documentation=”documentation of the funcrtion”
  |-[parameter] int, direction=return, documentation: ”the return type”
  |-[parameter] param:int, direction=in, documentation: ”the first parameter”
]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th>Other commands</th><td><div class="content-wrapper"><p>Other commands (such as @author) will be added to the Item documentation as is.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f636f888-8370-4950-a170-d4569b3c5bb0"><ac:parameter ac:name="title">Example</ac:parameter><ac:plain-text-body><![CDATA[C++:
/** @author someone*/
int myProperty;
uml:
[property]myproperty:int, documentation: ”@author someone”]]></ac:plain-text-body></ac:structured-macro><p><br /></p></div></td></tr><tr class=""><th>@param[in|out|inout]</th><td><div class="content-wrapper"><p>@param[in|out|inout]: direction set by @param command will be taken into account to set direction in the UML argument.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ec4a6ed4-73a4-4c07-b343-82800d986bc7"><ac:plain-text-body><![CDATA[C++:
/** 
 * @brief documentation of function
 * @param[out] param the first parameter
 */
int func(int* param);
uml:
+class
|-[operation] func, documentation=”documentation of the funcrtion”
  |-[parameter] int, direction=return
  |-[parameter] param:int, direction=out, documentation: ”the first parameter”]]></ac:plain-text-body></ac:structured-macro></div></td></tr></tbody></table><p><br /></p><h4>Code reverse behavior specification</h4><p>The behavior of the code reverse depending on the Cpp element is described in the following table.</p><table class="relative-table" style="width: 88.1994%;"><colgroup class=""><col class="" style="width: 15.0221%;" /><col class="" style="width: 40.5409%;" /><col class="" style="width: 44.4379%;" /></colgroup><tbody class=""><tr class=""><th>Function / Element</th><th>Description</th><th>Example</th></tr><tr class=""><th rowspan="4"><p><span>Namespace declaration</span></p></th><td>The inline namespace (Since C++11) is ignored during parsing.</td><td><br /></td></tr><tr class=""><td><p>A package with the stereotype “C++ Namespace” is expected to be created with the name of the namespace for any declared namespace in the code.</p></td><td><br /></td></tr><tr class=""><td>“unique namespace name” attribute of “C++ Namespace” stereotype of the created package will have the name of the namespace.</td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d267b19b-8840-4f4d-aee5-ce132b88809a"><ac:parameter ac:name="title">Namespace declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
namespace ns1
{
  namespace ns2
    …
  {
}
UML:
RootPackage
|-[package]ns1 [[C++ Namespace]]
  |-[package]ns2 [[C++ Namespace]]

]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d2315f16-e479-4a1c-a6d7-865d7c76d8f5"><ac:parameter ac:name="title">Namespace declaration since C++17</ac:parameter><ac:plain-text-body><![CDATA[C++:
namespace ns1::ns2{
  …
}
UML:
RootPackage
|-[package] ns1 [[C++ Namespace]]
  |-[package]ns2 [[C++ Namespace]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><td>If a class is defined in a namespace, the UML class will be created under the package corresponding to the namespace.</td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="83a9862b-60cf-4d93-8273-a40266d173a0"><ac:parameter ac:name="title">Class declaration with namespace</ac:parameter><ac:plain-text-body><![CDATA[C++:
namespace ns1 {
class MyClass{
};
}
UML:
RootPackage
|-ns1[package]
  |-[class]MyClass]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p> Class</p></th><td>A UML class is created for each declared Cpp class.</td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4de03a22-36fc-42aa-940e-88a86b87c88c"><ac:parameter ac:name="title">Class declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
};
UML:
RootPackage
|-[class]MyClass]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th rowspan="2">Inheritance</th><td>If a class inherits from another class, a generalization relation is created from the class to the other class.</td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>The visibility of the inheritance is used in the created generalization relation.</p><p>See: <span><a href="http://www.geeksforgeeks.org/visibility-modes-in-c-with-examples/">www.geeksforgeeks.org/visibility-modes-in-c-with-examples/</a></span></p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="05f0c8e4-9aed-486f-b79c-b26bca8cb1a7"><ac:parameter ac:name="title">Class declaration with generalization</ac:parameter><ac:plain-text-body><![CDATA[C++:
class B {};
class A : public B {
};
UML:
]]></ac:plain-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="Class_declaration_with_generalization.png" /></ac:image></div></td></tr><tr class=""><th rowspan="2">Nested Class</th><td><p>A declaration of a <span><a href="https://en.cppreference.com/w/cpp/language/class">class/struct</a></span> or <span><a href="https://en.cppreference.com/w/cpp/language/union">union</a></span> appearing within another class is known as a nested class. <span><a href="https://en.cppreference.com/w/cpp/language/nested_types">https://en.cppreference.com/w/cpp/language/nested_types</a></span></p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>A UML class will be generated under the parent class for the Cpp nested class.</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><th><p>Abstract Class</p></th><td><p>A Class is abstract when all functions are defined as virtual. See virtual operation. </p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><th rowspan="2">Global functions and variables</th><td>A “global” Class is created without any name and with the “C++ Global” stereotype when code contains functions and variables declared outside any class (global functions and global variables).</td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>The “global” Class is created under the root package.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e317f715-9264-4b21-8207-eafed5349f9b"><ac:plain-text-body><![CDATA[C++ :
void globalFunction();
UML:]]></ac:plain-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="Global_functions_and_variables.png" /></ac:image></div></td></tr><tr class=""><th rowspan="3"><p><br /></p><p>Class constructor</p></th><td><p>An operation with the stereotype “C++ Constructor” will be generated for any constructor declared in the code of the class.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f4da60e4-e21f-4291-999c-b65e19d6fd26"><ac:parameter ac:name="title">Constructor</ac:parameter><ac:plain-text-body><![CDATA[++:
class Door{
  Door();
};
UML :
[class]Door
|-[operation]Door [[C++ Constructor]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><td><p>The Initializer List of a constructor is replicated in the “Initialization list” field of the “C++ Constructor” stereotype applied to the operation.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="20777d0f-5f71-48e2-a29a-15c854d926ef"><ac:parameter ac:name="title">Constructor with Initialization list</ac:parameter><ac:plain-text-body><![CDATA[C++:
class Door{
  const int t;
  Door(int t):t(t){};
};
UML :
[class]Door
|-[operation]Door [[C++ Constructor,Initialization list=t(t)]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><td><p>The “explicit” specifier of a constructor is replicated in the “Explicit” field of the “C++ Constructor” stereotype applied to the operation.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="dfe7d2e4-47b5-4fe9-b34f-a2f2064121dd"><ac:parameter ac:name="title">Constructor with explicit specifier</ac:parameter><ac:plain-text-body><![CDATA[C++:
class Door{
  explicit Door(){};
};
UML :
[class]Door
|-[operation]Door [[C++ Constructor,Explicit=true]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Class destructor</p></th><td><p>An operation with the stereotype “C++ Destructor” will be generated for any destructor declared in the code of the class.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="39780fd8-e38b-44cc-94e6-0d9c628662b8"><ac:plain-text-body><![CDATA[C++:
class Door{
  ~Door();
};
UML :
[class] Door
|-[operation] Door [[C++ Destructor]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th rowspan="5"><p>Variable (Class Member Variable and Global Variable)</p><p><br /></p><p><br /></p><p><br /></p><p><br /></p></th><td><p>A property is generated in the UML class for each member variable of the Cpp class.</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>Properties created from the reverse code analysis will keep the order in which they are read.</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>Visibility of the property is configured according to the declaration in the code for that variable.</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>The type of the variable is used to configure the type of the property.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d5832e68-9d84-4ecc-869a-09a743e9dc59"><ac:parameter ac:name="title">Property</ac:parameter><ac:plain-text-body><![CDATA[C++:
class Door{
private:
  bool isLocked;
};
UML :
[class] Door
|-[property] isLocked:bool, Visibility=private]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><td><p>The default value of the property is a string set as defined in the code.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7e78d4af-40c5-4234-8eeb-57fb2aaa6690"><ac:parameter ac:name="title">Property</ac:parameter><ac:plain-text-body><![CDATA[C++:
enum LockEnum { 
  Open, 
  Closed 
};

class Door{
	LockEnum lockStatus = Closed;
};
UML :
[class] Door
|-[property] lockedStatus:LockEnum,Default value=Closed]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th rowspan="5"><p>Pointer and reference declaration</p><p><br /></p><p><br /></p><p><br /></p><p><br /></p></th><td><p>“Type Modifier” attribute of the property will be set to “*” for a variable declared as a pointer.</p></td><td rowspan="5"><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="dcd80d4c-7c9d-4a0a-85f7-1c6d91b9dc12"><ac:parameter ac:name="title">Pointer and reference</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
	chat *pointerVar;
int &referenceVar;
};
UML :
[class] MyClass
|-[property] pointerVar:char, type modifier=*
|-[property] referenceVar:int, type modifier=&]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><td><p>“Type Modifier” attribute of the property will be set to “&amp;” for a variable declared as a reference.</p></td></tr><tr class=""><td><p>“Type Modifier” attribute of the property will be set to “&amp;&amp;” for a variable declared as a rvalue reference.</p></td></tr><tr class=""><td><p>“Type Modifier” attribute of the property will be set to “**” for a variable declared as a double pointer.</p></td></tr><tr class=""><td><p>“Type Modifier” attribute of the property will be set to “*&amp;” for a variable declared as a reference to a pointer.</p></td></tr><tr class=""><th><p>List &amp; Vector declaration</p></th><td><p>Multiplicity attribute of the property will be set to “*” for a variable declared as a list or a vector.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="bea7c72d-9c7d-4d85-9c9b-7f70bb04ee07"><ac:parameter ac:name="title">List declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
#include <list>
class MyClass{
	std::list<bool> myList;
};
UML:
[class] MyClass
|-[property] myList:bool, multiplicity=*]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="63250bee-32bc-462d-af0c-198047672cc6"><ac:parameter ac:name="title">List declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
#include <vector>
class MyClass{
	std::vector<bool> myVector;
};
UML:
[class] MyClass
|-[property] myVector:bool, multiplicity=*]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Array declaration</p></th><td><p>For a variable declared as an array, the corresponding property will be created with the stereotype “C++ Attributes,” and the “Array” attribute is set with the size of the array.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2b51fa2b-0c78-4074-bc47-a94803a672a3"><ac:parameter ac:name="title">Array declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
#include <array>
class MyClass{
	std::array<int,2> myArray;
};
UML:
[class] MyClass
|-[property] myArray:int [[C++ Attributes:Array=2]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Const</p></th><td><p>For a variable declared as const, the corresponding property will be created with the “Is Read Only” attribute set to true.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="75e4fce4-7068-45f2-8a21-8179945d5857"><ac:parameter ac:name="title">Const declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
	const int myConst;
};
UML:
[class] MyClass
|-[property] myConst:int,”Is Read Only”=true]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Static</p></th><td><p>For a variable declared with the storage class “static”, the corresponding property will be created with “Is Static” attribute set to true.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d3e23527-169c-410c-955d-b1343ce33c10"><ac:parameter ac:name="title">Static declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
	static int myStatic;
};
UML:
[class] MyClass
|-[property] myStatic:int,”Is Static”=true]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Mutable</p></th><td><p>For a variable declared with the storage class “mutable”, the corresponding property will be created with the stereotype “C++ Attributes” and the “Mutable” attribute is set to true.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="6a77e1ba-9b6d-4418-ab37-dbd3532e1839"><ac:parameter ac:name="title">Mutable declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
	mutable int myMutable;
};
UML:
[class] MyClass
|-[property] myMutable:int,”Is Static”=true]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Bit field</p></th><td><p>For a variable declared using a bit field pattern, the corresponding property will be created with the stereotype “C++ Attributes,” and the “Bit Field” attribute is set with the size of the bit field.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="698adc42-d634-4c30-b312-6483c9311810"><ac:parameter ac:name="title">Bitfield declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
	int myVar:20;
};
UML:
[class] MyClass
|-[property] myVar:int [[C++ Attributes:”Bit Field”=20]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Extern</p></th><td><p>For a variable declared with the storage class “extern”, the corresponding property will be created with the stereotype “C++ Extern”.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="15150982-b6ea-414a-b3ed-28eb9dce5095"><ac:plain-text-body><![CDATA[C++:

extern int myExtern;

UML:
[class] 
|-[property] myExtern:int [[C++ Extern]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th rowspan="2"><p>Function Declaration (Class Member Function &amp; Global Function)</p><p><br /></p></th><td><p>An operation is generated in the UML class for each member function of the Cpp class.</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>Visibility of the operation is configured according to the declaration in the code for that variable.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="cd2007bd-4128-4b06-ae27-70c4a427e9bb"><ac:parameter ac:name="title">Function</ac:parameter><ac:plain-text-body><![CDATA[C++:
class Door{
private:
  void lock();
};
UML :
[class] Door
|-[operation] lock:void, Visibility=private]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Virtual</p></th><td><p>For a function declared as virtual, the corresponding operation will be created with the stereotype “C++ Operation,” and the “Virtual” attribute is set to true.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="0fd58cf5-940e-4754-9ac6-1abea66a6272"><ac:plain-text-body><![CDATA[C++:
class Door{
private:
  virtual void lock();
};
UML :
[class] Door
|-[operation] lock:void[[C++ Operation, Inline=true]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Volatile</p></th><td><p>For a function declared as volatile, the corresponding operation will be created with the stereotype “C++ Operation,” and the “Volatile” attribute is set to true.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="448a1281-f955-445b-9c7a-b453d21eea26"><ac:plain-text-body><![CDATA[C++:
class Door{
private:
  void lock() volatile;
};
UML :
[class] Door
|-[operation] lock:void[[C++ Operation, Volatile=true]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Static</p></th><td><p>For a function declared with the storage class “static”, the corresponding operation will be created with the “Is Static” attribute set to true.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="584a63ac-3358-454b-8a2b-1e1eb9b7ee5b"><ac:parameter ac:name="title">Static declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
	static void lock();
};
UML:
[class] MyClass
|-[operation] lock:void,”Is Static”=true]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Const</p></th><td><p>For a function declared as const, the corresponding operation will be created with the “Is Query” attribute set to true.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="20f85843-37d2-4273-b959-b3a63cc733ca"><ac:plain-text-body><![CDATA[C++:
class MyClass{
	void lock() const;
};
UML:
[class] MyClass
|-[operation] lock:void,”Is Query”=true]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Operator</p></th><td><div class="content-wrapper"><p>For a function having the name “operator&lt;overloaded_operator&gt;”, an operation will be created with the C++ Operator” stereotype. &lt;overloaded_operator&gt; can have the following values:</p><p><ac:image><ri:attachment ri:filename="operator_values.png" /></ac:image></p></div></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8f8970d0-ae8f-45cb-994a-894f434ce34b"><ac:plain-text-body><![CDATA[C++:
class MyClass{
	void operator+() const;
};
UML:
[class] MyClass
|-[operation] operator+:void[[C++ Operator]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th rowspan="3"><p> Function Argument</p><p><br /></p><p><br /></p></th><td><p>For a function declaring a returned value, a parameter will be generated with direction set as “return”.</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>For each argument of a function, a parameter will be generated with direction set as “in” or “inout”.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="34b2357e-909e-43c3-aabb-2b9b641ab543"><ac:parameter ac:name="title">Operation with arguments</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
  bool myFct1(int arg);
  bool myFct2(int * arg);
  bool myFct3(const int * arg);
};
UML :
[class] MyClass
|-[operation] myFct1
  |-[parameter] bool, direction=return
  |-[parameter] arg, type=int, direction=in
|-[operation] myFct2
  |-[parameter] bool, direction=return
  |-[parameter] arg, type=int, modifier=*, direction=inout
|-[operation] myFct3
  |-[parameter] bool, direction=return
  |-[parameter] arg, type=int, modifier=*, direction=in]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><td><p>The type of the argument is used to configure the type of the parameter.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f383f357-46c6-4bc3-a228-f56d2591b15d"><ac:parameter ac:name="title">Operation with arguments</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
  bool myFct(int arg);
};
UML :
[class] MyClass
|-[operation] myFct
  |-[parameter] bool, direction=return
  |-[parameter] arg, type=int, direction=in]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th rowspan="2"><p>Pointer and reference declaration</p><p><br /></p></th><td><p>“Type Modifier” attribute of a parameter will be set to “*” for an argument declared as a pointer. </p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>“Type Modifier” attribute of parameter will be set to “&amp;” for an argument declared as a reference. </p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="13c5e345-4a07-4873-9b76-e9f9fad1da43"><ac:parameter ac:name="title">Pointer and reference</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
	void myFct(int *pointer	Arg);
void myFct2(int &referenceArg);
};
UML :
[class] MyClass
|-[operation] myFct:void
  |-[parameter] : type=void, direction=return
  |-[parameter] pointerArg: type=int, direction=inout, type modifier=*
|-[operation] myFct2:void 
  |-[parameter] : type=void, direction=return
  |-[parameter] referencearg:int, direction=inout, type modifier=&]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>List declaration</p></th><td><p>Multiplicity attribute of parameter will be set to “*” for an argument declared as a list.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c3ed76a3-1421-4b5b-9628-de04b0120420"><ac:plain-text-body><![CDATA[C++:
#include <list>
class MyClass{
	void myFct(std::list<bool> myList);
};
UML:
[class] MyClass
|-[operation] myFct:void
  |-[parameter] myList: type=bool, direction=in, multiplicity=*]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Array declaration</p></th><td><p>For an argument declared as an array, the corresponding parameter will be created with the stereotype “C++ Attributes,” and the “Array” attribute is set with the size of the array.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="b8d6ee68-315e-4b8f-b6b5-5e18cbb5a643"><ac:plain-text-body><![CDATA[C++:
#include <array>
class MyClass{
	void myFct(std::array<int,2> myArray);
};
UML:
[class] MyClass
|-[operation] myFct:void
  |-[parameter] myArray: type=int [[C++ Attributes:Array=2]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Const</p></th><td><p>For an argument declared as const, the corresponding parameter will be created with direction set to “in”</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="3df38822-46c8-4ca1-add9-a53e718b346f"><ac:plain-text-body><![CDATA[C++:
class MyClass{
	void myFct(const int myConst);
};
UML:
[class] MyClass
|-[operation] myFct:void
  |-[parameter] myConst: type=int,”direction”=”in”]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Variable length parameter list</p></th><td><p>For a variable length function, the latest parameter will be created with the name “…” without any type</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="dab5b38b-29f5-463c-9f6c-a398cb048c2a"><ac:plain-text-body><![CDATA[C++:
class MyClass{
	void myFct(const int myConst, ...);
};
UML:
[class] MyClass
|-[operation] myFct:void
  |-[parameter] myConst: type=int,”direction”=true
  |-[parameter] …]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p>Function Definition (Class Member Function &amp; Global Function)</p></th><td><p>For the implementation body of a function, an opaque behavior will be generated, the language attribute will be set to “C++”, and the body attribute will be filled with the body of the function. This opaque behavior will be referenced by the operation with the “Method” attribute.  </p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a968d1ed-0ce6-4444-9ec1-dbe1995507ed"><ac:parameter ac:name="title">Operation with behavior</ac:parameter><ac:plain-text-body><![CDATA[C++:
void ClassA::myFct(){
  // This is the implementation of operation
}
UML:
[class] MyClass
|-[opaque behavior] myFctBeh, language=C++, body=“// This is the implementation of operation”
|-[operation] myFct:type=void, method=myFctBeh]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p><span>Standard Data Types</span></p></th><td><div class="content-wrapper"><p>When a model element  (eg, property, parameter) references a type, the reference is mapped to standard types for the following types:</p><p><ac:image><ri:attachment ri:filename="datatypes.png" /></ac:image></p></div></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><th rowspan="2"><p><span> </span><span>Structure</span></p><p><br /></p></th><td><p>A UML class with the stereotype “C++ Struct” will be created for each declared struct.</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>A property will be created for each field of the struct.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="565089b1-3a5b-4c0b-90ee-24f7b901265f"><ac:parameter ac:name="title">Structure definition</ac:parameter><ac:plain-text-body><![CDATA[C++:
struct Struct{
  unsigned int data1;
};
UML: 
[class] Struct [[C++ Struct]]
|-[property]data1:type=C++ ANSI profile::datatypes::unsigned int]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th rowspan="4"><p><span> </span><span>Enumeration</span></p><p><br /></p><p><br /></p><p><br /></p></th><td><p>An enumeration will be generated for an enum in the code.</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>An enumeration literal with the stereotype “<em>C++LiteralValue”</em> will be generated for each field of the enum.</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>A value attribute of “<em>C++LiteralValue”</em> will be configured with the value of the field, if any.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ddf6a619-ba5a-444f-8f64-df0ba8ea2e05"><ac:plain-text-body><![CDATA[C++:
enum ControlEnum{
	Idle,
	Open,
	Close
};
UML: ]]></ac:plain-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="enum_definition.png" /></ac:image></div></td></tr><tr class=""><td><p>Since C++11, an enum can be defined using enum class. Such a pattern will be supported when detecting enums in code.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4cc8aea7-79e0-4f93-8497-a6d4e64391cc"><ac:plain-text-body><![CDATA[C++:
Enum class ControlEnum{
	Idle,
	Open,
	Close
};
UML: ]]></ac:plain-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="enum_definition_with_class.png" /></ac:image></div></td></tr><tr class=""><th rowspan="2"><p><span> </span><span>Union</span></p></th><td><p>A UML class with the stereotype “C++ Union” will be created for each declared union.</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>A property will be created for each field of the union.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="bff42d8b-2289-4b17-bea7-0c775cac5672"><ac:parameter ac:name="title">Union definition</ac:parameter><ac:plain-text-body><![CDATA[C++:
union MyUnion{
  int intVal;
  float realVal;
  char charVal;
};
UML: 
[class] MyUnion [[C++ Union]]
|-[property]data1:type=C++ ANSI profile::datatypes::int
|-[property]data1:type=C++ ANSI profile::datatypes::float
|-[property]data1:type= UML Standard Profile::MagicDraw Profile::datatypes::char ]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p><span> </span><span>Alias (Typedef and Using)</span></p></th><td><p>For an alias to another type (via typedef or using), a Data Type will be generated and a generalization relation will be created between this Data Type and the Data Type source of the alias.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="109bb0f3-4256-4bce-a3a1-9411e7ccc891"><ac:parameter ac:name="title">typedef declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
  typedef int myInt;
};
UML:
[class] MyClass
|-[data type] myInt
  |- [dependency] Target=”UML Standard Profile::MagicDraw Profile::datatypes::int”]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1afe2120-c6df-4798-84c6-866d69ab7c79"><ac:parameter ac:name="title">Using declaration</ac:parameter><ac:plain-text-body><![CDATA[C++:
class MyClass{
  using myInt = unsigned int;
};
UML:
[class] MyClass
|-[data type] myInt
  |- [dependency] Target=” C++ ANSI profile::datatypes::unsigned int”]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p><span> </span><span>typedef of an array</span></p></th><td><p>For an alias to another type (via typedef or using) declaring an array, a Data Type will be generated with the<strong> </strong>“C++ Attributes” and “Array” attribute is set with the size of the array<strong> </strong>and a generalization relation will be created between this Data Type and the Data Type source of alias.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7a7e8c32-fe2d-4a1c-959a-e6b4b67d827b"><ac:plain-text-body><![CDATA[C++:
class MyClass{
	typedef int array[3];
};
UML:
[class] MyClass
|-[data type] array [[C++ Attributes:Array=3]]
  |- [dependency] Target=”UML Standard Profile::MagicDraw Profile::datatypes::int”]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th rowspan="2"><p><span> </span><span>typedef of a struct</span></p><p><span> </span></p></th><td><p>For an alias (via typedef or using) declaring a struct, a class will be generated (same as for a Union).</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>For an alias (via typedef or using) declaring a struct, if the struct is anonymous, the created class will have the name of the alias with the suffix “Struct”.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="17040fd0-4935-4be1-83a2-437ed254cab2"><ac:parameter ac:name="title">Structure definition</ac:parameter><ac:plain-text-body><![CDATA[C++:
typedef struct{
  unsigned int data1;
} MyStructStruct ;
UML: 
[data type] MyStructStruct 
|-[generalization] Target=<>
  |-[class] <> [[C++ Struct]]
    |-[property]data1:type=C++ ANSI profile::datatypes::unsigned int]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th rowspan="2"><p><span> </span><span>typedef of an enum</span></p><p><span> </span></p></th><td><p>For an alias (via typedef or using), declaring an enum, an enumeration will be generated (same as for Enumeration)</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>For an alias (via typedef or using) declaring an enum, if the enum is anonymous, the created enumeration will have the name of the alias with the suffix “Enum”.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="85c5f58f-c3be-47d8-a3f2-087cc3d43d39"><ac:parameter ac:name="title">enum definition</ac:parameter><ac:plain-text-body><![CDATA[C++:
typedef enum {
	Idle,
	Open,
	Close
} Control;
UML: ]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th rowspan="2"><p><span> </span><span>typedef of a union</span></p><p><span> </span></p></th><td><p>For an alias (via typedef or using), declaring a union, a class will be generated (same as for Union)</p></td><td><div class="content-wrapper"><br /></div></td></tr><tr class=""><td><p>For an alias (via typedef or using) declaring a union, if the unionenum is anonymous, the created class will have the name of the alias with the suffix “Union”.</p></td><td><div class="content-wrapper"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e6b80c2a-7b7a-4026-bb85-62bb078445d2"><ac:parameter ac:name="title">Union definition</ac:parameter><ac:plain-text-body><![CDATA[C++:
typedef union {
  int intVal;
  float realVal;
  char charVal;
} MyUnion;
UML:

[data type] MyUnion
|-[generalization] Target=<>
  |-[class] <>[[C++ Union]]
    |-[property]data1:type=C++ ANSI profile::datatypes::int
    |-[property]data1:type=C++ ANSI profile::datatypes::float
    |-[property]data1:type= UML Standard Profile::MagicDraw Profile::datatypes::char ]]></ac:plain-text-body></ac:structured-macro></div></td></tr></tbody></table><h4 style="margin-left: 40.0px;">Limitations</h4><p>In the following table, you can see functionalities that are not yet supported in the code reverse.</p><table style="margin-left: 0.0px;"><thead class=""><tr class=""><th style="text-align: left;vertical-align: middle;">Icon</th><th style="text-align: left;vertical-align: middle;">Meaning</th></tr></thead><tbody class=""><tr class=""><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td>Not yet supported.</td></tr></tbody></table><table class="relative-table" style="width: 96.3435%;"><colgroup class=""><col class="" style="width: 16.3406%;" /><col class="" style="width: 4.71807%;" /><col class="" style="width: 78.9413%;" /></colgroup><tbody class=""><tr class=""><th>Function</th><th>Status</th><th>Description</th></tr><tr class=""><th><p>Friend class</p></th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>If a class is declared a friend to another one, a usage relation with the “C++ Friend” stereotype is expected to be generated.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="44efbc87-7738-4cea-813a-8136e5535fe4"><ac:plain-text-body><![CDATA[C++:
class FriendClass{
	friend class ClassA;
}
UML:]]></ac:plain-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="Friend_relation_between_classes.png" /></ac:image></p></div></td></tr><tr class=""><th rowspan="3"><p> #Include preprocessor directive</p></th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>If a file contains one or multiple class definitions and contains #include directives to other files containing class definitions, a usage relation is created for the corresponding UML classes and the targeted classes with the stereotype “C++ Include”.</p></div></td></tr><tr class=""><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>If the #include directive is declared using &lt;&gt;, the “header include” attribute will be configured with the value “System Include“</p></div></td></tr><tr class=""><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>If the #include directive is declared using “ “, the “header include” attribute will be configured with the value “User Include“</p></div></td></tr><tr class=""><th>Variable supported by an association</th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>If the annotation @association is defined before the declaration of a variable and this variable is a pointer, a directed association relation will be created from the class to the type of the variable, and the role on the target will have the name of the variable.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="64493065-a194-4796-9fab-fa81739050dd"><ac:plain-text-body><![CDATA[Cpp:
class A {
  /* @association */
  B *a;
};
UML:]]></ac:plain-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="variable_supported_by_association.png" /></ac:image></p></div></td></tr><tr class=""><th>Flow Property variable</th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>If the annotation @port:&lt;port_name&gt; is defined before the declaration of a variable, a Property will be generated in an Interface referenced by a Port. A Port and an Interface will be created for each port_name. The &lt;port_name&gt; will be part of the prefix of the variable.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="019eaa19-19ff-4a14-86d3-709ab9964fc5"><ac:plain-text-body><![CDATA[Cpp:
class A {
  /* @port:myPort */
  B myPort_myData;
};
UML:
[class] A
|-[port] myPort:myPortItf
[interface] myItf
|-[property]myData:B]]></ac:plain-text-body></ac:structured-macro><p><br /></p></div></td></tr><tr class=""><th>Function pointer</th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>For a variable declared as a function pointer, the corresponding property will be created with the stereotype “C++ FunctionPtr,” and the signature attribute will be set with the signature definition.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e2f7aeda-15ba-459b-9de0-e621b43bc381"><ac:plain-text-body><![CDATA[C++:
class MyClass{
	void (*fctPtr)();
};
UML:
[class] MyClass
|-[property] fctPtr:void,[[C++ FunctionPtr]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro><p><br /></p></div></td></tr><tr class=""><th>Multiple declarations</th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>For a variable declared with a complex collection of storage classes or declarations, the Type Modifier attribute will be used to register the complete declaration. “$” char replaces the type name.</p><p><strong>const on pointer</strong> <strong>not yet supported: </strong>const int* <strong>const</strong></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="79a83225-9c85-47cc-99dd-500301049ca9"><ac:plain-text-body><![CDATA[C++:
class MyClass{
	const int* myConstPtr;
};
UML:
[class] MyClass
|-[property] myConstPtr:type=int, Type modifier=”const$*”]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th>Friend</th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>For a function declared as a friend in a class, a usage relation with the “C++ Friend”  stereotype is created between the operation in the class declaring it and the current class.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="39388129-6c16-4a3f-94b1-ccc91e93956b"><ac:plain-text-body><![CDATA[C++:
class ClassC{
	friend void ClassD::func(Integer myParam);
};
UML:]]></ac:plain-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="friend_function.png" /></ac:image></p></div></td></tr><tr class=""><th rowspan="4">Exception</th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>For a function declared with the suffix noexcept  (since C++11), the corresponding operation will be created with the stereotype “C++ Operation” and the “Throw exception” attribute is set to “none”.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d6291c3c-7ec1-4c0d-b3d2-8277fe0a1e3b"><ac:plain-text-body><![CDATA[C++:
class MyClass{
	void myOp() noexcept;
};
UML:
[class] MyClass
|-[operation] myOp:void[[C++ Operation, Throw exception=none]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td>For a function declared with the suffix noexcept (&lt;condition&gt;) (since C++11), the corresponding operation will be created with the stereotype “C++ Operation”, and the “Throw exception” attribute is set to “none”, and the condition will be configured somewhere.</td></tr><tr class=""><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>For a function declaring an exception without any argument (C++98 and C++03 only), the corresponding operation will be created with the stereotype “C++ Operation” and the “Throw exception” attribute is set to “any”.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="982b66d7-f5bb-4578-88aa-ed544c5d77e2"><ac:plain-text-body><![CDATA[C++:
class MyClass{
	void myOp() throw();
};
UML:
[class] MyClass
|-[operation] operator+:void[[C++ Operation, Throw exception=any]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro><p><br /></p></div></td></tr><tr class=""><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>For a function declaring an exception with arguments (C++98 and C++03 only), the corresponding operation will be created with the stereotype “C++ Operation”, “Throw exception” attribute is set to “any”, and “Raised exception” attribute is set with the value of the exception arguments.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="3c907e0d-7851-40f9-b0f6-2eb07b58ad6e"><ac:plain-text-body><![CDATA[C++:
class MyClass{
	void myOp() throw(std::exception);
};
UML:
[class] MyClass
|-[operation] operator+:void[[C++ Operation, Throw exception=any, Raised exception=std::exception]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th>@getter</th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><p>For a function having annotation @getter before its declaration, the corresponding operation will be created with the stereotype “getter”, and “getter/setter for attribute” will be configured with the corresponding property. </p></td></tr><tr class=""><th>@setter</th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>For a function having annotation @setter before its declaration, the corresponding operation will be created with the stereotype “getter” and “getter/setter for attribute” will be configured with the corresponding property. </p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5e95c569-5666-4b6d-b46c-8b08b985b566"><ac:plain-text-body><![CDATA[Cpp:
class Door {
  ControlEnum WindowPosition;

  /* @setter:WindowPosition */
  void setWindowPosition(ControlEnum /*in*/ windowPosition);
		
  /* @getter:WindowPosition */
  ControlEnum getWindowPosition();
};

UML:]]></ac:plain-text-body></ac:structured-macro><p><strong><ac:image><ri:attachment ri:filename="example_getter_setter.png" /></ac:image></strong></p></div></td></tr><tr class=""><th>“C++ Parameter” and “volatile” attribute set to “true”</th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><div class="content-wrapper"><p>For a return type declared with the modifier volatile, the corresponding return parameter will be created with the stereotype “C++ Parameter” and “volatile” attribute set to “true” </p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="aba31711-a216-4602-9d35-f77ff2e798f2"><ac:plain-text-body><![CDATA[C++:
class MyClass{
	volatile int method();
};
UML:
[class] MyClass
|-[operation] method
  |-[parameter]int, direction=return [[C++ Parameter:”volatile”=true]]]]><![CDATA[]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr class=""><th><p> #define preprocessor directive</p></th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td><p>A macro can be defined via a property with Is Read Only=true, but the C++ profile needs to be extended with a new stereotype “C++ Macro” to distinguish it from a regular const.</p><p>Another alternative is to use the notes to attach a const to a Class.</p></td></tr><tr class=""><th><p> Templates</p></th><td style="text-align: center;"><ac:emoticon ac:name="cross" /></td><td>Not supported.</td></tr></tbody></table><h2>Software Governance</h2><p style="text-align: left;"><span>To commit elements from the modeling tool, you need to:</span></p><ul style="text-align: left;"><li data-uuid="514fa8e9-81d4-4405-a1cc-533297dc2c81">Associate a SCM repository to the model element<ul><li>Using Connected Software Connectors</li><li>With a local configuration</li></ul></li><li data-uuid="da8a852a-79c6-45d6-b275-5bf54b003d17">Create an SCM Configuration element</li><li data-uuid="e43c8c5d-0e7d-498c-9df7-94fa457763b0">Configure an SCM branch<ul><li>Using Software Logical Items of Connected Software </li><li>With a local configuration</li></ul></li></ul><h3 style="text-align: left;">SCM Repository association</h3><h4 style="text-align: left;">Associating repository using Connected Software Connectors</h4><p style="text-align: left;">To associate the SCM repository</p><hr /><ol><li data-uuid="5991c684-0636-4ce0-a1ce-9da3d21913f3">In the Containment tree, right-click Model.</li><li data-uuid="e6a1cebe-61fe-4f6f-b1da-fa25f887cbf3">In the shortcut menu, click <strong>Software Code Generation</strong> &gt; <strong>Associate SCM Repository</strong>.</li><li data-uuid="54231802-b0ed-4d7b-8660-0c1254bd9735">In the open <strong>Associate SCM Repository</strong> dialog, choose the needed repository,</li><li data-uuid="3d0ec60d-1693-40e7-bb26-0f7d8163bfae">Click <strong>OK</strong>.</li></ol><p style="text-align: left;"><span class="image-wrap"><ac:image><ri:attachment ri:filename="image-2024-05-07-15-31-16-554.png" /></ac:image></span><span class="image-wrap"><ac:image><ri:attachment ri:filename="image-2024-05-07-16-22-46-874.png" /></ac:image></span></p><p style="text-align: left;">After you click <strong>OK</strong> in the <strong>Associate SCM Repository</strong> dialog, the repository information will be associated to the model via the «Connector» stereotype from the Embedded Software Profile:</p><ul style="text-align: left;"><li data-uuid="3d8bba96-491c-4bd0-a3e7-6bedd1311b8d">repositoryHost: root url of the targeted Git server (ex: :<span> </span><a class="external-link" href="https://gitlab.com)/" title="Follow link">https://gitlab.com)</a></li><li data-uuid="8c634ddc-6810-462c-9900-1c0dcc81b96d">repositoryPath: relative path of the repository (ex: SJA/cubesat-control)</li><li data-uuid="1aa7fe8d-d65f-4092-a80f-2ce3281a12d7">repositoryToken: associate the access token to the repository (example: glpat-6_y_4y8hMDNDxWyaATi4)</li></ul><p style="text-align: left;"><br /></p><p style="text-align: left;">To remove the association of the SCM repository</p><hr /><ol><li data-uuid="f7a82dc3-585e-4034-9379-41fcfe208388">In the Containment tree, right-click Model.</li><li data-uuid="d047a427-167c-47a3-8bcd-4a193d0c83eb">In the shortcut menu, click <strong>Software Code Generation</strong> &gt; <strong>Associate SCM Repository</strong>.</li><li data-uuid="d8b49622-3243-4fa7-adfe-112503dd87c4">In the open <strong>Associate SCM Repository</strong> dialog, click the selected repository for which you want to remove the association.</li><li data-uuid="3c66c9f3-155b-4cf3-8efa-e42d23872cd1">Click <strong>OK</strong>.</li></ol><p style="text-align: left;">When you click <strong>OK</strong>, the association will be removed and the branches will be detached from elements if there were any. </p><h4 style="text-align: left;">Local Configuration</h4><p style="text-align: left;">If Connected Software is not used, it is still possible to attach a repository to the model element.</p><p style="text-align: left;">To do so, associate the «Connector» stereotype from Embedded Software Profile to the model element and configure it as following:</p><ul style="text-align: left;"><li data-uuid="8a7c1c5e-cf48-47fd-a373-d104c4c4290a">repositoryHost: root url of the targeted Git server (ex: :<span> </span><a class="external-link" href="https://gitlab.com)/" title="Follow link">https://gitlab.com)</a></li><li data-uuid="354e1830-6e8d-4158-879a-76424434acb5">repositoryPath: relative path of the repository (ex: SJA/cubesat-control)</li><li data-uuid="3bf82ad3-a7d1-4090-8bdb-211b754dc904">repositoryToken: associate the access token to the repository (example: glpat-6_y_4y8hMDNDxWyaATi4)</li></ul><h3 style="text-align: left;">SCM Configuration creation</h3><p style="text-align: left;">It is necessary to associate a repository before attaching a branch from the configuration dialog.</p><p style="text-align: left;">From the diagram palette, the you can create a SCM Configuration that will contain <span>a reminder of the repository path of the model: you cannot edit the repository here. If you need to change the repository, see </span><ac:link ac:anchor="SCM Repository association" /><span>.</span></p><p style="text-align: left;"><span><ac:image><ri:attachment ri:filename="scm_cofig_creation.png" /></ac:image></span></p><p style="text-align: left;">To use the SCM Configuration, you have to drag and drop the SCM configuration on the code configuration or application configuration that you wants to execute and commit:</p><p style="text-align: left;"><span class="image-wrap"><ac:image><ri:attachment ri:filename="image-2024-05-07-16-37-27-308.png" /></ac:image></span></p><h3 style="text-align: left;">SCM Branch Configuration</h3><p style="text-align: left;">This is the branch to which you are going to commit the code.</p><p style="text-align: left;">It is necessary to associate a repository before attaching a branch from the configuration dialog.</p><h4 style="text-align: left;">With Software Logical Items of Connected Software</h4><ul><li data-uuid="05006dd8-dd9b-42ff-93fa-498b512c5339"><span>you can edit the branch in the <strong>Specification </strong>window by clicking the three dots in the branch value field:</span></li></ul><p style="margin-left: 40.0px;text-align: left;"><span> <ac:image><ri:attachment ri:filename="image-2024-05-07-16-29-11-710.png" /></ac:image><br /></span><ac:image><ri:attachment ri:filename="image-2024-05-07-16-33-07-936.png" /></ac:image></p><ul><li data-uuid="386cb46f-9773-436c-8582-35c65ad373da">When you click <strong>OK </strong>in the <strong>Associate Branch of Repository</strong> dialog, the branch information will be associated to the configuration via the «SoftwareLogicalItem» stereotype from Embedded Software Profile:</li></ul><ul><li style="list-style-type: none;" data-uuid="c78c5d2a-5ee2-4c50-ac63-24d914c28afd"><ul><li style="list-style-type: none;"><ul><li>branchName: the branch name to target (example: “main”)</li><li>SoftwareLogicalItemId: ID of the logical Item linked to the branch (from Connected Software)</li></ul></li></ul></li></ul><p><span>If if you remove the repository association, the branches will also be detached from elements if there were any. See </span><ac:link ac:anchor="SCM Repository association" /><span>.</span></p><h4 style="text-align: left;">Local Configuration</h4><p style="text-align: left;">The you can edit it in the branch:</p><ul style="text-align: left;"><li data-uuid="dbcf44cf-f88a-4acf-914d-36e698a1865e">branchName: the branch name to target (example: “main”)</li></ul><h3 style="text-align: left;">Code persistency</h3><p style="text-align: left;">Code generation is executed via the regular mechanism.</p><p style="text-align: left;"><br /></p><p style="text-align: left;">The code will be committed after a successful execution of code generation.</p><p style="text-align: left;"><ac:image><ri:attachment ri:filename="persistency.png" /></ac:image></p><p style="text-align: left;">At execution phase, mandatory parameters are checked, if they are not present or are invalid, the operation is canceled and a message is printed (see an example below).</p><p style="text-align: left;"><ac:image><ri:attachment ri:filename="log.png" /></ac:image></p><p style="text-align: left;">The mandatory parameters are:       </p><ul style="text-align: left;"><li data-uuid="acb3c6b7-4249-4f7c-a62c-1cffb6750c58">the repository path: must be present</li><li data-uuid="a7cc02a5-c0ae-46ee-a26b-b2cc89e16df3">the repository token: must be present</li><li data-uuid="d3e83e60-1e7c-4736-91b1-a8f35ae5fe69">the repository host: must be present and must reference a valid URL (syntax check only)</li><li data-uuid="79b2b18c-9851-4387-b3f0-3b22543cf891">the commit message: must be present</li><li data-uuid="459a6536-84fb-4916-9f24-e9a7c8fe673c">the commit author: must be present</li><li data-uuid="c25239b5-709a-4341-902e-f7e793ab814a">the branch name: must be present</li></ul><h2>Local workspace of the software producer</h2><p>Under the local workspace, you can find the generated files, if you have selected the download option and left the default location (as seen above) in the configurations. You can also find some other files under an “etc” folder:</p><ul><li data-uuid="7c46e988-b118-4a0a-b8c9-f74fb6f56ba9">&lt;Local_workspace_path&gt;</li></ul><ul><ul><li data-uuid="de6f9225-5485-4436-838f-34663236ad27">&lt;configuration1_name&gt;</li><li data-uuid="74047f9a-379d-4f87-b7fa-ba727b79890b">&lt;configuration2_name&gt;</li><li data-uuid="d64c63a4-b771-4be6-88b6-58a85c1fa63a">etc<ul><li>json<sup>3</sup></li></ul><ul><li>log<sup>4</sup></li></ul></li><ul><li data-uuid="ff0e0804-3a1b-46c4-b6dd-a649be46602c">operations</li><li data-uuid="a866e813-02ec-46bf-9952-20f9e9121b3c">backup<sup>2</sup></li><li data-uuid="950160b5-c434-4172-819f-2c06c48b005c">logs</li></ul></ul></ul><hr /><p><sup>1</sup>You can change the root of the local workspace path in the project options.</p><p><sup>2</sup>By default, a backup of your downloaded files is saved in this folder so that in case something wrong happens with the download of new files, you can still reach your previous files. You can disable this option in the <strong>Project Options </strong></p><p><sup>3</sup>SPO Report files are rotated by size and date so that you might see multiple report files here.</p><p><sup>4</sup>Log files are rotated by size and date so that you might see multiple log files here.</p><h2><span>Views</span></h2><h3>Files tab</h3><p><span>The </span><strong>Files </strong><span>tab lists the existing configurations in the model and displays as children the files contained in the directory referenced by the configuration. </span><span>This behavior is available for the code generation configuration and the reverse code configurations.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5a72eb52-1201-4ad6-b562-01ef106135aa"><ac:rich-text-body><p>Configurations are greyed if they have no content (no files yet).</p></ac:rich-text-body></ac:structured-macro><p><br /><ac:image><ri:attachment ri:filename="files_tab.png" /></ac:image></p><p><span>In the <strong>Files </strong>tab, double-click a file to see its content in a </span><ac:link ac:anchor="Code viewer"><ac:plain-text-link-body><![CDATA[code viewer]]></ac:plain-text-link-body></ac:link><span>. </span></p><p>You can select any file in the <strong>Files </strong>tab, and open the Specification of an element that was used to generate the file, or navigate to that element in the Containment tree. Right-click the file and from the shortcut menu, choose <strong>Select in Containment Tree</strong>. If there is more than one element in the file, you will be offered to choose the needed element.</p><p><ac:image ac:width="477"><ri:attachment ri:filename="select_in_containment_from_file_tab.png" /></ac:image></p><p>You can activate the filter mode in the <strong>File</strong> tab to display the files impacted by the element which you select in the Containent tree.</p><p><br /></p><p>To display files related with the selected element</p><hr /><ul><li data-uuid="f0b5831a-2952-441a-aa5c-57a015273e5a">In the <strong>Files </strong>tab toolbar, click<strong> Filter on Selection</strong>.</li></ul><p><ac:image><ri:attachment ri:filename="filter_mode.png" /></ac:image></p><p><br /></p><p>From the <strong>Files </strong>tab, <span>you can open the generated files</span><span> </span>in the default editor configured for that file type on your machine. If no default application is associated with the file type, you will be prompted to choose one<span>.</span></p><p><ac:image><ri:attachment ri:filename="open_in_default_editor.png" /></ac:image></p><h3>Code viewer</h3><p>The code viewer opens when you double click a file in the <strong>Files </strong>tab. The code viewer is read-only.</p><p><span>In the open code viewer, you can see the highlighted markers where the selected element is used in the file.</span></p><p><br /></p><p><span>To view the markers</span></p><hr /><ol><li data-uuid="a1d608ed-8f52-483b-86ff-e3f095c986cf">In the <strong>Files</strong> tab, right-click the needed file.</li><li data-uuid="f4805d37-fa25-4461-bec3-beef2112f912">In the shortcut menu, click <strong>Select in Containment Tree</strong>.</li></ol><p><ac:image><ri:attachment ri:filename="markers_in_code.png" /></ac:image></p><p>You can also navigate from the code viewer to the element in the <strong>Containment </strong>tree from which the code was generated.</p><p><br /></p><p>To navigate to the element in the <strong>Containment </strong>tree</p><hr /><ol><li data-uuid="272e4bf6-e2e4-4f99-b28f-1bf326b84615"><p>In the open code viewer, hover over the id near the <em>@generated_from</em>.</p></li><li data-uuid="6976a8df-ed6d-46dd-9905-50d39c176afe">In the displayed tooltip, click the element name.</li></ol><p><ac:image><ri:attachment ri:filename="navigate_from_code_viewer.png" /></ac:image></p><h3>Software Producer Logs</h3><p>In the Software Producer Log panel, you can see the messages of the running SPO.</p><p><ac:image><ri:attachment ri:filename="software_producer_logs.png" /></ac:image></p><p style="text-align: left;">In the following table, the <span style="color:var(--ds-text,#172b4d);">actions to enhance the navigation in this window are explained:</span></p><table><colgroup class=""><col class="" /><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><th>Icon</th><th>Name</th><th>Description</th></tr><tr class=""><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="scroll_start.png" /></ac:image></p></div></td><td><p>Scroll to the Start</p></td><td>Scrolls to the tip of the panel.</td></tr><tr class=""><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="scroll_end.png" /></ac:image></p></div></td><td>Scroll to the End</td><td>Scrolls to the bottom of the panel.</td></tr><tr class=""><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="lock_position.png" /></ac:image></p></div></td><td>Lock Position</td><td>By default, when some new logs are printed, the scrollbar goes down. If the user wants to prevent the panel to be scrolled automatically to the bottom, he can click on this button.</td></tr><tr class=""><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="clear.png" /></ac:image></p></div></td><td>Clear</td><td>Clears the panel.</td></tr><tr class=""><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="show_log_file.png" /></ac:image></p></div></td><td>Show Log File</td><td>Opens the file where the logs are written (each project has its own log file).</td></tr><tr class=""><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="19"><ri:attachment ri:filename="show_timestamp.png" /></ac:image></p></div></td><td>Show Timestamp</td><td>Adds a timestamp as a prefix to the messages.</td></tr><tr class=""><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="additional_messages.png" /></ac:image></p></div></td><td>Show Additional Messages</td><td>Shows more messages related to the SOP client.</td></tr><tr class=""><td><br /></td><td>Level combo box</td><td>Shows the messages of the selected level, hide the others. By default, <strong>All levels </strong>is selected to display all types of messages. Other available types are: Info, Error, Warning.</td></tr><tr class=""><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="search.png" /></ac:image></p></div></td><td>Find</td><td>Highlights the search results and navigate to them</td></tr></tbody></table><p><span>A log file for general Software Producer messages not related to a specific project is stored next to the modeling tool log file.</span></p><p>At the bottom right corner of the modeling tool, in the progress bar, you can see whether the generation is running. After the generation is completed, the notification is displayed in case of failure or always if the verbose mode is activated (<span><strong>Environment Options </strong>&gt; <strong>CATIA Software Producer Client General Properties</strong> &gt; <strong>Notifications</strong> section</span>).</p><h3>Validation Results</h3><p>When an operation produces a report, the plugin reads it and opens it in a <strong>Validation Result</strong> window if any element has a diagnostic associated.</p><p><ac:image><ri:attachment ri:filename="validation_results_window.png" /></ac:image></p><p>A diagnostic is associated with a rule consisting of a severity, message, and source.</p><p>You can navigate to the source in the Containment tree.  If you need to show more details concerning the rule or open the full report, right-click the appropriate lines of the table.</p><p>You can turn off the <strong>Validation Results</strong> window's opening after the operation produces a report.</p><p><br /></p><p>To turn the validation report off</p><hr /><ol><li data-uuid="69ad2647-4d0d-4c08-b414-7f338a585524">In the modeling tool main menu, click <strong>Options </strong>and select <strong>Project</strong>.</li><li data-uuid="38ad40a1-cd0c-48c4-96a5-6587a1df4479"><span>Set the <strong>Show Validation Report </strong>property to <em>false</em>.</span></li></ol><p><br /></p><p>When you execute a configuration, before calling the operation the plugin checks the UML Completeness Constraints. If a mandatory property is missing (“elements” in the example below), a validation warning and a notification will be displayed informing which tag value(s) are missing.</p><p><ac:image><ri:attachment ri:filename="validation_results_missing_properties.png" /></ac:image></p><h3>Diagrams and Containment tree</h3><p>The following commands are available from the diagrams toolbar or from the shortcut menu of the supported elements in the Containment tree:</p><table class="relative-table" style="width: 64.2105%;"><colgroup class=""><col class="" style="width: 26.6803%;" /><col class="" style="width: 73.3197%;" /></colgroup><tbody class=""><tr class=""><th><p><strong>Button</strong></p></th><th><p><strong>Description</strong></p></th></tr><tr class=""><th><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="see_in_file.png" /></ac:image>Show in File Explorer</p></div></th><td><p>Open a location in your file system wherein the Software Production Operation results file is stored.</p></td></tr><tr class=""><th><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="execute_selected_configuration.png" /></ac:image> Execute Selected Configuration</p></div></th><td><div class="content-wrapper"><p>Runs the code generation for the selected configuration.</p></div></td></tr></tbody></table><h2>Code Generation Result Table</h2><p><span style="color:var(--ds-text,#172b4d);">When the option &quot;storeExecutionSummaryInModel&quot; is set to true in the configuration, the results of the execution of the configuration is saved as an object under the configuration inside the model.</span></p><p><span style="color:var(--ds-text,#172b4d);"><ac:image><ri:attachment ri:filename="store_execution_option.png" /></ac:image></span></p><p style="text-align: left;">You can have an overview of all of these execution objects in the <strong>Code Generation Result Table</strong>.</p><p style="text-align: left;"><br /></p><p style="text-align: left;">To create a table</p><hr /><ol><li data-uuid="78077737-ddd9-477a-83e3-6114e28d07eb">In the Containment tree, right-click a package.</li><li data-uuid="4997087b-4606-4f97-b794-d394acb949b6">From the shortcut menu, select <strong>Create Diagram</strong>.</li><li data-uuid="82f48a22-87b0-4474-84c8-724e02079fa5">Search for <strong>Code Generation Result Table</strong> and click it.</li></ol><p style="text-align: left;"><ac:image><ri:attachment ri:filename="create_code_generation_result_table.png" /></ac:image></p><p style="text-align: left;"><ac:image ac:width="1559"><ri:attachment ri:filename="image-2024-08-23-12-51-12-576.png" /></ac:image></p><p style="text-align: left;">In the Containment tree on the above image, you can see under the configurations that new objects were created:</p><ul style="text-align: left;"><li data-uuid="a9f9caa4-5bed-440a-a5b2-09ee65bb1b84">Configuration Execution: for example, &quot;fmu&quot; execution at 2024-08-23T12:47:14.008&quot;</li><li data-uuid="dc0b19fe-5992-4281-8566-b7dedebaac16">Operation Instance: for example, &quot;FMU Middleware Generation&quot;</li></ul><p style="text-align: left;">Those objects are displayed in the <strong>Code Generation Result Table</strong>. Among other information you can see the duration of each operation and the total duration on the execution, same as for the status.</p><p style="text-align: left;">If you click the Open Logs in the Logs column,  you will see the logs of the selected operation.</p><p style="text-align: left;"><ac:image><ri:attachment ri:filename="logs_of_operations.png" /></ac:image></p><p>If you click the location in the Local Result Path column, your file explorer is opened at the specified location.</p><h2>Options</h2><h3>Project Options</h3><p>You can specify <strong>Project Options</strong> for the CATIA Software Producer Client.</p><p><ac:image><ri:attachment ri:filename="project_options.png" /></ac:image></p><table class="relative-table" style="width: 91.0249%;"><colgroup class=""><col class="" style="width: 12.362%;" /><col class="" style="width: 19.1215%;" /><col class="" style="width: 68.5165%;" /></colgroup><tbody class=""><tr class=""><th>Option name</th><th>Default value</th><th>Description</th></tr><tr class=""><td>Workspace path</td><td>&lt;project_directory&gt;\&lt;project_name&gt;</td><td>Local workspace path for this project. Bu default, it is next to the project file, and named after it. It is used by default in the local path property of the configurations, represented by the variable &lt;sop.lokal.worspace.path&gt;.</td></tr><tr class=""><td>Backup property</td><td>true</td><td>If set to true, then before each generation, the code will be backed-up in the etc/backup folder of the local workspace.</td></tr><tr class=""><td>Show validation report</td><td>true</td><td>If set to true, then each time a report will be generated by an operation, the Validation Results Window will be displayed.</td></tr></tbody></table><h3>Environment Options</h3><p>You can specify <strong>Environment Options</strong> for the CATIA Software Producer Client and CATIA Software Producer Client General Properties.</p><p>A workspace is automatically created on our cloud servers for each of your projects using the widget. This workspace gathers the assets needed for the generation. A cloud workspace is automatically deleted after 30 days of inactivity. You can also delete it manually in the<strong> Environment Options </strong>dialog. If you delete the workspace, all the components will have to be regenerated on the cloud on your next session because you will not be able to push any files to a workspace through the plugin.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0f7e6bff-74fa-4c74-a896-532c9a7600a1"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">To monitor the CATIA Software Producer Client workspaces, you must login to the platform first.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:image><ri:attachment ri:filename="SOP_environment_options.png" /></ac:image></p><table><colgroup class=""><col class="" /><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><th>Option name</th><th>Default value</th><th>Description</th></tr><tr class=""><td>Enable Software Governance</td><td>true</td><td>Enable Software Governance to manage generated code in SCM repositories. </td></tr><tr class=""><td>Activate Smart Launch Mode</td><td>false</td><td>Activate Smart Launch Mode to execute the operations only when a change is detected.</td></tr><tr class=""><td>Activate Verbose Mode</td><td>false</td><td>Activate Verbose Mode to get more notifications during the generation process,</td></tr><tr class=""><td>Show next time the question to clean lock files</td><td>true</td><td>If set to false, deletion of local files previously generated by the configuration will be done (in the clean and full generated mode) without asking for it in a dialog to the user. </td></tr></tbody></table><h2>Additional Information</h2><p><span>You can switch projects (or even shut down your computer, saving your work first) while waiting for the generation result as it is running on the cloud and as the widget keeps the IDs of the cloud assets in the record files located in &lt;local workspace path&gt;\etc\operations\spoRecordFile.json (you will have access to it if you need it, for example, for the debugging purpose). When you come back, another dialog will tell you that operations were running while you were away and will propose you inspect the result and download it.</span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Sample models</strong></p><p>The following sample models are available in <em>&lt;modeling tool instalation directory&gt;\samples\CATIA Software Producer\</em></p><ul><li data-uuid="5f454418-bcb4-422a-8f00-fb6532c3630d"><em>SysML Flashlight Tempo.mdzip</em></li><li data-uuid="9c57eba3-538a-417d-9283-b63233bb6ca3"><em>UML Lock Manager.mdzip</em></li><li data-uuid="4bc0772f-c204-4c96-957d-98d0278f9dac"><em>Contact Book - Cpp Reverse.mdzip</em></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````
