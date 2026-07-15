# NI OFFLINE AGENT ROUTING DIGEST

<!--MACHINE_ROUTING priority=exact_reference_then_concept_then_release -->

## QUERY_CLASS_TO_CORPUS

| query class | primary corpus | secondary corpus |
|---|---|---|
| LabVIEW G syntax, nodes, VI Server, VI Scripting, properties, methods, events | `NI_LABVIEW/PROGRAMMING_REFERENCE/` | `NI_LABVIEW/USER_MANUAL/` |
| LabVIEW architecture, execution, projects, builds, deployment | `NI_LABVIEW/USER_MANUAL/` | `NI_LABVIEW/PROGRAMMING_REFERENCE/` |
| LabVIEW 2024+ changes, compatibility, known issues | `NI_LABVIEW/RELEASES/` | matching ecosystem bundle |
| NI driver LabVIEW VI, property, function, error | `NI_ECOSYSTEM/BUNDLES/<matching *labview-api-ref or product bundle>/` | driver C/.NET bundle |
| C/C++/LabWindows-CVI | matching `*-c-api-ref`, `*-cvi`, or `labwindows-cvi` bundle | OSS protobuf/OpenAPI/source record |
| C#/.NET | matching `*-csharp-*`, `*-dotnet-*`, or `*-net-*` bundle | TestStand/VeriStand exact reference |
| Python standard language/library | `PYTHON_3_12_13/` | NI Python OSS interface |
| NI Python API, examples, signatures, docstrings | `NI_ECOSYSTEM/OSS_INTERFACES/<repository>/` | matching driver bundle |
| REST/OpenAPI/SystemLink | `NI_ECOSYSTEM/OSS_INTERFACES/systemlink-OpenAPI-documents/` and `nisystemlink-clients-python/` | `NI_ECOSYSTEM/BUNDLES/systemlink-*` |
| gRPC/protobuf remote driver control | `NI_ECOSYSTEM/OSS_INTERFACES/grpc-device/` | matching driver C/LabVIEW/.NET bundle |
| TestStand API | `NI_ECOSYSTEM/BUNDLES/teststand-api-reference/` | `grpc-teststand-api` and `teststand` |
| VeriStand API/custom devices | `veristand-*` bundles and `niveristand-python` | `NI_ECOSYSTEM/00_SOURCE_UNAVAILABLE.md` |
| RFmx/RFSA/RFSG/USRP | exact RFmx language bundle | matching OSS/gRPC record |
| DAQmx | `ni-daqmx-{labview,c,net}*` bundle | `nidaqmx-python` |
| FPGA/CompactRIO/Real-Time | `labview-fpga-module`, `lvfpga-api-ref`, `ni-compactrio`, `fpga-interface-c*` | `nifpga-python` |
| Vision/IMAQ/IMAQdx | `ni-vision*`, `ni-imaq*`, `ni-imaqdx*` | driver-language exact reference |
| XNET/automotive/industrial communications | `ni-xnet*`, `automotive-*`, `ecu-*`, `ni-industrial-*` | `nixnet-python` |

## RESOLUTION_RULES

1. Match exact symbol, VI, property, method, class, error code, or endpoint before conceptual text.
2. Prefer records whose interface language matches the requested output language.
3. Prefer current 2024+ product records; use retained legacy/NXG records only for migration or when the exact interface is legacy.
4. Treat every `SOURCE STATUS: UNAVAILABLE` record as a provenance tombstone, never as API content.
5. Preserve NI type names, units, enum spellings, calling order, ownership rules, and error behavior exactly.
6. For generated scripts, cross-check the language API and the driver/product concept record.
7. For LabVIEW VI generation, cross-check VI Scripting construction methods with the target driver VI connector/parameter record.

## MACHINE_COUNTS

- bundle_records: 70669
- bundle_count: 471
- oss_repository_count: 23
- oss_text_source_records: 5945
