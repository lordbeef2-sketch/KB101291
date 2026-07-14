# NI OSS SOURCE SNAPSHOT: systemlink-OpenAPI-documents

<!--NI_OSS_SNAPSHOT repo=ni/systemlink-OpenAPI-documents commit=c99cb7610a1d7e4ebe9fa6a4f979d3b10308a8ff -->

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=test-monitor/SLE/nitestmonitor-v2.yml sha256=64bbc925cddc367b359186dc1b320d3d23731625062a347a41510ef8e819c5aa bytes=89258 -->
## FILE: test-monitor/SLE/nitestmonitor-v2.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `test-monitor/SLE/nitestmonitor-v2.yml`
- sha256: `64bbc925cddc367b359186dc1b320d3d23731625062a347a41510ef8e819c5aa`
- bytes: 89258

````yaml
swagger: '2.0'
info:
  version: '2'
  title: Test Monitor Web Service
  description: Test Monitor HTTP API
  contact:
    name: NI
    url: 'https://www.ni.com/systemlink'
    email: support@ni.com
basePath: /nitestmonitor
consumes:
  - application/json
produces:
  - application/json
securityDefinitions:
  apiKeyAuth:
    type: apiKey
    name: x-ni-api-key
    in: header
security:
  - apiKeyAuth: []
