# NI DOCUMENT BUNDLE: ni-switch-soft-front-panel

<!--NI_BUNDLE_CHUNK bundle=ni-switch-soft-front-panel start=1 end=48 -->
<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=accessing-the-ni-switch-soft-front-panel.html language=enus -->
## TOPIC 00001: Accessing the NI-SWITCH Soft Front Panel

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `accessing-the-ni-switch-soft-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/accessing-the-ni-switch-soft-front-panel.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to access the NI-SWITCH Soft Front Panel.You can open the NI-SWITCH Soft Front Panel from Measurement & Automation Explorer (MAX) or Hardware Configuration Utility. You can also launch it from a command line. The NI-SWITCH Soft Front Panel does not support switch devices used with the LabV

### Accessing the NI-SWITCH Soft Front Panel

Learn how to access the NI-SWITCH Soft Front Panel.

NI-SWITCH Soft Front Panel

Hardware Configuration Utility

Note

NI-SWITCH Soft Front Panel

not

#### From Measurement &
 Automation Explorer

NI-SWITCH Soft Front Panel

1. Select the switch device.
2. Click Test Panels .

#### From Hardware Configuration Utility

NI-SWITCH Soft Front Panel

1. Select the switch device.
2. Click Soft Front Panel .

#### From a Command Line

NI-SWITCH Soft Front Panel

```text
"<SFP_path>" -- /device:<Device_name>
```

<SFP_path>

NI-SWITCH Soft Front Panel

C:\Program Files (x86)\IVI
 Foundation\IVI\Drivers\niSwitch\NI-SWITCH_Soft_Front_Panel.exe

<Device_name>

Dev1

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=copyright.html language=enus -->
## TOPIC 00002: Copyright

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `copyright.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/copyright.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: Under the copyright laws, this publication may not be reproduced or transmitted in any form, electronic or mechanical, including photocopying, recording, storing in an information retrieval system, or translating, in whole or in part, without the prior written consent of Emerson Electric Company.NI

### Copyright

Under the copyright laws, this publication may not be reproduced or transmitted in any form,
 electronic or mechanical, including photocopying, recording, storing in an information
 retrieval system, or translating, in whole or in part, without the prior written consent
 of Emerson Electric Company.

NI respects the intellectual property of others, and we ask our users to do the same. NI software
 is protected by copyright and other intellectual property laws. Where NI software may be
 used to reproduce software or other materials belonging to others, you may use NI
 software only to reproduce materials that you may reproduce in accordance with the terms
 of any applicable license or other legal restriction.

#### End-User License Agreements and Third-Party Legal
 Notices

You can find end-user license agreements (EULAs) and third-party
 legal notices in the following locations:

- Notices are located in the <National Instruments>\_Legal
 Information and <National Instruments> 
 directories.
- EULAs are located in the <National
 Instruments>\Shared\MDF\Legal\license directory.
- Review <National Instruments>\_Legal Information.txt for
 information on including legal information in installers built with NI
 products.

#### U.S. Government Restricted Rights

If you
 are an agency, department, or other entity of the United States Government
 ("Government"), the use, duplication, reproduction, release, modification,
 disclosure or transfer of the technical data included in this manual is governed by
 the Restricted Rights provisions under Federal Acquisition Regulation 52.227-14 for
 civilian agencies and Defense Federal Acquisition Regulation Supplement Section
 252.227-7014 and 252.227-7015 for military agencies.

#### IVI Foundation Copyright Notice

Content from the IVI specifications reproduced with permission from
 the IVI Foundation.

The IVI Foundation and its member companies
 make no warranty of any kind with regard to this material, including, but not
 limited to, the implied warranties of merchantability and fitness for a particular
 purpose. The IVI Foundation and its member companies shall not be liable for errors
 contained herein or for incidental or consequential damages in connection with the
 furnishing, performance, or use of this material.

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=creating-a-new-window.html language=enus -->
## TOPIC 00003: Creating a New Window

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `creating-a-new-window.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/creating-a-new-window.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create a new window to monitor multiple switch devices simultaneously. You can create a new window for the same device or different devices without causing changes in the hardware. To open multiple instances of the NI-SWITCH SFP, select File»New Window.

### Creating a New Window

Create a new window to monitor multiple switch devices simultaneously. You can create a new
 window for the same device or different devices without causing changes in the hardware.
 To open multiple instances of the NI-SWITCH SFP, select File»New
 Window.

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=customizing-the-ni-switch-soft-front-panel.html language=enus -->
## TOPIC 00004: Customizing the NI-SWITCH Soft Front Panel

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `customizing-the-ni-switch-soft-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/customizing-the-ni-switch-soft-front-panel.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can customize settings and operations in the NI-SWITCH SFP. Customizing the Refresh SettingsSelect File»Options, and click Automatic Refresh to disable the automatic refresh settings for the Schematic and Relay tabs. To enable the refresh settings, click Automatic Refresh again. Type in a delay

### Customizing the NI-SWITCH Soft Front Panel

You can customize settings and operations in the NI-SWITCH SFP.

#### Customizing the Refresh Settings

Select
 File»Options, and click Automatic Refresh to
 disable the automatic refresh settings for the Schematic and
 Relay tabs. To enable the refresh settings, click
 Automatic Refresh again. Type in a delay time, in milliseconds, to
 customize the delay interval, or the amount of time that must elapse before the
 Schematic and Relays tabs are refreshed with
 the latest information for the switch device.

#### Customizing Relay Operations

Select
 File»Options, and click Enable changing relay
 positions to customize relay operations. With the Enable changing
 relay positions control enabled, you can change the relay positions of the
 switch device from within the Relays tab.

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=debugging-with-the-ni-switch-soft-front-panel.html language=enus -->
## TOPIC 00005: Debugging with the NI-SWITCH Soft Front Panel

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `debugging-with-the-ni-switch-soft-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/debugging-with-the-ni-switch-soft-front-panel.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you launch the NI-SWITCH SFP for a particular switch device, the current connections on the switch device are displayed in the Schematic tab of the SFP window. Manually closing or opening a relay does not update the Schematic tab. By default, the NI-SWITCH SFP automatically updates all changes

### Debugging with the NI-SWITCH Soft Front Panel

Schematic

Note

Schematic

By default, the NI-SWITCH SFP automatically updates all changes in the connection state of the
 switch device. If an application changes the state of the connections on the switch
 device, and you have enabled the Automatic Refresh option in the NI-SWITCH SFP, this
 change is reflected in the Schematic tab. For example, if you
 have an application running in LabVIEW, the NI-SWITCH SFP displays the connections made
 by the LabVIEW application.

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=determining-relay-end-of-life.html language=enus -->
## TOPIC 00006: Determining Relay End-of-Life

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `determining-relay-end-of-life.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/determining-relay-end-of-life.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: Relay use affects, and relay arcing can accelerate, the end-of-life of a relay. For more detailed information about relay life and arcing, refer to the NI Switches Help. To determine the expected life of your relay, refer to the specifications document for your switch module. To determine if you nee

### Determining Relay End-of-Life

