# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/clean.sh

- repository: `SysML-v2-API-Services`
- source_path: `clean.sh`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/clean.sh
- source_bytes: 327
- source_sha256: `89710c19be81f23a56ac12ad60ebdf689eec6827d4c03613d62877bc14492924`
- decoded_as: `utf-8`


## EXACT SOURCE

````bash
#!/usr/bin/env bash

set -e

find app/org/omg/sysml/metamodel/ -type f -not -name 'SysMLType.java' -not -name 'SysMLTypeImpl.java' -delete
rm generated/org/omg/sysml/metamodel/impl/* > /dev/null 2>&1 || true
rm conf/json/schema/metamodel/* > /dev/null 2>&1 || true
rm public/jsonld/metamodel/* > /dev/null 2>&1 || true

````
