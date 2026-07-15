# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.jupyter.kernel/src/main/resources/sysml/kernel.json

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.jupyter.kernel/src/main/resources/sysml/kernel.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.jupyter.kernel/src/main/resources/sysml/kernel.json
- source_bytes: 298
- source_sha256: `afb488e154601e02f93e80623841d94388aa0191e06988b4f0a605b7f132c86f`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
    "argv": [
        "java",
		"-cp",
		"@KERNEL_INSTALL_DIRECTORY@/*",
		"org.omg.sysml.jupyter.kernel.ISysML",
        "{connection_file}"
    ],
    "display_name": "SysML",
    "language": "sysml",
    "interrupt_mode": "message",
    "env": {
    },
    "metadata": {
    }
}
````
