# NOMAGIC ATTACHMENT: 2026-01 SysMLv2 Cheatsheet A3-Printable complete.pdf

- attachment_id: `304005791`
- space_key: `SYSML2P`
- parent_page_id: `304005789`
- parent_page_title: (2026x Refresh1) SysML v2 Quick Sheet
- media_type: `application/pdf`
- reported_bytes: 1330566
- download_url: https://docs.nomagic.com/download/attachments/304005789/2026-01%20SysMLv2%20Cheatsheet%20A3-Printable%20complete.pdf?version=1&modificationDate=1777461526219&api=v2
- payload_kind: `pdf-extracted`
- downloaded_sha256: `9400aa26d260b0b605b40c6ecf8cd9a99875eef67053aecb6570bd8d8aef65ca`

## LAYOUT-PRESERVING PDF EXTRACTION

### PDF PAGE 1

```text
x                                                                                                      Actions   action def Land;
                                                                                                                 action def 'Operate Drone' {
                        Deﬁnition  Usages
                                                                                                                        action 'define mission' { out item mission; }
   Deﬁnition and Usage                                                                                                  first start;
                                                                                                                        then 'define mission';
                        occurrence def 'MBSE Project';                                                                  action 'lift off';
                        occurrence 'thirty meter telescope' : 'MBSE Project';                                           decide decide1;
                        occurrence 'TVP Coffee Machine' : 'MBSE Project';                                               fork fork1;
                        occurrence 'ITER Fusion Reactor' : 'MBSE Project';                                              join join1;
                                                                                                                        action 'fly mission' { in item mission; }
                                                                                                                        action 'capture photos' { out item photo; }
                                                                                                                        action land : Land;
                                                                                                                        merge merge1;
                                                                                                                        first fork1 then 'fly mission';
                                                                                                                        first fork1 then decide1;
                                                                                                                        first 'fly mission' then join1;
                                                                                                                        first 'capture photos' then merge1;
                                                                                                                        first land then done;
                                                                                                                        out item photo;
                                                                                                                        first 'lift off' then fork1;
                                                                                                                        flow flow1 from 'define mission'.mission to 'fly
                                                                                                                 mission'.mission;
                                                                                                                        first decide1;
                                                                                                                        if 'camera on' then 'capture photos';
                                                                                                                        else merge1;
                                                                                                                        first join1 then land;
                                                                                                                        first merge1 then join1;
                                                                                                                        in attribute 'camera on' : ScalarValues::Boolean;
                                                                                                                        first 'define mission' then 'lift off';
                                                                                                                        binding bind 'capture photos'.photo = photo;
                                                                                                                 }

   Specializations                                                                                     Packages

                            part def Drone {                                                                                                                                                                  package Drone {
                                         part engine [4..8];                                                                                                                                                         package Architecture {
                                         part boom [4..8];                                                                                                                                                                  private import 'Parts Library'::*;
                                                                                                                                                                                                                            part def Drone {
                            }                                                                                                                                                                                                      part battery : Battery;
                            part def Battery;                                                                                                                                                                               }
                            requirement 'electric propulsion';                                                                                                                                                       }
                            part def 'Electric Drone' :> Drone {                                                                                                                                                     package 'Parts Library' {
                                                                                                                                                                                                                            part def Battery;
                                         part 'front left boom' :> boom;                                                                                                                                             }
                                         part 'engine' :>> engine [4];
                                         part 'energy provider' : Battery;                                                                                                                                    }
                                         satisfy requirement 'is electric' ::> 'electric propulsion';
                            }                                                                                    Master SysML v2 your way: expert-designed, self-paced.

   oose: Your partner for systems engineering.                                                                                  Explore our SysML v2 online learning platform with hands-on tutorials
                                                                                                                                from the co-developers of the SysML v2 speciﬁcation, real-world
                 Our team of domain experts o ers in-depth training programs on SysML v2,                                       modeling challenges and direct access to our expert community.
                 systems architecture, and requirements modeling – designed for professionals                                   All tailored to elevate your SE skills at clubs.oose.com.
                 who shape the systems of tomorrow. Explore our full seminar portfolio and
                 expert insights at oose.com/topics/systems-engineering
```