x-ni-routing-key: Skyline.TestMonitor
definitions:
  Error:
    description: Contains error information
    type: object
    properties:
      name:
        description: String error code
        type: string
      code:
        description: Numeric error code
        type: integer
        format: int32
      resourceType:
        description: Type of resource associated with the error
        type: string
      resourceId:
        description: Identifier of the resource associated with the error
        type: string
      message:
        description: Complete error message
        type: string
      args:
        description: Positional argument values for the error code
        type: array
        items:
          type: string
      innerErrors:
        type: array
        items:
          $ref: '#/definitions/Error'
    example:
      name: TestMonitorErrorCodes.OneOrMoreErrorsOccurred
      code: -252921
      message: >-
        One or more errors occurred. See the contained list for details of each
        error.
      args: []
      innerErrors:
        - name: TestMonitor.InvalidId
          code: -253700
          resourceType: TestResult
          resourceId: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
          message: Invalid Id.
          args: []
  Operation:
    description: Operation provided by the API
    type: object
    properties:
      available:
        type: boolean
        description: Whether the operation is available to the caller
      version:
        type: integer
        format: int32
        description: Version of the available operation
    required: [available]
    example:
      available: true
      version: 1
  V1Operations:
    title: V1 Operations
    description: V1 operations
    type: object
    properties:
      operations:
        description: Available operations in the v1 version of the API.
        type: object
        properties:
          getResults:
            $ref: '#/definitions/Operation'
          queryResults:
            $ref: '#/definitions/Operation'
          createResults:
            $ref: '#/definitions/Operation'
          updateResults:
            $ref: '#/definitions/Operation'
          deleteResult:
            $ref: '#/definitions/Operation'
          deleteManyResults:
            $ref: '#/definitions/Operation'
          getSteps:
            $ref: '#/definitions/Operation'
          querySteps:
            $ref: '#/definitions/Operation'
          createSteps:
            $ref: '#/definitions/Operation'
          updateSteps:
            $ref: '#/definitions/Operation'
          deleteStep:
            $ref: '#/definitions/Operation'
          deleteManySteps:
            $ref: '#/definitions/Operation'
  V2Operations:
    title: V2 Operations
    description: V2 operations
    type: object
    properties:
      operations:
        description: Available operations in the v2 version of the API.
        type: object
        properties:
          getResults:
            $ref: '#/definitions/Operation'
          getResultsPropertyKeys:
            $ref: '#/definitions/Operation'
          queryResults:
            $ref: '#/definitions/Operation'
          createResults:
            $ref: '#/definitions/Operation'
          updateResults:
            $ref: '#/definitions/Operation'
          deleteResult:
            $ref: '#/definitions/Operation'
          deleteManyResults:
            $ref: '#/definitions/Operation'
          getSteps:
            $ref: '#/definitions/Operation'
          querySteps:
            $ref: '#/definitions/Operation'
          createSteps:
            $ref: '#/definitions/Operation'
          updateSteps:
            $ref: '#/definitions/Operation'
          deleteStep:
            $ref: '#/definitions/Operation'
          deleteManySteps:
            $ref: '#/definitions/Operation'
          getProducts:
            $ref: '#/definitions/Operation'
          queryProducts:
            $ref: '#/definitions/Operation'
          createProducts:
            $ref: '#/definitions/Operation'
          updateProducts:
            $ref: '#/definitions/Operation'
          deleteProducts:
            $ref: '#/definitions/Operation'
          deleteManyProducts:
            $ref: '#/definitions/Operation'
          queryPaths:
            $ref: '#/definitions/Operation'
  StatusObject:
    title: Status Object
    description: Status object comprised of a type and display name
    type: object
    required:
      - statusType
    properties:
      statusType:
        description: Status type enum
        type: string
        enum:
          - LOOPING
          - SKIPPED
          - CUSTOM
          - DONE
          - PASSED
          - FAILED
          - RUNNING
          - WAITING
          - TERMINATED
          - ERRORED
          - TIMED_OUT
        example: PASSED
      statusName:
        description: Status name
        type: string
        example: Passed
  NamedValueObject:
    title: Named Value
    description: Represents a named value or parameter
    type: object
    required:
      - name
    properties:
      name:
        description: The name of the value
        type: string
        example: Voltage
      value:
        description: The value
        type: object
        example: 1.3
  OrderByComparisonType:
    title: Order By Comparison Type
    description: >-
        An enumeration of comparison types that can be used for ordered queries.
        For non-DEFAULT comparisons, values that cannot be converted will be considered the smallest value.
    type: string
    enum:
      - DEFAULT
      - LEXICOGRAPHIC
      - NUMERIC
  ProductValuesQueryField: 
    title: Product Values Query Field
    description: An enumeration of product fields for which the values can be queried for.
    type: string
    enum:
      - ID
      - PART_NUMBER
      - NAME
      - FAMILY
      - UPDATED_AT
    example:
      FAMILY
  ProductQueryOrderByField: 
    title: Product Query OrderBy Field
    description: An enumeration of fields by which products can be ordered.
    type: string
    enum:
      - ID
      - PART_NUMBER
      - NAME
      - FAMILY
      - UPDATED_AT
    example:
      FAMILY
  ProductField:
    title: Product Field
    description: An enumeration of all fields in a Product.
    type: string
    enum:
      - ID
      - PART_NUMBER
      - NAME
      - FAMILY
      - UPDATED_AT
      - KEYWORDS
      - PROPERTIES
      - FILE_IDS
    example:
      FAMILY
  ResultValuesQueryField:
    title: Result Values Query Field
    description: An enumeration of result fields for which the values can be queried for.
    type: string
    enum:
      - ID
      - STARTED_AT
      - UPDATED_AT
      - PROGRAM_NAME
      - SYSTEM_ID
      - HOST_NAME
      - OPERATOR
      - SERIAL_NUMBER
      - PART_NUMBER
      - TOTAL_TIME_IN_SECONDS
    example:
      PROGRAM_NAME
  ResultQueryOrderByField:
    title: Result Query OrderBy Field
    description: An enumeration of fields by which results can be ordered.
    type: string
    enum:
      - ID
      - STARTED_AT
      - UPDATED_AT
      - PROGRAM_NAME
      - SYSTEM_ID
      - HOST_NAME
      - OPERATOR
      - SERIAL_NUMBER
      - PART_NUMBER
      - PROPERTIES
      - TOTAL_TIME_IN_SECONDS
    example:
      PROGRAM_NAME
  ResultField:
    title: Result Field
    description: An enumeration of all fields in a Result.
    type: string
    enum:
      - ID
      - STATUS
      - STARTED_AT
      - UPDATED_AT
      - PROGRAM_NAME
      - SYSTEM_ID
      - HOST_NAME
      - OPERATOR
      - SERIAL_NUMBER
      - PART_NUMBER
      - TOTAL_TIME_IN_SECONDS
      - KEYWORDS
      - PROPERTIES
      - FILE_IDS
      - DATA_TABLE_IDS
      - STATUS_TYPE_SUMMARY
      - WORKSPACE
    example:
      PROGRAM_NAME
  StepValuesQueryField:
    title: Step Values Query Field
    description: An enumeration of step fields for which the values can be queried for.
    type: string
    enum:
      - NAME
      - STEP_TYPE
      - STEP_ID
      - PARENT_ID
      - RESULT_ID
      - PATH
      - TOTAL_TIME_IN_SECONDS
      - STARTED_AT
      - UPDATED_AT
      - DATA_MODEL
    example:
      STEP_TYPE
  StepQueryOrderByField:
    title: Step Query OrderBy Field
    description: An enumeration of fields by which steps can be ordered.
    type: string
    enum:
      - NAME
      - STEP_TYPE
      - STEP_ID
      - PARENT_ID
      - RESULT_ID
      - PATH
      - TOTAL_TIME_IN_SECONDS
      - STARTED_AT
      - UPDATED_AT
      - DATA_MODEL
    example:
      STEP_TYPE
  StepField:
    title: Step Field
    description: An enumeration of all fields in a Step.
    type: string
    enum:
      - NAME
      - STEP_TYPE
      - STEP_ID
      - PARENT_ID
      - RESULT_ID
      - PATH
      - PATH_IDS
      - STATUS
      - TOTAL_TIME_IN_SECONDS
      - STARTED_AT
      - UPDATED_AT
      - INPUTS
      - OUTPUTS
      - DATA_MODEL
      - DATA
      - HAS_CHILDREN
      - WORKSPACE
      - KEYWORDS
      - PROPERTIES
    example:
      STEP_TYPE
  PathQueryOrderByField:
    title: Path Query OrderBy Field
    description: An enumeration of fields by which paths can be ordered.
    type: string
    enum:
      - ID
      - PROGRAM_NAME
      - PART_NUMBER
      - PATH
    example:
      PROGRAM_NAME
  PathField:
    title: Path Field
    description: An enumeration of all fields in a Path.
    type: string
    enum:
      - ID
      - PROGRAM_NAME
      - PART_NUMBER
      - PATH
      - PATH_NAMES
      - INPUTS
      - OUTPUTS
      - MEASUREMENTS
    example:
      PROGRAM_NAME
  ValueType:
    title: Value Type
    description: An enumeration of the possible types of variant values.
    type: string
    enum:
      - MIXED
      - NULL
      - BOOLEAN
      - NUMBER
      - STRING
      - ARRAY
      - OBJECT
  ResponseFormat:
    title: Response Format
    description: Enum indicating the expected response format (CSV or JSON). If unspecified, JSON is the default.
    type: string
    enum:
      - JSON
      - CSV
    default: 'JSON'
  ProductRequestObject:
    title: Product Request
    type: object
    properties:
      partNumber:
        description: The part number of the product
        type: string
        example: 156502A-11L
      name:
        description: The name of the product
        type: string
        example: cRIO-9030
      family:
        description: The family of the product
        type: string
        example: cRIO
      keywords:
        description: Words or phrases associated with the product
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      properties:
        description: Key-value pairs associated with the product
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
      fileIds:
        description: Array of file IDs attached to the product. This API does not verify that the file IDs included exist.
        type: array
        items:
          type: string
        example: [5ccb19ce5aa0a3348872c3e3]
  ProductResponseObject:
    title: Product Response
    type: object
    properties:
      id:
        description: ID of the product
        type: string
        example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
      partNumber:
        description: The part number of the product
        type: string
        example: 156502A-11L
      name:
        description: The name of the product
        type: string
        example: cRIO-9030
      family:
        description: The family of the product
        type: string
        example: cRIO
      updatedAt:
        description: >-
          ISO-8601 formatted timestamp indicating when the product
          was last updated.
        type: string
        format: date-time
        example: '2018-05-09T15:07:42.527921Z'
      keywords:
        description: Words or phrases associated with the product
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      properties:
        description: Key-value pairs associated with the product
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
      fileIds:
        description: Array of file IDs attached to the product. This API does not verify that the file IDs included exist.
        type: array
        items:
          type: string
        example: [5e30934193cac8046851acb2]
  ProductUpdateRequestObject:
    title: Product Update Request
    type: object
    properties:
      id:
        description: ID of the product to update
        type: string
        example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
      name:
        description: The name of the product
        type: string
        example: cRIO-9030
      family:
        description: The family of the product
        type: string
        example: cRIO
      keywords:
        description: Words or phrases associated with the product
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      properties:
        description: Key-value pairs associated with the product
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
      fileIds:
        description: Array of file IDs attached to the product. This API does not verify that the file IDs included exist.
        type: array
        items:
          type: string
        example: [5e30934193cac8046851acb2]
  TestResultRequestObject:
    title: Test Result Request
    type: object
    required: [programName, status]
    properties:
      programName:
        description: Program name
        type: string
        example: My Program Name
      status:
        $ref: '#/definitions/StatusObject'
      systemId:
        description: System id
        type: string
        example: my-system
      hostName:
        description: Host name
        type: string
        example: My-Host
      properties:
        description: Test result properties
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
      keywords:
        description: Words or phrases associated with the test result
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      serialNumber:
        description: Serial number
        type: string
        example: 123-456
      operator:
        description: Operator
        type: string
        example: admin
      partNumber:
        description: The part number of the device under test.
        type: string
        example: cRIO-9030
      fileIds:
        description: Array of file ids attached to the test result. This API does not verify that the file IDs included exist.
        type: array
        items:
          type: string
        example: [5e30934193cac8046851acb2]
      dataTableIds:
        description: Array of data table ids attached to the test result. This API does not verify that the data table IDs included exist.
        type: array
        items:
          type: string
        example: [62333547f7521f2f2f4615e5]
      startedAt:
        description: ISO-8601 formatted timestamp indicating when the test result began
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
      totalTimeInSeconds:
        description: Total run-time of the test in seconds
        type: number
        format: double
        default: 0
        example: 29.9
      workspace:
        description: The workspace the test result belongs to
        type: string
        example: f94b178e-288c-4101-afb1-833992413aa7
  TestResultResponseObject:
    title: Test Result Response
    type: object
    required:
      - id
    properties:
      status:
        $ref: '#/definitions/StatusObject'
      startedAt:
        description: ISO-8601 formatted timestamp indicating when the test result began
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
      updatedAt:
        description: ISO-8601 formatted timestamp indicating when the result was last updated
        type: string
        format: date-time
        example: '2018-05-09T15:07:42.527921Z'
      programName:
        description: Program name
        type: string
        example: My test program
      id:
        description: Id of the test result
        type: string
        example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
      systemId:
        description: Id of the system
        type: string
        example: 5e30931993cac8046850a996
      hostName:
        description: Host name of the system
        type: string
        example: My-Host
      operator:
        description: Name of the operator running the test
        type: string
        example: admin
      partNumber:
        description: The part number of the device under test.
        type: string
        example: cRIO-9030
      serialNumber:
        description: Sequential number of the device under test
        type: string
        example: abc-123
      totalTimeInSeconds:
        description: Total run-time of the test in seconds
        type: number
        format: double
        example: 29.9
      keywords:
        description: Words or phrases associated with the test result
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      properties:
        description: Test result properties
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
      fileIds:
        description: Array of file ids attached to the test result. This API does not verify that the file IDs included exist.
        type: array
        items:
          type: string
        example: []
      dataTableIds:
        description: Array of data table ids attached to the test result. This API does not verify that the data table IDs included exist.
        type: array
        items:
          type: string
        example: []
      statusTypeSummary:
        description: Status type summary
        type: object
        additionalProperties:
          type: integer
          format: int32
        example:
          FAILED: 5
      workspace:
        description: The workspace the test result belongs to
        type: string
        example: f94b178e-288c-4101-afb1-833992413aa7
  TestResultUpdateFailureObject:
    title: Test Result Update Failure Object
    type: object
    properties:
      id:
        description: Test result id to update
        type: string
        example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
      programName:
        description: Program name
        type: string
        example: My Program Name
      status:
        $ref: '#/definitions/StatusObject'
      systemId:
        description: System id
        type: string
        example: my-system
      hostName:
        description: Host name
        type: string
        example: My-Host
      properties:
        description: Test result properties
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
      keywords:
        description: Words or phrases associated with the test result
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      serialNumber:
        description: Serial number
        type: string
        example: 123-456
      operator:
        description: Operator
        type: string
        example: admin
      partNumber:
        description: The part number of the device under test.
        type: string
        example: cRIO-9030
      fileIds:
        description: Array of file ids attached to the test result. This API does not verify that the file IDs included exist.
        type: array
        items:
          type: string
        example: [5e30934193cac8046851acb2]
      dataTableIds:
        description: Array of data table ids attached to the test result. This API does not verify that the data table IDs included exist.
        type: array
        items:
          type: string
        example: [62333547f7521f2f2f4615e5]
      startedAt:
        description: ISO-8601 formatted timestamp indicating when the test result began
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
      totalTimeInSeconds:
        description: Total run-time of the test in seconds
        type: number
        format: double
        default: 0
        example: 29.9
      workspace:
        description: The workspace the test result belongs to
        type: string
        example: f94b178e-288c-4101-afb1-833992413aa7
  TestResultUpdateRequestObject:
    title: Test Result Update
    type: object
    required:
      - id
    properties:
      id:
        description: Test result id to update
        type: string
        example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
      programName:
        description: Program name
        type: string
        example: My Program Name
      status:
        $ref: '#/definitions/StatusObject'
      systemId:
        description: System id
        type: string
        example: my-system
      hostName:
        description: Host name
        type: string
        example: My-Host
      properties:
        description: Test result properties
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
      keywords:
        description: Words or phrases associated with the test result
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      serialNumber:
        description: Serial number
        type: string
        example: 123-456
      operator:
        description: Operator
        type: string
        example: admin
      partNumber:
        description: The part number of the device under test.
        type: string
        example: cRIO-9030
      fileIds:
        description: Array of file ids attached to the test result. This API does not verify that the file IDs included exist.
        type: array
        items:
          type: string
        example: [5e30934193cac8046851acb2]
      dataTableIds:
        description: Array of data table ids attached to the test result. This API does not verify that the data table IDs included exist.
        type: array
        items:
          type: string
        example: [62333547f7521f2f2f4615e5]
      startedAt:
        description: ISO-8601 formatted timestamp indicating when the test result began
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
      totalTimeInSeconds:
        description: Total run-time of the test in seconds
        type: number
        format: double
        default: 0
        example: 29.9
      workspace:
        description: The workspace the test result belongs to
        type: string
        example: f94b178e-288c-4101-afb1-833992413aa7
  UpdateTestResultsRequest:
    title: Update Test Results Request
    required:
      - results
    properties:
      results:
        description: Array of test results to update
        type: array
        items:
          $ref: '#/definitions/TestResultUpdateRequestObject'
      replace:
        description: Replace the existing fields instead of merging them
        type: boolean
        default: false
      determineStatusFromSteps:
        description: Determine test result status from the test step statuses
        type: boolean
        default: false
  ValueSummaryObject:
    title: Value Summary
    type: object
    properties:
      type:
        $ref: '#/definitions/ValueType'
      min:
        description: The minimum recorded value, if `type` is "NUMBER."
        type: number
        example: 1.3
      max:
        description: The maximum recorded value, if `type` is "NUMBER."
        type: number
        example: 2.6
  PathResponseObject:
    title: Path Response Object
    type: object
    properties:
      id:
        description: >-
          The unique ID of this path. Note that this value may change if
          the collection is repaired.
        type: string
        example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
      path:
        description: >-
          Identifies the steps that this path is representative of.
        type: string
        example: MainSequence Callback
          
          My Step Name
      programName:
        description: The program name for which this path is defined.
        type: string
        example: MyProgram.seq
      partNumber:
        description: The part number for which this path is defined.
        type: string
        example: 156502A-11L
      pathNames:
        description: >-
          The list of all ancestor step names for any step which corresponds
          to this path.
        type: array
        items:
          type: string
        example: ['MainSequence Callback', 'VoltageTest']
      inputs:
        description: >-
          The set of inputs that steps which correspond to this path may take.
        type: object
        additionalProperties:
          $ref: '#/definitions/ValueSummaryObject'
      outputs:
        description: >-
          The set of outputs that steps which correspond to this path may log.
        type: object
        additionalProperties:
          $ref: '#/definitions/ValueSummaryObject'
      measurements:
        description: >-
          The set of measurements that steps which correspond to this path may take.
        type: object
        additionalProperties:
          type: object
        example:
          myMeasurement: {}
  ProductsAdvancedQuery:
    title: Advanced Query Object for Products
    description: >-
      Product fields that the response can be ordered by are 
      `ID`, `PART_NUMBER`, `NAME`, `FAMILY`, and `UPDATED_AT`.
    properties:
      filter:
        description: The query filter in Dynamic Linq
        type: string
        example: (name != "cRIO-9030") && (family == @0)
      substitutions:
        description: >-
          Makes substitutions in the query filter expression. Substitutions for the query expression
          are indicated by non-negative integers that are prefixed with the "at" symbol. Each
          substitution in the given expression will be replaced by the element at the corresponding
          index (zero-based) in this list. For example, "@0" in the filter expression will be replaced with
          the element at the zeroth index of the substitutions list.
        type: array
        items:
          type: object
        example:
          - "cRIO"
      orderBy:
        $ref: '#/definitions/ProductQueryOrderByField'
      descending:
        description: ->
          Whether to return the products in descending order.
        type: boolean
        default: false
        example: false
      projection:
        description: >-
          Specifies the product fields to project. When a field value is given here,
          the corresponding field will be present in all returned products, and all
          unspecified fields will be excluded. If no projection is specified,
          all product fields will be returned.
        type: array
        items:
          $ref: '#/definitions/ProductField'
      take:
        description: >-
          The maximum number of products to return.
        type: integer
        format: int32
        default: 1000
        minimum: -1
        example: 1000
      continuationToken:
        description: >-
          A token which allows the user to resume a query at the next item in
          the matching product set. When querying for products, a token will
          be returned if a query may be continued. To obtain the next page of
          products, pass the token to the service on a subsequent request.
        type: string
        example: token
      returnCount:
        description: >-
          Whether to return the total number of products which match the
          provided filter, disregarding the take value.
        type: boolean
        default: false
        example: false
  PathsAdvancedQuery:
    title: Advanced Query Object for Paths
    description: >-
      Path fields that the response can be ordered by are 
      `ID`, `PROGRAM_NAME`, `PART_NUMBER`, and `PATH`.
    properties:
      filter:
        description: The query filter in Dynamic Linq
        type: string
        example: programName == "MyTests.seq" || partNumber == "cRIO-9030"
      substitutions:
        description: >-
          Makes substitutions in the query filter expression. Substitutions for the query expression
          are indicated by non-negative integers that are prefixed with the "at" symbol. Each
          substitution in the given expression will be replaced by the element at the corresponding
          index (zero-based) in this list. For example, "@0" in the filter expression will be replaced with
          the element at the zeroth index of the substitutions list.
        type: array
        items:
          type: object
        example:
          - 2.5
      orderBy:
        $ref: '#/definitions/PathQueryOrderByField'
      descending:
        description: ->
          Whether to return the paths in descending order.
        type: boolean
        default: false
        example: false
      projection:
        description: >-
          Specifies the path fields to project. When a field value is given here,
          the corresponding field will be present in all returned paths, and all
          unspecified fields will be excluded. If no projection is specified,
          all path fields will be returned.
        type: array
        items:
          $ref: '#/definitions/PathField'
      take:
        description: >-
          The maximum number of paths to return.
        type: integer
        format: int32
        default: 1000
        minimum: -1
        example: 1000
      continuationToken:
        description: >-
          A token which allows the user to resume a query at the next item in
          the matching path set. When querying for paths, a token will
          be returned if a query may be continued. To obtain the next page of
          paths, pass the token to the service on a subsequent request.
        type: string
        example: token
      returnCount:
        description: >-
          Whether to return the total number of paths which match the
          provided filter, disregarding the take value.
        type: boolean
        default: false
        example: false
  ResultsAdvancedQuery:
    title: Advanced Query Object for Test Results
    description: Results advanced query request object.
    properties:
      filter:
        description: The result query filter in Dynamic Linq
        type: string
        example: (operator == "user1") || ((programName != "MyProgram") && (totalTimeInSeconds < @0))
      substitutions:
        description: >-
          Makes substitutions in the query filter expression. Substitutions for the query expression
          are indicated by non-negative integers that are prefixed with the "at" symbol. Each
          substitution in the given expression will be replaced by the element at the corresponding
          index (zero-based) in this list. For example, "@0" in the filter expression will be replaced with
          the element at the zeroth index of the substitutions list.
        type: array
        items:
          type: object
        example:
          - 2.5
      productFilter:
        description: The product query filter in Dynamic Linq
        type: string
        example: (name != "cRIO-9030") && (family == @0)
      productSubstitutions:
        description: >-
          Makes substitutions in the query filter expression. Substitutions for the query expression
          are indicated by non-negative integers that are prefixed with the "at" symbol. Each
          substitution in the given expression will be replaced by the element at the corresponding
          index (zero-based) in this list. For example, "@0" in the filter expression will be replaced with
          the element at the zeroth index of the substitutions list.
        type: array
        items:
          type: object
        example:
          - cRIO
      orderBy:
        $ref: '#/definitions/ResultQueryOrderByField'
      descending:
        description: >-
          Whether to return the results in descending order.
        type: boolean
        default: false
        example: false
      orderByKey:
        description: >-
          The property name to order by when ordering by PROPERTIES. Results that do not contain the orderByKey
          will be considered the smallest value.
        type: string
        example: null
      orderByComparisonType:
        $ref: '#/definitions/OrderByComparisonType'
      projection:
        description: >-
          Specifies the result fields to project. When a field value is given here,
          the corresponding field will be present in all returned results, and all
          unspecified fields will be excluded. If no projection is specified,
          all result fields will be returned.
        type: array
        items:
          $ref: '#/definitions/ResultField'
      take:
        description: >-
          The maximum number of products to return.
        type: integer
        format: int32
        default: 1000
        minimum: -1
        example: 1000
      continuationToken:
        description: >-
          A token which allows the user to resume a query at the next item in
          the matching product set. When querying for products, a token will
          be returned if a query may be continued. To obtain the next page of
          products, pass the token to the service on a subsequent request.
        type: string
        example: token
      returnCount:
        description: >-
          Whether to return the total number of products which match the
          provided filter, disregarding the take value.
        type: boolean
        default: false
        example: false
      responseFormat:
        $ref: '#/definitions/ResponseFormat'
  StepsAdvancedQuery:
    title: Advanced Query Object for Test Steps
    description: >-
      Test Step fields that the response can be ordered by are 
      `NAME`, `STEP_TYPE`, `STEP_ID`, `PARENT_ID`, `RESULT_ID`, 
      `PATH`, `TOTAL_TIME_IN_SECONDS`, `STARTED_AT`, `UPDATED_AT`,
      and `DATA_MODEL`.
    properties:
      filter:
        description: The step query filter in Dynamic Linq
        type: string
        example: (stepType == "NumericLimitTest") && (totalTimeInSeconds > @0)
      substitutions:
        description: >-
          Makes substitutions in the query filter expression. Substitutions for the query expression
          are indicated by non-negative integers that are prefixed with the "at" symbol. Each
          substitution in the given expression will be replaced by the element at the corresponding
          index (zero-based) in this list. For example, "@0" in the filter expression will be replaced with
          the element at the zeroth index of the substitutions list.
        type: array
        items:
          type: object
        example:
          - 2.5
      resultFilter:
        description: >-
          The result query filter in Dynamic Linq.
        type: string
        example: (programName != "mySequence.seq") && (operator == @0)
      resultSubstitutions:
        description: >-
          Makes substitutions in the query filter expression for results.
          Substitutions for the query expression are indicated by non-negative
          integers that are prefixed with the "at" symbol. Each substitution in
          the given expression will be replaced by the element at the
          corresponding index (zero-based) in this list. For example, "@0" in
          the filter expression will be replaced with the element at the zeroth
          index of the substitutions list.
        type: array
        items:
          type: object
        example:
          - user1
      orderBy:
        $ref: '#/definitions/StepQueryOrderByField'
      descending:
        description: ->
          Whether to return the steps in descending order.
        type: boolean
        default: false
        example: false
      projection:
        description: >-
          Specifies the step fields to project. When a field value is given here,
          the corresponding field will be present in all returned steps, and all
          unspecified fields will be excluded. If no projection is specified,
          all step fields will be returned.
        type: array
        items:
          $ref: '#/definitions/StepField'
      take:
        description: >-
          The maximum number of steps to return.
        type: integer
        format: int32
        default: 1000
        minimum: -1
        example: 1000
      continuationToken:
        description: >-
          A token which allows the user to resume a query at the next item in
          the matching step set. When querying for steps, a token will
          be returned if a query may be continued. To obtain the next page of
          steps, pass the token to the service on a subsequent request.
        type: string
        example: token
      returnCount:
        description: >-
          Whether to return the total number of steps which match the
          provided filter, disregarding the take value.
        type: boolean
        default: false
        example: false
      responseFormat:
        $ref: '#/definitions/ResponseFormat'
  ProductValuesQuery:
    title: Product Values Query
    required:
    - field
    properties:
      field:
        $ref: '#/definitions/ProductValuesQueryField'
      filter:
        description: >-
          A Dynamic Linq query which specifies the products to consider when
          getting values.
        type: string
        example: name != "cRIO-9030"
      substitutions:
        description: >-
          Makes substitutions in the query filter expression. Substitutions for the query expression
          are indicated by non-negative integers that are prefixed with the "at" symbol. Each
          substitution in the given expression will be replaced by the element at the corresponding
          index (zero-based) in this list. For example, "@0" in the filter expression will be replaced with
          the element at the zeroth index of the substitutions list.
        type: array
        items:
          type: object
        example:
          - 2.5
      startsWith:
        description: >-
          Only return string values prefixed by this value (case sensitive).
        type: string
        example: cR
  ResultValuesQuery:
    title: Result Values Query
    required:
    - field
    properties:
      field:
        $ref: '#/definitions/ResultValuesQueryField'
      filter:
        description: >-
          A Dynamic Linq query which specifies the results to consider when
          getting values.
        type: string
        example: programName != "MyProgram"
      substitutions:
        description: >-
          Makes substitutions in the query filter expression. Substitutions for the query expression
          are indicated by non-negative integers that are prefixed with the "at" symbol. Each
          substitution in the given expression will be replaced by the element at the corresponding
          index (zero-based) in this list. For example, "@0" in the filter expression will be replaced with
          the element at the zeroth index of the substitutions list.
        type: array
        items:
          type: object
        example:
          - 2.5
      startsWith:
        description: >-
          Only return string values prefixed by this value (case sensitive).
        type: string
        example: op
  StepValuesQuery:
    title: Step Values Query
    required:
    - field
    properties:
      field:
        $ref: '#/definitions/StepValuesQueryField'
      filter:
        description: >-
          A Dynamic Linq query which specifies the steps to consider when
          getting values.
        type: string
        example: stepType != "NumericLimitTest"
      substitutions:
        description: >-
          Makes substitutions in the query filter expression. Substitutions for the query expression
          are indicated by non-negative integers that are prefixed with the "at" symbol. Each
          substitution in the given expression will be replaced by the element at the corresponding
          index (zero-based) in this list. For example, "@0" in the filter expression will be replaced with
          the element at the zeroth index of the substitutions list.
        type: array
        items:
          type: object
        example:
          - 2.5
      startsWith:
        description: >-
          Only return string values prefixed by this value (case sensitive).
        type: string
        example: op
  StepIdResultIdPair:
    title: Step Id / Result Id Pair
    type: object
    required:
      - stepId
      - resultId
    properties:
      stepId:
        type: string
        example: bd9126f5-b0b1-446a-8b08-dc6460047377
      resultId:
        type: string
        example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
  StepDataObject:
    title: Step Data
    description: Data returned by the test step
    type: object
    properties:
      text:
        description: Text string describing the output data
        type: string
        example: My output string
      parameters:
        description: Array of properties objects
        type: array
        items:
          description: Dictionary of key-value property pairs
          type: object
          additionalProperties:
            type: string
          example:
            key1: value1
        example:
          - name: Voltage
            status: Passed
            measurement: "3.725"
            lowLimit: "3.65"
            highLimit: "3.8"
            nominalValue: "3.7"
            units: volt
            comparisonType: GELE
          - nitmParameterType: ADDITIONAL_RESULTS
            additionalProp: myValue
  TestStepsDeleteRequest:
    title: Test Steps Delete Request
    required:
      - steps
    properties:
      steps:
        description: Array of test step id and result id pairs to delete
        type: array
        items:
          $ref: '#/definitions/StepIdResultIdPair'
  TestStepRequestObject:
    title: Test Step Request
    type: object
    properties:
      stepId:
        description: Step id
        type: string
        example: Step1
      parentId:
        description: Parent step id
        type: string
        example: root
      resultId:
        description: Result id
        type: string
        example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
      children:
        description: Nested child steps
        type: array
        items:
          $ref: '#/definitions/TestStepRequestObject'
        example: []
      data:
        $ref: '#/definitions/StepDataObject'
      dataModel:
        description: Data model for the step
        type: string
        example: TestStand
      name:
        description: Step name
        type: string
        example: My Step
      startedAt:
        description: ISO-8601 formatted timestamp indicating when the test result began
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
      status:
        $ref: '#/definitions/StatusObject'
      stepType:
        description: Step type
        type: string
        example: NumericLimitTest
      totalTimeInSeconds:
        description: Total number of seconds the step took to execute
        type: number
        format: double
        default: 0
        example: 29.9
      inputs:
        description: Inputs and their values passed to the test
        type: array
        items:
          $ref: '#/definitions/NamedValueObject'
      outputs:
        description: Outputs and their values logged by the test
        type: array
        items:
          $ref: '#/definitions/NamedValueObject'
      keywords:
        description: Words or phrases associated with the step
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      properties:
        description: Test step properties
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
  TestStepCreateRequestObject:
    title: Test Step Create Request
    required:
      - steps
    properties:
      steps:
        description: Array of test steps to create
        type: array
        items:
          $ref: '#/definitions/TestStepRequestObject'
      updateResultTotalTime:
        description: Determine test result total time from the test step total times.
        type: boolean
        default: false
  TestStepUpdateRequestObject:
    title: Test Step Update Request
    required:
      - steps
    properties:
      steps:
        description: Array of test steps to create
        type: array
        items:
          $ref: '#/definitions/TestStepRequestObject'
      updateResultTotalTime:
        description: Determine test result total time from the test step total times.
        type: boolean
        default: false
      replaceKeywords:
        description: Replace with existing keywords instead of merging them
        type: boolean
        default: false
      replaceProperties:
        description: Replace with existing properties instead of merging them
        type: boolean
        default: false
  TestStepResponseObject:
    title: Test Step Response
    type: object
    properties:
      name:
        description: Step name
        type: string
        example: My Step Name
      stepType:
        description: Step type
        type: string
        example: NumericLimitTest
      stepId:
        description: Step id
        type: string
        example: Step1
      parentId:
        description: Parent step id
        type: string
        example: root
      resultId:
        description: Result id
        type: string
        example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
      path:
        description: Step path
        type: string
        example: root.My Step Name
      pathIds:
        description: Ids of the steps in the path
        type: array
        items:
          type: string
        example:
          - root
          - Step1
      status:
        $ref: '#/definitions/StatusObject'
      totalTimeInSeconds:
        description: Total number of seconds the step took to execute
        type: number
        format: double
        example: 0
      startedAt:
        description: ISO-8601 formatted timestamp indicating when the test result began
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
      updatedAt:
        description: ISO-8601 formatted timestamp indicating when the result was last updated
        type: string
        format: date-time
        example: '2018-05-09T15:07:42.527921Z'
      inputs:
        description: Inputs and their values passed to the test
        type: array
        items:
          $ref: '#/definitions/NamedValueObject'
      outputs:
        description: Outputs and their values logged by the test
        type: array
        items:
          $ref: '#/definitions/NamedValueObject'
      dataModel:
        description: Custom string defining the model of the data object
        type: string
        example: TestStand
      data:
        $ref: '#/definitions/StepDataObject'
      hasChildren:
        description: >-
          Whether this step object has any children step objects. When false, this means
          that this step object is a leaf node.
        type: boolean
        example: false
      workspace:
        description: The workspace the test step belongs to
        type: string
        example: f94b178e-288c-4101-afb1-833992413aa7
      keywords:
        description: Words or phrases associated with the test step
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      properties:
        description: Test step properties
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
responses:
  Error:
    description: Error
    schema:
      description: Error response
      title: ErrorResponse
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
  Unauthorized:
    description: Not authorized
    headers:
      WWW_Authenticate:
        description: Information for how to authenticate
        type: string
  ProductsSuccessResponse:
    description: Products Success Response
    schema:
      description: Products Success Response
      title: ProductsSuccessResponse
      type: object
      required:
        - products
      properties:
        products:
          description: Array of products
          type: array
          items:
            $ref: '#/definitions/ProductResponseObject'
  ProductsPartialSuccessResponse:
    description: Products Partial Success Response
    schema:
      description: Products Partial Success Response
      title: ProductsPartialSuccessResponse
      type: object
      required:
        - products
      properties:
        products:
          description: Array of products
          type: array
          items:
            $ref: '#/definitions/ProductResponseObject'
        failed:
          description: Array of product requests that failed
          type: array
          items:
            $ref: '#/definitions/ProductRequestObject'
        error:
          $ref: '#/definitions/Error'
  DeleteProductsResponse:
    description: Delete Products Response
    schema:
      description: Delete Products Response
      title: DeleteProductsResponse
      type: object
      required:
        - ids
      properties:
        ids:
          description: Array of product ids to delete
          type: array
          items:
            type: string
          example:
            - 02600cf8-c2bb-4ff9-a139-031e943fb0c0
        failed:
          description: Array of product ids that failed to delete
          type: array
          items:
            type: string
          example: []
        error:
          $ref: '#/definitions/Error'
  ProductsQueryResponse:
    description: Products Query Response
    schema:
      description: Products Query Response
      title: ProductsQueryResponse
      type: object
      x-ni-sparse: true
      required:
        - products
      properties:
        products:
          description: Array of products
          type: array
          items:
            $ref: '#/definitions/ProductResponseObject'
        continuationToken:
          description: >-
            A token which allows the user to resume this query at the next item
            in the matching product set. In order to continue paginating a
            query, pass this token to the service on a subsequent request. The
            service will respond with a new continuation token. To paginate a
            set of products, continue sending requests with the newest
            continuation token provided by the service, until this value is
            null.
          type: string
          example: "token"
        totalCount:
          description: >-
            The number of matching products, if returnCount is true.
            This value is not present if returnCount is false.
          type: integer
          format: int64
          example: 1
  ResultsSuccessResponse:
    description: Test Results Success Response
    schema:
      description: Test Results Success Response
      title: ResultsSuccessResponse
      type: object
      required:
        - results
      properties:
        results:
          description: Array of test results
          type: array
          items:
            $ref: '#/definitions/TestResultResponseObject'
  ResultsPartialSuccessResponse:
    description: Test Results Partial Success Response
    schema:
      description: Test Results Partial Success Response
      title: ResultsPartialSuccessResponse
      type: object
      required:
        - results
      properties:
        results:
          description: Array of test results
          type: array
          items:
            $ref: '#/definitions/TestResultResponseObject'
        failed:
          description: Array of test result requests that failed
          type: array
          items:
            $ref: '#/definitions/TestResultRequestObject'
        error:
          $ref: '#/definitions/Error'
  ResultsUpdatePartialSuccessResponse:
    description: Test Results Update Partial Success Response
    schema:
      description: Test Results Update Partial Success Response
      title: ResultsUpdatePartialSuccessResponse
      type: object
      required:
        - results
      properties:
        results:
          description: Array of test results
          type: array
          items:
            $ref: '#/definitions/TestResultResponseObject'
        failed:
          description: Array of test result update requests that failed
          type: array
          items:
            $ref: '#/definitions/TestResultUpdateFailureObject'
        error:
          $ref: '#/definitions/Error'
  DeleteResultsResponse:
    description: Delete Test Results Response
    schema:
      description: Delete Test Results Response
      title: DeleteResultsResponse
      type: object
      required:
        - ids
      properties:
        ids:
          description: Array of test result ids to delete
          type: array
          items:
            type: string
        failed:
          description: Array of test result ids that failed to delete
          type: array
          items:
            type: string
        error:
          $ref: '#/definitions/Error'
  ResultsQueryResponse:
    description: Test Results Query Response
    schema:
      description: Test Results Query Response
      title: ResultsQueryResponse
      type: object
      x-ni-sparse: true
      required:
        - results
      properties:
        results:
          description: Array of test results
          type: array
          items:
            $ref: '#/definitions/TestResultResponseObject'
        continuationToken:
          description: >-
            A token which allows the user to resume this query at the next item
            in the matching result set. In order to continue paginating a
            query, pass this token to the service on a subsequent request. The
            service will respond with a new continuation token. To paginate a
            set of results, continue sending requests with the newest
            continuation token provided by the service, until this value is
            null.
          type: string
          example: "token"
        totalCount:
          description: >-
            The number of matching test results, if returnCount is true.
            This value is not present if returnCount is false.
          type: integer
          format: int64
          example: 1
  StepsSuccessResponse:
    description: Test Steps Success Response
    schema:
      description: Test Steps Success Response
      title: StepsSuccessResponse
      type: object
      required:
        - steps
      properties:
        steps:
          description: Array of test steps
          type: array
          items:
            $ref: '#/definitions/TestStepResponseObject'
  StepsPartialSuccessResponse:
    description: Test Steps Partial Success Response
    schema:
      description: Test Steps Partial Success Response
      title: StepsPartialSuccessResponse
      type: object
      required:
        - steps
      properties:
        steps:
          description: Array of test steps
          type: array
          items:
            $ref: '#/definitions/TestStepResponseObject'
        failed:
          description: Array of test step requests that failed
          type: array
          items:
            $ref: '#/definitions/TestStepRequestObject'
        error:
          $ref: '#/definitions/Error'
  StepsQueryResponse:
    description: Test Steps Query Response
    schema:
      description: Test Steps Query Response
      title: StepsQueryResponse
      type: object
      x-ni-sparse: true
      required:
        - steps
      properties:
        steps:
          description: Array of test steps
          type: array
          items:
            $ref: '#/definitions/TestStepResponseObject'
        continuationToken:
          description: >-
            A token which allows the user to resume this query at the next item
            in the matching step set. In order to continue paginating a
            query, pass this token to the service on a subsequent request. The
            service will respond with a new continuation token. To paginate a
            set of steps, continue sending requests with the newest
            continuation token provided by the service, until this value is
            null.
          type: string
          example: "token"
        totalCount:
          description: >-
            The number of matching test steps, if returnCount is true.
            This value is not present if returnCount is false.
          type: integer
          format: int64
          example: 1
  StepsDeletePartialSuccessResponse:
    description: Delete Test Steps Partial Success Response
    schema:
      description: Delete Test Steps Partial Success Response
      title: StepsDeletePartialSuccessResponse
      type: object
      required:
        - steps
      properties:
        steps:
          description: Array of test step id result id pairs that were deleted
          type: array
          items:
            $ref: '#/definitions/StepIdResultIdPair'
        failed:
          description: Array of test step id result id pairs that failed to delete
          type: array
          items:
            $ref: '#/definitions/StepIdResultIdPair'
        error:
          $ref: '#/definitions/Error'
  ValuesResponse:
    description: Values Response
    schema:
      description: Values Response
      title: ValuesResponse
      type: array
      items:
        type: string
      example:
      - operator1
      - operator2
  PathsQueryResponse:
    description: Paths Query Response
    schema:
      description: Paths Query Response
      title: PathsQueryResponse
      type: object
      x-ni-sparse: true
      required:
        - paths
      properties:
        paths:
          description: An array of path objects.
          type: array
          items:
            $ref: '#/definitions/PathResponseObject'
        continuationToken:
          description: >-
            A token which allows the user to resume this query at the next item
            in the matching path set. In order to continue paginating a
            query, pass this token to the service on a subsequent request. The
            service will respond with a new continuation token. To paginate a
            set of paths, continue sending requests with the newest
            continuation token provided by the service, until this value is
            null.
          type: string
          example: "token"
        totalCount:
          description: >-
            The number of matching paths, if returnCount is true.
            This value is not present if returnCount is false.
          type: integer
          format: int64
