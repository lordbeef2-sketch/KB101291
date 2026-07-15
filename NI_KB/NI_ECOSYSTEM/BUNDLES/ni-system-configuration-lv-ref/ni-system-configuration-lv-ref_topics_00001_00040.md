# NI DOCUMENT BUNDLE: ni-system-configuration-lv-ref

<!--NI_BUNDLE_CHUNK bundle=ni-system-configuration-lv-ref start=1 end=40 -->
<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/add_software_feed.html language=enus -->
## TOPIC 00001: Add Software Feed (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/add_software_feed.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/add_software_feed.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Add Software Feed (VI)

Installed With:

Adds a software feed to the system. This requires Secure Shell Server (sshd) to be enabled on the target.

[IMAGE alt='Add Software Feed' src='add_software_feed.gif']

|  | Session in specifies the system receiving changes. |
| --- | --- |
|  | Feed Name specifies the name of the feed for identification purposes. |
|  | URI specifies the location of the feed, such as "file://..." or "http://...". NI feeds often start with "http://download.ni.com/". |
|  | Enabled specifies whether the feed is enabled. |
|  | Trusted specifies whether the feed is trusted. A trusted feed will not be cryptographically verified by the package manager to be a safe and secure source of packages. Feeds are not trusted by default. A system administrator may have reason to trust the feed regardless. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Session out returns the refnum for the system. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/bp_copyright.html language=dede -->
## TOPIC 00002: Copyright

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/bp_copyright.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/dede/nisyscfg/bp_copyright.html
- source_language: `dede`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Copyright

Gemäß den Bestimmungen des Urheberrechts darf diese Publikation ohne vorherige schriftliche Zustimmung der Firma National Instruments Corporation weder vollständig noch teilweise vervielfältigt oder verbreitet werden, gleich in welcher Form, ob elektronisch oder mechanisch. Das Verbot erfasst u. a. das Fotokopieren, das Aufzeichnen und das Speichern von Informationen in Informationsgewinnungssystemen sowie das Anfertigen von Übersetzungen, gleich welcher Art.

NI achtet das geistige Eigentum anderer und fordert seine Nutzer auf, dies ebenso zu tun. Die Software von NI ist urheberrechtlich und durch andere Rechtsvorschriften zum Schutz geistigen Eigentums geschützt. Wenn Sie Software von NI nutzen, um Software oder andere Materialien, die im Eigentum Dritter stehen, zu vervielfältigen, dürfen Sie Software von NI nur insoweit nutzen, als Sie die betreffenden Materialien nach den jeweils anwendbaren Lizenzbestimmungen oder Rechtsvorschriften vervielfältigen dürfen.

#### Lizenzverträge von NI und Rechtshinweise von Drittanbietern

Lizenzverträge (EULAs) von NI und Rechtshinweise von Drittanbietern befinden sich in folgenden Verzeichnissen:

- Rechtshinweise: <National Instruments>\_Legal Information und <National Instruments>
- EULAs: <National Instruments>\Shared\MDF\Legal\license
- Informationen zum Hinzufügen von Rechtshinweisen zu Installationsprogrammen, die mit Hilfe von NI-Produkten erzeugt werden: <National Instruments>\_Legal Information.txt

#### Eingeschränkte Rechte der US-Regierung

Für Behörden, Regierungsstellen oder andere Rechtsträger der US-Regierung ("Government") ist die Verwendung, Vervielfältigung, Reproduktion, Veröffentlichung, Änderung, Verbreitung oder Übertragung der technischen Daten in diesem Handbuch gemäß der folgenden Verordnungen der US-Bundesbehörden weiter beschränkt: Federal Acquisition Regulation 52.227-14 für zivile Behörden und Defense Federal Acquisition Regulation Supplement Section 252.227-7014 und 252.227-7015 für Militärbehörden.

#### IVI Foundation - Urheberrechtsvermerk

Content from the IVI specifications reproduced with permission from the IVI Foundation.

The IVI Foundation and its member companies make no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The IVI Foundation and its member companies shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/bp_export_compliance.html language=dede -->
## TOPIC 00003: Export Compliance Information

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/bp_export_compliance.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/dede/nisyscfg/bp_export_compliance.html
- source_language: `dede`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Export Compliance Information

Informationen zu den Global-Trade-Compliance-Richtlinien von NI sowie zu Bezugsquellen für relevante HTS-Codes, ECCNs und andere Import-/Exportangaben finden Sie auf ni.com/legal unter der Überschrift *Export Compliance Information*.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/bp_important_information.html language=dede -->
## TOPIC 00004: Rechtliche Hinweise

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/bp_important_information.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/dede/nisyscfg/bp_important_information.html
- source_language: `dede`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Rechtliche Hinweise

[Beschränkte Gewährleistung](bp_warranty.html)

[Copyright](bp_copyright.html)

[Marken](bp_trademarks.html)

[Patente](bp_patents.html)

[Bestimmungen für die Ausfuhrkontrolle](bp_export_compliance.html)

[Warnung zur Nutzung von Produkten von NI](bp_warning_ni.html)

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/bp_patents.html language=dede -->
## TOPIC 00005: Patente

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/bp_patents.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/dede/nisyscfg/bp_patents.html
- source_language: `dede`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Patente

Nähere Informationen über den Patentschutz von NI-Produkten und -Technologien finden Sie unter **Hilfe»Patente** in Ihrer Software, in der Datei patents.txt auf Ihrem Datenträger oder unter *Patent Notice* auf der Website ni.com/patents.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/bp_technical_support_resources.html language=dede -->
## TOPIC 00006: NI-Serviceleistungen

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/bp_technical_support_resources.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/dede/nisyscfg/bp_technical_support_resources.html
- source_language: `dede`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### NI-Serviceleistungen

Die Website von NI bietet verschiedene Ressourcen für den technischen Support. Unter ni.com/support erhalten Sie Zugriff auf Informationen zur Fehlersuche und Entwicklung von Anwendungen sowie Möglichkeiten zum Anfordern persönlicher technischer Unterstützung per E-Mail oder Telefon.

Besuchen Sie ni.com/services für Informationen zu den von NI angebotenen Serviceleistungen.

Auf ni.com/register können Sie Ihr Produkt von NI registrieren. Die Produktregistrierung erleichtert den technischen Support und die Zusendung wichtiger Update-Informationen.

Die Adresse der Hauptniederlassung von NI lautet: 11500 North Mopac Expressway, Austin, Texas, 78759-3504, USA. Auf ni.com/contact finden Sie stets aktuelle Kontaktdaten einer NI-Niederlassung in Ihrer Nähe.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/bp_trademarks.html language=dede -->
## TOPIC 00007: Marken

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/bp_trademarks.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/dede/nisyscfg/bp_trademarks.html
- source_language: `dede`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Marken

Besuchen Sie *NI Trademarks and Logo Guidelines* auf ni.com/trademarks für weitere Informationen zu Marken von NI.

ARM, Keil, and µVision are trademarks or registered of ARM Ltd or its subsidiaries.

LEGO, the LEGO logo, WEDO, and MINDSTORMS are trademarks of the LEGO Group.

TETRIX by Pitsco is a trademark of Pitsco, Inc.

FIELDBUS FOUNDATION™ and FOUNDATION™ are trademarks of the Fieldbus Foundation.

EtherCAT® is a registered trademark of and licensed by Beckhoff Automation GmbH.

CANopen® is a registered Community Trademark of CAN in Automation e.V.

DeviceNet™ and EtherNet/IP™ are trademarks of ODVA.

Go!, SensorDAQ, and Vernier are registered trademarks of Vernier Software & Technology. Vernier Software & Technology and vernier.com are trademarks or trade dress.

Xilinx is the registered trademark of Xilinx, Inc.

Taptite and Trilobular are registered trademarks of Research Engineering & Manufacturing Inc.

FireWire® is the registered trademark of Apple Inc.

Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

Handle Graphics®, MATLAB®, Simulink®, Stateflow®, and xPC TargetBox® are registered trademarks, and Simulink Coder™, TargetBox™, and Target Language Compiler™ are trademarks of The MathWorks, Inc.

Tektronix®, Tek, and Tektronix, Enabling Technology are registered trademarks of Tektronix, Inc.

The Bluetooth® word mark is a registered trademark owned by the Bluetooth SIG, Inc.

The ExpressCard™ word mark and logos are owned by PCMCIA and any use of such marks by National Instruments is under license.

The mark LabWindows is used under a license from Microsoft Corporation. Windows is a registered trademark of Microsoft Corporation in the United States and other countries.

Sonstige hierin erwähnte Produkt- und Firmenbezeichnungen sind Marken oder Handelsnamen der jeweiligen Unternehmen.

Ein NI Partner ist ein eigenständiges und von NI unabhängiges Unternehmen; zwischen einem NI Partner und NI besteht keine gesellschaftliche Verbindung und auch kein Auftragsverhältnis.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/bp_warning_ni.html language=dede -->
## TOPIC 00008: Warnung zur Nutzung von Produkten von National Instruments

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/bp_warning_ni.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/dede/nisyscfg/bp_warning_ni.html
- source_language: `dede`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Warnung zur Nutzung von Produkten von National Instruments Corporation

Es liegt in Ihrer alleinigen Verantwortung, die Eignung und die Zuverlässigkeit der Produkte und Dienstleistungen für Ihre Zwecke zu prüfen und zu validieren, wenn die Produkte oder Dienstleistungen in Ihre Systeme oder Anwendungen eingebaut werden, inklusive der Eignung des Designs, Betriebsablaufs und des Sicherheitsniveaus solcher Systeme oder Anwendungen.

