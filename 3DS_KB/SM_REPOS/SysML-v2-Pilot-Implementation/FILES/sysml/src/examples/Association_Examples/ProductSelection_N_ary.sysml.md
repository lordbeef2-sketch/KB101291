# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Association Examples/ProductSelection_N_ary.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Association Examples/ProductSelection_N_ary.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Association Examples/ProductSelection_N_ary.sysml
- source_bytes: 616
- source_sha256: `84ca25cfe16c47ca74f4d2673b4e3cc4b6f8fbb80c668f03181d58f7b2b917c7`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ProductSelection_N_ary_SysML {
	
	item def ShoppingCart;
	item def Product;
	item def Account;
	
	// User-specified connection defiation definition
	connection def ProductSelection {
		end [0..1] item cart: ShoppingCart[1];
		end [0..*] item selectedProduct: Product[1];
		end [1..1] item account : Account[1];
	}
	
	// Equivalent connection defiation definition with named end items.
	connection def ProductSelection1 {
		end inCart[0..1] item cart: ShoppingCart[1];
		end selectedProducts[0..*] item selectedProduct: Product[1];
		end withAccount[1..1] item account : Account[1];
	}
	
}
````
