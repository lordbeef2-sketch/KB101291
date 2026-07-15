# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=imports/protobuf/data_moniker.proto sha256=df7e1af799f11a2a0c58c2a7704c111ea6035322bde7867aec1398bbec283051 bytes=1780 -->
## FILE: imports/protobuf/data_moniker.proto

- repository: `ni/grpc-device`
- source_path: `imports/protobuf/data_moniker.proto`
- sha256: `df7e1af799f11a2a0c58c2a7704c111ea6035322bde7867aec1398bbec283051`
- bytes: 1780

````protobuf
syntax = "proto3";

option cc_enable_arenas = true;
option csharp_namespace = "NationalInstruments.DataMonikers";

package ni.data_monikers;

import "google/protobuf/any.proto";

service DataMoniker {
  rpc BeginSidebandStream(BeginMonikerSidebandStreamRequest) returns (BeginMonikerSidebandStreamResponse) {};
  rpc StreamReadWrite(stream MonikerWriteRequest) returns (stream MonikerReadResponse) {};
  rpc StreamRead(MonikerList) returns (stream MonikerReadResponse) {};
  rpc StreamWrite(stream MonikerWriteRequest) returns (stream StreamWriteResponse) {};
}

enum SidebandStrategy
{
  UNKNOWN = 0;
  GRPC = 1;
  SHARED_MEMORY = 2;
  DOUBLE_BUFFERED_SHARED_MEMORY = 3;
  SOCKETS = 4;
  SOCKETS_LOW_LATENCY = 5;
  HYPERVISOR_SOCKETS = 6;
  RDMA = 7;
  RDMA_LOW_LATENCY = 8;
}

message BeginMonikerSidebandStreamRequest {
  SidebandStrategy strategy = 1;
  MonikerList monikers = 2;
}

message BeginMonikerSidebandStreamResponse {
  SidebandStrategy strategy = 1;
  string connection_url = 2;
  string sideband_identifier = 3;
  sint64 buffer_size = 4;
}

message Moniker {
  string service_location = 1;
  string data_source = 2;
  int64 data_instance = 3;
}

message MonikerWriteRequest {
  oneof write_data {
    MonikerList monikers = 1;
    MonikerValues data = 2;
  }
}

message MonikerReadResponse {
  MonikerValues data = 1;
}

message MonikerList {
  repeated Moniker read_monikers = 2;
  repeated Moniker write_monikers = 3;
}

message MonikerValues {
  repeated google.protobuf.Any values = 1;
}

message SidebandWriteRequest {
  bool cancel = 1;
  MonikerValues values = 2;
}

message SidebandReadResponse {
  bool cancel = 1;
  MonikerValues values = 2;
}