Relay use affects, and relay arcing can accelerate, the end-of-life of a relay. 
For more detailed information about relay life and arcing, refer to the NI Switches Help.
To determine the expected life of your relay, refer to the specifications document for your switch module.

To determine if you need to replace a relay, monitor the relay count of your switch module in the Relays Tab of the SFP window. 
If you have switched a relay beyond its expected life or it has sustained excessive arcing, refer to *Replacing a Relay*.

Parent topic:

Relay Maintenance

Related concepts:

- Replacing a Relay

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=hot-keys-and-keyboard-shortcuts.html language=enus -->
## TOPIC 00007: Hot Keys and Keyboard Shortcuts

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `hot-keys-and-keyboard-shortcuts.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/hot-keys-and-keyboard-shortcuts.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: The table below lists the hot keys and keyboard shortcuts you can use with NI-SWITCH SFP: <F5> Refreshes the Schematic and Relays tabs of the SFP window <F1> Displays online help <Ctrl+N> Creates a new window <Ctrl+Q> Exits NI-SWITCH SFP

### Hot Keys and Keyboard Shortcuts

The table below lists the hot keys and keyboard shortcuts you can use with NI-SWITCH SFP:

<F5>

Schematic

Relays

<F1>

<Ctrl+N>

<Ctrl+Q>

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/bp_copyright.html language=jajp -->
## TOPIC 00008: 著作権

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/bp_copyright.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/bp_copyright.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 著作権

著作権法に基づき、National Instruments Corporationの書面による事前の許可なく、本書のすべて又は一部を写真複写、記録、情報検索システムへの保存、及び翻訳を含め、電子的又は機械的ないかなる形式によっても複製又は転載することを禁止します。

National Instrumentsは他者の知的財産を尊重しており、お客様も同様の方針に従われますようお願いいたします。NIソフトウェアは著作権法その他知的財産権に関する法律により保護されています。NIソフトウェアを用いて他者に帰属するソフトウェアその他のマテリアルを複製することは、適用あるライセンスの条件その他の法的規制に従ってそのマテリアルを複製できる場合に限り可能であるものとします。

#### エンドユーザ使用許諾契約及び他社製品の法的注意事項

エンドユーザ使用許諾契約 (EULA) 及び他社製品の法的注意事項は以下の場所にあります。

- 注意事項は、 <National Instruments>¥_Legal Information 及び <National Instruments> ディレクトリにあります。
- EULAは、 <National Instruments>¥Shared¥MDF¥Legal¥license ディレクトリにあります。
- NI製品で作成したインストーラに法律情報を組み込む方法については、 <National Instruments>¥_Legal Information.txt を確認してください。

#### 米国政府の権利の制限

お客様が米国政府の機関、省又はその他の事業体 (「米国政府」と総称する) である場合、本書に記載の技術データの使用、複製、再製、公表、修正、開示又は転送は、民間機関用の連邦調達規則52.227-14と軍事機関用の国防省連邦調達規則補足252.227-7014及び252.227-7015に基づく限定権利条項の適用を受けます。

#### IVI Foundation Copyright Notice

Content from the IVI specifications reproduced with permission from the IVI Foundation.

The IVI Foundation and its member companies make no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The IVI Foundation and its member companies shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material.

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/bp_important_information.html language=jajp -->
## TOPIC 00009: 法的情報

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/bp_important_information.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/bp_important_information.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 法的情報

[限定的保証](bp_warranty.html)

[著作権](bp_copyright.html)

[商標](bp_trademarks.html)

[特許](bp_patents.html)

[輸出関連法規の遵守に関する情報](bp_export_compliance.html)

[NI製品を使用する際の警告](bp_warning_ni.html)

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/bp_patents.html language=jajp -->
## TOPIC 00010: 特許

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/bp_patents.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/bp_patents.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 特許

National Instrumentsの製品を保護する特許については、ソフトウェアで参照できる特許情報 (**ヘルプ→特許**)、メディアに含まれているpatents.txtファイル、またはni.com/patents/jaからアクセスできる**「ナショナルインスツルメンツ特許情報」のうち、該当するリソースから参照してください。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/bp_technical_support_resources.html language=jajp -->
## TOPIC 00011: NIサービス

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/bp_technical_support_resources.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/bp_technical_support_resources.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### NIサービス

ナショナルインスツルメンツは、お客さまを成功に導く手助けとしてグローバルサービスとサポートを提供しています。デプロイメントや継続的メンテナンスにおける計画から開発などの、アプリケーションライフサイクルの各段階で役立つトレーニングおよび認定プログラムに加え、製品サービスもご利用ください。

製品のサービスを利用するには、ナショナルインスツルメンツのユーザプロファイルにログインして、ni.com/myproductsでお客様の製品をご登録ください。

登録されているNI製品をご使用のユーザには次の特典があります。

- 適用される製品のサービスへのアクセス。
- オンラインアカウントによる簡単な製品管理。
- 製品に関する重要な通知、ソフトウェア更新、サービス期限の通知を受信。

#### サービスとリソース

- メンテナンスとハードウェアサービス ―NIは、ご使用のシステムの確度および信頼性の要件を確認する手助けや、製品の寿命期間にわたって確度を維持し、ダウンタイムを最小限に抑えることができるように、保証や予備製品およびキャリブレーションサービスを提供しています。詳細については、ni.com/servicesをご覧ください。
  - 保証と修理 ―すべてのNIハードウェア製品には、5年まで延長可能な1年の標準保証が提供されています。NIの修理サービスは、高度な訓練を受けた技術者によりナショナルインスツルメンツサービスセンターで迅速に行われ、修理に際しては純正部品のみを使用しています。
  - キャリブレーション ―標準のキャリブレーションを通じて、計測器の測定性能を定量化および改善することができます。NIでは、最新式のキャリブレーションサービスを提供しています。ご使用の製品でキャリブレーションがサポートされている場合は、ni.com/calibrationからその製品のCalibration Certificateを入手できます。
- システムインテグレーション ―時間の制約がある場合や社内の技術リソースが不足している場合、またはプロジェクトに関連する問題がある場合、ナショナルインスツルメンツのアライアンスパートナーによるサービスをご利用いただけます。詳細はNIオフィスにお電話いただくか、ni.com/allianceをご覧ください。
- トレーニングと認定 ―NIのトレーニングおよび認定プログラムは、アプリケーション開発の習熟度と生産性を高める最も効果的な方法です。詳細については、ni.com/trainingをご覧ください。
  - 「NI LabVIEWスキルガイド」は、現在のアプリケーションの習熟度要件の確認を手助けし、これらのスキルを習得するための時間や予算の制約と個人的な学習方法の好みに合ったオプションを提供しています。これらのカスタムパスを確認するには、ni.com/skills-guideを参照してください。
  - NIでは、お客様のニーズに応じて、講師による各国の施設でのクラスや、お客様の施設で行う出張コース、およびオンラインコースなど、複数の言語および形式のコースを提供しています。
- サポート ―技術サポート (ni.com/support) からは以下のリソースにアクセスできます。
  - セルフヘルプリソース ―質問に対する回答やソリューションが必要な場合は、ナショナルインスツルメンツのWebサイト (ni.com/support) でソフトウェアドライバとアップデート、検索可能な技術サポートデータベース、製品マニュアル、トラブルシューティングウィザード、種類豊富なサンプルプログラム、チュートリアル、アプリケーションノート、計測器ドライバなどをご利用いただけます。ユーザ登録されたお客様は、NIディスカッションフォーラム (ni.com/jp/dforum) にアクセスすることもできます。NIのアプリケーションエンジニアは、お客様からのご質問すべてにお答えしています。
  - ソフトウェアサポートサービスメンバーシップ ―標準サポート・保守プログラム (SSP) は、NI Developer Suiteを含む、ほとんどのNIソフトウェア製品に含まれている、更新可能な1年間のサブスクリプションです。このプログラムでは、NIのアプリケーションエンジニアによる電話またはEメールでの個別サポートが提供されます。また、SSPの特典を必要な限り中断なく利用できる柔軟な延長契約オプションもご利用いただけます。詳細については、ni.com/sspをご覧ください。
- 適合宣言 (DoC) ―適合宣言とは、適合宣言書によるさまざまな欧州閣僚理事会指令への適合宣言です。この制度により、電磁両立性 (EMC) に対するユーザ保護や製品の安全性に関する情報が提供されます。ご使用の製品の適合宣言は、ni.com/certification (英語) から入手できます。

ご利用の地域のその他の技術サポートのオプションについては、ni.com/servicesをご覧頂くか、またはni.com/contactから最寄の営業所までお問い合わせください。

また、弊社Webサイトの*Worldwide Offices*セクション (ni.com/niglobal) から各支社のWebサイトにアクセスすることもできます。各支社のサイトでは、お問い合わせ先、サポート電話番号、Eメールアドレス、現行のイベントなどに関する最新情報を提供しています。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/bp_trademarks.html language=jajp -->
## TOPIC 00012: 商標

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/bp_trademarks.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/bp_trademarks.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 商標

National Instrumentsの商標の詳細については、ni.com/trademarksに掲載されている*NI Trademarks and Logo Guidelines*を参照してください。

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

Handle Graphics®, MATLAB®, Real-Time Workshop®, Simulink®, Stateflow®, and xPC TargetBox® are registered trademarks, and TargetBox™ and Target Language Compiler™ are trademarks of The MathWorks, Inc.

Tektronix®, Tek, and Tektronix, Enabling Technology are registered trademarks of Tektronix, Inc.

The Bluetooth® word mark is a registered trademark owned by the Bluetooth SIG, Inc.

The ExpressCard™ word mark and logos are owned by PCMCIA and any use of such marks by National Instruments is under license.

The mark LabWindows is used under a license from Microsoft Corporation. Windows is a registered trademark of Microsoft Corporation in the United States and other countries.

本書中に記載されたその他の製品名及び企業名は、それぞれの企業の商標又は商号です。

National Instruments Alliance Partner Programのメンバーは、National Instrumentsより独立している事業体であり、National Instrumentsと何ら代理店、パートナーシップ又はジョイントベンチャーの関係にありません。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/bp_warning_ni.html language=jajp -->
## TOPIC 00013: National Instruments Corporation製品を使用する際の警告

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/bp_warning_ni.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/bp_warning_ni.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### National Instruments Corporation製品を使用する際の警告

お客様は、National Instruments Corporation (以下「NI」という) の製品がお客様のシステム又はアプリケーションに組み込まれるかどうかにかかわらず常にNI製品の適合性及び信頼性 (システム又はアプリケーションの適切な設計、プロセス及び安全性を含みます) を確認し、検証する最終的な責任を負います。

NI製品は、生命若しくは安全の維持に不可欠なシステム、危険な環境若しくはフェイル・セーフ機能が必要となる他のあらゆる環境(原子力施設の運用、航空機ナビゲーション、航空交通管制システム、救命若しくは生命維持システムその他の医療装置の運用若しくは操作を含みます)、又はこの製品の欠陥が死亡、傷害、重大な財産損害若しくは環境被害をもたらしうるその他あらゆる用途における使用 (以下｢高リスク用途｣と総称する) のために設計、製造又は試験されたものではありません。さらに、故障・機能不全を防ぐために、バックアップ及びシャットダウン機構の準備などの慎重な処置を講じる必要があります。NIは、NI製品の高リスク用途への適合性について、明示又は黙示を問わず、いかなる保証も行いません。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/bp_warranty.html language=jajp -->
## TOPIC 00014: 限定的保証

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/bp_warranty.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/bp_warranty.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 限定的保証

本書は、「現状有姿」 (as is) で提供されており、事前の通知なしに次の改訂版で変更される場合があります。最新版については、ni.com/manualsをご参照ください。National Instruments Corporation (以下「NI」という) は、本書の技術的な正確性を入念にチェックしております。ただし、NIは、本書に記載の情報の正確性について、一切の明示又は黙示の保証を行わず、技術的な誤りについて一切の責任を負いません。

NIは、請求日から1年間、ハードウェア製品について、当該製品が適用あるNIの公表された仕様に実質的に適合しないこととなるような素材及び製造技術上の欠陥は存在しないことを保証します。

NIは、請求日から90日間、 (ⅰ) ソフトウェア製品が適用される付属のマニュアル文書に実質的に従って機能し、かつ (ⅱ) 当該ソフトウェアの媒体に素材及び製造技術上の欠陥が存在しないことを保証します。

NIが適用ある保証期間中に欠陥又は不適合の通知を受領した場合、NIはその裁量により、 (ⅰ) 問題のある製品を修理若しくは交換し、又は (ⅱ) 問題のある製品の料金を払い戻します。修理又は交換後のハードウェアは、当初の保証期間の残期間又は90日間のうちいずれか長い期間について保証されます。NIが問題のある製品を修理又は交換することを選択する場合、NIは、新品、又は新品と同等の性能及び信頼性を有し、当初の部品又は製品と少なくとも同等の機能を有する整備済みの部品又は製品を使用することができます。

お客様は製品をNIに返却する前に、NIからRMA番号を取得する必要があります。NIは、限定的保証の対象外のハードウェアの検査及び試験についてその費用を請求する権利を留保します。

限定的保証は、NI製品の欠陥が次のいずれかの事柄に起因するものである場合には適用されません： (NI以外の者によって実施された) 不適切又は不十分なメンテナンス、設置、修理又は校正、許可を受けていない改変、不適切な環境、不適切なハードウェア又はソフトウェア・キーの使用、製品の仕様の範囲を超えた不適切な使用又は操作。不適切な電圧の印加、事故、誤用又は不注意、雷、洪水又は他の天災等の災害。

上記の救済手段は排他的なものであり、お客様が有する唯一の救済手段です。また、これらの救済手段がその主要な目的を達成しえない場合であっても適用されます。

本書に明示に規定される場合を除いては、NI製品は、いかなる種類の保証も付されることなく、｢現状有姿｣ (as is) で提供されます。NIは、NI製品に関するいかなる保証 (商品性の黙示の保証、特定目的適合性、第三者の所有権その他の財産権を侵害していないこと、及び取引慣行又は取引過程により生じうるあらゆる保証を含みます) も、明示、黙示を問わず、行いません。NIは、正確さ、的確性、信頼性その他いかなる点についても、NI製品の使用又は使用結果に関して、保証せず、またいかなる表明も行いません。NIは、NI製品の稼働に中断がなく、又は誤作動がないことを保証しません。

お客様とNIがNI製品を対象とする保証条件について、別途署名又は記名押印済みの契約を締結している場合、当該契約書における保証条件が適用されます。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/dpdt.html language=jajp -->
## TOPIC 00015: 双極双投 (DPDT) トポロジ

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/dpdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/dpdt.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 双極双投 (DPDT) トポロジ

双極双投 (DPDT) トポロジは、2つの極と2つの投接点を持つリレーで構成されます。極のデフォルト位置によって、1つの投接点はノーマリオープン (NO)、もう一方はノーマリクローズ (NC)とみなされます。DPDTトポロジの詳細情報については、**『NI スイッチヘルプ』を参照してください。

|  | メモ SFPウィンドウのサイズを変更してDPDTリレーをさらに表示することができます。 |
| --- | --- |

下記の回路図は8-DPDTトポロジのNI　PXI-2566の例を示しています。

[IMAGE alt='image' src='loc_dpdt.gif']

#### DPDT接続を行う

個別のリレーをクリックしてDPDTの接続を構成します。たとえば、no5をcom5へ接続するには、該当するリレーをクリックします。極がno5をcom5に接続し、NI-SWITCH SFPは適切な接続/接続解除処理の呼び出しをドライバに行います。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/dpst.html language=jajp -->
## TOPIC 00016: 双極単投 (DPST) トポロジ

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/dpst.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/dpst.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 双極単投 (DPST) トポロジ

双極単投 (DPST) トポロジは、2つの極と1つの投接点を持つリレーで構成されます。DPSTリレー形式についての詳細は『NI スイッチヘルプ』を参照してください。**

|  | メモ SFPウィンドウのサイズを変更してDPSTリレーをさらに表示することができます。 |
| --- | --- |

下記の回路図は16-DPSTトポロジのNI　PXI-2564の例を示しています。

[IMAGE alt='image' src='loc_dpst.gif']

#### DPSTの接続を行う

個別のリレーをクリックしてDPSTの接続を構成します。NI-SWITCH SFPは、この接続を認識し、ドライバの接続処理の呼び出しを行います。たとえば、ch2をcom2へ接続するには、該当するリレーをクリックします。極はch2をcom2へ接続します。接続を解除するには、接続点をクリックします。NI-SWITCH SFPは、ドライバに対して適切な接続/接続解除処理の呼び出しを行います。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/independent.html language=jajp -->
## TOPIC 00017: 独立結線タブ

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/independent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/independent.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 独立結線タブ

いくつかのNIスイッチモジュールは、次の図に示すように、結線の描写が必要な情報を含む独立トポロジが設定されています。

[IMAGE alt='image' src='loc_independent2.gif']

|  | メモ SFPウィンドウのサイズを変更し結線全体を表示することができます。 |
| --- | --- |

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/matrix.html language=jajp -->
## TOPIC 00018: マトリクストポロジ

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/matrix.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### マトリクストポロジ

マトリクスは列と行を使用して複数入力を複数出力に接続することができる柔軟性のあるトポロジです。どの列でも任意の数の行に接続でき、どの行でも任意の数の列に接続できます。マトリクストポロジの詳細情報については、**『NI スイッチヘルプ』を参照してください。

#### マトリクス回路

マトリクス回路上での行と列の交点は、スイッチデバイス上で可能な接続を示します。また、NI-SWITCH SFPでは、マトリクス回路上の各接続とそれに関連する接続経路を異なる色で表します。複数接続したチャンネルでは、NI-SWITCH SFPはすべての接続およびそれに関連した接続経路を同じ色で示します。複数接続のあるマトリクスチャンネルの例は、次の回路の行0(r0) を参照してください。

|  | メモ SFPウィンドウのサイズを変更しチャンネルをさらに表示することができます。 |
| --- | --- |

[IMAGE alt='image' src='loc_matrix.gif']

#### マトリクスの接続を行う

行と列の交点をクリックしてマトリクス上で接続を構成します。接続を解除するには、接続点を再度クリックします。NI-SWITCH SFPは、ドライバに対して適切な接続/接続解除処理の呼び出しを行います。

#### ＮＩ スイッチブロックデバイスのマトリクス回路図

NI-SWITCH SFPを使用して1つのNI スイッチブロックマルチカードデバイス内のカードを接続したり、複数のNI スイッチブロックデバイスを接続することができます。次の手順を参照して、NI-SWITCH SFPを使用してNI スイッチブロックデバイスを接続します。

##### NI スイッチブロックマルチカードデバイスでチャンネルを接続する

同一のアナログバスチャンネルを各カードの対応する行に接続することで、マルチカードデバイス内の異なるカードのチャンネルを接続します。

|  | メモ 回路図で確認したいカードは、カードドロップダウンリストから選択できます。 |
| --- | --- |

次の回路図は、単一カード内の行と列 (カード1のcard1r1からc33) 接続、および1つのアナログバスライン (行0とab0は両方のカードで接続されている) を介した同一デバイス内の複数カード間のチャンネル接続を示します。

[IMAGE alt='image' src='loc_switchblock_matrix_card1.gif']

次の回路図は、前述のマルチカードデバイスのカード2でカード2のc82をカード1のc34に接続するための接続を示します。両カードで行0とab0間のリレーは閉じています。

[IMAGE alt='image' src='loc_switchblock_matrix_card2.gif']

##### 複数のNI スイッチブロックデバイス間のチャンネルを接続する

NI-SWITCH SFPを使用すると、アナログバスラインを共有することができ、同一キャリア内またはNI 2806拡張ブリッジで接続された隣接キャリア間の複数NI スイッチブロックデバイス間の信号を接続することが可能になります。次の手順を実行して、NI-SWITCH SFPで複数のNI スイッチブロックデバイス間の信号を接続します。

1. アナログバスラインを共有するデバイスを決定します。
2. 結線 タブで、 デバイス リストからデバイスを1つ選択します。
3. オプションダイアログボックス ( ファイル → オプション ) を開きます。
4. オプションダイアログボックスの アナログバス タブをクリックします。
5. デバイスが共有するアナログバスラインのチェックボックスを選択して、 OK をクリックします。
6. 結線 タブで、共有アナログバスラインに対応するチャンネルのabリレーを閉じます。
7. 結線 タブで、必要があればデバイス上の終端端子と手順6でアナログバスラインに接続したチャンネル間の接続を行います。
8. アナログバスラインを共有する各デバイスで、手順2～7を繰り返します。

NI スイッチブロックキャリアでのアナログバスの使い方については、**『NI スイッチヘルプ』を参照してください。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/mux.html language=jajp -->
## TOPIC 00019: マルチプレクサトポロジ

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/mux.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/mux.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### マルチプレクサトポロジ

マルチプレクサ (MUX)は、1つの入力を複数の出力に、または1つの出力を複数の入力に接続できるトポロジです。このトポロジを使用して一連のチャンネルを共通ラインに接続します。マルチプレクサトポロジの詳細情報については、**『NI スイッチヘルプ』を参照してください。

|  | メモ SFPウィンドウのサイズを変更しチャンネルをさらに表示することができます。 |
| --- | --- |

下記の回路図はマルチプレクサトポロジで構成されたスイッチモジュールの例を示しています。

[IMAGE alt='image' src='loc_mux.gif']

#### マルチプレクサの接続を行う

comチャンネル (右) に接続したいチャンネル (左) のポールの端をクリックします。NI-SWITCH SFPは、ドライバに対して適切な接続/接続解除処理の呼び出しを行います。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/related_documentation.html language=jajp -->
## TOPIC 00020: 関連ドキュメント

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/related_documentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/related_documentation.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 関連ドキュメント

最新のドキュメントについては、ni.com/manualsからナショナルインスツルメンツの製品マニュアルライブラリをご覧ください。

以下のドキュメントには、このヘルプファイルを使用する上で役に立つ情報が記載されています。

- 『NI スイッチヘルプ』

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/relay_determine.html language=jajp -->
## TOPIC 00021: リレー寿命を確認する

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/relay_determine.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/relay_determine.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### リレー寿命を確認する

リレーの使用量はリレーの寿命に影響を与え、**アーク**は寿命を短縮します。リレー寿命およびアークについての詳細は、『NI スイッチヘルプ』を参照してください。**リレーの予測寿命については、スイッチモジュールの仕様書を参照してください。

リレー交換の必要性は、SFPウィンドウの**リレータブ**にあるスイッチモジュールのリレーカウントで確認します。リレーが予測寿命を超えて動作している場合、または過度のアーク電流が発生している場合は、[リレーを交換する](relay_replace.html)を参照してください。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/relay_maintain.html language=jajp -->
## TOPIC 00022: リレー管理

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/relay_maintain.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/relay_maintain.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### リレー管理

リレーの交換およびリセット等のリレー管理についてはこのトピックを展開してください。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/relay_replace.html language=jajp -->
## TOPIC 00023: リレーを交換する

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/relay_replace.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/relay_replace.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### リレーを交換する

リレーを交換する手順については、『NI スイッチヘルプ』に記載されている該当するスイッチモジュールのリレー交換トピックを参照してください。**リレーを交換した後は、[リレーカウントをリセットする](relay_reset.html)を参照してください。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/relay_reset.html language=jajp -->
## TOPIC 00024: リレーカウントをリセットする

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/relay_reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/relay_reset.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### リレーカウントをリセットする

|  | 注意 リレーカウントのリセット処理中はNI-SWITCH SFPによってリレーカウントの同期化が無効となるため、リレーカウントをリセットする10分前までに実行したリレー動作のカウント値が失われる可能性があります。 |
| --- | --- |

リレーカウントをリセットするには、以下の手順に従ってください。

1. ファイル→リレー管理 を選択します。リレー管理ダイアログボックスが表示されます。
2. リレー名 ドロップダウンリストからリセットするリレーを選択します。
3. (オプション) 後に参照できるように 既存のリレーカウント を記録します。
4. リセットするよう選択したリレーを確認し、 OK をクリックしてリレーカウントを0にリセットします。 NI-SWITCH SFP は新しいリレーカウントをハードウェアに保存し、デバイスをリセットします。

#### リレーカウントを復元する

リレーカウントをリセットした後でも、次の手順を実行して以前のリレーカウントを復元することができます。

1. 上記の手順1および2を繰り返してリレーカウントをリセットします。
2. リセットするよう選択したリレーを確認し、 カウントを編集 を有効にします。
3. 新規リレーカウント に以前のカウントを入力して OK をクリックします。 NI-SWITCH SFP はリレーカウントをハードウェアに保存し、デバイスをリセットします。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/sfp_access.html language=jajp -->
## TOPIC 00025: NI-SWITCHソフトフロントパネルにアクセスする

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/sfp_access.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/sfp_access.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### NI-SWITCHソフトフロントパネルにアクセスする

NI-SWITCH SFPへは、MAX (Measurement & Automation Explorer) からアクセスすることができます。

|  | メモ NI-SWITCH SFPは、Real-Timeターゲット上のスイッチデバイスに対しては実行できません。 |
| --- | --- |

##### MAXから起動する

- スイッチデバイスを右クリックして、 テストパネル を選択します。

##### コマンドラインから起動する

コマンドライン (**スタート→ファイル名を指定して実行**を選択するなど) からNI-SWITCH SFPを起動するには、以下の構文を使用します。

"<SFP_path>" -- /device:<Device_name>

<SFP_path> は、インストールされているSFP実行可能ファイルへの絶対パスです。たとえば、Windows 64ビットシステムではこの場所は以下のようになります。

C:\Program Files (x86)\IVI Foundation\IVI\Drivers\NI-Switch Soft Front Panel\NI-SWITCH_Soft_Front_Panel.exe

<Device_name> は、スイッチモジュールのリソース名です。たとえば、Dev1などです。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/sfp_channels.html language=jajp -->
## TOPIC 00026: チャンネルタブ

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/sfp_channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/sfp_channels.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### チャンネルタブ

いくつかのNIスイッチモジュールは、独立トポロジに設定できます。独立トポロジを使用しているNI スイッチモジュールには、結線の描写に必要な情報が含まれない場合がありますｌ。その代わりに次の図に示すように、NI-SWITCH SFPは結線を3つのリストボックス (**チャンネル1**、**チャンネル2**、および**接続**) として表示します。

|  | メモ SFPウィンドウのサイズを変更しチャンネルをさらに表示することができます。 |
| --- | --- |

[IMAGE alt='image' src='loc_independent.gif']

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/sfp_debugging.html language=jajp -->
## TOPIC 00027: NI-SWITCHソフトフロントパネルを使用してデバッグする

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/sfp_debugging.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/sfp_debugging.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### NI-SWITCHソフトフロントパネルを使用してデバッグする

特定のスイッチデバイスに対してNI-SWITCH SFPを起動すると、スイッチデバイス上の現在の接続はSFPウィンドウの**結線**タブに表示されます。

|  | メモ リレーを手動で開閉すると、結線タブは更新されません。 |
| --- | --- |

NI-SWITCH SFPはデフォルトの設定では、スイッチデバイスの接続状態を自動的に更新します。アプリケーションからスイッチデバイスの接続状態が変更され、NI-SWITCH SFPで自動更新オプションが有効になっている場合、この変更は**結線**タブに反映されます。たとえば、LabVIEWでアプリケーションを実行している場合、NI-SWITCH SFPはLabVIEWアプリケーションから変更される接続を表示します。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/sfp_menu.html language=jajp -->
## TOPIC 00028: NI-SWITCHソフトフロントパネルをカスタマイズする

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/sfp_menu.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/sfp_menu.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### NI-SWITCHソフトフロントパネルをカスタマイズする

NI-SWITCH SFPの設定と操作をカスタマイズすることができます。

#### 更新設定をカスタマイズする

**ファイル→オプション**を選択して**自動更新**のチェックを解除すると、**結線**および**リレー**タブの自動更新設定を無効にすることができます。更新設定を有効にするには、**自動更新**を再度クリックします。遅延時間をミリ秒で入力し、遅延間隔(スイッチデバイスの状態が**結線**および**リレー**タブに反映されるまでの時間)を変更することができます。

#### リレー操作をカスタマイズする

**ファイル→オプション**を選択し、**リレー位置の変更を有効化**をクリックしてリレー操作をカスタマイズできます。**リレー位置の変更を有効化**制御が有効になっている場合、**リレー**タブ内でスイッチデバイスのリレー位置を変更することができます。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/sfp_new_window.html language=jajp -->
## TOPIC 00029: 新規ウィンドウを作成する

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/sfp_new_window.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/sfp_new_window.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 新規ウィンドウを作成する

新しいウインドウを作成すると、複数のスイッチデバイスを同時に監視することができます。ハードウェアに変更を加えることなく新規ウィンドウを同じデバイスまたは異なるデバイスに対して作成できます。NI-SWITCH SFPのウィンドウを複数開くには、**ファイル→新規ウィンドウ**を選択します。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/sfp_overview.html language=jajp -->
## TOPIC 00030: NI-SWITCHソフトフロントパネル

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/sfp_overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/sfp_overview.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### NI-SWITCHソフトフロントパネル

NI-SWITCH SFPソフトフロントパネル (SFP)はスイッチモジュールの基本機能のテストや、アプリケーションのトラブルシュートに使用します。NI-SWITCH SFPを使用すると、スイッチモジュール上の接続の切り替えを監視できるため、NI-SWITCH SFPは強力なデバッグツールとしても使用できます。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/sfp_relays.html language=jajp -->
## TOPIC 00031: リレータブ

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/sfp_relays.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/sfp_relays.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### リレータブ

**リレー**タブは、スイッチデバイスの各リレーの名前、位置、カウントを表示します。リレーカウント情報を使用して、スイッチデバイスのリレーの寿命が近づいているかどうか、また保守が必要かどうか確認します。スイッチデバイスがリレーカウントをサポートしていない場合、**リレー**タブにはリレーの名前と位置のみが表示されます。

|  | メモ NI USB-1359を使用してスイッチを制御する場合、NI-SWITCH SFPは表示されているリレーのみを更新することでリレー状態の更新を最適化します。更新されていないリレー状態は青で表示されます。更新されるとリレー状態の色は青から黒へ変わります。 |
| --- | --- |

スイッチモジュールの交換部品をご注文いただくには、ni.comでスイッチモジュール名を検索してください。リレーの交換手順については、**『NI スイッチヘルプ』にあるスイッチモジュールの「リレーの交換」セクションを参照してください。

下の図は、NI PXI-2566のリレー位置およびカウントを示しています。

[IMAGE alt='image' src='loc_relays.gif']

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/sfp_schematics.html language=jajp -->
## TOPIC 00032: 結線タブ

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/sfp_schematics.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/sfp_schematics.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 結線タブ

**結線**タブには、スイッチデバイスのトポロジ図が含まれます。

**結線**タブの行と列の交点をクリックするだけでスイッチデバイスの接続を構成することができます。NI-SWITCH SFPは、これらの接続を認識し、接続を実行するドライバ呼び出しを行います。さらに、**結線**タブを使用してスイッチデバイスの接続状態を検証します。

|  | メモ スキャンリストをダウンロードしてアクティブスイッチデバイスがスキャンされている間は、結線タブでスイッチハードウェアの状態変更はできません。 |
| --- | --- |

NI-SWITCH SFP[ツールバー](sfp_tools.html)にあるトポロジリングで選択するトポロジによって、次の6つのいずれかのトポロジが**結線**タブに表示されます。

- マトリクス
- マルチプレクサ
- 単極双投 (SPDT)
- 単極単投 (SPST)
- 双極双投 (DPDT)
- 双極単投 (DPST)

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/sfp_shortcuts.html language=jajp -->
## TOPIC 00033: ホットキーおよびキーボードショートカット

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/sfp_shortcuts.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/sfp_shortcuts.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### ホットキーおよびキーボードショートカット

下の表はNI-SWITCH SFPで使用できるホットキーおよびキーボードショートカットを記載しています。

| <F5> | SFPウィンドウの結線タブおよびリレータブを更新する |
| --- | --- |
| <F1> | オンラインヘルプを表示する |
| <Ctrl+N> | 新規ウィンドウを作成する |
| <Ctrl+Q> | NI-SWITCH SFPを終了する |

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/sfp_title.html language=jajp -->
## TOPIC 00034: NI-SWITCHソフトフロントパネルヘルプ

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/sfp_title.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/sfp_title.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='ni_mainbitlogo_48.gif']

### NI-SWITCHソフトフロントパネルヘルプ

2021年10月、371497K-0112

『NI-SWITCHソフトフロントパネルヘルプ』**は、NI-SWITCHソフトフロントパネル (SFP)を使用してスイッチモジュールの基本機能をテストし、アプリケーションをトラブルシュートする方法をステップごとに説明しています。

このヘルプの詳細については、次のトピックを参照してください。

[関連ドキュメント](related_documentation.html)

[法的情報](bp_important_information.html)

[NIサービス](bp_technical_support_resources.html)

© 2005-2021 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/sfp_tools.html language=jajp -->
## TOPIC 00035: NI-SWITCHソフトフロントパネルツールバー

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/sfp_tools.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/sfp_tools.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### NI-SWITCHソフトフロントパネルツールバー

#### コントロール

**デバイス**―システムに取り付けられているすべてのスイッチデバイスをリスト表示します。このリストにはMAXで作成されたスイッチのシミュレーションデバイスも含まれます。 
 
 **トポロジ**ースイッチデバイスに関連するすべてのトポロジをリスト表示します。

|  | 注意 トポロジを変更すると、デバイスのハードウェア構成も変更される場合があります。 |
| --- | --- |

#### アイコン

|  | 更新アイコンを選択して、SFPウィンドウの結線タブおよびリレータブの表示を更新します。 |
| --- | --- |
|  | すべてを接続解除アイコンを選択して、現在スイッチデバイスで構成されているすべての接続を解除します。 |
|  | 現在アクティブなデバイスとトポロジを使用してNI Switch Executiveバーチャルデバイスを作成するには、NI Switch Executiveバーチャルデバイスを作成アイコンを選択します。NI-SWITCH SFPは、MAX内のNI Switch Executiveを起動します。このボタンはNI Switch Executiveがインストールされていない場合は無効になります。 |

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/spdt.html language=jajp -->
## TOPIC 00036: 単極双投 (SPDT) トポロジ

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/spdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/spdt.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 単極双投 (SPDT) トポロジ

Single-pole double-throw (SPDT) トポロジは、1つの極と2つの投接点を持つリレーで構成されます。極のデフォルト位置によって、1つの投接点はノーマリオープン (NO)、もう一方はノーマリクローズ (NC)とみなされます。SPDTトポロジの詳細情報については、**『NI スイッチヘルプ』を参照してください。

|  | メモ SFPウィンドウのサイズを変更してSPDTリレーをさらに表示することができます。 |
| --- | --- |

下記の回路図は16-SPDTトポロジのNI　PXI-2566の例を示しています。

[IMAGE alt='image' src='loc_spdt.gif']

#### SPDT接続を行う

個別のリレーをクリックしてSPDTの接続を構成します。たとえば、no5をcom5へ接続するには、該当するリレーをクリックします。極がno5をcom5に接続し、NI-SWITCH SFPは適切な接続/接続解除処理の呼び出しをドライバに行います。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=niswitchsfp/spst.html language=jajp -->
## TOPIC 00037: 単極単投 (SPST) トポロジ

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `niswitchsfp/spst.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/jajp/niswitchsfp/spst.html
- source_language: `jajp`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: ``

