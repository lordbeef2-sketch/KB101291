# NOMAGIC ATTACHMENT: log4J_procedure.pdf

- attachment_id: `85764684`
- space_key: `FAQ`
- parent_page_id: `85764682`
- parent_page_title: CATIA Magic and No Magic products affected by Log4j vulnerability - CVE-2021-44228, CVE-2021-45046, CVE-2021-44832
- media_type: `application/pdf`
- reported_bytes: 797637
- download_url: https://docs.nomagic.com/download/attachments/85764682/log4J_procedure.pdf?version=1&modificationDate=1639412076064&api=v2
- payload_kind: `pdf-extracted`
- downloaded_sha256: `3cccf3009306ee75bdd17cdfe0a54306edb3edf9b1f7cf8d7e339e9772faeca1`

## LAYOUT-PRESERVING PDF EXTRACTION

### PDF PAGE 1

```text
Procedure to mitigate the risk concerning the CVE-2021-44228 vulnerability.

Please find below the tested and validated procedure to mitigate the risk concerning the CVE-2021-44228
vulnerability.

In your installation base, please search for the following file: *log4j-core*.jar
     If you do not find any result, you can stop the procedure here. Your installation is not vulnerable
     If you find a match, the log4j2 library is installed and could be exploited. Please execute these steps:
          Download log4j v2.15.0 from apache website (link)
          Search now for all the additional jar files (see complete list at the bottom) and replace any match by
              the 2.15.0 version. Make sure the original filename is unchanged.
          The replacing and renaming operations must be performed for all jar files found from the list

Example#1 (with version number in the name):
If you find log4j-core-2.11.2.jar:

    1. Remove log4j-core-2.11.2.jar
    2. Copy log4j-core-2.15.0.jar to the same location
    3. Rename log4j-core-2.15.0.jar to log4j-core-2.11.2.jar

Example#2 (without any version number in the name):
If you find log4j-docker.jar:

    1. Remove log4j-docker.jar
    2. Copy log4j-docker.jar to the same location
    3. Rename log4j-docker.jar to log4j-docker.jar

Complete list of jar files to look for if *log4j-core*.jar is found:
    o *log4j-1.2-api*.jar
    o *log4j-api*.jar
    o *log4j-appserver*.jar
    o *log4j-cassandra*.jar
    o *log4j-core*-tests.jar
    o *log4j-core*.jar
    o *log4j-couchdb*.jar
    o *log4j-docker*.jar
    o *log4j-flume-ng*.jar
    o *log4j-iostreams*.jar
    o *log4j-jcl*.jar
    o *log4j-jdbc-dbcp2*.jar
    o *log4j-jmx-gui*.jar
    o *log4j-jpa*.jar
    o *log4j-jul*.jar
    o *log4j-liquibase*.jar
    o *log4j-mongodb3*.jar
    o *log4j-mongodb4*.jar
    o *log4j-slf4j-impl*.jar
    o *log4j-slf4j18-impl*.jar
    o *log4j-spring-boot*.jar
    o *log4j-spring-cloud-config-client*.jar
    o *log4j-taglib*.jar
    o *log4j-to-slf4j*.jar
    o *log4j-web*.jar

Please restart the system.
```


## EXACT ATTACHMENT METADATA

````json
{
  "id": "85764684",
  "type": "attachment",
  "status": "current",
  "title": "log4J_procedure.pdf",
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
    "when": "2021-12-13T17:14:36.064+01:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/85764684/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/85764684"
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
    "fileSize": 797637,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/85764682/log4J_procedure.pdf?version=1&modificationDate=1639412076064&api=v2",
    "webui": "/spaces/FAQ/pages/85764682/CATIA+Magic+and+No+Magic+products+affected+by+Log4j+vulnerability+-+CVE-2021-44228+CVE-2021-45046+CVE-2021-44832?preview=%2F85764682%2F85764684%2Flog4J_procedure.pdf",
    "self": "https://docs.nomagic.com/rest/api/content/85764684"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/85764684/child",
    "restrictions": "/rest/api/content/85764684/restriction/byOperation",
    "history": "/rest/api/content/85764684/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/85764684/descendant",
    "space": "/rest/api/space/FAQ",
    "relevantViewRestrictions": "/rest/api/content/85764684/restriction/relevantViewRestrictions"
  }
}
````
