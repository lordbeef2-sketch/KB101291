# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Simple Tests/FeatureChains.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Simple Tests/FeatureChains.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Simple Tests/FeatureChains.kerml
- source_bytes: 585
- source_sha256: `5991e72e76d2f3d01fadd3c2d959d03c1d568756a562f9df3f219c4645661659`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package FeatureChains {
	classifier F {
		feature a : A;
	}
	  
	feature f : F;
	  
	classifier A {
		feature g = f.a;
	}
	  
	classifier B {
	  	feature f : F;
	  	feature a : A;
	}
	  
	feature b : B {
	  	connector f.a to a.g;
	  	binding f.a = a.g;
	}
	  
	feature g subsets f.a;
	subset g.g subsets b.f.a;
	redefinition b.f redefines b.a;
	  
	subtype g.g specializes b.f.a;
	
	disjoint b.f.a from b.a;
	
	feature h1 unions f, b.f, b.a;
	feature h2 differences b.f, b.a intersects f.a, g disjoint from h1;
	
	feature b_f_a chains b chains f.a;
}

````
