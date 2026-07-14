# NOMAGIC ATTACHMENT: script_commandline.bat

- attachment_id: `189140111`
- space_key: `MD2024xR2`
- parent_page_id: `189140110`
- parent_page_title: Running the CATIA FLXML Exporter plugin in command line
- media_type: `application/octet-stream`
- reported_bytes: 1295
- download_url: https://docs.nomagic.com/download/attachments/189140110/script_commandline.bat?version=1&modificationDate=1727980603595&api=v2
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
  "id": "189140111",
  "type": "attachment",
  "status": "current",
  "title": "script_commandline.bat",
  "version": {
    "by": {
      "type": "known",
      "username": "kbe12",
      "userKey": "2c9f81f87674fd7d017a0928ba470000",
      "profilePicture": {
        "path": "/images/icons/profilepics/default.svg",
        "width": 48,
        "height": 48,
        "isDefault": true
      },
      "displayName": "Kristina B.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=2c9f81f87674fd7d017a0928ba470000"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2024-10-03T20:36:43.595+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/189140111/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/189140111"
    }
  },
  "position": -1,
  "container": {
    "id": "189140110",
    "type": "page",
    "status": "current",
    "title": "Running the CATIA FLXML Exporter plugin in command line",
    "position": -1,
    "extensions": {
      "position": "none"
    },
    "_links": {
      "webui": "/spaces/MD2024xR2/pages/189140110/Running+the+CATIA+FLXML+Exporter+plugin+in+command+line",
      "edit": "/pages/resumedraft.action?draftId=189140110",
      "tinyui": "/x/jgxGCw",
      "self": "https://docs.nomagic.com/rest/api/content/189140110"
    },
    "_expandable": {
      "container": "/rest/api/space/MD2024xR2",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/189140110/child",
      "restrictions": "/rest/api/content/189140110/restriction/byOperation",
      "history": "/rest/api/content/189140110/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/189140110/descendant",
      "space": "/rest/api/space/MD2024xR2",
      "relevantViewRestrictions": "/rest/api/content/189140110/restriction/relevantViewRestrictions"
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
    "download": "/download/attachments/189140110/script_commandline.bat?version=1&modificationDate=1727980603595&api=v2",
    "webui": "/spaces/MD2024xR2/pages/189140110/Running+the+CATIA+FLXML+Exporter+plugin+in+command+line?preview=%2F189140110%2F189140111%2Fscript_commandline.bat",
    "self": "https://docs.nomagic.com/rest/api/content/189140111"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/189140111/child",
    "restrictions": "/rest/api/content/189140111/restriction/byOperation",
    "history": "/rest/api/content/189140111/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/189140111/descendant",
    "space": "/rest/api/space/MD2024xR2",
    "relevantViewRestrictions": "/rest/api/content/189140111/restriction/relevantViewRestrictions"
  }
}
````