paths:
  /:
    get:
      tags: [versioning]
      summary: API information
      description: Returns information about API versions and available operations.
      operationId: root-endpoint
      # Explicitly mark security as an empty array - this route does not require any privileges.
      # Marking it this way prevents it from inheriting the top-level security settings.
      security: []
      responses:
        200:
          description: OK
          schema:
            description: Version information
            title: RootEndpointResponse
            type: object
            properties:
              v1:
                $ref: '#/definitions/V1Operations'
              v2:
                $ref: '#/definitions/V2Operations'
              version:
                description: Implementation version of the web service
                type: string
  /v2:
    get:
      tags: [versioning]
      summary: API version 2 information
      description: Returns available operations for version 2 of the API.
      operationId: root-endpoint-v2
      # Explicitly mark security as an empty array - this route does not require any privileges.
      # Marking it this way prevents it from inheriting the top-level security settings.
      security: []
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/V2Operations'
        404:
          description: Not Found
          schema:
            $ref: '#/definitions/Error'
  /v2/query-products:
    post:
      tags: [products]
      summary: Queries products
      description: >-
        Uses the Dynamic Linq query language to specify a filter and return
        product. An empty request body queries all products.
      operationId: query-products-v2
      x-ni-operation: queryProducts
      x-ni-auth: true
      parameters:
        - in: body
          name: postBody
          description: Query filter
          required: false
          schema:
            $ref: '#/definitions/ProductsAdvancedQuery'
      responses:
        200:
          $ref: '#/responses/ProductsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/products:
    get:
      tags: [products]
      summary: Gets products
      description: Gets a list of products.
      operationId: get-products-v2
      x-ni-operation: getProducts
      x-ni-auth: true
      parameters:
        - in: query
          name: continuationToken
          description: >-
            A token which allows the user to resume a query at the next item in
            the matching product set. When querying for products, a token will
            be returned if a query may be continued. To obtain the next page of
            products, pass the token to the service on a subsequent request.
          type: string
        - in: query
          name: take
          description: >-
            The maximum number of products to return.
          type: integer
          format: int32
          default: 1000
          minimum: -1
        - in: query
          name: returnCount
          description: >-
            Whether to return the total number of products,
            disregarding the take value.
          type: boolean
          default: false
      responses:
        200:
          $ref: '#/responses/ProductsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      tags: [products]
      summary: Creates new products
      description: Creates new products from the supplied models. The server automatically generates the product ids.
      operationId: create-products-v2
      x-ni-operation: createProducts
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Product object
          required: true
          schema:
            description: Array of products to create
            title: CreateProductsRequest
            required:
              - products
            properties:
              products:
                description: Array of products to create
                type: array
                items:
                  $ref: '#/definitions/ProductRequestObject'
      responses:
        200:
          $ref: '#/responses/ProductsPartialSuccessResponse'
        201:
          $ref: '#/responses/ProductsSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/products/{productId}:
    get:
      tags: [products]
      summary: Gets a product
      description: Gets a single product.
      operationId: get-product-v2
      x-ni-operation: getProducts
      x-ni-auth: true
      parameters:
        - in: path
          name: productId
          description: The id of the product to get.
          type: string
          required: true
      responses:
        200:
          description: Get Product Response
          schema:
            $ref: '#/definitions/ProductResponseObject'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      tags: [products]
      summary: Deletes a product
      description: Deletes the product with the specified id. The request succeeds for products that do not exist.
      operationId: delete-product-v2
      x-ni-operation: deleteProduct
      x-ni-auth: true
      parameters:
        - in: path
          name: productId
          description: Id of the product to delete
          type: string
          required: true
      responses:
        204:
          description: The resource was deleted successfully.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/query-product-values:
    post:
      tags: [products]
      summary: Queries values for a product field
      description: >-
        Queries known values for an indexed, scalar product field. Supported
        fields are `ID`, `PART_NUMBER`, `NAME`, `FAMILY`, and `UPDATED_AT`.
      operationId: query-product-values-v2
      x-ni-operation: queryProducts
      x-ni-auth: true
      parameters:
        - in: body
          name: postBody
          description: Query parameters
          required: true
          schema:
            $ref: '#/definitions/ProductValuesQuery'
      responses:
        200:
          $ref: '#/responses/ValuesResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/update-products:
    post:
      tags: [products]
      summary: Updates existing products
      description: Updates existing products by merging or replacing values.
      operationId: update-products-v2
      x-ni-operation: updateProducts
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Array of products to update
          required: true
          schema:
            description: Array of products to update
            title: UpdateProductsRequest
            required:
              - products
            properties:
              products:
                description: Array of products to update
                type: array
                items:
                  $ref: '#/definitions/ProductUpdateRequestObject'
              replace:
                description: Replace the existing fields instead of merging them
                type: boolean
                default: false
      responses:
        200:
          $ref: '#/responses/ProductsPartialSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/delete-products:
    post:
      tags: [products]
      summary: Deletes products
      description: Deletes multiple products in a single request.
      operationId: delete-products-v2
      x-ni-operation: deleteProducts
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Array of products
          required: true
          schema:
            description: Array of products
            title: DeleteProductsRequest
            required:
              - ids
            properties:
              ids:
                description: Array of product ids to delete
                type: array
                items:
                  type: string
                  example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
      responses:
        200:
          $ref: '#/responses/DeleteProductsResponse'
        204:
          description: The resources were deleted successfully.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/query-results:
    post:
      tags: [results]
      summary: Queries test results
      description: >-
        Uses the Dynamic Linq query language to specify filters for results.
        Both result and product filters can be specified and matching test
        results are returned. An empty request body queries all test results.
      operationId: query-results-v2
      x-ni-operation: queryResults
      x-ni-auth: true
      parameters:
        - in: body
          name: postBody
          description: Query filter
          required: false
          schema:
            $ref: '#/definitions/ResultsAdvancedQuery'
      produces:
        - application/json
        - text/csv
      responses:
        200:
          $ref: '#/responses/ResultsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/results:
    get:
      tags: [results]
      summary: Gets test results
      description: Gets a list of test results.
      operationId: get-results-v2
      x-ni-operation: getResults
      x-ni-auth: true
      parameters:
        - in: query
          name: continuationToken
          description: >-
            A token which allows the user to resume a query at the next item in
            the matching result set. When querying for results, a token will
            be returned if a query may be continued. To obtain the next page of
            results, pass the token to the service on a subsequent request.
          type: string
        - in: query
          name: take
          description: >-
            The maximum number of results to return.
          type: integer
          format: int32
          default: 1000
          minimum: -1
        - in: query
          name: returnCount
          description: >-
            Whether to return the total number of results,
            disregarding the take value.
          type: boolean
          default: false
      responses:
        200:
          $ref: '#/responses/ResultsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      tags: [results]
      summary: Creates new test results
      description: Creates new test results from the supplied models. The server automatically generates the result ids. The server will populate the start time if one is not provided.
      operationId: create-results-v2
      x-ni-operation: createResults
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Result object
          required: true
          schema:
            description: Array of test results to create
            title: CreateTestResultsRequest
            required:
              - results
            properties:
              results:
                description: Array of test results to create
                type: array
                items:
                  $ref: '#/definitions/TestResultRequestObject'
      responses:
        200:
          $ref: '#/responses/ResultsPartialSuccessResponse'
        201:
          $ref: '#/responses/ResultsSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/results/{resultId}:
    get:
      tags: [results]
      summary: Gets a test result
      description: Gets a single test result.
      operationId: get-result-v2
      x-ni-operation: getResults
      x-ni-auth: true
      parameters:
        - in: path
          name: resultId
          description: The id of the result to get.
          type: string
          required: true
      responses:
        200:
          description: Get Test Result Response
          schema:
            $ref: '#/definitions/TestResultResponseObject'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      tags: [results]
      summary: Deletes a test result
      description: Deletes the test result with the specified id. The request succeeds for result ids that do not exist.
      operationId: delete-result-v2
      x-ni-operation: deleteResult
      x-ni-auth: true
      parameters:
        - in: path
          name: resultId
          description: Id of the test result to delete
          type: string
          required: true
        - in: query
          name: deleteSteps
          description: Indicates whether to delete the test steps associated with the test result
          type: boolean
          default: true
      responses:
        204:
          description: The resource was deleted successfully.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/query-result-values:
    post:
      tags: [results]
      summary: Queries values for a result field
      description: >-
        Queries known values for an indexed, scalar result field. Supported
        fields are `ID`, `STARTED_AT`, `UPDATED_AT`, `PROGRAM_NAME`,
        `SYSTEM_ID`, `HOST_NAME`, `OPERATOR`, `SERIAL_NUMBER`, `PART_NUMBER`,
        and `TOTAL_TIME_IN_SECONDS`.
      operationId: query-result-values-v2
      x-ni-operation: queryResults
      x-ni-auth: true
      parameters:
        - in: body
          name: postBody
          description: Query parameters
          required: true
          schema:
            $ref: '#/definitions/ResultValuesQuery'
      responses:
        200:
          $ref: '#/responses/ValuesResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/update-results:
    post:
      tags: [results]
      summary: Updates existing test results
      description: Updates existing test results by merging or replacing values.
      operationId: update-results-v2
      x-ni-operation: updateResults
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Array of test results to update
          required: true
          schema:
            $ref: '#/definitions/UpdateTestResultsRequest'
      responses:
        200:
          $ref: '#/responses/ResultsUpdatePartialSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/delete-results:
    post:
      tags: [results]
      summary: Deletes test results
      description: Deletes multiple test results in a single request.
      operationId: delete-results-v2
      x-ni-operation: deleteResults
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Array of test result ids
          required: true
          schema:
            description: Array of test result ids
            title: DeleteResultsRequest
            required:
              - ids
            properties:
              ids:
                description: Array of test result ids to delete
                type: array
                items:
                  type: string
                  example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
              deleteSteps:
                description: Indicates whether to delete the test steps associated with the test result
                type: boolean
                default: true
      responses:
        200:
          $ref: '#/responses/DeleteResultsResponse'
        204:
          description: The resources were deleted successfully.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/query-steps:
    post:
      tags: [steps]
      summary: Queries test steps
      description: >-
        Uses the Dynamic Linq query language to specify filters for steps.
        Both step and result filters can be specified and matching test
        steps are returned. An empty request body queries all test steps.
      operationId: query-steps-v2
      x-ni-operation: querySteps
      x-ni-auth: true
      parameters:
        - in: body
          name: postBody
          description: Query filter
          required: false
          schema:
            $ref: '#/definitions/StepsAdvancedQuery'
      produces:
        - application/json
        - text/csv
      responses:
        200:
          $ref: '#/responses/StepsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/steps:
    get:
      tags: [steps]
      summary: Gets test steps
      description: Gets a list of test steps.
      operationId: get-steps-v2
      x-ni-operation: getSteps
      x-ni-auth: true
      parameters:
        - in: query
          name: continuationToken
          description: >-
            A token which allows the user to resume a query at the next item in
            the matching step set. When querying for steps, a token will
            be returned if a query may be continued. To obtain the next page of
            steps, pass the token to the service on a subsequent request.
          type: string
        - in: query
          name: take
          description: >-
            The maximum number of steps to return.
          type: integer
          format: int32
          default: 1000
          minimum: -1
        - in: query
          name: returnCount
          description: >-
            Whether to return the total number of results,
            disregarding the take value.
          type: boolean
          default: false
      responses:
        200:
          $ref: '#/responses/StepsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      tags: [steps]
      summary: Creates new test steps
      description: Creates new test steps from the supplied models. The result associated with the step must exist prior to step creation. The server automatically generates step ids if not supplied.
      operationId: create-steps-v2
      x-ni-operation: createSteps
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Test step object
          required: true
          schema:
            $ref: '#/definitions/TestStepCreateRequestObject'
      responses:
        200:
          $ref: '#/responses/StepsPartialSuccessResponse'
        201:
          $ref: '#/responses/StepsSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/results/{resultId}/steps/{stepId}:
    get:
      tags: [steps]
      summary: Gets a test step
      description: Gets a single test step.
      operationId: get-step-v2
      x-ni-operation: getSteps
      x-ni-auth: true
      parameters:
        - in: path
          name: resultId
          description: The resultId of the step to get.
          type: string
          required: true
        - in: path
          name: stepId
          description: The stepId of the step to get.
          type: string
          required: true
      responses:
        200:
          description: Get Test Step Response
          schema:
            $ref: '#/definitions/TestStepResponseObject'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      tags: [steps]
      summary: Deletes a test step
      description: Deletes the test step with the specified id. The request succeeds for step ids that do not exist.
      operationId: delete-step-v2
      x-ni-operation: deleteStep
      x-ni-auth: true
      parameters:
        - in: path
          name: resultId
          description: Id of the test result the step belongs to
          type: string
          required: true
        - in: path
          name: stepId
          description: Id of the test step to delete
          type: string
          required: true
        - in: query
          name: updateResultTotalTime
          description: Determine test result total time from the test step total times.
          type: boolean
          default: false
      responses:
        204:
          description: The resource was deleted successfully.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/query-step-values:
    post:
      tags: [steps]
      summary: Queries values for a step field
      description: >-
        Queries known values for an indexed, scalar step field. Supported
        fields are `NAME`, `STEP_TYPE`, `STEP_ID`, `PARENT_ID`, `RESULT_ID`,
        `PATH`, `TOTAL_TIME_IN_SECONDS`, `STARTED_AT`, `UPDATED_AT`, and
        `DATA_MODEL`.
      operationId: query-step-values-v2
      x-ni-operation: querySteps
      x-ni-auth: true
      parameters:
        - in: body
          name: postBody
          description: Query parameters
          required: true
          schema:
            $ref: '#/definitions/StepValuesQuery'
      responses:
        200:
          $ref: '#/responses/ValuesResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/update-steps:
    post:
      tags: [steps]
      summary: Updates existing test steps
      description: Updates existing steps by merging or replacing values.
      operationId: update-steps-v2
      x-ni-operation: updateSteps
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Array of test steps
          required: true
          schema:
            $ref: '#/definitions/TestStepUpdateRequestObject'
      responses:
        200:
          $ref: '#/responses/StepsPartialSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/delete-steps:
    post:
      tags: [steps]
      summary: Deletes test steps
      description: Deletes multiple test steps in a single request.
      operationId: delete-steps-v2
      x-ni-operation: deleteSteps
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Delete steps request
          required: true
          schema:
            $ref: '#/definitions/TestStepsDeleteRequest'
        - in: query
          name: updateResultTotalTime
          description: Determine test result total time from the test step total times.
          type: boolean
          default: false
      responses:
        200:
          $ref: '#/responses/StepsDeletePartialSuccessResponse'
        204:
          description: The resources were deleted successfully.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/paths:
    get:
      tags: [paths]
      summary: Gets paths
      description: Gets a list of paths.
      operationId: get-paths-v2
      x-ni-operation: queryPaths
      x-ni-auth: true
      parameters:
        - in: query
          name: continuationToken
          description: >-
            A token which allows the user to resume a query at the next item in
            the matching path set. When querying for paths, a token will
            be returned if a query may be continued. To obtain the next page of
            paths, pass the token to the service on a subsequent request.
          type: string
        - in: query
          name: take
          description: >-
            The maximum number of paths to return.
          type: integer
          format: int32
          default: 1000
          minimum: -1
        - in: query
          name: returnCount
          description: >-
            Whether to return the total number of paths,
            disregarding the take value.
          type: boolean
          default: false
      responses:
        200:
          $ref: '#/responses/PathsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/paths/{pathId}:
    get:
      tags: [paths]
      summary: Gets a path
      description: Gets a single path.
      operationId: get-path-v2
      x-ni-operation: queryPaths
      x-ni-auth: true
      parameters:
        - in: path
          name: pathId
          description: The ID of the path to get.
          type: string
          required: true
      responses:
        200:
          description: Get Path Response
          schema:
            $ref: '#/definitions/PathResponseObject'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/query-paths:
    post:
      tags: [paths]
      summary: Queries paths
      description: >-
        Uses the Dynamic Linq query language to specify a filter and return
        paths. An empty request body queries all paths.
      operationId: query-paths-v2
      x-ni-operation: queryPaths
      x-ni-auth: true
      parameters:
        - in: body
          name: postBody
          description: Query filter
          required: false
          schema:
            $ref: '#/definitions/PathsAdvancedQuery'
      responses:
        200:
          $ref: '#/responses/PathsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=user/niuser.yaml sha256=84616f715efe728d07292eb7f2f5d8002a7559a9e9bf5a4136f2d5d6183decee bytes=28478 -->
