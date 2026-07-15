# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Association Examples/ProductSelection_UnownedEnds.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Association Examples/ProductSelection_UnownedEnds.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Association Examples/ProductSelection_UnownedEnds.sysml
- source_bytes: 915
- source_sha256: `da6a677c7bfc868174390e3a0213514b340580665d119dfbcd82dd17c66d8895`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ProductSelection_UnownedEnds_SysML {
	
	item def SelectionInfo;
	item def ShoppingCart {
		item selectedProducts : Product[0..*];
	}
	item def Product {
		item inCart: ShoppingCart[0..1];
	}
	
	connection def ProductSelection {
		item info: SelectionInfo[1];
		
		end item cart: ShoppingCart[1] crosses selectedProduct.inCart;
		end item selectedProduct: Product[1] crosses cart.selectedProducts;
	}
	
	connection def SingleProductSelection :> ProductSelection {
		end item cart: ShoppingCart[1];
		end [0..1] item selectedProduct: Product[1];
	}
	
	item def OnlineCustomer {
		item info1: SelectionInfo;	
		item myCart: ShoppingCart[1];	
		item products: Product[0..*];
		
		connection ps1 : ProductSelection connect myCart to products {
			:>> info = info1;
		}
		
		connection ps2 : ProductSelection connect [1] myCart to [1] products {
			:>> info = info1;
		}
	}
	
}
````