Die Produkte wurden nicht für lebens- oder sicherheitskritische Anwendungen, gefährliche Umgebungen oder für sonstige Verwendungen, die Ausfallsicherheit erfordern, entwickelt, hergestellt und getestet. Dazu gehören z. B. der Einsatz in der Atomkraft, der Flugzeugnavigation, der Luftverkehrskontrolle, in lebensrettenden, lebenserhaltenden oder ähnlichen medizinischen Systemen oder in sonstigen Anwendungen, bei denen die Fehlfunktion der Produkte oder Dienstleistungen zu erheblichen Schäden an Leib und Leben von Menschen, erheblicher Sachbeschädigung oder Umweltschäden führen kann (sog. "High-Risk Uses"). Darüber hinaus müssen angemessene Maßnahmen ergriffen werden, um gegen Fehlfunktionen der Produkte gesichert zu sein, z. B. durch Erstellen von Backups oder durch Mechanismen, die ein Ausschalten oder Herunterfahren des Produkts im Fehlerfall ermöglichen. NI leistet keine Gewähr, dass die Produkte für High-Risk Uses geeignet sind.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/bp_warranty.html language=dede -->
## TOPIC 00009: Beschränkte Gewährleistung

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/bp_warranty.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/dede/nisyscfg/bp_warranty.html
- source_language: `dede`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Beschränkte Gewährleistung

Dieses Dokument wird "wie es ist" zur Verfügung gestellt, und NI kann den Inhalt dieses Dokuments ohne Ankündigung in zukünftigen Ausgaben ändern. Die jeweils aktuelle Version dieses Dokuments finden Sie auf der Website ni.com/manuals. NI prüft die technische Richtigkeit dieses Dokuments sorgfältig, übernimmt jedoch weder ausdrücklich noch stillschweigend irgendeine Gewährleistung für die Richtigkeit oder Vollständigkeit der in diesem Dokument enthaltenen Informationen und haftet nicht für Fehler.

NI garantiert bei Hardwareprodukten für die Dauer eines (1) Jahres ab Rechnungsdatum, dass das Produkt frei von Material- und Verarbeitungsfehlern ist und den von NI veröffentlichten anwendbaren Spezifikationen im Wesentlichen entspricht.

NI garantiert für einen Zeitraum von neunzig (90) Tagen ab Rechnungsdatum, dass NI-Software (i) im Wesentlichen gemäß der mitgelieferten schriftlichen Dokumentation funktioniert, und (ii) das Speichermedium, auf dem die Software geliefert wird, frei von Material- und Fabrikationsfehlern ist.

Wenn NI innerhalb der entsprechenden Gewährleistungsperiode über einen aufgetretenen Fehler oder eine nicht eingehaltene Spezifikation unterrichtet wird, dann wird NI nach eigenem Ermessen (i) das betroffene Produkt reparieren oder ersetzen oder (ii) den gezahlten Preis für das betroffene Produkt zurückerstatten. Die Gewährleistungsfrist für die reparierte oder ersetzte Hardware entspricht der Restzeit der Gewährleistungsfrist des ursprünglichen Produkts, sofern diese noch mindestens neunzig (90) Tage beträgt. Anderenfalls beträgt die Gewährleistungsfrist neunzig (90) Tage. Wenn sich NI dafür entscheidet, Hardware zu reparieren oder zu ersetzen, verwendet NI neue oder neuwertige Teile oder Produkte, welche in ihrer Leistung und Beständigkeit zumindest funktional neuen Teilen oder neuer Hardware entsprechen.

Vor dem Zurücksenden eines Produkts an NI müssen Sie von NI eine RMA-Nummer ("Return Material Authorization") anfordern. NI behält sich das Recht vor, für das Prüfen und Testen von Hardware eine Gebühr zu berechnen, für die unter der beschränkten Gewährleistung kein Garantieanspruch besteht.

Diese beschränkte Gewährleistung gilt nicht, wenn der Defekt des Produkts von unsachgemäßem oder inadäquatem Gebrauch; unsachgemäßer oder inadequater Installation, Reparatur oder Kalibrierung (welche von einem Dritten und nicht von NI vorgenommen wurde); eigenmächtigen Abänderungen; Betrieb in falscher Umgebung; Verwendung eines falschen Hardware- oder Softwareschlüssels; unsachgemäßer Verwendung oder Betrieb außerhalb der Spezifikation für das Produkt; unzulässigen Spannungen; Unfall; missbräuchlichem oder fahrlässigem Umgang oder einer Naturkatastrophe wie Blitzschlag, Überschwemmung oder anderen Naturgewalten herrührt.

Die einzigen und ausschließlichen Verpflichtungen von NI in Verbindung mit der Gewährleistung sind oben beschrieben und sind auch dann anwendbar, wenn der wesentliche Zweck dieser Verpflichtungen verfehlt wird.

Unter dem Vorbehalt der oben erwähnten Gewährleistungsausführungen werden die NI-Produkte geliefert, "wie sie sind", ohne jede zusätzliche Garantie oder Gewährleistung, weder ausdrücklich noch indirekt in irgendeiner Art, inbegriffen aber nicht ausschließlich jede Garantie oder Gewährleistung der Kommerzialisierung, Eignung für einen bestimmten Zweck oder Gewährleistung für das Bestehen rechtmäßigen Eigentums und die Nichtverletzung von Schutzrechten Dritter. Weder bestätigt noch garantiert NI den Gebrauch der Produkte oder der Resultate dieses Gebrauchs betreffend Richtigkeit, Präzision, Zuverlässigkeit oder anderem. NI garantiert auch nicht das ununterbrochene und fehlerfreie Funktionieren der Produkte.

Falls Sie eine separate, unterzeichnete Vereinbarung mit NI haben, die Gewährleistungsbedingungen der Produkte regelt, haben Gewährleistungsbedingungen in der separaten Vereinbarung Vorrang.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/change_administrator_password.html language=enus -->
## TOPIC 00010: Change Administrator Password (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/change_administrator_password.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/change_administrator_password.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Change Administrator Password (VI)

Installed With:

Change the administrator password. This requires Secure Shell Server (sshd) to be enabled on the target.

[IMAGE alt='Change Administrator Password' src='change_administrator_password.gif']

|  | Session in specifies the system receiving changes. |
| --- | --- |
|  | New Password specifies the new password to set on the target. Although not recommended, the value of an empty string clears the password. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Session out returns the refnum for the system. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/close.html language=enus -->
## TOPIC 00011: Close (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/close.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/close.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Close (VI)

Installed With:

Closes a reference to a previously allocated filter, resource, or session. Error I/O operates uniquely in this function. The function closes the device session regardless of whether an error occurred in a preceding operation.

#### Close (Hardware)

Closes a reference to a hardware resource.

[IMAGE alt='Close (Hardware)' src='close_(hardware).gif']

|  | Resource in specifies the resource to be closed. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |
|  | error out returns error information. This output provides standard error out functionality. |

#### Close (System)

Closes a reference to a system.

[IMAGE alt='Close (System)' src='close_(system).gif']

|  | Session in specifies a user-defined reference number (refnum) for the system framework instance. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |
|  | error out returns error information. This output provides standard error out functionality. |

#### Close (Filter)

Closes a reference to a system filter.

[IMAGE alt='Close (Filter)' src='close_(filter).gif']

|  | Filter in specifies a user-defined system filter refnum to be closed. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |
|  | error out returns error information. This output provides standard error out functionality. |

#### Close (Resources)

Closes references to multiple hardware resources.

[IMAGE alt='Close (Resources)' src='close_(resources).gif']

|  | Resources in specifies the resources to be closed. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/concepts.html language=enus -->
## TOPIC 00012: Concepts

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/concepts.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/concepts.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### NI System Configuration Concepts

The **NI System Configuration Concepts** section provides you with information about the LabVIEW System Configuration API. Following is a brief introduction of the concepts discussed in this manual.

[Finding Systems and Hardware](finding_systems_hardware.html)—Creates a filter object used to query for specific devices on a system and locates systems and resources on systems.

[Deploying System Images](import_export_concept.html)—Imports and exports system configuration data to be used in programs such as MAX.

[Initialize](initialize_concept.html)—Initializes a session for a specified system.

[Modifying System State](reset_rename.html)—Use the property nodes and Rename Alias VI to change the state of the system.

[Reset and Restart](reset_restart.html)—Returns the device or system to a known initialized state.

[Self-Test and Self-Calibrate](self_test_calibrate.html)—Tests and calibrates resources.

[Modifying Installed Software](software_install_uninstall.html)—Installs and uninstalls individual pieces of software and software sets.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/create_filter_wrapper.html language=enus -->
## TOPIC 00013: Create Filter Wrapper (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/create_filter_wrapper.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/create_filter_wrapper.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Create Filter Wrapper (VI)

Installed With:

Creates a system filter object that is used to query for specific resources in a system. After creating a filter, set one or more [properties](property_node_filter.html) using the Property Node (Filter) to limit the set of detected resources.

[IMAGE alt='Create Filter Wrapper' src='create_filter_wrapper.gif']

|  | Session in specifies a user-defined reference number (refnum) for the system framework instance. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Session out returns the refnum for the system. |
|  | Filter out returns the user-defined refnum for the system filter instance. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/create_system_image.html language=enus -->
## TOPIC 00014: Create System Image (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/create_system_image.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/create_system_image.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Create System Image (VI)

