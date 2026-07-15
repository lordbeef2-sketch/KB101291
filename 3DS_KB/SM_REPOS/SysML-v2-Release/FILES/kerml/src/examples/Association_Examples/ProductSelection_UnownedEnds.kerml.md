# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Association Examples/ProductSelection_UnownedEnds.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Association Examples/ProductSelection_UnownedEnds.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Association Examples/ProductSelection_UnownedEnds.kerml
- source_bytes: 1357
- source_sha256: `47a86ed1692b4c9fc5a042cc8c0212eb854276525fc8845ec373d99b4bd33fb3`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package ProductSelection_UnownedEnds {
	
	class SelectionInfo;
	class ShoppingCart {
		feature selectedProducts : Product[0..*];
	}
	class Product {
		feature inCart: ShoppingCart[0..1];
	}
	
	assoc ProductSelection {
		feature info: SelectionInfo[1];
		
		end feature cart: ShoppingCart[1] crosses selectedProduct.inCart;
		end feature selectedProduct: Product[1] crosses cart.selectedProducts;
	}
	
	assoc SingleProductSelection :> ProductSelection {
		end feature cart: ShoppingCart[1];
		end [0..1] feature selectedProduct: Product[1];
	}
	
	// Equivalent association showing implied relationships explicitly.
	assoc SingleProductSelection1 :> ProductSelection {
		end feature cart: ShoppingCart[1] redefines cart {
			public import selectedProduct::selectedProduct1;
		}
		end feature selectedProduct: Product[1] redefines selectedProduct crosses cart.selectedProduct1 {
			member feature selectedProduct1[0..1] subsets ShoppingCart::selectedProducts featured by ShoppingCart;
		}
	}
	
	class OnlineCustomer {
		feature info1: SelectionInfo;	
		feature myCart: ShoppingCart[1];	
		feature products: Product[0..*];
		
		connector ps1 : ProductSelection from myCart to products {
			:>> info = info1;
		}
		
		connector ps2 : ProductSelection from [1] myCart to [1] products {
			:>> info = info1;
		}
	}
	
}
````
