# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/validation/15-Properties-Values-Expressions/15_08-Range Restriction.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/validation/15-Properties-Values-Expressions/15_08-Range Restriction.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/validation/15-Properties-Values-Expressions/15_08-Range Restriction.sysml
- source_bytes: 555
- source_sha256: `2239e863f011055195507c9220bdb38988a7b935f9e30b0afde3d23136b525a0`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '15_08-Range Restriction' {
	private import ISQ::*;
	private import SI::*;
	private import '15_01-Constants'::'Mathematical Constants'::pi;
	
	part def HeadLightsTiltKnob {
		attribute headLightsTile : LightBeamTiltAngleValue[1];
	}
	
	attribute def LightBeamTiltAngleValue :> PlaneAngleValue {
		attribute angle: LightBeamTiltAngleValue :>> self {
			doc
			/*
			 * Tilt angle shall be limited to the range between 50 and 80 degrees (inclusive).
			 */
		}
		assert constraint { angle >= 50 ['°'] and angle <= 80 ['°'] }
	}
}
````
