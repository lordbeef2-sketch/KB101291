# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/public/docs/openapi-extensions.json

- repository: `SysML-v2-API-Services`
- source_path: `public/docs/openapi-extensions.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/public/docs/openapi-extensions.json
- source_bytes: 4549
- source_sha256: `3d7b118e4e369ef5b6d687b77870ef032a1ef57b0b32216bd3a5d43e1b353fae`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "tags": [
    {
      "name": "Extension"
    }
  ],
  "paths": {
    "/x/named/projects/{projectId}/commits": {
      "post": {
        "tags": [
          "Extension"
        ],
        "summary": "Create commit by project, resolving references by qualified name",
        "operationId": "postCommitByProjectNameResolved",
        "parameters": [
          {
            "name": "projectId",
            "in": "path",
            "description": "ID of the project",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "name": "branchId",
            "in": "query",
            "description": "ID of the branch - project's default branch if unspecified",
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Identified"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Commit"
                }
              }
            }
          },
          "415": {
            "description": "The requested content type is not acceptable.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "default": {
            "description": "Unexpected response.",
            "content": {}
          }
        },
        "x-codegen-request-body-name": "body"
      }
    },
    "/x/named/projects/{projectId}/commits/{commitId}/elements/{qualifiedName}": {
      "get": {
        "tags": [
          "Extension"
        ],
        "summary": "Get element by project, commit and qualified name",
        "operationId": "getElementByProjectCommitQualifiedName",
        "parameters": [
          {
            "name": "projectId",
            "in": "path",
            "description": "ID of the project",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "name": "commitId",
            "in": "path",
            "description": "ID of the commit",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "name": "qualifiedName",
            "in": "path",
            "description": "Qualified name of the element",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Ok",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Element"
                }
              }
            }
          },
          "404": {
            "description": "Not found.",
            "content": {}
          },
          "415": {
            "description": "The requested content type is not acceptable.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "default": {
            "description": "Unexpected response.",
            "content": {}
          }
        }
      }
    }
  }
}
````
