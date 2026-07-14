# NOMAGIC ATTACHMENT: CATIA_No_Magic_log4j_procedure_V4.pdf

- attachment_id: `85768114`
- space_key: `FAQ`
- parent_page_id: `85764682`
- parent_page_title: CATIA Magic and No Magic products affected by Log4j vulnerability - CVE-2021-44228, CVE-2021-45046, CVE-2021-44832
- media_type: `application/pdf`
- reported_bytes: 764075
- download_url: https://docs.nomagic.com/download/attachments/85764682/CATIA_No_Magic_log4j_procedure_V4.pdf?version=1&modificationDate=1641485130791&api=v2
- payload_kind: `pdf-extracted`
- downloaded_sha256: `057159b82538920d36f252994cedb93a94e35cb9eae75d8ef9dcc052799b1827`

## LAYOUT-PRESERVING PDF EXTRACTION

### PDF PAGE 1

```text
Procedure to mitigate the risk concerning the CVE-2021-44228
vulnerability.

Please find below the tested and validated procedure to mitigate the risk concerning the CVE-
202144228 vulnerability.

For modeling tools (Magic Software Architect, Magic Cyber Systems
Engineer, Magic Systems of Systems Architect, MagicDraw, Cameo Systems
Modeler, Cameo Enterprise Architecture)

In your installation base, please search for the following file: log4j-core-2*.jar

 If you do not find any result, you can stop the procedure here. Your installation is not vulnerable
 If you find a match, the log4j2 library is installed and could be exploited. Please execute these steps:

    1. Make sure application is not running
    2. Download log4j v2.16.0 (or 2.17.1) from apache website (link)
    3. Search now for these jar files in installation base

              o log4j-core-2.*.jar
              o log4j-1.2-api-2.*.jar
              o log4j-api-2.*.jar
              o log4j-slf4j-impl-2.*.jar
    4. Replace any match by the 2.16.0 (or 2.17.1) version. Make sure the original filename is
         unchanged. See example below.
    5. The replacing and renaming operations must be performed for all jar files found from the list

Example - if you find log4j-core-2.11.2.jar:

    1. Remove log4j-core-2.11.2.jar
    2. Copy log4j-core-2.16.0.jar to the same location
    3. Rename log4j-core-2.16.0.jar to log4j-core-2.11.2.jar

For collaboration tools (Magic Collaboration Studio, Cameo Collaborator for
Teamwork Cloud, Teamwork Cloud)

In your installation base, please search for the following files: webapp.war, admin.war,
collaborator.war, document-exporter.war, resource-usage-map.war, resources.war.

 If you do not find any result, you can stop the procedure here. Your installation does not contain
    web applications

 If you find a match, you might need to replace log4j2 libraries inside each found war files (for
    example webapp.war). Please execute these steps:

    1. Make sure application is not running
    2. Download log4j v2.16.0 (or 2.17.1) from apache website (link)
```

### PDF PAGE 2

```text
    3. Uncompress (unzip) webapp.war into any tmp folder
    4. Search now for these jar files among unzipped ones

              o log4j-core-2.*.jar
              o log4j-api-2.*.jar
    5. Replace any match by the 2.16.0 (or 2.17.1) version. Make sure the original filename is
         unchanged. See example below.

         NOTE: For collaboration tools of 19.0 SPx version (Magic Collaboration Studio, Cameo
         Collaborator for Teamwork Cloud, Teamwork Cloud):

               look for a file named org.apache.log4j-19.0.0.jar. Delete it if found.

    6. Compress (zip) all extracted files back to webapp_patched.war. Make sure files structure in new
         war is same as in original war.

    7. Replace original webapp.war with webapp_patched.war and restore name back
         to webapp.war

    8. Look for a folder named webapp next to webapp.war. Delete it if found.
    9. Start application

Example - if you find log4j-core-2.11.2.jar:

    1. Remove log4j-core-2.11.2.jar
    2. Copy log4j-core-2.16.0.jar to the same location
    3. Rename log4j-core-2.16.0.jar to log4j-core-2.11.2.jar
```


## EXACT ATTACHMENT METADATA

````json
{
  "id": "85768114",
  "type": "attachment",
  "status": "current",
  "title": "CATIA_No_Magic_log4j_procedure_V4.pdf",
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
    "when": "2022-01-06T17:05:30.791+01:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/85768114/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/85768114"
    }
  },
  "position": -1,
  "container": {
    "id": "85764682",
    "type": "page",
    "status": "current",
    "title": "CATIA Magic and No Magic products affected by Log4j vulnerability - CVE-2021-44228, CVE-2021-45046, CVE-2021-44832",
    "position": -1,
    "extensions": {
      "position": "none"
    },
    "_links": {
      "webui": "/spaces/FAQ/pages/85764682/CATIA+Magic+and+No+Magic+products+affected+by+Log4j+vulnerability+-+CVE-2021-44228+CVE-2021-45046+CVE-2021-44832",
      "edit": "/pages/resumedraft.action?draftId=85764682&draftShareId=40a3ab2a-ceda-401c-84d0-b0eb6c691816",
      "tinyui": "/x/SqocBQ",
      "self": "https://docs.nomagic.com/rest/api/content/85764682"
    },
    "_expandable": {
      "container": "/rest/api/space/FAQ",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/85764682/child",
      "restrictions": "/rest/api/content/85764682/restriction/byOperation",
      "history": "/rest/api/content/85764682/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/85764682/descendant",
      "space": "/rest/api/space/FAQ",
      "relevantViewRestrictions": "/rest/api/content/85764682/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/pdf"
  },
  "extensions": {
    "mediaType": "application/pdf",
    "fileSize": 764075,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/85764682/CATIA_No_Magic_log4j_procedure_V4.pdf?version=1&modificationDate=1641485130791&api=v2",
    "webui": "/spaces/FAQ/pages/85764682/CATIA+Magic+and+No+Magic+products+affected+by+Log4j+vulnerability+-+CVE-2021-44228+CVE-2021-45046+CVE-2021-44832?preview=%2F85764682%2F85768114%2FCATIA_No_Magic_log4j_procedure_V4.pdf",
    "self": "https://docs.nomagic.com/rest/api/content/85768114"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/85768114/child",
    "restrictions": "/rest/api/content/85768114/restriction/byOperation",
    "history": "/rest/api/content/85768114/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/85768114/descendant",
    "space": "/rest/api/space/FAQ",
    "relevantViewRestrictions": "/rest/api/content/85768114/restriction/relevantViewRestrictions"
  }
}
````
