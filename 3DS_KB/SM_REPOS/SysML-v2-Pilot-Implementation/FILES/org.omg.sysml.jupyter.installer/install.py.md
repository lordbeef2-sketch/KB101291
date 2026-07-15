# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.jupyter.installer/install.py

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.jupyter.installer/install.py`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.jupyter.installer/install.py
- source_bytes: 588
- source_sha256: `691418f236f976b297f348bd623cdbab6716f4c80cc06bac46e1d307c1fbc49a`
- decoded_as: `utf-8`


## EXACT SOURCE

````python
import json
import os
from jupyterlab.labapp import get_app_dir

if __name__ == '__main__':
    # Enable line numbers and code folding by default
    override_file = os.path.join(get_app_dir(), 'settings', 'overrides.json')
    settings = {
        '@jupyterlab/notebook-extension:tracker': {
            'codeCellConfig': {
                'lineNumbers': True,
                'codeFolding': True
            }
        }
    }
    os.makedirs(os.path.dirname(override_file), exist_ok=True)
    with open(override_file, 'w+') as f:
        f.write(json.dumps(settings))

````
