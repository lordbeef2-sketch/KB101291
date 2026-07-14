# NOMAGIC ATTACHMENT: SysML v2 Quick Sheet.pdf

- attachment_id: `272740923`
- space_key: `SYSML2P`
- parent_page_id: `272740914`
- parent_page_title: CATIA Magic/Cameo SysML v2 Solution
- media_type: `application/pdf`
- reported_bytes: 1159564
- download_url: https://docs.nomagic.com/download/attachments/272740914/SysML%20v2%20Quick%20Sheet.pdf?version=1&modificationDate=1764162594816&api=v2
- payload_kind: `pdf-extracted`
- downloaded_sha256: `4b851a06c0d0b50f9c44466a7d0c7fbeda797d3f85ec4b5892cb51477c84d0c9`

## LAYOUT-PRESERVING PDF EXTRACTION

### PDF PAGE 1

```text
                                x                                                                                                  part def Human;                                                                         attribute def PowerConsumptionData {
                                                                                                                                   part def Environment;                                                                          attribute min : Real;
SysML v2 Quick Sheet                                                                                                    Use Cases  part def Drone;                                            Attributes and Units                attribute max : Real;                                           Requirements
                                                                                                                                   use case def <ObsDrone> 'Observe area                                                          attribute mean : Real;
Version for Webview                                                                                                                                                                                                                                                                                             part def UAV {
                                                                                                                                      by drone' {                                                                          }                                                                                         attribute maxFlightTime :> duration;
                     Deﬁnition     Usages                                                                                                 subject SOI : Drone;                                                             attribute pcd : PowerConsumptionData {
                                                                                                                                          actor operator : Human;                                                                                                                                               }
Deﬁnition and Usage  occurrence def 'MBSE Project';                                                                     Actions           actor forest : Environment;                         Occurrences in Space & Time         attribute :>> min = 1.0 [W];                                                  part def UAVEnvironment {
                     occurrence 'thirty meter telescope' : 'MBSE Project';                                                                objective {                                                                             attribute :>> max = 3.0 [W];
                     occurrence 'TVP Coffee Machine' : 'MBSE Project';                                                                         doc                                                                                attribute mean :>> mean = 2.0 [W];                                                 attribute windSpeed;
                     occurrence 'ITER Fusion Reactor' : 'MBSE Project';                                                                        /* Observe a defined area and                                               }                                                                                    }
                                                                                                                                                 * identify and report
                                                                                                                                                 * potential forest fires.                                                 part myDrone {                                                                       requirement <REQ2> uavFlightTime {
                                                                                                                                         }                                                                                        port chargingPlugPort;                                                             doc /* When standard conditions apply, the UAV shall fly
                                                                                                                                                                                                                                  timeslice part charging {                                                             for at least 2 hours. */
                                                                                                                                     }                                                                                                   interface connect chargingPlugPort to                                            subject uav : UAV;
                                                                                                                                                                                                                                            chargingStation.chargingSocketPort;                                           actor environment : UAVEnvironment;
                                                                                                                                   action def Land;                                                                               }                                                                                       stakeholder uavExpert;
                                                                                                                                   action def 'Operate Drone' {                                                                   timeslice part flying;                                                                  assume constraint {
                                                                                                                                                                                                                                                                                                                                environment.windSpeed <= 20 ['km/h']
                                                                                                                                          action 'define mission' { out item mission; }                                    }                                                                                              }
                                                                                                                                          first start;                                                                                                                                                                    require constraint {
                                                                                                                                          then 'define mission';                                                           state droneState {                                                                                   uav.maxFlightTime >= 120 [min]
                                                                                                                                          action 'lift off';                                                                      private import ScalarValues::Boolean;                                                   }
                                                                                                                                          then 'lift off';                                                                        in attribute hasErrors : Boolean;
                                                                                                                                          decide decide1;                                                                         entry ;                                                                       }
                                                                                                                                          fork fork1;                                                                             then off;
                                                                                                                                          join join1;                                                                             transition t1 first off accept SigSwitchOn if not hasErrors do                part droneX42 : UAV {
                                                                                                                                          action 'fly mission' { in item mission; }                                                  checkSystem then standBy;                                                       attribute :>> maxFlightTime = 142 [min];
                                                                                                                                          action 'capture photos' { out item photo; }                                             transition t2 first standBy then ready;                                            satisfy uavFlightTime by self;
                                                                                                                                          action land : Land;                                                                     transition t3 first ready then flying;
                                                                                                                                          merge merge1;                                                                           state off;                                                                    }
                                                                                                                                          first fork1 then 'fly mission';                                                         state standBy;
Specializations                                                                                                                           first fork1 then decide1;                           States                              state ready;
                                                                                                                                          first 'fly mission' then join1;                                                         state flying {
                     part def Drone {                                                                                   Structure         first 'capture photos' then merge1;                                                            entry action prepareflight;                              What‘s next?
                            part engine [4..8];                                                                                           first land then done;                                                                          do action fly;
                            part boom [4..8];                                                                                             out item photo;                                                                                exit action resumeflight;                                       Deepen your knowledge with our SysML v2 trainings
                                                                                                                                          first 'lift off' then fork1;                                                            }
                     }                                                                                                                    flow flow1 from 'define mission'.mission.                                               transition first start then off;                                       Explore SysML Club, our online learning platform and
                     part def Battery;                                                                                                                                                                                            transition first flying then standBy;                                  community
                     requirement 'electric propulsion';                                                                                    'define mission'::mission to 'fly                                                      transition first standBy then off;
                     part def 'Electric Drone' :> Drone {                                                                                  mission'.mission;                                                                                                                                             Share your feedback to help improve this QuickSheet
                                                                                                                                          first decide1;                                                                   }
                            part 'front left boom' :> boom;                                                                               if 'camera on' then 'capture photos';                                            item def SigSwitchOn;                                                                Hamza Bassam                                                   Marco Höhmann
                            part 'engine[4]' :>> engine;                                                                                  else merge1;                                                                     action checkSystem;
                            part 'energy provider' : Battery;                                                                             first join1 then land;                                                                                                                                                Trainer & Consultant                                           Sales & Organisation
                            satisfy requirement 'is electric' ::> 'electric propulsion';                                                  first merge1 then join1;
Packages                    }                                                                                                             binding bind 'capture photos'.photo = photo;
                                                                                                                                          in attribute 'camera on' : Boolean;
                                                                      package Drone {                                                     first 'define mission' then 'lift off';                                                                                                                                  AI Soft                Design Business
                                                                             package Architecture {                                       binding bind 'capture photos'.photo = photo;                                                                                                                                                   Thinking Processes
                                                                                    private import 'Parts Library'::*;             }                                                                                                                                                                                   Skills &
                                                                                    part def Drone {                                                                                                                                                                                                                     New                             Agile &
                                                                                           part battery : Battery;                 part forestFireObservationDrone {                                                                                                                                                    Work                             Project
                                                                                    }                                                     part droneHeatSensor : HeatSensor;                                                                                                                                      Systems                            Management
                                                                             }                                                                                                                                                                                                                                  Engineering
                                                                             package 'Parts Library' {                             }
                                                                                    part def Battery;                              part def HeatSensor {
                                                                             }
                                                                                                                                          part controlUnit;
                                                                      }                                                                   part body;
                                                                                                                                          part sensingUnit;
                                                                                                                                          attribute powerConsumption : PowerConsumptionData;                                                                                                                    Security                                  Usability &
                                                                                                                                   }                                                                                                                                                                            Testing &                             User Experience
                                                                                                                                   attribute def PowerConsumptionData;                                                                                                                                           Quality                           Requirements
                                                                                                                                   port def HeatPort {                                                                                                                                                          Assurance                           Engineering
                                                                                                                                          out item 'heat energy';                                                                                                                                                                              Software
                                                                                                                                   }                                                                                                                                                                                       Technology &      Engineering
                                                                                                                                                                                                                                                                                                                           Programming     Software
                                                                                                                                   part simpleDrone {                                                                                                                                                                                    Architecture
                                                                                                                                          part battery {
                                                                                                                                                 port powerOut;
                                                                                                                                          }
                                                                                                                                          part engine {
                                                                                                                                                 port heatOut : HeatPort;
                                                                                                                                                 port powerIn;
                                                                                                                                          }
                                                                                                                                          connection pwC : PowerCable connect
                                                                                                                                             battery.powerOut to engine.powerIn {
                                                                                                                                                 flow of Energy {
                                                                                                                                                        end :> sourceSocket;
                                                                                                                                                        end :> targetSocket;
                                                                                                                                                 }
                                                                                                                                             }
                                                                                                                                                 port heatOut : HeatPort;
                                                                                                                                                 binding bind heatOut = engine.heatOut;

                                                                                                                                   connection def PowerCable {
                                                                                                                                          end sourceSocket;
                                                                                                                                          end targetSocket;
                                                                                                                                          attribute length;
                                                                                                                                          part cable;
                                                                                                                                          part sourcePlug;
                                                                                                                                          part targetPlug;
                                                                                                                                          connection connect sourceSocket to sourcePlug;
                                                                                                                                          connection connect sourcePlug to cable;
                                                                                                                                          connection connect targetPlug to cable;
                                                                                                                                          connection connect targetSocket to targetPlug;

                                                                                                                                   }

oose: Your partner for systems engineering.                                                                                        Master SysML v2 your way: expert-designed, self-paced.

              Our team of domain experts o ers in-depth training programs on SysML v2,                                                            Explore our SysML v2 online learning platform with hands-on tutorials
              systems architecture, and requirements modeling – designed for professionals                                                        from the co-developers of the SysML v2 speciﬁcation, real-world
              who shape the systems of tomorrow. Explore our full seminar portfolio and                                                           modeling challenges and direct access to our expert community.
              expert insights at oose.com/topics/systems-engineering                                                                              All tailored to elevate your SE skills at clubs.oose.com.
```


