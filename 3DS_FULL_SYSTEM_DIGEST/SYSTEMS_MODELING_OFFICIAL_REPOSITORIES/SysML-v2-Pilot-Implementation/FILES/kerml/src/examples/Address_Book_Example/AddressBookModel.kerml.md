# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Address Book Example/AddressBookModel.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Address Book Example/AddressBookModel.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Address Book Example/AddressBookModel.kerml
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
