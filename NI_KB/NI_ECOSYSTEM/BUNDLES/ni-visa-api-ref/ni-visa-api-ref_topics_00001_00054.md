# NI DOCUMENT BUNDLE: ni-visa-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-visa-api-ref start=1 end=54 -->
<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_asrl_ri_state.html language=enus -->
## TOPIC 00001: VI_ATTR_ASRL_RI_STATE

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_asrl_ri_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_asrl_ri_state.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_ASRL_RI_STATE

#### Resource Classes

Serial INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteGlobal | ViInt16 | VI_STATE_ASSERTED (1)VI_STATE_UNASSERTED (0)VI_STATE_UNKNOWN (–1) | N/A |

#### Description

VI_ATTR_ASRL_RI_STATE represents the current state of the Ring Indicator (RI) input signal. The RI signal is often used by modems to indicate that the telephone line is ringing. This attribute is Read Only except when the VI_ATTR_ASRL_WIRE_MODE attribute is set to VI_ASRL_WIRE_232_DCE, or VI_ASRL_WIRE_232_AUTO with the hardware currently in the DCE state.

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_ASRL_CTS_STATE](vi_attr_asrl_cts_state.html)

[VI_ATTR_ASRL_DCD_STATE](vi_attr_asrl_dcd_state.html)

[VI_ATTR_ASRL_DSR_STATE](vi_attr_asrl_dsr_state.html)

[VI_ATTR_ASRL_DTR_STATE](vi_attr_asrl_dtr_state.html)

[VI_ATTR_ASRL_RTS_STATE](vi_attr_asrl_rts_state.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_asrl_rts_state.html language=enus -->
## TOPIC 00002: VI_ATTR_ASRL_RTS_STATE

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_asrl_rts_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_asrl_rts_state.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_ASRL_RTS_STATE

#### Resource Classes

Serial INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteGlobal | ViInt16 | VI_STATE_ASSERTED (1)VI_STATE_UNASSERTED (0)VI_STATE_UNKNOWN (–1) | N/A |

#### Description

VI_ATTR_ASRL_RTS_STATE is used to manually assert or unassert the Request To Send (RTS) output signal.

When the VI_ATTR_ASRL_FLOW_CNTRL attribute is set to VI_ASRL_FLOW_RTS_CTS, this attribute is Read Only. Querying the value will return VI_STATE_UNKNOWN.

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_ASRL_CTS_STATE](vi_attr_asrl_cts_state.html)

[VI_ATTR_ASRL_DCD_STATE](vi_attr_asrl_dcd_state.html)

[VI_ATTR_ASRL_DSR_STATE](vi_attr_asrl_dsr_state.html)

[VI_ATTR_ASRL_DTR_STATE](vi_attr_asrl_dtr_state.html)

