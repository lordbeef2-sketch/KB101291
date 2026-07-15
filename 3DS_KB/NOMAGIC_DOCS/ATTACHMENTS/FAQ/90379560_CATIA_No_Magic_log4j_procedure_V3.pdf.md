# NOMAGIC ATTACHMENT: CATIA_No_Magic_log4j_procedure_V3.pdf

- attachment_id: `90379560`
- space_key: `FAQ`
- parent_page_id: `90379558`
- parent_page_title: CATIA Magic and No Magic products affected by Spring Framework - Spring4Shell - vulnerability - CVE-2022-22965
- media_type: `application/pdf`
- reported_bytes: 738974
- download_url: https://docs.nomagic.com/download/attachments/90379558/CATIA_No_Magic_log4j_procedure_V3.pdf?version=1&modificationDate=1649072325364&api=v2
- payload_kind: `pdf-extracted`
- downloaded_sha256: `af29506a1d0c02115e05167e7acee795dc6405447dcc5a96dceffac1ee464968`

## LAYOUT-PRESERVING PDF EXTRACTION

### PDF PAGE 1

```text
Procedure to mitigate the risk concerning the CVE-2021-44228
vulnerability.

Please find below the tested and validated procedure to mitigate the risk concerning the CVE-2021-
44228 vulnerability.

For modeling tools (Magic Software Architect, Magic Cyber Systems Engineer, Magic
Systems of Systems Architect , MagicDraw, Cameo Systems Modeler, Cameo
Enterprise Architecture)

In your installation base, please search for the following file: log4j-core-2*.jar
If you do not find any result, you can stop the procedure here. Your installation is not vulnerable
If you find a match, the log4j2 library is installed and could be exploited. Please execute these
steps:

          Make sure application is not running
          Download log4j v2.16.0 (or 2.17.0) from apache website (link)
          Search now for these jar files

                   o log4j-core-2.*.jar
                   o log4j-1.2-api-2.*.jar
                   o log4j-api-2.*.jar
                   o log4j-slf4j-impl-2.*.jar
          Replace any match by the 2.16.0 (or 2.17.0) version. Make sure the original filename is
              unchanged. See example below.
          The replacing and renaming operations must be performed for all jar files found from
              the list

Example - if you find log4j-core-2.11.2.jar:

    1. Remove log4j-core-2.11.2.jar
    2. Copy log4j-core-2.16.0.jar to the same location
    3. Rename log4j-core-2.16.0.jar to log4j-core-2.11.2.jar

For collaboration tools (Magic Collaboration Studio, Cameo Collaborator for Teamwork
Cloud, Teamwork Cloud)

In your installation base, please search for the following files: webapp.war, admin.war,
collaborator.war, document-exporter.war, resource-usage-map.war, resources.war.
If you do not find any result, you can stop the procedure here. Your installation does not contain
web applications
If you find a match, you might need to replace log4j2 libraries inside found war files (for example
webapp.war). Please execute these steps with each found war file:

          Make sure application is not running
          Download log4j v2.16.0 (or 2.17.0) from apache website (link)
          Uncompress(unzip) webapp.war into any tmp folder
          Search now for these jar files among unzipped ones

                   o log4j-core-2.*.jar
                   o log4j-api-2.*.jar
```

### PDF PAGE 2

```text
          Replace any match by the 2.16.0 (or 2.17.0) version. Make sure the original filename is
              unchanged. See example below.

          Compress(zip) all extracted files back to webapp_patched.war. Make sure files structure
              in new war is same as in original war.

          Replace original webapp.war with webapp_patched.war and restore name back to
              webapp.war

          Look for a folder named webapp next to webapp.war. Delete folder if found.
          Start application

Example - if you find log4j-core-2.11.2.jar:

    1. Remove log4j-core-2.11.2.jar
    2. Copy log4j-core-2.16.0.jar to the same location
    3. Rename log4j-core-2.16.0.jar to log4j-core-2.11.2.jar
```


## EXACT ATTACHMENT METADATA

````json
{
  "id": "90379560",
  "type": "attachment",
  "status": "current",
  "title": "CATIA_No_Magic_log4j_procedure_V3.pdf",
  "version": {
    "by": {
      "type": "known",
      "username": "developer",
      "userKey": "8acad0e54bbfc3ed014c02c0967c0006",
      "profilePicture": {
        "path": "/images/icons/profilepics/default.svg",
        "width": 48,
        "height": 48,
        "isDefault": true
      },
      "displayName": "Developer",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=8acad0e54bbfc3ed014c02c0967c0006"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2022-04-04T13:38:45.364+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/90379560/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/90379560"
    }
  },
  "position": -1,
  "container": {
    "id": "90379558",
    "type": "page",
    "status": "current",
    "title": "CATIA Magic and No Magic products affected by Spring Framework - Spring4Shell - vulnerability - CVE-2022-22965",
    "position": -1,
    "extensions": {
      "position": "none"
    },
    "_links": {
      "webui": "/spaces/FAQ/pages/90379558/CATIA+Magic+and+No+Magic+products+affected+by+Spring+Framework+-+Spring4Shell+-+vulnerability+-+CVE-2022-22965",
      "edit": "/pages/resumedraft.action?draftId=90379558&draftShareId=06e1f6b7-300e-4691-8b8a-2a1f08d04f44",
      "tinyui": "/x/JhVjBQ",
      "self": "https://docs.nomagic.com/rest/api/content/90379558"
    },
    "_expandable": {
      "container": "/rest/api/space/FAQ",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/90379558/child",
      "restrictions": "/rest/api/content/90379558/restriction/byOperation",
      "history": "/rest/api/content/90379558/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/90379558/descendant",
      "space": "/rest/api/space/FAQ",
      "relevantViewRestrictions": "/rest/api/content/90379558/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/pdf"
  },
  "extensions": {
    "mediaType": "application/pdf",
    "fileSize": 738974,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/90379558/CATIA_No_Magic_log4j_procedure_V3.pdf?version=1&modificationDate=1649072325364&api=v2",
    "webui": "/spaces/FAQ/pages/90379558/CATIA+Magic+and+No+Magic+products+affected+by+Spring+Framework+-+Spring4Shell+-+vulnerability+-+CVE-2022-22965?preview=%2F90379558%2F90379560%2FCATIA_No_Magic_log4j_procedure_V3.pdf",
    "self": "https://docs.nomagic.com/rest/api/content/90379560"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/90379560/child",
    "restrictions": "/rest/api/content/90379560/restriction/byOperation",
    "history": "/rest/api/content/90379560/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/90379560/descendant",
    "space": "/rest/api/space/FAQ",
    "relevantViewRestrictions": "/rest/api/content/90379560/restriction/relevantViewRestrictions"
  }
}
````