## EXACT ATTACHMENT METADATA

````json
{
  "id": "272740923",
  "type": "attachment",
  "status": "current",
  "title": "SysML v2 Quick Sheet.pdf",
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
    "when": "2025-11-26T14:09:54.816+01:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/272740923/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/272740923"
    }
  },
  "position": -1,
  "container": {
    "id": "272740914",
    "type": "page",
    "status": "current",
    "title": "CATIA Magic/Cameo SysML v2 Solution",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/SYSML2P/pages/272740914/CATIA+Magic+Cameo+SysML+v2+Solution",
      "edit": "/pages/resumedraft.action?draftId=272740914&draftShareId=920d9f5c-694f-4624-95c5-2e4c02bcc741",
      "tinyui": "/x/MrJBE",
      "self": "https://docs.nomagic.com/rest/api/content/272740914"
    },
    "_expandable": {
      "container": "/rest/api/space/SYSML2P",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/272740914/child",
      "restrictions": "/rest/api/content/272740914/restriction/byOperation",
      "history": "/rest/api/content/272740914/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/272740914/descendant",
      "space": "/rest/api/space/SYSML2P",
      "relevantViewRestrictions": "/rest/api/content/272740914/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/pdf"
  },
  "extensions": {
    "mediaType": "application/pdf",
    "fileSize": 1159564,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/272740914/SysML%20v2%20Quick%20Sheet.pdf?version=1&modificationDate=1764162594816&api=v2",
    "webui": "/spaces/SYSML2P/pages/272740914/CATIA+Magic+Cameo+SysML+v2+Solution?preview=%2F272740914%2F272740923%2FSysML+v2+Quick+Sheet.pdf",
    "self": "https://docs.nomagic.com/rest/api/content/272740923"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/272740923/child",
    "restrictions": "/rest/api/content/272740923/restriction/byOperation",
    "history": "/rest/api/content/272740923/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/272740923/descendant",
    "space": "/rest/api/space/SYSML2P",
    "relevantViewRestrictions": "/rest/api/content/272740923/restriction/relevantViewRestrictions"
  }
}
````