[VI_ATTR_ASRL_RI_STATE](vi_attr_asrl_ri_state.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_asrl_wire_mode.html language=enus -->
## TOPIC 00003: VI_ATTR_ASRL_WIRE_MODE

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_asrl_wire_mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_asrl_wire_mode.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_ASRL_WIRE_MODE

#### Resource Classes

Serial INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteGlobal | ViInt16 | VI_ASRL_WIRE_485_4 (0)VI_ASRL_WIRE_485_2_DTR_ECHO (1)VI_ASRL_WIRE_485_2_DTR_CTRL (2)VI_ASRL_WIRE_485_2_AUTO (3)VI_ASRL_WIRE_232_DTE (128) VI_ASRL_WIRE_232_DCE (129) VI_ASRL_WIRE_232_AUTO (130)VI_STATE_UNKNOWN (–1) | N/A |

#### Description

VI_ATTR_ASRL_WIRE_MODE represents the current wire/transceiver mode.

For RS-485 hardware, this attribute is valid only with the RS-485 serial driver developed by National Instruments.

For RS-232 hardware, the values RS232/DCE and RS232/AUTO are valid only with RS-232 serial drivers developed by National Instruments and documented to support this feature with the corresponding National Instruments hardware. When this feature is not supported, RS232/DTE is the only valid value.

RS-232 settings:

- VI_ASRL_WIRE_232_DTE uses DTE mode.
- VI_ASRL_WIRE_232_DCE uses DCE mode.
- VI_ASRL_WIRE_232_AUTO automatically detects which mode to use.

(Windows) RS-485 settings:

- VI_ASRL_WIRE_485_4 uses 4-wire mode.
- VI_ASRL_WIRE_485_2_DTR_ECHO uses 2-wire DTR mode controlled with echo.
- VI_ASRL_WIRE_485_2_DTR_CTRL uses 2-wire DTR mode controlled without echo.
- VI_ASRL_WIRE_485_2_AUTO uses 2-wire auto mode controlled with TXRDY.

(Linux) RS-485 settings:

- VI_ASRL_WIRE_485_4 uses 4-wire mode.
- VI_ASRL_WIRE_485_2_AUTO uses 2-wire auto mode controlled with TXRDY.

|  | Note This attribute is valid only on the platforms on which National Instruments supports its RS-232 or RS-485 products. |
| --- | --- |

**Related Topics**

[INSTR Resource](instr_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_dest_byte_order.html language=enus -->
## TOPIC 00004: VI_ATTR_DEST_BYTE_ORDER

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_dest_byte_order.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_dest_byte_order.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_DEST_BYTE_ORDER

#### Resource Classes

VXI INSTR, VXI MEMACC

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteLocal | ViUInt16 | VI_BIG_ENDIAN (0)VI_LITTLE_ENDIAN (1) | VI_BIG_ENDIAN |

#### Description

VI_ATTR_DEST_BYTE_ORDER specifies the byte order to be used in high-level access operations, such as viOut*XX*() and viMoveOut*XX*(), when writing to the destination.

**Related Topics**

[INSTR Resource](instr_resource.html)

[MEMACC Resource](memacc_resource.html)

[VI_ATTR_DEST_ACCESS_PRIV](vi_attr_dest_access_priv.html)

[VI_ATTR_DEST_INCREMENT](vi_attr_dest_increment.html)

[VI_ATTR_SRC_BYTE_ORDER](vi_attr_src_byte_order.html)

[VI_ATTR_WIN_BYTE_ORDER](vi_attr_win_byte_order.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_dest_increment.html language=enus -->
## TOPIC 00005: VI_ATTR_DEST_INCREMENT

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_dest_increment.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_dest_increment.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_DEST_INCREMENT

#### Resource Classes

PXI INSTR, PXI MEMACC, VXI INSTR, VXI MEMACC

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteLocal | ViInt32 | 0 to 1 | 1 |

#### Description

VI_ATTR_DEST_INCREMENT is used in the viMoveOut*XX*() operations to specify by how many elements the destination offset is to be incremented after every transfer. The default value of this attribute is 1 (that is, the destination address will be incremented by 1 after each transfer), and the viMoveOut*XX*() operations move into consecutive elements. If this attribute is set to 0, the viMoveOut*XX*() operations will always write to the same element, essentially treating the destination as a FIFO register.

**Related Topics**

[INSTR Resource](instr_resource.html)

[MEMACC Resource](memacc_resource.html)

[VI_ATTR_DEST_ACCESS_PRIV](vi_attr_dest_access_priv.html)

[VI_ATTR_DEST_BYTE_ORDER](vi_attr_dest_byte_order.html)

[VI_ATTR_SRC_INCREMENT](vi_attr_src_increment.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_gpib_primary_addr.html language=enus -->
## TOPIC 00006: VI_ATTR_GPIB_PRIMARY_ADDR

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_gpib_primary_addr.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_gpib_primary_addr.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_GPIB_PRIMARY_ADDR

#### Resource Classes

GPIB INSTR, GPIB INTFC

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| INSTR, MEMACC, BACKPLANE:Read OnlyGlobal INTFC:Read/WriteGlobal | ViUInt16 | 0 to 30 | N/A |

#### Description

VI_ATTR_GPIB_PRIMARY_ADDR specifies the primary address of the GPIB device used by the given session. For the GPIB INTFC Resource, this attribute is Read-Write.

**Related Topics**

[BACKPLANE Resource](backplane_resource.html)

[INSTR Resource](instr_resource.html)

[INTFC Resource](intfc_resource.html)

[MEMACC Resource](memacc_resource.html)

[VI_ATTR_GPIB_SECONDARY_ADDR](vi_attr_gpib_secondary_addr.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_gpib_readdr_en.html language=enus -->
## TOPIC 00007: VI_ATTR_GPIB_READDR_EN

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_gpib_readdr_en.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_gpib_readdr_en.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_GPIB_READDR_EN

#### Resource Classes

GPIB INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteLocal | ViBoolean | VI_TRUE (1)VI_FALSE (0) | VI_TRUE |

#### Description

VI_ATTR_GPIB_READDR_EN specifies whether to use repeat addressing before each read or write operation.

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_GPIB_UNADDR_EN](vi_attr_gpib_unaddr_en.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_gpib_srq_state.html language=enus -->
## TOPIC 00008: VI_ATTR_GPIB_SRQ_STATE

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_gpib_srq_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_gpib_srq_state.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_GPIB_SRQ_STATE

#### Resource Classes

GPIB INTFC

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViInt16 | VI_STATE_ASSERTED(1)VI_STATE_UNASSERTED(0)VI_STATE_UNKNOWN(-1) | N/A |

#### Description

This attribute shows the current state of the GPIB SRQ (Service ReQuest) interface line.

**Related Topics**

[INTFC Resource](intfc_resource.html)

[VI_ATTR_GPIB_ATN_STATE](vi_attr_gpib_atn_state.html)

[VI_ATTR_GPIB_NDAC_STATE](vi_attr_gpib_ndac_state.html)

[VI_ATTR_GPIB_REN_STATE](vi_attr_gpib_ren_state.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_gpib_sys_cntrl_state.html language=enus -->
## TOPIC 00009: VI_ATTR_GPIB_SYS_CNTRL_STATE

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_gpib_sys_cntrl_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_gpib_sys_cntrl_state.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_GPIB_SYS_CNTRL_STATE

#### Resource Classes

GPIB INTFC

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteGlobal | ViBoolean | VI_TRUE(1)VI_FALSE(0) | N/A |

#### Description

This attribute shows whether the specified GPIB interface is currently the system controller. In some implementations, this attribute may be modified only through a configuration utility. On these systems this attribute is read-only (RO).

**Related Topics**

[INTFC Resource](intfc_resource.html)

[VI_ATTR_GPIB_CIC_STATE](vi_attr_gpib_cic_state.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_gpib_unaddr_en.html language=enus -->
## TOPIC 00010: VI_ATTR_GPIB_UNADDR_EN

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_gpib_unaddr_en.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_gpib_unaddr_en.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_GPIB_UNADDR_EN

#### Resource Classes

GPIB INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteLocal | ViBoolean | VI_TRUE (1)VI_FALSE (0) | VI_FALSE |

#### Description

VI_ATTR_GPIB_UNADDR_EN specifies whether to unaddress the device (UNT and UNL) after each read or write operation.

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_GPIB_READDR_EN](vi_attr_gpib_readdr_en.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_intr_status_id.html language=enus -->
## TOPIC 00011: VI_ATTR_INTR_STATUS_ID

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_intr_status_id.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_intr_status_id.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_INTR_STATUS_ID

#### Resource Classes

VI_EVENT_VXI_VME_INTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViUInt32 | 0 to FFFFFFFFh | N/A |

#### Description

VI_ATTR_INTR_STATUS_ID specifies the 32-bit status/ID retrieved during the IACK cycle.

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_EVENT_TYPE](vi_attr_event_type.html)

[VI_ATTR_RECV_INTR_LEVEL](vi_attr_recv_intr_level.html)

[VI_EVENT_VXI_VME_INTR](vi_event_vxi_vme_intr.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_io_prot.html language=enus -->
## TOPIC 00012: VI_ATTR_IO_PROT

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_io_prot.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_io_prot.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_IO_PROT

#### Resource Classes

GPIB INTFC, GPIB INSTR, Serial INSTR, TCPIP SOCKET, USB INSTR, USB RAW, VXI INSTR, VXI SERVANT

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteLocal | ViUInt16 | GPIB:VI_PROT_NORMAL (1)VI_PROT_HS488 (3) | VI_PROT_NORMAL |
|  |  | VXIVI_PROT_NORMAL (1)VI_PROT_FDC (2) | VI_PROT_NORMAL |
|  |  | Serial, TCPIP, USB RAW:VI_PROT_NORMAL (1)VI_PROT_4882_STRS (4) | VI_PROT_NORMAL |
|  |  | USB INSTR:VI_PROT_NORMAL (1)VI_PROT_USBTMC_VENDOR (5) | VI_PROT_NORMAL |

#### Description

VI_ATTR_IO_PROT specifies which protocol to use. In VXI, you can choose normal word serial or fast data channel (FDC). In GPIB, you can choose normal or high-speed (HS-488) transfers. In serial, TCPIP, or USB RAW, you can choose normal transfers or 488.2-defined strings. In USB INSTR, you can choose normal or vendor-specific transfers.

In previous versions of VISA, VI_PROT_NORMAL was known as VI_NORMAL, VI_PROT_FDC was known as VI_FDC, VI_PROT_HS488 was known as VI_HS488, and VI_PROT_4882_STRS was known as VI_ASRL488.

**Related Topics**

[INSTR Resource](instr_resource.html)

[INTFC Resource](intfc_resource.html)

[RAW Resource](raw_resource.html)

[SERVANT Resource](servant_resource.html)

[SOCKET Resource](socket_resource.html)

[VI_ATTR_FDC_CHNL](vi_attr_fdc_chnl.html)

[VI_ATTR_FDC_MODE](vi_attr_fdc_mode.html)

[VI_ATTR_FDC_USE_PAIR](vi_attr_fdc_use_pair.html)

[VI_ATTR_GPIB_HS488_CBL_LEN](vi_attr_gpib_hs488_cbl_len.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_mainframe_la.html language=enus -->
## TOPIC 00013: VI_ATTR_MA.infRAME_LA

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_mainframe_la.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_mainframe_la.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_MAINfRAME_LA

#### Resource Classes

VXI INSTR, VXI BACKPLANE

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViInt16 | 0 to 255VI_UNKNOWN_LA (–1) | N/A |

#### Description

VI_ATTR_MA.infRAME_LA specifies the lowest logical address in the mainframe. If the logical address is not known, VI_UNKNOWN_LA is returned.

**Related Topics**

[BACKPLANE Resource](backplane_resource.html)

[INSTR Resource](instr_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_max_queue_length.html language=enus -->
## TOPIC 00014: VI_ATTR_MAX_QUEUE_LENGTH

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_max_queue_length.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_max_queue_length.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_MAX_QUEUE_LENGTH

#### Resource Classes

All I/O session types

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteLocal | ViUInt32 | 1h to FFFFFFFFh | 50 |

#### Description

VI_ATTR_MAX_QUEUE_LENGTH specifies the maximum number of events that can be queued at any time on the given session. Events that occur after the queue has become full will be discarded.

VI_ATTR_MAX_QUEUE_LENGTH is a Read/Write attribute until the first time viEnableEvent() is called on a session. Thereafter, this attribute is Read Only.

**Related Topics**

[Operations](operations.html)

[viEnableEvent](vienableevent.html)

[VISA Resource Template](visa_resource_template.html)

[viWaitOnEvent](viwaitonevent.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_mem_base.html language=enus -->
## TOPIC 00015: VI_ATTR_MEM_BASE/VI_ATTR_MEM_BASE_32/VI_ATTR_MEM_BASE_64

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_mem_base.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_mem_base.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_MEM_BASE/VI_ATTR_MEM_BASE_32/VI_ATTR_MEM_BASE_64

#### Resource Classes

VXI INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | VI_ATTR_MEM_BASE: ViBusAddress VI_ATTR_MEM_BASE_32: ViUInt32 VI_ATTR_MEM_BASE_64: ViUInt64 | VI_ATTR_MEM_BASE: 0h to FFFFFFFFh for 32‑bit applications 0h to FFFFFFFFFFFFFFFFh for 64‑bit applications VI_ATTR_MEM_BASE_32: 0h to FFFFFFFFh VI_ATTR_MEM_BASE_64: 0h to FFFFFFFFFFFFFFFFh | N/A |

#### Description

VI_ATTR_MEM_BASE, VI_ATTR_MEM_BASE_32, and VI_ATTR_MEM_BASE_64 specify the base address of the device in VXIbus memory address space. This base address is applicable to A24 or A32 address space. If the value of VI_ATTR_MEM_SPACE is VI_A16_SPACE, the value of this attribute is meaningless for the given VXI device.

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_MEM_SIZE/VI_ATTR_MEM_SIZE_32/VI_ATTR_MEM_SIZE_64](vi_attr_mem_size.html)

[VI_ATTR_MEM_SPACE](vi_attr_mem_space.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_mem_size.html language=enus -->
## TOPIC 00016: VI_ATTR_MEM_SIZE/VI_ATTR_MEM_SIZE_32/VI_ATTR_MEM_SIZE_64

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_mem_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_mem_size.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_MEM_SIZE/VI_ATTR_MEM_SIZE_32/VI_ATTR_MEM_SIZE_64

#### Resource Classes

VXI INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | VI_ATTR_MEM_SIZE: ViBusSize VI_ATTR_MEM_SIZE_32: ViUInt32 VI_ATTR_MEM_SIZE_64: ViUInt64 | VI_ATTR_MEM_SIZE: 0h to FFFFFFFFh for 32‑bit applications 0h to FFFFFFFFFFFFFFFFh for 64‑bit applications VI_ATTR_MEM_SIZE_32: 0h to FFFFFFFFh VI_ATTR_MEM_SIZE_64: 0h to FFFFFFFFFFFFFFFFh | N/A |

#### Description

VI_ATTR_MEM_SIZE, VI_ATTR_MEM_SIZE_32, and VI_ATTR_MEM_SIZE_64 specify the size of memory requested by the device in VXIbus address space. If the value of VI_ATTR_MEM_SPACE is VI_A16_SPACE, the value of this attribute is meaningless for the given VXI device.

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_MEM_BASE/VI_ATTR_MEM_BASE_32/VI_ATTR_MEM_BASE_64](vi_attr_mem_base.html)

[VI_ATTR_MEM_SPACE](vi_attr_mem_space.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_mem_space.html language=enus -->
## TOPIC 00017: VI_ATTR_MEM_SPACE

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_mem_space.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_mem_space.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_MEM_SPACE

#### Resource Classes

VXI INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViUInt16 | VI_A16_SPACE (1)VI_A24_SPACE (2)VI_A32_SPACE (3) | VI_A16_SPACE |

#### Description

VI_ATTR_MEM_SPACE specifies the VXIbus address space used by the device. The three types are A16, A24, or A32 memory address space.

A VXI device with memory in A24 or A32 space also has registers accessible in the configuration section of A16 space. A VME device with memory in multiple address spaces requires one VISA resource for each address space used.

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_MEM_BASE/VI_ATTR_MEM_BASE_32/VI_ATTR_MEM_BASE_64](vi_attr_mem_base.html)

[VI_ATTR_MEM_SIZE/VI_ATTR_MEM_SIZE_32/VI_ATTR_MEM_SIZE_64](vi_attr_mem_size.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_model_code.html language=enus -->
## TOPIC 00018: VI_ATTR_MODEL_CODE

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_model_code.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_model_code.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_MODEL_CODE

#### Resource Classes

PXI INSTR, USB INSTR, USB RAW, VXI INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViUInt16 | 0h to FFFFh | N/A |

#### Description

VI_ATTR_MODEL_CODE specifies the model code for the device.

For VXI resources, this refers to the VXI Model Code.

For PXI INSTR resources, if the subsystem PCI Vendor ID is nonzero, this refers to the subsystem Device ID. Otherwise, this refers to the Device ID.

For USB resources, this refers to the Product ID (PID).

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_MANF_ID](vi_attr_manf_id.html)

[VI_ATTR_MODEL_NAME](vi_attr_model_name.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_model_name.html language=enus -->
## TOPIC 00019: VI_ATTR_MODEL_NAME

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_model_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_model_name.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_MODEL_NAME

#### Resource Classes

PXI INSTR, PXI BACKPLANE, USB INSTR, USB RAW, VXI INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViString | N/A | N/A |

#### Description

This string attribute is the model name of the device.

|  | Note The value of this attribute should be used for display purposes only and not for programmatic decisions, as the value can be different between VISA implementations and/or revisions. |
| --- | --- |

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_MANF_NAME](vi_attr_manf_name.html)

[VI_ATTR_MODEL_CODE](vi_attr_model_code.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_oper_name.html language=enus -->
## TOPIC 00020: VI_ATTR_OPER_NAME

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_oper_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_oper_name.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_OPER_NAME

#### Resource Classes

VI_EVENT_IO_COMPLETION, VI_EVENT_EXCEPTION

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read Only | ViString | N/A | N/A |

#### Description

VI_ATTR_OPER_NAME contains the name of the operation generating this event.

**Related Topics**

[VI_ATTR_EVENT_TYPE](vi_attr_event_type.html)

[VI_ATTR_STATUS](vi_attr_status.html)

[VI_EVENT_EXCEPTION](vi_event_exception.html)

[VI_EVENT_IO_COMPLETION](vi_event_io_completion.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_pxi_actual_lwidth.html language=enus -->
## TOPIC 00021: VI_ATTR_PXI_ACTUAL_LWIDTH

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_pxi_actual_lwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_pxi_actual_lwidth.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_PXI_ACTUAL_LWIDTH

#### Resource Classes

PXI INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read Only Global | ViInt16 | –1, 1, 2, 4, 8, 16 | N/A |

#### Description

VI_ATTR_PXI_ACTUAL_LWIDTH specifies the PCI Express link width negotiated between the PCI Express host controller and the device. A value of –1 indicates that the device is not a PXI/PCI Express device.

**Related Topics**

[INSTR Resource](instr_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_pxi_bus_num.html language=enus -->
## TOPIC 00022: VI_ATTR_PXI_BUS_NUM

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_pxi_bus_num.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_pxi_bus_num.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_PXI_BUS_NUM

#### Resource Classes

PXI INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read Only Global | ViUInt16 | 0 to 255 | N/A |

#### Description

VI_ATTR_PXI_BUS_NUM specifies the PCI bus number of this device.

**Related Topics**

[INSTR Resource](instr_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_pxi_chassis.html language=enus -->
## TOPIC 00023: VI_ATTR_PXI_CHASSIS

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_pxi_chassis.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_pxi_chassis.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_PXI_CHASSIS

#### Resource Classes

PXI INSTR, PXI BACKPLANE

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read Only Global | ViInt16 | -1, 0 to 255 | N/A |

#### Description

VI_ATTR_PXI_CHASSIS specifies the PXI chassis number of this device. A value of –1 means the chassis number is unknown.

**Related Topics**

[INSTR Resource](instr_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_pxi_dest_trig_bus.html language=enus -->
## TOPIC 00024: VI_ATTR_PXI_DEST_TRIG_BUS

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_pxi_dest_trig_bus.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_pxi_dest_trig_bus.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_PXI_DEST_TRIG_BUS

#### Resource Classes

PXI BACKPLANE

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/Write Local | ViInt16 | Single-Segment Chassis (8 Slots or Less):N/AMultisegment Chassis (More than 8 Slots):1...number of chassis segments* | –1 |

#### Description

VI_ATTR_PXI_DEST_TRIG_BUS specifies the segment to use to qualify trigDest in viMapTrigger.

|  | Note Some PXI chassis, typically those with more than 8 slots, have multiple trigger buses (also called segments). viMapTrigger is used on the PXI BACKPLANE resource to map a trigger between two trigger buses. One trigger bus, specified by VI_ATTR_PXI_SRC_TRIG_BUS, is the source or "writer" for this trigger line. The other trigger bus, specified by VI_ATTR_PXI_DEST_TRIG_BUS, is a "reader." You can have multiple readers, but only one writer for a given trigger line. For example, if you want to have triggers mapped from trigger bus 1 to trigger bus 2 and then from trigger bus 2 to trigger bus 3, observe that in this case trigger bus 1 is the writer for this line, writing to both trigger bus 2 and trigger bus 3. Therefore, you should perform your viMapTrigger from 1 to 2 and from 1 to 3—mapping from 1 to 2 and then 2 to 3 would not be allowed because it would require 2 also to be a writer (as well as 1). Note also that mapping from one line in the source trigger bus to a different line in the destination trigger bus (trigSrc != trigDest) is dependent on hardware capabilities and a specific software implementation, and may not be supported.Code to map trigger 5 from trigger segment 1 to trigger segment 2 of an 18-slot chassis would look like the following, where backplaneSession is a session to a PXI BACKPLANE resource: viSetAttribute(backplaneSession, VI_ATTR_PXI_SRC_TRIG_BUS, 1); viSetAttribute(backplaneSession, VI_ATTR_PXI_DEST_TRIG_BUS, 2); viMapTrigger(backplaneSession, VI_TRIG_TTL5, VI_TRIG_TTL5, VI_NULL); |
| --- | --- |

*You can determine the number of segments from MAX (in the trigger reservation panel), from the chassis documentation, and by looking at the dividing lines on the physical front panel of the chassis itself.

**Related Topics**

[BACKPLANE Resource](backplane_resource.html)

[VI_ATTR_PXI_SRC_TRIG_BUS](vi_attr_pxi_src_trig_bus.html)

[VI_ATTR_PXI_TRIG_BUS](vi_attr_pxi_trig_bus.html)

[viMapTrigger](vimaptrigger.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_pxi_dev_num.html language=enus -->
## TOPIC 00025: VI_ATTR_PXI_DEV_NUM

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_pxi_dev_num.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_pxi_dev_num.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_PXI_DEV_NUM

#### Resource Classes

PXI INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViUInt16 | 0 to 31 | N/A |

#### Description

This is the PXI device number.

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_PXI_FUNC_NUM](vi_attr_pxi_func_num.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_usb_intfc_num.html language=enus -->
## TOPIC 00026: VI_ATTR_USB_INTFC_NUM

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_usb_intfc_num.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_usb_intfc_num.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_USB_INTFC_NUM

#### Resource Classes

USB INSTR, USB RAW

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read Only Global | ViInt16 | 0 to FEh | 0 |

#### Description

VI_ATTR_USB_INTFC_NUM specifies the USB interface number used by the given session.

**Related Topics**

[INSTR Resource](instr_resource.html)

[RAW Resource](raw_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_usb_num_intfcs.html language=enus -->
## TOPIC 00027: VI_ATTR_USB_NUM_INTFCS

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_usb_num_intfcs.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_usb_num_intfcs.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_USB_NUM_INTFCS

#### Resource Classes

USB RAW

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read Only Global | ViInt16 | 1 to FFh | N/A |

#### Description

VI_ATTR_USB_NUM_INTFCS specifies the number of interfaces supported by this USB device.

**Related Topics**

[RAW Resource](raw_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_usb_num_pipes.html language=enus -->
## TOPIC 00028: VI_ATTR_USB_NUM_PIPES

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_usb_num_pipes.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_usb_num_pipes.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_USB_NUM_PIPES

#### Resource Classes

USB RAW

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read Only Global | ViInt16 | 0 to 30 | N/A |

#### Description

VI_ATTR_USB_NUM_PIPES specifies the number of pipes supported by this USB interface. This does not include the default control pipe.

**Related Topics**

[RAW Resource](raw_resource.html)

[VI_ATTR_USB_BULK_IN_PIPE](vi_attr_usb_bulk_in_pipe.html)

[VI_ATTR_USB_BULK_OUT_PIPE](vi_attr_usb_bulk_out_pipe.html)

[VI_ATTR_USB_INTR_IN_PIPE](vi_attr_usb_intr_in_pipe.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_usb_protocol.html language=enus -->
## TOPIC 00029: VI_ATTR_USB_PROTOCOL

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_usb_protocol.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_usb_protocol.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_USB_PROTOCOL

#### Resource Classes

USB INSTR, USB RAW

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read Only Global | ViInt16 | 0 to FFh | N/A |

#### Description

VI_ATTR_USB_PROTOCOL specifies the USB protocol used by this USB interface.

**Related Topics**

[INSTR Resource](instr_resource.html)

[RAW Resource](raw_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_usb_recv_intr_size.html language=enus -->
## TOPIC 00030: VI_ATTR_USB_RECV_INTR_SIZE

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_usb_recv_intr_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_usb_recv_intr_size.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_USB_RECV_INTR_SIZE

#### Resource Classes

VI_EVENT_USB_INTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read Only | ViUInt16 | N/A | N/A |

#### Description

VI_ATTR_USB_RECV_INTR_SIZE contains the number of bytes of USB interrupt data that is stored.

**Related Topics**

[VI_ATTR_USB_RECV_INTR_DATA](vi_attr_usb_recv_intr_data.html)

[VI_EVENT_USB_INTR](vi_event_usb_intr.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_vxi_dev_class.html language=enus -->
## TOPIC 00031: VI_ATTR_VXI_DEV_CLASS

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_vxi_dev_class.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_vxi_dev_class.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_VXI_DEV_CLASS

#### Resource Classes

VXI INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViUInt16 | VI_VXI_CLASS_MEMORY(0)VI_VXI_CLASS_EXTENDED(1)VI_VXI_CLASS_MESSAGE(2)VI_VXI_CLASS_REGISTER(3)VI_VXI_CLASS_OTHER(4) | N/A |

#### Description

This attribute represents the VXI-defined device class to which the resource belongs, either message based (VI_VXI_CLASS_MESSAGE), register based (VI_VXI_CLASS_REGISTER), extended (VI_VXI_CLASS_EXTENDED), or memory (VI_VXI_CLASS_MEMORY). VME devices are usually either register based or belong to a miscellaneous class (VI_VXI_CLASS_OTHER).

**Related Topics**

[INSTR Resource](instr_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_vxi_la.html language=enus -->
## TOPIC 00032: VI_ATTR_VXI_LA

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_vxi_la.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_vxi_la.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_VXI_LA

#### Resource Classes

VXI INSTR, VXI MEMACC, VXI SERVANT

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViInt16 | 0 to 511 | N/A |

#### Description

For an INSTR session, VI_ATTR_VXI_LA specifies the logical address of the VXI or VME device used by the given session. For a MEMACC or SERVANT session, this attribute specifies the logical address of the local controller.

**Related Topics**

[INSTR Resource](instr_resource.html)

[MEMACC Resource](memacc_resource.html)

[SERVANT Resource](servant_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_vxi_trig_dir.html language=enus -->
## TOPIC 00033: VI_ATTR_TRIG_DIR

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_vxi_trig_dir.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_vxi_trig_dir.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_TRIG_DIR

#### Resource Classes

VXI INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteGlobal | ViUInt16 | N/A | 0 |

#### Description

VI_ATTR_TRIG_DIR is a bit map of the directions of the mapped TTL trigger lines. Bits 0-7 represent TTL triggers 0-7 respectively. A bit's value of 0 means the line is routed out of the frame, and a value of 1 means into the frame. In order for a direction to be set, the line must also be enabled using VI_ATTR_VXI_TRIG_LINES_EN.

##### Related Topics

[INSTR Resource](instr_resource.html)

[VI_ATTR_VXI_TRIG_LINES_EN](vi_attr_vxi_trig_lines_en.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_vxi_trig_lines_en.html language=enus -->
## TOPIC 00034: VI_ATTR_VXI_TRIG_LINES_EN

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_vxi_trig_lines_en.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_vxi_trig_lines_en.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_VXI_TRIG_LINES_EN

#### Resource Classes

VXI INSTR

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteGlobal | ViUInt16 | N/A | 0 |

#### Description

VI_ATTR_VXI_TRIG_LINES_EN is a bit map of what VXI TLL triggers have mappings. Bits 0-7 represent TTL triggers 0-7 respectively. A bit's value of 0 means the trigger line is unmapped, and 1 means a mapping exists. Use VI_ATTR_VXI_TRIG_DIR to set an enabled line's direction.

##### Related Topics

[INSTR Resource](instr_resource.html)

[VI_ATTR_VXI_TRIG_DIR](vi_attr_vxi_trig_dir.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_vxi_trig_status.html language=enus -->
## TOPIC 00035: VI_ATTR_VXI_TRIG_STATUS

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_vxi_trig_status.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_vxi_trig_status.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_VXI_TRIG_STATUS

#### Resource Classes

VXI BACKPLANE

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViUInt32 | N/A | N/A |

#### Description

This attribute shows the current state of the VXI trigger lines. This is a bit vector with bits 0-9 corresponding to VI_TRIG_TTL0 through VI_TRIG_ECL1.

**Related Topics**

[BACKPLANE Resource](backplane_resource.html)

[VI_ATTR_VXI_TRIG_SUPPORT](vi_attr_vxi_trig_support.html)

[VI_ATTR_VXI_VME_INTR_STATUS](vi_attr_vxi_vme_intr_status.html)

[VI_ATTR_VXI_VME_SYSFAIL_STATE](vi_attr_vxi_vme_sysfail_state.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_vxi_trig_support.html language=enus -->
## TOPIC 00036: VI_ATTR_VXI_TRIG_SUPPORT

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_vxi_trig_support.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_vxi_trig_support.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_VXI_TRIG_SUPPORT

#### Resource Classes

VXI INSTR, VXI BACKPLANE

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViUInt32 | N/A | N/A |

#### Description

This attribute shows which VXI trigger lines this implementation supports. This is a bit vector with bits 0-9 corresponding to VI_TRIG_TTL0 through VI_TRIG_ECL1.

**Related Topics**

[BACKPLANE Resource](backplane_resource.html)

[INSTR Resource](instr_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_vxi_vme_intr_status.html language=enus -->
## TOPIC 00037: VI_ATTR_VXI_VME_INTR_STATUS

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_vxi_vme_intr_status.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_vxi_vme_intr_status.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_VXI_VME_INTR_STATUS

#### Resource Classes

VXI BACKPLANE

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViUInt16 | N/A | N/A |

#### Description

This attribute shows the current state of the VXI/VME interrupt lines. This is a bit vector with bits 0-6 corresponding to interrupt lines 1-7.

**Related Topics**

[BACKPLANE Resource](backplane_resource.html)

[VI_ATTR_VXI_TRIG_STATUS](vi_attr_vxi_trig_status.html)

[VI_ATTR_VXI_VME_SYSFAIL_STATE](vi_attr_vxi_vme_sysfail_state.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_vxi_vme_sysfail_state.html language=enus -->
## TOPIC 00038: VI_ATTR_VXI_VME_SYSFAIL_STATE

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_vxi_vme_sysfail_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_vxi_vme_sysfail_state.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_VXI_VME_SYSFAIL_STATE

#### Resource Classes

VXI BACKPLANE

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyGlobal | ViInt16 | VI_STATE_ASSERTED(1)VI_STATE_DEASSERTED(0)VI_STATE_UNKNOWN(–1) | N/A |

#### Description

This attribute shows the current state of the VXI/VME SYSFAIL (SYStem FAILure) backplane line.

**Related Topics**

[BACKPLANE Resource](backplane_resource.html)

[VI_ATTR_VXI_TRIG_STATUS](vi_attr_vxi_trig_status.html)

[VI_ATTR_VXI_VME_INTR_STATUS](vi_attr_vxi_vme_intr_status.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_win_access.html language=enus -->
## TOPIC 00039: VI_ATTR_WIN_ACCESS

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_win_access.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_win_access.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_WIN_ACCESS

#### Resource Classes

PXI INSTR, PXI MEMACC, VXI INSTR, VXI MEMACC

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyLocal | ViUInt16 | VI_NMAPPED (1)VI_USE_OPERS (2)VI_DEREF_ADDR (3) | VI_NMAPPED |

#### Description

VI_ATTR_WIN_ACCESS specifies the modes in which the current window may be accessed.

- If VI_NMAPPED , the window is not currently mapped.
- If VI_USE_OPERS , the window is accessible through the viPeek XX () and viPoke XX () operations only.
- If VI_DEREF_ADDR , you can either use operations or directly dereference the mapped address as a pointer.

**Related Topics**

[INSTR Resource](instr_resource.html)

[MEMACC Resource](memacc_resource.html)

[VI_ATTR_WIN_ACCESS_PRIV](vi_attr_win_access_priv.html)

[VI_ATTR_WIN_BASE_ADDR/VI_ATTR_WIN_BASE_ADDR_32/VI_ATTR_WIN_BASE_ADDR_64](vi_attr_win_base_addr.html)

[VI_ATTR_WIN_BYTE_ORDER](vi_attr_win_byte_order.html)

[VI_ATTR_WIN_SIZE/VI_ATTR_WIN_SIZE_32/VI_ATTR_WIN_SIZE_64](vi_attr_win_size.html)

[viMapAddress/viMapAddressEx](vimapaddress.html)

[viPeek8/viPeek16/viPeek32/viPeek64](vipeek8_vipeek16_vipeek32.html)

[viPoke8/viPoke16/viPoke32/viPoke64](vipoke8_vipoke16_vipoke32.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_win_access_priv.html language=enus -->
## TOPIC 00040: VI_ATTR_WIN_ACCESS_PRIV

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_win_access_priv.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_win_access_priv.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_WIN_ACCESS_PRIV

#### Resource Classes

VXI INSTR, VXI MEMACC

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteLocal | ViUInt16 | VI_DATA_PRIV (0)VI_DATA_NPRIV (1)VI_PROG_PRIV (2)VI_PROG_NPRIV (3)VI_BLCK_PRIV (4)VI_BLCK_NPRIV (5) | VI_DATA_PRIV |

#### Description

VI_ATTR_WIN_ACCESS_PRIV specifies the address modifier to be used in low-level access operations, such as viMapAddress(), viPeek*XX*(), and viPoke*XX*(), when accessing the mapped window.

This attribute is Read/Write when the corresponding session is not mapped (that is, when VI_ATTR_WIN_ACCESS is VI_NMAPPED. When the session is mapped, this attribute is Read Only.

**Related Topics**

[INSTR Resource](instr_resource.html)

[MEMACC Resource](memacc_resource.html)

[VI_ATTR_DEST_ACCESS_PRIV](vi_attr_dest_access_priv.html)

[VI_ATTR_SRC_ACCESS_PRIV](vi_attr_src_access_priv.html)

[VI_ATTR_WIN_ACCESS](vi_attr_win_access.html)

[VI_ATTR_WIN_BASE_ADDR/VI_ATTR_WIN_BASE_ADDR_32/VI_ATTR_WIN_BASE_ADDR_64](vi_attr_win_base_addr.html)

[VI_ATTR_WIN_BYTE_ORDER](vi_attr_win_byte_order.html)

[VI_ATTR_WIN_SIZE/VI_ATTR_WIN_SIZE_32/VI_ATTR_WIN_SIZE_64](vi_attr_win_size.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_win_base_addr.html language=enus -->
## TOPIC 00041: VI_ATTR_WIN_BASE_ADDR/VI_ATTR_WIN_BASE_ADDR_32/VI_ATTR_WIN_BASE_ADDR_64

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_win_base_addr.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_win_base_addr.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_WIN_BASE_ADDR/VI_ATTR_WIN_BASE_ADDR_32/VI_ATTR_WIN_BASE_ADDR_64

#### Resource Classes

PXI INSTR, PXI MEMACC, VXI INSTR, VXI MEMACC

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyLocal | VI_ATTR_WIN_BASE_ADDR: ViBusAddress VI_ATTR_WIN_BASE_ADDR_32: ViUInt32 VI_ATTR_WIN_BASE_ADDR_64: ViUInt64 | VI_ATTR_WIN_BASE_ADDR: 0h to FFFFFFFFh for 32‑bit applications 0h to FFFFFFFFFFFFFFFFh for 64‑bit applications VI_ATTR_WIN_BASE_ADDR_32: 0h to FFFFFFFFh VI_ATTR_WIN_BASE_ADDR_64: 0h to FFFFFFFFFFFFFFFFh | N/A |

#### Description

VI_ATTR_WIN_BASE_ADDR, VI_ATTR_WIN_BASE_ADDR_32, and VI_ATTR_WIN_BASE_ADDR_64 specify the base address of the interface bus to which this window is mapped. If the value of VI_ATTR_WIN_ACCESS is VI_NMAPPED, the value of this attribute is undefined.

**Related Topics**

[INSTR Resource](instr_resource.html)

[MEMACC Resource](memacc_resource.html)

[VI_ATTR_WIN_ACCESS](vi_attr_win_access.html)

[VI_ATTR_WIN_ACCESS_PRIV](vi_attr_win_access_priv.html)

[VI_ATTR_WIN_BYTE_ORDER](vi_attr_win_byte_order.html)

[VI_ATTR_WIN_SIZE/VI_ATTR_WIN_SIZE_32/VI_ATTR_WIN_SIZE_64](vi_attr_win_size.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_win_byte_order.html language=enus -->
## TOPIC 00042: VI_ATTR_WIN_BYTE_ORDER

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_win_byte_order.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_win_byte_order.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_WIN_BYTE_ORDER

#### Resource Classes

VXI INSTR, VXI MEMACC

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read/WriteLocal | ViUInt16 | VI_BIG_ENDIAN (0)VI_LITTLE_ENDIAN (1) | VI_BIG_ENDIAN |

#### Description

VI_ATTR_WIN_BYTE_ORDER specifies the byte order to be used in low-level access operations, such as viMapAddress(), viPeek*XX*(), and viPoke*XX*(), when accessing the mapped window.

This attribute is Read/Write when the corresponding session is not mapped (that is, when VI_ATTR_WIN_ACCESS is VI_NMAPPED. When the session is mapped, this attribute is Read Only.

**Related Topics**

[INSTR Resource](instr_resource.html)

[MEMACC Resource](memacc_resource.html)

[VI_ATTR_DEST_BYTE_ORDER](vi_attr_dest_byte_order.html)

[VI_ATTR_SRC_BYTE_ORDER](vi_attr_src_byte_order.html)

[VI_ATTR_WIN_ACCESS](vi_attr_win_access.html)

[VI_ATTR_WIN_ACCESS_PRIV](vi_attr_win_access_priv.html)

[VI_ATTR_WIN_BASE_ADDR/VI_ATTR_WIN_BASE_ADDR_32/VI_ATTR_WIN_BASE_ADDR_64](vi_attr_win_base_addr.html)

[VI_ATTR_WIN_SIZE/VI_ATTR_WIN_SIZE_32/VI_ATTR_WIN_SIZE_64](vi_attr_win_size.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_attr_wr_buf_size.html language=enus -->
## TOPIC 00043: VI_ATTR_WR_BUF_SIZE

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_attr_wr_buf_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_attr_wr_buf_size.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_ATTR_WR_BUF_SIZE

#### Resource Classes

GPIB INSTR, GPIB INTFC, Serial INSTR, TCPIP INSTR, TCPIP SOCKET, USB INSTR, USB RAW, VXI INSTR, VXI SERVANT

#### Attribute Information

| Access Privilege | Data Type | Range | Default |
| --- | --- | --- | --- |
| Read OnlyLocal | ViUInt32 | N/A | N/A |

#### Description

This is the current size of the formatted I/O output buffer for this session. The user can modify this value by calling viSetBuf().

**Related Topics**

[VI_ATTR_RD_BUF_SIZE](vi_attr_rd_buf_size.html)

[VI_ATTR_WR_BUF_OPER_MODE](vi_attr_wr_buf_oper_mode.html)

[viSetBuf](visetbuf.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_event_asrl_char.html language=enus -->
## TOPIC 00044: VI_EVENT_ASRL_CHAR

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_event_asrl_char.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_event_asrl_char.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_EVENT_ASRL_CHAR

|  | Note This event is supported for all serial ports on Windows and LabVIEW RT, and ENET-Serial on all platforms. Except for ENET-Serial, it is not supported for serial ports on Mac. |
| --- | --- |

#### Resource Classes

Serial INSTR

#### Description

Notification that at least one data byte has been received. Each data character will not necessarily result in an event notification. In other words, if multiple data bytes arrive at once, you may get only one event. After receiving this event, you should query the serial port for the number of bytes available via the VI_ATTR_ASRL_AVAIL_NUM attribute.

#### Event Attributes

| Symbolic Name | Description |
| --- | --- |
| VI_ATTR_EVENT_TYPE | Unique logical identifier of the event. |

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_ASRL_AVAIL_NUM](vi_attr_asrl_avail_num.html)

[VI_ATTR_EVENT_TYPE](vi_attr_event_type.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_event_asrl_dcd.html language=enus -->
## TOPIC 00045: VI_EVENT_ASRL_DCD

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_event_asrl_dcd.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_event_asrl_dcd.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_EVENT_ASRL_DCD

|  | Note This event is supported for all serial ports on Windows and LabVIEW RT, and ENET-Serial on all platforms. Except for ENET-Serial, it is not supported for serial ports on Mac. |
| --- | --- |

#### Resource Classes

Serial INSTR

#### Description

Notification that the Data Carrier Detect (DCD) line changed state. If the DCD line changes state quickly several times in succession, not all line state changes will necessarily result in event notifications.

#### Event Attributes

| Symbolic Name | Description |
| --- | --- |
| VI_ATTR_EVENT_TYPE | Unique logical identifier of the event. |

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_ASRL_DCD_STATE](vi_attr_asrl_dcd_state.html)

[VI_ATTR_EVENT_TYPE](vi_attr_event_type.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_event_asrl_dsr.html language=enus -->
## TOPIC 00046: VI_EVENT_ASRL_DSR

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_event_asrl_dsr.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_event_asrl_dsr.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_EVENT_ASRL_DSR

|  | Note This event is supported for all serial ports on Windows and LabVIEW RT, and ENET-Serial on all platforms. Except for ENET-Serial, it is not supported for serial ports on Mac. |
| --- | --- |

#### Resource Classes

Serial INSTR

#### Description

Notification that the Data Set Ready (DSR) line changed state. If the DSR line changes state quickly several times in succession, not all line state changes will necessarily result in event notifications.

#### Event Attributes

| Symbolic Name | Description |
| --- | --- |
| VI_ATTR_EVENT_TYPE | Unique logical identifier of the event. |

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_ASRL_DSR_STATE](vi_attr_asrl_dsr_state.html)

[VI_ATTR_EVENT_TYPE](vi_attr_event_type.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_event_asrl_ri.html language=enus -->
## TOPIC 00047: VI_EVENT_ASRL_RI

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_event_asrl_ri.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_event_asrl_ri.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_EVENT_ASRL_RI

|  | Note This event is supported for all serial ports on Windows and LabVIEW RT, and ENET-Serial on all platforms. Except for ENET-Serial, it is not supported for serial ports on Mac. |
| --- | --- |

#### Resource Classes

Serial INSTR

#### Description

Notification that the Ring Indicator (RI) signal level was asserted.

#### Event Attributes

| Symbolic Name | Description |
| --- | --- |
| VI_ATTR_EVENT_TYPE | Unique logical identifier of the event. |

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_ASRL_RI_STATE](vi_attr_asrl_ri_state.html)

[VI_ATTR_EVENT_TYPE](vi_attr_event_type.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_event_gpib_cic.html language=enus -->
## TOPIC 00048: VI_EVENT_GPIB_CIC

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_event_gpib_cic.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_event_gpib_cic.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_EVENT_GPIB_CIC

#### Resource Classes

GPIB INTFC

#### Description

Notification that the GPIB controller has gained or lost CIC (controller in charge) status.

#### Event Attributes

| Symbolic Name | Description |
| --- | --- |
| VI_ATTR_EVENT_TYPE | Unique logical identifier of the event. |
| VI_ATTR_GPIB_RECV_CIC_STATE | Specifies whether the CIC status was gained or lost. |

**Related Topics**

[INTFC Resource](intfc_resource.html)

[VI_ATTR_EVENT_TYPE](vi_attr_event_type.html)

[VI_ATTR_GPIB_RECV_CIC_STATE](vi_attr_gpib_recv_cic_state.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_event_pxi_intr.html language=enus -->
## TOPIC 00049: VI_EVENT_PXI_INTR

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_event_pxi_intr.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_event_pxi_intr.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_EVENT_PXI_INTR

#### Resource Classes

PXI INSTR

#### Description

This event notifies that a PXI interrupt has occurred.

#### Event Attributes

| Symbolic Name | Description |
| --- | --- |
| VI_ATTR_EVENT_TYPE | Unique logical identifier of the event. |
| VI_ATTR_PXI_RECV_INTR_SEQ | The index of the interrupt sequence that detected the interrupt condition. |
| VI_ATTR_PXI_RECV_INTR_DATA | The first PXI/PCI register that was read in the successful interrupt detection sequence. |

**Related Topics**

[INSTR Resource](instr_resource.html)

[VI_ATTR_EVENT_TYPE](vi_attr_event_type.html)

[VI_ATTR_PXI_RECV_INTR_DATA](vi_attr_pxi_recv_intr_data.html)

[VI_ATTR_PXI_RECV_INTR_SEQ](vi_attr_pxi_recv_intr_seq.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_event_usb_intr.html language=enus -->
## TOPIC 00050: VI_EVENT_USB_INTR

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_event_usb_intr.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_event_usb_intr.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_EVENT_USB_INTR

#### Resource Classes

USB INSTR, USB RAW

#### Description

This event notifies that a USB interrupt has occurred.

#### Event Attributes

| Symbolic Name | Description |
| --- | --- |
| VI_ATTR_EVENT_TYPE | Unique logical identifier of the event. |
| VI_ATTR STATUS | Contains the status code returned by this event. |
| VI_ATTR_USB_RECV_INTR_SIZE | The number of bytes of USB interrupt data that is stored. |
| VI_ATTR_USB_RECV_INTR_DATA | The actual received data from the USB Interrupt. |

**Related Topics**

[INSTR Resource](instr_resource.html)

[RAW Resource](raw_resource.html)

[VI_ATTR_EVENT_TYPE](vi_attr_event_type.html)

[VI_ATTR_STATUS](vi_attr_status.html)

[VI_ATTR_USB_RECV_INTR_DATA](vi_attr_usb_recv_intr_data.html)

[VI_ATTR_USB_RECV_INTR_SIZE](vi_attr_usb_recv_intr_size.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vi_event_vxi_vme_sysreset.html language=enus -->
## TOPIC 00051: VI_EVENT_VXI_VME_SYSRESET

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vi_event_vxi_vme_sysreset.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vi_event_vxi_vme_sysreset.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

VI_EVENT_VXI_VME_SYSRESET

#### Resource Classes

VXI BACKPLANE, VXI SERVANT

#### Description

Notification that the VXI/VME SYSRESET* line has been asserted.

#### Event Attributes

| Symbolic Name | Description |
| --- | --- |
| VI_ATTR_EVENT_TYPE | Unique logical identifier of the event |

**Related Topics**

[BACKPLANE Resource](backplane_resource.html)

[SERVANT Resource](servant_resource.html)

[VI_ATTR_EVENT_TYPE](vi_attr_event_type.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vigpibcommand.html language=enus -->
## TOPIC 00052: viGpibCommand

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vigpibcommand.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vigpibcommand.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

viGpibCommand

#### Purpose

Write GPIB command bytes on the bus.

#### C Syntax

ViStatus viGpibCommand (ViSession **vi**, ViBuf **buf**, ViUInt32 **count**, ViPUInt32 **retCount**)

#### Visual Basic Syntax

viGpibCommand&(ByVal **vi**&, ByVal **buf**$, ByVal **count**&, **retCount**&)

#### Resource Classes

GPIB INTFC

#### Parameters

| Name | Direction | Description |
| --- | --- | --- |
| vi | IN | Unique logical identifier to a session. |
| buf | IN | Buffer containing valid GPIB commands. |
| count | IN | Number of bytes to be written. |
| retCount | OUT | Number of bytes actually transferred. |

#### Return Values

| Completion Codes | Description |
| --- | --- |
| VI_SUCCESS | Operation completed successfully. |

| Error Codes | Description |
| --- | --- |
| VI_ERROR_INV_OBJECT | The given session reference is invalid. |
| VI_ERROR_NSUP_OPER | The given vi does not support this operation. |
| VI_ERROR_RSRC_LOCKED | Specified operation could not be performed because the resource identified by vi has been locked for this kind of access. |
| VI_ERROR_TMO | Timeout expired before operation completed. |
| VI_ERROR_INV_SETUP | Unable to start write operation because setup is invalid (due to attributes being set to an inconsistent state). |
| VI_ERROR_NCIC | The interface associated with the given vi is not currently the controller in charge. |
| VI_ERROR_NLISTENERS | No Listeners condition is detected (both NRFD and NDAC are deasserted). |
| VI_ERROR_IO | An unknown I/O error occurred during transfer. |

#### Description

This operation attempts to write **count** number of bytes of GPIB commands to the interface bus specified by **vi**. This operation is valid only on GPIB INTFC (interface) sessions. This operation returns only when the transfer terminates.

If you pass VI_NULL as the **retCount** parameter to the viGpibCommand() operation, the number of bytes transferred will not be returned. This may be useful if it is important to know only whether the operation succeeded or failed. The command bytes contained in **buf** should be valid IEEE 488-defined Multiline Interface Messages.

|  | Note The retCount parameter always is valid on both success and error. |
| --- | --- |

**Related Topics**

[INTFC Resource](intfc_resource.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vigpibcontrolren.html language=enus -->
## TOPIC 00053: viGpibControlREN

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vigpibcontrolren.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vigpibcontrolren.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

viGpibControlREN

#### Purpose

Controls the state of the GPIB Remote Enable (REN) interface line, and optionally the remote/local state of the device.

#### C Syntax

ViStatus viGpibControlREN(ViSession **vi**, ViUInt16 **mode**)

#### Visual Basic Syntax

viGpibControlREN&(ByVal **vi**&, ByVal **mode**%)

#### Resource Classes

GPIB INSTR, GPIB INTFC, USB INSTR

#### Parameters

| Name | Direction | Description |
| --- | --- | --- |
| vi | IN | Unique logical identifier to a session. |
| mode | IN | Specifies the state of the REN line and optionally the device remote/local state. See the Description section for actual values. |

#### Return Values

| Completion Codes | Description |
| --- | --- |
| VI_SUCCESS | Operation completed successfully. |

| Error Codes | Description |
| --- | --- |
| VI_ERROR_INV_OBJECT | The given session reference is invalid. |
| VI_ERROR_NSUP_OPER | The given vi does not support this operation. |
| VI_ERROR_RSRC_LOCKED | Specified operation could not be performed because the resource identified by vi has been locked for this kind of access. |
| VI_ERROR_NCIC | The interface associated with this session is not currently the controller in charge. |
| VI_ERROR_NLISTENERS | No-listeners condition is detected (both NRFD and NDAC are unasserted). |
| VI_ERROR_NSYS_CNTLR | The interface associated with this session is not the system controller. |
| VI_ERROR_INV_MODE | The value specified by the mode parameter is invalid. |

#### Description

The viGpibControlREN() operation asserts or unasserts the GPIB REN interface line according to the specified mode. The mode can also specify whether the device associated with this session should be placed in local state (before deasserting REN) or remote state (after asserting REN). This operation is valid only if the GPIB interface associated with the session specified by **vi** is currently the system controller.

The following table lists special values for the **mode** parameter.

| Value | Description |
| --- | --- |
| VI_GPIB_REN_DEASSERT | Deassert REN line. |
| VI_GPIB_REN_ASSERT | Assert REN line. |
| VI_GPIB_REN_DEASSERT_GTL | Send the Go To Local (GTL) command and deassert REN line. |
| VI_GPIB_REN_ASSERT_ADDRESS | Assert REN line and address device. |
| VI_GPIB_REN_ASSERT_LLO | Send LLO to any devices that are addressed to listen. |
| VI_GPIB_REN_ASSERT_ADDRESS_LLO | Address this device and send it LLO, putting it in RWLS. |
| VI_GPIB_REN_ASSERT_GTL | Send the Go To Local command (GTL) to this device. |

**Related Topics**

[INSTR Resource](instr_resource.html)

[INTFC Resource](intfc_resource.html)

[viGpibControlATN](vigpibcontrolatn.html)

<!--NI_TOPIC bundle=ni-visa-api-ref path=ni-visa-api-ref/vigpibpasscontrol.html language=enus -->
## TOPIC 00054: viGpibPassControl

- bundle_id: `ni-visa-api-ref`
- source_path: `ni-visa-api-ref/vigpibpasscontrol.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-api-ref/raw/resource/enus/ni-visa-api-ref/vigpibpasscontrol.html
- document_id: `ni-visa-api-ref`
- page_type: `leaf`
- content_type: ``

viGpibPassControl

#### Purpose

Tell the GPIB device at the specified address to become controller in charge (CIC).

#### C Syntax

ViStatus viGpibPassControl(ViSession **vi**, ViUInt16 **primAddr**, ViUInt16 **secAddr**)

#### Visual Basic Syntax

viGPIBPassControl& (ByVal **vi**&, ByVal **primAddr**%, ByValsec **Addr**%)

#### Resource Classes

GPIB INTFC

#### Parameters

| Name | Direction | Description |
| --- | --- | --- |
| vi | IN | Unique logical identifier to a session. |
| primAddr | IN | Primary address of the GPIB device to which you want to pass control. |
| secAddr | IN | Secondary address of the targeted GPIB device. If the targeted device does not have a secondary address, this parameter should contain the value VI_NO_SEC_ADDR. |

#### Return Values

| Completion Codes | Description |
| --- | --- |
| VI_SUCCESS | Operation completed successfully. |

| Error Codes | Description |
| --- | --- |
| VI_ERROR_INV_OBJECT | The given session reference is invalid. |
| VI_ERROR_NSUP_OPER | The given vi does not support this operation. |
| VI_ERROR_RSRC_LOCKED | Specified operation could not be performed because the resource identified by vi has been locked for this kind of access. |
| VI_ERROR_TMO | Timeout expired before operation completed. |
| VI_ERROR_NCIC | The interface associated with the given vi is not currently the controller in charge. |
| VI_ERROR_NLISTENERS | No Listeners condition is detected (both NRFD and NDAC are deasserted). |
| VI_ERROR_IO | An unknown I/O error occurred during transfer. |
| VI_ERROR_INV_PARAMETER | The primary or secondary address is invalid. |

#### Description

This operation passes controller in charge status to the device indicated by **primAddr** and **secAddr**, and then deasserts the ATN line. This operation assumes that the targeted device has controller capability. This operation is valid only on GPIB INTFC (interface) sessions.

**Related Topics**

[INTFC Resource](intfc_resource.html)