Installed With:

Creates a system image file or folder—a copy of the file contents on a primary hard drive of a system. You may want to create a system image to restore a system to its original state or to deploy the image to other systems.

#### Create System Image (File)

Creates a system image file—a copy of the file contents on a primary hard drive of a system in zip format. You may want to create a system image to restore a system to its original state or to deploy the image to other systems.

[IMAGE alt='Create System Image (File)' src='create_system_image_(file).gif']

|  | Encryption Passphrase specifies the passphrase used to encrypt a portion of the image that contains sensitive information. |
| --- | --- |
|  | Restart Automatically restarts the system into install mode by default before the operation is performed, and restarts back to a running state after the operation is complete. If you choose not to restart automatically, and the system is not in install mode, the resulting image may not be valid. |
|  | Session in specifies the system from which the image is being created. |
|  | Destination File specifies the destination where the data is copied. |
|  | Image Metadata in specifies the metadata to add to the system image. Title is required if you specify the value of any additional cluster elements. If you specify the ID , it must be in the GUID format "{00000000-0000-0000-0000-000000000000}" where each '0' represents a hexadecimal digit. title specifies the title of the system image. description specifies the short description of the system image. ID specifies the unique identifier for the system image. version specifies the version of the system image. component type specifies the component type for the system image. NI recommends leaving the default value, image , if you are creating a new system image. |
|  | title specifies the title of the system image. |
|  | description specifies the short description of the system image. |
|  | ID specifies the unique identifier for the system image. |
|  | version specifies the version of the system image. |
|  | component type specifies the component type for the system image. NI recommends leaving the default value, image , if you are creating a new system image. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Overwrite saves the new output file over an older file of the same name if TRUE. By default, this VI will not overwrite the file. |
|  | File and Directory Blacklist specifies the list of files and folders to exclude when creating a system image. Files on the blacklist will not be copied from the target to the image. |
|  | Session out returns the refnum for the system being imaged. |
|  | Image Metadata out returns the metadata added to the system image. title is the title of the system image. description is the short description of the system image. ID is the unique identifier for the system image. version is the version of the system image. component type is the component type for the system image. |
|  | title is the title of the system image. |
|  | description is the short description of the system image. |
|  | ID is the unique identifier for the system image. |
|  | version is the version of the system image. |
|  | component type is the component type for the system image. |
|  | error out returns error information. This output provides standard error out functionality. |

#### Create System Image (Folder)

Creates a system image folder—a copy of the contents and software on a primary hard drive of a system. You may want to create a system image to restore a system to its original state or to deploy the image to other systems.

[IMAGE alt='Create System Image (Folder)' src='create_system_image_(folder).gif']

|  | Encryption Passphrase specifies the passphrase used to encrypt a portion of the image that contains sensitive information. |
| --- | --- |
|  | Restart Automatically restarts the system into install mode by default before the operation is performed, and restarts back to a running state after the operation is complete. If you choose not to restart automatically, and the system is not in install mode, the resulting image may not be valid. |
|  | Session in specifies the system from which the image is being created. |
|  | Destination Folder specifies the directory where the image is stored. |
|  | Image Metadata in specifies the metadata to add to the system image. Title is required if you specify the value of any additional cluster elements. If you specify the ID , it must be in the GUID format "{00000000-0000-0000-0000-000000000000}" where each '0' represents a hexadecimal digit. title specifies the title of the system image. description specifies the short description of the system image. ID specifies the unique identifier for the system image. version specifies the version of the system image. component type specifies the component type for the system image. NI recommends leaving the default value, image , if you are creating a new system image. |
|  | title specifies the title of the system image. |
|  | description specifies the short description of the system image. |
|  | ID specifies the unique identifier for the system image. |
|  | version specifies the version of the system image. |
|  | component type specifies the component type for the system image. NI recommends leaving the default value, image , if you are creating a new system image. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Overwrite saves the new output folder over an older folder of the same name if TRUE. By default, this VI will not overwrite the folder. |
|  | File and Directory Blacklist specifies the list of files and folders to exclude when creating a system image. Files on the blacklist will not be copied from the target to the image. |
|  | Session out returns the refnum for the system being imaged. |
|  | Image Metadata out returns the metadata added to the system image. title is the title of the system image. description is the short description of the system image. ID is the unique identifier for the system image. version is the version of the system image. component type is the component type for the system image. |
|  | title is the title of the system image. |
|  | description is the short description of the system image. |
|  | ID is the unique identifier for the system image. |
|  | version is the version of the system image. |
|  | component type is the component type for the system image. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/delete_resource.html language=enus -->
## TOPIC 00015: Delete Resource (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/delete_resource.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/delete_resource.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Delete Resource (VI)

Installed With:

Permanently removes a hardware resource and its configuration data from the system. Not all devices can be deleted; consult your product documentation.

[IMAGE alt='Delete Resource' src='delete_resource.gif']

|  | Resource in is the resource object refnum returned from the Find Hardware VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. In some cases, the operation may take longer to complete. This timeout is for remote systems only. |
|  | Delete Mode specifies the conditions under which to delete the specified resource. Validate but do not delete (-1) Verify whether the resource can be deleted and whether it has dependencies. Delete if no dependencies exist (0) Delete the resource only if no dependencies exist. These could be tasks or child resources. Delete item and any dependencies (1) Delete this resource. If any dependencies exist, delete them too. Delete item but keep dependencies (2) Delete this resource. If any dependencies exist, leave them in an unusable state. |
| Validate but do not delete (-1) | Verify whether the resource can be deleted and whether it has dependencies. |
| Delete if no dependencies exist (0) | Delete the resource only if no dependencies exist. These could be tasks or child resources. |
| Delete item and any dependencies (1) | Delete this resource. If any dependencies exist, delete them too. |
| Delete item but keep dependencies (2) | Delete this resource. If any dependencies exist, leave them in an unusable state. |
|  | Dependent Items Deleted returns whether resources other than the specified one were deleted. For example, this may happen if the resource is a simulated chassis that contained modules. |
|  | Resource out returns the resource that was deleted. If the call was successful, the only valid use of this resource is to call the Close VI. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the results of the VI execution. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/erase_firmware.html language=enus -->
## TOPIC 00016: Erase Firmware (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/erase_firmware.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/erase_firmware.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Erase Firmware (VI)

Installed With:

Removes the firmware image from the resource or target.

[IMAGE alt='Erase Firmware' src='erase_firmware.gif']

|  | Stop Tasks Automatically specifies to automatically end all tasks running on the target, even if they are incomplete and switch to firmware update mode. The default is TRUE. |
| --- | --- |
|  | Resource in is the resource from which you want to erase the firmware image. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits to initiate the firmware process before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. This timeout is for remote systems only. |
|  | Resource out returns basic information about the system resource. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the value returned in Firmware Status . |
|  | Firmware Status returns the status of the firmware update. If this parameter returns update pending user restart , call the Restart VI. If this parameter returns update pending user action , refer to Detailed Result for more information. |
|  | error out returns error information. This output provides standard error out functionality. |
|  | Previous Firmware Version is the firmware version you removed from the resource. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/export.html language=enus -->
## TOPIC 00017: Export (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/export.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/export.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Export (VI)

Installed With:

|  | Note This VI is a replacement for the deprecated MAX Copy Configuration. |
| --- | --- |

Use this VI to export configuration data from MAX into a file. Not all products are supported; consult your product documentation.

[IMAGE alt='Export' src='export.gif']

|  | Session in specifies the system from which to export configuration data. |
| --- | --- |
|  | Destination File specifies the destination where the data is copied. |
|  | Experts specifies a case-insensitive comma-separated string specifying which experts' data to copy. If Experts is unwired or blank, this VI copies all configuration data from the specified system. If you specify an expert name, this VI copies only that expert's data. The list of supported experts for a given system is returned from the Get System Experts VI. Note Examples of expert names include daqmx and ni-visa . For a listing of the available experts for this operation and the input strings to use, refer to KnowledgeBase article 5FFA2JBP . |
|  | Note Examples of expert names include daqmx and ni-visa . For a listing of the available experts for this operation and the input strings to use, refer to KnowledgeBase article 5FFA2JBP . |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Overwrite saves the new output file over an older file of the same name if TRUE. By default, this VI will not overwrite the file. |
|  | Session out returns the refnum for the system. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/feeds_subpalette.html language=enus -->
## TOPIC 00018: Feed Management VIs

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/feeds_subpalette.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/feeds_subpalette.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Feed Management VIs

**Owning Palette:** [Software Management VIs](software_subpalette.html)

**Requires:** NI System Configuration

The Feed Management subpalette contains VIs used to manage software feeds for a system. This requires Secure Shell Server (sshd) to be enabled on the target.

| Palette Object | Description |
| --- | --- |
| Get Software Feeds | Retrieves a list of software feeds installed on a system. |
| Add Software Feed | Adds a software feed to the system. |
| Modify Software Feed | Modifies an existing software feed by name. |
| Remove Software Feed | Removes an existing software feed by name. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/find_hardware.html language=enus -->
## TOPIC 00019: Find Hardware (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/find_hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/find_hardware.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Find Hardware (VI)

Installed With:

Returns a list of hardware in a specified system using the system's session refnum.

[IMAGE alt='Find Hardware' src='find_hardware.gif']