## FILE: user/niuser.yaml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `user/niuser.yaml`
- sha256: `84616f715efe728d07292eb7f2f5d8002a7559a9e9bf5a4136f2d5d6183decee`
- bytes: 28478

````yaml
swagger: '2.0'
info:
  version: '1.0'
  title: SystemLink User Service
  description: 'Manage users, workspaces, and permissions for a SystemLink server.'
  contact:
    name: NI
    url: https://www.ni.com/systemlink
    email: support@ni.com
basePath: /niuser/v1
consumes:
  - application/json
produces:
  - application/json
securityDefinitions:
  ApiKeyAuth:
    type: apiKey
    name: x-ni-api-key
    in: header
  BasicAuth:
    type: basic
security:
  - ApiKeyAuth: []
  - BasicAuth: []
paths:
  '/users/query':
    post:
      tags:
        - users
      summary: Query the users
      description: >-
        Use the Dynamic Linq query language to specify filters for users.
        An empty request body queries all users.
      operationId: query-users
      parameters:
        - $ref: '#/parameters/QueryUsersRequest'
      responses:
        200:
          $ref: '#/responses/QueryUsersResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'

  '/users':
    post:
      tags:
        - users
      summary: Creates a new user
      description: Create a user
      operationId: create-user
      parameters:
        - $ref: '#/parameters/CreateUserRequest'
      responses:
        200:
          $ref: '#/responses/CreateUserResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'

  '/users/{id}':
    get:
      tags:
        - users
      summary: 'Get user'
      operationId: get-user
      description: Lookup a user by user id
      parameters:
        - in: path
          required: true
          name: id
          description: The user id
          type: string
      responses:
        200:
          $ref: '#/responses/GetUserResponse'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
    put:
      tags:
        - users
      summary: 'Update user'
      operationId: update-user
      description: Update the user record
      parameters:
        - $ref: '#/parameters/UserId'
        - $ref: '#/parameters/UpdateUserRequest'
      responses:
        200:
          $ref: '#/responses/UpdateUserResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
    delete:
      tags:
        - users
      summary: 'Delete user'
      description: Delete a user by user id
      operationId: delete-user
      parameters:
        - type: string
          required: true
          name: id
          in: path
          description: The user id
      responses:
        204:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'

  '/workspaces':
    get:
      tags:
        - workspaces
      summary: List workspaces
      description: List the workspaces of an organization
      operationId: get-workspaces
      parameters:
        - in: query
          name: name
          description: Filters the workspaces by name
          type: string
        - in: query
          name: skip
          description: How many workspaces to skip in the result when paging.
          type: integer
        - in: query
          name: take
          description: How many workspaces to return in the result.
          type: integer
          default: 50
          maximum: 100
        - in: query
          name: sortby
          description: The field name for sorting the results
          type: string
          enum: [name]
        - in: query
          name: order
          description: Sort by ascending or descending order
          type: string
          enum: [ascending, descending]
      responses:
        200:
          $ref: '#/responses/GetWorkspacesResponse'
        401:
          $ref: '#/responses/Unauthorized'
    post:
      tags:
        - workspaces
      summary: Creates a new workspace
      description: Create a workspace
      operationId: create-workspace
      parameters:
        - $ref: '#/parameters/CreateWorkspaceRequest'
      responses:
        200:
          $ref: '#/responses/CreateWorkspaceResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'

  '/workspaces/{id}':
    put:
      tags:
        - workspaces
      summary: 'Update workspace'
      operationId: update-workspace
      description: Update the workspace
      parameters:
        - $ref: '#/parameters/WorkspaceId'
        - $ref: '#/parameters/UpdateWorkspaceRequest'
      responses:
        200:
          $ref: '#/responses/UpdateWorkspaceResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'

  '/auth-mappings':
    get:
      tags:
        - auth-mappings
      summary: List auth-mappings
      description: List the auth-mappings of an organization
      operationId: get-auth-mappings
      parameters:
        - in: query
          name: workspace
          description: Filters the auth mappings by workspace
          type: string
        - in: query
          name: skip
          description: How many auth mappings to skip in the result when paging.
          type: integer
        - in: query
          name: take
          description: How many auth mappings to return in the result
          type: integer
          default: 50
          maximum: 100
        - in: query
          name: type
          description: Filters the auth mappings by type (multiple types can be specified with comma separator)
          type: string
      responses:
        200:
          $ref: '#/responses/GetAuthMappingsResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      tags:
        - auth-mappings
      summary: Creates a new auth-mapping
      description: Create a auth-mapping
      operationId: create-auth-mapping
      parameters:
        - $ref: '#/parameters/CreateAuthMappingRequest'
      responses:
        200:
          $ref: '#/responses/CreateAuthMappingResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'

  '/auth-mappings/{id}':
    put:
      tags:
        - auth-mappings
      summary: 'Update auth-mapping'
      operationId: update-auth-mapping
      description: Update the auth-mapping
      parameters:
        - $ref: '#/parameters/AuthMappingId'
        - $ref: '#/parameters/UpdateAuthMappingRequest'
      responses:
        200:
          $ref: '#/responses/UpdateAuthMappingResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
    delete:
      tags:
        - auth-mappings
      summary: Deletes an auth-mapping
      description: Deletes the auth-mapping with the given Id
      operationId: delete-auth-mapping
      parameters:
        - $ref: '#/parameters/AuthMappingId'
      responses:
        204:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'

  '/orgs/{name}':
    get:
      tags:
        - whitelisted operations
      summary: 'Get organization'
      operationId: get-org
      description: Returns the organization with the given name. The caller needs a whitelisted API key to read organizations.
      parameters:
        - in: path
          required: true
          name: name
          description: The org name, e.g. 'SystemLink Server'
          type: string
      responses:
        200:
          $ref: '#/responses/GetOrgResponse'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'

  '/websocket':
    get:
      tags:
        - web socket
      summary: Open a WebSocket session
      description: Opens a persistent connection to the web server that allows two-way communication using
                   a JSON protocol. After you open a connection, you can subscribe to workspace creation notifications.
                   Refer to the *Models* section to access the schema for these actions.
      operationId: OpenWebSocketSession
      parameters:
        - in: header
          name: Upgrade
          type: string
          required: true
          x-example: websocket
        - in: header
          name: Connection
          type: string
          required: true
          x-example: Upgrade
        - in: header
          name: Sec-WebSocket-Version
          description: Protocol version of the WebSocket connection.
          type: string
          required: true
          x-example: 13
        - in: header
          name: Sec-WebSocket-Key
          description: Randomly selected sixteen-byte base64-encoded string. Used to confirm a
            valid WebSocket handshake. Must be selected randomly for each new connection.
          type: string
          required: true
          x-example: dGhlIHNhbXBsZSBub25jZQ==
      responses:
        101:
          description: Switching Protocols
          headers:
            Sec-WebSocket-Accept:
              description: Used in the WebSocket opening handshake. Set to a value derived from the
                Sec-WebSocket-Key header.
              type: string
        401:
          $ref: '#/responses/Unauthorized'
        426:
          description: Upgrade Required
        default:
          $ref: '#/responses/Error'

