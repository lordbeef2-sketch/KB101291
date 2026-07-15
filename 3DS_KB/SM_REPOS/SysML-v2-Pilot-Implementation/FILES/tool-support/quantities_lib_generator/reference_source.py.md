# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/tool-support/quantities_lib_generator/reference_source.py

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `tool-support/quantities_lib_generator/reference_source.py`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/tool-support/quantities_lib_generator/reference_source.py
- source_bytes: 164
- source_sha256: `19d91652fb6ac70dabb74e3c1f0a10a4f2d2338c6aa718eae085aeae7dbd99ee`
- decoded_as: `utf-8`


## EXACT SOURCE

````python
from dataclasses import dataclass

@dataclass
class ReferenceSource:
    id: str
    title: str
    short_name: str
    publication_year: int
    uri: str

````