|  | Filter Mode specifies an enumerated list of filter modes. Filter Mode is ignored if Filter in is not wired. all values match (1) (default) includes all of the properties specified in the input filter. any value matches (2) includes any of the properties specified in the input filter. values do not match (3) includes none of the properties specified in the input filter. all properties exist (4) includes all of the properties specified in the input filter, regardless of the value of each property. |
| --- | --- |
| all values match (1) | (default) includes all of the properties specified in the input filter. |
| any value matches (2) | includes any of the properties specified in the input filter. |
| values do not match (3) | includes none of the properties specified in the input filter. |
| all properties exist (4) | includes all of the properties specified in the input filter, regardless of the value of each property. |
|  | Session in specifies the system being initialized. |
|  | Filter in specifies a user-defined refnum of system filter instance. The filter is used to limit the results to hardware matching specific properties. The default is no filter. Use the Create Filter VI and Filter Property Node to configure a new filter. |
|  | Experts specifies a case-insensitive comma-separated string specifying which experts to query. If Experts is unwired or blank, this VI queries all supported experts. The list of supported experts for a given system is returned from the Get System Experts VI. Note Examples of expert names include daqmx and ni-visa . For a listing of the available experts for this operation and the input strings to use, refer to KnowledgeBase article 5FFA2JBP . |
|  | Note Examples of expert names include daqmx and ni-visa . For a listing of the available experts for this operation and the input strings to use, refer to KnowledgeBase article 5FFA2JBP . |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. In some cases, the operation may take longer to complete. This timeout is for remote systems only. |
|  | Session out returns the refnum for the system. |
|  | Filter out returns the user-defined refnum for the system filter instance. |
|  | Resources out returns an array of references to hardware in the system. Call the Close (Hardware) VI on each reference when you no longer need it. Note This parameter may return some devices that were recently online even if they are no longer present. To determine if the device is present, you can use the Hardware Property Node to return the Devices & Chassis:Is Present property or make other application specific API calls. |
|  | Note This parameter may return some devices that were recently online even if they are no longer present. To determine if the device is present, you can use the Hardware Property Node to return the Devices & Chassis:Is Present property or make other application specific API calls. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/find_systems.html language=enus -->
## TOPIC 00020: Find Systems (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/find_systems.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/find_systems.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Find Systems (VI)

Installed With:

Retrieves a list of systems on the network.

[IMAGE alt='Find Systems' src='find_systems.gif']

|  | Device Class specifies the type of device for which you are searching. Common values are PXI and cRIO . To specify multiple classes, use a comma to separate the values. For a listing of the other available values and an explanation of the intended use, refer to KnowledgeBase article extu82 . |
| --- | --- |
|  | Detect Online Systems detects systems that are online. This option checks for all local online systems by default. (Real-Time) You must set this parameter to TRUE if you want to return RT targets that are in safe mode and RT targets that do not have NI System Configuration network support installed. (Windows) Set this parameter to FALSE if you only want to return previously detected results. Setting this parameter to FALSE still returns any current Real-Time targets that are in the Connected - Running system state that also have NI System Configuration network support installed. |
|  | Session in specifies the host that will detect the systems. The default is the local system. |
|  | Include Cached Results specifies whether to include cached results. This parameter only affects Windows operating systems. None (0) includes none of the cached results. Only if online (1) includes only the results from systems that are online. All (3) (default) includes all of the cached results. |
| None (0) | includes none of the cached results. |
| Only if online (1) | includes only the results from systems that are online. |
| All (3) | (default) includes all of the cached results. |
|  | Output specifies the preferred output format of the hostname and IP address for systems on the network. The Initialize Session VI accepts all of these formats. Note In some cases this parameter may return a system that is not in the requested format. For example, if you request the default hostname(IP) but an unconfigured system is detected, that system is returned as IP(MAC). Hostname (16) includes only the hostname. Hostname (IP) (18) (default) includes both the hostname and IP address. Hostname (MAC) (19) includes both the hostname and MAC address. IP (32) includes only the IP address. IP (Hostname) (33) includes both the IP address and hostname. IP (MAC) (35) includes both the IP address and MAC address. MAC (48) includes only the MAC address. MAC (Hostname) (49) includes both the MAC address and hostname. MAC (IP) (50) includes both the MAC address and the IP address. |
|  | Note In some cases this parameter may return a system that is not in the requested format. For example, if you request the default hostname(IP) but an unconfigured system is detected, that system is returned as IP(MAC). |
| Hostname (16) | includes only the hostname. |
| Hostname (IP) (18) | (default) includes both the hostname and IP address. |
| Hostname (MAC) (19) | includes both the hostname and MAC address. |
| IP (32) | includes only the IP address. |
| IP (Hostname) (33) | includes both the IP address and hostname. |
| IP (MAC) (35) | includes both the IP address and MAC address. |
| MAC (48) | includes only the MAC address. |
| MAC (Hostname) (49) | includes both the MAC address and hostname. |
| MAC (IP) (50) | includes both the MAC address and the IP address. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Timeout specifies the time in milliseconds that the VI waits before it times out. The default is 4 seconds. In some cases, the operation may take longer to time out. |
|  | Only Installable Systems detects only the systems that support the ability to install software remotely. This includes all Real-Time systems. |
|  | Session out returns the refnum for the system. |
|  | Detected Systems returns a list of systems detected on the network. Note This parameter may return some systems that were recently online even if they are no longer present on the network. To determine if the system is online, you can use the System Property Node to return the System Status property or make other application specific API calls. |
|  | Note This parameter may return some systems that were recently online even if they are no longer present on the network. To determine if the system is online, you can use the System Property Node to return the System Status property or make other application specific API calls. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/finding_systems_hardware.html language=enus -->
## TOPIC 00021: Finding Systems and Hardware

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/finding_systems_hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/finding_systems_hardware.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Finding Systems and Hardware

#### Create Filter VI

Use the [Create Filter Wrapper](create_filter_wrapper.html) VI to query for specific resources on a system. You can find the Create Filter Wrapper VI on the [Utilities](utilities_subpalette.html) subpalette.

#### Find Systems and Hardware

Use the [Find Systems](find_systems.html) VI to detect systems on the network. Use the [Find Hardware](find_hardware.html) VI to detect devices on a specified system. You can find these VIs on the [System Configuration](main_palette.html) palette.

To find a system, you can specify what types of systems you want, and you can specify the output format of each detected system. The output is an array and its entries can be wired to the [Initialize Session](initialize_session.html) VI and/or the [System Property Node](property_node_system.html).

You can also use the Find VI to find hardware (for example: devices and chassis). Specify what types of hardware you want by creating a filter using the Create Filter VI. The output is an array of resources that you can wire to the [Hardware Property Node](property_node_hardware.html) or any of the functions on the [Hardware Management](hardware_subpalette.html) subpalette.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/hardware_subpalette.html language=enus -->
## TOPIC 00022: Hardware Management VIs

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/hardware_subpalette.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/hardware_subpalette.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Hardware Management VIs

**Owning Palette:** [System Configuration VIs](main_palette.html)

**Requires:** NI System Configuration

The Hardware Management subpalette contains VIs used to control hardware on local and remote systems.

| Palette Object | Description |
| --- | --- |
| Erase Firmware | Removes the firmware image from the resource or target. |
| Hardware Property Node | Gets or sets properties on local or remote hardware systems. |
| Save Changes | Saves property changes on a system or device. |
| Rename Alias | Changes the display name of a resource. |
| Reset Resource | Executes reset on a specified resource and returns detailed results. |
| Self-Calibrate | Performs a self-calibration. Self-calibration adjusts the calibration constants with respect to an onboard reference stored on the device. |
| Self-Test | Verifies that system devices are able to perform basic I/O functions and returns detailed results. |
| Upgrade Firmware | Updates the firmware on the target. You can specify to update a file or the version. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/import.html language=enus -->
## TOPIC 00023: Import (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/import.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/import.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Import (VI)

Installed With:

Use this VI to import configuration data from a file into MAX. Not all products are supported; consult your product documentation.

[IMAGE alt='Import' src='import.gif']

|  | Session in specifies the system to which to import. |
| --- | --- |
|  | Source File specifies the configuration to copy. This input may point to a configuration file. To specify a configuration file, set Source to an existing file path. |
|  | Experts specifies a case-insensitive comma-separated string specifying which experts' data to copy. If Experts is unwired or blank, this VI copies all configuration data from the specified configuration file. If you specify an expert name, this VI copies only that expert's data. The list of supported experts for a given system is returned from the Get System Experts VI. Note Examples of expert names include daqmx and ni-visa . For a listing of the available experts for this operation and the input strings to use, refer to KnowledgeBase article 5FFA2JBP . |
|  | Note Examples of expert names include daqmx and ni-visa . For a listing of the available experts for this operation and the input strings to use, refer to KnowledgeBase article 5FFA2JBP . |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Import Mode specifies how to treat existing data at the destination. Merge (0) (default) Merges the source data in with any existing data at the destination. The source wins by default in the case of overwrite conflicts. Replace all (1048576) Replaces all configuration data at the destination with the source data. Preserve existing (2097152) Preserves the original data. The destination wins by default in the case of overwrite conflicts. ExampleFor this example, consider an initial configuration state with items A1 and B. The configuration file from which you are importing data includes items A2 and C. In this case, it is the same item A with different configuration data. Action Result Merge A2, B, C Replace all A2, C Preserve existing A1, B, C |
| Merge (0) | (default) Merges the source data in with any existing data at the destination. The source wins by default in the case of overwrite conflicts. |
| Replace all (1048576) | Replaces all configuration data at the destination with the source data. |
| Preserve existing (2097152) | Preserves the original data. The destination wins by default in the case of overwrite conflicts. |
| Action | Result |
| Merge | A2, B, C |
| Replace all | A2, C |
| Preserve existing | A1, B, C |
|  | Session out returns the refnum for the system. |
|  | Detailed Result returns a list of items that were imported or the results of any errors that occurred during the VI execution. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/import_export_concept.html language=enus -->
## TOPIC 00024: Deploying System Images

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/import_export_concept.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/import_export_concept.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Deploying System Images