parameters:
  UserId:
    in: path
    name: id
    description: The identifier of a user
    type: string
    required: true
  WorkspaceId:
    in: path
    name: id
    description: The identifier of a workspace
    type: string
    required: true
  AuthMappingId:
    in: path
    name: id
    description: The identifier of an auth mapping
    type: string
    required: true

  QueryUsersRequest:
    in: body
    name: queryUsersRequest
    description: Request to query for users
    schema:
      title: Query Users Request
      description: Filters to query for users
      type: object
      properties:
        filter:
          description: >-
              The filter criteria for users, consisting of a string of queries composed using AND/OR operators.
              String values need to be enclosed in double quotes.
              Parenthesis can be used within the filter to better define the order of operations.


              Filter syntax: '[property name][operator][operand] and [property name][operator][operand]'


              Operators:

              - Equals operator '='. Example: 'x = y'

              - Not equal operator '!='. Example: 'x != y'

              - Greater than operator '>'. Example: 'x > y'

              - Greater than or equal operator '>='. Example: 'x >= y'

              - Less than operator '<'. Example: 'x < y'

              - Less than or equal operator '<='. Example: 'x <= y'

              - Logical AND operator 'and'. Example: 'x and y'

              - Logical OR operator 'or'. Example: 'x or y'

              - Starts with operator '.StartsWith()', used to check whether a string starts with another string. Example: 'x.StartsWith(y)'

              - Does not start with operator '!.StartsWith()', used to check whether a string does not start with another string. Example: '!x.StartsWith(y)'

              - String null or empty 'string.IsNullOrEmpty()', used to check whether a string is null or empty. Example: 'string.IsNullOrEmpty(x)'

              - String is not null or empty '!string.IsNullOrEmpty()', used to check whether a string is not null or empty. Example: '!string.IsNullOrEmpty(x)'


              Valid user properties that can be used in the filter:

              - id

              - firstName

              - lastName

              - email

              - niuaId

              - login

              - status
          type: string
          example: firstName.StartsWith("John") && status == "active"
        take:
          description: The maximum number of users to return
          type: integer
          default: 50
          minimum: 0
          maximum: 100
          example: 10
        sortby:
          description: The field name for sorting the results
          type: string
          enum: [firstName, lastName, email, niuaId, login, status]
        order:
          description: Sort by ascending or descending order
          type: string
          enum: [ascending, descending]
        continuationToken:
          description: The continuation token can be used to paginate through the user query results. Provide this token in the next query users call.
          type: string
          example: token
  CreateUserRequest:
    in: body
    name: createUserRequest
    description: Request to create a new user
    schema:
      title: Create User Request
      description: Creates a new user in the callers' organization
      type: object
      properties:
        firstName:
          type: string
          description: First name filter
        lastName:
          type: string
          description: Last name filter
        email:
          type: string
          description: Email filter
        niuaId:
          type: string
          description: niua Id filter
        acceptedToS:
          type: boolean
          description: Filter for users which accepted or not accepted the terms of services
        policies:
          type: array
          items:
            type: string
          description: A list of policy ids. Defines the permissions of the user in the organization.
        keywords:
          type: array
          items:
            type: string
          description: A list of keywords associated with the user
        properties:
          type: object
          description: A map of key value properties
          additionalProperties:
            type: string
          example:
            key1: value1
  UpdateUserRequest:
    in: body
    name: updateUserRequest
    description: Request to update an existing user
    schema:
      title: Update User Request
      description: Updates an existing user
      type: object
      properties:
        firstName:
          type: string
          description: First name filter
        lastName:
          type: string
          description: Last name filter
        email:
          type: string
          description: Email filter
        acceptedToS:
          type: boolean
          description: Filter for users which accepted or not accepted the terms of services
        policies:
          type: array
          items:
            type: string
          description: A list of policy ids. Defines the permissions of the user in the organization.
        keywords:
          type: array
          items:
            type: string
          description: A list of keywords associated with the user
        properties:
          type: object
          description: A map of key value properties
          additionalProperties:
            type: string
          example:
            key1: value1

  CreateWorkspaceRequest:
    in: body
    name: createWorkspaceRequest
    description: Request to create a new workspace
    schema:
      title: Create Workspace Request
      description: Creates a new workspace
      type: object
      properties:
        name:
          type: string
          description: The workspace name, must be unique in the organization
  UpdateWorkspaceRequest:
    in: body
    name: updateWorkspaceRequest
    description: Request to update an existing workspace
    schema:
      title: Update Workspace Request
      description: Updates an existing workspace
      type: object
      properties:
        name:
          type: string
          description: The workspace name, must be unique in the organization
        enabled:
          type: boolean
          description: Whether the workspace is enabled or disabled. If a workspace is disabled, requests to create new resources in this workspace will fail but queries still return the resources in this workspace.

  CreateAuthMappingRequest:
    in: body
    name: createAuthMappingRequest
    description: Request to create a new auth mapping
    schema:
      title: Create Auth Mapping Request
      description: Creates a new auth mapping
      type: object
      properties:
        type:
          type: string
          enum: [user, windows-group, windows-user, ldap-group, ldap-attribute, ldap-user, oidc-claim, user-id]
          description: The Auth Mapping type
        policyId:
          type: string
          description: The policy id this mapping references.
        policyTemplateId:
          type: string
          description: The policy template id this mapping references.
        workspace:
          type: string
          description: The workspace id.
        selector:
          type: object
          description: The selector
          properties:
            key:
              type: string
              description: The Auth Mapping selector key
            value:
              type: string
              description: The Auth Mapping selector value

  UpdateAuthMappingRequest:
    in: body
    name: updateAuthMappingRequest
    description: Request to update an existing auth mapping
    schema:
      title: Update Auth Mapping Request
      description: Updates an existing auth mapping
      type: object
      properties:
        type:
          type: string
          enum: [user, windows-group, windows-user, ldap-group, ldap-attribute, ldap-user, oidc-claim, user-id]
          description: The Auth Mapping type
        policyId:
          type: string
          description: The policy id this mapping references.
        policyTemplateId:
          type: string
          description: The policy template id this mapping references.
        selector:
          type: object
          description: The selector
          properties:
            key:
              type: string
              description: The Auth Mapping selector key
            value:
              type: string
              description: The Auth Mapping selector value

