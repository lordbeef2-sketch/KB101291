# OFFICIAL REPOSITORY FILE: SysML-v2-API-Cookbook/Req_Str_Beh_Decomposition_Recipe.ipynb

- repository: `SysML-v2-API-Cookbook`
- source_path: `Req_Str_Beh_Decomposition_Recipe.ipynb`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Cookbook/blob/7a7d92939e6c68533d61bbd8d308037e814abd96/Req_Str_Beh_Decomposition_Recipe.ipynb
- source_bytes: 12909
- source_sha256: `32d5eeac82fdd58a725409f00eafe6ec54dded3ca0ac6fa58f8e529da0a5373c`
- decoded_as: `utf-8`

## NORMALIZED NOTEBOOK CELLS

### CELL 1: markdown

# Initializing the SysML v2 API

### CELL 2: code

from __future__ import print_function

import time
import requests
from pprint import pprint
import pandas as pd
import json

#host = "<SysML2-API-Repo-Host:Port>"
host = "Specify the URL of the SysML v2 API and Service Repository"

### CELL 3: markdown

# Get projects

### CELL 4: code

projects_url = f"{host}/projects" 
projects_response = requests.get(projects_url)

if projects_response.status_code == 200:
    projects = projects_response.json()
    
    df = pd.DataFrame({'Project Name':[], 'Project ID':[]})
    for p in projects:
        df = pd.concat([df, pd.DataFrame({'Project Name':[p['name']], 'Project ID':[p['@id']]})], ignore_index=True)
    display(df)

### CELL 5: markdown

# Define a function to recursively iterate over feature members 
## Recursive graph traversal using FeatureMembership relations

### CELL 6: code

def get_member_features(project_id, commit_id, element_id, member_type, indent):
    
    # Fetch the element
    element_url = f"{host}/projects/{project_id}/commits/{commit_id}/elements/{element_id}" 
    response = requests.get(element_url)
    
    element_data = response.json()
    element_name = element_data['name']
    element_id = element_data['@id']
    element_type = element_data ['@type']
    
    if element_type == member_type:
        print(f"{indent} - {element_name} (id = {element_id}, type = {element_type})")
        # Feature memberships
        element_features = element_data['feature']
        if len(element_features) > 0:
            for feature in element_features:
                get_member_features(project_id, commit_id, feature['@id'], member_type, indent + "  ")


### CELL 7: markdown

# Parts tree navigation

### CELL 8: code

parts_tree_project_id = '85d874ae-1f68-4949-9b16-378f1cbc477e'
parts_tree_commit_id = ''

commits_url = f"{host}/projects/{parts_tree_project_id}/commits" 
commits_response = requests.get(commits_url)
if commits_response.status_code == 200:
    commits = commits_response.json()
    pprint(commits)
    parts_tree_commit_id = commits[0]['@id']


### CELL 9: markdown

## Query to find vehicle1

### CELL 10: code

# Query vehicle1 (PartUsage) in the 
data = {
  '@type':'Query',
  'select': ['name','@id','@type','owner'],
  'where': {
    '@type': 'CompositeConstraint',
    'operator': 'and',
    'constraint': [
        {
            '@type': 'PrimitiveConstraint',
            'inverse': False,
            'operator': '=',
            'property': 'name',
            'value': 'vehicle1'
        },
        {
            '@type': 'PrimitiveConstraint',
            'inverse': False,
            'operator': '=',
            'property': '@type',
            'value': 'PartUsage'
        }
    ]
  }
}

payload = json.dumps(data)

vehicle1_id = ''
query_url = f"{host}/projects/{parts_tree_project_id}/query-results" 

query_response = requests.post(query_url, json=data)

if query_response.status_code == 200:
    query_response_json = query_response.json()
    pprint(query_response_json)
    vehicle1_id = query_response_json[0]['@id']

### CELL 11: markdown

## Parts tree for vehicle1 (recursive FeatureMembership relation navigation)

### CELL 12: code

get_member_features(parts_tree_project_id,parts_tree_commit_id,vehicle1_id,'PartUsage'," ")

### CELL 13: markdown

## Query to find vehicle1_c1

### CELL 14: code


data = {
  '@type':'Query',
  'select': ['name','@id','@type','owner'],
  'where': {
    '@type': 'CompositeConstraint',
    'operator': 'and',
    'constraint': [
        {
            '@type': 'PrimitiveConstraint',
            'inverse': False,
            'operator': '=',
            'property': 'name',
            'value': 'vehicle1_c1'
        },
        {
            '@type': 'PrimitiveConstraint',
            'inverse': False,
            'operator': '=',
            'property': '@type',
            'value': 'PartUsage'
        }
    ]
  }
}
payload = json.dumps(data)

vehicle1_c1_id = ''
query_url = f"{host}/projects/{parts_tree_project_id}/query-results" 

