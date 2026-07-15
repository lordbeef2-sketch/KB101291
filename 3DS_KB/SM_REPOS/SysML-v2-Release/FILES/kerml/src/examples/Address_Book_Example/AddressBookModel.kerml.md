# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Address Book Example/AddressBookModel.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Address Book Example/AddressBookModel.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Address Book Example/AddressBookModel.kerml
- source_bytes: 176
- source_sha256: `30baae0ada289e144667adbe2f92409b21f3a3f4caf66329d9e829bd34f8226b`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
private import ScalarValues::*;
package AddressBookModel {
	
	class Entry {
		name: String;
		address: String;
	}
	
	class AddressBook {
		entries: Entry[*];
	}
	
}
````