responses:
  Unauthorized:
    description: API Key is missing or invalid
    schema:
      description: Error response
      title: ErrorResponse
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

  ValidationError:
    description: Invalid input data
    schema:
      description: Error response
      title: ErrorResponse
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

  NotFound:
    description: The resource was not found.
    schema:
      description: Error response
      title: ErrorResponse
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

  Error:
    description: Error Response
    schema:
      description: Error response
      title: ErrorResponse
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

  GetOrgResponse:
    description: Auth Response
    schema:
      $ref: '#/definitions/Org'

  QueryUsersResponse:
    description: Query Users Response
    schema:
      title: Query Users Response
      type: object
      properties:
        continuationToken:
          description: The continuation token can be used to paginate through the user list results. Provide this token in the next list users call.
          type: string
          example: token
        users:
          description: List of users
          type: array
          items:
            $ref: '#/definitions/User'
  CreateUserResponse:
    description: Create User Response
    schema:
      $ref: '#/definitions/User'
  GetUserResponse:
    description: Get User Response
    schema:
      $ref: '#/definitions/User'
  UpdateUserResponse:
    description: Update User Response
    schema:
      $ref: '#/definitions/User'

  GetWorkspacesResponse:
    description: Get Workspaces Response
    schema:
      title: Get Workspaces Response
      type: object
      properties:
        workspaces:
          description: List of workspaces
          type: array
          items:
            $ref: '#/definitions/Workspace'
  CreateWorkspaceResponse:
    description: Create Workspaces Response
    schema:
      $ref: '#/definitions/Workspace'
  UpdateWorkspaceResponse:
    description: Update Workspaces Response
    schema:
      $ref: '#/definitions/Workspace'

  GetAuthMappingsResponse:
    description: Get Auth Mappings Response
    schema:
      title: Get Auth Mappings Response
      type: object
      properties:
        authMappings:
          description: List of auth mappings
          type: array
          items:
            $ref: '#/definitions/AuthMapping'
  CreateAuthMappingResponse:
    description: Create Auth Mapping Response
    schema:
      $ref: '#/definitions/AuthMapping'
  UpdateAuthMappingResponse:
    description: Update Auth Mapping Response
    schema:
      $ref: '#/definitions/AuthMapping'
definitions:
  User:
    type: object
    title: User
    description: The user details
    properties:
      id:
        type: string
        description: The unique id
      firstName:
        type: string
        description: The first name
      lastName:
        type: string
        description: The last name
      email:
        type: string
        description: The email
      niuaId:
        type: string
        description: The external id (niuaId, SID, login name)
      acceptedToS:
        type: boolean
        description: Whether the user accepted the terms of service
      properties:
        type: object
        description: A map of key value properties associated with the user
      keywords:
        type: array
        items:
          type: string
        description: A list of keywords associated with the user
      created:
        type: string
        format: date-time
        description: The created timestamp
        example: "2019-12-02T15:31:45.379Z"
      updated:
        type: string
        format: date-time
        description: The last updated timestamp
        example: "2019-12-02T15:31:45.379Z"
      orgId:
        type: string
        description: The id of the organization
      policies:
        type: array
        items:
          type: string
        description: A list of policy ids
      status:
        type: string
        enum: [pending, active]
        description: The status of the users' registration
  Org:
    type: object
    title: Org
    description: Organization the user belongs to
    properties:
      id:
        type: string
        description: The unique id
      name:
        type: string
        description: The name of the organization
      owner:
        $ref: '#/definitions/User'
      workspaces:
        description: The list of workspaces in the organization
        type: array
        items:
          $ref: '#/definitions/Workspace'
  Workspace:
    type: object
    title: Workspace
    description: Information about the workspace
    properties:
      id:
        type: string
        description: The unique id
      name:
        type: string
        description: The workspace name
      enabled:
        type: boolean
        description: Whether the workspace is enabled or not
      default:
        type: boolean
        description: Whether the workspace is the default. The default workspace is used when callers omit a workspace id
  AuthMapping:
    type: object
    title: Auth Mapping
    description: Information about the auth mapping
    properties:
      id:
        type: string
        description: The unique id
      type:
        type: string
        description: The auth mapping type
      policyId:
        type: string
        description: The policy id this mapping references.
      policyTemplateId:
        type: string
        description: The policy template id this mapping references.
      workspace:
        type: string
        description: The workspace id.
      selector:
        type: object
        description: The selector
        properties:
          key:
            type: string
            description: The Auth Mapping selector key
          value:
            type: string
            description: The Auth Mapping selector value
  Error:
    description: Contains error information
    type: object
    properties:
      name:
        description: String error code
        type: string
      code:
        description: Numeric error code
        type: integer
        format: int32
      resourceType:
        description: Type of resource associated with the error
        type: string
      resourceId:
        description: Identifier of the resource associated with the error
        type: string
      message:
        description: Complete error message
        type: string
      args:
        description: Positional argument values for the error code
        type: array
        items:
          type: string
      innerErrors:
        type: array
        items:
          $ref: '#/definitions/Error'
    example:
      name: Auth.ServerError
      code: -12345
      message: There has been an error with your request
      args: []
      innerErrors: []

  WebSocketAsyncWorkspacesSubscribeRequest:
    title: Web Socket Workspaces Subscribe Request
    description: A web socket message sent by the client to subscribe to notifications when workspaces are created
    type: object
    required:
      - action
    properties:
      action:
        description: The action to perform. Must be set to "UserAsyncWorkspacesSubscribeRequest".
        type: string
        enum: ['UserAsyncWorkspacesSubscribeRequest']
        example: UserAsyncWorkspacesSubscribeRequest

  WebSocketAsyncWorkspacesSubscribeResponse:
    title: Web Socket Workspaces Subscribe Response
    description: A web socket message sent by the server to confirm a *WebSocketAsyncWorkspacesSubscribeRequest*.
    type: object
    properties:
      action:
        description: The action performed. Must be set to "UserAsyncWorkspacesSubscribeResponse".
        type: string
        enum: ['UserAsyncWorkspacesSubscribeResponse']
        example: UserAsyncWorkspacesSubscribeResponse

  WebSocketWorkspaceCreatedMessage:
    title: Web Socket Workspace Created Message
    description: A web socket message sent by the server when a new workspace is created.
    type: object
    properties:
      action:
        description: The action performed. Must be set to "UserWorkspacesCreatedRoutedMessage".
        type: string
        enum: ['UserWorkspacesCreatedRoutedMessage']
        example: UserWorkspacesCreatedRoutedMessage
      workspace:
        $ref: '#/definitions/Workspace'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=user-data/niuserdata.yml sha256=5d538a1c0a0cf1747734c4d8612b170deba29924b0cb8101760fc6230051db81 bytes=29413 -->
## FILE: user-data/niuserdata.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `user-data/niuserdata.yml`
- sha256: `5d538a1c0a0cf1747734c4d8612b170deba29924b0cb8101760fc6230051db81`
- bytes: 29413

````yaml
swagger: '2.0'
info:
  version: '1'
  title: User Data Service
  description: Manage user specific data.
  contact:
    name: NI
    url: https://www.ni.com/systemlink
    email: support@ni.com
basePath: /niuserdata
x-ni-routing-key: Skyline.UserData
consumes: [application/json]
produces: [application/json]

securityDefinitions:
  apiKeyAuth:
    type: apiKey
    name: x-ni-api-key
    in: header
  basicAuth:
    type: basic
  cookieAuth:
    type: apiKey
    in: header
    name: Cookie

security:
  - apiKeyAuth: []        
  - basicAuth: []
  - cookieAuth: []