### 単極単投 (SPST) トポロジ

Single-pole single-throw (SPST) トポロジは、1つの極と1つの投接点を持つリレーで構成されます。SPSTリレー形式についての詳細は『NI スイッチヘルプ』を参照してください。**

|  | メモ SFPウィンドウのサイズを変更してSPSTリレーをさらに表示することができます。 |
| --- | --- |

下記の回路図は16-SPSTトポロジのNI　PXI-2564の例を示しています。

[IMAGE alt='image' src='loc_spst.gif']

#### SPST接続を行う

個別のリレーをクリックしてSPSTの接続を構成します。NI-SWITCH SFPは、この接続を認識し、ドライバの接続処理の呼び出しを行います。たとえば、ch2をcom2へ接続するには、該当するリレーをクリックします。極はch2をcom2へ接続します。接続を解除するには、接続点をクリックします。NI-SWITCH SFPは、ドライバに対して適切な接続/接続解除処理の呼び出しを行います。

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=overview.html language=enus -->
## TOPIC 00038: NI-SWITCH Soft Front Panel Overview

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/overview.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI-SWITCH Soft Front Panel (SFP) as a tool to test the basic functionality of your switch device and troubleshoot your applications. Because the NI-SWITCH SFP enables you to monitor connections on a switch module as you make them, the NI-SWITCH SFP is also a powerful debugging tool.