#### Import and Export VIs

Use the [Import](import.html) VI to import system configuration data from a file into Measurement & Automation Explorer (MAX.) Use the [Export](export.html) VI to export system configuration data from MAX into a file. MAX is not required to use these VIs. You can find both VIs on the [Utilities](utilities_subpalette.html) subpalette.

#### Save and Load System Image

Use the [Create System Image](create_system_image.html) VI to save an image file or folder, which is a copy of the file contents set up on the primary hard drive of a system. Apply the image to a system using the [Set System Image](set_system_image.html) VI. You can find these VIs on the [Software Management](software_subpalette.html) subpalette.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/initialize_concept.html language=enus -->
## TOPIC 00025: Initialize

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/initialize_concept.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/initialize_concept.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Session VI

Use the [Initialize Session](initialize_session.html) VI to initialize any system configuration VI. Unless specified otherwise, the VI selects the local system. Provide a username and password to gain access to a remote system. Wire the Initialize Session VI to other system configuration VIs to enable them to operate on your specified target system. You can find this VI on the [System Configuration](main_palette.html) palette.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/install_all.html language=enus -->
## TOPIC 00026: Install All (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/install_all.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/install_all.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Install All (VI)

Installed With:

Use the Install All VI to install the highest installable version of all available components, even if the component(s) are already installed on the target.

[IMAGE alt='Install All' src='install_all.gif']

|  | Restart Automatically restarts the system into install mode by default before the operation is performed, and restarts back to a running state after the operation is complete. If you choose not to restart automatically, the operation will fail if the system is not already in install mode. |
| --- | --- |
|  | Session in specifies the IP address or hostname of the system on which to perform this operation. When left blank, this VI operates on the local system. |
|  | Deselect Conflicts specifies whether to deselect conflicting software components automatically. Select TRUE to deselect the conflicting software components. By default, conflicting software components will still be installed. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Session out returns the refnum for the system. |
|  | Installed Software returns a list of installed software components. title is the title of the software component. description is a short description of the software component. ID is the unique identifier for the software component. version is the version of the software component. component type is the component type. Components can be standard, hidden, system, unknown, startup, image, or essential. |
|  | title is the title of the software component. |
|  | description is a short description of the software component. |
|  | ID is the unique identifier for the software component. |
|  | version is the version of the software component. |
|  | component type is the component type. Components can be standard, hidden, system, unknown, startup, image, or essential. |
|  | Broken Dependencies returns a list of broken dependencies, which are specific software components that cannot operate without another software component installed. This array will be empty when an installation succeeds. Depender is the software component that requires another software component (the dependee ) to install and operate correctly. title is the title of the software components. description is a short description of the software components. ID is the unique identifier for the software components. version is the version of the software components. component type is the component type. Components can be standard, hidden, system, unknown, startup, image, or essential. Dependee is the software component that must be present for the depender to install and operate correctly. title is the title of the software components. description is a short description of the software components. ID is the unique identifier for the software components. version is the version of the software components. component type is the component type. Components can be standard, hidden, system, unknown, startup, image, or essential. |
|  | Depender is the software component that requires another software component (the dependee ) to install and operate correctly. title is the title of the software components. description is a short description of the software components. ID is the unique identifier for the software components. version is the version of the software components. component type is the component type. Components can be standard, hidden, system, unknown, startup, image, or essential. |
|  | title is the title of the software components. |
|  | description is a short description of the software components. |
|  | ID is the unique identifier for the software components. |
|  | version is the version of the software components. |
|  | component type is the component type. Components can be standard, hidden, system, unknown, startup, image, or essential. |
|  | Dependee is the software component that must be present for the depender to install and operate correctly. title is the title of the software components. description is a short description of the software components. ID is the unique identifier for the software components. version is the version of the software components. component type is the component type. Components can be standard, hidden, system, unknown, startup, image, or essential. |
|  | title is the title of the software components. |
|  | description is a short description of the software components. |
|  | ID is the unique identifier for the software components. |
|  | version is the version of the software components. |
|  | component type is the component type. Components can be standard, hidden, system, unknown, startup, image, or essential. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/reset_resource.html language=enus -->
## TOPIC 00027: Reset Resource (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/reset_resource.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/reset_resource.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Reset Resource (VI)

Installed With:

Executes reset on a specified resource. By default, it reinitializes the hardware to its power-on state.

[IMAGE alt='Reset Resource' src='reset_resource.gif']

|  | Resource in is the resource object refnum returned from the Find Hardware VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. In some cases, the operation may take longer to complete. This timeout is for remote systems only. |
|  | Reset Mode specifies how to reset the specified resource. reinitialize hardware (0) (default) Resets the hardware to its power-on state. This fully reinitializes the device. If the device had exceeded a threshold such as the temperature operating range, this operation clears that status. clear software settings (1) Resets the software settings for this item to the initial configuration state. If the item supports the Rename Alias operation, this mode changes the alias to the value this item would have if it were only now being added to the system. If configuring this device caused the creation of dependent child items which cannot exist standalone, this mode will delete those dependent items. |
| reinitialize hardware (0) | (default) Resets the hardware to its power-on state. This fully reinitializes the device. If the device had exceeded a threshold such as the temperature operating range, this operation clears that status. |
| clear software settings (1) | Resets the software settings for this item to the initial configuration state. If the item supports the Rename Alias operation, this mode changes the alias to the value this item would have if it were only now being added to the system. If configuring this device caused the creation of dependent child items which cannot exist standalone, this mode will delete those dependent items. |
|  | Dependent Items Deleted returns whether resources other than the specified one were deleted. For example, this may happen if the resource is a simulated chassis that contained modules. |
|  | Resource out returns basic information about the system resource. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the results of the VI execution. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/reset_restart.html language=enus -->
## TOPIC 00028: Reset and Restart

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/reset_restart.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/reset_restart.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Reset and Restart

The System Configuration API provides two VIs, [Reset Resource](reset_resource.html) and [Restart](restart.html), that allow you to return your device or system to a known initialized state.

Use the [Reset Resource](reset_resource.html) VI to restore a hardware target to its previous state.

Use the [Restart](restart.html) VI to reboot a system.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/restart.html language=enus -->
## TOPIC 00029: Restart (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/restart.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/restart.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Restart (VI)

Installed With:

Reboots a system or network device.

[IMAGE alt='Restart' src='restart.gif']

|  | Wait Until Complete waits until the reboot has finished before the VI operation is completed, by default. Select FALSE to not wait until the reboot is finished before the VI completes its operation. |
| --- | --- |
|  | Session in specifies the system being rebooted. |
|  | Install Mode does not reboot the system into install mode by default. To reboot into install mode, select TRUE. |
|  | Flush DNS does not clear the DNS cache by default. DNS clients temporarily store system hostnames. Flushing the DNS allows you to clear those names from the memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Timeout specifies the time in seconds that the VI waits to establish a connection before it returns an error. The default is 3 minutes. |
|  | Session out returns the refnum for the system. |
|  | New IP Address returns the new IP address of the rebooted system. This may differ from the previous IP address if the system acquires a different IP address from the DHCP server. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/save_changes.html language=enus -->
## TOPIC 00030: Save Changes (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/save_changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/save_changes.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Save Changes (VI)

Installed With:

Saves changes made to hardware and systems.

#### Save Changes (Hardware)

Writes and saves property changes on a device. Save Changes (Hardware) VI wires into the Hardware Property node where property changes are selected.

[IMAGE alt='Save Changes (Hardware)' src='save_changes_(hardware).gif']

|  | Resource in specifies the resource receiving property changes. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. In some cases, the operation may take longer to complete. This timeout is for remote systems only. |
|  | Resource out returns basic information about the system resource. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the results of the VI execution. |
|  | Changes Require Restart returns whether the changes require a reboot to take effect. If TRUE, run the Restart VI. |
|  | error out returns error information. This output provides standard error out functionality. |

#### Save Changes (System)

Writes and saves property changes on a system. Save Changes (System) VI wires into the System Property node where property changes are selected.

[IMAGE alt='Save Changes (System)' src='save_changes_(system).gif']

|  | Session in specifies the system receiving changes. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. In some cases, the operation may take longer to complete. This timeout is for remote systems only. |
|  | Session out returns the refnum for the system. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the results of the VI execution. |
|  | Changes Require Restart returns whether the changes require a reboot to take effect. If TRUE, run the Restart VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/self-calibrate.html language=enus -->
## TOPIC 00031: Self-Calibrate (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/self-calibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/self-calibrate.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Self-Calibrate (VI)

Installed With:

Performs a self-calibration on a device. Self-calibration adjusts the calibration constants with respect to an onboard reference stored on the device. The new calibration constants are defined with respect to the calibration constants created during an external calibration to ensure that the measurements are traceable to these external standards. The new calibration constants do not affect the constants created during an external calibration because they are stored in a different area of the device memory. You can perform a self-calibration at any time to adjust the device for use in environments other than those in which the device was externally calibrated.