### PDF PAGE 2

```text
Structure  part forestFireObservationDrone {               Attributes and Units  private import ScalarValues::*;                                   Occurrences in Space & Time
                  part droneHeatSensor : HeatSensor;                             private import SI::*;
                                                                                                                                                                                part myDrone {
           }                                                                     attribute def PowerConsumptionData {                                                                 port chargingPlugPort;
           part def HeatSensor {                                                        attribute min : Real;                                                                         timeslice part flying :> myDrone;
                                                                                        attribute max : Real;                                                                         timeslice part charging :> myDrone;
                  part controlUnit;                                                     attribute mean : Real;
                  part body;                                                                                                                                                    }
                  part sensingUnit;                                              }                                                                                              part chargingStation {
                  attribute powerConsumption :                                   attribute pcd : PowerConsumptionData {
                                                                                                                                                                                      port chargingSocketPort;
                       PowerConsumptionData;                                            attribute :>> min = 1.0 [W];                                                            }
           }                                                                            attribute :>> max = 3.0 [W];                                                            interface connect myDrone.charging.chargingPlugPort to
           attribute def PowerConsumptionData;                                          attribute mean :>> mean = 2.0 [W];                                                      chargingStation.chargingSocketPort;
           port def HeatPort {                                                   }

                  out item heatEnergy;                     States
           }
           part simpleDrone {                                                                                                                      Requirements

Use Cases         part battery {                                            state droneState {                                                                                  private import SI::**;
                         port powerOut;                                            in attribute hasErrors : ScalarValues::Boolean;                                              part def UAV {
                                                                                   transition t1 first off accept SigSwitchOn if not hasErrors do
                  }                                                                   checkSystem then standBy;                                                                        attribute maxFlightTime :> duration;
                  part engine {                                                    transition t2 first standBy then ready;                                                      }
                                                                                   transition t3 first ready then flying;                                                       part def UAVEnvironment {
                         port heatOut : HeatPort;                                  state off;
                         port powerIn;                                             state standBy;                                                                                      attribute windSpeed;
                  }                                                                state ready;                                                                                 }
                  connection pwC : PowerCable connect                              state flying {                                                                               requirement <REQ2> uavFlightTime {
                   battery.powerOut to engine.powerIn {                                   entry action prepareflight;
                         flow of Energy {                                                 do action fly;                                                                               doc
                                                                                          exit action resumeflight;                                                                    /* When standard conditions apply, the UAV shall fly
                                end ::> sourceSocket;                              }
                                end ::> targetSocket;                              transition first start then off;                                                                     * for at least 2 hours.
                         }                                                         transition first flying then standBy;                                                                */
                  }                                                                transition first standBy then off;                                                                  subject uav : UAV;
                  port heatOut : HeatPort;                                                                                                                                             actor environment : UAVEnvironment;
                  binding bind heatOut = engine.heatOut;                    }                                                                                                          stakeholder uavExpert;
           }                                                                item def SigSwitchOn;                                                                                      assume constraint {
           item def Energy;                                                 action checkSystem;
           connection def PowerCable {                                                                                                                                                        environment.windSpeed <= 20 ['km/h']
                  end sourceSocket;                        What‘s next?                                                                                                                }
                  end targetSocket;                                                                                                                                                    require constraint {
                  attribute length;                               Deepen your knowledge with our SysML v2 trainings
                  part cable;                                                                                                                                                                 uav.maxFlightTime >= 120 [min]
                  part sourcePlug;                                Explore SysML Club, our online learning platform and                                                                 }
                  part targetPlug;                                community                                                                                                     }
                  connection connect sourceSocket to                                                                                                                            part droneX42 : UAV {
                       sourcePlug;                                Share your feedback to help improve this QuickSheet                                                                  attribute :>> maxFlightTime = 142 [min];
                  connection connect sourcePlug to cable;                                                                                                                              satisfy uavFlightTime;
                  connection connect targetPlug to cable;                                                                                                                       }
                  connection connect targetSocket to
                       targetPlug;                                                                                                                                              Hamza Bassam             AI Soft                Design Business
           }                                                                                                                                                                                                                   Thinking Processes
                                                                                                                                                                                Trainer & Consultant         Skills &
           part def Human;                                                                                                                                                                                     New                             Agile &
           part def Environment;                                                                                                                                                Julia Stede                   Work                             Project
           part def Drone;                                                                                                                                                                              Systems                            Management
           use case def <ObsDrone> 'Observe area by                                                                                                                             Sales & Organisation  Engineering

                       drone' {
                  subject SOI : Drone;
                  actor operator : Human;
                  actor forest : Environment;
                  objective {

                         doc
                         /* Observe a defined area and

                           * identify and report
                           * potential forest fires.
                           */
                  }
           }

                                                                                                                                                                                                      Security                                  Usability &
                                                                                                                                                                                                      Testing &                             User Experience
                                                                                                                                                                                                       Quality                           Requirements
                                                                                                                                                                                                      Assurance                           Engineering
                                                                                                                                                                                                                                     Software
                                                                                                                                                                                                                 Technology &      Engineering
                                                                                                                                                                                                                 Programming     Software
                                                                                                                                                                                                                               Architecture
```


