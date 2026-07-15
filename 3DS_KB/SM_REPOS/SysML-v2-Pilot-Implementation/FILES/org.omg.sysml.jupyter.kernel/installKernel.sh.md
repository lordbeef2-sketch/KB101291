# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.jupyter.kernel/installKernel.sh

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.jupyter.kernel/installKernel.sh`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.jupyter.kernel/installKernel.sh
- source_bytes: 726
- source_sha256: `332836df8e0606a7a13352a96571f138ae90819e91a1dcc80ea151d5f6d61e81`
- decoded_as: `utf-8`


## EXACT SOURCE

````bash
#!/bin/sh

echo "--- Step 1: Testing Python installation ---"
if command -v python; then
     PYTHON="python"
else
    if command -v python3; then
        PYTHON="python3"
    else
        echo "Python is not installed. Please install Python and re-run."    
        exit 1
    fi
fi

command $PYTHON --version

echo "--- Step 2: Testing Java installation ---"

if ! command -v java; then
    echo "Java is not installed. Please install Java and re-run."
    exit 1
fi

echo "--- Step 3: Building kernel ---"

./../mvnw prepare-package resources:copy-resources@create-kernel -pl "org.omg.sysml:jupyter-sysml-kernel" -am

echo "--- Step 4: Installing kernel ---"

$PYTHON ./target/kernel/install.py
````