definitions:
  Error:
    title: Error
    description: Contains error information.
    type: object
    properties:
      name:
        description: String error code
        type: string
        example: Skyline.OneOrMoreErrorsOccurred
      code:
        description: Numeric error code
        type: integer
        format: int32
        example: -251040
      resourceType:
        description: Type of resource associated with the error
        type: string
        example: UserDataItem
      resourceId:
        description: Identifier of the resource associated with the error
        type: string
        example: '5c4b2c0756c8b455a8f849c4'
      message:
        description: Complete error message
        type: string
        example: One or more errors occurred. See the contained list for details of each error
      args:
        description: Positional argument values for the error code
        type: array
        items:
          type: string
          example: '5c4b2c0756c8b455a8f849c4'
      innerErrors:
        type: array
        example:
          - name: Skyline.InsufficientPrivileges
            code: -251009
            resourceType: string
            resourceId: '5c4b2c0756c8b455a8f849c4'
            message: Insufficient privileges.
            args: []
        items:
          $ref: '#/definitions/Error'
    example:
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251040
      message: One or more errors occurred. See the contained list for details of each error.
      args: []
      innerErrors:
        - name: Skyline.InsufficientPrivileges
          code: -251009
          resourceType: string
          resourceId: '5c4b2c0756c8b455a8f849c4'
          message: Insufficient privileges.
          args: []
  Operation:
    title: Operation
    description: An operation provided by the API
    type: object
    required:
      - available
    properties:
      available:
        description: Whether the operation is available to the caller
        type: boolean
        example: true
      version:
        description: Version of the available operation
        type: integer
        format: int32
        default: 1
        example: 1
    example:
      available: true
      version: 1
  V1Operations:
    title: Version 1 Operations
    description: V1 operations
    type: object
    properties:
      operations:
        description: >-
          Available operations in the v1 version of the API:

          - queryUserDataItems: Query a set of user data items

          - createOrUpdateUserDataItems: Create or update a set of user data items

          - deleteUserDataItems: Delete a set of user data items
        type: object
        properties:
          queryUserDataItems:
            $ref: '#/definitions/Operation'
          createOrUpdateUserDataItems:
            $ref: '#/definitions/Operation'
          deleteUserDataItems:
            $ref: '#/definitions/Operation'
  QueryOperation:
    title: Query Operation
    description: >-
      Query operation enum. Note that 'LESS_THAN', 'GREATER_THAN', 'LESS_THAN_OR_EQUAL', and
      'GREATER_THAN_OR_EQUAL' are only supported when the data type of the comparison is a string,
      ISO date time, or numeric value. These are not supported on booleans, arrays, or objects
      (also known as dictionaries).
    type: string
    enum:
      - EQUAL
      - NOT_EQUAL
      - LESS_THAN
      - GREATER_THAN
      - LESS_THAN_OR_EQUAL
      - GREATER_THAN_OR_EQUAL
  IntegerQueryObject:
    title: Integer Query
    description: Integer query object
    type: object
    required:
      - operation
      - comparisonValue
    properties:
      operation:
        $ref: '#/definitions/QueryOperation'
      comparisonValue:
        description: Integer value to compare
        type: integer
        format: int64
        example: 360
  JsonQueryObject:
    title: JSON Query
    description: >-
      JSON query object. This is used when querying a field that can be any valid JSON type.
    type: object
    required:
      - operation
      - comparisonValue
    properties:
      operation:
        $ref: '#/definitions/QueryOperation'
      comparisonValue:
        description: >-
          Value to compare. This can be any valid JSON type. The type of this must match the type
          of the data being compared to.
        type: object
        example: 'john.smith@company.com'
  TimeQueryObject:
    title: Time Query
    description: Time query object
    type: object
    required:
      - operation
      - comparisonValue
    properties:
      operation:
        $ref: '#/definitions/QueryOperation'
      comparisonValue:
        description: ISO-8601 formatted timestamp value to compare.
        type: string
        format: date-time
        example: '2017-11-14T15:41:06.106Z'
  UserDataItemField:
    title: User Data Item Field
    description: User data item field enum
    type: string
    enum:
      - ID
      - USER
      - APPLICATION
      - CATEGORY
      - NAME
      - VALUE
      - VISIBLE_TO_OTHERS
      - REVISION
      - CREATED_AT
      - UPDATED_AT
  UserDataItemSortField:
    title: User Data Item Sort Field
    description: User data item sort field enum
    type: string
    enum:
      - ID
      - USER
      - APPLICATION
      - CATEGORY
      - NAME
      - VISIBLE_TO_OTHERS
      - REVISION
      - CREATED_AT
      - UPDATED_AT
  UserDataItemSortDefinitionObject:
    title: User Data Item Sort Definition
    description: Defines the field and direction for sorting user data items.
    type: object
    required:
      - field
    properties:
      field:
        $ref: '#/definitions/UserDataItemSortField'
      orderByDescending:
        description: >-
          Whether to sort descending instead of ascending.
          The elements in the list are sorted ascending by default. If the
          orderByDescending parameter is specified, the elements in the list
          are sorted based on its value. The orderByDescending value must be
          a boolean string. The elements in the list are sorted ascending if
          false and descending if true.
        type: boolean
        default: false
  UserDataItemQueryObject:
    title: User Data Item Query
    type: object
    properties:
      ids:
        description: Array of user data item IDs
        type: array
        items:
          type: string
        example:
          - '5c4b2c0756c8b455a8f849c4'
          - '5c4ed77d56c8b455a80f86b5'
          - '5c4ed78f56c8b455a80f870a'
      applications:
        description: Array of application names
        type: array
        items:
          type: string
        example:
          - 'ni-swif'
          - 'ni-test-management'
      categories:
        description: Array of category names
        type: array
        items:
          type: string
        example:
          - 'reports'
          - 'states'
      names:
        description: Array of user data item names
        type: array
        items:
          type: string
        example:
          - 'email'
          - 'language'
      valueQuery:
        description: >-
          Array of JSON query objects to query against the values of the user data items.
        type: array
        items:
          $ref: '#/definitions/JsonQueryObject'
      visibleToOthers:
        description: >-
          Match against the 'visibleToOthers' field in the user item data. If not set, will match
          both true and false values.
        type: boolean
        example: true
      revisionQuery:
        description: >-
          Array of integer query objects used to query the revision of the user data items.
        type: array
        items:
          $ref: '#/definitions/IntegerQueryObject'
      createdAtQuery:
        description: >-
          Array of time query objects used to query when the user data items were created.
        type: array
        items:
          $ref: '#/definitions/TimeQueryObject'
      updatedAtQuery:
        description: >-
          Array of time query objects used to query when the user data items were last updated.
        type: array
        items:
          $ref: '#/definitions/TimeQueryObject'
      sortBy:
        description: >-
          Array of user data item sort definition objects to define how to sort the results.
        type: array
        items:
          $ref: '#/definitions/UserDataItemSortDefinitionObject'
      projection:
        description: >-
          Array of user data item fields. If you specify an array, the query returns a result with
          the user data items containing the fields that are both specified and available. If you
          do not specify an array, the query will return a result with the user data items
          containing all available fields.
        type: array
        items:
          $ref: '#/definitions/UserDataItemField'
  UserDataItem:
    title: User Data Item
    description: >-
       Information about a specific user data item. A specific user data item may be uniquely
       identified by a combination of its 'user', 'application', 'category', and 'name' fields.
       A specific user data item is also uniquely identified by its assigned ID.
    type: object
    properties:
      id:
        description: The ID for this user data item.
        type: string
        example: '5c4b2c0756c8b455a8f849c4'
      user:
        description: >-
          The user that this data item belongs to.
        type: string
        example: jsmith
      application:
        description: >-
          The application name that this user data item belongs to.
        type: string
        example: 'ni-test-management'
      category:
        description: >-
          The category name in the application that this user data item belongs to. An empty category
          name is accepted.
        type: string
        example: 'reports'
        default: ''
      name:
        description: The name of the user data item.
        type: string
        example: 'email'
      value:
        description: The value of the user data item.
        type: object
        example: 'john.smith@company.com'
      visibleToOthers:
        description: >-
          Whether this user data item is visible to other users. This will allow other users to
          query this data.
        type: boolean
        example: false
      revision:
        description: >-
          The revision number for this user data item. When a user data item is created, the
          revision number starts at 1. Every time it is updated, the revision number is
          incremented by 1.
        type: integer
        format: int64
        example: 1
      createdAt:
        description: ISO-8601 formatted timestamp specifying when the user data item was created.
        type: string
        format: date-time
        example: '2017-11-14T15:41:06.106Z'
      updatedAt:
        description: >-
          ISO-8601 formatted timestamp specifying when the user data item was last updated.
        type: string
        format: date-time
        example: '2017-11-14T15:41:06.106Z'
  CreateOrUpdateUserDataItem:
    title: Create or Update User Data Item
    description: >-
      Create or update a specific user data item. User data items are unique to the currently
      logged in user. The combination of the 'application', 'category', and 'name' fields identify
      the specific item to create or update.
    type: object
    required:
      - application
      - name
      - value
    properties:
      application:
        description: >-
          The application name that this user data item belongs to.
        type: string
        example: 'ni-test-management'
      category:
        description: >-
          The category name in the application that this user data item belongs to. An empty category
          name is accepted.
        type: string
        example: 'reports'
        default: ''
      name:
        description: The name of the user data item.
        type: string
        example: 'email'
      value:
        description: The value of the user data item.
        type: object
        example: 'john.smith@company.com'
      visibleToOthers:
        description: >-
          Whether this user data item is visible to other users. This will allow other users to
          query this data.
        type: boolean
        example: false
      expectedRevision:
        description: >-
          This is an optional value. When specified, this is an integer that should be set to
          match the last known revision number of the user data item. If it doesn't match at the
          time of execution, the update request will be rejected. This is used to ensure that
          changes to this user data item are correctly using the previous state. This may be
          important, for instance, in the case where multiple clients are updating an array value
          at the same time. A value of 0 means that the item must not already exist.
        type: integer
        format: int64
        minimum: 0
        example: 5
  UpdateUserDataItem:
    title: Update User Data Item
    description: >-
       Update a specific user data item.
    type: object
    required:
      - id
      - value
    properties:
      id:
        description: The ID for this user data item.
        type: string
        example: '5c4b2c0756c8b455a8f849c4'
      value:
        description: The value of the user data item.
        type: object
        example: 'john.smith@company.com'
      visibleToOthers:
        description: >-
          Whether this user data item is visible to other users. This will allow other users to
          query this data.
        type: boolean
        example: false
      expectedRevision:
        description: >-
          This is an optional value. When specified, this is an integer that should be set to
          match the last known revision number of the user data item. If it doesn't match at the
          time of execution, the update request will be rejected. This is used to ensure that
          changes to this user data item are correctly using the previous state. This may be
          important, for instance, in the case where multiple clients are updating an array value
          at the same time.
        type: integer
        format: int64
        minimum: 1
        example: 5
  CreateOrUpdateUserDataItemsPartialSuccessResponse:
    title: Create or Update User Data Items Partial Success Response
    description: Create or update user data items partial success response
    type: object
    required:
      - succeeded
      - failed
      - error
    properties:
      succeeded:
        description: Array of user data items that were created or updated.
        type: array
        items:
          $ref: '#/definitions/UserDataItem'
      failed:
        description: Array of user data item create or update requests that failed.
        type: array
        items:
          $ref: '#/definitions/CreateOrUpdateUserDataItem'
      error:
        $ref: '#/definitions/Error'
  UpdateUserDataItemsPartialSuccessResponse:
    title: Update User Data Items Partial Success Response
    description: Update user data items partial success response
    type: object
    required:
      - succeeded
      - failed
      - error
    properties:
      succeeded:
        description: Array of user data item IDs that were updated.
        type: array
        items:
          type: string
        example:
          - '5c4b2c0756c8b455a8f849c4'
          - '5c4ed77d56c8b455a80f86b5'
          - '5c4ed78f56c8b455a80f870a'
      failed:
        description: Array of user data item update requests that failed.
        type: array
        items:
          $ref: '#/definitions/UpdateUserDataItem'
      error:
        $ref: '#/definitions/Error'
  DeleteUserDataItemsPartialSuccessResponse:
    title: Delete User Data Items Partial Success Response
    description: Delete user data items partial success response
    type: object
    required:
      - succeeded
      - failed
      - error
    properties:
      succeeded:
        description: Array of user data item IDs that were successfully deleted
        type: array
        items:
          type: string
        example:
          - '5c4b2c0756c8b455a8f849c4'
          - '5c4ed77d56c8b455a80f86b5'
          - '5c4ed78f56c8b455a80f870a'
      failed:
        description: Array of user data item IDs that failed to delete
        type: array
        items:
          type: string
        example:
          - '5c4ed7a256c8b455a80f87a5'
          - '5c4ed7b356c8b455a80f887f'
      error:
        $ref: '#/definitions/Error'

parameters:
  userDataItemId:
    in: path
    name: id
    description: The ID of a specific user data item.
    type: string
    required: true
    x-example: '5c4b2c0756c8b455a8f849c4'

responses:
  Error:
    description: Error definition object
    schema:
      description: Error response
      title: ErrorResponse
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
  Unauthorized:
    description: Not authorized
    headers:
      WWW_Authenticate:
        description: Information for how to authenticate
        type: string

paths:
  /:
    get:
      operationId: RootEndpoint
      summary: API information
      description: Returns information about API versions and available operations.
      tags: [versioning]
      security: []
      responses:
        200:
          description: OK
          schema:
            description: Version information
            title: RootEndpointResponse
            type: object
            properties:
              v1:
                $ref: '#/definitions/V1Operations'
              version:
                description: Implementation version of the web service
                type: string
  /{version}:
    parameters:
      - in: path
        name: version
        description: Version of the API to retrieve operations
        type: string
        required: true
    get:
      operationId: RootEndpointWithVersion
      summary: API version information
      description: Returns available operations for a single version of the API
      tags: [versioning]
      security: []
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/V1Operations'
        404:
          description: Not Found
          schema:
            $ref: '#/definitions/Error'
  /v1/items:
    get:
      operationId: GetUserDataItems
      x-ni-operation: queryUserDataItems
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      summary: Get All User Data Items
      description: >-
        Get all the visible the user data items. Which items are visible are according to the
        access level of the logged in user.

        Use the skip and take parameters to return paged responses.

        The orderBy and orderByDescending fields can be used to manage sorting
        the list by specific fields.
      tags: [user-data]
      parameters:
        - in: query
          name: skip
          description: >-
            How many user data items to skip in the result when paging.
            For example, a list of 100 user data items with a skip value of 50 and a take
            value of 25 will return entries 51 through 75.
          type: integer
          format: int32
          default: 0
          minimum: 0
        - in: query
          name: take
          description: >-
            How many user data items to return in the result.
            For example, a list of 100 user data items with a skip value of 50 and a take
            value of 25 will return entries 51 through 75.
          type: integer
          format: int32
          minimum: 0
        - in: query
          name: sortBy
          description: The name of the field to sort by.
          type: string
          enum:
            - ID
            - USER
            - APPLICATION
            - CATEGORY
            - NAME
            - VISIBLE_TO_OTHERS
            - REVISION
            - CREATED_AT
            - UPDATED_AT
        - in: query
          name: orderByDescending
          description: >-
            Whether to sort descending instead of ascending.
            The elements in the list are sorted ascending by default. If the
            orderByDescending parameter is specified, the elements in the list
            are sorted based on its value. The orderByDescending value must be
            a boolean string. The elements in the list are sorted ascending if
            false and descending if true.
          type: boolean
          default: false
      responses:
        200:
          description: OK
          schema:
            description: User data item information
            title: QueryUserDataItemsResponse
            type: object
            required:
              - items
              - totalCount
            properties:
              items:
                description: Array of user data items
                type: array
                items:
                  $ref: '#/definitions/UserDataItem'
              totalCount:
                description: Number of matching user data items
                type: integer
                format: int64
    post:
      operationId: CreateOrUpdateUserDataItems
      x-ni-operation: createOrUpdateUserDataItems
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      summary: Create or update one or more user data items
      description: >-
        Creates one or more user data items.
      tags: [user-data]
      parameters:
        - in: body
          name: createOrUpdateUserDataItems
          description: Array of data item information for creation or update.
          required: true
          schema:
            description: Array of data item information for creation or update.
            title: CreateOrUpdateUserDataItemsRequest
            type: array
            items:
              $ref: '#/definitions/CreateOrUpdateUserDataItem'
            minItems: 1
      responses:
        201:
          description: Created
          schema:
            description: Array of user data items that were created or updated.
            title: CreateOrUpdateUserDataItemsResponse
            type: array
            items:
              $ref: '#/definitions/UserDataItem'
        200:
          description: Partial success
          schema:
            $ref: '#/definitions/CreateOrUpdateUserDataItemsPartialSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/items/{id}:
    parameters:
      - $ref: '#/parameters/userDataItemId'
    get:
      operationId: GetUserDataItem
      x-ni-operation: queryUserDataItems
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      summary: Get information about the specified user data item
      description: >-
        Get information about the specified user data item.
      tags: [user-data]
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/UserDataItem'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      operationId: DeleteUserDataItem
      x-ni-operation: deleteUserDataItems
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      summary: Delete the specified user data item
      description: Deletes the specified user data item.
      tags: [user-data]
      responses:
        204:
          description: No content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/query-items:
    post:
      operationId: QueryUserDataItems
      x-ni-operation: queryUserDataItems
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      summary: Query User Data Items
      description: Queries the user data items.
      tags: [user-data]
      parameters:
        - in: body
          name: queryUserDataItems
          description: User data item query object
          required: true
          schema:
            $ref: '#/definitions/UserDataItemQueryObject'
        - in: query
          name: skip
          description: >-
            How many user data items to skip in the result when paging.
            For example, a list of 100 user data items with a skip value of 50 and a take
            value of 25 will return entries 51 through 75.
          type: integer
          format: int32
          default: 0
          minimum: 0
        - in: query
          name: take
          description: >-
            How many user data items to return in the result.
            For example, a list of 100 user data items with a skip value of 50 and a take
            value of 25 will return entries 51 through 75.
          type: integer
          format: int32
          minimum: 0
      responses:
        200:
          description: OK
          schema:
            description: User data item information
            title: QueryUserDataItemsResponse
            type: object
            required:
              - items
              - totalCount
            properties:
              items:
                description: Array of user data items
                type: array
                items:
                  $ref: '#/definitions/UserDataItem'
              totalCount:
                description: Number of matching user data items
                type: integer
                format: int64
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/update-items:
    post:
      operationId: UpdateUserDataItems
      x-ni-operation: createOrUpdateUserDataItems
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      summary: Update one or more user data items
      description: >-
        Updates one or more user data items.
      tags: [user-data]
      parameters:
        - in: body
          name: updateUserDataItems
          description: Array of data item information for update.
          required: true
          schema:
            description: Array of data item information for update.
            title: UpdateUserDataItemsRequest
            type: array
            items:
              $ref: '#/definitions/UpdateUserDataItem'
            minItems: 1
      responses:
        204:
          description: No content
        200:
          description: Partial success
          schema:
            $ref: '#/definitions/UpdateUserDataItemsPartialSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/delete-items:
    post:
      operationId: DeleteUserDataItems
      x-ni-operation: deleteUserDataItems
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      summary: Delete user data items
      description: >-
        Deletes multiple user data items in a single API call.
      tags: [user-data]
      parameters:
        - in: body
          name: items
          description: Array of user data item IDs to delete.
          required: true
          schema:
            description: Array of user data item IDs to delete.
            title: DeleteUserDataItemsRequest
            type: array
            items:
              description: The ID of a user data item to delete.
              type: string
              example: '5c4b2c0756c8b455a8f849c4'
            minItems: 1
      responses:
        204:
          description: No content
        200:
          description: Partial success
          schema:
            $ref: '#/definitions/DeleteUserDataItemsPartialSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=webapp/niapp.yaml sha256=0eb5175d82173f9d1f4ef4403ff25863bae78039840da632c08e25cefd9fda32 bytes=21245 -->
## FILE: webapp/niapp.yaml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `webapp/niapp.yaml`
- sha256: `0eb5175d82173f9d1f4ef4403ff25863bae78039840da632c08e25cefd9fda32`
- bytes: 21245