## EXACT ATTACHMENT METADATA

````json
{
  "id": "304005791",
  "type": "attachment",
  "status": "current",
  "title": "2026-01 SysMLv2 Cheatsheet A3-Printable complete.pdf",
  "version": {
    "by": {
      "type": "known",
      "username": "kbe12",
      "userKey": "2c9f81f87674fd7d017a0928ba470000",
      "profilePicture": {
        "path": "/images/icons/profilepics/default.svg",
        "width": 48,
        "height": 48,
        "isDefault": true
      },
      "displayName": "Kristina B.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=2c9f81f87674fd7d017a0928ba470000"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2026-04-29T13:18:46.219+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/304005791/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/304005791"
    }
  },
  "position": -1,
  "container": {
    "id": "304005789",
    "type": "page",
    "status": "current",
    "title": "(2026x Refresh1) SysML v2 Quick Sheet",
    "position": 2,
    "extensions": {
      "position": 2
    },
    "_links": {
      "webui": "/spaces/SYSML2P/pages/304005789/2026x+Refresh1+SysML+v2+Quick+Sheet",
      "edit": "/pages/resumedraft.action?draftId=304005789",
      "tinyui": "/x/ncIeEg",
      "self": "https://docs.nomagic.com/rest/api/content/304005789"
    },
    "_expandable": {
      "container": "/rest/api/space/SYSML2P",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/304005789/child",
      "restrictions": "/rest/api/content/304005789/restriction/byOperation",
      "history": "/rest/api/content/304005789/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/304005789/descendant",
      "space": "/rest/api/space/SYSML2P",
      "relevantViewRestrictions": "/rest/api/content/304005789/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/pdf"
  },
  "extensions": {
    "mediaType": "application/pdf",
    "fileSize": 1330566,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/304005789/2026-01%20SysMLv2%20Cheatsheet%20A3-Printable%20complete.pdf?version=1&modificationDate=1777461526219&api=v2",
    "webui": "/spaces/SYSML2P/pages/304005789/2026x+Refresh1+SysML+v2+Quick+Sheet?preview=%2F304005789%2F304005791%2F2026-01+SysMLv2+Cheatsheet+A3-Printable+complete.pdf",
    "self": "https://docs.nomagic.com/rest/api/content/304005791"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/304005791/child",
    "restrictions": "/rest/api/content/304005791/restriction/byOperation",
    "history": "/rest/api/content/304005791/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/304005791/descendant",
    "space": "/rest/api/space/SYSML2P",
    "relevantViewRestrictions": "/rest/api/content/304005791/restriction/relevantViewRestrictions"
  }
}
````