### NI-SWITCH Soft Front Panel
 Overview

Use the NI-SWITCH Soft Front Panel (SFP) as a tool to test the basic functionality of
 your switch device and troubleshoot your applications. Because the NI-SWITCH SFP enables
 you to monitor connections on a switch module as you make them, the NI-SWITCH SFP is
 also a powerful debugging tool.

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=relay-maintenance.html language=enus -->
## TOPIC 00039: Relay Maintenance

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `relay-maintenance.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/relay-maintenance.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about relay maintenance, including instructions for replacing and resetting a relay.

### Relay Maintenance

Expand this topic for information about relay maintenance, including instructions for replacing
 and resetting a relay.

- [Determining Relay End-of-Life](determining-relay-end-of-life.html)
- [Replacing a Relay](replacing-a-relay.html)
- [Resetting a Relay Count](resetting-a-relay-count.html)

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=replacing-a-relay.html language=enus -->
## TOPIC 00040: Replacing a Relay

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `replacing-a-relay.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/replacing-a-relay.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the Relay Replacement topic for your switch module in the NI Switches Help for instructions on how to replace a relay. After you replace the relay, refer to Resetting a Relay Count.

### Replacing a Relay

Refer to the Relay Replacement topic for your switch module in the NI Switches Help for instructions on how to replace a relay.
After you replace the relay, refer to *Resetting a Relay Count*.