[IMAGE alt='Self-Calibrate' src='self-calibrate.gif']

|  | Resource in is the resource object refnum returned from the Find Hardware VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. In some cases, the operation may take longer to complete. This timeout is for remote systems only. |
|  | Resource out returns basic information about the system resource. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the results of the VI execution. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/self-test.html language=enus -->
## TOPIC 00032: Self-Test (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/self-test.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Self-Test (VI)

Installed With:

Verifies that system devices can perform basic I/O functions. Ensure that no other tasks are running on the system while the self-test executes because the driver may need exclusive access to some device resources.

You can select from three modes that provide different levels of self-test functionality. The mode you select might require you to disconnect cables from the device. For details about each mode, refer to the description for the **Self-Test Mode** input.

[IMAGE alt='Self-Test' src='self-test.gif']

|  | Resource in is the resource object refnum returned from the Find Hardware VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. In some cases, the operation may take longer to complete. This timeout is for remote systems only. |
|  | Self-Test Mode specifies the type of self-test to perform. For hardware without intermediate or full self-test functionality, this VI executes a basic self-test regardless of the requested mode. basic (0) (default) A basic self-test should complete in under 3 seconds and does not require you to disconnect devices from external equipment because the states of I/O lines are maintained throughout the test. At minimum, a basic self-test verifies host-device communication (for example: validation of device registers). intermediate (1) An intermediate self-test should complete in under 30 seconds and try to verify as much I/O as possible using internal loop-backs. This does not require you to disconnect devices from external equipment because the states of I/O lines are maintained throughout the test. full (2) A full self-test verifies as much I/O as possible and takes longer to complete. This advanced test is used to perform the most exhaustive diagnostic possible. This mode requires you to disconnect external I/O signals before starting the operation. |
| basic (0) | (default) A basic self-test should complete in under 3 seconds and does not require you to disconnect devices from external equipment because the states of I/O lines are maintained throughout the test. At minimum, a basic self-test verifies host-device communication (for example: validation of device registers). |
| intermediate (1) | An intermediate self-test should complete in under 30 seconds and try to verify as much I/O as possible using internal loop-backs. This does not require you to disconnect devices from external equipment because the states of I/O lines are maintained throughout the test. |
| full (2) | A full self-test verifies as much I/O as possible and takes longer to complete. This advanced test is used to perform the most exhaustive diagnostic possible. This mode requires you to disconnect external I/O signals before starting the operation. |
|  | If TRUE, Prompt if Full Mode will show a dialog box prompting the user to disconnect the device from external signals before beginning a full self-test. If the mode is basic or intermediate , this input is ignored. |
|  | Resource out returns basic information about the system resource. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the results of the VI execution. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/self_test_calibrate.html language=enus -->
## TOPIC 00033: Self-Test and Self-Calibrate

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/self_test_calibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/self_test_calibrate.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Self-Test and Self-Calibrate VIs

Use the [Self-Calibrate](self-calibrate.html) VI to perform self-calibration on a device. Self-calibration adjusts the calibration constants with respect to an onboard reference stored on the device. The new calibration constants are defined with respect to the calibration constants created during an external calibration to ensure that the measurements are traceable to these external standards. The new calibration constants do not affect the constants created during an external calibration because they are stored in a different area of the device memory. You can perform a self-calibration at any time to adjust the device for use in environments other than those in which the device was externally calibrated.

|  | NotesExternal calibration must be performed by a metrology laboratory or another facility that maintains traceable calibration standards. For more information, visit ni.com/calibration. Disconnect or disable any AC input signals before starting self-calibration. AC or varying signals can cause self-calibration to fail or compromise the accuracy of the calibration. Some device types (for example, SCXI modules) do not support self-calibration. Refer to the NI-DAQmx documentation to determine which devices can be self-calibrated. |
| --- | --- |

|  | Tip The analog output channels on E Series devices fluctuate during self-calibration, so you might need to disconnect the AO channels before self-calibration. |
| --- | --- |

Use the [Self-Test](self-test.html) VI to verify that system devices are able to perform basic I/O functions. No other tasks should run on the system while executing the self test because the driver may need exclusive access to some device resources. You do not need to disconnect devices from external equipment because the state of I/O lines are maintained throughout the test.

You can find these VIs on the [Hardware Management](hardware_subpalette.html) subpalette.

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/set_time.html language=enus -->
## TOPIC 00034: Set Time (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/set_time.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/set_time.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Set Time (VI)

Installed With:

Sets the current time and/or time zone on the specified system.

|  | Note This function is not intended for synchronization of multiple real-time devices. Refer to the Choosing a CompactRIO Synchronization Technology white paper for information on the synchronization of multiple real-time devices. |
| --- | --- |

[IMAGE alt='Set Time' src='set_time.gif']

|  | Session in specifies the system receiving changes. |
| --- | --- |
|  | Time specifies the current time for a remote system or network device. Use the default timestamp to leave the current time unchanged. LabVIEW calculates this timestamp using the number of seconds elapsed since 12:00 a.m., Friday, January 1, 1904, Universal Time. |
|  | Time Zone specifies the time zone for a remote system or network device. Use an empty string to leave the current time zone unchanged. For a complete list of supported time zone strings by city, refer to the Date and Time Gateway by visiting ni.com/info and entering the Info Code exiyy5 . The following table includes example cities and their corresponding time zone string: City Time zone string Algiers Africa/Algiers Cairo Africa/Cairo Chicago America/Chicago Dubai Asia/Dubai Dublin Europe/Dublin Guam Pacific/Guam Lima America/Lima Madrid Europe/Madrid Maldives Indian/Maldives Perth Australia/Perth Reykjavik Atlantic/Reykjavik Note If your target does not support automatic daylight saving time adjustment, specify the GMT time equivalent for your location instead of the actual time zone. Otherwise, data timestamps may be inaccurate. |
| City | Time zone string |
| Algiers | Africa/Algiers |
| Cairo | Africa/Cairo |
| Chicago | America/Chicago |
| Dubai | Asia/Dubai |
| Dublin | Europe/Dublin |
| Guam | Pacific/Guam |
| Lima | America/Lima |
| Madrid | Europe/Madrid |
| Maldives | Indian/Maldives |
| Perth | Australia/Perth |
| Reykjavik | Atlantic/Reykjavik |
|  | Note If your target does not support automatic daylight saving time adjustment, specify the GMT time equivalent for your location instead of the actual time zone. Otherwise, data timestamps may be inaccurate. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. In some cases, the operation may take longer to complete. This timeout is for remote systems only. |
|  | Session out returns the refnum for the system. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the results of the VI execution. |
|  | Changes Require Restart returns whether the changes require a reboot to take effect. If TRUE, run the Restart VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/status_codes.html language=enus -->
## TOPIC 00035: System Configuration VI Status Codes

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/status_codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/status_codes.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### System Configuration VI Status Codes