````yaml
swagger: '2.0'
info:
  version: '1.0'
  title: SystemLink WebApp Service
basePath: /niapp/v1
consumes:
  - application/json
produces:
  - application/json
securityDefinitions:
  ApiKeyAuth:
    type: apiKey
    name: x-ni-api-key
    in: header
  BasicAuth:
    type: basic
security:
  - ApiKeyAuth: []
  - BasicAuth: []
paths:
  '/webapps/{id}':
    get:
      tags:
        - metadata
      summary: Get webapp metadata by Id
      description: Get webapp metadata by Id
      operationId: get-webapp
      parameters:
        - $ref: '#/parameters/WebAppId'
      responses:
        200:
          $ref: '#/responses/GetWebAppResponse'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
    put:
      tags:
        - metadata
      summary: Update webapp metadata by Id
      description: Update existing webapp metadata
      operationId: update-webapp
      parameters:
        - $ref: '#/parameters/WebAppId'
        - $ref: '#/parameters/UpdateWebAppRequest'
      responses:
        200:
          $ref: '#/responses/UpdateWebAppResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
    delete:
      tags:
        - metadata
      summary: Delete webapp by Id
      description: Delete existing webapp metadata and content
      operationId: delete-webapp
      parameters:
        - $ref: '#/parameters/WebAppId'
      responses:
        200:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  '/webapps':
    get:
      tags:
        - metadata
      summary: List the webapps
      description: List the webapps
      operationId: list-webapps
      parameters:
        - in: query
          name: name
          description: Filters the webapps by name
          type: string
        - in: query
          name: type
          description: Filters the webapps by type
          type: string
          enum:
          - Dashboard
          - DashboardTemplate
          - WebVI
        - in: query
          name: userId
          description: Filters the webapps by the user Id of the owner
          type: string
        - in: query
          name: workspace
          description: Filters the webapps by workspace Id
          type: string
        - in: query
          name: continuationToken
          description: The continuation token can be used to paginate through the webapp list results. Provide a token to continue a previous listing.
          type: string
        - in: query
          name: take
          description: The maximum number of webapps to return
          type: integer
          default: 100
          minimum: 0
          maximum: 1000
      responses:
        200:
          $ref: '#/responses/ListWebAppsResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      tags:
        - metadata
      summary: Create a new webapp
      description: Create a new webapp
      operationId: create-webapp
      parameters:
        - $ref: '#/parameters/CreateWebAppRequest'
      responses:
        200:
          $ref: '#/responses/CreateWebAppResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  '/webapps/query':
    post:
      tags:
        - metadata
      summary: Query the webapps
      description: >-
        Use the Dynamic Linq query language to specify filters for webapps.
        An empty request body queries all webapps.
      operationId: query
      parameters:
        - in: body
          name: postBody
          description: Query filter
          required: false
          schema:
            $ref: '#/definitions/WebAppsAdvancedQuery'
      responses:
        200:
          $ref: '#/responses/ListWebAppsResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  '/webapps/{id}/sharing':
    put:
      tags:
        - metadata
      summary: Update sharing settings of the webapp
      description: Update sharing settings of the webapp
      operationId: update-webapp-sharing
      parameters:
        - $ref: '#/parameters/WebAppId'
        - $ref: '#/parameters/UpdateWebAppSharingRequest'
      responses:
        200:
          $ref: '#/responses/UpdateWebAppSharingResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  '/webapps/shared-emails':
    get:
      tags:
        - metadata
      summary: List the emails with which the user has shared webapps
      description: List the emails with which the user has shared webapps
      operationId: list-shared-emails
      responses:
        200:
          $ref: '#/responses/SharedEmailsResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  '/webapps/import':
    post:
      tags:
        - metadata
      summary: Import webapp metadata
      description: >-
        Import a list of webapp metadata.

        The webapp Id, created timestamp, and updated timestamp are optional. These fields will be generated by the service if they are not provided in the request.
      operationId: import-webapps
      parameters:
        - $ref: '#/parameters/ImportWebAppsRequest'
      responses:
        200:
          $ref: '#/responses/ImportWebAppsResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  '/webapps/{id}/content':
    get:
      tags:
        - content
      summary: Get webapp content
      description: Get the content of a webapp. ContentType varies from JSON for dashboards and templates or redirect to main HTML for WebVIs
      operationId: get-content-index
      parameters:
        - $ref: '#/parameters/WebAppId'
      responses:
        200:
          description: The webapp's content. JSON for Dashboards, HTML for WebVIs
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
    put:
      tags:
        - content
      summary: Upload content for an existing webapp
      description: Upload content for an existing webapp
      operationId: update-content
      parameters:
        - $ref: '#/parameters/WebAppId'
        - in: body
          required: true
          name: content
          description: The webapp content to upload
          schema:
            $ref: '#/definitions/WebAppContent'
      responses:
        200:
          description: Success
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  '/webapps/{id}/content/{path}':
    get:
      tags:
        - content
      summary: Get webapp content by path
      description: Get the webapp content at a path. This applies to webapps with multiple files, such as WebVIs.
      operationId: get-content
      parameters:
        - $ref: '#/parameters/WebAppId'
        - $ref: '#/parameters/WebAppContentPath'
      responses:
        200:
          $ref: '#/definitions/WebAppContent'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'

  '/webapps/{sourceId}/duplicate':
    post:
      tags:
        - content
      summary: Duplicate webapp
      description: Duplicate a webapp by creating new webapp metadata with the specified name and duplicating existing content into the new webapp.
      operationId: duplicate-webapp
      parameters:
        - in: path
          type: string
          required: true
          name: sourceId
          description: The Id of the source webapp to copy content from
        - $ref: '#/parameters/DuplicateWebAppRequest'
      responses:
        200:
          $ref: '#/responses/CreateWebAppResponse'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  '/webapps/{id}/duplicate/{sourceId}':
    post:
      tags:
        - content
      summary: Duplicate webapp content
      description: Duplicate webapp content
      operationId: duplicate-content
      parameters:
        - $ref: '#/parameters/WebAppId'
        - in: path
          type: string
          required: true
          name: sourceId
          description: The Id of the source webapp to copy content from
      responses:
        200:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'

parameters:
  WebAppId:
    in: path
    name: id
    description: The webapp identifier
    type: string
    required: true
  WebAppContentPath:
    in: path
    name: path
    description: Path to webapp content
    type: string
    required: true
  CreateWebAppRequest:
    in: body
    name: CreateWebAppRequest
    description: Create WebApp Request
    schema:
      type: object
      title: Create WebApp Request
      properties:
        name:
          type: string
          description: The webapp's name
          example: My webapp
        workspace:
          type: string
          description: The workspace Id for the webapp. If this is not specified, the webapp will be created in the default workspace.
          example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
        policyIds:
          type: array
          items:
            type: string
            example: "asdsad-17a6-45323-b64b-65325287372d"
          description: List of policy Ids associated with the webapp, which give it access to the user's resources"
        properties:
          type: object
          description: A map of key value properties associated with the webapp
          additionalProperties:
            type: string
          example:
            key1: value1
  UpdateWebAppRequest:
    in: body
    name: UpdateWebAppRequest
    description: Update WebApp Request
    schema:
      type: object
      title: Update WebApp Request
      properties:
        name:
          type: string
          description: The webapp's name
          example: My webapp
        workspace:
          type: string
          description: The workspace Id for the webapp. If this is not specified, the webapp will remain in its existing workspace.
          example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
        policyIds:
          type: array
          items:
            type: string
            example: "asdsad-17a6-45323-b64b-65325287372d"
          description: List of policy Ids associated with the webapp, which give it access to the user's resources"
        properties:
          type: object
          description: A map of key value properties associated with the webapp
          additionalProperties:
            type: string
          example:
            key1: value1
  UpdateWebAppSharingRequest:
    in: body
    name: UpdateWebAppSharingRequest
    description: Update WebApp Sharing Request
    schema:
      type: object
      title: Update WebApp Sharing Request
      properties:
        shared:
          type: string
          enum:
            - private
            - direct
            - public
          example: direct
          description: The webapp's sharing option
        sharedEmails:
          type: array
          items:
            type: string
            example: john.doe@email.com
          description: List of emails of users to share the webapp with. Applies when "shared" option is "direct"
  ImportWebAppsRequest:
    in: body
    name: ImportWebAppsRequest
    description: Import WebApp Metadata Request
    schema:
      type: object
      title: Import WebApp Metadata Request
      properties:
        webapps:
          description: List of webapps to import
          type: array
          items:
            $ref: '#/definitions/WebApp'
  DuplicateWebAppRequest:
    in: body
    name: DuplicateWebAppRequest
    description: Duplicate WebApp Request
    schema:
      type: object
      title: Duplicate WebApp Request
      properties:
        name:
          type: string
          description: The name of the new webapp created during the duplication
          example: My webapp name
        workspace:
          type: string
          description: The Id of the workspace in which to create the new webapp. If no workspace is specified, the new webapp will be put in the default workspace.
          example: 0c80cf49-54e9-4e92-b117-3bfa574caa84

responses:
  Error:
    description: Error
    schema:
      description: Error response
      title: ErrorResponse
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
  Unauthorized:
    description: API Key is missing or invalid
  NotFound:
    description: The resource was not found.
  ValidationError:
    description: Invalid input data
  GetWebAppResponse:
    description: Get WebApp Response
    schema:
      $ref: '#/definitions/WebApp'
  CreateWebAppResponse:
    description: Create WebApp Response
    schema:
      $ref: '#/definitions/WebApp'
  ImportWebAppsResponse:
    description: Import WebApps Response
    schema:
      title: Import WebApps Response
      type: object
      properties:
        webapps:
          description: List of webapps that were imported
          type: array
          items:
            $ref: '#/definitions/WebApp'
  UpdateWebAppResponse:
    description: Update WebApp Response
    schema:
      $ref: '#/definitions/WebApp'
  UpdateWebAppSharingResponse:
    description: Update WebApp Sharing Response
    schema:
      $ref: '#/definitions/WebApp'
  ListWebAppsResponse:
    description: List WebApps Response
    schema:
      title: List WebApps Response
      type: object
      properties:
        webapps:
          description: List of webapps
          type: array
          items:
            $ref: '#/definitions/WebApp'
        continuationToken:
          description: The continuation token can be used to paginate through the webapp list results. Provide this token in the next list webapps call.
          type: string
          example: token
  SharedEmailsResponse:
    description: Shared Emails Response
    schema:
      title: Shared Emails Response
      type: array
      items:
        type: string
        example: john.doe@email.com

definitions:
  WebApp:
    type: object
    title: WebApp Metadata
    properties:
      id :
        type: string
        description: The webapp Id
        example: "asdsad-17a6-45323-b64b-65325287372d"
      type:
        type: string
        enum:
          - Dashboard
          - TileDashboard
          - DashboardTemplate
          - WebVI
          - Visualization
          - VisualizationTemplate
        description: The webapp type
      name:
        type: string
        description: The webapp name
        example: My webapp
      workspace:
        type: string
        description: The Id of the workspace containing the webapp
        example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
      userId:
        type: string
        description: The Id of the user that created the webapp
        example: d4f6b766-da45-4fe5-85c5-bd745c402cf9
      shared:
        type: string
        enum:
          - private
          - direct
          - public
        description: The webapp's sharing option
      sharedEmails:
        type: array
        items:
          type: string
          example: john.doe@ni.com
        description: List of emails of users to share the webapp with. Applies when "shared" option is "direct"
      policyIds:
        type: array
        items:
          type: string
          example: asdsad-17a6-45323-b64b-65325287372d
        description: List of policy Ids associated with the webapp, which give it access to the user's resources"
      created:
        type: string
        format: date-time
        description: The created timestamp (iso8601 format)
        example: "2019-12-02T15:31:45.379Z"
      updated:
        type: string
        format: date-time
        description: The last updated timestamp (iso8601 format)
        example: "2019-12-02T15:31:45.379Z"
      properties:
        type: object
        description: A map of key value properties associated with the webapp
  WebAppContent:
    type: string
    format: binary
    title: WebApp Content
    description: The webapp binary content. Depending on the webapp's type it can be a dashboard, template or *.nipkg file exported from LabVIEW NXG
  WebAppsAdvancedQuery:
    type: object
    title: Advanced Query Object for WebApps
    properties:
      filter:
        description: >-
            The filter criteria for webapps, consisting of a string of queries composed using AND/OR operators.
            String values need to be enclosed in double quotes.
            Parenthesis can be used within the filter to better define the order of operations.


            Filter syntax: '[property name][operator][operand] and [property name][operator][operand]'

            Operators:

            - Equals operator '='. Example: 'x = y'

            - Not equal operator '!='. Example: 'x != y'

            - Greater than operator '>'. Example: 'x > y'

            - Greater than or equal operator '>='. Example: 'x >= y'

            - Less than operator '<'. Example: 'x < y'

            - Less than or equal operator '<='. Example: 'x <= y'

            - Logical AND operator 'and'. Example: 'x and y'

            - Logical OR operator 'or'. Example: 'x or y'

            - Starts with operator '.StartsWith()', used to check whether a string starts with another string. Example: 'x.StartsWith(y)'

            - Does not start with operator '!.StartsWith()', used to check whether a string does not start with another string. Example: '!x.StartsWith(y)'

            - String null or empty 'string.IsNullOrEmpty()', used to check whether a string is null or empty. Example: 'string.IsNullOrEmpty(x)'

            - String is not null or empty '!string.IsNullOrEmpty()', used to check whether a string is not null or empty. Example: '!string.IsNullOrEmpty(x)'


            Valid webapp properties that can be used in the filter:

            - id

            - name

            - properties.embedLocation

            - shared

            - type

            - workspace
        type: string
        example: name.StartsWith("myWebApp") || type == "WebVI"
      take:
        description: The maximum number of webapps to return
        type: integer
        default: 100
        minimum: 0
        maximum: 1000
        example: 10
      continuationToken:
        description: The continuation token can be used to paginate through the webapp query results. Provide this token in the next query webapps call.
        type: string
        example: token
  Error:
    description: Contains error information
    type: object
    properties:
      name:
        description: String error code
        type: string
      code:
        description: Numeric error code
        type: integer
      message:
        description: Complete error message
        type: string
      args:
        description: Positional argument values for the error code
        type: array
        items:
          type: string
      innerErrors:
        type: array
        items:
          $ref: '#/definitions/Error'
    example:
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251041
      message: >-
        One or more errors occurred. See the contained list for details of each
        error.
      args: []
      innerErrors:
        - name: DocumentManager.NotFound
          code: -252520
          message: The specified document was not found.
          args: []
````