Parent topic:

Relay Maintenance

Related concepts:

- Resetting a Relay Count

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=resetting-a-relay-count.html language=enus -->
## TOPIC 00041: Resetting a Relay Count

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `resetting-a-relay-count.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/resetting-a-relay-count.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because the NI-SWITCH SFP disables relay count synchronization during the relay count reset process, counts may be lost for any relay operation performed up to ten minutes prior to resetting a relay count. Complete the following steps to reset a relay count. Select File»Relay Maintenance. The Rela

### Resetting a Relay Count

Caution

Complete the following steps to reset a relay count.

1. Select File»Relay Maintenance . The Relay Maintenance dialog box appears.
2. Select the relay to reset from the Relay Name drop-down list.
3. (Optional) Record the Existing Relay Count for your records.
4. Verify the relay you selected for reset, and click OK to reset the relay count to zero. The NI-SWITCH SFP saves the new relay count to the hardware and resets the active device.

Restoring a Relay Count

In case of unintentional relay reset, complete the following steps to restore a previous relay count.

1. Repeat steps 1 and 2 above for resetting a relay count.
2. Verify the relay you selected for reset, and enable Edit Count .
3. Type the previous count in New Relay Count and click OK . The NI-SWITCH SFP saves the relay count to the hardware and resets the active device.

Parent topic:

Relay Maintenance

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=the-double-pole-double-throw-topology.html language=enus -->
## TOPIC 00042: The Double-Pole Double-Throw Topology

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `the-double-pole-double-throw-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/the-double-pole-double-throw-topology.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: The double-pole double-throw (DPDT) topology is composed of two-poles, two-throw relays. Based on the default position of the pole, one throw is considered normally open (NO) while the other is normally closed (NC). Refer to the NI Product Documentation Center for more information about DPDT topolog

