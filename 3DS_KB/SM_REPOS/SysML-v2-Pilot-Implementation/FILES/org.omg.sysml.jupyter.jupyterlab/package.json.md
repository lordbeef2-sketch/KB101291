# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.jupyter.jupyterlab/package.json

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.jupyter.jupyterlab/package.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.jupyter.jupyterlab/package.json
- source_bytes: 876
- source_sha256: `3b3402560cf23c09e90f585e8111f7019ae930c82ec1aadb44681adca1f897bc`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "name": "@systems-modeling/jupyterlab-sysml",
  "version": "0.60.0-SNAPSHOT",
  "description": "A JupyterLab extension for system modeling using SysML",
  "repository": "github:Systems-Modeling/SysML-v2-Pilot-Implementation",
  "author": "SysML v2 Submission Team",
  "license": "LGPL-3.0-or-later",
  "main": "build/plugin.js",
  "keywords": [
    "jupyter",
    "jupyterlab",
    "jupyterlab-extension"
  ],
  "dependencies": {
    "@jupyterlab/application": "4.x"
  },
  "devDependencies": {
    "@codemirror/legacy-modes": "^6.3.2",
    "@jupyterlab/codemirror": ">=4.0",
    "@types/json-schema": "*",
    "typescript": "~5.8.3"
  },
  "files": [
    "build/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}"
  ],
  "jupyterlab": {
    "extension": true
  },
  "scripts": {
    "build": "tsc",
    "watch": "tsc -w"
  }
}

````
