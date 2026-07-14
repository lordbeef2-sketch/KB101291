# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/library.systems/Ports.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/library.systems/Ports.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/library.systems/Ports.sysml
- source_bytes: 1647
- source_sha256: `a5d0e567124a734437648c986e71b6a892557711f5643c429d2c7cf4598805be`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package Ports {
    doc
    /*
     * This package defines the base types for ports and related structural elements 
     * in the SysML language.
     */

    private import Objects::Object;
    private import Objects::objects;
    
    abstract port def Port :> Object {
        doc
        /*
         * Port is the most general class of objects that represent connection points
         * for interacting with a Part. Port is the base type of all PortDefinitions.
         * 
         * Transfers outgoing from a Port are always targeted to a Port connected to
         * the original Port by an Interface.
         */
    
        ref self: Port :>> Object::self;
        
        port subports: Port [0..*] :> ports, timeEnclosedOccurrences {
            doc
            /*
             * The Ports that are subports of this Port.
             */
        }
        
        abstract ref port interfacingPorts : Port[0..*] nonunique :> ports {
            doc
            /*
             * Ports that are connected to this Port by an Interface.
             */
        }
        
        ref :>> outgoingTransfersFromSelf :> interfacingPorts.incomingTransfersToSelf {
            doc
            /* 
             * The target of each of the outgoingTransfersFromSelf of a Port must be an interfacingPort.
             */
             
             end ref source;
             end ref target;
        }
    }
    
    abstract port ports : Port[0..*] nonunique :> objects {
        doc
        /*
         * ports is the base feature of all PortUsages.
         */
    }
}
````
