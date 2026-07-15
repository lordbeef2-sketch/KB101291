# NOMAGIC ATTACHMENT: script_commandline.bat

- attachment_id: `258048975`
- space_key: `CFE`
- parent_page_id: `258048973`
- parent_page_title: (2026x) Running the CATIA FLXML Exporter plugin in command line
- media_type: `application/octet-stream`
- reported_bytes: 1295
- download_url: https://docs.nomagic.com/download/attachments/258048973/script_commandline.bat?version=1&modificationDate=1758798828088&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `0801e40e865fea6eeb379471c3144ffa4158f8949ad035c5d7fcfb490b2b1ea0`

## EXACT ATTACHMENT SOURCE

````text

@echo off
setlocal EnableExtensions
   
:: either local script variable or environment variable MAGICDRAW_HOME should be defined
set "%MAGICDRAW_HOME%"="<path_to_modeling_tool_install_directory>"
  
if "%MAGICDRAW_HOME%" == "" (
    echo MAGICDRAW_HOME environment variable not set, please set it to the MagicDraw installation folder
    exit /B 1
)
  
setlocal enableDelayedExpansion
:: change slashes if needed
set MAGICDRAW_HOME=!MAGICDRAW_HOME:\=/!
setlocal disableDelayedExpansion
    
pushd "%MAGICDRAW_HOME%"
    
:: Reads CLASSPATH value from magicdraw.properties files (change to your properties file name)
For /F "tokens=1* delims==" %%A IN (bin\magicdraw.properties) DO (
    IF "%%A"=="CLASSPATH" set MD_CLASSPATH=%%B
)
   
:: Modify classpath to a valid Windows style classpath. Replace \: with ;
set MD_CLASSPATH=%MD_CLASSPATH:\:=;%
    
:: Run the GenerateFLXMLCommandLineAction 
java -Xmx1200M -Xss1024K ^
     -cp "%MD_CLASSPATH%" ^
     -Desi.system.config="data\application.conf" ^
     -Dcom.nomagic.magicdraw.commandline.action=com.dassault_systemes.flxml.exporter.commandLine.GenerateFLXMLCommandLineAction ^
     com.nomagic.magicdraw.commandline.CommandLineActionLauncher properties="<path_to_generate_flxml.properties_file>"
 

popd

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "258048975",
  "type": "attachment",
  "status": "current",
  "title": "script_commandline.bat",
  "version": {
    "by": {
      "type": "known",
      "username": "ingabe",
      "userKey": "ff80808151f3008c0152c05ba1a40003",
      "profilePicture": {
        "path": "/download/attachments/7415957/user-avatar",
        "width": 48,
        "height": 48,
        "isDefault": false
      },
      "displayName": "Inga A.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=ff80808151f3008c0152c05ba1a40003"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2025-09-25T13:13:48.088+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/258048975/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/258048975"
    }
  },
  "position": -1,
  "container": {
    "id": "258048973",
    "type": "page",
    "status": "current",
    "title": "(2026x) Running the CATIA FLXML Exporter plugin in command line",
    "position": 2,
    "extensions": {
      "position": 2
    },
    "_links": {
      "webui": "/spaces/CFE/pages/258048973/2026x+Running+the+CATIA+FLXML+Exporter+plugin+in+command+line",
      "edit": "/pages/resumedraft.action?draftId=258048973",
      "tinyui": "/x/zYNhDw",
      "self": "https://docs.nomagic.com/rest/api/content/258048973"
    },
    "_expandable": {
      "container": "/rest/api/space/CFE",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/258048973/child",
      "restrictions": "/rest/api/content/258048973/restriction/byOperation",
      "history": "/rest/api/content/258048973/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/258048973/descendant",
      "space": "/rest/api/space/CFE",
      "relevantViewRestrictions": "/rest/api/content/258048973/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/octet-stream"
  },
  "extensions": {
    "mediaType": "application/octet-stream",
    "fileSize": 1295,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/258048973/script_commandline.bat?version=1&modificationDate=1758798828088&api=v2",
    "webui": "/spaces/CFE/pages/258048973/2026x+Running+the+CATIA+FLXML+Exporter+plugin+in+command+line?preview=%2F258048973%2F258048975%2Fscript_commandline.bat",
    "self": "https://docs.nomagic.com/rest/api/content/258048975"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/258048975/child",
    "restrictions": "/rest/api/content/258048975/restriction/byOperation",
    "history": "/rest/api/content/258048975/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/258048975/descendant",
    "space": "/rest/api/space/CFE",
    "relevantViewRestrictions": "/rest/api/content/258048975/restriction/relevantViewRestrictions"
  }
}
````
