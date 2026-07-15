# NI OSS SOURCE SNAPSHOT: systemlink-OpenAPI-documents

<!--NI_OSS_SNAPSHOT repo=ni/systemlink-OpenAPI-documents commit=c99cb7610a1d7e4ebe9fa6a4f979d3b10308a8ff -->

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=.github/PULL_REQUEST_TEMPLATE.md sha256=22ab3e6821b9f9d06ad9a0a67e70c10c6a970af488b2f81c6a881531cc5c2ac0 bytes=676 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `22ab3e6821b9f9d06ad9a0a67e70c10c6a970af488b2f81c6a881531cc5c2ac0`
- bytes: 676

````markdown
- [ ] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/systemlink-OpenAPI-documents/blob/master/CONTRIBUTING.md).

TODO: Check the above box with an 'x' indicating you've read and followed [CONTRIBUTING.md](https://github.com/ni/systemlink-OpenAPI-documents/blob/master/CONTRIBUTING.md).

### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=.travis.yml sha256=4b5c27aaf2ba0971cc71c8bec972aff84322b1058c0162dff48a06bb8b08daaf bytes=834 -->
## FILE: .travis.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `.travis.yml`
- sha256: `4b5c27aaf2ba0971cc71c8bec972aff84322b1058c0162dff48a06bb8b08daaf`
- bytes: 834

````yaml
language: generic
deploy:
  provider: npm
  email: webapps.ops@ni.com
  api_key:
    secure: S3pu1Ti7RpTxoA6SuDlYsKhxQ5QRxFRqDX1Q1w9rRyGYCWHG1XoLW8Tw7P7TrKEii8sjL+D6+dt2NGm/uTpE1fetOBA/0+gF8z8gTgS9QI0XMfjTJ0twtIFWdEPQ39pX/MlWJXPW2r80iGNyXsdx+USD3s9ucRDXkX2xbHt/EkSDoRQR64yJd3ZZYcReO+YFlaA5q0eF++WmdHkbC7exnl33d0BQjuaVA/f8tpWVfQLZZExMCFSircOG3R8GDY00KkIMkoeTMpMSPTpH9LKQLrI7Au4A/SH/W26p894LQgoijU9uid52PQtFbr/InWGLJexjqPoSRMeMmlAE4GYPCb0DV7XOxcj1OrDdKJdreap/hUTWDQoiMimC6prg2l83jdhtLoPzidITsLkU+R9GWLG9NFD8biLa9TzJT/3hlYiicmNmsBPjLY86aSb3aFAz5K0N1ZS3M4R5W3SOAMa8Ewbt3ygzBQO+K4SEEXVt0huPacrUh0M4Q84CqitTbXWivjZ5FjWsRdhWqsW/DGoM44IHF+HIPkbpvb/lVhq3HYF0TvH4cCnaD/0injEiuaqROK97beqqH12mSpgyTMjP57Nh2P6lR5uCvWL997nxIQz+QW1Ae8/BqQwwEFvdWU9CX8M6yX/SuhwSaVaJzcKHIxQ9ZRGzYATelOzrgTtbsFM=
  on:
    repo: ni/systemlink-OpenAPI-documents
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=alarm/nialarm.yml sha256=823a9ccc4c50b258fce417150927845b00095add11fed982eb3abe16fc3b0816 bytes=39933 -->
## FILE: alarm/nialarm.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `alarm/nialarm.yml`
- sha256: `823a9ccc4c50b258fce417150927845b00095add11fed982eb3abe16fc3b0816`
- bytes: 39933

````yaml
swagger: '2.0'
info:
  version: '1'
  title: Alarm Web Service
  description: SystemLink Alarm Service HTTP API. Only available on SystemLink Server.
  contact:
    name: NI
    url: 'https://www.ni.com/systemlink'
    email: support@ni.com
basePath: /nialarm
consumes:
  - application/json
produces:
  - application/json
securityDefinitions:
  basicAuth:
    type: basic
  apiKeyAuth:
    type: apiKey
    name: x-ni-api-key
    in: header
security:
  - basicAuth: []
  - apiKeyAuth: []
x-ni-routing-key: Skyline.AlarmInstance
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
      message:
        description: Complete error message
        type: string
      args:
        description: Positional argument values for the error code
        type: array
        items:
          type: string
      resourceType:
        description: Type of resource associated with the error.
          This field is only present for entries in *innerErrors*.
        type: string
        enum: [instanceId]
      resourceId:
        description: Identifier of the resource associated with the error.
          This field is only present for entries in *innerErrors*.
        type: string
      innerErrors:
        description: Array of individual errors when a request results in multiple errors.
          This field is only present when *name* is 'Skyline.OneOrMoreErrorsOccurred'.
        type: array
        items:
          $ref: '#/definitions/Error'
    example:
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251041
      message: One or more errors occurred. See the contained list for details of each error.
      args: []
      innerErrors:
        - name: AlarmInstance.InstanceNotFound
          code: -253006
          message: An instance with instanceId '5c2cf7e0e0d64403b486fcb4' was not found.
          resourceType: instanceId
          resourceId: 5c2cf7e0e0d64403b486fcb4
          args: [5c2cf7e0e0d64403b486fcb4]
  Operation:
    description: Operation provided by the API
    type: object
    properties:
      available:
        type: boolean
        description: Whether the operation is available to the caller
      version:
        type: integer
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
        description: >-
          Available operations in the v1 version of the API:

          - deleteAlarmInstances: The ability to delete alarm instances

          - readAlarmInstances: The ability to query for alarm instances

          - writeAlarmInstances: The ability to create and modify alarm instances

        type: object
        properties:
          deleteAlarmInstances:
            $ref: '#/definitions/Operation'
          readAlarmInstances:
            $ref: '#/definitions/Operation'
          writeAlarmInstances:
            $ref: '#/definitions/Operation'
  AlarmInstance:
    title: Alarm Instance
    description: An individual instance of an alarm. The lifecycle of an alarm instance begins the first
      time it is triggered and ends when it has been both acknowledged and cleared. The service enforces the
      invariant that there can be at most one *active*/true instance of an alarm with a given *alarmId*.
    type: object
    required:
      - alarmId
    properties:
      instanceId:
        description: The unique ID of a particular instance of an alarm.
        type: string
        example: 5c33c212e0d6444320d9a9f4
      alarmId:
        description: A value meant to uniquely identify the particular process or condition tracked by an
          alarm. For example, alarm instances created by the Tag Rule Engine Service have their *alarmIds* set
          to the concatenation of the path of the tag which caused the rule to be triggered and the ID of the
          rule.
        type: string
        example: CRIO1.System.Health.DiskSpaceUsePercentage.Bdd9u!4aMd!$pYrf*CnaIZ2tbu$-Ct%?
      workspace:
        description: The ID of the workspace to which this alarm instance belongs. Added in version 3 of the
          readAlarmInstances operation.
        type: string
        example: 3d411024-9db8-42d1-8ab8-6cee0e6cd841
      active:
        description: Whether or not the alarm instance is active. An active alarm deserves human or automated
          attention. Alarm instances always begin life with *active*/true. This field will be automatically
          set to false when the *clear* and *acknowledged* fields are set to true.
        type: boolean
      clear:
        description: When set to true, the condition that triggered the alarm no longer matches the trigger
          condition. When an alarm instance is created, *clear* is initially set to false. The creator of the
          alarm (typically a rule engine or application element of some sort) may determine that the trigger
          condition no longer applies, and may send an update, clearing the condition. Clearing the alarm
          does not deactivate the alarm, unless the alarm had previously been acknowledged. As long as the
          alarm is *active*/true, the alarm may transition from *clear*/true to *clear*/false (or vice versa)
          multiple times.
        type: boolean
      acknowledged:
        description: When set to true, the alarm has been acknowledged by an alarm handler, which is typically
          a human. Alarm instances always begin life with *acknowledged*/false. Acknowledging an alarm will
          not affect the *active* flag unless *clear* is also true. When *clear* and *acknowledged* are
          true, the alarm will become inactive (*active*/false). This field is automatically reset to false
          when an alarm instance's *highestSeverityLevel* field increases.
        type: boolean
      acknowledgedAt:
        description: ISO-8601 formatted timestamp specifying when the alarm instance was acknowledged. This
          field will be cleared when an alarm instance's *highestSeverityLevel* field increases.
        type: string
        format: date-time
        example: '2019-01-14T23:15:53.7270539Z'
      acknowledgedBy:
        description: An identifier for who acknowledged a given alarm instance. This field will be cleared
          when an alarm instance's *highestSeverityLevel* field increases.
        type: string
        example: Daffy Duck
      occurredAt:
        description: ISO-8601 formatted timestamp specifying when the alarm instance was created
        type: string
        format: date-time
        example: '2019-01-14T23:15:53.7270539Z'
      updatedAt:
        description: ISO-8601 formatted timestamp specifying when the alarm instance was last updated
        type: string
        format: date-time
        example: '2019-01-14T23:15:53.7270539Z'
      createdBy:
        description: An identifier for who or what created a given alarm instance. This is usually used to
          identify the particular rule engine which requested that a given alarm instance be created.
        type: string
        example: TagRuleEngine
      transitions:
        description: A collection of transitions for a given alarm instance. Transitions record changes to
          an alarm instance's *clear* flag, as well as increases or decreases in severity. The service stores
          the first transition and the most recent one hundred other transitions.
        type: array
        items:
          $ref: '#/definitions/AlarmTransition'
      transitionOverflowCount:
        description: The number of transitions which overflowed a given alarm instance's *transition's* field
        type: integer
        example: 0
      notificationStrategyIds:
        description: The IDs of the notification strategies which should be triggered if this request results
          in an alarm instance being created or transitioning to a new highest severity
        type: array
        items:
          type: string
        example: []
      currentSeverityLevel:
        description: The current severity level of a given alarm instance
        type: integer
        example: 2
      highestSeverityLevel:
        description: The highest severity level that a given alarm instance has ever been in
        type: integer
        example: 4
      channel:
        description: An identifier for the tag or resource associated with a given alarm instance
        type: string
        example: CRIO1.System.Health.DiskSpaceUsePercentage
      condition:
        description: A description of the condition associated with a given alarm instance
        type: string
        example: Greater than 90
      displayName:
        description: Optional display name for a given alarm instance. Display names do not need to be unique.
        type: string
        example: Low disk space on tester-1.
      description:
        description: Optional description text for a given alarm instance
        type: string
        example: Disk space on tester-1 is high. Disk usage was 95% when this alarm was created.
      keywords:
        description: Words or phrases associated with an alarm instance. Alarm instances can be tagged
          with keywords to make it easier to find them with queries.
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      notes:
        description: A collection of notes for a given alarm instance. Notes are set by humans to record
          information about an alarm after it has been investigated.
        type: array
        items:
          $ref: '#/definitions/AlarmNote'
      properties:
        description: Key-value-pair metadata associated with an alarm instance. Alarm instances can be tagged
          with properties to make it easier to find them with queries. Additionally, alarm instance properties
          are used to expand message templates in the notification strategies associated with a given alarm
          instance.
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
      resourceType:
        description: The type of resource associated with a given alarm instance
        type: string
        example: Tag
  AlarmNote:
    title: Alarm Note
    description: Information about a particular alarm instance, such as a description of an
      investigation into an alarm's root cause.
    required:
      - note
    properties:
      note:
        description: Information about a particular alarm instance, such as a description of an investigation
          into an alarm's root cause.
        type: string
        example: Temperature sensor was faulty
      createdAt:
        description: ISO-8601 formatted timestamp specifying when the note was created
        type: string
        format: date-time
        example: '2019-01-14T23:15:53.7270539Z'
      user:
        description: The user who created the note
        type: string
        readOnly: true
        example: Philip
  AlarmTransitionType:
    title: Alarm Transition Type
    type: string
    enum: [SET, CLEAR]
  AlarmTransition:
    title: Alarm Transition
    description: A transition within a given alarm instance. Transitions record changes to an alarm's
      *clear* field, as well as an alarm increasing or decreasing in severity.
    type: object
    required:
      - transitionType
    properties:
      transitionType:
        $ref: '#/definitions/AlarmTransitionType'
      occurredAt:
        description: ISO-8601 formatted timestamp specifying when the transition occurred
        type: string
        format: date-time
        example: '2019-01-14T23:15:53.7270539Z'
      severityLevel:
        description: The severity of the transition. Valid values for CLEAR transitions are [-1,-1]. Valid
          values for SET transitions are [1, infinity]. Note that the SystemLink Alarm UI only has display
          strings for SET severities in the range [1, 4].
        type: integer
        example: 2
        default: 2
        minimum: -1
      condition:
        description: A description of the condition associated with the transition
        type: string
        example: Greater than 90
      shortText:
        description: Short description of the condition
        type: string
        example: Low disk space
      detailText:
        description: Detailed description of the condition
        type: string
        example: Disk usage on CRIO1 is 95% (lower than configured threshold of 90%)
      keywords:
        description: Words or phrases associated with a transition. Useful for attaching additional metadata
          to a given transition which could aid in an investigation into an alarm's root cause in the future.
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      properties:
        description: Key-value-pair metadata associated with a transition. Useful for attaching additional
          metadata to a given transition which could aid in an investigation into an alarm's root cause
          in the future.
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
  SubQuery:
    title: SubQuery
    description: Object describing the fields of an alarm instance query which can be composed in the query
      request's *subQuery* array, enabling multiple queries to be AND'ed together
    type: object
    properties:
      alarmId:
        type: string
        description: AlarmId query. The service will return alarm instances whose *alarmId* fields are equal
          to the query. This query takes case into account.
        example: System.Health.DiskSpaceLow.Bdd9u!4aMd!$pYrf*CnaIZ2tbu$-Ct%?
      description:
        type: string
        description: Description query. The service will return alarm instances whose *description* fields
          contain the description query string. This query does not take case into account.
        example: Disk usage
      displayName:
        type: string
        description: Display name query. The service will return alarm instances whose *displayName* fields
          contain the display name query string. This query does not take case into account.
        example: Low disk space on CRIO1
      active:
        type: boolean
        description: Active status query. The service will return alarm instances whose *active* fields are
          equal to the query.
      clear:
        type: boolean
        description: Clear status query. The service will return alarm instances whose *clear* fields are
          equal to the query.
      acknowledged:
        type: boolean
        description: Acknowledged status query. The service will return alarm instances whose *acknowledged*
          fields are equal to the query.
      acknowledgedAtMin:
        type: string
        description: Acknowledged at minimum date query. The service will return instances which were
          acknowledged between *acknowledgedAtMin* and *acknowledgedAtMax*, inclusive.
        format: date-time
        example: '2019-01-14T23:15:53.7270539Z'
      acknowledgedAtMax:
        type: string
        description: Acknowledged at maximum date query. The service will return instances which were
          acknowledged between *acknowledgedAtMin* and *acknowledgedAtMax*, inclusive.
        format: date-time
        example: '2019-01-15T23:15:53.7270539Z'
      occurredAtMin:
        type: string
        description: Occurred at minimum date query. The service will return instances which occurred between
          *occurredAtMin* and *occurredAtMax*, inclusive.
        format: date-time
        example: '2019-01-14T23:15:53.7270539Z'
      occurredAtMax:
        type: string
        description: Occurred at maximum date query. The service will return instances which occurred between
          *occurredAtMin* and *occurredAtMax*, inclusive.
        format: date-time
        example: '2019-01-15T23:15:53.7270539Z'
      currentSeverityLevelMin:
        type: integer
        description: Current severity minimum query. The service will return instances whose current severity
          is between *currentSeverityLevelMin* and *currentSeverityLevelMax*, inclusive.
        example: 1
      currentSeverityLevelMax:
        type: integer
        description: Current severity maximum query. The service will return instances whose current severity
          is between *currentSeverityLevelMin* and *currentSeverityLevelMax*, inclusive.
        example: 4
      highestSeverityLevelMin:
        type: integer
        description: Highest severity minimum query. The service will return instances whose highest severity
          is between *highestSeverityLevelMin* and *highestSeverityLevelMax*, inclusive.
        example: 1
      highestSeverityLevelMax:
        type: integer
        description: Highest severity maximum query. The service will return instances whose highest severity
          is between *highestSeverityLevelMin* and *highestSeverityLevelMax*, inclusive.
        example: 4
      createdBy:
        type: string
        description: Created by query. The service will return instances whose *createdBy* fields are equal to
          the query. This query takes case into account.
        example: TagRuleEngine
      channel:
        type: string
        description: Channel query. The service will return instances whose *channel* fields are equal to the
          query. This query takes case into account and supports wildcard match checking with glob-style wildcards.
        example: '*.System.Health.DiskSpaceUsePercentage'
      resourceType:
        type: string
        description: Resource type query. The service will return instances whose *resourceType* fields are
          equal to the query. This query takes case into account.
        example: Tag
      properties:
        type: object
        description: Property query. The service will return instances whose *properties* fields contain all
          of the specified key/value pairs.
        additionalProperties:
          type: string
        example:
          key1: value1
      keywords:
        type: array
        description: Keyword query. The service will return instances whose *keywords* fields contain all of
          the specified keywords.
        items:
          type: string
        example:
          - keyword1
          - keyword2
      workspaces:
        type: array
        description: Workspace query. The service will return instances whose *workspace* field is one of
          the specified workspaces. By default, only instances in the default workspace are returned.
          Specify an array containing a single value of *\** to query all workspaces. Added in version 3 of the
          readAlarmInstances operation.
        items:
          type: string
        example:
          - '*'
  QueryRequest:
    title: Query Request
    description: Object describing the request body for an alarm instance query request
    allOf:
    - $ref: '#/definitions/SubQuery'
    - type: object
      properties:
        subQueries:
          description: Additional queries. The service will return instances which match any of the queries
            in the subQueries array. If a top-level query was provided, the top-level query will be AND'ed
            with each of the sub queries.
          type: array
          items:
            $ref: '#/definitions/SubQuery'
        returnMostRecentlyOccurredOnly:
          description: Whether or not the alarm service should group the instances matched by this query by
            *alarmId*, and then only return the most recent instance for each grouping. In this context,
            recency is based on when the alarm instance occurred, not when it was last updated.
          type: boolean
          default: false
        orderBy:
          description: Whether or not results should be sorted in ascending or descending order relative to
            the alarm instance's *updatedAt* field.
          type: string
          enum: [DATE_UPDATED_FORWARD, DATE_UPDATED_BACKWARD]
          default: DATE_UPDATED_FORWARD
        skip:
          description: Number of entries to skip in the response list. Typically used in combination with the
            take parameter to implement pagination.
          type: integer
          default: 0
        take:
          description: Number of entries to include in the response list. Typically used in combination with
            the skip parameter to implement pagination.
          type: integer
          default: 10000
          maximum: 10000

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
  QueryResponse:
    description: Success
    schema:
      description: Query response
      title: QueryResponse
      type: object
      properties:
        totalCount:
          description: The total number of alarm instances which matched your query
          type: integer
          example: 1
        filterMatches:
          description: Array containing the alarm instances which matched your query
          type: array
          items:
            $ref: '#/definitions/AlarmInstance'
  Unauthorized:
    description: Not authorized
    headers:
      WWW_Authenticate:
        description: Information for how to authenticate
        type: string
paths:
  /:
    get:
      tags: [versioning]
      summary: API information
      description: Returns information about API versions and available operations.
      operationId: RootEndpoint
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
              version:
                description: Implementation version of the web service
                type: string
  /{version}:
    parameters:
      - in: path
        name: version
        description: Version of the API to retrieve operations.
        type: string
        required: true
    get:
      tags: [versioning]
      summary: API version information
      description: Returns available operations for a single version of the API.
      operationId: RootEndpointWithVersion
      # Explicitly mark security as an empty array - this route does not require any privileges.
      # Marking it this way prevents it from inheriting the top-level security settings.
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
  /v1/acknowledge-instances-by-instance-id:
    post:
      tags: [alarm instances]
      summary: Acknowledge alarm instances
      description: Acknowledges one or more alarm instances, optionally forcing them clear and adding notes to
        them. Added in version 2 of the writeAlarmInstances operation.
      operationId: AcknowledgeInstancesByInstanceId
      x-ni-operation: writeAlarmInstances
      parameters:
        - in: body
          name: Request body
          required: true
          schema:
            type: object
            title: AcknowledgeByInstanceIdRequestBody
            required:
              - instanceIds
            properties:
              instanceIds:
                description: The *instanceId*s of the alarm instances which should be acknowledged.
                type: array
                items:
                  type: string
                example: [5c33c212e0d6444320d9a9f4, 5c2cf7e0e0d64403b486fcb4]
              forceClear:
                description: Whether or not the affected alarm instances should have their *clear* field set
                  to true.
                type: boolean
                default: false
              notes:
                description: Notes which should be added to the alarm instances.
                type: array
                items:
                  $ref: '#/definitions/AlarmNote'
      responses:
        200:
          description: Success - Indicates the request to acknowledge was processed successfully.
            If any instances failed to be acknowledged, the included *error* object will contain
            an entry in the *innerErrors* array for each failed instance.
          schema:
            type: object
            title: AcknowledgeByInstanceIdResponse
            properties:
              acknowledged:
                description: The *instanceId*s of the alarm instances which were successfully acknowledged.
                type: array
                items:
                  type: string
                example: [5c33c212e0d6444320d9a9f4]
              failed:
                description: The *instanceId*s of the alarm instances which were not acknowledged.
                  See *error* for why each instance failed to be acknowledged. Reasons include the instance
                  could not be found, the instance was already acknowledged, or the caller is not authorized
                  to acknowledge the instance.
                type: array
                items:
                  type: string
                example: [5c2cf7e0e0d64403b486fcb4]
              error:
                $ref: '#/definitions/Error'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/acknowledge-instances:
    post:
      tags: [deprecated]
      deprecated: true
      summary: Acknowledge alarm instances
      description: As of version 2 of the writeAlarmInstances operation, this route is deprecated.
        Instead, use the POST /v1/acknowledge-instances-by-instance-id route.


        Acknowledges one or more alarm instances in the default workspace by alarm id,
        optionally forcing them clear and adding notes to them.
      operationId: AcknowledgeInstances
      x-ni-operation: writeAlarmInstances
      parameters:
        - in: body
          name: Request body
          required: true
          schema:
            type: object
            title: AcknowledgeRequestBody
            required:
              - alarmIds
            properties:
              alarmIds:
                description: The *alarmIds* of the alarm instances which should be acknowledged.
                type: array
                items:
                  type: string
                example: [System1.Health.DiskSpaceAlarm, System2.Health.DiskSpaceAlarm]
              forceClear:
                description: Whether or not the affected alarm instances should have their *clear* field set
                  to true.
                type: boolean
                default: false
              notes:
                description: Notes which should be added to the alarm instances.
                type: array
                items:
                  $ref: '#/definitions/AlarmNote'
      responses:
        200:
          description: OK
          schema:
            type: object
            title: AcknowledgeResponse
            properties:
              acknowledged:
                description: The *alarmId*s which were successfully acknowledged.
                type: array
                items:
                  type: string
                example: [System1.Health.DiskSpaceAlarm, System2.Health.DiskSpaceAlarm]
              alreadyAcknowledged:
                description: The *alarmId*s which had already been previously acknowledged.
                type: array
                items:
                  type: string
                example: [System1.Health.DiskSpaceAlarm]
              notFound:
                description: A collection of *alarmId*s for which no active alarm instances were found.
                type: array
                items:
                  type: string
                example: [System2.Health.DiskSpaceAlarm]
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/instances:
    post:
      tags: [alarm instances]
      summary: Create or update an alarm instance
      description: Creates or updates an instance of an alarm based on the requested transition and the state
        of the current active alarm instance with the given *alarmId*.
      operationId: CreateOrUpdateInstance
      x-ni-operation: writeAlarmInstances
      parameters:
        - in: body
          name: Request body
          description: Container which holds data for the request. If an alarm instance is being updated, only
            alarmId, workspace, and transition are applied.
          schema:
            type: object
            title: CreateOrUpdateInstanceRequest
            required:
              - transition
              - alarmId
            properties:
              alarmId:
                description: A value meant to uniquely identify the particular process or condition tracked
                  by a given alarm within a workspace. For example, alarms created by the Tag Rule Engine
                  Service have their alarmIds set to the concatenation of the path of the tag which caused
                  the rule to be triggered and the ID of the rule.
                type: string
                example: CRIO1.System.Health.DiskSpaceMeanUsePercentage.Bdd9u!4aMd!$pYrf*CnaIZ2tbu$-Ct%?
              workspace:
                description: The ID of the workspace in which to create or update the alarm. When not specified,
                  the default workspace is used based on the requesting user. Added in version 2 of the
                  writeAlarmInstances operation.
                type: string
                example: 3d411024-9db8-42d1-8ab8-6cee0e6cd841
              transition:
                $ref: '#/definitions/AlarmTransition'
              notificationStrategyIds:
                description: The IDs of the notification strategies which should be triggered if this request results
                  in an alarm instance being created or transitioning to a new highest severity
                type: array
                items:
                  type: string
                example: []
              createdBy:
                description: An identifier for who or what created a given alarm instance. This is usually
                  used to identify the particular rule engine which requested that a given alarm be created.
                type: string
                example: TagRuleEngine
              channel:
                description: An identifier for the tag or resource associated with the alarm
                type: string
                example: CRIO1.System.Health.DiskSpaceMeanUsePercentage
              resourceType:
                description: The type of resource associated with the alarm
                type: string
                example: Tag
              displayName:
                description: Optional display name for a given alarm instance. Display names do not need to be
                  unique.
                type: string
                example: Low disk space on tester-1.
              description:
                description: Optional description text for a given alarm instance
                type: string
                example: Disk space on tester-1 is high. Disk usage was 95% when this alarm was created.
              keywords:
                description: Words or phrases associated with an alarm instance. Alarm instances can be
                  tagged with keywords to make it easier to find them with queries.
                type: array
                items:
                  type: string
                example:
                  - keyword1
                  - keyword2
              properties:
                description: Key-value-pair metadata associated with an alarm instance. Alarm instances can be
                  tagged with properties to make it easier to find them with queries. Additionally, alarm
                  instance properties are used to expand message templates in the notification strategies
                  associated with a given alarm instance.
                type: object
                additionalProperties:
                  type: string
                example:
                  key1: value1
          required: true
      responses:
        200:
          description: OK
          schema:
            type: object
            title: CreateOrUpdateInstanceResponse
            properties:
              instanceId:
                description: The ID of the created or modified alarm instance.
                type: string
                example: 5c40ec55e0d6441168b4c543
        401:
          $ref: '#/responses/Unauthorized'
        409:
          description: For requests which would result in an update to an existing alarm instance, this is
            returned when the request does not represent a valid transition for the existing alarm instance.
            This can occur when attempting to clear an alarm instance which is already clear, or when
            attempting to set an alarm instance which is already set at the given severity level.
          schema:
            $ref: '#/definitions/Error'
        default:
          $ref: '#/responses/Error'
  /v1/instances/{instanceId}:
    parameters:
      - in: path
        name: instanceId
        description: Instance ID
        type: string
        required: true
    get:
      tags: [alarm instances]
      summary: Get an alarm instance
      description: Gets an alarm instance by its *instanceId*.
      operationId: GetInstance
      x-ni-operation: readAlarmInstances
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/AlarmInstance'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      tags: [alarm instances]
      summary: Delete an alarm instance
      description: Deletes an alarm instance by its *instanceId*.
      operationId: DeleteInstance
      x-ni-operation: deleteAlarmInstances
      responses:
        204:
          description: No Content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/instances/{instanceId}/notes:
    parameters:
      - in: path
        name: instanceId
        description: Instance ID
        type: string
        required: true
    post:
      tags: [alarm instances]
      summary: Add notes to an alarm instance
      description: Adds one or more notes to an alarm instance.
      operationId: AddNotesToInstance
      x-ni-operation: writeAlarmInstances
      parameters:
        - in: body
          name: Request body
          required: true
          schema:
            type: object
            title: AddNotesRequestBody
            required:
              - notes
            properties:
              notes:
                type: array
                description: Notes to be added to the alarm instance
                items:
                  $ref: '#/definitions/AlarmNote'
      responses:
        204:
          description: No Content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/query-instances:
    post:
      tags: [alarm instances]
      summary: Query alarm instances
      description: Queries for alarm instances. Specifying an empty JSON object in the request body will
        result in all alarm instances in the default workspace being returned.
      operationId: QueryInstances
      x-ni-operation: readAlarmInstances
      parameters:
        - in: body
          name: Request body
          required: false
          schema:
            $ref: '#/definitions/QueryRequest'
      responses:
        200:
          $ref: '#/responses/QueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/delete-instances-by-instance-id:
    post:
      tags: [alarm instances]
      summary: Delete alarm instances
      description: Deletes multiple alarm instances by their *instanceIds*.
      operationId: DeleteInstancesByInstanceId
      x-ni-operation: deleteAlarmInstances
      parameters:
        - in: body
          name: Request body
          required: true
          schema:
            type: object
            title: Instance IDs to delete
            properties:
              instanceIds:
                description: Instance IDs to delete
                type: array
                items:
                  type: string
                example:
                  - 5c33c212e0d6444320d9a9f4
                  - 5c2cf7e0e0d64403b486fcb4
      responses:
        200:
          description: Partial Success - Indicates the request to delete was processed successfully,
            but one or more instances failed to delete. The included *error* object will contain
            an entry in the *innerErrors* array for each failed instance.
          schema:
            type: object
            title: DeleteInstancesByInstanceIdPartialSuccess
            properties:
              deleted:
                description: The *instanceId*s of the alarm instances that were successfully deleted.
                type: array
                items:
                  type: string
                example:
                  - 5c33c212e0d6444320d9a9f4
              failed:
                description: The *instanceId*s of the alarm instances that were not deleted.
                  See *error* for why each instance failed to delete. Reasons include the
                  instance could not be found or the caller is not authorized to delete the instance.
                type: array
                items:
                  type: string
                example:
                  - 5c2cf7e0e0d64403b486fcb4
              error:
                $ref: '#/definitions/Error'
        204:
          description: Success - Indicates all requested instances were deleted successfully.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=asset-management-rule/niapmrule.yml sha256=dcca32cedbda92b8bda9959fa0d16a60e948a7664208527e5270152151576d02 bytes=14319 -->
## FILE: asset-management-rule/niapmrule.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `asset-management-rule/niapmrule.yml`
- sha256: `dcca32cedbda92b8bda9959fa0d16a60e948a7664208527e5270152151576d02`
- bytes: 14319

````yaml
swagger: '2.0'
info:
  version: '1'
  title: Asset Performance Management Rule Web Service
  description: Create and manage calibration rules for assets.
  contact:
    name: NI
    url: 'https://www.ni.com/systemlink'
    email: support@ni.com
basePath: /niapmrule
consumes:
  - application/json
produces:
  - application/json
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
x-ni-routing-key: Skyline.AssetPerformanceManagementRuleEngine
x-ni-privilege-application: ninotification
definitions:
  Error:
    description: Contains error information.
    type: object
    properties:
      name:
        description: String error code
        type: string
      code:
        description: Numeric error code
        type: integer
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
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251040
      message: >-
        One or more errors occurred. See the contained list for details of each
        error.
      args: []
      innerErrors:
        - name: AssetPerformanceManagementRuleEngine.RuleNotFound
          code: -254051
          resourceType: CalibrationRuleEntry
          resourceId: 4afb2ce3741fe11d88838cc9
          message: "The rule with identifier 4afb2ce3741fe11d88838cc9 was not found."
          args: [ 4afb2ce3741fe11d88838cc9 ]
  Operation:
    description: An operation provided by the API.
    type: object
    required:
        - available
    properties:
      available:
        type: boolean
        description: Whether or not the operation is available to the caller.
      version:
        type: integer
        description: Version of the available operation.
    example:
      available: true
      version: 1
  V1Operations:
    title: V1 Operations
    description: Object containing available operations in the v1 version of the API.
    type: object
    properties:
      operations:
        description: >-
          Available operations in the v1 version of the API:

          - getCalibrationRule: Obtain calibration rule information.

          - updateCalibrationRule: Update calibration rule information.
        type: object
        properties:
          getCalibrationRule:
            $ref: '#/definitions/Operation'
          updateCalibrationRule:
            $ref: '#/definitions/Operation'
  CalibrationSeverityModel:
    title: Calibration Severity Model
    description: A calibration severity level for a rule.
    type: object
    required:
      - name
      - severityLevel
      - daysUntilCalibrationDue
    properties:
      name:
        description: The name of the severity.
        type: string
        example: Approaching
      severityLevel:
        description: The level of the severity.
        type: integer
        minimum: 1
        maximum: 4
        default: 2
        example: 2
      notificationStrategyIds:
        description: The unique identifiers for notification strategies to use when this rule is triggered for an asset.
        type: array
        items:
          type: string
          example: e3491890f7b15b83d3fc174a
      daysUntilCalibrationDue:
        description: The number of days until recommended calibration due date to trigger the alarm.
        type: integer
        example: 30
  CalibrationRulePutRequestModel:
    title: Calibration Rule Put Request Model
    description: A request to replace a calibration rule.
    type: object
    required:
      - displayName
      - description
      - disabled
      - instanceDisplayNameTemplate
      - instanceDescriptionTemplate
      - severityLevels
    properties:
      displayName:
        description: Display name of the rule.
        type: string
        example: Calibration
      description:
        description: Description of what the rule does.
        type: string
        example: Rule to identify assets that passed their recommended calibration due date.
      disabled:
        description: Whether or not the rule is disabled.
        type: boolean
        example: false
      instanceDisplayNameTemplate:
        description: Template used for the display name that appears on an alarm instance created by this rule.
        type: string
        example: Asset <AssetName> passed recommended calibration date.
      instanceDescriptionTemplate:
        description: Template used for the description that appears on an alarm instance created by this rule.
        type: string
        example: Asset <AssetName> from system <SystemName> has the next recommended calibration date as <NextExternalCalibrationDate> but that date already passed.
      severityLevels:
        description: Severity levels for the alarm rule.
        type: array
        items:
          $ref: '#/definitions/CalibrationSeverityModel'
  CalibrationRuleModel:
    allOf:
      - $ref: '#/definitions/CalibrationRulePutRequestModel'
      - title: Calibration Rule Model
      - description: A calibration rule that runs on assets.
      - type: object
      - required:
        - id
      - properties:
          id:
            description: Calibration rule identifier.
            type: string
            example: "5b83d3fc174ae3491890f7ae"
          lastUpdatedTimestamp:
            description: ISO-8601 formatted timestamp specifying the last date the rule was updated.
            type: string
            format: date-time
            example: '2018-05-07T18:58:05.219692Z'
          workspace:
            type: string
            description: The ID of the workspace.
            example: '5bc5e9092a4fa4c71cfa7197'
  RuleStateUpdateModel:
    title: Rule State Update Model
    description: The collection of rule identifiers and the enable/disable state to apply on them.
    type: object
    required:
      - ruleIds
      - disabled
    properties:
      ruleIds:
        description: Array containing the rule identifiers on which to set the enable/disable state.
        type: array
        items:
          type: string
          example: '5b83d3fc174ae3491890f7ae'
      disabled:
        description: Whether or not to disable all the specified rules.
        type: boolean
        example: true
parameters:
  RuleId:
    in: path
    name: ruleId
    description: Calibration rule identifier.
    type: string
    required: true
    x-example: '5b83d3fc174ae3491890f7ae'
  SetRulesState:
    in: body
    name: setRulesState
    description: The collection of rule identifiers and the enable/disable state to apply on them.
    required: true
    schema:
      $ref: '#/definitions/RuleStateUpdateModel'
  Workspaces:
    in: query
    name: workspaces
    description: A string representing the collection of workspace IDs separated by comma used to filter the rules.
    required: false
    type: string
    x-example: '5bc5e9092a4fa4c71cfa7197,3a83d3fc174ae3491890f7ae'
responses:
  BadRequest:
    description: The server was unable to process the request because of invalid syntax.
    schema:
      title: Bad Request Error Response
      description: Bad request error response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
  NotFound:
    description: The requested resource was not found.
    schema:
      title: Not Found Request Error Response
      description: Not found error response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
  CalibrationRuleResponse:
    description: Response containing the rule having the specified identifier.
    schema:
      $ref: '#/definitions/CalibrationRuleModel'
  CalibrationRulesResponse:
    description: Response containing all the calibration rules that the service manages.
    schema:
      description: Response containing all the calibration rules.
      title: Calibration Rules Response
      type: object
      required:
        - calibrationRules
        - totalCount
      properties:
        calibrationRules:
          description: Array of calibration rules.
          type: array
          items:
            $ref: '#/definitions/CalibrationRuleModel'
        totalCount:
            description: The total number of calibration rules.
            type: integer
            example: 1
  Error:
    description: Error
    schema:
      description: Error response containing error information.
      title: Error Response
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
  PartialSuccessResponse:
    description: Rules update was partially successful. Only part of the requested information was successfully processed.
    schema:
      title: Partial Success Response
      description: Partial success response containing error information.
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
      tags: [versioning]
      summary: API information
      description: Returns information about API versions and available operations.
      operationId: RootEndpoint
      # Explicitly mark security as an empty array - this route does not require any privileges.
      # Marking it this way prevents it from inheriting the top-level security settings.
      security: []
      responses:
        200:
          description: OK
          schema:
            description: Version information
            title: Root Endpoint Response
            type: object
            properties:
              v1:
                $ref: '#/definitions/V1Operations'
              version:
                description: Defines the implementation version of the web service.
                type: string
                example: 1
  /{version}:
    parameters:
      - in: path
        name: version
        description: The version of the API to retrieve operations.
        type: string
        required: true
    get:
      tags: [versioning]
      summary: API version information
      description: Returns available operations for a single version of the API.
      operationId: RootEndpointWithVersion
      security: []
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/V1Operations'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/calibration-rules:
    get:
      tags: [calibration rules]
      summary: Get calibration rules
      description: Gets a list containing all rules specific to calibration.
      operationId: get-calibration-rules
      x-ni-operation: getCalibrationRule
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/Workspaces'
      responses:
        200:
          $ref: '#/responses/CalibrationRulesResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/calibration-rules/{ruleId}:
    parameters:
      - $ref: '#/parameters/RuleId'
    get:
      tags: [calibration rules]
      summary: Get a specific calibration rule
      description: Gets the calibration rule with the specified identifier.
      operationId: get-calibration-rule-by-id
      x-ni-operation: getCalibrationRule
      x-ni-auth: true
      responses:
        200:
          $ref: '#/responses/CalibrationRuleResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
    put:
      tags: [calibration rules]
      summary: Replace a specific calibration rule
      description: Replaces a specific calibration rule with the given one.
      operationId: put-calibration-rule
      x-ni-operation: updateCalibrationRule
      x-ni-auth: true
      parameters:
        - in: body
          name: CalibrationRulePutRequestModel
          description: The calibration rule that replaces the other rule.
          required: true
          schema:
            $ref: '#/definitions/CalibrationRulePutRequestModel'
      responses:
        204:
          description: No Content
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/set-calibration-rules-state:
    post:
      tags: [calibration rules]
      summary: Set specific calibration rules state
      description: Sets specific calibration rules state by enabling or disabling them.
      operationId: set-calibration-rules-state
      x-ni-operation: updateCalibrationRule
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/SetRulesState'
      responses:
        200:
          $ref: '#/responses/PartialSuccessResponse'
        204:
          description: No Content
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=asset-managment/niapm.yml sha256=2602ec5819b2811bee226475e0b6a54cc93187d260b66190fabea526a1f4b917 bytes=139260 -->
## FILE: asset-managment/niapm.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `asset-managment/niapm.yml`
- sha256: `2602ec5819b2811bee226475e0b6a54cc93187d260b66190fabea526a1f4b917`
- bytes: 139260

````yaml
swagger: "2.0"
info:
  version: '1'
  title: Asset Performance Management Web Service
  description: Asset Performance Management HTTP API
  contact:
    name: NI
    url: 'https://www.ni.com/systemlink'
    email: support@ni.com
basePath: /niapm
x-ni-privilege-application: 'niws.niasset'
consumes:
  - application/json
produces:
  - application/json
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
x-ni-routing-key: Skyline.AssetPerformanceManagement
definitions:
  Error:
    description: Contains error information.
    type: object
    properties:
      name:
        description: String error code
        type: string
      code:
        description: Numeric error code
        type: integer
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
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251040
      message: >-
        One or more errors occurred. See the contained list for details of each
        error.
      args: []
      innerErrors:
        - name: AssetPerformanceManagement.NonExistingAssetWithIdentifier
          code: -253426
          resourceType: AssetEntry
          resourceId: 29162;01B245D6;4243;0
          message: 'No asset found with the specified identifier: 29162;01B245D6;4243;0.'
          args: [29162;01B245D6;4243;0]
  Operation:
    description: An operation provided by the API.
    type: object
    properties:
      available:
        type: boolean
        description: Whether the operation is available to the caller.
      version:
        type: integer
        description: Version of the available operation.
    required: [available]
    example:
      available: true
      version: 1
  V1Operations:
    title: V1 Operations
    description: Object containing available operations in the v1 version of the API.
    type: object
    properties:
      operations:
        description: >-
          Available operations in the v1 version of the API:

          - readAssets: Read information related to assets.

          - writeAssets: Write information related to assets.

          - deleteAssets: Delete information related to assets.
        type: object
        properties:
          readAssets:
            $ref: '#/definitions/Operation'
          writeAssets:
            $ref: '#/definitions/Operation'
          deleteAssets:
            $ref: '#/definitions/Operation'
  DiscoveryType:
    title: Discovery Type
    description: Indicates how the asset was discovered. "Automatic" indicates that SystemLink discovered the asset. "Manual" indicates that the asset was discovered using other methods.
    type: string
    enum:
      - Manual
      - Automatic
  BusType:
    title: Bus Type
    description: All supported bus types for an asset.
    type: string
    enum:
      - BUILT_IN_SYSTEM
      - PCI_PXI
      - USB
      - GPIB
      - VXI
      - SERIAL
      - TCP_IP
      - CRIO
      - SCXI
      - CDAQ
      - SWITCH_BLOCK
      - SCC
      - FIRE_WIRE
      - ACCESSORY
      - CAN
      - SWITCH_BLOCK_DEVICE
      - SLSC
  AssetType:
    title: Asset Type
    description: All supported asset types.
    type: string
    enum:
      - GENERIC
      - DEVICE_UNDER_TEST
      - FIXTURE
      - SYSTEM
  SystemConnectionStatus:
    title: System Connection Status
    description: Whether or not the minion is connected to the server and has updated the server with its data.
    type: string
    enum:
      - APPROVED
      - DISCONNECTED
      - CONNECTED_UPDATE_PENDING
      - CONNECTED_UPDATE_SUCCESSFUL
      - CONNECTED_UPDATE_FAILED
      - UNSUPPORTED
      - ACTIVATED
  AssetPresenceStatus:
    title: Asset Presence Status
    description: The status of an asset's presence in a system.
    type: string
    default: NOT_PRESENT
    enum:
      - INITIALIZING
      - UNKNOWN
      - NOT_PRESENT
      - PRESENT
  AssetPresenceUpdateStatus:
    title: Asset Presence Update Status
    description: The status update of an asset's presence in a system.
    type: string
    default: NOT_PRESENT
    enum:
      - INITIALIZING
      - UNKNOWN
      - NOT_PRESENT
      - PRESENT
      - REMOVED
  CalibrationHistoryModel:
    title: Calibration History
    description: The calibration history for an asset.
    allOf:
      - $ref: '#/definitions/ExternalCalibrationModel'
      - type: object
        required:
        - id
        - calibrationType
        properties:
          id:
            description: The calibration entry identifier.
            type: string
            example: "5c4f0834174ae321b8a95a03"
          calibrationType:
            $ref: '#/definitions/CalibrationType'
          timestamp:
            description: ISO-8601 formatted timestamp specifying the creation date of the entry.
            type: string
            format: date-time
            example: '2018-05-07T18:58:05.219692Z'
        example:
          temperatureSensors: [
            { name: 'Sensor0' , reading: 25.7 }
          ]
          isLimited: false
          date: '2018-05-07T18:58:05.000Z'
          recommendedInterval: 12
          nextRecommendedDate: '2019-05-07T18:58:05.000Z'
          nextCustomDueDate: '2019-06-07T18:58:05.000Z'
          comments: 'This is a comment.'
          entryType: MANUAL
          operator:
            displayName: John Doe
            userId: johnDoe2020
          id: 5c4f0834174ae321b8a95a03
          calibrationType: EXTERNAL_CALIBRATION
          timestamp: '2018-05-07T18:58:05.219692Z'
  CalibrationStatus:
    title: Calibration Status
    description: The calibration category the asset belongs to based on the next due calibration date.
    type: string
    enum:
      - OK
      - APPROACHING_RECOMMENDED_DUE_DATE
      - PAST_RECOMMENDED_DUE_DATE
  CalibrationMode:
    title: Calibration Mode
    description: Whether SystemLink automatically discovered the calibration data for an asset or if it was manually entered.
    type: string
    enum:
      - AUTOMATIC
      - MANUAL
  CalibrationType:
    title: Calibration Type
    description: The type of calibration the asset received, such as self or external calibration.
    type: string
    enum:
      - SELF_CALIBRATION
      - EXTERNAL_CALIBRATION
  AssetPresenceModel:
    title: Asset Presence Model
    description: The presence of an asset. Wraps the AssetPresenceStatus into an object.
    type: object
    required:
      - assetPresence
    properties:
      assetPresence:
        $ref: '#/definitions/AssetPresenceStatus'
  AssetPresenceUpdateModel:
    title: Asset Presence Update Model
    description: The presence update of an asset. Wraps the AssetPresenceUpdateStatus into an object.
    type: object
    required:
      - assetPresence
    properties:
      assetPresence:
        $ref: '#/definitions/AssetPresenceUpdateStatus'
  AssetPresenceWithSystemConnectionModel:
    title: Asset Presence With System Connection Model
    description: The presence of an asset and the connection of the system in which it resides.
    allOf:
      - $ref: '#/definitions/AssetPresenceModel'
      - type: object
        properties:
          systemConnection:
            $ref: '#/definitions/SystemConnectionStatus'
  TemperatureSensorModel:
    title: Temperature Sensor
    description: The sensor name and temperature reading in Celsius.
    type: object
    required:
        - reading
    properties:
      name:
        description: Sensor name
        type: string
        example: Sensor0
      reading:
        description: Sensor reading
        type: number
        format: double
        example: 25.8
  BaseAssetLocationModel:
    title: Base Asset Location Model
    description: Basic information about the asset and the system in which it resides. Base class for other models.
    type: object
    required:
      - minionId
    properties:
      minionId:
        description: Identifier of the minion where the asset is located.
        type: string
        example: NI_PXIe-8135_Embedded_Controller--MAC-00-80-2F-23-52-65
      parent:
        description: The parent of the asset.
        type: string
        example: Chassis1
      resourceUri:
        description: Identifier of a resource.
        type: string
        example: 1/4243/1949942980/01BB877A/3
      slotNumber:
        description: The number of the slot in which the asset is located.
        type: integer
        example: 2
  AssetLocationWithPresenceModel:
    title: Asset Location With Presence Model
    description: Information about the asset location and presence. Used in create operations.
    allOf:
      - $ref: '#/definitions/BaseAssetLocationModel'
      - type: object
        properties:
          state:
            $ref: '#/definitions/AssetPresenceModel'
  AssetLocationWithPresenceUpdateModel:
    title: Asset Location With Presence Update Model
    description: Information about the asset location and presence update. Used in update operations.
    allOf:
      - $ref: '#/definitions/BaseAssetLocationModel'
      - type: object
        properties:
          state:
            $ref: '#/definitions/AssetPresenceUpdateModel'
  AssetLocationModel:
    title: Asset Location Model
    description: Information about the asset location, presence and the connection status of the system in which it resides.
    allOf:
      - $ref: '#/definitions/BaseAssetLocationModel'
      - type: object
        properties:
          systemName:
            description: Hostname of the system.
            type: string
            example: APM-PXI1
          state:
            $ref: '#/definitions/AssetPresenceWithSystemConnectionModel'
  ExternalCalibrationOperatorModel:
    title: External Calibration Operator
    description: The information about the operator who performed the calibration.
    type: object
    properties:
      displayName:
        description: Display name of logged in user.
        type: string
        example: John Doe
      userId:
        description: Identifier of the logged in user.
        type: string
        example: johnDoe2020
  SelfCalibrationModel:
    title: Self-Calibration
    description: Contains data from the last self-calibration.
    type: object
    required:
        - date
    properties:
      temperatureSensors:
          description: An array of temperature sensor information.
          type: array
          items:
            $ref: '#/definitions/TemperatureSensorModel'
      isLimited:
        description: Whether the last self-calibration of the asset was a limited calibration.
        type: boolean
        example: false
      date:
        description: ISO-8601 formatted timestamp specifying the last date the asset was self-calibrated.
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
  ExternalCalibrationBaseModel:
    title: Base External Calibration
    description: Data for an external calibration entry.
    type: object
    required:
        - date
        - recommendedInterval
        - nextRecommendedDate
        - temperatureSensors
    properties:
      temperatureSensors:
          description: An array of temperature sensor information.
          type: array
          items:
            $ref: '#/definitions/TemperatureSensorModel'
      isLimited:
        description: Whether the last external calibration of the asset was a limited calibration.
        type: boolean
        example: false
      date:
        description: ISO-8601 formatted timestamp specifying the last date the asset was externally calibrated.
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
      recommendedInterval:
        description: The manufacturer's recommended calibration interval in months.
        type: integer
        example: 12
      nextRecommendedDate:
        description: ISO-8601 formatted timestamp specifying the recommended date for the next external calibration.
        type: string
        format: date-time
        example: '2019-05-07T18:58:05.219692Z'
      nextCustomDueDate:
        description: ISO-8601 formatted timestamp specifying the date for the next external calibration.
        type: string
        format: date-time
        example: '2019-06-07T18:58:05.219692Z'
      comments:
        description: Calibration comments provided by an operator.
        type: string
        example: This is a comment.
    example:
      temperatureSensors: [
        { name: 'Sensor0' , reading: 25.7 }
      ]
      isLimited: false
      date: '2018-05-07T18:58:05.000Z'
      recommendedInterval: 12
      nextRecommendedDate: '2019-05-07T18:58:05.000Z'
      nextCustomDueDate: '2019-06-07T18:58:05.000Z'
      comments: 'This is a comment.'
  ExternalCalibrationModel:
    title: External Calibration
    description: Data from the last external calibration.
    allOf:
      - $ref: '#/definitions/ExternalCalibrationBaseModel'
      - type: object
        properties:
          entryType:
            $ref: '#/definitions/CalibrationMode'
          operator:
            $ref: '#/definitions/ExternalCalibrationOperatorModel'
        example:
          temperatureSensors: [
            { name: 'Sensor0' , reading: 25.7 }
          ]
          isLimited: false
          date: '2018-05-07T18:58:05.000Z'
          recommendedInterval: 12
          nextRecommendedDate: '2019-05-07T18:58:05.000Z'
          nextCustomDueDate: '2019-06-07T18:58:05.000Z'
          comments: 'This is a comment.'
          entryType: MANUAL
          operator:
            displayName: John Doe
            userId: johnDoe2020
  ExternalCalibrationWithChecksumModel:
    title: External Calibration
    description: Data from the last external calibration including checksum.
    allOf:
      - $ref: '#/definitions/ExternalCalibrationModel'
      - type: object
        properties:
          checksum:
            description: Checksum for the external calibration.
            type: string
            example: 7d9f4953655d48a6a5fd68e9dfd41345
        example:
          temperatureSensors: [
            { name: 'Sensor0' , reading: 25.7 }
          ]
          isLimited: false
          date: '2018-05-07T18:58:05.000Z'
          recommendedInterval: 12
          nextRecommendedDate: '2019-05-07T18:58:05.000Z'
          nextCustomDueDate: '2019-06-07T18:58:05.000Z'
          comments: 'This is a comment.'
          entryType: MANUAL
          operator:
            displayName: John Doe
            userId: johnDoe2020
          checksum: 7d9f4953655d48a6a5fd68e9dfd41345
  BaseAssetModel:
    title: Base Asset Model
    description: An object describing basic properties of an asset. Base class for other models.
    allOf:
      - $ref: '#/definitions/AssetIdentificationModel'
      - type: object
        properties:
          name:
            description: Name of the asset.
            type: string
            example: PCISlot2
          assetType:
            $ref: '#/definitions/AssetType'
          firmwareVersion:
            description: Firmware version of the asset.
            type: string
            example: A1
          hardwareVersion:
            description: Hardware version of the asset.
            type: string
            example: 12A
          visaResourceName:
            description: VISA resource name of the asset.
            type: string
            example : vs-1234
          temperatureSensors:
            description: An array of temperature sensor information.
            type: array
            items:
              $ref: '#/definitions/TemperatureSensorModel'
          supportsSelfCalibration:
            description: Whether the asset supports self-calibration.
            type: boolean
            example: true
          supportsExternalCalibration:
            description: Whether the asset supports external calibration.
            type: boolean
            example: true
          customCalibrationInterval:
            description: The interval represented in months used for computing calibration due date. If not set, the recommended calibration interval from the calibration model is used.
            type: integer
            example: 24
          selfCalibration:
            $ref: '#/definitions/SelfCalibrationModel'
          isNIAsset:
            description: Whether this asset is an NI asset (true) or a third-party asset (false).
            type: boolean
            example: true
          workspace:
            type: string
            description: The ID of the workspace containing the asset.
            example: '5bc5e9092a4fa4c71cfa7197'
          fileIds:
            description: The file IDs linked to the asset.
            type: array
            items:
                type: string
                example: '608a5684800e325b48837c2a'
          supportsSelfTest:
            description: Whether the asset supports self-test.
            type: boolean
            example: true
          supportsReset:
            description: Whether the asset supports reset.
            type: boolean
            example: true
  AssetCreateModel:
    title: Asset Create Model
    description: >-
          An object describing the properties for creating an asset.
          
          
          Unique Asset Identification is required to create an asset. See AssetIdentificationModel for details.
    allOf:
      - $ref: '#/definitions/BaseAssetModel'
      - type: object
        required:
          - name
          - location
        properties:
          location:
            $ref: '#/definitions/AssetLocationWithPresenceModel'
          externalCalibration:
            $ref: '#/definitions/ExternalCalibrationWithChecksumModel'
          discoveryType:
            $ref: '#/definitions/DiscoveryType'
          properties:
            description: Key-value-pair metadata associated with an asset.
            type: object
            additionalProperties:
              type: string
            example:
              Key1: Value1
          keywords:
            description: Words or phrases associated with an asset.
            type: array
            items:
              type: string
              example: Keyword1
  AssetUpdateModel:
    title: Asset Update Model
    description: >-
          An object describing the properties for updating an asset.
          
          
          Unique Asset Identification is required to create an asset. If the id property is not specified, a set of properties are required to identify an asset. See AssetIdentificationModel for details.
          If the id is specified on the model, the following properties will be ignored: busType, modelName, modelNumber, vendorName, vendorNumber and serialNumber.
    allOf:
      - $ref: '#/definitions/BaseAssetModel'
      - type: object
        properties:
          id:
            description: Unique identifier of the asset.
            type: string
            example: "123;01BB877A;4244;0"
          location:
            $ref: '#/definitions/AssetLocationWithPresenceUpdateModel'
          externalCalibration:
            $ref: '#/definitions/ExternalCalibrationWithChecksumModel'
          properties:
            description: Key-value-pair metadata associated with an asset.
            type: object
            additionalProperties:
              type: string
            example:
              Key1: Value1
          keywords:
            description: Words or phrases associated with an asset.
            type: array
            items:
              type: string
              example: Keyword1
  AssetModel:
    title: Asset Model
    description: An object describing an asset with all of its properties.
    allOf:
      - $ref: '#/definitions/BaseAssetModel'
      - type: object
        properties:
          id:
            description: Unique identifier of the asset.
            type: string
            example: "29162;01B245D6;4243;0"
          location:
            $ref: '#/definitions/AssetLocationModel'
          calibrationStatus:
            $ref: '#/definitions/CalibrationStatus'
          isSystemController:
            description: Whether this asset represents a System Controller.
            type: boolean
            example: true
          externalCalibration:
            $ref: '#/definitions/ExternalCalibrationModel'
          discoveryType:
            $ref: '#/definitions/DiscoveryType'
          properties:
            description: Key-value-pair metadata associated with an asset.
            type: object
            additionalProperties:
              type: string
            example:
              Key1: Value1
          keywords:
            description: Words or phrases associated with an asset.
            type: array
            items:
              type: string
              example: Keyword1
          lastUpdatedTimestamp:
            description: ISO-8601 formatted timestamp specifying the last date that the asset has had a property update.
            type: string
            format: date-time
            example: '2018-05-07T18:58:05.219692Z'
  AssetMetadata:
    title: Asset Metadata
    description: Information about asset metadata
    type: object
    properties:
      keywords:
        description: Words or phrases associated with an asset.
        type: array
        items:
          type: string
          example: Keyword1
      properties:
        description: Key-value-pair metadata associated with an asset.
        type: object
        additionalProperties:
          type: string
        example:
          Key1: Value1
  AssetWithAvailabilityHistoryModel:
    title: Asset With Availability History
    description: Information about the availability, or connection, history of an asset, which also contains information about each system in which the asset was present.
    type: object
    properties:
      assetName:
        description: The asset name for which availability history is computed.
        type: string
        example: PCI-Slot2
      assetIdentifier:
        description: The identifier of the asset for which availability history is computed.
        type: string
        example: 29162;01B245D6;4243;0
      availabilityHistory:
        description: The availability history for the asset consisting in availability information for each system in which the asset was present.
        type: array
        items:
          $ref: '#/definitions/OverallAvailabilityInTimespanModel'
    required:
      - assetName
      - assetIdentifier
      - availabilityHistory
  AvailabilityTimeInterval:
    title: Availability Time Interval
    description: Time interval containing a start and an end date.
    type: object
    properties:
      startDate:
        description: >-
          A date value which can be used to specify the beginning of a timespan. 
          
          This parameter is required to have the "ISO 8601" format in order to be considered valid. 
          
          The time component of the request is ignored.
        type: string
        format: date-time
        example: '2018-05-01T00:00:00Z'
      endDate:
        description: >- 
          A date value which can be used to specify the end of a timespan.
          
          This parameter is required to have the "ISO 8601" format in order to be considered valid. 
          
          The time component of the request is ignored.
        type: string
        format: date-time
        example: '2018-05-20T00:00:00Z'
    required:
      - startDate
      - endDate
  AssetWithAvailabilityInIntervalModel:
    title: Asset With Availability In Interval
    description: Information about the availability, or connection history, of an asset. This includes the name of each system in which the asset was present during an interval of time you specify.
    type: object
    properties:
      assetName:
        description: The asset name for which the availability was computed.
        type: string
        example: PCI-Slot2
      assetIdentifier:
        description: The identifier of the asset for which the availability was computed.
        type: string
        example: 29162;01B245D6;4243;0
      interval:
        $ref: '#/definitions/AvailabilityTimeInterval'
      availabilityInSystems:
        description: List containing the availability percentage of an asset for each system it was present in during a given time interval.
        type: array
        items:
          $ref: '#/definitions/AssetAvailabilityInSystemModel'
  AssetAvailabilityInSystemModel:
    title: Asset Availability In System Model
    description: Contains the availability percentage and the name of the system an asset was present in during an interval.
    type: object
    properties:
      systemName:
        description: Name of the system to which the availability data corresponds.
        type: string
        example: 'PXI1'
      availabilityPercentage:
        description: The percentage of time in which the asset was available in the system.
        type: number
        format: double
        example: 7.38958
    required:
      - systemName
      - availabilityPercentage
  OverallAvailabilityInSystemModel:
    title: Overall Availability In System
    description: Availability information for an asset in a single system for the specified timespan.
    type: object
    properties:
      key:
        description: Date representing the beginning of a timespan.
        type: string
        example: 2018/11/01
      value:
        description: The percentage of time in which the asset was available in a system during the specific timespan.
        type: number
        format: double
        example: 7.38958
    required:
      - key
      - value
  OverallAvailabilityInTimespanModel:
    title: Overall Availability In Timespan
    description: Contains availability information for an asset in a single system for the specified timespan.
    type: object
    properties:
      key:
        description: The name of the system in which the asset was available.
        type: string
        example: APM-PXI1
      value:
        description: The percentage of time in which the asset was available in a system during a specific timespan.
        type: number
        format: double
        example: 7.38958
    required:
      - key
      - value
  ResponseFormat:
    title: Response Format
    description: The return type. Valid options are "JSON" and "CSV".
    type: string
    default: JSON
    enum:
      - JSON
      - CSV
  Destination:
    title: Request Destination
    description:
      The destination of the request.
      "INLINE" (default) returns the list of resources as the body of the response.
      "DOWNLOAD" returns the list of resources as the body of the response and indicates to the client that it should be downloaded as a file.
      "FILE_SERVICE" sends the list of resources to the file ingestion service and returns the ID of the file to the client in a JSON object.
    type: string
    default: INLINE
    enum:
      - INLINE
      - DOWNLOAD
      - FILE_SERVICE
  FileIngestionWorkspace:
    title: File Ingestion Workspace
    description: The ID of the workspace to put the file into, if the destination is "FILE_SERVICE".
    type: string
    example: '5bc5e9092a4fa4c71cfa7197'
  QueryHistoryRequestModel:
    title: Query History Request Model
    description: Object containing options for querying history.
    type: object
    properties:
      responseFormat:
        $ref: '#/definitions/ResponseFormat'
      destination:
        $ref: '#/definitions/Destination'
      fileIngestionWorkspace:
        $ref: '#/definitions/FileIngestionWorkspace'
    example:
      responseFormat: CSV
      destination: DOWNLOAD
  ServicePolicyModel:
    title: Service policy
    description: An object containing the service policy.
    type: object
    properties:
      calibrationPolicy:
        description: Calibration policy
        type: object
        properties:
          daysForApproachingCalibrationDueDate:
            description: The number of days for an asset to be considered as approaching calibration.
            type: integer
            example: 30
      workingHoursPolicy:
        description: An object that describes the start time and end time of a working day.
        type: object
        properties:
          startTime:
            description: A string formatted as an hour with minutes and seconds representing the start time of a working day.
            type: string
            example: "09:00:00"
          endTime:
            description: A string formatted as an hour with minutes and seconds representing the end time of a working day.
            type: string
            example: "17:00:00"
  UtilizationHistoryField:
    title: Asset Utilization History Field
    description: An enumeration of all fields in an Asset Utilization History record.
    type: string
    enum:
      - UTILIZATION_IDENTIFIER
      - ASSET_IDENTIFIER
      - MINION_ID
      - CATEGORY
      - TASK_NAME
      - USER_NAME
      - START_TIMESTAMP
    example:
      START_TIMESTAMP
  AssetIdentificationModel:
    title: Asset Identification
    description: >-
        Object containing properties which identify an asset.
        An asset is uniquely identified by a combination of:
            - busType
            - modelName or modelNumber
            - vendorName or vendorNumber
            - serialNumber or minionId (part of the Location)
    type: object
    properties:
      modelName:
        description: Model name of the asset.
        type: string
        example: "NI PXIe-6368"
      modelNumber:
        description: Model number of the asset.
        type: integer
        example : 123
      serialNumber:
        description: Serial number of the asset.
        type: string
        example: "01BB877A"
      vendorName:
        description: Vendor name of the asset.
        type: string
        example: NI
      vendorNumber:
        description: Vendor number of the asset.
        type: integer
        example: 4244
      busType:
        $ref: '#/definitions/BusType'
  UtilizationIdentifiersWithTimestampModel:
    title: Utilization Identifiers With Timestamp
    description: Object containing a collection of utilization identifiers with a timestamp.
    type: object
    required:
      - utilizationIdentifiers
      - utilizationTimestamp
    properties:
      utilizationIdentifiers:
        description: Array representing the unique identifier of an asset utilization history record.
        type: array
        items:
          type: string
          example: "2916201B245D642430"
      utilizationTimestamp:
        description: >-
          A date time value which can be used to specify the end of an asset utilization.

          This parameter must have the "ISO 8601" format in order to be considered valid.
        type: string
        format: date-time
        example: '2019-05-01T00:00:00.519Z'
  Skip:
    description:
      The number of resources to skip in the result when paging.
      For example, a list of 100 resources with a skip value of 50 will return
      entries 51 through 100.
    type: integer
    default: 0
    example: 0
    x-example: 0
  Take:
    description:
      How many resources to return in the result, or -1 to take all.
      The default is 1000.
      For example, a list of 100 resources with a take value of 25 will return
      entries 1 through 25.
    type: integer
    default: 1000
    example: 1000
    x-example: 1000
  UtilizationTimeIntervalModel:
    title:  Utilization Time Interval
    description: Time interval for which to retrieve asset/system utilization.
    type: object
    properties:
        startDate:
            description: >-
                A date time value which can be used to specify the beginning of a timespan.

                This parameter is required to have the "ISO 8601" format in order to be considered valid. 
            
                The time component of the request is ignored.
            type: string
            format: date-time
            example: '2019-05-01T00:00:00.000Z'
        endDate:
            description: >-
                A date time value which can be used to specify the end of a timespan.

                This parameter is required to have the "ISO 8601" format in order to be considered valid.
            
                The time component of the request is ignored.
            type: string
            format: date-time
            example: '2019-05-20T00:00:000Z' 
parameters:
  TimespanGranularity:
    in: query
    name: granularity
    description: The possible granularities that can be used to obtain asset availability. WEEK is used when no granularity is specified.
    type: string
    enum:
      - NONE
      - WEEK
      - MONTH
  AssetId:
    in: path
    name: assetId
    description: The identifier of an asset.
    type: string
    required: true
    x-example: "29162;01B245D6;4243;0"
  FileId:
    in: path
    name: fileId
    description: The identifier of a file.
    type: string
    required: true
    x-example: "607fffe41e4564dda3593eb0"
  Skip:
    in: query
    name: skip
    description:
      The number of resources to skip in the result when paging.
      For example, a list of 100 resources with a skip value of 50 will return
      entries 51 through 100.
    type: integer
    default: 0
    x-example: 0
  Take:
    in: query
    name: take
    description:
      How many resources to return in the result, or -1 to take all.
      The default is 1000.
      For example, a list of 100 resources with a take value of 25 will return
      entries 1 through 25.
    type: integer
    default: 1000
    x-example: 1000
  AssetAvailabilityComparison:
    in: body
    name: compareAvailability
    description: Request body consisting in a time interval and a list of assets to compute availability history for.
    schema:
      title: Compare Asset Availability
      type: object
      required:
        - assetIds
        - startDate
        - endDate
      properties:
        assetIds:
          description: Multiple asset identifiers for which to compare availability history.
          type: array
          items:
            type: string
          example: ["29162;01B245D6;4243;0", "29162;01B245D6;4243;1"]
        startDate:
          description: >-
            A date value which can be used to specify the beginning of a timespan. 
            
            This parameter is required to have the "ISO 8601" format in order to be considered valid. 
            
            The time component of the request is ignored.
          type: string
          example: '2018-05-01T00:00:00.519Z'
        endDate:
          description: >- 
            A date value which can be used to specify the end of a timespan.
            
            This parameter is required to have the "ISO 8601" format in order to be considered valid. 
            
            The time component of the request is ignored.
          type: string
          example: '2018-05-20T00:00:00Z'
    required: true
  QueryAssetsAvailabilityRequestBody:
    in: body
    name: queryAssetsAvailability
    description: Request body containing a list of asset identifiers and a list of time intervals.
    schema:
      title: Query Assets Availability Request Body
      type: object
      required:
        - ids
        - intervals
      properties:
        ids:
          description: Multiple asset identifiers for which the availability data is retrieved.
          type: array
          items:
            type: string
          example: ["29162;01B245D6;4243;0", "29162;01B245D6;4243;1"]
        intervals:
          description: Time intervals for which the availability data is retrieved.
          type: array
          items:
            $ref: '#/definitions/AvailabilityTimeInterval'
  QueryAssetsAvailabilityReportRequestBody:
    in: body
    name: queryAssetsAvailabilityReport
    description: Request body containing a list of asset identifiers and a list of time intervals.
    schema:
      title: Query Assets Availability Report Request Body
      type: object
      required:
        - ids
        - intervals
      properties:
        ids:
          description: Multiple asset identifiers for which the availability data is retrieved.
          type: array
          items:
            type: string
          example: ["29162;01B245D6;4243;0", "29162;01B245D6;4243;1"]
        intervals:
          description: Time intervals for which the availability data is retrieved.
          type: array
          items:
            $ref: '#/definitions/AvailabilityTimeInterval'
  DeleteAssetsRequestBody:
    in: body
    name: deleteAssets
    description: Request body containing identifiers of the assets for which all data must be deleted.
    required: true
    schema:
      title: Delete Assets Request
      description: Request body containing identifiers of the assets to delete all information for.
      type: object
      properties:
        ids:
          description: Multiple asset identifiers for which to delete all data.
          type: array
          items:
            type: string
          example: ["29162;01B245D6;4243;0"]
  CreateAssetsRequestBody:
    in: body
    name: createAssets
    description: Request body containing an array of assets that should be created.
    required: true
    schema:
      title: Create Assets Request
      description: Request body containing an array of assets that should be created.
      type: object
      properties:
        assets:
          description: Multiple assets that should be created.
          type: array
          items:
            $ref: '#/definitions/AssetCreateModel'
  UpdateAssetsRequestBody:
    in: body
    name: updateAssets
    description: Request body containing an array of assets to update.
    required: true
    schema:
      title: Update Assets Request
      description: Request body containing an array of assets to update.
      type: object
      properties:
        assets:
          description: Multiple assets that should be updated.
          type: array
          items:
            $ref: '#/definitions/AssetUpdateModel'
  DeleteCalibrationsRequestBody:
    in: body
    name: deleteCalibrationsRequestBody
    description: Request body containing identifiers of the calibration history entries to delete.
    schema:
      title: Delete Calibrations Request
      description: Request body containing identifiers of the calibration history entries to delete.
      type: object
      properties:
        calibrationIds:
          description: Identifiers of the calibration entries to delete.
          type: array
          items:
            type: string
          example: ["5c4f0834174ae321b8a95a03"]
  ExternalCalibrationRequestBody:
    in: body
    name: externalCalibrationRequestBody
    description: Request body containing data to create a new external calibration entry for an asset.
    schema:
      title: Post External Calibration Request
      description: Request body containing data to create a new external calibration entry for an asset.
      type: object
      properties:
        externalCalibration:
          $ref: '#/definitions/ExternalCalibrationWithChecksumModel'
  UpdateMetadata:
    in: body
    name: updateMetadata
    description: >-
      The metadata to be updated on the asset. The method overrides any asset metadata with what is contained in the request.

      - In order to ignore metadata properties update, leave the value off the request.

      - In order to set the value to null, assign an empty array or an empty object to the request metadata object.
    required: true
    schema:
      title: Update Metadata Request
      description: The asset metadata information to be updated.
      type: object
      properties:
        keywords:
          description: Keywords associated with an asset.
          type: array
          items:
            type: string
            example: Keyword1
        properties:
          description: Properties associated with an asset.
          type: object
          additionalProperties:
            type: string
          example:
            Key1: Value1
  LinkFiles:
    in: body
    name: linkFiles
    description: Link files to an asset.
    required: true
    schema:
      title: Link Files Request
      description: Link files to an asset
      type: object
      properties:
        fileIds:
          description: File IDs to be linked to an asset.
          type: array
          items:
            type: string
            example: 607fffe41e4564dda3593eb0
  QueryInUseAssetsRequest:
    in: body
    name: queryInUseAssets
    description: Request body consisting of filters to apply when retrieving assets currently being utilized.
    schema:
      title: Query In Use Assets Request
      description: Object containing filters to apply when retrieving utilized assets.
      type: object
      properties:
        assetFilter:
          description: >-
            The filter criteria for assets. Consists of a string of queries composed using AND/OR operators.
            String values and date strings need to be enclosed in double quotes.
            Parenthesis can be used around filters to better define the order of operations.

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

            - Contains operator '.Contains()', used to check whether a string contains another string. Example: 'x.Contains(y)'

            - Does not contain operator '!.Contains()', used to check whether a string does not contain another string. Example: '!x.Contains(y)'


            Valid asset properties that can be used in the filter:

            - AssetIdentifier: String representing the unique identifier of an asset.

            - SerialNumber: String representing the serial number of an asset.

            - ModelName: String representing the model name of an asset.

            - ModelNumber: Unsigned integer representing the model number of an asset.

            - VendorName: String representing the vendor name of an asset.

            - VendorNumber: Unsigned integer representing the vendor number of an asset.

            - AssetName: String representing the asset name.

            - FirmwareVersion: String representing the firmware version of an asset.

            - HardwareVersion: String representing the hardware version of an asset.

            - BusType: String enumeration representing the bus type of an asset. Possible values are: BUILT_IN_SYSTEM, PCI_PXI, USB, GPIB, VXI, SERIAL, TCP_IP, CRIO, SCXI, CDAQ, SWITCH_BLOCK, SCC, FIRE_WIRE, ACCESSORY, CAN, SWITCH_BLOCK_DEVICE, SLSC.

            - IsNIAsset: Boolean flag specifying whether the asset is an NI asset or a third-party asset.

            - Keywords: Collection of string values representing asset metadata keywords. Example: 'Keywords=["keyword1", "keyword2"]'.

            - Properties: Collection of key-value pairs, each key-value pair representing an asset metadata property. Example: 'Properties=["key1":"value1", "key2":"value2"]'.

            - Location.MinionId: String representing the identifier of the minion in which the asset is located in.

            - Location.SystemName: String representing the name of the system that the asset is located in.

            - Location.SlotNumber: Unsigned integer representing the slot number the asset is located in.

            - Location.AssetState.SystemConnection: String enumeration representing the connection state of the system the asset is currently located in. Possible values are: APPROVED, DISCONNECTED, CONNECTED_UPDATE_PENDING, CONNECTED_UPDATE_SUCCESSFUL, CONNECTED_UPDATE_FAILED, UNSUPPORTED, ACTIVATED.

            - Location.AssetState.AssetPresence: String enumeration representing the present status of an asset in a system. Possible values are: INITIALIZING, UNKNOWN, NOT_PRESENT, PRESENT.

            - SupportsSelfCalibration: Boolean flag specifying whether the asset supports self-calibration.

            - SelfCalibration.CalibrationDate: ISO-8601 formatted timestamp string specifying the last date the asset was self-calibrated. Example: "2018-05-20T00:00:00Z"

            - SupportsExternalCalibration: Boolean flag specifying whether the asset supports external calibration.

            - CustomCalibrationInterval: Integer representing the custom calibration interval, in months.

            - CalibrationStatus: String enumeration representing the calibration status of an asset. Possible values are: OK, APPROACHING_RECOMMENDED_DUE_DATE, PAST_RECOMMENDED_DUE_DATE.

            - ExternalCalibration.CalibrationDate: ISO-8601 formatted timestamp string specifying the last date the asset was externally-calibrated. Example: "2018-05-20T00:00:00Z"

            - ExternalCalibration.NextRecommendedDate: ISO-8601 formatted timestamp string specifying the recommended date for the next external calibration. Example: "2018-05-20T00:00:00Z"

            - ExternalCalibration.RecommendedInterval: Integer representing the manufacturer-recommended calibration interval, in months.

            - ExternalCalibration.Comments: String representing any external calibration comments.

            - ExternalCalibration.IsLimited: Boolean flag specifying whether the last external calibration was a limited calibration.

            - ExternalCalibration.Operator.DisplayName: String representing the name of the operator which performed an external calibration on a third-party asset.
          type: string
          example: IsSystemController = True
        utilizationFilter:
          description: >-
            The filter criteria for asset utilization. Consists of a string of queries composed using AND/OR operators.
            String values and date strings need to be enclosed in double quotes.
            Parenthesis can be used around filters to better define the order of operations.

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

            - Contains operator '.Contains()', used to check whether a string contains another string. Example: 'x.Contains(y)'

            - Does not contain operator '!.Contains()', used to check whether a string does not contain another string. Example: '!x.Contains(y)'


            Valid asset utilization properties that can be used in the filter:

            - MinionId:  String representing the identifier of a minion in which an asset might be located in.

            - Category: String representing the utilization task category.

            - UserName: : String representing the name of the operator who utilized the asset.
          type: string
          example: Category = "Test"
        skip:
          description:
            The number of resources to skip in the result when paging.
            For example, a list of 100 resources with a skip value of 50 will return
            entries 51 through 100.
          type: integer
          default: 0
          example: 0
        take:
          description: The maximum number of asset utilization history records to return.
          type: integer
          format: int32
          default: 1000
          minimum: 0
          example: 1000
  QueryAssetsRequest:
    in: body
    name: queryAssets
    description: Request body consisting of filters to apply when retrieving assets. Currently, the valid combinations of ResponseFormat and Destination are [JSON;INLINE], [CSV;DOWNLOAD], [CSV;FILE_SERVICE].
    schema:
      title: Query Assets Request
      description: Object containing filters to apply when retrieving assets. If no assets match the filter and the destination is "DOWNLOAD" or "FILE_SERVICE", an empty report will be generated.
      type: object
      properties:
        ids:
          description: Identifiers of the assets to be retrieved.
          type: array
          items:
            type: string
          example: []
        responseFormat:
          $ref: '#/definitions/ResponseFormat'
        destination:
          $ref: '#/definitions/Destination'
        fileIngestionWorkspace:
          $ref: '#/definitions/FileIngestionWorkspace'
        skip:
          $ref: '#/definitions/Skip'
        take:
          $ref: '#/definitions/Take'
        calibratableOnly:
          description: >-
            Whether to generate a report with calibrated asset specific columns.

            When the destination is "DOWNLOAD or "FILE_SERVICE" this property is used as follows:

            - It determines the type of the report. When true, the file will be a calibration report. If this is false, the file will be an asset report. 
            
            - If asset IDs property or the filter string are in the request, this property will not be used for filtering. If no asset IDs are in the request and the filter string is unspecified, setting this property to true will generate a report only for the calibrated assets.
          
          type: boolean
          default: false
        filter:
          description: >-
            The filter criteria for assets. Consists of a string of queries composed using AND/OR operators.
            String values and date strings need to be enclosed in double quotes.
            Parenthesis can be used around filters to better define the order of operations.

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

            - Contains operator '.Contains()', used to check whether a string contains another string. Example: 'x.Contains(y)'

            - Does not contain operator '!.Contains()', used to check whether a string does not contain another string. Example: '!x.Contains(y)'


            Valid asset properties that can be used in the filter:

            - AssetIdentifier: String representing the unique identifier of an asset.

            - SerialNumber: String representing the serial number of an asset.

            - ModelName: String representing the model name of an asset.

            - ModelNumber: Unsigned integer representing the model number of an asset.

            - VendorName: String representing the vendor name of an asset.

            - VendorNumber: Unsigned integer representing the vendor number of an asset.

            - AssetName: String representing the asset name.

            - FirmwareVersion: String representing the firmware version of an asset.

            - HardwareVersion: String representing the hardware version of an asset.

            - BusType: String enumeration representing the bus type of an asset. Possible values are: BUILT_IN_SYSTEM, PCI_PXI, USB, GPIB, VXI, SERIAL, TCP_IP, CRIO, SCXI, CDAQ, SWITCH_BLOCK, SCC, FIRE_WIRE, ACCESSORY, CAN, SWITCH_BLOCK_DEVICE, SLSC.

            - IsNIAsset: Boolean flag specifying whether the asset is an NI asset or a third-party asset.

            - Keywords: Collection of string values representing asset metadata keywords. Example: 'Keywords=["keyword1", "keyword2"]'.

            - Properties: Collection of key-value pairs, each key-value pair representing an asset metadata property. Example: 'Properties=["key1":"value1", "key2":"value2"]'.

            - Location.MinionId: String representing the identifier of the minion in which the asset is located in.

            - Location.SystemName: String representing the name of the system that the asset is located in.

            - Location.SlotNumber: Unsigned integer representing the slot number the asset is located in.

            - Location.AssetState.SystemConnection: String enumeration representing the connection state of the system the asset is currently located in. Possible values are: APPROVED, DISCONNECTED, CONNECTED_UPDATE_PENDING, CONNECTED_UPDATE_SUCCESSFUL, CONNECTED_UPDATE_FAILED, UNSUPPORTED, ACTIVATED.

            - Location.AssetState.AssetPresence: String enumeration representing the present status of an asset in a system. Possible values are: INITIALIZING, UNKNOWN, NOT_PRESENT, PRESENT.

            - SupportsSelfCalibration: Boolean flag specifying whether the asset supports self-calibration.

            - SelfCalibration.CalibrationDate: ISO-8601 formatted timestamp string specifying the last date the asset was self-calibrated. Example: "2018-05-20T00:00:00Z"

            - SupportsExternalCalibration: Boolean flag specifying whether the asset supports external calibration.

            - CustomCalibrationInterval: Integer representing the custom calibration interval, in months.

            - CalibrationStatus: String enumeration representing the calibration status of an asset. Possible values are: OK, APPROACHING_RECOMMENDED_DUE_DATE, PAST_RECOMMENDED_DUE_DATE.

            - ExternalCalibration.CalibrationDate: ISO-8601 formatted timestamp string specifying the last date the asset was externally-calibrated. Example: "2018-05-20T00:00:00Z"

            - ExternalCalibration.NextRecommendedDate: ISO-8601 formatted timestamp string specifying the recommended date for the next external calibration. Example: "2018-05-20T00:00:00Z"

            - ExternalCalibration.RecommendedInterval: Integer representing the manufacturer-recommended calibration interval, in months.

            - ExternalCalibration.Comments: String representing any external calibration comments.

            - ExternalCalibration.IsLimited: Boolean flag specifying whether the last external calibration was a limited calibration.

            - ExternalCalibration.Operator.DisplayName: String representing the name of the operator which performed an external calibration on a third-party asset.
          type: string
          example: IsSystemController = True
  QueryHistoryRequestBody:
    in: body
    name: queryHistory
    description: Request body consisting of options to be used for querying history for an asset.
    schema:
      $ref: '#/definitions/QueryHistoryRequestModel'
  ServicePolicyUpdateRequestBody:
    in: body
    name: servicePolicyUpdateRequest
    required: true
    description: The request to update properties of the current service policy.
    schema:
      $ref: '#/definitions/ServicePolicyModel'
  QueryAssetUtilizationRequest:
    in: body
    name: queryBody
    description: Request body consisting of filters for asset utilization, assets, and time intervals.
    schema:
      title: Query Asset Utilizations Request
      description: Object containing filters for asset utilization, assets, and time intervals.
      type: object
      required:
        - utilizationIntervals
      properties:
        utilizationFilter:
          description: >-
            The filter criteria for asset utilization. Consists of a string of queries composed using AND/OR operators.
            String values and date strings need to be enclosed in double quotes.
            Parenthesis can be used around filters to better define the order of operations.

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

            - Contains operator '.Contains()', used to check whether a string contains another string. Example: 'x.Contains(y)'

            - Does not contain operator '!.Contains()', used to check whether a string does not contain another string. Example: '!x.Contains(y)'


            Valid asset utilization properties that can be used in the filter:

            - MinionId:  String representing the identifier of a minion in which an asset might be located in.

            - Category: String representing the utilization task category.

            - UserName: : String representing the name of the operator who utilized the asset.
          type: string
          example: Category = "Test"
        assetFilter:
          description: >-
              The filter criteria for assets. Consists of a string of queries composed using AND/OR operators.
              String values and date strings need to be enclosed in double quotes.
              Parenthesis can be used around filters to better define the order of operations.

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

              - Contains operator '.Contains()', used to check whether a string contains another string. Example: 'x.Contains(y)'

              - Does not contain operator '!.Contains()', used to check whether a string does not contain another string. Example: '!x.Contains(y)'


              Valid asset properties that can be used in the filter:

              - AssetIdentifier: String representing the unique identifier of an asset.

              - SerialNumber: String representing the serial number of an asset.

              - ModelName: String representing the model name of an asset.

              - ModelNumber: Unsigned integer representing the model number of an asset.

              - VendorName: String representing the vendor name of an asset.

              - VendorNumber: Unsigned integer representing the vendor number of an asset.

              - AssetName: String representing the asset name.

              - FirmwareVersion: String representing the firmware version of an asset.

              - HardwareVersion: String representing the hardware version of an asset.

              - BusType: String enumeration representing the bus type of an asset. Possible values are: BUILT_IN_SYSTEM, PCI_PXI, USB, GPIB, VXI, SERIAL, TCP_IP, CRIO, SCXI, CDAQ, SWITCH_BLOCK, SCC, FIRE_WIRE, ACCESSORY, CAN, SWITCH_BLOCK_DEVICE, SLSC.

              - IsNIAsset: Boolean flag specifying whether the asset is an NI asset or a third-party asset.

              - Keywords: Collection of string values representing asset metadata keywords. Example: 'Keywords=["keyword1", "keyword2"]'.

              - Properties: Collection of key-value pairs, each key-value pair representing an asset metadata property. Example: 'Properties=["key1":"value1", "key2":"value2"]'.

              - Location.MinionId: String representing the identifier of the minion in which the asset is located in.

              - Location.SystemName: String representing the name of the system that the asset is located in.

              - Location.SlotNumber: Unsigned integer representing the slot number the asset is located in.

              - Location.AssetState.SystemConnection: String enumeration representing the connection state of the system the asset is currently located in. Possible values are: APPROVED, DISCONNECTED, CONNECTED_UPDATE_PENDING, CONNECTED_UPDATE_SUCCESSFUL, CONNECTED_UPDATE_FAILED, UNSUPPORTED, ACTIVATED.

              - Location.AssetState.AssetPresence: String enumeration representing the present status of an asset in a system. Possible values are: INITIALIZING, UNKNOWN, NOT_PRESENT, PRESENT.

              - SupportsSelfCalibration: Boolean flag specifying whether the asset supports self-calibration.

              - SelfCalibration.CalibrationDate: ISO-8601 formatted timestamp string specifying the last date the asset was self-calibrated. Example: "2018-05-20T00:00:00Z"
              
              - SupportsExternalCalibration: Boolean flag specifying whether the asset supports external calibration.

              - CustomCalibrationInterval: Integer representing the custom calibration interval, in months.
              
              - CalibrationStatus: String enumeration representing the calibration status of an asset. Possible values are: OK, APPROACHING_RECOMMENDED_DUE_DATE, PAST_RECOMMENDED_DUE_DATE.

              - ExternalCalibration.CalibrationDate: ISO-8601 formatted timestamp string specifying the last date the asset was externally-calibrated. Example: "2018-05-20T00:00:00Z"

              - ExternalCalibration.NextRecommendedDate: ISO-8601 formatted timestamp string specifying the recommended date for the next external calibration. Example: "2018-05-20T00:00:00Z"

              - ExternalCalibration.RecommendedInterval: Integer representing the manufacturer-recommended calibration interval, in months.

              - ExternalCalibration.Comments: String representing any external calibration comments.

              - ExternalCalibration.IsLimited: Boolean flag specifying whether the last external calibration was a limited calibration.

              - ExternalCalibration.Operator.DisplayName: String representing the name of the operator which performed an external calibration on a third-party asset.
          type: string
          example: IsNIAsset = true
        utilizationIntervals:
          description: Multiple time intervals for which to retrieve asset utilization.
          type: array
          items:
            $ref: '#/definitions/UtilizationTimeIntervalModel'
  QuerySystemUtilizationRequest:
    in: body
    name: queryBody
    description: Request body consisting of filters for asset utilization, assets, and time intervals.
    schema:
      title: Query System Utilizations Request
      description: Object containing filters for asset utilization, assets, and time intervals.
      type: object
      required:
        - utilizationIntervals
      properties:
        utilizationFilter:
          description: >-
            The filter criteria for asset utilization. Consists of a string of queries composed using AND/OR operators.
            String values and date strings need to be enclosed in double quotes.
            Parenthesis can be used around filters to better define the order of operations.

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

            - Contains operator '.Contains()', used to check whether a string contains another string. Example: 'x.Contains(y)'

            - Does not contain operator '!.Contains()', used to check whether a string does not contain another string. Example: '!x.Contains(y)'


            Valid asset utilization properties that can be used in the filter:

            - MinionId:  String representing the identifier of a minion in which an asset might be located in.

            - Category: String representing the utilization task category.

            - UserName: : String representing the name of the operator who utilized the asset.
          type: string
          example: Category = "Test"
        assetFilter:
          description: >-
              The filter criteria for assets. Consists of a string of queries composed using AND/OR operators.
              String values and date strings need to be enclosed in double quotes.
              Parenthesis can be used around filters to better define the order of operations.

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

              - Contains operator '.Contains()', used to check whether a string contains another string. Example: 'x.Contains(y)'

              - Does not contain operator '!.Contains()', used to check whether a string does not contain another string. Example: '!x.Contains(y)'


              Valid asset properties that can be used in the filter:

              - AssetIdentifier: String representing the unique identifier of an asset.

              - SerialNumber: String representing the serial number of an asset.

              - ModelName: String representing the model name of an asset.

              - ModelNumber: Unsigned integer representing the model number of an asset.

              - VendorName: String representing the vendor name of an asset.

              - VendorNumber: Unsigned integer representing the vendor number of an asset.

              - AssetName: String representing the asset name.

              - FirmwareVersion: String representing the firmware version of an asset.

              - HardwareVersion: String representing the hardware version of an asset.

              - BusType: String enumeration representing the bus type of an asset. Possible values are: BUILT_IN_SYSTEM, PCI_PXI, USB, GPIB, VXI, SERIAL, TCP_IP, CRIO, SCXI, CDAQ, SWITCH_BLOCK, SCC, FIRE_WIRE, ACCESSORY, CAN, SWITCH_BLOCK_DEVICE, SLSC.

              - IsNIAsset: Boolean flag specifying whether the asset is an NI asset or a third-party asset.

              - Keywords: Collection of string values representing asset metadata keywords. Example: 'Keywords=["keyword1", "keyword2"]'.

              - Properties: Collection of key-value pairs, each key-value pair representing an asset metadata property. Example: 'Properties=["key1":"value1", "key2":"value2"]'.

              - Location.MinionId: String representing the identifier of the minion in which the asset is located in.

              - Location.SystemName: String representing the name of the system that the asset is located in.

              - Location.SlotNumber: Unsigned integer representing the slot number the asset is located in.

              - Location.AssetState.SystemConnection: String enumeration representing the connection state of the system the asset is currently located in. Possible values are: APPROVED, DISCONNECTED, CONNECTED_UPDATE_PENDING, CONNECTED_UPDATE_SUCCESSFUL, CONNECTED_UPDATE_FAILED, UNSUPPORTED, ACTIVATED.

              - Location.AssetState.AssetPresence: String enumeration representing the present status of an asset in a system. Possible values are: INITIALIZING, UNKNOWN, NOT_PRESENT, PRESENT.

              - SupportsSelfCalibration: Boolean flag specifying whether the asset supports self-calibration.

              - SelfCalibration.CalibrationDate: ISO-8601 formatted timestamp string specifying the last date the asset was self-calibrated. Example: "2018-05-20T00:00:00Z"
              
              - SupportsExternalCalibration: Boolean flag specifying whether the asset supports external calibration.

              - CustomCalibrationInterval: Integer representing the custom calibration interval, in months.
              
              - CalibrationStatus: String enumeration representing the calibration status of an asset. Possible values are: OK, APPROACHING_RECOMMENDED_DUE_DATE, PAST_RECOMMENDED_DUE_DATE.

              - ExternalCalibration.CalibrationDate: ISO-8601 formatted timestamp string specifying the last date the asset was externally-calibrated. Example: "2018-05-20T00:00:00Z"

              - ExternalCalibration.NextRecommendedDate: ISO-8601 formatted timestamp string specifying the recommended date for the next external calibration. Example: "2018-05-20T00:00:00Z"

              - ExternalCalibration.RecommendedInterval: Integer representing the manufacturer-recommended calibration interval, in months.

              - ExternalCalibration.Comments: String representing any external calibration comments.

              - ExternalCalibration.IsLimited: Boolean flag specifying whether the last external calibration was a limited calibration.

              - ExternalCalibration.Operator.DisplayName: String representing the name of the operator which performed an external calibration on a third-party asset.
          type: string
          example: IsNIAsset = true
        utilizationIntervals:
          description: Multiple time intervals for which to retrieve system utilization.
          type: array
          items:
            $ref: '#/definitions/UtilizationTimeIntervalModel'
  QueryAssetUtilizationHistoryRequest:
    in: body
    name: queryBody
    description: Request body consisting of filters for asset utilization and assets, with ordering and continuation token support.
    schema:
      title: Query Asset Utilization History Request
      description: Object containing filters for asset utilization and assets. When continuation token is used, the orderBy parameter needs to be provided as well.
      type: object
      properties:
        utilizationFilter:
          description: >-
            The filter criteria for asset utilization. Consists of a string of queries composed using AND/OR operators.
            String values and date strings need to be enclosed in double quotes.
            Parenthesis can be used around filters to better define the order of operations.

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

            - Contains operator '.Contains()', used to check whether a string contains another string. Example: 'x.Contains(y)'

            - Does not contain operator '!.Contains()', used to check whether a string does not contain another string. Example: '!x.Contains(y)'

            Valid asset utilization properties that can be used in the filter:

            - MinionId: String representing the identifier of a minion in which an asset might be located in.

            - Category: String representing the utilization task category.

            - UserName: String representing the name of the operator who utilized the asset.

            - TaskName: String representing the name of the task.

            - StartTimestamp:
                description: >-
                  A date time value which can be used to specify the start of an utilization.

                  This parameter is required to have the "ISO 8601" format in order to be considered valid.
                type: string
                format: date-time
                example: '2019-05-20T00:00:00Z'
            - EndTimestamp:
                description: >-
                  A date time value which can be used to specify the end of an utilization.

                  This parameter is required to have the "ISO 8601" format in order to be considered valid.
                type: string
                format: date-time
                example: '2019-05-20T00:00:00Z'
          type: string
          example: Category = "Test"
        assetFilter:
          description: >-
              The filter criteria for assets. Consists of a string of queries composed using AND/OR operators.
              String values and date strings need to be enclosed in double quotes.
              Parenthesis can be used around filters to better define the order of operations.

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

              - Contains operator '.Contains()', used to check whether a string contains another string. Example: 'x.Contains(y)'

              - Does not contain operator '!.Contains()', used to check whether a string does not contain another string. Example: '!x.Contains(y)'


              Valid asset properties that can be used in the filter:

              - AssetIdentifier: String representing the unique identifier of an asset.

              - SerialNumber: String representing the serial number of an asset.

              - ModelName: String representing the model name of an asset.

              - ModelNumber: Unsigned integer representing the model number of an asset.

              - VendorName: String representing the vendor name of an asset.

              - VendorNumber: Unsigned integer representing the vendor number of an asset.

              - AssetName: String representing the asset name.

              - FirmwareVersion: String representing the firmware version of an asset.

              - HardwareVersion: String representing the hardware version of an asset.

              - BusType: String enumeration representing the bus type of an asset. Possible values are: BUILT_IN_SYSTEM, PCI_PXI, USB, GPIB, VXI, SERIAL, TCP_IP, CRIO, SCXI, CDAQ, SWITCH_BLOCK, SCC, FIRE_WIRE, ACCESSORY, CAN, SWITCH_BLOCK_DEVICE, SLSC.

              - IsNIAsset: Boolean flag specifying whether the asset is an NI asset or a third-party asset.

              - Keywords: Collection of string values representing asset metadata keywords. Example: 'Keywords=["keyword1", "keyword2"]'.

              - Properties: Collection of key-value pairs, each key-value pair representing an asset metadata property. Example: 'Properties=["key1":"value1", "key2":"value2"]'.

              - Location.MinionId: String representing the identifier of the minion in which the asset is located in.

              - Location.SystemName: String representing the name of the system that the asset is located in.

              - Location.SlotNumber: Unsigned integer representing the slot number the asset is located in.

              - Location.AssetState.SystemConnection: String enumeration representing the connection state of the system the asset is currently located in. Possible values are: APPROVED, DISCONNECTED, CONNECTED_UPDATE_PENDING, CONNECTED_UPDATE_SUCCESSFUL, CONNECTED_UPDATE_FAILED, UNSUPPORTED, ACTIVATED.

              - Location.AssetState.AssetPresence: String enumeration representing the present status of an asset in a system. Possible values are: INITIALIZING, UNKNOWN, NOT_PRESENT, PRESENT.

              - SupportsSelfCalibration: Boolean flag specifying whether the asset supports self-calibration.

              - SelfCalibration.CalibrationDate: ISO-8601 formatted timestamp string specifying the last date the asset was self-calibrated. Example: "2018-05-20T00:00:00Z"

              - SupportsExternalCalibration: Boolean flag specifying whether the asset supports external calibration.

              - CustomCalibrationInterval: Integer representing the custom calibration interval, in months.
              
              - CalibrationStatus: String enumeration representing the calibration status of an asset. Possible values are: OK, APPROACHING_RECOMMENDED_DUE_DATE, PAST_RECOMMENDED_DUE_DATE.

              - ExternalCalibration.CalibrationDate: ISO-8601 formatted timestamp string specifying the last date the asset was externally-calibrated. Example: "2018-05-20T00:00:00Z"

              - ExternalCalibration.NextRecommendedDate: ISO-8601 formatted timestamp string specifying the recommended date for the next external calibration. Example: "2018-05-20T00:00:00Z"

              - ExternalCalibration.RecommendedInterval: Integer representing the manufacturer-recommended calibration interval, in months.

              - ExternalCalibration.Comments: String representing any external calibration comments.

              - ExternalCalibration.IsLimited: Boolean flag specifying whether the last external calibration was a limited calibration.

              - ExternalCalibration.Operator.DisplayName: String representing the name of the operator which performed an external calibration on a third-party asset.
          type: string
          example: IsSystemController = true
        continuationToken:
          description: >-
            A token which allows the user to resume a query at the next item in
            the matching asset utilization history set. When querying for asset utilization history, a token will
            be returned if a query may be continued. To obtain the next page of
            asset utilization history records, pass the token to the service on a subsequent request.

          type: string
          example: token
        take:
          description: The maximum number of asset utilization history records to return.
          type: integer
          format: int32
          default: 1000
          minimum: 0
          example: 1000
        orderBy:
          $ref: '#/definitions/UtilizationHistoryField'
        orderByDescending:
          description: Whether to return the asset utilization history records in descending order.
          type: boolean
          default: false
          example: false
  StartUtilizationRequest:
    in: body
    name: utilizationBody
    description: Request body specifying utilization start information for multiple assets.
    schema:
      title: Start Utilization Request
      description: Object containing utilization unique identifier, the asset identifiers of the utilized assets and the details of the utilization type, such as category, task name and utilization start timestamp.
      type: object
      required:
        - utilizationIdentifier
        - minionId
        - assetIdentifications
        - utilizationCategory
        - utilizationTimestamp
      properties:
        utilizationIdentifier:
          description: String representing the unique identifier of an asset utilization history record.
          type: string
          example: "2916201B245D642430"
        minionId:
          description: Identifier of the minion where the utilized assets are located.
          type: string
          example: NI_PXIe-8135_Embedded_Controller--MAC-00-80-2F-23-52-65
        assetIdentifications:
          description: Array of the identification information for the assets which are utilized.
          type: array
          items:
            $ref: '#/definitions/AssetIdentificationModel'
        utilizationCategory: 
          description: String representing the utilization category.
          type: string
          example: Test
        taskName:
          description: String representing the name of the task.
          type: string
          example: DUTTestingRoutine
        userName:
          description: String representing the name of the operator who utilized the asset.
          type: string
          example: johnDoe
        utilizationTimestamp:
          description: >-
            A date time value which can be used to specify the start of an utilization.

            This parameter must have the "ISO 8601" format in order to be considered valid.
          type: string
          format: date-time
          example: '2019-05-01T00:00:00.519Z'
  EndUtilizationRequest:
    in: body
    name: utilizationBody
    description: Request body consisting of data specifying the utilization end event for an asset.
    schema:
      $ref: '#/definitions/UtilizationIdentifiersWithTimestampModel'
  HeartbeatUtilizationRequest:
    in: body
    name: utilizationBody
    description: Request body consisting of data specifying the utilization heartbeat event for multiple ongoing utilizations.
    schema:
      $ref: '#/definitions/UtilizationIdentifiersWithTimestampModel'
responses:
  Error:
    description: Error
    schema:
      title: Error Response
      description: Error Response.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
  BadRequest:
    description: Bad Request indicates that the server was unable to process the request because of invalid syntax.
    schema:
      title: Bad Request Error Response
      description: Bad request error response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
  NotFound:
    description: The requested resource was not found.
    schema:
      title: Not Found Request Error Response
      description: Not found error response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
      example:
        error:
          name: AssetPerformanceManagement.NonExistingAssetWithIdentifier
          code: -253426
          message: >-
            No asset found with the specified identifier: 29162;01B245D6;4243;0.
          args: [29162;01B245D6;4243;0]
          innerErrors: []
  Unauthorized:
    description: Not authorized
    headers:
      WWW_Authenticate:
        description: Information for how to authenticate
        type: string
  AssetsResponse:
    description: Assets Response containing the assets satisfying the query and the total count of matching assets.
    schema:
      title: Assets Response
      description: Assets Response containing the assets satisfying the query and the total count of matching assets.
      type: object
      required:
        - assets
        - totalCount
      properties:
        assets:
          description: Array of assets
          type: array
          items:
            $ref: '#/definitions/AssetModel'
        totalCount:
            description: The total number of Assets which match the query.
            type: integer
            example: 1
  AssetDetailsResponse:
    description: Asset details response containing a single asset with the requested identifier.
    schema:
      $ref: '#/definitions/AssetModel'
  AssetSummaryResponse:
    description: Asset summary response containing the count of active assets, inactive assets and the total number of assets.
    schema:
      title: Asset Summary Response
      description: Response containing the total number of assets, the number of assets which are active (present in a connected system), and the number of assets which are not active. Also returns the number of assets that are in use and the number of assets that are not in use.
      type: object
      properties:
        active:
          description: Number of assets which are active, i.e. present in a connected system.
          type: integer
          example: 12
        notActive:
          description: Number of assets which are not active.
          type: integer
          example: 5
        total:
          description: Total number of managed assets.
          type: integer
          example: 17
        inUse:
          description: Total number of used assets.
          type: integer
          example: 10
        notInUse:
          description: Total number of unused assets.
          type: integer
          example: 7
        withAlarms:
          description: Total number of assets with associated alarms.
          type: integer
          example: 3
        approachingRecommendedDueDate:
          description: Number of assets approaching calibration date.
          type: integer
          example: 3
        pastRecommendedDueDate:
          description: Number of assets past their calibration date.
          type: integer
          example: 4
        totalCalibrated:
          description: Total number of assets supporting calibration.
          type: integer
          example: 7
  DeleteAssetsResponse:
    description: Delete Assets Response containing the IDs of the assets which were deleted, the IDs of the assets which failed to be deleted and any errors encountered.
    schema:
      title: Delete Assets Response
      description: Delete Assets Response containing the IDs of the assets which were deleted, the IDs of the assets which failed to be deleted and any errors encountered.
      type: object
      required:
        - ids
      properties:
        ids:
          description: Array of asset identifiers which were deleted
          type: array
          items:
            type: string
            example: "29162;01B245D6;4243;0"
        failed:
          description: Array of asset identifiers that failed to delete
          type: array
          items:
            type: string
            example: "13562;01B245D6;4243;0"
        error:
          $ref: '#/definitions/Error'
  AvailabilityInSystemResponse:
    description: >-
      Returns asset availability information in the specified timespan split based on the specified timespan granularity.
      The response contains a collection of systems that an asset has been present during the timespan, along with the percentage of time the asset was present in the system in each timespan.
    schema:
      title: Asset Availability
      description: The response contains a collection of systems that an asset has been present during the timespan, along with the percentage of time the asset was present in the system in each timespan.
      type: array
      items:
        title: Availability in System Model
        type: object
        properties:
          systemName:
            description: Hostname of the system in which the asset was located.
            type: string
            example: APM-PXI1
          availabilityData:
            description: Collection of asset availability data consisting of timespans and percentage of time the asset was available in each timespan.
            type: array
            items:
              $ref: '#/definitions/OverallAvailabilityInSystemModel'
  CalibratedAssetSummaryResponse:
    description: Response containing summary of assets supporting calibration. Contains the count of assets approaching recommended calibration due date, assets past recommended calibration due date and count of assets supporting (any type of) calibration.
    schema:
      title: Calibrated Asset Summary Response
      description: Asset summary of the total number of assets supporting calibration, the number of assets approaching recommended calibration date and the number of assets past their recommended calibration date.
      type: object
      properties:
        approachingRecommendedDueDate:
          description: Number of assets approaching calibration date.
          type: integer
          example: 12
        pastRecommendedDueDate:
          description: Number of assets past their calibration date.
          type: integer
          example: 5
        total:
          description: Total number of assets supporting calibration.
          type: integer
          example: 17
  CalibrationHistoryResponse:
    description: Calibration history response for a single asset with the requested identifier.
    schema:
      title: Calibration History Response
      description: Calibration history response containing all calibration history entries for the requested asset.
      type: object
      required:
        - calibrationHistory
        - totalCount
      properties:
        calibrationHistory:
          description: Array of calibration history entries
          type: array
          items:
            $ref: '#/definitions/CalibrationHistoryModel'
        totalCount:
          description: The total number of calibration history entries for the requested asset.
          type: integer
          example: 1
  DeleteCalibrationsPartialSuccessResponse:
    description: Delete Calibrations Partial Success Response
    schema:
      description: Delete Calibrations Partial Success Response
      title: DeleteCalibrationsPartialSuccessResponse
      type: object
      required:
        - calibrationIds
      properties:
        calibrationIds:
          description: Array of calibration entry identifiers that were deleted
          type: array
          items:
            type: string
            example: "5c4f0834174ae321b8a95a03"
        failed:
          description: Array of calibration entry identifiers that failed to delete
          type: array
          items:
            type: string
            example: "5c4f0834174ae321b8a95a03"
        error:
          $ref: '#/definitions/Error'
  CreateAssetsPartialSuccessResponse:
    description: Create Assets Partial Success Response
    schema:
      title: CreateAssetsPartialSuccessResponse
      description: Create Assets Partial Success Response
      type: object
      properties:
        assets:
          description: Array of created assets
          type: array
          items:
            $ref: '#/definitions/AssetModel'
        failed:
          description: Array of assets create requests that failed
          type: array
          items:
            $ref: '#/definitions/AssetCreateModel'
        error:
          $ref: '#/definitions/Error'
  SendToFileIngestionOrDownloadResponse:
    description: Response for the query operation that consists either in the file information for when the result was sent to the file ingestion service or the report file content for download. In the latter case, the name of the file is provided in the header of the response with key='Filename'.
    schema:
      title: Send to File Ingestion Or Download Response
      description: Response for the query that consists in the file information for when the result was sent to the file ingestion service or the CSV file content for download.
      type: object
      required:
        - fileId
      properties:
        fileId:
          description: File identifier in the file ingestion service
          type: string
          example: "5c6be9dc174ae3305ca4e7e1"
  ServicePolicyResponse:
    description: Service policy response containing the service calibration policy with the number of days for an asset to be considered as approaching calibration.
    schema:
      $ref: '#/definitions/ServicePolicyModel'
  UpdateAssetsPartialSuccessResponse:
    description: Update Assets Partial Success Response
    schema:
      title: UpdateAssetsPartialSuccessResponse
      description: Update Assets Partial Success Response
      type: object
      properties:
        assets:
          description: Array of updated assets
          type: array
          items:
            $ref: '#/definitions/AssetModel'
        failed:
          description: Array of assets update requests that failed
          type: array
          items:
            $ref: '#/definitions/AssetUpdateModel'
        error:
          $ref: '#/definitions/Error'
  UpdateAssetMetadataPartialSuccessResponse:
    description: Update Asset Metadata Partial Success Response
    schema:
      description: Update Asset Metadata Partial Success Response
      title: UpdateAssetMetadataPartialSuccessResponse
      type: object
      required:
        - succeeded
      properties:
        succeeded:
          $ref: '#/definitions/AssetMetadata'
        failed:
          $ref: '#/definitions/AssetMetadata'
        error:
          $ref: '#/definitions/Error'
      example:
        succeeded:
          keywords: [ Keyword1 ]
          properties:
            Key1: Value1
        failed:
          keywords: [ BadKeyword1 ]
          properties:
            BadKey1: BadValue1
        error:
          name: Skyline.OneOrMoreErrorsOccurred
          code: -251040
          message: >-
            One or more errors occurred. See the contained list for details of each
            error.
          args: []
          innerErrors:
            - name: AssetPerformanceManagement.InvalidKeywordInUpdateMetadataRequest
              code: -253435
              resourceType: Asset
              resourceId: BadKeyword1
              message: 'Invalid keyword value: BadKeyword1.'
              args: [BadKeyword1]
  LinkFilesPartialSuccessResponse:
    description: Link Files Partial Success Response
    schema:
      description: Link Files Partial Success Response
      title: LinkFilesPartialSuccessResponse
      type: object
      required:
        - succeeded
      properties:
        succeeded:
          description: File IDs that are valid.
          type: array
          items:
            type: string
            example: 607fffe41e4564dda3593eb0
        failed:
          description: File IDs that are not valid.
          type: array
          items:
            type: string
            example: invalid
        error:
          $ref: '#/definitions/Error'
      example:
        succeeded: [ 607fffe41e4564dda3593eb0 ]
        failed: [ invalidId ]
        error:
          name: Skyline.OneOrMoreErrorsOccurred
          code: -251040
          message: >-
            One or more errors occurred. See the contained list for details of each
            error.
          args: []
          innerErrors:
            - name: AssetPerformanceManagement.InvalidFileId
              code: -254806
              resourceType: Asset
              resourceId: invalidId
              message: 'The operation failed because an invalid file id was given: invalidId.'
              args: [invalidId]
  UtilizationWithPercentageResponse:
    description: Utilization response containing the collection of utilizations matching the provided filters, in a specific time interval. Besides a time interval, each element contains an asset identifier, a minion id, an utilization category, and a percentage of time that the asset was utilized in the time interval.
    schema:
      title: Utilization with Percentage Response
      description: Response for the utilization query containing the collection of utilizations. Besides a time interval, each element contains an asset identifier, a minion id, an utilization category, and a percentage of time that the asset was utilized in the time interval.
      type: array
      items:
          title: Utilization with Percentage Model
          type: object
          required:
            - startTimestamp
            - endTimestamp
            - assetIdentifier
            - percentage
          properties:
            startTimestamp:
              description: >-
                A date time value representing the beginning of an asset utilization interval.

                This parameter has the "ISO 8601" format in order to be considered valid.
              type: string
              format: date-time
              example: '2019-05-01T00:00:00.519Z'
            endTimestamp:
              description: >-
                A date time value representing the end of an asset utilization interval.

                This parameter has the "ISO 8601" format in order to be considered valid.
              type: string
              format: date-time
              example: '2019-05-20T00:00:00Z'
            assetIdentifier:
              description: String representing the unique identifier of an asset.
              type: string
              example: "29162;01B245D6;4243;0"
            assetName:
              description: String representing the name of an asset.
              type: string
              example: PCISlot2
            minionId:
              description: Identifier of the minion where the asset is located.
              type: string
              example: NI_PXIe-8135_Embedded_Controller--MAC-00-80-2F-23-52-65
            category:
              description: String representing the utilization task category.
              type: string
              example: Test
            percentage:
              description: Percentage of time that the asset was utilized in the specified time interval.
              type: number
              format: double
              example: 7.38958
  SystemUtilizationWithPercentageResponse:
    description: Utilization response containing the collection of utilizations matching the provided filters, in a specific time interval. Besides a time interval, each element contains an asset identifier, a minion id, an utilization category, and a percentage of time that the system was utilized in the time interval.
    schema:
      title: System Utilization with Percentage Response
      description: Response for the utilization query containing the collection of utilizations. Besides a time interval, each element contains an asset identifier, a minion id, an utilization category, and a percentage of time that the system was utilized in the time interval.
      type: array
      items:
          title: System Utilization with Percentage Model
          type: object
          required:
            - startTimestamp
            - endTimestamp
            - minionId
            - percentage
          properties:
            startTimestamp:
              description: >-
                A date time value representing the beginning of a system utilization interval.

                This parameter has the "ISO 8601" format in order to be considered valid.
              type: string
              format: date-time
              example: '2019-05-01T00:00:00.519Z'
            endTimestamp:
              description: >-
                A date time value representing the end of a system utilization interval.

                This parameter has the "ISO 8601" format in order to be considered valid.
              type: string
              format: date-time
              example: '2019-05-20T00:00:00Z'
            minionId:
              description: String representing the unique identifier of a system.
              type: string
              example: NI_PXIe-8135_Embedded_Controller--MAC-00-80-2F-23-52-65
            systemName:
              description: String representing the alias of a system.
              type: string
              example: PXIe Alias
            category:
              description: String representing the utilization task category.
              type: string
              example: Test
            percentage:
              description: Percentage of time that the system was utilized in the specified time interval.
              type: number
              format: double
              example: 7.38958
  QueryUtilizationHistoryResponse:
    description: Asset Utilization History response containing the collection of utilizations records matching the provided filters.
    schema:
      title: Asset Utilization History Response
      description: Response for the asset utilization history query containing the collection of utilizations as well as a continuation token and a total count.
      required:
       - assetUtilizations
      type: object
      properties:
        assetUtilizations:
          description: Array of asset utilizations
          type: array
          items:
              type: object
              required:
                - utilizationIdentifier
                - assetIdentifier
                - minionId
                - category
                - startTimestamp
              properties:
                utilizationIdentifier:
                  description: String representing the unique identifier of an asset utilization history record.
                  type: string
                  example: "2916201B245D642430"
                assetIdentifier:
                  description: String representing the unique identifier of an asset.
                  type: string
                  example: "29162;01B245D6;4243;0"
                minionId:
                  description: Identifier of the minion where the asset is located.
                  type: string
                  example: NI_PXIe-8135_Embedded_Controller--MAC-00-80-2F-23-52-65
                category:
                  description: String representing the utilization task category.
                  type: string
                  example: Test
                taskName:
                  description: String representing the name of the task.
                  type: string
                  example: DUTTestingRoutine
                userName:
                  description: String representing the name of the operator who utilized the asset.
                  type: string
                  example: johnDoe
                startTimestamp:
                  description: >-
                    A date time value which can be used to specify the start of an utilization.

                    This parameter has the "ISO 8601" format in order to be considered valid.
                  type: string
                  format: date-time
                  example: '2019-05-01T00:00:00.519Z'
                endTimestamp:
                  description: >-
                    A date time value which can be used to specify the end of an utilization.

                    This parameter has the "ISO 8601" format in order to be considered valid.
                  type: string
                  format: date-time
                  example: '2019-05-20T00:00:00Z'
                heartbeatTimestamp:
                  description: >-
                    A date time value which can be used to specify the heartbeat of an utilization.

                    This parameter has the "ISO 8601" format in order to be considered valid.
                  type: string
                  format: date-time
                  example: '2019-05-20T00:00:00Z'
        continuationToken:
          description: >-
            A token which allows the user to resume a query at the next item in
            the matching asset utilization history set. When querying for asset utilization history, a token will
            be returned if a query may be continued. To obtain the next page of
            asset utilization history records, pass the token to the service on a subsequent request.

          type: string
          example: token
  UpdateUtilizationPartialSuccessResponse:
    description: Update utilization partial success response. The update operation can be either a heartbeat update or a utilization end.
    schema:
      description: Update utilization partial success response.
      title: UpdateUtilizationPartialSuccessResponse
      type: object
      required:
        - updatedUtilizationIds
      properties:
        updatedUtilizationIds:
          description: Array of utilization identifiers for the entries that were updated.
          type: array
          items:
            type: string
            example: "5c4f0834174ae321b8a95a03"
        failed:
          description: Array of utilization identifiers for the entries that failed to update.
          type: array
          items:
            type: string
            example: "5c4f0834174ae321b8a95a04"
        error:
          $ref: '#/definitions/Error'
  StartUtilizationPartialSuccessResponse:
    description: Start utilization partial success response.
    schema:
      description: Start utilization partial success response.
      title: StartUtilizationPartialSuccessResponse
      type: object
      required:
        - assetsWithStartedUtilization
      properties:
        assetsWithStartedUtilization:
          description: Array containing the asset identification data for the assets that started being utilized.
          type: array
          items:
            $ref: '#/definitions/AssetIdentificationModel'
        failed:
          description: Array containing the asset identification data for the assets that failed to start being utilized.
          type: array
          items:
            $ref: '#/definitions/AssetIdentificationModel'
        error:
          $ref: '#/definitions/Error'
paths:
  /:
    get:
      tags: [versioning]
      summary: API information
      description: Returns information about API versions and available operations.
      operationId: RootEndpoint
      # Explicitly mark security as an empty array - this route does not require any privileges.
      # Marking it this way prevents it from inheriting the top-level security settings.
      security: []
      responses:
        200:
          description: OK
          schema:
            title: Root Endpoint Response
            description: Version Information.
            type: object
            properties:
              v1:
                $ref: '#/definitions/V1Operations'
              version:
                description: Implementation version of the web service.
                type: string
        default:
          $ref: '#/responses/Error'
  /v1:
    get:
      tags: [versioning]
      summary: API version information
      description: Returns available operations for a single version of the API.
      operationId: RootEndpointWithVersion
      security: []
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/V1Operations'
        default:
          $ref: '#/responses/Error'
  /v1/assets:
    get:
      tags: [assets]
      summary: Gets assets
      description: >-
        Gets a list of assets. Calibrated assets can be obtained by setting calibratableOnly=true. To obtain a report of the assets, responseFormat=csv&destination=download should be sent as query parameters.


        Currently, the valid combinations of ResponseFormat and Destination are [JSON;INLINE], [CSV;DOWNLOAD], [CSV;FILE_SERVICE].
      operationId: get-assets
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/Skip'
        - $ref: '#/parameters/Take'
        - in: query
          name: calibratableOnly
          description: Whether to filter only assets which support calibration.
          type: boolean
        - in: query
          name: responseFormat
          description: The return type. Valid options are "JSON" and "CSV".
          type: string
          enum:
            - JSON
            - CSV
        - in: query
          name: destination
          description:
            The destination of the request.
            "INLINE" (default) returns the list of assets as the body of the response.
            "DOWNLOAD" returns the list of assets as the body of the response and indicates to the client that it should be downloaded as a file.
            "FILE_SERVICE" sends the list of assets to the file ingestion service and returns the ID of the file to the client in a JSON object.
          type: string
          enum:
            - INLINE
            - DOWNLOAD
            - FILE_SERVICE
        - in: query
          name: fileIngestionWorkspace
          description: The ID of the workspace to put the file into, if the destination is "FILE_SERVICE".
          type: string
          x-example: '5bc5e9092a4fa4c71cfa7197'
      responses:
        200:
          $ref: '#/responses/AssetsResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      tags: [assets]
      summary: Creates assets
      description: >-
        Creates new assets with the provided information. 
        
        
        If an asset with the provided identification does not exist on the server, a new asset is created. If an asset with the provided identification already exists on the server, no create or update operation will be performed for the respective identification and the final response will contain an error message describing the actual reason.
        
        
        If the selfCalibration property is set, the supportsSelfCalibration property is automatically set to true by the service no matter if it is specified as false. The same is true for the externalCalibration and supportsExternalCalibration properties.
      operationId: create-assets
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/CreateAssetsRequestBody'
      responses:
        200:
          $ref: '#/responses/CreateAssetsPartialSuccessResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/update-assets:
    post:
      tags: [assets]
      summary: Updates multiple assets
      description: >-
        Updates multiple assets. To identify the assets that need to be updated, the following properties must be provided:

        - id

        OR

        - asset identification properties. See AssetIdentificationModel for details.
        
        If an asset with the provided identification does not exist, that asset is not created and an error is returned instead.
        Any property that is not set or set to null is ignored.

        The properties that cannot be updated are:

        - busType

        - modelName

        - modelNumber

        - vendorName

        - vendorNumber

        - serialNumber

        - id


        If the selfCalibration property is set, the supportsSelfCalibration property is automatically set to true by the service, no matter if it is specified as false. The same is true for the externalCalibration and supportsExternalCalibration properties.


        Updating the assetPresence property to NOT_PRESENT succeeds only if it is updated with the same minionId, parent and slotNumber. Updating it to PRESENT always succeeds.
      operationId: update-assets
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/UpdateAssetsRequestBody'
      responses:
        200:
          $ref: '#/responses/UpdateAssetsPartialSuccessResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/asset-summary:
    get:
      tags: [assets]
      summary: Gets a summary of assets
      description: Gets asset summary response containing the total number of assets, the number of assets which are active, i.e. present in a connected system, and the number of assets which are not active.
      operationId: get-asset-summary
      x-ni-auth: true
      responses:
          200:
            $ref: '#/responses/AssetSummaryResponse'
          401:
            $ref: '#/responses/Unauthorized'
          default:
            $ref: '#/responses/Error'
  /v1/calibratable-asset-summary:
    get:
      tags: [assets]
      summary: Gets a summary of assets supporting calibration
      description: Gets asset summary of the total number of assets supporting calibration, the number of assets approaching calibration date and the number of assets past their calibration date
      operationId: get-calibratable-asset-summary
      x-ni-auth: true
      responses:
          200:
            $ref: '#/responses/CalibratedAssetSummaryResponse'
          401:
            $ref: '#/responses/Unauthorized'
          default:
            $ref: '#/responses/Error'
  /v1/query-assets:
    post:
      tags: [assets]
      summary: Query assets
      description: Returns the assets satisfying the provided filtering criteria. If the the caller requests a JSON inline response, the returned assets are filtered based on the filter string and the IDs and calibratableOnly properties are not taken into consideration. When the caller requests a CSV response, the IDs property has higher precedence than the filter string when used to filter the assets from the response.
      operationId: query-assets
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/QueryAssetsRequest'
      responses:
        200:
          $ref: '#/responses/AssetsResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/query-in-use-assets:
    post:
      tags: [assets]
      summary: Query assets that are currently in use
      description: Returns the assets that are currently marked as being in use by a utilization entry and that satisfy the provided filtering criteria. The caller can filter based on asset properties as well as utilization properties.
      operationId: query-in-use-assets
      x-ni-auth: true
      parameters: 
        - $ref: '#/parameters/QueryInUseAssetsRequest'
      responses:
        200:
          $ref: '#/responses/AssetsResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/assets/{assetId}:
    get:
      tags: [assets]
      summary: Gets asset with identifier
      description: Gets the asset which has the given identifier.
      operationId: get-asset-with-identifier
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/AssetId'
      responses:
        200:
          $ref: '#/responses/AssetDetailsResponse'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/assets/{assetId}/history/availability:
    get:
      tags: [assets]
      summary: Retrieves asset availability history
      description: Returns availability information for an asset in the specified timespan and split based on the specified time granularity.
      operationId: get-asset-availability-history
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/AssetId'
        - in: query
          name: startDate
          required: true
          description: >-
            A date value which can be used to specify the beginning of a timespan. 
            
            This parameter is required to have the "ISO 8601" format in order to be considered valid. 
            
            The time component of the request is ignored.
          type: string
          x-example: '2018-05-01T00:00:00.000Z'
        - in: query
          name: endDate
          required: true
          description: >- 
            A date value which can be used to specify the end of a timespan.
            
            This parameter is required to have the "ISO 8601" format in order to be considered valid. 
            
            The time component of the request is ignored.
          type: string
          x-example: '2018-05-20T00:00:00Z'
        - $ref: '#/parameters/TimespanGranularity'
      responses:
        200:
          $ref: '#/responses/AvailabilityInSystemResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/assets/{assetId}/history/calibration:
    get:
      tags: [assets]
      summary: Retrieves asset calibration history
      description: Returns the calibration history of the asset which has the given identifier.
      operationId: get-asset-calibration-history
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/AssetId'
        - $ref: '#/parameters/Skip'
        - $ref: '#/parameters/Take'
      responses:
        200:
          $ref: '#/responses/CalibrationHistoryResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
    post:
      tags: [deprecated]
      summary: Creates a new calibration history entry for an asset
      description: Deprecated. Creates a new calibration history entry for an asset. Use /v1/update-assets.
      operationId: post-asset-calibration-history
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER, USER_NAME]
      deprecated: true
      parameters:
        - $ref: '#/parameters/AssetId'
        - $ref: '#/parameters/ExternalCalibrationRequestBody'
      responses:
        201:
          description: Created
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/assets/{assetId}/history/delete-calibrations:
    post:
      tags: [assets]
      summary: Deletes calibration history entries
      description: Deletes multiple calibration history entries for an asset.
      operationId: post-delete-asset-calibration-history
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/AssetId'
        - $ref: '#/parameters/DeleteCalibrationsRequestBody'
      responses:
        200:
          $ref: '#/responses/DeleteCalibrationsPartialSuccessResponse'
        204:
          description: No Content
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/assets/{assetId}/history/query-calibration:
    post:
      tags: [assets]
      summary: Queries asset calibration history
      description: Computes the calibration history of an asset in CSV format. If the destination is download, the response will contain the calibration history file content. If the destination is file ingestion service, the CSV file is sent to the file storing service and an object containing the file identifier is returned. Any other format and destination combinations are not supported yet.
      operationId: post-asset-query-calibration-history
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/AssetId'
        - $ref: '#/parameters/QueryHistoryRequestBody'
      responses:
        200:
          $ref: '#/responses/SendToFileIngestionOrDownloadResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        500:
          description: Internal server error. Possible while sending the file to the FileIngestion service because the service is not running; there is not enough space on disk to store the file; or there are network issues.
        default:
          $ref: '#/responses/Error'
  /v1/assets/{assetId}/history/query-location:
    post:
      tags: [assets]
      summary: Queries asset location history
      description: Computes the location history of an asset in CSV format. If the destination is download, the response will contain the location history file content. If the destination is file ingestion service, the CSV file is sent to the file storing service and an object containing the file identifier is returned. Any other format and destination combinations are not supported yet.
      operationId: post-asset-query-location-history
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/AssetId'
        - $ref: '#/parameters/QueryHistoryRequestBody'
      responses:
        200:
          $ref: '#/responses/SendToFileIngestionOrDownloadResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        500:
          description: Internal server error. Possible while sending the file to the FileIngestion service, because the service is not running or there is not enough space on disk to store the file or the file could not be sent due to networking issues.
        default:
          $ref: '#/responses/Error'
  /v1/assets/{assetId}/metadata:
    patch:
      tags: [assets]
      summary: Updates asset metadata
      description: Performs a request to update the metadata information of an asset.
      operationId: update-asset-metadata
      x-ni-auth: true
      consumes:
        - application/merge-patch+json
      parameters:
        - $ref: '#/parameters/AssetId'
        - $ref: '#/parameters/UpdateMetadata'
      responses:
        200:
          $ref: '#/responses/UpdateAssetMetadataPartialSuccessResponse'
        204:
          description: No Content
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/assets/{assetId}/file:
    post:
      tags: [assets]
      summary: Link files
      description: Performs a request to link files to an asset.
      operationId: link-files
      x-ni-auth: true
      consumes:
        - application/merge-patch+json
      parameters:
        - $ref: '#/parameters/AssetId'
        - $ref: '#/parameters/LinkFiles'
      responses:
        200:
          $ref: '#/responses/LinkFilesPartialSuccessResponse'
        204:
          description: No Content
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/assets/{assetId}/files/{fileId}:
    delete:
      tags: [assets]
      summary: Unlink files
      description: Performs a request to unlink a file from an asset.
      operationId: unlink-files
      x-ni-auth: true
      consumes:
        - application/merge-patch+json
      parameters:
        - $ref: '#/parameters/AssetId'
        - $ref: '#/parameters/FileId'
      responses:
        204:
          description: No Content
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/assets/start-utilization:
    post:
      tags: [utilization]
      summary: Stores assets utilization start
      description: >- 
          Stores information related to assets utilization start. The operation is successful when utilization information can be stored for all asset identifiers provided in the request.
          It will return a partial success when storing the utilization start information failed for one or more assets.
      operationId: start-multiple-asset-utilization
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/StartUtilizationRequest'
      responses:
        200:
          $ref: '#/responses/StartUtilizationPartialSuccessResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/assets/end-utilization:
    post:
      tags: [utilization]
      summary: Stores assets utilization end
      description: >-
          Stores information related to assets utilization end. The operation is successful and will return No Content when end utilization information can be stored for all utilization identifiers provided in the request.
          It will return a partial success when end utilization information can be stored for only a subset of the utilization identifiers provided in the request.
          It will return a not found response when no stored utilizations matched the provided utilization identifiers.
      operationId: end-multiple-asset-utilization
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/EndUtilizationRequest'
      responses:
        200:
          $ref: '#/responses/UpdateUtilizationPartialSuccessResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/assets/utilization-heartbeat:
    post:
      tags: [utilization]
      summary: Stores asset utilization heartbeats
      description: >-
          Stores information related to ongoing asset utilizations. The operation is successful and will return No Content when utilization heartbeat information can be stored for all utilization identifiers provided in the request.
          It will return a partial success when utilization heartbeat information can be stored for only a subset of the utilization identifiers provided in the request.
          It will return a not found response when no stored utilizations matched the provided utilization identifiers.
      operationId: asset-utilization-multiple-heartbeats
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/HeartbeatUtilizationRequest'
      responses:
        200:
          $ref: '#/responses/UpdateUtilizationPartialSuccessResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/compare-assets-availability:
    post:
      tags: [assets]
      summary: Gets availability history for multiple assets.
      description: Gets availability history for multiple assets based on a specified timespan.
      operationId: compare-asset-availability
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/AssetAvailabilityComparison'
      responses:
        200:
          description: Asset availability comparison response containing availability history for requested assets based on the requested timespan.
          schema:
            title: Asset Availability Comparison Response
            description: Asset availability comparison response containing availability history for the requested assets. If availability history could not be resolved for some assets, the response contains error information on the assets which could not be resolved.
            type: object
            properties:
              availabilityComparisons:
                type: array
                items:
                  $ref: '#/definitions/AssetWithAvailabilityHistoryModel'
              failed:
                description: Array of asset identifiers for which obtaining availability failed
                type: array
                items:
                  type: string
                  example: [ "13562;01B245D6;4243;0" ]
              error:
                $ref: '#/definitions/Error'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/assets/history/query-assets-availability:
    post:
      tags: [assets]
      summary: Gets availability history for multiple assets.
      description: Gets availability history for multiple assets based on the specified timespans.
      operationId: query-assets-availability
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/QueryAssetsAvailabilityRequestBody'
      responses:
        200:
          description: Query Assets Availability response containing information about the availability of the assets specified by their IDs during the given time intervals.
          schema:
            title: Query Assets Availability Response
            description: Query assets availability response containing availability history for the requested assets. If availability history could not be resolved for some assets, the response contains error information on the assets which could not be resolved.
            type: object
            properties:
              availabilityData:
                type: array
                items:
                  $ref: '#/definitions/AssetWithAvailabilityInIntervalModel'
              failed:
                description: Array of asset identifiers for which obtaining availability failed.
                type: array
                items:
                  type: string
                  example: [ "13562;01B245D6;4243;0" ]
              error:
                $ref: '#/definitions/Error'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/assets/history/report/query-assets-availability:
    post:
      tags: [reports]
      summary: Gets an asset availability history report for multiple assets.
      description: Gets a CSV file report containing asset availability history for multiple assets based on the specified timespans.
      operationId: query-assets-availability-report
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/QueryAssetsAvailabilityReportRequestBody'
      responses:
        200:
          description: A CSV file report containing the asset availability history of the assets specified by their IDs during the given time intervals.
          schema:
            type: file
            example: "Asset Id,Asset Name,Start Date,End Date,System Alias,Availability Percentage\n0030b58e-4e1a-47ea-9e1e-d60ba3341551,PXI3Slot7,2020-11-10 00:00:00Z,2021-01-06 00:00:00Z,NI_PXIe-8133_Embedded_Controller--MAC-00-80-2F-14-2C-06,0.0815299529054917"
          headers:
            X-Not-Found-Resources:
              description: The IDs of the resources that were not found.
              type: array
              items:
                type: string
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/delete-assets:
    post:
      tags: [assets]
      summary: Deletes assets and all information associated with assets.
      description: Deletes all persisted data for the assets with the provided identifiers. This includes asset properties and all related historical information.
      operationId: delete-assets
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/DeleteAssetsRequestBody'
      responses:
        200:
          $ref: '#/responses/DeleteAssetsResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/query-asset-utilization:
    post:
      tags: [utilization]
      summary: Query Asset Utilization
      description: Retrieves asset utilization matching the provided filters.
      operationId: read-asset-utilization
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/QueryAssetUtilizationRequest'
      responses:
        200:
          $ref: '#/responses/UtilizationWithPercentageResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/query-system-utilization:
    post:
      tags: [utilization]
      summary: Query System Utilization
      description: Retrieves system utilization matching the provided filters.
      operationId: read-system-utilization
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/QuerySystemUtilizationRequest'
      responses:
        200:
          $ref: '#/responses/SystemUtilizationWithPercentageResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/query-asset-utilization-history:
    post:
      tags: [utilization]
      summary: Query Asset Utilization Historical Data
      description: Retrieves historical asset utilization data matching the provided filters. An empty request body queries all historical asset utilization data.
      operationId: query-asset-utilizations
      x-ni-auth: true
      parameters:
        - $ref: '#/parameters/QueryAssetUtilizationHistoryRequest'
      responses:
        200:
          $ref: '#/responses/QueryUtilizationHistoryResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/policy:
    get:
      tags: [policy]
      summary: Retrieves the service policy
      description: Retrieves the service policy.
      operationId: get-policy
      x-ni-auth: true
      responses:
        200:
          $ref: '#/responses/ServicePolicyResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    patch:
      tags: [policy]
      summary: Updates the service policy
      description: Performs a request to update the service policy.
      operationId: update-policy
      x-ni-auth: true
      consumes:
        - application/merge-patch+json
      parameters:
        - $ref: '#/parameters/ServicePolicyUpdateRequestBody'
      responses:
        204:
          description: No Content
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=auth/niauth.yaml sha256=6e39670ae37ead9f97120f86d880fb676153064887e21ec4b4712bb02869458f bytes=35293 -->
## FILE: auth/niauth.yaml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `auth/niauth.yaml`
- sha256: `6e39670ae37ead9f97120f86d880fb676153064887e21ec4b4712bb02869458f`
- bytes: 35293

````yaml
swagger: '2.0'
info:
  version: '1.0'
  title: SystemLink Auth Service
  description: Manage authorization policies for a SystemLink server.
  contact:
    name: NI
    url: https://www.ni.com/systemlink
    email: support@ni.com
basePath: /niauth/v1
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
  /auth:
    get:
      tags:
        - auth
      summary: Authenticates API Keys
      description: Authenticates the given x-ni-api-key and returns information about the caller
      operationId: auth
      responses:
        200:
          $ref: '#/responses/AuthResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'

  /keys:
    get:
      tags:
        - keys
      summary: Lists all API Keys
      description: Returns the list of permanent api keys
      operationId: get-keys
      parameters:
        - in: query
          name: name
          description: Filters the keys by name
          type: string
        - in: query
          name: skip
          description: How many keys to skip in the result when paging.
          type: integer
        - in: query
          name: take
          description: How many keys to return in the result
          type: integer
          default: 50
          maximum: 100
        - in: query
          name: sortby
          description: The field name for sorting the results
          type: string
          enum: [name, created, updated]
        - in: query
          name: order
          description: Sort by ascending or descending order
          type: string
          enum: [ascending, descending]
      responses:
        200:
          $ref: '#/responses/GetKeysResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      tags:
        - keys
      summary: Creates a new API Key
      description: Create a permanent API Key
      operationId: create-key
      parameters:
        - $ref: '#/parameters/CreateKeyRequest'
      responses:
        200:
          $ref: '#/responses/CreateKeyResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /keys/{id}:
    get:
      tags:
        - keys
      summary: Gets an API Key by the given Id
      description: Returns the API Key for the given Id
      operationId: get-key
      parameters:
        - $ref: '#/parameters/KeyId'
      responses:
        200:
          $ref: '#/responses/GetKeyResponse'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
    put:
      tags:
        - keys
      summary: Updates an API Key
      description: Updates the API Key with the given Id
      operationId: update-key
      parameters:
        - $ref: '#/parameters/KeyId'
        - $ref: '#/parameters/UpdateKeyRequest'
      responses:
        200:
          $ref: '#/responses/UpdateKeyResponse'
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
        - keys
      summary: Deletes an API Key
      description: Deletes the API Key with the given Id
      operationId: delete-key
      parameters:
        - $ref: '#/parameters/KeyId'
      responses:
        204:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'

  /policies:
    get:
      tags:
        - policies
      summary: Lists all policies
      description: Returns the list of policies
      operationId: get-policies
      parameters:
        - in: query
          name: name
          description: Filters the policies by name
          type: string
        - in: query
          name: type
          description: Filters the policies by type. Can be a comma-separated list of types.
          type: string
        - in: query
          name: builtIn
          description: Filters the policies by the builtIn flag.
          type: boolean
        - in: query
          name: id
          description: Filters the policies by id. Can be a comma-separated list of ids.
          type: string
        - in: query
          name: skip
          description: How many policies to skip in the result when paging.
          type: integer
        - in: query
          name: take
          description: How many policies to return in the result
          type: integer
          default: 50
          maximum: 100
        - in: query
          name: sortby
          description: The field name for sorting the results
          type: string
          enum: [name, created, updated]
        - in: query
          name: order
          description: Sort by ascending or descending order
          type: string
          enum: [ascending, descending]
      responses:
        200:
          $ref: '#/responses/GetPoliciesResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      tags:
        - policies
      summary: Creates a new policy
      description: Creates a new policy
      operationId: create-policy
      parameters:
        - $ref: '#/parameters/CreatePolicyRequest'
      responses:
        200:
          $ref: '#/responses/CreatePolicyResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /policies/{id}:
    get:
      tags:
        - policies
      summary: Gets a policy by the given Id
      description: Returns the policy for the given Id
      operationId: get-policy
      parameters:
        - $ref: '#/parameters/PolicyId'
      responses:
        200:
          $ref: '#/responses/GetPolicyResponse'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
    put:
      tags:
        - policies
      summary: Updates a policy
      description: Updates the policy with the given Id
      operationId: update-policy
      parameters:
        - $ref: '#/parameters/PolicyId'
        - $ref: '#/parameters/UpdatePolicyRequest'
      responses:
        200:
          $ref: '#/responses/UpdatePolicyResponse'
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
        - policies
      summary: Deletes a policy
      description: Deletes the policy with the given Id
      operationId: delete-policy
      parameters:
        - $ref: '#/parameters/PolicyId'
      responses:
        204:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'

  /policy-templates:
    get:
      tags:
        - policy-templates
      summary: Lists all policy-templates
      description: Returns the list of policy-templates
      operationId: get-policy-templates
      parameters:
        - in: query
          name: name
          description: Filters the policy-templates by name
          type: string
        - in: query
          name: type
          description: Filters the policy-templates by type. Can be a comma-separated list of types.
          type: string
        - in: query
          name: builtIn
          description: Filters the policy-templates by the builtIn flag.
          type: boolean
        - in: query
          name: id
          description: Filters the policy-templates by id. Can be a comma-separated list of ids.
          type: string
        - in: query
          name: skip
          description: How many policy-templates to skip in the result when paging.
          type: integer
        - in: query
          name: take
          description: How many policy-templates to return in the result
          type: integer
          default: 50
          maximum: 100
        - in: query
          name: sortby
          description: The field name for sorting the results
          type: string
          enum: [name, created, updated]
        - in: query
          name: order
          description: Sort by ascending or descending order
          type: string
          enum: [ascending, descending]
      responses:
        200:
          $ref: '#/responses/GetPolicyTemplatesResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      tags:
        - policy-templates
      summary: Creates a new policy-template
      description: Creates a new policy-template
      operationId: create-policy-template
      parameters:
        - $ref: '#/parameters/CreatePolicyTemplateRequest'
      responses:
        200:
          $ref: '#/responses/CreatePolicyTemplateResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /policy-templates/{id}:
    get:
      tags:
        - policy-templates
      summary: Gets a policy-template by the given Id
      description: Returns the policy-template for the given Id
      operationId: get-policy-template
      parameters:
        - $ref: '#/parameters/PolicyTemplateId'
      responses:
        200:
          $ref: '#/responses/GetPolicyTemplateResponse'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
    put:
      tags:
        - policy-templates
      summary: Updates a policy-template
      description: Updates the policy-template with the given Id
      operationId: update-policy-template
      parameters:
        - $ref: '#/parameters/PolicyTemplateId'
        - $ref: '#/parameters/UpdatePolicyTemplateRequest'
      responses:
        200:
          $ref: '#/responses/UpdatePolicyTemplateResponse'
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
        - policy-templates
      summary: Deletes a policy-template
      description: Deletes the policy-template with the given Id
      operationId: delete-policy-template
      parameters:
        - $ref: '#/parameters/PolicyTemplateId'
      responses:
        204:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'

  /session-keys:
    post:
      tags:
        - whitelisted operations
      summary: Creates temporary API Keys
      description: Create a temporary session key which is valid for 1 hour. The caller needs a whitelisted API key to issue session keys.
      operationId: create-session-key
      parameters:
        - $ref: '#/parameters/CreateSessionKeyRequest'
      responses:
        200:
          $ref: '#/responses/CreateSessionKeyResponse'
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'

  /user:
    get:
      tags:
        - user
      summary: Authenticates API Keys
      description: Authenticates the given x-ni-api-key and returns information about the caller
      operationId: user
      responses:
        200:
          $ref: '#/responses/UserResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'

definitions:
  AuthStatement:
    type: object
    title: Auth Statement
    description: A statement defines what a user or device is allowed to do
    properties:
      actions:
        type: array
        items:
          type: string
        description: A list of actions the user is allowed to perform
      resource:
        type: array
        items:
          type: string
        description: A list of resources the user is allowed to access
      workspace:
        type: string
        description: The workspace the user is allowed to access
  AuthPolicy:
    type: object
    title: Auth Policy
    description: A policy defines what a user or device is allowed to do
    properties:
      statements:
        type: array
        items:
          $ref: '#/definitions/AuthStatement'
        description: A list of statements defining the actions the user can perform on a resource in a workspace
  PolicyTemplate:
    type: object
    title: Policy Template
    description: A policy template defines what a user or device is allowed to do but is not bound to a workspace. When the template is referenced by a policy, the connection between the actions and the workspace is created.
    properties:
      id:
        type: string
        description: The unique id
      name:
        type: string
        description: The policy template's name
      type:
        type: string
        description: The type of the policy template
      builtIn:
        type: boolean
        description: Whether the policy template is built-in
      userId:
        type: string
        description: The user id
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
      deleted:
        type: boolean
        description: Whether the policy is deleted or not
      properties:
        type: object
        description: A map of key value properties
        additionalProperties:
          type: string
        example:
          key1: value1
      statements:
        type: array
        items:
          $ref: '#/definitions/Statement'
        description: A list of statements defining the actions the user can perform on a resource
  Statement:
    type: object
    title: Statement
    description: A statement defines what a user or device is allowed to do
    properties:
      actions:
        type: array
        items:
          type: string
        description: A list of actions the user is allowed to perform
      resource:
        type: array
        items:
          type: string
        description: A list of resources the user is allowed to access
      workspace:
        type: string
        description: The workspace the user is allowed to access
      description:
        type: string
        description: A description for this statement
  Policy:
    type: object
    title: Policy
    description: A policy defines what a user or device is allowed to do
    properties:
      id:
        type: string
        description: The unique id
      name:
        type: string
        description: The policies's name
      type:
        type: string
        description: The type of the policy
      builtIn:
        type: boolean
        description: Whether the policy is built-in
      userId:
        type: string
        description: The user id
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
      deleted:
        type: boolean
        description: Whether the policy is deleted or not
      properties:
        type: object
        description: A map of key value properties
        additionalProperties:
          type: string
        example:
          key1: value1
      statements:
        type: array
        items:
          $ref: '#/definitions/Statement'
        description: A list of statements defining the actions the user can perform on a resource in a workspace
      templateId:
        type: string
        description: The id of the policy template. Only set if the policy has been created based on a template and does not contain inline statements.
      workspace:
        type: string
        description: The workspace the policy template applies to. Only set if the policy has been created based on a template and does not contain inline statements.
  Key:
    type: object
    title: API Key
    description: The API Key can be used to authenticate a user or device
    properties:
      id:
        type: string
        description: The unique id
      name:
        type: string
        description: The key's name
      userId:
        type: string
        description: The user id
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
      expiry:
        type: string
        format: date-time
        description: The time when the key expires (epoch in milliseconds)
        example: "2019-12-02T15:31:45.379Z"
      enabled:
        type: boolean
        description: Whether the key is enabled or not
      deleted:
        type: boolean
        description: Whether the key is deleted or not
      defaultWorkspace:
        type: string
        description: This field overrides the default workspace when authenticating.
      properties:
        type: object
        description: A map of key value properties
        additionalProperties:
          type: string
        example:
          key1: value1
      policies:
        type: array
        items:
          $ref: '#/definitions/Policy'
        description: A list of policy definitions including statements and permissions
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
        description: A map of key value properties
        additionalProperties:
          type: string
        example:
          key1: value1
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
        description: A list of policy ids to reference existing policies
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
      ownerId:
        type: string
        description: The userId of the organization owner
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

  UserPolicy:
    type: object
    title: User Policy
    description: A policy defines what a user or device is allowed to do
    properties:
      id:
        description: The identifier of a policy
        type: string
      name:
        description: The policy name
        type: string
      templateId:
        description: The identifier of a policy template
        type: string
      workspaceId:
        description: The identifier of a workspace
        type: string

  UserPolicyTemplate:
    type: object
    title: User Policy Template
    description: A policy template defines what a user or device is allowed to do but is not bound to a workspace. When the template is referenced by a policy, the connection between the actions and the workspace is created.
    properties:
      id:
        description: The identifier of a policy template
        type: string
      name:
        description: The policy template name
        type: string

parameters:
  KeyId:
    in: path
    name: id
    description: The identifier of an API Key.
    type: string
    required: true
  PolicyId:
    in: path
    name: id
    description: The identifier of a policy.
    type: string
    required: true
  PolicyTemplateId:
    in: path
    name: id
    description: The identifier of a policy template.
    type: string
    required: true
  CreateSessionKeyRequest:
    in: body
    name: createSessionKey
    description: The request to create session keys
    schema:
      title: Create Session Key Request
      description: Parameters for creating temporary session keys
      type: object
      properties:
        orgId:
          type: string
          description: The org id
        userId:
          type: string
          description: The user id
        policies:
          type: array
          items:
            $ref: '#/definitions/Policy'
          description: A list of policy definitions including statements and permissions
        policyIds:
          type: array
          items:
            type: string
          description: A list of policy ids to reference existing policies
        defaultWorkspace:
          type: string
          description: This field overrides the default workspace when authenticating.
        durationSeconds:
          type: integer
          minimum: 1
          maximum: 86400
          description: The time in seconds how long the temporary key is valid
        properties:
          type: object
          description: A map of key value properties
          additionalProperties:
            type: string
          example:
            key1: value1

  CreateKeyRequest:
    in: body
    name: createKey
    description: The request to create an API Key
    schema:
      title: Create Key Request
      description: Parameters for creating API Keys
      type: object
      properties:
        name:
          type: string
          description: The name
        policyIds:
          type: array
          items:
            type: string
          description: A list of policy ids to reference existing policies
        defaultWorkspace:
          type: string
          description: This field overrides the default workspace when authenticating.
        properties:
          type: object
          description: A map of key value properties
          additionalProperties:
            type: string
          example:
            key1: value1
  UpdateKeyRequest:
    in: body
    name: updateKey
    description: The request to update an existing API Key
    schema:
      title: Update Key Request
      description: Parameters for updating API Keys
      type: object
      properties:
        name:
          type: string
          description: The name
        policyIds:
          type: array
          items:
            type: string
          description: A list of policy ids to reference existing policies
        defaultWorkspace:
          type: string
          description: This field overrides the default workspace when authenticating.
        properties:
          type: object
          description: A map of key value properties
          additionalProperties:
            type: string
          example:
            key1: value1
        enabled:
          type: boolean
          description: Whether the key is enabled or not

  CreatePolicyRequest:
    in: body
    name: createPolicy
    description: The request to create a policy
    schema:
      title: Create Policy Request
      description: Parameters for creating policies
      type: object
      properties:
        name:
          type: string
          description: The name
        type:
          type: string
          enum: [default, internal, custom, role]
          description: The policy type
        statements:
          type: array
          items:
            $ref: '#/definitions/Statement'
          description: A list of statements which define the actions a user or device is allowed to perform
        properties:
          type: object
          description: A map of key value properties
          additionalProperties:
            type: string
          example:
            key1: value1
  UpdatePolicyRequest:
    in: body
    name: updatePolicy
    description: The request to update an existing policy
    schema:
      title: Update Policy Request
      description: Parameters for updating policies
      type: object
      properties:
        name:
          type: string
          description: The name
        type:
          type: string
          enum: [default, internal, custom, role]
          description: The policy type
        statements:
          type: array
          items:
            $ref: '#/definitions/Statement'
          description: A list of statements which define the actions a user or device is allowed to perform
        properties:
          type: object
          description: A map of key value properties
          additionalProperties:
            type: string
          example:
            key1: value1

  CreatePolicyTemplateRequest:
    in: body
    name: createPolicyTemplate
    description: The request to create a policy template
    schema:
      title: Create Policy Template Request
      description: Parameters for creating policies
      type: object
      properties:
        name:
          type: string
          description: The name
        type:
          type: string
          enum: [user, service]
          description: The policy template type
        statements:
          type: array
          items:
            $ref: '#/definitions/Statement'
          description: A list of statements which define the actions a user or device is allowed to perform
        properties:
          type: object
          description: A map of key value properties
          additionalProperties:
            type: string
          example:
            key1: value1
  UpdatePolicyTemplateRequest:
    in: body
    name: updatePolicyTemplate
    description: The request to update an existing policy
    schema:
      title: Update Policy Template Request
      description: Parameters for updating policy templates
      type: object
      properties:
        name:
          type: string
          description: The name
        type:
          type: string
          enum: [user, service]
          description: The policy template type
        statements:
          type: array
          items:
            $ref: '#/definitions/Statement'
          description: A list of statements which define the actions a user or device is allowed to perform
        properties:
          type: object
          description: A map of key value properties
          additionalProperties:
            type: string
          example:
            key1: value1

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

  AuthResponse:
    description: Auth Response
    schema:
      type: object
      title: Auth Response
      properties:
        user:
          $ref: '#/definitions/User'
        org:
          $ref: '#/definitions/Org'
        workspaces:
          type: array
          items:
            $ref: '#/definitions/Workspace'
        policies:
          type: array
          items:
            $ref: '#/definitions/AuthPolicy'
        properties:
          type: object
          description: A map of key value properties
          additionalProperties:
            type: string
          example:
            key1: value1

  CreateSessionKeyResponse:
    description: Create Session Key Response
    schema:
      $ref: '#/definitions/Key'

  GetKeysResponse:
    description: Get Keys Response
    schema:
      title: Get Keys Response
      type: object
      properties:
        totalCount:
          description: Total number of keys which match a given query
          type: integer
        keys:
          description: List of keys
          type: array
          items:
            $ref: '#/definitions/Key'
  CreateKeyResponse:
    description: Create Key Response
    schema:
      $ref: '#/definitions/Key'
  GetKeyResponse:
    description: Get Key Response
    schema:
      $ref: '#/definitions/Key'
  UpdateKeyResponse:
    description: Update Key Response
    schema:
      $ref: '#/definitions/Key'

  GetPoliciesResponse:
    description: Get Policies Response
    schema:
      title: Get Policies Response
      type: object
      properties:
        totalCount:
          description: Total number of policies which match a given query
          type: integer
        policies:
          description: List of policies
          type: array
          items:
            $ref: '#/definitions/Policy'
  CreatePolicyResponse:
    description: Create Policy Response
    schema:
      $ref: '#/definitions/Policy'
  GetPolicyResponse:
    description: Get Policy Response
    schema:
      $ref: '#/definitions/Policy'
  UpdatePolicyResponse:
    description: Update Policy Response
    schema:
      $ref: '#/definitions/Policy'

  GetPolicyTemplatesResponse:
    description: Get Policy Templates Response
    schema:
      title: Get Policy Templates Response
      type: object
      properties:
        totalCount:
          description: Total number of policy templates which match a given query
          type: integer
        policyTemplates:
          description: List of policy templates
          type: array
          items:
            $ref: '#/definitions/PolicyTemplate'
  CreatePolicyTemplateResponse:
    description: Create Policy Template Response
    schema:
      $ref: '#/definitions/PolicyTemplate'
  GetPolicyTemplateResponse:
    description: Get Policy Template Response
    schema:
      $ref: '#/definitions/PolicyTemplate'
  UpdatePolicyTemplateResponse:
    description: Update Policy Template Response
    schema:
      $ref: '#/definitions/PolicyTemplate'

  UserResponse:
    description: User Response
    schema:
      type: object
      title: User Response
      properties:
        user:
          $ref: '#/definitions/User'
        org:
          $ref: '#/definitions/Org'
        workspaces:
          type: array
          items:
            $ref: '#/definitions/Workspace'
        policies:
          type: array
          items:
            $ref: '#/definitions/UserPolicy'
        policyTemplates:
          type: array
          items:
            $ref: '#/definitions/UserPolicyTemplate'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=CONTRIBUTING.md sha256=eb74d297481e5720da96b88a87fdc2e86cb5d45a7a6556b0af460f6a6467720b bytes=2334 -->
## FILE: CONTRIBUTING.md

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `CONTRIBUTING.md`
- sha256: `eb74d297481e5720da96b88a87fdc2e86cb5d45a7a6556b0af460f6a6467720b`
- bytes: 2334

````markdown
# Contributing to systemlink-OpenAPI-documents 

Contributions to systemlink-OpenAPI-documents are welcome from all!

systemlink-OpenAPI-documents is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on [GitHub](https://github.com/ni/systemlink-OpenAPI-documents/).

systemlink-OpenAPI-documents follows a pull-request model for development.  If you wish to
contribute, you will need to create a GitHub account, fork this project, push a
branch with your changes to your project, and then submit a pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for more details.

# Testing

Before making a pull request, ensure that there are no syntax errors in your document by pasting it into [editor.swagger.io](https://editor.swagger.io).

# Developer Certificate of Origin (DCO)

   Developer's Certificate of Origin 1.1

   By making a contribution to this project, I certify that:

   (a) The contribution was created in whole or in part by me and I
       have the right to submit it under the open source license
       indicated in the file; or

   (b) The contribution is based upon previous work that, to the best
       of my knowledge, is covered under an appropriate open source
       license and I have the right under that license to submit that
       work with modifications, whether created in whole or in part
       by me, under the same open source license (unless I am
       permitted to submit under a different license), as indicated
       in the file; or

   (c) The contribution was provided directly to me by some other
       person who certified (a), (b) or (c) and I have not modified
       it.

   (d) I understand and agree that this project and the contribution
       are public and that a record of the contribution (including all
       personal information I submit with it, including my sign-off) is
       maintained indefinitely and may be redistributed consistent with
       this project or the open source license(s) involved.

(taken from [developercertificate.org](https://developercertificate.org/))

See [LICENSE](https://github.com/ni/systemlink-OpenAPI-documents/blob/master/LICENSE)
for details about how systemlink-OpenAPI-documents is licensed.
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=file/nifile.yml sha256=57ce21947e936febd1561956a7b9d33655749a093464d0a8f46b6b164a3353c2 bytes=30525 -->
## FILE: file/nifile.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `file/nifile.yml`
- sha256: `57ce21947e936febd1561956a7b9d33655749a093464d0a8f46b6b164a3353c2`
- bytes: 30525

````yaml
swagger: '2.0'
info:
  version: '1'
  title: SystemLink File Service
  description: Upload and download files from a SystemLink server
  contact:
    name: NI
    url: https://www.ni.com/systemlink
    email: support@ni.com
basePath: /nifile
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

x-ni-routing-key: Skyline.FileIngestion
definitions:
  Link:
    description: A hyperlink for a resource or action on a resource
    type: object
    properties:
      href:
        type: string
        description: URI of the link
        example: /nifile/v1/service-groups
    required: [href]
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
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251040
      message: One or more errors occurred. See the contained list for details of each error.
      args: []
      innerErrors:
        - name: FileIngestion.IdNotFound
          code: -251608
          resourceType: file
          resourceId: '4afb2ce3741fe11d88838cc9'
          message: File with id '4afb2ce3741fe11d88838cc9' not found.
          args: ['4afb2ce3741fe11d88838cc9']
  FileMetadata:
    description: File metadata
    type: object
    properties:
      _links:
        description: >-
          The links to access and manipulate the file:

          - data: Link to download the file using a GET request

          - delete: Link to delete the file using a DELETE request

          - self: Link to the file's metadata

          - updateMetadata: Link to update the file's metadata using a POST request
        type: object
        required: [self]
        additionalProperties:
          $ref: '#/definitions/Link'
        properties:
          self:
            $ref: '#/definitions/Link'
        example:
          data:
            href: /nifile/v1/service-groups/Default/files/5b0739cc741fe114f08bd06c/data
          delete:
            href: /nifile/v1/service-groups/Default/files/5b0739cc741fe114f08bd06c
          self:
            href: /nifile/v1/service-groups/Default/files/5b0739cc741fe114f08bd06c
          updateMetadata:
            href: /nifile/v1/service-groups/Default/files/5b0739cc741fe114f08bd06c/update-metadata
      created:
        description: The date and time the file was created in the file service
        type: string
        format: date-time
        example: '2018-05-15T18:54:27.519Z'
      id:
        description: The file's ID within the service group
        type: string
        example: '5afb2ce3741fe11d88838cc9'
      path:
        description: The path to the file on the server.  This field is returned only if the user has associated privileges to view file paths.
        type: string
        example: 'C:\temp\4afb2ce3741fe11d88838cc9.txt'
      properties:
        description: The file's properties
        type: object
        additionalProperties:
          type: string
        example:
          Name: myfile.txt
          MyProperty: Value
      metaDataRevision:
        description: The file's properties revision number. When a file is uploaded, the revision number starts at 1. Every time metadata is updated, the revision number is incremented by 1. New in version 3 of the listFiles operation.
        type: integer
        format: int32
        example: 1
      serviceGroup:
        description: The service group that owns the file
        type: string
        example: Default
      size:
        description: The 32-bit file size in bytes. If the value is larger than a 32-bit integer, this value is -1 and the size64 parameter contains the correct value.
        type: integer
        format: int32
        example: 7277
      size64:
        description: The 64-bit file size in bytes
        type: integer
        format: int64
        example: 7277
      workspace:
        description: The workspace the file belongs to
        type: string
        example: MyWorkspace
      lastUpdatedTimestamp:
        description: The date and time the file was last updated in the file service
        type: string
        format: date-time
        example: '2018-05-15T18:54:27.519Z'
  ServiceGroup:
    type: object
    properties:
      name:
        type: string
        description: The service group's name
        example: Default
      _links:
        description: >-
          The links that apply to a service group:

          - deleteFiles: Link to delete multiple files from the service group using POST

          - files: Link to retrieve a list of files in the service group using GET

          - query: Link to query for available files in the service group using POST

          - searchFiles: Link to retrieve a filtered list of files in the service group using GET

          - self: Link to the current service group

          - upload: Link to upload files to the service group using POST
        type: object
        required: [self]
        additionalProperties:
          $ref: '#/definitions/Link'
        properties:
          self:
            $ref: '#/definitions/Link'
        example:
          deleteFiles:
            href: /nifile/v1/service-groups/Default/delete-files
          files:
            href: /nifile/v1/service-groups/Default/files
          query:
            href: /nifile/v1/service-groups/Default/query-files
          searchFiles:
            href: /nifile/v1/service-groups/Default/files
          self:
            href: /nifile/v1/service-groups/Default
          upload:
            href: /nifile/v1/service-groups/Default/upload-files
  DateQuery:
    description: A query for a date and time field
    type: object
    properties:
      operation:
        description: The query operation
        type: string
        enum:
          - EQUAL
          - GREATER_THAN
          - GREATER_THAN_OR_EQUAL
          - LESS_THAN
          - LESS_THAN_OR_EQUAL
          - NOT_EQUAL
      value:
        description: The value of the field to search for
        type: string
        format: date-time
        example: '2018-05-14T00:00:00.000Z'
    required:
      - operation
      - value
    example:
      operation: GREATER_THAN
      value: '2018-05-14T00:00:00.000Z'
  IntegerQuery:
    description: A query for an integer field
    type: object
    properties:
      operation:
        description: The query operation
        type: string
        enum:
          - EQUAL
          - GREATER_THAN
          - GREATER_THAN_OR_EQUAL
          - LESS_THAN
          - LESS_THAN_OR_EQUAL
          - NOT_EQUAL
      value:
        description: The value of the field to search for
        type: integer
        format: int32
        example: 5000
    required:
      - operation
      - value
    example:
      operation: LESS_THAN
      value: 5000
  PropertyQuery:
    description: A query for a file property
    type: object
    properties:
      key:
        description: The name of the property to search against
        type: string
        example: Name
      operation:
        description: The query operation
        type: string
        enum:
          - CONTAINS
          - EQUAL
          - NOT_CONTAINS
          - NOT_EQUAL
      value:
        description: The value of the property to search for
        type: string
        example: myfile.txt
    required:
      - key
      - operation
      - value
    example:
      key: Name
      operation: CONTAINS
      value: myfile
  IdsQuery:
    description: A query for a list of ids
    type: object
    properties:
      operation:
        description: The query operation
        type: string
        enum:
          - EQUAL
          - NOT_EQUAL
      ids:
        description: The array of ids to search for
        type: array
        items:
          type: string
          example: '4afb2ce3741fe11d88838cc9'
    required:
      - operation
      - ids
  StringQuery:
    description: A query for a string field
    type: object
    properties:
      operation:
        description: The query operation
        type: string
        enum:
          - EQUAL
          - NOT_EQUAL
      value:
        description: The value of the field to search for
        type: string
        example: txt
    required:
      - operation
      - value
  Operation:
    description: An operation provided by the API
    type: object
    properties:
      available:
        type: boolean
        description: Whether the operation is available to the caller
      version:
        type: integer
        format: int32
        description: The version of the available operation
    required: [available]
    example:
      available: true
      version: 1
  V1Operations:
    description: V1 operations
    type: object
    properties:
      operations:
        description: >-
          Available operations in the v1 version of the API:

          - deleteFiles: The ability to delete uploaded files

          - downloadData: The ability to download file data

          - listFiles: The ability to list available files and service groups

          - queryFiles: The ability to query available files and service groups

          - updateMetadata: The ability to update file metadata properties

          - uploadFiles: The ability to upload files
        type: object
        properties:
          deleteFiles:
            $ref: '#/definitions/Operation'
          downloadData:
            $ref: '#/definitions/Operation'
          listFiles:
            $ref: '#/definitions/Operation'
          queryFiles:
            $ref: '#/definitions/Operation'
          updateMetadata:
            $ref: '#/definitions/Operation'
          uploadFiles:
            $ref: '#/definitions/Operation'

parameters:
  id:
    in: path
    name: id
    description: The ID of the file
    type: string
    required: true
    x-example: '4afb2ce3741fe11d88838cc9'

responses:
  PartialSuccess:
    description: Partial Success in the case when only a part of the request body metadata information was processed successfully.
    schema:
      title: PartialSuccessResponse
      description: Partial success response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
  Query:
    description: OK
    schema:
      description: The result of a file query
      title: QueryResponse
      type: object
      properties:
        _links:
          description: >-
            The links that apply to the collection of files for a service group:

            - deleteFiles: Link to delete multiple files from the service group using a POST

            - query: Link to query for available files in the service group using a POST

            - search: Link to retrieve a filtered list of files in the service group using a GET

            - self: Link to the current service group

            - upload: Link to upload files to the service group using a POST
          type: object
          required: [self]
          additionalProperties:
            $ref: '#/definitions/Link'
          properties:
            self:
              $ref: '#/definitions/Link'
          example:
            deleteFiles:
              href: /nifile/v1/service-groups/Default/delete-files
            query:
              href: /nifile/v1/service-groups/Default/query-files
            search:
              href: /nifile/v1/service-groups/Default/files
            self:
              href: /nifile/v1/service-groups/Default/files
            upload:
              href: /nifile/v1/service-groups/Default/upload-files
        availableFiles:
          description: The list of files returned by the query
          type: array
          items:
            $ref: '#/definitions/FileMetadata'
        totalCount:
          description: The total number of files that match the query regardless of skip and take values
          type: integer
          format: int64
          example: 1
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

paths:
  /:
    get:
      tags: [versioning]
      summary: API information
      description: Returns information about API versions and available operations.
      operationId: RootEndpoint      
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
              version:
                description: The implementation version of the web service
                type: string
  /{version}:
    parameters:
      - in: path
        name: version
        description: The version of the API to retrieve operations.
        type: string
        required: true
    get:
      tags: [versioning]
      summary: API version information
      description: Returns available operations for a single version of the API.
      operationId: RootEndpointWithVersion
      # Explicitly mark security as an empty array - this route does not require any privileges.
      # Marking it this way prevents it from inheriting the top-level security settings.
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
  /v1/service-groups:
    get:
      tags: [service groups]
      summary: List service groups      
      description: >-
        Returns an array of File service group names. Each service group is a
        distinct collection of files.
      operationId: ListServiceGroups
      x-ni-auth: true
      x-ni-operation: listFiles
      responses:
        200:
          description: OK
          schema:
            description: Service group information
            title: ListServiceGroupsResponse
            type: object
            properties:
              _links:
                type: object
                description: >-
                  Links that apply to the collection of service groups:

                  - self: Link to the collection of service groups
                properties:
                  self:
                    $ref: '#/definitions/Link'
              serviceGroups:
                type: array
                description: Array of service groups within the file service
                items:
                  $ref: '#/definitions/ServiceGroup'
        401:
          $ref: '#/responses/Unauthorized'
  /v1/service-groups/Default/files:
    get:
      tags: [files]
      summary: List available files
      description: >-
        Lists available files on the SystemLink File service.

        Use the skip and take parameters to return paged responses.

        The orderBy and orderByDescending fields can be used to manage sorting
        the list by metadata objects.
      operationId: ListAvailableFiles_GET
      x-ni-auth: true
      x-ni-operation: listFiles
      parameters:
        - in: query
          name: skip
          description: >-
            How many files to skip in the result when paging.
            For example, a list of 100 files with a skip value of 50 and a take
            value of 25 will return entries 51 through 75.
          type: integer
          format: int32
          default: 0
          minimum: 0
        - in: query
          name: take
          description: >-
            How many files to return in the result, or 0 to use a default
            defined by the service.
            For example, a list of 100 files with a skip value of 50 and a take
            value of 25 will return entries 51 through 75.
          type: integer
          format: int32
          default: 0
          minimum: 0
          maximum: 10000
        - in: query
          name: orderBy
          description: >-
            The name of the metadata key to sort by. The value of the orderBy field should be
            the name of a metadata key.
          type: string
          enum:
            - created
            - id
            - size
            - lastUpdatedTimestamp
        - in: query
          name: orderByDescending
          description: >-
            Whether to sort descending instead of ascending.
            The elements in the list are sorted ascending by default. If the
            orderByDescending parameter is specified, the elements in the list
            are sorted based on it's value. The orderByDescending value must be
            a boolean string. The elements in the list are sorted ascending if
            false and descending if true.
          type: boolean
          default: false
        - in: query
          name: id
          description: Comma-separated list of file IDs to search by
          type: string
          x-example: '5afb2ce3741fe11d88838cc9,4afb2ce3741fe11d88838cc9'
      responses:
        200:
          $ref: '#/responses/Query'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/service-groups/Default/files/{id}:
    parameters:
      - $ref: '#/parameters/id'
    delete:
      tags: [files]
      summary: Delete file
      description: Deletes the file indicated by the resource ID.
      operationId: Delete
      x-ni-auth: true
      x-ni-operation: deleteFiles
      x-ni-request-variables: [REMOTE_USER, USER_NAME]
      responses:
        204:
          description: No content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
      parameters:
        - in: query
          name: force
          description: Whether the deletion of a file will be forced.  New in version 2 of this operation.
          type: boolean
          default: false
  /v1/service-groups/Default/files/{id}/data:
    parameters:
      - $ref: '#/parameters/id'
    get:
      tags: [files]
      summary: Download file
      description: >-
        Downloads a file from the SystemLink File service in
        a single HTTP response.

        Use the inline parameter in the query string to control the download
        behavior.
      x-ni-auth: true
      operationId: ReceiveFile
      x-ni-operation: downloadData
      x-ni-request-variables:
        - REQUEST_METHOD
      parameters:
        - in: query
          name: inline
          description: >-
            Whether to return the file data inline rather than as an attachment.
            When the inline query parameter is true, the file contents return
            directly for the caller to handle. The Content-Disposition header
            and MIME type remain unset.
            When the the inline query parameter is not specified or is
            false, the file contents are handled as a download. The
            Content-Disposition header is set to 'attachment' and
            the MIME type is set to binary.
          type: boolean
          default: false
      produces:
        - application/octet-stream
        - application/json
      responses:
        200:
          description: OK
          schema:
            description: The file data
            type: file
          examples:
            application/octet-stream:
              File data
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/service-groups/Default/files/{id}/update-metadata:
    parameters:
      - $ref: '#/parameters/id'
    post:
      tags: [files]
      summary: Update file metadata properties
      description: >-
        Updates an existing file's metadata with the specified metadata
        properties.

        Use the replaceExisting element to determine the replace or merge
        behavior.
      operationId: UpdateMetadata
      x-ni-auth: true
      x-ni-operation: updateMetadata
      x-ni-request-variables: [REMOTE_USER, USER_NAME]
      parameters:
        - in: body
          name: metadata
          description: The file's metadata and options for updating it
          required: true
          schema:
            description: The file's metadata and options for updating it
            title: UpdateMetadataRequest
            type: object
            properties:
              replaceExisting:
                description: >-
                  Determines whether the current list should be entirely
                  replaced by the specified list or merged with the existing
                  list.
                type: boolean
              expectedRevision:
                description: This is an optional value. When specified, this is an integer that should be set to match the last known revision number of the metadata. If it doesn't match at the time of execution, the update request will be rejected. This is used to ensure that changes to this file metadata are correctly using the previous state.
                type: integer
                format: int32
              properties:
                description: >-
                  The properties to set. A map of key value properties containing the metadata to be attached.
                  Predefined:
                  - Name: This is an optional property for renaming the file. When specified, the file will be renamed.
                type: object
                additionalProperties:
                  type: string
                example:
                  key: value
              workspace:
                description: This is an optional value. When specified, the workspace of the metadata will be updated to the new value.
                type: string
            required:
              - replaceExisting
              - properties
      responses:
        204:
          description: No content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/service-groups/Default/delete-files:
    post:
      tags: [files]
      summary: Delete multiple files
      description: >-
        Deletes multiple files in a single API call. The request body contains
        an array of file ids to delete.
      operationId: DeleteMultiple
      x-ni-auth: true
      x-ni-operation: deleteFiles
      x-ni-request-variables: [REMOTE_USER, USER_NAME]
      parameters:
        - in: query
          name: force
          description: Whether the deletion of files will be forced.  New in version 2 of this operation.
          type: boolean
          default: false
        - in: body
          name: files
          description: The description of files to delete
          required: true
          schema:
            description: The description of files to delete
            title: DeleteMultipleRequest
            type: object
            properties:
              ids:
                description: The list of file IDs to delete
                type: array
                items:
                  description: The ID of a file to delete
                  type: string
                  example: '5afb2ce3741fe11d88838cc9'
            required: [ids]
      responses:
        200:
          $ref: '#/responses/PartialSuccess'
        204:
          description: No content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/service-groups/Default/query-files:
    post:
      tags: [files]
      summary: Query files
      description: >-
        Queries the SystemLink File service for a list of files that match
        specified metadata properties.

        Query elements:

        - idQuery: a JSON query object with a string value.

        - sizeMaxQuery: a JSON query object with an integer value.

        - sizeMinQuery: a JSON query object with an integer value.

        - createdQuery: a JSON query object with an ISO8601 date string value.

        - propertiesQuery: a JSON array of query objects with string values.
      operationId: QueryAvailableFiles
      x-ni-auth: true
      x-ni-operation: listFiles
      parameters:
        - in: query
          name: skip
          description: How many files to skip in the result when paging.  New in version 2 of the list-files operation.
          type: integer
          format: int32
          default: 0
          minimum: 0
        - in: query
          name: take
          description: >-
            How many files to return in the result.  New in version 2 of the list-files operation.
            The default value is defined by the service.
          type: integer
          format: int32
          default: 1000
          minimum: 0
          maximum: 1000
        - in: query
          name: workspace
          description: Limit the query to the workspace with the given id.  New in version 2 of this operation.
          type: string
          default: null
          x-example: 1f2641dd-a5ac-4869-835e-5340b4cd386c
        - in: body
          name: query
          description: The queries used to filter the result
          schema:
            description: The queries used to filter the results
            title: QueryAvailableFilesRequest
            type: object
            properties:
              idsQuery:
                $ref: '#/definitions/IdsQuery'
              idQuery:
                $ref: '#/definitions/StringQuery'
              extensionQuery:
                $ref: '#/definitions/StringQuery'
              sizeMaxQuery:
                $ref: '#/definitions/IntegerQuery'
              sizeMinQuery:
                $ref: '#/definitions/IntegerQuery'
              createdQuery:
                $ref: '#/definitions/DateQuery'
              propertiesQuery:
                description: An array of queries for file properties
                type: array
                items:
                  $ref: '#/definitions/PropertyQuery'
      responses:
        200:
          $ref: '#/responses/Query'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/service-groups/Default/upload-files:
    post:
      tags: [files]
      summary: Upload file
      description: >-
        Uploads a file using multipart/form-data headers to send the file
        payload in the HTTP body.
      operationId: Upload
      x-ni-auth: true
      x-ni-operation: uploadFiles
      x-ni-request-variables: [REMOTE_USER, USER_NAME]
      consumes:
        - multipart/form-data
      parameters:
        - in: formData
          name: file
          description: The file to upload.
          type: file
          required: true
        - in: formData
          name: metadata
          description: JSON Dictionary with key/value pairs
          type: string
        - in: formData
          name: id
          description: >-
            Optional field that allows the client to specify the ID of the file
            once it is uploaded. An ID is expected to be a 24-digit hex string,
            which is unique among all files.
          type: string
        - in: query
          name: workspace
          description: The id of the workspace the file belongs to
          type: string
          default: null
          x-example: 1f2641dd-a5ac-4869-835e-5340b4cd386c
      responses:
        201:
          description: OK
          schema:
            description: Uploaded file information
            title: UploadResponse
            type: object
            properties:
              uri:
                type: string
                description: URI of the uploaded file
                example: '/nifile/v1/service-groups/Default/files/5b874c4adedd0f1c78a22a96'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/ping:
    get:
      tags: [deprecated]
      summary: Check service status
      description: Determines if the web service is available
      operationId: Ping
      deprecated: true
      # Explicitly mark security as an empty array - this route does not require any privileges.
      # Marking it this way prevents it from inheriting the top-level security settings.
      security: []
      responses:
        204:
          description: No content
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=LICENSE sha256=431e6e9e2f5c5700455b16c214e06f7a1b821b53bb82a7595108eb1bc4709d99 bytes=1091 -->
## FILE: LICENSE

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `LICENSE`
- sha256: `431e6e9e2f5c5700455b16c214e06f7a1b821b53bb82a7595108eb1bc4709d99`
- bytes: 1091

````text
Copyright (c) 2018, National Instruments Corp.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=message/nimessage.yml sha256=267db283e966d0bc377e5ab247322cd0b47abe22848241c90cc3ef76593688e7 bytes=14238 -->
## FILE: message/nimessage.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `message/nimessage.yml`
- sha256: `267db283e966d0bc377e5ab247322cd0b47abe22848241c90cc3ef76593688e7`
- bytes: 14238

````yaml
swagger: '2.0'
info:
  description: Send and receive messages between systems using a publish-subscribe model.
  version: '1'
  title: SystemLink Message Service
  contact:
    name: NI
    url: 'https://www.ni.com/systemlink'
    email: support@ni.com
basePath: /nimessage
consumes:
  - application/json
produces:
  - application/json
securityDefinitions:
  apiKeyAuth:
    type: apiKey
    name: x-ni-api-key
    in: header
  basicAuth:
    type: basic
security:
  - apiKeyAuth: []
  - basicAuth: []

responses:
  Unauthorized:
    description: Not authorized
    headers:
      WWW_Authenticate:
        description: Information for how to authenticate (sent only from SystemLink Server).
        type: string

  ValidationError:
    description: Invalid input data
    schema:
      description: Error response
      title: ErrorResponse
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

  Error:
    description: Error
    schema:
      description: Error response
      title: ErrorResponse
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

parameters:
  Token:
    in: path
    name: token
    description: Unique session ID
    type: string
    required: true
  CreateSessionRequest:
    in: body
    name: createSessionRequest
    description: Request to create a new session
    schema:
      title: Create Session Request
      description: Creates a message session with the server to send and receive messages.
      type: object
      properties:
        workspace:
          type: string
          description: The ID of the workspace used by this session.
          example: 8472777d-8e2f-4c42-bceb-7901ede23085
      example:
        workspace: 8472777d-8e2f-4c42-bceb-7901ede23085

paths:
  /v1/sessions:
    post:
      tags:
        - sessions
      summary: Create a session
      description: Creates a message session with the server to send and receive messages.
      operationId: CreateSession
      parameters:
        - $ref: '#/parameters/CreateSessionRequest'
      responses:
        200:
          schema:
            $ref: '#/definitions/SessionToken'
          description: Success
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        403:
          description: Reached the maximum number of sessions
        default:
          $ref: '#/responses/Error'
  /v1/sessions/{token}:
    delete:
      tags:
        - sessions
      summary: Delete a session
      description: Terminates the message session. If you do not delete the message session, the message service deletes the sesssion after five minutes of inactivity
      operationId: DeleteSession
      parameters:
        - $ref: '#/parameters/Token'
      responses:
        204:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/sessions/{token}/subscriptions/subscribe:
    post:
      tags:
        - topics
      summary: Subscribe to a topic
      description: Subscribes to a topic to receive all messages broadcast with that topic name.
      operationId: SubscribeToTopic
      parameters:
        - $ref: '#/parameters/Token'
        - in: body
          name: topic
          description: The topic to subscribe to
          required: true
          schema:
            $ref: '#/definitions/Topic'
      responses:
        204:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/sessions/{token}/subscriptions/unsubscribe:
    post:
      tags:
        - topics
      summary: Unsubscribe from a topic
      description: Unsubscribes from a topic to stop receiving messages for that topic.
      operationId: UnsubscribeFromTopic
      parameters:
        - $ref: '#/parameters/Token'
        - in: body
          name: topic
          description: Topic to unsubscribe from
          required: true
          schema:
            $ref: '#/definitions/Topic'
      responses:
        204:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'

  /v1/sessions/{token}/messages:
    post:
      tags:
        - message queue
      summary: Publish a message
      description: Broadcasts a message to a topic. Subscribers of a topic receive every message published to the topic.
      operationId: PublishMessage
      parameters:
        - $ref: '#/parameters/Token'
        - in: body
          name: topicAndMessage
          description: The message to publish, and the topic to publish to
          required: true
          schema:
            $ref: '#/definitions/TopicAndMessage'
      responses:
        204:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    get:
      tags:
        - message queue
      summary: Read a message from the queue
      description: Returns a message from the queue. To read a message, subscribe to a topic first.
      operationId: ReadMessage
      parameters:
        - $ref: '#/parameters/Token'
        - in: query
          name: timeoutMilliseconds
          description: Amount of time, in milliseconds, to keep the messaging connection open. May be overridden by a maximum value that the server administrator allows.
          type: integer
          required: false
      responses:
        200:
          schema:
            $ref: '#/definitions/TopicAndMessage'
          description: Success
        204:
          description: No messages were available.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      tags:
        - message queue
      summary: Flush the message queue
      description: Clears all messages from the session queue without reading them.
      operationId: DeleteMessages
      parameters:
        - $ref: '#/parameters/Token'
      responses:
        204:
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/sessions/{token}/configuration/queueSizeBytes:
    get:
      tags:
        - message queue
      summary: Get the current queue size
      description: Returns the size (in bytes) of the message queue associated with this session. This is helpful for determining the amount of memory that unread messages are consuming.
      operationId: GetCurrentQueueSize
      parameters:
        - $ref: '#/parameters/Token'
      responses:
        200:
          schema:
            $ref: '#/definitions/QueueSizeBytes'
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/sessions/{token}/configuration/maxQueueSizeBytes:
    get:
      tags:
        - message queue
      summary: Get the maximum queue size
      description: Returns the maximum size (in bytes) of the message queue associated with this session. This is helpful for determining how much total memory is available for storing messages.
      operationId: GetMaximumQueueSize
      parameters:
        - $ref: '#/parameters/Token'
      responses:
        200:
          schema:
            $ref: '#/definitions/MaxQueueSizeBytes'
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/websocket:
    get:
      tags:
        - webSocket
      summary: Open a WebSocket session
      description: Opens a persistent connection to the web server that allows two-way communication using a JSON
                   protocol. After you open a connection, you can publish messages and subscribe or unsubscribe to topics.
                   Refer to the *Models* section to access the schema for these actions.
      operationId: OpenWebSocketSession
      parameters:
        - in: query
          name: workspace
          description: The ID of the workspace used by this session.
          type: string
          required: false
          x-example: c04c612b-0ba8-4c8e-a8af-a7f314c44715
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
          description: Randomly selected sixteen-byte base64-encoded string. Used to confirm a valid WebSocket handshake. Must be selected randomly for each new connection.
          type: string
          required: true
          x-example: dGhlIHNhbXBsZSBub25jZQ==
      responses:
        101:
          description: Switching Protocols
          headers:
            Sec-WebSocket-Accept:
              description: Used in the WebSocket opening handshake. Set to a value derived from the Sec-WebSocket-Key header.
              type: string
        400:
          $ref: '#/responses/ValidationError'
        401:
          $ref: '#/responses/Unauthorized'
        403:
          description: Reached the maximum number of sessions
        426:
          description: Upgrade Required

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
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251040
      message: One or more errors occurred. See the contained list for details of each error.
      args: []
      innerErrors:
        - name: Message.SessionTokenNotFound
          code: -251608
          resourceType:
          resourceId:
          message: Session token 'f755d531-2403-433f-a0b7-463ccb8f2b9' not found.
          args: ['f755d531-2403-433f-a0b7-463ccb8f2b9']
  TopicAndMessage:
    type: object
    title: Topic and Message
    required:
      - topic
      - message
    properties:
      topic:
        description: Topic name
        type: string
      message:
        description: Message content
        type: string
    description: The topic and message content
    example:
      topic: systemHealth
      message: System A has crashed
  Topic:
    type: object
    title: Topic
    required:
      - topic
    properties:
      topic:
        description: Topic name
        type: string
    description: Topic name
    example:
      topic: systemHealth
  SessionToken:
    type: object
    title: Session Token
    required:
      - token
    properties:
      token:
        description: Unique session ID
        type: string
    description: Unique session ID
    example:
      token: BAB2AFFA-7AFA-4C79-BD41-00F25E3B8F61
  QueueSizeBytes:
    type: object
    title: Current Queue Size
    required:
      - queueSizeBytes
    properties:
      queueSizeBytes:
        description: Current queue size (in bytes)
        type: integer
    description: Current queue size (in bytes)
    example:
      queueSizeBytes: 100
  MaxQueueSizeBytes:
    type: object
    title: Maximum Queue Size
    required:
      - maxQueueSizeBytes
    properties:
      maxQueueSizeBytes:
        description: Maximum queue size (in bytes)
        type: integer
    description: Maximum queue size (in bytes)
    example:
      maxQueueSizeBytes: -1
  WebSocketPublish:
    type: object
    title: WebSocket Publish Action
    required:
      - action
      - topic
      - message
    properties:
      action:
        description: The action to perform. Must be set to "publish".
        type: string
        enum: ['publish']
        example: publish
      topic:
        description: Topic to publish a message to
        type: string
      message:
        description: Message to publish
        type: string
    example:
      action: publish
      topic: systemHealth
      message: System A has crashed
  WebSocketSubscribe:
    type: object
    title: WebSocket Subscribe Action
    required:
      - action
      - topic
    properties:
      action:
        description: Action to perform. Must be set to "subscribe".
        type: string
        enum: ['subscribe']
        example: subscribe
      topic:
        description: Topic to subscribe to
        type: string
    example:
      action: subscribe
      topic: systemHealth
  WebSocketUnsubscribe:
    type: object
    title: WebSocket Unsubscribe Action
    required:
      - action
      - topic
    properties:
      action:
        description: Action to perform. Must be set to "unsubscribe".
        type: string
        enum: ['unsubscribe']
        example: unsubscribe
      topic:
        description: Topic to unsubscribe from
        type: string
    example:
      action: unsubscribe
      topic: systemHealth
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=ni-notebook-execution/ninbexec.yml sha256=fcc39a8530fe18622b88883a1d5ab2b37de65c1cd152cc58f52b3bc84498b63e bytes=50287 -->
## FILE: ni-notebook-execution/ninbexec.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `ni-notebook-execution/ninbexec.yml`
- sha256: `fcc39a8530fe18622b88883a1d5ab2b37de65c1cd152cc58f52b3bc84498b63e`
- bytes: 50287

````yaml
swagger: '2.0'
info:
  version: '1'
  title: Notebook Execution Service
  description: Execute Jupyter notebooks.
  contact:
    name: NI
    url: https://www.ni.com/systemlink
    email: support@ni.com
basePath: /ninbexec
x-ni-routing-key: Skyline.NotebookExecution
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
        example: string
      resourceId:
        description: Identifier of the resource associated with the error
        type: string
        example: '46fc8c2b-bcc9-4bac-b016-34d9396d3f99'
      message:
        description: Complete error message
        type: string
        example: One or more errors occurred. See the contained list for details of each error
      args:
        description: Positional argument values for the error code
        type: array
        items:
          type: string
          example: '46fc8c2b-bcc9-4bac-b016-34d9396d3f99'
      innerErrors:
        type: array
        example:
          - name: NotebookExecution.InvalidProperty
            code: -253700
            resourceType: string
            resourceId: '46fc8c2b-bcc9-4bac-b016-34d9396d3f99'
            message: Invalid property.
            args: []
        items:
          $ref: '#/definitions/Error'
    example:
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251040
      message: One or more errors occurred. See the contained list for details of each error.
      args: []
      innerErrors:
        - name: NotebookExecution.InvalidProperty
          code: -253700
          resourceType: string
          resourceId: '46fc8c2b-bcc9-4bac-b016-34d9396d3f99'
          message: Invalid property.
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
  CreateExecutionOperation:
    title: Create Executions Operation
    description: Create Executions array object including export formats
    allOf:
      - $ref: '#/definitions/Operation'
      - type: object
        properties:
          exportFormats:
            description: List of export formats
            type: array
            items:
              $ref: '#/definitions/NotebookExportFormat'
        example:
          exportFormats: [PDF, HTML]
  V1Operations:
    title: Version 1 Operations
    description: V1 operations
    type: object
    properties:
      operations:
        description: >-
          Available operations in the v1 version of the API:

          - queryNotebooks: Query a set of notebooks

          - downloadNotebook: Download notebook file data

          - deleteExecutions: Delete a set of executions

          - queryExecutions: Query a set of executions

          - createExecutions: Create a set of executions

          - cancelExecutions: Cancel a set of executions
        type: object
        properties:
          queryNotebooks:
            $ref: '#/definitions/Operation'
          downloadNotebook:
            $ref: '#/definitions/Operation'
          deleteExecutions:
            $ref: '#/definitions/Operation'
          queryExecutions:
            $ref: '#/definitions/Operation'
          createExecutions:
            $ref: '#/definitions/CreateExecutionOperation'
          cancelExecutions:
            $ref: '#/definitions/Operation'
  V2Operations:
    title: Version 2 Operations
    description: V2 operations
    type: object
    properties:
      operations:
        description: >-
          Available operations in the v2 version of the API:

          - queryNotebooks: Query a set of notebooks

          - downloadNotebook: Download notebook file data

          - deleteExecutions: Delete a set of executions

          - queryExecutions: Query a set of executions

          - createExecutions: Create a set of executions

          - cancelExecutions: Cancel a set of executions
        type: object
        properties:
          queryNotebooks:
            $ref: '#/definitions/Operation'
          downloadNotebook:
            $ref: '#/definitions/Operation'
          deleteExecutions:
            $ref: '#/definitions/Operation'
          queryExecutions:
            $ref: '#/definitions/Operation'
          createExecutions:
            $ref: '#/definitions/CreateExecutionOperation'
          cancelExecutions:
            $ref: '#/definitions/Operation'
  QueryOperation:
    title: Query Operation
    description: Query operation enum
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
        format: int32
        example: 360
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
  ArrayContainsObject:
    title: Array Contains
    description: >-
      Array contains object. This searches an array to find at least one element that matches the
      provided value.
    type: object
    required:
      - name
      - contains
    properties:
      name:
        description: >-
          The name of the key in the parent object that corresponds to the array to search.
        type: string
        example: 'namespaces'
      contains:
        description: The value to search for inside the array.
        type: object
        example: 'namespace 1'
  NotebookField:
    title: Notebook Field
    description: Notebook field enum
    type: string
    enum:
      - PATH
      - CREATED_AT
      - UPDATED_AT
      - PARAMETERS
      - METADATA
  NotebookSortField:
    title: Notebook Sort Field
    description: Notebook sort field enum
    type: string
    enum:
      - PATH
      - CREATED_AT
      - UPDATED_AT
  NotebookExportFormat:
    title: Notebook Export Format
    description: >-
      Specifies the file format for the notebook execution export. If this value is null or
      omitted then no export is performed.
    type: string
    enum:
      - HTML
      - PDF
  NotebookExportOptions:
    title: Notebook Export Options
    description: Configures the notebook execution export.
    type: object
    properties:
      excludeCodeInput:
        description: Exclude the source code cell inputs of the notebook from the export.
        type: boolean
        default: false
  NotebookSortDefinitionObject:
    title: Notebook Sort Definition
    description: Defines the field and direction for sorting notebooks.
    type: object
    required:
      - field
    properties:
      field:
        $ref: '#/definitions/NotebookSortField'
      orderByDescending:
        type: boolean
        default: false
  NotebookQueryObject:
    title: Notebook Query
    type: object
    properties:
      paths:
        description: Array of notebook paths
        type: array
        items:
          type: string
        example:
          - '_shared/reports/First Pass Yield.ipynb'
      createdAtQuery:
        description: Array of time query objects for when the notebook was created
        type: array
        items:
          $ref: '#/definitions/TimeQueryObject'
      updatedAtQuery:
        description: Array of time query objects for when the notebook was modified
        type: array
        items:
          $ref: '#/definitions/TimeQueryObject'
      parameters:
        description: >-
          Array of input parameter dictionaries and their default values. When querying, entries
          in the same dictionary must all match (an "and" relationship within dictionaries).
          Only one of the dictionaries need to match the query (an "or" relationship between
          different dictionaries).
        type: array
        items:
          type: object
          additionalProperties:
            type: object
        example:
          - stringParam: 'my default string value'
            dictParam:
              key1: val1
              key2: val2
          - stringParam: 'my other string value'
            dictParam:
              key1: val3
              key2: val4
      metadata:
        description: >-
          Array of metadata dictionaries to query for. When querying, entries within the same
          dictionary must all match (an "and" relationship within dictionaries). Only one of the
          dictionaries need to match the query (an "or" relationship between different
          dictionaries).
        type: array
        items:
          type: object
          additionalProperties:
            type: object
        example:
          - metadataString: 'my first string value'
            metadataDict:
              key1: val1
              key2: val2
          - metadataString: 'my alternative string value'
            metadataDict:
              key1: val3
              key2: val4
      metadataArrayContains:
        description: >-
          This is a specialized query on the metadata dictionary. It is designed to query one or
          more arrays inside the metadata dictionary such that these arrays contain at least one
          instance of the specified value. It is represented by an array of an array of objects
          referred to as 'Array Contains Objects'. When querying, all elements of the inner array
          of 'Array Contains Objects' must match (an "and" relationship within the inner array).
          Only one element in the outer array needs to match (an "or" relationship within the
          outer array).
        type: array
        items:
          description: >-
            Inner array of 'Array Contains Objects' to query for. When querying, all elements of
            the inner array of 'Array Contains Objects' must match (an "and" relationship within
            the inner array).
          type: array
          items:
            $ref: '#/definitions/ArrayContainsObject'
        example:
          - - name: 'namespaces'
              contains: 'namespace 1'
      sortBy:
        description: Array of notebook sort definition objects to define how to sort the results
        type: array
        items:
          $ref: '#/definitions/NotebookSortDefinitionObject'
      projection:
        description: >-
          Array of notebook fields. If you specify an array, the query returns a result with the
          notebook objects containing the fields that are both specified and available. If you do
          not specify an array, the query will return a result with the notebook objects containing
          all available fields.
        type: array
        items:
          $ref: '#/definitions/NotebookField'
  NotebookAdvancedQuery:
    title: Advanced Query Object for Notebooks
    type: object
    properties:
      filter:
        description: The query filter in Dynamic Linq
        type: string
        example: (metadata["key1"] == "value1") || ((parameters["key2"] != "value2") && (updatedAt >= "2002-12-25T01:01:01.1234567Z"))
      orderBy:
        $ref: '#/definitions/NotebookSortField'
      descending:
        description: ->
          Whether to return the notebooks in descending order.
        type: boolean
        default: false
        example: false
      projection:
        description: >-
          Array of notebook fields. If you specify an array, the query returns a result with the
          notebook objects containing the fields that are both specified and available. If you do
          not specify an array, the query will return a result with the notebook objects containing
          all available fields.
        type: array
        items:
          $ref: '#/definitions/NotebookField'
      skip:
        description: >-
          The number of notebooks to skip over when returning the result. Used for paging.
        type: integer
        format: int32
        default: 0
        minimum: 0
        example: 1000
      take:
        description: >-
          The maximum number of notebooks to return.
        type: integer
        format: int32
        default: 1000
        minimum: 0
        example: 1000
      returnCount:
        description: >-
          Whether to return the total number of notebooks which match the
          provided filter, disregarding the take value.
        type: boolean
        default: false
        example: false
  Notebook:
    title: Notebook
    description: Information about a Jupyter notebook
    type: object
    properties:
      path:
        description: The notebook path.
        type: string
        example: '_shared/reports/First Pass Yield.ipynb'
      createdAt:
        description: File timestamp of when the notebook was created
        type: string
        format: date-time
        example: '2017-11-14T15:41:06.106Z'
      updatedAt:
        description: File timestamp of when the notebook was last modified
        type: string
        format: date-time
        example: '2017-11-14T15:41:06.106Z'
      parameters:
        description: >-
          Input parameters of this notebook and their default values. The keys are strings and
          the values can be of any valid JSON type.
        type: object
        additionalProperties:
          type: object
        example:
          stringParam: 'my default string value'
          dictParam:
            key1: val1
            key2: val2
      metadata:
        description: >-
          Metadata associated with this notebook. The keys are strings and the values can be
          of any valid JSON type.
        type: object
        additionalProperties:
          type: object
        example:
          metadataString: 'my metadata string value'
          metadataDict:
            key1: val1
            key2: val2
  CreateExecution:
    title: Create Execution
    description: Creation information about an execution of a Jupyter notebook
    type: object
    required:
      - notebookPath
    properties:
      notebookPath:
        description: The notebook path associated with the execution.
        type: string
        example: '_shared/reports/First Pass Yield.ipynb'
      parameters:
        description: >-
          The input parameters for this execution of the notebook. The keys are strings and the
          values can be of any valid JSON type.
        type: object
        additionalProperties:
          type: object
        example:
          stringParam: 'my default string value'
          dictParam:
            key1: val1
            key2: val2
      timeout:
        description: >-
          The number of seconds the execution runs before it aborts if uncompleted.
          The timer starts once status is IN_PROGRESS. 0 means infinite. The default is 1 hour
          (3600 seconds).
        type: integer
        format: int32
        default: 3600
        example: 300
      resultCachePeriod:
        description: >-
          The period of time, in seconds, when the result of a previous notebook execution can be
          used as the result of the current notebook execution. Results will only be reused if the
          notebook paths and input parameters match. A value of 0 means that the service will not
          reuse results from any previous notebook executions. A value of -1 means that the
          service will always reuse results if possible. If not possible, return an error. This
          prevents actual execution of a notebook. The default is 24 hours (86400 seconds).
        type: integer
        format: int32
        default: 86400
        example: 3600
      exportFormat:
        description: >-
          Renders the executed notebook and uploads it to the File Ingestion Service. If the user
          specifies an export format and a resultCachePeriod, the export format would be honored
          and resultCachePeriod will be ignored. The file will be exported to the File Ingestion Service.
        $ref: '#/definitions/NotebookExportFormat'
      exportOptions:
        description: >-
          Configures the rendered output of the executed notebook. This will be ignored if no export
          is created.
        $ref: '#/definitions/NotebookExportOptions'
  ExecutionHashInformation:
    title: Execution Hash Information
    description: >-
      Information used to calculate an execution hash. Execution hashes are used
      internally to identify a distinct execution, where if this hash matches, it
      means that the result may be reused. This hash is based on information
      including the notebook path, the last modified timestamp of the notebook, and
      the given parameters of the notebook overriding the default parameters of
      the notebook. This will use the current last modified timestamp of the
      notebook as well as the current default parameters of the notebook. It is
      not possible to calculate hashes based on notebooks that have since been
      modified because the default parameters may have changed. Historical
      versions of default parameters are not tracked.
    type: object
    required:
      - notebookPath
    properties:
      notebookPath:
        description: The notebook path associated with the execution.
        type: string
        example: '_shared/reports/First Pass Yield.ipynb'
      parameters:
        description: >-
          The input parameters for the execution of the notebook. The keys are strings and the
          values can be of any valid JSON type. The hash is calculated, in part, by applying
          these input parameters on top of the default parameters of the notebook. Hence, if the
          value of an input parameter matches the value of the default parameter, the resulting
          hash is the same whether or not that input parameter is present.
        type: object
        additionalProperties:
          type: object
        example:
          stringParam: 'my default string value'
          dictParam:
            key1: val1
            key2: val2
  ExecutionStatus:
    title: Execution Status
    description: Status of the execution
    type: string
    enum:
      - QUEUED
      - IN_PROGRESS
      - FAILED
      - SUCCEEDED
      - CANCELED
      - TIMED_OUT
    example: SUCCEEDED
  ExecutionField:
    title: Execution Field
    description: Execution field enum
    type: string
    enum:
      - ID
      - NOTEBOOK_PATH
      - PARAMETERS
      - EXECUTION_HASH
      - TIMEOUT
      - QUEUED_AT
      - STARTED_AT
      - COMPLETED_AT
      - STATUS
      - EXCEPTION
      - RESULT
  ExecutionSortField:
    title: Execution Sort Field
    description: Execution sort field enum
    type: string
    enum:
      - ID
      - NOTEBOOK_PATH
      - EXECUTION_HASH
      - TIMEOUT
      - QUEUED_AT
      - STARTED_AT
      - COMPLETED_AT
      - STATUS
  ExecutionSortDefinitionObject:
    title: Execution Sort Definition
    description: Defines the field and direction for sorting executions.
    type: object
    required:
      - field
    properties:
      field:
        $ref: '#/definitions/ExecutionSortField'
      orderByDescending:
        type: boolean
        default: false
  ExecutionQueryObject:
    title: Execution Query
    type: object
    properties:
      ids:
        description: Array of execution IDs.
        type: array
        items:
          type: string
        example:
          - 1f05c3c8-7a8c-4ebb-a87f-7a60d5dd8938
      notebookPaths:
        description: Array of notebook paths.
        type: array
        items:
          type: string
        example:
          - '_shared/reports/First Pass Yield.ipynb'
      parameters:
        description: >-
          Array of input parameter dictionaries. When querying, entries within the same dictionary
          must all match (an "and" relationship within dictionaries). Only one of the dictionaries
          needs to match the query (an "or" relationship between different dictionaries).
        type: array
        items:
          type: object
          additionalProperties:
            type: object
        example:
          - stringParam: 'my default string value'
            dictParam:
              key1: val1
              key2: val2
          - stringParam: 'my other string value'
            dictParam:
              key1: val3
              key2: val4
      timeoutQuery:
        description: Array of integer query objects for the execution's timeout
        type: array
        items:
          $ref: '#/definitions/IntegerQueryObject'
      executionHashes:
        description: >-
          Array of objects used to calculate execution hashes. Execution hashes are used
          internally to identify a distinct execution, where if this hash matches, it
          means that the result may be reused. This hash is based on information
          including the notebook path, the last modified timestamp of the notebook, and
          the given parameters of the notebook overriding the default parameters of
          the notebook.
        type: array
        items:
          $ref: '#/definitions/ExecutionHashInformation'
      statuses:
        description: Array of execution statuses.
        type: array
        items:
          $ref: '#/definitions/ExecutionStatus'
      queuedAtQuery:
        description: Array of time query objects for the execution's queue timestamp
        type: array
        items:
          $ref: '#/definitions/TimeQueryObject'
      startedAtQuery:
        description: Array of time query objects for the execution's started timestamp
        type: array
        items:
          $ref: '#/definitions/TimeQueryObject'
      completedAtQuery:
        description: Array of time query objects for the execution's completed timestamp
        type: array
        items:
          $ref: '#/definitions/TimeQueryObject'
      sortBy:
        description: Array of execution sort definition objects that define how to sort the results
        type: array
        items:
          $ref: '#/definitions/ExecutionSortDefinitionObject'
      projection:
        description: >-
          Array of execution fields. If this is not specified, the query returns a result with
          the execution objects containing all available fields. If this is specified, the query
          returns a result with the execution objects containing only the fields that are both
          specified and available.
        type: array
        items:
          $ref: '#/definitions/ExecutionField'
  ExecutionAdvancedQuery:
    title: Advanced Query Object for Notebook Executions
    type: object
    properties:
      filter:
        description: The query filter in Dynamic Linq
        type: string
        example: ((status == "SUCCEEDED") && (result["key1"] == "value1")) || ((status == "FAILED") && (completedAt >= "2002-12-25T01:01:01.1234567Z"))
      orderBy:
        $ref: '#/definitions/ExecutionSortField'
      descending:
        description: ->
          Whether to return the notebook executions in descending order.
        type: boolean
        default: false
        example: false
      projection:
        description: >-
          Array of execution fields. If this is not specified, the query returns a result with
          the execution objects containing all available fields. If this is specified, the query
          returns a result with the execution objects containing only the fields that are both
          specified and available.
        type: array
        items:
          $ref: '#/definitions/ExecutionField'
      skip:
        description: >-
          The number of notebook executions to skip over when returning the result. Used for paging.
        type: integer
        format: int32
        default: 0
        minimum: 0
        example: 1000
      take:
        description: >-
          The maximum number of notebook executions to return.
        type: integer
        format: int32
        default: 1000
        minimum: 0
        example: 1000
      returnCount:
        description: >-
          Whether to return the total number of notebook executions which match the
          provided filter, disregarding the take value.
        type: boolean
        default: false
        example: false
  Execution:
    title: Execution
    description: Information about an execution of a Jupyter notebook.
    type: object
    properties:
      id:
        description: Execution ID
        type: string
        example: '6d958d07-2d85-4655-90ba-8ff84a0482aa'
      notebookPath:
        description: Notebook path associated with the execution
        type: string
        example: '_shared/reports/First Pass Yield.ipynb'
      parameters:
        description: >-
          Input parameters for this execution of the notebook. The keys are strings and the
          values can be of any valid JSON type.
        type: object
        additionalProperties:
          type: object
        example:
          stringParam: 'my default string value'
          dictParam:
            key1: val1
            key2: val2
      metadata:
        description: >-
          Metadata associated with the notebook, at time of execution.
        type: object
        additionalProperties:
          type: object
        example:
          metadataString: 'my metadata string value'
          metadataDict:
            key1: val1
            key2: val2
      executionHash:
        description: >-
          Execution hashes are used internally to identify a distinct execution, where if this
          hash matches, it means that the result may be reused. This hash is based on information
          including the notebook path, the last modified timestamp of the notebook, and the given
          parameters of the notebook overriding the default parameters of the notebook.
        type: string
        example: 'ac6d0228705ad33f91d53aee16acbc012298192f'
      timeout:
        description: >-
          The number of seconds the execution runs before it aborts if uncompleted.
          The timer starts once status is IN_PROGRESS. 0 means infinite.
        type: integer
        format: int32
        example: 300
      status:
        $ref: '#/definitions/ExecutionStatus'
      queuedAt:
        description: Timestamp of when the notebook execution was queued
        type: string
        format: date-time
        example: '2017-11-14T15:41:06.106Z'
      startedAt:
        description: Timestamp of when the notebook execution was started
        type: string
        format: date-time
        example: '2017-11-14T15:41:06.106Z'
      completedAt:
        description: Timestamp of when the notebook execution was completed
        type: string
        format: date-time
        example: '2017-11-14T15:41:06.106Z'
      exception:
        description: >-
          Exception information. This is used only when status is FAILED.
        type: string
        example: 'Traceback (most recent call last):\n  File "<stdin>", line 1, in <module>\n  File "D:\Perforce\MAX\skyline\components\notebook_execution_service\trunk\18.5\objects\export\installers\allos\allproc\systemlink\messagebus\paths.py", line 200, in load_utf8_file_to_string\n    with codecs.open(filename, ''r\'', encoding=''utf-8-sig'') as fp_:\n  File "C:\Program Files\National Instruments\Shared\Skyline\Python\lib\codecs.py", line 897, in open\n    file = builtins.open(filename, mode, buffering)\nFileNotFoundError: [Errno 2] No such file or directory: ''not_existing_file.txt'''
      result:
        description: >-
          Information about the result of an execution of a Jupyter notebook. This is used only
          when the status of the execution is SUCCEEDED.
        type: object
        additionalProperties:
          type: object
        example:
          title: First Pass Yield
          axis_labels:
            - Time (s)
            - '% Yield'
          result_type: STANDARD
          result:
            - index:
                - values
                - percentages
              columns:
                - 0
                - 1
                - 2
                - 3
                - 4
              data:
                - - 40
                  - 5
                  - 3
                  - 1
                  - 1
                - - 80
                  - 90
                  - 96
                  - 98
                  - 100
      cachedResult:
        description: >-
          Whether or not the service is using a cached result instead of running a new execution
        type: boolean
        example: true
      exportFileId:
        description: >-
          File ID of notebook report exported to the File Ingestion Service.
        type: string
        example: '5d1b72663629224d047d1c77'
  CreateExecutionsPartialSuccessResponse:
    title: Create Executions Partial Success Response
    description: Create executions partial success response
    type: object
    required:
      - executions
      - failed
      - error
    properties:
      executions:
        description: Array of executions that were created
        type: array
        items:
          $ref: '#/definitions/Execution'
      failed:
        description: Array of execution requests that failed
        type: array
        items:
          $ref: '#/definitions/CreateExecution'
      error:
        $ref: '#/definitions/Error'
  DeleteExecutionsPartialSuccessResponse:
    title: Delete Executions Partial Success Response
    description: Delete executions partial success response
    type: object
    required:
      - ids
      - failed
      - error
    properties:
      ids:
        description: Array of execution IDs that were successfully deleted
        type: array
        items:
          type: string
        example:
          - '6d9cd574-2c35-4514-8b0e-04c45a7b2cc5'
          - 'b64c45b0-cb9b-4cb9-9207-ff54ab76a25e'
          - '35031757-d6ac-4ea9-b351-eba38ffffcfd'
      failed:
        description: Array of execution IDs that failed to delete
        type: array
        items:
          type: string
        example:
          - '1bcfa300-732a-45a8-80a1-01546d5c4ac1'
          - '293c0b80-6551-4e05-9ae3-e1e2fab8b39f'
      error:
        $ref: '#/definitions/Error'
  CancelExecutionsPartialSuccessResponse:
    title: Cancel Executions Partial Success Response
    description: Cancel executions partial success response
    type: object
    required:
      - ids
      - failed
      - error
    properties:
      ids:
        description: Array of canceled execution IDs
        type: array
        items:
          type: string
        example:
          - '6d9cd574-2c35-4514-8b0e-04c45a7b2cc5'
          - 'b64c45b0-cb9b-4cb9-9207-ff54ab76a25e'
          - '35031757-d6ac-4ea9-b351-eba38ffffcfd'
      failed:
        description: Array of execution IDs that failed to cancel
        type: array
        items:
          type: string
        example:
          - '1bcfa300-732a-45a8-80a1-01546d5c4ac1'
          - '293c0b80-6551-4e05-9ae3-e1e2fab8b39f'
      error:
        $ref: '#/definitions/Error'

parameters:
  notebookPath:
    in: path
    name: path
    description: >-
      Path of the Jupyter notebook. This is a relative path and uses '/' as the delimiter.
    type: string
    required: true
    x-example: '_shared/reports/First Pass Yield.ipynb'
  executionId:
    in: path
    name: id
    description: The ID of the Execution job of a Jupyter notebook
    type: string
    required: true
    x-example: '6d958d07-2d85-4655-90ba-8ff84a0482aa'

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
      x-ni-request-variables: [API_KEY]
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
              v2:
                $ref: '#/definitions/V2Operations'
              version:
                description: Implementation version of the web service
                type: string
  /v1:
    get:
      tags: [versioning]
      summary: API version 1 information
      description: Returns available operations for version 1 of the API.
      operationId: RootEndpointV1
      x-ni-request-variables: [API_KEY]
      # Explicitly mark security as an empty array - this route does not require any privileges.
      # Marking it this way prevents it from inheriting the top-level security settings.
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
  /v2:
    get:
      tags: [versioning]
      summary: API version 2 information
      description: Returns available operations for version 2 of the API.
      operationId: RootEndpointV2
      x-ni-request-variables: [API_KEY]
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
  /v2/notebooks/{path}:
    parameters:
      - $ref: '#/parameters/notebookPath'
    get:
      operationId: GetNotebook
      x-ni-auth: true
      x-ni-operation: queryNotebooks
      x-ni-oldest-compatible-version: 1
      summary: Get information about the specified Jupyter notebook
      description: >-
        Get information about the specified Jupyter notebook.
      tags: [notebooks]
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/Notebook'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/query-notebooks:
    post:
      operationId: QueryNotebooksV2
      x-ni-auth: true
      x-ni-operation: queryNotebooks
      x-ni-request-variables: [REMOTE_USER]
      summary: Query Jupyter notebooks
      description: >-
        Queries the Jupyter notebooks. Notebooks return in descending order of
        'modifiedTime' if no sort order is specified.
      tags: [notebooks]
      parameters:
        - in: body
          name: queryNotebooks
          description: Notebook query object
          required: false
          schema:
            $ref: '#/definitions/NotebookAdvancedQuery'
      responses:
        200:
          description: OK
          schema:
            description: Jupyter notebook information
            title: QueryNotebooksResponseV2
            type: object
            required:
              - notebooks
            properties:
              notebooks:
                description: Array of Jupyter notebooks
                type: array
                items:
                  $ref: '#/definitions/Notebook'
              totalCount:
                description: Number of matching executions
                type: integer
                format: int64
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/notebooks/{path}/data:
    parameters:
      - $ref: '#/parameters/notebookPath'
    get:
      tags: [notebooks]
      summary: Download a notebook file
      description: >-
        Downloads a notebook file in a single HTTP response. Use the inline parameter in the query
        string to control the download behavior.
      operationId: DownloadNotebook
      x-ni-auth: true
      x-ni-operation: downloadNotebook
      x-ni-request-variables:
        - REMOTE_USER
        - REQUEST_METHOD
      x-ni-oldest-compatible-version: 1
      parameters:
        - in: query
          name: inline
          description: >-
            Whether to return the file data inline rather than as an attachment.
            When this parameter is set to true, the file contents return
            directly for the caller to handle. The Content-Disposition header
            is set to 'inline' and the MIME type is unset.
            When the the inline query parameter is not specified or is
            false, the file contents are handled as an attachment. The
            Content-Disposition header is set to 'attachment' and
            the MIME type is set to 'application/json'.
          type: boolean
          default: false
      responses:
        200:
          description: OK
          schema:
            description: Notebook file data
            type: file
          examples:
            application/octet-stream:
              Notebook file data
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/executions/{id}:
    parameters:
      - $ref: '#/parameters/executionId'
    get:
      operationId: GetExecution
      x-ni-auth: true
      x-ni-operation: queryExecutions
      x-ni-oldest-compatible-version: 1
      summary: Get information on the specified execution of a Jupyter notebook
      description: >-
        Gets information on the specified execution of a Jupyter notebook.
      tags: [executions]
      responses:
        200:
          description: Execution information
          schema:
            $ref: '#/definitions/Execution'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      operationId: DeleteExecution
      x-ni-operation: deleteExecutions
      x-ni-oldest-compatible-version: 1
      summary: Delete the specified execution of a Jupyter notebook
      description: Deletes the execution of a Jupyter notebook specified by an execution ID.
      tags: [executions]
      responses:
        204:
          description: No content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/delete-executions:
    post:
      operationId: DeleteExecutions
      x-ni-auth: true
      x-ni-operation: deleteExecutions
      x-ni-oldest-compatible-version: 1
      summary: Delete executions of Jupyter notebooks
      description: >-
        Deletes multiple executions in a single API call. The request body contains
        an array of execution IDs to delete.
      tags: [executions]
      parameters:
        - in: body
          name: executions
          description: Array of executions to delete.
          required: true
          schema:
            description: Array of executions to delete.
            title: DeleteExecutionsRequest
            type: array
            items:
              description: The ID of an execution to delete.
              type: string
              example: '6d958d07-2d85-4655-90ba-8ff84a0482aa'
            minItems: 1
      responses:
        204:
          description: No content
        200:
          description: OK
          schema:
            $ref: '#/definitions/DeleteExecutionsPartialSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/query-executions:
    post:
      operationId: QueryExecutionsV2
      x-ni-auth: true
      x-ni-operation: queryExecutions
      summary: Query executions of Jupyter notebooks
      description: >-
        Queries the executions of Jupyter notebooks. If no sort order is specified,
        executions return in descending order of 'queueTime'.
      tags: [executions]
      parameters:
        - in: body
          name: queryExecutions
          description: Execution query object
          required: false
          schema:
            $ref: '#/definitions/ExecutionAdvancedQuery'
      responses:
        200:
          description: OK
          schema:
            description: Queried execution information
            title: QueryExecutionsResponseV2
            type: object
            required:
              - executions
            properties:
              executions:
                description: Array of executions
                type: array
                items:
                  $ref: '#/definitions/Execution'
              totalCount:
                description: Number of matching executions
                type: integer
                format: int64
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/executions:
    post:
      operationId: CreateExecutions
      x-ni-auth: true
      x-ni-operation: createExecutions
      x-ni-request-variables: [REMOTE_USER]
      x-ni-oldest-compatible-version: 1
      summary: Create one or more executions of Jupyter notebooks
      description: >-
        Creates one or more executions of Jupyter notebooks.
      tags: [executions]
      parameters:
        - in: body
          name: createExecutions
          description: Array of execution creation information
          required: true
          schema:
            description: Array of execution creation information
            title: CreateExecutionsRequest
            type: array
            items:
              $ref: '#/definitions/CreateExecution'
            minItems: 1
      responses:
        201:
          description: Created
          schema:
            description: Array of executions that were created
            title: CreateExecutionsResponse
            type: array
            items:
              $ref: '#/definitions/Execution'
        200:
          description: OK
          schema:
            $ref: '#/definitions/CreateExecutionsPartialSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/cancel-executions:
    post:
      operationId: CancelExecutions
      x-ni-auth: true
      x-ni-operation: cancelExecutions
      x-ni-oldest-compatible-version: 1
      summary: Cancel executions of Jupyter notebooks
      description: >-
        Cancels multiple executions in a single API call. The request body contains an array of
        execution IDs to cancel.
      tags: [executions]
      parameters:
        - in: body
          name: executions
          description: Array of executions to cancel
          required: true
          schema:
            description: Array of executions to cancel
            title: CancelExecutionsRequest
            type: array
            items:
              description: ID of an execution to cancel
              type: string
              example: '6d958d07-2d85-4655-90ba-8ff84a0482aa'
            minItems: 1
      responses:
        204:
          description: No content
        200:
          description: OK
          schema:
            $ref: '#/definitions/CancelExecutionsPartialSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/query-notebooks:
    post:
      operationId: QueryNotebooks
      x-ni-auth: true
      x-ni-operation: queryNotebooks
      x-ni-request-variables: [REMOTE_USER]
      summary: Query Jupyter notebooks
      description: >-
        Queries the Jupyter notebooks. If no Jupyter notebooks are specified, this request returns
        all Jupyter notebooks under the user-specific directory with "reports" sub-directory as
        well as all notebooks under the "_shared" directory with "reports" sub-directory. If you
        specify a relative folder instead of a notebook path for a given array element, this
        request queries all notebooks in the specified folder or in a sub-folder (i.e. a recursive
        search). If you specify a notebook path or relative folder that begins with '/', this
        request searches both the user-specific directory and '_shared' directory. Notebooks return
        in descending order of 'modifiedTime'.
      tags: [deprecated]
      parameters:
        - in: body
          name: queryNotebooks
          description: Notebook query object
          required: false
          schema:
            $ref: '#/definitions/NotebookQueryObject'
        - in: query
          name: skip
          type: integer
          format: int32
          default: 0
          minimum: 0
        - in: query
          name: take
          type: integer
          format: int32
          default: -1
          minimum: -1
      responses:
        200:
          description: OK
          schema:
            description: Jupyter notebook information
            title: QueryNotebooksResponse
            type: object
            required:
              - notebooks
              - totalCount
            properties:
              notebooks:
                description: Array of Jupyter notebooks
                type: array
                items:
                  $ref: '#/definitions/Notebook'
              totalCount:
                description: Number of matching executions
                type: integer
                format: int64
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/query-executions:
    post:
      operationId: QueryExecutions
      x-ni-auth: true
      x-ni-operation: queryExecutions
      summary: Query executions of Jupyter notebooks
      description: >-
        Queries the executions of Jupyter notebooks. If no execution IDs or notebook paths are
        specified, this request returns all executions. Executions return in descending order of
        'queueTime'.
      tags: [deprecated]
      parameters:
        - in: body
          name: queryExecutions
          description: Execution query object
          required: false
          schema:
            $ref: '#/definitions/ExecutionQueryObject'
        - in: query
          name: skip
          type: integer
          format: int32
          default: 0
          minimum: 0
        - in: query
          name: take
          type: integer
          format: int32
          default: -1
          minimum: -1
      responses:
        200:
          description: OK
          schema:
            description: Queried execution information
            title: QueryExecutionsResponse
            type: object
            required:
              - executions
              - totalCount
            properties:
              executions:
                description: Array of executions
                type: array
                items:
                  $ref: '#/definitions/Execution'
              totalCount:
                description: Number of matching executions
                type: integer
                format: int64
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=opcclient/niopcclient.yml sha256=e81dea3b600e668020263dcd5c4f8fdaa4356caf80cee63eda2c7da73d60aaac bytes=34466 -->
## FILE: opcclient/niopcclient.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `opcclient/niopcclient.yml`
- sha256: `e81dea3b600e668020263dcd5c4f8fdaa4356caf80cee63eda2c7da73d60aaac`
- bytes: 34466

````yaml
swagger: "2.0"
info:
  version: "1"
  title: OpcClientService HTTP APIs
  description: OpcClientService HTTP APIs
  contact:
    name: NI
    url: https://www.ni.com/systemlink
    email: support@ni.com
basePath: /niopcclient
x-ni-routing-key: 'Skyline.OpcClient'
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

paths:
  /:
    get:
      operationId: HandleGetVersionInfo
      summary: Gets API information
      tags: [versioning]
      description: Returns permissions and operations for the OpcClientService
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
                description: The implementation version of the web service
                type: string
        default:
          $ref: '#/responses/Error'

  /{version}:
    parameters:
      - in: path
        name: version
        description: The version of the API to retrieve operations.
        type: string
        required: true
    get:
      operationId: RootEndpointWithVersion
      summary: API version information
      description: Returns available operations for a single version of the API.
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
        default:
          $ref: '#/responses/Error'

  /v1/client-certificate:
    get:
      operationId: HandleHttpGetClientCertificate
      x-ni-auth: true
      tags: [certificate]
      summary: Gets SystemLink OPC UA client certificate
      description: Gets SystemLink OPC UA client certificate
      produces:
        - application/x-x509-ca-cert
        - application/json
      responses:
        200:
          description: Successful response
          schema:
            type: file
        default:
          $ref: '#/responses/Error'

  /v1/server-certificates:
    get:
      operationId: HandleHttpGetServerCertificates
      x-ni-auth: true
      tags: [certificate]
      summary: Gets list of certificates from the application's trusted store
      description: Returns list of certificates from the application's trusted store
      responses:
        200:
          description: Successful response
          schema:
            type: array
            items:
              $ref: '#/definitions/SslCertificateInfoModel'
        default:
          $ref: '#/responses/Error'
    post:
      operationId: HandleHttpUploadServerCertificate
      x-ni-auth: true
      tags: [certificate]
      summary: Uploads a certificate to application's trusted store
      description: Uploads the certificate file
      consumes: [multipart/form-data]
      parameters:
        - in: formData
          name: certificate
          description: The certificate to upload.
          type: file
          required: true
      responses:
        201:
          description: Successful response
          schema:
            $ref: '#/definitions/SslCertificateInfoModel'
        default:
          $ref: '#/responses/Error'

  /v1/delete-server-certificates:
    post:
      operationId: HandleHttpDeleteServerCertificates
      x-ni-auth: true
      tags: [certificate]
      summary: Deletes certificates from application's trusted store
      description: Deletes specified certificates
      parameters:
        - in: body
          description: File names of the certificates to be deleted
          required: true
          name: fileNamesToDelete
          schema:
            type: array
            items:
              type: string
            example: ["NI SystemLink OPC UA Connector (1FA889F76A1DEE5DAB2B5880CC6BFE248F12A8EB).der", "zc39017b236b8b67785c4a1b"]
      responses:
        200:
          description: Partial success
          schema:
            $ref: '#/definitions/PartialSuccess'
        204:
          description: Successful response
        default:
          $ref: '#/responses/Error'

  /v1/endpoints:
    get:
      operationId: HandleHttpGetEndpoints
      x-ni-auth: true
      tags: [sessions]
      summary: Gets OPC UA server endpoints
      description: Returns endpoints of an OPC UA server
      parameters:
        - in: path
          description: URL of an OPC UA discovery server
          required: true
          name: uri
          type: string
      responses:
        200:
          description: Successful response
          schema:
            type: array
            items:
              $ref: '#/definitions/SessionEndpointModel'
        default:
          $ref: '#/responses/Error'

  /v1/sessions:
    get:
      operationId: HandleHttpGetSessionsRequest
      x-ni-auth: true
      tags: [sessions]
      summary: Gets existing OPC UA sessions
      description: Returns information about in-progress OPC UA sessions
      responses:
        200:
          description: Successful response
          schema:
            type: array
            items:
              $ref: '#/definitions/SessionResponse'
        default:
          $ref: '#/responses/Error'
    post:
      operationId: HandleHttpCreateSessionRequest
      x-ni-auth: true
      tags: [sessions]
      summary: Creates a new OPC UA session
      description: Connects to an OPC UA server to start a new session
      parameters:
        - in: body
          name: NewSessionRequest
          description: Info about the session to be created
          schema:
            $ref: '#/definitions/NewSessionRequest'
      responses:
        201:
          description: Successful response
          schema:
            $ref: '#/definitions/SessionResponse'
        default:
          $ref: '#/responses/Error'

  /v1/delete-sessions:
    post:
      operationId: HandleHttpDeleteSessionsRequest
      x-ni-auth: true
      tags: [sessions]
      summary: Deletes existing OPC UA sessions
      description: Deletes existing OPC UA sessions
      parameters:
        - in: body
          name: sessionIds
          description: Ids of the sessions to be deleted
          schema:
            type: array
            items:
              title: SessionIds
              type: object
              properties:
                sessionId:
                  type: string
                  description: Id of the session to be deleted
                removeTags:
                  type: boolean
                  default: false
                  description: If set to true it will remove tags for this session's monitored items from taghistorian
              required: [sessionId]
              example:
               - sessionId: 5c39017b236b8b67785c4a1b
                 removeTags: false
               - sessionId: zc39017b236b8b67785c4a1b
                 removeTags: false
      responses:
        200:
          description: Partial success
          schema:
            $ref: '#/definitions/PartialSuccess'
        204:
          description: Successful response
        default:
          $ref: '#/responses/Error'

  /v1/update-sessions:
    post:
      operationId: HandleHttpUpdateSessionsRequest
      x-ni-auth: true
      tags: [sessions]
      summary: Updates existing OPC UA sessions
      description: Modifies name and publishing interval of the existing session
      parameters:
        - in: body
          description: Information to update the session
          name: updateSessionsData
          schema:
            type: array
            items:
                $ref: '#/definitions/UpdateSessionRequest'
            example:
                - sessionId: 5c39017b236b8b67785c4a1b
                  name: "Renamed.opcuaserver.com-48010"
                  monitoringInterval: 5000
                - sessionId: zc39017b236b8b67785c4a1b
                  name: "Renamed.opcuaserver.com-48011"
                  monitoringInterval: 5000
      responses:
        200:
          description: Partial success
          schema:
            $ref: '#/definitions/PartialSuccess'
        204:
          description: Successful response
        default:
          $ref: '#/responses/Error'

  /v1/sessions/{id}/nodes/{path}:
    get:
      operationId: HandleHttpBrowseRequest
      x-ni-auth: true
      tags: [browse]
      summary: Gets child nodes of a node
      description: Gets child nodes of the node specified by {path}
      parameters:
        - name: id
          in: path
          description: session id
          required: true
          type: string
        - name: path
          in: path
          description: Browse path of the node to be browsed. No need to encode the path.
          required: true
          type: string
        - in: query
          name: refresh
          description: If set to true invalidates the cached SystemLinke server browser tree
          type: boolean
          default: false
        - in: query
          name: depth
          description: Depth to which the nodes should be retrieved
          type: integer
          format: int32
          default: 1
      responses:
        200:
          description: Successful response
          schema:
            $ref: '#/definitions/OpcNode'
        default:
          $ref: '#/responses/Error'

  /v1/sessions/{id}/attributes/{opcNodeId}:
    get:
      operationId: HandleHttpReadAttributesRequest
      x-ni-auth: true
      tags: [read]
      summary: Reads attributes of a node
      description: Gets attributes for the node speicified by {opcNodeId}
      parameters:
        - name: id
          in: path
          description: session id
          required: true
          type: string
        - name: opcNodeId
          in: path
          description: Node Id of node.
          required: true
          type: string
      responses:
        200:
          description: Successful response
          schema:
            $ref: '#/definitions/ReadAttributesResponse'
        default:
          $ref: '#/responses/Error'

  /v1/sessions/{id}/monitors:
    get:
      operationId: HandleHttpGetMonitorsRequest
      x-ni-auth: true
      tags: [monitors]
      summary: Gets existing monitored items
      description: Creates SystemLink tags with specified display names
      parameters:
        - name: id
          in: path
          description: session id
          required: true
          type: string
      responses:
        200:
          description: Successful response
          schema:
            type: array
            items:
              $ref: '#/definitions/MonitoredItemResponse'
        default:
            $ref: '#/responses/Error'
    post:
      operationId: HandleHttpCreateMonitorsRequest
      x-ni-auth: true
      x-ni-request-timeout: 50000
      tags: [monitors]
      summary: Creates new monitored items
      description: Adds OPC UA nodes to a subscription for monitoring them. Creates SystemLink tags with specified display names
      parameters:
      - name: id
        in: path
        description: session id
        required: true
        type: string
      - in: body
        name: itemsToCreate
        description: Info of the OPC UA nodes to be monitored
        required: true
        schema:
            type: array
            items:
                $ref: '#/definitions/NewMonitoredItem'
      responses:
        201:
          description: Successful response
          schema:
            type: array
            items:
              $ref: '#/definitions/MonitoredItemResponse'
        200:
          description: Partial success
          schema:
            $ref: '#/definitions/PartialSuccess'
        default:
          $ref: '#/responses/Error'

  /v1/sessions/{id}/delete-monitors:
    post:
      operationId: HandleHttpDeleteMonitorRequest
      x-ni-auth: true
      tags: [monitors]
      summary: Removes existing monitored items
      description: Removes OPC UA nodes from subscription to stop monitoring them. Can optionally remove the SystemLink tags
      parameters:
        - name: id
          in: path
          description: session id
          required: true
          type: string
        - in: body
          name: ItemsToDelete
          description: Info of the nodes for which monitoring should be stopped.
          required: true
          schema:
            type: array
            items:
              $ref: '#/definitions/MonitoredItemDeleteData'
            example:
                - id: "6c3907c6236b8b67785c4a1c"
                  removeTag: false
                - id: "zc39017b236b8b67785c4a1b"
                  removeTag: false
      responses:
        200:
          description: Partial success
          schema:
            $ref: '#/definitions/PartialSuccess'
        204:
          description: Successful response
        default:
          $ref: '#/responses/Error'

  /v1/sessions/{id}/pause-monitors:
    post:
      operationId: HandleHttpPauseMonitorRequest
      x-ni-auth: true
      tags: [monitors]
      summary: Pauses existing monitored items
      description: Pauses to update tag history for the specified OPC UA variables. Doesn't remove the SystemLink tags.
      parameters:
        - name: id
          in: path
          description: session id
          required: true
          type: string
        - in: body
          name: MonitoredItemsIds
          description: Ids of the nodes for which monitoring should be paused.
          required: true
          schema:
            type: array
            items:
              type: string
            example: [ "6c3907c6236b8b67785c4a1c", "zc39017b236b8b67785c4a1b" ]
      responses:
        200:
          description: Partial success
          schema:
            $ref: '#/definitions/PartialSuccess'
        204:
          description: Successful response
        default:
          $ref: '#/responses/Error'

  /v1/sessions/{id}/resume-monitors:
    post:
      operationId: HandleHttpResumeMonitorRequest
      x-ni-auth: true
      tags: [monitors]
      summary: Resumes paused monitored items
      description: Resumes to update the tag history for the specified OPC UA variables.
      parameters:
        - name: id
          in: path
          description: session id
          required: true
          type: string
        - in: body
          name: MonitoredItemsIds
          description: Ids of the nodes for which monitoring should be resumed.
          required: true
          schema:
            type: array
            items:
              type: string
            example: [ "6c3907c6236b8b67785c4a1c", "zc39017b236b8b67785c4a1b" ]
      responses:
        200:
          description: Partial success
          schema:
            $ref: '#/definitions/PartialSuccess'
        204:
          description: Successful response
        default:
          $ref: '#/responses/Error'

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

definitions:
  SecurityModeEnum:
    type: string
    enum: [INVALID, NONE, SIGN, SIGN_AND_ENCRYPT]
    description: Security mode used by the endpoint
    example: SIGN

  UserTokenTypeEnum:
    type: string
    enum: [ANONYMOUS, USERNAME, CERTIFICATE, ISSUEDTOKEN]
    description: User identity type
    example: USERNAME

  DatatypeEnum:
    type: string
    enum: [NONE, DOUBLE, INT, STRING, BOOLEAN, UINT64, DATE_TIME]
    description: Datatype of the SystemLink tag
    example: DOUBLE

  SessionStateEnum:
    type: string
    enum: [NOT_INITIALIZED, CONNECTED, RECONNECTING, STOPPED]
    description: State of the OPC UA session
    example: CONNECTED

  MonitoredItemStateEnum:
    type: string
    enum: [NO_TAG_EXISTS, MONITORING, PAUSED]
    description: Current state of the monitored node
    example: MONITORING

  MonitoredItemDirectionEnum:
    type: string
    enum: [READ, WRITE]
    description: Wether the monitored item is being read from OPC UA server or Systemlink is writing to OPC UA server
    default: READ
    example: READ

  SessionEndpointModel:
    type: object
    description: Information about the endpoint on OPC UA server
    properties:
      securityMode:
        $ref: '#/definitions/SecurityModeEnum'
      securityPolicy:
        type: string
        description: Security policy used by the endpoint
      certificateInfo:
        $ref: '#/definitions/SslCertificateInfoModel'
      supportedUserIdentities:
        description: List of user authentication schemes supported by the endpoint
        type: array
        items:
          $ref: '#/definitions/SessionUserToken'
    example:
        securityMode: "SIGN"
        securityPolicy: "Basic256"
        certificateInfo:
            id: null
            name: ""
            isCertificateTrusted: true
            issuerName: "CN=UaServerCpp@opcuaserver.com, OU=OPC UA, O=One-Way Automation, L=Edmonton, S=Alberta, C=CA, DC=opcuaserver.com"
            subjectName: "CN=UaServerCpp@opcuaserver.com, OU=OPC UA, O=One-Way Automation, L=Edmonton, S=Alberta, C=CA, DC=opcuaserver.com"
            thumbprint: "83A0C843ECC0D3EA7C858CC76D671DC14E2A2DE4"
            validFrom: "1/24/2018 5:29:36 PM"
            validTo: "1/23/2023 5:29:36 PM"
        supportedUserIdentities:
           - tokenType: "USERNAME"
             userTokenSecurityPolicy: "http://opcfoundation.org/UA/SecurityPolicy#Basic256"
           - tokenType: "ANONYMOUS"
             userTokenSecurityPolicy: null

  SslCertificateInfoModel:
    type: object
    description: Information about the SSL certificate
    properties:
      id:
        type: string
        description: unique id for this certificate. This can be null if the certificate is not yet saved on the SystemLink server
        example: "NI SystemLink OPC UA Connector [1FA889F76A1DEE5DAB2B5880CC6BFE248F12A8EB].der"
      name:
        type: string
        description: file name of the certificate. This can be empty if the certificate is not yet saved on the SystemLink server
        example: "NI SystemLink OPC UA Connector [1FA889F76A1DEE5DAB2B5880CC6BFE248F12A8EB].der"
      subjectName:
        type: string
        description: subject name in the certificate
        example: "CN=UaServerCpp@opcuaserver.com, OU=OPC UA, O=One-Way Automation, L=Edmonton, S=Alberta, C=CA, DC=opcuaserver.com"
      issuerName:
        type: string
        description: issuer name in the certificate
        example: "CN=UaServerCpp@opcuaserver.com, OU=OPC UA, O=One-Way Automation, L=Edmonton, S=Alberta, C=CA, DC=opcuaserver.com"
      validFrom:
        type: string
        description: time from this certificate is valid
        example: "1/24/2018 5:29:36 PM"
      validTo:
        type: string
        description: time till this certificate is valid
        example: "1/23/2023 5:29:36 PM"
      thumbprint:
        type: string
        description: thumbprint in the certificate
        example: "83A0C843ECC0D3EA7C858CC76D671DC14E2A2DE4"
      isCertificateTrusted:
        type: boolean
        description: 'true, if the certificate is trusted by the SystemLink server'
        example: true

  SessionUserToken:
    type: object
    description: Information about the user authentication token
    properties:
      tokenType:
        $ref: '#/definitions/UserTokenTypeEnum'
      userTokenSecurityPolicy:
        type: string
        description: Security policy to use when communicating the user identification information
        example: "http://opcfoundation.org/UA/SecurityPolicy#Basic256Sha256"

  NewSessionRequest:
    type: object
    description: Information about the new session to be created
    properties:
      name:
        type: string
        description: Name of the OPC UA session
        example: "opcuaserver.com-48010"
      url:
        type: string
        description: URL of the OPC UA server
        example: "opc.tcp://opcuaserver.com:48010"
      monitoringInterval:
        type: integer
        format: int32
        description: 'Publishing interval, in milliseconds, for monitoring nodes. Must be greater than or equal to 1000.'
        default: 10000
        example: 1000
      useDiscoveryCertificate:
        type: boolean
        description: 'If set to true, the SSL certificate provided by discovery server is used'
        example: true
      endpoint:
        $ref: '#/definitions/SelectedEndpointModel'
    required:
      - name
      - url
      - useDiscoveryCertificate
      - endpoint
    example:
        name: "opcuaserver.com-48010"
        url: "opc.tcp://opcuaserver.com:48010"
        monitoringInterval: 10000
        useDiscoveryCertificate: true
        endpoint:
            securityMode: "SIGN"
            securityPolicy: "Basic256"
            userTokenSecurityPolicy: "http://opcfoundation.org/UA/SecurityPolicy#Basic256"
            tokenType: "USERNAME"
            userName: "admin"
            password: "admin"
            x509CertificateData: []

  SelectedEndpointModel:
    type: object
    description: Information about the selected endpoint
    properties:
      securityMode:
        $ref: '#/definitions/SecurityModeEnum'
      securityPolicy:
        type: string
        description: Security policy used by the endpoint
        example: "Basic256"
      tokenType:
        $ref: '#/definitions/UserTokenTypeEnum'
      userTokenSecurityPolicy:
        type: string
        description: Security policy used by the endpoint for encrypting the user identification information
        default: ''
        example: "http://opcfoundation.org/UA/SecurityPolicy#Basic256"
      userName:
        type: string
        description: user name
        default: ''
        example: admin
      password:
        type: string
        description: password. Request objects should contain the actual password. Response objects will contain the encrypted password.
        default: ''
        example: admin
      x509CertificateData:
        type: string
        format: byte
        description: certificate to authenticate the user
        default: []
        example: []
    required:
      - securityMode
      - securityPolicy
      - tokenType

  UpdateSessionRequest:
    type: object
    description: Information about updating the existing session
    properties:
        sessionId:
            type: string
            description: session id
            example: 5c39017b236b8b67785c4a1b
        name:
            type: string
            description: New name
            example: "Renamed.opcuaserver.com-48010"
        monitoringInterval:
            type: integer
            description: 'New Publishing interval, in milliseconds, for monitoring nodes. Must be greater than or equal to 1000.'
            example: 5000
    required:
        - sessionId
        - name
        - monitoringInterval

  SessionResponse:
    type: object
    description: Information about the existing session
    properties:
      id:
        type: string
        description: session id
      name:
        type: string
        description: session name
      url:
        type: string
        description: OPC UA server url
      state:
        $ref: '#/definitions/SessionStateEnum'
      monitoringInterval:
        type: integer
        description: Publishing interval for monitoring nodes
      numberOfMonitoredItems:
        type: integer
        description: Number of monitored OPC UA node by the session
      useDiscoveryCertificate:
        type: boolean
        description: 'If set to true, then SSL certificate provided by discovery server is used'
      certificateInfo:
        $ref: '#/definitions/SslCertificateInfoModel'
      endpoint:
        $ref: '#/definitions/SelectedEndpointModel'
    example:
        id: "5c39017b236b8b67785c4a1b"
        name: "opcuaserver.com-48010"
        url: "opc.tcp://opcuaserver.com:48010"
        state: "CONNECTED"
        monitoringInterval: 10000
        numberOfMonitoredItems: 0
        useDiscoveryCertificate: true
        certificateInfo:
            id: null
            name: "18d48415-13a8-4867-9791-b7b7b4551de9.der"
            isCertificateTrusted: true
            issuerName: "CN=UaServerCpp@opcuaserver.com, OU=OPC UA, O=One-Way Automation, L=Edmonton, S=Alberta, C=CA, DC=opcuaserver.com"
            subjectName: "CN=UaServerCpp@opcuaserver.com, OU=OPC UA, O=One-Way Automation, L=Edmonton, S=Alberta, C=CA, DC=opcuaserver.com"
            thumbprint: "83A0C843ECC0D3EA7C858CC76D671DC14E2A2DE4"
            validFrom: "1/24/2018 5:29:36 PM"
            validTo: "1/23/2023 5:29:36 PM"
        endpoint:
            securityMode: "SIGN"
            securityPolicy: "Basic256"
            userTokenSecurityPolicy: "http://opcfoundation.org/UA/SecurityPolicy#Basic256"
            tokenType: "USERNAME"
            userName: "admin"
            password: "AQAAANCMnd8BFdERjHoBwE/Cl+sBAAAAYaA/LG/ktykZHp/tt6PfMAAAAAACAAAAAAAAwAAAABBBBBCZKwgu3/NIN5ScsQiBB4i+AAAAAASAAACgAAAAEBBBBH0QaMIJBh9ZnZLeHQSCZMoIAAAACkct5+OV1pgUAAAAL+ue1DKXQ+b3s1D19HT7716tmHY="
            x509CertificateData: []

  OpcNode:
    type: object
    description: Represntation of the node in the browse tree on SystemLink server
    properties:
      id:
        type: string
        description: NodeId of the node on the OPC UA server
        example: "i=87"
      displayName:
        type: string
        description: Display name of the node on the OPC UA server
        example: "Views"
      browsePath:
        type: string
        description: Browse path of the node on the OPC UA server
        example: "/Views"
      isLeaf:
        type: boolean
        description: If set to true then the node doesn't have any child nodes
        example: false
      opcNodes:
        type: array
        description: child nodes of the node
        items:
          $ref: '#/definitions/OpcNode'
        example:
            - browsePath: "/Views/3:AirConditionerView"
              displayName: "AirConditionerView"
              id: "ns=3;i=5000"
              isLeaf: false
              opcNodes: []
            - browsePath: "/Views/3:FurnaceView"
              displayName: "FurnaceView"
              id: "ns=3;i=5001"
              isLeaf: false
              opcNodes: []

  ReadAttributesResponse:
    type: object
    description: Response for the read attributes request
    properties:
      attributes:
        type: object
        description: OPC UA attributes
        additionalProperties:
          type: string
      isCompatibleForTag:
        type: boolean
        description: 'If set to true, a monitor can be created for this node'
    example:
        attributes:
            BrowseName: "3:AirConditionerView"
            ContainsNoLoops: "True"
            Description: "View containing the AirConditioner objects"
            DisplayName: "AirConditionerView"
            EventNotifier: "None"
            NodeClass: "View"
            NodeId: "ns=3;i=5000"
            UserWriteMask: "0"
            WriteMask: "0"
        isCompatibleForTag: false

  NewMonitoredItem:
    type: object
    description: Information to create a new monitored item
    properties:
      displayName:
        type: string
        description: Name of the SystemLink tag to be created for this monitored item
      opcNodeId:
        type: string
        description: OPC Node Id for the node on the OPC UA server
      direction:
        $ref: '#/definitions/MonitoredItemDirectionEnum'
      opcSamplingInterval:
        type: integer
        format: int32
        description: Sampling interval at which the OPC UA server should sample the values
        default: 0
      opcQueueSize:
        type: integer
        format: int32
        minimum: 0
        description: Queue size that the OPC server should reserve for this node
        default: 1000
    required:
      - displayName
      - opcNodeId
    example:
        displayname: "opc.opcuaserver.com-48010.Views.AirConditionerView.AirConditioner_1.Temperature"
        opcNodeId: "ns=3;s=AirConditioner_1.Temperature"
        direction: "Read"
        opcSamplingInterval: 1000
        opcQueueSize: 1000

  MonitoredItemResponse:
    type: object
    description: Information about the existing monitored item
    properties:
      id:
        type: string
        description: Unique id of the monitored item
      sessionId:
        type: string
        description: Session id of the session on which this node is being monitored
      dataType:
        $ref: '#/definitions/DatatypeEnum'
      displayName:
        type: string
        description: SystemLink tag name
      opcNodeId:
        type: string
        description: OPC Node Id for the node on the OPC UA server
      direction:
        $ref: '#/definitions/MonitoredItemDirectionEnum'
      opcSamplingInterval:
        type: integer
        description: Sampling interval at which the OPC UA server should sample the values
      opcQueueSize:
        type: integer
        description: Queue size that the OPC server should reserve for this node
      state:
        $ref: '#/definitions/MonitoredItemStateEnum'
    example:
        id: "6c3907c6236b8b67785c4a1c"
        sessionId: "5c39017b236b8b67785c4a1b"
        dataType: "DOUBLE"
        displayName: "opc.opcuaserver.com-48010.Views.AirConditionerView.AirConditioner_1.Temperature"
        opcNodeId: "ns=3;s=AirConditioner_1.Temperature"
        direction: "READ"
        opcSamplingInterval: 1000
        opcQueueSize: 1000
        state: "MONITORING"

  MonitoredItemDeleteData:
    type: object
    description: Information to delete the existing monitored item
    properties:
      id:
        type: string
        description: Id of the monitored item to be deleted
        example: 6c3907c6236b8b67785c4a1c
      removeTag:
        type: boolean
        description: 'If set to true, then the corresponding tag will be removed from the tag service'
        default: false
        example: false
    required:
      - id

  Error:
    description: Contains error information
    type: object
    properties:
      name:
        description: The string error code
        type: string
      code:
        description: Numeric error code
        type: integer
      resourceType:
        description: The type of resource associated with the error
        type: string
      resourceId:
        description: The identifier of the resource associated with the error
        type: string
      message:
        description: The filled in error message
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
        code: -251040
        message: One or more errors occurred. See the contained list for details of each error.
        args: []
        innerErrors:
          - name: OpcClientErrorCodes.ResourceNotFound
            code: -251608
            resourceId: 'zc39017b236b8b67785c4a1b'
            message: Resource with id 'zc39017b236b8b67785c4a1b' is not found.
            args: ['zc39017b236b8b67785c4a1b']

  PartialSuccess:
    description: Partial success response
    type: object
    properties:
      failed:
        type: array
        items:
          type: string
          example: zc39017b236b8b67785c4a1b
      error:
        $ref: '#/definitions/Error'

  Operation:
    description: An operation provided by the API
    type: object
    properties:
      available:
        type: boolean
        description: Whether the operation is available to the caller
      version:
        type: integer
        description: The version of the available operation
    required: [available]
    example:
      available: true
      version: 1

  V1Operations:
    description: V1 operations
    type: object
    properties:
      operations:
        description: >-
          Available operations in the v1 version of the API:

          - getSessions: The ability to retrieve the session

          - modifySessions: The ability to create/modify the sessions

          - deleteSessions: The ability to delete the sessions

          - getMonitoredItems: The ability to retrieve the monitored items

          - modifyMonitoredItems: The ability to create/modify the monitored items

          - deleteMonitoredItems: The ability to delete the monitored items

          - browseNodes: The ability to browse the nodes

          - readNode: The ability to read the attributes of OPC UA node

          - getCertificates: The ability to retrieve the existing certificates

          - uploadCertificates: The ability to upload the certificates

          - deleteCertificates: The ability to delete the certificates
        type: object
        additionalProperties:
          $ref: '#/definitions/Operation'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=package.json sha256=342b3ced8c15a215eaa90b1c7e43ac187ab23f43e57b4cdb604eb74f78cde3b6 bytes=684 -->
## FILE: package.json

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `package.json`
- sha256: `342b3ced8c15a215eaa90b1c7e43ac187ab23f43e57b4cdb604eb74f78cde3b6`
- bytes: 684

````json
{
  "name": "@ni-kismet/systemlink-openapi-documents",
  "version": "1.0.1",
  "description": "Package containing OpenAPI documents which describe some of the HTTP APIs provided by web services in SystemLink and SystemLink Cloud",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/ni/systemlink-OpenAPI-documents.git"
  },
  "author": "National Instruments",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/ni/systemlink-OpenAPI-documents/issues"
  },
  "homepage": "https://github.com/ni/systemlink-OpenAPI-documents#readme"
}
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=README.md sha256=9099391264f24694be6dfcbd083f1d818d58bdb20ce1efd2a90f03f74130b7a8 bytes=397 -->
## FILE: README.md

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `README.md`
- sha256: `9099391264f24694be6dfcbd083f1d818d58bdb20ce1efd2a90f03f74130b7a8`
- bytes: 397

````markdown
# SystemLink OpenAPI Documents

This repository contains OpenAPI documents which describe some of the HTTP APIs provided by web services in SystemLink and SystemLink Cloud.

## Using an OpenAPI document to generate a client

To generate a client from an OpenAPI document, paste the document into [editor.swagger.io](https://editor.swagger.io), click "Generate Client", and select a language.
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=repo/nirepo.yml sha256=8e297ba0f8221b436ad5c4a0d95a8003e2487a7f6859b7dc3fc9c9da6c116e74 bytes=70022 -->
## FILE: repo/nirepo.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `repo/nirepo.yml`
- sha256: `8e297ba0f8221b436ad5c4a0d95a8003e2487a7f6859b7dc3fc9c9da6c116e74`
- bytes: 70022

````yaml
swagger: '2.0'
info:
  version: "1"
  title: "Package Repository Service"
  description: "Manages a repository of packages"
  contact:
    name: NI
    url: https://www.ni.com/systemlink
    email: support@ni.com
basePath: "/nirepo"
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
  
x-ni-routing-key: Skyline.Repository

definitions:
  JobError:
    description: Contains error information about the job.
    type: object
    properties:
      name:
        type: string
        description: String error code.
        example: "Repository.CouldNotDownloadFeedIndexFile"
      message:
        type: string
        description: Complete error message.
        example: "Unable to download feed index file at URI 'http://download.ni.com/Packages'."
      args:
        type: array
        description: Array of arguments for the error.
        items:
          type: string
          description: Positional argument values for the error code.
          example: "http://download.ni.com/Packages"
      innerErrors:
        type: array
        description: Internal errors that occured in the service.
        items:
          $ref: '#/definitions/JobError'
  Job:
    description: A resource, such as a package or feed, created to track the status of asynchronous operations and redirect the user to the results of such operations when they complete.
    type: object
    properties:
      id:
        description: The unique ID of the job. Use this to get more information about the job as it runs.
        type: string
        example: 5c51be40781e2b0ad0b0108c
      operation:
        description: The type of the job that is going to be executeed.
        type: string
        enum:
          - CREATE_FEED
          - CLONE_FEED
          - REPLICATE_FEED
          - UPDATE_FEED
          - DELETE_FEED
          - IMPORT_FEEDS
          - REMOVE_PACKAGE_REFERENCES
          - DELETE_PACKAGE
          - ADD_PACKAGE_REFERENCES
          - UPLOAD_PACKAGE
          - CHECK_FOR_UPDATES
          - APPLY_UPDATES
          - CLEAN_FEED
          - REPLICATE_STORE_ITEM
          - IMPORT_STORE_ITEMS
          - IMPORT_PACKAGES
          - JOB_OPERATION_COUNT
        example: REPLICATE_FEED
      status:
        description: The state in which the job is in.
        type: string
        enum: [PENDING, RUNNING, SUCCEEDED, FAILED, COMPLETED_WITH_ERROR]
        example: FAILED
      error:
        $ref: '#/definitions/JobError'
      created:
        description: The date when the job was created.
        type: string
        format: date-time
        example: '2019-02-11T13:32:06.030958Z'
      resourceId:
        description: The ID of the feed or package which this job created or modified.
        type: string
        example: 58339eb8e0d6442db09f03f5
      resourceIds:
        type: array
        items:
          description: The ID of the feed or package which this job created or modified.
          type: string
          example: 58339eb8e0d6442db09f03f5
      returnType:
        description: The type of resource, such as a package or feed, that this job will return when completed.
        type: string
        enum: [FEED, FEEDS, PACKAGE, UPDATE_DESCRIPTORS, SIMPLE]
        example: FEED
  JobResponse:
    type: object
    description: Contains a single job.
    properties:
      job:
        $ref: '#/definitions/Job'
  JobsResponse:
    type: object
    description: Points to the location of a jobs array.
    properties:
      jobs:
        type: array
        items:
          $ref: '#/definitions/Job'
  JobIdsResponse:
    description: Points to the location of a job IDs array.
    type: object
    properties:
      jobIds:
        type: array
        items:
          type: string
          description: The ID of a single job.
          example: '5c66b6bd781e2b2ce42ca818'
  ErrorObject:
    description: Contains error information.
    type: object
    properties:
      name:
        description: String error code.
        type: string
        example: Repository.StoreApiException
      code:
        description: Numeric error code.
        type: integer
        example: -251340
      message:
        description: Complete error message.
        type: string
        example: "Unable to download feed index file at URI 'http://download.ni.com/Packages'."
      args:
        description: Positional argument values for the error code.
        type: array
        items:
          type: string
          example: "http://download.ni.com/Packages"
      innerErrors:
        type: array
        description: Internal errors that occured in the service.
        items:
          $ref: '#/definitions/ErrorObject'
  Error:
    description: Contains error information.
    type: object
    properties:
      error:
        $ref: '#/definitions/ErrorObject'
  Platform:
    type: string
    enum: [windows, ni-linux-rt]
    description: "Depending on the selected platform, the following package extensions are available: .nipkg for windows feeds, .ipk and .deb for ni-linux-rt feeds."
    example: windows
  PackageImportDescriptor:
    type: object
    description: A defined list of packages that need to be imported into the feed from a remote feed.
    properties:
      architecture:
        description: The architecture of the package.
        type: string
        example: x64
      description:
        description: The description of the package.
        type: string
        example: "LabVIEW Runtime (32-bit) Resource contains support for non-English languages to display in dialog boxes, menus, and error messages that are part of the LabVIEW Runtime."
      feedUri:
        description: The path to the feed.
        type: string
        example: "https://download.ni.com/support/nipkg/products/ni-l/ni-labview-nxg-3.0.0/6.4/released-critical"
      packageName:
        description: The package name.
        type: string
        example: "ni-labview-2015-runtime-engine-resource"
      packageUri:
        description: The path to the package.
        type: string
        example: "/nirepo/v1/files/packages/ni-labview-2015-runtime-engine-resource_15.6.0.49152-0+f0_windows_all.nipkg"
      version:
        description: The package version.
        type: string
        example: "15.6.0.49152-0+f0"
  PackageImportDescriptors:
    type: object
    description: Points to the location of a package importer array.
    properties:
      packageImportDescriptors:
        description: An array containing objects which describe the packages in the remote feed.
        type: array
        items:
          $ref: '#/definitions/PackageImportDescriptor'
  ArchitectureInformation:
    type: object
    description: An object defining the architecture the software can run on.
    properties:
      id:
        type: string
        description: The ID of this element.
        example: "1"
      value:
        type: string
        description: The architecture that this package can run on.
        example: "64-bit"
  LanguageInformation:
    type: object
    description: Contains information about the supported locale of the product.
    properties:
      id:
        type: string
        description: The ID of this element.
        example: "2"
      value:
        type: string
        description: The language the product supports.
        example: English
  SoftwareInformation:
    type: object
    description: Contains information about a piece of software that a store item contains.
    properties:
      storeItemId:
        type: string
        description: The ID of this element.
        example: "654"
      productName:
        type: string
        description: The name of one the products contained in the software suite.
        example: LabVIEW NXG
      shortDescription:
        type: string
        description: A short description of the product.
        example: LabVIEW NXG enables engineers to quickly automate hardware, customize tests to project specifications, and easily view measurement results from anywhere.
      downloadItemVersion:
        type: string
        description: The item version number.
        example: "2.1"
      packageName:
        type: string
        description: The name of the package to install.
        example: ni-labview-nxg-2.0.0
      packageVersion:
        type: string
        description: The version of the package to install.
        example: 5.3.1.49156-0+f4
      feeds:
        type: array
        description: The feeds where the suite contents are located at.
        items:
          $ref: '#/definitions/FeedNameAndUri'
  StoreItemInstaller:
    type: object
    properties:
      guid:
        type: string
        description: The global unique identifier (GUID) of the store item.
        example: LABVIEWPKGBLDR10
      bitnesses:
        type: array
        description: An array containing information about the possible architectures the software can run on.
        items:
          $ref: '#/definitions/ArchitectureInformation'
      languages:
        type: array
        description: An array containing objects that offer information about the supported locale of the product.
        items:
          $ref: '#/definitions/LanguageInformation'
      suiteContents:
        type: array
        description: Array of descriptions about what this store item contains.
        items:
          $ref: '#/definitions/SoftwareInformation'
      feeds:
        type: array
        description: The feeds where the suite contents are located at.
        items:
          $ref: '#/definitions/FeedNameAndUri'
  StoreDownloadItems:
    type: object
    properties:
      downloadItemVersion:
        type: string
        example: '1.2.3'
        description: The version of the download item.
      productVersionedId:
        type: string
        example: 'LVNXG210SUITE'
        description: The ID of the product.
      storeItemInstallers:
        type: array
        items:
          $ref: '#/definitions/StoreItemInstaller'
  UpdateDescriptor:
    type: object
    description: Data specifying what to update.
    properties:
      packageName:
        type: string
        example: ni-svcloc
        description: The name of the package.
      operation:
        type: string
        enum:
          - ADD
          - UPGRADE
        default: ADD
        example: UPGRADE
        description: The operation type.
      fromVersion:
        type: string
        example: 17.0.0.7-0+d7
        description: The old version of the package.
      toVersion:
        type: string
        example: 17.0.0.8-0+d8
        description: The new version of the package.
      packageUri:
        type: string
        example: path/to/package
        description: The path to the package.
      packageId:
        type: string
        example: 5de11fd6a47a402c643e4b62
        description: The unique ID of the package.
      packageToReplace:
        type: string
        example: 58339eb8e0d6442db09f03f5
        description: The ID of the package which will replace another package.
      destinationFeedId:
        type: string
        description: The ID of the feed which will be modified.
        example: 58339eb7e0d6442db09f03ec
      isLocal:
        type: boolean
        description: Whether it is local or remote.
        example: false
  FeedBasicData:
    type: object
    description: |
        Only one of the 'name' and 'feedName' properties is requested.
        There are both 'name' and 'feedName' for backwards compatibility.
        The 'feedName' parameter will be considered if both of them are provided.
    properties:
      feedName:
        type: string
        description: Name of the feed.
        example: My LabVIEW feed
      name:
        type: string
        description: Name of the feed.
        example: My LabVIEW feed
      description:
        type: string
        description: A short description of the feed.
        example: Feed containing all the necessary packages for configuring LabVIEW 2015
      workspace:
        type: string
        description: The workspace's id where the feed belongs to
        example: 3651818c-9b31-4d25-8b35-0afc4e305f2d
  FeedData:
    type: object
    description: |
        Only one of the 'name' and 'feedName' properties is requested.
        There are both 'name' and 'feedName' for backwards compatibility.
        The 'feedName' parameter will be considered if both of them are provided.
    properties:
      feedName:
        type: string
        description: The name of this feed.
        example: My LabVIEW feed
      name:
        type: string
        description: The name of this feed.
        example: My LabVIEW feed
      description:
        type: string
        description: A short description of the feed.
        example: Feed containing all the necessary packages for configuring LabVIEW 2015
      platform:
        $ref: '#/definitions/Platform'
      workspace:
        type: string
        description: The workspace's id where the feed belongs to
        example: 3651818c-9b31-4d25-8b35-0afc4e305f2d
  FeedDataWithURI:
    type: object
    description: |
        Only one of the 'name' and 'feedName' properties is requested.
        There are both 'name' and 'feedName' for backwards compatibility.
        The 'feedName' parameter will be considered if both of them are provided.
    properties:
      feedName:
        type: string
        description: The name of this feed.
        example: My LabVIEW feed
      name:
        type: string
        description: The name of the feed.
        example: My LabVIEW feed
      description:
        type: string
        description: A short description of the feed.
        example: Feed containing all the necessary packages for configuring LabVIEW 2015
      platform:
        $ref: '#/definitions/Platform'
      workspace:
        type: string
        description: The workspace's id where the feed belongs to
        example: 3651818c-9b31-4d25-8b35-0afc4e305f2d
      uri:
        type: string
        description: 'The path of the feed to replicate. Appending /Packages to the URI should yield the "Packages" file of the feed.'
        example: "https://download.ni.com/support/nipkg/products/ni-l/ni-labview-nxg-3.0.0/6.4/released-critical"
  FeedUrisAndIds:
    type: object
    description: Contains the list of URIs and the list of IDs for a group of feeds.
    properties:
      feedUris:
        type: array
        items:
          type: string
          description: The URI of a single feed.
          example: "https://download.ni.com/support/nipkg/products/ni-l/ni-labview-nxg-3.0.0/6.4/released-critical"
      feedIds:
        type: array
        items:
          type: string
          description: The ID of a single feed.
          example: 5c62bf36781e2b1c7c57daf4
  FeedUriObject:
    type: object
    description: Contains the URI of a single feed.
    properties:
      feedUri:
        type: string
        example: /path/to/feed
        description: The URI of a feed.
  FeedNameAndUri:
    type: object
    description: |
        Only one of the 'name' and 'feedName' properties is requested.
        There are both 'name' and 'feedName' for backwards compatibility.
        The 'feedName' parameter will be considered if both of them are provided.
    properties:
      feedName:
        type: string
        description: The name of the feed. Feed names must begin with an alphabetical character and contain only alphanumeric characters, spaces, underscores, and hyphens.
        example: "SystemLink 19.0"
      name:
        type: string
        description: The name of this feed.
        example: My LabVIEW feed
      uri:
        type: string
        description: The path to the feed.
        example: "https://download.ni.com/support/nipkg/products/ni-l/ni-labview-nxg-3.0.0/6.4/released-critical"
      
  StoreItemRequest:
    type: object
    description: |
        Only one of the 'name' and 'feedName' properties is requested.
        There are both 'name' and 'feedName' for backwards compatibility.
        The 'feedName' parameter will be considered if both of them are provided.
    properties:
      storeItemId:
        type: string
        description: The ID of the store item to replicate.
        example: '468'
      downloadItemVersion:
        type: string
        description: The version of the store item to replicate.
        example: '1.0'
      storeItemInstallerGuid:
        type: string
        description: Value uniquely identifying the specific store item installer to replicate.
        example: LABVIEWPKGBLDR10
      feedName:
        type: string
        description: If "split" is false, the name of the feed which will be created. If "split" is true, this field is ignored.
        example: My LabVIEW feed
      name:
        type: string
        description: The name of this feed.
        example: My LabVIEW feed
      description:
        type: string
        description: If "split" is false, the description of the feed which will be created. If "split" is true, this field is ignored.
        example: Feed containing all the necessary packages for configuring LabVIEW 2015
      workspace:
        type: string
        description: The workspace's id where the feed belongs to
        example: 3651818c-9b31-4d25-8b35-0afc4e305f2d
  StoreItem:
    type: object
    properties:
      id:
        type: string
        description: The ID of the store item.
        example: 1.0
      storeItemName:
        type: string
        description: The name of the store item.
        example: LabVIEW Package Builder
      shortDescription:
        type: string
        example: LabVIEW Package Builder adds NI Package creation capabilities to LabVIEW Application Builder.
        description: The short description of the store item.
      longDescription:
        type: string
        example: LabVIEW Package Builder enables LabVIEW users to create Packages by adding a new Build Specification option in Application Builder. Packages provide a standard container for the distribution of executables, VIs, libraries, and other supporting files. LabVIEW must be installed prior to installing LabVIEW Package Builder.
        description: The long description of the store item.
      iconUri:
        type: string
        example: 'http://s7d5.scene7.com/is/image/ni/Generic_NI?$ni-icon-pm$'
        description: The icon location of the store item.
      isSuite:
        type: boolean
        example: false
        description: Whether this store item is a suite.
      downloadItems:
        type: array
        items:
          $ref: '#/definitions/StoreDownloadItems'
  StoreItemsExtendedResponse:
    type: object
    description: Contains a list of StoreItem elements together with the coresponding paging information.
    properties:
      items:
        type: array
        items:
          $ref: '#/definitions/StoreItem'
      pageSize:
        description: The number of the records contained by one page. Maximum is 1000.
        type: integer
        example: 100
      pageNumber:
        description: The number of the current page.
        type: integer
        example: 5
      totalPages:
        description: The total number of pages.
        type: integer
        example: 20
      totalItems:
        description: The total number of items.
        type: integer
        example: 1975
  StoreItemResponse:
    type: object
    description: Contains a single StoreItem.
    properties:
      storeItem:
        $ref: '#/definitions/StoreItem'
  StoreItemDescriptor:
    type: object
    properties:
      storeItemId:
        type: string
        description: The ID of the store item to replicate.
        example: '1.0'
      downloadItemVersion:
        type: string
        description: The version of the store item to replicate.
        example: '1.0'
      storeItemInstallerGuid:
        type: string
        description: Value uniquely identifying the specific store item installer to replicate.
        example: LABVIEWPKGBLDR10
  StoreItemDescriptorsObject:
    type: object
    description:  An array of objects which describe which specific store items to replicate.
    properties:
      storeItemDescriptors:
        type: array
        items:
          $ref: '#/definitions/StoreItemDescriptor'
  UpdateDescriptorRequest:
    type: object
    description: An array of update descriptors.
    properties:
      updateDescriptors:
        type: array
        items:
          $ref: '#/definitions/UpdateDescriptor'
  Feed:
    description: |
        Only one of the 'name' and 'feedName' properties is requested.
        There are both 'name' and 'feedName' for backwards compatibility.
        The 'feedName' parameter will be considered if both of them are provided.
    type: object
    properties:
      id:
        type: string
        description: The unique ID of this feed.
        example: "5c4f13c3781e2b17101f8220"
      feedName: 
        type: string
        description: The name of this feed.
        example: My LabVIEW feed
      name:
        type: string
        description: The name of this feed.
        example: My LabVIEW feed
      directoryUri: 
        type: string
        description: The location of this feed.
        example: "/nirepo/v1/files/feeds/asd"
      description: 
        type: string
        description: The description of this feed.
        example: Feed that contains all the necessary packages for configuring LabVIEW 2015
      platform:
        $ref: '#/definitions/Platform'
      workspace:
        type: string
        description: The workspace's id where the feed belongs to
        example: 3651818c-9b31-4d25-8b35-0afc4e305f2d
      packageReferences:
        type: array
        description: An array containing the IDs of the packages in this feed.
        items:
          type: string
          description: The ID of a package.
          example: "5c652e1f781e2b05cc4d589e"
      packageSources:
        type: array
        description: IDs and/or external URIs of package sources
        items:
          description: The source of a package.
          type: string
          example: https://download.ni.com/support/nipkg/products/idne/idnet-ad/17.5/released
      lastUpdated:
        type: string
        description: The date this feed was last updated at.
        format: date-time
        example: '2019-02-11T13:32:06.030958Z'
      ready:
        type: boolean
        description: If the job that creates this feed is complete.
        example: true
  Unauthorized:
    type: string
    description: A not authorized response from a web log in page.
    example: Web Page with login information.
  Feeds:
    description: An object containing an array of feeds.
    type: object
    properties:
      feeds:
        description: An array of feeds.
        type: array
        items:
          $ref: '#/definitions/Feed'
  FeedObject:
    description: Contains a feed.
    type: object
    properties:
      feed:
        $ref: '#/definitions/Feed'
  JobID:
    description: An object containing the Job ID.
    type: object
    properties:
      jobId:
        description: The ID of the job that was created for tracking the status of the operation.
        type: string
        example: "5c666def781e2b2f64208709"
  PackageMetadata:
    type: object
    description: Information about the metadata of this package.
    properties:
      packageName:
        type: string
        description: The name of the package.
        example: "ni-securityupdate-kb67l8lcqw-killbits"
      version:
        type: string
        description: The version of the package.
        example: "2.0.0.22-0+d22"
      architecture:
        type: string
        description: The architecture of the package.
        example: windows_x64
      breaks:
        type: array
        description: An array containing information about other packages this package breaks.
        items:
          type: string
          description: The name of a package that this package breaks. This also contains information about the version of the package.
          example: "ni-sysapi (>= 18.0.0)"
      conflicts:
        type: array
        description: An array containing information about other packages this package conflicts with.
        items:
          type: string
          description: The name of a package that this package conflicts with. This also contains information about the version of the package.
          example: "ni-msvcrt-2015 (>= 14.1.4)"
      depends:
        type: array
        description: An array containing information about other packages this package depends on.
        items:
          type: string
          description: The name of a package that this package depends on. This also contains information about the version of the package.
          example: "ni-metauninstaller (>= 18.0.1)"
      description:
        type: string
        description: The description of the package.
        example: This is an infrastructure package for NI Software.
      enhances:
        type: array
        description: An array containing information about other packages this package enhances.
        items:
          type: string
          description: The name of a package that this package enhances. This also contains information about the version of the package.
          example: "ni-msiproperties (>= 18.0.1)"
      essential:
        type: boolean
        description: Whether this package is essential.
        example: true
      fileName:
        type: string
        description: |
            The location of the file, including the file extension.
            Depending on the selected platform, the following package extensions are available: .nipkg for windows feeds, .ipk and .deb for ni-linux-rt feeds.
        example: ni-securityupdate-kb67l8lcqw-killbits_2.0.0.22-0+d22_windows_x64.nipkg
      homepage:
        type: string
        description: The website of the maintainers for this package.
        example: "http://www.ni.com"
      installedSize:
        type: integer
        description: The size of this package after install.
        example: 0
      maintainer:
        type: string
        description: The maintainer of this package.
        example: "NI <support@ni.com>"
      predepends:
        type: array
        description: An array containing information about other packages this package predepends.
        items:
          description: The name of a package that this package predepends. This also contains information about the version of the package.
          type: string
          example: "ni-teststand-2017-tools (>= 17.0.0)"
      priority:
        type: integer
        description: The priority of the package.
        example: 4
      provides:
        type: array
        description: An array containing information about other packages that this package provides.
        items:
          type: string
          example: "ni-curl (= 17.0.0.49152-0+f0)"
          description: One of the packages that the containing package provides. This also contains information about the version of the package.
      recommends:
        type: array
        description: An array containing information about other packages this package recommends.
        items:
          type: string
          description: The name of a package that this package recommends. This also contains information about the version of the package.
          example: "ni-systemlink-client-2018.5-realtime-bin (>= 18.5.0)"
      releaseNotes:
        type: string
        description: A page containing the release notes of the package.
        example: Refer to the NI website at http://www.ni.com/r/slrm185 for installation instructions, known issues, bug fixes, compatibility information, and other important notices about this product.
      replaces:
        type: array
        description: An array containing information about other packages this package replaces.
        items:
          type: string
          description: The name of a package that this package replaces. This also contains information about the version of the package.
          example: "b235b862-6a92-4a04-a8b2-6d71f777de67 (< 16.99.65535)"
      section:
        type: string
        description: The section of the package.
        example: Infrastructure
      size:
        type: integer
        description: The size of the package in bytes.
        example: 750070
      source:
        type: string
        description: The source of this package, if any.
        example: "thunar-archive-plugin_0.3.1.bb"
      suggests:
        type: array
        description: An array containing information about other packages this package suggests.
        items:
          type: string
          description: The name of a package that this package suggests. This also contains information about the version of the package.
          example: "ni-systemlink-client-2018.5-realtime-bin (>= 18.5.0)"
      tags:
        type: string
        description: Tags of the package.
        example: "KillBits, Security Update 2013"
      attributes:
        type: object
        description: Attributes of the package.
        example:
          Architecture: windows_x64
          Description: An infrastructure package for NI Software.
          Filename: 71e47fbf-2782-4c10-873e-dba414213dc9.nipkg
          Homepage: http://www.ni.com
          MD5Sum: 672a667ca32b6915ae9a968c55f80825
          Maintainer: NI <support@ni.com>
          Package: ni-securityupdate-kb67l8lcqw-killbits
          Priority: standard
          Section: Infrastructure
          Size: '750070'
          Version: 2.0.0.22-0+d22
          XB-DisplayName: NI Security Update (KB 67L8LCQW)
          XB-DisplayVersion: 2.0.0
          XB-LanguageSupport: en
          XB-Plugin: wininst
          XB-Tags: KillBits, Security Update 2013
          FileName: ni-securityupdate-kb67l8lcqw-killbits_2.0.0.22-0+d22_windows_x64.nipkg
  Package:
    description: A single package.
    type: object
    properties:
      id: 
        type: string
        description: The ID of this package. This is used to reference this package in the service.
        example: "581a6818e0d644f7f0c1902c"
      fileUri: 
        type: string
        description: The location of the file for this package.
        example: "files/packages/ni-securityupdate-kb67l8lcqw-killbits_2.0.0.22-0+d22_windows_x64.nipkg"
      feedReferences:
        type: array
        description: An array containing the IDs of the feeds which reference this package.
        items:
          type: string
          description: A reference to the feed that contains this package.
          example: "581a6818e0d644f7f0c19028"
      lastUpdated:
        type: string
        description: The date this package was last updated.
        format: date-time
        example: '2019-02-11T13:32:06.030958Z'
      metadata: 
        $ref: '#/definitions/PackageMetadata'
  PackageResponse:
    description: Contains a single package.
    type: object
    properties:
      package:
        $ref: '#/definitions/Package'
  Packages:
    description: An object containing an array of packages.
    type: object
    properties:
      packages:
        description: An array of packages.
        type: array
        items:
          $ref: '#/definitions/Package'
  PackageReferencesObject:
    type: object
    description: Points to the location of a package references array.
    properties:
      packageReferences:
        type: array
        items:
          type: string
          description: The reference of a package.
          example: 5c62bf36781e2b1c7c57daf4
  PackageSourcesObject:
    type: object
    description: Points to the location of a package sources array.
    properties:
      packageSources:
        description: IDs and/or external URIs of package sources
        type: array
        items:
          description: The source of a package.
          type: string
          example: https://nuget.org/api/v2/
  UpdateDescriptorsResponse:
    type: object
    description: Object containing an array of update descriptors.
    properties:
      updateDescriptors:
        description: An array of update descriptors.
        type: array
        items:
          $ref: '#/definitions/UpdateDescriptor'
    
responses:
  JobIdResponse:
    description: Response with a JobID in it. This is the usual result after executing a write operation.
    headers:
      Location:
        type: string
        description: Contains the relative URI of the job that was created for tracking the status of the operation. Execute a GET against this URI to get information about the status of the operation.
    schema:
      $ref: '#/definitions/JobID'

paths:
  /v1/ping:
    get:
      operationId: Ping
      x-ni-operation: ping
      tags: [ping]
      summary: Ping the service
      description: Return if the service is up.
      responses:
        204:
          description: The service is up.
        302:
          description: The user does not have the required privilege.
        404:
          description: Service is down.
        500:
          description: The request encountered an error.
        default:
          $ref: '#/definitions/Error'
  /v1/files/{pathToFile}:
    parameters:
      - in: path
        name: pathToFile
        description: The path to the file to download.
        type: string
        required: true
        x-example: "filePath"
    get:
      operationId: DownloadFiles
      x-ni-operation: getResource
      x-ni-route-type: Static
      x-ni-static-download: true
      x-ni-static-alias: /files
      tags: [files]
      summary: Download files located in Package Repository
      description: Download files located in Package Repository.
      produces:
        - application/octet-stream
      responses:
        200:
          description: The request has succeeded.
          schema:
            type: file
        404:
          description: File not found.
        default:
          $ref: '#/definitions/Error'
  /v1/feeds:
    get:
      operationId: ListFeeds
      x-ni-auth: true
      x-ni-operation: getFeeds
      tags: [feeds]
      summary: List all feeds
      description: Returns a JSON array of all the feeds in the service.
      parameters:
        - in: query
          name: omitPackageReferences
          type: boolean
          default: false
          description: Whether the "packageReferences" array for each feed, which contains the IDs of all of the packages in that feed, should be omitted.
      responses:
        200:
          description: The request has succeeded.
          schema:
            $ref: '#/definitions/Feeds'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
    post:
      operationId: CreateFeed
      x-ni-auth: true
      x-ni-operation: createFeed
      tags: [feeds]
      summary: Create a feed
      description: Asynchronously creates a feed. Returns the ID of a resource which can be queried to determine the status of the operation.
      parameters:
        - in: body
          name: feedData
          schema:
            $ref: '#/definitions/FeedData'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    get:
      operationId: GetFeed
      x-ni-auth: true
      x-ni-operation: getFeeds
      tags: [feeds]
      summary: Get feed
      description: Returns a JSON representation of a feed.
      responses:
        200:
          description: The request has succeeded.
          schema:
            $ref: '#/definitions/FeedObject'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
    delete:
      operationId: DeleteFeed
      x-ni-auth: true
      x-ni-operation: deleteFeeds
      tags: [feeds]
      summary: Remove a feed
      description: Asynchronously removes a feed. Returns the ID of a resource which can be queried to determine the status of the operation.
      parameters:
        - in: query
          name: deleteUnreferencedPackages
          type: boolean
          description: Whether the packages in the feed that are no longer referenced will be deleted. If true, they will be deleted.
          default: true
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/clone:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    post:
      operationId: CloneFeed
      x-ni-auth: true
      x-ni-operation: cloneFeed
      tags: [feeds]
      summary: Clone a feed
      description: Asynchronously clones a feed. Returns the ID of a resource which can be queried to determine the status of the operation.
      parameters:
        - in: body
          name: feedRequestData
          schema:
            $ref: '#/definitions/FeedBasicData'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/packages:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    get:
      operationId: ListFeedPackages
      x-ni-auth: true
      x-ni-operation: getPackages
      tags: [feeds, packages]
      summary: Get all packages in a feed
      description: Gets all of the packages in the service's package pool.
      parameters:
        - in: query
          name: omitAttributes
          type: boolean
          description: Whether the "Attributes" dictionary for the packages will be omitted. If true, they will be omitted.
          default: false
        - in: query
          name: omitFeedReferences
          type: boolean
          description: Whether the array of feed reference will be omitted from each package. If true, they will be omitted.
          default: false
      responses:
        200:
          description: The request has succeeded.
          schema:
            $ref: '#/definitions/Packages'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/replicate-feed:
    post:
      operationId: ReplicateFeed
      x-ni-auth: true
      x-ni-operation: replicateFeed
      tags: [feeds]
      summary: Replicate a feed
      description: Asynchronously replicates a feed. Returns the ID of a resource which can be queried to determine the status of the operation.
      parameters:
        - in: query
          name: shouldOverwrite
          type: boolean
          description: A query parameter that determines if existing packages with the same filename as a package to be added to the pool should be overwritten.
          default: false
        - in: query
          name: ignoreImportErrors
          type: boolean
          description: A query parameter that determines whether the service should abort the request if errors occur while importing some packages. If true, the service will abort and roll back the request if an error occurs while importing a package. If false, the service will import as many packages as it can, and return an error describing which packages could not be imported.
          default: false
        - in: body
          name: feedRequest
          schema:
            $ref: '#/definitions/FeedDataWithURI'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/import-packages:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    post:
      operationId: ImportPackages
      x-ni-auth: true
      x-ni-operation: importPackages
      tags: [feeds, packages]
      summary: Import packages into a feed
      description: Import packages into a feed.
      parameters:
        - in: query
          name: shouldOverwrite
          type: boolean
          description: A query parameter that determines if existing packages with the same filename as a package to be added to the pool should be overwritten.
          default: false
        - in: query
          name: ignoreImportErrors
          type: boolean
          description: A query parameter that determines whether the service should abort the request if errors occur while importing some packages. If true, the service will abort and roll back the request if an error occurs while importing a package. If false, the service will import as many packages as it can, and return an error describing which packages could not be imported.
          default: false
        - in: body
          name: feedRequest
          schema:
            $ref: '#/definitions/PackageImportDescriptors'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/import-feeds:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    post:
      operationId: ImportFeedsAlternative
      x-ni-auth: true
      x-ni-operation: importFeeds
      tags: [feeds]
      summary: Import feeds into an existing feed
      description: Asynchronously imports feeds into an existing feed. Returns the ID of a resource which can be queried to track the status of the operation. Same as /v1/feeds/{id}/import.
      parameters:
        - in: query
          name: shouldCleanSourceFeeds
          type: boolean
          description: A value indicating whether only the most recent version of every package in the source feed should be added to the destination feed. If true, only the most recent version of each package will be added. If false, all versions of each package will be added.
          default: true
        - in: query
          name: shouldOverwrite
          type: boolean
          description: A query parameter that determines if existing packages with the same filename as a package to be added to the pool should be overwritten.
          default: false
        - in: query
          name: ignoreImportErrors
          type: boolean
          description: A query parameter that determines whether the service should abort the request if errors occur while importing some packages. If true, the service will abort and roll back the request if an error occurs while importing a package. If false, the service will import as many packages as it can, and return an error describing which packages could not be imported.
          default: false
        - in: body
          name: feedUris
          description: An array containing the URIs of remote feeds whose packages should be added to the destination feed. Appending /Packages to each URI should yield the "Packages" file for that feed.
          schema:
            $ref: '#/definitions/FeedUrisAndIds'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/packages:
    get:
      operationId: ListPackages
      x-ni-auth: true
      x-ni-operation: getPackages
      tags: [packages]
      summary: Get all packages
      description: Gets all of the packages in the service's package pool.
      parameters:
        - in: query
          name: omitAttributes
          type: boolean
          description: If true, the "Attributes" dictionary for the package will be omitted.
          default: false
        - in: query
          name: omitFeedReferences
          type: boolean
          description: If true, the array of feed references will be omitted from each package.
          default: false
        - in: query
          name: returnUnreferencedOnly
          type: boolean
          description: A query parameter that determines if only packages without referencing feeds should be returned.
          default: false
      responses:
        200:
          description: The request has succeeded.
          schema:
            $ref: '#/definitions/Packages'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/packages/{packageId}:
    parameters:
      - in: path
        name: packageId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    get:
      operationId: GetPackage
      x-ni-auth: true
      x-ni-operation: getPackages
      tags: [packages]
      summary: Get package details
      description: Get package details.
      responses:
        200:
          description: |
            The request has succeeded. - The requested Package object. Not all of the fields on package objects will be available depending on the package.
            Not all fields will have content because not all packages will store this information.
            Do not rely on all of these fields being available in any application as some may be null, empty, or nonexistent.
            However, key properties such as _id, name, owners, and FileName will never be null.
          schema:
            $ref: '#/definitions/PackageResponse'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
    delete:
      operationId: DeletePackage
      x-ni-auth: true
      x-ni-operation: deletePackage
      tags: [packages]
      summary: Remove a package
      description: Remove a package. The package will be removed from all of the feeds that reference it, potentially creating feeds with unsatisfied dependencies.
      parameters:
        - in: query
          name: autoRemoveReferences
          type: boolean
          description: If true, the "References" will be automatically removed.
          default: false
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/upload-packages:
    post:
      operationId: UploadPackage
      x-ni-auth: true
      x-ni-operation: uploadPackage
      tags: [packages]
      summary: Upload packages to the pool
      description: Asynchronously uploads packages to the service's package pool. Returns an array of IDs of resources which can be queried to track the status of each upload operation.
      consumes:
        - multipart/form-data
      parameters:
        - in: query
          name: shouldOverwrite
          type: boolean
          description: A query parameter that determines if existing packages with the same filename as a package to be added to the pool should be overwritten.
          default: false
        - in: formData 
          name: filename
          type: file
          required: true
          description: The name of this parameter is the name of the file that will be uploaded. If the uploaded file is test.ipkg, put instead of filename that name.
        - in: header
          name: X-File-Name
          type: string
          required: false
        - in: header
          name: X-File-Size
          type: string
          required: false
        - in: header
          name: X-File-Type
          type: string
          required: false
      responses:
        202:
          description: The request has succeeded.
          headers:
            Location:
              type: string
              description: Contains the relative URI of the job that was created for tracking the status of the operation. Execute GET against this URI to get information about the status of the operation.
          schema:
            $ref: '#/definitions/JobIdsResponse'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/get-package-import-descriptors:
    post:
      operationId: ObtainPackageImportDescriptorsFromFeedUri
      x-ni-auth: true
      x-ni-operation: getPackageImportDescriptors
      tags: [packages]
      summary: Returns the package import descriptors from the specified feed URI
      description: Returns a list of PackageImportDescriptor objects based on the specified feed URI.
      parameters:
        - in: body
          name: feedUri
          schema:
            $ref: '#/definitions/FeedUriObject'
      responses:
        200:
          description: The request has succeeded.
          schema:
            $ref: '#/definitions/PackageImportDescriptors'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/metadata:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    put:
      operationId: UpdateFeed
      x-ni-auth: true
      x-ni-operation: getFeedMetadata
      tags: [feeds]
      summary: Update a feed's name and/or description and/or workspace
      description: Asynchronously updates a feed's name and/or description and/or workspace. Returns the ID of a resource which can be queried to determine the status of the operation.
      parameters:
        - in: body
          name: updateData
          schema:
            $ref: '#/definitions/FeedBasicData'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/add-package-references:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    post:
      operationId: AddPackageReferences
      x-ni-auth: true
      x-ni-operation: addPackageReferences
      tags: [feeds, packages]
      summary: Add package references to feed
      description: Asynchronously adds packages to a feed. Returns the ID of a resource which can be queried to determine the status of the operation.
      parameters:
        - in: body
          name: packageReferences
          description: Array of IDs of the packages that are going to be added to the feed.
          schema:
            $ref: '#/definitions/PackageReferencesObject'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/remove-package-references:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    post:
      operationId: RemovePackageReferences
      x-ni-auth: true
      x-ni-operation: removePackageReferences
      tags: [feeds, packages]
      summary: Remove package references
      description: Remove package references.
      parameters:
        - in: query
          name: deleteIfLastReference
          type: boolean
          description: A value indicating whether any packages that are no longer referenced after being removed from the feeds should be deleted.
          default: true
        - in: body
          name: packageReferences
          description: An array of package IDs to be removed from the feeds.
          schema:
            $ref: '#/definitions/PackageReferencesObject'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/import:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    post:
      operationId: ImportFeeds
      x-ni-auth: true
      x-ni-operation: importFeeds
      tags: [feeds]
      summary: Import feeds into an existing feed
      description: Asynchronously imports feeds into an existing feed. Returns the ID of a resource which can be queried to track the status of the operation.
      parameters:
        - in: query
          name: shouldCleanSourceFeeds
          type: boolean
          description: A value indicating whether only the most recent version of every package in the source feed should be added to the destination feed. If true, only the most recent version of each package will be added. If false, all versions of each package will be added.
          default: true
        - in: query
          name: shouldOverwrite
          type: boolean
          description: A query parameter that determines if existing packages with the same filename as a package to be added to the pool should be overwritten.
          default: false
        - in: query
          name: ignoreImportErrors
          type: boolean
          description: A query parameter that determines whether the service should abort the request if errors occur while importing some packages. If true, the service will abort and roll back the request if an error occurs while importing a package. If false, the service will import as many packages as it can, and return an error describing which packages could not be imported.
          default: false
        - in: body
          name: feeds
          description: An array containing the URIs of remote feeds whose packages should be added to the destination feed. Appending /Packages to each URI should yield the "Packages" file for that feed.
          schema:
            $ref: '#/definitions/FeedUrisAndIds'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/update-check:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    post:
      operationId: CheckForUpdates
      x-ni-auth: true
      x-ni-operation: checkForUpdates
      tags: [feeds]
      summary: Check for updates to a feed
      description: Asynchronously checks for updates to a feed, based on the latest versions of the packages available in the package sources for that feed. Offers to upgrade packages in the feed to the latest version available, as well as add any new packages to the feed if new packages were added to the package sources. Returns the ID of a resource which can be queried to determine the status of the operation. Upon completion, the resource redirects to an array of UpdateDescriptor objects, describing the updates available for the feed. Any routes that are not intended to be applied can be removed, and then send the modified array to the "Apply updates to a feed" route below.
      parameters:
        - in: body
          name: packageSources
          description: An optional array of the IDs and/or external URIs of package sources which should be queried for updates. If not given, all of the feed's package sources will be checked. Package sources that are not present in the feed's array of package sources will be ignored. Import route can be used for adding additional package sources.
          schema:
            $ref: '#/definitions/PackageSourcesObject'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/update-apply:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    post:
      operationId: ApplyUpdates
      x-ni-auth: true
      x-ni-operation: applyUpdates
      tags: [feeds]
      summary: Apply updates
      description: Asynchronously applies a set of updates to a feed. Returns the ID of a resource which can be queried to determine the status of the operation. Upon completion, the resource redirects to the modified feed.
      parameters:
        - in: query
          name: shouldOverwrite
          type: boolean
          description: A query parameter that determines if existing packages with the same filename as a package to be added to the pool should be overwritten.
          default: false
        - in: query
          name: ignoreImportErrors
          type: boolean
          description: A query parameter that determines whether the service should abort the request if errors occur while importing some packages. If true, the service will abort and roll back the request if an error occurs while importing a package. If false, the service will import as many packages as it can, and return an error describing which packages could not be imported.
          default: false
        - in: body
          name: updateDescriptors
          description: An array containing the update descriptors that should be applied to the feed. Update descriptors should be obtained from a call to the "Check for updates to a feed" route, detailed above. You can remove any update descriptors returned from the "Check for updates" route, but modifying them in any other way is not supported.
          schema:
            $ref: '#/definitions/UpdateDescriptorRequest'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/clean:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    post:
      operationId: CleanFeed
      x-ni-auth: true
      x-ni-operation: cleanFeed
      tags: [feeds]
      summary: Clean a feed
      description: Asynchronously cleans a feed by removing all but the most recent version of every package in the feed. Returns the ID of a resource which can be queried to track the status of the operation. Upon completion, the resource redirects to the modified feed.
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/feeds/{feedId}/import-store-items:
    parameters:
      - in: path
        name: feedId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    post:
      operationId: ImportStoreItems
      x-ni-auth: true
      x-ni-operation: importStoreItems
      tags: [feeds, store]
      summary: Import store items
      description: Route for importing one or more store items into an existing feed.
      parameters:
        - in: query
          name: shouldOverwrite
          type: boolean
          description: Determines if the existing packages with the same filename as the package to be added to the pool should be overwritten.
          default: false
        - in: body
          name: storeItemDescriptors
          schema:
            $ref: '#/definitions/StoreItemDescriptorsObject'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/jobs:
    get:
      operationId: ListJobs
      x-ni-auth: true
      x-ni-operation: listJobs
      tags: [jobs]
      summary: List all jobs
      description: Gets all jobs in the service. See the entry for "Get job details" route for more information about jobs.
      parameters:
        - in: query
          name: id
          type: string
          required: false
          description: A comma-delimited list of job IDs.
        - in: query
          name: operation
          type: string
          required: false
          description: A comma-delimited list of operations.
        - in: query
          name: status
          type: string
          required: false
          description: A comma-delimited list of statuses.
        - in: query
          name: resourceId
          type: string
          required: false
          description: A comma-delimited list of resource IDs.
      responses:
        200:
          description: The request has succeeded.
          schema:
            $ref: '#/definitions/JobsResponse'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/jobs/{jobId}:
    parameters:
      - in: path
        name: jobId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    get:
      operationId: GetJob
      x-ni-auth: true
      x-ni-operation: getJobs
      tags: [jobs]
      summary: Get job details
      description: Gets a job with a specific identifier.
      responses:
        200:
          description: The request has succeeded. - If the job has not completed.
          headers:
            Location:
              type: string
              description: Contains the relative URI of the job that was created for tracking the status of the operation. Execute a GET against this URI to get information about the status of the operation.
          schema:
              $ref: '#/definitions/JobResponse'
        303:
          description: If the job has completed, see Other with the Location header set to the URI of the created or modified resource.
          headers:
            Location:
              type: string
              description: Contains the relative URI of the job that was created for tracking the status of the operation. Execute a GET against this URI to get information about the status of the operation.
          schema:
              $ref: '#/definitions/JobResponse'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/can-write:
    get:
      operationId: CheckWritePermission
      x-ni-auth: true
      x-ni-operation: canWrite
      tags: [misc]
      summary: Check if the logged user can write
      description: Check if the logged user can write.
      responses:
        200:
          description: The request has succeeded.
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/updates/{updateDescriptorListId}:
    parameters:
      - in: path
        name: updateDescriptorListId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    get:
      operationId: GetUpdateDescriptors
      x-ni-auth: true
      x-ni-operation: getUpdateDescriptors
      tags: [updates]
      summary: Retrieve updates for a feed
      description: Retrieve updates for a feed.
      responses:
        200:
          description: The request has succeeded.
          schema:
            $ref: '#/definitions/UpdateDescriptorsResponse'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/store/items:
    get:
      operationId: QueryStoreItems
      x-ni-auth: true
      x-ni-operation: getStoreItems
      tags: [store]
      summary: Query store items
      description: Route for querying for store items.
      parameters:
        - in: query
          name: query
          type: string
          description: A search string. E.g., "labview".
          default: ""
        - in: query
          name: pageSize
          type: integer
          description: How many results should be returned in the response.
          default: 10
        - in: query
          name: pageNumber
          type: integer
          description: The page of the response to return.
          default: 0
      responses:
        200:
          description: The request has succeeded.
          schema:
            $ref: '#/definitions/StoreItemsExtendedResponse'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/store/items/{storeItemId}:
    parameters:
      - in: path
        name: storeItemId
        description: The ID of this resource.
        type: string
        required: true
        x-example: "5c5d49f2781e2b2cd045267b"
    get:
      operationId: GetStoreItem
      x-ni-auth: true
      x-ni-operation: getStoreItems
      tags: [store]
      summary: Get a store item
      description: Route for getting an individual store item.
      responses:
        200:
          description: The request has succeeded.
          schema:
            $ref: '#/definitions/StoreItemResponse'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
  /v1/replicate-store-item:
    post:
      operationId: ReplicateStoreItem
      x-ni-auth: true
      x-ni-operation: replicateStoreItem
      tags: [store]
      summary: Replicate a store item
      description: Route for replicating a store item into either a single feed, or a separate feed for each feed within the store item.
      parameters:
        - in: query
          name: shouldOverwrite
          type: boolean
          description: A query parameter that determines if existing packages with the same filename as a package to be added to the pool should be overwritten.
          default: false
        - in: query
          name: split
          type: boolean
          description: A query parameter that determines if the store item should be merged into one feed, or if each feed in the store item should be copied into a separate feed.
          default: false
        - in: body
          name: feedRequest
          schema:
            $ref: '#/definitions/StoreItemRequest'
      responses:
        202:
          $ref: '#/responses/JobIdResponse'
        400:
          $ref: '#/definitions/Error'
        401:
          $ref: '#/definitions/Unauthorized'
        default:
          $ref: '#/definitions/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=service-registry/niserviceregistry.yml sha256=6005318e6f39d0d976799fc52cff6c8021d15cf145cf084940c9ccf382aca8a3 bytes=3446 -->
## FILE: service-registry/niserviceregistry.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `service-registry/niserviceregistry.yml`
- sha256: `6005318e6f39d0d976799fc52cff6c8021d15cf145cf084940c9ccf382aca8a3`
- bytes: 3446

````yaml
swagger: '2.0'
info:
  version: '1'
  title: Service Registry Web Service
  description: View information about installed SystemLink services
  contact:
    name: NI
    url: 'https://www.ni.com/systemlink'
    email: support@ni.com
basePath: /niserviceregistry
consumes:
  - application/json
produces:
  - application/json
definitions:
  Statement:
    description: Contains information about a statement
    type: object
    properties:
      actions:
        description: Contains information about actions that can be performed
        type: array
        items:
          type: string
        example: ['asset:*']
      type:
        description: Contains information about the resource type for which the statement applies
        type: string
        example: "asset"
  Translation:
    description: Contains translation information for a permission configuration
    type: object
    properties:
      en-us:
        description: The united states english permission name translation
        type: string
        example: "All"
      zn-ch:
        description: The traditional chinese permission name translation
        type: string
        example: "所有"
      de:
        description: The german permission name translation
        type: string
        example: "Alle"
      ja:
        description: The japanese permission name translation
        type: string
        example: "すべて"
  Permission:
    description: Contains information about a installed permission
    type: object
    properties:
      id:
        description: The ID of the permission
        type: string
        example: "1242342"
      translation:
        $ref: '#/definitions/Translation'
      statements:
        type: array
        items:
          $ref: '#/definitions/Statement'
  Privilege:
    description: Contains information about a installed privilege
    type: object
    properties:
      id:
        description: The ID of the privilege
        type: string
        example: "12314121"
      show:
        description: Specifies whether this privilege is user visible
        type: boolean
        example: true
      showResource:
        description: Specifies whether the resource specificity to be shown
        type: boolean
        example: false
      permissions:
        type: array
        items:
          $ref: '#/definitions/Permission'
responses:
  PrivilegeResponse:
    description: Response containing a list of installed privileges
    schema:
      description: Response containing a list of installed privileges
      title: Privilege Response
      type: object
      required:
        - privileges
      properties:
        privileges:
          description: Array of installed privilege information
          type: array
          items:
            $ref: '#/definitions/Privilege'
  Unauthorized:
    description: Not authorized
    headers:
      WWW_Authenticate:
        description: Information for how to authenticate
        type: string
paths:
  /v1/privileges:
    get:
      tags: [privileges]
      summary: Get installed SystemLink privilege configuration
      description: Gets information about installed privileges
      operationId: get-privileges
      responses:
        200:
          $ref: '#/responses/PrivilegeResponse'
        401:
          $ref: '#/responses/Unauthorized'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=systems-management/nisysmgmt.yml sha256=b6d581443382fb840b08e25b84bd8d598247cc2fbcea76165e005a52deec5408 bytes=90089 -->
## FILE: systems-management/nisysmgmt.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `systems-management/nisysmgmt.yml`
- sha256: `b6d581443382fb840b08e25b84bd8d598247cc2fbcea76165e005a52deec5408`
- bytes: 90089

````yaml
swagger: '2.0'
info:
  description: 'Systems Management Service HTTP API. Manage and monitor your distributed systems.'
  version: '1'
  title: 'SystemLink Systems Management'
  contact:
    name: NI
    url: https://www.ni.com/systemlink
    email: support@ni.com
basePath: '/nisysmgmt'
x-ni-routing-key: 'Skyline.Salt'
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

  BadRequest:
    description: Bad Request indicates that the server was unable to process the request because of invalid syntax.
    schema:
      title: Bad Request Error Response
      description: Bad request error response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

  Unauthorized:
    description: Not authorized.
    headers:
      WWW_Authenticate:
        description: Information for how to authenticate.
        type: string

  PartialSuccess:
    description: Partial Success indicates only part of the request body metadata information was processed successfully.
    schema:
      title: PartialSuccessResponse
      description: Partial success response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

  NotFound:
    description: The requested resource was not found.
    schema:
      title: Not Found Request Error Response
      description: Not found error response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
  
  ServerNotActivated:
    description: The server is not activated.
    schema:
      title: Server Not Activated Error Response
      description: Server not activated response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

definitions:
  CreateJobRequest:
    description: Request describing a job to send to systems.
    title: Create Job Request
    type: object
    x-ni-cs-json-converter: JsonObjectConverter
    properties:
      tgt:
        description: Array of strings representing system IDs.
        type: array
        items:
          type: string
          example: VMware_Virtual_Platform--SN-VMware-56_4d_30_26_4f_c9_5c_05-b7_68_d1_cd_99_6e_22_16--MAC-02-01-02-03-04-08
      fun:
        description: An array of strings each representing an execution module function.
        type: array
        items:
          type: string
          example: pkg.remove
        example:
          - pkg.remove
          - pkg.install
      arg:
        description: An array of variable type element arrays, which are arguments to the function specified by the "fun" property. If at least one function requires arguments, an array must be provided for each function, even if it is empty. Keyword arguments may be provided as a parameter of type object with at least one property of type boolean ("__kwarg__") that evaluates to true.
        type: array
        items:
          type: array
          items:
            type: object
            example: true
          example:
            - __kwarg__: true
              pkgs:
              - acl: ''
        example:
          - - __kwarg__: true
              pkgs:
              - acl: ''
          - - __kwarg__: true
              pkgs:
              - acl-dbg: 1.0.0-0
      metadata:
        description: Additional information of the job.
        type: object
        additionalProperties:
          type: object
        example:
          queued: true
          timeout: 600
          refresh_minion_cache:
            grains: true
    required: [tgt, fun]

  CreateJobResponse:
    title: Create Job Response
    description: Response describing a job sent to systems.
    type: object
    properties:
      jid:
        description: The ID of the created job.
        type: string
        example: '20190211135234448026_28320'
      tgt:
        description: Array of strings representing system IDs.
        type: array
        items:
          type: string
          example: VMware_Virtual_Platform--SN-VMware-56_4d_30_26_4f_c9_5c_05-b7_68_d1_cd_99_6e_22_16--MAC-02-01-02-03-04-08
      fun:
        description: An array of strings each representing an execution module function.
        type: array
        items:
          type: string
          example: pkg.remove
        example:
          - pkg.remove
          - pkg.install
      arg:
        description: An array of arrays of variable type elements that are arguments to the function specified by the "fun" property. If at least one function requires arguments, an array must be provided for each function, even if it is empty. Keyword arguments may be provided as a parameter of type object with at least one property of type boolean, "__kwarg__", that is evaluated to true.
        type: array
        items:
          type: array
          items:
            type: object
            example: true
          example:
            - __kwarg__: true
              pkgs:
              - acl: ''
        example:
          - - __kwarg__: true
              pkgs:
              - acl: ''
          - - __kwarg__: true
              pkgs:
              - acl-dbg: 1.0.0-0
      metadata:
        description: Additional information passed along with the job.
        type: object
        additionalProperties:
          type: object
        example:
          queued: true
          timeout: 600
          refresh_minion_cache:
            grains: true
      error:
        $ref: '#/definitions/Error'
    required: [jid, tgt, fun]

  RegisterSystemsRequest:
    description: Request for registering systems.
    title: Register Systems Request
    type: object
    properties:
      systemsCredentials:
        description: An array of objects representing system credentials.
        type: array
        items:
          $ref: '#/definitions/SystemCredentials'
      activate:
        type: boolean
        description: Whether to activate the systems or not.
        default: false
        example: true
      workspaces:
        description: List containing the corresponding workspace for each system credential information.
        type: array
        items:
          type: string
          description: The ID of the workspace.
          example: '5bc5e9092a4fa4c71cfa7197'
    required: [systemsCredentials]

  SystemCredentials:
    description: The hostname, IP address, and login information of a system.
    title: System Credentials
    type: object
    properties:
      hostname:
        type: string
        description: Required if ip_address is not provided. A string representing the hostname of the system to register.
        example: testvm
      ipAddress:
        type: string
        description: Required if hostname is not provided. A string representing the IP address of the system to register.
        example: 10.10.10.10
      password:
        type: string
        description: A string representing the password to use access the system.
        example: test
      username:
        type: string
        description: A string representing the username to use access the system.
        example: root

  RegisterSystemsResponse:
    title: Register Systems Response
    description: Response to a request to register systems to the server.
    type: object
    properties:
      requestId:
        description: The ID of the registration request.
        type: string
        example: '068530b9-b059-4c0e-9820-9e9cc4e0832c'
      error:
        $ref: '#/definitions/Error'
    required: [requestId]

  UnregisterSystemsRequest:
    title: Unregister Systems Request
    description: Request to unregister systems from the server.
    type: object
    properties:
      tgt:
        description: Array of strings representing the IDs of systems to remove from SystemLink Server.
        type: array
        items:
          type: string
          example: VMware_Virtual_Platform--SN-VMware-56_4d_30_26_4f_c9_5c_05-b7_68_d1_cd_99_6e_22_16--MAC-02-01-02-03-04-08
      force:
        description: A Boolean which specifies whether to remove systems from the database immediately (True) or wait until the unregister job returns from systems (False). If True, unregister job failures are not cached.
        type: boolean
        default: true
        example: false
    required: [tgt]

  UnregisterSystemsResponse:
    title: Unregister Systems Response
    description: Response of the request to unregister systems.
    type: object
    properties:
      jid:
        description: The job ID of the unregistration job sent to connected systems.
        type: string
        example: '20190211135234448026_28320'
      removedIds:
        description: An array of system IDs removed from the database immediately.
        type: array
        items:
          type: string
          example: VMware_Virtual_Platform--SN-VMware-56_4d_30_26_4f_c9_5c_05-b7_68_d1_cd_99_6e_22_16--MAC-02-01-02-03-04-08
      failedIds:
        description: An array of objects defining failed unregister operations.
        type: array
        items:
          type: object
          title: Failed Unregister Request
          properties:
            id:
              description: The ID of the system on which unregister operation failed.
              type: string
              example: VMware_Virtual_Platform--SN-VMware-56_4d_30_26_4f_c9_5c_05-b7_68_d1_cd_99_6e_22_16--MAC-02-01-02-03-04-08
            error:
              $ref: '#/definitions/Error'

  CancelJobRequest:
    description: Object containing the job ID and system ID.
    title: Cancel Job Request
    type: object
    properties:
      jid:
        description: The job ID of the job to cancel.
        type: string
        example: '20190211135234448026_28320'
      systemId:
        description: The system ID on which the job is canceled.
        type: string
        example: VMware_Virtual_Platform--SN-VMware-56_4d_d2_08_ce_89_1b_70-e6_32_fc_21_6c_d0_d9_f9--MAC-00-0C-29-D0-D9-F9
    required: [jid, systemId]

  ManagedSystemsSummary:
    title: Managed Systems Summary
    description: Summary information about managed systems.
    type: object
    properties:
      connectedCount:
        type: integer
        format: int64
        description: Number of the connected systems.
        example: 4
      disconnectedCount:
        type: integer
        format: int64
        description: Number of the disconnected systems.
        example: 2
    required: [connectedCount, disconnectedCount]

  JobsSummary:
    title: Jobs Summary
    description: Summary information about jobs.
    type: object
    properties:
      activeCount:
        type: integer
        format: int64
        description: Number of active jobs.
        example: 4
      failedCount:
        type: integer
        format: int64
        description: Number of failed jobs.
        example: 2
      succeededCount:
        type: integer
        format: int64
        description: Number of succeeded jobs.
        example: 4
    required: [activeCount, failedCount, succeededCount]

  DiscoveredSystemsSummary:
    title: Discovered Systems Summary
    description: Summary information about discovered systems.
    type: object
    properties:
      discoveredCount:
        type: integer
        format: int64
        description: Number of systems that are discovered and not managed by your SystemLink Server.
        example: 100
    required: [discoveredCount]

  PendingSystemsSummary:
    title: Pending Systems Summary
    description: Summary information about the systems attempting to connect to the server but aren't accepted yet.
    type: object
    properties:
      pendingCount:
        type: integer
        format: int64
        description: Number of systems pending approval to connect to the server.
        example: 5
    required: [pendingCount]

  SystemInfo:
    title: System Information
    description: Network published information about a system.
    type: object
    properties:
      comments:
        description: System description.
        type: string
        example: Test system
      cpuArch:
        description: System CPU architecture.
        type: string
        example: armv7l
      deviceClass:
        description: System device class.
        type: string
        example: FlexRIO
      hostname:
        description: System hostname.
        type: string
        example: testvm
      ipAddress:
        description: System IP address.
        type: string
        example: 10.10.10.10
      lastUpdatedTimestamp:
        description: Last updated timestamp.
        type: string
        format: date-time
        example: '2019-02-11T13:32:06.030958Z'
      master:
        description: Master of the system.
        type: string
        example: SystemLinkServer
      minionId:
        description: Salt minion_id of the system.
        type: string
        example: NI-7935R--SN-1111111--MAC-00-12-34-56-78-90
      modelName:
        description: System model name.
        type: string
        example: NI-7935R
      modelNumber:
        description: System model number.
        type: string
        example: 0x77AC
      osFamily:
        description: System OS family.
        type: string
        example: NILinuxRT
      osRelease:
        description: System OS release.
        type: string
        example: 7.0
      serialNumber:
        description: System serial number.
        type: string
        example: 1111111
      vendorName:
        description: System vendor name.
        type: string
        example: NI
      version:
        description: Salt version.
        type: string
        example: 2018.3.0-541-g76c6845
    required: [comments, cpuArch, deviceClass, hostname, ipAddress, lastUpdatedTimestamp, master, minionId, modelName, modelNumber, osFamily, osRelease, serialNumber, vendorName, version]

  JobState:
    title: Job State
    type: string
    enum:
      - CANCELED
      - FAILED
      - SUCCEEDED
      - INQUEUE
      - INPROGRESS
    example: SUCCEEDED
    description: >
      The state of the job.
       * CANCELED: The job was canceled by the user.
       * FAILED: The job completed with failures. The job fails if at least one of the its functions executing fails.
       * SUCCEEDED: The job completed successfully.
       * INQUEUE: The job is in queue, waiting to be dispatched to the system.
       * INPROGRESS: The job was dispatched to the system and is still running.

  Job:
    description: Information about a job.
    title: Job
    type: object
    properties:
      jid:
        type: string
        description: ID of the job.
        example: '20190211135234448026_28320'
      id:
        type: string
        description: ID of the system.
        example: VMware_Virtual_Platform--SN-VMware-56_4d_70_f1_81_06_04_3b-55_19_2a_87_f6_41_20_e5--MAC-00-0C-29-41-20-E5
      createdTimestamp:
        type: string
        format: date-time
        description: The date when the job was created.
        example: '2019-02-11T13:32:06.030958Z'
      lastUpdatedTimestamp:
        type: string
        format: date-time
        description: The date when the job was last updated.
        example: '2019-02-11T13:32:06.030958Z'
      dispatchedTimestamp:
        type: string
        format: date-time
        description: The date when the job was actually sent to the system.
        example: '2019-02-11T13:32:06.030958Z'
      state:
        $ref: '#/definitions/JobState'
      metadata:
        description: Job metadata.
        type: object
        additionalProperties:
          type: object
        example:
          queued: true
      config:
        type: object
        description: Job configuration.
        title: JobConfig
        properties:
          user:
            type: string
            description: User who created the job.
            example: admin
          tgt:
            type: array
            items:
              type: string
              description: String representing the system ID.
              example: VMware_Virtual_Platform--SN-VMware-56_4d_70_f1_81_06_04_3b-55_19_2a_87_f6_41_20_e5--MAC-00-0C-29-41-20-E5
          fun:
            type: array
            description: An array of strings each representing an execution module function.
            items:
              type: string
              example: system.set_computer_desc
            example:
              - system.set_computer_desc
              - nisysmgmt.grains_items
          arg:
            description: An array of arrays of variable type elements that are arguments to the function specified by the "fun" property. If at least one function requires arguments, an array must be provided for each function, even if it is empty. Keyword arguments may be provided as a parameter of type object with at least one property of type boolean, "__kwarg__", that is evaluated to true.
            type: array
            items:
              type: array
              items:
                type: object
                example: true
              example:
                - test
        required: [user, tgt, fun]
      result:
        description: The result of job execution.
        type: object
        title: Job Result
        properties:
          return:
            type: array
            items:
              type: object
              example: 'Computer Description: test'
            description: An array of objects representing return values for each executed function.
            example:
              - Computer Description: test
              - null
          retcode:
            type: array
            items:
              type: integer
              format: int32
              example: 1
            description: An array of integers representing code values for each executed function.
            example:
              - 0
              - 0
          success:
            type: array
            items:
              type: boolean
              example: false
            description: An array of booleans representing success values for each executed function.
            example:
              - true
              - true
        required: [success]
    required: [jid, id, createdTimestamp, lastUpdatedTimestamp, state, config]

  ManagedSystemState:
    title: Managed System State
    type: string
    enum:
      - ACTIVATED_WITHOUT_CONNECTION
      - APPROVED
      - DISCONNECTED
      - CONNECTED_REFRESH_PENDING
      - CONNECTED
      - CONNECTED_REFRESH_FAILED
    example: CONNECTED
    description: >
      The connection state of a system.
       * ACTIVATED_WITHOUT_CONNECTION: The system is activated but the connection is not established yet.
       * APPROVED: The system is approved but it didn't try to connect yet.
       * DISCONNECTED: The system is disconnected.
       * CONNECTED_REFRESH_PENDING: The system is connected and the refresh job is running. A refresh job is sent to the system every time the connection is established in order to gather the system information.
       * CONNECTED: The system is connected. The refresh job completed successfully.
       * CONNECTED_REFRESH_FAILED: The system is connected but the refresh job failed.

  ManagedSystemActivationData:
    description: Information about the license of a system.
    type: object
    properties:
      activated:
        type: boolean
        description: Whether the system is activated or not.
        example: true
      licenseName:
        type: string
        description: The name of the license.
        example: NILicense
      licenseVersion:
        type: string
        description: The license version.
        example: 19.0
    required: [activated]

  ManagedSystemSysApiData:
    description: Contains the SysAPI information.
    type: object
    properties:
      lastUpdatedTimestamp:
        description: Last updated timestamp.
        type: string
        format: date-time
        example: '2019-02-11T13:32:06.030958Z'
      data:
        description: The lists of SysAPI property-bags.
        type: array
        items:
          description: >
            A property-bag tend to look like
            {
              resource_uri = <str>,
              [
                {
                  type = <str>,
                  tag = <int64>,
                  value = <str>
                }
              ]
            }
          type: object
    required: [lastUpdatedTimestamp, data]

  ManagedSystemDataPropertyMap:
    description: Property of a system composed by the last updated timestamp and a dictionary with the actual data.
    type: object
    properties:
      lastUpdatedTimestamp:
        description: Last updated timestamp.
        type: string
        format: date-time
        example: '2019-02-11T13:32:06.030958Z'
      data:
        description: This map is used for grains/feeds. All these are heterogeneous (integers, booleans, lists, dictionaries, ...) collections containing open-ended properties and flags.
        type: object
        additionalProperties:
          type: object
        example:
          key: value
    required: [lastUpdatedTimestamp, data]

  ManagedSystemPackagesData:
    description: Property of a system composed by the last updated timestamp and a dictionary with the actual packages installed on the system.
    type: object
    properties:
      lastUpdatedTimestamp:
        description: Last updated timestamp.
        type: string
        format: date-time
        example: '2019-02-11T13:32:06.030958Z'
      data:
        description: Installed packages. The key of the dictionary is the name of the package, and the value is a dictionary with open-ended properties and flags
        type: object
        additionalProperties:
          type: object
          additionalProperties:
            type: object
        example:
          key: value
    required: [lastUpdatedTimestamp, data]

  ManagedSystem:
    description: Information about a managed system.
    title: Managed System
    type: object
    properties:
      id:
        type: string
        description: The ID of the system.
        example: VMware_Virtual_Platform--SN-VMware-56_4d_d2_08_ce_89_1b_70-e6_32_fc_21_6c_d0_d9_f9--MAC-00-0C-29-D0-D9-F9
      createdTimestamp:
        description: The time when the system was registered.
        type: string
        format: date-time
        example: '2019-02-19T11:42:25.078Z'
      lastUpdatedTimestamp:
        description: Last time when the system information updated.
        type: string
        format: date-time
        example: '2019-02-19T11:42:25.078Z'
      alias:
        description: The alias of the system.
        type: string
        example: testVM
      workspace:
        type: string
        description: The ID of the workspace.
        example: '5bc5e9092a4fa4c71cfa7197'
      activation:
        description: Activation information.
        type: object
        properties:
          lastUpdatedTimestamp:
            description: Last time when the system activation information updated.
            type: string
            format: date-time
            example: '2019-02-19T11:42:25.078Z'
          data:
            $ref: '#/definitions/ManagedSystemActivationData'
        required: [lastUpdatedTimestamp, data]
      connected:
        description: System connection status information.
        type: object
        properties:
          lastUpdatedTimestamp:
            description: Last time when the system connection information updated.
            type: string
            format: date-time
            example: '2019-02-19T11:42:25.078Z'
          data:
            type: object
            properties:
              state:
                $ref: '#/definitions/ManagedSystemState'
            required: [state]
        required: [lastUpdatedTimestamp, data]
      grains:
        description: General information about the system.
        $ref: '#/definitions/ManagedSystemDataPropertyMap'
        example:
          lastUpdatedTimestamp: '2019-02-19T11:42:25.078Z'
          data:
            kernel: Windows
            nodename: WIN-8NTJI2568QV
            kernelrelease: 6.1.7601
            kernelversion: 6.1.7601
            cpuarch: x86
            os: Windows
            os_family: Windows
            mem_total: 1023
            osversion: 6.1.7601
            osrelease: 7
      packages:
        description: Software packages installed on the system.
        $ref: '#/definitions/ManagedSystemPackagesData'
        example:
          lastUpdatedTimestamp: '2019-02-19T11:42:25.078Z'
          data:
            ni-package-manager-upgrader:
              description: Application used to upgrade the package manager.
              displayname: NI Package Manager Upgrader
              displayversion: 19.5.0
              url: http://www.ni.com
              packager: NI <support@ni.com>
              priority: required
              group: Infrastructure
              version: 19.5.0.28-0+d28
            system-windows-x64:
              description: Package that indicates the current system is running a 64-bit Windows operating system.
              displayname: System Package for 64-Bit Windows OS
              displayversion: 19.5.0
              url: http://www.ni.com
              packager: NI <support@ni.com>
              priority: standard
              group: Infrastructure
              version: 19.5.0.28-0+d28
      feeds:
        description: Feeds configured on the system.
        $ref: '#/definitions/ManagedSystemDataPropertyMap'
        example:
          lastUpdatedTimestamp: '2019-02-19T11:42:25.078Z'
          data:
            http://download.ni.com/support/nipkg/products/ni-package-manager/released:
            - configurable: false
              enabled: true
              name: ni-package-manager-released
              uri: http://download.ni.com/support/nipkg/products/ni-package-manager/released
            http://download.ni.com/support/nipkg/products/ni-package-manager/eulas:
            - configurable: false
              enabled: true
              name: ni-package-manager-eulas
              uri: http://download.ni.com/support/nipkg/products/ni-package-manager/eulas
      sysapi:
        description: System API information.
        $ref: '#/definitions/ManagedSystemSysApiData'
        example:
          lastUpdatedTimestamp: '2019-02-19T11:42:25.078Z'
          data:
            - resource_uri: nisyscfg//sys/bus/pci/devices/0000:04:00.0
              properties:
              - type: string
                tag: 16777216
                value: "//localhost/nisyscfg/%2Fsys%2Fbus%2Fpci%2Fdevices%2F0000:04:00.0"
              - type: bool
                tag: 16781312
                value: true
            - resource_uri: nisyscfg/enp0s25
              properties:
              - type: string
                tag: 16777216
                value: "//localhost/nisyscfg/enp0s25"
              - type: bool
                tag: 16781312
                value: false
      groups:
        description: Specifies the groups to which the system is assigned.
        type: object
        properties:
          lastUpdatedTimestamp:
            description: Last updated timestamp.
            type: string
            format: date-time
            example: '2019-02-19T11:42:25.078Z'
          data:
            description: A list of strings defining metadata information about a system.
            type: array
            items:
              type: string
              example: Lab1
        required: [lastUpdatedTimestamp, data]
      keywords:
        description: Keywords metadata information about a system.
        type: object
        properties:
          lastUpdatedTimestamp:
            description: Last updated timestamp.
            type: string
            format: date-time
            example: '2019-02-19T11:42:25.078Z'
          data:
            description: A list of strings defining metadata information about a system.
            type: array
            items:
              type: string
              example: testVM
        required: [lastUpdatedTimestamp, data]
      properties:
        description: Properties metadata information about a system.
        type: object
        properties:
          lastUpdatedTimestamp:
            description: Last updated timestamp.
            type: string
            format: date-time
            example: '2019-02-19T11:42:25.078Z'
          data:
            description: An object defining key-value pairs metadata information about a system.
            type: object
            additionalProperties:
              type: string
            example:
              owner: admin
        required: [lastUpdatedTimestamp, data]
    required: [id, createdTimestamp, lastUpdatedTimestamp, connected, workspace]

  ReportType:
    title: Report Type
    type: string
    enum:
      - SOFTWARE
      - HARDWARE
    example: SOFTWARE
    description: >
      The type of the report to be created.
       * SOFTWARE: The report will contain the installed software packages.
       * HARDWARE: The report will contain information about the hardware configuration of the system.

  SystemsReportRequest:
    description: Request containing the report type followed by a query filter that will be applied on systems.
    title: Systems Report Request
    type: object
    properties:
      type:
        $ref: '#/definitions/ReportType'
      filter:
        type: string
        example: grains.data.os=="NILinuxRT"
        description: Specifies the filter criteria for systems.
    required: [ids, type]

  CreateGroupRequest:
    title: Create Group Request
    description: Request to create groups.
    type: object
    properties:
      systems:
        type: array
        items:
          type: string
          description: A string representing a system ID to be associated with this group.
          example: VMware_Virtual_Platform--SN-VMware-56_4d_70_f1_81_06_04_3b-55_19_2a_87_f6_41_20_e5--MAC-00-0C-29-41-20-E5
      name:
        type: string
        description: A string of the group name to create.
        example: testVMs
    required: [name]

  CreateGroupsPartialSuccessResponse:
    title: Create Group Response
    description: Response containing the IDs of the created groups along with the failures.
    type: object
    properties:
      groups:
        type: array
        description: The groups created.
        items:
          $ref: '#/definitions/GroupInfo'
      error:
        $ref: '#/definitions/Error'

  GroupInfo:
    title: Group Info
    description: Information about a group.
    type: object
    properties:
      gid:
        description: The ID of the group.
        type: string
        example: de4ccb7b-95e1-447f-a7dd-50782c3e06d6
      name:
        description: The name of the group.
        type: string
        example: group
      lastUpdatedTimestamp:
        description: The time when the group was alst updated.
        type: string
        format: date-time
        example: '2019-02-12T14:49:03.013000Z'
    required: [gid, name, lastUpdatedTimestamp]

  SystemGroupPair:
    title: System Group Pair
    description: Pair containing the system ID and the group ID.
    type: object
    properties:
      id:
        type: string
        description: The ID of the system.
        example: VMware_Virtual_Platform--SN-VMware-56_4d_70_f1_81_06_04_3b-55_19_2a_87_f6_41_20_e5--MAC-00-0C-29-41-20-E5
      gid:
        type: string
        description: The ID of the group.
        example: de4ccb7b-95e1-447f-a7dd-50782c3e06d6
    required: [id, gid]

  GetInfoResponse:
    description: Discoverable information about the system provided in the GetInfo request.
    title: GetInfoResponse
    type: object
    properties:
      request:
        description: The original request excluding the username and password.
        type: object
        properties:
          hostname:
            description: The hostname of the system.
            type: string
            example: testvm
          ipAddress:
            description: The IP of the system.
            type: string
            example: 10.10.10.10
      result:
        $ref: '#/definitions/SystemInfo'
      statusCode:
        description: The status of the request to get information about a system.
        type: string
        example: 0
    required: [request, statusCode]

  SystemsKeys:
    description: An object containing pending, denied, approved, and rejected system keys. If there are no entries in a given category, then the key representing that category is omitted. The value for the keys is in itself a dictionary, with the key representing the system ID and the value the public authorization key used.
    title: Systems Keys
    type: object
    properties:
      systemsPending:
        type: object
        description: An object of system ID to key pairs that are pending approval or rejection. Keys may be pending when they are not pre-seeded via the automated registration process and attempt to connect to the master.
        additionalProperties:
          type: string
        example:
          VMware_Virtual_Platform--SN-VMware-56_4d_d2_08_ce_89_1b_70-e6_32_fc_21_6c_d0_d9_f9--MAC-00-0C-29-D0-D9-F6: "-----BEGIN PUBLIC KEY-----↵MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlFgEKiRwWBD/QSDHCpNQ↵Zml9q224YzIxG6reByDV16BNsQoH0lc2bT9LZ7o6xf6dTpQl7shIMc/abSAcl4/F↵VpKguH1yRmOG2Nhout/9wMP6kYBTlThzpop93rlxIo/I7nDkQDz07cMhNWYDvrut↵PVnjRg70xOCAzQRCHRy4GW3TLvfp2WAbCuoQ5oPHQLx+YBSRYDcgfo9jiW8vNzt4↵Bcg72c2PmHEJjGslzJeqcKdRjK0z4/VFgLYfMUBz4LCoy7DohU/uc9ZbHSlOy/BK↵1/S8O1vUyk8DEq+/kQumJWKh1Cl0SWcZGSDkdhQhoTiWqXGb1BBtU7vkxYgQoYjM↵rwIDAQAB↵-----END PUBLIC KEY-----"
      systemsDenied:
        type: object
        description: An object of system ID to key pairs that have been denied. A key is denied when a system is trying to connect the master with a different key than the one that is accepted. This can occur if two systems have the same ID or if a key is removed from a system.
        additionalProperties:
          type: string
        example:
          VMware_Virtual_Platform--SN-VMware-56_4d_d2_08_ce_89_1b_70-e6_32_fc_21_6c_d0_d9_f9--MAC-00-0C-29-D0-D9-F7: "-----BEGIN PUBLIC KEY-----↵MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlFgEKiRwWBD/QSDHCpNQ↵Zml9q224YzIxG6reByDV16BNsQoH0lc2bT9LZ7o6xf6dTpQl7shIMc/abSAcl4/F↵VpKguH1yRmOG2Nhout/9wMP6kYBTlThzpop93rlxIo/I7nDkQDz07cMhNWYDvrut↵PVnjRg70xOCAzQRCHRy4GW3TLvfp2WAbCuoQ5oPHQLx+YBSRYDcgfo9jiW8vNzt4↵Bcg72c2PmHEJjGslzJeqcKdRjK0z4/VFgLYfMUBz4LCoy7DohU/uc9ZbHSlOy/BK↵1/S8O1vUyk8DEq+/kQumJWKh1Cl0SWcZGSDkdhQhoTiWqXGb1BBtU7vkxYgQoYjM↵rwIDAQAB↵-----END PUBLIC KEY-----"
      systemsApproved:
        type: object
        description: An object of system ID to key pairs that have been approved. These could have been approved explicitly by the user or pre-seeded via the automated registration process.
        additionalProperties:
          type: string
        example:
          VMware_Virtual_Platform--SN-VMware-56_4d_d2_08_ce_89_1b_70-e6_32_fc_21_6c_d0_d9_f9--MAC-00-0C-29-D0-D9-F8: "-----BEGIN PUBLIC KEY-----↵MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlFgEKiRwWBD/QSDHCpNQ↵Zml9q224YzIxG6reByDV16BNsQoH0lc2bT9LZ7o6xf6dTpQl7shIMc/abSAcl4/F↵VpKguH1yRmOG2Nhout/9wMP6kYBTlThzpop93rlxIo/I7nDkQDz07cMhNWYDvrut↵PVnjRg70xOCAzQRCHRy4GW3TLvfp2WAbCuoQ5oPHQLx+YBSRYDcgfo9jiW8vNzt4↵Bcg72c2PmHEJjGslzJeqcKdRjK0z4/VFgLYfMUBz4LCoy7DohU/uc9ZbHSlOy/BK↵1/S8O1vUyk8DEq+/kQumJWKh1Cl0SWcZGSDkdhQhoTiWqXGb1BBtU7vkxYgQoYjM↵rwIDAQAB↵-----END PUBLIC KEY-----"
      systemsRejected:
        type: object
        description: An object of system ID to key pairs that have been rejected. Keys are rejected explicitly by the user.
        additionalProperties:
          type: string
        example:
          VMware_Virtual_Platform--SN-VMware-56_4d_d2_08_ce_89_1b_70-e6_32_fc_21_6c_d0_d9_f9--MAC-00-0C-29-D0-D9-F9: "-----BEGIN PUBLIC KEY-----↵MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlFgEKiRwWBD/QSDHCpNQ↵Zml9q224YzIxG6reByDV16BNsQoH0lc2bT9LZ7o6xf6dTpQl7shIMc/abSAcl4/F↵VpKguH1yRmOG2Nhout/9wMP6kYBTlThzpop93rlxIo/I7nDkQDz07cMhNWYDvrut↵PVnjRg70xOCAzQRCHRy4GW3TLvfp2WAbCuoQ5oPHQLx+YBSRYDcgfo9jiW8vNzt4↵Bcg72c2PmHEJjGslzJeqcKdRjK0z4/VFgLYfMUBz4LCoy7DohU/uc9ZbHSlOy/BK↵1/S8O1vUyk8DEq+/kQumJWKh1Cl0SWcZGSDkdhQhoTiWqXGb1BBtU7vkxYgQoYjM↵rwIDAQAB↵-----END PUBLIC KEY-----"

  KeyAction:
    type: string
    title: Key Action
    enum:
      - ACCEPT
      - REJECT
      - DELETE
      - ACTIVATE_ACCEPT
    example: ACCEPT
    description: >
      Action to be performed.
        * ACCEPT: Accept the associated key.
        * REJECT: Reject the associated key.
        * DELETE: Delete the associated key.
        * ACTIVATE_ACCEPT: Activate the system with the associated key and then accept the key.

  ManageKeysRequest:
    description: Request to perform specific acceptance actions to system keys.
    title: Manage Keys Request
    type: object
    properties:
      isAsync:
        description: Whether the request is async or not. If async is true the request will return immediately without waiting for the operation to complete.
        type: boolean
        default: false
        example: true
      keyActions:
        type: array
        items:
          description: Object defining a system ID and the action that should be performed over the key.
          title: Key Request
          type: object
          properties:
            id:
              type: string
              description: A string representing the system ID.
              example: VMware_Virtual_Platform--SN-VMware-56_4d_30_26_4f_c9_5c_05-b7_68_d1_cd_99_6e_22_16--MAC-02-01-02-03-04-08
            action:
              $ref: '#/definitions/KeyAction'
            key:
              type: string
              description: A string representing the public authorization key. If this field is specified, verification that the system ID is associated with this auth key will happen before the desired action is executed.
              example: -----BEGIN PUBLIC KEY-----↵MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlFgEKiRwWBD/QSDHCpNQ↵Zml9q224YzIxG6reByDV16BNsQoH0lc2bT9LZ7o6xf6dTpQl7shIMc/abSAcl4/F↵VpKguH1yRmOG2Nhout/9wMP6kYBTlThzpop93rlxIo/I7nDkQDz07cMhNWYDvrut↵PVnjRg70xOCAzQRCHRy4GW3TLvfp2WAbCuoQ5oPHQLx+YBSRYDcgfo9jiW8vNzt4↵Bcg72c2PmHEJjGslzJeqcKdRjK0z4/VFgLYfMUBz4LCoy7DohU/uc9ZbHSlOy/BK↵1/S8O1vUyk8DEq+/kQumJWKh1Cl0SWcZGSDkdhQhoTiWqXGb1BBtU7vkxYgQoYjM↵rwIDAQAB↵-----END PUBLIC KEY-----
            workspace:
              type: string
              description: The ID of the workspace.
              example: '5bc5e9092a4fa4c71cfa7197'
          required: [id, action]
        required: [keyActions]

  SystemPatchRequest:
    description: System data that needs to be assigned to the system.
    title: System Patch Request
    x-ni-sparse: true
    type: object
    properties:
      keywords:
        description: The new keywords assigned to the system.
        type: array
        items:
          type: string
        example:
          - test
          - vm
      properties:
        description: The new properties assigned to the system.
        type: object
        additionalProperties:
          type: string
        example:
          owner: admin
      alias:
        description: The new  alias of the system.
        type: string
        example: testVM
      workspace:
        type: string
        description: The ID of the workspace.
        example: '5bc5e9092a4fa4c71cfa7197'
        
  UpdateSystemsRequest:
    description: List of systems and metadata to be updated.
    title: Update Systems Request
    type: object
    properties:
      SystemsUpdateInformation:
        description: The list of system ids and changes.
        type: array
        items:
          description: System ids and changes that need to be applied to the systems.
          title: SystemUpdateInformation
          type: object
          properties:
            systemId:
              type: string
              description: The system id.
              example: 'VMware_Virtual_Platform--SN-VMware-56_4d_d2_08_ce_89_1b_70-e6_32_fc_21_6c_d0_d9_f9--MAC-00-0C-29-D0-D9-F9'
            systemMetadata:
              $ref: '#/definitions/SystemMetadata'

  SystemMetadata:
    description: System metadata to be updated.
    title: SystemMetadata
    x-ni-sparse: true
    type: object
    properties:
      workspace:
        type: string
        description: The ID of the workspace.
        example: '5bc5e9092a4fa4c71cfa7197'
      properties:
        type: object
        description: The new properties (key-value pairs).
        additionalProperties:
          type: string
        example:
          owner: admin
      
  QueryAvailablePackagesRequest:
    title: Get Available Packages Request
    description: Request to get the available packages from the feeds specified in the request.
    type: object
    properties:
      returnDuplicates:
        description: A boolean representing whether to return packages of equal version for each architecture.
        type: boolean
        default: false
        example: false
      systemConfigurations:
        description: An array of system configurations.
        type: array
        items:
          type: object
          title: System Configuration
          properties:
            feedUris:
              type: array
              description: An array of strings representing feed URIs a system(s) has configured.
              items:
                type: string
              example:
                - http://download.ni.com/ni-linux-rt/feeds/SystemLink/18.5/x64/
                - http://download.ni.com/ni-linux-rt/feeds/SystemLink/salt/18.5/x64/x64/
            osArchitectures:
              type: array
              description: An array of strings representing OS architectures supported by a system(s) in descending priority.
              items:
                type: string
              example:
                - x64
                - core2-64
                - x86_64
                - noarch
                - any
                - all
          required: [feedUris]
    required: [systemConfigurations]

  PackageResponse:
    title: Get Available Packages Response
    description: A list with the available packages.
    type: object
    properties:
      arch:
        type: string
        description: The architecture of the package.
        example: windows_x64
      breaks:
        type: array
        description: An array containing information about other packages this package breaks.
        items:
          type: string
          description: The name of a package this package breaks. This also contains information about the version of the package.
          example: "ni-sysapi (>= 18.0.0)"
      conflicts:
        type: array
        description: An array containing information about other packages this package conflicts with.
        items:
          type: string
          description: The name of a package this package conflicts with. This also contains information about the version of the package.
          example: "ni-msvcrt-2015 (>= 14.1.4)"
      depends:
        type: array
        description: An array containing information about other packages this package depends on.
        items:
          type: string
          description: The name of a package this package depends on. This also contains information about the version of the package.
          example: "ni-metauninstaller (>= 18.0.1)"
      description:
        type: string
        description: The description of the package.
        example: This is an infrastructure package for NI Software.
      displayName:
        type: string
        description: The display name of the package.
        example: NI Security Update (KB 67L8LCQW)
      displayVersion:
        type: string
        description: The display version of the package.
        example: 2.0.0
      enhances:
        type: array
        description: An array containing information about other packages this package enhances.
        items:
          type: string
          description: The name of a package this package enhances. This also contains information about the version of the package.
          example: "ni-msiproperties (>= 18.0.1)"
      essential:
        type: boolean
        description: Whether the package is essential or not. If true then the package management system will refuse to remove the package (upgrading and replacing it is still possible).
        example: true
      fileName:
        type: string
        description: |
          The location of the file, including the file extension.
          Depending on the platform you select, you will be able to use the following package extensions: .nipkg for windows feeds, .ipk and .deb for ni-linux-rt feeds.
        example: ni-securityupdate-kb67l8lcqw-killbits_2.0.0.22-0+d22_windows_x64.nipkg
      hardwareSupport:
        type: array
        description: When a package provides functionality for specific hardware product(s), it can list such products in this section
        items:
          type: string
          example: NI cRIO-9035 (Sync)
      homepage:
        type: string
        description: The website of the maintainers for this package.
        example: "http://www.ni.com"
      installedSize:
        type: integer
        format: int64
        description: The size of this package after install.
        example: 1024
      maintainer:
        type: string
        description: The maintainer of this package.
        example: "NI <support@ni.com>"
      name:
        type: string
        description: The name of the package.
        example: "ni-securityupdate-kb67l8lcqw-killbits"
      plugin:
        type: string
        description: Agent that will be used to install the package.
        example: "wininst"
      predepends:
        type: array
        description: An array containing information about other packages this package predepends.
        items:
          description: The name of a package this package predepends. This also contains information about the version of the package.
          type: string
          example: "ni-teststand-2017-tools (>= 17.0.0)"
      priority:
        type: string
        description: The priority of the package.
        example: "standard"
      provides:
        type: array
        description: An array containing information about other packages this package provides.
        items:
          type: string
          example: "ni-curl (= 17.0.0.49152-0+f0)"
          description: One of the packages the containing package provides. This also contains information about the version of the package.
      recommends:
        type: array
        description: An array containing information about other packages this package recommends.
        items:
          type: string
          description: The name of a package this package recommends. This also contains information about the version of the package.
          example: "ni-systemlink-client-2018.5-realtime-bin (>= 18.5.0)"
      releaseNotes:
        type: string
        description: A page containing the release notes of the package.
        example: Refer to the NI website at http://www.ni.com/r/slrm185 for installation instructions, known issues, bug fixes, compatibility information, and other important notices about this product.
      replaces:
        type: array
        description: An array containing information about other packages this package replaces.
        items:
          type: string
          description: The name of a package this package replaces. This also contains information about the version of the package.
          example: "b235b862-6a92-4a04-a8b2-6d71f777de67 (< 16.99.65535)"
      section:
        type: string
        description: The section of the package.
        example: Infrastructure
      size:
        type: integer
        format: int64
        description: The size of the package in bytes.
        example: 750070
      source:
        type: string
        description: The source of this package, if any.
        example: "thunar-archive-plugin_0.3.1.bb"
      storeProduct:
        type: boolean
        description: Whether the package represent a product in the store or not.
        example: true
      suggests:
        type: array
        description: An array containing information about other packages this package suggests.
        items:
          type: string
          description: The name of a package this package suggests. This also contains information about the version of the package.
          example: "ni-systemlink-client-2018.5-realtime-bin (>= 18.5.0)"
      tags:
        type: array
        description: An array containing tags for the package.
        items:
          type: string
          description: The tag for the package.
          example: ".NET"
      uservisible:
        type: boolean
        description: The installed packages with this attribute set to true are considered to be installed by a user, thus not installed to fulfill some dependency. This is needed input for the calculation of unneeded packages when removing a package.
        example: true
      version:
        type: string
        description: The version of the package.
        example: "2.0.0.22-0+d22"
    required:
      - name
      - version

  Error:
    description: Contains error information
    type: object
    properties:
      name:
        description: The string error code.
        type: string
        example: SaltCancelJobFailed
      code:
        description: Numeric error code.
        type: integer
        format: int32
        example: -254003
      resourceType:
        description: The type of resource associated with the error.
        type: string
        example: Job
      resourceId:
        description: The identifier of the resource associated with the error.
        type: string
        example: '20190211135234448026_28320'
      message:
        description: The filled in error message.
        type: string
        example: Cannot cancel the job id '{0}' on system id '{1}'.
      args:
        description: Positional argument values for the error code.
        type: array
        items:
          type: string
          example: '20190211135234448026_28320'
        example:
          - '20190211135234448026_28320'
          - VMware_Virtual_Platform--SN-VMware-56_4d_30_26_4f_c9_5c_05-b7_68_d1_cd_99_6e_22_16--MAC-02-01-02-03-04-08
      innerErrors:
        type: array
        description: Internal errors that occured in the service.
        items:
          $ref: '#/definitions/Error'

  Operation:
    description: An operation provided by the API
    type: object
    properties:
      available:
        type: boolean
        description: Whether the operation is available to the caller.
        example: true
      version:
        type: integer
        format: int32
        description: The version of the available operation.
        example: 1
    required: [available]

  V1Operations:
    description: V1 operations
    type: object
    properties:
      operations:
        description: >-
          Available operations in the v1 version of the API:

          - getJobs: The ability to retrieve the jobs.

          - getSystems: The ability to retrieve the systems information.

          - getGroups: The ability to retrieve the groups.

          - manageSystems: The ability to manage keys and unregister systems.

          - discoverSystems: The ability to discover and register systems.

          - createOrCancelJobs: The ability to create or cancel jobs.

          - activateSystems: The ability to activate systems.

          - updateSystemMetadata: The ability to update systems metadata.

          - manageFeeds: The ability to configure feeds and retrieve the available packages.

          - createOrUpdateGroups: The ability to create, update, or delete groups.

        type: object
        properties:
          getJobs:
            $ref: '#/definitions/Operation'
          getSystems:
            $ref: '#/definitions/Operation'
          getGroups:
            $ref: '#/definitions/Operation'
          manageSystems:
            $ref: '#/definitions/Operation'
          discoverSystems:
            $ref: '#/definitions/Operation'
          createOrCancelJobs:
            $ref: '#/definitions/Operation'
          activateSystems:
            $ref: '#/definitions/Operation'
          updateSystemMetadata:
            $ref: '#/definitions/Operation'
          manageFeeds:
            $ref: '#/definitions/Operation'
          createOrUpdateGroups:
            $ref: '#/definitions/Operation'

  QuerySystemsRequest:
    description: Request for querying systems resources. Dynamic LINQ is used for query syntax. More info can be found at https://dynamic-linq.net
    title: Query Systems Request
    properties:
      skip:
        description: The number of resources to skip.
        type: integer
        format: int64
        default: 0
        minimum: 0
        example: 0
      take:
        description: The number of resources to return. The maximum value is 1000.
        type: integer
        format: int64
        minimum: 0
        maximum: 1000
        example: 100
      filter:
        type: string
        example: connected.data.state=="CONNECTED"
        description: >-
          The filter criteria for jobs or systems. Consists of a string of queries composed using AND/OR operators.
          String values and date strings need to be enclosed in double quotes.
          Parenthesis can be used around filters to better define the order of operations.

          Filter syntax: '[property name][operator][operand] and [property name][operator][operand]'


          Operators:

          - Equals operator '='. Example: 'x = y'

          - Not equal operator '!='. Example: 'x != y'

          - Greater than operator '>'. Example: 'x > y'

          - Greater than or equal operator '>='. Example: 'x >= y'

          - Less than operator '<'. Example: 'x < y'

          - Less than or equal operator '<='. Example: 'x <= y'

          - Logical AND operator 'and' or '&&'. Example: 'x and y'

          - Logical OR operator 'or' or '||'. Example: 'x or y'

          - Contains operator '.Contains()', used to check if a list contains an element. Example: 'x.Contains(y)'

          - Not Contains operator '!.Contains()', used to check if a list does not contain an element. Example: '!x.Contains(y)'


          Valid system properties that can be used in the filter:

          - id : String representing the ID of the system.

          - createdTimestamp: ISO-8601 formatted timestamp string specifying the date when the system was registered.

          - lastUpdatedTimestamp: ISO-8601 formatted timestamp string specifying the last date the system was updated.

          - alias: String representing the alias of the system.

          - activation.lastUpdatedTimestamp: ISO-8601 formatted timestamp string specifying the last date the system activation was updated.

          - activation.data.activated: Boolean representing whether the system is activated or not.

          - activation.data.licenseName: String representing the name of the license.

          - activation.data.licenseVersion: String representing the license version.

          - connected.lastUpdatedTimestamp: ISO-8601 formatted timestamp string specifying the last date the system connection was updated.

          - connected.data.state: String representing the state of the system.

          - grains.lastUpdatedTimestamp: ISO-8601 formatted timestamp string specifying the last date the system grains were updated.

          - grains.data: Dictionary of string to object representing general information about the system. Example: grains.data.os == "Windows" or DateTime(grains.data.boottime) > "2021-06-01T08:20:09.512Z"

          - packages.lastUpdatedTimestamp: ISO-8601 formatted timestamp string specifying the last date the system installed packages were updated.

          - packages.data: Dictionary representing software packages installed on the system. Example: packages.data.ni-package-manager-upgrader.version: String representing the installed version of ni-package-manager-upgrader package.

          - feeds.lastUpdatedTimestamp: ISO-8601 formatted timestamp string specifying the last date the system configured feeds were updated.

          - feeds.data: Dictionary representing the feeds configured on the system.

          - sysapi.lastUpdatedTimestamp: ISO-8601 formatted timestamp string specifying the last date the system sysapi data was updated.

          - sysapi.data: Dictionary representing system API information of a system.

          - groups.lastUpdatedTimestamp: ISO-8601 formatted timestamp string specifying the last date the system groups data was updated.

          - groups.data: Array of strings representing the IDs of the groups the system is assigned to. Example: groups.data.Contains("id")

          - keywords.lastUpdatedTimestamp: ISO-8601 formatted timestamp string specifying the last date the system keywords were updated.

          - keywords.data: Array of strings representing the keywords of the system. Example: keywords.data.Contains("test")

          - properties.lastUpdatedTimestamp: ISO-8601 formatted timestamp string specifying the last date the system properties were updated.

          - properties.data: Dictionary of string to string representing metadata information about a system. Example: properties.data.owner == "admin"
      projection:
        type: string
        example: 'new(id,grains,lastUpdatedTimestamp)'
        description: >-
            Specifies the projection for resources. Use this field to receive specific properties of the model.

            Examples:
                - 'new(id,connected)'
                - 'new(id,alias,grains.data.host as host)'
                - 'new(id,lastUpdatedTimestamp,properties.data.location as location)'
      orderBy:
        type: string
        example: 'lastUpdatedTimestamp descending'
        description: The order in which data returns.

  QueryJobsRequest:
    description: Request for querying jobs resources. Dynamic LINQ is used for query syntax. More info can be found at https://dynamic-linq.net
    title: Query Jobs Request
    properties:
      skip:
        description: The number of resources to skip.
        type: integer
        format: int64
        default: 0
        minimum: 0
        example: 0
      take:
        description: The number of resources to return. The maximum value is 1000.
        type: integer
        format: int64
        minimum: 0
        maximum: 1000
        example: 100
      filter:
        type: string
        example: state=="SUCCEEDED"
        description: >-
          The filter criteria for jobs or systems. Consists of a string of queries composed using AND/OR operators.
          String values and date strings need to be enclosed in double quotes.
          Parenthesis can be used around filters to better define the order of operations.

          Filter syntax: '[property name][operator][operand] and [property name][operator][operand]'


          Operators:

          - Equals operator '='. Example: 'x = y'

          - Not equal operator '!='. Example: 'x != y'

          - Greater than operator '>'. Example: 'x > y'

          - Greater than or equal operator '>='. Example: 'x >= y'

          - Less than operator '<'. Example: 'x < y'

          - Less than or equal operator '<='. Example: 'x <= y'

          - Logical AND operator 'and' or '&&'. Example: 'x and y'

          - Logical OR operator 'or' or '||'. Example: 'x or y'

          - Contains operator '.Contains()', used to check if a list contains an element. Example: 'x.Contains(y)'

          - Not Contains operator '!.Contains()', used to check if a list does not contain an element. Example: '!x.Contains(y)'


          Valid job properties that can be used in the filter:

          - jid : String representing the ID of the job.

          - id : String representing the ID of the system.

          - createdTimestamp: ISO-8601 formatted timestamp string specifying the date when the job was created.

          - lastUpdatedTimestamp: ISO-8601 formatted timestamp string specifying the last date the job was updated.

          - dispatchedTimestamp: ISO-8601 formatted timestamp string specifying the date when the job was actually sent to the system.

          - state: String representing the state of the job.

          - metadata: Object containg the the metadata of job. Example: metadata.queued

          - config.user: String representing the user who created the job.

          - config.tgt: List of strings representing the targeted systems. Example: config.tgt.Contains("id")

          - config.fun: List of strings representing the functions to be executed within the job. Example: config.fun.Contains("nisysmgmt.set_blackout")

          - config.arg: An array of arrays of variable type elements that are arguments to the function specified by the "fun" property. Example: config.arg[0].Contains("test")

          - result.return: An array of objects representing return values for each executed function. Example:
            result.return[0].Contains("Success")

          - result.retcode: An array of integers representing code values for each executed function. Example: result.retcode

          - result.success: An array of booleans representing success values for each executed function. Example:
            result.success.Contains(false)
      projection:
        type: string
        example: 'new(id,jid,state,lastUpdatedTimestamp,config.fun as fun)'
        description: >-
            Specifies the projection for resources. Use this field to receive specific properties of the model.

            Examples:
                - 'new(id,jid,state)'
                - 'new(id,jid,config.user as user)'
                - 'new(id,jid,state,lastUpdatedTimestamp,metadata.queued as queued)'
      orderBy:
        type: string
        example: 'lastUpdatedTimestamp descending'
        description: The order in which data returns.

  QueryJobsResponse:
    description: Response of a query request.
    title: Query Response
    properties:
      data:
        description: The data returned by query.
        type: array
        items:
          type: object
        example:
          - jid: '20190211135234448026_28320'
      count:
        description: The total number of resources that matched the query.
        type: integer
        format: int64
        example: 1
    required: [data, count]

  QuerySystemsResponse:
    description: Response of a query systems request.
    title: Query Systems response
    properties:
      data:
        description: The data returned by query.
        type: array
        items:
          type: object
        example:
          id: 'NI_PXIe-8880--SN-030A5D78--MAC-00-80-2F-21-C6-86'
          grains:
            data:
              key: 'value'
          lastUpdatedTimestamp: '2019-10-29T10:47:04.596+02:00'
      count:
        description: The total number of resources that matched the query.
        type: integer
        format: int64
        example: 1
    required: [data, count]

paths:
  /:
    get:
      operationId: HandleGetVersionInfo
      summary: API information
      tags: [versioning]
      security: []
      description: Gets permissions and operations for the Systems Management Service.
      responses:
        200:
          description: OK.
          schema:
            description: Version information.
            title: RootEndpointResponse
            type: object
            properties:
              v1:
                $ref: '#/definitions/V1Operations'
              version:
                description: The implementation version of the web service.
                type: string
        default:
            $ref: '#/responses/Error'
  /{version}:
    get:
      operationId: RootEndpointWithVersion
      summary: API version information
      description: Returns available operations for a single version of the API.
      tags: [versioning]
      security: []
      parameters:
        - in: path
          name: version
          description: The version of the API to retrieve operations.
          x-example: v1
          type: string
          required: true
      responses:
        200:
          description: OK.
          schema:
            $ref: '#/definitions/V1Operations'
        404:
          description: Not Found.
        default:
            $ref: '#/responses/Error'
  /v1/jobs:
    post:
      operationId: CreateJob
      x-ni-auth: true
      x-ni-operation: createOrCancelJobs
      x-ni-request-timeout: 300000
      x-ni-request-variables: [REMOTE_USER, USER_NAME]
      tags: [jobs]
      summary: Create a job
      description: Create a job and returns the newly created job including the job ID.
      parameters:
        - in: body
          name: CreateJobRequest
          required: true
          description: The definition of job to be executed.
          schema:
            $ref: '#/definitions/CreateJobRequest'
      responses:
        201:
          description: Created
          schema:
            $ref: '#/definitions/CreateJobResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    get:
      operationId: GetJobs
      x-ni-auth: true
      x-ni-operation: getJobs
      x-ni-request-timeout: 120000
      tags: [jobs]
      summary: Get jobs
      description: Get jobs from the jobs cache.
      parameters:
        - in: query
          name: jid
          description: A string defining the job ID.
          type: string
          x-example: '20190211135234448026_28320'
        - in: query
          name: state
          description: A string defining the job state.
          type: string
          x-example: SUCCEEDED
        - in: query
          name: fun
          description: A string defining the function executed by the job.
          type: string
          x-example: test.ping
        - in: query
          name: systemId
          description: A string defining the system ID.
          type: string
          x-example: VMware_Virtual_Platform--SN-VMware-56_4d_30_26_4f_c9_5c_05-b7_68_d1_cd_99_6e_22_16--MAC-02-01-02-03-04-08
      responses:
        200:
          description: OK.
          schema:
            type: array
            items:
              $ref: '#/definitions/Job'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/systems:
    get:
      operationId: GetSystems
      x-ni-auth: true
      x-ni-operation: getSystems
      x-ni-request-timeout: 120000
      tags: [systems]
      summary: Get systems information
      description: Get the systems information cached on the server.
      parameters:
        - in: query
          name: id
          description: A string defining the system ID.
          type: string
          x-example: VMware_Virtual_Platform--SN-VMware-56_4d_30_26_4f_c9_5c_05-b7_68_d1_cd_99_6e_22_16--MAC-02-01-02-03-04-08
      responses:
        200:
          description: OK.
          schema:
            type: array
            items:
              $ref: '#/definitions/ManagedSystem'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/register-systems:
    post:
      operationId: RegisterSystems
      x-ni-auth: true
      x-ni-operation: manageSystems
      tags: [systems]
      summary: Register systems
      description: Make a request to register systems. This is an asynchronous request. A successful status code informs that the request has been acknowledged and not that all the registration procedures have completed successfully.
      parameters:
        - in: body
          name: RegisterRequest
          description: Registration information.
          required: true
          schema:
            $ref: '#/definitions/RegisterSystemsRequest'
      responses:
        200:
          description: OK.
          schema:
            $ref: '#/definitions/RegisterSystemsResponse'
        401:
          $ref: '#/responses/Unauthorized'
        400:
          $ref: '#/responses/BadRequest'
        default:
          $ref: '#/responses/Error'
  /v1/remove-systems:
    post:
      operationId: UnregisterSystems
      x-ni-auth: true
      x-ni-request-timeout: 180000
      x-ni-operation: manageSystems
      x-ni-request-variables: [REMOTE_USER, USER_NAME]
      tags: [systems]
      summary: Unregister Systems
      description: Request to unregister systems.
      parameters:
        - in: body
          name: UnregisterSystemsRequest
          description: Request data to unregister systems.
          required: true
          schema:
            $ref: '#/definitions/UnregisterSystemsRequest'
      responses:
        200:
          description: OK.
          schema:
            $ref: '#/definitions/UnregisterSystemsResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/cancel-jobs:
    post:
      operationId: CancelJobs
      x-ni-auth: true
      x-ni-operation: createOrCancelJobs
      x-ni-request-timeout: 120000
      tags: [jobs]
      summary: Cancel jobs
      description: Cancel jobs that are running on systems. This won't stop the jobs from executing on systems if the jobs have already been dispatched to the systems.
      parameters:
        - in: body
          name: CancelJobsRequest
          description: An array of pairs defining the job ID and the targeted systems.
          required: true
          schema:
            type: array
            items:
              $ref: '#/definitions/CancelJobRequest'
      responses:
        200:
          $ref: '#/responses/PartialSuccess'
        204:
          description: No Content.
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/activate-systems:
    post:
      operationId: ActivateSystems
      x-ni-auth: true
      x-ni-operation: activateSystems
      x-ni-request-timeout: 120000
      tags: [systems]
      summary: Activate systems
      description: Activate managed systems.
      parameters:
        - in: body
          name: ActivateSystemsRequest
          description: Array of system IDs to activate.
          required: true
          schema:
            type: array
            items:
              type: string
              example: VMware_Virtual_Platform--SN-VMware-56_4d_d2_08_ce_89_1b_70-e6_32_fc_21_6c_d0_d9_f9--MAC-00-0C-29-D0-D9-F9
      responses:
        200:
          $ref: '#/responses/PartialSuccess'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        500:
          $ref: '#/responses/ServerNotActivated'
        default:
          $ref: '#/responses/Error'
  /v1/get-discovered-systems:
    get:
      operationId: GetDiscoveredSystems
      x-ni-auth: true
      x-ni-operation: getSystems
      tags: [systems]
      summary: Get discovered systems
      description: Get network discovered systems.
      responses:
        200:
          description: OK.
          schema:
            type: array
            items:
              $ref: '#/definitions/SystemInfo'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/get-systems-summary:
    get:
      operationId: GetSystemsSummary
      x-ni-auth: true
      x-ni-operation: getSystems
      tags: [systems]
      summary: Get systems summary
      description: Get the number of connected and disconnected managed systems.
      responses:
        200:
          description: OK.
          schema:
            $ref: '#/definitions/ManagedSystemsSummary'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/get-jobs-summary:
    get:
      operationId: GetJobsSummary
      x-ni-auth: true
      x-ni-operation: getJobs
      tags: [jobs]
      summary: Get jobs summary
      description: Get the number of active, failed, and succeeded jobs.
      responses:
        200:
          description: OK.
          schema:
            $ref: '#/definitions/JobsSummary'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/configure-feeds:
    post:
      operationId: ConfigureAndUpdateMultipleFeeds
      x-ni-auth: true
      x-ni-request-timeout: 360000
      x-ni-operation: manageFeeds
      tags: [feeds]
      summary: Configure and update multiple feeds
      description: Configure and update multiple feeds.
      parameters:
        - in: body
          name: FeedUris
          required: true
          description: Feeds to be configured and updated.
          schema:
            type: array
            items:
              type: string
              description: The URI of the feed.
              example: 'http://download.ni.com/support/nipkg/products/ni-package-manager/released'
      responses:
        200:
          $ref: '#/responses/PartialSuccess'
        204:
          description: No Content.
        400:
          $ref: '#/responses/BadRequest'
  /v1/get-discovered-systems-summary:
    get:
      operationId: GetDiscoveredSystemsSummary
      x-ni-auth: true
      x-ni-operation: getSystems
      tags: [systems]
      summary: Get discovered systems summary
      description: Get the number of network discovered systems. This number refers to the count of systems that are discovered and not managed.
      responses:
        200:
          description: OK.
          schema:
            $ref: '#/definitions/DiscoveredSystemsSummary'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/get-pending-systems-summary:
    get:
      operationId: GetPendingSystemsSummary
      x-ni-auth: true
      x-ni-operation: getSystems
      x-ni-request-timeout: 120000
      tags: [systems]
      summary: Get pending systems summary
      description: Get the number of systems that are currently pending to be added to the master but have not yet been approved by the master.
      responses:
        200:
          description: OK.
          schema:
            $ref: '#/definitions/PendingSystemsSummary'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/generate-systems-report:
    post:
      operationId: GetSystemsReport
      x-ni-auth: true
      x-ni-operation: getSystems
      x-ni-request-timeout: 120000
      tags: [systems]
      summary: Get systems report
      description: Get a report containing software/hardware information about the requested systems.
      parameters:
        - in: body
          name: SystemsReportRequest
          description: The type of the request followed by the list of system Ids.
          required: true
          schema:
            $ref: '#/definitions/SystemsReportRequest'
      responses:
        200:
          description: OK.
          schema:
            description: The file data
            type: file
          examples:
            text/csv:
              Systems report file data
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/create-groups:
    post:
      operationId: CreateGroups
      x-ni-auth: true
      x-ni-operation: createOrUpdateGroups
      tags: [groups]
      summary: Create groups
      description: Create groups.
      parameters:
        - in: body
          name: CreateGroupRequest
          description: Request for creating groups.
          required: true
          schema:
            type: array
            items:
              $ref: '#/definitions/CreateGroupRequest'
      responses:
        200:
          description: OK.
          schema:
            $ref: '#/definitions/CreateGroupsPartialSuccessResponse'
        204:
          description: No Content.
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/groups:
    get:
      operationId: GetGroups
      x-ni-auth: true
      x-ni-operation: getGroups
      tags: [groups]
      summary: Get groups
      description: Get groups information.
      parameters:
        - in: query
          name: gid
          type: string
          description: A group ID.
      responses:
        200:
          description: OK.
          schema:
            type: array
            items:
              $ref: '#/definitions/GroupInfo'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/remove-groups:
    post:
      operationId: RemoveGroups
      x-ni-auth: true
      x-ni-operation: createOrUpdateGroups
      tags: [groups]
      summary: Remove groups
      description: Remove groups.
      parameters:
        - in: body
          name: Groups
          description: Array of strings representing group ids.
          required: true
          schema:
            type: array
            items:
              type: string
              example: de4ccb7b-95e1-447f-a7dd-50782c3e06d6
      responses:
        200:
          $ref: '#/responses/PartialSuccess'
        204:
          description: No Content.
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/add-systems-to-groups:
    post:
      operationId: AddSystemsToGroups
      x-ni-auth: true
      x-ni-operation: createOrUpdateGroups
      tags: [groups]
      summary: Add systems to groups
      description: Add systems to groups.
      parameters:
        - in: body
          name: SystemGroupPairs
          description: An array of objects representing system group pairs.
          required: true
          schema:
            type: array
            items:
              $ref: '#/definitions/SystemGroupPair'
      responses:
        200:
          $ref: '#/responses/PartialSuccess'
        204:
          description: No Content.
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/remove-systems-from-groups:
    post:
      operationId: RemoveSystemsFromGroups
      x-ni-auth: true
      x-ni-operation: createOrUpdateGroups
      tags: [groups]
      summary: Remove systems from groups
      description: Remove systems from groups.
      parameters:
        - in: body
          name: SystemGroupPairs
          description: An array of objects representing system group pairs.
          required: true
          schema:
            type: array
            items:
              $ref: '#/definitions/SystemGroupPair'
      responses:
        200:
          $ref: '#/responses/PartialSuccess'
        204:
          description: No Content
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/obtain-systems-info:
    post:
      operationId: GetSystemsInfo
      x-ni-auth: true
      x-ni-operation: getSystems
      tags: [systems]
      summary: Get systems info
      description: Get information about a specific set of systems by providing their credentials.
      parameters:
        - in: body
          name: SystemsCredentials
          description: Credentials of the systems to get the information
          required: true
          schema:
            type: array
            items:
              $ref: '#/definitions/SystemCredentials'
      responses:
        200:
          description: OK.
          schema:
            type: array
            items:
              $ref: '#/definitions/GetInfoResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/get-systems-keys:
    get:
      operationId: GetSystemsKeys
      x-ni-auth: true
      x-ni-request-timeout: 120000
      tags: [systems]
      x-ni-operation: getSystems
      summary: Get systems keys
      description: Returns the pending, denied, approved, and rejected systems keys.
      responses:
        200:
          description: OK.
          schema:
            $ref: '#/definitions/SystemsKeys'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/manage-systems-keys:
    post:
      operationId: ManageSystemsKeys
      x-ni-auth: true
      x-ni-request-timeout: 300000
      x-ni-operation: manageSystems
      tags: [systems]
      summary: Manage systems keys
      description: Perform actions over system keys.
      parameters:
        - in: body
          name: ManageKeysRequest
          required: true
          description: Request indicating actions like accept, reject, delete, activate_accept to systems keys.
          schema:
            $ref: '#/definitions/ManageKeysRequest'
      responses:
        200:
          $ref: '#/responses/PartialSuccess'
        204:
          description: No Content
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/systems/managed/{id}:
    patch:
      operationId: UpdateMetadata
      x-ni-auth: true
      x-ni-operation: updateSystemMetadata
      consumes:
        - application/merge-patch+json
      tags: [systems]
      summary: Update system metadata
      description: Update keywords or properties of a system.
      parameters:
        - name: id
          in: path
          description: ID of the system to be updated.
          required: true
          type: string
          x-example: VMware_Virtual_Platform--SN-VMware-56_4d_30_26_4f_c9_5c_05-b7_68_d1_cd_99_6e_22_16--MAC-02-01-02-03-04-08
        - in: body
          name: SystemPatchRequest
          required: true
          description: The new metadata associated with this system.
          schema:
            $ref: '#/definitions/SystemPatchRequest'
      responses:
        200:
          $ref: '#/responses/PartialSuccess'
        204:
          description: No Content
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/update-systems:
    post:
      operationId: UpdateSystemsMetadata
      x-ni-auth: true
      x-ni-operation: updateSystemMetadata
      tags: [systems]
      summary: Update systems metadata
      description: Update metadata for a list of systems.
      parameters:
        - in: body
          name: UpdateSystemsRequest
          required: true
          description: The new metadata associated with a list of systems.
          schema:
            $ref: '#/definitions/UpdateSystemsRequest'
      responses:
        200:
          $ref: '#/responses/PartialSuccess'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/query-available-packages:
    post:
      operationId: GetAvailablePackagesByQuery
      x-ni-auth: true
      x-ni-request-timeout: 300000
      x-ni-operation: manageFeeds
      tags: [feeds]
      summary: Query packages
      description: Get available packages for a set of system configurations. If multiple system configurations are provided, only packages available to all applicable systems are returned. If OS architectures are provided, only the package with highest priority will be returned for packages of equal version.
      parameters:
        - in: body
          name: FeedsConfigurations
          description: The configurations of the feeds.
          required: true
          schema:
            $ref: '#/definitions/QueryAvailablePackagesRequest'
      responses:
        200:
          description: OK.
          schema:
            type: array
            items:
              $ref: '#/definitions/PackageResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/query-jobs:
    post:
      operationId: GetJobsByQuery
      x-ni-auth: true
      x-ni-operation: getJobs
      x-ni-request-timeout: 120000
      tags: [jobs]
      summary: Query jobs
      description: Get jobs by query.
      parameters:
        - in: body
          name: Query
          description: Query for getting jobs data.
          required: true
          schema:
            $ref: '#/definitions/QueryJobsRequest'
      responses:
        200:
          description: OK.
          schema:
            $ref: '#/definitions/QueryJobsResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/query-systems:
    post:
      operationId: GetSystemsByQuery
      x-ni-auth: true
      x-ni-operation: getSystems
      x-ni-request-timeout: 120000
      tags: [systems]
      summary: Query systems
      description: Get systems by query.
      parameters:
        - in: body
          name: Query
          description: Query for getting systems data.
          required: true
          schema:
            $ref: '#/definitions/QuerySystemsRequest'
      responses:
        200:
          description: OK.
          schema:
            $ref: '#/definitions/QuerySystemsResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=systems-state/nisystemsstate.yml sha256=3de3925db4ddcb5e3cbecbf7fbbf997b071c5b89b1b4ba267ad25dc7511b8259 bytes=32966 -->
## FILE: systems-state/nisystemsstate.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `systems-state/nisystemsstate.yml`
- sha256: `3de3925db4ddcb5e3cbecbf7fbbf997b071c5b89b1b4ba267ad25dc7511b8259`
- bytes: 32966

````yaml
swagger: '2.0'
info:
  description: "Creates and manages states you can apply to managed systems."
  version: "1"
  title: "SystemLink Systems State Manager"
  contact:
    name: NI
    url: https://www.ni.com/systemlink
    email: support@ni.com
basePath: "/nisystemsstate"
x-ni-routing-key: 'Skyline.SystemsStateManager'
x-ni-privilege-application: 'niws.nisysmgmt'
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

  BadRequest:
    description: Bad Request indicates that the server was unable to process the request because of invalid syntax.
    schema:
      title: Bad Request Error Response
      description: Bad request error response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

  Unauthorized:
    description: Not authorized.
    headers:
      WWW_Authenticate:
        description: Information for how to authenticate.
        type: string

  Conflict:
    description: This response is sent when a request conflicts with the current state of the server.
    schema:
      title: Conflict Error Response
      description: Conflict error response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

  PartialSuccess:
    description: Partial Success in the case when only a part of the request body metadata information was processed successfully.
    schema:
      title: PartialSuccessResponse
      description: Partial success response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

  NotFound:
    description: The requested resource was not found.
    schema:
      title: Not Found Request Error Response
      description: Not found error response containing error information.
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'

definitions:
  StateIDVersionPair:
    type: object
    title: StateID-Version Pair
    properties:
      stateID:
        description: The ID of the state.
        type: string
      stateVersion:
        description: The version of the state. The latest package/feed set of the state will be used if the version is not specified.
        type: string
    required:
      - stateID
    example:
      stateID: 5bcde471fc13379595ce9b13
      stateVersion: 9ae65370c79ac158ad061032944afe6b94d927ca

  ExportStateRequest:
    type: object
    title: Export State
    properties:
      inline:
        description: >-
            Whether to return the state data inline or as an attachment.
            When the inline is true, the
            Content-Disposition header is set to 'inline'.
            When the inline is not specified or is
            false, the state contents are handled as a download. The
            Content-Disposition header is set to 'attachment' and
            the MIME type is set to text/x-yaml; charset=UTF-8.
        type: boolean
        example: true
      state:
        $ref: '#/definitions/StateIDVersionPair'
    required:
      - state

  ExportStateFromSystemRequest:
    type: object
    title: Export State From System
    properties:
      inline:
        description: >-
            Whether to return the state data inline or as an attachment.
            When the inline is true, the
            Content-Disposition header is set to 'inline'.
            When the inline is not specified or is
            false, the state contents are handled as a download. The
            Content-Disposition header is set to 'attachment' and
            the MIME type is set to text/x-yaml; charset=UTF-8.
        type: boolean
        example: true
      systemID:
        description: System ID.
        type: string
        example: cRIO-9064--SN-11111111--MAC-00-01-02-03-04-05
    required:
      - systemID

  RevertStateRequest:
    type: object
    title: Revert Request
    properties:
      id:
        description: The ID of the state.
        type: string
      version:
        description: The version of the state.
        type: string
    required:
      - id
      - version
    example:
      id: 5bcde471fc13379595ce9b13
      version: 9ae65370c79ac158ad061032944afe6b94d927ca

  Error:
    description: Contains error information
    type: object
    properties:
      name:
        description: The string error code.
        type: string
      code:
        description: Numeric error code.
        type: integer
      resourceType:
        description: The type of resource associated with the error.
        type: string
      resourceId:
        description: The identifier of the resource associated with the error.
        type: string
      message:
        description: The filled-in error message.
        type: string
      args:
        description: Positional argument values for the error code.
        type: array
        items:
          type: string
      innerErrors:
        type: array
        items:
          $ref: '#/definitions/Error'
    example:
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251040
      message: >-
        One or more errors occurred. See the contained list for details of each
        error.
      args: []
      innerErrors:
        - name: SystemsStateManager.StateNotFound
          code: -253401
          resourceType: SystemStateEntry
          resourceId: 5bc4463af0f06f4585003ae6
          message: 'The state with identifier 5bc4463af0f06f4585003ae6 was not found.'
          args: [5bc4463af0f06f4585003ae6]

  Operation:
    description: An operation provided by the API
    type: object
    properties:
      available:
        type: boolean
        description: Whether the operation is available to the caller.
      version:
        type: integer
        description: The version of the available operation.
    required: [available]
    example:
      available: true
      version: 1

  V1Operations:
    description: V1 operations
    type: object
    properties:
      operations:
        description: >-
          Available operations in the v1 version of the API:

          - getStates: The ability to retrieve states

          - createOrUpdateStates: The ability to create or update states

          - deleteStates: The ability to delete states
        type: object
        properties:
          getStates:
            $ref: '#/definitions/Operation'
          createOrUpdateStates:
            $ref: '#/definitions/Operation'
          deleteStates:
            $ref: '#/definitions/Operation'

  StateArchitecture:
    description: Supported architecture by a state.
    title: State Architecture
    type: string
    enum:
      - ARM
      - X64
      - X86
      - ANY
    example: ARM

  StateDistribution:
    description: Supported distribution by a state.
    title: State Distribution
    type: string
    enum:
      - NI_LINUXRT
      - NI_LINUXRT_NXG
      - WINDOWS
      - ANY
    example: NI_LINUXRT

  StateMetadata:
    description: State metadata information.
    title: State Description
    type: object
    properties:
      id:
        type: string
        description: The ID of the state.
        example: 5bc4463af0f06f4585003ae6
      name:
        type: string
        description: The name of the state.
        example: crio9064State
      fileName:
        type: string
        description: The file name of the state.
        example: crio9064State
      description:
        type: string
        description: The description of the state.
        example: crio9064 Setup State
      distribution:
        $ref: '#/definitions/StateDistribution'
      architecture:
        $ref: '#/definitions/StateArchitecture'
      createdTimestamp:
        description: ISO-8601 formatted timestamp specifying the state creation date.
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
      lastUpdatedTimestamp:
        description: ISO-8601 formatted timestamp specifying the last date that the state was updated.
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
      workspace:
        type: string
        description: The ID of the workspace. This property is available starting with version 3 of the getStates operation.
        example: '5bc5e9092a4fa4c71cfa7197'
    required:
      - id
      - name
      - fileName
      - distribution
      - architecture
      - createdTimestamp
      - lastUpdatedTimestamp
      - workspace

  StateDescriptionListResponse:
    description: The response containing a list of state metadata.
    title: State Description List Response
    type: object
    properties:
      totalCount:
        type: integer
        description: Total count of states.
      states:
        type: array
        items:
          $ref: '#/definitions/StateMetadata'
    example:
      totalCount: 2
      states:
        - id: '5bc5e9092a4fa4c71cfa7197'
          name: vim
          description: Having Vim installed on the windows system.
          distribution: WINDOWS
          architecture: x64
          createdTimestamp: '2018-05-07T18:58:05.219692Z'
          lastUpdatedTimestamp: '2018-05-07T18:58:05.219692Z'
          workspace: '5bc5e9092a4fa4c71cfa7197'
        - id: '5bcde471fc13379595ce9b13'
          name: emacs
          description: Having Emacs installed on the windows system.
          distribution: WINDOWS
          architecture: x86
          createdTimestamp: '2018-05-07T18:58:05.219692Z'
          lastUpdatedTimestamp: '2018-05-07T18:58:05.219692Z'
          workspace: '5bc5e9092a4fa4c71cfa7198'
    required:
      - totalCount
      - states

  StateRequest:
    description: System state object.
    title: State Request
    type: object
    properties:
      name:
        type: string
        description: Name of the state.
        example: crio9064State
      description:
        type: string
        description: Description of the state.
        example: crio9064 Setup State
      distribution:
        $ref: '#/definitions/StateDistribution'
      architecture:
        $ref: '#/definitions/StateArchitecture'
      feeds:
        type: array
        items:
          $ref: '#/definitions/Feed'
      systemImage:
          $ref: '#/definitions/SystemImage'
      packages:
        type: array
        items:
          $ref: '#/definitions/Package'
      workspace:
        type: string
        description: The ID of the workspace. This property is available starting with version 3 of the createOrUpdateStates operation.
        example: '5bc5e9092a4fa4c71cfa7197'
    required:
      - name
      - distribution
      - architecture

  StatePatchRequest:
    description: System state object defining which attributes have to be replaced.
    title: State Patch Request
    x-ni-sparse: true
    type: object
    properties:
      name:
        type: string
        description: Name of the state.
        example: crio9064State
      description:
        type: string
        description: Description of the state.
        example: crio9064 Setup State
      distribution:
        $ref: '#/definitions/StateDistribution'
      architecture:
        $ref: '#/definitions/StateArchitecture'
      feeds:
        type: array
        items:
          $ref: '#/definitions/Feed'
      systemImage:
        $ref: '#/definitions/SystemImage'
      packages:
        type: array
        items:
          $ref: '#/definitions/Package'
      changeDescription:
        type: string
        description: Description of the change operation.
        example: I've changed the state
      workspace:
        type: string
        description: The ID of the workspace. This property is available starting with version 3 of the createOrUpdateStates operation.
        example: '5bc5e9092a4fa4c71cfa7197'

  StateResponse:
    description: System state object.
    title: State response
    type: object
    properties:
      id:
        type: string
        description: The ID of the state.
        example: 5bc4463af0f06f4585003ae6
      name:
        type: string
        description: The name of the state.
        example: crio9064State
      fileName:
        type: string
        description: The file name of the state.
        example: crio9064State
      description:
        type: string
        description: The description of the state.
        example: crio9064 Setup State
      distribution:
        $ref: '#/definitions/StateDistribution'
      architecture:
        $ref: '#/definitions/StateArchitecture'
      createdTimestamp:
        description: ISO-8601 formatted timestamp specifying the state creation date.
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
      lastUpdatedTimestamp:
        description: ISO-8601 formatted timestamp specifying the last date that the state has been updated.
        type: string
        format: date-time
        example: '2018-05-07T18:58:05.219692Z'
      feeds:
        type: array
        items:
          $ref: '#/definitions/Feed'
      systemImage:
        $ref: '#/definitions/SystemImage'
      packages:
        type: array
        items:
          $ref: '#/definitions/Package'
      containsExtraOperations:
        type: boolean
        description: Whether the state contains extra operations in addition to feeds and packages.
        example: true
      workspace:
        type: string
        description: The ID of the workspace. This property is available starting with version 3 of the getStates operation.
        example: '5bc5e9092a4fa4c71cfa7197'
    required:
      - id
      - name
      - fileName
      - distribution
      - architecture
      - createdTimestamp
      - lastUpdatedTimestamp
      - containsExtraOperations
      - workspace

  StateVersion:
    description: A given version of a state.
    title: State Version
    type: object
    properties:
      version:
        type: string
      description:
        type: string
        description: The description of this specific change.
    required:
      - version
    example:
      version: 26783106b56d87c5ef6c70c549b82e4ab004e590
      description: added package

  StateHistoryResponse:
    description: The history of a state.
    title: State History Response
    type: object
    properties:
      totalCount:
        type: integer
        description: Total number of versions of a state.
      versions:
        type: array
        items:
          $ref: '#/definitions/StateVersion'
    example:
      totalCount: 2
      versions:
        - version: 4d514a6b31ee6ed72ae509c360be8dca6e68ffb0
          description: initial version
        - version: 0520222b9e7edae30c37c244dbce0deb23982c11
          description: added new package
    required:
      - totalCount
      - versions

  Feed:
    description: Object defining a feed, which contains the name, url, and Booleans for whether the feed is enabled and compressed.
    type: object
    properties:
      name:
        type: string
        description: Name of the feed.
      url:
        type: string
        description: The url for the repository.
      enabled:
        type: boolean
        description: Whether the feed is enabled or not.
        default: true
      compressed:
        type: boolean
        description: Whether the feed is compressed or not.
        default: false
    required:
      - name
      - url
    example:
      name: ni
      enabled: true
      url: ni.com
      compressed: true

  SystemImage:
    description: Object defining a system image containing the name, version and optionally if the image should be reinstalled if it is already installed.
    type: object
    properties:
      name:
        type: string
        description: Name of the system image.
      version:
        type: string
        description: Version of the system image.
      reinstall:
        type: boolean
        description: Whether the image should be reinstalled if it is already installed.
        default: false
    required:
      - name
      - version
    example:
      name: dist-nilrt-grub
      version: '20.5.0'

  Package:
    description: Object defining a package containing the name and version.
    type: object
    properties:
      name:
        type: string
        description: Name of the package.
      version:
        type: string
        description: Version of the package.
      installRecommends:
        type: boolean
        description: A boolean variable whose value controls the installation of the recommended packages. This property is available starting with version 2 of the getStates and createOrUpdateStates operations.
        default: true
    required:
      - name
      - version
    example:
      name: vim
      version: '7.1'
      installRecommends: true

paths:
  /:
    get:
      operationId: HandleGetVersionInfo
      x-ni-auth: true
      summary: API information
      tags: [versioning]
      security: []
      description: Gets permissions and operations for the States Service. This API now includes organizational modeling, starting with version 3 of getStates and createOrUpdateStates operations. This route doesn't return granular permissions, but the operation is available if the current user has the corresponding access to at least one resource, regardless of the workspace. We recommend using the User Service API instead.
      responses:
        200:
          description: OK
          schema:
            description: Version information.
            title: RootEndpointResponse
            type: object
            properties:
              v1:
                $ref: '#/definitions/V1Operations'
              version:
                description: The implementation version of the web service.
                type: string
        default:
            $ref: '#/responses/Error'
  /{version}:
    get:
      operationId: RootEndpointWithVersion
      x-ni-auth: true
      summary: API version information
      description: Returns available operations for a single version of the API. This API now includes organizational modeling, starting with version 3 of getStates and createOrUpdateStates operations. This route doesn't return granular permissions, but the operation is available if the current user has the corresponding access to at least one resource, regardless of the workspace. We recommend using the User Service API instead.
      tags: [versioning]
      security: []
      parameters:
        - in: path
          name: version
          description: The version of the API to retrieve operations.
          x-example: v1
          type: string
          required: true
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/V1Operations'
        404:
          description: Not Found
        default:
            $ref: '#/responses/Error'
  /v1/states:
    get:
      operationId: GetStates
      x-ni-auth: true
      x-ni-operation: getStates
      tags: [states]
      summary: Get all system states
      description: Return metadata information of all system states.
      parameters:
        - in: query
          name: skip
          description: How many states to skip. Used for pagination.
          type: integer
          x-ni-data-type: U32
          default: 0
        - in: query
          name: take
          description: How many states to retrieve. Used for pagination.
          type: integer
          x-ni-data-type: U32
          default: 1000
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/StateDescriptionListResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      operationId: CreateState
      x-ni-auth: true
      x-ni-operation: createOrUpdateStates
      tags: [states]
      summary: Create a new system state
      description: Create a new System State by providing the required metadata and content.
      parameters:
        - in: body
          name: state
          description: The state to create.
          required: true
          schema:
            $ref: '#/definitions/StateRequest'
      responses:
        201:
          description: Created
          schema:
            $ref: '#/definitions/StateResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        409:
          $ref: '#/responses/Conflict'
        default:
          $ref: '#/responses/Error'
  /v1/states/{id}:
    get:
      operationId: GetState
      x-ni-auth: true
      x-ni-operation: getStates
      tags: [states]
      summary:  Get system state
      description: Returns the metadata, feeds, and packages from the state content. If the state contains only feed and package entries, the containsExtraOperations property of the response will be false. You may use the export route to get all state content.
      parameters:
        - name: id
          in: path
          description: ID of the state to return.
          required: true
          type: string
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/StateResponse'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
            $ref: '#/responses/Error'
    patch:
      operationId: UpdateState
      x-ni-auth: true
      x-ni-operation: createOrUpdateStates
      consumes:
        - application/merge-patch+json
      tags: [states]
      summary: Update a state
      description: Update a state by providing specific changes to the state. The method overrides all state properties with those contained in the request. Therefore, if you want to ignore a properties update, leave the value off the request.
      parameters:
        - name: id
          in: path
          description: ID of state that needs to be updated.
          required: true
          type: string
        - in: body
          name: patch
          required: true
          description: Json Patch describing the changes.
          schema:
            $ref: '#/definitions/StatePatchRequest'
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/StateResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        409:
          $ref: '#/responses/Conflict'
        default:
          $ref: '#/responses/Error'
    delete:
      operationId: DeleteState
      x-ni-auth: true
      x-ni-operation: deleteStates
      tags: [states]
      summary: Delete state
      description: Delete a state by providing its id.
      parameters:
        - name: id
          in: path
          description: ID of state that needs to be deleted.
          required: true
          type: string
      responses:
        204:
          description: No Content
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/replace-state-content:
    post:
      operationId: ReplaceContent
      x-ni-auth: true
      x-ni-operation: createOrUpdateStates
      tags: [states]
      summary: Replace the content of a state
      description: Replace the existing content of a state with new content.
      consumes:
        - multipart/form-data
      parameters:
        - name: id
          in: formData
          description: ID of the state for which to update the content.
          required: true
          type: string
        - in: formData
          description: New content of the state.
          name: file
          type: file
          required: true
        - in: formData
          description: Description of the change operation.
          name: changeDescription
          type: string
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/StateResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        409:
          $ref: '#/responses/Conflict'
        default:
          $ref: '#/responses/Error'
  /v1/states/{id}/history:
    get:
      operationId: GetStateHistory
      x-ni-auth: true
      x-ni-operation: getStates
      tags: [history]
      summary: Get state history
      description: Returns a list of version-description pairs defining the history of the state.
      parameters:
        - name: id
          in: path
          description: ID of the state for which it returns the history.
          required: true
          type: string
        - in: query
          name: skip
          description: Number of state versions to skip. Used for pagination.
          type: integer
          x-ni-data-type: U32
          default: 0
        - in: query
          name: take
          description: Number of state versions to retrieve. Used for pagination.
          type: integer
          x-ni-data-type: U32
          default: 1000
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/StateHistoryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/states/{id}/history/{version}:
    get:
      operationId: GetStateVersion
      x-ni-auth: true
      x-ni-operation: getStates
      tags: [history]
      summary: Get state by version
      description: Returns the snapshot of a state at a specific version. Returns the metadata, feeds, and packages from the state content. If the state contains only feed and package entries, the containsExtraOperations property of the response will be false. You may use the export route to get all state content.
      parameters:
        - name: id
          in: path
          description: ID of the state for which it returns the history.
          required: true
          type: string
        - name: version
          in: path
          description: State version to retrieve.
          type: string
          required: true
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/StateResponse'
        401:
          $ref: '#/responses/Unauthorized'
        404:
          $ref: '#/responses/NotFound'
        default:
          $ref: '#/responses/Error'
  /v1/export-state:
    post:
      operationId: ExportState
      x-ni-auth: true
      x-ni-operation: getStates
      tags: [states]
      summary: Export a state
      description: Export the state content to a file. If the version is not provided in body, then the latest content will be exported. 
      parameters:
        - name: stateInfo
          in: body
          description: State to be exported.
          required: true
          schema:
            $ref: '#/definitions/ExportStateRequest'
      produces:
        - text/x-yaml
        - application/json
      responses:
        200:
          description: OK
          schema:
            description: The file data
            type: file
          examples:
            application/octet-stream:
              File data
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/import-state:
    post:
      operationId: ImportState
      x-ni-auth: true
      x-ni-operation: createOrUpdateStates
      tags: [states]
      summary: Import a state
      description: Import a state by providing the metadata and content of an existing state file.
      consumes:
        - multipart/form-data
      parameters:
        - in: formData
          name: file
          type: file
          required: true
        - in: formData
          name: name
          type: string
          required: true
        - in: formData
          name: description
          type: string
        - in: formData
          name: distribution
          type: string
          enum:
            - NI_LINUXRT
            - NI_LINUXRT_NXG
            - WINDOWS
        - in: formData
          name: architecture
          type: string
          enum:
            - ARM
            - x64
            - x86
          required: true
        - in: formData
          name: workspace
          type: string
      responses:
        201:
          description: Created
          schema:
            $ref: '#/definitions/StateResponse'
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        409:
          $ref: '#/responses/Conflict'
        default:
          $ref: '#/responses/Error'
  /v1/export-state-from-system:
    post:
      operationId: ExportStateFromSystem
      x-ni-auth: true
      x-ni-operation: getStates
      tags: [states]
      summary: Export the state of a system by providing its ID.
      description: Export the state of a system by providing its ID. 
      parameters:
        - name: systemInfo
          in: body
          description: The information about the system.
          required: true
          schema:
            $ref: '#/definitions/ExportStateFromSystemRequest'
      responses:
        200:
          description: OK
          schema:
            description: The file data
            type: file
          examples:
            text/x-yaml:
              State file data
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/delete-states:
    post:
      operationId: DeleteStates
      x-ni-auth: true
      x-ni-operation: deleteStates
      tags: [states]
      summary: Delete states
      description: Delete a list of states by providing their IDs.
      parameters:
        - in: body
          name: StateIDs
          description: The list of state IDs to delete.
          required: true
          schema:
            type: array
            items:
              description: The ID of a state to delete.
              type: string
              example: '5bcde471fc13379595ce9b13'
      responses:
        200:
          $ref: '#/responses/PartialSuccess'
        204:
          description: No Content
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/revert-state-version:
    post:
      operationId: RevertStateToVersion
      x-ni-auth: true
      x-ni-operation: createOrUpdateStates
      tags: [history]
      summary: Revert a state
      description: Revert a state to a certain version. This operation will create a new version of the state and the contents will be the same as in specified version.
      parameters:
        - in: body
          name: Revert information
          description: Revert information that contains the stateID and the version.
          required: true
          schema:
            $ref: '#/definitions/RevertStateRequest'
      responses:
        204:
          description: No Content
        400:
          $ref: '#/responses/BadRequest'
        401:
          $ref: '#/responses/Unauthorized'
        409:
          $ref: '#/responses/Conflict'
        default:
          $ref: '#/responses/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=tag/nitag.yml sha256=27b5bd95dfc50430d0102dc51151f6345fc4544e3f5be189658ce7655bfb4c82 bytes=67044 -->
## FILE: tag/nitag.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `tag/nitag.yml`
- sha256: `27b5bd95dfc50430d0102dc51151f6345fc4544e3f5be189658ce7655bfb4c82`
- bytes: 67044

````yaml
swagger: '2.0'
info:
  description: Publish and manage timestamped key-value-pair data.
  version: '2'
  title: SystemLink Tag Service
  contact:
    name: NI
    url: 'https://www.ni.com/systemlink'
    email: support@ni.com
basePath: /nitag
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

responses:
  Unauthorized:
    description: Not authorized
    headers:
      WWW_Authenticate:
        description: Information for how to authenticate (sent only from SystemLink Server).
        type: string
  Error:
    description: Error (sent only from SystemLink Server)
    schema:
      description: Error response
      title: ErrorResponse
      type: object
      properties:
        error:
          $ref: '#/definitions/Error'
  GetTagsWithValuesResponse:
    description: List of tags, including their current and aggregate values
    schema:
      title: Get Tags With Values Response
      type: object
      properties:
        totalCount:
          description: Total number of tags which match a given query
          type: integer
        tagsWithValues:
          description: List of tags with their current and aggregate values
          type: array
          items:
            $ref: '#/definitions/TagWithValue'
  QueryTagsWithValuesResponse:
    description: List of tags, including their current and aggregate values
    schema:
      title: Query Tags With Values Response
      type: object
      properties:
        continuationToken:
          description: >-
            Token to pass to a subsequent query to retrieve the next
            page of tags
          type: string
          example: token
        tagsWithValues:
          description: List of tags with their current and aggregate values
          type: array
          items:
            $ref: '#/definitions/TagWithValue'
      required: [tagsWithValues]
  GetTagsResponse:
    description: List of tags, excluding current and aggregate values
    schema:
      title: Get Tags Response
      type: object
      properties:
        totalCount:
          type: integer
          description: Total number of tags which match a given query
        tags:
          description: List of tags
          type: array
          items:
            $ref: '#/definitions/Tag'
  UpdateSubscriptionsHeartbeatResponse:
    description: Success
    schema:
      description: Update subscriptions' heartbeat response
      type: object
      title: Update Subscriptions Heartbeat Response
      properties:
        invalidSubscriptionIds:
          description: List of invalid subscription IDs
          type: array
          items:
            type: string
  V1GetSubscriptionUpdatesResponse:
    description: List of subscription updates
    schema:
      title: V1 Get Subscription Updates Response
      type: object
      properties:
        subscriptionUpdates:
          description: Subscription updates
          type: array
          items:
            $ref: '#/definitions/V1SubscriptionUpdate'
        invalidSubscriptionIds:
          description: List of invalid subscription IDs
          type: array
          items:
            type: string
  V2GetSubscriptionUpdatesResponse:
    description: List of subscription updates
    schema:
      title: V2 Get Subscription Updates Response
      type: object
      properties:
        subscriptionUpdates:
          description: Subscription updates
          type: array
          items:
            $ref: '#/definitions/V2SubscriptionUpdate'
        invalidSubscriptionIds:
          description: List of invalid subscription IDs
          type: array
          items:
            type: string

paths:
  /:
    get:
      tags: [versioning]
      summary: API information
      description: Returns information about API versions and available operations.
      operationId: RootEndpoint
      security: []
      responses:
        200:
          description: OK
          schema:
            title: Root Endpoint Response
            description: Version information.
            type: object
            properties:
              version:
                description: Implementation version of the web service.
                type: string
              v2:
                $ref: '#/definitions/V2Operations'
        default:
          $ref: '#/responses/Error'
  /v2:
    get:
      tags: [versioning]
      summary: API version information
      description: Returns available operations for a single version of the API.
      operationId: RootEndpointWithVersion
      security: []
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/V2Operations'
        default:
          $ref: '#/responses/Error'
  /v2/subscriptions:
    post:
      tags:
        - subscriptions
      summary: Create a subscription
      description: Creates a subscription for a list of tags to get notifications when the tags change.
      operationId: CreateSubscription
      parameters:
        - in: body
          name: subscription
          description: Subscription to create.
          schema:
            $ref: '#/definitions/Subscription'
          required: true
      responses:
        200:
          description: Success
          schema:
            description: Response for creating a subscription.
            type: object
            title: Create Subscription Response
            properties:
              subscriptionId:
                type: string
              nonexistentTags:
                description: List of tags which did not exist.
                type: array
                items:
                  type: string
              alias:
                type: string
                description: Name of the subscription.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    get:
      tags:
        - subscriptions
      summary: Get active subscription IDs
      description: Returns a list of all active subscription IDs.
      operationId: GetSubscriptions
      parameters: []
      responses:
        200:
          description: Success
          schema:
            description: Get subscriptions response.
            type: object
            title: Get Subscriptions Response
            properties:
              subscriptionIds:
                description: List of all the active subscription IDs.
                type: array
                items:
                  type: string
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/subscriptions/{id}:
    get:
      tags:
        - subscriptions
      summary: Get a subscription
      description: Returns a subscription's metadata.
      operationId: GetSubscription
      parameters:
        - in: path
          name: id
          description: Subscription ID
          type: string
          required: true
      responses:
        200:
          schema:
            $ref: '#/definitions/Subscription'
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      tags:
        - subscriptions
      summary: Delete a subscription
      description: Deletes a specific subscription.
      operationId: DeleteSubscription
      parameters:
        - in: path
          name: id
          description: Subscription ID
          type: string
          required: true
      responses:
        204:
          description: Subscription successfully deleted.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/subscriptions/{id}/heartbeat:
    put:
      tags:
        - subscriptions
      summary: Update the heartbeat timer for a subscription
      description: Updates the heartbeat timer for the specified subscription. If a subscription's heartbeat timer elapses, the subscription will go inactive and will no longer record updates.
      operationId: UpdateSubscriptionHeartbeat
      parameters:
        - in: path
          name: id
          description: Subscription ID
          type: string
          required: true
      responses:
        200:
          description: Success
        204:
          description: No content (Sent only from SystemLink Server)
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/subscriptions/{id}/values/current:
    get:
      tags:
        - subscriptions
      summary: Get the current values for the tags in a subscription
      description: Returns the current values for the tags in the subscription. Can return either all values or only new values since the last request.
      operationId: GetSubscriptionTagValues
      parameters:
        - in: path
          name: id
          description: Subscription ID
          type: string
          required: true
      responses:
        200:
          $ref: '#/responses/V2GetSubscriptionUpdatesResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/refresh-subscriptions:
    post:
      tags:
        - subscriptions
      summary: Update the heartbeat timer for multiple subscriptions
      description: Updates the heartbeat timers for multiple subscriptions.
      operationId: UpdateSubscriptionHeartbeats
      parameters:
        - in: body
          name: subscriptionIds
          description: IDs of the subscriptions whose heartbeat timers you want to update.
          required: true
          schema:
            $ref: '#/definitions/SubscriptionIds'
      responses:
        200:
          $ref: '#/responses/UpdateSubscriptionsHeartbeatResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/query-subscription-values:
    post:
      tags:
        - subscriptions
      summary: Get the current values for the tags from multiple subscriptions
      description: Returns tag values from multiple subscriptions.
      operationId: GetSubscriptionsTagValues
      parameters:
        - in: body
          name: subscriptionIds
          required: true
          schema:
            $ref: '#/definitions/SubscriptionIds'
      responses:
        200:
          $ref: '#/responses/V2GetSubscriptionUpdatesResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/delete-subscriptions:
    post:
      tags:
        - subscriptions
      summary: Delete multiple subscriptions
      description: Delete one or more subscriptions based on the request body.
      operationId: DeleteSubscriptions
      parameters:
        - in: body
          name: subscriptionIds
          required: true
          schema:
            $ref: '#/definitions/SubscriptionIds'
      responses:
        200:
          description: Success
          schema:
            description: Response for deleting subscriptions.
            type: object
            title: Delete Subscriptions Response
            properties:
              invalidSubscriptionIds:
                description: List of invalid subscription IDs.
                type: array
                items:
                  type: string
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections:
    post:
      tags:
        - selections
      summary: Create a selection
      description: Selects a collection of tags for subsequent operations. Selections expire after up to fifteen minutes of inactivity.
      operationId: CreateSelection
      parameters:
        - in: body
          name: selection
          description: Selection to create.
          schema:
            $ref: '#/definitions/Selection'
          required: true
      responses:
        200:
          description: Success
          schema:
            $ref: '#/definitions/Selection'
        400:
          description: Bad Request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    get:
      tags:
        - selections
      summary: Get all selections
      description: Get all selections.
      operationId: GetSelections
      parameters: []
      responses:
        200:
          schema:
            type: array
            items:
              $ref: '#/definitions/Selection'
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}:
    put:
      tags:
        - selections
      summary: Modify a selection
      description: Modifies a selection's metadata.
      operationId: UpdateSelection
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
        - in: body
          name: selection
          description: Selection to replace the existing selection with.
          schema:
            $ref: '#/definitions/Selection'
          required: true
      responses:
        200:
          description: Success
          schema:
            $ref: '#/definitions/Selection'
        400:
          description: Bad Request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    get:
      tags:
        - selections
      summary: Get a selection
      description: Returns a selection's metadata.
      operationId: GetSelection
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            $ref: '#/definitions/Selection'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      tags:
        - selections
      summary: Delete a selection
      description: Deletes a selection.
      operationId: DeleteSelection
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        204:
          description: Successfully deleted.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}/tags-with-values:
    get:
      tags:
        - selections
      summary: Get the tags in a selection, including their current and aggregate values
      description: Returns the tags in a selection, including their current and aggregate values.
      operationId: GetSelectionTagsWithValues
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        200:
          $ref: '#/responses/GetTagsWithValuesResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}/tags:
    get:
      tags:
        - selections
      summary: Get the tags in a selection
      description: Returns the metadata of the tags in a selection.
      operationId: GetSelectionTags
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            type: array
            items:
              $ref: '#/definitions/Tag'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      tags:
        - selections
      summary: Delete all of the tags in a selection
      description: Deletes all of the tags in a selection.
      operationId: DeleteSelectionTags
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        204:
          description: Successfully deleted
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}/values:
    get:
      tags:
        - selections
      summary: Get the values of the tags in a selection, excluding tag metadata
      description: Returns the current values of the tags in a given selection. Does not return tag metadata.
      operationId: GetSelectionValues
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            type: array
            items:
              $ref: '#/definitions/TagPathWithCurrentAndAggregateValue'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}/values/current:
    get:
      tags:
        - selections
      summary: Get the current values of the tags in a selection, including timestamps
      description: Returns the current values of the tags in a selection, including timestamps for each value.
      operationId: GetSelectionCurrentTimestampedValues
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            type: array
            items:
              $ref: '#/definitions/TagPathWithTimestampedValue'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}/values/current/value:
    get:
      tags:
        - selections
      summary: Get the current values of the tags in a selection, excluding timestamps
      description: Returns the current values of the tags in a selection, excluding timestamps.
      operationId: GetSelectionCurrentValues
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            type: array
            items:
              $ref: '#/definitions/TagPathWithValue'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}/values/current/timestamp:
    get:
      tags:
        - selections
      summary: Get the timestamps of the current values of the tags in a selection
      description: Gets the timestamps of the current values of the tags in a selection.
      operationId: GetSelectionValuesCurrentTimestamp
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            description: Array containing the paths of the tags in the selection, along with the timestamp of their current values.
            type: array
            title: Tag Paths With Timestamps
            items:
              $ref: '#/definitions/TagPathWithTimestamp'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}/values/aggregates/min:
    get:
      tags:
        - selections
      summary: Get the "min" aggregate values for the tags in a selection
      description: Returns the minimum aggregate values for the tags in a selection.
      operationId: GetSelectionMinValues
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            description: Array of the "min" values from the aggregates for each tag in the selection.
            type: array
            items:
              $ref: '#/definitions/TagPathWithMinAggregate'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}/values/aggregates/max:
    get:
      tags:
        - selections
      summary: Get the "max" aggregate values for the tags in a selection
      description: Returns the maximum aggregate values for the tags in a selection.
      operationId: GetSelectionMaxAggregates
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            description: Array of the "max" values from the aggregates for each tag in the selection.
            type: array
            items:
              $ref: '#/definitions/TagPathWithMaxAggregate'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}/values/aggregates/mean:
    get:
      tags:
        - selections
      summary: Get the "avg" aggregate values for the tags in a selection
      description: Returns the mean aggregate values for the tags in a selection.
      operationId: GetSelectionMeanValues
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            description: Array of the "avg" values from the aggregates for each tag in the selection.
            type: array
            items:
              $ref: '#/definitions/TagPathWithMeanAggregate'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}/values/aggregates/count:
    get:
      tags:
        - selections
      summary: Get the "count" aggregate values for the tags in a selection
      description: Returns the count aggregate values for the tags in a selection.
      operationId: GetSelectionCountValues
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            description: Array of the "count" values from the aggregates for each tag in the selection.
            type: array
            items:
              $ref: '#/definitions/TagPathWithCountAggregate'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/selections/{id}/reset-aggregates:
    post:
      tags:
        - selections
      summary: Reset the aggregates of all tags in a selection
      description: Resets the aggregate values for all tags in a selection.
      operationId: ResetSelectionAggregates
      parameters:
        - in: path
          name: id
          description: Selection ID
          type: string
          required: true
      responses:
        204:
          description: No Content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/update-tags:
    post:
      tags:
        - tags
      summary: 'Create or update multiple tags'
      description: Creates or update multiple tags in one request.
      operationId: CreateOrUpdateTags
      parameters:
        - in: body
          name: tagsAndMerge
          description: Tags to create or update. Also specifies whether to merge keywords and properties when updating.
          required: true
          schema:
            type: object
            title: Tag List and Merge Flag
            properties:
              tags:
                description: List of tags
                type: array
                items:
                  $ref: '#/definitions/Tag'
              merge:
                description: If set, performs a merge of any specified Keywords or Properties.
                type: boolean
                default: false
      responses:
        200:
          $ref: '#/responses/Error'
        201:
          description: Created
        400:
          description: Bad Request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags:
    post:
      tags:
        - tags
      summary: Create or update a tag
      description: Creates or update a single tag and merges any keywords or properties you specify. You cannot change a tag's data type.
      operationId: CreateTag
      parameters:
        - in: body
          name: tag
          description: Tag to create
          schema:
            $ref: '#/definitions/Tag'
          required: true
      responses:
        201:
          description: 'Created: Tag created successfully'
        400:
          description: Bad Request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    get:
      tags:
        - tags
      summary: Get multiple tags
      description: Returns a list of tags based on query parameters you specify.
      operationId: GetTags
      parameters:
        - in: query
          name: path
          description: Comma-separated list of tag paths. May include glob-style wildcards.
          type: string
          required: false
          x-example: foo,bar,baz,*.System.Health.*
        - in: query
          name: keywords
          description: Comma-separated list of case-sensitive keywords.
          type: string
          required: false
          x-example: foo,bar,baz
        - in: query
          name: properties
          description: Comma-separated list of name=value strings
          type: string
          required: false
          x-example: foo=bar,baz=boo
        - in: query
          name: skip
          description: Number of entries to skip in the response list. Typically used in combination with the take parameter to implement pagination.
          type: integer
          required: false
          default: 0
        - in: query
          name: take
          description: Number of entries to include in the response list. Typically used in combination with the skip parameter to implement pagination.
          type: integer
          default: 100000
        - in: query
          name: workspace
          description: Workspace to search for tags.
          type: string
          required: false
          x-example: "b71390c0-977b-4153-a939-487b0b7a1fa5"
      responses:
        200:
          $ref: '#/responses/GetTagsResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags-count:
    get:
      tags:
        - tags
      summary: Get the total number of tags
      description: Returns the total number of tags.
      operationId: GetTagCount
      parameters: []
      responses:
        200:
          description: Contains the number of tags.
          schema:
            type: integer
            example: 2
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags-with-values:
    get:
      tags:
        - tags
      summary: Get the current values of multiple tags
      description: Returns current values of multiple tags.
      responses:
        200:
          $ref: '#/responses/GetTagsWithValuesResponse'
        400:
          description: Bad Request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
      operationId: GetTagsWithValues
      parameters:
        - in: query
          name: path
          description: Comma-separated list of tag paths. May include glob-style wildcards.
          type: string
          required: false
          x-example: foo,bar,baz,*.System.Health.*
        - in: query
          name: keywords
          description: Comma-separated list of case-sensitive keywords.
          type: string
          required: false
          x-example: foo,bar,baz
        - in: query
          name: properties
          description: Comma-separated list of name=value strings.
          type: string
          required: false
          x-example: foo=bar,baz=boo
        - in: query
          name: skip
          description: Number of entries to skip in the response list. Typically used in combination with the take parameter to implement pagination.
          type: integer
          required: false
          default: 0
        - in: query
          name: take
          description: Number of entries to include in the response list. Typically used in combination with the skip parameter to implement pagination.
          type: integer
          default: 100000
        - in: query
          name: workspace
          description: Workspace to search for tags.
          type: string
          required: false
          x-example: "b71390c0-977b-4153-a939-487b0b7a1fa5"
  /v2/tags-with-values/{workspace}/{path}:
    get:
      tags:
        - tags
      description: Get a tag and its value.
      summary: Returns a tag and its current value
      operationId: GetTagWithValueInWorkspace
      parameters:
        - in: path
          name: workspace
          type: string
          required: true
          x-example: "b71390c0-977b-4153-a939-487b0b7a1fa5"
        - in: path
          name: path
          type: string
          required: true
          x-example: my-tag-1
      responses:
        200:
          schema:
            $ref: '#/definitions/TagWithValue'
          description: Success
        400:
          description: Bad Request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags-with-values/{path}:
    get:
      tags:
        - tags
      description: Get a tag and its value from the default workspace.
      summary: Returns a tag and its current value
      operationId: GetTagWithValue
      parameters:
        - in: path
          name: path
          type: string
          required: true
      responses:
        200:
          schema:
            $ref: '#/definitions/TagWithValue'
          description: Success
        400:
          description: Bad Request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/{path}:
    put:
      tags:
        - tags
      summary: Create or replace a tag
      description: Replaces the tag at the location path specifies. If a tag does not exist where the path specifies, this route creates one.
      operationId: CreateOrReplaceTag
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
        - in: body
          name: tag
          description: Tag to create or replace. A complete resource representation must be sent (no partial updates).
          schema:
            $ref: '#/definitions/Tag'
          required: true
      responses:
        201:
          description: 'Created: Tag created successfully'
        204:
          description: 'No Content: Tag replaced successfully'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    get:
      tags:
        - tags
      summary: Get a tag
      description: Returns the metadata for a tag.
      operationId: GetTag
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            $ref: '#/definitions/Tag'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      tags:
        - tags
      summary: Delete a tag
      description: Deletes a tag.
      operationId: DeleteTag
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
      responses:
        204:
          description: 'No content: Tag deleted successfully'
        default:
          $ref: '#/responses/Error'
  /v2/tags/{path}/values:
    get:
      tags:
        - tags
      summary: Get the aggregates and current value of a tag
      description: Returns the current aggregate values for the tag at the path from the default workspace.
      operationId: GetTagValues
      parameters:
        - in: path
          name: path
          type: string
          required: true
          x-example: my-tag-1
      responses:
        200:
          description: Success
          schema:
            $ref: '#/definitions/TagCurrentAndAggregateValue'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/{workspace}/{path}/values:
    get:
      tags:
        - tags
      summary: Get the aggregates and current value of a tag
      description: Returns the current aggregate values for the tag at the path.
      operationId: GetTagValuesInWorkspace
      parameters:
        - in: path
          name: workspace
          type: string
          required: true
          x-example: "b71390c0-977b-4153-a939-487b0b7a1fa5"
        - in: path
          name: path
          type: string
          required: true
          x-example: my-tag-1
      responses:
        200:
          description: Success
          schema:
            $ref: '#/definitions/TagCurrentAndAggregateValue'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/{workspace}/{path}/values/current:
    put:
      tags:
        - tags
      summary: Update the current value of a tag.
      description: Updates the current value of the tag at the path within the given workspace.
      operationId: UpdateTagCurrentValuesInWorkspace
      parameters:
        - in: path
          name: workspace
          description: The ID of the workspace containing the tag.
          type: string
          required: true
          x-example: "f0144202-52d5-4861-98fa-615ed4b2f751"
        - in: path
          name: path
          description: The tag path.
          type: string
          required: true
          x-example: "my-tag-path"
        - in: body
          name: tagValue
          description: A timestamped tag value.
          schema:
            type: object
            $ref: '#/definitions/TimestampedTagValue'
      responses:
        202:
          description: Accepted
        400:
          description: Bad request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    
  /v2/tags/{path}/values/current:
    get:
      tags:
        - tags
      summary: Get the current value of a tag
      description: Returns the current value of the tag at the path.
      operationId: GetTagCurrentValue
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            $ref: '#/definitions/TimestampedTagValue'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    put:
      tags:
        - tags
      summary: Update the current value of a tag
      description: Updates the current value of the tag at the path.
      operationId: UpdateTagCurrentValue
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
        - in: body
          name: tagValue
          description: Timestamped value
          schema:
            $ref: '#/definitions/TimestampedTagValue'
          required: true
      responses:
        200:
          description: Tag Value Updated
        202:
          description: Accepted (Sent only from SystemLink Server)
        400:
          description: Bad Request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/{path}/values/current/timestamp:
    get:
      tags:
        - tags
      summary: Get the timestamp of a tag's current value
      description: Returns the timestamp of the tag's current value.
      operationId: GetTagCurrentValueTimestamp
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
      responses:
        200:
          description: Timestamp
        204:
          description: No timestamped value found
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/{path}/values/current/value:
    get:
      tags:
        - tags
      summary: Get the current value of a tag without its timestamp
      description: Returns the current value of a tag.
      operationId: GetTagCurrentValueWithoutTimestamp
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
      responses:
        200:
          schema:
            $ref: '#/definitions/TagValue'
          description: Success
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/{path}/values/aggregates/min:
    get:
      tags:
        - tag aggregates
      summary: Get the value of a tag's "min" aggregate
      description: Get the value of a tag's "min" aggregate.
      operationId: GetTagMinimum
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
      responses:
        200:
          description: Minimum aggregate value
          schema:
            type: string
        204:
          description: No aggregate value found
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/{path}/values/aggregates/max:
    get:
      tags:
        - tag aggregates
      summary: Get the value of a tag's "max" aggregate
      description: Get the value of a tag's "max" aggregate.
      operationId: GetTagMaxAggregate
      responses:
        200:
          description: Maximum aggregate value.
          schema:
            type: string
        204:
          description: No aggregate value found.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
  /v2/tags/{path}/values/aggregates/mean:
    get:
      tags:
        - tag aggregates
      summary: Get the value of a tag's "avg" aggregate
      description: Get the value of a tag's "avg" aggregate.
      operationId: GetTagMeanAggregate
      responses:
        200:
          description: Mean aggregate value.
          schema:
            type: number
            format: double
        204:
          description: No aggregate value found.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
  /v2/tags/{path}/values/aggregates/count:
    get:
      tags:
        - tag aggregates
      summary: Get the value of a tag's "count" aggregate
      description: Get the value of a tag's "count" aggregate.
      operationId: GetTagCountAggregate
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
      responses:
        200:
          description: Count aggregate value.
          schema:
            type: integer
        204:
          description: No aggregate value found.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/{path}/reset-aggregates:
    post:
      tags:
        - tag aggregates
      summary: Reset the aggregates of a tag
      description: Resets aggregate values for a tag from the default workspace.
      operationId: ResetTagAggregates
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
          x-example: my-tag-1
      responses:
        200:
          description: Success
        204:
          description: No content (Sent only from SystemLink Server)
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/{workspace}/{path}/reset-aggregates:
    post:
      tags:
        - tag aggregates
      summary: Reset the aggregates of a tag
      description: Resets aggregate values for a tag.
      operationId: ResetTagAggregatesInWorkspace
      parameters:
        - in: path
          name: workspace
          type: string
          required: true
          x-example: "b71390c0-977b-4153-a939-487b0b7a1fa5"
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
          x-example: my-tag-1
      responses:
        200:
          description: Success
        204:
          description: No content (Sent only from SystemLink Server)
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/update-current-values:
    post:
      tags:
        - tags
      summary: Update the current values of multiple tags
      description: Updates multiple tags to their current values.
      operationId: UpdateTagCurrentValues
      parameters:
        - in: body
          name: updates
          description: Updates
          schema:
            type: array
            items:
              $ref: '#/definitions/TagUpdate'
          required: true
      responses:
        202:
          description: Success
        400:
          description: Bad Request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/{path}/update-values:
    post:
      tags:
        - tags
      summary: Send multiple value updates to a tag
      description: Updates the current value of a tag at multiple times you specify. Use this route to send tag value history in bulk.
      operationId: update-tag-values
      responses:
        200:
          description: Tag Values Updated
        202:
          description: Accepted (Sent only from SystemLink Server)
        400:
          description: Bad Request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
      parameters:
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
        - in: body
          name: tagValues
          description: Timestamped values
          schema:
            type: array
            items:
              $ref: '#/definitions/TimestampedTagValue'
          required: true
  /v2/query-tags-with-values:
    post:
      tags:
        - tags
      summary: Query for tags
      description: Returns tags with values satisfying the provided filtering criteria.
      operationId: query-tags-with-values
      responses:
        200:
          $ref: '#/responses/QueryTagsWithValuesResponse'
        400:
          description: Bad Request
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
      parameters:
        - in: body
          name: tagQuery
          description: Request body consisting of filtering criteria to apply when retrieving tags.
          schema:
            $ref: '#/definitions/TagQuery'
          required: true
  /v2/tags/{workspace}/{path}:
    put:
      tags:
        - tags
      summary: Create or replace a tag in the given workspace
      description: Replaces the tag at the location path specifies. If a tag does not exist where the path specifies, one is created.
      operationId: CreateOrReplaceTagInWorkspace
      parameters:
        - in: path
          name: workspace
          description: Workspace
          type: string
          required: true
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
        - in: body
          name: tag
          description: Tag to create or replace. A complete resource representation must be sent (no partial updates).
          schema:
            $ref: '#/definitions/Tag'
          required: true
      responses:
        201:
          description: 'Created: Tag created successfully'
        204:
          description: 'No Content: Tag replaced successfully'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    get:
      tags:
        - tags
      summary: Get a tag from the given workspace
      description: Returns the metadata for a tag.
      operationId: GetTagInWorkspace
      parameters:
        - in: path
          name: workspace
          description: Workspace
          type: string
          required: true
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
      responses:
        200:
          description: Success
          schema:
            $ref: '#/definitions/Tag'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      tags:
        - tags
      summary: Delete a tag from the given workspace
      description: Deletes a tag.
      operationId: DeleteTagInWorkspace
      parameters:
        - in: path
          name: workspace
          description: Workspace
          type: string
          required: true
        - in: path
          name: path
          description: Tag path
          type: string
          required: true
      responses:
        204:
          description: 'No content: Tag deleted successfully'
        default:
          $ref: '#/responses/Error'

definitions:
  Operation:
    description: An operation in the API.
    type: object
    properties:
      version:
        type: integer
        description: The version of the available operation.
        example: 2
  V2Operations:
    title: V2 Operations
    description: An object containing available operations in the V2 version of the API.
    type: object
    properties:
      operations:
        description: >-
          Available operations in the V2 version of the API:
        
          - createSubscriptions: Create tag subscriptions
          
          - createSelections: Select a group of tags
          
          - createTags: Create tags
          
          - deleteTags: Delete tags
          
          - getTagMetadata: Get information about tags
          
          - readTagValues: Read tag values
          
          - updateTagMetadata: Update information about tags
          
          - writeTagValues: Update tag values
        properties:
          createSubscriptions:
            $ref: '#/definitions/Operation'
          createSelections:
            $ref: '#/definitions/Operation'
          createTags:
            $ref: '#/definitions/Operation'
          deleteTags:
            $ref: '#/definitions/Operation'
          getTagMetadata:
            $ref: '#/definitions/Operation'
          readTagValues:
            $ref: '#/definitions/Operation'
          updateTagMetadata:
            $ref: '#/definitions/Operation'
          writeTagValues:
            $ref: '#/definitions/Operation'
  Error:
    description: Contains error information.
    type: object
    properties:
      name:
        description: String error code.
        type: string
      code:
        description: Numeric error code.
        type: integer
      resourceType:
        description: Type of resource associated with the error.
        type: string
      resourceId:
        description: Identifier of the resource associated with the error.
        type: string
      message:
        description: Complete error message.
        type: string
      args:
        description: Positional argument values for the error code.
        type: array
        items:
          type: string
      innerErrors:
        type: array
        items:
          $ref: '#/definitions/Error'
    example:
      name: Tag.NoSuchTag
      code: -251909
      resourceType:
      resourceId:
      message: "No such tag: 'foo'"
      args: ['foo']
  TagType:
    type: string
    title: Tag Data Type
    enum: [DOUBLE, INT, STRING, BOOLEAN, U_INT64, DATE_TIME]
  TagWithValue:
    description: A tag and its current value.
    type: object
    title: Tag With Value
    properties:
      tag:
        $ref: '#/definitions/Tag'
      current:
        $ref: '#/definitions/TimestampedTagValue'
      aggregates:
        $ref: '#/definitions/V2TagAggregates'
    example:
      tag:
        path: foo
        type: DOUBLE
        keywords: [fooKeyword, barKeyword]
      current:
        value:
          type: DOUBLE
          value: "3.14"
        timestamp: '2018-09-04T18:45:08Z'
      aggregates:
        min: "0.0"
        max: "5.0"
        avg: 2.0
        count: 5
  TagValue:
    description: Value of a tag.
    type: object
    title: Tag Value
    required: [value,type]
    properties:
      value:
        type: string
      type:
        $ref: '#/definitions/TagType'
    example:
      type: DOUBLE
      value: "3.14"
  TagPathWithCountAggregate:
    type: object
    title: Tag Path with Count Aggregate
    properties:
      path:
        type: string
      count:
        description: Count value from the tag's aggregates.
        type: integer
      workspace:
        type: string
    example:
      path: foo
      count: 1
      workspace: "f0144202-52d5-4861-98fa-615ed4b2f751"
  TagPathWithCurrentAndAggregateValue:
    description: Tag path with its current value and aggregates.
    type: object
    title: Tag Path Current And Aggregate Value
    properties:
      path:
        type: string
      current:
        $ref: '#/definitions/TimestampedTagValue'
      aggregates:
        $ref: '#/definitions/V2TagAggregates'
      workspace:
        type: string
    example:
      path: foo
      current:
        value:
          type: DOUBLE
          value: "3.14"
      aggregates:
        min: "0.0"
        max: "5.0"
        avg: 2.0
        count: 5
      workspace: "f0144202-52d5-4861-98fa-615ed4b2f751"
  TagPathWithTimestampedValue:
    description: Tag path with timestamped value.
    type: object
    title: Tag Path with Timestamped Value
    properties:
      path:
        type: string
        description: Tag path.
      current:
        $ref: '#/definitions/TimestampedTagValue'
      workspace:
        type: string
    example:
      path: foo
      current:
        value:
          type: DOUBLE
          value: "3.14"
        timestamp: '2018-09-04T18:45:08Z'
      workspace: "f0144202-52d5-4861-98fa-615ed4b2f751"
  TagPathWithValue:
    description: Tag path with value.
    type: object
    title: Tag Path With Value
    properties:
      path:
        type: string
        description: Tag path.
      current:
        $ref: '#/definitions/TagValue'
      workspace:
        type: string
    example:
      path: foo
      current:
        type: DOUBLE
        value: "3.14"
      workspace: "f0144202-52d5-4861-98fa-615ed4b2f751"
  TagPathWithTimestamp:
    type: object
    title: Tag Path with Timestamp
    description: A tag path and the timestamp of its current value.
    properties:
      timestamp:
        description: Timestamp associated with the current value.
        type: string
        format: date-time
        example: '2018-09-04T18:45:08Z'
      path:
        type: string
      workspace:
        type: string
    example:
      timestamp: '2018-09-04T18:45:08Z'
      path: foo
      workspace: "f0144202-52d5-4861-98fa-615ed4b2f751"
  TagPathWithMaxAggregate:
    type: object
    title: Tag Path With Max Aggregate
    properties:
      path:
        type: string
      max:
        description: Maximum value from the tag's aggregates.
        type: string
      workspace:
        type: string
    example:
      path: foo
      max: "1"
      workspace: "f0144202-52d5-4861-98fa-615ed4b2f751"
  TagPathWithMinAggregate:
    type: object
    title: Tag Path with Min Aggregate
    properties:
      path:
        type: string
      min:
        description: Minimum value from the tag's aggregates.
        type: string
      workspace:
        type: string
    example:
      path: foo
      min: "1"
      workspace: "f0144202-52d5-4861-98fa-615ed4b2f751"
  TagPathWithMeanAggregate:
    type: object
    title: Tag Path with Mean Aggregate
    properties:
      path:
        type: string
      avg:
        description: Mean value from the tag's aggregates.
        type: number
        format: double
      workspace:
        type: string
    example:
      path: foo
      avg: 1
      workspace: "f0144202-52d5-4861-98fa-615ed4b2f751"
  TagQuery:
    type: object
    title: Tag Query
    properties:
      filter:
        type: string
        description: >-
          The filter criteria for tags. Consists of a string of queries composed using AND/OR operators.
          String values and date strings need to be enclosed in double quotes.
          Parentheses can be used around filters to better define the order of operations.


          Filter syntax: '[property name][operator][operand] and [property name][operator][operand]'


          Operators:

          - Equals operator '='. Example: 'x = y'

          - Not equal operator '!='. Example: 'x != y'

          - Greater than operator '>'. Example: 'x > y'

          - Greater than or equal operator '>='. Example: 'x >= y'

          - Less than operator '<'. Example: 'x < y'

          - Less than or equal operator '<='. Example: 'x <= y'

          - Logical AND operator 'and' or '&&'. Example: 'x and y'

          - Logical OR operator 'or' or '||'. Example: 'x or y'

          - Contains operator '.Contains()', which is used to check if a list contains an element. Example: 'x.Contains(y)'

          - Not Contains operator '!.Contains()', which is used to check if a list does not contain an element. Example: '!x.Contains(y)'


          Valid tag properties that can be used in the filter:

          - path : String representing the tag path. May include glob-style wildcards.

          - type: Tag type. Example: INT

          - keywords: Tag keywords. Example: keywords.Contains(x)

          - properties: Tag properties. Example: properties['x'] = 'y'

          - workspace : The workspace of the tags. Example: 88974b87-07d4-4f84-b54f-48eec89b11ed
      orderBy:
        description: >-
          The tag value property to order results by; value and timestamp are from the current tag value.
          When ordering by value, tags will be grouped by type, first numbers (INT, DOUBLE, U_INT64), then strings,
          then booleans, then times. Null values will be at the end of the list regardless of type.
        type: string
        enum: [PATH, VALUE, TIMESTAMP, WORKSPACE]
        default: PATH
      descending:
        description: A Boolean that determines whether to return the tags in descending order.
        type: boolean
        default: false
      projection:
        description: The tag metadata and value fields to return.
        type: string
        default: ''
      continuationToken:
        description: >-
          A token used for resuming a query at the next item in the matching tag set; to
          obtain the next page of steps, pass the token to the service on a subsequent request.
        type: string
      take:
        description: Maximum number of tags to return.
        type: number
        default: 100000
        minimum: -1
    example:
      filter: (path = "*.tag1") OR keywords.Contains("key1")
      orderBy: TIMESTAMP
      descending: true
      projection: new(tag.path as path,current)
      continuationToken: token
      take: 20
  TimestampedTagValue:
    description: Current value of a tag.
    type: object
    title: Timestamped Tag Value
    properties:
      value:
        $ref: '#/definitions/TagValue'
      timestamp:
        description: Timestamp associated with the value.
        type: string
        format: date-time
    example:
      value:
        type: DOUBLE
        value: "3.14"
      timestamp: '2018-09-04T18:45:08Z'
  TagCurrentAndAggregateValue:
    type: object
    title: Tag Current And Aggregate Value
    properties:
      current:
        $ref: '#/definitions/TimestampedTagValue'
      aggregates:
        $ref: '#/definitions/V2TagAggregates'
    example:
      current:
        value:
          type: DOUBLE
          value: "3.14"
        timestamp: '2018-09-04T18:45:08Z'
      aggregates:
        min: "0.0"
        max: "5.0"
        avg: 2.0
        count: 5
  V1TagAggregates:
    description: Aggregate values of a tag
    type: object
    title: Tag Aggregate Value
    properties:
      min:
        description: Minimum aggregate value.
        type: number
        format: double
      max:
        description: Maximum aggregate value.
        type: number
        format: double
      count:
        description: Count aggregate value.
        type: integer
      avg:
        description: Mean aggregate value.
        type: number
        format: double
    example:
      min: 0
      max: 5
      avg: 2.0
      count: 5
  V2TagAggregates:
    description: Aggregate values of a tag.
    type: object
    title: Tag Aggregate Value
    properties:
      min:
        description: Minimum aggregate value.
        type: string
      max:
        description: Maximum aggregate value.
        type: string
      count:
        description: Count aggregate value.
        type: integer
      avg:
        description: Mean aggregate value.
        type: number
        format: double
    example:
      min: "0.0"
      max: "5.0"
      avg: 2.0
      count: 5
  Tag:
    description: Object containing a tag's metadata, excluding current and aggregate values.
    type: object
    title: Tag Data
    required: [path,type]
    properties:
      type:
        $ref: '#/definitions/TagType'
      properties:
        type: object
        additionalProperties:
          type: string
      path:
        type: string
      keywords:
        type: array
        items:
          type: string
      collectAggregates:
        type: boolean
      workspace:
        type: string
    example:
      type: DOUBLE
      properties:
        key1: value1
        key2: value2
      path: foo
      keywords: [fooKeyword, barKeyword]
      collectAggregates: true
      workspace: "10e020d7-64df-45e9-b717-c537f374ca2f"
  TagUpdate:
    description: Object containing a tag's path, and one or more values to update the tag with at times you specify.
    type: object
    title: Tag Update
    required: [path,updates]
    properties:
      path:
        type: string
      updates:
        type: array
        items:
          $ref: '#/definitions/TimestampedTagValue'
      workspace:
        type: string
    example:
      path: foo
      updates:
        - value:
            type: DOUBLE
            value: "3.14"
          timestamp: '2018-09-04T18:45:08Z'
        - value:
            type: DOUBLE
            value: "5.0"
          timestamp: '2018-09-04T18:45:08Z'
      workspace: "bbcd6db8-10f6-4caf-af28-81157b741a5a"
  V1SubscriptionUpdate:
    description: Updates for a subscriptions.
    type: object
    title: Subscription Update
    properties:
      updates:
        type: array
        items:
          $ref: '#/definitions/V1SubscriptionTagUpdate'
      subscriptionId:
        type: string
      nonexistentTags:
        description: List of tags which did not exist.
        type: array
        items:
          type: string
      deletedTags:
        description: List of tags which have been deleted.
        type: array
        items:
          type: string
      createdTags:
        description: List of tags which have been created.
        type: array
        items:
          type: string
      alias:
        description: Name of the subscription.
        type: string
  V2SubscriptionUpdate:
    description: Updates for a subscriptions.
    type: object
    title: Subscription Update
    properties:
      updates:
        type: array
        items:
          $ref: '#/definitions/V2SubscriptionTagUpdate'
      subscriptionId:
        type: string
      nonexistentTags:
        description: List of tags which did not exist.
        type: array
        items:
          type: string
      deletedTags:
        description: List of tags which have been deleted.
        type: array
        items:
          type: string
      createdTags:
        description: List of tags which have been created.
        type: array
        items:
          type: string
      alias:
        description: Name of the subscription.
        type: string
  V1SubscriptionTagUpdate:
    description: Update details for a tag subscription.
    type: object
    title: Subscription Tag Update
    properties:
      value:
        description: Updated tag value.
        type: string
      type:
        $ref: '#/definitions/TagType'
      timestamp:
        description: Updated timestamp.
        type: string
        format: date-time
      tag:
        $ref: '#/definitions/Tag'
      aggregates:
        $ref: '#/definitions/V1TagAggregates'
    example:
      value: "5.0"
      type: DOUBLE
      timestamp: '2018-09-04T18:45:08Z'
      tag:
        type: DOUBLE
        properties:
          key1: value1
          key2: value2
        path: foo
        keywords: [fooKeyword, barKeyword]
      aggregates:
        min: 0
        max: 5
        avg: 2.0
        count: 5
  V2SubscriptionTagUpdate:
    description: Update details for a tag subscription.
    type: object
    title: Subscription Tag Update
    properties:
      value:
        description: Updated tag value.
        type: string
      type:
        $ref: '#/definitions/TagType'
      timestamp:
        description: Updated timestamp.
        type: string
        format: date-time
      tag:
        $ref: '#/definitions/Tag'
      aggregates:
        $ref: '#/definitions/V2TagAggregates'
    example:
      value: "5.0"
      type: DOUBLE
      timestamp: '2018-09-04T18:45:08Z'
      tag:
        type: DOUBLE
        properties:
          key1: value1
          key2: value2
        path: foo
        keywords: [fooKeyword, barKeyword]
      aggregates:
        min: "0.0"
        max: "5.0"
        avg: 2.0
        count: 5
  Subscription:
    description: Object describing a subscription's metadata.
    type: object
    title: Subscription
    required: [tags]
    properties:
      updatesOnly:
        description: Whether to notify only about updates.
        type: boolean
        default: false
      tags:
        description: List of subscribed tag paths.
        type: array
        items:
          type: string
      alias:
        description: Name of the subscription.
        type: string
      workspace:
        description: Workspace of the tags to subscribe to.
        type: string
    example:
      updatesOnly: true
      tags: [tag1, tag2, tag3]
      alias: foo
      workspace: "3e884a30-5623-4403-932b-375a715ef065"
  SubscriptionIds:
    type: object
    properties:
      subscriptionIds:
        type: array
        items:
          type: string
  Selection:
    description: Object describing a selection's metadata.
    type: object
    title: Selection
    required:
      - searchPaths
    properties:
      searchPaths:
        type: array
        items:
          type: string
      inactivityTimeout:
        description: Inactivity timeout in seconds.
        type: integer
        maximum: 900
        default: 900
      id:
        type: string
      workspace:
        description: Workspace of the tags to select.
        type: string
    example:
      searchPaths: [tag1, tag2, tag3]
      inactivityTimeout: 1000
      id: 22520497-e85b-427f-980c-ca328fc72f75
      workspace: "3e884a30-5623-4403-932b-375a715ef065"
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=tag-historian/nitaghistorian.yml sha256=aaef6d34e3f9baf9b60cd9eb55d737cd651bbd510db97fb4ebb29795c2b16269 bytes=43649 -->
## FILE: tag-historian/nitaghistorian.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `tag-historian/nitaghistorian.yml`
- sha256: `aaef6d34e3f9baf9b60cd9eb55d737cd651bbd510db97fb4ebb29795c2b16269`
- bytes: 43649

````yaml
swagger: '2.0'
info:
  version: '1'
  title: Tag Historian Web Service
  description: SystemLink Tag Historian Service HTTP API.
  contact:
    name: NI
    url: 'https://www.ni.com/systemlink'
    email: support@ni.com
basePath: /nitaghistorian
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
      message:
        description: Complete error message
        type: string
      args:
        description: Positional argument values for the error code
        type: array
        items:
          type: string
    example:
      name: TagHistorian.InvalidId
      code: -251913
      message: 'Invalid id: 5c88d2ae26b41e22f08b4407.'
      args: []
  ErrorEntry:
    description: Populated with any errors that occur when performing multiple operations in a single
      request, with one inner error per failed operation.
    title: Error Entry
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
      resourceType:
        description: Type of resource associated with the error
        type: string
      resourceId:
        description: Identifier of the resource associated with the error
        type: string
      innerErrors:
        type: array
        items:
          $ref: '#/definitions/ErrorEntry'
    example:
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251040
      message: One or more errors occurred. See the contained list for details of each error.
      args: []
      innerErrors:
        - name: TagHistorian.DatabaseError
          code: -253304
          resourceType: tag
          resourceId: system2.tag1
          message: Database error.
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
        description: >-
          Available operations in the v1 version of the API:

          - queryHistoricalTagValues: The ability to read historical tag values

          - modifyHistoricalTagValues: The ability to modify properties of historical tag values

        type: object
        properties:
          queryHistoricalTagValues:
            $ref: '#/definitions/Operation'
          modifyHistoricalTagValues:
            $ref: '#/definitions/Operation'
  HttpHistoricalValue:
    type: object
    title: Http Historical Value
    properties:
      value:
        description: The value of the tag at the time it was written, converted to a string.
        type: string
        example: '12.87'
      timestamp:
        description: The ISO-8601 formatted timestamp when the historical value was written, in UTC.
        type: string
        format: date-time
        example: '2019-03-13T09:51:38Z'
  HistoricalTagDecimatedQuery:
    description: Defines how decimated historical values are queried and for which tags. Only used for web
      socket messages.
    type: object
    title: Historical Tag Decimated Query
    properties:
      paths:
        description: One or more paths identifying the tags whose decimated historical values should be returned.
        type: array
        items:
          type: string
        example:
          - system1.tag1
          - system2.tag1
      workspace:
        description: The workspace ID for querying decimated tag values. If this is not specified, the tag values from the default workspace will be returned.
        type: string
        example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
      startTime:
        description: Limits the returned historical values to those written at or after the given
          time in ISO-8601 format.
        type: string
        format: date-time
        example: '2018-09-04T18:45:08Z'
        default: '0001-01-01T00:00:00Z'
      endTime:
        description: Limits the returned historical values to those written at or before the given
          time in ISO-8601 format.
        type: string
        format: date-time
        example: '2018-09-04T18:45:08Z'
        default: '0001-01-01T00:00:00Z'
      decimation:
        description: When non-zero, the returned historical values are decimated across requested time
          span divided into the specified number of equal-sized intervals.
        type: integer
        minimum: 0
        default: 0
      sortOrder:
        description: Specifies ascending or descending order to return historical values, based
          on when each tag was written.
        type: string
        enum: [ASCENDING, DESCENDING]
        default: ASCENDING
  HistoricalTagUndecimatedQuery:
    description: Defines how undecimated historical values are queried and for which tags. Only used for web
      socket messages.
    type: object
    title: Historical Tag Undecimated Query
    properties:
      paths:
        description: One or more paths identifying the tags whose undecimated historical values should be returned.
        type: array
        items:
          type: string
        example:
          - system1.tag1
          - system2.tag1
      workspace:
        description: The workspace ID for querying tag values. If this is not specified, the tag values from the default workspace will be returned.
        type: string
        example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
      startTime:
        description: Limits the returned historical values to those written at or after the given
          time in ISO-8601 format.
        type: string
        format: date-time
        example: '2018-09-04T18:45:08Z'
        default: '0001-01-01T00:00:00Z'
      endTime:
        description: Limits the returned historical values to those written at or before the given
          time in ISO-8601 format.
        type: string
        format: date-time
        example: '2018-09-04T18:45:08Z'
        default: '0001-01-01T00:00:00Z'
      take:
        description: Limits the returned historical values to the specified number of values. Use
          with the continuationToken property to implement pagination. Only applies when not specifying a decimation.
        type: integer
        minimum: 0
        default: 0
        example: 1
      continuationToken:
        type: string
        description: For non-decimated queries, a value generated by the server which should be sent
          in the next request to retrieve the next page of values.
        default: ''
      sortOrder:
        description: Specifies ascending or descending order to return historical values, based
          on when each tag was written.
        type: string
        enum: [ASCENDING, DESCENDING]
        default: ASCENDING
  HistoricalValue:
    type: object
    title: Historical Value
    properties:
      path:
        description: The path of the tag corresponding to the historical value.
        type: string
        example: system1.tag1
      workspace:
        description: The workspace ID of the tag
        type: string
        example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
      value:
        description: The value of the tag at the time it was written, converted to a string.
        type: string
        example: '12.87'
      timestamp:
        description: The ISO-8601 formatted timestamp that the historical value was written, in UTC.
        type: string
        format: date-time
        example: '2019-03-13T09:51:38Z'
  TypeAndValues:
    type: object
    title: TypeAndValues
    properties:
      type:
        description: The type of the values
        type: string
        enum: [DOUBLE, INT, STRING, BOOLEAN, U_INT64, DATE_TIME]
      values:
        description: The values, encoded as strings
        type: array
        items:
          $ref: '#/definitions/HttpHistoricalValue'
  TagHistorianValues:
    type: object
    title: Tag Historian Values
    properties:
      results:
        description: An object containing the historical values for each requested tag that
          was successfully queried. The object's property names correspond to a tag path.
        type: object
        additionalProperties:
          $ref: '#/definitions/TypeAndValues'
        example:
          system1.tag1:
            type: DOUBLE
            values:
              - value: '12.87'
                timestamp: '2019-03-13T09:51:38Z'
              - value: '3.2'
                timestamp: '2019-03-14T09:51:38Z'
      workspace:
        description: The workspace ID of the tag values
        type: string
        example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
      error:
        description: This value is always null.
        type: object
        example: null
      failed:
        description: This value is always null.
        type: object
        example: null
  HistoricalTagAsyncDecimatedQueryJob:
    description: Information about an asynchronous decimated query.
    title: Historical Tag Async Decimated Query Job
    type: object
    properties:
      query:
          $ref: '#/definitions/HistoricalTagDecimatedQuery'
      requestId:
        description: The identifier of the asynchronous query to associate with a result in a later message.
        type: string
        example: '4cbba25a-c1b8-4fbe-8829-9ddfde555188'
      hasError:
        description: Whether the query had an error and cannot be completed.
        type: boolean
  HistoricalTagAsyncUndecimatedQueryJob:
    description: Information about an asynchronous undecimated query.
    title: Historical Tag Async Undecimated Query Job
    type: object
    properties:
      query:
        $ref: '#/definitions/HistoricalTagUndecimatedQuery'
      requestId:
        description: The identifier of the asynchronous query to associate with a result in a later message.
        type: string
        example: '4cbba25a-c1b8-4fbe-8829-9ddfde555188'
      hasError:
        description: Whether the query had an error and cannot be completed.
        type: boolean
  WebSocketAsyncDecimatedQueryRequest:
    title: Web Socket Async Decimated Query Request
    description: A web socket message sent by the client to asynchronously query for decimated historical tag
      values. The server will respond with a *WebSocketAsyncDecimatedQueryResponse* message confirming the start
      of the query, a *WebSocketAsyncQueryData* message for each query as they complete, and finally
      a *WebSocketAsyncDecimatedQueryComplete* once all queries have completed.
    type: object
    required:
      - action
      - queries
    properties:
      action:
        description: The action to perform. Must be set to "TagHistorianAsyncDecimatedQueryRequest".
        type: string
        enum: ['TagHistorianAsyncDecimatedQueryRequest']
        example: TagHistorianAsyncDecimatedQueryRequest
      queries:
        description: The list of historical queries to perform.
        type: array
        items:
          $ref: '#/definitions/HistoricalTagDecimatedQuery'
    example:
      action: TagHistorianAsyncDecimatedQueryRequest
      queries:
        - decimation: 1000
          endTime: '9999-01-01T00:00:00Z'
          sortOrder: ASCENDING
          startTime: '0001-01-01T00:00:00Z'
          paths: [system1.tag1]
  WebSocketAsyncUndecimatedQueryRequest:
    title: Web Socket Async Undecimated Query Request
    description: A web socket message sent by the client to asynchronously query for undecimated historical tag
      values. The server will respond with a *WebSocketAsyncUndecimatedQueryResponse* message confirming the start
      of the query, a *WebSocketAsyncQueryData* message for each query as they complete, and finally
      a *WebSocketAsyncUndecimatedQueryComplete* once all queries have completed.
    type: object
    required:
      - action
      - queries
    properties:
      action:
        description: The action to perform. Must be set to "TagHistorianAsyncUndecimatedQueryRequest".
        type: string
        enum: ['TagHistorianAsyncUndecimatedQueryRequest']
        example: TagHistorianAsyncUndecimatedQueryRequest
      queries:
        description: The list of historical queries to perform.
        type: array
        items:
          $ref: '#/definitions/HistoricalTagDecimatedQuery'
    example:
      action: TagHistorianAsyncUndecimatedQueryRequest
      queries:
        - endTime: '9999-01-01T00:00:00Z'
          sortOrder: ASCENDING
          startTime: '0001-01-01T00:00:00Z'
          paths: [system1.tag1]
  WebSocketAsyncDecimatedQueryResponse:
    title: Web Socket Async Decimated Query Response
    description: A web socket message sent by the server to confirm a *WebSocketAsyncDecimatedQueryRequest* sent
      by the client. A *WebSocketAsyncQueryData* message will be sent for each query as they complete
      and a *WebSocketAsyncDecimatedQueryComplete* once all queries have completed.
    type: object
    properties:
      action:
        description: The action performed. Must be set to "TagHistorianAsyncDecimatedQueryResponse".
        type: string
        enum: ['TagHistorianAsyncDecimatedQueryResponse']
        example: TagHistorianAsyncQueryResponse
      queryJobs:
        description: A list containing the information about each query started.
        type: array
        items:
          $ref: '#/definitions/HistoricalTagAsyncDecimatedQueryJob'
  WebSocketAsyncUndecimatedQueryResponse:
    title: Web Socket Async Undecimated Query Response
    description: A web socket message sent by the server to confirm a *WebSocketAsyncUndecimatedQueryRequest* sent
      by the client. A *WebSocketAsyncQueryData* message will be sent for each query as they complete
      and a *WebSocketAsyncUndecimatedQueryComplete* once all queries have completed.
    type: object
    properties:
      action:
        description: The action performed. Must be set to "TagHistorianAsyncUndecimatedQueryResponse".
        type: string
        enum: ['TagHistorianAsyncUndecimatedQueryResponse']
        example: TagHistorianAsyncQueryResponse
      queryJobs:
        description: A list containing the information about each query started.
        type: array
        items:
          $ref: '#/definitions/HistoricalTagAsyncUndecimatedQueryJob'
  WebSocketAsyncQueryData:
    title: Web Socket Async Query Data
    description: A web socket message sent by the server containing the result of a single completed
      asychronous query job and contains the result of the query. The server will send one of these
      messages as each query completes, followed by a single *WebSocketAsyncQueryComplete* message
      once all queries have completed.
    allOf:
      - type: object
        properties:
          action:
            description: The action performed. Must be set to "TagHistorianAsyncQueryDataRoutedMessage".
            type: string
            enum: ['TagHistorianAsyncQueryDataRoutedMessage']
            example: TagHistorianAsyncQueryDataRoutedMessage
          requestId:
            description: The identifier of the completed asynchronous query as given in the corresponding
              *WebSocketAsyncQueryResponse* message.
            type: string
            example: '4cbba25a-c1b8-4fbe-8829-9ddfde555188'
      - $ref: '#/definitions/TagHistorianValues'
  WebSocketAsyncDecimatedQueryComplete:
    title: Web Socket Async Decimated Query Complete
    description: A web socket message sent by the server indicating that all asynchronous queries
      for a single decimated query request are complete.
    type: object
    properties:
      action:
        description: The action performed. Must be set to "TagHistorianAsyncDecimatedQueryCompleteRoutedMessage".
        type: string
        enum: ['TagHistorianAsyncDecimatedQueryCompleteRoutedMessage']
        example: TagHistorianAsyncDecimatedQueryCompleteRoutedMessage
      queryJobs:
        description: A list containing the information about each query started.
        type: array
        items:
          $ref: '#/definitions/HistoricalTagAsyncDecimatedQueryJob'
  WebSocketAsyncUndecimatedQueryComplete:
    title: Web Socket Async Undecimated Query Complete
    description: A web socket message sent by the server indicating that all asynchronous undecimated queries
      for a single request are complete.
    type: object
    properties:
      action:
        description: The action performed. Must be set to "TagHistorianAsyncUndecimatedQueryCompleteRoutedMessage".
        type: string
        enum: ['TagHistorianAsyncUndecimatedQueryCompleteRoutedMessage']
        example: TagHistorianAsyncUndecimatedQueryCompleteRoutedMessage
      queryJobs:
        description: A list containing the information about each query started.
        type: array
        items:
          $ref: '#/definitions/HistoricalTagAsyncUndecimatedQueryJob'
  WebSocketSubscribeRequest:
    title: Web Socket Subscribe Request
    description: A web socket message sent by the client to subscribe to notifications when one or more
      tags have recorded new historical values. The server will send a *WebSocketSubscribeResponse*
      message to confirm the subscription and a *WebSocketAsyncValuesProcessed* message to notify of
      new values. Clients may send a *WebSocketUnsubscribeRequest* message to stop future notifications
      without closing the connection.
    type: object
    required:
      - action
      - searchPaths
    properties:
      action:
        description: The action to perform. Must be set to "TagHistorianAsyncSubscribeRequest".
        type: string
        enum: ['TagHistorianAsyncSubscribeRequest']
        example: TagHistorianAsyncSubscribeRequest
      searchPaths:
        description: Contains one or more tag paths to subscribe to. The paths may contain wildcards
          to subscribe to similar tags.
        type: array
        items:
          type: string
        example:
          - 'system1.tag1'
          - 'system2.*'
          - '*.tag2'
      workspace:
        description: The workspace ID to subscribe to for tag updates. If this is not specified, the tag values from the default workspace will be returned.
        type: string
        example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
  WebSocketSubscribeResponse:
    title: Web Socket Subscribe Response
    description: A web socket message sent by the server to confirm a *WebSocketSubscribeRequest* sent
      by the client. A *WebSocketAsyncValuesProcessed* message will be sent each time new values are
      available.
    type: object
    properties:
      action:
        description: The action performed. Must be set to "TagHistorianAsyncSubscribeResponse".
        type: string
        enum: ['TagHistorianAsyncSubscribeResponse']
        example: TagHistorianAsyncSubscribeResponse
  WebSocketAsyncValuesProcessed:
    title: Web Socket Async Values Processed
    description: A web socket message sent by the server when new historical values are available
      for any of the tags the client has subscribed to via a *WebSocketSubscribeRequest* message.
    type: object
    properties:
      action:
        description: The action performed. Must be set to "TagHistorianAsyncValuesProcessedRoutedMessage".
        type: string
        enum: ['TagHistorianAsyncValuesProcessedRoutedMessage']
        example: TagHistorianAsyncValuesProcessedRoutedMessage
      values:
        description: The newly recorded historical values.
        type: array
        items:
          $ref: '#/definitions/HistoricalValue'
  WebSocketUnsubscribeRequest:
    title: Web Socket Unsubscribe Request
    description: A web socket message sent by the client to unsubscribe from notifications when one or
      more tags have recorded new historical values created by a previous *WebSocketSubscribeRequest*.
      The server will respond with a *WebSocketUnsubscribeResponse* message to confirm.
    type: object
    required:
      - action
      - searchPaths
    properties:
      action:
        description: The action to perform. Must be set to "TagHistorianAsyncUnsubscribeRequest".
        type: string
        enum: ['TagHistorianAsyncUnsubscribeRequest']
        example: TagHistorianAsyncUnsubscribeRequest
      searchPaths:
        description: Contains one or more tag paths to unsubscribe from. Paths must exactly match
          search paths used in the subscribe request to be unsubscribed, including wildcards.
          Specify the special value *\*\*\** (three wildcard characters) to unsubscribe from all tags.
        type: array
        items:
          type: string
      workspace:
        description: The workspace ID to unsubscribe from for tag updates. If this is not specified, the default workspace is assumed.
        type: string
        example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
  WebSocketUnsubscribeResponse:
    title: Web Socket Unsubscribe Response
    description: A web socket message sent by the server to confirm a *WebSocketUnsubscribeRequest*.
    type: object
    properties:
      action:
        description: The action performed. Must be set to "TagHistorianAsyncUnsubscribeResponse".
        type: string
        enum: ['TagHistorianAsyncUnsubscribeResponse']
        example: TagHistorianAsyncUnsubscribeResponse
  DeleteRangeOfValues:
    title: Delete Range of Values
    description: Defines the range of values to delete for a tag.
    type: object
    properties:
      path:
        description: A tag path identifying the tag whose historical values in the range should
          be deleted.
        type: string
        example: system1.tag1
      startTime:
        description: Limits the range of historical values being deleted to those written at or after the
          given time in ISO-8601 format.
        type: string
        format: date-time
        example: '2000-01-01T00:00:00Z'
      endTime:
        description: Limits the range of historical values being deleted to those written at or before the
          given time in ISO-8601 format.
        type: string
        format: date-time
        example: '2099-01-01T00:00:00Z'
      workspace:
        description: The workspace ID for the tag. If this is not specified, the default workspace will be used.
        type: string
        example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
  InsertValue:
    title: Insert Value
    description: Defines a value to insert for a tag.
    type: object
    required:
      - path
      - timestamp
      - value
    properties:
      path:
        description: The path of the tag for which to insert the value.
        type: string
        example: system1.tag1
      timestamp:
        description: The timestamp for the new value in ISO-8601 format.
        type: string
        format: date-time
        example: '2018-09-04T18:45:08Z'
      value:
        description: The value to insert.
        type: string
        example: '1234'
      workspace:
        description: The workspace ID for the tag. If this is not specified, the default workspace will be used.
        type: string
        example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
  UpdateMetadata:
    title: Update Metadata
    description: Defines metadata values to update on a tag.
    type: object
    required:
      - path
      - type
      - retention
    properties:
      path:
        description: The path of the tag for which to update metadata.
        type: string
        example: system1.tag1
      type:
        description: Tag Data Type
        type: string
        enum: [BOOLEAN, INT, U_INT64, DATE_TIME, DOUBLE, STRING]
      retention:
        description: Retention period for tag values
        type: string
        enum: [COUNT, DURATION, PERMANENT, NONE]
      maxHistoryCount:
        description: For COUNT retention, it indicates the maximum number of tag istoric values that should be stored
        type: integer
        minimum: 0
      historyTTLDays:
        description: For DURATION retention, it indicates the maximum number of days the tag values should be stored
        type: integer
        minimum: 0
      workspace:
        description: The workspace ID of the tag. If not specified, the default workspace will be used.
        type: string
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
    description: Not authorized
    headers:
      WWW_Authenticate:
        description: Information for how to authenticate
        type: string
paths:
  /:
    get:
      tags: [versioning]
      summary: API information
      description: Returns information about API versions and available operations.
      operationId: RootEndpoint
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
              version:
                description: Implementation version of the web service
                type: string
                example: 18.0.0.1722
  /{version}:
    parameters:
      - in: path
        name: version
        description: Version of the API to retrieve operations.
        type: string
        required: true
    get:
      tags: [versioning]
      summary: API version information
      description: Returns available operations for a single version of the API.
      operationId: RootEndpointWithVersion
      # Explicitly mark security as an empty array - this route does not require any privileges.
      # Marking it this way prevents it from inheriting the top-level security settings.
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
  /v2/tags/query-history:
    post:
      tags: [history]
      summary: Read historical tag values
      description: Queries for the historical values of one or more tags.
      operationId: QueryHistory
      x-ni-operation: queryHistoricalTagValues
      produces:
        - application/json
      parameters:
        - in: body
          name: Request body
          required: true
          description: Defines how historical values are queried and for which tags.
          schema:
            description: Defines how historical values are queried and for which tags.
            type: object
            title: Http Query Request Body
            properties:
              path:
                description: A tag path identifying the tag whose historical values should
                  be returned.
                type: string
                example: system1.tag1
              workspace:
                description: The workspace ID for querying tag values. If this is not specified, the tag values from the default workspace will be returned.
                type: string
                example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
              startTime:
                description: Limits the returned historical values to those written at or after at the
                  given time in ISO-8601 format.
                type: string
                format: date-time
                example: '2018-09-04T18:45:08Z'
                default: '0001-01-01T00:00:00Z'
              endTime:
                description: Limits the returned historical values to those written at or before the
                  given time in ISO-8601 format.
                type: string
                format: date-time
                example: '2018-09-04T18:45:08Z'
                default: '9999-12-31T23:59:59Z'
              take:
                description: Limits the returned historical values to the specified number of values. Use
                  with the continuationToken property to implement pagination. Only applies when not specifying a decimation.
                type: integer
                minimum: 0
                default: 0
                example: 1
              continuationToken:
                description: For non-decimated queries, a value generated by the server which should be sent
                  in the next request to retrieve the next page of values.
                type: string
                default: ''
              sortOrder:
                description: Specifies the order to return historical values, either ascending or
                  descending order based on when each tag value was written.
                type: string
                enum: [ASCENDING, DESCENDING]
                default: ASCENDING
      responses:
        200:
          description: OK
          schema:
            type: object
            title: Http Query Response Body
            properties:
              values:
                description: An array of HttpHistoricalValue elements
                type: array
                items:
                  $ref: '#/definitions/HttpHistoricalValue'
              continuationToken:
                description: For non-decimated queries, a value generated by the server which should be sent
                  in the next request to retrieve the next page of values.
                type: string
                default: ''
              workspace:
                description: The workspace ID of the tag values
                type: string
                example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
              error:
                $ref: '#/definitions/ErrorEntry'
              failed:
                description: The paths of the tags that had errors.
                type: array
                items:
                  type: string
                example: [system2.tag1]
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/query-decimated-history:
    post:
      tags: [history]
      summary: Read decimated historical tag values
      description: Queries for the decimated historical data for one or more tags
      operationId: QueryDecimatedHistory
      x-ni-operation: queryDecimatedHistoricalTagValues
      produces:
        - application/json
      parameters:
        - in: body
          name: Request body
          required: true
          description: Defines how historical values are queried and for which tags.
          schema:
            description: Defines how historical values are queried and for which tags.
            type: object
            title: Http Query Request Body
            properties:
              paths:
                description: One or more paths identifying the tags whose historical values should
                  be returned.
                type: array
                items:
                  type: string
                example:
                  - system1.tag1
                  - system2.tag1
              workspace:
                description: The workspace ID for querying decimated tag values. If this is not specified, the tag values from the default workspace will be returned.
                type: string
                example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
              startTime:
                description: Limits the returned historical values to those written at or after at the
                  given time in ISO-8601 format.
                type: string
                format: date-time
                example: '2018-09-04T18:45:08Z'
                default: '0001-01-01T00:00:00Z'
              endTime:
                description: Limits the returned historical values to those written at or before the
                  given time in ISO-8601 format.
                type: string
                format: date-time
                example: '2018-09-04T18:45:08Z'
                default: '9999-12-31T23:59:59Z'
              decimation:
                description: The number of intervals to break the data between start and end time up into. The
                  service will return the entry, exit, min, and max value for each interval.
                type: integer
                minimum: 1
                default: 500
              sortOrder:
                description: Specifies the order to return historical values, either ascending or
                  descending order based on when each tag value was written.
                type: string
                enum: [ASCENDING, DESCENDING]
                default: ASCENDING
      responses:
        200:
          description: OK
          schema:
            type: object
            title: Http Query Response Body
            properties:
              results:
                description: An object containing the historical values for each requested tag that
                  was successfully queried. The object's property names correspond to a tag path.
                type: object
                additionalProperties:
                  $ref: '#/definitions/TypeAndValues'
                example:
                  system1.tag1:
                    type: DOUBLE
                    values:
                      - value: '12.87'
                        timestamp: '2019-03-13T09:51:38Z'
                      - value: '3.2'
                        timestamp: '2019-03-14T09:51:38Z'
              workspace:
                description: The workspace ID of the tag values
                type: string
                example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
              error:
                $ref: '#/definitions/ErrorEntry'
              failed:
                description: The paths of the tags that had errors.
                type: array
                items:
                  type: string
                example: [system2.tag1]
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/export-history:
    post:
      tags: [history]
      summary: Exports the undecimated data of one or more tags
      description: Exports the undecimated data of one or more tags. If "CSV" is specified as the responseFormat,
        the data is streamed as a single CSV file.
      operationId: ExportHistory
      x-ni-operation: exportHistory
      produces:
        - text/csv
      parameters:
        - in: body
          name: Request body
          required: true
          description: Contains the paths of the tags whose data should be exported
          schema:
            description: Contains the paths of the tags whose data should be exported
            type: object
            title: Tag Historian Export History Request
            properties:
              paths:
                description: The paths whose data should be exported
                type: array
                items:
                  type: string
                example:
                  - tag1
                  - tag2
              workspace:
                description: The workspace ID for exporting tag values. If this is not specified, the tag values from the default workspace will be returned.
                type: string
                example: 0c80cf49-54e9-4e92-b117-3bfa574caa84
              responseFormat:
                description: The format of the response. Currently only supports "CSV"
                type: string
                enum: [CSV]
                default: CSV
      responses:
        200:
          description: OK
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/update-metadata:
    post:
      tags: [history]
      summary: Update metadata
      description: Updates metadata for the specified tag. If the tag metadata does not exist it will be created.
      operationId: UpdateMetadata
      x-ni-operation: updateMetadata
      parameters:
        - in: body
          name: Metadata
          required: true
          description: Defines the tag metadata to update.
          schema:
            description: Defines the tag metadata to update.
            type: object
            title: Update Metadata Request
            properties:
              metadata:
                description: The metadata to update
                type: array
                items:
                  $ref: '#/definitions/UpdateMetadata'
      responses:
        204:
          description: No Content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/insert-values:
    post:
      tags: [history]
      summary: Inserts values for the specified tag
      description: Inserts values for the specified tag. The tag metadata must already exist.
      operationId: InsertValues
      x-ni-operation: insertValues
      parameters:
        - in: body
          name: Values
          required: true
          description: Defines the values to insert.
          schema:
            description: Defines the values to insert.
            type: object
            title: Insert Values Request
            properties:
              values:
                description: The values to insert
                type: array
                items:
                  $ref: '#/definitions/InsertValue'
      responses:
        204:
          description: No Content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/tags/delete-values-by-range:
    post:
      tags: [history]
      summary: Deletes a range of data for the specified tag
      description: Deletes a range of data for the specified tag.
      operationId: DeleteValuesByRange
      x-ni-operation: deleteValuesByRange
      parameters:
        - in: body
          name: Request body
          required: true
          description: Defines the tag and range of values to delete.
          schema:
            description: Defines the tag and range of values to delete.
            type: object
            title: Delete Ranges of Values Request
            properties:
              ranges:
                description: The ranges of values to delete
                type: array
                items:
                  $ref: '#/definitions/DeleteRangeOfValues'
      responses:
        204:
          description: No Content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/storage:
    get:
      tags: [storage]
      summary: Gets statistics about the user's storage
      description: Gets statistics about the user's storage.
      operationId: Storage
      x-ni-operation: storage
      responses:
        200:
          description: OK
          schema:
            type: object
            title: Storage Response
            properties:
              used:
                description: The amount of storage used in bytes.
                type: integer
                example: 1024
              limit:
                description: The total amount of storage in bytes.
                type: integer
                example: 104857600
              resource:
                description: The type of resource stored, e.g., "tags" or "files".
                type: string
                example: tags
              lastUpdated:
                description: The timestamp when the storage was last updated in ISO-8601 format.
                type: string
                format: date-time
                example: '2000-01-01T00:00:00Z'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v2/websocket:
    get:
      tags:
        - web socket
      summary: Open a WebSocket session
      description: Opens a persistent connection to the web server that allows two-way communication using
                   a JSON protocol. After you open a connection, you can query for historical values and
                   subscribe or unsubscribe for notifications when new historical values are recorded.
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
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=tag-rule/nitagrule.yml sha256=a15f5ebd5fa9b4ab9a73d8e98d9149afbad2e50bd1f78546bdaf8174d16f9320 bytes=28258 -->
## FILE: tag-rule/nitagrule.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `tag-rule/nitagrule.yml`
- sha256: `a15f5ebd5fa9b4ab9a73d8e98d9149afbad2e50bd1f78546bdaf8174d16f9320`
- bytes: 28258

````yaml
swagger: '2.0'
info:
  version: '1'
  title: Tag Rule Engine Web Service
  description: SystemLink Tag Rule Engine Service HTTP API. Only available on SystemLink Server.
  contact:
    name: NI
    url: 'https://www.ni.com/systemlink'
    email: support@ni.com
basePath: /nitagrule
consumes:
  - application/json
produces:
  - application/json
securityDefinitions:
  apiKeyAuth:
    type: apiKey
    name: x-ni-api-key
    in: header        
  basicAuth:
    type: basic
security:
  - apiKeyAuth: []        
  - basicAuth: []
x-ni-routing-key: Skyline.TagRuleEngine
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
      message:
        description: Complete error message
        type: string
      args:
        description: Positional argument values for the error code
        type: array
        items:
          type: string
      resourceType:
        description: Type of resource associated with the error.
          This field is only present for entries in *innerErrors*.
        type: string
        enum: [tagRule]
      resourceId:
        description: Identifier of the resource associated with the error.
          This field is only present for entries in *innerErrors*.
        type: string
      innerErrors:
        description: Array of individual errors when a request results in multiple errors.
          This field is only present when *name* is 'Skyline.OneOrMoreErrorsOccurred'.
        type: array
        items:
          $ref: '#/definitions/Error'
    example:
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251041
      message: One or more errors occurred. See the contained list for details of each error.
      args: []
      innerErrors:
        - name: TagRuleEngine.RuleNotFound
          code: -253103
          message: A rule with ID '5c2cf7e0e0d64403b486fcb4' was not found.
          resourceType: tagRule
          resourceId: 5c2cf7e0e0d64403b486fcb4
          args: [5c2cf7e0e0d64403b486fcb4]
  Operation:
    description: Operation provided by the API
    type: object
    properties:
      available:
        type: boolean
        description: Whether the operation is available to the caller
      version:
        type: integer
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
        description: >-
          Available operations in the v1 version of the API:

          - deleteRules: The ability to delete tag alarm rules

          - readRules: The ability to query for tag alarm rules

          - writeRules: The ability to create and modify tag alarm rules

        type: object
        properties:
          deleteRules:
            $ref: '#/definitions/Operation'
          readRules:
            $ref: '#/definitions/Operation'
          writeRules:
            $ref: '#/definitions/Operation'
  Condition:
    title: Condition
    description: An object describing the circumstances under which an alarm should be created.
    type: object
    required:
      - setPoints
      - comparator
    properties:
      setPoints:
        description: Values compared against the tag's current value to determine whether or not the condition
          is true. Conditions associated with the IN_RANGE and OUT_OF_RANGE comparators will have two set
          points. All other conditions should have only one set point. For tags of the DATE_TIME type, a timespan
          (for example, "01:00:00") is a valid value and represents a time interval relative to the server's current
          time when the rule is evaluated. Positive timespans represent times in the future, and negative timespans
          represent times in the past. The expected timespan format is `[-]d.hh:mm:ss.ff`.
        type: array
        items:
          type: string
        example: ["10"]
      comparator:
          type: string
          description: Operator which will be used when comparing the tag's current value to the set point(s).
            Note that the CONTAINS and NOT_CONTAINS comparators are only valid for rules associated with
            string tags. Similarly, LESS_THAN, GREATER_THAN, IN_RANGE, and the other numeric comparators are 
            not valid for rules associated with string tags.
          enum: [LESS_THAN, LESS_THAN_OR_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, IN_RANGE, OUT_OF_RANGE,
            EQUAL, NOT_EQUAL, CONTAINS, NOT_CONTAINS]  
      deadband:
        description: The change in signal from the set point necessary to clear an alarm. For example, a
          condition with a set point of 10, a comparator of GREATER_THAN, and a deadband of 2 will request 
          that alarms be cleared if the tag's values is less than or equal to (10 - 2) = 8. Similarly, if the
          condition had a comparator of LESS_THAN, the condition would request that alarms be cleared if the
          tag's value is greater than or equal to (10 + 2) = 12.
        type: string
        example: '2'
      severityLevel:
        description: An integer in the range [1,4] which specifies the severity level of a condition.
          Higher numeric values correspond to higher severity levels.
        type: integer
        minimum: 1
        maximum: 4
        example: 2
        default: 2
      notificationStrategyIds:
        description: The IDs of the notification strategies which should be triggered if a condition
          results in alarms being created or increasing in severity.
        type: array
        items:
          type: string
        example: []
  TagDataType:
    title: Tag Data Type
    description: The data type of the tags which a rule applies to. Rules are only evaluated
      against tags whose data type matches their *tagDataType*. For the TAG_TIME type, rules are
      evaluated against a tag's last updated time rather than its value. These rules will match tags
      of any data type.
    type: string
    enum: [DOUBLE, INT, STRING, BOOLEAN, U_INT64, DATE_TIME, TAG_TIME]
    example: DOUBLE
  Conditions:
    description: Array containing one or more conditions which control when a rule creates or clears alarms.
    type: array
    items:
      $ref: '#/definitions/Condition'
  Keywords:
    description: Words or phrases associated with a rule. Rules can be tagged with keywords to make it easier
      to find them with queries.
    type: array
    items:
      type: string
    example:
      - keyword1
      - keyword2
  Properties:
    description: Key-value-pair metadata associated with a rule. Rules can be tagged with properties to make
      it easier to find them with queries.
    type: object
    additionalProperties:
      type: string
    example:
      key1: value1
  RuleCommonFields:
    title: Rule Common Fields
    description: A single-sourced definition of available fields in both an update request and the rule type
      itself.
    properties:
      searchPath:
        description: A string describing which tag(s) a rule applies to. This can take the form of either
          a single tag's path, or a string containing wildcard characters which can match multiple tags.
        type: string
        example: '*.System.Health.DiskUsePercentage'
      workspace:
        description: The ID of the workspace to which this rule belongs. Added in version 2 of the
          readRules operation.
        type: string
        example: 3d411024-9db8-42d1-8ab8-6cee0e6cd841
      tagDataType:
        $ref: '#/definitions/TagDataType'
      conditions:
        $ref: '#/definitions/Conditions'
      disabled:
        description: A value indicating whether or not a rule is disabled.
        type: boolean
        example: false
        default: false
      displayName:
        description: Display string for a rule's name.
        type: string
        example: Low Disk Space Rule
      description:
        description: Display string for a rule's description.
        type: string
        example: Preconfigured rule for monitoring managed system's disk space
      alarmInstanceDisplayNameTemplate:
        description: Template string which will be used to set the *displayName* field on alarms created
          by a rule. Values surrounded by angle brackets will be substituted with values from the tag's property
          dictionary. For example, if an *alarmInstanceDisplayNameTemplate* contained the string "Excessive vibration
          on turbine <turbine_number>", and the rule was evaluated against a tag whose property dictionary
          contained the key "turbine_number" with value "5", then the rule would request that an alarm with 
          display name "Excessive vibration on turbine 5" be created.
        example: Excessive vibration on turbine <turbine_number>
        type: string
      alarmInstanceDescriptionTemplate:
        description: Template string which will be used to set the *description* field on alarms created by a rule.
          Values surrounded by angle brackets will be substituted with values from the tag's property dictionary.
          See the description of AlarmInstanceDisplayNameTemplate for more information.
        example: Disk space on <system> is low. Disk usage was <value>% when this alarm was triggered.
        type: string
      keywords:
        $ref: '#/definitions/Keywords'
      properties:
        $ref: '#/definitions/Properties'
  Rule:
    title: Rule
    description: A rule which contains one or more conditions which will be evaluated against updates
      to tags matched by the rule's searchPath.
    allOf:
     - type: object
       properties:
          id:
            description: The unique ID of a particular rule.
            type: string
            example: 5c33c212e0d6444320d9a9f4
     - $ref: '#/definitions/RuleCommonFields'
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
paths:
  /:
    get:
      tags: [versioning]
      summary: API information
      description: Returns information about API versions and available operations.
      operationId: RootEndpoint
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
              version:
                description: Implementation version of the web service
                type: string
                example: 18.0
  /{version}:
    parameters:
      - in: path
        name: version
        description: Version of the API to retrieve operations.
        type: string
        required: true
    get:
      tags: [versioning]
      summary: API version information
      description: Returns available operations for a single version of the API.
      operationId: RootEndpointWithVersion
      # Explicitly mark security as an empty array - this route does not require any privileges.
      # Marking it this way prevents it from inheriting the top-level security settings.
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
  /v1/rules:
    post:
      tags: [rules]
      summary: Create a rule
      description: Creates a rule.
      operationId: CreateRule
      x-ni-operation: writeRules
      parameters:
        - in: body
          name: Request body
          required: true
          schema:
            type: object
            title: CreateRuleRequestBody
            required:
              - searchPath
              - tagDataType
              - conditions
            properties:
              searchPath:
                description: A string describing which tag(s) a rule applies to. This can take the form of either
                  a single tag's path, or a string containing wildcard characters which can match multiple tags.
                type: string
                example: '*.System.Health.DiskUsePercentage'
              workspace:
                description: The ID of the workspace in which to create or update the rule. When not specified,
                  the default workspace is used based on the requesting user. Added in version 2 of the
                  writeRules operation.
                type: string
                example: 3d411024-9db8-42d1-8ab8-6cee0e6cd841
              tagDataType:
                $ref: '#/definitions/TagDataType'
              conditions:
                $ref: '#/definitions/Conditions'
              disabled:
                description: A value indicating whether or not a rule is disabled.
                type: boolean
                example: false
                default: false
              displayName:
                description: Display string for a rule's name.
                type: string
                example: Low Disk Space Rule
              description:
                description: Display string for a rule's description.
                type: string
                example: Preconfigured rule for monitoring managed system's disk space
              alarmInstanceDisplayNameTemplate:
                description: Template string which will be used to set the *displayName* field on alarms created
                  by a rule. Values surrounded by angle brackets will be substituted with values from the tag's property
                  dictionary. For example, if an *alarmInstanceDisplayNameTemplate* contained the string "Excessive vibration
                  on turbine <turbine_number>", and the rule was evaluated against a tag whose property dictionary
                  contained the key "turbine_number" with value "5", then the rule would request that an alarm with 
                  display name "Excessive vibration on turbine 5" be created.
                example: Excessive vibration on turbine <turbine_number>
                type: string
              alarmInstanceDescriptionTemplate:
                description: Template string which will be used to set the *description* field on alarms created by a rule.
                  Values surrounded by angle brackets will be substituted with values from the tag's property dictionary.
                  See the description of AlarmInstanceDisplayNameTemplate for more information.
                example: Disk space on <system> is low. Disk usage was <value>% when this alarm was triggered.
                type: string
              keywords:
                $ref: '#/definitions/Keywords'
              properties:
                $ref: '#/definitions/Properties'
      responses:
        200:
          description: OK
          schema:
            type: object
            title: CreateRuleResponse
            properties:
              id:
                description: The unique ID of the created rule
                type: string
                example: 5c40ec55e0d6441168b4c543
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/rules/{id}:
    parameters:
      - in: path
        name: id
        description: Rule ID
        type: string
        required: true
    get:
      tags: [rules]
      summary: Get a rule
      description: Gets a rule by ID.
      operationId: GetRule
      x-ni-operation: readRules
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/Rule'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    delete:
      tags: [rules]
      summary: Delete a rule
      description: Deletes a rule by ID.
      operationId: DeleteRule
      x-ni-operation: deleteRules
      responses:
        204:
          description: No Content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    patch:
      tags: [rules]
      summary: Modify a rule
      description: Modifies a rule. All fields specified will have their values replaced with the given values.
      operationId: ModifyRule
      x-ni-operation: writeRules
      consumes:
        - application/merge-patch+json
      parameters:
        - in: body
          name: Request body
          required: true
          schema:
            $ref: '#/definitions/RuleCommonFields'
      responses:
        204:
          description: No Content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/delete-rules:
    post:
      tags: [rules]
      summary: Delete rules
      description: Deletes multiple rules.
      operationId: DeleteRules
      x-ni-operation: deleteRules
      parameters:
        - in: body
          name: Request body
          required: true
          schema:
            title: DeleteRequestBody
            type: object
            required:
              - ids
            properties:
              ids:
                description: The IDs of the rules which should be deleted.
                type: array
                items:
                  type: string
                example: [5c40ec55e0d6441168b4c543, 5c40ec55e0d6441168b4c543]
      responses:
        200:
            description: Partial Success - Indicates the request to delete was processed successfully,
              but one or more rules failed to delete. The included *error* object will contain
              an entry in the *innerErrors* array for each failed rule.
            schema:
              type: object
              title: DeleteRulesPartialSuccess
              properties:
                deleted:
                  description: The *ruleId*s of the rules that were successfully deleted.
                  type: array
                  items:
                    type: string
                  example:
                    - 5c33c212e0d6444320d9a9f4
                failed:
                  description: The *ruleId*s of the rules that were not deleted.
                    See *error* for why each rule failed to delete. Reasons include the
                    rule could not be found or the caller is not authorized to delete the rule.
                  type: array
                  items:
                    type: string
                  example:
                    - 5c2cf7e0e0d64403b486fcb4
                error:
                  $ref: '#/definitions/Error'
        204:
          description: Success - Indicated all requested rules were deleted successfully.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/toggle-rules:
    post:
      tags: [rules]
      summary: Toggle rules
      description: Enables or disables multiple rules.
      operationId: ToggleRules
      x-ni-operation: writeRules
      parameters:
        - in: body
          name: Request body
          required: true
          schema:
            title: ToggleRequestBody
            type: object
            required:
              - ids
              - disabled
            properties:
              ids:
                description: The IDs of the rules which should be toggled.
                type: array
                items:
                  type: string
                example: [5c40ec55e0d6441168b4c543, 5c40ec55e0d6441168b4c543]
              disabled:
                description: A value indicating whether or not a rule is disabled.
                type: boolean
                example: false
                default: false
      responses:
        200:
          description: OK
          schema:
            title: ToggleResponse
            type: object
            properties:
              toggled:
                description: The IDs of the rules which were toggled.
                type: array
                items:
                  type: string
                example: [5c40ec55e0d6441168b4c543, 5c40ec55e0d6441168b4c544]
              notFoundIds:
                description: The IDs of the rules which were not found.
                type: array
                items:
                  type: string
                example: [5c40ec55e0d6441168b4c541]
              error:
                $ref: '#/definitions/Error'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/query-rules:
    post:
      tags: [rules]
      summary: Query rules
      description: Queries for rules.
      operationId: QueryRules
      x-ni-operation: readRules
      parameters:
        - in: body
          name: Request body
          required: true
          schema:
            title: QueryRequestBody
            type: object
            properties:
              displayName:
                description: Display name query. Returns rules whose *displayName* fields contain the query
                  string, without taking case into account.
                type: string
                example: low disk space
              description:
                description: Description query. Returns rules whose *description* fields contain the query
                  string, without taking case into account.
                type: string
                example: turbine 5
              tagPath:
                description: Tag path query. If the query string contains wildcard characters, the service
                  will return rules whose *searchPaths* either intersect with, or are matched by, the query
                  string. For example, if the query string is CRIO1.System.Health.*, then the service would
                  return rules with search paths of CRIO1.System.Health.Foo and
                  *.System.Health.DiskUsePercentage. The former is matched by the query string, and the latter
                  intersects with the query string, as there exists a string which could be matched by both
                  expressions (such as CRIO1.System.Health.DiskUsePercentage). If the query string does not
                  contain wildcard characters, the service will return rules whose *searchPaths* match the
                  query string.
                type: string
                example: System1.System.Health.DiskUsePercentage
              properties:
                type: object
                description: Property query. The service will return rules whose *properties* fields
                  contain all of the specified key/value pairs.
                additionalProperties:
                  type: string
                example:
                  key1: value1
              keywords:
                type: array
                description: Keyword query. The service will return rules whose *keywords* fields contain
                  all of the specified keywords.
                items:
                  type: string
                example:
                  - keyword1
                  - keyword2
              workspaces:
                type: array
                description: Workspace query. The service will return rules whose *workspace* field is one of
                  the specified workspaces. Added in version 2 of the readRules operation.
                items:
                  type: string
                example:
                  - '*'    
              skip:
                description: Number of entries to skip in the response list. Typically used in combination
                  with the take parameter to implement pagination.
                type: integer
                default: 0
              take:
                description: Number of entries to include in the response list. Typically used in combination
                  with the skip parameter to implement pagination.
                type: integer
                default: 10000
                maximum: 10000
      responses:
        200:
          description: OK
          schema:
            title: QueryResponse
            type: object
            properties:
              rules:
                description: The rules matched by the filter criteria in the request body.
                type: array
                items:
                  $ref: '#/definitions/Rule'
              totalCount:
                description: The total number of rules which matched the filter criteria.
                type: integer
                example: 1
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/duplicate-rules:
    post:
      tags: [rules]
      summary: Duplicate rules
      description: Duplicates multiple rules into a given workspace
      operationId: DuplicateRules
      x-ni-operation: writeRules
      parameters:
        - in: body
          name: Request body
          required: true
          schema:
            title: DuplicateRequestBody
            type: object
            required:
              - ids
              - workspace
            properties:
              ids:
                description: The IDs of the rules which should be duplicated.
                type: array
                items:
                  type: string
                example: [5c40ec55e0d6441168b4c543, 5c40ec55e0d6441168b4c543]
              workspace:
                description: The ID of the workspace in which to duplicate the specified rules.
                type: string
                example: 3d411024-9db8-42d1-8ab8-6cee0e6cd841
      responses:
        200:
          description: OK
          schema:
            title: DuplicateResponse
            type: object
            properties:
              duplicatedIds:
                description: A dictionary where the keys are the IDs of the rules which were successfully
                  duplicated, and the values are the IDs of the new duplicate rules.
                type: object
                additionalProperties:
                  type: string
                example: 
                  5c40ec55e0d6441168b4c543: 5c40ec55e0d6441168b4c545
                  5c40ec55e0d6441168b4c544: 5c40ec55e0d6441168b4c546
              failed:
                description: The IDs of the rules which were failed to be duplicated.
                  See *error* for why each rule failed to duplicate. Reasons include the
                  rule could not be found or the caller is not authorized to create the rule.
                type: array
                items:
                  type: string
                example: [5c40ec55e0d6441168b4c541]
              error:
                $ref: '#/definitions/Error'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=tdm-reader/nitdmreader.yml sha256=3afdb436bcaa584f9df3eba12d056bcdcf29020294a272b206eda95ad8485633 bytes=23770 -->
## FILE: tdm-reader/nitdmreader.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `tdm-reader/nitdmreader.yml`
- sha256: `3afdb436bcaa584f9df3eba12d056bcdcf29020294a272b206eda95ad8485633`
- bytes: 23770

````yaml
swagger: '2.0'
info:
  version: '1'
  title: TDMReader Web Service
  description: TDMReader HTTP API
  contact:
    name: NI
    url: 'https://www.ni.com/systemlink'
    email: support@ni.com
basePath: /nitdmreader
consumes:
  - application/json
produces:
  - application/json
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
x-ni-routing-key: Skyline.TDMReader
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
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251040
      message: >-
        One or more errors occurred. See the contained list for details about each
        error.
      args: []
      innerErrors:
        - name: TDMReader.FileServiceFailed
          code: -253500
          resourceType: File
          resourceId: 4afb2ce3741fe11d88838cc9
          message: File service failed.
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
        description: The version of the available operation
    required: [available]
    example:
      available: true
      version: 1
  V1Operations:
    description: V1 operations
    type: object
    properties:
      operations:
        description: >-
          Available operations in the v1 version of the API:

          - readData: Ability to read data
        type: object
        properties:
          readData:
            $ref: '#/definitions/Operation'
  Property:
    description: A property and its value.
    type: object
    properties:
      name:
        type: string
        description: Name of the property
        example: Name
      type:
        type: string
        description: Data type of 'value'
        example: String
      value:
        type: string
        example: Channel name
  Properties:
    type: object
    properties:
      properties:
        description: Property values
        type: array
        items:
          $ref: '#/definitions/Property'
      totalCount:
        type: integer
        description: Count of all properties. This might be more than the items returned in Properties.
        example: 1
  FileList:
    type: object
    properties:
      fileIds:
        description: File IDs
        type: array
        items:
          type: string
          example: 5b8453dba8808c22b0f99023
  DataWindow:
    description: Data window.
    properties:
      decimatex:
        type: integer
        description: Number of values on the x axis. This determines the number of points that can be displayed.
        example: 1000
        default: null
        format: int32
      decimatey:
        type: integer
        description: Number of values on the y axis. This determines the number of points that can be displayed.
        example: 1000
        default: null
        format: int32
      xmin:
        type: number
        default: null
        format: double
        description: Minimum x value of the display x axis.
        example: -1
      xmax:
        type: number
        default: null
        format: double
        description: Maximum x value of the display x axis.
        example: 1
      ymin:
        type: number
        default: null
        format: double
        description: Minimum y value of the display y axis.
        example: -1
      ymax:
        type: number
        default: null
        format: double
        description: Maximum y value of the display y axis.
        example: 1
      xlog:
        type: boolean
        default: false
        description: Logrithmic X channel.
      ylog:
        type: boolean
        default: false
        description: Logrithmic Y channel.
      showLines:
        type: boolean
        description: Represent data as lines. When decimation is performed, the data returned represents the min and max values for that x-axis increment.
        default: true
      showPoints:
        type: boolean
        default: false
        description: Represent data as points. When decimation is performed, the data returned represents all the points in that x-axis increment.
      filter:
        type: string
        default: null
        description: Expression to apply to a group of channels. Valid variables are x, y0-yn, f0-fn (optional filterChannels). 
        example: (x > 0) and (y0 = 1)
      filterChannels:
        type: array
        items:
          $ref: '#/definitions/OneChannelSpecifier'
        default: null
        description: Channels to use only to filter. Values from these channels are not returned.
      function:
        type: string
        default: null
        description: Function to perform on the channel data.
        example: y0-y1
      outputObjectNames:
        type: array
        items:
          type: string
        default: null
        description: Transpose the returned data for the channels with the specified names.
        example:
          - name1
          - name2
      xminStringData:
        description: >-
          ISO-8601 formatted timestamp indicating the starting point for x data
        type: string
        example: '2018-05-09T15:07:42.527921Z'
      xmaxStringData:
        description: >-
          ISO-8601 formatted timestamp indicating the ending point for x data
        type: string
        example: '2018-05-09T15:07:42.527921Z'
      sort:
        type: string
        default: null
        description: Specify how to sort values before returning them.
        example: '-y0,x,s0'
      sortChannels:
        type: array
        items:
          $ref: '#/definitions/OneChannelSpecifier'
        default: null
        description: Channels to use only to sort. Values from these channels are not returned.
      useWaveformProperties:
        type: boolean
        description: Look for specific properties in a channel that define the start and increment x values to use for each channel.
        default: false
      groupBy:
        type: string
        description: List of channels to group by.
        default: null
        example: 'y0,x'
      groupStride:
        type: integer
        description: Number of samples per group.
        default: null
        format: int32
        example: 100
      groupChannels:
        type: array
        items:
          $ref: '#/definitions/OneChannelSpecifier'
        default: null
        description: Channels to use only to group. Values from these channels are not returned.
      maxGroupsToReturn:
        type: integer
        default: null
        format: int32
        description: Maximum number of groups to return when grouping.
        example: 100
      groupItemIndexStart:
        type: integer
        default: null
        format: int32
        description: Index of first item in each group to return.
        example: 100
      groupItemMaxCount:
        type: integer
        default: null
        format: int32
        description: Maximum number of items to return per group.
        example: 100
      ignoreXForDecimation:
        type: boolean
        default: null
        description: If true, x is not used in decimation. Instead, indices are returend for x.
        example: true
  OneChannelSpecifier:
    description: Specification for a channel of data
    properties:
      fileId:
        description: file descriptor
        type: string
        example: "5b8453dba8808c22b0f99023"
      groupName:
        type: string
        description: group name
        example: Group 1
      channelName:
        type: string
        description: channel name
        example: Channel 1
    required: 
      - fileId
  ChannelSpecifications:
    description: Array of x-y channel groups.  The x channel of each grouping is optional.
    properties:
      xyChannels:
        type: array
        items:
          description: y channel(s) and an optional x channel
          properties:
            xChannel:
              $ref: '#/definitions/OneChannelSpecifier'
            yChannels:
              description: 'Channels to be treated as y channels associated with x channel'
              type: array
              items:
                $ref: '#/definitions/OneChannelSpecifier'
            dataWindow:
              $ref: '#/definitions/DataWindow'
          required:
            - yChannels
        minItems: 1
    required:
      - xyChannels
  QueryChannelsRequest:
    description: Object containing the channels to request metadata for.
    properties:
      channelSpecifications:
        type: array
        items:
          $ref: '#/definitions/OneChannelSpecifier'
      calculateChannelLength:
        type: boolean
        description: Determines whether or not to calculate the channel length
        default: false
    required:
      - channelSpecifications
  OneChannelData:
    properties:
      dataType:
        type: string
        description: Native data type for the channel
      numericData:
        type: array
        description: Channel data
        items:
          type: number
      stringData:
        type: array
        description: Channel data
        items:
          type: string
      decimated:
        type: boolean
        description: Specifies whether returned data is decimated
      lossyDecimation:
        type: boolean
        description: Specifies whether data was decimated in a lossy manner such that the returned data is not necessarily a true visual representation
      undecimatedLength:
        type: integer
        description: Number of points of undecimated data
  XYData:
    properties:
      x:
        $ref: '#/definitions/OneChannelData'
      'y':
        type: array
        description: Array of y channels
        items:
          $ref: '#/definitions/OneChannelData'
  ReturnedXYData:
    properties:
      data:
        type: array
        description: Pairing of data from an x channel and multiple y channels
        items:
            $ref: '#/definitions/XYData'
      timeUtcOffsetHours:
        type: number
        description: Time zone offset applied to local time values
      error:
        $ref: '#/definitions/Error'
  QueryDataSpecifier:
    properties:
      channelSpecifications:
        $ref: '#/definitions/ChannelSpecifications'
    required:
      - channelSpecifications
  CreateCalculatedResultSpecifier:
    properties:
      channelSpecifications:
        $ref: '#/definitions/ChannelSpecifications'
      workspaceId:
        type: string
    required:
      - channelSpecifications
  ReturnedUniqueValues:
    properties:
      uniqueValues:
        type: array
        items:
          $ref: '#/definitions/OneChannelData'
      timeUtcOffsetHours:
        type: number
        description: Time zone offset applied to local time values
        example: 0
  UniqueValuesSpecifier:
    properties:
      channelSpecifications:
        type: array
        description: Channel specifications
        items:
          $ref: '#/definitions/OneChannelSpecifier'
      maxNumberOfUniqueValues:
        description: Maximum number of unique values to identify
        type: integer
        example: 10
  NamesList:
    description: List of names and number of names
    properties:
      names:
        description: All names
        type: array
        items:
          type: string
          description: Name
          example: Channel 1
      totalCount:
        type: integer
        description: Total number of names. This might be more than the number of names in the list.
        example: 1
  FileInformation:
    type: object
    properties:
      fileId:
        type: string
        description: File ID
        example: "5b8453dba8808c22b0f99023"
      properties:
        $ref: '#/definitions/Properties'
      groups:
        type: array
        items:
          properties:
            name:
              type: string
              description: Group name
              example: Group 1
            properties:
              $ref: '#/definitions/Properties'
            channels:
              type: array
              items:
                properties:
                  name:
                    type: string
                    description: Channel name
                    example: Channel 1
                  dataCount:
                    type: number
                    description: Number of data points in the channel
                    example: 1
                  dataType:
                    type: string
                    description: Data type of this channel
                    example: String
                  properties:
                    $ref: '#/definitions/Properties'
  FileInformationList:
    type: array
    items:
      $ref: '#/definitions/FileInformation'
paths:
  /:
    get:
      tags: [versioning]
      summary: API information
      description: Returns information about API versions and available operations.
      operationId: RootEndpoint
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
                example: '18.0'
  /{version}:
    parameters:
      - in: path
        name: version
        description: Version of the API to retrieve operations
        type: string
        required: true
    get:
      tags: [versioning]
      summary: API version information
      description: Returns available operations for a single version of the API.
      operationId: RootEndpointWithVersion
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
  /v1/files/{fileId}:
    get:
      tags: [metadata]
      summary: Gets file, group, and channel information
      description: 'Gets all group names, channel names, channel information, and properties at all levels. This does not return channel data.'
      operationId: getAllFileInfo
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      x-ni-request-timeout: 60000
      produces:
        - application/json
      parameters:
        - name: fileId
          description: File ID
          in: path
          type: string
          required: true
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/FileInformation'
        default:
          description: Error
          schema:
            $ref: '#/definitions/Error'
  /v1/query-files:
    post:
      tags: [metadata]
      summary: Gets file, group, and channel information
      description: 'Gets all group names, channel names, channel information, and properties at all levels. This does not return channel data.'
      operationId: getMultipleFileInfo
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      x-ni-request-timeout: 60000
      produces:
        - application/json
      parameters:
        - name: fileIds
          description: List of File IDs to inspect
          in: body
          required: true
          schema:
            $ref: '#/definitions/FileList'
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/FileInformationList'
        default:
          description: Error
          schema:
            $ref: '#/definitions/Error'
  /v1/query-channels:
    post:
      tags: [metadata]
      summary: Gets channel information
      description: 'Gets all channel names, channel information, and properties for the channel. This does not return channel data.'
      operationId: queryChannels
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      x-ni-request-timeout: 60000
      produces:
        - application/json
      parameters:
        - name: QueryChannelsRequest
          description: Channel request parameters
          in: body
          required: true
          schema:
            $ref: '#/definitions/QueryChannelsRequest'
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/FileInformationList'
        default:
          description: Error
          schema:
            $ref: '#/definitions/Error'
  /v1/files/{fileId}/groups:
    get:
      tags: [metadata]
      summary: Lists all groups in the file
      description: Lists all group names in the file.
      operationId: getGroups
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      x-ni-request-timeout: 60000
      produces:
        - application/json
      parameters:
        - name: fileId
          description: File ID
          in: path
          required: true
          type: string
        - name: skip
          description: Number of items to skip
          in: query
          type: integer
          default: 0
        - name: take
          description: Number of items to take after skipping
          in: query
          type: integer
          default: -1
        - name: returnCount
          description: Specifies whether to return the total number of items
          in: query
          type: boolean
          default: false
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/NamesList'
        default:
          description: Error
          schema:
            $ref: '#/definitions/Error'
  /v1/files/{fileId}/groups/{groupName}/channels:
    get:
      tags: [metadata]
      summary: Lists all channels in the group
      description:  Lists all channel names for a group in a specific file.
      operationId: getChannels
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      x-ni-request-timeout: 60000
      produces:
        - application/json
      parameters:
        - name: fileId
          description: File ID
          in: path
          required: true
          type: string
        - name: groupName
          description: Group name
          in: path
          required: true
          type: string
        - name: skip
          description: Number of items to skip
          in: query
          type: integer
          default: 0
        - name: take
          description: Number of items to take after skipping
          in: query
          type: integer
          default: -1
        - name: returnCount
          description: Specify this to return the total count of items
          in: query
          type: boolean
          default: false
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/NamesList'
        default:
          description: Error
          schema:
            $ref: '#/definitions/Error'
  /v1/query-data:
    post:
      tags: [data]
      summary: Returns data from channels.
      description: Queries files based on channel and window specifications and returns channel data that matches the query. The channel specifications select channels by group and channel relationships. Window specifications determine a bounding box of minimum and maximum x and y values, as well as specify the type of decimation performed on data within the window.
      operationId: queryData
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      x-ni-request-timeout: 60000
      produces:
        - application/json
      parameters:
        - name: ChannelSpecifications
          description: Channel specifications and window information
          in: body
          required: true
          schema:
            $ref: '#/definitions/QueryDataSpecifier'
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/ReturnedXYData'
        default:
          description: Error
          schema:
            $ref: '#/definitions/Error'
  /v1/query-unique-values:
    post:
      tags: [data]
      summary: Returns unique data from channels.
      description: Queries files based on channel specifications and returns unique channel data values. The channel specifications select channels by group and channel relationships. The maximum number of unique values to return is determined by MaxNumberOfUniqueValues. If there are more unique values, then the first MaxNumberOfUniqueValues + 1 values are returned.
      operationId: queryUniqueValues
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      x-ni-request-timeout: 60000
      produces:
        - application/json
      parameters:
        - name: ChannelSpecifications
          description: Channel specifications
          in: body
          required: true
          schema:
            $ref: '#/definitions/UniqueValuesSpecifier'
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/ReturnedUniqueValues'
        default:
          description: Error
          schema:
            $ref: '#/definitions/Error'
  /v1/create-calculated-result:
    post:
      tags: [data]
      summary: Returns a calculated result channel.
      description: Creates a channel based on values from other channels.
      operationId: createCalculatedResult
      x-ni-auth: true
      x-ni-request-variables: [REMOTE_USER]
      x-ni-request-timeout: 60000
      produces:
        - application/json
      parameters:
        - name: ChannelSpecifications
          description: Channel specifications and window information
          in: body
          required: true
          schema:
            $ref: '#/definitions/CreateCalculatedResultSpecifier'
      responses:
        200:
          description: OK
          schema:
            $ref: '#/definitions/ReturnedUniqueValues'
        default:
          description: Error
          schema:
            $ref: '#/definitions/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=test-monitor/nitestmonitor-v1.yml sha256=bf1e11c689a1dcc0ce5e660d9b83e586b85c9413e2bdf4ffe390997ee01ce952 bytes=44855 -->
## FILE: test-monitor/nitestmonitor-v1.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `test-monitor/nitestmonitor-v1.yml`
- sha256: `bf1e11c689a1dcc0ce5e660d9b83e586b85c9413e2bdf4ffe390997ee01ce952`
- bytes: 44855

````yaml
swagger: '2.0'
info:
  version: '1'
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
      name: Skyline.OneOrMoreErrorsOccurred
      code: -251040
      message: >-
        One or more errors occurred. See the contained list for details of each
        error.
      args: []
      innerErrors:
        - name: TestMonitor.InvalidId
          code: -253700
          resourceType: TestResult
          resourceId: bd9126f5-b0b1-446a-8b08-dc6460047377
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
  ResultField:
    title: Result Field
    description: Result field enum
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
      - PRODUCT
      - TOTAL_TIME_IN_SECONDS
      - KEYWORDS
      - PROPERTIES
      - FILE_IDS
      - STATUS_TYPE_SUMMARY
  StepField:
    title: Step Field
    description: Step field enum
    type: string
    enum:
      - NAME
      - STEP_TYPE
      - ID
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
  ResultSortDefinitionObject:
    title: Result Sort Definition
    description: Defines the field and direction for sorting test results.
    type: object
    required:
      - field
    properties:
      field:
        $ref: '#/definitions/ResultField'
      orderByDescending:
        type: boolean
        default: false
  StepSortDefinitionObject:
    title: Step Sort Definition
    description: Defines the field and direction for sorting test steps.
    type: object
    required:
      - field
    properties:
      field:
        $ref: '#/definitions/StepField'
      orderByDescending:
        type: boolean
        default: false
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
  DictionaryQueryObject:
    title: Dictionary Query
    description: Dictionary query object
    type: object
    required:
      - name
    properties:
      name:
        description: The name of the dictionary key to query for.
        type: string
      value:
        description: >-
          The value to compare with. This is compared to the value that is stored in the
          dictionary. When the comparison is performed, the value stored in the dictionary is on
          the left hand side of the operation and this value is on the right hand side.
        type: object
        example: 1.2
      operation:
        $ref: '#/definitions/QueryOperation'
        default: 'EQUAL'
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
        description: ISO-8601 formatted timestamp value to compare
        type: string
        format: iso-date-time
        example: '2017-11-14T15:41:06.106Z'
  RelativeTimeQueryObject:
    title: Relative Time Query
    description: 'Object describing a number of time units used for calculating a date and time relative to the current server time. The calculated date and time will be whole values of the smallest time unit provided; 30 days evaluates to 30 days ago at midnight, and 10 hours evaluates to 10 hours ago at 0 minutes.'
    type: object
    required:
      - unit
      - value
    properties:
      unit:
        description: The unit of time that the value represents.
        type: string
        enum:
          - DAYS
          - HOURS
          - MINUTES
          - SECONDS
        example: DAYS
      value:
        description: Number of whole time units relative to the current server time.
        type: integer
        format: int32
        example: 30
  TestResultRequestObject:
    title: Test Result Request
    type: object
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
        description: Keywords associated with the test result
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
      product:
        description: The type of device under test. Added in version 2.
        type: string
        example: cRIO-9030
      fileIds:
        description: Array of file ids attached to the test result
        type: array
        items:
          type: string
        example: [5e30934193cac8046851acb2]
      startedAt:
        description: ISO-8601 formatted timestamp indicating when the test result began
        type: string
        format: iso-date-time
        example: '2018-05-07T18:58:05.219692Z'
      totalTimeInSeconds:
        description: Total run-time of the test in seconds
        type: number
        format: double
        default: 0
        example: 29.9
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
        format: iso-date-time
        example: '2018-05-07T18:58:05.219692Z'
      updatedAt:
        description: ISO-8601 formatted timestamp indicating when the result was last updated
        type: string
        format: iso-date-time
        example: '2018-05-09T15:07:42.527921Z'
      programName:
        description: Program name
        type: string
        example: My test program
      id:
        description: Id of the test result
        type: string
        example: bd9126f5-b0b1-446a-8b08-dc6460047377
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
      product:
        description: The type of device under test. Added in version 2.
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
        description: Keywords associated with the test result
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
        description: Array of file ids attached to the test result
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
  TestResultUpdateRequestObject:
    title: Test Result Update
    type: object
    required:
      - id
    properties:
      id:
        description: Test result id to update
        type: string
        example: bd9126f5-b0b1-446a-8b08-dc6460047377
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
        description: Keywords associated with the test result
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
      product:
        description: The type of device under test. Added in version 2.
        type: string
        example: cRIO-9030
      fileIds:
        description: Array of file ids attached to the test result
        type: array
        items:
          type: string
        example: [5e30934193cac8046851acb2]
      startedAt:
        description: ISO-8601 formatted timestamp indicating when the test result began
        type: string
        format: iso-date-time
        example: '2018-05-07T18:58:05.219692Z'
      totalTimeInSeconds:
        description: Total run-time of the test in seconds
        type: number
        format: double
        default: 0
        example: 29.9
  TestResultQueryObject:
    title: Test Result Query
    type: object
    properties:
      ids:
        description: Array of test result ids
        type: array
        items:
          type: string
        example:
          - bd9126f5-b0b1-446a-8b08-dc6460047377
      programNames:
        description: Array of program names
        type: array
        items:
          type: string
        example:
          - Result Creation Test
      operators:
        description: Array of operators
        type: array
        items:
          type: string
        example:
          - admin
      serialNumbers:
        description: Array of serial numbers
        type: array
        items:
          type: string
        example:
          - 1f05c3c8-7a8c-4ebb-a87f-7a60d5dd8938
      products:
        description: Array of products. Added in version 2.
        type: array
        items:
          type: string
        example:
          - cRIO-9030
      systemIds:
        description: Array of system ids
        type: array
        items:
          type: string
        example:
          - 5e30931993cac8046850a996
      hostNames:
        description: Array of host names
        type: array
        items:
          type: string
        example:
          - My-Host
      keywords:
        description: Array of keywords
        type: array
        items:
          type: string
        example:
          - keyword1
          - keyword2
      properties:
        description: Dictionary of key-value property pairs
        type: object
        additionalProperties:
          type: string
        example:
          key1: value1
      updatedAtQuery:
        description: Time query object for the test result's last updated timestamp
        type: array
        items:
          $ref: '#/definitions/TimeQueryObject'
      startedAtQuery:
        description: Time query object for the test result's started at timestamp
        type: array
        items:
          $ref: '#/definitions/TimeQueryObject'
      updatedWithin:
        $ref: '#/definitions/RelativeTimeQueryObject'
      startedWithin:
        $ref: '#/definitions/RelativeTimeQueryObject'
      fileIds:
        description: Array of file ids
        type: array
        items:
          type: string
        example:
          - 5982002b5d67371430c80e73
      statuses:
        description: Array of result statuses
        type: array
        items:
          $ref: '#/definitions/StatusObject'
      sortBy:
        type: array
        items:
          $ref: '#/definitions/ResultSortDefinitionObject'
  StepIdResultIdPair:
    title: Step Id / Result Id Pair
    type: object
    required:
      - stepId
      - resultId
    properties:
      stepId:
        type: string
        example: 02600cf8-c2bb-4ff9-a139-031e943fb0c0
      resultId:
        type: string
        example: bd9126f5-b0b1-446a-8b08-dc6460047377
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
          - key1: value1
            key2: value2
          - key1: value3
  TestStepsDeleteRequest:
    title: Test Steps Delete Request
    type: object
    required:
      - steps
    properties:
      steps:
        description: Array of test step id and result id pairs to delete
        type: array
        items:
          $ref: '#/definitions/StepIdResultIdPair'
  TestStepQueryObject:
    title: Test Step Query
    type: object
    properties:
      excludeFields:
        description: Array of step field names to exclude
        type: array
        items:
          $ref: '#/definitions/StepField'
      names:
        description: Array of test step names
        type: array
        items:
          type: string
        example:
          - My Test Step
      stepIds:
        description: Array of step ids
        type: array
        items:
          type: string
        example:
          - Step1
      parentIds:
        description: Array of parent step ids
        type: array
        items:
          type: string
        example:
          - bd9126f5-b0b1-446a-8b08-dc6460047377
      resultIds:
        description: Array of result ids
        type: array
        items:
          type: string
        example:
          - 02600cf8-c2bb-4ff9-a139-031e943fb0c0
      path:
        description: Step path
        type: string
        example: root.step1.step2
      pathIds:
        description: Array of path ids
        type: array
        items:
          type: string
        example:
          - 4e303cdd-efc5-477f-a331-932dcbdd1ca8
          - 5bb6aa1a-4e88-4e50-ada4-4aa20b4e82b3
      statuses:
        description: Array of step statuses
        type: array
        items:
          $ref: '#/definitions/StatusObject'
      inputs:
        description: >-
          This is a query on the inputs dictionary.  It is represented by an array of an array of
          objects referred to as 'Dictionary Query Objects'. When querying, all elements of the
          inner array of 'Dictionary Query Objects' must match (an "and" relationship within the
          inner array).  Only one element in the outer array needs to match (an "or" relationship
          within the outer array).
        type: array
        items:
          description: >-
            Inner array of 'Dictionary Query Objects' to query for. When querying, all elements of
            the inner array of 'Dictionary Query Objects' must match (an "and" relationship within
            the inner array).
          type: array
          items:
            $ref: '#/definitions/DictionaryQueryObject'
        example:
          - - name: 'Current'
              value: 1.2
            - name: 'Voltage'
              value: 2.3
              operation: 'LESS_THAN_OR_EQUAL'
      outputs:
        description: >-
          This is a query on the outputs dictionary.  It is represented by an array of an array of
          objects referred to as 'Dictionary Query Objects'. When querying, all elements of the
          inner array of 'Dictionary Query Objects' must match (an "and" relationship within the
          inner array).  Only one element in the outer array needs to match (an "or" relationship
          within the outer array).
        type: array
        items:
          description: >-
            Inner array of 'Dictionary Query Objects' to query for. When querying, all elements of
            the inner array of 'Dictionary Query Objects' must match (an "and" relationship within
            the inner array).
          type: array
          items:
            $ref: '#/definitions/DictionaryQueryObject'
        example:
          - - name: 'Power'
              value: 1.4
              operation: 'GREATER_THAN_OR_EQUAL'
            - name: 'Power'
              value: 2.3
              operation: 'LESS_THAN_OR_EQUAL'
      startedAtQuery:
        description: Time query object
        type: array
        items:
          $ref: '#/definitions/TimeQueryObject'
      updatedAtQuery:
        description: Time query object
        type: array
        items:
          $ref: '#/definitions/TimeQueryObject'
      sortBy:
        type: array
        items:
          $ref: '#/definitions/StepSortDefinitionObject'
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
        format: iso-date-time
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
        description: Inputs and their values passed to this test
        type: array
        items:
          $ref: '#/definitions/NamedValueObject'
      outputs:
        description: Outputs and their values logged by this test
        type: array
        items:
          $ref: '#/definitions/NamedValueObject'
  TestStepCreateOrUpdateRequestObject:
    title: Test Step Create or Update Request
    type: object
    required:
      - steps
    properties:
      steps:
        description: Array of test steps to create
        type: array
        items:
          $ref: '#/definitions/TestStepRequestObject'
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
        format: iso-date-time
        example: '2018-05-07T18:58:05.219692Z'
      updatedAt:
        description: ISO-8601 formatted timestamp indicating when the result was last updated
        type: string
        format: iso-date-time
        example: '2018-05-09T15:07:42.527921Z'
      inputs:
        description: Inputs and their values passed to this test
        type: array
        items:
          $ref: '#/definitions/NamedValueObject'
      outputs:
        description: Outputs and their values logged by this test
        type: array
        items:
          $ref: '#/definitions/NamedValueObject'
      dataModel:
        description: Custom string defining the model of the data object
        type: string
        example: TestStand
      data:
        $ref: '#/definitions/StepDataObject'
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
        - failed
        - error
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
  DeleteResultsResponse:
    description: Delete Test Results Response
    schema:
      description: Delete Test Results Response
      title: DeleteResultsResponse
      type: object
      required:
        - ids
        - failed
        - error
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
      required:
        - results
        - totalCount
      properties:
        results:
          description: Array of test results
          type: array
          items:
            $ref: '#/definitions/TestResultResponseObject'
        totalCount:
          description: Number of matching test results
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
        - failed
        - error
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
      required:
        - steps
        - totalCount
      properties:
        steps:
          description: Array of test steps
          type: array
          items:
            $ref: '#/definitions/TestStepResponseObject'
        totalCount:
          description: Number of matching test steps
          type: integer
          format: int64
          example: 1
  StepsDeletePartialSuccessResponse:
    description: Delete Test Steps Partial Success Response
    schema:
      description: Delete Test Steps Partial Success Response
      title: StepsDeletePartialSuccessResponse
      type: object
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
paths:
  /v1:
    get:
      tags: [versioning]
      summary: API version 1 information
      description: Returns available operations for version 1 of the API.
      operationId: root-endpoint-v1
      # Explicitly mark security as an empty array - this route does not require any privileges.
      # Marking it this way prevents it from inheriting the top-level security settings.
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
  /v1/query-results:
    post:
      tags: [results]
      summary: Queries test results
      description: Uses input criteria to filter and return test results. An empty request body queries all test results.
      operationId: query-results
      x-ni-operation: queryResults
      x-ni-auth: true
      parameters:
        - in: body
          name: postBody
          description: Result query object
          required: false
          schema:
            $ref: '#/definitions/TestResultQueryObject'
        - in: query
          name: skip
          type: integer
          format: int32
          default: 0
          minimum: 0
        - in: query
          name: take
          type: integer
          format: int32
          default: -1
          minimum: -1
      responses:
        200:
          $ref: '#/responses/ResultsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/results:
    get:
      tags: [results]
      summary: Gets test results
      description: Gets a list of test results.
      operationId: get-results
      x-ni-operation: getResults
      x-ni-auth: true
      parameters:
        - in: query
          name: skip
          type: integer
          format: int32
          default: 0
          minimum: 0
        - in: query
          name: take
          type: integer
          format: int32
          default: -1
          minimum: -1
      responses:
        200:
          $ref: '#/responses/ResultsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    put:
      tags: [results]
      summary: Updates existing test results
      description: Updates existing test results by merging or replacing values.
      operationId: update-results
      x-ni-operation: updateResults
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Array of test results to update
          required: true
          schema:
            description: Array of test results to update
            title: UpdateTestResultsRequest
            type: object
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
      responses:
        200:
          $ref: '#/responses/ResultsPartialSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      tags: [results]
      summary: Creates new test results
      description: Creates new test results from the supplied models. The server automatically generates the result ids. The server will populate the start time if one is not provided.
      operationId: create-results
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
            type: object
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
  /v1/results/{resultId}:
    delete:
      tags: [results]
      summary: Deletes a test result
      description: Deletes the test result with the specified id. The request succeeds for result ids that do not exist.
      operationId: DeleteResult
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
  /v1/delete-results:
    post:
      tags: [results]
      summary: Deletes test results
      description: Deletes multiple test results in a single request.
      operationId: delete-results
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
            type: object
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
          description: The resource was deleted successfully.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/query-steps:
    post:
      tags: [steps]
      summary: Queries test steps
      description: Uses input criteria to filter and return test steps. An empty request body queries all test steps.
      operationId: query-steps
      x-ni-operation: querySteps
      x-ni-auth: true
      parameters:
        - in: body
          name: postBody
          description: Step query object
          required: false
          schema:
            $ref: '#/definitions/TestStepQueryObject'
        - in: query
          name: skip
          type: integer
          format: int32
          default: 0
          minimum: 0
        - in: query
          name: take
          type: integer
          format: int32
          default: -1
          minimum: -1
      responses:
        200:
          $ref: '#/responses/StepsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/steps:
    get:
      tags: [steps]
      summary: Gets test steps
      description: Gets a list of test steps.
      operationId: get-steps
      x-ni-operation: getSteps
      x-ni-auth: true
      parameters:
        - in: query
          name: skip
          type: integer
          format: int32
          default: 0
          minimum: 0
        - in: query
          name: take
          type: integer
          format: int32
          default: -1
          minimum: -1
      responses:
        200:
          $ref: '#/responses/StepsQueryResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    put:
      tags: [steps]
      summary: Update test steps
      description: Updates existing test steps by replacing values for the specified fields.
      operationId: update-steps
      x-ni-operation: updateSteps
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Array of test steps
          required: true
          schema:
            $ref: '#/definitions/TestStepCreateOrUpdateRequestObject'
        - in: query
          name: updateResultTotalTime
          description: Determine test result total time from the test step total times. Added in version 2.
          type: boolean
          default: false
      responses:
        200:
          $ref: '#/responses/StepsPartialSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
    post:
      tags: [steps]
      summary: Create test steps
      description: Creates new test steps from the supplied models. The result associated with the step must exist prior to step creation. The server automatically generates step ids if not supplied.
      operationId: create-steps
      x-ni-operation: createSteps
      x-ni-auth: true
      parameters:
        - in: body
          name: requestBody
          description: Test step object
          required: true
          schema:
            $ref: '#/definitions/TestStepCreateOrUpdateRequestObject'
        - in: query
          name: updateResultTotalTime
          description: Determine test result total time from the test step total times. Added in version 2.
          type: boolean
          default: false
      responses:
        200:
          $ref: '#/responses/StepsPartialSuccessResponse'
        201:
          $ref: '#/responses/StepsSuccessResponse'
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/results/{resultId}/steps/{stepId}:
    delete:
      tags: [steps]
      summary: Deletes a test step
      description: Deletes the test step with the specified id. The request succeeds for step ids that do not exist.
      operationId: DeleteStep
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
          description: Determine test result total time from the test step total times. Added in version 2.
          type: boolean
          default: false
      responses:
        204:
          description: The resource was deleted successfully.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/delete-steps:
    post:
      tags: [steps]
      summary: Deletes test steps
      description: Deletes multiple test steps in a single request.
      operationId: delete-steps
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
          description: Determine test result total time from the test step total times. Added in version 2.
          type: boolean
          default: false
      responses:
        200:
          $ref: '#/responses/StepsDeletePartialSuccessResponse'
        204:
          description: The resource was deleted successfully.
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
  /v1/ping:
    get:
      tags: [deprecated]
      summary: Pings the test monitor service
      description: Deprecated. Pings the test monitor service to ensure that it is online.
      operationId: ping
      deprecated: true
      responses:
        204:
          description: No Content
        401:
          $ref: '#/responses/Unauthorized'
        default:
          $ref: '#/responses/Error'
````

<!--NI_OSS_SOURCE repo=systemlink-OpenAPI-documents path=test-monitor/nitestmonitor-v2.yml sha256=717113e128c9fe040d2cf5e109240dddf8f6795f49f9091bec55eee08ef8bae9 bytes=83541 -->
## FILE: test-monitor/nitestmonitor-v2.yml

- repository: `ni/systemlink-OpenAPI-documents`
- source_path: `test-monitor/nitestmonitor-v2.yml`
- sha256: `717113e128c9fe040d2cf5e109240dddf8f6795f49f9091bec55eee08ef8bae9`
- bytes: 83541

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
      - STATUS_TYPE_SUMMARY
      - WORKSPACE
    example:
      PROGRAM_NAME
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
    example:
      STEP_TYPE
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
        description: Array of file IDs attached to the product
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
        description: Array of file IDs attached to the product
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
        description: Array of file IDs attached to the product
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
        description: Array of file ids attached to the test result
        type: array
        items:
          type: string
        example: [5e30934193cac8046851acb2]
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
        description: Array of file ids attached to the test result
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
        description: Array of file ids attached to the test result
        type: array
        items:
          type: string
        example: [5e30934193cac8046851acb2]
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
        description: Array of file ids attached to the test result
        type: array
        items:
          type: string
        example: [5e30934193cac8046851acb2]
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
    type: object
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
    type: object
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
        $ref: '#/definitions/ProductField'
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
    type: object
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
        $ref: '#/definitions/PathField'
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
    description: >-
      Test Result fields that the response can be ordered by are
      `ID`, `STARTED_AT`, `UPDATED_AT`, `PROGRAM_NAME`, `SYSTEM_ID`, 
      `HOST_NAME`, `OPERATOR`, `SERIAL_NUMBER`, `PART_NUMBER`, 
      and `TOTAL_TIME_IN_SECONDS`.
    type: object
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
        $ref: '#/definitions/ResultField'
      descending:
        description: ->
          Whether to return the results in descending order.
        type: boolean
        default: false
        example: false
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
    type: object
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
        $ref: '#/definitions/StepField'
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
    type: object
    required:
    - field
    properties:
      field:
        $ref: '#/definitions/ProductField'
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
    type: object
    required:
    - field
    properties:
      field:
        $ref: '#/definitions/ResultField'
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
    type: object
    required:
    - field
    properties:
      field:
        $ref: '#/definitions/StepField'
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
    type: object
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
  TestStepCreateOrUpdateRequestObject:
    title: Test Step Create or Update Request
    type: object
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
            type: object
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
            type: object
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
            type: object
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
            type: object
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
            type: object
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
            $ref: '#/definitions/TestStepCreateOrUpdateRequestObject'
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
            $ref: '#/definitions/TestStepCreateOrUpdateRequestObject'
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