### The Double-Pole Double-Throw Topology

NI Product Documentation
 Center

Note

Refer to the schematic below for an example of the NI PXI-2566 in the 8-DPDT topology.

Figure 1.

[IMAGE alt='image' src='GUID-93460C07-3EEE-4D44-9E5A-9E179C83D55B-a5.gif']

#### Make a DPDT Connection

Click on an
 individual relay to make a DPDT connection. To connect no5 to com5, for example,
 simply click on the relay. The pole connects no5 to com5, and the NI-SWITCH SFP
 makes the appropriate connect/disconnect calls to the driver.

Related information:

- NI Product Documentation Center

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=the-double-pole-single-throw-topology.html language=enus -->
## TOPIC 00043: The Double-Pole Single-Throw Topology

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `the-double-pole-single-throw-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/the-double-pole-single-throw-topology.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: The double-pole single-throw (DPST) topology is composed of two-poles, one-throw relays. Refer to the NI Product Documentation Center for more information about DPST relay forms.You can resize the SFP window to see more DPST relays. Refer to the schematic below for an example of the NI PXI-2564 in t

### The Double-Pole Single-Throw Topology

NI Product Documentation Center

Note

Refer to the schematic below for an example of the NI PXI-2564 in the 16-DPST topology.

[IMAGE alt='image' src='GUID-3D16727F-6BD6-47CC-9425-E40A2F577B65-a5.gif']

#### Make a DPST Connection

Click on an individual relay to make an DPST
 connection. The NI-SWITCH SFP translates this click into the appropriate channel connection
 and makes the connect call to the driver. To connect ch2 to com2, for example, click on the
 relay. The pole connects ch2 to com2. To break a connection, simply click the connection.
 The NI-SWITCH SFP makes the appropriate connect/disconnect calls to the
 driver.

Related information:

- NI Product Documentation Center

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=the-matrix-topology.html language=enus -->
## TOPIC 00044: The Matrix Topology

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `the-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/the-matrix-topology.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: A matrix is a flexible topology that can connect multiple inputs to multiple outputs organized as columns and rows. You can connect any column to any number of rows and any row to any number of columns. Refer to the NI Switches Help for more information about matrix topologies. The Matrix SchematicO

