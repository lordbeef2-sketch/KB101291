# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/06. Enumeration Definitions/Enumeration Definitions-1.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/06. Enumeration Definitions/Enumeration Definitions-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/06. Enumeration Definitions/Enumeration Definitions-1.sysml
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
