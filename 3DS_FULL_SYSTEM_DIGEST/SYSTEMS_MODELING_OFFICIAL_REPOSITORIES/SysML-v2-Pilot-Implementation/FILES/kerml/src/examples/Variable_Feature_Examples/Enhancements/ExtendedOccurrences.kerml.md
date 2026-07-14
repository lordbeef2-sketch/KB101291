# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Variable Feature Examples/Enhancements/ExtendedOccurrences.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Variable Feature Examples/Enhancements/ExtendedOccurrences.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Variable Feature Examples/Enhancements/ExtendedOccurrences.kerml
- source_bytes: 2076
- source_sha256: `0ee38dc5959b592636fbdcfc7a14496526250bd3207f9ff43e068e721f05c283`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package ExtendedOccurrences {
    class Interval;
    class Moment :> Interval;
    class Timeslice {
        feature interval : Interval;
        :>> self : Timeslice;
    }
    class Snapshot :> Timeslice {
        feature moment :>> interval : Moment;
        :>> self : Snapshot;
    }
    class Life :> Timeslice;
    class ExtendedOccurrence :> Life {
        :>> timeSlices : Timeslice [1..*];
        :>> snapshots :> timeSlices : Snapshot [1..*];
        expr at {
        	:>> that : Timeslice;
            in interval : Interval;
            return result : Timeslice;

            binding result.portionOf = that;
            binding result.interval = interval;
        }

        expr while {
            in timeslice : Timeslice;
            return result : Timeslice = at(timeslice.interval);
        }
        
        var feature activeOccurrences :> Occurrences::occurrences {
        	connector : Occurrences::HappensDuring from [1] that to [1] self;
        }
        
        var feature activeSuboccurrences :> Occurrences::occurrences {
        	connector : Occurrences::HappensDuring from [1] that to [1] self;
        }
        
        // occurrences and performances are abstract package-level features.
        // It would be nice to put the variable next to them, but they cannot 
        // be package-level, or featured by Anything. Nevertheless, since
        // Occurrence is a specialization of Anything, it will have these 
        // features (might be worth redefining them explicitly), so the
        // variables can subset them. In the case below, performances will
        // contain every step in the occurrence, which is the correct domain
        // for the variable.
        var feature activePerformances :> Performances::performances {
        	connector : Occurrences::HappensDuring from [1] that to [1] self;
        }
    }
    struct ExtendedObject :> ExtendedOccurrence {
        feature self : ExtendedObject :>> Objects::Object::self, ExtendedOccurrence::self;
    }

}
````