The [System Configuration VI](main_palette.html) functions and methods can return the following status codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| -2147467263 | This operation is not implemented for this target or resource. |
| -2147467261 | A required pointer parameter was NULL. |
| -2147467259 | Miscellaneous operation failure. |
| -2147418113 | A critical unexpected error occurred. Please report this error to NI. |
| -2147220592 | Failed transmitting data to or from the web server at the specified target address. |
| -2147220591 | The NI System Configuration API at the specified target address could not decrypt the data. |
| -2147220624 | The property already exists with a different type or value. |
| -2147220623 | The property does not exist for this resource. |
| -2147220622 | The name of the target or expert contains illegal characters. Each label of the hostname must be between 1 and 63 characters long, and the entire hostname, including delimiting dots, must be 255 characters or less. |
| -2147220621 | Could not contact the System Configuration API at the specified target address. |
| -2147220620 | A specified expert is not installed. |
| -2147220619 | The specified resource name does not exist. |
| -2147220618 | The specified mode is invalid. |
| -2147220616 | The System Configuration API is not installed on the specified target. |
| -2147220614 | The suggested name contains illegal characters. |
| -2147220613 | Another resource already has the suggested name. |
| -2147220612 | None of the changed properties can be validated. |
| -2147220611 | Username or password is incorrect. |
| -2147220610 | The resource being renamed has dependencies, and the updateDependencies flag was false. |
| -2147220609 | A property contained a value that is not valid or is out of range. |
| -2147220608 | Multiple properties contained values that are inconsistent with each other. |
| -2147220607 | The operation was canceled. |
| -2147220606 | Could not parse the response from the NI System Configuration API at the specified target address. |
| -2147220605 | The resource name is valid but the operation requires the resource to be present. |
| -2147220604 | The resource name is valid but the operation is not supported on simulated resources. |
| -2147220603 | The resource requires being in the firmware update state to perform this operation. |
| -2147220602 | The uploaded firmware image does not work with this resource. |
| -2147220601 | The uploaded firmware image is corrupt or incomplete. |
| -2147220600 | The specified firmware version does not exist. |
| -2147220599 | The specified firmware version is older than what is currently installed. |
| -2147220598 | The username or password is invalid. |
| -2147220597 | The specified firmware was not successfully installed. See the output parameters for more information. |
| -2147220596 | The data could not be encrypted. |
| -2147220595 | The changes were not saved. Some of the modified properties were not validated because they do not apply to this item. |
| -2147220594 | The calibration password is incorrect. |
| -2147220593 | Could not delete the specified resource because it is present. |
| -2147220592 | Failed transmitting data to or from the web server at the specified target address. |
| -2147220591 | The NI System Configuration API at the specified target address could not decrypt the data. |
| -2147220590 | The specified firmware requires a newer version of the expert than what is currently installed. |
| -2147220589 | There was uncertainty regarding what action to take during an import. |
| -2147220588 | A required item could not be imported. |
| -2147220587 | Could not perform the specified operation because the item is currently in use. |
| -2147220586 | Could not perform the specified operation because the item type is unknown or not supported. |
| -2147220560 | Unable to write to file. Permission denied. |
| -2147220559 | Unable to connect to the specified system. Ensure that the system is online. |
| -2147220558 | Error running transform to generate report. |
| -2147220557 | Unable to find NI MAX on the system. Please re-install. |
| -2147220556 | Unexpected error launching nimax.exe. |
| -2147220555 | Launched nimax.exe but it did not complete in a reasonable time. |
| -2147220554 | Unable to find XSL transform to generate report. |
| -2147220553 | Incorrect report file extension provided. |
| -2147220552 | Report file is read-only. Unable to generate report. |
| -2147220551 | Report file exists and the NIMAX_FailIfOverwritingReport flag was set. |
| -2147220550 | Error creating directory for report files. |
| -2147220480 | Error opening a file. |
| -2147220479 | The object cannot be accessed because of insufficient permissions. |
| -2147220478 | Error with the object copier. |
| -2147220477 | Error performing a file operation. |
| -2147220476 | Names from one expert have collided with another expert. |
| -2147220475 | Unexpected error has happened. |
| -2147220474 | The expert requested its stream for import but we could not give it one because it didn't export a stream. |
| -2147220473 | Error compressing or decompressing file. |
| -2147220472 | Error reading from a stream. |
| -2147220471 | Error writing to a stream. |
| -2147220470 | Error seeking to a position in a stream. |
| -2147220469 | Repository not ready to be exported. |
| -2147220468 | The file or stream chosen to import the repository from is not a valid repository. |
| -2147220467 | The repository was exported with a newer version of MAX than what is on the importing machine. |
| -2147220466 | The import storage could not be opened. |
| -2147220465 | The export storage could not be created. |
| -2147220464 | The object copier could not be created. |
| -2147220463 | A PortCfg operation is already in progress. |
| -2147220462 | The custom file doesn't belong to a given expert. |
| -2147220461 | A specified system is not supported by this expert. |
| -2147220460 | A specified system is presumably supported, but network errors prevent connection. |
| -2147220459 | The product is not installed on the specified system. |
| -2147220458 | The product is installed on the remote system, but is too old. |
| -2147220457 | The product is installed on the remote system, but is too new. |
| -2147220456 | The import data is too old. The product is not backward-compatible with this data. |
| -2147220455 | The import data is too new. The product is not forward-compatible with this data. |
| -2147220454 | The operation failed because no source items were specified. |
| -2147220453 | The operation failed because some items were orphans. |
| -2147220452 | The operation failed because some items were in-edit and not saved. |
| -2147220451 | The operation failed because it would overwrite a file. |
| -2147220450 | The operation failed because it would overwrite items. |
| -2147220449 | The operation failed because of missing dependency items. |
| -2147220448 | The operation timed out. |
| -2147220447 | The operation was canceled by the client. |
| -2147220446 | The operation failed because of warning conflicts. |
| -2147220445 | The operation failed because of conflicts, in general. |
| -2147220444 | The operation failed because of unresolved conflicts requiring user input. |
| -2147220443 | An expert is not ready to accept the specified source or destination, but may become ready in the future. |
| -2147220442 | The operation failed because some files were orphans. |
| -2147220441 | Caller called a non-const method on an object that is logically const. |
| -2147220440 | An expert does not support the attempted copy mode (e.g. merge to file, etc) . |
| -2147220385 | The target requires newer functionality not supported by the software on your computer. Update NI System Configuration to the latest version to configure this target. See www.ni.com/r/rtconfigerror for more information. |
| -2147220384 | Running 'opkg update' failed to access at least one enabled feed. Consider disabling unnecessary feeds. |
| -2147220383 | The specified software feed was not found. |
| -2147220382 | Could not add the specified software feed because it already exists. |
| -2147220381 | The target does not support one of the specified installation options. |
| -2147220380 | The target does not include the functionality this operation requires. Update the firmware to the latest version. |
| -2147220379 | The target does not include the functionality this operation requires. Update the software to the latest version. |
| -2147220378 | SSH must be enabled on the target. |
| -2147220377 | Could not parse the response from opkg at the specified target address. |
| -2147220376 | The specified software set is the wrong type for this operation. |
| -2147220375 | The target requires using opkg to modify installed software. |
| -2147220374 | Disk encryption is not supported by the target. |
| -2147220373 | Could not find a device suitable for storing the encrypted disk recovery key. Format a USB drive with the appropriate filesystem label and insert it into the target. |
| -2147220372 | To restart your system, either specify 'localhost' on the front panel for Session in, or call Initialize Session first. |
| -2147220371 | The image is corrupt or the file type is invalid. |
| -2147220370 | Can only perform this action in safe or install mode, and the 'auto restart' flag was false. |
| -2147220369 | The encryption passphrase when applying an image was not the same as when the image was created. |
| -2147220368 | The IP address is invalid. |
| -2147220367 | The gateway address is invalid. |
| -2147220366 | The DNS server address is invalid. |
| -2147220365 | The subnet mask is invalid. |
| -2147220364 | The specified target does not support this operation or property. |
| -2147220363 | The remote system failed to configure. |
| -2147220362 | The remote system is locked. A password is required to configure. |
| -2147220361 | Incorrect password. |
| -2147220360 | The remote device is not configurable for some reason other than password. |
| -2147220359 | Failed to unlock the system. |
| -2147220358 | Failed to lock the system. |
| -2147220357 | General installation failure. |
| -2147220356 | Installation files were corrupt or not found in the repository. |
| -2147220355 | The installation file is empty. |
| -2147220354 | The system must have a valid IP address before certain operations such as installation. The IP address cannot be 0.0.0.0. |
| -2147220352 | General install error. |
| -2147220350 | Installation to the specified target has already begun. Only one installation can be performed at a time. |
| -2147220349 | Remote action aborted. |
| -2147220338 | Hard drive on the remote system is either full or has encountered an I/O error. |
| -2147220337 | Hard drive format failed. The disk on the target may be unrecoverable. |
| -2147220336 | System must be in safe mode before attempting a hard drive format. Restart the target into safe mode and attempt the command again. |
| -2147220335 | System failed to restart after the hard drive was formatted. The system is in an unknown state. You may have to manually restart the target. |
| -2147220334 | The server refused the network connection. |
| -2147220331 | Failed to get one or more files while creating system image. The image is incomplete or invalid. |
| -2147220330 | Failed to put one or more files while applying system image. The system may be in a corrupt state. |
| -2147220329 | The specified path does not contain a valid image. |
| -2147220328 | The image is incompatible with the target. |
| -2147220327 | The image was not created from the specified target. |
| -2147220326 | The requested file system is not supported on the specified target. |
| -2147220325 | The specified target does not support custom software installations. |
| -2147220324 | A file transfer error (FTP or WebDAV) occurred. |
| -2147220323 | Operation timed out. |
| -2147220322 | The specified file was not found. |
| -2147220321 | Directory not found. |
| -2147220320 | The specified file or directory path was not found. |
| -2147220319 | No software is available for installation to this target. |
| -2147220318 | The file or directory exists and the overwrite flag was false. |
| -2147220317 | Cannot keep configuration after formatting HD. This option is supported only for targets on the local subnet. |
| -2147220316 | Filename or pathname is too long. |
| -2147220315 | Failed when communicating with the system. This issue is usually caused by a high latency in the network. Refer to KnowledgeBase article 42GH3O00 on ni.com for possible solutions. |
| -2147220314 | The operation failed because of insufficient permissions. |
| -2147220313 | The operation failed because the path already exists. |
| -2147220312 | The execution of an external command, script, or application failed. |
| -2147220311 | Failed to download the file from the RT image repository. |
| -2147220309 | Failure to send command. |
| -2147220308 | Could not contact remote host. |
| -2147220307 | Could not access network. |
| -2147220306 | Command was not confirmed, result of operation is uncertain. |
| -2147220305 | Hostname could not be resolved by DNS. |
| -2147220304 | Timeout while waiting for restart. The system is offline. |
| -2147220303 | The sending new configuration operation returned a failure. However, the operation might not have failed. |
| -2147220300 | Cannot install more than one startup component. |
| -2147220299 | Invalid argument. |
| -2147220298 | Cannot uninstall a specified software component from the target because there are dependencies. |
| -2147220297 | Cannot install multiple packages of the same component. |
| -2147220296 | Cannot install a specified software component to the target because there are dependencies. |
| -2147220295 | A specified software component is incompatible with this target. |
| -2147220294 | A specified software component is incompatible with this target's operating system. |
| -2147220293 | A firmware update is required before installing. |
| -2147220292 | Cannot open file or folder. |
| -2147220291 | Duplicate or missing components on target installation. |
| -2147220290 | Buffer overflow, size is too small. |
| -2147220289 | The software installed on the target uses a CDF format not supported by the software on your computer. Update NI System Configuration or NI MAX to the latest version to configure this target. |
| -2147220288 | The specified software set is invalid and cannot be installed to the target. |
| -2147220287 | The specified software set definition is incomplete and cannot be installed to the target. Some hidden dependencies were added. |
| -2147220286 | One or more software set items could not be found in the repository. |
| -2147220285 | There is a top-level hidden component installed. |
| -2147220284 | A component was passed in that is not an installable add-on. It may be an unknown ID, a defined item that is not an add-on, a missing add-on, or a non-installable add-on. |
| -2147220283 | Could not find the 'RT Images' repository location. |
| -2147220282 | Could not read the 'RT Images' registry key. |
| -2147220281 | Could not find the rts2cdf conversion utility. |
| -2147220280 | The operating system is not supported. |
| -2147220279 | Unspecified version while trying to install exact version of a component. |
| -2147220278 | Unsupported MAC address format. Supply the MAC address as a colon separated string of characters instead of Hex display. |
| -2147220277 | A component was passed in that is not a startup. |
| -2147024882 | Out of memory. |
| -2147024809 | Invalid parameter. |
| 263024 | The expert performed a basic self-test because it does not implement the specified mode. |
| 263168 | Initialization succeeded but the target is offline. Only cached system properties are available. |
| 263169 | For the local system, the option to wait until the restart is complete is ignored. The function has successfully initiated a restart with the operating system. |
| 263170 | The requested property value was changed in this session but the change was not successfully validated and saved. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/system_name_constant.html language=enus -->
## TOPIC 00036: System Name Constant

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/system_name_constant.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/system_name_constant.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### System Name Constant

