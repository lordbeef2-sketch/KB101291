# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/library.domain/Quantities and Units/SI.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/library.domain/Quantities and Units/SI.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/library.domain/Quantities and Units/SI.sysml
- source_bytes: 31302
- source_sha256: `c6af4b72d6d098b7655f737ee162e7bae58089e8bcf7b9209e71041707c1e4e0`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package SI {
	doc
	/*
	 * International System of (Measurement) Units -- Système International d'Unités (SI), as defined in ISO/IEC 80000
	 *
	 * Note 1: In accordance with ISO/IEC 80000 en-GB spelling is used for the names and definitions of the units.
	 * Note 2: This is a representative but not yet complete list of measurement units.
	 */

    private import MeasurementReferences::*;
    public import ISQ::*;
    public import SIPrefixes::*;

    /*
     * SI simple unit needed in support of creation of the base units
     */
    attribute <g> gram : MassUnit;

    /*
     * SI base units
     */
    attribute <m> metre : LengthUnit;
    attribute <kg> kilogram : MassUnit { :>> unitConversion: ConversionByPrefix { :>> prefix = kilo; :>> referenceUnit = g; } }
    attribute <s> second : DurationUnit;
    attribute <A> ampere : ElectricCurrentUnit;
    attribute <K> kelvin : ThermodynamicTemperatureUnit, TemperatureDifferenceUnit {
        attribute temperatureOfWaterAtTriplePointInK: DefinitionalQuantityValue {
            :>> num = 27316/100;
            :>> definition = "temperature in kelvin of pure water at the triple point";
        }
        attribute :>> definitionalQuantityValues = temperatureOfWaterAtTriplePointInK;
        attribute :>> ThermodynamicTemperatureUnit::quantityDimension, TemperatureDifferenceUnit::quantityDimension {
            :>> ThermodynamicTemperatureUnit::quantityDimension::quantityPowerFactors, TemperatureDifferenceUnit::quantityDimension::quantityPowerFactors;
        }
    }
    attribute <mol> mole : AmountOfSubstanceUnit;
    attribute <cd> candela : LuminousIntensityUnit;

    /*
     * Declare the SI system of units with its explicit base units
     * and its associated system of quantities, the ISQ.
     */
	attribute <si> 'ISO/IEC 80000 International System of Units' : SystemOfUnits {
		:>> systemOfQuantities = isq;
		:>> baseUnits = (m, kg, s, A, K, mol, cd);
	}

    /*
     * Units with special names
     */
    attribute <B> byte : StorageCapacityUnit = one;
    attribute <Bd> baud : ModulationRateUnit = s^-1;
    attribute <bit> bit : StorageCapacityUnit = one;
    attribute <Bq> becquerel : NuclearActivityUnit = s^-1;
    attribute <C> coulomb : ElectricChargeUnit = A*s;
    attribute <dB> decibel : SoundPressureLevelUnit = one;
    attribute <dec> decade : LogarithmicFrequencyRangeUnit = one;
    attribute <E> erlang : TrafficIntensityUnit = one;
    attribute <F> farad : CapacitanceUnit = C/V;
    attribute <Gy> gray : AbsorbedDoseUnit = J/kg;
    attribute <H> henry : PermeanceUnit, InductanceUnit = Wb/A {
        attribute :>> PermeanceUnit::quantityDimension, InductanceUnit::quantityDimension {
            :>> PermeanceUnit::quantityDimension::quantityPowerFactors, InductanceUnit::quantityDimension::quantityPowerFactors;
        }
    }
    attribute <Hart> hartley : InformationContentUnit = one;
    attribute <Hz> hertz : FrequencyUnit = s^-1;
    attribute <J> joule : EnergyUnit = N*m;
    //attribute <kat> katal : CatalyticActivityUnit = mol/s;
    attribute <lm> lumen : LuminousFluxUnit = cd*sr;
    attribute <lx> lux : IlluminanceUnit = lm/m^2;
    attribute <N> newton : ForceUnit = kg*m/s^2;
    attribute <nat> 'natural unit of information' : InformationContentUnit = one;
    attribute <o> octet : StorageCapacityUnit = one;
    attribute <oct> octave : LogarithmicFrequencyRangeUnit = one;
    attribute <Pa> pascal : PressureUnit = N/m^2;
    attribute <rad> radian : AngularMeasureUnit = m/m;
    attribute <S> siemens : ConductanceUnit = 'Ω'^-1;
    attribute <Sh> shannon : InformationContentUnit = one;
    attribute <sr> steradian : SolidAngularMeasureUnit = m^2/m^2;
    attribute <Sv> sievert : DoseEquivalentUnit = J/kg;
    attribute <T> tesla : MagneticFluxDensityUnit = Wb/m^2;
    attribute <V> volt : ElectricPotentialUnit = W/A;
    attribute <W> watt : PowerUnit = J/s;
    attribute <Wb> weber : MagneticFluxUnit = V*s;
    attribute <'Ω'> ohm : ResistanceUnit = V/A;

    /*
     * Units recognized in SI as specified in ISO 80000-1:2009
     */
    attribute <'Å'> 'ångström' : LengthUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = m; :>> conversionFactor = 1.0e-10; } }
    attribute <b> barn : AreaUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = 'm²'; :>> conversionFactor = 1.0e-28; } }
    attribute <d> day: DurationUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = hour; :>> conversionFactor = 24; } }
    attribute <Da> dalton : MassUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = kg; :>> conversionFactor = 1.66053906660e-27; :>> isExact = false; } }
    attribute <eV> electronvolt : EnergyUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = J; :>> conversionFactor = 1.602176487e-19; :>> isExact = false; } }
    attribute <h> hour: DurationUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = min; :>> conversionFactor = 60; } }
    attribute <min> minute : DurationUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = s; :>> conversionFactor = 60; } }
    attribute <L> litre : VolumeUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = 'm³'; :>> conversionFactor = 1.0e-3; } }
    attribute tonne : MassUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = kg; :>> conversionFactor = 1.0e-3; } }
    alias 'metric ton' for tonne;
    attribute <u> 'atomic mass unit' : MassUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = Da; :>> conversionFactor = 1.0; } }
    attribute <ua> 'astronomical unit' : LengthUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = m; :>> conversionFactor = 149597870691e11; :>> isExact = false; } }
    attribute <var> 'volt ampere reactive' : PowerUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = V*A; :>> conversionFactor = 1.0; } }
    attribute <'°'> degree : AngularMeasureUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = rad; :>> conversionFactor = 1.745329E-02; :>> isExact = false; } } // conversionFactor should become pi/180
    attribute <'′'> 'minute (angle)' : AngularMeasureUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = rad; :>> conversionFactor = 2.908882E-04; :>> isExact = false; } }
    alias arcmin for '′';
    attribute <'″'> 'second (angle)' : AngularMeasureUnit { :>> unitConversion: ConversionByConvention { :>> referenceUnit = rad; :>> conversionFactor = 4.848137E-06; :>> isExact = false; } }
    alias arcsec for '″';

    /*
     * Derived units used in parts 3 to 12 of ISO/IEC 80000
     */
    attribute <'A⋅m⁻²⋅K⁻²'> 'ampere metre to the power minus 2 kelvin to the power minus 2' : RichardsonConstantUnit = A*m^-2*K^-2;
    attribute <'A⋅m²'> 'ampere metre squared' : MagneticMomentUnit = A*m^2;
    attribute <'A⋅m²⋅J⁻¹⋅s⁻¹'> 'ampere metre squared joule to the power minus 1 second to the power minus 1' : GyromagneticRatioUnit = A*m^2*J^-1*s^-1;
    attribute <'A⋅s/kg'> 'ampere second per kilogram' : GyromagneticRatioUnit = A*s/kg;
    attribute <'A/m'> 'ampere per metre' : LinearElectricCurrentDensityUnit = A/m;
    attribute <'A/m²'> 'ampere per square metre' : ElectricCurrentDensityUnit = A/m^2;
    attribute <'B/s'> 'byte per second' : TransferRateUnit = B/s;
    attribute <'bit/s'> 'bit per second' : BinaryDigitRateUnit = bit/s;
    attribute <'Bq/kg'> 'becquerel per kilogram' : SpecificActivityUnit = Bq/kg;
    attribute <'Bq/m²'> 'becquerel per square metre' : SurfaceActivityDensityUnit = Bq/m^2;
    attribute <'Bq/m³'> 'becquerel per cubic metre' : ActivityDensityUnit = Bq/m^3;
    attribute <'C⋅m'> 'coulomb metre' : ElectricDipoleMomentUnit = C*m;
    attribute <'C/(kg⋅s)'> 'coulomb per kilogram second' : ExposureRateUnit = C/(kg*s);
    attribute <'C/kg'> 'coulomb per kilogram' : ExposureUnit = C/kg;
    attribute <'C/m'> 'coulomb per metre' : LinearDensityOfElectricChargeUnit = C/m;
    attribute <'C/m²'> 'coulomb per square metre' : SurfaceDensityOfElectricChargeUnit = C/m^2;
    attribute <'C/m³'> 'coulomb per cubic metre' : ElectricChargeDensityUnit = C/m^3;
    attribute <'cd⋅m⁻²'> 'candela metre to the power minus 2' : LuminanceUnit = cd*m^-2;
    attribute <'cd⋅sr'> 'candela steradian' : LuminousFluxUnit = cd*sr;
    attribute <'cd⋅sr⋅kg⁻¹⋅m⁻²⋅s³'> 'candela steradian kilogram to the power minus 1 metre to the power minus 2 second to the power 3' : LuminousEfficacyOfRadiationUnit = cd*sr*kg^-1*m^-2*s^3;
    attribute <'cd⋅sr⋅m⁻²'> 'candela steradian metre to the power minus 2' : IlluminanceUnit = cd*sr*m^-2;
    attribute <'cd⋅sr⋅m⁻²⋅s'> 'candela steradian metre to the power minus 2 second' : LuminousExposureUnit = cd*sr*m^-2*s;
    attribute <'cd⋅sr⋅s'> 'candela steradian second' : LuminousEnergyUnit = cd*sr*s;
    attribute <'eV⋅J⋅kg⋅m²⋅s⁻²'> 'electronvolt joule kilogram metre squared second to the power minus 2' : HartreeEnergyUnit = eV*J*kg*m^2*s^-2;
    attribute <'eV⋅m⁻²/kg'> 'electronvolt metre to the power minus 2 per kilogram' : TotalMassStoppingPowerUnit = eV*m^-2/kg;
    attribute <'eV/m'> 'electronvolt per metre' : TotalLinearStoppingPowerUnit = eV/m;
    attribute <'eV/m²'> 'electronvolt per square metre' : EnergyFluenceUnit = eV/m^2;
    attribute <'F/m'> 'farad per metre' : ElectricConstantUnit = F/m;
    attribute <'g/L'> 'g per l' : MassConcentrationUnit = g/L;
    attribute <'g/mol'> 'g per mole' : MolarMassUnit = g/mol;
    attribute <'Gy/s'> 'gray per second' : AbsorbedDoseRateUnit = Gy/s;
    attribute <'H/m'> 'henry per metre' : MagneticConstantUnit = H/m;
    attribute <'H⁻¹'> 'henry to the power minus 1' : ReluctanceUnit = H^-1;
    attribute <'Hart/s'> 'hartley per second' : AverageInformationRateUnit = Hart/s;
    attribute <'J⋅m²/kg'> 'joule metre squared per kilogram' : TotalMassStoppingPowerUnit = J*m^2/kg;
    attribute <'J⋅s'> 'joule second' : ActionQuantityUnit = J*s;
    attribute <'J⋅s⋅eV⋅s'> 'joule second electronvolt second' : TotalAngularMomentumUnit = J*s*eV*s;
    attribute <'J⋅s⁻¹'> 'joule second to the power minus 1' : PowerUnit = J*s^-1;
    attribute <'J/(kg⋅K)'> 'joule per kilogram kelvin' : SpecificHeatCapacityUnit = J/(kg*K);
    attribute <'J/(m²⋅nm)'> 'joule per square metre nm' : SpectralRadiantExposureUnit = J/(m^2*nm);
    attribute <'J/(m³⋅nm)'> 'joule per cubic metre nm' : SpectralRadiantEnergyDensityInTermsOfWavelengthUnit = J/(m^3*nm);
    attribute <'J/(mol⋅K)'> 'joule per mole kelvin' : MolarHeatCapacityUnit = J/(mol*K);
    attribute <'J/K'> 'joule per kelvin' : HeatCapacityUnit = J/K;
    attribute <'J/kg'> 'joule per kilogram' : SpecificEnergyUnit = J/kg;
    attribute <'J/m'> 'joule per metre' : TotalLinearStoppingPowerUnit = J/m;
    attribute <'J/m²'> 'joule per square metre' : SpectralRadiantEnergyDensityInTermsOfWavenumberUnit = J/m^2;
    attribute <'J/m³'> 'joule per cubic metre' : ElectromagneticEnergyDensityUnit = J/m^3;
    attribute <'J/mol'> 'joule per mole' : MolarInternalEnergyUnit = J/mol;
    attribute <'J/nm'> 'joule per nm' : SpectralRadiantEnergyUnit = J/nm;
    attribute <'J/s'> 'joule per second' : HeatFlowRateUnit = J/s;
    attribute <'J⁻¹⋅m⁻³⋅eV⁻¹⋅m⁻³'> 'joule to the power minus 1 metre to the power minus 3 electronvolt to the power minus 1 metre to the power minus 3' : EnergyDensityOfStatesUnit = J^-1*m^-3*eV^-1*m^-3;
    attribute <'K/Pa'> 'kelvin per pascal' : JouleThomsonCoefficientUnit = K/Pa;
    attribute <'K/W'> 'kelvin per watt' : ThermalResistanceUnit = K/W;
    attribute <'K⁻¹'> 'kelvin to the power minus 1' : LinearExpansionCoefficientUnit = K^-1;
    attribute <'kg⋅m⋅s⁻¹'> 'kilogram metre second to the power minus 1' : MomentumUnit = kg*m*s^-1;
    attribute <'kg⋅m⋅s⁻²'> 'kilogram metre second to the power minus 2' : ForceUnit = kg*m*s^-2;
    attribute <'kg⋅m⋅s⁻³'> 'kilogram metre second to the power minus 3' : SpectralRadiantFluxUnit = kg*m*s^-3;
    attribute <'kg⋅m⋅s⁻³⋅K⁻¹'> 'kilogram metre second to the power minus 3 kelvin to the power minus 1' : ThermalConductivityUnit = kg*m*s^-3*K^-1;
    attribute <'kg⋅m⋅s⁻³⋅sr⁻¹'> 'kilogram metre second to the power minus 3 steradian to the power minus 1' : SpectralRadiantIntensityUnit = kg*m*s^-3*sr^-1;
    attribute <'kg⋅m⁻¹'> 'kilogram metre to the power minus 1' : LinearMassDensityUnit = kg*m^-1;
    attribute <'kg⋅m⁻¹⋅s⁻¹'> 'kilogram metre to the power minus 1 second to the power minus 1' : DynamicViscosityUnit = kg*m^-1*s^-1;
    attribute <'kg⋅m⁻¹⋅s⁻²'> 'kilogram metre to the power minus 1 second to the power minus 2' : PressureUnit = kg*m^-1*s^-2;
    attribute <'kg⋅m⁻¹⋅s⁻²⋅K⁻¹'> 'kilogram metre to the power minus 1 second to the power minus 2 kelvin to the power minus 1' : PressureCoefficientUnit = kg*m^-1*s^-2*K^-1;
    attribute <'kg⋅m⁻¹⋅s⁻³'> 'kilogram metre to the power minus 1 second to the power minus 3' : SpectralIrradianceUnit = kg*m^-1*s^-3;
    attribute <'kg⋅m⁻¹⋅s⁻³⋅sr⁻¹'> 'kilogram metre to the power minus 1 second to the power minus 3 steradian to the power minus 1' : SpectralRadianceUnit = kg*m^-1*s^-3*sr^-1;
    attribute <'kg⋅m⁻²'> 'kilogram metre to the power minus 2' : SurfaceMassDensityUnit = kg*m^-2;
    attribute <'kg⋅m⁻²⋅s⁻¹'> 'kilogram metre to the power minus 2 second to the power minus 1' : MassFlowUnit = kg*m^-2*s^-1;
    attribute <'kg⋅m⁻²⋅s⁻²'> 'kilogram metre to the power minus 2 second to the power minus 2' : SpectralRadiantEnergyDensityInTermsOfWavelengthUnit = kg*m^-2*s^-2;
    attribute <'kg⋅m⁻³'> 'kilogram metre to the power minus 3' : MassDensityUnit = kg*m^-3;
    attribute <'kg⋅m⁻⁴⋅s⁻¹'> 'kilogram metre to the power minus 4 second to the power minus 1' : AcousticImpedanceUnit = kg*m^-4*s^-1;
    attribute <'kg⋅m²'> 'kilogram metre squared' : MomentOfInertiaUnit = kg*m^2;
    attribute <'kg⋅m²⋅s⁻¹'> 'kilogram metre squared second to the power minus 1' : AngularMomentumUnit = kg*m^2*s^-1;
    attribute <'kg⋅m²⋅s⁻²'> 'kilogram metre squared second to the power minus 2' : MomentOfForceUnit = kg*m^2*s^-2;
    attribute <'kg⋅m²⋅s⁻²⋅K⁻¹'> 'kilogram metre squared second to the power minus 2 kelvin to the power minus 1' : HeatCapacityUnit = kg*m^2*s^-2*K^-1;
    attribute <'kg⋅m²⋅s⁻²⋅K⁻¹⋅mol⁻¹'> 'kilogram metre squared second to the power minus 2 kelvin to the power minus 1 mole to the power minus 1' : MolarHeatCapacityUnit = kg*m^2*s^-2*K^-1*mol^-1;
    attribute <'kg⋅m²⋅s⁻²⋅mol⁻¹'> 'kilogram metre squared second to the power minus 2 mole to the power minus 1' : MolarInternalEnergyUnit = kg*m^2*s^-2*mol^-1;
    attribute <'kg⋅m²⋅s⁻³'> 'kilogram metre squared second to the power minus 3' : PowerUnit = kg*m^2*s^-3;
    attribute <'kg⋅m²⋅s⁻³⋅A⁻¹'> 'kilogram metre squared second to the power minus 3 ampere to the power minus 1' : ElectricPotentialDifferenceUnit = kg*m^2*s^-3*A^-1;
    attribute <'kg⋅m²⋅s⁻³⋅A⁻¹⋅K⁻¹'> 'kilogram metre squared second to the power minus 3 ampere to the power minus 1 kelvin to the power minus 1' : SeebeckCoefficientForSubstancesAAndBUnit = kg*m^2*s^-3*A^-1*K^-1;
    attribute <'kg⋅m²⋅s⁻³⋅K⁻¹'> 'kilogram metre squared second to the power minus 3 kelvin to the power minus 1' : ThermalConductanceUnit = kg*m^2*s^-3*K^-1;
    attribute <'kg⋅m²⋅s⁻³⋅sr⁻¹'> 'kilogram metre squared second to the power minus 3 steradian to the power minus 1' : RadiantIntensityUnit = kg*m^2*s^-3*sr^-1;
    attribute <'kg⋅m³⋅s⁻³⋅A⁻²'> 'kilogram metre cubed second to the power minus 3 ampere to the power minus 2' : ResistivityUnit = kg*m^3*s^-3*A^-2;
    attribute <'kg⋅mol⁻¹'> 'kilogram mole to the power minus 1' : MolarMassUnit = kg*mol^-1;
    attribute <'kg⋅s⁻¹'> 'kilogram second to the power minus 1' : MassFlowRateUnit = kg*s^-1;
    attribute <'kg⋅s⁻²'> 'kilogram second to the power minus 2' : SurfaceTensionUnit = kg*s^-2;
    attribute <'kg⋅s⁻²⋅A⁻¹'> 'kilogram second to the power minus 2 ampere to the power minus 1' : MagneticFluxDensityUnit = kg*s^-2*A^-1;
    attribute <'kg⋅s⁻³'> 'kilogram second to the power minus 3' : DensityOfHeatFlowRateUnit = kg*s^-3;
    attribute <'kg⋅s⁻³⋅K⁻¹'> 'kilogram second to the power minus 3 kelvin to the power minus 1' : CoefficientOfHeatTransferUnit = kg*s^-3*K^-1;
    attribute <'kg⋅s⁻³⋅sr⁻¹'> 'kilogram second to the power minus 3 steradian to the power minus 1' : RadianceUnit = kg*s^-3*sr^-1;
    attribute <'kg⁻¹⋅A'> 'kilogram to the power minus 1 ampere' : ExposureRateUnit = kg^-1*A;
    attribute <'kg⁻¹⋅m⋅s²'> 'kilogram to the power minus 1 metre second to the power 2' : CompressibilityUnit = kg^-1*m*s^2;
    attribute <'kg⁻¹⋅m⋅s²⋅K'> 'kilogram to the power minus 1 metre second to the power 2 kelvin' : JouleThomsonCoefficientUnit = kg^-1*m*s^2*K;
    attribute <'kg⁻¹⋅m⁻²⋅s³⋅K'> 'kilogram to the power minus 1 metre to the power minus 2 second to the power 3 kelvin' : ThermalResistanceUnit = kg^-1*m^-2*s^3*K;
    attribute <'kg⁻¹⋅m⁻³⋅s³⋅A²'> 'kilogram to the power minus 1 metre to the power minus 3 second to the power 3 ampere to the power 2' : ElectrolyticConductivityUnit = kg^-1*m^-3*s^3*A^2;
    attribute <'kg⁻¹⋅m⁻⁵⋅s²'> 'kilogram to the power minus 1 metre to the power minus 5 second to the power 2' : EnergyDensityOfStatesUnit = kg^-1*m^-5*s^2;
    attribute <'kg⁻¹⋅m²'> 'kilogram to the power minus 1 metre squared' : MassAttenuationCoefficientUnit = kg^-1*m^2;
    attribute <'kg⁻¹⋅m³'> 'kilogram to the power minus 1 metre cubed' : SpecificVolumeUnit = kg^-1*m^3;
    attribute <'kg⁻¹⋅s⋅A'> 'kilogram to the power minus 1 second ampere' : GyromagneticRatioUnit = kg^-1*s*A;
    attribute <'kg⁻¹⋅s⁻¹'> 'kilogram to the power minus 1 second to the power minus 1' : SpecificActivityUnit = kg^-1*s^-1;
    attribute <'kg⁻¹⋅s²'> 'kilogram to the power minus 1 second to the power 2' : EnergyDistributionOfCrossSectionUnit = kg^-1*s^2;
    attribute <'kg⁻¹⋅s²⋅A'> 'kilogram to the power minus 1 second to the power 2 ampere' : MobilityUnit = kg^-1*s^2*A;
    attribute <'kg⁻¹⋅s³⋅A²⋅mol⁻¹'> 'kilogram to the power minus 1 second to the power 3 ampere to the power 2 mole to the power minus 1' : MolarConductivityUnit = kg^-1*s^3*A^2*mol^-1;
    attribute <'kg⁻¹⋅s³⋅K'> 'kilogram to the power minus 1 second to the power 3 kelvin' : ThermalInsulanceUnit = kg^-1*s^3*K;
    attribute <'kg²⋅m⁻²⋅s⁻³'> 'kilogram to the power 2 metre to the power minus 2 second to the power minus 3' : SoundExposureUnit = kg^2*m^-2*s^-3;
    attribute <'kg²⋅m⁴⋅s⁻⁶⋅A⁻²⋅K⁻²'> 'kilogram to the power 2 metre to the power 4 second to the power minus 6 ampere to the power minus 2 kelvin to the power minus 2' : LorenzCoefficientUnit = kg^2*m^4*s^-6*A^-2*K^-2;
    attribute <'lm⋅s'> 'lumen second' : LuminousEnergyUnit = lm*s;
    attribute <'lm/m²'> 'lumen per square metre' : LuminousExitanceUnit = lm/m^2;
    attribute <'lm/W'> 'lumen per watt' : LuminousEfficacyOfRadiationUnit = lm/W;
    attribute <'lx⋅s'> 'lux second' : LuminousExposureUnit = lx*s;
    attribute <'m⋅s⁻¹'> 'metre second to the power minus 1' : SpeedUnit = m*s^-1;
    attribute <'m⋅s⁻²'> 'metre second to the power minus 2' : AccelerationUnit = m*s^-2;
    attribute <'m/s'> 'metre per second' : SpeedUnit = m/s;
    attribute <'m⁻¹'> 'metre to the power minus 1' : CurvatureUnit = m^-1;
    attribute <'m⁻²'> 'metre to the power minus 2' : PhotonExposureUnit = m^-2;
    attribute <'m⁻²⋅s⁻¹'> 'metre to the power minus 2 second to the power minus 1' : PhotonIrradianceUnit = m^-2*s^-1;
    attribute <'m⁻²⋅s⁻¹⋅sr⁻¹'> 'metre to the power minus 2 second to the power minus 1 steradian to the power minus 1' : PhotonRadianceUnit = m^-2*s^-1*sr^-1;
    attribute <'m⁻³'> 'metre to the power minus 3' : ParticleConcentrationUnit = m^-3;
    attribute <'m⁻³⋅s'> 'metre to the power minus 3 second' : DensityOfVibrationalStatesUnit = m^-3*s;
    attribute <'m⁻³⋅s⁻¹'> 'metre to the power minus 3 second to the power minus 1' : ActivityDensityUnit = m^-3*s^-1;
    attribute <'m²'> 'metre squared' : AreaUnit = m^2;
    attribute <'m²⋅A'> 'metre squared ampere' : MagneticDipoleMomentUnit = m^2*A;
    attribute <'m²⋅K/W'> 'metre squared kelvin per watt' : ThermalInsulanceUnit = m^2*K/W;
    attribute <'m²⋅mol⁻¹'> 'metre squared mole to the power minus 1' : MolarAbsorptionCoefficientUnit = m^2*mol^-1;
    attribute <'m²⋅s⁻¹'> 'metre squared second to the power minus 1' : KinematicViscosityUnit = m^2*s^-1;
    attribute <'m²⋅s⁻²'> 'metre squared second to the power minus 2' : SpecificEnergyUnit = m^2*s^-2;
    attribute <'m²⋅s⁻²⋅K⁻¹'> 'metre squared second to the power minus 2 kelvin to the power minus 1' : SpecificHeatCapacityUnit = m^2*s^-2*K^-1;
    attribute <'m²⋅s⁻³'> 'metre squared second to the power minus 3' : DoseEquivalentUnit = m^2*s^-3;
    attribute <'m²⋅sr⁻¹'> 'metre squared steradian to the power minus 1' : DirectionDistributionOfCrossSectionUnit = m^2*sr^-1;
    attribute <'m²/(J⋅sr)'> 'metre squared per joule steradian' : DirectionAndEnergyDistributionOfCrossSectionUnit = m^2/(J*sr);
    attribute <'m²/(V⋅s)'> 'metre squared per volt second' : MobilityUnit = m^2/(V*s);
    attribute <'m²/J'> 'metre squared per joule' : EnergyDistributionOfCrossSectionUnit = m^2/J;
    attribute <'m³'> 'metre cubed' : VolumeUnit = m^3;
    attribute <'m³⋅mol⁻¹'> 'metre cubed mole to the power minus 1' : MolarVolumeUnit = m^3*mol^-1;
    attribute <'m³⋅s⁻¹'> 'metre cubed second to the power minus 1' : VolumeFlowRateUnit = m^3*s^-1;
    attribute <'m³/C⋅m³⋅s⁻¹⋅A⁻¹'> 'metre cubed per coulomb cubic metre second to the power minus 1 ampere to the power minus 1' : HallCoefficientUnit = m^3/C*m^3*s^-1*A^-1;
    attribute <'m⁴'> 'metre to the power 4' : SecondAxialMomentOfAreaUnit = m^4;
    attribute <'m⁴⋅s⁻²'> 'metre to the power 4 second to the power minus 2' : TotalMassStoppingPowerUnit = m^4*s^-2;
    attribute <'mL/L '> 'ml per l' : VolumeFractionUnit = mL/L;
    attribute <'mol⋅kg⁻¹'> 'mole kilogram to the power minus 1' : IonicStrengthUnit = mol*kg^-1;
    attribute <'mol⋅m⁻³'> 'mole metre to the power minus 3' : AmountOfSubstanceConcentrationUnit = mol*m^-3;
    attribute <'mol/kg'> 'mole per kilogram' : MolalityUnit = mol/kg;
    attribute <'mol/L'> 'mole per l' : AmountOfSubstanceConcentrationUnit = mol/L;
    attribute <'mol/m³'> 'mole per cubic metre' : EquilibriumConstantOnConcentrationBasisUnit = mol/m^3;
    attribute <'N⋅m'> 'newton metre' : MomentOfForceUnit, TorqueUnit = N*m {
        attribute :>> MomentOfForceUnit::quantityDimension, TorqueUnit::quantityDimension {
            :>> MomentOfForceUnit::quantityDimension::quantityPowerFactors, TorqueUnit::quantityDimension::quantityPowerFactors;
        }
    }
    attribute <'N⋅m⋅s'> 'newton metre second' : AngularImpulseUnit = N*m*s;
    attribute <'N⋅m⋅s⁻¹'> 'newton metre second to the power minus 1' : PowerUnit = N*m*s^-1;
    attribute <'N⋅m⁻¹'> 'newton metre to the power minus 1' : SurfaceTensionUnit = N*m^-1;
    attribute <'N⋅m⁻²'> 'newton metre to the power minus 2' : PressureUnit = N*m^-2;
    attribute <'N⋅s'> 'newton second' : ImpulseUnit = N*s;
    attribute <'nat/s'> 'natural unit of information per second' : AverageInformationRateUnit = nat/s;
    attribute <'o/s'> 'octet per second' : TransferRateUnit = o/s;
    attribute <'Pa⋅s'> 'pascal second' : DynamicViscosityUnit = Pa*s;
    attribute <'Pa⋅s/m'> 'pascal second per metre' : CharacteristicImpedanceOfAMediumForLongitudinalWavesUnit = Pa*s/m;
    attribute <'Pa⋅s/m³'> 'pascal second per cubic metre' : AcousticImpedanceUnit = Pa*s/m^3;
    attribute <'Pa/K'> 'pascal per kelvin' : PressureCoefficientUnit = Pa/K;
    attribute <'Pa⁻¹'> 'pascal to the power minus 1' : CompressibilityUnit = Pa^-1;
    attribute <'Pa²⋅s'> 'pascal to the power 2 second' : SoundExposureUnit = Pa^2*s;
    attribute <'rad⋅m²/kg¹'> 'radian metre squared per kilogram to the power 1' : SpecificOpticalRotatoryPowerUnit = rad*m^2/kg^1;
    attribute <'rad⋅m²/mol'> 'radian metre squared per mole' : MolarOpticalRotatoryPowerUnit = rad*m^2/mol;
    attribute <'rad⋅s⁻¹'> 'radian second to the power minus 1' : AngularVelocityUnit = rad*s^-1;
    attribute <'rad⋅s⁻²'> 'radian second to the power minus 2' : AngularAccelerationUnit = rad*s^-2;
    attribute <'rad/m'> 'radian per metre' : PhaseCoefficientUnit = rad/m;
    attribute <'s⋅A'> 'second ampere' : ElectricChargeUnit = s*A;
    attribute <'S⋅m²/mol'> 'siemens metre squared per mole' : MolarConductivityUnit = S*m^2/mol;
    attribute <'S/m'> 'siemens per metre' : ConductivityUnit = S/m;
    attribute <'s⁻¹'> 'second to the power minus 1' : AngularVelocityUnit = s^-1;
    attribute <'s⁻¹⋅sr⁻¹'> 'second to the power minus 1 steradian to the power minus 1' : PhotonIntensityUnit = s^-1*sr^-1;
    attribute <'s⁻²'> 'second to the power minus 2' : AngularAccelerationUnit = s^-2;
    attribute <'Sh/s'> 'shannon per second' : AverageInformationRateUnit = Sh/s;
    attribute <'Sv/s'> 'sievert per second' : DoseEquivalentUnit = Sv/s;
    attribute <'V⋅A'> 'volt ampere' : PowerUnit = V*A;
    attribute <'V/K'> 'volt per kelvin' : SeebeckCoefficientForSubstancesAAndBUnit = V/K;
    attribute <'V/m'> 'volt per metre' : ElectricFieldStrengthUnit = V/m;
    attribute <'V²/K²'> 'volt to the power 2 per kelvin to the power 2' : LorenzCoefficientUnit = V^2/K^2;
    attribute <'W⋅h'> 'watt hour' : EnergyUnit = W*h;
    attribute <'W/(m⋅K)'> 'watt per metre kelvin' : ThermalConductivityUnit = W/(m*K);
    attribute <'W/(m²⋅K)'> 'watt per square metre kelvin' : CoefficientOfHeatTransferUnit = W/(m^2*K);
    attribute <'W/(m²⋅nm)'> 'watt per square metre nm' : SpectralIrradianceUnit = W/(m^2*nm);
    attribute <'W/(sr⋅m²)'> 'watt per steradian square metre' : RadianceUnit = W/(sr*m^2);
    attribute <'W/(sr⋅m²⋅nm)'> 'watt per steradian square metre nm' : SpectralRadianceUnit = W/(sr*m^2*nm);
    attribute <'W/(sr⋅nm)'> 'watt per steradian nm' : SpectralRadiantIntensityUnit = W/(sr*nm);
    attribute <'W/K'> 'watt per kelvin' : ThermalConductanceUnit = W/K;
    attribute <'W/kg'> 'watt per kilogram' : DoseEquivalentUnit = W/kg;
    attribute <'W/m²'> 'watt per square metre' : DensityOfHeatFlowRateUnit = W/m^2;
    attribute <'W/nm'> 'watt per nm' : SpectralRadiantFluxUnit = W/nm;
    attribute <'W/sr'> 'watt per steradian' : RadiantIntensityUnit = W/sr;
    attribute <'Wb⋅m'> 'weber metre' : MagneticDipoleMomentUnit = Wb*m;
    attribute <'Wb/m'> 'weber per metre' : MagneticVectorPotentialUnit = Wb/m;
    attribute <'Ω⋅m'> 'ohm metre' : ResistivityUnit = 'Ω'*m;

    alias 'm/s²' for 'm⋅s⁻²';

    /*
     * Prefixed units
     */

    /* Length */
    attribute <nm> nanometre : LengthUnit { :>> unitConversion: ConversionByPrefix { :>> prefix = nano; :>> referenceUnit = m; } }
    attribute <mm> millimetre : LengthUnit { :>> unitConversion: ConversionByPrefix { :>> prefix = milli; :>> referenceUnit = m; } }
    attribute <cm> centimetre : LengthUnit { :>> unitConversion: ConversionByPrefix { :>> prefix = centi; :>> referenceUnit = m; } }
    attribute <km> kilometre : LengthUnit { :>> unitConversion: ConversionByPrefix { :>> prefix = kilo; :>> referenceUnit = m; } }

    /* Volume */
    attribute <mL> millilitre : VolumeUnit { :>> unitConversion: ConversionByPrefix { :>> prefix = milli; :>> referenceUnit = L; } }

    /* Force */
    attribute <mN> millinewton : ForceUnit { :>> unitConversion: ConversionByPrefix { :>> prefix = milli; :>> referenceUnit = N; } }

    /* Energy */
    attribute <kJ> kilojoule : EnergyUnit { :>> unitConversion: ConversionByPrefix { :>> prefix = kilo; :>> referenceUnit = J; } }
    attribute <MJ> megajoule : EnergyUnit { :>> unitConversion: ConversionByPrefix { :>> prefix = mega; :>> referenceUnit = J; } }
    attribute <GJ> gigajoule : EnergyUnit { :>> unitConversion: ConversionByPrefix { :>> prefix = giga; :>> referenceUnit = J; } }

    /* Power */
    attribute <kW> kilowatt : PowerUnit { :>> unitConversion: ConversionByPrefix { :>> prefix = kilo; :>> referenceUnit = W; } }

    /* Speed */
    attribute <'km/h'> 'kilometre per hour': SpeedUnit = km/h;

	/* 
	 * Celsius units
	 */
	 
    attribute <'°C'> 'degree celsius (temperature difference)' : TemperatureDifferenceUnit {
    	doc
	    /*
	     * degree Celsius unit for temperature interval (i.e. temperature difference) quantities
	     */
	     
        attribute :>> unitConversion: ConversionByConvention { :>> referenceUnit = K; :>> conversionFactor = 1; }
   	}

    attribute <'°C_abs'> 'degree celsius (absolute temperature scale)' : IntervalScale {
    	doc
	     /*
	     * degree Celsius interval scale for absolute (thermodynamic) temperature quantities
	     *
	     * The interval scale is defined with an explicit transformation with respect to 
	     * the kelvin thermodynamic temperature scale that specifies the zero shift.
	     */
 
        attribute :>> unit = '°C';
        attribute temperatureWaterAtFreezingPointInC: DefinitionalQuantityValue {
            :>> num = 0; :>> definition = "temperature in degree Celsius of pure water at freezing point";
        }
        private attribute temperatureWaterAtTriplePointInC: DefinitionalQuantityValue {
            :>> num = 1/100; :>> definition = "temperature in degree Celsius of pure water at the triple point";
        }
        private attribute celsiusToKelvinScaleMapping: QuantityValueMapping {
            :>> mappedQuantityValue = temperatureWaterAtTriplePointInC; 
            :>> referenceQuantityValue = K.temperatureOfWaterAtTriplePointInK;
        }
        attribute :>> definitionalQuantityValues = (temperatureWaterAtTriplePointInC, temperatureWaterAtFreezingPointInC);
        attribute :>> quantityValueMapping = celsiusToKelvinScaleMapping;

        /* CoordinateFramePlacement (zero shift) w.r.t. the kelvin thermodynamic temperature scale */
        private attribute zeroDegreeCelsiusInKelvin: ThermodynamicTemperatureValue = 273.15 [K];
        attribute zeroDegreeCelsiusToKelvinShift : CoordinateFramePlacement :>> transformation { 
        	:>> source = K; :>> origin = zeroDegreeCelsiusInKelvin;
        }
    }
}

````