### The Matrix Topology

A matrix is a flexible topology that can connect multiple inputs to multiple outputs organized as
 columns and rows. You can connect any column to any number of rows and any row to any
 number of columns. Refer to the NI Switches Help for more information
 about matrix topologies.

#### The Matrix Schematic

Note

[IMAGE alt='image' src='GUID-E5F25B33-982C-4370-9E10-A1E23038A844-a5.gif']

#### Make a Matrix Connection

Click a
 row-column cross-point to make a connection on the matrix. To break a connection,
 simply click the connection again. The NI-SWITCH SFP makes the appropriate
 connect/disconnect calls to the driver.

#### The Matrix Schematic for NI SwitchBlock
 Devices

You can also use the NI-SWITCH SFP to connect channels on
 different cards in an NI SwitchBlock multicard device or between multiple
 NI SwitchBlock devices. Refer to the following instructions for making connections
 to NI SwitchBlock devices in the NI-SWITCH SFP.

#### Connecting Channels Within an
 NI SwitchBlock Multicard Device

You can connect channels between cards in a multicard device by connecting the same
 analog bus channel to the corresponding row on each card.

Note

Card

The following schematic shows a connection between a row and column on the same card
 (card1r1 to c33 on card 1), and connections between channels on multiple cards in
 the same device through an analog bus line (row 0 connected to ab0 on both
 cards).