message StreamWriteResponse {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/protobuf/nidevice.proto sha256=9d146d9ae8a7d1b3f5af7dc305b511f0a6e9a1c89c4644a78657f356f2d5b6da bytes=622 -->
## FILE: imports/protobuf/nidevice.proto

- repository: `ni/grpc-device`
- source_path: `imports/protobuf/nidevice.proto`
- sha256: `9d146d9ae8a7d1b3f5af7dc305b511f0a6e9a1c89c4644a78657f356f2d5b6da`
- bytes: 622

````protobuf
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.device";
option java_outer_classname = "NiDevice";
option csharp_namespace = "NationalInstruments.Grpc.Device";

package nidevice_grpc;

message NIComplexNumber {
  double real = 1;
  double imaginary = 2;
}

message NIComplexNumberF32 {
  float real = 1;
  float imaginary = 2;
}

message NIComplexI16 {
  sint32 real = 1;
  sint32 imaginary = 2;
}

message SmtSpectrumInfo {
  uint32 spectrum_type = 1;
  uint32 linear_db = 2;
  uint32 window = 3;
  sint32 window_size = 4;
  sint32 fft_size = 5;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/protobuf/README.md sha256=bfe0827ebf1bb384009f56ad07e37d69750ea8094c4556c5c683afffde4031c7 bytes=136 -->
## FILE: imports/protobuf/README.md

- repository: `ni/grpc-device`
- source_path: `imports/protobuf/README.md`
- sha256: `bfe0827ebf1bb384009f56ad07e37d69750ea8094c4556c5c683afffde4031c7`
- bytes: 136

````markdown
# Updating

To update this protobuf folder. Find the hapigen_grpc_device_plugin export and copy the contents of its proto folder here.
````

<!--NI_OSS_SOURCE repo=grpc-device path=LICENSE sha256=16f05777125b5662a206c2ce068bdf3771f6dedb3ecb8b73a767ae6fe0a4f9ab bytes=1091 -->
## FILE: LICENSE

- repository: `ni/grpc-device`
- source_path: `LICENSE`
- sha256: `16f05777125b5662a206c2ce068bdf3771f6dedb3ecb8b73a767ae6fe0a4f9ab`
- bytes: 1091

````text
Copyright (c) 2022, National Instruments Corp.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
````

<!--NI_OSS_SOURCE repo=grpc-device path=pyproject.toml sha256=ecdf42d2e6037c3663a26019d3e473fe2b8c477f74042b0e49f6758e4fb251be bytes=194 -->
## FILE: pyproject.toml

- repository: `ni/grpc-device`
- source_path: `pyproject.toml`
- sha256: `ecdf42d2e6037c3663a26019d3e473fe2b8c477f74042b0e49f6758e4fb251be`
- bytes: 194

````toml
[tool.black]
line-length = 100
exclude = "source/codegen/metadata/"

[tool.mypy]
mypy_path = "$MYPY_CONFIG_FILE_DIR/source/codegen/:$MYPY_CONFIG_FILE_DIR/../grpc-device-example-template/"
````

<!--NI_OSS_SOURCE repo=grpc-device path=python_build_requirements.txt sha256=a1b0506ca9c35d8ce6fb46bdb30622de7678ad91a4b5a28c87b60f57cf65e4e1 bytes=171 -->
## FILE: python_build_requirements.txt

- repository: `ni/grpc-device`
- source_path: `python_build_requirements.txt`
- sha256: `a1b0506ca9c35d8ce6fb46bdb30622de7678ad91a4b5a28c87b60f57cf65e4e1`
- bytes: 171

````text
contextlib2==21.6.0
Mako==1.2.2
MarkupSafe==2.0.1
schema==0.7.4
black==23.3.0
mypy>=0.910
ni-python-styleguide~=0.1
pycodestyle==2.7.0
importlib-metadata==4.12.0
````

<!--NI_OSS_SOURCE repo=grpc-device path=README.md sha256=4bec73fe8d7c3146300f9de27fdacaa73e1790d70479aca3f28042fc1a4e3cff bytes=12560 -->
## FILE: README.md

- repository: `ni/grpc-device`
- source_path: `README.md`
- sha256: `4bec73fe8d7c3146300f9de27fdacaa73e1790d70479aca3f28042fc1a4e3cff`
- bytes: 12560

````markdown
# NI gRPC Device Server and Client APIs

This repo contains the source code needed to build and run the NI gRPC Device Server for supported NI hardware driver APIs. Also contained in this repo are instructions and examples that demonstrate how to create client code that interacts with devices connected to an instance of the NI gRPC Device Server.

The server and the client APIs allow NI's instrumentation to be accessed and controlled through a remote interface via pre-defined APIs using a client/server architecture. The API is not a driver but instead a layer on top of the existing driver C APIs that provides remote capabilities.

For more detailed information on the server and API design refer to the [wiki](https://github.com/ni/grpc-device/wiki).

## Supported NI drivers
Indicates the most recent driver version used to test builds of the current source. Supported driver versions for specific releases will be found in the release notes for that version.

|NI Driver|Version Tested (Windows)|Version Tested (Linux) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Version Tested (Linux RT)|
| :------------------------ | :------------ | :------------ | :------------ |
| FPGA Interface            | 2024 Q2       | 2024 Q2       | 2024 Q2       |
| NI-DAQmx                  | 2026 Q1       | 2026 Q1       | 2026 Q1       |
| NI-DCPower                | 2023 Q1       | 2023 Q1       | 2023 Q1       |
| NI-Digital Pattern Driver | 2023 Q1       | Not Supported | Not Supported |
| NI-DMM                    | 2025 Q4       | 2025 Q4       | 2025 Q4       |
| NI-FGEN                   | 2023 Q1       | 2023 Q1       | 2023 Q1       |
| NI-RFmx Bluetooth         | 2026 Q3       | Not Supported | Not Supported |
| NI-RFmx BluetoothGen      | 2026 Q3       | Not Supported | Not Supported |
| NI-RFmx CDMA2k            | 2025 Q1       | Not Supported | Not Supported |
| NI-RFmx Demod             | 2026 Q3       | Not Supported | Not Supported |
| NI-RFmx GSM               | 2025 Q1       | Not Supported | Not Supported |
| NI-RFmx LTE               | 2026 Q3       | Not Supported | Not Supported |
| NI-RFmx Pulse             | 2026 Q3       | Not Supported | Not Supported |
| NI-RFmx NR                | 2026 Q3       | Not Supported | Not Supported |
| NI-RFmx SpecAn            | 2025 Q4       | Not Supported | Not Supported |
| NI-RFmx TD-SCDMA          | 2025 Q1       | Not Supported | Not Supported |
| NI-RFmx VNA               | 2026 Q3       | Not Supported | Not Supported |
| NI-RFmx WCDMA             | 2025 Q1       | Not Supported | Not Supported |
| NI-RFmx WLAN              | 2026 Q3       | Not Supported | Not Supported |
| NI-RFmx WLANGen           | 2026 Q2       | Not Supported | Not Supported |
| NI-RFSA                   | 2026 Q2       | 2026 Q2       | 2026 Q2       |
| NI-RFSG                   | 2025 Q3       | 2025 Q3       | 2025 Q3       |
| NI-SCOPE                  | 2023 Q2       | 2023 Q2       | 2023 Q2       |
| NI-SWITCH                 | 2023 Q1       | 2023 Q1       | 2023 Q1       |
| NI-TClk                   | 2023 Q1       | 2023 Q1       | 2023 Q1       |
| NI-VISA                   | 2024 Q1       | 2024 Q1       | 2024 Q1       |
| NI-XNET                   | 21.5.0        | 21.5.0        | 21.5.0        |

## Build Status
![Linux Build](https://github.com/ni/grpc-device/workflows/Build%20Matrix/badge.svg)
![NI Linux Real-Time Build](https://github.com/ni/grpc-device/workflows/NI%20Linux%20Real-Time%20Build/badge.svg)

## Downloading a Release

### Download the Server
1. (Windows Only) Download and install the latest [Microsoft Visual C++ Redistributable for Visual Studio 2022](https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0).
2. Navigate to the [Releases](https://github.com/ni/grpc-device/releases) page.
3. Download the latest Server Release `.tar.gz` or `.zip` for the desired platform.
4. Extract the contents of the `.tar.gz` or `.zip` to a directory with read and write permissions.
5. [Run the server](#running-the-grpc-server)
* **List of supported OS:**
  - Windows 64-bit
  - Linux 64-bit
  - NI Linux RT

### Download the Client Files
1. Navigate to the [Releases](https://github.com/ni/grpc-device/releases) page.
2. Download the latest Client Release's `ni-grpc-device-client.tar.gz` or `ni-grpc-device-client.zip` depending on the client platform.
3. Extract the contents of `ni-grpc-device-client.tar.gz` or `ni-grpc-device-client.zip` to a directory with read and write permissions.
4. [Create a gRPC client](#creating-a-grpc-client).

## Building Locally

If you're looking to build the grpc-device repo locally, look at the [Getting Started section of CONTRIBUTING.md](https://github.com/ni/grpc-device/blob/main/CONTRIBUTING.md#getting-started).

## Running the gRPC Server

The server's startup configuration is set by specifying port and security settings in a JSON configuration file. A default configuration file named `server_config.json` with an insecure configuration (no SSL/TLS) bound to localhost is located in the same directory as the server executable. For more information on SSL/TLS related security settings refer to the [SSL/TLS Support section](#ssltls-support). For more information on address binding refer to the [Bind Address Support section](#bind-address-support). The location of the server binary is not important as long as the user has proper permissions in the chosen directory.

There are two ways to start the server:

1. Launch the server application without specifying a path to a configuration file (use the default configuration file):

    **Windows**

    `.\ni_grpc_device_server.exe`

   **Note:** It is also possible to start the server by double-clicking the executable. Starting the server through a command prompt, however, allows for observation of [startup errors](#common-server-startup-errors).

    **Linux and Linux RT**

    `./ni_grpc_device_server`

2. Launch the server application by specifying a path (relative or absolute) to the configuration file:

    **Windows**

    `.\ni_grpc_device_server.exe C:\path\to\config\file\server_config.json`

    **Linux and Linux RT**

    `./ni_grpc_device_server /path/to/config/file/server_config.json`


If the server starts successfully on the port specified in the configuration file, then it will print a message to the terminal output:

```
Server listening on port 12345. Security is configured with insecure credentials.
```

**Note:** If port `0` is specified then the server will automatically select a port from the dynamic range. The port used will be reflected in the startup message.

If the server fails to start (i.e. a port is not specified in the configuration file) then an error message is printed in the terminal and the application will exit.

### Common Server Startup Errors

1. The datatypes of the values in the configuration file don't match the expected datatypes. For example, the port must be an integer type and not a string. The error message will provide specific details on the type requirements.
1. The configuration file can't be found at the provided location. This error can also occur if the user lacks read permissions for the file.
1. The server configuration file is malformed and is not in proper JSON format. Refer to the JSON configuration file in this readme for an example of the expected format.
1. The specified address is not valid. The solution is to select a valid IPv4 or IPv6 address.
1. The specified port is out of the allowed port range. The solution is to select a port in the allowable range (0-65535).
1. The specified port is already in use. The solution is to select another port or terminate the other application using the port.
1. Security configuration errors. See [Server Security Support wiki page](https://github.com/ni/grpc-device/wiki/Server-Security-Support).

### Default Configuration File (localhost):

Below are the contents of a default configuration file accepting localhost connections on port `31763` and configured without SSL/TLS.  A configuration file with these contents also exists in the same directory as the `ni_grpc_device_server` binary.

```json
{
    "address": "[::1]",
    "port": 31763,
    "security" : {
       "server_cert": "",
       "server_key": "",
       "root_cert": ""
    }
 }
```

### Bind Address Support

The server supports specifying the address to bind to in the JSON configuration file via the `"address"` field. The address can be used to enable local or remote connections. Address values include any valid IPv4 or IPv6 address.

| Address | Effect |
|---------|--------|
| `"[::1]"` or `"127.0.0.1"` | Bind to loopback only (local connections) |
| `"[::]"` or `"0.0.0.0"` | Bind to all interfaces (remote connections) |

**Default behavior by version:**

- **Versions < 2.18:** If no `"address"` field is specified, the server defaults to binding on all interfaces (`"[::]"`), allowing remote connections.
- **Versions >= 2.18:** If no `"address"` field is specified, the server defaults to binding on localhost only (`"[::1]"`). To allow remote connections, explicitly set `"address": "[::]"` in the configuration file.

Starting with version 2.18, the server logs a warning at startup if the bound address is a loopback address without TLS enabled, and also warns if binding to all interfaces without TLS. This helps ensure that remote-accessible deployments are configured securely.

Example configuration for remote access:
```json
{
   "port": 31763,
   "address": "[::]",
   "security": "..."
}
```

### Licensing behaviour

If you are using gRPC to control a licensed software, e.g. RFmx, the license checkout will happen on the machine running the gRPC server, not in the client side. As the license check-in happens, when the process which requested the license terminates, you need to close the gRPC server application to return the license. 

## Creating a gRPC Client

Each supported driver API has a corresponding `.proto` file that defines the interface used by clients to interact with the NI devices connected to the server. Creating a client requires compiling the `.proto` into supporting files in the client's language of choice using the protocol buffer compiler `protoc`. For more detailed information refer to the [Creating a gRPC Client wiki page](https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client).

## SSL/TLS Support

The server supports both server-side TLS and mutual TLS. Security configuration is accomplished by setting the `server_cert`, `server_key` and `root_cert` values in the server's configuration file. The server expects the certificate files specified in the configuration file to exist in a `certs` folder that is located in the same directory as the configuration file being used by the server. For more detailed information on SSL/TLS support refer to the [Server Security Support wiki page](https://github.com/ni/grpc-device/wiki/Server-Security-Support).

### NI TLS Config Integration

Alternatively, when the `ni-tls-config` package is installed, the server can delegate TLS configuration by setting the top-level `"security"` field to `"ni-tls-config"` in `server_config.json`. The following snippet shows only the `ni-tls-config`-specific fields; keep other required fields (for example, `port`) in your configuration.

```json
{
   "security": "ni-tls-config",
   "feature_toggles": {
      "ni-tls-config": true
   }
}
```

When `ni-tls-config` is enabled, certificate and trust settings are read from the `ni-tls-config` YAML file instead of `server_config.json` certificate fields.

With this setting the server reads TLS configuration at startup from the per-service YAML file managed by `ni-tls-config` (`ni-grpc-device.conf.yml`). A template for this file is distributed alongside the server binary. Place it in the location expected by `ni-tls-config`:

- **Windows**: `C:\ProgramData\National Instruments\nitlsconfig\server.d\ni-grpc-device.conf.yml`
- **Linux**: `/etc/nitlsconfig/server.d/ni-grpc-device.conf.yml`

If `"security": "ni-tls-config"` is configured but the `ni-tls-config` library is not installed, the server logs an error and exits instead of starting insecurely.

Once `ni-tls-config` is enabled, use NI Hardware Configuration Utility on each client machine to configure the desired security settings.
````

<!--NI_OSS_SOURCE repo=grpc-device path=SECURITY.md sha256=c788c4751defbc1485124709557b5d5a6b9ccd07304bc7b9ae4619a4317c1fc6 bytes=1329 -->
## FILE: SECURITY.md

- repository: `ni/grpc-device`
- source_path: `SECURITY.md`
- sha256: `c788c4751defbc1485124709557b5d5a6b9ccd07304bc7b9ae4619a4317c1fc6`
- bytes: 1329

````markdown
<!-- Begin NI SECURITY.md V1.0 -->

# Security

NI views the security of our software products as an important part of our commitment to our users.  This includes source code repositories managed through the [NI](https://github.com/ni) GitHub organization.

## Reporting Security Issues

We encourage you to report security vulnerabilities to us privately so we can follow the principle of [Coordinated Vulnerability Disclosure (CVD)](https://vuls.cert.org/confluence/display/CVD).  This allows us time to thoroughly investigate security issues and publicly disclose them when appropriate.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them by sending an email to [security@ni.com](mailto:security@ni.com) with sufficient details about the type of issue, the impact of the issue, and how to reproduce the issue.  You may use the [NI PGP key](https://www.ni.com/en/support/security/pgp.html) to encrypt any sensitive communications you send to us. When you notify us of a potential security issue, our remediation process includes acknowledging receipt and coordinating any necessary response activities with you.

## Learn More

To learn more about NI Security, please see [https://ni.com/security](https://ni.com/security)

<!-- End NI SECURITY.md -->
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/__init__.py sha256=1d5cec7fc61ac15aed058ade8874faa1081517b160fdb22d46ebc3f80d0dbbe0 bytes=24 -->
## FILE: source/codegen/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/__init__.py`
- sha256: `1d5cec7fc61ac15aed058ade8874faa1081517b160fdb22d46ebc3f80d0dbbe0`
- bytes: 24

````python
"""Codegen package."""
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/client_helpers.py sha256=fd654aa2cd2009afc2fa8a06b09e3f1e713128297d8298de57f0593a1b107237 bytes=7212 -->
## FILE: source/codegen/client_helpers.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/client_helpers.py`
- sha256: `fd654aa2cd2009afc2fa8a06b09e3f1e713128297d8298de57f0593a1b107237`
- bytes: 7212

````python
"""Helpers for creating client .h/.cpp files."""

import re
from collections import namedtuple
from enum import Enum
from typing import List, Tuple

import common_helpers


class ParamMechanism(Enum):
    """Enumeration of parameter mechanisms supported by client codegen."""

    BASIC = 0
    ARRAY = 1
    ENUM = 2
    MAPPED_ENUM = 3
    COPY = 4
    BITFIELD_AS_ENUM_ARRAY = 5


ClientParam = namedtuple("ClientParam", ["name", "cppName", "type", "mechanism", "default"])


PROTOBUF_PRIM_TYPES = ["bool", "double", "float"]
PROTOBUF_TYPE_TO_CPP_TYPE = {
    "double": "double",
    "float": "float",
    "int32": "int32",
    "int64": "int64",
    "uint32": "uint32",
    "uint64": "uint64",
    "sint32": "int32",
    "sint64": "int64",
    "fixed32": "uint32",
    "fixed64": "uint64",
    "sfixed32": "int32",
    "sfixed64": "int64",
    "bool": "bool",
    "string": "string",
    "bytes": "string",
}
NIDEVICE_ENUMS = ["nidevice_grpc.SessionInitializationBehavior"]


def _to_parameter_for_list(client_param: ClientParam, for_header: bool) -> str:
    if not for_header or client_param.default is None:
        return f"{client_param.type} {client_param.cppName}"
    else:
        return f"{client_param.type} {client_param.cppName} = {client_param.default}"


def _to_parameter_list(client_params: List[ClientParam], for_header: bool) -> List[str]:
    param_list = [_to_parameter_for_list(p, for_header) for p in client_params]

    return param_list


def stub_param() -> str:
    """Get the C++ stub parameter."""
    return f"const {stub_ptr_alias()}& stub"


def create_streaming_params(client_params: List[ClientParam], for_header: bool) -> str:
    """Build the C++ parameter list for streaming functions."""
    params = _to_parameter_list(client_params, for_header)
    client_context_param = "::grpc::ClientContext& context"
    params = [stub_param()] + [client_context_param] + params
    return str.join(", ", params)


def create_unary_params(client_params: List[ClientParam], for_header: bool) -> str:
    """Build the C++ parameter list for normal functions."""
    params = _to_parameter_list(client_params, for_header)
    params = [stub_param()] + params
    return str.join(", ", params)


def _is_basic_type(grpc_type: str) -> bool:
    return (
        grpc_type in PROTOBUF_PRIM_TYPES
        or grpc_type in PROTOBUF_TYPE_TO_CPP_TYPE
        or grpc_type.endswith("Attributes")
        or grpc_type.endswith("Attribute")
        or grpc_type in NIDEVICE_ENUMS
    )


def protobuf_namespace_alias() -> str:
    """Get the protobuf namespace alias."""
    return "pb"


def _get_cpp_client_param_type(param: dict, enums: dict) -> str:
    grpc_type = param["grpc_type"]

    if _is_grpc_array(param):
        underlying_type = common_helpers.strip_prefix(grpc_type, "repeated ")
        underlying_type = _get_cpp_type_for_protobuf_type(underlying_type)
        return f"std::vector<{underlying_type}>"

    if "enum" in param:
        base_type = _get_cpp_type_for_protobuf_type(grpc_type)
        if base_type:
            return f"simple_variant<{param['enum']}, {base_type}>"
        return param["enum"]

    if "mapped-enum" in param:
        enum = param["mapped-enum"]
        base_type = common_helpers.get_enum_value_cpp_type(enums[enum])
        return f"simple_variant<{enum}, {base_type}>"

    if common_helpers.is_bitfield_as_enum_array(param):
        enum = common_helpers.get_bitfield_enum_type(param)
        base_type = common_helpers.get_enum_value_cpp_type(enums[enum])
        return f"simple_variant<std::vector<{enum}>, {base_type}>"

    return _get_cpp_type_for_protobuf_type(grpc_type)


def _get_cpp_type_for_protobuf_type(protobuf_type: str) -> str:
    if protobuf_type in PROTOBUF_PRIM_TYPES:
        return protobuf_type

    if protobuf_type in PROTOBUF_TYPE_TO_CPP_TYPE:
        cpp_type = PROTOBUF_TYPE_TO_CPP_TYPE[protobuf_type]
        if cpp_type in ["string"]:
            return f"std::{cpp_type}"
        return f"{protobuf_namespace_alias()}::{cpp_type}"

    return protobuf_type.replace(".", "::")


def _const_ref_t(t: str) -> str:
    return f"const {t}&"


def _get_param_mechanism(param: dict) -> ParamMechanism:
    if _is_grpc_array(param):
        return ParamMechanism.ARRAY
    if common_helpers.is_bitfield_as_enum_array(param):
        return ParamMechanism.BITFIELD_AS_ENUM_ARRAY
    if "enum" in param:
        return ParamMechanism.ENUM
    if "mapped-enum" in param:
        return ParamMechanism.MAPPED_ENUM
    if _is_basic_type(param["grpc_type"]):
        return ParamMechanism.BASIC
    return ParamMechanism.COPY


def _get_param_default(param: dict) -> str:
    if param["grpc_type"] == "nidevice_grpc.SessionInitializationBehavior":
        return "nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED"
    return None


def _create_client_param(param: dict, enums: dict) -> ClientParam:
    name = common_helpers.get_grpc_field_name(param)
    cppname = common_helpers.get_grpc_client_field_name(param)
    param_type = _get_cpp_client_param_type(param, enums)
    param_type = _const_ref_t(param_type)
    param_mechanism = _get_param_mechanism(param)
    param_default = _get_param_default(param)

    return ClientParam(name, cppname, param_type, param_mechanism, param_default)


def _is_grpc_array(param: dict) -> bool:
    return param["grpc_type"].startswith("repeated ")


def stub_ptr_alias():
    """Get the stub pointer alias."""
    return "StubPtr"


def get_client_parameters(func: dict, enums: dict) -> List[ClientParam]:
    """Create a list of ClientParam objects for the given function."""
    inputs = [p for p in func["parameters"] if common_helpers.is_input_parameter(p)]

    inputs = common_helpers.filter_parameters_for_grpc_fields(inputs)

    return [_create_client_param(p, enums) for p in inputs]


def _split_types_from_variant(variant_type: str) -> Tuple[str, str]:
    match = re.match(r".*simple_variant<([^,]+), ([^>]+)>", variant_type)
    assert match
    return (match[1], match[2])


def get_enum_value_type(param: ClientParam) -> str:
    """Get the enum name of the given enum ClientParam."""
    enum, _ = _split_types_from_variant(param.type)
    return enum


def get_enum_raw_type(param: ClientParam) -> str:
    """Get the raw C++ value_type of the given enum ClientParam."""
    _, raw = _split_types_from_variant(param.type)
    return raw


def streaming_response_type(response_type: str) -> str:
    """Wrap the given response type with a reader for streaming functions."""
    return f"std::unique_ptr<grpc::ClientReader<{response_type}>>"


def filter_functions_to_include_in_client(functions: dict) -> dict:
    """Include only those functions which dont have 'include_in_client' tag in metadata."""
    filtered_functions = {}
    for func_name in functions.keys():
        if functions[func_name].get("include_in_client", True) is True:
            filtered_functions[func_name] = functions[func_name]
    return filtered_functions
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/common_helpers.py sha256=d0aed5f977accabae55c9b4ed052043fc2d41c6cdc63950e0cffb615c6eab07f bytes=51089 -->
## FILE: source/codegen/common_helpers.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/common_helpers.py`
- sha256: `d0aed5f977accabae55c9b4ed052043fc2d41c6cdc63950e0cffb615c6eab07f`
- bytes: 51089

````python
"""Common helpers."""

import os
import re
from collections import defaultdict, namedtuple
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

_NIDEVICE_COMMON_MESSAGE_TYPES = (
    "nidevice_grpc.NIComplexNumber",
    "nidevice_grpc.NIComplexNumberF32",
    "nidevice_grpc.NIComplexI16",
    "nidevice_grpc.SmtSpectrumInfo",
)

_WELL_KNOWN_MESSAGE_TYPES = ("google.protobuf.Timestamp",)

PascalTokenSubstitution = namedtuple(
    "PascalTokenSubstitution", ["pascal_representation", "preferred_representation"]
)
SPECIAL_CASE_PASCAL_TOKENS = [
    # NI uses UInt, not Uint, and never U_INT when converting to snake.
    PascalTokenSubstitution("Uint", "UInt")
]


def is_output_parameter(parameter):
    """Whether the parameter is an output parameter."""
    return "out" in parameter["direction"]


def is_input_parameter(parameter):
    """Whether the parameter is an input parameter."""
    return "in" in parameter["direction"]


def get_first_streaming_parameter(parameters: List[Dict]) -> Optional[Dict]:
    """Get the streaming parameter from the list of parameters."""
    for param in parameters:
        if param.get("is_streaming_type", False):
            return param
    return None


def levels_of_pointer_indirection(parameter: dict) -> int:
    """Levels of pointer indirection for pointer. I.e. number of '*'s."""
    return [is_output_parameter(parameter), parameter.get("pointer", False)].count(True)


def is_repeated_varargs_parameter(parameter: dict):
    """Whether the parameter is a repeated varargs parameter.

    This means the parameter follows a specific varargs convention where the user can pass in an
    arbitrary repetition of fixed arguments.
    """
    return parameter.get("repeated_var_args", False)


def is_proto_only_parameter(parameter: dict):
    """Whether the parameter is only included in the proto file and not the driver API."""
    return parameter.get("proto_only", False)


def is_repeating_parameter(parameter: dict):
    """Whether the parameter is a repeating parameter.

    This means the parameter can be repeated as many times as desired. See also
    is_repeated_varargs_parameter().
    """
    return parameter.get("repeating_argument", False)


def is_array(data_type: str):
    """Whether the parameter is an array parameter."""
    return data_type.endswith("[]") or data_type.endswith("*")


def get_bitfield_enum_type(parameter: dict) -> str:
    """Get the enum type for a bitfield represented as an enum array."""
    return parameter["bitfield_as_enum_array"]


def is_bitfield_as_enum_array(parameter: dict) -> bool:
    """Whether the parameter is a bitfield represented as an enum array."""
    return "bitfield_as_enum_array" in parameter


def is_enum(parameter: dict):
    """Whether the parameter's type is an enum."""
    return "enum" in parameter or "mapped-enum" in parameter or is_bitfield_as_enum_array(parameter)


def _is_custom_struct(parameter: dict) -> bool:
    return parameter["type"].startswith("struct")


def uses_nidevice_common_message_types(config: dict, functions: dict) -> bool:
    """Whether a custom_type or function has any parameters whose type is a common nidevice type."""
    any_funcs = any(
        p
        for f in functions.values()
        for p in f["parameters"]
        if _is_nidevice_common_message_type(p)
    )
    any_custom_types = any(
        field
        for ct in config.get("custom_types", {})
        for field in ct["fields"]
        if _is_nidevice_common_message_type(field)
    )
    return any_funcs or any_custom_types


def _is_nidevice_common_message_type(parameter: dict) -> bool:
    if "grpc_type" not in parameter:
        return False
    grpc_type = _get_underlying_grpc_type(parameter)
    return grpc_type in _NIDEVICE_COMMON_MESSAGE_TYPES


def _is_supported_well_known_type(parameter: dict) -> bool:
    grpc_type = _get_underlying_grpc_type(parameter)
    return grpc_type in _WELL_KNOWN_MESSAGE_TYPES


def is_struct(parameter: dict) -> bool:
    """Whether the parameter's type is a struct."""
    return (
        _is_nidevice_common_message_type(parameter)
        or _is_supported_well_known_type(parameter)
        or _is_custom_struct(parameter)
    )


def is_driver_typedef_with_same_size_but_different_qualifiers(type: str) -> bool:
    """Whether the type has different per-platform qualifiers.

    Some of the drivers use different qualifiers for integers of same size on windows vs linux. We
    need to reinterpret_cast in the generated code to get the correct value.
    """
    return type in (
        "ViAddr",
        "ViInt32",
        "ViUInt32",
        "ViUInt16",
        "uInt32",
        "int32",
        "uInt64",
        "int64",
        "nxTimestamp1ns_t",
        "nxTimestamp100ns_t",
        "ViAttr",
    )


def _has_copy_convert_tag(parameter):
    return parameter.get("supports_standard_copy_convert", False)


def supports_standard_copy_conversion_routines(parameter: dict) -> bool:
    """Whether the parameter can be converted with convert_from_grpc and convert_to_grpc."""
    return (
        _has_copy_convert_tag(parameter)
        or is_struct(parameter)
        or parameter.get("grpc_type", "") == "repeated bool"
    )


def supports_standard_output_allocation_routines(parameter: dict) -> bool:
    """Whether the parameter can be allocated as an output param with allocate_output_storage."""
    return parameter.get("supports_standard_output_allocation", False)


def _any_function_uses_grpc_type(functions, type_name):
    return any(p["grpc_type"] == type_name for f in functions for p in functions[f]["parameters"])


def list_external_proto_dependencies(functions: dict) -> List[str]:
    """Return a list of external proto files required by the functions dictionary."""
    mappings = {
        "google.protobuf.Timestamp": "google/protobuf/timestamp.proto",
        "google.protobuf.Duration": "google/protobuf/duration.proto",
    }
    return [
        proto_name
        for type_name, proto_name in mappings.items()
        if _any_function_uses_grpc_type(functions, type_name)
    ]


def get_custom_types(config: dict) -> List[Dict[str, Any]]:
    """Get the custom_types config setting."""
    return config.get("custom_types", [])


def get_input_and_output_custom_types(config, functions):
    """Return a set of custom types used by input and output parameters separately."""
    input_custom_types = set()
    output_custom_types = set()
    for function in functions:
        struct_params = [p for p in functions[function]["parameters"] if _is_custom_struct(p)]
        for parameter in struct_params:
            underlying_type_name = get_underlying_type_name(parameter["type"])
            nested_types = _get_nested_types(config, underlying_type_name)
            if is_input_parameter(parameter):
                input_custom_types.add(underlying_type_name)
                input_custom_types = input_custom_types.union(nested_types)
            elif is_output_parameter(parameter):
                output_custom_types.add(underlying_type_name)
                output_custom_types = output_custom_types.union(nested_types)
    return (input_custom_types, output_custom_types)


def _get_nested_types(config, type_name):
    custom_types = set()
    matching_custom_types = [
        custom_type
        for custom_type in config.get("custom_types", [])
        if custom_type["name"] == type_name
    ]
    if not matching_custom_types:
        return custom_types
    for field in matching_custom_types[0]["fields"]:
        if field["type"].startswith("struct "):
            nested_type_name = get_underlying_type_name(field["type"])
            custom_types.add(nested_type_name)
            custom_types = custom_types.union(_get_nested_types(config, nested_type_name))
    return custom_types


def _is_null_terminated_in_c(parameter):
    return parameter["grpc_type"] == "string"


def is_string_arg(parameter):
    """Whether the parameter's type is string or bytes."""
    return parameter["grpc_type"] in ["string", "bytes"]


def is_nidevice_enum_parameter(grpc_type):
    """Whether the grpc_type is one of the enums in nidevice_grpc."""
    return grpc_type in ["nidevice_grpc.SessionInitializationBehavior"]


def strip_repeated_from_grpc_type(grpc_type):
    """Strip "repeated" from the grpc_type."""
    if not grpc_type.startswith("repeated "):
        raise Exception("varargs grpc_type " + grpc_type + " must be repeated")
    return grpc_type[len("repeated ") :]


def get_underlying_type_name(parameter_type: str) -> str:
    """Get the underlying type name of the given type.

    Strip away information from type name like brackets for arrays, leading "struct ", etc. leaving
    just the underlying type name.
    """
    return parameter_type.replace("struct ", "").replace("[]", "")


def _get_underlying_grpc_type_name(grpc_type: str) -> str:
    return strip_prefix(grpc_type, "repeated ")


def get_underlying_type(parameter_or_attribute: dict) -> str:
    """Get the underlying type name of the given parameter or attribute."""
    return get_underlying_type_name(parameter_or_attribute["type"])


def _get_underlying_grpc_type(parameter: dict) -> str:
    return _get_underlying_grpc_type_name(parameter.get("grpc_type", ""))


def has_unsupported_parameter(function):
    """Whether the given function has a parameter that's not supported.

    Examples of unsupported parameters:
        * Parameters with an unsupported size mechanism
        * Output array parameters whose type is an enum whose underlying type is not a string or
          32-bit int
    """
    return any(_is_unsupported_parameter(p) for p in function["parameters"])


def _is_unsupported_parameter(parameter):
    return is_unsupported_size_mechanism(parameter) or _is_unsupported_scalar_array(parameter)


def is_unsupported_size_mechanism(parameter: dict) -> bool:
    """Whether the parameter has a size that uses an unsupported mechanism."""
    size_mechanism = get_size_mechanism(parameter)
    if size_mechanism is None:
        return False
    return is_unsupported_size_mechanism_type(size_mechanism)


# These are the mechanisms that are used to specify the size of arrays/strings. Here's what they
# mean:
# - fixed:
#     the array is of a constant size. The size is specified in the 'value' member.
# - len:
#     the array's length needs to be passed into the function. The parameter to pass it in is
#     specified in the 'value' member. Should only be used for input arrays. Multiple input arrays
#     can use this mechanism with the same 'value' member - in that case, the service will enforce
#     that those arrays are all the same length.
# - ivi-dance:
#     This is a two-step process. On the first call, pass in NULL, and the function will return how
#     big the array should be (instead of an error as usual). Then, the service creates an array of
#     that size and passes it in. Should only be used for output arrays. The size of the array
#     (which is still passed in) is specified in the 'value' member. Note that it is possible that
#     the second call will return a "buffer too small" error (if the underlying value in the driver
#     has changed size between calls), in which case the "dance" will start again by passing NULL.
# - ivi-dance-with-a-twist:
#     This is similar to ivi-dance, but the size is returned in an output parameter that is
#     specified in the 'value_twist' member. Should only be used for output arrays. The size of the
#     array is specified in the 'value' member. This mechanism is necessary if there are multiple
#     output arrays (so ivi-dance won't work). Similar to ivi-dance, this will loop around if a
#     "buffer too small" error is returned on the second call.
# - passed-in:
#     The array's size is passed in in a separate parameter, which is specified in the 'value'
#     member. Should only be used for output arrays (otherwise you can just use 'len').
# - passed-in-by-ptr:
#     The array's size is passed in in a separate parameter, which is specified in the 'value'
#     member. It is passed in by pointer, and on return the underlying call will set the actual
#     number of elements filled in to the array as long as that is smaller than the passed-in value.
#     (If it is larger, the underlying call will return an error.)
#     Should only be used for output arrays.
# - two-dimension:
#     The array being operated on is two dimensional in nature and the size specified in the 'value'
#     member is an array that specifies the size of each array in the two dimensional array. The
#     user will still need to pass in the array of sizes and some validation is done to ensure the
#     sum of the size array matches the size of the two dimensional array.
# - custom-code:
#     The array's size is determined by the C++ code in the 'value' member.


def is_unsupported_size_mechanism_type(size_mechanism: str) -> bool:
    """Whether the given size mechanism is unknown/unsupported."""
    return size_mechanism not in {
        "fixed",
        "len",
        "len-in-bytes",
        "ivi-dance",
        "passed-in",
        "passed-in-by-ptr",
        "ivi-dance-with-a-twist",
        "two-dimension",
        "custom-code",
    }


def _is_unsupported_scalar_array(parameter):
    return is_array(parameter["type"]) and _is_unsupported_enum_array(parameter)


def _is_unsupported_enum_array(parameter):
    if is_enum(parameter):
        if is_input_parameter(parameter):
            return False

        return not _is_supported_enum_array_output_type(parameter)
    return False


def _is_supported_enum_array_output_type(parameter):
    return is_string_arg(parameter) or is_static_castable_enum_type(parameter)


def is_static_castable_enum_type(parameter):
    """Whether the underlying type of the parameter's enum is static_castable."""
    grpc_type = _get_underlying_grpc_type(parameter)
    # Note: sint32 could work here but causes issue with existing attribute output accessors
    # because it's not wire-compatible with enum. If it's added here, we need to make sure that
    # we're handling compatibility issues on those methods.
    return grpc_type in ["int32", "uint32"]


def _normalize_special_pascal_tokens(pascal_or_camel_string: str) -> str:
    for pascal_token, special_case_override in SPECIAL_CASE_PASCAL_TOKENS:
        pascal_or_camel_string = pascal_or_camel_string.replace(special_case_override, pascal_token)
    return pascal_or_camel_string


def _insert_special_case_pascal_tokens(normal_pascal_string: str) -> str:
    for pascal_token, special_case_override in SPECIAL_CASE_PASCAL_TOKENS:
        normal_pascal_string = normal_pascal_string.replace(pascal_token, special_case_override)
    return normal_pascal_string


def _insert_leading_special_case_pascal_tokens(camel_string: str) -> str:
    for pascal_token, special_case_override in SPECIAL_CASE_PASCAL_TOKENS:
        camel_string = _replace_prefix(camel_string, pascal_token.lower(), special_case_override)
    return camel_string


def _normalize_leading_special_case_pascal_tokens(pascal_string: str) -> str:
    for pascal_token, special_case_override in SPECIAL_CASE_PASCAL_TOKENS:
        pascal_string = _replace_prefix(pascal_string, special_case_override, pascal_token)
    return pascal_string


def _is_actually_pascal(camel_or_pascal_string: str) -> bool:
    return "A" <= camel_or_pascal_string[0] <= "Z"


def camel_to_snake(camel_string: str) -> str:
    """Return a snake_string for a given camelString.

    External callers should use/create a wrapper instead (i.e. get_grpc_field_name).
    """
    if _is_actually_pascal(camel_string):
        camel_string = _pascal_to_camel(camel_string)

    camel_string = _normalize_special_pascal_tokens(camel_string)
    # Add _ before Words:
    # someDeviceIPAddress -> some_DeviceIP_Address
    s1 = re.sub(r"([^_])([A-Z][a-z]+[0-9]*)", r"\1_\2", camel_string)
    # Add _ before any capital letters not already preceded by _ and convert to lower:
    # some_DeviceIP_Address -> some_Device_IP_Address
    # some_Device_IP_Address -> some_device_ip_address
    return re.sub(r"([^_])([A-Z]+[0-9]*)", r"\1_\2", s1).lower()


def snake_to_pascal(snake_string):
    """Return a PascalString for a given snake_string."""
    snake_string = list(snake_string)
    index = 0
    snake_string[index] = snake_string[index].upper()
    for x in snake_string:
        if x == "_":
            snake_string[index + 1] = snake_string[index + 1].upper()
            del snake_string[index]
        index = index + 1
    result = "".join(snake_string)
    return _insert_special_case_pascal_tokens(result)


def _pascal_to_camel(pascal_string):
    """Return a camelString for a given PascalString."""
    pascal_string = _normalize_leading_special_case_pascal_tokens(pascal_string)
    if not _is_actually_pascal(pascal_string):
        return pascal_string

    # Full string all-caps: IEPE -> iepe. HTTP2 -> http2.
    match = re.fullmatch(r"([A-Z]+[0-9]*)", pascal_string)
    if match:
        return match[1].lower()

    # Leading all-caps: IPAddress -> ipAddress. HTTP2Stream -> http2Stream.
    match = re.fullmatch(r"([A-Z]+[0-9]*)([A-Z].*)", pascal_string)
    if match:
        return match[1].lower() + match[2]

    # Normal case: NormalCase -> normalCase
    match = re.fullmatch(r"([A-Z])(.*)", pascal_string)
    return match[1].lower() + match[2]


def ensure_pascal_case(pascal_or_camel_string):
    """Ensure that a camel/pascal case string is pascal case.

    NOTE: does not distinguish leading all-caps acronyms.
    """
    pascal_or_camel_string = _insert_leading_special_case_pascal_tokens(pascal_or_camel_string)

    match = re.fullmatch(r"^([a-z])(.*)$", pascal_or_camel_string)
    if match:
        return match[1].upper() + match[2]

    return pascal_or_camel_string


def pascal_to_snake(pascal_string):
    """Return a snake_string for a given PascalString."""
    camel_string = _pascal_to_camel(pascal_string)
    snake_string = camel_to_snake(camel_string)
    return "".join(snake_string)


def filter_proto_rpc_functions(functions):
    """Return function metadata only for functions to include for generating proto rpc methods."""
    functions_for_proto = {
        "public",
        "CustomCode",
        "CustomCodeCustomProtoMessage",
        "CustomCodeNoLibrary",
    }
    return [
        name
        for name, function in functions.items()
        if function.get("codegen_method", "public") in functions_for_proto
    ]


def filter_proto_rpc_functions_for_message(functions):
    """Return function metadata only for functions to include for generating proto rpc messages."""
    functions_for_proto = {"public", "CustomCode", "CustomCodeNoLibrary"}
    return [
        name
        for name, function in functions.items()
        if function.get("codegen_method", "public") in functions_for_proto
    ]


def get_attribute_enums_by_type(attributes):
    """Return a dict of attribute data types that use enum, along with set of enums used."""
    attribute_enums_by_type = defaultdict(set)
    # For Compatibility: Pre-adding the following types to the map causes them to use value_raw
    # params even if they have no enum values. This is part of the shipping API for MI drivers.
    for enum_type in ["ViInt32", "ViInt64", "ViReal64", "ViString"]:
        attribute_enums_by_type[enum_type] = set()

    for attribute_name in attributes:
        attribute = attributes[attribute_name]
        if "enum" in attribute:
            attribute_type = get_underlying_type(attribute)
            enum_name = attribute["enum"]
            if "bitfield_enum" in attribute:
                enum_name = attribute["bitfield_enum"]
                if enum_name.startswith("_"):  # nidaqmx-python uses a leading underscore
                    enum_name = enum_name[1:]
            attribute_enums_by_type[attribute_type].add(enum_name)
    return attribute_enums_by_type


def get_function_enums(functions, enums: List[dict]):
    """Get a list of the enums used by functions."""
    function_enums = set()
    for function in functions:
        for parameter in functions[function]["parameters"]:
            if "enum" in parameter:
                function_enums.add(parameter["enum"])
            if "mapped-enum" in parameter:
                function_enums.add(parameter["mapped-enum"])
            if "bitfield_as_enum_array" in parameter:
                function_enums.add(parameter["bitfield_as_enum_array"])
    function_enums.update(_get_force_include_enums(enums))
    return sorted(function_enums)


def _get_force_include_enums(enums: List[dict]):
    force_include_enums = set()
    for enum in enums:
        if enums[enum].get("force-include", False):
            force_include_enums.add(enum)
    return force_include_enums


def has_viboolean_array_param(functions):
    """Whether at least one function has parameter of type ViBoolean[]."""
    for function in functions:
        for parameter in functions[function]["parameters"]:
            if parameter["type"] == "ViBoolean[]":
                return True
    return False


def has_enum_array_string_out_param(functions):
    """Whether at least one function has an output parameter that is a string-based enum."""
    for function in functions:
        for parameter in functions[function]["parameters"]:
            if is_output_parameter(parameter) and is_string_arg(parameter) and is_enum(parameter):
                return True
    return False


def get_size_mechanism(parameter: dict) -> Optional[str]:
    """Get the size mechanism of the given parameter."""
    size = parameter.get("size", {})
    return size.get("mechanism", None)


def get_size_param(parameter: dict) -> Optional[str]:
    """Get the size of the given parameter."""
    size = parameter.get("size", {})
    return size.get("value", None)


def _get_ivi_dance_twist_param_name(parameter: dict) -> Optional[str]:
    return parameter.get("size", {}).get("value_twist")


def has_size_mechanism_tag(parameter: dict, tag: str) -> bool:
    """Whether the given parameter specifies a size mechanism."""
    size_request = parameter.get("size", {})
    tags = size_request.get("tags", {})
    return tag in tags


def _has_strlen_bug(parameter: dict) -> bool:
    """Return whether the parameter is a string output whose size mechanism has the 'strlen bug'.

    Reports strlen instead of strlen + 1 for the required buffersize.

    We assume that this bug may some day be fixed, so the implementation needs to allocate the extra
    character but also trim it off if it's an extra null.
    """
    return has_size_mechanism_tag(parameter, "strlen-bug")


def has_optional_size_tag(parameter: dict) -> bool:
    """Whether the given parameter has a size mechanism tag "optional"."""
    return has_size_mechanism_tag(parameter, "optional")


def get_buffer_size_expression(parameter: dict) -> str:
    """Return the C++ size expression for the underlying C API buffer for a string/array parameter.

    Unlike get_size_expression, this will include the trailing null terminator for strings (which is
    in the size reported by driver APIs).
    """
    size_mechanism = get_size_mechanism(parameter)
    if "size" not in parameter:
        raise Exception("No size for parameter " + parameter["name"])
    if size_mechanism == "fixed":
        return parameter["size"]["value"]
    elif size_mechanism == "ivi-dance-with-a-twist":
        # Double the size to accommodate interleaved I and Q input values which will be
        # implicitly converted into NIComplexNumber while passing it to the C Driver API
        return get_grpc_field_name_from_str(parameter["size"]["value_twist"]) + (
            " * 2" if "value_converted_to_c_representation" in parameter else ""
        )
    elif size_mechanism == "passed-in-by-ptr":
        return get_grpc_field_name_from_str(parameter["size"]["value"]) + "_copy"
    else:
        return get_grpc_field_name_from_str(parameter["size"]["value"])


def get_size_expression(parameter: dict) -> str:
    """Return the C++ size expression for sizing the C++ container type for a given parameter."""
    expression = get_buffer_size_expression(parameter)
    if _is_null_terminated_in_c(parameter):
        # if the C API reports strlen instead of size:
        # Don't subtract one for the null terminator, the API already did!
        if _has_strlen_bug(parameter):
            return f"{expression} /* Workaround: strlen-bug */"
        return f"{expression} - 1"
    return expression


def _is_ivi_dance_array_param(parameter):
    return get_size_mechanism(parameter) == "ivi-dance"


def has_ivi_dance_param(parameters):
    """Whether any parameter uses the ivi-dance size mechanism."""
    return any(_is_ivi_dance_array_param(p) for p in parameters)


def is_two_dimension_array_param(parameter):
    """Whether the given parameter is a two-dimensional array."""
    return get_size_mechanism(parameter) == "two-dimension"


def has_two_dimension_array_param(parameters):
    """Whether any parameter is a two-dimensional array."""
    return any(is_two_dimension_array_param(p) for p in parameters)


def has_repeated_varargs_parameter(parameters):
    """Whether any parameter is a repeated varargs parameter."""
    return any(is_repeated_varargs_parameter(p) for p in parameters)


def can_mock_function(parameters):
    """Whether a function with the given parameters can be mocked by googlemock.

    Google Mock can't handle the case where a function has a variable number of arguments and
    there's also a limit on the max number of arguments.
    """
    # I'm not sure this is exactly right, but it does enough to distinguish between
    # non-varargs functions and varargs functions that take > 100 parameters.
    max_mock_param_len = 20
    repeated_varargs_parameters = [p for p in parameters if is_repeated_varargs_parameter(p)]
    first_repeating_parameters = len([p for p in parameters if is_repeating_parameter(p)])
    if not any(repeated_varargs_parameters):
        return len(parameters) - first_repeating_parameters <= max_mock_param_len
    varargs_parameter = repeated_varargs_parameters[0]
    return (
        len(parameters)
        - first_repeating_parameters
        - len(repeated_varargs_parameters)
        + (first_repeating_parameters * varargs_parameter["max_length"])
        <= max_mock_param_len
    )


def get_ivi_dance_params(parameters):
    """Get the relevant parameters for the first ivi-dance parameter, if any."""
    array_param = next((p for p in parameters if _is_ivi_dance_array_param(p)), None)
    size_param = (
        next(p for p in parameters if p["name"] == array_param["size"]["value"])
        if array_param
        else None
    )
    other_params = (p for p in parameters if p != array_param and p != size_param)
    return (size_param, array_param, other_params)


def is_ivi_dance_array_with_a_twist_param(parameter):
    """Whether the given parameter is an ivi-dance-with-a-twist parameter."""
    return get_size_mechanism(parameter) == "ivi-dance-with-a-twist"


def has_ivi_dance_with_a_twist_param(parameters):
    """Whether any parameter is an ivi-dance-with-a-twist parameter."""
    return any(is_ivi_dance_array_with_a_twist_param(p) for p in parameters)


def get_param_with_name(parameters: List[dict], name: str) -> dict:
    """Get the parameter that has the given name."""
    matched_params = (p for p in parameters if p["name"] == name)
    return next(matched_params)


def get_first_session_param(parameters: List[dict]) -> dict:
    """Get the first parameter whose type is a Session."""
    matched_params = (p for p in parameters if p.get("grpc_type", None) == "nidevice_grpc.Session")
    return next(matched_params)


class IviDanceWithATwistParamSet(NamedTuple):  # noqa: D101
    array_params: List[dict]
    size_param: dict
    twist_param: dict

    @property
    def all_params(self):
        """All parameters in the set."""
        return self.array_params + [self.size_param, self.twist_param]

    @property
    def size_param_name(self) -> str:
        """Size parameter."""
        return get_cpp_local_name(self.size_param)

    @property
    def twist_param_name(self) -> str:
        """Twist parameter."""
        return get_cpp_local_name(self.twist_param)

    @property
    def is_in_out_twist(self) -> bool:
        """Return whether this is an "in-out" twist.

        An "in-out" twist is a rare variant of ivi-dance-with-a-twist where the size and the twist
        are the same param used as an in-out param, rather than separate input and output params.
        """
        return self.size_param_name == self.twist_param_name


def _make_ivi_twist_param_set(
    twist_param_name: str, parameters: List[dict]
) -> IviDanceWithATwistParamSet:
    matched_array_params = [
        p for p in parameters if _get_ivi_dance_twist_param_name(p) == twist_param_name
    ]
    return IviDanceWithATwistParamSet(
        matched_array_params,
        get_param_with_name(parameters, matched_array_params[0]["size"]["value"]),
        get_param_with_name(parameters, twist_param_name),
    )


def _unique_twist_params(parameters) -> List[str]:
    unique_set = {_get_ivi_dance_twist_param_name(p) for p in parameters}

    # Sort and remove None
    return sorted((p for p in unique_set if p))


def get_ivi_dance_with_a_twist_params(parameters: List[dict]) -> List[IviDanceWithATwistParamSet]:
    """Get the ivi-dance-with-a-twist parameters."""
    return [
        _make_ivi_twist_param_set(twist_name, parameters)
        for twist_name in _unique_twist_params(parameters)
    ]


def get_params_not_in_ivi_twist(
    parameters: List[dict], ivi_param_sets: List[IviDanceWithATwistParamSet]
) -> List[dict]:
    """Get the parameters that are not involved with an ivi-dance-with-a-twist mechanism."""
    all_params_in_ivi_set = {p["name"] for ivi_set in ivi_param_sets for p in ivi_set.all_params}

    return [p for p in parameters if p["name"] not in all_params_in_ivi_set]


def is_init_method(function_data):
    """Whether the function is an init_method."""
    return function_data.get("init_method", False)


def _get_session_output_param(function_data):
    return next(
        p
        for p in function_data["parameters"]
        if p["direction"] == "out" and "nidevice_grpc.Session" in p["grpc_type"]
    )


def is_init_array_method(function_data):
    """Whether the function is an init_method with a repeated Session output parameter."""
    return (
        is_init_method(function_data)
        and "repeated" in _get_session_output_param(function_data)["grpc_type"]
    )


def is_cross_driver_init_method(function_data: dict) -> bool:
    """Whether the function is an init_method for a cross_driver_session."""
    return is_init_method(function_data) and any(
        p
        for p in function_data["parameters"]
        if "cross_driver_session" in p and p["direction"] == "out"
    )


def has_streaming_response(function_data):
    """Whether the function has a stream_response."""
    return function_data.get("stream_response", False)


def _has_callback_param(function_data):
    return any((p for p in function_data["parameters"] if "callback_params" in p))


def has_async_streaming_response(function_data):
    """Whether the function has an async stream_response."""
    return has_streaming_response(function_data) and _has_callback_param(function_data)


def get_library_interface_type_name(config):
    """Get the LibraryInterface type name, based on the service_class_prefix config setting."""
    service_class_prefix = config["service_class_prefix"]
    return f"{service_class_prefix}LibraryInterface"


def indent(level):
    """For use as a mako filter.

    Returns a function that indents a block of text to the provided level.
    """

    def indent_text_to_level(text, level):
        result = ""
        indentation = level * "  "
        for line in text.splitlines(True):
            if line.strip():
                result += indentation
            result += line
        return result

    return lambda text: indent_text_to_level(text, level)


def trim_trailing_comma():
    """For use as a mako filter.

    Returns a function that removes the last comma from a block of text (preserves newlines).
    Consider this as an alternative to str.join when it allows preserving context in the mako file.
    """

    def trim_trailing_comma_impl(text: str) -> str:
        i = text.rfind(",")
        return text[:i] + text[i + 1 :]

    return lambda text: trim_trailing_comma_impl(text)


def os_conditional_compile_block(config):
    """For use as a mako filter.

    That wraps a block of text in #if blocks based on the config's OS support.
    """
    windows_only = config.get("windows_only", False)

    def windows_only_block_impl(text):
        # Pure python code, by default, will convert to platform-specific linesep characters on
        # save. But mako uses the platform-specific linesep characters from the template file in the
        # template string. This is balanced by the newline="" args in template_helpers, which
        # preserve newlines from the input.
        #
        # We use os.linesep here for consistency with makos template strings and to ensure that we
        # don't get a mix of CRLF and LF on windows.
        return f"#if defined(_MSC_VER){os.linesep}{text}#endif // defined(_MSC_VER){os.linesep}"

    if windows_only:
        return lambda text: windows_only_block_impl(text)

    return lambda text: text


def filter_parameters_for_grpc_fields(parameters_or_fields: List[dict]):
    """Filter out the parameters that shouldn't be represented by a field on a grpc message.

    For example, get rid of any parameters whose values should be determined from another parameter.
    """
    return [p for p in parameters_or_fields if p.get("include_in_proto", True)]


class AttributeGroup:  # noqa: D101
    def __init__(self, name, attributes, config):  # noqa: D107
        self.name = name
        self.attributes = attributes
        self._config = config

    def get_attributes_split_by_sub_group(self):
        """Split attributes by type, with an added "Reset" sub-group for resettable attributes."""
        if not get_split_attributes_by_type(self._config):
            return {"": self.attributes}

        categorized_attributes = defaultdict(dict)
        for id, data in self.attributes.items():
            data_type = data["type"]
            if "bitfield_enum" in data:
                assert data_type == "int32[]"
                data_type = "int32"
            data_type = get_grpc_type_name_for_identifier(data_type, self._config)
            categorized_attributes[data_type][id] = data
            if data.get("resettable", False):
                categorized_attributes["Reset"][id] = data
        return categorized_attributes


def get_attribute_enum_suffix(config: dict) -> str:
    """Get the name suffix of the enum whose values are the attributes."""
    use_legacy_prefix = _use_legacy_attribute_prefix(config)
    return "Attributes" if use_legacy_prefix else "Attribute"


def get_attribute_enum_name(group_name: str, data_type: str, config: dict) -> str:
    """Get the name of the enum whose values are the attributes."""
    attribute_suffix = get_attribute_enum_suffix(config)
    return f"{group_name}{data_type}{attribute_suffix}"


def get_attribute_groups(data):
    """Get the attribute groups."""
    attributes = data["attributes"]
    config = data["config"]

    # If the attributes are already in string categories: those are the groups. Return as-is.
    first_key = next(iter(attributes), None)
    if isinstance(first_key, str):
        return [AttributeGroup(name, attributes, config) for name, attributes in attributes.items()]

    # If there's just one level of attributes: use the service_class_prefix as the group.
    service_class_prefix = config["service_class_prefix"]
    return [AttributeGroup(service_class_prefix, attributes, config)]


def strip_prefix(s: str, prefix: str) -> str:
    """Strip the given prefix, if present, and return the resulting string."""
    return s[len(prefix) :] if s.startswith(prefix) else s


def strip_suffix(s: str, suffix: str) -> str:
    """Strip the given suffix, if present, and return the resulting string."""
    return s[: -len(suffix)] if s.endswith(suffix) else s


def _replace_prefix(s: str, prefix: str, sub: str) -> str:
    return sub + s[len(prefix) :] if s.startswith(prefix) else s


def get_grpc_type_name_for_identifier(data_type, config):
    """Create an identifier string based on the grpc_type.

    i.e., double -> Double. repeated double -> DoubleArray.
    """
    grpc_type = get_grpc_type(data_type, config)
    grpc_type = re.sub(r"^(repeated )(\w+)$", r"\2Array", grpc_type)
    # take the last identifier if the type is namespaced (i.e., Timestamp)
    grpc_type = grpc_type.split(".")[-1]
    return ensure_pascal_case(grpc_type)


def _get_grpc_type_from_ivi(
    type: str, is_array: bool, driver_name_pascal: str, config: dict
) -> str:
    add_repeated = is_array
    if "ViSession" in type:
        type = "nidevice_grpc.Session"
    if "ViBoolean" in type:
        type = "bool"
    if "ViReal64" in type:
        type = "double"
    if "ViInt32" in type:
        type = "sint32"
    if "ViConstString" in type:
        type = "string"
    if "ViString" in type:
        type = "string"
    if "ViRsrc" in type:
        type = "string"
    if "ViChar" in type:
        if is_array:
            add_repeated = False
            type = "string"
        else:
            type = "uint32"
    if "ViReal32" in type:
        type = "float"
    if "ViAttr" in type:
        type = get_attribute_enum_name(driver_name_pascal, "", config)
    if "ViInt8" in type:
        if is_array:
            type = "bytes"
            add_repeated = False
        else:
            type = "uint32"
    if "void*" in type:
        type = "fixed64"
    if "ViInt16" in type:
        type = "sint32"
    if "ViInt64" in type:
        type = "int64"
    if "ViUInt16" in type:
        type = "uint32"
    if "ViUInt32" in type:
        type = "uint32"
    if "ViUInt64" in type:
        type = "uint64"
    if "ViUInt8" in type:
        if is_array:
            type = "bytes"
            add_repeated = False
        else:
            type = "uint32"
    if "ViStatus" in type:
        type = "sint32"
    if "ViAddr" in type:
        type = "fixed64"
    if "int" == type:
        type = "sint32"
    if "[]" in type:
        type = type.replace("[]", "")

    return "repeated " + type if add_repeated else type


def get_grpc_type(data_type, config):
    """Get the grpc_type for the given type."""
    service_class_prefix = config["service_class_prefix"]
    if "type_to_grpc_type" in config:
        type_map = config["type_to_grpc_type"]
        stripped_type = strip_prefix(data_type, "const ")
        if stripped_type in type_map:
            return type_map[stripped_type]

        repeated = is_array(data_type)

        stripped_type = strip_suffix(stripped_type, "*")
        stripped_type = strip_suffix(stripped_type, "[]")

        # Note: if we never resolve or strip anything, this will fallback
        # to the original datatype.
        resolved_type = type_map.get(stripped_type, stripped_type)

        return f"repeated {resolved_type}" if repeated else resolved_type

    return _get_grpc_type_from_ivi(data_type, is_array(data_type), service_class_prefix, config)


def _use_legacy_attribute_prefix(config: dict) -> bool:
    return config.get("use_legacy_attribute_prefix", False)


def get_split_attributes_by_type(config):
    """Get the split_attributes_by_type config setting."""
    return config.get("split_attributes_by_type", False)


def supports_raw_attributes(config: dict) -> bool:
    """Get the supports_raw_attributes config setting."""
    return config.get("supports_raw_attributes", False)


def get_enum_value_cpp_type(enum: dict) -> str:
    """Use the python datatype of the first value in the enum to infer the C++ type.

    Used for mapped enums.
    """
    enum_value = enum["values"][0]["value"]
    if isinstance(enum_value, float):
        return "double"
    if isinstance(enum_value, int):
        return "std::int32_t"
    if isinstance(enum_value, str):
        return "std::string"
    return "std::int32_t"


def is_regular_string_arg(parameter: dict) -> bool:
    """Return whether the parameter is a "regular" string.

    This excludes byte arrays.
    """
    return is_string_arg(parameter) and not parameter["grpc_type"] == "bytes"


def is_regular_byte_array_arg(parameter: dict) -> bool:
    """Return whether the parameter is a "regular" byte array.

    This excludes byte arrays that are mapped to enums.
    """
    return parameter["grpc_type"] == "bytes" and not is_enum(parameter)


def get_additional_headers(config: dict, including_from_file: str) -> List[str]:
    """Get the list of additional headers required by the given file."""
    additional_header_requirements = config.get("additional_headers", {})
    return [
        header
        for header, required_by in additional_header_requirements.items()
        if including_from_file in required_by
    ]


def get_enum_value_prefix(enum_name: str, enum: dict) -> str:
    """Get the enum value prefix for the given enum."""
    return enum.get("enum-value-prefix", pascal_to_snake(enum_name).upper())


def get_driver_readiness(config: dict) -> str:
    """Get the code_readiness config setting."""
    return config.get("code_readiness", "Release")


def is_driver_restricted(config: dict) -> str:
    """Get the is_restricted config setting."""
    return config.get("is_restricted", False)


def get_grpc_field_name(param: dict) -> str:
    """Get the name of the protobuf field for the given param.

    This will be a snake_case_string, that can be used in the proto
    definition itself, as well as in C++ code that accesses the field
    from a Request/Response message.
    """
    return param.get("grpc_name", camel_to_snake(param["name"]))


def get_grpc_client_field_name(param: dict) -> str:
    """Get the name of the protobuf field for the given param.

    This will be a snake_case_string, that can be used in the client generated files.
    """
    return param.get("grpc_name", camel_to_snake(param["cppName"]))


def get_grpc_field_name_from_str(field_name: str) -> str:
    """Get the default grpc_name for the given parameter name."""
    # NOTE: Does not account for "grpc_name" overrides, but can be used to get a proto name from a
    # camelCase field name when no overrides are present.
    return camel_to_snake(field_name)


def get_cpp_local_name(param: dict) -> str:
    """Return a similar token to get_grpc_field_name, but ensure it is valid as a C++ variable name.

    NOTE: this is not used consistently to differentiate from get_grpc_field_name.  For that reason,
    the field respects the "grpc_name" override so that the two will match in the vast majority of
    cases where "name" is not a reserved keyword.  If "grpc_name" is a reserved keyword, this may be
    an issue (but don't use reserved grpc_name!).
    """
    return param.get("cpp_local_name", param.get("grpc_name", camel_to_snake(param["cppName"])))


def get_grpc_field_names_for_param_names(params: List[dict], names: List[str]) -> List[str]:
    """Get the grpc field name for the corresponding param in params given a list of names."""
    return [get_grpc_field_name(get_param_with_name(params, name)) for name in names]


def is_return_value(parameter: dict) -> bool:
    """Whether the parameter is marked as a return_value."""
    return parameter.get("return_value", False)


def is_get_last_error_output_param(parameter: dict) -> bool:
    """Return True if parameter is a get_last_error parameter."""
    return "get_last_error" in parameter


def is_optional_param(parameter: dict) -> bool:
    """Whether the parameter is marked is_optional."""
    return parameter.get("is_optional", False)


def get_driver_api_params(parameters: List[dict]) -> List[dict]:
    """Return all parameters that are passed as parameters to the driver API.

    Excludes:
    * Return values.
    * Outputs that are calculated/populated after the API call.
    * Proto only params.
    """
    return [
        p
        for p in parameters
        if not (
            is_return_value(p) or is_get_last_error_output_param(p) or is_proto_only_parameter(p)
        )
    ]


def get_params_needing_initialization(parameters: List[dict]) -> List[dict]:
    """Return all parameters that need to be initialized before the API call.

    Excludes:
    * Return values.
    * Outputs that are calculated/populated after the API call.
    """
    return [p for p in parameters if not (is_return_value(p) or is_get_last_error_output_param(p))]


def filter_moniker_streaming_functions(
    functions: dict, functions_to_generate: List[str]
) -> List[str]:
    """Return streaming functions that need to be generated."""
    return [
        name for name in functions_to_generate if is_moniker_streaming_function(functions[name])
    ]


def is_moniker_streaming_function(function: dict) -> bool:
    """Whether this function is for streaming data through moniker."""
    return function.get("is_streaming_api", False)


def get_data_moniker_function_name(function_name: str) -> str:
    """Return the corresponding moniker function name for the given C API function."""
    return function_name.replace("Begin", "Moniker")


def get_data_moniker_struct_name(begin_function_name: str) -> str:
    """Return the Moniker function name.

    Input expected is Begin* streaming API name.
    """
    return f"{begin_function_name.replace('Begin', 'Moniker')}Data"


def get_data_moniker_request_message_type(begin_function_name: str) -> str:
    """Return the request message type for Moniker functions.

    Input expected is Begin* streaming API name.
    """
    return f"{begin_function_name.replace('Begin', 'Moniker')}Request"


def get_data_moniker_response_message_type(begin_function_name: str) -> str:
    """Return the response message type for Moniker functions.

    Input expected is Begin* streaming API name.
    """
    return f"{begin_function_name.replace('Begin', 'Moniker')}Response"


def get_data_moniker_function_parameters(function: dict) -> Tuple[List[dict], List[dict]]:
    """Return moniker function parameters split into input/output.

    Input expected is equivalent non-streaming function.
    Add a default "status" output parameter if there isn't one already.
    """
    parameter_array = filter_parameters_for_grpc_fields(function["parameters"])
    input_parameters = [
        p for p in parameter_array if is_input_parameter(p) and p.get("is_streaming_type", False)
    ]
    default_status_param = {"name": "status", "type": "int32", "grpc_type": "int32"}
    output_parameters = [default_status_param]
    output_parameters.extend([p for p in parameter_array if is_output_parameter(p)])
    return (input_parameters, output_parameters)


def is_function_in_streaming_functions(
    function_name: str, streaming_functions_to_generate: List[str]
):
    """Check if a function name is in the streaming functions to generate."""
    return function_name in streaming_functions_to_generate


def _is_streaming_param_input_array(streaming_param: dict) -> bool:
    """Check if the streaming parameter is an input array."""
    return (
        streaming_param
        and streaming_param["direction"] == "in"
        and is_array(streaming_param["type"])
    )


def get_non_streaming_input_parameters(parameters: List[dict]) -> List[dict]:
    """Determine if a parameter should be passed from Begin streaming API to Moniker function."""
    streaming_param = get_first_streaming_parameter(parameters)
    params = []
    for param in parameters:
        if is_input_parameter(param) and not param.get("is_streaming_type", False):
            if _is_streaming_param_input_array(streaming_param):
                size_param_name = get_size_param(streaming_param)
                if size_param_name != param["name"]:
                    params.append(param)
            else:
                params.append(param)
    return params


def extend_input_params_with_size_params(input_parameters: List[dict], function_metadata: dict):
    """Return the input_parameters list with size parameters added to it."""
    for param in input_parameters:
        size_param_name = get_size_param(param)
        size_param = [p for p in function_metadata["parameters"] if p["name"] == size_param_name]
        input_parameters.extend(size_param)


def has_value_converted_to_c_representation(parameters: List[dict], parameter: dict) -> bool:
    """Check if the parameter contains a casted name."""
    for p in parameters:
        if "value_converted_to_c_representation" in p and p.get("size", {}).get(
            "value_twist"
        ) == parameter.get("name"):
            return True
    return parameter.get("value_converted_to_c_representation", False)


def get_value_converted_to_c_representation(parameters: List[dict], parameter: dict) -> str:
    """Get the casted name of the parameter."""
    for p in parameters:
        if "value_converted_to_c_representation" in p and p.get("size", {}).get(
            "value_twist"
        ) == parameter.get("name"):
            return camel_to_snake(parameter["name"] + " * 2")
    return camel_to_snake(parameter.get("value_converted_to_c_representation", ""))
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/format_mi_metadata.py sha256=7382240332b2d077abcff31b0668a2b77588a54271504b20d1a4c72b39a03fc3 bytes=4377 -->
## FILE: source/codegen/format_mi_metadata.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/format_mi_metadata.py`
- sha256: `7382240332b2d077abcff31b0668a2b77588a54271504b20d1a4c72b39a03fc3`
- bytes: 4377

````python
"""Script for formatting mi-driver metadata in same style as hapigen output."""

import argparse
import io
import os
from enum import Enum

import metadata_mutation
from template_helpers import load_metadata


class _Formatter(object):
    # From https://stackoverflow.com/questions/3229419/how-to-pretty-print-nested-dictionaries
    # Changes
    #  - sort keys in tuple and dictionary for reproducability
    #  - Use 4 spaces rather than tab (\t) per indent level
    def __init__(self):
        self.types = {}
        self.htchar = "    "
        self.lfchar = "\n"
        self.indent = 0
        self._set_formatter(object, self.__class__._format_object)
        self._set_formatter(dict, self.__class__._format_dict)
        self._set_formatter(list, self.__class__._format_list)
        self._set_formatter(tuple, self.__class__._format_tuple)
        self._set_formatter(Enum, self.__class__._format_enum)

    def _set_formatter(self, obj, callback):
        self.types[obj] = callback

    def _get_formatter(self, value):
        formater = self.types[type(value) if type(value) in self.types else object]
        if isinstance(value, Enum):
            formater = self.types[Enum]

        return formater

    def __call__(self, value, **args):
        for key in args:
            setattr(self, key, args[key])
        formater = self._get_formatter(value)
        return formater(self, value, self.indent)

    def _format_object(self, value, indent):
        return repr(value)

    def _format_enum(self, value, indent):
        return repr(value.value)

    def _format_dict(self, value, indent):
        items = [
            self.lfchar
            + self.htchar * (indent + 1)
            + (self._get_formatter(key))(self, key, indent)
            + ": "
            + (self._get_formatter(value[key]))(self, value[key], indent + 1)
            for key in sorted(value)
        ]
        return "{%s}" % (",".join(items) + self.lfchar + self.htchar * indent)

    def _format_list(self, value, indent):
        items = [
            self.lfchar
            + self.htchar * (indent + 1)
            + (self._get_formatter(item))(self, item, indent + 1)
            for item in value
        ]
        return "[%s]" % (",".join(items) + self.lfchar + self.htchar * indent)

    def _format_tuple(self, value, indent):
        items = [
            self.lfchar
            + self.htchar * (indent + 1)
            + (self._get_formatter(item))(self, item, indent + 1)
            for item in sorted(value)
        ]
        return "(%s)" % (",".join(items) + self.lfchar + self.htchar * indent)


def _format_mi_metadata(metadata_dir: str):
    mi_drivers_to_update = [
        "nidcpower",
        "nidigitalpattern",
        "nidmm",
        "nifake",
        "nifgen",
        "niscope",
        "niswitch",
        "nitclk",
    ]
    mi_drivers = [driver for driver in os.listdir(metadata_dir) if driver in mi_drivers_to_update]
    pretty = _Formatter()
    for mi_driver in mi_drivers:
        metadata_names = ["attributes", "config", "enums", "functions"]
        path = f"{metadata_dir}/{mi_driver}/"
        metadata = load_metadata(path)
        metadata_mutation.mutate(metadata)
        api_name = metadata["config"]["driver_name"]
        api_version = metadata["config"]["api_version"]
        for metadata_name in metadata_names:
            actual_metadata = metadata[metadata_name]
            pretty_metadata = "# -*- coding: utf-8 -*-"
            pretty_metadata += "\n"
            pretty_metadata += (
                f"# This file is generated from {api_name} API metadata version {api_version}"
            )
            pretty_metadata += "\n"
            pretty_metadata += f"{metadata_name} = {pretty(actual_metadata)}\n"
            with io.open(f"{path}{metadata_name}.py", "w", encoding="utf-8") as temp:
                temp.write(pretty_metadata)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check if any file has changed that affects the Linux RT Feed."
    )
    parser.add_argument(
        "metadata",
        help="The path to the directory containing all of the metadata.",
    )
    args = parser.parse_args()
    _format_mi_metadata(args.metadata)
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/generate_server_capabilities.py sha256=5fe35a65ffa5d703b63fecf344fddf4640bb1eeb3a33b6f02d6dc0a67d9a8fb3 bytes=1773 -->
## FILE: source/codegen/generate_server_capabilities.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/generate_server_capabilities.py`
- sha256: `5fe35a65ffa5d703b63fecf344fddf4640bb1eeb3a33b6f02d6dc0a67d9a8fb3`
- bytes: 1773

````python
"""Service information generation."""

import argparse
import json
from pathlib import Path

from common_helpers import get_driver_readiness, is_driver_restricted
from template_helpers import load_metadata


def _generate_file(metadata_dir: Path, output_dir: Path) -> None:
    service_instance_names = []
    driver_modules = [
        load_metadata(p)
        for p in sorted(metadata_dir.iterdir())
        if p.is_dir() and "fake" not in p.name
    ]
    for data in driver_modules:
        config = data["config"]
        if get_driver_readiness(config) == "Release" and not is_driver_restricted(config):
            service_name = f'{config["module_name"]}_grpc.{config["service_class_prefix"]}'
            service_instance_names.append(service_name)
    service_information_dict = {}
    service_information_dict["provided_service_interfaces"] = service_instance_names
    output_file_path = Path(output_dir).joinpath("server_capabilities.json")
    with open(output_file_path, "w") as outfile:
        json.dump(service_information_dict, outfile, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate NI gRPC-device server implementation information."
    )
    parser.add_argument(
        "metadata",
        help="The path to the directory containing the metadata for the API being generated.",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="The path to the top-level directory to save the generated files. The API-specific sub-directories will be automatically created.",
    )
    args = parser.parse_args()
    output_path = "." if args.output is None else args.output
    _generate_file(Path(args.metadata), Path(output_path))
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/generate_service.py sha256=6f4dd0959026bd1fa16b08bdc36a04506db47da28cf1b8c6aefc8d3aad6c3ef5 bytes=3596 -->
## FILE: source/codegen/generate_service.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/generate_service.py`
- sha256: `6f4dd0959026bd1fa16b08bdc36a04506db47da28cf1b8c6aefc8d3aad6c3ef5`
- bytes: 3596

````python
"""Service generation."""

import argparse
import os

import metadata_mutation
import metadata_validation
from mako.lookup import TemplateLookup  # type: ignore
from mako.template import Template  # type: ignore
from template_helpers import instantiate_mako_template, load_metadata, write_if_changed


def _generate_service_file_with_mako(metadata, template, generated_file_suffix, gen_dir):
    module_name = metadata["config"]["module_name"]
    output_dir = os.path.join(gen_dir, module_name)
    file_name = module_name + generated_file_suffix
    output_file_path = os.path.join(output_dir, file_name)
    os.makedirs(output_dir, exist_ok=True)
    write_if_changed(output_file_path, template.render(data=metadata))


def _generate_service_file(metadata, template_file_name, generated_file_suffix, gen_dir):
    template = instantiate_mako_template(template_file_name)
    _generate_service_file_with_mako(metadata, template, generated_file_suffix, gen_dir)


def _generate_all(metadata_dir: str, gen_dir: str, validate_only: bool):
    metadata = load_metadata(metadata_dir)
    metadata_validation.validate_metadata(metadata)
    if validate_only:
        return

    lookup = TemplateLookup(directories=metadata_dir)
    metadata["lookup"] = lookup
    metadata_mutation.mutate(metadata)
    _generate_service_file(metadata, "proto.mako", ".proto", gen_dir)
    _generate_service_file(metadata, "service.h.mako", "_service.h", gen_dir)
    _generate_service_file(metadata, "service.cpp.mako", "_service.cpp", gen_dir)
    _generate_service_file(metadata, "service_registrar.h.mako", "_service_registrar.h", gen_dir)
    _generate_service_file(
        metadata, "service_registrar.cpp.mako", "_service_registrar.cpp", gen_dir
    )
    _generate_service_file(metadata, "library_interface.h.mako", "_library_interface.h", gen_dir)
    _generate_service_file(metadata, "library.cpp.mako", "_library.cpp", gen_dir)
    _generate_service_file(metadata, "library.h.mako", "_library.h", gen_dir)
    _generate_service_file(metadata, "mock_library.h.mako", "_mock_library.h", gen_dir)
    _generate_service_file(metadata, "client.h.mako", "_client.h", gen_dir)
    _generate_service_file(metadata, "client.cpp.mako", "_client.cpp", gen_dir)
    _generate_service_file(metadata, "compilation_test.cpp.mako", "_compilation_test.cpp", gen_dir)
    if "custom_header_suffix" in metadata["config"]:
        custom_mako_full_path = os.path.join(metadata_dir, "custom_header.mako")
        template = Template(filename=str(custom_mako_full_path), lookup=lookup)
        _generate_service_file_with_mako(
            metadata, template, metadata["config"]["custom_header_suffix"], gen_dir
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate files for specified NI driver API gRPC service."
    )
    parser.add_argument(
        "metadata",
        help="The path to the directory containing the metadata for the API being generated.",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="The path to the top-level directory to save the generated files. The API-specific sub-directories will be automatically created.",
    )
    parser.add_argument(
        "--validate",
        "-v",
        dest="validate",
        action="store_true",
        help="Just validate the metadata and don't generate any files",
    )
    args = parser.parse_args()
    _generate_all(args.metadata, "." if args.output is None else args.output, args.validate)
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/generate_shared_service_files.py sha256=11dccc9495789ced12a110fa65b86914539fa5ed14f82cdd46c3f7d1618b254b bytes=1386 -->
## FILE: source/codegen/generate_shared_service_files.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/generate_shared_service_files.py`
- sha256: `11dccc9495789ced12a110fa65b86914539fa5ed14f82cdd46c3f7d1618b254b`
- bytes: 1386

````python
"""Shared service file generation."""

from argparse import ArgumentParser
from pathlib import Path

from template_helpers import instantiate_mako_template, write_if_changed, load_metadata


def _generate_register_all_services(metadata_dir: Path, output_dir: Path) -> None:
    driver_modules = [
        load_metadata(p)
        for p in sorted(metadata_dir.iterdir())
        if p.is_dir() and "fake" not in p.name
    ]

    template = instantiate_mako_template("register_all_services.h.mako")

    write_if_changed(
        output_dir / "register_all_services.h", template.render(drivers=driver_modules)
    )

    template = instantiate_mako_template("register_all_services.cpp.mako")

    write_if_changed(
        output_dir / "register_all_services.cpp", template.render(drivers=driver_modules)
    )


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate shared service files for grpc-device.")
    parser.add_argument(
        "metadata", help="The path to the root directory containing all API metadata."
    )
    parser.add_argument(
        "--output", "-o", help="The path to the top-level directory to save the generated files.."
    )

    args = parser.parse_args()
    output_path = "." if args.output is None else args.output
    _generate_register_all_services(Path(args.metadata), Path(output_path))
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/Imported_From_Hapigen.md sha256=37a21632555a6eeecc41188b9da7eb7bb8bb67550054fd76ae1f86a8dcfac345 bytes=702 -->
## FILE: source/codegen/metadata/Imported_From_Hapigen.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/Imported_From_Hapigen.md`
- sha256: `37a21632555a6eeecc41188b9da7eb7bb8bb67550054fd76ae1f86a8dcfac345`
- bytes: 702

````markdown
# Why are there .proto files here?

Hapigen is also producing .proto files based on the metadata files (functions.py, etc). We are importing the hapigen created
.proto files here so we can validate that they match against the ones generated in grpc-device.

# Failing build on Validate Imported Protos step

Check these three potential issues, in order, to fix the build error:

1. Make sure .proto from driver export is copied over to grpc-device
2. Make sure you built grpc-device locally to get any generated folder changes (specifically .proto files there)
3. The proto generators (mako and helper python files) likely changed between grpc-device and hapigen and need to be synced up. 
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidaqmx/__init__.py sha256=05615637b82a5c33a519f8aa42d8214b6360318b8c15bf97737098f180aef17a bytes=680 -->
## FILE: source/codegen/metadata/nidaqmx/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidaqmx/__init__.py`
- sha256: `05615637b82a5c33a519f8aa42d8214b6360318b8c15bf97737098f180aef17a`
- bytes: 680

````python
from .functions import functions
from .functions_addon import functions_validation_suppressions, functions_override_metadata
from .attributes import attributes
from .enums import enums
from .enums_addon import enums_validation_suppressions, enums_override_metadata
from .config import config

metadata = {
    "functions" : functions,
    "functions_validation_suppressions": functions_validation_suppressions,
    "attributes" : attributes,
    "enums" : enums,
    "enums_validation_suppressions": enums_validation_suppressions,
    "config" : config
}
metadata['functions'].update(functions_override_metadata)
metadata['enums'].update(enums_override_metadata)
````