query_response = requests.post(query_url, json=data)

if query_response.status_code == 200:
    query_response_json = query_response.json()
    pprint(query_response_json)
    vehicle1_c1_id = query_response_json[0]['@id']

### CELL 15: markdown

## Parts tree for vehicle1_c1 (recursive FeatureMembership relation navigation)

### CELL 16: code

get_member_features(parts_tree_project_id,parts_tree_commit_id,vehicle1_c1_id,'PartUsage'," ")

### CELL 17: markdown

# Behavior Tree Navigation

### CELL 18: code

behavior_project_id = '128710cd-978f-4c6f-93ac-8afbbd194185'
behavior_project_commit_id = ''

commits_url = f"{host}/projects/{behavior_project_id}/commits" 
commits_response = requests.get(commits_url)
if commits_response.status_code == 200:
    commits = commits_response.json()
    pprint(commits)
    behavior_project_commit_id = commits[0]['@id']

### CELL 19: markdown

## Query to find Provide Power behavior (ActionUsage)

### CELL 20: code

data = {
  '@type':'Query',
  'select': ['name','@id','@type','owner'],
  'where': {
    '@type': 'CompositeConstraint',
    'operator': 'and',
    'constraint': [
        {
            '@type': 'PrimitiveConstraint',
            'inverse': False,
            'operator': '=',
            'property': 'name',
            'value': 'provide power'
        },
        {
            '@type': 'PrimitiveConstraint',
            'inverse': False,
            'operator': '=',
            'property': '@type',
            'value': 'ActionUsage'
        }
    ]
  }
}

payload = json.dumps(data)

provide_power_id = ''
query_url = f"{host}/projects/{behavior_project_id}/query-results" 

query_response = requests.post(query_url, json=data)

if query_response.status_code == 200:
    query_response_json = query_response.json()
    pprint(query_response_json)
    provide_power_id = query_response_json[0]['@id']

### CELL 21: markdown

## Behavior tree for vehicle1 (recursive FeatureMembership relation navigation)

### CELL 22: code

get_member_features(behavior_project_id, behavior_project_commit_id, provide_power_id,"ActionUsage"," ")

### CELL 23: markdown

# Requirement tree for vehicle

### CELL 24: code

simple_vehicle_model_project = '8b377f03-9f29-4ae9-b60b-d266dc4a8180'
vehicle_commit = '10f84681-3d17-43be-b59a-89c480d1abeb'

### CELL 25: code

data = {
  '@type':'Query',
  'select': ['name','@id','@type','owner'],
  'where': {
    '@type': 'CompositeConstraint',
    'operator': 'and',
    'constraint': [
        {
            '@type': 'PrimitiveConstraint',
            'inverse': False,
            'operator': '=',
            'property': 'name',
            'value': 'vehicleSpecification'
        },
        {
            '@type': 'PrimitiveConstraint',
            'inverse': False,
            'operator': '=',
            'property': '@type',
            'value': 'RequirementUsage'
        }
    ]
  }
}

payload = json.dumps(data)

vehicle_specification_id = ''
query_url = f"{host}/projects/{simple_vehicle_model_project}/query-results" 

query_response = requests.post(query_url, json=data)

if query_response.status_code == 200:
    query_response_json = query_response.json()
    pprint(query_response_json)
    vehicle_specification_id = query_response_json[0]['@id']

### CELL 26: code

get_member_features(simple_vehicle_model_project, vehicle_commit, vehicle_specification_id,"RequirementUsage"," ")

## EXACT SOURCE

