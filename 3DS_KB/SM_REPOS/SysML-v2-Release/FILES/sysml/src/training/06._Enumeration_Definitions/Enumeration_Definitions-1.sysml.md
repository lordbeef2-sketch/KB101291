# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/06. Enumeration Definitions/Enumeration Definitions-1.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/06. Enumeration Definitions/Enumeration Definitions-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/06. Enumeration Definitions/Enumeration Definitions-1.sysml
- source_bytes: 363
- source_sha256: `059e3935ce1916811646901df80b492f18992198b88efbe4980c25d8c62ce84a`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Enumeration Definitions-1' {
	private import ScalarValues::Real;
	
	enum def TrafficLightColor {
		enum green;
		enum yellow;
		enum red;
	}
	
	part def TrafficLight {
		attribute currentColor : TrafficLightColor;
	}
	
	part def TrafficLightGo specializes TrafficLight {
		attribute redefines currentColor = TrafficLightColor::green;
	}
}
````
