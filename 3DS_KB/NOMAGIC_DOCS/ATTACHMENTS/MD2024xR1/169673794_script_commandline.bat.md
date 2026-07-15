# NOMAGIC ATTACHMENT: script_commandline.bat

- attachment_id: `169673794`
- space_key: `MD2024xR1`
- parent_page_id: `169673793`
- parent_page_title: Running the CATIA FLXML Exporter plugin in command line
- media_type: `application/octet-stream`
- reported_bytes: 1295
- download_url: https://docs.nomagic.com/download/attachments/169673793/script_commandline.bat?version=1&modificationDate=1715140239463&api=v2
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
  "id": "169673794",
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
    "when": "2024-05-08T05:50:39.463+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/169673794/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/169673794"
    }
  },
  "position": -1,
  "container": {
    "id": "169673793",
    "type": "page",
    "status": "current",
    "title": "Running the CATIA FLXML Exporter plugin in command line",
    "position": -1,
    "extensions": {
      "position": "none"
    },
    "_links": {
      "webui": "/spaces/MD2024xR1/pages/169673793/Running+the+CATIA+FLXML+Exporter+plugin+in+command+line",
      "edit": "/pages/resumedraft.action?draftId=169673793",
      "tinyui": "/x/QQQdCg",
      "self": "https://docs.nomagic.com/rest/api/content/169673793"
    },
    "_expandable": {
      "container": "/rest/api/space/MD2024xR1",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/169673793/child",
      "restrictions": "/rest/api/content/169673793/restriction/byOperation",
      "history": "/rest/api/content/169673793/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/169673793/descendant",
      "space": "/rest/api/space/MD2024xR1",
      "relevantViewRestrictions": "/rest/api/content/169673793/restriction/relevantViewRestrictions"
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
    "download": "/download/attachments/169673793/script_commandline.bat?version=1&modificationDate=1715140239463&api=v2",
    "webui": "/spaces/MD2024xR1/pages/169673793/Running+the+CATIA+FLXML+Exporter+plugin+in+command+line?preview=%2F169673793%2F169673794%2Fscript_commandline.bat",
    "self": "https://docs.nomagic.com/rest/api/content/169673794"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/169673794/child",
    "restrictions": "/rest/api/content/169673794/restriction/byOperation",
    "history": "/rest/api/content/169673794/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/169673794/descendant",
    "space": "/rest/api/space/MD2024xR1",
    "relevantViewRestrictions": "/rest/api/content/169673794/restriction/relevantViewRestrictions"
  }
}
````
