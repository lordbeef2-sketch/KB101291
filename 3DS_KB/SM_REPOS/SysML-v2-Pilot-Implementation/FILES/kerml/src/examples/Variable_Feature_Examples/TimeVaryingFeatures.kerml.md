# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Variable Feature Examples/TimeVaryingFeatures.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Variable Feature Examples/TimeVaryingFeatures.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Variable Feature Examples/TimeVaryingFeatures.kerml
- source_bytes: 2705
- source_sha256: `8f91104b332d5d1baa4f02a574646d8792fe55c80685d292d5376120ea45dda4`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package TimeVaryingFeatures {
    class CC0 {
        var feature x;
        
        portion :>> startShot {
            var feature :>> x = 0;
        }
        
        portion t :> timeSlices {
            var feature y;
            
            portion :>> startShot {
                var feature :>> x = 0; 
                var feature :>> y = 1;
            }
            
            portion t1 :> timeSlices {
                portion :>> startShot {
                    var feature :>> x = 2;
                    var feature :>> y = 3;
                }
            }
        }
    }
    
    class CC1 {
        // var feature x;
        member feature x featured by CC1_snapshots {
            member feature CC1_snapshots :>> Occurrences::Occurrence::snapshots featured by CC1;
        }
        
        // portions are not variable
        portion :>> startShot {
            // var feature :>> x = 0;
            member feature :>> CC1::x featured by CC1_startShot_snapshots = 0 {
                member feature CC1_startShot_snapshots :>> CC1_snapshots featured by CC1::startShot;
            }
        }
        
        portion t :> timeSlices {
            // var feature y;
            member feature y featured by CC1_t_snapshots {
                member feature CC1_t_snapshots :>> Occurrences::Occurrence::snapshots featured by CC1::t;
            }
            portion :>> startShot {
                // var feature :>> x = 0;
                member feature :>> CC1::x featured by CC1_t_startShot_snapshots = 0 {
                    member feature CC1_t_startShot_snapshots :>> CC1_snapshots featured by CC1::t::startShot;
                }
                // var feature :>> y = 1;
                member feature :>> CC1::t::y featured by CC1_t_startShot_snapshots = 1 {
                    member feature CC1_t_startShot_snapshots :>> CC1_t_snapshots featured by CC1::t::startShot;
                }
            }
            portion t1 :> timeSlices {
                portion :>> startShot {
                    // var feature :>> x = 2;
                    member feature :>> CC1::x featured by CC1_t_t1_startShot_snapshots = 2 {
                        member feature CC1_t_t1_startShot_snapshots :>> CC1_snapshots featured by CC1::t::t1::startShot;
                    }
                    // var feature :>> y = 3;
                    member feature :>> CC1::t::y featured by CC1_t_t1_startShot_snapshots = 3 {
                        member feature CC1_t_t1_startShot_snapshots :>> CC1_t_snapshots featured by CC1::t::t1::startShot;
                    }
                }
            }
        }
    }
}
````