[IMAGE alt='image' src='GUID-D76D0C52-76C3-459B-86B0-8358F152487C-a5.gif']

The following schematic shows the connections required on card 2 of the previously
 mentioned multicard device to connect c82 on card 2 to c34 on card 1. The relay
 between row 0 and ab0 is closed on both cards.

[IMAGE alt='image' src='GUID-9A357482-BC9F-4A7D-84C8-36AF50C504F1-a5.gif']

#### Connecting Channels Between Multiple
 NI SwitchBlock Devices

You can use the NI-SWITCH SFP to enable sharing of an analog bus line and connect
 signals between multiple NI SwitchBlock devices in the same carrier or in adjacent
 carriers connected by the NI 2806 expansion bridge. Complete the following procedure
 to connect signals between multiple NI SwitchBlock devices in the NI-SWITCH SFP.

1. Determine which devices you would like to share an analog bus line.
2. In the Schematic tab, select one of the devices from the
 Device list.
3. Launch the Options dialog box
 ( File » Options ).
4. Click the Analog Bus tab in the Options dialog box.
5. Select the checkbox for the analog bus line that the device will share, then
 click OK .
6. In the Schematic tab, close the ab relay for the channel
 that corresponds to the shared analog bus line.
7. In the Schematic tab, make any additional connections to
 connect the desired end terminal on the device to the channel that you connected
 to the analog bus line in step 6.
8. Repeat steps 2-7 for each device you would like to share the analog bus
 line.

Refer to the *NI Product Documentation Center* for additional information
 about the use of the analog bus in NI SwitchBlock carriers.

Related information:

- NI Product Documentation Center

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=the-multiplexer-topology.html language=enus -->
## TOPIC 00045: The Multiplexer Topology

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `the-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/the-multiplexer-topology.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: A multiplexer, or a mux, is a topology in which you can connect one input to multiple outputs or one output to multiple inputs. Use this topology to connect a sequence of channels to a common line. Refer to the NI Product Documentation Center for more information about multiplexer topologies. You ca

### The Multiplexer Topology

NI Product Documentation Center

Note

Refer to the schematic below for an example of a switch module configured in a multiplexer topology.

[IMAGE alt='image' src='GUID-3CD6C4FC-A84D-4880-9853-D54B5472AB78-a5.gif']

#### Make a Multiplexer Connection

Click the end of the pole associated with the channel (left) you
 want to connect to the com channel (right). The NI-SWITCH SFP makes
 the appropriate connect/disconnect calls to the
 driver.

Related information:

- NI Product Documentation Center

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=the-single-pole-double-throw-topology.html language=enus -->
## TOPIC 00046: The Single-Pole Double-Throw Topology

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `the-single-pole-double-throw-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/the-single-pole-double-throw-topology.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: The single-pole double-throw (SPDT) topology is composed of one-pole, two-throw relays. Based on the default position of the pole, one throw is considered normally open (NO) while the other is normally closed (NC). Refer to the NI Product Documentation Center for more information about SPDT topologi

### The Single-Pole Double-Throw Topology

NI Product Documentation Center

Note

Refer to the schematic below for an example of the NI PXI-2566 in the 16-SPDT topology.

[IMAGE alt='image' src='GUID-C0492E8D-C66C-42DB-8409-54145FFE2D6C-a5.gif']

#### Make an SPDT Connection

Click on an
 individual relay to make an SPDT connection. To connect no5 to com5, for example,
 simply click on the relay. The pole connects no5 to com5, and the NI-SWITCH SFP
 makes the appropriate connect/disconnect calls to the driver.

Related information:

- NI Product Documentation Center

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=the-single-pole-single-throw-topology.html language=enus -->
## TOPIC 00047: The Single-Pole Single-Throw Topology

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `the-single-pole-single-throw-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/the-single-pole-single-throw-topology.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: The single-pole single-throw (SPST) topology is composed of one-pole, one-throw relays. Refer to the NI Product Documentation Center for more information about SPST relay forms. You can resize the SFP window to see more SPST relays. Refer to the schematic below for an example of the NI PXI-2564 in t

### The Single-Pole Single-Throw Topology

NI Product Documentation Center

Note

Refer to the schematic below for an example of the NI PXI-2564 in the 16-SPST topology.

[IMAGE alt='image' src='GUID-EDD31C09-B56C-4B64-AFEF-5B6B0AF13C3D-a5.gif']

#### Make an SPST Connection

Click on an
 individual relay to make an SPST connection. The NI-SWITCH SFP translates this click
 into the appropriate channel connection and makes the connect call to the driver. To
 connect ch2 to com2, for example, click on the relay. The pole connects ch2 to com2.
 To break a connection, simply click the connection. The NI-SWITCH SFP makes the
 appropriate connect/disconnect calls to the driver.

Related information:

- NI Product Documentation Center

<!--NI_TOPIC bundle=ni-switch-soft-front-panel path=user-manual-welcome.html language=enus -->
## TOPIC 00048: NI-SWITCH Soft Front Panel User Manual

- bundle_id: `ni-switch-soft-front-panel`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-soft-front-panel/raw/resource/enus/user-manual-welcome.html
- source_language: `enus`
- document_id: `ni-switch-soft-front-panel`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-SWITCH Soft Front Panel User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Informatio

### NI-SWITCH Soft Front Panel
 User Manual

The NI-SWITCH Soft Front Panel User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System
 Compatibility
- License Setup and Activation
