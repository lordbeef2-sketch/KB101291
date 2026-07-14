# NI DOCUMENT BUNDLE: ni-dcpower-compensating-lcr-measurements

<!--NI_BUNDLE_CHUNK bundle=ni-dcpower-compensating-lcr-measurements start=1 end=14 -->
<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=compensation-types-lcr.html language=enus -->
## TOPIC 00001: Types of Compensation for NI LCR Meters

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `compensation-types-lcr.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/compensation-types-lcr.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `concept`
- source_description: Compensation improves the accuracy of LCR measurements you make with NI LCR meters. There are multiple compensation types, which you can combine in various ways to achieve the accuracy you need. You can make LCR measurements your NI LCR meter without applying any compensation at all. However, the mo

Types of Compensation for NI LCR
 Meters

*Compensation* improves the accuracy of LCR measurements you make with NI LCR
 meters. There are multiple compensation types, which you can combine in various ways to
 achieve the accuracy you need.

You can make LCR measurements your NI LCR meter without applying any
 compensation at all. However, the more comprehensive your approach to compensation, the
 closer you can expect your measurements to be to the actual values of the quantities you
 are measuring. You can perform as much or as little compensation as is necessary for the
 degree of measurement accuracy your application requires.

There are two overall compensation types for NI LCR meters—*cable
 compensation* and *LCR compensation*—and there are a few ways to
 perform each based on your test setup and requirements.

Cable compensation

- Standard cable compensation —Applies a
 compensation for a typical NI-made cable of supported lengths. Does not
 require you to generate compensation data experimentally.
- Custom cable compensation —Generates
 compensation data for your specific test setup using open and short
 configurations. Best suited to complex test setups or setups that
 involve non-NI cables.

LCR compensation

- Open LCR compensation —Generates data to
 compensate for stray admittance in your test setup by determining
 corrections when the circuit is open.
- Short LCR compensation —Generates data
 to compensate for residual impedance in your test setup by determining
 corrections when the circuit is shorted and no DUT is connected.
- Load LCR compensation —Generates data to
 compensate for effects in complex circuit configurations that open and
 short compensation alone cannot account for by determining corrections
 when a reference load with well-known characteristics that are similar
 to those of your DUT is used in place of the DUT.

Access this compensation functionality with the NI-DCPower instrument driver, which provides the API that
 controls NI LCR meters.

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-applying-standard-cable-compensation.html language=enus -->
## TOPIC 00002: Selecting a Standard Cable Compensation

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-applying-standard-cable-compensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-applying-standard-cable-compensation.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `task`
- source_description: Standard cable compensation applies a preset compensation based on supported NI cables. Standard cable compensation is the simplest way to improve your LCR measurements because you do not need to manually generate your own cable compensation data. Complete this process only in the context of the ove

Selecting a Standard Cable
 Compensation

Standard cable compensation applies a preset compensation based on supported NI cables.
 Standard cable compensation is the simplest way to improve your LCR measurements because you do
 not need to manually generate your own cable compensation data.

Note

Compensating an NI LCR Meter

Note

Supported cables are those NI cables represented by an "NI
 Standard" value of the Cable Length property. Though standard
 cable compensation may also improve LCR measurements with non-NI cables, NI
 recommends custom cable compensation for such setups.

Cable Length

| Cable Type | Description |
| --- | --- |
| NI standard cable | Set Cable Length to the "NI Standard" length that corresponds to your NI cabling. |
| Non-NI cable | Set Cable Length to the "NI Standard" length that best describes your non-NI cable. |

Note

Once you have completed this process, return to *Compensating an NI
 LCR Meter* to continue any other parts of the overall compensation process you want
 to perform.

Parent topic:

Compensating an NI LCR Meter

Related tasks:

- Compensating an NI LCR Meter

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-compensating-lcr-measurements.html language=jajp -->
## TOPIC 00003: NI-DCPowerを使用したLCR測定補正

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-compensating-lcr-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/jajp/ni-dcpower-compensating-lcr-measurements.html
- source_language: `jajp`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `topic`
- source_description: NI-DCPowerを使用したLCR測定補正 補正を実行することにより、NI-DCPowerで行うLCR測定の確度が向上します。NI-DCPowerには、複数の補正方法が用意されており、これらを組み合わせることで、必要な確度を得ることができます。 NI-DCPowerでは、補正を何も適用しないでLCR測定を行うことができます。ただし、補正に関して、より包括的なアプローチをとれば、それだけ測定対象の本当の値に近い値が測定できることが期待できます。ユーザは、アプリケーションで必要な測定確度に応じて、どれだけ補正を実行するかを選択することができます。 LCR機能をサポートするNI-DCPower計測

NI-DCPowerを使用したLCR測定補正

#### NI-DCPowerを使用したLCR測定補正

補正を実行することにより、NI-DCPowerで行うLCR測定の確度が向上します。NI-DCPowerには、複数の補正方法が用意されており、これらを組み合わせることで、必要な確度を得ることができます。

NI-DCPowerでは、補正を何も適用しないでLCR測定を行うことができます。ただし、補正に関して、より包括的なアプローチをとれば、それだけ測定対象の本当の値に近い値が測定できることが期待できます。ユーザは、アプリケーションで必要な測定確度に応じて、どれだけ補正を実行するかを選択することができます。

LCR機能をサポートするNI-DCPower計測器では、「ケーブル補正」** と「LCR補正」**という2つの全体的な補正タイプがあり、テストのセットアップと要件に応じて、それぞれを実行する方法がいくつかあります。

ケーブル補正

NI-DCPower

標準ケーブル補正

カスタムケーブル補正

LCR補正

NI-DCPower

開放LCR補正

短絡LCR補正

負荷LCR補正

#### どの補正を実行すべきかを決定する

ケーブル補正とLCR補正の両方を実行するための複数のオプションがあります。採用する必要のあるアプローチは、テストセットアップ、およびアプリケーションに必要な確度と補正の実行に必要な労力のトレードオフによって異なります。

確度を最大限に高めるために、少なくとも何らかの形の補正を実行することをお勧めしますが、LCR測定を行う前に補正を実行する必要はありません。

以下を参照して、実行する可能性のある補正のタイプと、関連する補正のタイプについて、収集して適用する可能性のある補正データのセット数を決定してください。

1. 次の基準に基づいて、実行するケーブル補正を決定します。 org.dita.html5/xsl/topic.xsl 455メモ 特に、ケーブルの影響が測定量に比べて重要である可能性がある低レベルのLCR測定の場合は、確度を最大限に高めるために、ケーブル補正を適用することをお勧めします。 オプション推奨される場合標準ケーブル補正 ケーブルの長さプロパティ内のプロファイルで表される標準NIケーブルを使用している。テストのセットアップは単純で、LCR測定に影響を与える可能性のあるスイッチなどの複雑な回路は除外されている。カスタムケーブル補正 セットアップに、NI以外のケーブルが使用されている。 テストのセットアップが複雑である。LCR測定に影響を与える可能性のあるスイッチなどの複雑な回路が含まれている。
2. 次の基準に基づいて、実行するLCR補正を決定します。 オプション推奨される場合開放LCR補正 テストのセットアップで漂遊アドミタンスがLCR測定に影響を与える可能性がある。このような漂遊アドミタンスは、ほとんどのテスト設定に存在します。短絡LCR補正 DUTのインピーダンスが低い (<100Ω) ため、ケーブルと装置の残留インピーダンスは、DUTインピーダンスの有意の割合になる可能性がある。負荷LCR補正 DUTと同様の基準負荷の値を知っているか、高い信頼度で特定できる。かつ、テストのセットアップが複雑である。LCR測定に影響を与える可能性のあるスイッチなどの複雑な回路が含まれている。オープンおよびショートのLCR補正だけでは、アプリケーションに十分な確度は得られない。org.dita.html5/xsl/topic.xsl 455メモ 負荷LCR補正を実行する場合は、開放 (オープン) および短絡 (ショート) LCR補正も実行する必要があります。
3. カスタムケーブル補正またはLCR補正を実行している場合は、補正データのセットをいくつ生成すればメリットが得られるかを次の基準に基づいて決定します。 オプション推奨される場合1つのデータセット テスト構成が1つだけであるか、測定確度を向上させるために1つのデータセットで十分な、単純なアプリケーション。複数のデータセット さまざまな測定条件があり、最大限の確度を必要とする、複雑なアプリケーション。次のようなアプリケーションが該当します。ウエハテスト。テストを行っており、ウエハ上の複数の物理的な位置を補正できるスイッチを使用して、スイッチを通るさまざまなパスを補正できる同じ実行で、シリアル番号ではなく部品番号に基づいて異なるDUTをテストするさまざまな測定パラメータを使用する org.dita.html5/xsl/topic.xsl 455メモ 複数の補正データのセットを生成する場合は、実行する補正タイプごとに同じ数のデータセットを生成する必要があります。たとえば、2つの異なるテストポイントがあり、カスタムケーブル補正と3種類のLCR補正すべてを実行する場合は、カスタムケーブル補正データ、開放LCR補正データ、短絡LCR補正データ、負荷LCR補正データをそれぞれ2セット生成します。

NI-DCPowerでLCRメータを補正する

#### NI-DCPowerでLCRメータを補正する

NI-DCPower LCRメータの補正プロセスを実行するには、次の手順に従ってください。アプリケーションに必要な確度と必要な労力の間のトレードオフに基づいて、LCRテストセットアップに対して実行する補正を柔軟に選択することができます。

始める前に、[どの補正を実行すべきかを決定する](ni-dcpower-compensating-lcr-measurements.html#GUID-3A7877BF-1055-4C92-BF22-3A9DDE7BCC75)を完了してください。

さらに、計測器を外部キャリブレーションする予定がある場合は、このプロセスを開始する前に外部校正を実行します。

LCRテストセットアップに対して実行する補正に基づいて、次の手順を実行します。

1. 使用しているプログラミング環境またはMeasurement & Automation Explorer (MAX) で、「Calセルフキャリブレーションを実行」を使用して、補正するチャンネルを自己校正します。
2. *ケーブル補正*を実行したい場合は、関連する手順を実行します。
  - 標準ケーブル補正: 標準ケーブル補正を選択する
  - カスタムケーブル補正: カスタムケーブル補正データを生成する
3. *カスタムケーブル補正*を実行したい場合は、生成した補正データセットの数に応じて、測定値に補正を適用します。
  - カスタムケーブル補正を適用する: 1つのデータセット
  - カスタムケーブル補正を適用する: 複数のデータセット
4. *LCR補正*を実行したい場合は、関連する手順を実行します。
  - 開放LCR補正: 開放LCR補正データを生成する
  - 短絡LCR補正: 短絡LCR補正データを生成する
  - 負荷LCR補正: 負荷LCR補正データを生成する
5. *LCR補正*を実行したい場合は、生成した補正データセットの数に応じて、測定値に補正を適用します。
  - LCR補正を適用する: 1つのデータセット
  - LCR補正を適用する: 複数のデータセット

アプリケーションに必要であると特定したこのプロセス全体の一部を完了すると、関連する修正がLCR測定に適用され、テストセットアップの測定の品質が向上します。

メモ

カスタムケーブル補正またはLCR補正用に新しいデータを生成することが必要な場合

##### 標準ケーブル補正を選択する

標準ケーブル補正は、サポートされているNIケーブル用に事前設定された補正を適用します。標準ケーブル補正は、独自のケーブル補正データを手動で生成する必要がないため、LCR測定を向上させる最も簡単な方法です。

メモ

NI-DCPowerでLCRメータを補正する

メモ

サポートされているケーブルは、ケーブルの長さプロパティの値が「NI標準」であるNIケーブルです。標準ケーブル補正によりNI以外のケーブル使用するLCR測定が向上する可能性もありますが、NI以外のケーブルを使用するセットアップにはカスタムケーブル補正を推奨します。

ケーブルの長さ

| ケーブルタイプ | 説明 |
| --- | --- |
| NI標準ケーブル | ケーブルの長さをNIケーブルに対応する「NI標準」の長さに設定します。 |
| NI以外のケーブル | ケーブルの長さをNI以外のケーブルの長さに相当する「NI標準」の長さに設定します。 |

メモ

このプロセスが完了したら、[NI-DCPowerでLCRメータを補正する](ni-dcpower-compensating-lcr-measurements.html#GUID-E2339A51-BDD1-425C-989A-3CDA2860107A)に戻り、実行したい全体的な補正プロセスの他の部分を続行します。

##### カスタムケーブル補正データを生成する

カスタムケーブル補正は、テストのセットアップに合わせて補正を計算します。カスタムケーブル補正を生成するには、テスト装置で開放接続と (オプションで) 短絡接続を設定して、実験的に補正を決定する必要があります。

メモ

NI-DCPowerでLCRメータを補正する

メモ

通知

LCRテストセットアップ用のカスタムケーブル補正データを生成するには、次の手順を実行します。

1. 図のように、テスト装置全体で回路を開放します。 図 1.補正: 開放セットアップ. 次の図は、4端子ペア (4TP) 接続スキームです。 
[IMAGE alt='1378' src='GUID-5A7AF4E2-EFE9-4A80-B0BF-DD3B35FA7367-a5.svg'] 
 HI CUR HI POT LO POT LO CUR 絶縁シールド導線間の接続
2. 開放補正データを生成するために、LCR開放カスタムケーブル補正を実行を呼び出します。 この関数を呼び出すと、開放データが計測器のオンボードストレージに書き込まれます。オンボードストレージに記録されるのは、最新のLCR開放カスタムケーブル補正を実行した結果データのみです。org.dita.html5/xsl/topic.xsl 455メモ この関数を呼び出すと、セッションのほとんどのNI-DCPowerプロパティはデフォルト値にリセットされます。
3. 維持したいすべてのセッションプロパティの値を再度書き込んでください。
4. 独自の短絡カスタムケーブル補正データを生成する必要があるかどうかを判断します。 オプション説明独自のデータを生成する アプリケーションで短絡接続を設定できる場合は、独自のデータを生成します。 データは正確なセットアップで計算されるため、最高の確度が得られます。 このオプションを使用する場合は、ステップ[5](ni-dcpower-compensating-lcr-measurements.html#GUID-74630D35-7A7D-42CD-B2C0-4CA909D44E04__STEP_R5P_WXW_WPB)に進んでください。デフォルトのデータを使用する アプリケーションで短絡接続を設定することが現実的でない場合は、デフォルトのデータを使用してください。 デフォルトのデータはお使いのセットアップ用にカスタム生成されたものではありませんが、短絡接続を設定する必要がありません。 このオプションを使用する場合は、ステップ[8](ni-dcpower-compensating-lcr-measurements.html#GUID-74630D35-7A7D-42CD-B2C0-4CA909D44E04__STEP_QYN_BMQ_3QB)に進んでください。
5. 図のように、テスト装置全体で物理的な短絡を構成します。 図 2.補正: 短絡セットアップ. 次の図は、4端子ペア (4TP) 接続スキームです。 
[IMAGE alt='1378' src='GUID-237DDE93-0550-49DA-963E-061485A827D5-a5.svg'] 
 HI CUR HI POT LO POT LO CUR 絶縁シールド導線間の接続
6. 開放短絡データを生成するために、LCR短絡カスタムケーブル補正を実行を呼び出します。 この関数を呼び出すと、短絡データが計測器のオンボードストレージに書き込まれます。オンボードストレージに記録されるのは、最新のLCR短絡カスタムケーブル補正を実行した結果データのみです。org.dita.html5/xsl/topic.xsl 455メモ この関数を呼び出すと、セッションのほとんどのNI-DCPowerプロパティはデフォルト値にリセットされます。
7. 維持したいすべてのセッションプロパティの値を再度書き込んでください。
8. アプリケーションで必要な個別の補正データのセットの数に基づいて、補正データを準備します。 必要なデータ説明1セット 必要な操作はありません。計測器のオンボードストレージには、開放カスタムケーブル補正データがすでに含まれています (生成された場合)。複数セット 前回生成されたカスタムケーブル補正データを、追跡可能な個別のデータセットとして返す「LCRカスタムケーブル補正データを取得」を呼び出します。 アプリケーションで必要なカスタムケーブル補正データのセットごとにステップ[1](ni-dcpower-compensating-lcr-measurements.html#GUID-74630D35-7A7D-42CD-B2C0-4CA909D44E04__STEP_J25_SXW_WPB)～[8](ni-dcpower-compensating-lcr-measurements.html#GUID-74630D35-7A7D-42CD-B2C0-4CA909D44E04__STEP_QYN_BMQ_3QB)を繰り返します。

これで、セットアップ用のすべてのカスタムケーブル補正データが生成されました。関連付けられている補正は、まだ測定に適用されていません。

このプロセスが完了したら、[NI-DCPowerでLCRメータを補正する](ni-dcpower-compensating-lcr-measurements.html#GUID-E2339A51-BDD1-425C-989A-3CDA2860107A)に戻り、実行したい全体的な補正プロセスの他の部分を続行します。

##### カスタムケーブル補正を適用する: 1つのデータセット

LCR測定に1つのカスタムケーブル補正用修正を適用するには、次の手順に従います。

メモ

NI-DCPowerでLCRメータを補正する

1. 独自の短絡カスタムケーブル補正データを生成したか、デフォルトデータを適用するかに応じて、LCR短絡カスタムケーブル補正が有効を次のように設定します。
  - 短絡データを生成した: TRUE
  - デフォルトデータを使用する: FALSE
2. ケーブルの長さを「カスタム (オンボードストレージ)」に設定します。

これで、生成した補正データがLCR測定に適用されます。

このプロセスが完了したら、[NI-DCPowerでLCRメータを補正する](ni-dcpower-compensating-lcr-measurements.html#GUID-E2339A51-BDD1-425C-989A-3CDA2860107A)に戻り、実行したい全体的な補正プロセスの他の部分を続行します。

##### カスタムケーブル補正を適用する: 複数のデータセット

LCR測定に複数のカスタムケーブル補正用修正を適用するには、次の手順に従います。

メモ

NI-DCPowerでLCRメータを補正する

1. ケーブルの長さを「カスタム (構成に従う)」に設定します。
2. 独自の短絡カスタムケーブル補正データを生成したか、デフォルトデータを適用するかに応じて、LCR短絡カスタムケーブル補正が有効を次のように設定します。
  - 短絡データを生成した: TRUE
  - デフォルトデータを使用する: FALSE
3. LCRカスタムケーブル補正データを取得で生成したカスタムケーブル補正データのセットごとに、プログラム内の、データセットが該当し、対応するカスタムケーブル補正データを提供する、テスト条件に対応するポイントでLCRカスタムケーブル補正を構成を呼び出します。

これで、生成した補正データがLCR測定に適用されます。

このプロセスが完了したら、[NI-DCPowerでLCRメータを補正する](ni-dcpower-compensating-lcr-measurements.html#GUID-E2339A51-BDD1-425C-989A-3CDA2860107A)に戻り、実行したい全体的な補正プロセスの他の部分を続行します。

##### 開放LCR補正データを生成する

開放LCR補正データを生成すると、LCR測定に適用できる補正が計算されます。

メモ

NI-DCPowerでLCRメータを補正する

メモ

適用するケーブル補正データは、このプロセスで生成されるLCR補正データに影響を与えます。このプロセスを実行する前に、標準のケーブル補正を適用するか、カスタムケーブル補正データを適用してください。

通知

開放LCR補正データを生成するには、次の手順を実行します。

1. 図のように、テスト装置全体で回路を開放します。 図 3.補正: 開放セットアップ. 次の図は、4端子ペア (4TP) 接続スキームです。 
[IMAGE alt='1378' src='GUID-5A7AF4E2-EFE9-4A80-B0BF-DD3B35FA7367-a5.svg'] 
 HI CUR HI POT LO POT LO CUR 絶縁シールド導線間の接続
2. ケーブル補正に関連する設定を、実行したケーブル補正に対応するように次のように再構成します。 ケーブル補正オプション説明標準ケーブル補正 ケーブルの長さを、選択したNI標準オプションに設定します。カスタムケーブル補正 ケーブルの長さを、使用したカスタムオプションに設定します。 LCR短絡カスタムケーブル補正が有効を、カスタムケーブル補正を適用したときと同じに設定します。 ケーブルの長さとして「カスタム (構成に従う)」を選択した場合、プログラムの現在のポイントのために生成したカスタムケーブル補正データを渡して「LCRカスタムケーブル補正を構成」を呼び出します。
3. 「LCR開放補正を実行」を呼び出して、補正したい周波数を指定します。 この関数は、テスト周波数のデフォルトセットと、追加指定できる周波数に基づいて、補正データを生成します。NI-DCPowerは、これらの周波数以外の周波数の補正を補間します。 この関数を呼び出すと、開放データが計測器のオンボードストレージに書き込まれます。オンボードストレージに記録されるのは、最新の開放LCR補正を実行した結果データのみです。org.dita.html5/xsl/topic.xsl 455メモ この関数を呼び出すと、セッションのほとんどのNI-DCPowerプロパティはデフォルト値にリセットされます。
4. 維持することが必要なすべてのセッションプロパティの値を再度書き込んでください。
5. アプリケーションで必要な個別の補正データのセットの数に基づいて、補正データを管理します。 必要なデータ説明1セット 必要な操作はありません。計測器のオンボードストレージには、すでに開放データが含まれています。複数セット 「複数のLCRを測定」または「複数のLCRをフェッチ」を使用して回路の複素アドミタンス (Y) を測定します。 複素アドミタンスからコンダクタンスとサセプタンスを計算し、それらの値を追跡します。 アプリケーションに関連する場合は、次の補正ポイント用にセットアップを物理的に変更します。 アプリケーションで必要な開放LCR補正データのセットごとにステップ[2](ni-dcpower-compensating-lcr-measurements.html#GUID-3D89AE25-9FB9-42D5-A3A2-2F8F81756C99__STEP_XR1_WXQ_WQB)～[5](ni-dcpower-compensating-lcr-measurements.html#GUID-3D89AE25-9FB9-42D5-A3A2-2F8F81756C99__STEP_EX2_FT2_JQB)を繰り返します。

これで、セットアップ用のすべての開放LCR補正データが生成されました。関連付けられている補正は、まだ測定に適用されていません。

このプロセスが完了したら、[NI-DCPowerでLCRメータを補正する](ni-dcpower-compensating-lcr-measurements.html#GUID-E2339A51-BDD1-425C-989A-3CDA2860107A)に戻り、実行したい全体的な補正プロセスの他の部分を続行します。

##### 短絡LCR補正データを生成する

短絡LCR補正データを生成すると、LCR測定に適用できる補正が計算されます。

メモ

NI-DCPowerでLCRメータを補正する

メモ

適用するケーブル補正データは、このプロセスで生成されるLCR補正データに影響を与えます。このプロセスを実行する前に、標準のケーブル補正を適用するか、カスタムケーブル補正データを適用してください。

通知

短絡LCR補正データを生成するには、次の手順を実行します。

1. 図のように、テスト装置全体で物理的な短絡を構成します。 図 4.補正: 短絡セットアップ. 次の図は、4端子ペア (4TP) 接続スキームです。 
[IMAGE alt='1378' src='GUID-237DDE93-0550-49DA-963E-061485A827D5-a5.svg'] 
 HI CUR HI POT LO POT LO CUR 絶縁シールド導線間の接続
2. ケーブル補正に関連する設定を、実行したケーブル補正に対応するように次のように再構成します。 ケーブル補正オプション説明標準ケーブル補正 ケーブルの長さを、選択したNI標準オプションに設定します。カスタムケーブル補正 ケーブルの長さを、使用したカスタムオプションに設定します。 LCR短絡カスタムケーブル補正が有効を、カスタムケーブル補正を適用したときと同じに設定します。 ケーブルの長さとして「カスタム (構成に従う)」を選択した場合、プログラムの現在のポイントのために生成したカスタムケーブル補正データを渡して「LCRカスタムケーブル補正を構成」を呼び出します。
3. 「LCR短絡補正を実行」を呼び出して、補正したい周波数を指定します。 この関数は、テスト周波数のデフォルトセットと、追加指定できる周波数に基づいて、補正データを生成します。NI-DCPowerは、これらの周波数以外の周波数の補正を補間します。 この関数を呼び出すと、短絡データが計測器のオンボードストレージに書き込まれます。オンボードストレージに記録されるのは、最新の短絡LCR補正を実行した結果データのみです。org.dita.html5/xsl/topic.xsl 455メモ この関数を呼び出すと、セッションのほとんどのNI-DCPowerプロパティはデフォルト値にリセットされます。
4. 維持することが必要なすべてのセッションプロパティの値を再度書き込んでください。
5. アプリケーションで必要な個別の補正データのセットの数に基づいて、補正データを管理します。 必要なデータ説明1セット 必要な操作はありません。計測器のオンボードストレージには、すでに短絡データが含まれています。複数セット 「複数のLCRを測定」または「複数のLCRをフェッチ」を使用して回路の複素インピーダンス (Z) を測定します。 複素インピーダンスから抵抗とリアクタンスを計算し、それらの値を追跡します。 アプリケーションに関連する場合は、次の補正ポイント用にセットアップを物理的に変更します。 アプリケーションで必要な短絡LCR補正データのセットごとにステップ[2](ni-dcpower-compensating-lcr-measurements.html#GUID-31C81272-8F15-4208-9734-7C2724EB32E7__STEP_HTF_WYQ_WQB)～[5](ni-dcpower-compensating-lcr-measurements.html#GUID-31C81272-8F15-4208-9734-7C2724EB32E7__STEP_E5V_2Y2_JQB)を繰り返します。

これで、セットアップ用のすべての短絡LCR補正データが生成されました。関連付けられている補正は、まだ測定に適用されていません。

このプロセスが完了したら、[NI-DCPowerでLCRメータを補正する](ni-dcpower-compensating-lcr-measurements.html#GUID-E2339A51-BDD1-425C-989A-3CDA2860107A)に戻り、実行したい全体的な補正プロセスの他の部分を続行します。

##### 負荷LCR補正データを生成する

負荷LCR補正データを生成すると、LCR測定に適用できる補正が計算されます。

メモ

NI-DCPowerでLCRメータを補正する

メモ

適用するケーブル補正データは、このプロセスで生成されるLCR補正データに影響を与えます。このプロセスを実行する前に、標準のケーブル補正を適用するか、カスタムケーブル補正データを適用してください。

メモ

通知

負荷LCR補正データを生成するには、次の手順を実行します。

1. 図のように、DUTを含む装置に基準負荷を接続します。 図 5.補正: 負荷セットアップ. 次の図は、4端子ペア (4TP) 接続スキームです。 
[IMAGE alt='1378' src='GUID-F35079AE-7DEF-4BF2-80CD-EDB3A6CE4274-a5.svg'] 
 HI CUR HI POT LO POT LO CUR 絶縁シールド導線間の接続
2. ケーブル補正に関連する設定を、実行したケーブル補正に対応するように次のように再構成します。 ケーブル補正オプション説明標準ケーブル補正 ケーブルの長さを、選択したNI標準オプションに設定します。カスタムケーブル補正 ケーブルの長さを、使用したカスタムオプションに設定します。 LCR短絡カスタムケーブル補正が有効を、カスタムケーブル補正を適用したときと同じに設定します。 ケーブルの長さとして「カスタム (構成に従う)」を選択した場合、プログラムの現在のポイントのために生成したカスタムケーブル補正データを渡して「LCRカスタムケーブル補正を構成」を呼び出します。
3. 生成された負荷LCR補正データに影響を与える追加のプロパティを設定します。 ケーブル補正の他に、このプロセスで生成する負荷LCR補正データに影響を与えるプロパティは、次のとおりです。電流補正周波数電流GBW電流の極/零点比LCR電流振幅LCRカスタム測定時間LCR DCバイアス電流レベルLCR DCバイアスソースLCR DCバイアス電圧レベルLCRインピーダンスレンジLCR測定時間LCR刺激機能LCR電圧振幅ソース遅延過渡応答電圧補正周波数電圧GBW電圧の極/零点比
4. 「LCR負荷補正を実行」を呼び出し、DUTで必要な負荷補正スポットを提供します。 org.dita.html5/xsl/topic.xsl 455メモ この関数は、指定した補正スポットに関する補正データのみを生成します。NI-DCPowerは、これらのスポット間の領域の補正データを補間しません。 この関数を呼び出すと、負荷データが計測器のオンボードストレージに書き込まれます。オンボードストレージに記録されるのは、最新の負荷LCR補正を実行した結果データのみです。org.dita.html5/xsl/topic.xsl 455メモ この関数を呼び出すと、セッションのほとんどのNI-DCPowerプロパティはデフォルト値にリセットされます。
  1. 補正するテスト周波数を提供する。
  2. 基準値タイプ (基準負荷の既知の仕様) を選択する。
  3. 基準値Aと基準値Bを使用して仕様値を提供する。 値タイプごとの基準値Aと基準値Bの使用方法については、選択した基準値タイプのドキュメントを参照してください。
  4. 必要なスポットに対して、許可されている最大スポット数以下の範囲で、ステップ[4.a](ni-dcpower-compensating-lcr-measurements.html#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__SUBSTEP_QLK_S3Y_WPB)～[4.c](ni-dcpower-compensating-lcr-measurements.html#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__SUBSTEP_FWZ_CJY_WPB)を繰り返します。
5. 維持することが必要なすべてのセッションプロパティの値を再度書き込んでください。
6. アプリケーションで必要な個別の補正データのセットの数に基づいて、補正データを管理します。 必要なデータ説明1セット 必要な操作はありません。計測器のオンボードストレージには、すでに負荷データが含まれています。複数セット 「複数のLCRを測定」または「複数のLCRをフェッチ」を使用して回路の複素インピーダンス (Z) を測定します。 複素インピーダンスから抵抗とリアクタンスを計算し、それらの値を追跡します。 アプリケーションに関連する場合は、次の補正ポイント用にセットアップを物理的に変更します。 アプリケーションで特定の基準負荷とDUTの組み合わせに必要な負荷LCR補正データのセットごとにステップ[2](ni-dcpower-compensating-lcr-measurements.html#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__STEP_HTF_WYQ_WQB)～[6](ni-dcpower-compensating-lcr-measurements.html#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__STEP_OQW_F1F_JQB)を繰り返します。 複数の基準負荷とDUTの組み合わせのデータも生成する必要がある場合は、ステップ[1](ni-dcpower-compensating-lcr-measurements.html#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__STEP_THG_YGY_WPB)～[6](ni-dcpower-compensating-lcr-measurements.html#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__STEP_OQW_F1F_JQB)を繰り返します。

これで、セットアップ用のすべての負荷LCR補正データが生成されました。関連付けられている補正は、まだ測定に適用されていません。

このプロセスが完了したら、[NI-DCPowerでLCRメータを補正する](ni-dcpower-compensating-lcr-measurements.html#GUID-E2339A51-BDD1-425C-989A-3CDA2860107A)に戻り、実行したい全体的な補正プロセスの他の部分を続行します。

##### LCR補正を適用する: 1つのデータセット

測定に1セットのLCR補正を適用するには、次の手順に従います。

メモ

NI-DCPowerでLCRメータを補正する

メモ

1. LCR開放/短絡/負荷補正データソースを「オンボードストレージ」に設定します。
2. データを生成したLCR補正に基づいて、関連付けられているNI-DCPowerプロパティをTRUEに設定します。 開放: LCR開放補正が有効 短絡: LCR短絡補正が有効 負荷: LCR負荷補正が有効 各プロパティを有効にすると、NI-DCPowerにより、関連付けられているチャンネルのLCR測定に、対応する補正に基づく修正を適用することが可能になります。

これで、生成した補正データがLCR測定に適用されます。

このプロセスが完了したら、[NI-DCPowerでLCRメータを補正する](ni-dcpower-compensating-lcr-measurements.html#GUID-E2339A51-BDD1-425C-989A-3CDA2860107A)に戻り、実行したい全体的な補正プロセスの他の部分を続行します。

##### LCR補正を適用する: 複数のデータセット

測定に複数のLCR補正用修正を適用するには、次の手順に従います。

メモ

NI-DCPowerでLCRメータを補正する

メモ

1. LCR開放/短絡/負荷補正データソースを「定義に従う」に設定します。
2. 生成したLCR補正データのセットごとに、データセットを適用するテスト条件に対応するプログラム内のポイントで、追跡した値を関連するプロパティに書き込みます。 LCR補正タイプ プロパティ開放LCR補正 LCR開放コンダクタンス LCR開放サセプタンス短絡LCR補正 LCR短絡抵抗 LCR短絡リアクタンス負荷LCR補正 LCR負荷抵抗測定値 LCR負荷リアクタンス測定値 LCR実際の負荷抵抗 LCR実際の負荷リアクタンス
3. データを生成したLCR補正に基づいて、関連付けられているNI-DCPowerプロパティをTRUEに設定します。 開放: LCR開放補正が有効 短絡: LCR短絡補正が有効 負荷: LCR負荷補正が有効 各プロパティを有効にすると、NI-DCPowerにより、関連付けられているチャンネルのLCR測定に、対応する補正に基づく修正を適用することが可能になります。

これで、生成した補正データがLCR測定に適用されます。

このプロセスが完了したら、[NI-DCPowerでLCRメータを補正する](ni-dcpower-compensating-lcr-measurements.html#GUID-E2339A51-BDD1-425C-989A-3CDA2860107A)に戻り、実行したい全体的な補正プロセスの他の部分を続行します。

#### カスタムケーブル補正またはLCR補正用に新しいデータを生成することが必要な場合

テストセットアップの特定の要素が変更され、カスタムケーブル補正または任意のタイプのLCR補正を実行した場合、生成した補正データは古くなり、効果が低下するため、補正データを再計算する必要があります。

次のいずれかの場合は、新しいカスタムケーブル補正データまたはLCR補正データを生成してください。

- 新しい外部校正を実行する
- 新規のセルフキャリブレーションを実行する
- ケーブルの端とDUTを含む装置の間に、スイッチなどの複雑な回路要素を追加する
- テストセットアップでケーブルの長さを変更する
- テストセットアップでケーブルの向きを変更する
- 最初に補正データを生成したDUTとは製品番号が異なるDUTのテストを開始する。負荷LCR補正の場合は、新しいDUTに適した新しい基準負荷も選択します。

ヒント

前回のLCR補正日時を取得

メモ

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-compensating-lcr.html language=enus -->
## TOPIC 00004: Compensating an NI LCR Meter

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-compensating-lcr.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-compensating-lcr.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `task`
- source_description: Follow this overall process to perform compensation for an NI LCR meter. You have the flexibility to choose which compensations to perform for your LCR test setup based on the tradeoff between the accuracy you need for your application and the effort required. If your instrument is due for an extern

Compensating an NI LCR Meter

Follow this overall process to perform compensation for an NI LCR meter. You have the
 flexibility to choose which compensations to perform for your LCR test setup based on the
 tradeoff between the accuracy you need for your application and the effort required.

If your instrument is due for an external calibration, perform the
 external calibration before beginning this process.

Complete the following steps to compensate your NI LCR meter:

Note

1. Self-calibrate the channels you are compensating with Cal Self
 Calibrate in your programming environment or in Measurement & Automation
 Explorer (MAX).
2. Complete [Determining
 Which Compensations to Perform](ni-dcpower-lcr-determining-compensations.html).
3. If you want to perform a *cable compensation*, complete the relevant
 procedure(s): 
 Type of Cable CompensationProceduresStandard cable compensation
 Complete [Selecting a Standard Cable Compensation](ni-dcpower-applying-standard-cable-compensation.html)Custom cable compensation
 Create the compensation data with [Generating Custom
 Cable Compensation Data](ni-dcpower-generating-custom-cable-compensation-data.html)
 Depending on how many discrete sets of custom cable
 compensation data you generated, complete the relevant procedure to apply the data
 to your measurements:Single set: [Applying Custom
 Cable Compensation: Single Data Set](ni-dcpower-custom-cable-compensation-applying-single-set.html)
 Multiple sets: [Applying Custom
 Cable Compensation: Multiple Data Sets](ni-dcpower-lcr-compensation-applying-multiple-sets.1.html)
4. If you want to perform any type of *LCR compensation*, complete the relevant
 procedure(s):
  1. Create the compensation data for each type of LCR compensation you want to
 perform: 
 Open LCR compensation: [Generating Open LCR
 Compensation Data](ni-dcpower-generating-open-lcr-data.html)
 Short LCR compensation: [Generating Short
 LCR Compensation Data](ni-dcpower-generating-short-lcr-data.html)
 Load LCR compensation: [Generating Load LCR
 Compensation Data](ni-dcpower-generating-load-lcr-data.html)
  2. Depending on how many discrete sets of LCR compensation data you generated,
 complete the relevant procedure to apply the data to your measurements: 
 Single set: [Applying LCR
 Compensation: Single Data Set](ni-dcpower-lcr-compensation-applying-single-set.html)
 Multiple sets: [Applying LCR
 Compensation: Multiple Data Sets](ni-dcpower-lcr-compensation-applying-multiple-sets.html)

Once you completing this overall compensation process, the
 relevant corrections you chose are applied to your LCR measurements to improve the quality of
 those measurements within your test setup.

Note

When to Use New Data for Custom Cable Compensation or LCR Compensation

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-custom-cable-compensation-applying-single-set.html language=enus -->
## TOPIC 00005: Applying Custom Cable Compensation: Single Data Set

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-custom-cable-compensation-applying-single-set.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-custom-cable-compensation-applying-single-set.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `task`
- source_description: Use this process to apply a single set of custom cable compensation corrections to your LCR measurements. Complete this process only in the context of the overall compensation process described in Compensating an NI LCR Meter. Based on whether you generated your own short custom cable compensation d

Applying Custom Cable Compensation: Single
 Data Set

Use this process to apply a single set of custom cable compensation corrections to your
 LCR measurements.

Note

Compensating an NI LCR
 Meter

1. Based on whether you generated your own short custom cable
 compensation data or want to apply default data, set
 LCR Short Custom Cable Compensation
 Enabled as follows.
  - Generated short data:
 TRUE
  - Using default data:
 FALSE
2. Set Cable Length to Custom
 (Onboard Storage).

The compensation data you generated are now applied
 to your instrument.

Once you have completed this process, return to *Compensating an NI
 LCR Meter* to continue any other parts of the overall compensation process you want
 to perform.

Parent topic:

Compensating an NI LCR Meter

Related tasks:

- Compensating an NI LCR Meter

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-generating-custom-cable-compensation-data.html language=enus -->
## TOPIC 00006: Generating Custom Cable Compensation Data

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-generating-custom-cable-compensation-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-generating-custom-cable-compensation-data.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `task`
- source_description: Custom cable compensation calculates corrections specifically for your exact test setup. Generating custom cable compensation involves setting up open and, optionally, short connections at the test fixture to determine corrections experimentally. Complete this process only in the context of the over

Generating Custom Cable Compensation
 Data

Custom cable compensation calculates corrections specifically for your exact test setup.
 Generating custom cable compensation involves setting up open and, optionally, short
 connections at the test fixture to determine corrections experimentally.

Note

Compensating an NI LCR Meter

Note

Notice

Complete the following steps to generate custom cable compensation data for an LCR
 test setup:

1. Leave the circuit open across the test fixture as shown. 
 Figure 1.Compensation: Open Setup. Four-terminal pair (4TP) connection scheme shown.
 
 
 
[IMAGE alt='1378' src='GUID-5A7AF4E2-EFE9-4A80-B0BF-DD3B35FA7367-a5.svg'] 

 HI CUR
 HI POT
 LO POT
 LO CUR
 Connection between isolated shield conductors
2. Call Perform LCR Open Custom Cable Compensation to
 generate the open compensation data. 
 Calling this function writes the open data to the onboard storage of the
 instrument. Data from only the most recently performed open custom cable
 compensation is recorded in onboard storage.org.dita.html5/xsl/topic.xsl 455Note When you
 call this function, most NI-DCPower
 properties in the session are reset to their default
 values.
3. Rewrite the values for any session properties that you want to maintain.
4. Determine whether you need to generate your own short custom cable compensation
 data. 
 OptionDescriptionGenerate your own data
 Generate your own data when it is feasible for you
 to set up short connections in your application.
 Yields the best accuracy because the data is
 calculated for your exact setup.
 For this option, proceed with step [5](#GUID-74630D35-7A7D-42CD-B2C0-4CA909D44E04__STEP_R5P_WXW_WPB).Use default data
 Use the default data when it is not practical for
 you to set up the short connections in your application.
 You avoid having to set up short connections,
 though the default data is not custom-generated for your exact
 setup.
 For this option, skip to step [8](#GUID-74630D35-7A7D-42CD-B2C0-4CA909D44E04__STEP_QYN_BMQ_3QB).
5. Configure a physical short across the test fixture as shown. 
 Figure 2.Compensation: Short
 Setup. Four-terminal pair (4TP) connection scheme shown.
 
 
 
[IMAGE alt='1378' src='GUID-237DDE93-0550-49DA-963E-061485A827D5-a5.svg'] 

 HI CUR
 HI POT
 LO POT
 LO CUR
 Connection between isolated shield conductors
6. Call Perform LCR Short Custom Cable Compensation to
 generate the short compensation data. 
 Calling this function writes the short data to the onboard storage of
 the instrument. Data from only the most recently performed short custom cable
 compensation is recorded in onboard storage.org.dita.html5/xsl/topic.xsl 455Note When you
 call this function, most NI-DCPower
 properties in the session are reset to their default
 values.
7. Rewrite the values for any session properties that you want to maintain.
8. Prepare the compensation data, based on how many discrete sets of compensation
 data your application requires. 
 Data RequiredDescriptionSingle set
 No action required: onboard storage of the instrument already
 contains the open and, if generated, short custom cable compensation
 data.Multiple sets
 Call Get LCR Custom Cable
 Compensation Data, which returns the most
 recently generated custom cable compensation data as a discrete
 set of data that you can track.
 Repeat steps [1](#GUID-74630D35-7A7D-42CD-B2C0-4CA909D44E04__STEP_J25_SXW_WPB) through [8](#GUID-74630D35-7A7D-42CD-B2C0-4CA909D44E04__STEP_QYN_BMQ_3QB) for each discrete set of custom
 cable compensation data your application
 requires.

You have now generated all the custom cable compensation
 data for your setup. The associated corrections are not yet applied to your
 measurements.

Once you have completed this process, return to *Compensating an NI
 LCR Meter* to continue any other parts of the overall compensation process you want
 to perform.

Parent topic:

Compensating an NI LCR Meter

Related tasks:

- Compensating an NI LCR Meter

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-generating-load-lcr-data.html language=enus -->
## TOPIC 00007: Generating Load LCR Compensation Data

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-generating-load-lcr-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-generating-load-lcr-data.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `task`
- source_description: Generating load LCR compensation data calculates corrections that you can then apply to your LCR measurements. Complete this process only in the context of the overall compensation process described in Compensating an NI LCR Meter. Before you begin, follow any instructions for preparing your cables

Generating Load LCR Compensation Data

Generating load LCR compensation data calculates
 corrections that you can then apply to your LCR measurements.

Note

Compensating an NI LCR Meter

Note

The cable compensation data you apply affects the LCR compensation data
 you generate with this process. Apply a standard cable compensation or apply custom cable
 compensation data before performing this process.

Note

Notice

Complete the following steps to generate load LCR
 compensation data:

1. Connect a reference load to the fixture that will contain your
 DUT as shown. 
 Figure 5.Compensation: Load Setup. Four-terminal pair (4TP) connection scheme shown.
 
 
 
[IMAGE alt='1378' src='GUID-F35079AE-7DEF-4BF2-80CD-EDB3A6CE4274-a5.svg'] 

 HI CUR
 HI POT
 LO POT
 LO CUR
 Connection between isolated shield conductors
2. Reconfigure settings related to cable compensation to correspond to the cable
 compensation you performed, as follows: 
 Cable Compensation OptionDescriptionStandard Cable Compensation
 Set Cable Length to the NI standard option you
 chose.Custom Cable Compensation
 Set Cable Length to the custom option you used.
 Set LCR Short Custom Cable Compensation Enabled in the
 same manner it was set when you applied the custom cable compensation.
 If you selected Custom (As Configured) for Cable
 Length, call Configure LCR Custom Cable
 Compensation and provide the custom cable compensation
 data you generated for the present point in your program to
 it.
3. Set the additional properties that influence the generated load
 LCR compensation data. 
 In addition to the cable compensation,
 properties that affect the load LCR compensation data you
 generate with this process are as follows:Current
 Compensation FreqCurrent
 GBWCurrent Pole-Zero
 RatioLCR Current
 AmplitudeLCR Custom
 Measurement TimeLCR DC Bias
 Current LevelLCR DC Bias
 SourceLCR DC Bias
 Voltage LevelLCR Impedance
 RangeLCR Measurement
 TimeLCR Stimulus
 FunctionLCR Voltage
 AmplitudeSource
 DelayTransient
 ResponseVoltage
 Compensation FreqVoltage
 GBWVoltage Pole-Zero
 Ratio
4. Call Perform LCR Load Compensation and
 supply the load compensation spots you need for your
 DUT. 
 
 org.dita.html5/xsl/topic.xsl 455Note This function generates compensation data for only those
 compensation spots you specify. NI-DCPower does not
 interpolate compensation data for areas between these spots. 
 Calling this function writes the load data to the
 onboard storage of the instrument. Data from only the most
 recently performed load LCR compensation is recorded in
 onboard storage.org.dita.html5/xsl/topic.xsl 455Note When you call
 this function, most NI-DCPower properties in the session are
 reset to their default values.
  1. Provide a test
 frequency to compensate
 for.
  2. Choose a reference value
 type—a known specification of the
 reference load.
  3. Use reference value A
 and reference value B to
 supply the specification value. 
 Documentation for the reference
 value type you choose tells you how
 to use reference value A
 and reference value B for
 each value type.
  4. Repeat steps [4.a](#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__SUBSTEP_QLK_S3Y_WPB) through [4.c](#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__SUBSTEP_FWZ_CJY_WPB) for as many spots as desired, up to
 the maximum allowed.
5. Rewrite the values for any session properties that you need to maintain.
6. Based on how many discrete sets of compensation data your
 application requires, manage the compensation data. 
 Data RequiredDescriptionSingle set
 No action required: onboard storage of the
 instrument already contains the load
 data.Multiple sets
 Measure the complex
 impedance, Z, of the circuit
 with Measure Multiple LCR or
 Fetch Multiple LCR.
 Calculate the resistance
 and reactance from the complex impedance and keep
 track of the values.
 If relevant to your
 application, physically reorient your setup for
 the next compensation point.
 Repeat steps [2](#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__STEP_HTF_WYQ_WQB) through [6](#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__STEP_OQW_F1F_JQB) for each discrete set of load LCR
 compensation data your application requires for
 that particular reference load–DUT pair.
 If you also need to
 generate data for multiple reference load–DUT
 pairs, repeat steps
 [1](#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__STEP_THG_YGY_WPB) through [6](#GUID-99D9821D-90D5-405E-A259-2DB256115F5B__STEP_OQW_F1F_JQB).

You have now generated load LCR compensation data for
 your setup. The associated corrections are not yet applied to your
 measurements.

Once you have completed this process, return to *Compensating an NI
 LCR Meter* to continue any other parts of the overall compensation process you want
 to perform.

Parent topic:

Compensating an NI LCR Meter

Related tasks:

- Compensating an NI LCR Meter

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-generating-open-lcr-data.html language=enus -->
## TOPIC 00008: Generating Open LCR Compensation Data

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-generating-open-lcr-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-generating-open-lcr-data.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `task`
- source_description: Generating open LCR compensation data calculates corrections that you can then apply to your LCR measurements. Complete this process only in the context of the overall compensation process described in Compensating an NI LCR Meter. Before you begin, follow any instructions for preparing your cables

Generating Open LCR Compensation
 Data

Generating open LCR compensation data calculates corrections
 that you can then apply to your LCR measurements.

Note

Compensating an NI LCR Meter

Note

The cable compensation data you apply affects the LCR compensation data
 you generate with this process. Apply a standard cable compensation or apply custom cable
 compensation data before performing this process.

Notice

Complete the following steps to generate open LCR compensation
 data:

1. Leave the circuit open across the test fixture as shown. 
 Figure 3.Compensation: Open Setup. Four-terminal pair (4TP) connection scheme shown.
 
 
 
[IMAGE alt='1378' src='GUID-5A7AF4E2-EFE9-4A80-B0BF-DD3B35FA7367-a5.svg'] 

 HI CUR
 HI POT
 LO POT
 LO CUR
 Connection between isolated shield conductors
2. Reconfigure settings related to cable compensation to correspond to the cable
 compensation you performed, as follows: 
 Cable Compensation OptionDescriptionStandard Cable Compensation
 Set Cable Length to the NI standard option you
 chose.Custom Cable Compensation
 Set Cable Length to the custom option you used.
 Set LCR Short Custom Cable Compensation Enabled in the
 same manner it was set when you applied the custom cable compensation.
 If you selected Custom (As Configured) for Cable
 Length, call Configure LCR Custom Cable
 Compensation and provide the custom cable compensation
 data you generated for the present point in your program to
 it.
3. Call Perform LCR Open Compensation and supply any specific
 frequencies you want to compensate for. 
 This function generates compensation data based on a default set of test frequencies
 and the additional frequencies you can specify. NI-DCPower
 interpolates compensation for frequencies other than these frequencies. 
 Calling this function writes the open data to the onboard storage of the
 instrument. Data from only the most recently performed open LCR compensation is recorded
 in onboard storage.org.dita.html5/xsl/topic.xsl 455Note When you call this function, most NI-DCPower properties in the session are reset to their
 default values.
4. Rewrite the values for any session properties that you need to maintain.
5. Based on how many discrete sets of compensation data your application requires, manage
 the compensation data. 
 Data RequiredDescriptionSingle set
 No action required: onboard storage of the instrument already contains the open
 data.Multiple sets
 Measure the complex admittance, Y, of the
 circuit with Measure Multiple LCR or Fetch Multiple
 LCR.
 Calculate the conductance and susceptance from the complex
 admittance and keep track of the values.
 If relevant to your application, physically reorient your
 setup for the next compensation point.
 Repeat steps [2](#GUID-3D89AE25-9FB9-42D5-A3A2-2F8F81756C99__STEP_XR1_WXQ_WQB) through [5](#GUID-3D89AE25-9FB9-42D5-A3A2-2F8F81756C99__STEP_EX2_FT2_JQB) for each discrete set of open LCR compensation data your application
 requires.

You have now generated open LCR compensation data for your setup.
 The associated corrections are not yet applied to your measurements.

Once you have completed this process, return to *Compensating an NI
 LCR Meter* to continue any other parts of the overall compensation process you want
 to perform.

Parent topic:

Compensating an NI LCR Meter

Related tasks:

- Compensating an NI LCR Meter

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-generating-short-lcr-data.html language=enus -->
## TOPIC 00009: Generating Short LCR Compensation Data

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-generating-short-lcr-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-generating-short-lcr-data.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `task`
- source_description: Generating short LCR compensation data calculates corrections that you can then apply to your LCR measurements. Complete this process only in the context of the overall compensation process described in Compensating an NI LCR Meter. Before you begin, follow any instructions for preparing your cables

Generating Short LCR Compensation Data

Generating short LCR compensation data calculates
 corrections that you can then apply to your LCR measurements.

Note

Compensating an NI LCR Meter

Note

The cable compensation data you apply affects the LCR compensation data
 you generate with this process. Apply a standard cable compensation or apply custom cable
 compensation data before performing this process.

Notice

Complete the following steps to generate short LCR
 compensation data:

1. Configure a physical short across the test fixture as
 shown. 
 Figure 4.Compensation: Short Setup. Four-terminal pair (4TP) connection scheme shown.
 
 
 
[IMAGE alt='1378' src='GUID-237DDE93-0550-49DA-963E-061485A827D5-a5.svg'] 

 HI CUR
 HI POT
 LO POT
 LO CUR
 Connection between isolated shield conductors
2. Reconfigure settings related to cable compensation to correspond to the cable
 compensation you performed, as follows: 
 Cable Compensation OptionDescriptionStandard Cable Compensation
 Set Cable Length to the NI standard option you
 chose.Custom Cable Compensation
 Set Cable Length to the custom option you used.
 Set LCR Short Custom Cable Compensation Enabled in the
 same manner it was set when you applied the custom cable compensation.
 If you selected Custom (As Configured) for Cable
 Length, call Configure LCR Custom Cable
 Compensation and provide the custom cable compensation
 data you generated for the present point in your program to
 it.
3. Call Perform LCR Short Compensation and
 supply any specific frequencies you want to compensate
 for. 
 This function generates compensation data based on a default
 set of test frequencies and the additional frequencies you
 can specify. NI-DCPower
 interpolates compensation for frequencies other than these
 frequencies. 
 Calling this function writes the short data to the
 onboard storage of the instrument. Data from only the most
 recently performed short LCR compensation is recorded in
 onboard storage.org.dita.html5/xsl/topic.xsl 455Note When you call
 this function, most NI-DCPower properties in the session are
 reset to their default values.
4. Rewrite the values for any session properties that you need to
 maintain.
5. Based on how many discrete sets of compensation data your
 application requires, manage the compensation data. 
 Data RequiredDescriptionSingle set
 No action required: onboard storage of the
 instrument already contains the short
 data.Multiple sets
 Measure the complex
 impedance, Z, of the circuit
 with Measure Multiple LCR or
 Fetch Multiple LCR.
 Calculate the resistance
 and reactance from the complex impedance and keep
 track of the values.
 If relevant to your
 application, physically reorient your setup for
 the next compensation point.
 Repeat steps [2](#GUID-31C81272-8F15-4208-9734-7C2724EB32E7__STEP_HTF_WYQ_WQB) through [5](#GUID-31C81272-8F15-4208-9734-7C2724EB32E7__STEP_E5V_2Y2_JQB) for each discrete set of short LCR
 compensation data your application requires.

You have now generated short LCR compensation data
 for your setup. The associated corrections are not yet applied to your
 measurements.

Once you have completed this process, return to *Compensating an NI
 LCR Meter* to continue any other parts of the overall compensation process you want
 to perform.

Parent topic:

Compensating an NI LCR Meter

Related tasks:

- Compensating an NI LCR Meter

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-lcr-compensation-applying-multiple-sets.1.html language=enus -->
## TOPIC 00010: Applying Custom Cable Compensation: Multiple Data Sets

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-lcr-compensation-applying-multiple-sets.1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-lcr-compensation-applying-multiple-sets.1.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `task`
- source_description: Use this process to apply multiple sets of custom cable compensation corrections to your LCR measurements. Complete this process only in the context of the overall compensation process described in Compensating an NI LCR Meter. Set Cable Length to Custom (As Configured). Based on whether you generat

Applying Custom Cable Compensation: Multiple
 Data Sets

Use this process to apply multiple sets of custom cable compensation corrections to your
 LCR measurements.

Note

Compensating an NI LCR Meter

1. Set Cable Length to Custom (As
 Configured).
2. Based on whether you generated your own short custom cable compensation data or
 want to apply default data, set LCR Short Custom Cable Compensation
 Enabled as follows.
  - Generated short data:
 TRUE
  - Using default data:
 FALSE
3. For each discrete set of custom cable compensation
 data you generated with Get LCR Custom Cable
 Compensation Data, call Configure LCR Custom Cable
 Compensation at the point in your program that corresponds to the
 test conditions where the data set applies and supply the corresponding
 custom cable compensation data.

The compensation data you generated are now applied to your
 instrument.

Once you have completed this process, return to *Compensating an NI
 LCR Meter* to continue any other parts of the overall compensation process you want
 to perform.

Parent topic:

Compensating an NI LCR Meter

Related tasks:

- Compensating an NI LCR Meter

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-lcr-compensation-applying-multiple-sets.html language=enus -->
## TOPIC 00011: Applying LCR Compensation: Multiple Data Sets

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-lcr-compensation-applying-multiple-sets.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-lcr-compensation-applying-multiple-sets.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete this procedure to apply multiple sets of LCR compensation corrections to your measurements. Complete this process only in the context of the overall compensation process described in Compensating an NI LCR Meter. Your complete set of LCR compensation data may include any of open, short, and

Applying LCR Compensation: Multiple Data
 Sets

Complete this procedure to apply multiple sets of LCR compensation corrections to your
 measurements.

Note

Compensating an NI LCR Meter

Note

1. Set LCR Open/Short/Load Compensation Data Source to
 As Defined.
2. For each discrete set of LCR compensation data you generated, and for each type of LCR
 compensation, write the values you tracked to the relevant properties at the point in your
 program that corresponds to the test conditions where the data set applies. 
 LCR Compensation TypePropertiesOpen LCR compensation
 LCR Open Conductance
 LCR Open SusceptanceShort LCR compensation
 LCR Short Resistance
 LCR Short ReactanceLoad LCR compensation
 LCR Measured Load Resistance
 LCR Measured Load Reactance
 LCR Actual Load Resistance
 LCR Actual Load Reactance
3. For each type of LCR compensation for which you generated data, set the associated NI-DCPower property to TRUE. 
 
 Enabling each property allows NI-DCPower to apply
 the corrections based on the corresponding compensation to LCR measurements on the
 associated channel(s).
  - Open: LCR Open Compensation
 Enabled
  - Short: LCR Short Compensation
 Enabled
  - Load: LCR Load Compensation
 Enabled

The compensation data you generated are now applied to your
 LCR measurements.

Once you have completed this process, return to *Compensating an NI
 LCR Meter* to continue any other parts of the overall compensation process you want
 to perform.

Parent topic:

Compensating an NI LCR Meter

Related tasks:

- Compensating an NI LCR Meter

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-lcr-compensation-applying-single-set.html language=enus -->
## TOPIC 00012: Applying LCR Compensation: Single Data Set

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-lcr-compensation-applying-single-set.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-lcr-compensation-applying-single-set.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete this procedure to apply a single set of LCR compensation corrections to your measurements. Complete this process only in the context of the overall compensation process described in Compensating an NI LCR Meter. Your complete set of LCR compensation data may include any of open, short, and

Applying LCR Compensation: Single Data
 Set

Complete this procedure to apply a single set of LCR compensation corrections to your
 measurements.

Note

Compensating an NI LCR Meter

Note

1. Set LCR Open/Short/Load Compensation Data Source to
 Onboard Storage.
2. For each type of LCR compensation for which you generated data, set the associated NI-DCPower property to TRUE. 
 
 Enabling each property allows NI-DCPower to apply
 the corrections based on the corresponding compensation to LCR measurements on the
 associated channel(s).
  - Open: LCR Open Compensation Enabled
  - Short: LCR Short Compensation Enabled
  - Load: LCR Load Compensation Enabled

The compensation data you generated are now applied to your
 LCR measurements.

Once you have completed this process, return to *Compensating an NI
 LCR Meter* to continue any other parts of the overall compensation process you want
 to perform.

Parent topic:

Compensating an NI LCR Meter

Related tasks:

- Compensating an NI LCR Meter

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-lcr-determining-compensations.html language=enus -->
## TOPIC 00013: Determining Which Compensations to Perform

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-lcr-determining-compensations.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-lcr-determining-compensations.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `task`
- source_description: There are multiple options for performing both cable compensation and LCR compensation. The approach you should take depends on your test setup, as well as the tradeoff between the degree of accuracy you need for your application and the amount of effort needed to perform the compensations. Complete

Determining Which Compensations to
 Perform

There are multiple options for performing both cable compensation and LCR compensation.
 The approach you should take depends on your test setup, as well as the tradeoff
 between the degree of accuracy you need for your application and the amount of
 effort needed to perform the compensations.

Compensating an NI LCR Meter

NI recommends performing at least some form of
 compensation for the best accuracy, but you are not required to
 perform compensation before making LCR measurements.

Refer to the following to determine the types of
 compensations you may want to perform and, for the relevant types of
 compensation, how many sets of compensation data you may want to
 collect and apply.

1. Determine the cable compensation to perform using the following criteria. 
 org.dita.html5/xsl/topic.xsl 455Note NI recommends applying cable
 compensation for the best accuracy, particularly for
 low-level LCR measurements where the effects of
 cabling may be significant relative to the quantity
 you are measuring. 
 OptionRecommended WhenStandard cable compensation
 You are using a standard NI cable that is
 represented with a profile in the Cable
 Length property, and your test setup
 is simple—it excludes complex circuitry, like
 switches, that could affect LCR
 measurements.Custom cable compensation
 Your setup includes non–NI
 cabling.
 Your test setup is complex—it includes complex
 circuitry, like switches, that could affect LCR
 measurements.
2. Determine the LCR compensation to perform using the following criteria. 
 OptionRecommended WhenOpen LCR compensation
 Stray admittance in your test setup may
 influence LCR measurements; such stray admittance
 is present in most test setups.Short LCR compensation
 The impedance of your DUT is low (<100 Ω), so the
 residual impedance of cabling and fixtures may be
 a meaningful percentage of your DUT
 impedance.Load LCR compensation
 You know, or can determine, the value of a
 reference load that is similar to your DUT with a
 high degree of confidence, and:Your test setup is
 complex—it includes complex circuitry, like
 switches, that could affect LCR measurements.Open and short LCR
 compensation alone do not yield sufficient
 accuracy for your application.org.dita.html5/xsl/topic.xsl 455Note If you want to
 perform load LCR compensation, you must also
 perform open and short LCR
 compensation.
3. If you are performing custom cable compensation or any LCR
 compensation, determine how many sets of compensation data
 you may benefit from generating with the following
 criteria. 
 OptionRecommended ForSingle data set
 Simpler applications that involve a single
 test configuration or where a single set of data
 improves measurement accuracy enough for your
 purposes.Multiple data sets
 More complex applications that involve
 different measurement conditions and that require
 the best accuracy. Applications may include:Wafer testing, where you
 are testing and can compensate for multiple
 physical locations on the waferUsing switches, where you
 can compensate for different paths through the
 switchTesting different DUTs (on
 the basis of part number, rather than serial
 number) in the same runUsing different
 measurement parameters 
 org.dita.html5/xsl/topic.xsl 455Note If you generate multiple sets of
 compensation data, you should generate the same
 number of data sets for each discrete compensation
 type you perform. For example, if you have two
 different test points and want to perform custom
 cable compensation and all three types of LCR
 compensation, generate two sets each of custom cable
 compensation data, open LCR compensation data, short
 LCR compensation data, and load LCR compensation
 data.

Compensating an NI LCR Meter

Parent topic:

Compensating an NI LCR Meter

Related tasks:

- Compensating an NI LCR Meter

<!--NI_TOPIC bundle=ni-dcpower-compensating-lcr-measurements path=ni-dcpower-lcr-when-to-repeat-compensation.html language=enus -->
## TOPIC 00014: When to Use New Data for Custom Cable Compensation or LCR Compensation

- bundle_id: `ni-dcpower-compensating-lcr-measurements`
- source_path: `ni-dcpower-lcr-when-to-repeat-compensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-compensating-lcr-measurements/raw/resource/enus/ni-dcpower-lcr-when-to-repeat-compensation.html
- source_language: `enus`
- document_id: `ni-dcpower-compensating-lcr-measurements`
- page_type: `leaf`
- content_type: `concept`
- source_description: If certain elements of your test setup change and you performed custom cable compensation or any type of LCR compensation, the compensation data you generated will become outdated and less effective, so you should recalculate and reapply the compensation data. Generate and apply new custom cable com

When to Use New Data for Custom Cable
 Compensation or LCR Compensation

If certain elements of your test setup change and you performed custom cable
 compensation or any type of LCR compensation, the compensation data you generated will become
 outdated and less effective, so you should recalculate and reapply the compensation
 data.

Generate and apply new custom cable compensation data or LCR compensation data if any of the
 following occur.

- You perform a new external calibration
- You perform a new self-calibration
- You add complex circuit elements, such as a switch, between the
 end of the cable and the fixture containing your DUT
- You change the length of the cabling in your test setup
- You change the physical orientation of the cabling in your test
 setup
- You begin testing a DUT that is different (on the basis of part
 number) from the DUT for which you originally generated compensation data; for load
 LCR compensation, also choose a new reference load appropriate for the new DUT

Tip

Get LCR Compensation Last Date
 And Time

Note
