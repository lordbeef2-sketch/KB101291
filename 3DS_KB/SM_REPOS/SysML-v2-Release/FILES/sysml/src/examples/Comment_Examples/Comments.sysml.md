# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Comment Examples/Comments.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Comment Examples/Comments.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Comment Examples/Comments.sysml
- source_bytes: 398
- source_sha256: `670d98ce74569b5c85a9a5abe6d8364cb2fafdd6ae06a4c8c28d17cc6642b623`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package Comments {
	doc /* Documentation Comment */

	doc /* Documentation about Package */

	comment cmt /* Named Comment */	
	comment cmt_cmt about cmt /* Comment about Comment */
	
	comment about C /* Documention Comment on Part Def */
	part def C {
		doc /* Documentation in Part Def */
		comment /* Comment in Part Def */
		comment about Comments /* Comment about Package */
	}
}
````
