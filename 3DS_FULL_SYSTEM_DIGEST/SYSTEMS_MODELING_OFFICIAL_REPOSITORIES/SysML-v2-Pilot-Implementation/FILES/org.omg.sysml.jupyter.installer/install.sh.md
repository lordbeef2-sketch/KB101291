# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.jupyter.installer/install.sh

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.jupyter.installer/install.sh`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.jupyter.installer/install.sh
- source_bytes: 2094
- source_sha256: `9b02744311b9c4b9d0c170b041ce121974c7917ed4db3bce57bbddbe8571a3c1`
- decoded_as: `utf-8`


## EXACT SOURCE

````bash
#!/bin/sh
#
# SysML 2 Pilot Implementation
# Copyright (C) 2020 California Institute of Technology ("Caltech")
# Copyright (C) 2021 Twingineer LLC
# Copyright (C) 2021 Model Driven Solutions, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Eclipse Public License as published by
# the Eclipse Foundation, version 2 of the License.
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Eclipse Public License for more details.
# You should have received a copy of the Eclipse Public License
# along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
#
# @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
#

set -e

SYSML_VERSION="${project.version.unqualified}"

echo "--- Step 1: Testing Conda installation ---"
command -v conda || (echo "Conda is not installed. Please install Conda and re-run." && return 1)
conda --version

echo "--- Step 2: Testing Java installation ---"
command -v java || (echo "Java is not installed. Please install Java and re-run." && return 1)
java -version

echo "--- Step 3: Installing Jupyter SysML kernel and dependencies ---"
jupyter kernelspec remove sysml -f > /dev/null 2>&1 || true
conda install "jupyter-sysml-kernel=$SYSML_VERSION" python=3.* jupyterlab=4.* graphviz=2.* nodejs -c conda-forge -y

echo "--- Step 4: Installing JupyterLab SysML extension ---"
jupyter labextension uninstall @systems-modeling/jupyterlab-sysml > /dev/null 2>&1 || true
jupyter labextension install "@systems-modeling/jupyterlab-sysml@$SYSML_VERSION"

echo "--- Step 5: Customizing JupyterLab ---"
python3 "$(dirname $0)/install.py"

echo "--- Step 6: Running Jupyter environment ---"
echo "To launch JupyterLab you can now run \"jupyter lab\" from Command Prompt."
echo "Re-running this script is not necessary and will re-install the environment."
printf "\n\n"
````