Installed With:

Use this constant to specify a system as an input to NI System Configuration VIs.

Right-click the constant and choose **I/O Name Filtering** from the shortcut menu to select which types of systems to display.

[IMAGE alt='System Name Constant' src='system_name_constant.gif']

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/uninstall_all.html language=enus -->
## TOPIC 00037: Uninstall All (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/uninstall_all.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/uninstall_all.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Uninstall All (VI)

Installed With:

This VI allows you to uninstall all Real-Time software from a system.

[IMAGE alt='Uninstall All' src='uninstall_all.gif']

|  | Restart Automatically restarts the system into install mode by default before the operation is performed, and restarts back to safe mode after the operation is complete. If you choose not to restart automatically, the operation will fail if the system is not already in install mode. |
| --- | --- |
|  | Session in specifies the IP address or hostname of the system on which to perform this operation. When left blank, this VI operates on the local system. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Session out returns the refnum for the system. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/update_calibration.html language=enus -->
## TOPIC 00038: Update Calibration (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/update_calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/update_calibration.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Update Calibration (VI)

Installed With:

Updates the external calibration information for a device. You can only use this VI to update calibration information if the Supports Calibration Write property is TRUE.

#### Update Calibration (Date)

Updates the external calibration information for a device. You can only use this VI to update calibration information if the Supports Calibration Write property is TRUE.

[IMAGE alt='Update Calibration (Date)' src='update_calibration_(date).gif']

|  | New Calibration Password specifies a new calibration password for this device. To leave the current password unchanged, do not specify a value for this parameter. |
| --- | --- |
|  | Calibration Password specifies the current calibration password for this device. |
|  | Resource in specifies the resource receiving property changes. |
|  | Calibration Date specifies the date and time of the last external calibration. Use the default timestamp to leave the current time unchanged. LabVIEW calculates this timestamp using the number of seconds elapsed since 12:00 a.m., Friday, January 1, 1904, Universal Time. |
|  | Calibration Due Date specifies the due date for the next external calibration. Use the default timestamp to clear the due date. LabVIEW calculates this timestamp using the number of seconds elapsed since 12:00 a.m., Friday, January 1, 1904, Universal Time. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. In some cases, the operation may take longer to complete. This timeout is for remote systems only. |
|  | Resource out returns a copy of the resource reference. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the results of the VI execution. |
|  | error out returns error information. This output provides standard error out functionality. |

#### Update Calibration (Months)

Updates the external calibration date in months for a device. You can only use this VI to update calibration information if the Supports Calibration Write property is TRUE.

[IMAGE alt='Update Calibration (Months)' src='update_calibration_(months).gif']

|  | New Calibration Password specifies a new calibration password for this device. To leave the current password unchanged, do not specify a value for this parameter. |
| --- | --- |
|  | Calibration Password specifies the current calibration password for this device. |
|  | Resource in specifies the resource receiving property changes. |
|  | Calibration Date specifies the date and time of the last external calibration. Use the default timestamp to leave the current time unchanged. LabVIEW calculates this timestamp using the number of seconds elapsed since 12:00 a.m., Friday, January 1, 1904, Universal Time. |
|  | Interval in Months specifies the time, in months, until the next due date for an external calibration. Use the default value of -1 to use the manufacturer-recommended calibration interval for this device. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. In some cases, the operation may take longer to complete. This timeout is for remote systems only. |
|  | Resource out returns a copy of the resource reference. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the results of the VI execution. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/upgrade_firmware.html language=enus -->
## TOPIC 00039: Upgrade Firmware (VI)

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/upgrade_firmware.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/upgrade_firmware.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Upgrade Firmware (VI)

Installed With:

Updates the firmware on the target. You can specify to update a file or the version.

#### Upgrade Firmware (File)

Updates the firmware on the target using a firmware file on the local computer.

[IMAGE alt='Upgrade Firmware (File)' src='upgrade_firmware_(file).gif']

|  | Stop Tasks Automatically specifies to automatically end all tasks running on the target, even if they are incomplete and switch to firmware update mode. The default is TRUE. |
| --- | --- |
|  | Resource in specifies the resource to be changed. |
|  | Firmware File specifies the name and location of the firmware file on the local computer. |
|  | Always Overwrite specifies to overwrite the destination firmware image even if the version is the same as or older than the version of the destination firmware image. If FALSE, the function checks the version of the firmware and returns an error if the current version is newer than the version to which you are upgrading. If the firmware version is the same and this parameter is set to FALSE, the VI does not upgrade the firmware and returns success. If TRUE, this VI automatically upgrades the firmware, regardless of the version of the destination firmware image. By default, this VI will overwrite the firmware image only if the specified version is newer. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits to initiate the firmware process before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. This timeout is for remote systems only. |
|  | Resource out returns basic information about the system resource. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the value returned in Firmware Status . |
|  | Firmware Status returns the status of the firmware update. If this parameter returns update pending user restart , call the Restart VI. If this parameter returns update pending user action , refer to Detailed Result for more information. |
|  | error out returns error information. This output provides standard error out functionality. |

#### Upgrade Firmware (Version)

Updates the firmware on the target to a specific version.

[IMAGE alt='Upgrade Firmware (Version)' src='upgrade_firmware_(version).gif']

|  | Stop Tasks Automatically specifies to automatically end all tasks running on the target, even if they are incomplete and switch to firmware update mode. The default is TRUE. |
| --- | --- |
|  | Resource in specifies the resource to be changed. |
|  | Firmware Version specifies the firmware version you want to apply to the target. |
|  | Always Overwrite specifies to overwrite the destination firmware image even if the version is the same as or older than the version of the destination firmware image. If FALSE, the function checks the version of the firmware and returns an error if the current version is newer than the version to which you are upgrading. If the firmware version is the same and this parameter is set to FALSE, the VI does not upgrade the firmware and returns success. If TRUE, this VI automatically upgrades the firmware, regardless of the version of the destination firmware image. By default, this VI will overwrite the firmware image only if the specified version is newer. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Remote Timeout specifies the time in milliseconds that this VI waits to initiate the firmware process before it times out. The default amount of time that the VI waits for a response on the network before timing out is 5 minutes. This timeout is for remote systems only. |
|  | Resource out returns basic information about the system resource. |
|  | Detailed Result returns a string containing results of any errors that may have occurred during the VI execution. This parameter also may return additional information about the value returned in Firmware Status . |
|  | Firmware Status returns the status of the firmware update. If this parameter returns update pending user restart , call the Restart VI. If this parameter returns update pending user action , refer to Detailed Result for more information. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-system-configuration-lv-ref path=nisyscfg/utilities_subpalette.html language=enus -->
## TOPIC 00040: Utilities VIs

- bundle_id: `ni-system-configuration-lv-ref`
- source_path: `nisyscfg/utilities_subpalette.html`
- source_url: https://docs-be.ni.com/bundle/ni-system-configuration-lv-ref/raw/resource/enus/nisyscfg/utilities_subpalette.html
- source_language: `enus`
- document_id: `ni-system-configuration-lv-ref`
- page_type: `leaf`
- content_type: ``

### Utilities VIs

**Owning Palette:** [System Configuration VIs](main_palette.html)

**Requires:** NI System Configuration

The Utilities subpalette contains Measurement & Automation Explorer (MAX) VIs and other system configuration utilities.

| Palette Object | Description |
| --- | --- |
| Change Administrator Password | Changes the administrator password on a system. |
| Create Filter Wrapper | Creates a system filter object to query for specific resources in a system. |
| Export | Exports configuration data from MAX into a file. |
| Generate MAX Report | Generates a report to document a local or remote system. |
| Get System Experts | Returns the experts available on the system. |
| Import | Imports configuration data from a file into MAX. |
| Set Time | Sets the current time and/or time zone on the specified system. |
| Update Calibration | Updates the external calibration information for a device. |
| Delete Resource | Removes a hardware resource and its configuration data from the system. |
| System Name Constant | Use this constant to specify a system as an input to NI System Configuration VIs. |