````json
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3ee4834f",
   "metadata": {},
   "source": [
    "# Initializing the SysML v2 API"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b5fef59",
   "metadata": {},
   "outputs": [],
   "source": [
    "from __future__ import print_function\n",
    "\n",
    "import time\n",
    "import requests\n",
    "from pprint import pprint\n",
    "import pandas as pd\n",
    "import json\n",
    "\n",
    "#host = \"<SysML2-API-Repo-Host:Port>\"\n",
    "host = \"Specify the URL of the SysML v2 API and Service Repository\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "04c1ff93",
   "metadata": {},
   "source": [
    "# Get projects"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78788ed9",
   "metadata": {},
   "outputs": [],
   "source": [
    "projects_url = f\"{host}/projects\" \n",
    "projects_response = requests.get(projects_url)\n",
    "\n",
    "if projects_response.status_code == 200:\n",
    "    projects = projects_response.json()\n",
    "    \n",
    "    df = pd.DataFrame({'Project Name':[], 'Project ID':[]})\n",
    "    for p in projects:\n",
    "        df = pd.concat([df, pd.DataFrame({'Project Name':[p['name']], 'Project ID':[p['@id']]})], ignore_index=True)\n",
    "    display(df)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d815e4fe",
   "metadata": {},
   "source": [
    "# Define a function to recursively iterate over feature members \n",
    "## Recursive graph traversal using FeatureMembership relations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24ec6146",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_member_features(project_id, commit_id, element_id, member_type, indent):\n",
    "    \n",
    "    # Fetch the element\n",
    "    element_url = f\"{host}/projects/{project_id}/commits/{commit_id}/elements/{element_id}\" \n",
    "    response = requests.get(element_url)\n",
    "    \n",
    "    element_data = response.json()\n",
    "    element_name = element_data['name']\n",
    "    element_id = element_data['@id']\n",
    "    element_type = element_data ['@type']\n",
    "    \n",
    "    if element_type == member_type:\n",
    "        print(f\"{indent} - {element_name} (id = {element_id}, type = {element_type})\")\n",
    "        # Feature memberships\n",
    "        element_features = element_data['feature']\n",
    "        if len(element_features) > 0:\n",
    "            for feature in element_features:\n",
    "                get_member_features(project_id, commit_id, feature['@id'], member_type, indent + \"  \")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2aff54c2",
   "metadata": {},
   "source": [
    "# Parts tree navigation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "482ddfe4",
   "metadata": {},
   "outputs": [],
   "source": [
    "parts_tree_project_id = '85d874ae-1f68-4949-9b16-378f1cbc477e'\n",
    "parts_tree_commit_id = ''\n",
    "\n",
    "commits_url = f\"{host}/projects/{parts_tree_project_id}/commits\" \n",
    "commits_response = requests.get(commits_url)\n",
    "if commits_response.status_code == 200:\n",
    "    commits = commits_response.json()\n",
    "    pprint(commits)\n",
    "    parts_tree_commit_id = commits[0]['@id']\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "487c0624",
   "metadata": {},
   "source": [
    "## Query to find vehicle1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d724e27",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Query vehicle1 (PartUsage) in the \n",
    "data = {\n",
    "  '@type':'Query',\n",
    "  'select': ['name','@id','@type','owner'],\n",
    "  'where': {\n",
    "    '@type': 'CompositeConstraint',\n",
    "    'operator': 'and',\n",
    "    'constraint': [\n",
    "        {\n",
    "            '@type': 'PrimitiveConstraint',\n",
    "            'inverse': False,\n",
    "            'operator': '=',\n",
    "            'property': 'name',\n",
    "            'value': 'vehicle1'\n",
    "        },\n",
    "        {\n",
    "            '@type': 'PrimitiveConstraint',\n",
    "            'inverse': False,\n",
    "            'operator': '=',\n",
    "            'property': '@type',\n",
    "            'value': 'PartUsage'\n",
    "        }\n",
    "    ]\n",
    "  }\n",
    "}\n",
    "\n",
    "payload = json.dumps(data)\n",
    "\n",
    "vehicle1_id = ''\n",
    "query_url = f\"{host}/projects/{parts_tree_project_id}/query-results\" \n",
    "\n",
    "query_response = requests.post(query_url, json=data)\n",
    "\n",
    "if query_response.status_code == 200:\n",
    "    query_response_json = query_response.json()\n",
    "    pprint(query_response_json)\n",
    "    vehicle1_id = query_response_json[0]['@id']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0092a660",
   "metadata": {},
   "source": [
    "## Parts tree for vehicle1 (recursive FeatureMembership relation navigation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "406504bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "get_member_features(parts_tree_project_id,parts_tree_commit_id,vehicle1_id,'PartUsage',\" \")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eba630b9",
   "metadata": {},
   "source": [
    "## Query to find vehicle1_c1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c13178f",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "data = {\n",
    "  '@type':'Query',\n",
    "  'select': ['name','@id','@type','owner'],\n",
    "  'where': {\n",
    "    '@type': 'CompositeConstraint',\n",
    "    'operator': 'and',\n",
    "    'constraint': [\n",
    "        {\n",
    "            '@type': 'PrimitiveConstraint',\n",
    "            'inverse': False,\n",
    "            'operator': '=',\n",
    "            'property': 'name',\n",
    "            'value': 'vehicle1_c1'\n",
    "        },\n",
    "        {\n",
    "            '@type': 'PrimitiveConstraint',\n",
    "            'inverse': False,\n",
    "            'operator': '=',\n",
    "            'property': '@type',\n",
    "            'value': 'PartUsage'\n",
    "        }\n",
    "    ]\n",
    "  }\n",
    "}\n",
    "payload = json.dumps(data)\n",
    "\n",
    "vehicle1_c1_id = ''\n",
    "query_url = f\"{host}/projects/{parts_tree_project_id}/query-results\" \n",
    "\n",
    "query_response = requests.post(query_url, json=data)\n",
    "\n",
    "if query_response.status_code == 200:\n",
    "    query_response_json = query_response.json()\n",
    "    pprint(query_response_json)\n",
    "    vehicle1_c1_id = query_response_json[0]['@id']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "10b45dd4",
   "metadata": {},
   "source": [
    "## Parts tree for vehicle1_c1 (recursive FeatureMembership relation navigation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1dbfe8f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "get_member_features(parts_tree_project_id,parts_tree_commit_id,vehicle1_c1_id,'PartUsage',\" \")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7319e39",
   "metadata": {},
   "source": [
    "# Behavior Tree Navigation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9c96cbe",
   "metadata": {},
   "outputs": [],
   "source": [
    "behavior_project_id = '128710cd-978f-4c6f-93ac-8afbbd194185'\n",
    "behavior_project_commit_id = ''\n",
    "\n",
    "commits_url = f\"{host}/projects/{behavior_project_id}/commits\" \n",
    "commits_response = requests.get(commits_url)\n",
    "if commits_response.status_code == 200:\n",
    "    commits = commits_response.json()\n",
    "    pprint(commits)\n",
    "    behavior_project_commit_id = commits[0]['@id']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d7c309e",
   "metadata": {},
   "source": [
    "## Query to find Provide Power behavior (ActionUsage)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5a63113",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {\n",
    "  '@type':'Query',\n",
    "  'select': ['name','@id','@type','owner'],\n",
    "  'where': {\n",
    "    '@type': 'CompositeConstraint',\n",
    "    'operator': 'and',\n",
    "    'constraint': [\n",
    "        {\n",
    "            '@type': 'PrimitiveConstraint',\n",
    "            'inverse': False,\n",
    "            'operator': '=',\n",
    "            'property': 'name',\n",
    "            'value': 'provide power'\n",
    "        },\n",
    "        {\n",
    "            '@type': 'PrimitiveConstraint',\n",
    "            'inverse': False,\n",
    "            'operator': '=',\n",
    "            'property': '@type',\n",
    "            'value': 'ActionUsage'\n",
    "        }\n",
    "    ]\n",
    "  }\n",
    "}\n",
    "\n",
    "payload = json.dumps(data)\n",
    "\n",
    "provide_power_id = ''\n",
    "query_url = f\"{host}/projects/{behavior_project_id}/query-results\" \n",
    "\n",
    "query_response = requests.post(query_url, json=data)\n",
    "\n",
    "if query_response.status_code == 200:\n",
    "    query_response_json = query_response.json()\n",
    "    pprint(query_response_json)\n",
    "    provide_power_id = query_response_json[0]['@id']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "10018cd0",
   "metadata": {},
   "source": [
    "## Behavior tree for vehicle1 (recursive FeatureMembership relation navigation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91193b07",
   "metadata": {},
   "outputs": [],
   "source": [
    "get_member_features(behavior_project_id, behavior_project_commit_id, provide_power_id,\"ActionUsage\",\" \")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a07cc348",
   "metadata": {},
   "source": [
    "# Requirement tree for vehicle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89840b26",
   "metadata": {},
   "outputs": [],
   "source": [
    "simple_vehicle_model_project = '8b377f03-9f29-4ae9-b60b-d266dc4a8180'\n",
    "vehicle_commit = '10f84681-3d17-43be-b59a-89c480d1abeb'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5fa94a05-c45e-4d93-a145-7e5967a87cd9",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {\n",
    "  '@type':'Query',\n",
    "  'select': ['name','@id','@type','owner'],\n",
    "  'where': {\n",
    "    '@type': 'CompositeConstraint',\n",
    "    'operator': 'and',\n",
    "    'constraint': [\n",
    "        {\n",
    "            '@type': 'PrimitiveConstraint',\n",
    "            'inverse': False,\n",
    "            'operator': '=',\n",
    "            'property': 'name',\n",
    "            'value': 'vehicleSpecification'\n",
    "        },\n",
    "        {\n",
    "            '@type': 'PrimitiveConstraint',\n",
    "            'inverse': False,\n",
    "            'operator': '=',\n",
    "            'property': '@type',\n",
    "            'value': 'RequirementUsage'\n",
    "        }\n",
    "    ]\n",
    "  }\n",
    "}\n",
    "\n",
    "payload = json.dumps(data)\n",
    "\n",
    "vehicle_specification_id = ''\n",
    "query_url = f\"{host}/projects/{simple_vehicle_model_project}/query-results\" \n",
    "\n",
    "query_response = requests.post(query_url, json=data)\n",
    "\n",
    "if query_response.status_code == 200:\n",
    "    query_response_json = query_response.json()\n",
    "    pprint(query_response_json)\n",
    "    vehicle_specification_id = query_response_json[0]['@id']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd2276aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "get_member_features(simple_vehicle_model_project, vehicle_commit, vehicle_specification_id,\"RequirementUsage\",\" \")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

````
