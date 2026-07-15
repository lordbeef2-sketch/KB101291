# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa.proto sha256=7256f08be96643451ff01d4ee1298f3157985d28c08006033a84eea873d4a0fa bytes=34852 -->
## FILE: generated/visa/visa.proto

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa.proto`
- sha256: `7256f08be96643451ff01d4ee1298f3157985d28c08006033a84eea873d4a0fa`
- bytes: 34852

````protobuf

//---------------------------------------------------------------------
// This file is generated from VISA API metadata version 23.0.0
//---------------------------------------------------------------------
// Proto file for the VISA Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.visa";
option java_outer_classname = "Visa";
option csharp_namespace = "NationalInstruments.Grpc.Visa";

package visa_grpc;

import "session.proto";

service Visa {
  rpc AssertIntrSignal(AssertIntrSignalRequest) returns (AssertIntrSignalResponse);
  rpc AssertTrigger(AssertTriggerRequest) returns (AssertTriggerResponse);
  rpc AssertUtilSignal(AssertUtilSignalRequest) returns (AssertUtilSignalResponse);
  rpc Clear(ClearRequest) returns (ClearResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc CloseEvent(CloseEventRequest) returns (CloseEventResponse);
  rpc DisableEvent(DisableEventRequest) returns (DisableEventResponse);
  rpc DiscardEvents(DiscardEventsRequest) returns (DiscardEventsResponse);
  rpc EnableEvent(EnableEventRequest) returns (EnableEventResponse);
  rpc FindRsrc(FindRsrcRequest) returns (FindRsrcResponse);
  rpc Flush(FlushRequest) returns (FlushResponse);
  rpc GetAttribute(GetAttributeRequest) returns (GetAttributeResponse);
  rpc GetAttributeEvent(GetAttributeEventRequest) returns (GetAttributeEventResponse);
  rpc GpibCommand(GpibCommandRequest) returns (GpibCommandResponse);
  rpc GpibControlATN(GpibControlATNRequest) returns (GpibControlATNResponse);
  rpc GpibControlREN(GpibControlRENRequest) returns (GpibControlRENResponse);
  rpc GpibPassControl(GpibPassControlRequest) returns (GpibPassControlResponse);
  rpc GpibSendIFC(GpibSendIFCRequest) returns (GpibSendIFCResponse);
  rpc In16(In16Request) returns (In16Response);
  rpc In32(In32Request) returns (In32Response);
  rpc In64(In64Request) returns (In64Response);
  rpc In8(In8Request) returns (In8Response);
  rpc Lock(LockRequest) returns (LockResponse);
  rpc MapAddress(MapAddressRequest) returns (MapAddressResponse);
  rpc MapTrigger(MapTriggerRequest) returns (MapTriggerResponse);
  rpc MemAlloc(MemAllocRequest) returns (MemAllocResponse);
  rpc MemAllocEx(MemAllocExRequest) returns (MemAllocExResponse);
  rpc MemFree(MemFreeRequest) returns (MemFreeResponse);
  rpc MoveIn16(MoveIn16Request) returns (MoveIn16Response);
  rpc MoveIn32(MoveIn32Request) returns (MoveIn32Response);
  rpc MoveIn64(MoveIn64Request) returns (MoveIn64Response);
  rpc MoveIn8(MoveIn8Request) returns (MoveIn8Response);
  rpc MoveOut16(MoveOut16Request) returns (MoveOut16Response);
  rpc MoveOut32(MoveOut32Request) returns (MoveOut32Response);
  rpc MoveOut64(MoveOut64Request) returns (MoveOut64Response);
  rpc MoveOut8(MoveOut8Request) returns (MoveOut8Response);
  rpc Open(OpenRequest) returns (OpenResponse);
  rpc Out16(Out16Request) returns (Out16Response);
  rpc Out32(Out32Request) returns (Out32Response);
  rpc Out64(Out64Request) returns (Out64Response);
  rpc Out8(Out8Request) returns (Out8Response);
  rpc ParseRsrc(ParseRsrcRequest) returns (ParseRsrcResponse);
  rpc Peek16(Peek16Request) returns (Peek16Response);
  rpc Peek32(Peek32Request) returns (Peek32Response);
  rpc Peek64(Peek64Request) returns (Peek64Response);
  rpc Peek8(Peek8Request) returns (Peek8Response);
  rpc Poke16(Poke16Request) returns (Poke16Response);
  rpc Poke32(Poke32Request) returns (Poke32Response);
  rpc Poke64(Poke64Request) returns (Poke64Response);
  rpc Poke8(Poke8Request) returns (Poke8Response);
  rpc PxiReserveTriggers(PxiReserveTriggersRequest) returns (PxiReserveTriggersResponse);
  rpc Read(ReadRequest) returns (ReadResponse);
  rpc ReadAsync(ReadAsyncRequest) returns (ReadAsyncResponse);
  rpc ReadSTB(ReadSTBRequest) returns (ReadSTBResponse);
  rpc SetAttribute(SetAttributeRequest) returns (SetAttributeResponse);
  rpc SetBuf(SetBufRequest) returns (SetBufResponse);
  rpc StatusDesc(StatusDescRequest) returns (StatusDescResponse);
  rpc Terminate(TerminateRequest) returns (TerminateResponse);
  rpc Unlock(UnlockRequest) returns (UnlockResponse);
  rpc UnmapAddress(UnmapAddressRequest) returns (UnmapAddressResponse);
  rpc UnmapTrigger(UnmapTriggerRequest) returns (UnmapTriggerResponse);
  rpc UsbControlIn(UsbControlInRequest) returns (UsbControlInResponse);
  rpc UsbControlOut(UsbControlOutRequest) returns (UsbControlOutResponse);
  rpc VxiCommandQuery(VxiCommandQueryRequest) returns (VxiCommandQueryResponse);
  rpc WaitOnEvent(WaitOnEventRequest) returns (WaitOnEventResponse);
  rpc Write(WriteRequest) returns (WriteResponse);
  rpc WriteAsync(WriteAsyncRequest) returns (WriteAsyncResponse);
}

enum VisaAttribute {
  VISA_ATTRIBUTE_UNSPECIFIED = 0;
  VISA_ATTRIBUTE_RSRC_CLASS = -1073807359;
  VISA_ATTRIBUTE_RSRC_NAME = -1073807358;
  VISA_ATTRIBUTE_MANF_NAME = -1073807246;
  VISA_ATTRIBUTE_MODEL_NAME = -1073807241;
  VISA_ATTRIBUTE_INTF_INST_NAME = -1073807127;
  VISA_ATTRIBUTE_RSRC_MANF_NAME = -1073806988;
  VISA_ATTRIBUTE_TCPIP_ADDR = -1073806955;
  VISA_ATTRIBUTE_TCPIP_HOSTNAME = -1073806954;
  VISA_ATTRIBUTE_TCPIP_DEVICE_NAME = -1073806951;
  VISA_ATTRIBUTE_USB_SERIAL_NUM = -1073806944;
  VISA_ATTRIBUTE_PXI_SLOTPATH = -1073806841;
  VISA_ATTRIBUTE_TCPIP_SERVER_CERT_ISSUER_NAME = -1073806736;
  VISA_ATTRIBUTE_TCPIP_SERVER_CERT_SUBJECT_NAME = -1073806735;
  VISA_ATTRIBUTE_TCPIP_SERVER_CERT_EXPIRATION_DATE = -1073806734;
  VISA_ATTRIBUTE_TCPIP_SASL_MECHANISM = -1073806732;
  VISA_ATTRIBUTE_TCPIP_TLS_CIPHER_SUITE = -1073806731;
  VISA_ATTRIBUTE_TCPIP_SERVER_CERT = -1073806730;
  VISA_ATTRIBUTE_OPER_NAME = -1073790910;
  VISA_ATTRIBUTE_RECV_TCPIP_ADDR = -1073790568;
  VISA_ATTRIBUTE_USB_RECV_INTR_DATA = -1073790543;
  VISA_ATTRIBUTE_RSRC_IMPL_VERSION = 1073676291;
  VISA_ATTRIBUTE_RSRC_LOCK_STATE = 1073676292;
  VISA_ATTRIBUTE_MAX_QUEUE_LENGTH = 1073676293;
  VISA_ATTRIBUTE_USER_DATA = 1073676295;
  VISA_ATTRIBUTE_FDC_CHNL = 1073676301;
  VISA_ATTRIBUTE_FDC_MODE = 1073676303;
  VISA_ATTRIBUTE_FDC_USE_PAIR = 1073676307;
  VISA_ATTRIBUTE_SEND_END_EN = 1073676310;
  VISA_ATTRIBUTE_TERMCHAR = 1073676312;
  VISA_ATTRIBUTE_TMO_VALUE = 1073676314;
  VISA_ATTRIBUTE_GPIB_READDR_EN = 1073676315;
  VISA_ATTRIBUTE_IO_PROT = 1073676316;
  VISA_ATTRIBUTE_DMA_ALLOW_EN = 1073676318;
  VISA_ATTRIBUTE_ASRL_BAUD = 1073676321;
  VISA_ATTRIBUTE_ASRL_DATA_BITS = 1073676322;
  VISA_ATTRIBUTE_ASRL_PARITY = 1073676323;
  VISA_ATTRIBUTE_ASRL_STOP_BITS = 1073676324;
  VISA_ATTRIBUTE_ASRL_FLOW_CNTRL = 1073676325;
  VISA_ATTRIBUTE_RD_BUF_OPER_MODE = 1073676330;
  VISA_ATTRIBUTE_RD_BUF_SIZE = 1073676331;
  VISA_ATTRIBUTE_WR_BUF_OPER_MODE = 1073676333;
  VISA_ATTRIBUTE_WR_BUF_SIZE = 1073676334;
  VISA_ATTRIBUTE_SUPPRESS_END_EN = 1073676342;
  VISA_ATTRIBUTE_TERMCHAR_EN = 1073676344;
  VISA_ATTRIBUTE_DEST_ACCESS_PRIV = 1073676345;
  VISA_ATTRIBUTE_DEST_BYTE_ORDER = 1073676346;
  VISA_ATTRIBUTE_SRC_ACCESS_PRIV = 1073676348;
  VISA_ATTRIBUTE_SRC_BYTE_ORDER = 1073676349;
  VISA_ATTRIBUTE_SRC_INCREMENT = 1073676352;
  VISA_ATTRIBUTE_DEST_INCREMENT = 1073676353;
  VISA_ATTRIBUTE_WIN_ACCESS_PRIV = 1073676357;
  VISA_ATTRIBUTE_WIN_BYTE_ORDER = 1073676359;
  VISA_ATTRIBUTE_GPIB_ATN_STATE = 1073676375;
  VISA_ATTRIBUTE_GPIB_ADDR_STATE = 1073676380;
  VISA_ATTRIBUTE_GPIB_CIC_STATE = 1073676382;
  VISA_ATTRIBUTE_GPIB_NDAC_STATE = 1073676386;
  VISA_ATTRIBUTE_GPIB_SRQ_STATE = 1073676391;
  VISA_ATTRIBUTE_GPIB_SYS_CNTRL_STATE = 1073676392;
  VISA_ATTRIBUTE_GPIB_HS488_CBL_LEN = 1073676393;
  VISA_ATTRIBUTE_CMDR_LA = 1073676395;
  VISA_ATTRIBUTE_VXI_DEV_CLASS = 1073676396;
  VISA_ATTRIBUTE_MAINFRAME_LA = 1073676400;
  VISA_ATTRIBUTE_VXI_VME_INTR_STATUS = 1073676427;
  VISA_ATTRIBUTE_VXI_TRIG_STATUS = 1073676429;
  VISA_ATTRIBUTE_VXI_VME_SYSFAIL_STATE = 1073676436;
  VISA_ATTRIBUTE_WIN_BASE_ADDR = 1073676440;
  VISA_ATTRIBUTE_WIN_SIZE = 1073676442;
  VISA_ATTRIBUTE_ASRL_AVAIL_NUM = 1073676460;
  VISA_ATTRIBUTE_MEM_BASE = 1073676461;
  VISA_ATTRIBUTE_ASRL_CTS_STATE = 1073676462;
  VISA_ATTRIBUTE_ASRL_DCD_STATE = 1073676463;
  VISA_ATTRIBUTE_ASRL_DISCARD_NULL = 1073676464;
  VISA_ATTRIBUTE_ASRL_DSR_STATE = 1073676465;
  VISA_ATTRIBUTE_ASRL_DTR_STATE = 1073676466;
  VISA_ATTRIBUTE_ASRL_END_IN = 1073676467;
  VISA_ATTRIBUTE_ASRL_END_OUT = 1073676468;
  VISA_ATTRIBUTE_ASRL_REPLACE_CHAR = 1073676478;
  VISA_ATTRIBUTE_ASRL_RI_STATE = 1073676479;
  VISA_ATTRIBUTE_ASRL_RTS_STATE = 1073676480;
  VISA_ATTRIBUTE_ASRL_XON_CHAR = 1073676481;
  VISA_ATTRIBUTE_ASRL_XOFF_CHAR = 1073676482;
  VISA_ATTRIBUTE_WIN_ACCESS = 1073676483;
  VISA_ATTRIBUTE_VXI_LA = 1073676501;
  VISA_ATTRIBUTE_MANF_ID = 1073676505;
  VISA_ATTRIBUTE_MEM_SIZE = 1073676509;
  VISA_ATTRIBUTE_MEM_SPACE = 1073676510;
  VISA_ATTRIBUTE_MODEL_CODE = 1073676511;
  VISA_ATTRIBUTE_SLOT = 1073676520;
  VISA_ATTRIBUTE_IMMEDIATE_SERV = 1073676544;
  VISA_ATTRIBUTE_INTF_PARENT_NUM = 1073676545;
  VISA_ATTRIBUTE_RSRC_SPEC_VERSION = 1073676656;
  VISA_ATTRIBUTE_INTF_TYPE = 1073676657;
  VISA_ATTRIBUTE_GPIB_PRIMARY_ADDR = 1073676658;
  VISA_ATTRIBUTE_GPIB_SECONDARY_ADDR = 1073676659;
  VISA_ATTRIBUTE_RSRC_MANF_ID = 1073676661;
  VISA_ATTRIBUTE_INTF_NUM = 1073676662;
  VISA_ATTRIBUTE_TRIG_ID = 1073676663;
  VISA_ATTRIBUTE_GPIB_REN_STATE = 1073676673;
  VISA_ATTRIBUTE_GPIB_UNADDR_EN = 1073676676;
  VISA_ATTRIBUTE_DEV_STATUS_BYTE = 1073676681;
  VISA_ATTRIBUTE_FILE_APPEND_EN = 1073676690;
  VISA_ATTRIBUTE_VXI_TRIG_SUPPORT = 1073676692;
  VISA_ATTRIBUTE_TCPIP_PORT = 1073676695;
  VISA_ATTRIBUTE_TCPIP_NODELAY = 1073676698;
  VISA_ATTRIBUTE_TCPIP_KEEPALIVE = 1073676699;
  VISA_ATTRIBUTE_4882_COMPLIANT = 1073676703;
  VISA_ATTRIBUTE_USB_INTFC_NUM = 1073676705;
  VISA_ATTRIBUTE_USB_BULK_OUT_PIPE = 1073676706;
  VISA_ATTRIBUTE_USB_BULK_IN_PIPE = 1073676707;
  VISA_ATTRIBUTE_USB_INTR_IN_PIPE = 1073676708;
  VISA_ATTRIBUTE_USB_CLASS = 1073676709;
  VISA_ATTRIBUTE_USB_SUBCLASS = 1073676710;
  VISA_ATTRIBUTE_USB_PROTOCOL = 1073676711;
  VISA_ATTRIBUTE_USB_ALT_SETTING = 1073676712;
  VISA_ATTRIBUTE_USB_END_IN = 1073676713;
  VISA_ATTRIBUTE_USB_NUM_INTFCS = 1073676714;
  VISA_ATTRIBUTE_USB_NUM_PIPES = 1073676715;
  VISA_ATTRIBUTE_USB_BULK_OUT_STATUS = 1073676716;
  VISA_ATTRIBUTE_USB_BULK_IN_STATUS = 1073676717;
  VISA_ATTRIBUTE_USB_INTR_IN_STATUS = 1073676718;
  VISA_ATTRIBUTE_USB_MAX_INTR_SIZE = 1073676719;
  VISA_ATTRIBUTE_USB_CTRL_PIPE = 1073676720;
  VISA_ATTRIBUTE_ASRL_CONNECTED = 1073676731;
  VISA_ATTRIBUTE_ASRL_BREAK_STATE = 1073676732;
  VISA_ATTRIBUTE_ASRL_BREAK_LEN = 1073676733;
  VISA_ATTRIBUTE_ASRL_ALLOW_TRANSMIT = 1073676734;
  VISA_ATTRIBUTE_ASRL_WIRE_MODE = 1073676735;
  VISA_ATTRIBUTE_FIREWIRE_DEST_UPPER_OFFSET = 1073676784;
  VISA_ATTRIBUTE_FIREWIRE_SRC_UPPER_OFFSET = 1073676785;
  VISA_ATTRIBUTE_FIREWIRE_WIN_UPPER_OFFSET = 1073676786;
  VISA_ATTRIBUTE_FIREWIRE_VENDOR_ID = 1073676787;
  VISA_ATTRIBUTE_FIREWIRE_LOWER_CHIP_ID = 1073676788;
  VISA_ATTRIBUTE_FIREWIRE_UPPER_CHIP_ID = 1073676789;
  VISA_ATTRIBUTE_PXI_DEV_NUM = 1073676801;
  VISA_ATTRIBUTE_PXI_FUNC_NUM = 1073676802;
  VISA_ATTRIBUTE_PXI_BUS_NUM = 1073676805;
  VISA_ATTRIBUTE_PXI_CHASSIS = 1073676806;
  VISA_ATTRIBUTE_PXI_SLOT_LBUS_LEFT = 1073676808;
  VISA_ATTRIBUTE_PXI_SLOT_LBUS_RIGHT = 1073676809;
  VISA_ATTRIBUTE_PXI_TRIG_BUS = 1073676810;
  VISA_ATTRIBUTE_PXI_STAR_TRIG_BUS = 1073676811;
  VISA_ATTRIBUTE_PXI_STAR_TRIG_LINE = 1073676812;
  VISA_ATTRIBUTE_PXI_SRC_TRIG_BUS = 1073676813;
  VISA_ATTRIBUTE_PXI_DEST_TRIG_BUS = 1073676814;
  VISA_ATTRIBUTE_PXI_MEM_TYPE_BAR0 = 1073676817;
  VISA_ATTRIBUTE_PXI_MEM_TYPE_BAR1 = 1073676818;
  VISA_ATTRIBUTE_PXI_MEM_TYPE_BAR2 = 1073676819;
  VISA_ATTRIBUTE_PXI_MEM_TYPE_BAR3 = 1073676820;
  VISA_ATTRIBUTE_PXI_MEM_TYPE_BAR4 = 1073676821;
  VISA_ATTRIBUTE_PXI_MEM_TYPE_BAR5 = 1073676822;
  VISA_ATTRIBUTE_PXI_MEM_BASE_BAR0 = 1073676833;
  VISA_ATTRIBUTE_PXI_MEM_BASE_BAR1 = 1073676834;
  VISA_ATTRIBUTE_PXI_MEM_BASE_BAR2 = 1073676835;
  VISA_ATTRIBUTE_PXI_MEM_BASE_BAR3 = 1073676836;
  VISA_ATTRIBUTE_PXI_MEM_BASE_BAR4 = 1073676837;
  VISA_ATTRIBUTE_PXI_MEM_BASE_BAR5 = 1073676838;
  VISA_ATTRIBUTE_PXI_MEM_SIZE_BAR0 = 1073676849;
  VISA_ATTRIBUTE_PXI_MEM_SIZE_BAR1 = 1073676850;
  VISA_ATTRIBUTE_PXI_MEM_SIZE_BAR2 = 1073676851;
  VISA_ATTRIBUTE_PXI_MEM_SIZE_BAR3 = 1073676852;
  VISA_ATTRIBUTE_PXI_MEM_SIZE_BAR4 = 1073676853;
  VISA_ATTRIBUTE_PXI_MEM_SIZE_BAR5 = 1073676854;
  VISA_ATTRIBUTE_PXI_IS_EXPRESS = 1073676864;
  VISA_ATTRIBUTE_PXI_SLOT_LWIDTH = 1073676865;
  VISA_ATTRIBUTE_PXI_MAX_LWIDTH = 1073676866;
  VISA_ATTRIBUTE_PXI_ACTUAL_LWIDTH = 1073676867;
  VISA_ATTRIBUTE_PXI_DSTAR_BUS = 1073676868;
  VISA_ATTRIBUTE_PXI_DSTAR_SET = 1073676869;
  VISA_ATTRIBUTE_PXI_ALLOW_WRITE_COMBINE = 1073676870;
  VISA_ATTRIBUTE_PXI_SLOT_WIDTH = 1073676871;
  VISA_ATTRIBUTE_PXI_SLOT_OFFSET = 1073676872;
  VISA_ATTRIBUTE_TCPIP_SERVER_CERT_IS_PERPETUAL = 1073676915;
  VISA_ATTRIBUTE_TCPIP_SERVER_CERT_SIZE = 1073676919;
  VISA_ATTRIBUTE_TCPIP_HISLIP_OVERLAP_EN = 1073677056;
  VISA_ATTRIBUTE_TCPIP_HISLIP_VERSION = 1073677057;
  VISA_ATTRIBUTE_TCPIP_HISLIP_MAX_MESSAGE_KB = 1073677058;
  VISA_ATTRIBUTE_TCPIP_IS_HISLIP = 1073677059;
  VISA_ATTRIBUTE_TCPIP_HISLIP_ENCRYPTION_EN = 1073677060;
  VISA_ATTRIBUTE_JOB_ID = 1073692678;
  VISA_ATTRIBUTE_EVENT_TYPE = 1073692688;
  VISA_ATTRIBUTE_SIGP_STATUS_ID = 1073692689;
  VISA_ATTRIBUTE_RECV_TRIG_ID = 1073692690;
  VISA_ATTRIBUTE_INTR_STATUS_ID = 1073692707;
  VISA_ATTRIBUTE_STATUS = 1073692709;
  VISA_ATTRIBUTE_RET_COUNT = 1073692710;
  VISA_ATTRIBUTE_BUFFER = 1073692711;
  VISA_ATTRIBUTE_RECV_INTR_LEVEL = 1073692737;
  VISA_ATTRIBUTE_VXI_TRIG_LINES_EN = 1073692739;
  VISA_ATTRIBUTE_VXI_TRIG_DIR = 1073692740;
  VISA_ATTRIBUTE_GPIB_RECV_CIC_STATE = 1073693075;
  VISA_ATTRIBUTE_USB_RECV_INTR_SIZE = 1073693104;
  VISA_ATTRIBUTE_PXI_RECV_INTR_SEQ = 1073693248;
  VISA_ATTRIBUTE_PXI_RECV_INTR_DATA = 1073693249;
}

enum AddressSpace {
  ADDRESS_SPACE_LOCAL_SPACE = 0;
  ADDRESS_SPACE_A16_SPACE = 1;
  ADDRESS_SPACE_A24_SPACE = 2;
  ADDRESS_SPACE_A32_SPACE = 3;
  ADDRESS_SPACE_A64_SPACE = 4;
  ADDRESS_SPACE_PXI_ALLOC_SPACE = 9;
  ADDRESS_SPACE_PXI_CFG_SPACE = 10;
  ADDRESS_SPACE_PXI_BAR0_SPACE = 11;
  ADDRESS_SPACE_PXI_BAR1_SPACE = 12;
  ADDRESS_SPACE_PXI_BAR2_SPACE = 13;
  ADDRESS_SPACE_PXI_BAR3_SPACE = 14;
  ADDRESS_SPACE_PXI_BAR4_SPACE = 15;
  ADDRESS_SPACE_PXI_BAR5_SPACE = 16;
  ADDRESS_SPACE_OPAQUE_SPACE = 65535;
}

enum AssertInterruptSignalMode {
  ASSERT_INTERRUPT_SIGNAL_MODE_ASSERT_USE_ASSIGNED = 0;
  ASSERT_INTERRUPT_SIGNAL_MODE_ASSERT_IRQ1 = 1;
  ASSERT_INTERRUPT_SIGNAL_MODE_ASSERT_IRQ2 = 2;
  ASSERT_INTERRUPT_SIGNAL_MODE_ASSERT_IRQ3 = 3;
  ASSERT_INTERRUPT_SIGNAL_MODE_ASSERT_IRQ4 = 4;
  ASSERT_INTERRUPT_SIGNAL_MODE_ASSERT_IRQ5 = 5;
  ASSERT_INTERRUPT_SIGNAL_MODE_ASSERT_IRQ6 = 6;
  ASSERT_INTERRUPT_SIGNAL_MODE_ASSERT_IRQ7 = 7;
  ASSERT_INTERRUPT_SIGNAL_MODE_ASSERT_SIGNAL = -1;
}

enum AssertUtilSignalMode {
  ASSERT_UTIL_SIGNAL_MODE_UNSPECIFIED = 0;
  ASSERT_UTIL_SIGNAL_MODE_UTIL_ASSERT_SYSRESET = 1;
  ASSERT_UTIL_SIGNAL_MODE_UTIL_ASSERT_SYSFAIL = 2;
  ASSERT_UTIL_SIGNAL_MODE_UTIL_DEASSERT_SYSFAIL = 3;
}

enum BufferMask {
  BUFFER_MASK_UNSPECIFIED = 0;
  BUFFER_MASK_IO_IN_BUF = 16;
  BUFFER_MASK_IO_OUT_BUF = 32;
  BUFFER_MASK_IO_IN_BUF_DISCARD = 64;
  BUFFER_MASK_IO_OUT_BUF_DISCARD = 128;
}

enum EventMechanism {
  EVENT_MECHANISM_UNSPECIFIED = 0;
  EVENT_MECHANISM_QUEUE = 1;
  EVENT_MECHANISM_HNDLR = 2;
  EVENT_MECHANISM_SUSPEND_HNDLR = 4;
  EVENT_MECHANISM_ALL_MECH = 65535;
}

enum EventType {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_ALL_ENABLED_EVENTS = 1073709055;
  EVENT_TYPE_EVENT_ASRL_BREAK = 1073684515;
  EVENT_TYPE_EVENT_ASRL_CTS = 1073684521;
  EVENT_TYPE_EVENT_ASRL_DSR = 1073684522;
  EVENT_TYPE_EVENT_ASRL_DCD = 1073684524;
  EVENT_TYPE_EVENT_ASRL_RI = 1073684526;
  EVENT_TYPE_EVENT_ASRL_CHAR = 1073684533;
  EVENT_TYPE_EVENT_ASRL_TERMCHAR = 1073684516;
  EVENT_TYPE_EVENT_IO_COMPLETION = 1073684489;
  EVENT_TYPE_EVENT_TRIG = -1073799158;
  EVENT_TYPE_EVENT_SERVICE_REQ = 1073684491;
  EVENT_TYPE_EVENT_CLEAR = 1073684493;
  EVENT_TYPE_EVENT_EXCEPTION = -1073799154;
  EVENT_TYPE_EVENT_GPIB_CIC = 1073684498;
  EVENT_TYPE_EVENT_GPIB_TALK = 1073684499;
  EVENT_TYPE_EVENT_GPIB_LISTEN = 1073684500;
  EVENT_TYPE_EVENT_VXI_VME_SYSFAIL = 1073684509;
  EVENT_TYPE_EVENT_VXI_VME_SYSRESET = 1073684510;
  EVENT_TYPE_EVENT_VXI_SIGP = 1073684512;
  EVENT_TYPE_EVENT_VXI_VME_INTR = -1073799135;
  EVENT_TYPE_EVENT_PXI_INTR = 1073684514;
  EVENT_TYPE_EVENT_TCPIP_CONNECT = 1073684534;
  EVENT_TYPE_EVENT_USB_INTR = 1073684535;
}

enum GpibControlAtnMode {
  GPIB_CONTROL_ATN_MODE_ATN_DEASSERT = 0;
  GPIB_CONTROL_ATN_MODE_ATN_ASSERT = 1;
  GPIB_CONTROL_ATN_MODE_ATN_DEASSERT_HANDSHAKE = 2;
  GPIB_CONTROL_ATN_MODE_ATN_ASSERT_IMMEDIATE = 3;
}

enum GpibControlRenMode {
  GPIB_CONTROL_REN_MODE_REN_DEASSERT = 0;
  GPIB_CONTROL_REN_MODE_REN_ASSERT = 1;
  GPIB_CONTROL_REN_MODE_REN_DEASSERT_GTL = 2;
  GPIB_CONTROL_REN_MODE_REN_ASSERT_ADDRESS = 3;
  GPIB_CONTROL_REN_MODE_REN_ASSERT_LLO = 4;
  GPIB_CONTROL_REN_MODE_REN_ASSERT_ADDRESS_LLO = 5;
  GPIB_CONTROL_REN_MODE_REN_ADDRESS_GTL = 6;
}

enum LockState {
  LOCK_STATE_NO_LOCK = 0;
  LOCK_STATE_EXCLUSIVE_LOCK = 1;
  LOCK_STATE_SHARED_LOCK = 2;
}

enum TriggerLine {
  TRIGGER_LINE_TTL0 = 0;
  TRIGGER_LINE_ALL = -2;
  TRIGGER_LINE_SW = -1;
  TRIGGER_LINE_TTL1 = 1;
  TRIGGER_LINE_TTL2 = 2;
  TRIGGER_LINE_TTL3 = 3;
  TRIGGER_LINE_TTL4 = 4;
  TRIGGER_LINE_TTL5 = 5;
  TRIGGER_LINE_TTL6 = 6;
  TRIGGER_LINE_TTL7 = 7;
  TRIGGER_LINE_ECL0 = 8;
  TRIGGER_LINE_ECL1 = 9;
  TRIGGER_LINE_ECL2 = 10;
  TRIGGER_LINE_ECL3 = 11;
  TRIGGER_LINE_ECL4 = 12;
  TRIGGER_LINE_ECL5 = 13;
  TRIGGER_LINE_STAR_SLOT1 = 14;
  TRIGGER_LINE_STAR_SLOT2 = 15;
  TRIGGER_LINE_STAR_SLOT3 = 16;
  TRIGGER_LINE_STAR_SLOT4 = 17;
  TRIGGER_LINE_STAR_SLOT5 = 18;
  TRIGGER_LINE_STAR_SLOT6 = 19;
  TRIGGER_LINE_STAR_SLOT7 = 20;
  TRIGGER_LINE_STAR_SLOT8 = 21;
  TRIGGER_LINE_STAR_SLOT9 = 22;
  TRIGGER_LINE_STAR_SLOT10 = 23;
  TRIGGER_LINE_STAR_SLOT11 = 24;
  TRIGGER_LINE_STAR_SLOT12 = 25;
  TRIGGER_LINE_STAR_INSTR = 26;
  TRIGGER_LINE_PANEL_IN = 27;
  TRIGGER_LINE_PANEL_OUT = 28;
  TRIGGER_LINE_STAR_VXI0 = 29;
  TRIGGER_LINE_STAR_VXI1 = 30;
  TRIGGER_LINE_STAR_VXI2 = 31;
  TRIGGER_LINE_TTL8 = 32;
  TRIGGER_LINE_TTL9 = 33;
  TRIGGER_LINE_TTL10 = 34;
  TRIGGER_LINE_TTL11 = 35;
}

enum TriggerProtocol {
  TRIGGER_PROTOCOL_PROT_DEFAULT = 0;
  TRIGGER_PROTOCOL_PROT_OFF = 1;
  TRIGGER_PROTOCOL_PROT_ON = 2;
  TRIGGER_PROTOCOL_PROT_SYNC = 5;
  TRIGGER_PROTOCOL_PROT_RESERVE = 6;
  TRIGGER_PROTOCOL_PROT_UNRESERVE = 7;
}

enum VxiCmdType {
  VXI_CMD_TYPE_UNSPECIFIED = 0;
  VXI_CMD_TYPE_VXI_RESP16 = 2;
  VXI_CMD_TYPE_VXI_RESP32 = 4;
  VXI_CMD_TYPE_VXI_CMD16 = 512;
  VXI_CMD_TYPE_VXI_CMD16_RESP16 = 514;
  VXI_CMD_TYPE_VXI_CMD32 = 1024;
  VXI_CMD_TYPE_VXI_CMD32_RESP16 = 1026;
  VXI_CMD_TYPE_VXI_CMD32_RESP32 = 1028;
}

message AttributeValueData {
  oneof data {
    uint32 value_u8 = 1;
    int32 value_i16 = 2;
    uint32 value_u16 = 3;
    int32 value_i32 = 4;
    uint32 value_u32 = 5;
    fixed64 value_u64 = 6;
    bool value_bool = 7;
    string value_string = 8;
    bytes value_bytes = 9;
  }
}

message AssertIntrSignalRequest {
  nidevice_grpc.Session vi = 1;
  oneof mode_enum {
    AssertInterruptSignalMode mode = 2;
    sint32 mode_raw = 3;
  }
  uint32 status_id = 4;
}

message AssertIntrSignalResponse {
  int32 status = 1;
}

message AssertTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof protocol_enum {
    TriggerProtocol protocol = 2;
    uint32 protocol_raw = 3;
  }
}

message AssertTriggerResponse {
  int32 status = 1;
}

message AssertUtilSignalRequest {
  nidevice_grpc.Session vi = 1;
  oneof mode_enum {
    AssertUtilSignalMode mode = 2;
    uint32 mode_raw = 3;
  }
}

message AssertUtilSignalResponse {
  int32 status = 1;
}

message ClearRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearResponse {
  int32 status = 1;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message CloseEventRequest {
  uint32 event_handle = 1;
}

message CloseEventResponse {
  int32 status = 1;
}

message DisableEventRequest {
  nidevice_grpc.Session vi = 1;
  oneof event_type_enum {
    EventType event_type = 2;
    uint32 event_type_raw = 3;
  }
  oneof event_mechanism_enum {
    EventMechanism event_mechanism = 4;
    uint32 event_mechanism_raw = 5;
  }
}

message DisableEventResponse {
  int32 status = 1;
}

message DiscardEventsRequest {
  nidevice_grpc.Session vi = 1;
  oneof event_type_enum {
    EventType event_type = 2;
    uint32 event_type_raw = 3;
  }
  oneof event_mechanism_enum {
    EventMechanism event_mechanism = 4;
    uint32 event_mechanism_raw = 5;
  }
}

message DiscardEventsResponse {
  int32 status = 1;
}

message EnableEventRequest {
  nidevice_grpc.Session vi = 1;
  oneof event_type_enum {
    EventType event_type = 2;
    uint32 event_type_raw = 3;
  }
  oneof event_mechanism_enum {
    EventMechanism event_mechanism = 4;
    uint32 event_mechanism_raw = 5;
  }
  uint32 filter_context = 6;
}

message EnableEventResponse {
  int32 status = 1;
}

message FindRsrcRequest {
  string expression = 1;
}

message FindRsrcResponse {
  int32 status = 1;
  repeated string instrument_descriptor = 2;
}

message FlushRequest {
  nidevice_grpc.Session vi = 1;
  oneof mask_enum {
    BufferMask mask = 2;
    uint32 mask_raw = 3;
  }
}

message FlushResponse {
  int32 status = 1;
}

message GetAttributeRequest {
  nidevice_grpc.Session vi = 1;
  VisaAttribute attribute_name = 2;
}

message GetAttributeResponse {
  int32 status = 1;
  AttributeValueData attribute_value = 2;
}

message GetAttributeEventRequest {
  uint32 event_handle = 1;
  VisaAttribute attribute_name = 2;
}

message GetAttributeEventResponse {
  int32 status = 1;
  AttributeValueData attribute_value = 2;
}

message GpibCommandRequest {
  nidevice_grpc.Session vi = 1;
  bytes buffer = 2;
}

message GpibCommandResponse {
  int32 status = 1;
  uint32 return_count = 2;
}

message GpibControlATNRequest {
  nidevice_grpc.Session vi = 1;
  oneof mode_enum {
    GpibControlAtnMode mode = 2;
    uint32 mode_raw = 3;
  }
}

message GpibControlATNResponse {
  int32 status = 1;
}

message GpibControlRENRequest {
  nidevice_grpc.Session vi = 1;
  oneof mode_enum {
    GpibControlRenMode mode = 2;
    uint32 mode_raw = 3;
  }
}

message GpibControlRENResponse {
  int32 status = 1;
}

message GpibPassControlRequest {
  nidevice_grpc.Session vi = 1;
  uint32 primary_address = 2;
  uint32 secondary_address = 3;
}

message GpibPassControlResponse {
  int32 status = 1;
}

message GpibSendIFCRequest {
  nidevice_grpc.Session vi = 1;
}

message GpibSendIFCResponse {
  int32 status = 1;
}

message In16Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
}

message In16Response {
  int32 status = 1;
  uint32 value = 2;
}

message In32Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
}

message In32Response {
  int32 status = 1;
  uint32 value = 2;
}

message In64Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
}

message In64Response {
  int32 status = 1;
  uint64 value = 2;
}

message In8Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
}

message In8Response {
  int32 status = 1;
  uint32 value = 2;
}

message LockRequest {
  nidevice_grpc.Session vi = 1;
  oneof lock_type_enum {
    LockState lock_type = 2;
    uint32 lock_type_raw = 3;
  }
  uint32 timeout = 4;
  string requested_key = 5;
}

message LockResponse {
  int32 status = 1;
  string access_key = 2;
}

message MapAddressRequest {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  uint64 map_size = 5;
  bool owner_access = 6;
  fixed64 suggested_address = 7;
}

message MapAddressResponse {
  int32 status = 1;
  fixed64 address = 2;
}

message MapTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_source_enum {
    TriggerLine trigger_source = 2;
    sint32 trigger_source_raw = 3;
  }
  oneof trigger_destination_enum {
    TriggerLine trigger_destination = 4;
    sint32 trigger_destination_raw = 5;
  }
  uint32 mode = 6;
}

message MapTriggerResponse {
  int32 status = 1;
}

message MemAllocRequest {
  nidevice_grpc.Session vi = 1;
  uint32 size = 2;
}

message MemAllocResponse {
  int32 status = 1;
  uint32 offset = 2;
}

message MemAllocExRequest {
  nidevice_grpc.Session vi = 1;
  uint64 size = 2;
}

message MemAllocExResponse {
  int32 status = 1;
  fixed64 offset = 2;
}

message MemFreeRequest {
  nidevice_grpc.Session vi = 1;
  fixed64 offset = 2;
}

message MemFreeResponse {
  int32 status = 1;
}

message MoveIn16Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  uint64 count = 5;
}

message MoveIn16Response {
  int32 status = 1;
  repeated uint32 buffer = 2;
}

message MoveIn32Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  uint64 count = 5;
}

message MoveIn32Response {
  int32 status = 1;
  repeated uint32 buffer = 2;
}

message MoveIn64Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  uint64 count = 5;
}

message MoveIn64Response {
  int32 status = 1;
  repeated uint64 buffer = 2;
}

message MoveIn8Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  uint64 count = 5;
}

message MoveIn8Response {
  int32 status = 1;
  bytes buffer = 2;
}

message MoveOut16Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  repeated uint32 buffer = 5;
}

message MoveOut16Response {
  int32 status = 1;
}

message MoveOut32Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  repeated uint32 buffer = 5;
}

message MoveOut32Response {
  int32 status = 1;
}

message MoveOut64Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  repeated uint64 buffer = 5;
}

message MoveOut64Response {
  int32 status = 1;
}

message MoveOut8Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  bytes buffer = 5;
}

message MoveOut8Response {
  int32 status = 1;
}

message OpenRequest {
  string session_name = 1;
  string instrument_descriptor = 2;
  oneof access_mode_enum {
    LockState access_mode = 3;
    uint32 access_mode_raw = 4;
  }
  uint32 open_timeout = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message OpenResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  bool new_session_initialized = 3;
  repeated EventType supported_events = 4;
}

message Out16Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  uint32 value = 5;
}

message Out16Response {
  int32 status = 1;
}

message Out32Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  uint32 value = 5;
}

message Out32Response {
  int32 status = 1;
}

message Out64Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  uint64 value = 5;
}

message Out64Response {
  int32 status = 1;
}

message Out8Request {
  nidevice_grpc.Session vi = 1;
  oneof address_space_enum {
    AddressSpace address_space = 2;
    uint32 address_space_raw = 3;
  }
  fixed64 offset = 4;
  uint32 value = 5;
}

message Out8Response {
  int32 status = 1;
}

message ParseRsrcRequest {
  string resource_name = 1;
}

message ParseRsrcResponse {
  int32 status = 1;
  uint32 interface_type = 2;
  uint32 interface_number = 3;
  string resource_class = 4;
  string expanded_unaliased_name = 5;
  string alias_if_exists = 6;
}

message Peek16Request {
  nidevice_grpc.Session vi = 1;
  fixed64 address = 2;
}

message Peek16Response {
  int32 status = 1;
  uint32 value = 2;
}

message Peek32Request {
  nidevice_grpc.Session vi = 1;
  fixed64 address = 2;
}

message Peek32Response {
  int32 status = 1;
  uint32 value = 2;
}

message Peek64Request {
  nidevice_grpc.Session vi = 1;
  fixed64 address = 2;
}

message Peek64Response {
  int32 status = 1;
  uint64 value = 2;
}

message Peek8Request {
  nidevice_grpc.Session vi = 1;
  fixed64 address = 2;
}

message Peek8Response {
  int32 status = 1;
  uint32 value = 2;
}

message Poke16Request {
  nidevice_grpc.Session vi = 1;
  fixed64 address = 2;
  uint32 value = 3;
}

message Poke16Response {
  int32 status = 1;
}

message Poke32Request {
  nidevice_grpc.Session vi = 1;
  fixed64 address = 2;
  uint32 value = 3;
}

message Poke32Response {
  int32 status = 1;
}

message Poke64Request {
  nidevice_grpc.Session vi = 1;
  fixed64 address = 2;
  uint64 value = 3;
}

message Poke64Response {
  int32 status = 1;
}

message Poke8Request {
  nidevice_grpc.Session vi = 1;
  fixed64 address = 2;
  uint32 value = 3;
}

message Poke8Response {
  int32 status = 1;
}

message PxiReserveTriggersRequest {
  nidevice_grpc.Session vi = 1;
  repeated sint32 trig_buses = 2;
  repeated sint32 trig_lines = 3;
}

message PxiReserveTriggersResponse {
  int32 status = 1;
}

message ReadRequest {
  nidevice_grpc.Session vi = 1;
  uint32 count = 2;
}

message ReadResponse {
  int32 status = 1;
  bytes buffer = 2;
  uint32 return_count = 3;
}

message ReadAsyncRequest {
  nidevice_grpc.Session vi = 1;
  uint32 count = 2;
}

message ReadAsyncResponse {
  int32 status = 1;
  uint32 job_identifier = 2;
}

message ReadSTBRequest {
  nidevice_grpc.Session vi = 1;
}

message ReadSTBResponse {
  int32 status = 1;
  uint32 status_byte = 2;
}

message SetAttributeRequest {
  nidevice_grpc.Session vi = 1;
  VisaAttribute attribute_name = 2;
  AttributeValueData attribute_value = 3;
}

message SetAttributeResponse {
  int32 status = 1;
}

message SetBufRequest {
  nidevice_grpc.Session vi = 1;
  oneof mask_enum {
    BufferMask mask = 2;
    uint32 mask_raw = 3;
  }
  uint32 buffer_size = 4;
}

message SetBufResponse {
  int32 status = 1;
}

message StatusDescRequest {
  nidevice_grpc.Session vi = 1;
  sint32 status_value = 2;
}

message StatusDescResponse {
  int32 status = 1;
  string status_description = 2;
}

message TerminateRequest {
  nidevice_grpc.Session vi = 1;
  uint32 degree = 2;
  uint32 job_identifier = 3;
}

message TerminateResponse {
  int32 status = 1;
}

message UnlockRequest {
  nidevice_grpc.Session vi = 1;
}

message UnlockResponse {
  int32 status = 1;
}

message UnmapAddressRequest {
  nidevice_grpc.Session vi = 1;
}

message UnmapAddressResponse {
  int32 status = 1;
}

message UnmapTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_source_enum {
    TriggerLine trigger_source = 2;
    sint32 trigger_source_raw = 3;
  }
  oneof trigger_destination_enum {
    TriggerLine trigger_destination = 4;
    sint32 trigger_destination_raw = 5;
  }
}

message UnmapTriggerResponse {
  int32 status = 1;
}

message UsbControlInRequest {
  nidevice_grpc.Session vi = 1;
  sint32 bm_request_type = 2;
  sint32 b_request = 3;
  uint32 w_value = 4;
  uint32 w_index = 5;
  uint32 w_length = 6;
}

message UsbControlInResponse {
  int32 status = 1;
  bytes buffer = 2;
  uint32 return_count = 3;
}

message UsbControlOutRequest {
  nidevice_grpc.Session vi = 1;
  sint32 bm_request_type = 2;
  sint32 b_request = 3;
  uint32 w_value = 4;
  uint32 w_index = 5;
  bytes buffer = 6;
}

message UsbControlOutResponse {
  int32 status = 1;
}

message VxiCommandQueryRequest {
  nidevice_grpc.Session vi = 1;
  oneof mode_enum {
    VxiCmdType mode = 2;
    uint32 mode_raw = 3;
  }
  uint32 command = 4;
}

message VxiCommandQueryResponse {
  int32 status = 1;
  uint32 command_response = 2;
}

message WaitOnEventRequest {
  nidevice_grpc.Session vi = 1;
  oneof in_event_type_enum {
    EventType in_event_type = 2;
    uint32 in_event_type_raw = 3;
  }
  uint32 timeout = 4;
}

message WaitOnEventResponse {
  int32 status = 1;
  EventType out_event_type = 2;
  uint32 out_event_type_raw = 3;
  uint32 event_handle = 4;
}

message WriteRequest {
  nidevice_grpc.Session vi = 1;
  bytes buffer = 2;
}

message WriteResponse {
  int32 status = 1;
  uint32 return_count = 2;
}

message WriteAsyncRequest {
  nidevice_grpc.Session vi = 1;
  bytes buffer = 2;
}

message WriteAsyncResponse {
  int32 status = 1;
  uint32 job_identifier = 2;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_attributes.h sha256=6c705f21a693d4f5ce313dd4a5a9178ea7cee1837a0baa3a7e412d8c3fc49233 bytes=8851 -->
## FILE: generated/visa/visa_attributes.h

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_attributes.h`
- sha256: `6c705f21a693d4f5ce313dd4a5a9178ea7cee1837a0baa3a7e412d8c3fc49233`
- bytes: 8851

````c

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
#ifndef VISA_ATTRIBUTE_TYPES_H
#define VISA_ATTRIBUTE_TYPES_H

#define NIVISA_USB

#include <visa.h>
#include <visa/visa_service.h>

namespace visa_grpc {

  inline AttributeValueData::DataCase GetAttributeType(ViAttr attributeID)
  {
    switch (attributeID) {
      case VI_ATTR_ASRL_REPLACE_CHAR:
      case VI_ATTR_ASRL_XOFF_CHAR:
      case VI_ATTR_ASRL_XON_CHAR:
      case VI_ATTR_DEV_STATUS_BYTE:
      case VI_ATTR_FIREWIRE_UPPER_CHIP_ID:
      case VI_ATTR_TERMCHAR:
        return AttributeValueData::kValueU8;

      case VI_ATTR_ASRL_BREAK_LEN:
      case VI_ATTR_ASRL_BREAK_STATE:
      case VI_ATTR_ASRL_CTS_STATE:
      case VI_ATTR_ASRL_DCD_STATE:
      case VI_ATTR_ASRL_DSR_STATE:
      case VI_ATTR_ASRL_DTR_STATE:
      case VI_ATTR_ASRL_RI_STATE:
      case VI_ATTR_ASRL_RTS_STATE:
      case VI_ATTR_ASRL_WIRE_MODE:
      case VI_ATTR_CMDR_LA:
      case VI_ATTR_GPIB_ATN_STATE:
      case VI_ATTR_GPIB_HS488_CBL_LEN:
      case VI_ATTR_GPIB_NDAC_STATE:
      case VI_ATTR_GPIB_REN_STATE:
      case VI_ATTR_GPIB_SRQ_STATE:
      case VI_ATTR_MAINFRAME_LA:
      case VI_ATTR_PXI_ACTUAL_LWIDTH:
      case VI_ATTR_PXI_CHASSIS:
      case VI_ATTR_PXI_DEST_TRIG_BUS:
      case VI_ATTR_PXI_DSTAR_BUS:
      case VI_ATTR_PXI_DSTAR_SET:
      case VI_ATTR_PXI_MAX_LWIDTH:
      case VI_ATTR_PXI_RECV_INTR_SEQ:
      case VI_ATTR_PXI_SLOT_LBUS_LEFT:
      case VI_ATTR_PXI_SLOT_LBUS_RIGHT:
      case VI_ATTR_PXI_SLOT_LWIDTH:
      case VI_ATTR_PXI_SRC_TRIG_BUS:
      case VI_ATTR_PXI_STAR_TRIG_BUS:
      case VI_ATTR_PXI_STAR_TRIG_LINE:
      case VI_ATTR_PXI_TRIG_BUS:
      case VI_ATTR_RECV_INTR_LEVEL:
      case VI_ATTR_RECV_TRIG_ID:
      case VI_ATTR_SLOT:
      case VI_ATTR_TRIG_ID:
      case VI_ATTR_USB_ALT_SETTING:
      case VI_ATTR_USB_BULK_IN_PIPE:
      case VI_ATTR_USB_BULK_IN_STATUS:
      case VI_ATTR_USB_BULK_OUT_PIPE:
      case VI_ATTR_USB_BULK_OUT_STATUS:
      case VI_ATTR_USB_CLASS:
      case VI_ATTR_USB_CTRL_PIPE:
      case VI_ATTR_USB_INTFC_NUM:
      case VI_ATTR_USB_INTR_IN_PIPE:
      case VI_ATTR_USB_INTR_IN_STATUS:
      case VI_ATTR_USB_NUM_INTFCS:
      case VI_ATTR_USB_NUM_PIPES:
      case VI_ATTR_USB_PROTOCOL:
      case VI_ATTR_USB_SUBCLASS:
      case VI_ATTR_VXI_LA:
      case VI_ATTR_VXI_VME_SYSFAIL_STATE:
        return AttributeValueData::kValueI16;

      case VI_ATTR_ASRL_DATA_BITS:
      case VI_ATTR_ASRL_END_IN:
      case VI_ATTR_ASRL_END_OUT:
      case VI_ATTR_ASRL_FLOW_CNTRL:
      case VI_ATTR_ASRL_PARITY:
      case VI_ATTR_ASRL_STOP_BITS:
      case VI_ATTR_DEST_ACCESS_PRIV:
      case VI_ATTR_DEST_BYTE_ORDER:
      case VI_ATTR_FDC_CHNL:
      case VI_ATTR_FDC_MODE:
      case VI_ATTR_FIREWIRE_DEST_UPPER_OFFSET:
      case VI_ATTR_FIREWIRE_SRC_UPPER_OFFSET:
      case VI_ATTR_FIREWIRE_WIN_UPPER_OFFSET:
      case VI_ATTR_GPIB_ADDR_STATE:
      case VI_ATTR_GPIB_PRIMARY_ADDR:
      case VI_ATTR_GPIB_SECONDARY_ADDR:
      case VI_ATTR_INTF_NUM:
      case VI_ATTR_INTF_PARENT_NUM:
      case VI_ATTR_INTF_TYPE:
      case VI_ATTR_IO_PROT:
      case VI_ATTR_MANF_ID:
      case VI_ATTR_MEM_SPACE:
      case VI_ATTR_MODEL_CODE:
      case VI_ATTR_PXI_BUS_NUM:
      case VI_ATTR_PXI_DEV_NUM:
      case VI_ATTR_PXI_FUNC_NUM:
      case VI_ATTR_PXI_MEM_TYPE_BAR0:
      case VI_ATTR_PXI_MEM_TYPE_BAR1:
      case VI_ATTR_PXI_MEM_TYPE_BAR2:
      case VI_ATTR_PXI_MEM_TYPE_BAR3:
      case VI_ATTR_PXI_MEM_TYPE_BAR4:
      case VI_ATTR_PXI_MEM_TYPE_BAR5:
      case VI_ATTR_PXI_SLOT_OFFSET:
      case VI_ATTR_PXI_SLOT_WIDTH:
      case VI_ATTR_RD_BUF_OPER_MODE:
      case VI_ATTR_RSRC_MANF_ID:
      case VI_ATTR_SIGP_STATUS_ID:
      case VI_ATTR_SRC_ACCESS_PRIV:
      case VI_ATTR_SRC_BYTE_ORDER:
      case VI_ATTR_TCPIP_PORT:
      case VI_ATTR_USB_END_IN:
      case VI_ATTR_USB_MAX_INTR_SIZE:
      case VI_ATTR_USB_RECV_INTR_SIZE:
      case VI_ATTR_VXI_DEV_CLASS:
      case VI_ATTR_VXI_TRIG_DIR:
      case VI_ATTR_VXI_TRIG_LINES_EN:
      case VI_ATTR_VXI_VME_INTR_STATUS:
      case VI_ATTR_WIN_ACCESS:
      case VI_ATTR_WIN_ACCESS_PRIV:
      case VI_ATTR_WIN_BYTE_ORDER:
      case VI_ATTR_WR_BUF_OPER_MODE:
        return AttributeValueData::kValueU16;

      case VI_ATTR_DEST_INCREMENT:
      case VI_ATTR_SRC_INCREMENT:
      case VI_ATTR_STATUS:
        return AttributeValueData::kValueI32;

      case VI_ATTR_ASRL_AVAIL_NUM:
      case VI_ATTR_ASRL_BAUD:
      case VI_ATTR_EVENT_TYPE:
      case VI_ATTR_FIREWIRE_LOWER_CHIP_ID:
      case VI_ATTR_FIREWIRE_VENDOR_ID:
      case VI_ATTR_INTR_STATUS_ID:
      case VI_ATTR_JOB_ID:
      case VI_ATTR_MAX_QUEUE_LENGTH:
      case VI_ATTR_MEM_BASE_32:
      case VI_ATTR_MEM_SIZE_32:
      case VI_ATTR_PXI_MEM_BASE_BAR0_32:
      case VI_ATTR_PXI_MEM_BASE_BAR1_32:
      case VI_ATTR_PXI_MEM_BASE_BAR2_32:
      case VI_ATTR_PXI_MEM_BASE_BAR3_32:
      case VI_ATTR_PXI_MEM_BASE_BAR4_32:
      case VI_ATTR_PXI_MEM_BASE_BAR5_32:
      case VI_ATTR_PXI_MEM_SIZE_BAR0_32:
      case VI_ATTR_PXI_MEM_SIZE_BAR1_32:
      case VI_ATTR_PXI_MEM_SIZE_BAR2_32:
      case VI_ATTR_PXI_MEM_SIZE_BAR3_32:
      case VI_ATTR_PXI_MEM_SIZE_BAR4_32:
      case VI_ATTR_PXI_MEM_SIZE_BAR5_32:
      case VI_ATTR_PXI_RECV_INTR_DATA:
      case VI_ATTR_RD_BUF_SIZE:
      case VI_ATTR_RET_COUNT_32:
      case VI_ATTR_RSRC_IMPL_VERSION:
      case VI_ATTR_RSRC_LOCK_STATE:
      case VI_ATTR_RSRC_SPEC_VERSION:
      case VI_ATTR_TCPIP_HISLIP_MAX_MESSAGE_KB:
      case VI_ATTR_TCPIP_HISLIP_VERSION:
      case VI_ATTR_TCPIP_SERVER_CERT_SIZE:
      case VI_ATTR_TMO_VALUE:
      case VI_ATTR_VXI_TRIG_STATUS:
      case VI_ATTR_VXI_TRIG_SUPPORT:
      case VI_ATTR_WIN_BASE_ADDR_32:
      case VI_ATTR_WIN_SIZE_32:
      case VI_ATTR_WR_BUF_SIZE:
        return AttributeValueData::kValueU32;

      case VI_ATTR_MEM_BASE_64:
      case VI_ATTR_MEM_SIZE_64:
      case VI_ATTR_PXI_MEM_BASE_BAR0_64:
      case VI_ATTR_PXI_MEM_BASE_BAR1_64:
      case VI_ATTR_PXI_MEM_BASE_BAR2_64:
      case VI_ATTR_PXI_MEM_BASE_BAR3_64:
      case VI_ATTR_PXI_MEM_BASE_BAR4_64:
      case VI_ATTR_PXI_MEM_BASE_BAR5_64:
      case VI_ATTR_PXI_MEM_SIZE_BAR0_64:
      case VI_ATTR_PXI_MEM_SIZE_BAR1_64:
      case VI_ATTR_PXI_MEM_SIZE_BAR2_64:
      case VI_ATTR_PXI_MEM_SIZE_BAR3_64:
      case VI_ATTR_PXI_MEM_SIZE_BAR4_64:
      case VI_ATTR_PXI_MEM_SIZE_BAR5_64:
      case VI_ATTR_RET_COUNT_64:
      case VI_ATTR_USER_DATA:
      case VI_ATTR_WIN_BASE_ADDR_64:
      case VI_ATTR_WIN_SIZE_64:
        return AttributeValueData::kValueU64;

      case VI_ATTR_4882_COMPLIANT:
      case VI_ATTR_ASRL_ALLOW_TRANSMIT:
      case VI_ATTR_ASRL_CONNECTED:
      case VI_ATTR_ASRL_DISCARD_NULL:
      case VI_ATTR_DMA_ALLOW_EN:
      case VI_ATTR_FDC_USE_PAIR:
      case VI_ATTR_FILE_APPEND_EN:
      case VI_ATTR_GPIB_CIC_STATE:
      case VI_ATTR_GPIB_READDR_EN:
      case VI_ATTR_GPIB_RECV_CIC_STATE:
      case VI_ATTR_GPIB_SYS_CNTRL_STATE:
      case VI_ATTR_GPIB_UNADDR_EN:
      case VI_ATTR_IMMEDIATE_SERV:
      case VI_ATTR_PXI_ALLOW_WRITE_COMBINE:
      case VI_ATTR_PXI_IS_EXPRESS:
      case VI_ATTR_SEND_END_EN:
      case VI_ATTR_SUPPRESS_END_EN:
      case VI_ATTR_TCPIP_HISLIP_ENCRYPTION_EN:
      case VI_ATTR_TCPIP_HISLIP_OVERLAP_EN:
      case VI_ATTR_TCPIP_IS_HISLIP:
      case VI_ATTR_TCPIP_KEEPALIVE:
      case VI_ATTR_TCPIP_NODELAY:
      case VI_ATTR_TCPIP_SERVER_CERT_IS_PERPETUAL:
      case VI_ATTR_TERMCHAR_EN:
        return AttributeValueData::kValueBool;

      case VI_ATTR_INTF_INST_NAME:
      case VI_ATTR_MANF_NAME:
      case VI_ATTR_MODEL_NAME:
      case VI_ATTR_OPER_NAME:
      case VI_ATTR_PXI_SLOTPATH:
      case VI_ATTR_RECV_TCPIP_ADDR:
      case VI_ATTR_RSRC_CLASS:
      case VI_ATTR_RSRC_MANF_NAME:
      case VI_ATTR_RSRC_NAME:
      case VI_ATTR_TCPIP_ADDR:
      case VI_ATTR_TCPIP_DEVICE_NAME:
      case VI_ATTR_TCPIP_HOSTNAME:
      case VI_ATTR_TCPIP_SASL_MECHANISM:
      case VI_ATTR_TCPIP_SERVER_CERT_EXPIRATION_DATE:
      case VI_ATTR_TCPIP_SERVER_CERT_ISSUER_NAME:
      case VI_ATTR_TCPIP_SERVER_CERT_SUBJECT_NAME:
      case VI_ATTR_TCPIP_TLS_CIPHER_SUITE:
      case VI_ATTR_USB_SERIAL_NUM:
        return AttributeValueData::kValueString;

      case VI_ATTR_BUFFER:
      case VI_ATTR_TCPIP_SERVER_CERT:
      case VI_ATTR_USB_RECV_INTR_DATA:
        return AttributeValueData::kValueBytes;

      default:
        return AttributeValueData::DATA_NOT_SET;
      }
  }
}

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_client.cpp sha256=4af1d522247ac8425f75a420baa07ca19bc5b984d61d5641808f2db290abb7be bytes=44682 -->
## FILE: generated/visa/visa_client.cpp

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_client.cpp`
- sha256: `4af1d522247ac8425f75a420baa07ca19bc5b984d61d5641808f2db290abb7be`
- bytes: 44682

````cpp

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// EXPERIMENTAL Client convenience wrapper for VISA.
//---------------------------------------------------------------------
#include "visa_client.h"

#include <grpcpp/grpcpp.h>

#include <visa.grpc.pb.h>

#include <cstdint>
#include <memory>
#include <stdexcept>
#include <vector>

namespace visa_grpc::experimental::client {

AssertIntrSignalResponse
assert_intr_signal(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AssertInterruptSignalMode, pb::int32>& mode, const pb::uint32& status_id)
{
  ::grpc::ClientContext context;

  auto request = AssertIntrSignalRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto mode_ptr = mode.get_if<AssertInterruptSignalMode>();
  const auto mode_raw_ptr = mode.get_if<pb::int32>();
  if (mode_ptr) {
    request.set_mode(*mode_ptr);
  }
  else if (mode_raw_ptr) {
    request.set_mode_raw(*mode_raw_ptr);
  }
  request.set_status_id(status_id);

  auto response = AssertIntrSignalResponse{};

  raise_if_error(
      stub->AssertIntrSignal(&context, request, &response),
      context);

  return response;
}

AssertTriggerResponse
assert_trigger(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<TriggerProtocol, pb::uint32>& protocol)
{
  ::grpc::ClientContext context;

  auto request = AssertTriggerRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto protocol_ptr = protocol.get_if<TriggerProtocol>();
  const auto protocol_raw_ptr = protocol.get_if<pb::uint32>();
  if (protocol_ptr) {
    request.set_protocol(*protocol_ptr);
  }
  else if (protocol_raw_ptr) {
    request.set_protocol_raw(*protocol_raw_ptr);
  }

  auto response = AssertTriggerResponse{};

  raise_if_error(
      stub->AssertTrigger(&context, request, &response),
      context);

  return response;
}

AssertUtilSignalResponse
assert_util_signal(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AssertUtilSignalMode, pb::uint32>& mode)
{
  ::grpc::ClientContext context;

  auto request = AssertUtilSignalRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto mode_ptr = mode.get_if<AssertUtilSignalMode>();
  const auto mode_raw_ptr = mode.get_if<pb::uint32>();
  if (mode_ptr) {
    request.set_mode(*mode_ptr);
  }
  else if (mode_raw_ptr) {
    request.set_mode_raw(*mode_raw_ptr);
  }

  auto response = AssertUtilSignalResponse{};

  raise_if_error(
      stub->AssertUtilSignal(&context, request, &response),
      context);

  return response;
}

ClearResponse
clear(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = ClearRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = ClearResponse{};

  raise_if_error(
      stub->Clear(&context, request, &response),
      context);

  return response;
}

CloseResponse
close(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = CloseRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = CloseResponse{};

  raise_if_error(
      stub->Close(&context, request, &response),
      context);

  return response;
}

CloseEventResponse
close_event(const StubPtr& stub, const pb::uint32& event_handle)
{
  ::grpc::ClientContext context;

  auto request = CloseEventRequest{};
  request.set_event_handle(event_handle);

  auto response = CloseEventResponse{};

  raise_if_error(
      stub->CloseEvent(&context, request, &response),
      context);

  return response;
}

DisableEventResponse
disable_event(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<EventType, pb::uint32>& event_type, const simple_variant<EventMechanism, pb::uint32>& event_mechanism)
{
  ::grpc::ClientContext context;

  auto request = DisableEventRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto event_type_ptr = event_type.get_if<EventType>();
  const auto event_type_raw_ptr = event_type.get_if<pb::uint32>();
  if (event_type_ptr) {
    request.set_event_type(*event_type_ptr);
  }
  else if (event_type_raw_ptr) {
    request.set_event_type_raw(*event_type_raw_ptr);
  }
  const auto event_mechanism_ptr = event_mechanism.get_if<EventMechanism>();
  const auto event_mechanism_raw_ptr = event_mechanism.get_if<pb::uint32>();
  if (event_mechanism_ptr) {
    request.set_event_mechanism(*event_mechanism_ptr);
  }
  else if (event_mechanism_raw_ptr) {
    request.set_event_mechanism_raw(*event_mechanism_raw_ptr);
  }

  auto response = DisableEventResponse{};

  raise_if_error(
      stub->DisableEvent(&context, request, &response),
      context);

  return response;
}

DiscardEventsResponse
discard_events(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<EventType, pb::uint32>& event_type, const simple_variant<EventMechanism, pb::uint32>& event_mechanism)
{
  ::grpc::ClientContext context;

  auto request = DiscardEventsRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto event_type_ptr = event_type.get_if<EventType>();
  const auto event_type_raw_ptr = event_type.get_if<pb::uint32>();
  if (event_type_ptr) {
    request.set_event_type(*event_type_ptr);
  }
  else if (event_type_raw_ptr) {
    request.set_event_type_raw(*event_type_raw_ptr);
  }
  const auto event_mechanism_ptr = event_mechanism.get_if<EventMechanism>();
  const auto event_mechanism_raw_ptr = event_mechanism.get_if<pb::uint32>();
  if (event_mechanism_ptr) {
    request.set_event_mechanism(*event_mechanism_ptr);
  }
  else if (event_mechanism_raw_ptr) {
    request.set_event_mechanism_raw(*event_mechanism_raw_ptr);
  }

  auto response = DiscardEventsResponse{};

  raise_if_error(
      stub->DiscardEvents(&context, request, &response),
      context);

  return response;
}

EnableEventResponse
enable_event(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<EventType, pb::uint32>& event_type, const simple_variant<EventMechanism, pb::uint32>& event_mechanism, const pb::uint32& filter_context)
{
  ::grpc::ClientContext context;

  auto request = EnableEventRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto event_type_ptr = event_type.get_if<EventType>();
  const auto event_type_raw_ptr = event_type.get_if<pb::uint32>();
  if (event_type_ptr) {
    request.set_event_type(*event_type_ptr);
  }
  else if (event_type_raw_ptr) {
    request.set_event_type_raw(*event_type_raw_ptr);
  }
  const auto event_mechanism_ptr = event_mechanism.get_if<EventMechanism>();
  const auto event_mechanism_raw_ptr = event_mechanism.get_if<pb::uint32>();
  if (event_mechanism_ptr) {
    request.set_event_mechanism(*event_mechanism_ptr);
  }
  else if (event_mechanism_raw_ptr) {
    request.set_event_mechanism_raw(*event_mechanism_raw_ptr);
  }
  request.set_filter_context(filter_context);

  auto response = EnableEventResponse{};

  raise_if_error(
      stub->EnableEvent(&context, request, &response),
      context);

  return response;
}

FindRsrcResponse
find_rsrc(const StubPtr& stub, const std::string& expression)
{
  ::grpc::ClientContext context;

  auto request = FindRsrcRequest{};
  request.set_expression(expression);

  auto response = FindRsrcResponse{};

  raise_if_error(
      stub->FindRsrc(&context, request, &response),
      context);

  return response;
}

FlushResponse
flush(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<BufferMask, pb::uint32>& mask)
{
  ::grpc::ClientContext context;

  auto request = FlushRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto mask_ptr = mask.get_if<BufferMask>();
  const auto mask_raw_ptr = mask.get_if<pb::uint32>();
  if (mask_ptr) {
    request.set_mask(*mask_ptr);
  }
  else if (mask_raw_ptr) {
    request.set_mask_raw(*mask_raw_ptr);
  }

  auto response = FlushResponse{};

  raise_if_error(
      stub->Flush(&context, request, &response),
      context);

  return response;
}

GetAttributeResponse
get_attribute(const StubPtr& stub, const nidevice_grpc::Session& vi, const VisaAttribute& attribute_name)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_attribute_name(attribute_name);

  auto response = GetAttributeResponse{};

  raise_if_error(
      stub->GetAttribute(&context, request, &response),
      context);

  return response;
}

GetAttributeEventResponse
get_attribute_event(const StubPtr& stub, const pb::uint32& event_handle, const VisaAttribute& attribute_name)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeEventRequest{};
  request.set_event_handle(event_handle);
  request.set_attribute_name(attribute_name);

  auto response = GetAttributeEventResponse{};

  raise_if_error(
      stub->GetAttributeEvent(&context, request, &response),
      context);

  return response;
}

GpibCommandResponse
gpib_command(const StubPtr& stub, const nidevice_grpc::Session& vi, const std::string& buffer)
{
  ::grpc::ClientContext context;

  auto request = GpibCommandRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_buffer(buffer);

  auto response = GpibCommandResponse{};

  raise_if_error(
      stub->GpibCommand(&context, request, &response),
      context);

  return response;
}

GpibControlATNResponse
gpib_control_atn(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<GpibControlAtnMode, pb::uint32>& mode)
{
  ::grpc::ClientContext context;

  auto request = GpibControlATNRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto mode_ptr = mode.get_if<GpibControlAtnMode>();
  const auto mode_raw_ptr = mode.get_if<pb::uint32>();
  if (mode_ptr) {
    request.set_mode(*mode_ptr);
  }
  else if (mode_raw_ptr) {
    request.set_mode_raw(*mode_raw_ptr);
  }

  auto response = GpibControlATNResponse{};

  raise_if_error(
      stub->GpibControlATN(&context, request, &response),
      context);

  return response;
}

GpibControlRENResponse
gpib_control_ren(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<GpibControlRenMode, pb::uint32>& mode)
{
  ::grpc::ClientContext context;

  auto request = GpibControlRENRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto mode_ptr = mode.get_if<GpibControlRenMode>();
  const auto mode_raw_ptr = mode.get_if<pb::uint32>();
  if (mode_ptr) {
    request.set_mode(*mode_ptr);
  }
  else if (mode_raw_ptr) {
    request.set_mode_raw(*mode_raw_ptr);
  }

  auto response = GpibControlRENResponse{};

  raise_if_error(
      stub->GpibControlREN(&context, request, &response),
      context);

  return response;
}

GpibPassControlResponse
gpib_pass_control(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint32& primary_address, const pb::uint32& secondary_address)
{
  ::grpc::ClientContext context;

  auto request = GpibPassControlRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_primary_address(primary_address);
  request.set_secondary_address(secondary_address);

  auto response = GpibPassControlResponse{};

  raise_if_error(
      stub->GpibPassControl(&context, request, &response),
      context);

  return response;
}

GpibSendIFCResponse
gpib_send_ifc(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = GpibSendIFCRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = GpibSendIFCResponse{};

  raise_if_error(
      stub->GpibSendIFC(&context, request, &response),
      context);

  return response;
}

In16Response
in16(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset)
{
  ::grpc::ClientContext context;

  auto request = In16Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);

  auto response = In16Response{};

  raise_if_error(
      stub->In16(&context, request, &response),
      context);

  return response;
}

In32Response
in32(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset)
{
  ::grpc::ClientContext context;

  auto request = In32Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);

  auto response = In32Response{};

  raise_if_error(
      stub->In32(&context, request, &response),
      context);

  return response;
}

In64Response
in64(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset)
{
  ::grpc::ClientContext context;

  auto request = In64Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);

  auto response = In64Response{};

  raise_if_error(
      stub->In64(&context, request, &response),
      context);

  return response;
}

In8Response
in8(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset)
{
  ::grpc::ClientContext context;

  auto request = In8Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);

  auto response = In8Response{};

  raise_if_error(
      stub->In8(&context, request, &response),
      context);

  return response;
}

LockResponse
lock(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<LockState, pb::uint32>& lock_type, const pb::uint32& timeout, const std::string& requested_key)
{
  ::grpc::ClientContext context;

  auto request = LockRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto lock_type_ptr = lock_type.get_if<LockState>();
  const auto lock_type_raw_ptr = lock_type.get_if<pb::uint32>();
  if (lock_type_ptr) {
    request.set_lock_type(*lock_type_ptr);
  }
  else if (lock_type_raw_ptr) {
    request.set_lock_type_raw(*lock_type_raw_ptr);
  }
  request.set_timeout(timeout);
  request.set_requested_key(requested_key);

  auto response = LockResponse{};

  raise_if_error(
      stub->Lock(&context, request, &response),
      context);

  return response;
}

MapAddressResponse
map_address(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& map_size, const bool& owner_access, const pb::uint64& suggested_address)
{
  ::grpc::ClientContext context;

  auto request = MapAddressRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  request.set_map_size(map_size);
  request.set_owner_access(owner_access);
  request.set_suggested_address(suggested_address);

  auto response = MapAddressResponse{};

  raise_if_error(
      stub->MapAddress(&context, request, &response),
      context);

  return response;
}

MapTriggerResponse
map_trigger(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<TriggerLine, pb::int32>& trigger_source, const simple_variant<TriggerLine, pb::int32>& trigger_destination, const pb::uint32& mode)
{
  ::grpc::ClientContext context;

  auto request = MapTriggerRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto trigger_source_ptr = trigger_source.get_if<TriggerLine>();
  const auto trigger_source_raw_ptr = trigger_source.get_if<pb::int32>();
  if (trigger_source_ptr) {
    request.set_trigger_source(*trigger_source_ptr);
  }
  else if (trigger_source_raw_ptr) {
    request.set_trigger_source_raw(*trigger_source_raw_ptr);
  }
  const auto trigger_destination_ptr = trigger_destination.get_if<TriggerLine>();
  const auto trigger_destination_raw_ptr = trigger_destination.get_if<pb::int32>();
  if (trigger_destination_ptr) {
    request.set_trigger_destination(*trigger_destination_ptr);
  }
  else if (trigger_destination_raw_ptr) {
    request.set_trigger_destination_raw(*trigger_destination_raw_ptr);
  }
  request.set_mode(mode);

  auto response = MapTriggerResponse{};

  raise_if_error(
      stub->MapTrigger(&context, request, &response),
      context);

  return response;
}

MemAllocResponse
mem_alloc(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint32& size)
{
  ::grpc::ClientContext context;

  auto request = MemAllocRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_size(size);

  auto response = MemAllocResponse{};

  raise_if_error(
      stub->MemAlloc(&context, request, &response),
      context);

  return response;
}

MemAllocExResponse
mem_alloc_ex(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& size)
{
  ::grpc::ClientContext context;

  auto request = MemAllocExRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_size(size);

  auto response = MemAllocExResponse{};

  raise_if_error(
      stub->MemAllocEx(&context, request, &response),
      context);

  return response;
}

MemFreeResponse
mem_free(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& offset)
{
  ::grpc::ClientContext context;

  auto request = MemFreeRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_offset(offset);

  auto response = MemFreeResponse{};

  raise_if_error(
      stub->MemFree(&context, request, &response),
      context);

  return response;
}

MoveIn16Response
move_in16(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& count)
{
  ::grpc::ClientContext context;

  auto request = MoveIn16Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  request.set_count(count);

  auto response = MoveIn16Response{};

  raise_if_error(
      stub->MoveIn16(&context, request, &response),
      context);

  return response;
}

MoveIn32Response
move_in32(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& count)
{
  ::grpc::ClientContext context;

  auto request = MoveIn32Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  request.set_count(count);

  auto response = MoveIn32Response{};

  raise_if_error(
      stub->MoveIn32(&context, request, &response),
      context);

  return response;
}

MoveIn64Response
move_in64(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& count)
{
  ::grpc::ClientContext context;

  auto request = MoveIn64Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  request.set_count(count);

  auto response = MoveIn64Response{};

  raise_if_error(
      stub->MoveIn64(&context, request, &response),
      context);

  return response;
}

MoveIn8Response
move_in8(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& count)
{
  ::grpc::ClientContext context;

  auto request = MoveIn8Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  request.set_count(count);

  auto response = MoveIn8Response{};

  raise_if_error(
      stub->MoveIn8(&context, request, &response),
      context);

  return response;
}

MoveOut16Response
move_out16(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const std::vector<pb::uint32>& buffer)
{
  ::grpc::ClientContext context;

  auto request = MoveOut16Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  copy_array(buffer, request.mutable_buffer());

  auto response = MoveOut16Response{};

  raise_if_error(
      stub->MoveOut16(&context, request, &response),
      context);

  return response;
}

MoveOut32Response
move_out32(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const std::vector<pb::uint32>& buffer)
{
  ::grpc::ClientContext context;

  auto request = MoveOut32Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  copy_array(buffer, request.mutable_buffer());

  auto response = MoveOut32Response{};

  raise_if_error(
      stub->MoveOut32(&context, request, &response),
      context);

  return response;
}

MoveOut64Response
move_out64(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const std::vector<pb::uint64>& buffer)
{
  ::grpc::ClientContext context;

  auto request = MoveOut64Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  copy_array(buffer, request.mutable_buffer());

  auto response = MoveOut64Response{};

  raise_if_error(
      stub->MoveOut64(&context, request, &response),
      context);

  return response;
}

MoveOut8Response
move_out8(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const std::string& buffer)
{
  ::grpc::ClientContext context;

  auto request = MoveOut8Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  request.set_buffer(buffer);

  auto response = MoveOut8Response{};

  raise_if_error(
      stub->MoveOut8(&context, request, &response),
      context);

  return response;
}

OpenResponse
open(const StubPtr& stub, const std::string& instrument_descriptor, const simple_variant<LockState, pb::uint32>& access_mode, const pb::uint32& open_timeout, const nidevice_grpc::SessionInitializationBehavior& initialization_behavior)
{
  ::grpc::ClientContext context;

  auto request = OpenRequest{};
  request.set_instrument_descriptor(instrument_descriptor);
  const auto access_mode_ptr = access_mode.get_if<LockState>();
  const auto access_mode_raw_ptr = access_mode.get_if<pb::uint32>();
  if (access_mode_ptr) {
    request.set_access_mode(*access_mode_ptr);
  }
  else if (access_mode_raw_ptr) {
    request.set_access_mode_raw(*access_mode_raw_ptr);
  }
  request.set_open_timeout(open_timeout);
  request.set_initialization_behavior(initialization_behavior);

  auto response = OpenResponse{};

  raise_if_error(
      stub->Open(&context, request, &response),
      context);

  return response;
}

Out16Response
out16(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint32& value)
{
  ::grpc::ClientContext context;

  auto request = Out16Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  request.set_value(value);

  auto response = Out16Response{};

  raise_if_error(
      stub->Out16(&context, request, &response),
      context);

  return response;
}

Out32Response
out32(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint32& value)
{
  ::grpc::ClientContext context;

  auto request = Out32Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  request.set_value(value);

  auto response = Out32Response{};

  raise_if_error(
      stub->Out32(&context, request, &response),
      context);

  return response;
}

Out64Response
out64(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& value)
{
  ::grpc::ClientContext context;

  auto request = Out64Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  request.set_value(value);

  auto response = Out64Response{};

  raise_if_error(
      stub->Out64(&context, request, &response),
      context);

  return response;
}

Out8Response
out8(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint32& value)
{
  ::grpc::ClientContext context;

  auto request = Out8Request{};
  request.mutable_vi()->CopyFrom(vi);
  const auto address_space_ptr = address_space.get_if<AddressSpace>();
  const auto address_space_raw_ptr = address_space.get_if<pb::uint32>();
  if (address_space_ptr) {
    request.set_address_space(*address_space_ptr);
  }
  else if (address_space_raw_ptr) {
    request.set_address_space_raw(*address_space_raw_ptr);
  }
  request.set_offset(offset);
  request.set_value(value);

  auto response = Out8Response{};

  raise_if_error(
      stub->Out8(&context, request, &response),
      context);

  return response;
}

ParseRsrcResponse
parse_rsrc(const StubPtr& stub, const std::string& resource_name)
{
  ::grpc::ClientContext context;

  auto request = ParseRsrcRequest{};
  request.set_resource_name(resource_name);

  auto response = ParseRsrcResponse{};

  raise_if_error(
      stub->ParseRsrc(&context, request, &response),
      context);

  return response;
}

Peek16Response
peek16(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address)
{
  ::grpc::ClientContext context;

  auto request = Peek16Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_address(address);

  auto response = Peek16Response{};

  raise_if_error(
      stub->Peek16(&context, request, &response),
      context);

  return response;
}

Peek32Response
peek32(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address)
{
  ::grpc::ClientContext context;

  auto request = Peek32Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_address(address);

  auto response = Peek32Response{};

  raise_if_error(
      stub->Peek32(&context, request, &response),
      context);

  return response;
}

Peek64Response
peek64(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address)
{
  ::grpc::ClientContext context;

  auto request = Peek64Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_address(address);

  auto response = Peek64Response{};

  raise_if_error(
      stub->Peek64(&context, request, &response),
      context);

  return response;
}

Peek8Response
peek8(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address)
{
  ::grpc::ClientContext context;

  auto request = Peek8Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_address(address);

  auto response = Peek8Response{};

  raise_if_error(
      stub->Peek8(&context, request, &response),
      context);

  return response;
}

Poke16Response
poke16(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address, const pb::uint32& value)
{
  ::grpc::ClientContext context;

  auto request = Poke16Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_address(address);
  request.set_value(value);

  auto response = Poke16Response{};

  raise_if_error(
      stub->Poke16(&context, request, &response),
      context);

  return response;
}

Poke32Response
poke32(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address, const pb::uint32& value)
{
  ::grpc::ClientContext context;

  auto request = Poke32Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_address(address);
  request.set_value(value);

  auto response = Poke32Response{};

  raise_if_error(
      stub->Poke32(&context, request, &response),
      context);

  return response;
}

Poke64Response
poke64(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address, const pb::uint64& value)
{
  ::grpc::ClientContext context;

  auto request = Poke64Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_address(address);
  request.set_value(value);

  auto response = Poke64Response{};

  raise_if_error(
      stub->Poke64(&context, request, &response),
      context);

  return response;
}

Poke8Response
poke8(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address, const pb::uint32& value)
{
  ::grpc::ClientContext context;

  auto request = Poke8Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_address(address);
  request.set_value(value);

  auto response = Poke8Response{};

  raise_if_error(
      stub->Poke8(&context, request, &response),
      context);

  return response;
}

PxiReserveTriggersResponse
pxi_reserve_triggers(const StubPtr& stub, const nidevice_grpc::Session& vi, const std::vector<pb::int32>& trig_buses, const std::vector<pb::int32>& trig_lines)
{
  ::grpc::ClientContext context;

  auto request = PxiReserveTriggersRequest{};
  request.mutable_vi()->CopyFrom(vi);
  copy_array(trig_buses, request.mutable_trig_buses());
  copy_array(trig_lines, request.mutable_trig_lines());

  auto response = PxiReserveTriggersResponse{};

  raise_if_error(
      stub->PxiReserveTriggers(&context, request, &response),
      context);

  return response;
}

ReadResponse
read(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint32& count)
{
  ::grpc::ClientContext context;

  auto request = ReadRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_count(count);

  auto response = ReadResponse{};

  raise_if_error(
      stub->Read(&context, request, &response),
      context);

  return response;
}

ReadAsyncResponse
read_async(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint32& count)
{
  ::grpc::ClientContext context;

  auto request = ReadAsyncRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_count(count);

  auto response = ReadAsyncResponse{};

  raise_if_error(
      stub->ReadAsync(&context, request, &response),
      context);

  return response;
}

ReadSTBResponse
read_stb(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = ReadSTBRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = ReadSTBResponse{};

  raise_if_error(
      stub->ReadSTB(&context, request, &response),
      context);

  return response;
}

SetAttributeResponse
set_attribute(const StubPtr& stub, const nidevice_grpc::Session& vi, const VisaAttribute& attribute_name, const AttributeValueData& attribute_value)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_attribute_name(attribute_name);
  request.mutable_attribute_value()->CopyFrom(attribute_value);

  auto response = SetAttributeResponse{};

  raise_if_error(
      stub->SetAttribute(&context, request, &response),
      context);

  return response;
}

SetBufResponse
set_buf(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<BufferMask, pb::uint32>& mask, const pb::uint32& buffer_size)
{
  ::grpc::ClientContext context;

  auto request = SetBufRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto mask_ptr = mask.get_if<BufferMask>();
  const auto mask_raw_ptr = mask.get_if<pb::uint32>();
  if (mask_ptr) {
    request.set_mask(*mask_ptr);
  }
  else if (mask_raw_ptr) {
    request.set_mask_raw(*mask_raw_ptr);
  }
  request.set_buffer_size(buffer_size);

  auto response = SetBufResponse{};

  raise_if_error(
      stub->SetBuf(&context, request, &response),
      context);

  return response;
}

StatusDescResponse
status_desc(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::int32& status_value)
{
  ::grpc::ClientContext context;

  auto request = StatusDescRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_status_value(status_value);

  auto response = StatusDescResponse{};

  raise_if_error(
      stub->StatusDesc(&context, request, &response),
      context);

  return response;
}

TerminateResponse
terminate(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint32& degree, const pb::uint32& job_identifier)
{
  ::grpc::ClientContext context;

  auto request = TerminateRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_degree(degree);
  request.set_job_identifier(job_identifier);

  auto response = TerminateResponse{};

  raise_if_error(
      stub->Terminate(&context, request, &response),
      context);

  return response;
}

UnlockResponse
unlock(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = UnlockRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = UnlockResponse{};

  raise_if_error(
      stub->Unlock(&context, request, &response),
      context);

  return response;
}

UnmapAddressResponse
unmap_address(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = UnmapAddressRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = UnmapAddressResponse{};

  raise_if_error(
      stub->UnmapAddress(&context, request, &response),
      context);

  return response;
}

UnmapTriggerResponse
unmap_trigger(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<TriggerLine, pb::int32>& trigger_source, const simple_variant<TriggerLine, pb::int32>& trigger_destination)
{
  ::grpc::ClientContext context;

  auto request = UnmapTriggerRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto trigger_source_ptr = trigger_source.get_if<TriggerLine>();
  const auto trigger_source_raw_ptr = trigger_source.get_if<pb::int32>();
  if (trigger_source_ptr) {
    request.set_trigger_source(*trigger_source_ptr);
  }
  else if (trigger_source_raw_ptr) {
    request.set_trigger_source_raw(*trigger_source_raw_ptr);
  }
  const auto trigger_destination_ptr = trigger_destination.get_if<TriggerLine>();
  const auto trigger_destination_raw_ptr = trigger_destination.get_if<pb::int32>();
  if (trigger_destination_ptr) {
    request.set_trigger_destination(*trigger_destination_ptr);
  }
  else if (trigger_destination_raw_ptr) {
    request.set_trigger_destination_raw(*trigger_destination_raw_ptr);
  }

  auto response = UnmapTriggerResponse{};

  raise_if_error(
      stub->UnmapTrigger(&context, request, &response),
      context);

  return response;
}

UsbControlInResponse
usb_control_in(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::int32& bm_request_type, const pb::int32& b_request, const pb::uint32& w_value, const pb::uint32& w_index, const pb::uint32& w_length)
{
  ::grpc::ClientContext context;

  auto request = UsbControlInRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_bm_request_type(bm_request_type);
  request.set_b_request(b_request);
  request.set_w_value(w_value);
  request.set_w_index(w_index);
  request.set_w_length(w_length);

  auto response = UsbControlInResponse{};

  raise_if_error(
      stub->UsbControlIn(&context, request, &response),
      context);

  return response;
}

UsbControlOutResponse
usb_control_out(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::int32& bm_request_type, const pb::int32& b_request, const pb::uint32& w_value, const pb::uint32& w_index, const std::string& buffer)
{
  ::grpc::ClientContext context;

  auto request = UsbControlOutRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_bm_request_type(bm_request_type);
  request.set_b_request(b_request);
  request.set_w_value(w_value);
  request.set_w_index(w_index);
  request.set_buffer(buffer);

  auto response = UsbControlOutResponse{};

  raise_if_error(
      stub->UsbControlOut(&context, request, &response),
      context);

  return response;
}

VxiCommandQueryResponse
vxi_command_query(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<VxiCmdType, pb::uint32>& mode, const pb::uint32& command)
{
  ::grpc::ClientContext context;

  auto request = VxiCommandQueryRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto mode_ptr = mode.get_if<VxiCmdType>();
  const auto mode_raw_ptr = mode.get_if<pb::uint32>();
  if (mode_ptr) {
    request.set_mode(*mode_ptr);
  }
  else if (mode_raw_ptr) {
    request.set_mode_raw(*mode_raw_ptr);
  }
  request.set_command(command);

  auto response = VxiCommandQueryResponse{};

  raise_if_error(
      stub->VxiCommandQuery(&context, request, &response),
      context);

  return response;
}

WaitOnEventResponse
wait_on_event(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<EventType, pb::uint32>& in_event_type, const pb::uint32& timeout)
{
  ::grpc::ClientContext context;

  auto request = WaitOnEventRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto in_event_type_ptr = in_event_type.get_if<EventType>();
  const auto in_event_type_raw_ptr = in_event_type.get_if<pb::uint32>();
  if (in_event_type_ptr) {
    request.set_in_event_type(*in_event_type_ptr);
  }
  else if (in_event_type_raw_ptr) {
    request.set_in_event_type_raw(*in_event_type_raw_ptr);
  }
  request.set_timeout(timeout);

  auto response = WaitOnEventResponse{};

  raise_if_error(
      stub->WaitOnEvent(&context, request, &response),
      context);

  return response;
}

WriteResponse
write(const StubPtr& stub, const nidevice_grpc::Session& vi, const std::string& buffer)
{
  ::grpc::ClientContext context;

  auto request = WriteRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_buffer(buffer);

  auto response = WriteResponse{};

  raise_if_error(
      stub->Write(&context, request, &response),
      context);

  return response;
}

WriteAsyncResponse
write_async(const StubPtr& stub, const nidevice_grpc::Session& vi, const std::string& buffer)
{
  ::grpc::ClientContext context;

  auto request = WriteAsyncRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_buffer(buffer);

  auto response = WriteAsyncResponse{};

  raise_if_error(
      stub->WriteAsync(&context, request, &response),
      context);

  return response;
}


} // namespace visa_grpc::experimental::client
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_client.h sha256=e7adc07d591810ad6cfe1a96f79bff3c3f1cf9163a16becc13bc08fb13941eb2 bytes=11370 -->
## FILE: generated/visa/visa_client.h

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_client.h`
- sha256: `e7adc07d591810ad6cfe1a96f79bff3c3f1cf9163a16becc13bc08fb13941eb2`
- bytes: 11370

````c

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// EXPERIMENTAL Client convenience wrapper for VISA.
//---------------------------------------------------------------------
#ifndef VISA_GRPC_CLIENT_H
#define VISA_GRPC_CLIENT_H

#include <grpcpp/grpcpp.h>

#include <visa.grpc.pb.h>
#include <tests/utilities/client_helpers.h>

#include <memory>
#include <vector>

namespace visa_grpc::experimental::client {

namespace pb = ::google::protobuf;
using StubPtr = std::unique_ptr<Visa::Stub>;
using namespace nidevice_grpc::experimental::client;


AssertIntrSignalResponse assert_intr_signal(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AssertInterruptSignalMode, pb::int32>& mode, const pb::uint32& status_id);
AssertTriggerResponse assert_trigger(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<TriggerProtocol, pb::uint32>& protocol);
AssertUtilSignalResponse assert_util_signal(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AssertUtilSignalMode, pb::uint32>& mode);
ClearResponse clear(const StubPtr& stub, const nidevice_grpc::Session& vi);
CloseResponse close(const StubPtr& stub, const nidevice_grpc::Session& vi);
CloseEventResponse close_event(const StubPtr& stub, const pb::uint32& event_handle);
DisableEventResponse disable_event(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<EventType, pb::uint32>& event_type, const simple_variant<EventMechanism, pb::uint32>& event_mechanism);
DiscardEventsResponse discard_events(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<EventType, pb::uint32>& event_type, const simple_variant<EventMechanism, pb::uint32>& event_mechanism);
EnableEventResponse enable_event(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<EventType, pb::uint32>& event_type, const simple_variant<EventMechanism, pb::uint32>& event_mechanism, const pb::uint32& filter_context);
FindRsrcResponse find_rsrc(const StubPtr& stub, const std::string& expression);
FlushResponse flush(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<BufferMask, pb::uint32>& mask);
GetAttributeResponse get_attribute(const StubPtr& stub, const nidevice_grpc::Session& vi, const VisaAttribute& attribute_name);
GetAttributeEventResponse get_attribute_event(const StubPtr& stub, const pb::uint32& event_handle, const VisaAttribute& attribute_name);
GpibCommandResponse gpib_command(const StubPtr& stub, const nidevice_grpc::Session& vi, const std::string& buffer);
GpibControlATNResponse gpib_control_atn(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<GpibControlAtnMode, pb::uint32>& mode);
GpibControlRENResponse gpib_control_ren(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<GpibControlRenMode, pb::uint32>& mode);
GpibPassControlResponse gpib_pass_control(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint32& primary_address, const pb::uint32& secondary_address);
GpibSendIFCResponse gpib_send_ifc(const StubPtr& stub, const nidevice_grpc::Session& vi);
In16Response in16(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset);
In32Response in32(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset);
In64Response in64(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset);
In8Response in8(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset);
LockResponse lock(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<LockState, pb::uint32>& lock_type, const pb::uint32& timeout, const std::string& requested_key);
MapAddressResponse map_address(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& map_size, const bool& owner_access, const pb::uint64& suggested_address);
MapTriggerResponse map_trigger(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<TriggerLine, pb::int32>& trigger_source, const simple_variant<TriggerLine, pb::int32>& trigger_destination, const pb::uint32& mode);
MemAllocResponse mem_alloc(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint32& size);
MemAllocExResponse mem_alloc_ex(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& size);
MemFreeResponse mem_free(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& offset);
MoveIn16Response move_in16(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& count);
MoveIn32Response move_in32(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& count);
MoveIn64Response move_in64(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& count);
MoveIn8Response move_in8(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& count);
MoveOut16Response move_out16(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const std::vector<pb::uint32>& buffer);
MoveOut32Response move_out32(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const std::vector<pb::uint32>& buffer);
MoveOut64Response move_out64(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const std::vector<pb::uint64>& buffer);
MoveOut8Response move_out8(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const std::string& buffer);
OpenResponse open(const StubPtr& stub, const std::string& instrument_descriptor, const simple_variant<LockState, pb::uint32>& access_mode, const pb::uint32& open_timeout, const nidevice_grpc::SessionInitializationBehavior& initialization_behavior = nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED);
Out16Response out16(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint32& value);
Out32Response out32(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint32& value);
Out64Response out64(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint64& value);
Out8Response out8(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<AddressSpace, pb::uint32>& address_space, const pb::uint64& offset, const pb::uint32& value);
ParseRsrcResponse parse_rsrc(const StubPtr& stub, const std::string& resource_name);
Peek16Response peek16(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address);
Peek32Response peek32(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address);
Peek64Response peek64(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address);
Peek8Response peek8(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address);
Poke16Response poke16(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address, const pb::uint32& value);
Poke32Response poke32(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address, const pb::uint32& value);
Poke64Response poke64(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address, const pb::uint64& value);
Poke8Response poke8(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint64& address, const pb::uint32& value);
PxiReserveTriggersResponse pxi_reserve_triggers(const StubPtr& stub, const nidevice_grpc::Session& vi, const std::vector<pb::int32>& trig_buses, const std::vector<pb::int32>& trig_lines);
ReadResponse read(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint32& count);
ReadAsyncResponse read_async(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint32& count);
ReadSTBResponse read_stb(const StubPtr& stub, const nidevice_grpc::Session& vi);
SetAttributeResponse set_attribute(const StubPtr& stub, const nidevice_grpc::Session& vi, const VisaAttribute& attribute_name, const AttributeValueData& attribute_value);
SetBufResponse set_buf(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<BufferMask, pb::uint32>& mask, const pb::uint32& buffer_size);
StatusDescResponse status_desc(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::int32& status_value);
TerminateResponse terminate(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::uint32& degree, const pb::uint32& job_identifier);
UnlockResponse unlock(const StubPtr& stub, const nidevice_grpc::Session& vi);
UnmapAddressResponse unmap_address(const StubPtr& stub, const nidevice_grpc::Session& vi);
UnmapTriggerResponse unmap_trigger(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<TriggerLine, pb::int32>& trigger_source, const simple_variant<TriggerLine, pb::int32>& trigger_destination);
UsbControlInResponse usb_control_in(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::int32& bm_request_type, const pb::int32& b_request, const pb::uint32& w_value, const pb::uint32& w_index, const pb::uint32& w_length);
UsbControlOutResponse usb_control_out(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::int32& bm_request_type, const pb::int32& b_request, const pb::uint32& w_value, const pb::uint32& w_index, const std::string& buffer);
VxiCommandQueryResponse vxi_command_query(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<VxiCmdType, pb::uint32>& mode, const pb::uint32& command);
WaitOnEventResponse wait_on_event(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<EventType, pb::uint32>& in_event_type, const pb::uint32& timeout);
WriteResponse write(const StubPtr& stub, const nidevice_grpc::Session& vi, const std::string& buffer);
WriteAsyncResponse write_async(const StubPtr& stub, const nidevice_grpc::Session& vi, const std::string& buffer);

} // namespace visa_grpc::experimental::client

#endif /* VISA_GRPC_CLIENT_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_compilation_test.cpp sha256=6c1740f202d0c99cf631470d246fcafda621fdbe46d08fefa431e3995e2baef0 bytes=10569 -->
## FILE: generated/visa/visa_compilation_test.cpp

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_compilation_test.cpp`
- sha256: `6c1740f202d0c99cf631470d246fcafda621fdbe46d08fefa431e3995e2baef0`
- bytes: 10569

````cpp
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Compilation test for the VISA Metadata
//---------------------------------------------------------------------
#include "visa_library.h"

namespace visa_grpc {

ViStatus AssertIntrSignal(ViSession vi, ViInt16 mode, ViUInt32 statusId)
{
  return viAssertIntrSignal(vi, mode, statusId);
}

ViStatus AssertTrigger(ViSession vi, ViUInt16 protocol)
{
  return viAssertTrigger(vi, protocol);
}

ViStatus AssertUtilSignal(ViSession vi, ViUInt16 mode)
{
  return viAssertUtilSignal(vi, mode);
}

ViStatus Clear(ViSession vi)
{
  return viClear(vi);
}

ViStatus Close(ViSession vi)
{
  return viClose(vi);
}

ViStatus CloseEvent(ViEvent eventHandle)
{
  return viClose(eventHandle);
}

ViStatus DisableEvent(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism)
{
  return viDisableEvent(vi, eventType, eventMechanism);
}

ViStatus DiscardEvents(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism)
{
  return viDiscardEvents(vi, eventType, eventMechanism);
}

ViStatus EnableEvent(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism, ViEventFilter filterContext)
{
  return viEnableEvent(vi, eventType, eventMechanism, filterContext);
}

ViStatus FindRsrc(ViSession rsrcManagerHandle, ViConstString expression, ViFindList* findHandle, ViUInt32* returnCount, ViChar instrumentDescriptor[256])
{
  return viFindRsrc(rsrcManagerHandle, expression, findHandle, returnCount, instrumentDescriptor);
}

ViStatus Flush(ViSession vi, ViUInt16 mask)
{
  return viFlush(vi, mask);
}

ViStatus GetAttribute(ViSession vi, ViAttr attributeName, void* attributeValue)
{
  return viGetAttribute(vi, attributeName, attributeValue);
}

ViStatus GetAttributeEvent(ViEvent eventHandle, ViAttr attributeName, void* attributeValue)
{
  return viGetAttribute(eventHandle, attributeName, attributeValue);
}

ViStatus GpibCommand(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount)
{
  return viGpibCommand(vi, buffer, count, returnCount);
}

ViStatus GpibControlATN(ViSession vi, ViUInt16 mode)
{
  return viGpibControlATN(vi, mode);
}

ViStatus GpibControlREN(ViSession vi, ViUInt16 mode)
{
  return viGpibControlREN(vi, mode);
}

ViStatus GpibPassControl(ViSession vi, ViUInt16 primaryAddress, ViUInt16 secondaryAddress)
{
  return viGpibPassControl(vi, primaryAddress, secondaryAddress);
}

ViStatus GpibSendIFC(ViSession vi)
{
  return viGpibSendIFC(vi);
}

ViStatus In16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt16* value)
{
  return viIn16Ex(vi, addressSpace, offset, value);
}

ViStatus In32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt32* value)
{
  return viIn32Ex(vi, addressSpace, offset, value);
}

ViStatus In64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt64* value)
{
  return viIn64Ex(vi, addressSpace, offset, value);
}

ViStatus In8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt8* value)
{
  return viIn8Ex(vi, addressSpace, offset, value);
}

ViStatus Lock(ViSession vi, ViAccessMode lockType, ViUInt32 timeout, ViConstKeyId requestedKey, ViChar accessKey[256])
{
  return viLock(vi, lockType, timeout, requestedKey, accessKey);
}

ViStatus MapAddress(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize mapSize, ViBoolean ownerAccess, ViAddr suggestedAddress, ViAddr* address)
{
  return viMapAddressEx(vi, addressSpace, offset, mapSize, ownerAccess, suggestedAddress, address);
}

ViStatus MapTrigger(ViSession vi, ViInt16 triggerSource, ViInt16 triggerDestination, ViUInt16 mode)
{
  return viMapTrigger(vi, triggerSource, triggerDestination, mode);
}

ViStatus MemAlloc(ViSession vi, ViUInt32 size, ViBusAddress* offset)
{
  return viMemAlloc(vi, size, offset);
}

ViStatus MemAllocEx(ViSession vi, ViBusSize size, ViBusAddress64* offset)
{
  return viMemAllocEx(vi, size, offset);
}

ViStatus MemFree(ViSession vi, ViBusAddress64 offset)
{
  return viMemFreeEx(vi, offset);
}

ViStatus MoveIn16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt16 buffer[])
{
  return viMoveIn16Ex(vi, addressSpace, offset, count, buffer);
}

ViStatus MoveIn32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt32 buffer[])
{
  return viMoveIn32Ex(vi, addressSpace, offset, count, buffer);
}

ViStatus MoveIn64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt64 buffer[])
{
  return viMoveIn64Ex(vi, addressSpace, offset, count, buffer);
}

ViStatus MoveIn8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt8 buffer[])
{
  return viMoveIn8Ex(vi, addressSpace, offset, count, buffer);
}

ViStatus MoveOut16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt16 buffer[])
{
  return viMoveOut16Ex(vi, addressSpace, offset, count, buffer);
}

ViStatus MoveOut32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt32 buffer[])
{
  return viMoveOut32Ex(vi, addressSpace, offset, count, buffer);
}

ViStatus MoveOut64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt64 buffer[])
{
  return viMoveOut64Ex(vi, addressSpace, offset, count, buffer);
}

ViStatus MoveOut8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt8 buffer[])
{
  return viMoveOut8Ex(vi, addressSpace, offset, count, buffer);
}

ViStatus Open(ViSession rsrcManagerHandle, ViConstRsrc instrumentDescriptor, ViAccessMode accessMode, ViUInt32 openTimeout, ViSession* vi)
{
  return viOpen(rsrcManagerHandle, instrumentDescriptor, accessMode, openTimeout, vi);
}

ViStatus Out16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt16 value)
{
  return viOut16Ex(vi, addressSpace, offset, value);
}

ViStatus Out32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt32 value)
{
  return viOut32Ex(vi, addressSpace, offset, value);
}

ViStatus Out64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt64 value)
{
  return viOut64Ex(vi, addressSpace, offset, value);
}

ViStatus Out8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt8 value)
{
  return viOut8Ex(vi, addressSpace, offset, value);
}

ViStatus ParseRsrc(ViSession sessionHandle, ViConstRsrc resourceName, ViUInt16* interfaceType, ViUInt16* interfaceNumber, ViChar resourceClass[256], ViChar expandedUnaliasedName[256], ViChar aliasIfExists[256])
{
  return viParseRsrcEx(sessionHandle, resourceName, interfaceType, interfaceNumber, resourceClass, expandedUnaliasedName, aliasIfExists);
}

void Peek16(ViSession vi, ViAddr address, ViUInt16* value)
{
  return viPeek16(vi, address, value);
}

void Peek32(ViSession vi, ViAddr address, ViUInt32* value)
{
  return viPeek32(vi, address, value);
}

void Peek64(ViSession vi, ViAddr address, ViUInt64* value)
{
  return viPeek64(vi, address, value);
}

void Peek8(ViSession vi, ViAddr address, ViUInt8* value)
{
  return viPeek8(vi, address, value);
}

void Poke16(ViSession vi, ViAddr address, ViUInt16 value)
{
  return viPoke16(vi, address, value);
}

void Poke32(ViSession vi, ViAddr address, ViUInt32 value)
{
  return viPoke32(vi, address, value);
}

void Poke64(ViSession vi, ViAddr address, ViUInt64 value)
{
  return viPoke64(vi, address, value);
}

void Poke8(ViSession vi, ViAddr address, ViUInt8 value)
{
  return viPoke8(vi, address, value);
}

ViStatus PxiReserveTriggers(ViSession vi, ViInt16 cnt, ViInt16 trigBuses[], ViInt16 trigLines[], ViInt16* failureIndex)
{
  return viPxiReserveTriggers(vi, cnt, trigBuses, trigLines, failureIndex);
}

ViStatus Read(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount)
{
  return viRead(vi, buffer, count, returnCount);
}

ViStatus ReadAsync(ViSession vi, ViByte readBuffer[], ViUInt32 count, ViJobId* jobIdentifier)
{
  return viReadAsync(vi, readBuffer, count, jobIdentifier);
}

ViStatus ReadSTB(ViSession vi, ViUInt16* statusByte)
{
  return viReadSTB(vi, statusByte);
}

ViStatus SetAttribute(ViSession vi, ViAttr attributeName, ViAttrState attributeValue)
{
  return viSetAttribute(vi, attributeName, attributeValue);
}

ViStatus SetBuf(ViSession vi, ViUInt16 mask, ViUInt32 bufferSize)
{
  return viSetBuf(vi, mask, bufferSize);
}

ViStatus StatusDesc(ViSession vi, ViStatus statusValue, ViChar statusDescription[256])
{
  return viStatusDesc(vi, statusValue, statusDescription);
}

ViStatus Terminate(ViSession vi, ViUInt16 degree, ViJobId jobIdentifier)
{
  return viTerminate(vi, degree, jobIdentifier);
}

ViStatus Unlock(ViSession vi)
{
  return viUnlock(vi);
}

ViStatus UnmapAddress(ViSession vi)
{
  return viUnmapAddress(vi);
}

ViStatus UnmapTrigger(ViSession vi, ViInt16 triggerSource, ViInt16 triggerDestination)
{
  return viUnmapTrigger(vi, triggerSource, triggerDestination);
}

ViStatus UsbControlIn(ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest, ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength, ViByte buffer[], ViUInt16* returnCount)
{
  return viUsbControlIn(vi, bmRequestType, bRequest, wValue, wIndex, wLength, buffer, returnCount);
}

ViStatus UsbControlOut(ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest, ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength, ViByte buffer[])
{
  return viUsbControlOut(vi, bmRequestType, bRequest, wValue, wIndex, wLength, buffer);
}

ViStatus VxiCommandQuery(ViSession vi, ViUInt16 mode, ViUInt32 command, ViUInt32* commandResponse)
{
  return viVxiCommandQuery(vi, mode, command, commandResponse);
}

ViStatus WaitOnEvent(ViSession vi, ViEventType inEventType, ViUInt32 timeout, ViEventType* outEventType, ViEvent* eventHandle)
{
  return viWaitOnEvent(vi, inEventType, timeout, outEventType, eventHandle);
}

ViStatus Write(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount)
{
  return viWrite(vi, buffer, count, returnCount);
}

ViStatus WriteAsync(ViSession vi, ViByte buffer[], ViUInt32 count, ViJobId* jobIdentifier)
{
  return viWriteAsync(vi, buffer, count, jobIdentifier);
}

}  // namespace visa_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_library.cpp sha256=1d0845a282757845323961f32176c3c1c029950ac4de6334022410ca5eb28884 bytes=30651 -->
## FILE: generated/visa/visa_library.cpp

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_library.cpp`
- sha256: `1d0845a282757845323961f32176c3c1c029950ac4de6334022410ca5eb28884`
- bytes: 30651

````cpp
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service implementation for the VISA Metadata
//---------------------------------------------------------------------
#include "visa_library.h"
#include <server/shared_library.h>

#include <memory>

#if defined(_MSC_VER)
static const char* kLibraryName = "visa64.dll";
#else
static const char* kLibraryName = "libvisa.so";
#endif

namespace visa_grpc {

VisaLibrary::VisaLibrary() : VisaLibrary(std::make_shared<nidevice_grpc::SharedLibrary>()) {}

VisaLibrary::VisaLibrary(std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library) : shared_library_(shared_library)
{
  shared_library_->set_library_name(kLibraryName);
  shared_library_->load();
  bool loaded = shared_library_->is_loaded();
  memset(&function_pointers_, 0, sizeof(function_pointers_));
  if (!loaded) {
    return;
  }
  function_pointers_.AssertIntrSignal = reinterpret_cast<AssertIntrSignalPtr>(shared_library_->get_function_pointer("viAssertIntrSignal"));
  function_pointers_.AssertTrigger = reinterpret_cast<AssertTriggerPtr>(shared_library_->get_function_pointer("viAssertTrigger"));
  function_pointers_.AssertUtilSignal = reinterpret_cast<AssertUtilSignalPtr>(shared_library_->get_function_pointer("viAssertUtilSignal"));
  function_pointers_.Clear = reinterpret_cast<ClearPtr>(shared_library_->get_function_pointer("viClear"));
  function_pointers_.Close = reinterpret_cast<ClosePtr>(shared_library_->get_function_pointer("viClose"));
  function_pointers_.CloseEvent = reinterpret_cast<CloseEventPtr>(shared_library_->get_function_pointer("viClose"));
  function_pointers_.DisableEvent = reinterpret_cast<DisableEventPtr>(shared_library_->get_function_pointer("viDisableEvent"));
  function_pointers_.DiscardEvents = reinterpret_cast<DiscardEventsPtr>(shared_library_->get_function_pointer("viDiscardEvents"));
  function_pointers_.EnableEvent = reinterpret_cast<EnableEventPtr>(shared_library_->get_function_pointer("viEnableEvent"));
  function_pointers_.FindNext = reinterpret_cast<FindNextPtr>(shared_library_->get_function_pointer("viFindNext"));
  function_pointers_.FindRsrc = reinterpret_cast<FindRsrcPtr>(shared_library_->get_function_pointer("viFindRsrc"));
  function_pointers_.Flush = reinterpret_cast<FlushPtr>(shared_library_->get_function_pointer("viFlush"));
  function_pointers_.GetAttribute = reinterpret_cast<GetAttributePtr>(shared_library_->get_function_pointer("viGetAttribute"));
  function_pointers_.GetAttributeEvent = reinterpret_cast<GetAttributeEventPtr>(shared_library_->get_function_pointer("viGetAttribute"));
  function_pointers_.GpibCommand = reinterpret_cast<GpibCommandPtr>(shared_library_->get_function_pointer("viGpibCommand"));
  function_pointers_.GpibControlATN = reinterpret_cast<GpibControlATNPtr>(shared_library_->get_function_pointer("viGpibControlATN"));
  function_pointers_.GpibControlREN = reinterpret_cast<GpibControlRENPtr>(shared_library_->get_function_pointer("viGpibControlREN"));
  function_pointers_.GpibPassControl = reinterpret_cast<GpibPassControlPtr>(shared_library_->get_function_pointer("viGpibPassControl"));
  function_pointers_.GpibSendIFC = reinterpret_cast<GpibSendIFCPtr>(shared_library_->get_function_pointer("viGpibSendIFC"));
  function_pointers_.In16 = reinterpret_cast<In16Ptr>(shared_library_->get_function_pointer("viIn16Ex"));
  function_pointers_.In32 = reinterpret_cast<In32Ptr>(shared_library_->get_function_pointer("viIn32Ex"));
  function_pointers_.In64 = reinterpret_cast<In64Ptr>(shared_library_->get_function_pointer("viIn64Ex"));
  function_pointers_.In8 = reinterpret_cast<In8Ptr>(shared_library_->get_function_pointer("viIn8Ex"));
  function_pointers_.Lock = reinterpret_cast<LockPtr>(shared_library_->get_function_pointer("viLock"));
  function_pointers_.MapAddress = reinterpret_cast<MapAddressPtr>(shared_library_->get_function_pointer("viMapAddressEx"));
  function_pointers_.MapTrigger = reinterpret_cast<MapTriggerPtr>(shared_library_->get_function_pointer("viMapTrigger"));
  function_pointers_.MemAlloc = reinterpret_cast<MemAllocPtr>(shared_library_->get_function_pointer("viMemAlloc"));
  function_pointers_.MemAllocEx = reinterpret_cast<MemAllocExPtr>(shared_library_->get_function_pointer("viMemAllocEx"));
  function_pointers_.MemFree = reinterpret_cast<MemFreePtr>(shared_library_->get_function_pointer("viMemFreeEx"));
  function_pointers_.MoveIn16 = reinterpret_cast<MoveIn16Ptr>(shared_library_->get_function_pointer("viMoveIn16Ex"));
  function_pointers_.MoveIn32 = reinterpret_cast<MoveIn32Ptr>(shared_library_->get_function_pointer("viMoveIn32Ex"));
  function_pointers_.MoveIn64 = reinterpret_cast<MoveIn64Ptr>(shared_library_->get_function_pointer("viMoveIn64Ex"));
  function_pointers_.MoveIn8 = reinterpret_cast<MoveIn8Ptr>(shared_library_->get_function_pointer("viMoveIn8Ex"));
  function_pointers_.MoveOut16 = reinterpret_cast<MoveOut16Ptr>(shared_library_->get_function_pointer("viMoveOut16Ex"));
  function_pointers_.MoveOut32 = reinterpret_cast<MoveOut32Ptr>(shared_library_->get_function_pointer("viMoveOut32Ex"));
  function_pointers_.MoveOut64 = reinterpret_cast<MoveOut64Ptr>(shared_library_->get_function_pointer("viMoveOut64Ex"));
  function_pointers_.MoveOut8 = reinterpret_cast<MoveOut8Ptr>(shared_library_->get_function_pointer("viMoveOut8Ex"));
  function_pointers_.Open = reinterpret_cast<OpenPtr>(shared_library_->get_function_pointer("viOpen"));
  function_pointers_.OpenDefaultRM = reinterpret_cast<OpenDefaultRMPtr>(shared_library_->get_function_pointer("viOpenDefaultRM"));
  function_pointers_.Out16 = reinterpret_cast<Out16Ptr>(shared_library_->get_function_pointer("viOut16Ex"));
  function_pointers_.Out32 = reinterpret_cast<Out32Ptr>(shared_library_->get_function_pointer("viOut32Ex"));
  function_pointers_.Out64 = reinterpret_cast<Out64Ptr>(shared_library_->get_function_pointer("viOut64Ex"));
  function_pointers_.Out8 = reinterpret_cast<Out8Ptr>(shared_library_->get_function_pointer("viOut8Ex"));
  function_pointers_.ParseRsrc = reinterpret_cast<ParseRsrcPtr>(shared_library_->get_function_pointer("viParseRsrcEx"));
  function_pointers_.Peek16 = reinterpret_cast<Peek16Ptr>(shared_library_->get_function_pointer("viPeek16"));
  function_pointers_.Peek32 = reinterpret_cast<Peek32Ptr>(shared_library_->get_function_pointer("viPeek32"));
  function_pointers_.Peek64 = reinterpret_cast<Peek64Ptr>(shared_library_->get_function_pointer("viPeek64"));
  function_pointers_.Peek8 = reinterpret_cast<Peek8Ptr>(shared_library_->get_function_pointer("viPeek8"));
  function_pointers_.Poke16 = reinterpret_cast<Poke16Ptr>(shared_library_->get_function_pointer("viPoke16"));
  function_pointers_.Poke32 = reinterpret_cast<Poke32Ptr>(shared_library_->get_function_pointer("viPoke32"));
  function_pointers_.Poke64 = reinterpret_cast<Poke64Ptr>(shared_library_->get_function_pointer("viPoke64"));
  function_pointers_.Poke8 = reinterpret_cast<Poke8Ptr>(shared_library_->get_function_pointer("viPoke8"));
  function_pointers_.PxiReserveTriggers = reinterpret_cast<PxiReserveTriggersPtr>(shared_library_->get_function_pointer("viPxiReserveTriggers"));
  function_pointers_.Read = reinterpret_cast<ReadPtr>(shared_library_->get_function_pointer("viRead"));
  function_pointers_.ReadAsync = reinterpret_cast<ReadAsyncPtr>(shared_library_->get_function_pointer("viReadAsync"));
  function_pointers_.ReadSTB = reinterpret_cast<ReadSTBPtr>(shared_library_->get_function_pointer("viReadSTB"));
  function_pointers_.SetAttribute = reinterpret_cast<SetAttributePtr>(shared_library_->get_function_pointer("viSetAttribute"));
  function_pointers_.SetBuf = reinterpret_cast<SetBufPtr>(shared_library_->get_function_pointer("viSetBuf"));
  function_pointers_.StatusDesc = reinterpret_cast<StatusDescPtr>(shared_library_->get_function_pointer("viStatusDesc"));
  function_pointers_.Terminate = reinterpret_cast<TerminatePtr>(shared_library_->get_function_pointer("viTerminate"));
  function_pointers_.Unlock = reinterpret_cast<UnlockPtr>(shared_library_->get_function_pointer("viUnlock"));
  function_pointers_.UnmapAddress = reinterpret_cast<UnmapAddressPtr>(shared_library_->get_function_pointer("viUnmapAddress"));
  function_pointers_.UnmapTrigger = reinterpret_cast<UnmapTriggerPtr>(shared_library_->get_function_pointer("viUnmapTrigger"));
  function_pointers_.UsbControlIn = reinterpret_cast<UsbControlInPtr>(shared_library_->get_function_pointer("viUsbControlIn"));
  function_pointers_.UsbControlOut = reinterpret_cast<UsbControlOutPtr>(shared_library_->get_function_pointer("viUsbControlOut"));
  function_pointers_.VxiCommandQuery = reinterpret_cast<VxiCommandQueryPtr>(shared_library_->get_function_pointer("viVxiCommandQuery"));
  function_pointers_.WaitOnEvent = reinterpret_cast<WaitOnEventPtr>(shared_library_->get_function_pointer("viWaitOnEvent"));
  function_pointers_.Write = reinterpret_cast<WritePtr>(shared_library_->get_function_pointer("viWrite"));
  function_pointers_.WriteAsync = reinterpret_cast<WriteAsyncPtr>(shared_library_->get_function_pointer("viWriteAsync"));
}

VisaLibrary::~VisaLibrary()
{
}

::grpc::Status VisaLibrary::check_function_exists(std::string functionName)
{
  return shared_library_->function_exists(functionName.c_str())
    ? ::grpc::Status::OK
    : ::grpc::Status(::grpc::NOT_FOUND, "Could not find the function " + functionName);
}

ViStatus VisaLibrary::AssertIntrSignal(ViSession vi, ViInt16 mode, ViUInt32 statusId)
{
  if (!function_pointers_.AssertIntrSignal) {
    throw nidevice_grpc::LibraryLoadException("Could not find viAssertIntrSignal.");
  }
  return function_pointers_.AssertIntrSignal(vi, mode, statusId);
}

ViStatus VisaLibrary::AssertTrigger(ViSession vi, ViUInt16 protocol)
{
  if (!function_pointers_.AssertTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find viAssertTrigger.");
  }
  return function_pointers_.AssertTrigger(vi, protocol);
}

ViStatus VisaLibrary::AssertUtilSignal(ViSession vi, ViUInt16 mode)
{
  if (!function_pointers_.AssertUtilSignal) {
    throw nidevice_grpc::LibraryLoadException("Could not find viAssertUtilSignal.");
  }
  return function_pointers_.AssertUtilSignal(vi, mode);
}

ViStatus VisaLibrary::Clear(ViSession vi)
{
  if (!function_pointers_.Clear) {
    throw nidevice_grpc::LibraryLoadException("Could not find viClear.");
  }
  return function_pointers_.Clear(vi);
}

ViStatus VisaLibrary::Close(ViSession vi)
{
  if (!function_pointers_.Close) {
    throw nidevice_grpc::LibraryLoadException("Could not find viClose.");
  }
  return function_pointers_.Close(vi);
}

ViStatus VisaLibrary::CloseEvent(ViEvent eventHandle)
{
  if (!function_pointers_.CloseEvent) {
    throw nidevice_grpc::LibraryLoadException("Could not find viClose.");
  }
  return function_pointers_.CloseEvent(eventHandle);
}

ViStatus VisaLibrary::DisableEvent(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism)
{
  if (!function_pointers_.DisableEvent) {
    throw nidevice_grpc::LibraryLoadException("Could not find viDisableEvent.");
  }
  return function_pointers_.DisableEvent(vi, eventType, eventMechanism);
}

ViStatus VisaLibrary::DiscardEvents(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism)
{
  if (!function_pointers_.DiscardEvents) {
    throw nidevice_grpc::LibraryLoadException("Could not find viDiscardEvents.");
  }
  return function_pointers_.DiscardEvents(vi, eventType, eventMechanism);
}

ViStatus VisaLibrary::EnableEvent(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism, ViEventFilter filterContext)
{
  if (!function_pointers_.EnableEvent) {
    throw nidevice_grpc::LibraryLoadException("Could not find viEnableEvent.");
  }
  return function_pointers_.EnableEvent(vi, eventType, eventMechanism, filterContext);
}

ViStatus VisaLibrary::FindNext(ViFindList findHandle, ViChar instrumentDescriptor[256])
{
  if (!function_pointers_.FindNext) {
    throw nidevice_grpc::LibraryLoadException("Could not find viFindNext.");
  }
  return function_pointers_.FindNext(findHandle, instrumentDescriptor);
}

ViStatus VisaLibrary::FindRsrc(ViSession rsrcManagerHandle, ViConstString expression, ViFindList* findHandle, ViUInt32* returnCount, ViChar instrumentDescriptor[256])
{
  if (!function_pointers_.FindRsrc) {
    throw nidevice_grpc::LibraryLoadException("Could not find viFindRsrc.");
  }
  return function_pointers_.FindRsrc(rsrcManagerHandle, expression, findHandle, returnCount, instrumentDescriptor);
}

ViStatus VisaLibrary::Flush(ViSession vi, ViUInt16 mask)
{
  if (!function_pointers_.Flush) {
    throw nidevice_grpc::LibraryLoadException("Could not find viFlush.");
  }
  return function_pointers_.Flush(vi, mask);
}

ViStatus VisaLibrary::GetAttribute(ViSession vi, ViAttr attributeName, void* attributeValue)
{
  if (!function_pointers_.GetAttribute) {
    throw nidevice_grpc::LibraryLoadException("Could not find viGetAttribute.");
  }
  return function_pointers_.GetAttribute(vi, attributeName, attributeValue);
}

ViStatus VisaLibrary::GetAttributeEvent(ViEvent eventHandle, ViAttr attributeName, void* attributeValue)
{
  if (!function_pointers_.GetAttributeEvent) {
    throw nidevice_grpc::LibraryLoadException("Could not find viGetAttribute.");
  }
  return function_pointers_.GetAttributeEvent(eventHandle, attributeName, attributeValue);
}

ViStatus VisaLibrary::GpibCommand(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount)
{
  if (!function_pointers_.GpibCommand) {
    throw nidevice_grpc::LibraryLoadException("Could not find viGpibCommand.");
  }
  return function_pointers_.GpibCommand(vi, buffer, count, returnCount);
}

ViStatus VisaLibrary::GpibControlATN(ViSession vi, ViUInt16 mode)
{
  if (!function_pointers_.GpibControlATN) {
    throw nidevice_grpc::LibraryLoadException("Could not find viGpibControlATN.");
  }
  return function_pointers_.GpibControlATN(vi, mode);
}

ViStatus VisaLibrary::GpibControlREN(ViSession vi, ViUInt16 mode)
{
  if (!function_pointers_.GpibControlREN) {
    throw nidevice_grpc::LibraryLoadException("Could not find viGpibControlREN.");
  }
  return function_pointers_.GpibControlREN(vi, mode);
}

ViStatus VisaLibrary::GpibPassControl(ViSession vi, ViUInt16 primaryAddress, ViUInt16 secondaryAddress)
{
  if (!function_pointers_.GpibPassControl) {
    throw nidevice_grpc::LibraryLoadException("Could not find viGpibPassControl.");
  }
  return function_pointers_.GpibPassControl(vi, primaryAddress, secondaryAddress);
}

ViStatus VisaLibrary::GpibSendIFC(ViSession vi)
{
  if (!function_pointers_.GpibSendIFC) {
    throw nidevice_grpc::LibraryLoadException("Could not find viGpibSendIFC.");
  }
  return function_pointers_.GpibSendIFC(vi);
}

ViStatus VisaLibrary::In16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt16* value)
{
  if (!function_pointers_.In16) {
    throw nidevice_grpc::LibraryLoadException("Could not find viIn16Ex.");
  }
  return function_pointers_.In16(vi, addressSpace, offset, value);
}

ViStatus VisaLibrary::In32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt32* value)
{
  if (!function_pointers_.In32) {
    throw nidevice_grpc::LibraryLoadException("Could not find viIn32Ex.");
  }
  return function_pointers_.In32(vi, addressSpace, offset, value);
}

ViStatus VisaLibrary::In64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt64* value)
{
  if (!function_pointers_.In64) {
    throw nidevice_grpc::LibraryLoadException("Could not find viIn64Ex.");
  }
  return function_pointers_.In64(vi, addressSpace, offset, value);
}

ViStatus VisaLibrary::In8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt8* value)
{
  if (!function_pointers_.In8) {
    throw nidevice_grpc::LibraryLoadException("Could not find viIn8Ex.");
  }
  return function_pointers_.In8(vi, addressSpace, offset, value);
}

ViStatus VisaLibrary::Lock(ViSession vi, ViAccessMode lockType, ViUInt32 timeout, ViConstKeyId requestedKey, ViChar accessKey[256])
{
  if (!function_pointers_.Lock) {
    throw nidevice_grpc::LibraryLoadException("Could not find viLock.");
  }
  return function_pointers_.Lock(vi, lockType, timeout, requestedKey, accessKey);
}

ViStatus VisaLibrary::MapAddress(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize mapSize, ViBoolean ownerAccess, ViAddr suggestedAddress, ViAddr* address)
{
  if (!function_pointers_.MapAddress) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMapAddressEx.");
  }
  return function_pointers_.MapAddress(vi, addressSpace, offset, mapSize, ownerAccess, suggestedAddress, address);
}

ViStatus VisaLibrary::MapTrigger(ViSession vi, ViInt16 triggerSource, ViInt16 triggerDestination, ViUInt16 mode)
{
  if (!function_pointers_.MapTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMapTrigger.");
  }
  return function_pointers_.MapTrigger(vi, triggerSource, triggerDestination, mode);
}

ViStatus VisaLibrary::MemAlloc(ViSession vi, ViUInt32 size, ViBusAddress* offset)
{
  if (!function_pointers_.MemAlloc) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMemAlloc.");
  }
  return function_pointers_.MemAlloc(vi, size, offset);
}

ViStatus VisaLibrary::MemAllocEx(ViSession vi, ViBusSize size, ViBusAddress64* offset)
{
  if (!function_pointers_.MemAllocEx) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMemAllocEx.");
  }
  return function_pointers_.MemAllocEx(vi, size, offset);
}

ViStatus VisaLibrary::MemFree(ViSession vi, ViBusAddress64 offset)
{
  if (!function_pointers_.MemFree) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMemFreeEx.");
  }
  return function_pointers_.MemFree(vi, offset);
}

ViStatus VisaLibrary::MoveIn16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt16 buffer[])
{
  if (!function_pointers_.MoveIn16) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMoveIn16Ex.");
  }
  return function_pointers_.MoveIn16(vi, addressSpace, offset, count, buffer);
}

ViStatus VisaLibrary::MoveIn32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt32 buffer[])
{
  if (!function_pointers_.MoveIn32) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMoveIn32Ex.");
  }
  return function_pointers_.MoveIn32(vi, addressSpace, offset, count, buffer);
}

ViStatus VisaLibrary::MoveIn64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt64 buffer[])
{
  if (!function_pointers_.MoveIn64) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMoveIn64Ex.");
  }
  return function_pointers_.MoveIn64(vi, addressSpace, offset, count, buffer);
}

ViStatus VisaLibrary::MoveIn8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt8 buffer[])
{
  if (!function_pointers_.MoveIn8) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMoveIn8Ex.");
  }
  return function_pointers_.MoveIn8(vi, addressSpace, offset, count, buffer);
}

ViStatus VisaLibrary::MoveOut16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt16 buffer[])
{
  if (!function_pointers_.MoveOut16) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMoveOut16Ex.");
  }
  return function_pointers_.MoveOut16(vi, addressSpace, offset, count, buffer);
}

ViStatus VisaLibrary::MoveOut32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt32 buffer[])
{
  if (!function_pointers_.MoveOut32) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMoveOut32Ex.");
  }
  return function_pointers_.MoveOut32(vi, addressSpace, offset, count, buffer);
}

ViStatus VisaLibrary::MoveOut64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt64 buffer[])
{
  if (!function_pointers_.MoveOut64) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMoveOut64Ex.");
  }
  return function_pointers_.MoveOut64(vi, addressSpace, offset, count, buffer);
}

ViStatus VisaLibrary::MoveOut8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt8 buffer[])
{
  if (!function_pointers_.MoveOut8) {
    throw nidevice_grpc::LibraryLoadException("Could not find viMoveOut8Ex.");
  }
  return function_pointers_.MoveOut8(vi, addressSpace, offset, count, buffer);
}

ViStatus VisaLibrary::Open(ViSession rsrcManagerHandle, ViConstRsrc instrumentDescriptor, ViAccessMode accessMode, ViUInt32 openTimeout, ViSession* vi)
{
  if (!function_pointers_.Open) {
    throw nidevice_grpc::LibraryLoadException("Could not find viOpen.");
  }
  return function_pointers_.Open(rsrcManagerHandle, instrumentDescriptor, accessMode, openTimeout, vi);
}

ViStatus VisaLibrary::OpenDefaultRM(ViSession* rsrcManagerHandle)
{
  if (!function_pointers_.OpenDefaultRM) {
    throw nidevice_grpc::LibraryLoadException("Could not find viOpenDefaultRM.");
  }
  return function_pointers_.OpenDefaultRM(rsrcManagerHandle);
}

ViStatus VisaLibrary::Out16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt16 value)
{
  if (!function_pointers_.Out16) {
    throw nidevice_grpc::LibraryLoadException("Could not find viOut16Ex.");
  }
  return function_pointers_.Out16(vi, addressSpace, offset, value);
}

ViStatus VisaLibrary::Out32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt32 value)
{
  if (!function_pointers_.Out32) {
    throw nidevice_grpc::LibraryLoadException("Could not find viOut32Ex.");
  }
  return function_pointers_.Out32(vi, addressSpace, offset, value);
}

ViStatus VisaLibrary::Out64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt64 value)
{
  if (!function_pointers_.Out64) {
    throw nidevice_grpc::LibraryLoadException("Could not find viOut64Ex.");
  }
  return function_pointers_.Out64(vi, addressSpace, offset, value);
}

ViStatus VisaLibrary::Out8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt8 value)
{
  if (!function_pointers_.Out8) {
    throw nidevice_grpc::LibraryLoadException("Could not find viOut8Ex.");
  }
  return function_pointers_.Out8(vi, addressSpace, offset, value);
}

ViStatus VisaLibrary::ParseRsrc(ViSession sessionHandle, ViConstRsrc resourceName, ViUInt16* interfaceType, ViUInt16* interfaceNumber, ViChar resourceClass[256], ViChar expandedUnaliasedName[256], ViChar aliasIfExists[256])
{
  if (!function_pointers_.ParseRsrc) {
    throw nidevice_grpc::LibraryLoadException("Could not find viParseRsrcEx.");
  }
  return function_pointers_.ParseRsrc(sessionHandle, resourceName, interfaceType, interfaceNumber, resourceClass, expandedUnaliasedName, aliasIfExists);
}

void VisaLibrary::Peek16(ViSession vi, ViAddr address, ViUInt16* value)
{
  if (!function_pointers_.Peek16) {
    throw nidevice_grpc::LibraryLoadException("Could not find viPeek16.");
  }
  return function_pointers_.Peek16(vi, address, value);
}

void VisaLibrary::Peek32(ViSession vi, ViAddr address, ViUInt32* value)
{
  if (!function_pointers_.Peek32) {
    throw nidevice_grpc::LibraryLoadException("Could not find viPeek32.");
  }
  return function_pointers_.Peek32(vi, address, value);
}

void VisaLibrary::Peek64(ViSession vi, ViAddr address, ViUInt64* value)
{
  if (!function_pointers_.Peek64) {
    throw nidevice_grpc::LibraryLoadException("Could not find viPeek64.");
  }
  return function_pointers_.Peek64(vi, address, value);
}

void VisaLibrary::Peek8(ViSession vi, ViAddr address, ViUInt8* value)
{
  if (!function_pointers_.Peek8) {
    throw nidevice_grpc::LibraryLoadException("Could not find viPeek8.");
  }
  return function_pointers_.Peek8(vi, address, value);
}

void VisaLibrary::Poke16(ViSession vi, ViAddr address, ViUInt16 value)
{
  if (!function_pointers_.Poke16) {
    throw nidevice_grpc::LibraryLoadException("Could not find viPoke16.");
  }
  return function_pointers_.Poke16(vi, address, value);
}

void VisaLibrary::Poke32(ViSession vi, ViAddr address, ViUInt32 value)
{
  if (!function_pointers_.Poke32) {
    throw nidevice_grpc::LibraryLoadException("Could not find viPoke32.");
  }
  return function_pointers_.Poke32(vi, address, value);
}

void VisaLibrary::Poke64(ViSession vi, ViAddr address, ViUInt64 value)
{
  if (!function_pointers_.Poke64) {
    throw nidevice_grpc::LibraryLoadException("Could not find viPoke64.");
  }
  return function_pointers_.Poke64(vi, address, value);
}

void VisaLibrary::Poke8(ViSession vi, ViAddr address, ViUInt8 value)
{
  if (!function_pointers_.Poke8) {
    throw nidevice_grpc::LibraryLoadException("Could not find viPoke8.");
  }
  return function_pointers_.Poke8(vi, address, value);
}

ViStatus VisaLibrary::PxiReserveTriggers(ViSession vi, ViInt16 cnt, ViInt16 trigBuses[], ViInt16 trigLines[], ViInt16* failureIndex)
{
  if (!function_pointers_.PxiReserveTriggers) {
    throw nidevice_grpc::LibraryLoadException("Could not find viPxiReserveTriggers.");
  }
  return function_pointers_.PxiReserveTriggers(vi, cnt, trigBuses, trigLines, failureIndex);
}

ViStatus VisaLibrary::Read(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount)
{
  if (!function_pointers_.Read) {
    throw nidevice_grpc::LibraryLoadException("Could not find viRead.");
  }
  return function_pointers_.Read(vi, buffer, count, returnCount);
}

ViStatus VisaLibrary::ReadAsync(ViSession vi, ViByte readBuffer[], ViUInt32 count, ViJobId* jobIdentifier)
{
  if (!function_pointers_.ReadAsync) {
    throw nidevice_grpc::LibraryLoadException("Could not find viReadAsync.");
  }
  return function_pointers_.ReadAsync(vi, readBuffer, count, jobIdentifier);
}

ViStatus VisaLibrary::ReadSTB(ViSession vi, ViUInt16* statusByte)
{
  if (!function_pointers_.ReadSTB) {
    throw nidevice_grpc::LibraryLoadException("Could not find viReadSTB.");
  }
  return function_pointers_.ReadSTB(vi, statusByte);
}

ViStatus VisaLibrary::SetAttribute(ViSession vi, ViAttr attributeName, ViAttrState attributeValue)
{
  if (!function_pointers_.SetAttribute) {
    throw nidevice_grpc::LibraryLoadException("Could not find viSetAttribute.");
  }
  return function_pointers_.SetAttribute(vi, attributeName, attributeValue);
}

ViStatus VisaLibrary::SetBuf(ViSession vi, ViUInt16 mask, ViUInt32 bufferSize)
{
  if (!function_pointers_.SetBuf) {
    throw nidevice_grpc::LibraryLoadException("Could not find viSetBuf.");
  }
  return function_pointers_.SetBuf(vi, mask, bufferSize);
}

ViStatus VisaLibrary::StatusDesc(ViSession vi, ViStatus statusValue, ViChar statusDescription[256])
{
  if (!function_pointers_.StatusDesc) {
    throw nidevice_grpc::LibraryLoadException("Could not find viStatusDesc.");
  }
  return function_pointers_.StatusDesc(vi, statusValue, statusDescription);
}

ViStatus VisaLibrary::Terminate(ViSession vi, ViUInt16 degree, ViJobId jobIdentifier)
{
  if (!function_pointers_.Terminate) {
    throw nidevice_grpc::LibraryLoadException("Could not find viTerminate.");
  }
  return function_pointers_.Terminate(vi, degree, jobIdentifier);
}

ViStatus VisaLibrary::Unlock(ViSession vi)
{
  if (!function_pointers_.Unlock) {
    throw nidevice_grpc::LibraryLoadException("Could not find viUnlock.");
  }
  return function_pointers_.Unlock(vi);
}

ViStatus VisaLibrary::UnmapAddress(ViSession vi)
{
  if (!function_pointers_.UnmapAddress) {
    throw nidevice_grpc::LibraryLoadException("Could not find viUnmapAddress.");
  }
  return function_pointers_.UnmapAddress(vi);
}

ViStatus VisaLibrary::UnmapTrigger(ViSession vi, ViInt16 triggerSource, ViInt16 triggerDestination)
{
  if (!function_pointers_.UnmapTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find viUnmapTrigger.");
  }
  return function_pointers_.UnmapTrigger(vi, triggerSource, triggerDestination);
}

ViStatus VisaLibrary::UsbControlIn(ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest, ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength, ViByte buffer[], ViUInt16* returnCount)
{
  if (!function_pointers_.UsbControlIn) {
    throw nidevice_grpc::LibraryLoadException("Could not find viUsbControlIn.");
  }
  return function_pointers_.UsbControlIn(vi, bmRequestType, bRequest, wValue, wIndex, wLength, buffer, returnCount);
}

ViStatus VisaLibrary::UsbControlOut(ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest, ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength, ViByte buffer[])
{
  if (!function_pointers_.UsbControlOut) {
    throw nidevice_grpc::LibraryLoadException("Could not find viUsbControlOut.");
  }
  return function_pointers_.UsbControlOut(vi, bmRequestType, bRequest, wValue, wIndex, wLength, buffer);
}

ViStatus VisaLibrary::VxiCommandQuery(ViSession vi, ViUInt16 mode, ViUInt32 command, ViUInt32* commandResponse)
{
  if (!function_pointers_.VxiCommandQuery) {
    throw nidevice_grpc::LibraryLoadException("Could not find viVxiCommandQuery.");
  }
  return function_pointers_.VxiCommandQuery(vi, mode, command, commandResponse);
}

ViStatus VisaLibrary::WaitOnEvent(ViSession vi, ViEventType inEventType, ViUInt32 timeout, ViEventType* outEventType, ViEvent* eventHandle)
{
  if (!function_pointers_.WaitOnEvent) {
    throw nidevice_grpc::LibraryLoadException("Could not find viWaitOnEvent.");
  }
  return function_pointers_.WaitOnEvent(vi, inEventType, timeout, outEventType, eventHandle);
}

ViStatus VisaLibrary::Write(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount)
{
  if (!function_pointers_.Write) {
    throw nidevice_grpc::LibraryLoadException("Could not find viWrite.");
  }
  return function_pointers_.Write(vi, buffer, count, returnCount);
}

ViStatus VisaLibrary::WriteAsync(ViSession vi, ViByte buffer[], ViUInt32 count, ViJobId* jobIdentifier)
{
  if (!function_pointers_.WriteAsync) {
    throw nidevice_grpc::LibraryLoadException("Could not find viWriteAsync.");
  }
  return function_pointers_.WriteAsync(vi, buffer, count, jobIdentifier);
}

}  // namespace visa_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_library.h sha256=b5a092210c7754c2dc95e8d2261f2cb48b3b352a1bc403e1c14f8a3c579623c7 bytes=13280 -->
## FILE: generated/visa/visa_library.h

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_library.h`
- sha256: `b5a092210c7754c2dc95e8d2261f2cb48b3b352a1bc403e1c14f8a3c579623c7`
- bytes: 13280

````c
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Real implementation of LibraryInterface for VISA
//---------------------------------------------------------------------
#ifndef VISA_GRPC_LIBRARY_H
#define VISA_GRPC_LIBRARY_H

#include "visa_library_interface.h"

#include <server/shared_library_interface.h>

#include <memory>

namespace visa_grpc {

class VisaLibrary : public visa_grpc::VisaLibraryInterface {
 public:
  VisaLibrary();
  explicit VisaLibrary(std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library);
  virtual ~VisaLibrary();

  ::grpc::Status check_function_exists(std::string functionName);
  ViStatus AssertIntrSignal(ViSession vi, ViInt16 mode, ViUInt32 statusId) override;
  ViStatus AssertTrigger(ViSession vi, ViUInt16 protocol) override;
  ViStatus AssertUtilSignal(ViSession vi, ViUInt16 mode) override;
  ViStatus Clear(ViSession vi) override;
  ViStatus Close(ViSession vi) override;
  ViStatus CloseEvent(ViEvent eventHandle) override;
  ViStatus DisableEvent(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism) override;
  ViStatus DiscardEvents(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism) override;
  ViStatus EnableEvent(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism, ViEventFilter filterContext) override;
  ViStatus FindNext(ViFindList findHandle, ViChar instrumentDescriptor[256]) override;
  ViStatus FindRsrc(ViSession rsrcManagerHandle, ViConstString expression, ViFindList* findHandle, ViUInt32* returnCount, ViChar instrumentDescriptor[256]) override;
  ViStatus Flush(ViSession vi, ViUInt16 mask) override;
  ViStatus GetAttribute(ViSession vi, ViAttr attributeName, void* attributeValue) override;
  ViStatus GetAttributeEvent(ViEvent eventHandle, ViAttr attributeName, void* attributeValue) override;
  ViStatus GpibCommand(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount) override;
  ViStatus GpibControlATN(ViSession vi, ViUInt16 mode) override;
  ViStatus GpibControlREN(ViSession vi, ViUInt16 mode) override;
  ViStatus GpibPassControl(ViSession vi, ViUInt16 primaryAddress, ViUInt16 secondaryAddress) override;
  ViStatus GpibSendIFC(ViSession vi) override;
  ViStatus In16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt16* value) override;
  ViStatus In32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt32* value) override;
  ViStatus In64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt64* value) override;
  ViStatus In8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt8* value) override;
  ViStatus Lock(ViSession vi, ViAccessMode lockType, ViUInt32 timeout, ViConstKeyId requestedKey, ViChar accessKey[256]) override;
  ViStatus MapAddress(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize mapSize, ViBoolean ownerAccess, ViAddr suggestedAddress, ViAddr* address) override;
  ViStatus MapTrigger(ViSession vi, ViInt16 triggerSource, ViInt16 triggerDestination, ViUInt16 mode) override;
  ViStatus MemAlloc(ViSession vi, ViUInt32 size, ViBusAddress* offset) override;
  ViStatus MemAllocEx(ViSession vi, ViBusSize size, ViBusAddress64* offset) override;
  ViStatus MemFree(ViSession vi, ViBusAddress64 offset) override;
  ViStatus MoveIn16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt16 buffer[]) override;
  ViStatus MoveIn32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt32 buffer[]) override;
  ViStatus MoveIn64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt64 buffer[]) override;
  ViStatus MoveIn8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt8 buffer[]) override;
  ViStatus MoveOut16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt16 buffer[]) override;
  ViStatus MoveOut32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt32 buffer[]) override;
  ViStatus MoveOut64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt64 buffer[]) override;
  ViStatus MoveOut8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt8 buffer[]) override;
  ViStatus Open(ViSession rsrcManagerHandle, ViConstRsrc instrumentDescriptor, ViAccessMode accessMode, ViUInt32 openTimeout, ViSession* vi) override;
  ViStatus OpenDefaultRM(ViSession* rsrcManagerHandle) override;
  ViStatus Out16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt16 value) override;
  ViStatus Out32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt32 value) override;
  ViStatus Out64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt64 value) override;
  ViStatus Out8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt8 value) override;
  ViStatus ParseRsrc(ViSession sessionHandle, ViConstRsrc resourceName, ViUInt16* interfaceType, ViUInt16* interfaceNumber, ViChar resourceClass[256], ViChar expandedUnaliasedName[256], ViChar aliasIfExists[256]) override;
  void Peek16(ViSession vi, ViAddr address, ViUInt16* value) override;
  void Peek32(ViSession vi, ViAddr address, ViUInt32* value) override;
  void Peek64(ViSession vi, ViAddr address, ViUInt64* value) override;
  void Peek8(ViSession vi, ViAddr address, ViUInt8* value) override;
  void Poke16(ViSession vi, ViAddr address, ViUInt16 value) override;
  void Poke32(ViSession vi, ViAddr address, ViUInt32 value) override;
  void Poke64(ViSession vi, ViAddr address, ViUInt64 value) override;
  void Poke8(ViSession vi, ViAddr address, ViUInt8 value) override;
  ViStatus PxiReserveTriggers(ViSession vi, ViInt16 cnt, ViInt16 trigBuses[], ViInt16 trigLines[], ViInt16* failureIndex) override;
  ViStatus Read(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount) override;
  ViStatus ReadAsync(ViSession vi, ViByte readBuffer[], ViUInt32 count, ViJobId* jobIdentifier) override;
  ViStatus ReadSTB(ViSession vi, ViUInt16* statusByte) override;
  ViStatus SetAttribute(ViSession vi, ViAttr attributeName, ViAttrState attributeValue) override;
  ViStatus SetBuf(ViSession vi, ViUInt16 mask, ViUInt32 bufferSize) override;
  ViStatus StatusDesc(ViSession vi, ViStatus statusValue, ViChar statusDescription[256]) override;
  ViStatus Terminate(ViSession vi, ViUInt16 degree, ViJobId jobIdentifier) override;
  ViStatus Unlock(ViSession vi) override;
  ViStatus UnmapAddress(ViSession vi) override;
  ViStatus UnmapTrigger(ViSession vi, ViInt16 triggerSource, ViInt16 triggerDestination) override;
  ViStatus UsbControlIn(ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest, ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength, ViByte buffer[], ViUInt16* returnCount) override;
  ViStatus UsbControlOut(ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest, ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength, ViByte buffer[]) override;
  ViStatus VxiCommandQuery(ViSession vi, ViUInt16 mode, ViUInt32 command, ViUInt32* commandResponse) override;
  ViStatus WaitOnEvent(ViSession vi, ViEventType inEventType, ViUInt32 timeout, ViEventType* outEventType, ViEvent* eventHandle) override;
  ViStatus Write(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount) override;
  ViStatus WriteAsync(ViSession vi, ViByte buffer[], ViUInt32 count, ViJobId* jobIdentifier) override;

 private:
  using AssertIntrSignalPtr = decltype(&viAssertIntrSignal);
  using AssertTriggerPtr = decltype(&viAssertTrigger);
  using AssertUtilSignalPtr = decltype(&viAssertUtilSignal);
  using ClearPtr = decltype(&viClear);
  using ClosePtr = decltype(&viClose);
  using CloseEventPtr = decltype(&viClose);
  using DisableEventPtr = decltype(&viDisableEvent);
  using DiscardEventsPtr = decltype(&viDiscardEvents);
  using EnableEventPtr = decltype(&viEnableEvent);
  using FindNextPtr = ViStatus (*)(ViFindList findHandle, ViChar instrumentDescriptor[256]);
  using FindRsrcPtr = decltype(&viFindRsrc);
  using FlushPtr = decltype(&viFlush);
  using GetAttributePtr = decltype(&viGetAttribute);
  using GetAttributeEventPtr = decltype(&viGetAttribute);
  using GpibCommandPtr = decltype(&viGpibCommand);
  using GpibControlATNPtr = decltype(&viGpibControlATN);
  using GpibControlRENPtr = decltype(&viGpibControlREN);
  using GpibPassControlPtr = decltype(&viGpibPassControl);
  using GpibSendIFCPtr = decltype(&viGpibSendIFC);
  using In16Ptr = decltype(&viIn16Ex);
  using In32Ptr = decltype(&viIn32Ex);
  using In64Ptr = decltype(&viIn64Ex);
  using In8Ptr = decltype(&viIn8Ex);
  using LockPtr = decltype(&viLock);
  using MapAddressPtr = decltype(&viMapAddressEx);
  using MapTriggerPtr = decltype(&viMapTrigger);
  using MemAllocPtr = decltype(&viMemAlloc);
  using MemAllocExPtr = decltype(&viMemAllocEx);
  using MemFreePtr = decltype(&viMemFreeEx);
  using MoveIn16Ptr = decltype(&viMoveIn16Ex);
  using MoveIn32Ptr = decltype(&viMoveIn32Ex);
  using MoveIn64Ptr = decltype(&viMoveIn64Ex);
  using MoveIn8Ptr = decltype(&viMoveIn8Ex);
  using MoveOut16Ptr = decltype(&viMoveOut16Ex);
  using MoveOut32Ptr = decltype(&viMoveOut32Ex);
  using MoveOut64Ptr = decltype(&viMoveOut64Ex);
  using MoveOut8Ptr = decltype(&viMoveOut8Ex);
  using OpenPtr = decltype(&viOpen);
  using OpenDefaultRMPtr = ViStatus (*)(ViSession* rsrcManagerHandle);
  using Out16Ptr = decltype(&viOut16Ex);
  using Out32Ptr = decltype(&viOut32Ex);
  using Out64Ptr = decltype(&viOut64Ex);
  using Out8Ptr = decltype(&viOut8Ex);
  using ParseRsrcPtr = decltype(&viParseRsrcEx);
  using Peek16Ptr = decltype(&viPeek16);
  using Peek32Ptr = decltype(&viPeek32);
  using Peek64Ptr = decltype(&viPeek64);
  using Peek8Ptr = decltype(&viPeek8);
  using Poke16Ptr = decltype(&viPoke16);
  using Poke32Ptr = decltype(&viPoke32);
  using Poke64Ptr = decltype(&viPoke64);
  using Poke8Ptr = decltype(&viPoke8);
  using PxiReserveTriggersPtr = decltype(&viPxiReserveTriggers);
  using ReadPtr = decltype(&viRead);
  using ReadAsyncPtr = decltype(&viReadAsync);
  using ReadSTBPtr = decltype(&viReadSTB);
  using SetAttributePtr = decltype(&viSetAttribute);
  using SetBufPtr = decltype(&viSetBuf);
  using StatusDescPtr = decltype(&viStatusDesc);
  using TerminatePtr = decltype(&viTerminate);
  using UnlockPtr = decltype(&viUnlock);
  using UnmapAddressPtr = decltype(&viUnmapAddress);
  using UnmapTriggerPtr = decltype(&viUnmapTrigger);
  using UsbControlInPtr = decltype(&viUsbControlIn);
  using UsbControlOutPtr = decltype(&viUsbControlOut);
  using VxiCommandQueryPtr = decltype(&viVxiCommandQuery);
  using WaitOnEventPtr = decltype(&viWaitOnEvent);
  using WritePtr = decltype(&viWrite);
  using WriteAsyncPtr = decltype(&viWriteAsync);

  typedef struct FunctionPointers {
    AssertIntrSignalPtr AssertIntrSignal;
    AssertTriggerPtr AssertTrigger;
    AssertUtilSignalPtr AssertUtilSignal;
    ClearPtr Clear;
    ClosePtr Close;
    CloseEventPtr CloseEvent;
    DisableEventPtr DisableEvent;
    DiscardEventsPtr DiscardEvents;
    EnableEventPtr EnableEvent;
    FindNextPtr FindNext;
    FindRsrcPtr FindRsrc;
    FlushPtr Flush;
    GetAttributePtr GetAttribute;
    GetAttributeEventPtr GetAttributeEvent;
    GpibCommandPtr GpibCommand;
    GpibControlATNPtr GpibControlATN;
    GpibControlRENPtr GpibControlREN;
    GpibPassControlPtr GpibPassControl;
    GpibSendIFCPtr GpibSendIFC;
    In16Ptr In16;
    In32Ptr In32;
    In64Ptr In64;
    In8Ptr In8;
    LockPtr Lock;
    MapAddressPtr MapAddress;
    MapTriggerPtr MapTrigger;
    MemAllocPtr MemAlloc;
    MemAllocExPtr MemAllocEx;
    MemFreePtr MemFree;
    MoveIn16Ptr MoveIn16;
    MoveIn32Ptr MoveIn32;
    MoveIn64Ptr MoveIn64;
    MoveIn8Ptr MoveIn8;
    MoveOut16Ptr MoveOut16;
    MoveOut32Ptr MoveOut32;
    MoveOut64Ptr MoveOut64;
    MoveOut8Ptr MoveOut8;
    OpenPtr Open;
    OpenDefaultRMPtr OpenDefaultRM;
    Out16Ptr Out16;
    Out32Ptr Out32;
    Out64Ptr Out64;
    Out8Ptr Out8;
    ParseRsrcPtr ParseRsrc;
    Peek16Ptr Peek16;
    Peek32Ptr Peek32;
    Peek64Ptr Peek64;
    Peek8Ptr Peek8;
    Poke16Ptr Poke16;
    Poke32Ptr Poke32;
    Poke64Ptr Poke64;
    Poke8Ptr Poke8;
    PxiReserveTriggersPtr PxiReserveTriggers;
    ReadPtr Read;
    ReadAsyncPtr ReadAsync;
    ReadSTBPtr ReadSTB;
    SetAttributePtr SetAttribute;
    SetBufPtr SetBuf;
    StatusDescPtr StatusDesc;
    TerminatePtr Terminate;
    UnlockPtr Unlock;
    UnmapAddressPtr UnmapAddress;
    UnmapTriggerPtr UnmapTrigger;
    UsbControlInPtr UsbControlIn;
    UsbControlOutPtr UsbControlOut;
    VxiCommandQueryPtr VxiCommandQuery;
    WaitOnEventPtr WaitOnEvent;
    WritePtr Write;
    WriteAsyncPtr WriteAsync;
  } FunctionLoadStatus;

  std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library_;
  FunctionPointers function_pointers_;
};

}  // namespace visa_grpc

#endif  // VISA_GRPC_LIBRARY_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_library_interface.h sha256=203d5a7ae53924ac2cc50d215312ea7752e0b59ec6e9957b2146544e62fb6018 bytes=7708 -->
## FILE: generated/visa/visa_library_interface.h

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_library_interface.h`
- sha256: `203d5a7ae53924ac2cc50d215312ea7752e0b59ec6e9957b2146544e62fb6018`
- bytes: 7708

````c
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Library wrapper for implementing interactions with VISA
//---------------------------------------------------------------------
#ifndef VISA_GRPC_LIBRARY_WRAPPER_H
#define VISA_GRPC_LIBRARY_WRAPPER_H

#include <grpcpp/grpcpp.h>
#include <visa.h>

namespace visa_grpc {

class VisaLibraryInterface {
 public:
  virtual ~VisaLibraryInterface() {}

  virtual ViStatus AssertIntrSignal(ViSession vi, ViInt16 mode, ViUInt32 statusId) = 0;
  virtual ViStatus AssertTrigger(ViSession vi, ViUInt16 protocol) = 0;
  virtual ViStatus AssertUtilSignal(ViSession vi, ViUInt16 mode) = 0;
  virtual ViStatus Clear(ViSession vi) = 0;
  virtual ViStatus Close(ViSession vi) = 0;
  virtual ViStatus CloseEvent(ViEvent eventHandle) = 0;
  virtual ViStatus DisableEvent(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism) = 0;
  virtual ViStatus DiscardEvents(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism) = 0;
  virtual ViStatus EnableEvent(ViSession vi, ViEventType eventType, ViUInt16 eventMechanism, ViEventFilter filterContext) = 0;
  virtual ViStatus FindNext(ViFindList findHandle, ViChar instrumentDescriptor[256]) = 0;
  virtual ViStatus FindRsrc(ViSession rsrcManagerHandle, ViConstString expression, ViFindList* findHandle, ViUInt32* returnCount, ViChar instrumentDescriptor[256]) = 0;
  virtual ViStatus Flush(ViSession vi, ViUInt16 mask) = 0;
  virtual ViStatus GetAttribute(ViSession vi, ViAttr attributeName, void* attributeValue) = 0;
  virtual ViStatus GetAttributeEvent(ViEvent eventHandle, ViAttr attributeName, void* attributeValue) = 0;
  virtual ViStatus GpibCommand(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount) = 0;
  virtual ViStatus GpibControlATN(ViSession vi, ViUInt16 mode) = 0;
  virtual ViStatus GpibControlREN(ViSession vi, ViUInt16 mode) = 0;
  virtual ViStatus GpibPassControl(ViSession vi, ViUInt16 primaryAddress, ViUInt16 secondaryAddress) = 0;
  virtual ViStatus GpibSendIFC(ViSession vi) = 0;
  virtual ViStatus In16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt16* value) = 0;
  virtual ViStatus In32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt32* value) = 0;
  virtual ViStatus In64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt64* value) = 0;
  virtual ViStatus In8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt8* value) = 0;
  virtual ViStatus Lock(ViSession vi, ViAccessMode lockType, ViUInt32 timeout, ViConstKeyId requestedKey, ViChar accessKey[256]) = 0;
  virtual ViStatus MapAddress(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize mapSize, ViBoolean ownerAccess, ViAddr suggestedAddress, ViAddr* address) = 0;
  virtual ViStatus MapTrigger(ViSession vi, ViInt16 triggerSource, ViInt16 triggerDestination, ViUInt16 mode) = 0;
  virtual ViStatus MemAlloc(ViSession vi, ViUInt32 size, ViBusAddress* offset) = 0;
  virtual ViStatus MemAllocEx(ViSession vi, ViBusSize size, ViBusAddress64* offset) = 0;
  virtual ViStatus MemFree(ViSession vi, ViBusAddress64 offset) = 0;
  virtual ViStatus MoveIn16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt16 buffer[]) = 0;
  virtual ViStatus MoveIn32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt32 buffer[]) = 0;
  virtual ViStatus MoveIn64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt64 buffer[]) = 0;
  virtual ViStatus MoveIn8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt8 buffer[]) = 0;
  virtual ViStatus MoveOut16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt16 buffer[]) = 0;
  virtual ViStatus MoveOut32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt32 buffer[]) = 0;
  virtual ViStatus MoveOut64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt64 buffer[]) = 0;
  virtual ViStatus MoveOut8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt8 buffer[]) = 0;
  virtual ViStatus Open(ViSession rsrcManagerHandle, ViConstRsrc instrumentDescriptor, ViAccessMode accessMode, ViUInt32 openTimeout, ViSession* vi) = 0;
  virtual ViStatus OpenDefaultRM(ViSession* rsrcManagerHandle) = 0;
  virtual ViStatus Out16(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt16 value) = 0;
  virtual ViStatus Out32(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt32 value) = 0;
  virtual ViStatus Out64(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt64 value) = 0;
  virtual ViStatus Out8(ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt8 value) = 0;
  virtual ViStatus ParseRsrc(ViSession sessionHandle, ViConstRsrc resourceName, ViUInt16* interfaceType, ViUInt16* interfaceNumber, ViChar resourceClass[256], ViChar expandedUnaliasedName[256], ViChar aliasIfExists[256]) = 0;
  virtual void Peek16(ViSession vi, ViAddr address, ViUInt16* value) = 0;
  virtual void Peek32(ViSession vi, ViAddr address, ViUInt32* value) = 0;
  virtual void Peek64(ViSession vi, ViAddr address, ViUInt64* value) = 0;
  virtual void Peek8(ViSession vi, ViAddr address, ViUInt8* value) = 0;
  virtual void Poke16(ViSession vi, ViAddr address, ViUInt16 value) = 0;
  virtual void Poke32(ViSession vi, ViAddr address, ViUInt32 value) = 0;
  virtual void Poke64(ViSession vi, ViAddr address, ViUInt64 value) = 0;
  virtual void Poke8(ViSession vi, ViAddr address, ViUInt8 value) = 0;
  virtual ViStatus PxiReserveTriggers(ViSession vi, ViInt16 cnt, ViInt16 trigBuses[], ViInt16 trigLines[], ViInt16* failureIndex) = 0;
  virtual ViStatus Read(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount) = 0;
  virtual ViStatus ReadAsync(ViSession vi, ViByte readBuffer[], ViUInt32 count, ViJobId* jobIdentifier) = 0;
  virtual ViStatus ReadSTB(ViSession vi, ViUInt16* statusByte) = 0;
  virtual ViStatus SetAttribute(ViSession vi, ViAttr attributeName, ViAttrState attributeValue) = 0;
  virtual ViStatus SetBuf(ViSession vi, ViUInt16 mask, ViUInt32 bufferSize) = 0;
  virtual ViStatus StatusDesc(ViSession vi, ViStatus statusValue, ViChar statusDescription[256]) = 0;
  virtual ViStatus Terminate(ViSession vi, ViUInt16 degree, ViJobId jobIdentifier) = 0;
  virtual ViStatus Unlock(ViSession vi) = 0;
  virtual ViStatus UnmapAddress(ViSession vi) = 0;
  virtual ViStatus UnmapTrigger(ViSession vi, ViInt16 triggerSource, ViInt16 triggerDestination) = 0;
  virtual ViStatus UsbControlIn(ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest, ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength, ViByte buffer[], ViUInt16* returnCount) = 0;
  virtual ViStatus UsbControlOut(ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest, ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength, ViByte buffer[]) = 0;
  virtual ViStatus VxiCommandQuery(ViSession vi, ViUInt16 mode, ViUInt32 command, ViUInt32* commandResponse) = 0;
  virtual ViStatus WaitOnEvent(ViSession vi, ViEventType inEventType, ViUInt32 timeout, ViEventType* outEventType, ViEvent* eventHandle) = 0;
  virtual ViStatus Write(ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount) = 0;
  virtual ViStatus WriteAsync(ViSession vi, ViByte buffer[], ViUInt32 count, ViJobId* jobIdentifier) = 0;
};

}  // namespace visa_grpc
#endif  // VISA_GRPC_LIBRARY_WRAPPER_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_mock_library.h sha256=9145d70fb7ee3491a511734abd70ae74297f52a3d30b77a0cdf319c5f5ff2756 bytes=8889 -->
## FILE: generated/visa/visa_mock_library.h

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_mock_library.h`
- sha256: `9145d70fb7ee3491a511734abd70ae74297f52a3d30b77a0cdf319c5f5ff2756`
- bytes: 8889

````c
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Mock of LibraryInterface for VISA
//---------------------------------------------------------------------
#ifndef VISA_GRPC_MOCK_LIBRARY_H
#define VISA_GRPC_MOCK_LIBRARY_H

#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "visa_library_interface.h"

namespace ni {
namespace tests {
namespace unit {

class VisaMockLibrary : public visa_grpc::VisaLibraryInterface {
 public:
  MOCK_METHOD(ViStatus, AssertIntrSignal, (ViSession vi, ViInt16 mode, ViUInt32 statusId), (override));
  MOCK_METHOD(ViStatus, AssertTrigger, (ViSession vi, ViUInt16 protocol), (override));
  MOCK_METHOD(ViStatus, AssertUtilSignal, (ViSession vi, ViUInt16 mode), (override));
  MOCK_METHOD(ViStatus, Clear, (ViSession vi), (override));
  MOCK_METHOD(ViStatus, Close, (ViSession vi), (override));
  MOCK_METHOD(ViStatus, CloseEvent, (ViEvent eventHandle), (override));
  MOCK_METHOD(ViStatus, DisableEvent, (ViSession vi, ViEventType eventType, ViUInt16 eventMechanism), (override));
  MOCK_METHOD(ViStatus, DiscardEvents, (ViSession vi, ViEventType eventType, ViUInt16 eventMechanism), (override));
  MOCK_METHOD(ViStatus, EnableEvent, (ViSession vi, ViEventType eventType, ViUInt16 eventMechanism, ViEventFilter filterContext), (override));
  MOCK_METHOD(ViStatus, FindNext, (ViFindList findHandle, ViChar instrumentDescriptor[256]), (override));
  MOCK_METHOD(ViStatus, FindRsrc, (ViSession rsrcManagerHandle, ViConstString expression, ViFindList* findHandle, ViUInt32* returnCount, ViChar instrumentDescriptor[256]), (override));
  MOCK_METHOD(ViStatus, Flush, (ViSession vi, ViUInt16 mask), (override));
  MOCK_METHOD(ViStatus, GetAttribute, (ViSession vi, ViAttr attributeName, void* attributeValue), (override));
  MOCK_METHOD(ViStatus, GetAttributeEvent, (ViEvent eventHandle, ViAttr attributeName, void* attributeValue), (override));
  MOCK_METHOD(ViStatus, GpibCommand, (ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount), (override));
  MOCK_METHOD(ViStatus, GpibControlATN, (ViSession vi, ViUInt16 mode), (override));
  MOCK_METHOD(ViStatus, GpibControlREN, (ViSession vi, ViUInt16 mode), (override));
  MOCK_METHOD(ViStatus, GpibPassControl, (ViSession vi, ViUInt16 primaryAddress, ViUInt16 secondaryAddress), (override));
  MOCK_METHOD(ViStatus, GpibSendIFC, (ViSession vi), (override));
  MOCK_METHOD(ViStatus, In16, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt16* value), (override));
  MOCK_METHOD(ViStatus, In32, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt32* value), (override));
  MOCK_METHOD(ViStatus, In64, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt64* value), (override));
  MOCK_METHOD(ViStatus, In8, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt8* value), (override));
  MOCK_METHOD(ViStatus, Lock, (ViSession vi, ViAccessMode lockType, ViUInt32 timeout, ViConstKeyId requestedKey, ViChar accessKey[256]), (override));
  MOCK_METHOD(ViStatus, MapAddress, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize mapSize, ViBoolean ownerAccess, ViAddr suggestedAddress, ViAddr* address), (override));
  MOCK_METHOD(ViStatus, MapTrigger, (ViSession vi, ViInt16 triggerSource, ViInt16 triggerDestination, ViUInt16 mode), (override));
  MOCK_METHOD(ViStatus, MemAlloc, (ViSession vi, ViUInt32 size, ViBusAddress* offset), (override));
  MOCK_METHOD(ViStatus, MemAllocEx, (ViSession vi, ViBusSize size, ViBusAddress64* offset), (override));
  MOCK_METHOD(ViStatus, MemFree, (ViSession vi, ViBusAddress64 offset), (override));
  MOCK_METHOD(ViStatus, MoveIn16, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt16 buffer[]), (override));
  MOCK_METHOD(ViStatus, MoveIn32, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt32 buffer[]), (override));
  MOCK_METHOD(ViStatus, MoveIn64, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt64 buffer[]), (override));
  MOCK_METHOD(ViStatus, MoveIn8, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt8 buffer[]), (override));
  MOCK_METHOD(ViStatus, MoveOut16, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt16 buffer[]), (override));
  MOCK_METHOD(ViStatus, MoveOut32, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt32 buffer[]), (override));
  MOCK_METHOD(ViStatus, MoveOut64, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt64 buffer[]), (override));
  MOCK_METHOD(ViStatus, MoveOut8, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViBusSize count, ViUInt8 buffer[]), (override));
  MOCK_METHOD(ViStatus, Open, (ViSession rsrcManagerHandle, ViConstRsrc instrumentDescriptor, ViAccessMode accessMode, ViUInt32 openTimeout, ViSession* vi), (override));
  MOCK_METHOD(ViStatus, OpenDefaultRM, (ViSession* rsrcManagerHandle), (override));
  MOCK_METHOD(ViStatus, Out16, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt16 value), (override));
  MOCK_METHOD(ViStatus, Out32, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt32 value), (override));
  MOCK_METHOD(ViStatus, Out64, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt64 value), (override));
  MOCK_METHOD(ViStatus, Out8, (ViSession vi, ViUInt16 addressSpace, ViBusAddress64 offset, ViUInt8 value), (override));
  MOCK_METHOD(ViStatus, ParseRsrc, (ViSession sessionHandle, ViConstRsrc resourceName, ViUInt16* interfaceType, ViUInt16* interfaceNumber, ViChar resourceClass[256], ViChar expandedUnaliasedName[256], ViChar aliasIfExists[256]), (override));
  MOCK_METHOD(void, Peek16, (ViSession vi, ViAddr address, ViUInt16* value), (override));
  MOCK_METHOD(void, Peek32, (ViSession vi, ViAddr address, ViUInt32* value), (override));
  MOCK_METHOD(void, Peek64, (ViSession vi, ViAddr address, ViUInt64* value), (override));
  MOCK_METHOD(void, Peek8, (ViSession vi, ViAddr address, ViUInt8* value), (override));
  MOCK_METHOD(void, Poke16, (ViSession vi, ViAddr address, ViUInt16 value), (override));
  MOCK_METHOD(void, Poke32, (ViSession vi, ViAddr address, ViUInt32 value), (override));
  MOCK_METHOD(void, Poke64, (ViSession vi, ViAddr address, ViUInt64 value), (override));
  MOCK_METHOD(void, Poke8, (ViSession vi, ViAddr address, ViUInt8 value), (override));
  MOCK_METHOD(ViStatus, PxiReserveTriggers, (ViSession vi, ViInt16 cnt, ViInt16 trigBuses[], ViInt16 trigLines[], ViInt16* failureIndex), (override));
  MOCK_METHOD(ViStatus, Read, (ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount), (override));
  MOCK_METHOD(ViStatus, ReadAsync, (ViSession vi, ViByte readBuffer[], ViUInt32 count, ViJobId* jobIdentifier), (override));
  MOCK_METHOD(ViStatus, ReadSTB, (ViSession vi, ViUInt16* statusByte), (override));
  MOCK_METHOD(ViStatus, SetAttribute, (ViSession vi, ViAttr attributeName, ViAttrState attributeValue), (override));
  MOCK_METHOD(ViStatus, SetBuf, (ViSession vi, ViUInt16 mask, ViUInt32 bufferSize), (override));
  MOCK_METHOD(ViStatus, StatusDesc, (ViSession vi, ViStatus statusValue, ViChar statusDescription[256]), (override));
  MOCK_METHOD(ViStatus, Terminate, (ViSession vi, ViUInt16 degree, ViJobId jobIdentifier), (override));
  MOCK_METHOD(ViStatus, Unlock, (ViSession vi), (override));
  MOCK_METHOD(ViStatus, UnmapAddress, (ViSession vi), (override));
  MOCK_METHOD(ViStatus, UnmapTrigger, (ViSession vi, ViInt16 triggerSource, ViInt16 triggerDestination), (override));
  MOCK_METHOD(ViStatus, UsbControlIn, (ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest, ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength, ViByte buffer[], ViUInt16* returnCount), (override));
  MOCK_METHOD(ViStatus, UsbControlOut, (ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest, ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength, ViByte buffer[]), (override));
  MOCK_METHOD(ViStatus, VxiCommandQuery, (ViSession vi, ViUInt16 mode, ViUInt32 command, ViUInt32* commandResponse), (override));
  MOCK_METHOD(ViStatus, WaitOnEvent, (ViSession vi, ViEventType inEventType, ViUInt32 timeout, ViEventType* outEventType, ViEvent* eventHandle), (override));
  MOCK_METHOD(ViStatus, Write, (ViSession vi, ViByte buffer[], ViUInt32 count, ViUInt32* returnCount), (override));
  MOCK_METHOD(ViStatus, WriteAsync, (ViSession vi, ViByte buffer[], ViUInt32 count, ViJobId* jobIdentifier), (override));
};

}  // namespace unit
}  // namespace tests
}  // namespace ni
#endif  // VISA_GRPC_MOCK_LIBRARY_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_service.cpp sha256=434b18eec0502d886dc61346d210c31110407ca6d5281fabcc56862e089d1857 bytes=81652 -->
## FILE: generated/visa/visa_service.cpp

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_service.cpp`
- sha256: `434b18eec0502d886dc61346d210c31110407ca6d5281fabcc56862e089d1857`
- bytes: 81652

````cpp

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service implementation for the VISA Metadata
//---------------------------------------------------------------------
#include "visa_service.h"

#include <sstream>
#include <fstream>
#include <iostream>
#include <atomic>
#include <vector>
#include <server/converters.h>

namespace visa_grpc {

  using nidevice_grpc::converters::allocate_output_storage;
  using nidevice_grpc::converters::calculate_linked_array_size;
  using nidevice_grpc::converters::convert_from_grpc;
  using nidevice_grpc::converters::convert_to_grpc;
  using nidevice_grpc::converters::MatchState;

  VisaService::VisaService(
      LibrarySharedPtr library,
      ResourceRepositorySharedPtr resource_repository,
      ViObjectResourceRepositorySharedPtr vi_object_resource_repository,
      const VisaFeatureToggles& feature_toggles)
      : library_(library),
      session_repository_(resource_repository),
      vi_object_resource_repository_(vi_object_resource_repository),
      feature_toggles_(feature_toggles)
  {
  }

  VisaService::~VisaService()
  {
  }

  // Returns true if it's safe to use outputs of a method with the given status.
  inline bool status_ok(int32 status)
  {
    return status >= 0;
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::AssertIntrSignal(::grpc::ServerContext* context, const AssertIntrSignalRequest* request, AssertIntrSignalResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViInt16 mode;
      switch (request->mode_enum_case()) {
        case visa_grpc::AssertIntrSignalRequest::ModeEnumCase::kMode: {
          mode = static_cast<ViInt16>(request->mode());
          break;
        }
        case visa_grpc::AssertIntrSignalRequest::ModeEnumCase::kModeRaw: {
          mode = static_cast<ViInt16>(request->mode_raw());
          break;
        }
        case visa_grpc::AssertIntrSignalRequest::ModeEnumCase::MODE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for mode was not specified or out of range");
          break;
        }
      }

      ViUInt32 status_id = request->status_id();
      auto status = library_->AssertIntrSignal(vi, mode, status_id);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::AssertTrigger(::grpc::ServerContext* context, const AssertTriggerRequest* request, AssertTriggerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 protocol;
      switch (request->protocol_enum_case()) {
        case visa_grpc::AssertTriggerRequest::ProtocolEnumCase::kProtocol: {
          protocol = static_cast<ViUInt16>(request->protocol());
          break;
        }
        case visa_grpc::AssertTriggerRequest::ProtocolEnumCase::kProtocolRaw: {
          protocol = static_cast<ViUInt16>(request->protocol_raw());
          break;
        }
        case visa_grpc::AssertTriggerRequest::ProtocolEnumCase::PROTOCOL_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for protocol was not specified or out of range");
          break;
        }
      }

      auto status = library_->AssertTrigger(vi, protocol);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::AssertUtilSignal(::grpc::ServerContext* context, const AssertUtilSignalRequest* request, AssertUtilSignalResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 mode;
      switch (request->mode_enum_case()) {
        case visa_grpc::AssertUtilSignalRequest::ModeEnumCase::kMode: {
          mode = static_cast<ViUInt16>(request->mode());
          break;
        }
        case visa_grpc::AssertUtilSignalRequest::ModeEnumCase::kModeRaw: {
          mode = static_cast<ViUInt16>(request->mode_raw());
          break;
        }
        case visa_grpc::AssertUtilSignalRequest::ModeEnumCase::MODE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for mode was not specified or out of range");
          break;
        }
      }

      auto status = library_->AssertUtilSignal(vi, mode);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Clear(::grpc::ServerContext* context, const ClearRequest* request, ClearResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      auto status = library_->Clear(vi);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Close(::grpc::ServerContext* context, const CloseRequest* request, CloseResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      session_repository_->remove_session(vi_grpc_session.name());
      auto status = library_->Close(vi);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::DisableEvent(::grpc::ServerContext* context, const DisableEventRequest* request, DisableEventResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViEventType event_type;
      switch (request->event_type_enum_case()) {
        case visa_grpc::DisableEventRequest::EventTypeEnumCase::kEventType: {
          event_type = static_cast<ViEventType>(request->event_type());
          break;
        }
        case visa_grpc::DisableEventRequest::EventTypeEnumCase::kEventTypeRaw: {
          event_type = static_cast<ViEventType>(request->event_type_raw());
          break;
        }
        case visa_grpc::DisableEventRequest::EventTypeEnumCase::EVENT_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for event_type was not specified or out of range");
          break;
        }
      }

      ViUInt16 event_mechanism;
      switch (request->event_mechanism_enum_case()) {
        case visa_grpc::DisableEventRequest::EventMechanismEnumCase::kEventMechanism: {
          event_mechanism = static_cast<ViUInt16>(request->event_mechanism());
          break;
        }
        case visa_grpc::DisableEventRequest::EventMechanismEnumCase::kEventMechanismRaw: {
          event_mechanism = static_cast<ViUInt16>(request->event_mechanism_raw());
          break;
        }
        case visa_grpc::DisableEventRequest::EventMechanismEnumCase::EVENT_MECHANISM_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for event_mechanism was not specified or out of range");
          break;
        }
      }

      auto status = library_->DisableEvent(vi, event_type, event_mechanism);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::DiscardEvents(::grpc::ServerContext* context, const DiscardEventsRequest* request, DiscardEventsResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViEventType event_type;
      switch (request->event_type_enum_case()) {
        case visa_grpc::DiscardEventsRequest::EventTypeEnumCase::kEventType: {
          event_type = static_cast<ViEventType>(request->event_type());
          break;
        }
        case visa_grpc::DiscardEventsRequest::EventTypeEnumCase::kEventTypeRaw: {
          event_type = static_cast<ViEventType>(request->event_type_raw());
          break;
        }
        case visa_grpc::DiscardEventsRequest::EventTypeEnumCase::EVENT_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for event_type was not specified or out of range");
          break;
        }
      }

      ViUInt16 event_mechanism;
      switch (request->event_mechanism_enum_case()) {
        case visa_grpc::DiscardEventsRequest::EventMechanismEnumCase::kEventMechanism: {
          event_mechanism = static_cast<ViUInt16>(request->event_mechanism());
          break;
        }
        case visa_grpc::DiscardEventsRequest::EventMechanismEnumCase::kEventMechanismRaw: {
          event_mechanism = static_cast<ViUInt16>(request->event_mechanism_raw());
          break;
        }
        case visa_grpc::DiscardEventsRequest::EventMechanismEnumCase::EVENT_MECHANISM_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for event_mechanism was not specified or out of range");
          break;
        }
      }

      auto status = library_->DiscardEvents(vi, event_type, event_mechanism);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::EnableEvent(::grpc::ServerContext* context, const EnableEventRequest* request, EnableEventResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViEventType event_type;
      switch (request->event_type_enum_case()) {
        case visa_grpc::EnableEventRequest::EventTypeEnumCase::kEventType: {
          event_type = static_cast<ViEventType>(request->event_type());
          break;
        }
        case visa_grpc::EnableEventRequest::EventTypeEnumCase::kEventTypeRaw: {
          event_type = static_cast<ViEventType>(request->event_type_raw());
          break;
        }
        case visa_grpc::EnableEventRequest::EventTypeEnumCase::EVENT_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for event_type was not specified or out of range");
          break;
        }
      }

      ViUInt16 event_mechanism;
      switch (request->event_mechanism_enum_case()) {
        case visa_grpc::EnableEventRequest::EventMechanismEnumCase::kEventMechanism: {
          event_mechanism = static_cast<ViUInt16>(request->event_mechanism());
          break;
        }
        case visa_grpc::EnableEventRequest::EventMechanismEnumCase::kEventMechanismRaw: {
          event_mechanism = static_cast<ViUInt16>(request->event_mechanism_raw());
          break;
        }
        case visa_grpc::EnableEventRequest::EventMechanismEnumCase::EVENT_MECHANISM_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for event_mechanism was not specified or out of range");
          break;
        }
      }

      ViEventFilter filter_context = request->filter_context();
      auto status = library_->EnableEvent(vi, event_type, event_mechanism, filter_context);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Flush(::grpc::ServerContext* context, const FlushRequest* request, FlushResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 mask;
      switch (request->mask_enum_case()) {
        case visa_grpc::FlushRequest::MaskEnumCase::kMask: {
          mask = static_cast<ViUInt16>(request->mask());
          break;
        }
        case visa_grpc::FlushRequest::MaskEnumCase::kMaskRaw: {
          mask = static_cast<ViUInt16>(request->mask_raw());
          break;
        }
        case visa_grpc::FlushRequest::MaskEnumCase::MASK_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for mask was not specified or out of range");
          break;
        }
      }

      auto status = library_->Flush(vi, mask);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::GpibCommand(::grpc::ServerContext* context, const GpibCommandRequest* request, GpibCommandResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViByte* buffer = (ViByte*)request->buffer().c_str();
      auto count_raw = request->buffer().size();
      ViUInt32 count = nidevice_grpc::converters::convert_size<ViUInt32>(count_raw, "count");
      ViUInt32 return_count {};
      auto status = library_->GpibCommand(vi, buffer, count, &return_count);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_return_count(return_count);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::GpibControlATN(::grpc::ServerContext* context, const GpibControlATNRequest* request, GpibControlATNResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 mode;
      switch (request->mode_enum_case()) {
        case visa_grpc::GpibControlATNRequest::ModeEnumCase::kMode: {
          mode = static_cast<ViUInt16>(request->mode());
          break;
        }
        case visa_grpc::GpibControlATNRequest::ModeEnumCase::kModeRaw: {
          mode = static_cast<ViUInt16>(request->mode_raw());
          break;
        }
        case visa_grpc::GpibControlATNRequest::ModeEnumCase::MODE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for mode was not specified or out of range");
          break;
        }
      }

      auto status = library_->GpibControlATN(vi, mode);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::GpibControlREN(::grpc::ServerContext* context, const GpibControlRENRequest* request, GpibControlRENResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 mode;
      switch (request->mode_enum_case()) {
        case visa_grpc::GpibControlRENRequest::ModeEnumCase::kMode: {
          mode = static_cast<ViUInt16>(request->mode());
          break;
        }
        case visa_grpc::GpibControlRENRequest::ModeEnumCase::kModeRaw: {
          mode = static_cast<ViUInt16>(request->mode_raw());
          break;
        }
        case visa_grpc::GpibControlRENRequest::ModeEnumCase::MODE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for mode was not specified or out of range");
          break;
        }
      }

      auto status = library_->GpibControlREN(vi, mode);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::GpibPassControl(::grpc::ServerContext* context, const GpibPassControlRequest* request, GpibPassControlResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 primary_address = request->primary_address();
      ViUInt16 secondary_address = request->secondary_address();
      auto status = library_->GpibPassControl(vi, primary_address, secondary_address);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::GpibSendIFC(::grpc::ServerContext* context, const GpibSendIFCRequest* request, GpibSendIFCResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      auto status = library_->GpibSendIFC(vi);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::In16(::grpc::ServerContext* context, const In16Request* request, In16Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::In16Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::In16Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::In16Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViUInt16 value {};
      auto status = library_->In16(vi, address_space, offset, &value);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_value(value);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::In32(::grpc::ServerContext* context, const In32Request* request, In32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::In32Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::In32Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::In32Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViUInt32 value {};
      auto status = library_->In32(vi, address_space, offset, &value);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_value(value);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::In64(::grpc::ServerContext* context, const In64Request* request, In64Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::In64Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::In64Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::In64Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViUInt64 value {};
      auto status = library_->In64(vi, address_space, offset, &value);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_value(value);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::In8(::grpc::ServerContext* context, const In8Request* request, In8Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::In8Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::In8Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::In8Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViUInt8 value {};
      auto status = library_->In8(vi, address_space, offset, &value);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_value(value);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Lock(::grpc::ServerContext* context, const LockRequest* request, LockResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViAccessMode lock_type;
      switch (request->lock_type_enum_case()) {
        case visa_grpc::LockRequest::LockTypeEnumCase::kLockType: {
          lock_type = static_cast<ViAccessMode>(request->lock_type());
          break;
        }
        case visa_grpc::LockRequest::LockTypeEnumCase::kLockTypeRaw: {
          lock_type = static_cast<ViAccessMode>(request->lock_type_raw());
          break;
        }
        case visa_grpc::LockRequest::LockTypeEnumCase::LOCK_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for lock_type was not specified or out of range");
          break;
        }
      }

      ViUInt32 timeout = request->timeout();
      auto requested_key_mbcs = convert_from_grpc<std::string>(request->requested_key());
      ViConstKeyId requested_key = (ViConstKeyId)requested_key_mbcs.c_str();
      std::string access_key(256 - 1, '\0');
      auto status = library_->Lock(vi, lock_type, timeout, requested_key, (ViChar*)access_key.data());
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      std::string access_key_utf8;
      convert_to_grpc(access_key, &access_key_utf8);
      response->set_access_key(access_key_utf8);
      nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_access_key()));
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MapAddress(::grpc::ServerContext* context, const MapAddressRequest* request, MapAddressResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::MapAddressRequest::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::MapAddressRequest::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::MapAddressRequest::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViBusSize map_size = request->map_size();
      ViBoolean owner_access = request->owner_access();
      ViAddr suggested_address = reinterpret_cast<ViAddr>(request->suggested_address());
      ViAddr address {};
      auto status = library_->MapAddress(vi, address_space, offset, map_size, owner_access, suggested_address, &address);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_address(reinterpret_cast<uint64_t>(address));
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MapTrigger(::grpc::ServerContext* context, const MapTriggerRequest* request, MapTriggerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViInt16 trigger_source;
      switch (request->trigger_source_enum_case()) {
        case visa_grpc::MapTriggerRequest::TriggerSourceEnumCase::kTriggerSource: {
          trigger_source = static_cast<ViInt16>(request->trigger_source());
          break;
        }
        case visa_grpc::MapTriggerRequest::TriggerSourceEnumCase::kTriggerSourceRaw: {
          trigger_source = static_cast<ViInt16>(request->trigger_source_raw());
          break;
        }
        case visa_grpc::MapTriggerRequest::TriggerSourceEnumCase::TRIGGER_SOURCE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for trigger_source was not specified or out of range");
          break;
        }
      }

      ViInt16 trigger_destination;
      switch (request->trigger_destination_enum_case()) {
        case visa_grpc::MapTriggerRequest::TriggerDestinationEnumCase::kTriggerDestination: {
          trigger_destination = static_cast<ViInt16>(request->trigger_destination());
          break;
        }
        case visa_grpc::MapTriggerRequest::TriggerDestinationEnumCase::kTriggerDestinationRaw: {
          trigger_destination = static_cast<ViInt16>(request->trigger_destination_raw());
          break;
        }
        case visa_grpc::MapTriggerRequest::TriggerDestinationEnumCase::TRIGGER_DESTINATION_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for trigger_destination was not specified or out of range");
          break;
        }
      }

      ViUInt16 mode = request->mode();
      auto status = library_->MapTrigger(vi, trigger_source, trigger_destination, mode);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MemAlloc(::grpc::ServerContext* context, const MemAllocRequest* request, MemAllocResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt32 size = request->size();
      ViBusAddress offset {};
      auto status = library_->MemAlloc(vi, size, &offset);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_offset(offset);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MemAllocEx(::grpc::ServerContext* context, const MemAllocExRequest* request, MemAllocExResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViBusSize size = request->size();
      ViBusAddress64 offset {};
      auto status = library_->MemAllocEx(vi, size, &offset);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_offset(offset);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MemFree(::grpc::ServerContext* context, const MemFreeRequest* request, MemFreeResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViBusAddress64 offset = request->offset();
      auto status = library_->MemFree(vi, offset);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MoveIn32(::grpc::ServerContext* context, const MoveIn32Request* request, MoveIn32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::MoveIn32Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::MoveIn32Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::MoveIn32Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViBusSize count = request->count();
      response->mutable_buffer()->Resize(count, 0);
      ViUInt32* buffer = reinterpret_cast<ViUInt32*>(response->mutable_buffer()->mutable_data());
      auto status = library_->MoveIn32(vi, address_space, offset, count, buffer);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MoveIn64(::grpc::ServerContext* context, const MoveIn64Request* request, MoveIn64Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::MoveIn64Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::MoveIn64Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::MoveIn64Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViBusSize count = request->count();
      response->mutable_buffer()->Resize(count, 0);
      ViUInt64* buffer = response->mutable_buffer()->mutable_data();
      auto status = library_->MoveIn64(vi, address_space, offset, count, buffer);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MoveIn8(::grpc::ServerContext* context, const MoveIn8Request* request, MoveIn8Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::MoveIn8Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::MoveIn8Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::MoveIn8Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViBusSize count = request->count();
      std::string buffer(count, '\0');
      auto status = library_->MoveIn8(vi, address_space, offset, count, (ViUInt8*)buffer.data());
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_buffer(buffer);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MoveOut16(::grpc::ServerContext* context, const MoveOut16Request* request, MoveOut16Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::MoveOut16Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::MoveOut16Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::MoveOut16Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      auto count_raw = request->buffer().size();
      ViBusSize count = nidevice_grpc::converters::convert_size<ViBusSize>(count_raw, "count");
      auto buffer_request = request->buffer();
      std::vector<ViUInt16> buffer;
      std::transform(
        buffer_request.begin(),
        buffer_request.end(),
        std::back_inserter(buffer),
        [](auto x) { return (ViUInt16)x; }); 
      auto status = library_->MoveOut16(vi, address_space, offset, count, buffer.data());
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MoveOut32(::grpc::ServerContext* context, const MoveOut32Request* request, MoveOut32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::MoveOut32Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::MoveOut32Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::MoveOut32Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      auto count_raw = request->buffer().size();
      ViBusSize count = nidevice_grpc::converters::convert_size<ViBusSize>(count_raw, "count");
      auto buffer = const_cast<ViUInt32*>(reinterpret_cast<const ViUInt32*>(request->buffer().data()));
      auto status = library_->MoveOut32(vi, address_space, offset, count, buffer);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MoveOut64(::grpc::ServerContext* context, const MoveOut64Request* request, MoveOut64Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::MoveOut64Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::MoveOut64Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::MoveOut64Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      auto count_raw = request->buffer().size();
      ViBusSize count = nidevice_grpc::converters::convert_size<ViBusSize>(count_raw, "count");
      auto buffer = const_cast<ViUInt64*>(request->buffer().data());
      auto status = library_->MoveOut64(vi, address_space, offset, count, buffer);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::MoveOut8(::grpc::ServerContext* context, const MoveOut8Request* request, MoveOut8Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::MoveOut8Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::MoveOut8Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::MoveOut8Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      auto count_raw = request->buffer().size();
      ViBusSize count = nidevice_grpc::converters::convert_size<ViBusSize>(count_raw, "count");
      ViUInt8* buffer = (ViUInt8*)request->buffer().c_str();
      auto status = library_->MoveOut8(vi, address_space, offset, count, buffer);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Out16(::grpc::ServerContext* context, const Out16Request* request, Out16Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::Out16Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::Out16Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::Out16Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViUInt16 value = request->value();
      auto status = library_->Out16(vi, address_space, offset, value);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Out32(::grpc::ServerContext* context, const Out32Request* request, Out32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::Out32Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::Out32Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::Out32Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViUInt32 value = request->value();
      auto status = library_->Out32(vi, address_space, offset, value);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Out64(::grpc::ServerContext* context, const Out64Request* request, Out64Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::Out64Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::Out64Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::Out64Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViUInt64 value = request->value();
      auto status = library_->Out64(vi, address_space, offset, value);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Out8(::grpc::ServerContext* context, const Out8Request* request, Out8Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 address_space;
      switch (request->address_space_enum_case()) {
        case visa_grpc::Out8Request::AddressSpaceEnumCase::kAddressSpace: {
          address_space = static_cast<ViUInt16>(request->address_space());
          break;
        }
        case visa_grpc::Out8Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
          address_space = static_cast<ViUInt16>(request->address_space_raw());
          break;
        }
        case visa_grpc::Out8Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
          break;
        }
      }

      ViBusAddress64 offset = request->offset();
      ViUInt8 value = request->value();
      auto status = library_->Out8(vi, address_space, offset, value);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Peek16(::grpc::ServerContext* context, const Peek16Request* request, Peek16Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViAddr address = reinterpret_cast<ViAddr>(request->address());
      ViUInt16 value {};
      library_->Peek16(vi, address, &value);
      auto status = 0;
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_value(value);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Peek32(::grpc::ServerContext* context, const Peek32Request* request, Peek32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViAddr address = reinterpret_cast<ViAddr>(request->address());
      ViUInt32 value {};
      library_->Peek32(vi, address, &value);
      auto status = 0;
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_value(value);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Peek64(::grpc::ServerContext* context, const Peek64Request* request, Peek64Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViAddr address = reinterpret_cast<ViAddr>(request->address());
      ViUInt64 value {};
      library_->Peek64(vi, address, &value);
      auto status = 0;
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_value(value);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Peek8(::grpc::ServerContext* context, const Peek8Request* request, Peek8Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViAddr address = reinterpret_cast<ViAddr>(request->address());
      ViUInt8 value {};
      library_->Peek8(vi, address, &value);
      auto status = 0;
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_value(value);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Poke16(::grpc::ServerContext* context, const Poke16Request* request, Poke16Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViAddr address = reinterpret_cast<ViAddr>(request->address());
      ViUInt16 value = request->value();
      library_->Poke16(vi, address, value);
      auto status = 0;
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Poke32(::grpc::ServerContext* context, const Poke32Request* request, Poke32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViAddr address = reinterpret_cast<ViAddr>(request->address());
      ViUInt32 value = request->value();
      library_->Poke32(vi, address, value);
      auto status = 0;
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Poke64(::grpc::ServerContext* context, const Poke64Request* request, Poke64Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViAddr address = reinterpret_cast<ViAddr>(request->address());
      ViUInt64 value = request->value();
      library_->Poke64(vi, address, value);
      auto status = 0;
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Poke8(::grpc::ServerContext* context, const Poke8Request* request, Poke8Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViAddr address = reinterpret_cast<ViAddr>(request->address());
      ViUInt8 value = request->value();
      library_->Poke8(vi, address, value);
      auto status = 0;
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::PxiReserveTriggers(::grpc::ServerContext* context, const PxiReserveTriggersRequest* request, PxiReserveTriggersResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      auto cnt_determine_from_sizes = std::array<int, 2>
      {
        request->trig_buses_size(),
        request->trig_lines_size()
      };
      const auto cnt_size_calculation = calculate_linked_array_size(cnt_determine_from_sizes, false);

      if (cnt_size_calculation.match_state == MatchState::MISMATCH) {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The sizes of linked repeated fields [trig_buses, trig_lines] do not match");
      }
      auto cnt = cnt_size_calculation.size;

      auto trig_buses_request = request->trig_buses();
      std::vector<ViInt16> trig_buses;
      std::transform(
        trig_buses_request.begin(),
        trig_buses_request.end(),
        std::back_inserter(trig_buses),
        [](auto x) { return (ViInt16)x; }); 
      auto trig_lines_request = request->trig_lines();
      std::vector<ViInt16> trig_lines;
      std::transform(
        trig_lines_request.begin(),
        trig_lines_request.end(),
        std::back_inserter(trig_lines),
        [](auto x) { return (ViInt16)x; }); 
      ViInt16 failure_index {};
      auto status = library_->PxiReserveTriggers(vi, cnt, trig_buses.data(), trig_lines.data(), &failure_index);
      context->AddTrailingMetadata("ni-failure-index", std::to_string(failure_index));
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::ReadSTB(::grpc::ServerContext* context, const ReadSTBRequest* request, ReadSTBResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 status_byte {};
      auto status = library_->ReadSTB(vi, &status_byte);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_status_byte(status_byte);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::SetBuf(::grpc::ServerContext* context, const SetBufRequest* request, SetBufResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 mask;
      switch (request->mask_enum_case()) {
        case visa_grpc::SetBufRequest::MaskEnumCase::kMask: {
          mask = static_cast<ViUInt16>(request->mask());
          break;
        }
        case visa_grpc::SetBufRequest::MaskEnumCase::kMaskRaw: {
          mask = static_cast<ViUInt16>(request->mask_raw());
          break;
        }
        case visa_grpc::SetBufRequest::MaskEnumCase::MASK_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for mask was not specified or out of range");
          break;
        }
      }

      ViUInt32 buffer_size = request->buffer_size();
      auto status = library_->SetBuf(vi, mask, buffer_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::StatusDesc(::grpc::ServerContext* context, const StatusDescRequest* request, StatusDescResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViStatus status_value = request->status_value();
      std::string status_description(256 - 1, '\0');
      auto status = library_->StatusDesc(vi, status_value, (ViChar*)status_description.data());
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      std::string status_description_utf8;
      convert_to_grpc(status_description, &status_description_utf8);
      response->set_status_description(status_description_utf8);
      nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_status_description()));
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Terminate(::grpc::ServerContext* context, const TerminateRequest* request, TerminateResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 degree = request->degree();
      ViJobId job_identifier = request->job_identifier();
      auto status = library_->Terminate(vi, degree, job_identifier);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Unlock(::grpc::ServerContext* context, const UnlockRequest* request, UnlockResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      auto status = library_->Unlock(vi);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::UnmapAddress(::grpc::ServerContext* context, const UnmapAddressRequest* request, UnmapAddressResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      auto status = library_->UnmapAddress(vi);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::UnmapTrigger(::grpc::ServerContext* context, const UnmapTriggerRequest* request, UnmapTriggerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViInt16 trigger_source;
      switch (request->trigger_source_enum_case()) {
        case visa_grpc::UnmapTriggerRequest::TriggerSourceEnumCase::kTriggerSource: {
          trigger_source = static_cast<ViInt16>(request->trigger_source());
          break;
        }
        case visa_grpc::UnmapTriggerRequest::TriggerSourceEnumCase::kTriggerSourceRaw: {
          trigger_source = static_cast<ViInt16>(request->trigger_source_raw());
          break;
        }
        case visa_grpc::UnmapTriggerRequest::TriggerSourceEnumCase::TRIGGER_SOURCE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for trigger_source was not specified or out of range");
          break;
        }
      }

      ViInt16 trigger_destination;
      switch (request->trigger_destination_enum_case()) {
        case visa_grpc::UnmapTriggerRequest::TriggerDestinationEnumCase::kTriggerDestination: {
          trigger_destination = static_cast<ViInt16>(request->trigger_destination());
          break;
        }
        case visa_grpc::UnmapTriggerRequest::TriggerDestinationEnumCase::kTriggerDestinationRaw: {
          trigger_destination = static_cast<ViInt16>(request->trigger_destination_raw());
          break;
        }
        case visa_grpc::UnmapTriggerRequest::TriggerDestinationEnumCase::TRIGGER_DESTINATION_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for trigger_destination was not specified or out of range");
          break;
        }
      }

      auto status = library_->UnmapTrigger(vi, trigger_source, trigger_destination);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::UsbControlOut(::grpc::ServerContext* context, const UsbControlOutRequest* request, UsbControlOutResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViInt16 bm_request_type = static_cast<ViInt16>(request->bm_request_type());
      ViInt16 b_request = static_cast<ViInt16>(request->b_request());
      ViUInt16 w_value = request->w_value();
      ViUInt16 w_index = request->w_index();
      auto w_length_raw = request->buffer().size();
      ViUInt16 w_length = nidevice_grpc::converters::convert_size<ViUInt16>(w_length_raw, "w_length");
      ViByte* buffer = (ViByte*)request->buffer().c_str();
      auto status = library_->UsbControlOut(vi, bm_request_type, b_request, w_value, w_index, w_length, buffer);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::VxiCommandQuery(::grpc::ServerContext* context, const VxiCommandQueryRequest* request, VxiCommandQueryResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViUInt16 mode;
      switch (request->mode_enum_case()) {
        case visa_grpc::VxiCommandQueryRequest::ModeEnumCase::kMode: {
          mode = static_cast<ViUInt16>(request->mode());
          break;
        }
        case visa_grpc::VxiCommandQueryRequest::ModeEnumCase::kModeRaw: {
          mode = static_cast<ViUInt16>(request->mode_raw());
          break;
        }
        case visa_grpc::VxiCommandQueryRequest::ModeEnumCase::MODE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for mode was not specified or out of range");
          break;
        }
      }

      ViUInt32 command = request->command();
      ViUInt32 command_response {};
      auto status = library_->VxiCommandQuery(vi, mode, command, &command_response);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_command_response(command_response);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status VisaService::Write(::grpc::ServerContext* context, const WriteRequest* request, WriteResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto vi_grpc_session = request->vi();
      ViSession vi = session_repository_->access_session(vi_grpc_session.name());
      ViByte* buffer = (ViByte*)request->buffer().c_str();
      auto count_raw = request->buffer().size();
      ViUInt32 count = nidevice_grpc::converters::convert_size<ViUInt32>(count_raw, "count");
      ViUInt32 return_count {};
      auto status = library_->Write(vi, buffer, count, &return_count);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->set_return_count(return_count);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }


  VisaFeatureToggles::VisaFeatureToggles(
    const nidevice_grpc::FeatureToggles& feature_toggles)
    : is_enabled(
        feature_toggles.is_feature_enabled("visa", CodeReadiness::kRelease))
  {
  }
} // namespace visa_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_service.h sha256=79b3be552a17f2dacb47bdb9d6bf24340a2007d6499a7ec70249fb0bdaf945f2 bytes=10980 -->
## FILE: generated/visa/visa_service.h

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_service.h`
- sha256: `79b3be552a17f2dacb47bdb9d6bf24340a2007d6499a7ec70249fb0bdaf945f2`
- bytes: 10980

````c

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service header for the VISA Metadata
//---------------------------------------------------------------------
#ifndef VISA_GRPC_SERVICE_H
#define VISA_GRPC_SERVICE_H

#include <visa.grpc.pb.h>
#include <condition_variable>
#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>
#include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <map>
#include <server/converters.h>
#include <server/feature_toggles.h>
#include <server/session_resource_repository.h>
#include <server/shared_library.h>
#include <server/exceptions.h>

#include "visa_library_interface.h"

namespace visa_grpc {

struct VisaFeatureToggles
{
  using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;
  VisaFeatureToggles(const nidevice_grpc::FeatureToggles& feature_toggles = {});

  bool is_enabled;
};

class VisaService final : public Visa::Service {
public:
  using LibrarySharedPtr = std::shared_ptr<VisaLibraryInterface>;
  using ResourceRepositorySharedPtr = std::shared_ptr<nidevice_grpc::SessionResourceRepository<ViSession>>;
  using ViObjectResourceRepositorySharedPtr = std::shared_ptr<nidevice_grpc::SessionResourceRepository<ViObject>>;

  VisaService(
    LibrarySharedPtr library,
    ResourceRepositorySharedPtr resource_repository,
    ViObjectResourceRepositorySharedPtr vi_object_resource_repository,
    const VisaFeatureToggles& feature_toggles = {});
  virtual ~VisaService();

  ::grpc::Status AssertIntrSignal(::grpc::ServerContext* context, const AssertIntrSignalRequest* request, AssertIntrSignalResponse* response) override;
  ::grpc::Status AssertTrigger(::grpc::ServerContext* context, const AssertTriggerRequest* request, AssertTriggerResponse* response) override;
  ::grpc::Status AssertUtilSignal(::grpc::ServerContext* context, const AssertUtilSignalRequest* request, AssertUtilSignalResponse* response) override;
  ::grpc::Status Clear(::grpc::ServerContext* context, const ClearRequest* request, ClearResponse* response) override;
  ::grpc::Status Close(::grpc::ServerContext* context, const CloseRequest* request, CloseResponse* response) override;
  ::grpc::Status CloseEvent(::grpc::ServerContext* context, const CloseEventRequest* request, CloseEventResponse* response) override;
  ::grpc::Status DisableEvent(::grpc::ServerContext* context, const DisableEventRequest* request, DisableEventResponse* response) override;
  ::grpc::Status DiscardEvents(::grpc::ServerContext* context, const DiscardEventsRequest* request, DiscardEventsResponse* response) override;
  ::grpc::Status EnableEvent(::grpc::ServerContext* context, const EnableEventRequest* request, EnableEventResponse* response) override;
  ::grpc::Status FindRsrc(::grpc::ServerContext* context, const FindRsrcRequest* request, FindRsrcResponse* response) override;
  ::grpc::Status Flush(::grpc::ServerContext* context, const FlushRequest* request, FlushResponse* response) override;
  ::grpc::Status GetAttribute(::grpc::ServerContext* context, const GetAttributeRequest* request, GetAttributeResponse* response) override;
  ::grpc::Status GetAttributeEvent(::grpc::ServerContext* context, const GetAttributeEventRequest* request, GetAttributeEventResponse* response) override;
  ::grpc::Status GpibCommand(::grpc::ServerContext* context, const GpibCommandRequest* request, GpibCommandResponse* response) override;
  ::grpc::Status GpibControlATN(::grpc::ServerContext* context, const GpibControlATNRequest* request, GpibControlATNResponse* response) override;
  ::grpc::Status GpibControlREN(::grpc::ServerContext* context, const GpibControlRENRequest* request, GpibControlRENResponse* response) override;
  ::grpc::Status GpibPassControl(::grpc::ServerContext* context, const GpibPassControlRequest* request, GpibPassControlResponse* response) override;
  ::grpc::Status GpibSendIFC(::grpc::ServerContext* context, const GpibSendIFCRequest* request, GpibSendIFCResponse* response) override;
  ::grpc::Status In16(::grpc::ServerContext* context, const In16Request* request, In16Response* response) override;
  ::grpc::Status In32(::grpc::ServerContext* context, const In32Request* request, In32Response* response) override;
  ::grpc::Status In64(::grpc::ServerContext* context, const In64Request* request, In64Response* response) override;
  ::grpc::Status In8(::grpc::ServerContext* context, const In8Request* request, In8Response* response) override;
  ::grpc::Status Lock(::grpc::ServerContext* context, const LockRequest* request, LockResponse* response) override;
  ::grpc::Status MapAddress(::grpc::ServerContext* context, const MapAddressRequest* request, MapAddressResponse* response) override;
  ::grpc::Status MapTrigger(::grpc::ServerContext* context, const MapTriggerRequest* request, MapTriggerResponse* response) override;
  ::grpc::Status MemAlloc(::grpc::ServerContext* context, const MemAllocRequest* request, MemAllocResponse* response) override;
  ::grpc::Status MemAllocEx(::grpc::ServerContext* context, const MemAllocExRequest* request, MemAllocExResponse* response) override;
  ::grpc::Status MemFree(::grpc::ServerContext* context, const MemFreeRequest* request, MemFreeResponse* response) override;
  ::grpc::Status MoveIn16(::grpc::ServerContext* context, const MoveIn16Request* request, MoveIn16Response* response) override;
  ::grpc::Status MoveIn32(::grpc::ServerContext* context, const MoveIn32Request* request, MoveIn32Response* response) override;
  ::grpc::Status MoveIn64(::grpc::ServerContext* context, const MoveIn64Request* request, MoveIn64Response* response) override;
  ::grpc::Status MoveIn8(::grpc::ServerContext* context, const MoveIn8Request* request, MoveIn8Response* response) override;
  ::grpc::Status MoveOut16(::grpc::ServerContext* context, const MoveOut16Request* request, MoveOut16Response* response) override;
  ::grpc::Status MoveOut32(::grpc::ServerContext* context, const MoveOut32Request* request, MoveOut32Response* response) override;
  ::grpc::Status MoveOut64(::grpc::ServerContext* context, const MoveOut64Request* request, MoveOut64Response* response) override;
  ::grpc::Status MoveOut8(::grpc::ServerContext* context, const MoveOut8Request* request, MoveOut8Response* response) override;
  ::grpc::Status Open(::grpc::ServerContext* context, const OpenRequest* request, OpenResponse* response) override;
  ::grpc::Status Out16(::grpc::ServerContext* context, const Out16Request* request, Out16Response* response) override;
  ::grpc::Status Out32(::grpc::ServerContext* context, const Out32Request* request, Out32Response* response) override;
  ::grpc::Status Out64(::grpc::ServerContext* context, const Out64Request* request, Out64Response* response) override;
  ::grpc::Status Out8(::grpc::ServerContext* context, const Out8Request* request, Out8Response* response) override;
  ::grpc::Status ParseRsrc(::grpc::ServerContext* context, const ParseRsrcRequest* request, ParseRsrcResponse* response) override;
  ::grpc::Status Peek16(::grpc::ServerContext* context, const Peek16Request* request, Peek16Response* response) override;
  ::grpc::Status Peek32(::grpc::ServerContext* context, const Peek32Request* request, Peek32Response* response) override;
  ::grpc::Status Peek64(::grpc::ServerContext* context, const Peek64Request* request, Peek64Response* response) override;
  ::grpc::Status Peek8(::grpc::ServerContext* context, const Peek8Request* request, Peek8Response* response) override;
  ::grpc::Status Poke16(::grpc::ServerContext* context, const Poke16Request* request, Poke16Response* response) override;
  ::grpc::Status Poke32(::grpc::ServerContext* context, const Poke32Request* request, Poke32Response* response) override;
  ::grpc::Status Poke64(::grpc::ServerContext* context, const Poke64Request* request, Poke64Response* response) override;
  ::grpc::Status Poke8(::grpc::ServerContext* context, const Poke8Request* request, Poke8Response* response) override;
  ::grpc::Status PxiReserveTriggers(::grpc::ServerContext* context, const PxiReserveTriggersRequest* request, PxiReserveTriggersResponse* response) override;
  ::grpc::Status Read(::grpc::ServerContext* context, const ReadRequest* request, ReadResponse* response) override;
  ::grpc::Status ReadAsync(::grpc::ServerContext* context, const ReadAsyncRequest* request, ReadAsyncResponse* response) override;
  ::grpc::Status ReadSTB(::grpc::ServerContext* context, const ReadSTBRequest* request, ReadSTBResponse* response) override;
  ::grpc::Status SetAttribute(::grpc::ServerContext* context, const SetAttributeRequest* request, SetAttributeResponse* response) override;
  ::grpc::Status SetBuf(::grpc::ServerContext* context, const SetBufRequest* request, SetBufResponse* response) override;
  ::grpc::Status StatusDesc(::grpc::ServerContext* context, const StatusDescRequest* request, StatusDescResponse* response) override;
  ::grpc::Status Terminate(::grpc::ServerContext* context, const TerminateRequest* request, TerminateResponse* response) override;
  ::grpc::Status Unlock(::grpc::ServerContext* context, const UnlockRequest* request, UnlockResponse* response) override;
  ::grpc::Status UnmapAddress(::grpc::ServerContext* context, const UnmapAddressRequest* request, UnmapAddressResponse* response) override;
  ::grpc::Status UnmapTrigger(::grpc::ServerContext* context, const UnmapTriggerRequest* request, UnmapTriggerResponse* response) override;
  ::grpc::Status UsbControlIn(::grpc::ServerContext* context, const UsbControlInRequest* request, UsbControlInResponse* response) override;
  ::grpc::Status UsbControlOut(::grpc::ServerContext* context, const UsbControlOutRequest* request, UsbControlOutResponse* response) override;
  ::grpc::Status VxiCommandQuery(::grpc::ServerContext* context, const VxiCommandQueryRequest* request, VxiCommandQueryResponse* response) override;
  ::grpc::Status WaitOnEvent(::grpc::ServerContext* context, const WaitOnEventRequest* request, WaitOnEventResponse* response) override;
  ::grpc::Status Write(::grpc::ServerContext* context, const WriteRequest* request, WriteResponse* response) override;
  ::grpc::Status WriteAsync(::grpc::ServerContext* context, const WriteAsyncRequest* request, WriteAsyncResponse* response) override;
private:
  LibrarySharedPtr library_;
  ResourceRepositorySharedPtr session_repository_;
  ViObjectResourceRepositorySharedPtr vi_object_resource_repository_;
  ::grpc::Status ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi);
  ::grpc::Status ConvertApiErrorStatusForViObject(::grpc::ServerContextBase* context, int32_t status, ViObject vi);

  VisaFeatureToggles feature_toggles_;
};

} // namespace visa_grpc

#endif  // VISA_GRPC_SERVICE_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_service_registrar.cpp sha256=e482a67ab00b095f7da158f2733b942ebb1d33b2bbeb98194b538ce01e86ece2 bytes=1254 -->
## FILE: generated/visa/visa_service_registrar.cpp

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_service_registrar.cpp`
- sha256: `e482a67ab00b095f7da158f2733b942ebb1d33b2bbeb98194b538ce01e86ece2`
- bytes: 1254

````cpp

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service registrar implementation for the VISA Metadata
//---------------------------------------------------------------------
#include "visa_library.h"

#include <grpcpp/server_builder.h>

#include "visa_service.h"
#include "visa_service_registrar.h"

namespace visa_grpc {

std::shared_ptr<void> register_service(
  grpc::ServerBuilder& builder,
  const std::shared_ptr<nidevice_grpc::SessionResourceRepository<ViSession>>& resource_repository,
  const std::shared_ptr<nidevice_grpc::SessionResourceRepository<ViObject>>& vi_object_resource_repository,
  const nidevice_grpc::FeatureToggles& feature_toggles)
{
  auto toggles = VisaFeatureToggles(feature_toggles);

  if (toggles.is_enabled)
  {
    auto library = std::make_shared<VisaLibrary>();
    auto service = std::make_shared<VisaService>(
      library,
      resource_repository,
      vi_object_resource_repository,
      toggles);
    builder.RegisterService(service.get());
    return service;
  }

  return {};
}

} // visa_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/visa/visa_service_registrar.h sha256=67b0feaabf7a521900b7a3e1181e064344a78f7d8adbdea04e603d619eb3f0c9 bytes=1130 -->
## FILE: generated/visa/visa_service_registrar.h

- repository: `ni/grpc-device`
- source_path: `generated/visa/visa_service_registrar.h`
- sha256: `67b0feaabf7a521900b7a3e1181e064344a78f7d8adbdea04e603d619eb3f0c9`
- bytes: 1130

````c

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service registrar header for the VISA Metadata
//---------------------------------------------------------------------
#ifndef VISA_GRPC_SERVICE_REGISTRAR_H
#define VISA_GRPC_SERVICE_REGISTRAR_H
#include <server/feature_toggles.h>
#include <server/session_resource_repository.h>

#include <memory>

#include <visa.h> // for ViSession, ViObject

namespace grpc {
class ServerBuilder;
}

namespace visa_grpc {
using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;

std::shared_ptr<void> register_service(
  grpc::ServerBuilder& server_builder, 
  const std::shared_ptr<nidevice_grpc::SessionResourceRepository<ViSession>>& resource_repository,
  const std::shared_ptr<nidevice_grpc::SessionResourceRepository<ViObject>>& vi_object_resource_repository,
  const nidevice_grpc::FeatureToggles& feature_toggles);

} // visa_grpc

#endif  // VISA_GRPC_SERVICE_REGISTRAR_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/ivi.h sha256=258f52fd1f5c6361925a099873f129d837b192223e71dc9ae6927648b0274f4c bytes=119433 -->
## FILE: imports/include/ivi.h

- repository: `ni/grpc-device`
- source_path: `imports/include/ivi.h`
- sha256: `258f52fd1f5c6361925a099873f129d837b192223e71dc9ae6927648b0274f4c`
- bytes: 119433

````c
/*============================================================================*/
/*                               I V I                                        */
/*----------------------------------------------------------------------------*/
/*    Copyright (c) 1998-2020 National Instruments.  All Rights Reserved.     */
/*----------------------------------------------------------------------------*/
/*                                                                            */
/* Title:       ivi.h                                                         */
/* Purpose:     Declarations for the Interchangeable Virtual Instruments      */
/*              (IVI) Library.                                                */
/*                                                                            */
/*============================================================================*/

/* This is intentionally placed outside of the include guard so that customers
 * can include driver headers in any order, even if some drivers do not want to
 * include VISA headers and others do.
 */
#ifndef IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include "visa.h"
#endif

#ifndef IVI_HEADER
#define IVI_HEADER

#include "IviVisaType.h"

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#ifdef __cplusplus
    extern "C" {
#endif

/* Define IVI development environment */
#ifdef _VI_INT64_UINT64_DEFINED
#define _IVI_64BIT_ATTR_DEFINED_
#endif

#ifndef IviDll
#define IviDll
#endif

/*****************************************************************************/
/* Useful constants                                                 ======== */
/*****************************************************************************/
#define IVI_ENGINE_MAJOR_VERSION        20
#define IVI_ENGINE_MINOR_VERSION        0

#define IVI_VIREAL64_MAX        1.79769313486231570814527423732e+308  /* Maximum possible ViReal64 value */
#define IVI_VIREAL64_MAX_NEG    (-IVI_VIREAL64_MAX)                   /* Maximum possible negative ViReal64 value */

    /* Defined values for powerline frequency */
#define IVI_VAL_50_HERTZ                50.0
#define IVI_VAL_60_HERTZ                60.0
#define IVI_VAL_400_HERTZ               400.0

    /* Defined values for I/O Session Type    */
#define IVI_VAL_VISA_SESSION_TYPE       "VISA"
#define IVI_VAL_NI4882_SESSION_TYPE     "NI-488.2"
#define IVI_VAL_NIVXI_SESSION_TYPE      "NI-VXI"
#define IVI_VAL_NIDAQ_SESSION_TYPE      "NI-DAQ"
#define IVI_VAL_NISERIAL_SESSION_TYPE   "NI-Serial"

#define IVI_MAX_MESSAGE_LEN             255
#define IVI_MAX_MESSAGE_BUF_SIZE        (IVI_MAX_MESSAGE_LEN + 1)

#define IVI_VAL_NO_WAIT                 0
#define IVI_VAL_WAIT_FOREVER            IVI_VIREAL64_MAX

/* Duplicated from visa.h to ensure that visa.h is not a required header file */
#ifndef VI_TMO_INFINITE
#define VI_TMO_INFINITE             (0xFFFFFFFFUL)
#endif

#ifndef VI_TMO_IMMEDIATE
#define VI_TMO_IMMEDIATE            (0L)
#endif

#define IVI_VAL_MAX_TIME_INFINITE       VI_TMO_INFINITE
#define IVI_VAL_MAX_TIME_IMMEDIATE      VI_TMO_IMMEDIATE

#define IVI_MAX_PATHNAME_LEN    260   /* includes nul byte */
#define IVI_MAX_DRIVENAME_LEN     3   /* includes nul byte */
#define IVI_MAX_DIRNAME_LEN     256   /* includes nul byte */
#define IVI_MAX_FILENAME_LEN    256   /* includes nul byte */

/* Duplicated from visa.h to ensure that visa.h is not a required header file */
#define VI_ERROR_ALLOC            (_VI_ERROR+0x3FFF003CL)

/*****************************************************************************/

#define IVI_VAL_TYPE_NORMAL     0
#define IVI_VAL_TYPE_NAN        1
#define IVI_VAL_TYPE_PINF       2
#define IVI_VAL_TYPE_NINF       3

#define IVI_VAL_NAN             (*Ivi_GetPtrToSpecialViReal64Value(IVI_VAL_TYPE_NAN))
#define IVI_VAL_PINF            (*Ivi_GetPtrToSpecialViReal64Value(IVI_VAL_TYPE_PINF))
#define IVI_VAL_NINF            (*Ivi_GetPtrToSpecialViReal64Value(IVI_VAL_TYPE_NINF))

/*****************************************************************************/
/*  Interchange Warning Codes: The Ivi_GetNextInterchangeWarning function    */
/*  returns these values to identify the type of interchangeability warning. */
/*****************************************************************************/

#define IVI_VAL_NOT_IN_USER_SPECIFIED_STATE             1
#define IVI_VAL_READ_ONLY_ATTR_SET_BY_USER              2
#define IVI_VAL_ATTR_SET_TO_INSTR_SPECIFIC_VALUE        3
#define IVI_VAL_FAILURE_APPLYING_UNUSED_EXTENSION_VALUE 4
#define IVI_VAL_CLASS_DEFINED_INTERCHANGE_WARNING       5

/*****************************************************************************/

#ifndef _VI_CONST_STRING_DEFINED
typedef const ViChar * ViConstString;
#define _VI_CONST_STRING_DEFINED
#endif

/*****************************************************************************/
/*= Typedefs and related constants for the range tables             ======== */
/*****************************************************************************/

/* Defined values for the type of IviRangeTable */
#define IVI_VAL_DISCRETE            0       /* Discrete set - discreteOrMinValue, and cmdString (or cmdValue) fields used */
#define IVI_VAL_RANGED              1       /* Ranged value - discreteOrMinValue, maxValue, and cmdString (or cmdValue) fields used */
#define IVI_VAL_COERCED             2       /* Coerced value - discreteOrMinValue, maxValue, coercedValue, and cmdString (or cmdValue) fields used */

typedef struct      /* IviRangeTable contains an array of IviRangeTableEntry structures */
{
    ViReal64     discreteOrMinValue;
    ViReal64     maxValue;
    ViReal64     coercedValue;
    ViString     cmdString;          /* optional */
    ViInt32      cmdValue;           /* optional */
} IviRangeTableEntry;

#ifdef _IVI_64BIT_ATTR_DEFINED_
typedef struct      /* IviRangeTable contains an array of IviRangeTableEntry structures */
{
    ViInt64     discreteOrMinValue;
    ViInt64     maxValue;
    ViInt64     coercedValue;
    ViString    cmdString;          /* optional */
    ViInt32     cmdValue;           /* optional */
} IviRangeTableEntryViInt64;
#endif

typedef struct
    {
    ViInt32                     type;
    ViBoolean                   hasMin;
    ViBoolean                   hasMax;
    /* The hasMin and hasMax fields are used by the                      */
    /* Ivi_GetAttrMinMaxViInt32 and Ivi_GetAttrMinMaxViReal64 functions  */
    /* to determine whether they can calculate the minimum and maximum   */
    /* values that the instrument implements for an attribute.           */
    /* They are NOT used to indicate the inclusion or exclusion of the   */
    /* boundary value in the range                                       */
    ViString                    customInfo;
    void*                       rangeValues;
    /* the end of rangeValues[] is marked by the entry  */
    /* IVI_RANGE_TABLE_LAST_ENTRY                       */
    /*                                                  */
    } IviRangeTable;

typedef IviRangeTable*  IviRangeTablePtr;

typedef void* IviConfigStoreHandle;

#define IVI_RANGE_TABLE_END_STRING      ((ViString)(-1))  /* The value for the command string of the last entry in an IviRangeTable */
#define IVI_RANGE_TABLE_LAST_ENTRY      VI_NULL, VI_NULL, VI_NULL, IVI_RANGE_TABLE_END_STRING, VI_NULL  /* Marks the last entry in an IviRangeTable */

/*****************************************************************************/
/*= Typedefs for string-value tables.                              ========= */
/*****************************************************************************/
typedef struct
    {
    ViInt32     value;
    ViString    string;
    } IviStringValueEntry;

typedef IviStringValueEntry IviStringValueTable[];

/*****************************************************************************/
/*= Typedef and related constants for the IVI attribute flags.     ========= */
/*= The flags determine how the attributes operate.                ========= */
/*****************************************************************************/
typedef ViInt32 IviAttrFlags;

#define IVI_VAL_NOT_SUPPORTED                (1L << 0)  /* attribute automatically returns IVI_ERROR_ATTRIBUTE_NOT_SUPPORTED when Set/Get/Checked/Invalidated */
#define IVI_VAL_NOT_READABLE                 (1L << 1)  /* attribute cannot be Got */
#define IVI_VAL_NOT_WRITABLE                 (1L << 2)  /* attribute cannot be Set */
#define IVI_VAL_NOT_USER_READABLE            (1L << 3)  /* attribute cannot be Got by end-user */
#define IVI_VAL_NOT_USER_WRITABLE            (1L << 4)  /* attribute cannot be Set by end-user */
#define IVI_VAL_NEVER_CACHE                  (1L << 5)  /* always write/read to set/get attribute, i.e., never use a cached value, regardless of the state of IVI_ATTR_CACHE */
#define IVI_VAL_ALWAYS_CACHE                 (1L << 6)  /* specifies to always cache the value, regardless of the state of IVI_ATTR_CACHE */
#define IVI_VAL_NO_DEFERRED_UPDATE           (1L << 7)  /* always write the attribute immediately when it is set */
#define IVI_VAL_DONT_RETURN_DEFERRED_VALUE   (1L << 8)  /* don't return a set value that hasn't been updated to the instrument, return the instrument's current value */
#define IVI_VAL_FLUSH_ON_WRITE               (1L << 9)  /* send IVI_MSG_FLUSH to the BufferIOCallback (which by default calls viFlush) after the write callback */
#define IVI_VAL_MULTI_CHANNEL                (1L << 10) /* specified when the attribute is added.  If set, the attribute has a separate value for each channel */
#define IVI_VAL_COERCEABLE_ONLY_BY_INSTR     (1L << 11) /* specifies that the instrument coerces the attribue value in a way that the driver cannot anticipate in software.  Do NOT use this flag UNLESS ABSOLUTELY NECESSARY !!! */
#define IVI_VAL_WAIT_FOR_OPC_BEFORE_READS    (1L << 12) /* specifies to wait for operation complete before reads */
#define IVI_VAL_WAIT_FOR_OPC_AFTER_WRITES    (1L << 13) /* specifies to wait for operation complete after writes */
#define IVI_VAL_USE_CALLBACKS_FOR_SIMULATION (1L << 14) /* specifies to call the read and write callbacks even in simulation mode */
#define IVI_VAL_DONT_CHECK_STATUS            (1L << 15) /* specifies to not call the checkStatus callback even when IVI_ATTR_QUERY_INSTR_STATUS is VI_TRUE */

#define IVI_VAL_HIDDEN     (IVI_VAL_NOT_USER_READABLE | IVI_VAL_NOT_USER_WRITABLE)

/*****************************************************************************/
/*= Constants for optionFlags argument to Set/Check/GetAttribute functions ==*/
/*****************************************************************************/
#define IVI_VAL_DIRECT_USER_CALL            (1<<0)  /* applies to Set/Check/Get;  if 1, then:  the IVI_VAL_NOT_USER_READABLE/WRITEABLE flags can apply,                                                   */
                                                    /* and the engine automatically checks status on a Set if IVI_ATTR_QUERY_INSTR_STATUS is TRUE and the attribute's IVI_VAL_DONT_CHECK_STATUS flag is 0 */
#define IVI_VAL_SET_CACHE_ONLY              (1<<1)  /* applies to Set only;  if 1, then only the cached value is set and no instrument I/O is performed;                                               */
                                                    /* use this when you set multiple instrument attributes with one I/O command;  if you call Set calls with this flag, the update is never deferred */
#define IVI_VAL_DONT_MARK_AS_SET_BY_USER    (1<<2)  /* applies to Set only;  if 0 (which is the typical case), then Ivi_AttributeWasSetByUser will return TRUE;  important for interchangeability checking  */

/*****************************************************************************/
/*= Constants for channels.                                        ========= */
/*****************************************************************************/
#define IVI_VAL_ALL_CHANNELS    "IVI_ALL_CHANNELS" /* special channel string */
#define IVI_VAL_ALL_INSTANCES   IVI_VAL_ALL_CHANNELS

/*****************************************************************************/
/*= Typedef for adding an attribute invalidation                   ========= */
/*****************************************************************************/
typedef struct
    {
    ViAttr      attribute;
    ViBoolean   allChannels;   /* if nonzero, invalidate on all channels;   */
                               /* otherwise, invalidate only on the channel */
                               /* which caused the invalidation to occur    */
    } IviInvalEntry;

/*****************************************************************************/
/*= Typedef for getting list of logical names.                     ========= */
/*****************************************************************************/
typedef struct
    {
    ViString    logicalName;
    ViBoolean   fromFile;   /* VI_TRUE if logical name was in configuration file;  VI_FALSE if was from Ivi_DefineLogicalName */
    } IviLogicalNameEntry;

/*****************************************************************************/
/*= Typedef and related constants for data types.                   ======== */
/*****************************************************************************/
typedef ViInt32 IviValueType;

#define IVI_VAL_INT32                           1L
#define IVI_VAL_INT64                           2L
#define IVI_VAL_REAL64                          4L
#define IVI_VAL_STRING                          5L
#define IVI_VAL_ADDR                            10L
#define IVI_VAL_SESSION                         11L
#define IVI_VAL_BOOLEAN                         13L
#define IVI_VAL_UNKNOWN_TYPE                    14L

/*****************************************************************************/
/*= Typedef and related constants for the callback types.          ========= */
/*****************************************************************************/
typedef ViInt32 IviCallbackType;   /* type used to identify which callback to set or get*/

#define IVI_VAL_READ_CALLBACK                   1
#define IVI_VAL_WRITE_CALLBACK                  2
#define IVI_VAL_COMPARE_CALLBACK                3
#define IVI_VAL_CHECK_CALLBACK                  4
#define IVI_VAL_COERCE_CALLBACK                 5
#define IVI_VAL_RANGE_TABLE_CALLBACK            6

/*****************************************************************************/
/*= Constants for the Ivi_ReadToFile function.                     ========= */
/*****************************************************************************/
/* fileAction */
#define IVI_VAL_TRUNCATE                        1
#define IVI_VAL_APPEND                          2

/*****************************************************************************/
/*= Constants for the Ivi_PerformClassInterchangeCheck function.         === */
/*****************************************************************************/
/* IVI Class API */
#define IVI_VAL_CLASS_API_DCPWR                 1
#define IVI_VAL_CLASS_API_DMM                   2
#define IVI_VAL_CLASS_API_FGEN                  3
#define IVI_VAL_CLASS_API_SCOPE                 4
#define IVI_VAL_CLASS_API_SWTCH                 5

/*****************************************************************************/
/*= Error constants                                                ========= */
/*****************************************************************************/
#define IVI_STATUS_CODE_BASE                    0x3FFA0000L

#define IVI_WARN_BASE                           (IVI_STATUS_CODE_BASE)
#define IVI_CROSS_CLASS_WARN_BASE               (IVI_WARN_BASE + 0x1000)
#define IVI_CLASS_WARN_BASE                     (IVI_WARN_BASE + 0x2000)
#define IVI_SPECIFIC_WARN_BASE                  (IVI_WARN_BASE + 0x4000)
#define IVI_MAX_SPECIFIC_WARN_CODE              (IVI_WARN_BASE + 0x7FFF)
#define IVI_NI_WARN_BASE                        (IVI_WARN_BASE + 0x6000)

#define IVI_ERROR_BASE                          (_VI_ERROR + IVI_STATUS_CODE_BASE)
#define IVI_CROSS_CLASS_ERROR_BASE              (IVI_ERROR_BASE + 0x1000)
#define IVI_CLASS_ERROR_BASE                    (IVI_ERROR_BASE + 0x2000)
#define IVI_SPECIFIC_ERROR_BASE                 (IVI_ERROR_BASE + 0x4000)
#define IVI_MAX_SPECIFIC_ERROR_CODE             (IVI_ERROR_BASE + 0x7FFF)
#define IVI_NI_ERROR_BASE                       (IVI_ERROR_BASE + 0x6000)
#define IVI_SHARED_COMPONENT_ERROR_BASE         (IVI_ERROR_BASE + 0x1000)

    /* IVI Foundation defined warnings */
#define IVI_WARN_NSUP_ID_QUERY                  (IVI_WARN_BASE + 0x65)
#define IVI_WARN_NSUP_RESET                     (IVI_WARN_BASE + 0x66)
#define IVI_WARN_NSUP_SELF_TEST                 (IVI_WARN_BASE + 0x67)
#define IVI_WARN_NSUP_ERROR_QUERY               (IVI_WARN_BASE + 0x68)
#define IVI_WARN_NSUP_REV_QUERY                 (IVI_WARN_BASE + 0x69)

    /* IVI Foundation defined errors */
#define IVI_ERROR_CANNOT_RECOVER                (IVI_ERROR_BASE + 0x00)
#define IVI_ERROR_INSTRUMENT_STATUS             (IVI_ERROR_BASE + 0x01)
#define IVI_ERROR_CANNOT_OPEN_FILE              (IVI_ERROR_BASE + 0x02)
#define IVI_ERROR_READING_FILE                  (IVI_ERROR_BASE + 0x03)
#define IVI_ERROR_WRITING_FILE                  (IVI_ERROR_BASE + 0x04)
#define IVI_ERROR_INVALID_PATHNAME              (IVI_ERROR_BASE + 0x0B)
#define IVI_ERROR_INVALID_ATTRIBUTE             (IVI_ERROR_BASE + 0x0C)
#define IVI_ERROR_IVI_ATTR_NOT_WRITABLE         (IVI_ERROR_BASE + 0x0D)
#define IVI_ERROR_IVI_ATTR_NOT_READABLE         (IVI_ERROR_BASE + 0x0E)
#define IVI_ERROR_INVALID_VALUE                 (IVI_ERROR_BASE + 0x10)
#define IVI_ERROR_FUNCTION_NOT_SUPPORTED        (IVI_ERROR_BASE + 0x11)
#define IVI_ERROR_ATTRIBUTE_NOT_SUPPORTED       (IVI_ERROR_BASE + 0x12)
#define IVI_ERROR_VALUE_NOT_SUPPORTED           (IVI_ERROR_BASE + 0x13)
#define IVI_ERROR_TYPES_DO_NOT_MATCH            (IVI_ERROR_BASE + 0x15)
#define IVI_ERROR_NOT_INITIALIZED               (IVI_ERROR_BASE + 0x1D)
#define IVI_ERROR_UNKNOWN_CHANNEL_NAME          (IVI_ERROR_BASE + 0x20)
#define IVI_ERROR_TOO_MANY_OPEN_FILES           (IVI_ERROR_BASE + 0x23)
#define IVI_ERROR_CHANNEL_NAME_REQUIRED         (IVI_ERROR_BASE + 0x44)
#define IVI_ERROR_CHANNEL_NAME_NOT_ALLOWED      (IVI_ERROR_BASE + 0x45)
#define IVI_ERROR_MISSING_OPTION_NAME           (IVI_ERROR_BASE + 0x49)
#define IVI_ERROR_MISSING_OPTION_VALUE          (IVI_ERROR_BASE + 0x4A)
#define IVI_ERROR_BAD_OPTION_NAME               (IVI_ERROR_BASE + 0x4B)
#define IVI_ERROR_BAD_OPTION_VALUE              (IVI_ERROR_BASE + 0x4C)
#define IVI_ERROR_OUT_OF_MEMORY                 (IVI_ERROR_BASE + 0x56)
#define IVI_ERROR_OPERATION_PENDING             (IVI_ERROR_BASE + 0x57)
#define IVI_ERROR_NULL_POINTER                  (IVI_ERROR_BASE + 0x58)
#define IVI_ERROR_UNEXPECTED_RESPONSE           (IVI_ERROR_BASE + 0x59)
#define IVI_ERROR_FILE_NOT_FOUND                (IVI_ERROR_BASE + 0x5B)
#define IVI_ERROR_INVALID_FILE_FORMAT           (IVI_ERROR_BASE + 0x5C)
#define IVI_ERROR_STATUS_NOT_AVAILABLE          (IVI_ERROR_BASE + 0x5D)
#define IVI_ERROR_ID_QUERY_FAILED               (IVI_ERROR_BASE + 0x5E)
#define IVI_ERROR_RESET_FAILED                  (IVI_ERROR_BASE + 0x5F)
#define IVI_ERROR_RESOURCE_UNKNOWN              (IVI_ERROR_BASE + 0x60)
#define IVI_ERROR_CANNOT_CHANGE_SIMULATION_STATE       (IVI_ERROR_BASE + 0x62)
#define IVI_ERROR_INVALID_NUMBER_OF_LEVELS_IN_SELECTOR (IVI_ERROR_BASE + 0x63)
#define IVI_ERROR_INVALID_RANGE_IN_SELECTOR     (IVI_ERROR_BASE + 0x64)
#define IVI_ERROR_UNKOWN_NAME_IN_SELECTOR       (IVI_ERROR_BASE + 0x65)
#define IVI_ERROR_BADLY_FORMED_SELECTOR         (IVI_ERROR_BASE + 0x66)
#define IVI_ERROR_UNKNOWN_PHYSICAL_IDENTIFIER   (IVI_ERROR_BASE + 0x67)

/* IVI Foundation reserved (grandfathered) errors */
#define IVI_ERROR_DRIVER_MODULE_NOT_FOUND       (IVI_ERROR_BASE + 0x05)
#define IVI_ERROR_CANNOT_OPEN_DRIVER_MODULE     (IVI_ERROR_BASE + 0x06)
#define IVI_ERROR_INVALID_DRIVER_MODULE         (IVI_ERROR_BASE + 0x07)
#define IVI_ERROR_UNDEFINED_REFERENCES          (IVI_ERROR_BASE + 0x08)
#define IVI_ERROR_FUNCTION_NOT_FOUND            (IVI_ERROR_BASE + 0x09)
#define IVI_ERROR_LOADING_DRIVER_MODULE         (IVI_ERROR_BASE + 0x0A)
#define IVI_ERROR_INVALID_PARAMETER             (IVI_ERROR_BASE + 0x0F)
#define IVI_ERROR_INVALID_TYPE                  (IVI_ERROR_BASE + 0x14)
#define IVI_ERROR_MULTIPLE_DEFERRED_SETTING     (IVI_ERROR_BASE + 0x16)
#define IVI_ERROR_ITEM_ALREADY_EXISTS           (IVI_ERROR_BASE + 0x17)
#define IVI_ERROR_INVALID_CONFIGURATION         (IVI_ERROR_BASE + 0x18)
#define IVI_ERROR_VALUE_NOT_AVAILABLE           (IVI_ERROR_BASE + 0x19)
#define IVI_ERROR_ATTRIBUTE_VALUE_NOT_KNOWN     (IVI_ERROR_BASE + 0x1A)
#define IVI_ERROR_NO_RANGE_TABLE                (IVI_ERROR_BASE + 0x1B)
#define IVI_ERROR_INVALID_RANGE_TABLE           (IVI_ERROR_BASE + 0x1C)
#define IVI_ERROR_NON_INTERCHANGEABLE_BEHAVIOR  (IVI_ERROR_BASE + 0x1E)
#define IVI_ERROR_NO_CHANNEL_TABLE              (IVI_ERROR_BASE + 0x1F)
#define IVI_ERROR_SYS_RSRC_ALLOC                (IVI_ERROR_BASE + 0x21)
#define IVI_ERROR_ACCESS_DENIED                 (IVI_ERROR_BASE + 0x22)
#define IVI_ERROR_UNABLE_TO_CREATE_TEMP_FILE    (IVI_ERROR_BASE + 0x24)
#define IVI_ERROR_NO_UNUSED_TEMP_FILENAMES      (IVI_ERROR_BASE + 0x25)
#define IVI_ERROR_DISK_FULL                     (IVI_ERROR_BASE + 0x26)
#define IVI_ERROR_CONFIG_FILE_NOT_FOUND         (IVI_ERROR_BASE + 0x27)
#define IVI_ERROR_CANNOT_OPEN_CONFIG_FILE       (IVI_ERROR_BASE + 0x28)
#define IVI_ERROR_ERROR_READING_CONFIG_FILE     (IVI_ERROR_BASE + 0x29)
#define IVI_ERROR_BAD_INTEGER_IN_CONFIG_FILE    (IVI_ERROR_BASE + 0x2A)
#define IVI_ERROR_BAD_DOUBLE_IN_CONFIG_FILE     (IVI_ERROR_BASE + 0x2B)
#define IVI_ERROR_BAD_BOOLEAN_IN_CONFIG_FILE    (IVI_ERROR_BASE + 0x2C)
#define IVI_ERROR_CONFIG_ENTRY_NOT_FOUND        (IVI_ERROR_BASE + 0x2D)
#define IVI_ERROR_DRIVER_DLL_INIT_FAILED        (IVI_ERROR_BASE + 0x2E)
#define IVI_ERROR_DRIVER_UNRESOLVED_SYMBOL      (IVI_ERROR_BASE + 0x2F)
#define IVI_ERROR_CANNOT_FIND_CVI_RTE           (IVI_ERROR_BASE + 0x30)
#define IVI_ERROR_CANNOT_OPEN_CVI_RTE           (IVI_ERROR_BASE + 0x31)
#define IVI_ERROR_CVI_RTE_INVALID_FORMAT        (IVI_ERROR_BASE + 0x32)
#define IVI_ERROR_CVI_RTE_MISSING_FUNCTION      (IVI_ERROR_BASE + 0x33)
#define IVI_ERROR_CVI_RTE_INIT_FAILED           (IVI_ERROR_BASE + 0x34)
#define IVI_ERROR_CVI_RTE_UNRESOLVED_SYMBOL     (IVI_ERROR_BASE + 0x35)
#define IVI_ERROR_LOADING_CVI_RTE               (IVI_ERROR_BASE + 0x36)
#define IVI_ERROR_CANNOT_OPEN_DLL_FOR_EXPORTS   (IVI_ERROR_BASE + 0x37)
#define IVI_ERROR_DLL_CORRUPTED                 (IVI_ERROR_BASE + 0x38)
#define IVI_ERROR_NO_DLL_EXPORT_TABLE           (IVI_ERROR_BASE + 0x39)
#define IVI_ERROR_UNKNOWN_DEFAULT_SETUP_ATTR    (IVI_ERROR_BASE + 0x3A)
#define IVI_ERROR_INVALID_DEFAULT_SETUP_VAL     (IVI_ERROR_BASE + 0x3B)
#define IVI_ERROR_UNKNOWN_MEMORY_PTR            (IVI_ERROR_BASE + 0x3C)
#define IVI_ERROR_EMPTY_CHANNEL_LIST            (IVI_ERROR_BASE + 0x3D)
#define IVI_ERROR_DUPLICATE_CHANNEL_STRING      (IVI_ERROR_BASE + 0x3E)
#define IVI_ERROR_DUPLICATE_VIRT_CHAN_NAME      (IVI_ERROR_BASE + 0x3F)
#define IVI_ERROR_MISSING_VIRT_CHAN_NAME        (IVI_ERROR_BASE + 0x40)
#define IVI_ERROR_BAD_VIRT_CHAN_NAME            (IVI_ERROR_BASE + 0x41)
#define IVI_ERROR_UNASSIGNED_VIRT_CHAN_NAME     (IVI_ERROR_BASE + 0x42)
#define IVI_ERROR_BAD_VIRT_CHAN_ASSIGNMENT      (IVI_ERROR_BASE + 0x43)
#define IVI_ERROR_ATTR_NOT_VALID_FOR_CHANNEL    (IVI_ERROR_BASE + 0x46)
#define IVI_ERROR_ATTR_MUST_BE_CHANNEL_BASED    (IVI_ERROR_BASE + 0x47)
#define IVI_ERROR_CHANNEL_ALREADY_EXCLUDED      (IVI_ERROR_BASE + 0x48)
#define IVI_ERROR_NOT_CREATED_BY_CLASS          (IVI_ERROR_BASE + 0x4D)
#define IVI_ERROR_IVI_INI_IS_RESERVED           (IVI_ERROR_BASE + 0x4E)
#define IVI_ERROR_DUP_RUNTIME_CONFIG_ENTRY      (IVI_ERROR_BASE + 0x4F)
#define IVI_ERROR_INDEX_IS_ONE_BASED            (IVI_ERROR_BASE + 0x50)
#define IVI_ERROR_INDEX_IS_TOO_HIGH             (IVI_ERROR_BASE + 0x51)
#define IVI_ERROR_ATTR_NOT_CACHEABLE            (IVI_ERROR_BASE + 0x52)
#define IVI_ERROR_ADDR_ATTRS_MUST_BE_HIDDEN     (IVI_ERROR_BASE + 0x53)
#define IVI_ERROR_BAD_CHANNEL_NAME              (IVI_ERROR_BASE + 0x54)
#define IVI_ERROR_BAD_PREFIX_IN_CONFIG_FILE     (IVI_ERROR_BASE + 0x55)

/* NI-Specific errors */
#define IVI_ERROR_CANNOT_MODIFY_REPEATED_CAPABILITY_TABLE  (IVI_NI_ERROR_BASE + 0)
#define IVI_ERROR_CANNOT_RESTRICT_ATTRIBUTE_TWICE          (IVI_NI_ERROR_BASE + 1)
#define IVI_ERROR_REPEATED_CAPABILITY_ALREADY_EXISTS       (IVI_NI_ERROR_BASE + 2)
#define IVI_ERROR_REPEATED_CAPABILITY_NOT_DEFINED          (IVI_NI_ERROR_BASE + 3)
#define IVI_ERROR_INVALID_REPEATED_CAPABILITY_NAME         (IVI_NI_ERROR_BASE + 4)
#define IVI_ERROR_CONFIG_SERVER_NOT_PRESENT                (IVI_NI_ERROR_BASE + 0xD)

/* NI-Specific renamed errors.  */
#define IVI_ERROR_REPEATED_CAPABILITY_NAME_REQUIRED        IVI_ERROR_CHANNEL_NAME_REQUIRED
#define IVI_ERROR_UNKNOWN_REPEATED_CAPABILITY_NAME         IVI_ERROR_UNKNOWN_CHANNEL_NAME
#define IVI_ERROR_EMPTY_REPEATED_CAPABILITY_LIST           IVI_ERROR_EMPTY_CHANNEL_LIST
#define IVI_ERROR_DUPLICATE_REPEATED_CAPABILITY_IDENTIFIER IVI_ERROR_DUPLICATE_CHANNEL_STRING
#define IVI_ERROR_REPEATED_CAPABILITY_NAME_NOT_ALLOWED     IVI_ERROR_CHANNEL_NAME_NOT_ALLOWED
#define IVI_ERROR_ATTR_NOT_VALID_FOR_REPEATED_CAPABILITY   IVI_ERROR_ATTR_NOT_VALID_FOR_CHANNEL
#define IVI_ERROR_ATTR_MUST_BE_REPEATED_CAPABILITY_BASED   IVI_ERROR_ATTR_MUST_BE_CHANNEL_BASED
#define IVI_ERROR_BAD_REPEATED_CAPABILITY_NAME             IVI_ERROR_BAD_CHANNEL_NAME

/*  renamed errors. Do not use these identifiers in your drivers and applications. */
#define IVI_ERROR_CANNOT_LOAD_IVI_ENGINE        (IVI_ERROR_BASE + 0x00)
#define IVI_ERROR_INSTR_SPECIFIC                (IVI_ERROR_BASE + 0x01)
#define IVI_ERROR_TOO_MANY_FILES_OPEN           (IVI_ERROR_BASE + 0x23)

/*  obsolete errors. Do not use these identifiers in your drivers and applications. */
#define IVI_ERROR_ALREADY_INITIALIZED                      (IVI_ERROR_BASE + 0x61)

/*****************************************************************************/
/*= Macros for checking for errors.                                 ======== */
/*= The checkErr and viCheckErr macros discard warnings.            ======== */
/*= The checkWarn and viCheckWarn macros preserve warnings.         ======== */
/*****************************************************************************/

#ifndef _IVI_USE_LEGACY_ERROR_MACROS_

/* Redefined error macros in IVI Engine 2.4.0 (ICP 2.3) */

#ifndef checkAlloc
#define checkAlloc(fCall)    if ((fCall) == 0) \
                                 {error = VI_ERROR_ALLOC; goto Error;}  else error = error
#endif

#ifndef checkErr
#define checkErr(fCall)      if (VI_SUCCESS != (error = (fCall), (error = (error < 0) ? error : VI_SUCCESS))) \
                                 {goto Error;}  else error = error
#endif

#ifndef checkWarn
#define checkWarn(fCall)     if ((void)1,1) {ViStatus _code_; if (_code_ = (fCall), _code_ < 0)    \
                                                {error = _code_;goto Error;}        \
                                               else error = (error==0)?_code_:error;} else error = error
#endif

#ifndef viCheckAlloc
#define viCheckAlloc(fCall)  if ((fCall) == 0) \
                                 {error = VI_ERROR_ALLOC; Ivi_SetErrorInfo(vi, VI_FALSE, error, 0, VI_NULL); goto Error;}  else error = error
#endif

#ifndef viCheckErr
#define viCheckErr(fCall)    if (VI_SUCCESS != (error = (fCall), (error = (error < 0) ? error : VI_SUCCESS))) \
                                 {Ivi_SetErrorInfo(vi, VI_FALSE, error, 0, VI_NULL); goto Error;}  else error = error
#endif

#ifndef viCheckErrElab
#define viCheckErrElab(fCall, elab) \
                             if (VI_SUCCESS != (error = (fCall), (error = (error < 0) ? error : VI_SUCCESS))) \
                                 {Ivi_SetErrorInfo(vi, VI_FALSE, error, 0, elab); goto Error;}  else error = error
#endif

#ifndef viCheckParm
#define viCheckParm(fCall, parameterPosition, parameterName) \
                             if (VI_SUCCESS != (error = (fCall), (error = (error < 0) ? (error) : VI_SUCCESS))) \
                                 {Ivi_SetErrorInfo(vi, VI_FALSE, error, Ivi_ParamPositionError(parameterPosition), parameterName); goto Error;}  else error = error
#endif

#ifndef viCheckWarn
#define viCheckWarn(fCall)   if ((void)1,1) {ViStatus _code_; if (_code_ = (fCall), _code_?Ivi_SetErrorInfo(vi, VI_FALSE, _code_, 0, VI_NULL) : 0, _code_ < 0)    \
                                                {error = _code_;goto Error;}        \
                                               else error = (error==0)?_code_:error;} else error = error
#endif

#else /* _IVI_USE_LEGACY_ERROR_MACROS_ */

/* Legacy error macros defined in IVI Engine 2.3.0 (ICP 2.2) and earlier */

#ifndef checkAlloc
#define checkAlloc(fCall)    if ((fCall) == 0) \
                                 {error = VI_ERROR_ALLOC; goto Error;}  else
#endif

#ifndef checkErr
#define checkErr(fCall)      if (VI_SUCCESS != (error = (fCall), (error = (error < 0) ? error : VI_SUCCESS))) \
                                 {goto Error;}  else
#endif

#ifndef checkWarn
#define checkWarn(fCall)     if (error = (fCall), error < 0) \
                                 {goto Error;}  else
#endif

#ifndef viCheckAlloc
#define viCheckAlloc(fCall)  if ((fCall) == 0) \
                                 {error = VI_ERROR_ALLOC; Ivi_SetErrorInfo(vi, VI_FALSE, error, 0, VI_NULL); goto Error;}  else
#endif

#ifndef viCheckErr
#define viCheckErr(fCall)    if (VI_SUCCESS != (error = (fCall), (error = (error < 0) ? error : VI_SUCCESS))) \
                                 {Ivi_SetErrorInfo(vi, VI_FALSE, error, 0, VI_NULL); goto Error;}  else
#endif

#ifndef viCheckErrElab
#define viCheckErrElab(fCall, elab) \
                             if (VI_SUCCESS != (error = (fCall), (error = (error < 0) ? error : VI_SUCCESS))) \
                                 {Ivi_SetErrorInfo(vi, VI_FALSE, error, 0, elab); goto Error;}  else
#endif

#ifndef viCheckParm
#define viCheckParm(fCall, parameterPosition, parameterName) \
                             if (VI_SUCCESS != (error = (fCall), (error = (error < 0) ? (error) : VI_SUCCESS))) \
                                 {Ivi_SetErrorInfo(vi, VI_FALSE, error, Ivi_ParamPositionError(parameterPosition), parameterName); goto Error;}  else
#endif

#ifndef viCheckWarn
#define viCheckWarn(fCall)   if (error = (fCall), (error ? Ivi_SetErrorInfo(vi, VI_FALSE, error, 0, VI_NULL) : 0), error < 0) \
                                 {goto Error;}  else
#endif

#endif /* _IVI_USE_LEGACY_ERROR_MACROS_ */

/*****************************************************************************/
/*= Function pointer typedefs for standard instrument driver functions. ==== */
/*****************************************************************************/
typedef ViStatus (_VI_FUNC *Ivi_InitFuncPtr)        (   ViRsrc resourceName, ViBoolean IDQuery,
                                                        ViBoolean resetDevice,
                                                        ViSession *vi);
typedef ViStatus (_VI_FUNC *Ivi_InitWithOptionsFuncPtr)(ViRsrc resourceName, ViBoolean IDQuery,
                                                        ViBoolean resetDevice, ViString optionString,
                                                        ViSession *vi);
typedef ViStatus (_VI_FUNC *Ivi_CloseFuncPtr)       (   ViSession vi);
typedef ViStatus (_VI_FUNC *Ivi_ResetFuncPtr)       (   ViSession vi);
typedef ViStatus (_VI_FUNC *Ivi_SelfTestFuncPtr)    (   ViSession vi,
                                                        ViInt16 * selfTestResult,
                                                        ViChar selfTestMessage[]);
typedef ViStatus (_VI_FUNC *Ivi_ErrorQueryFuncPtr)  (   ViSession vi,
                                                        ViInt32  *errorCode,
                                                        ViChar errorMessage[]);
typedef ViStatus (_VI_FUNC *Ivi_ErrorMessageFuncPtr)(   ViSession vi,
                                                        ViStatus statusCode,
                                                        ViChar message[]);
typedef ViStatus (_VI_FUNC *Ivi_RevisionQueryFuncPtr)(  ViSession vi,
                                                        ViChar driverRev[],
                                                        ViChar instrRev[]);
/*****************************************************************************/
/*= Function pointer typedefs for IVI Required instrument driver functions.= */
/*****************************************************************************/

typedef ViStatus (_VI_FUNC *Ivi_GetAttributeViInt32FuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 *value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
typedef ViStatus (_VI_FUNC *Ivi_GetAttributeViInt64FuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt64 *value);
#endif

typedef ViStatus (_VI_FUNC *Ivi_GetAttributeViReal64FuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViReal64 *value);

typedef ViStatus (_VI_FUNC *Ivi_GetAttributeViStringFuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 bufSize, ViChar value[]);

typedef ViStatus (_VI_FUNC *Ivi_GetAttributeViBooleanFuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViBoolean *value);

typedef ViStatus (_VI_FUNC *Ivi_GetAttributeViSessionFuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViSession *value);

typedef ViStatus (_VI_FUNC *Ivi_SetAttributeViInt32FuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
typedef ViStatus (_VI_FUNC *Ivi_SetAttributeViInt64FuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt64 value);
#endif

typedef ViStatus (_VI_FUNC *Ivi_SetAttributeViReal64FuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViReal64 value);

typedef ViStatus (_VI_FUNC *Ivi_SetAttributeViStringFuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViConstString value);

typedef ViStatus (_VI_FUNC *Ivi_SetAttributeViBooleanFuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViBoolean value);

typedef ViStatus (_VI_FUNC *Ivi_SetAttributeViSessionFuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViSession value);

typedef ViStatus (_VI_FUNC *Ivi_CheckAttributeViInt32FuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
typedef ViStatus (_VI_FUNC *Ivi_CheckAttributeViInt64FuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt64 value);
#endif

typedef ViStatus (_VI_FUNC *Ivi_CheckAttributeViReal64FuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViReal64 value);

typedef ViStatus (_VI_FUNC *Ivi_CheckAttributeViStringFuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViConstString value);

typedef ViStatus (_VI_FUNC *Ivi_CheckAttributeViBooleanFuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViBoolean value);

typedef ViStatus (_VI_FUNC *Ivi_CheckAttributeViSessionFuncPtr) (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViSession value);

typedef ViStatus (_VI_FUNC *Ivi_GetErrorInfoFuncPtr) (ViSession vi, ViStatus *primaryError, ViStatus *secondaryError, ViChar errorElaboration[IVI_MAX_MESSAGE_BUF_SIZE]);

typedef ViStatus (_VI_FUNC *Ivi_ClearErrorInfoFuncPtr) (ViSession vi);

typedef ViStatus (_VI_FUNC *Ivi_LockSessionFuncPtr) (ViSession vi, ViBoolean *callerHasLock);

typedef ViStatus (_VI_FUNC *Ivi_UnlockSessionFuncPtr) (ViSession vi, ViBoolean *callerHasLock);

typedef ViStatus (_VI_FUNC *Ivi_GetNextCoercionRecordFuncPtr) (ViSession vi, ViInt32 bufferSize, ViChar recordBuf[]);

typedef ViStatus (_VI_FUNC *Ivi_GetNextInterchangeWarningPtr) (ViSession vi, ViInt32 bufferSize, ViChar buffer[]);

typedef ViStatus (_VI_FUNC *Ivi_ResetInterchangeCheckPtr) (ViSession vi);


/*****************************************************************************/
/*= Typedef for function pointer passed to Ivi_BuildChannelTable    ======== */
/*= when you want to allow virtual channel names in the IVI         ======== */
/*= configuration file to reference channel strings not passed      ======== */
/*= into Ivi_BuildChannelTable.                                     ======== */
/*****************************************************************************/
typedef ViStatus    (_VI_FUNC *Ivi_ValidateChannelStringFunc)(ViSession vi, ViConstString channelString, ViBoolean *isValid, ViStatus *secondaryError);
    /*
        You should return an error code only if you are unable to determine
        whether the channel string is valid or not.
        If the channel string is not a valid one, you should set *isValid
        to VI_FALSE but return VI_SUCCESS.
        If you set *isValid to VI_FALSE, IVI sets the primary error to
        IVI_ERROR_BAD_VIRT_CHAN_ASSIGNMENT and formats the error elaboration
        to include both the virtual channel name and the channel string.
        You can optionally set *secondaryError to specify what is wrong
        with the channel string.
    */

/*****************************************************************************/
/*= Typedef for function pointer passed to ReadAttrViStringCallback ======== */
/*= and CoerceAttrViStringCallback.  The callback uses this         ======== */
/*= function pointer to set the string value.                       ======== */
/*****************************************************************************/
typedef ViStatus    (_VI_FUNC *Ivi_SetValInStringCallbackFunc)(ViSession vi, ViAttr attributeId, ViConstString value);

/*****************************************************************************/
/*= Function pointer typedefs for ViInt32 attribute callbacks       ======== */
/*****************************************************************************/
typedef ViStatus    (_VI_FUNC *ReadAttrViInt32_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViInt32 *value);
typedef ViStatus    (_VI_FUNC *WriteAttrViInt32_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViInt32 value);
typedef ViStatus    (_VI_FUNC *CheckAttrViInt32_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 value);
typedef ViStatus    (_VI_FUNC *CompareAttrViInt32_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 coercedNewValue, ViInt32 cacheValue, ViInt32 *result);
typedef ViStatus    (_VI_FUNC *CoerceAttrViInt32_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 value, ViInt32 *coercedValue);

/*****************************************************************************/
/*= Function pointer typedefs for ViInt64 attribute callbacks       ======== */
/*****************************************************************************/
#ifdef _IVI_64BIT_ATTR_DEFINED_
typedef ViStatus    (_VI_FUNC *ReadAttrViInt64_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViInt64 *value);
typedef ViStatus    (_VI_FUNC *WriteAttrViInt64_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViInt64 value);
typedef ViStatus    (_VI_FUNC *CheckAttrViInt64_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt64 value);
typedef ViStatus    (_VI_FUNC *CompareAttrViInt64_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt64 coercedNewValue, ViInt64 cacheValue, ViInt32 *result);
typedef ViStatus    (_VI_FUNC *CoerceAttrViInt64_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt64 value, ViInt64 *coercedValue);
#endif
/*****************************************************************************/
/*= Function pointer typedefs for ViReal64 attribute callbacks      ======== */
/*****************************************************************************/
typedef ViStatus    (_VI_FUNC *ReadAttrViReal64_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViReal64 *value);
typedef ViStatus    (_VI_FUNC *WriteAttrViReal64_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViReal64 value);
typedef ViStatus    (_VI_FUNC *CheckAttrViReal64_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViReal64 value);
typedef ViStatus    (_VI_FUNC *CompareAttrViReal64_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViReal64 coercedNewValue, ViReal64 cacheValue, ViInt32 *result);
typedef ViStatus    (_VI_FUNC *CoerceAttrViReal64_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViReal64 value, ViReal64 *coercedValue);

/*****************************************************************************/
/*= Function pointer typedefs for ViString attribute callbacks      ======== */
/*****************************************************************************/
typedef ViStatus    (_VI_FUNC *ReadAttrViString_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, const ViConstString cacheValue);
typedef ViStatus    (_VI_FUNC *WriteAttrViString_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViConstString value);
typedef ViStatus    (_VI_FUNC *CheckAttrViString_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViConstString value);
typedef ViStatus    (_VI_FUNC *CompareAttrViString_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViConstString coercedNewValue, ViConstString cacheValue, ViInt32 *result);
typedef ViStatus    (_VI_FUNC *CoerceAttrViString_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, const ViConstString value);

/*****************************************************************************/
/*= Function pointer typedefs for ViBoolean attribute callbacks     ======== */
/*****************************************************************************/
typedef ViStatus    (_VI_FUNC *ReadAttrViBoolean_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViBoolean *value);
typedef ViStatus    (_VI_FUNC *WriteAttrViBoolean_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViBoolean value);
typedef ViStatus    (_VI_FUNC *CheckAttrViBoolean_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViBoolean value);
typedef ViStatus    (_VI_FUNC *CompareAttrViBoolean_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViBoolean coercedNewValue, ViBoolean cacheValue, ViInt32 *result);
typedef ViStatus    (_VI_FUNC *CoerceAttrViBoolean_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViBoolean value, ViBoolean *coercedValue);

/*****************************************************************************/
/*= Function pointer typedefs for ViSession attribute callbacks     ======== */
/*****************************************************************************/
typedef ViStatus    (_VI_FUNC *ReadAttrViSession_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViSession *value);
typedef ViStatus    (_VI_FUNC *WriteAttrViSession_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViSession value);
typedef ViStatus    (_VI_FUNC *CheckAttrViSession_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViSession value);
typedef ViStatus    (_VI_FUNC *CompareAttrViSession_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViSession coercedNewValue, ViSession cacheValue, ViInt32 *result);
typedef ViStatus    (_VI_FUNC *CoerceAttrViSession_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViSession value, ViSession *coercedValue);

/*****************************************************************************/
/*= Function pointer typedefs for ViAddr attribute callbacks        ======== */
/*****************************************************************************/
typedef ViStatus    (_VI_FUNC *ReadAttrViAddr_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViAddr *value);
typedef ViStatus    (_VI_FUNC *WriteAttrViAddr_CallbackPtr)(ViSession vi, ViSession io, ViConstString repCapName, ViAttr attributeId, ViAddr value);
typedef ViStatus    (_VI_FUNC *CheckAttrViAddr_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViAddr value);
typedef ViStatus    (_VI_FUNC *CompareAttrViAddr_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViAddr coercedNewValue, ViAddr cacheValue, ViInt32 *result);
typedef ViStatus    (_VI_FUNC *CoerceAttrViAddr_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViAddr value, ViAddr *coercedValue);

/*****************************************************************************/
/*= Function pointer typedef for the callback that retrieves        ======== */
/*= the range table.   Applies only to ViInt32, ViReal64,           ======== */
/*= ViInt64, and ViBoolean attributes.                              ======== */
/*****************************************************************************/
typedef ViStatus    (_VI_FUNC *RangeTable_CallbackPtr)(ViSession vi, ViConstString repCapName, ViAttr attributeId, IviRangeTablePtr *rangeTablePtr);

/*****************************************************************************/
/* Function pointer typedef for the Operation Complete (OPC)        ======== */
/* callback.  The OPC callback is called after writing an           ======== */
/* attribute value to the instrument (if the                        ======== */
/* IVI_VAL_WAIT_FOR_OPC_AFTER_WRITES flag is set for the attribute) ======== */
/* and before reading an attribute value from the instrument (if    ======== */
/* the IVI_VAL_WAIT_FOR_OPC_BEFORE_READS flag is set for the        ======== */
/* attribute).  You can install an OPC callback by setting the      ======== */
/* IVI_ATTR_OPC_CALLBACK attribute for the instrument.              ======== */
/*****************************************************************************/
typedef ViStatus (_VI_FUNC *Ivi_OPCCallbackPtr)(ViSession vi, ViSession io);


/*****************************************************************************/
/* Function pointer typedef for the Check Status callback.          ======== */
/* This Check Status callback is called after interaction with      ======== */
/* the instrument if the IVI_ATTR_QUERY_INSTR_STATUS is set to      ======== */
/* VI_TRUE.  The callback queries the instrument to determine if    ======== */
/* the instrument encountered an error.   You can install a Check   ======== */
/* Status callback by using the IVI_ATTR_CHECK_STATUS_CALLBACK      ======== */
/* attribute for the instrument.                                    ======== */
/*****************************************************************************/
typedef ViStatus (_VI_FUNC *Ivi_CheckStatusCallbackPtr)(ViSession vi, ViSession io);

/*****************************************************************************/
/* Function pointer typedef for the Interchange Check callback.     ======== */
/*****************************************************************************/
typedef ViStatus (_VI_FUNC *Ivi_InterchangeCheckCallbackPtr)(ViSession vi, ViInt32 funcEnum,
                                    ViConstString repCapName, ViAttr attributeId);

/*****************************************************************************/
/*= Base values for attribute constants.                            ======== */
/*= A private attribute is one that is defined for use within       ======== */
/*= that module and is not exported via an include file.            ======== */
/*****************************************************************************/
#define IVI_ATTR_BASE                   1000000
#define IVI_ENGINE_PRIVATE_ATTR_BASE    (IVI_ATTR_BASE +  00000)   /* base for private attributes of the IVI engine */
#define IVI_ENGINE_PUBLIC_ATTR_BASE     (IVI_ATTR_BASE +  50000)   /* base for public attributes of the IVI engine */
#define IVI_SPECIFIC_PUBLIC_ATTR_BASE   (IVI_ATTR_BASE + 150000)   /* base for public attributes of specific drivers */
#define IVI_SPECIFIC_PRIVATE_ATTR_BASE  (IVI_ATTR_BASE + 200000)   /* base for private attributes of specific drivers */
                                                                   /* This value was changed from IVI_ATTR_BASE + 100000 in the version of this file released in August 2013 (ICP 4.6). */
                                                                   /* A private attribute, by its very definition, should not be passed to another module; it should stay private to the compiled module. */
#define IVI_CLASS_PUBLIC_ATTR_BASE      (IVI_ATTR_BASE + 250000)   /* base for public attributes of class drivers */
#define IVI_CLASS_PRIVATE_ATTR_BASE     (IVI_ATTR_BASE + 300000)   /* base for private attributes of class drivers */
                                                                   /* This value was changed from IVI_ATTR_BASE + 200000 in the version of this file released in August 2013 (ICP 4.6). */
                                                                   /* A private attribute, by its very definition, should not be passed to another module; it should stay private to the compiled module. */

/*****************************************************************************/
/*= Public IVI engine attributes                                    ======== */
/*= The data type of each attribute is listed, followed by the      ======== */
/*= default value or a remark.                                      ======== */
/*= Note:  "hidden" means not readable or writable by the end-user. ======== */
/*****************************************************************************/
#define IVI_ATTR_NONE                   /* no attribute */              0xFFFFFFFF

#define IVI_ATTR_RANGE_CHECK            /* ViBoolean, VI_TRUE */        (IVI_ENGINE_PUBLIC_ATTR_BASE + 2)
#define IVI_ATTR_QUERY_INSTRUMENT_STATUS /* ViBoolean, VI_FALSE */      (IVI_ENGINE_PUBLIC_ATTR_BASE + 3)   /* If VI_TRUE, the specific driver is allowed to query the instrument error status after each operation */
#define IVI_ATTR_CACHE                  /* ViBoolean, VI_TRUE */        (IVI_ENGINE_PUBLIC_ATTR_BASE + 4)
#define IVI_ATTR_SIMULATE               /* ViBoolean, VI_FALSE */       (IVI_ENGINE_PUBLIC_ATTR_BASE + 5)
#define IVI_ATTR_RECORD_COERCIONS       /* ViBoolean, VI_FALSE */       (IVI_ENGINE_PUBLIC_ATTR_BASE + 6)
#define IVI_ATTR_DRIVER_SETUP           /* ViString,  "" */             (IVI_ENGINE_PUBLIC_ATTR_BASE + 7)

#define IVI_ATTR_INTERCHANGE_CHECK      /* ViBoolean, VI_TRUE */        (IVI_ENGINE_PUBLIC_ATTR_BASE + 21)
#define IVI_ATTR_SPY                    /* ViBoolean, VI_FALSE */       (IVI_ENGINE_PUBLIC_ATTR_BASE + 22)
#define IVI_ATTR_USE_SPECIFIC_SIMULATION  /* ViBoolean */               (IVI_ENGINE_PUBLIC_ATTR_BASE + 23)  /* simulate values in specific rather than class driver;  default is VI_TRUE if session opened through class driver, VI_FALSE otherwise */

#define IVI_ATTR_PRIMARY_ERROR          /* ViInt32  */                  (IVI_ENGINE_PUBLIC_ATTR_BASE + 101)
#define IVI_ATTR_SECONDARY_ERROR        /* VIInt32  */                  (IVI_ENGINE_PUBLIC_ATTR_BASE + 102)
#define IVI_ATTR_ERROR_ELABORATION      /* ViString */                  (IVI_ENGINE_PUBLIC_ATTR_BASE + 103)

#define IVI_ATTR_CHANNEL_COUNT          /* ViInt32,  not writable*/     (IVI_ENGINE_PUBLIC_ATTR_BASE + 203)   /* set by the specific-driver;  default: 1 */

#define IVI_ATTR_CLASS_DRIVER_PREFIX    /* ViString, not writable*/     (IVI_ENGINE_PUBLIC_ATTR_BASE + 301)  /* instrument prefix for the class driver;  empty string if not using class driver */
#define IVI_ATTR_SPECIFIC_DRIVER_PREFIX /* ViString, not writable*/     (IVI_ENGINE_PUBLIC_ATTR_BASE + 302)  /* instrument prefix for the specific driver */
#define IVI_ATTR_SPECIFIC_DRIVER_LOCATOR/* ViString, not writable*/     (IVI_ENGINE_PUBLIC_ATTR_BASE + 303)  /* the pathnname of the specific driver code module; from the configuration file */
#define IVI_ATTR_IO_RESOURCE_DESCRIPTOR /* ViString, not writable*/     (IVI_ENGINE_PUBLIC_ATTR_BASE + 304)  /* the string that describes how to find the physical instrument; from the configuration file */
#define IVI_ATTR_LOGICAL_NAME           /* ViString, not writable*/     (IVI_ENGINE_PUBLIC_ATTR_BASE + 305)  /* for class drivers, the logical name used in the Init call to identify the specific instrument */
#define IVI_ATTR_VISA_RM_SESSION        /* ViSession,hidden      */     (IVI_ENGINE_PUBLIC_ATTR_BASE + 321)
#define IVI_ATTR_SYSTEM_IO_SESSION      /* ViSession,not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 322)
#define IVI_ATTR_IO_SESSION_TYPE        /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 324)
#define IVI_ATTR_SYSTEM_IO_TIMEOUT      /* ViInt32 */                   (IVI_ENGINE_PUBLIC_ATTR_BASE + 325)
#define IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS   /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 327)

#define IVI_ATTR_GROUP_CAPABILITIES     /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 401)
#define IVI_ATTR_FUNCTION_CAPABILITIES  /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 402)

#define IVI_ATTR_ENGINE_MAJOR_VERSION       /* ViInt32,  not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 501)
#define IVI_ATTR_ENGINE_MINOR_VERSION       /* ViInt32,  not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 502)
#define IVI_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION /* ViInt32,  not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 503)
#define IVI_ATTR_SPECIFIC_DRIVER_MINOR_VERSION /* ViInt32,  not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 504)
#define IVI_ATTR_CLASS_DRIVER_MAJOR_VERSION /* ViInt32,  not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 505)
#define IVI_ATTR_CLASS_DRIVER_MINOR_VERSION /* ViInt32,  not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 506)

#define IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 510)
#define IVI_ATTR_INSTRUMENT_MANUFACTURER    /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 511)
#define IVI_ATTR_INSTRUMENT_MODEL           /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 512)
#define IVI_ATTR_SPECIFIC_DRIVER_VENDOR     /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 513)
#define IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION/* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 514)
#define IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION /* ViInt32, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 515)
#define IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION /* ViInt32, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 516)
#define IVI_ATTR_CLASS_DRIVER_VENDOR        /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 517)
#define IVI_ATTR_CLASS_DRIVER_DESCRIPTION   /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 518)
#define IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION /* ViInt32, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 519)
#define IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION /* ViInt32, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 520)

#define IVI_ATTR_SPECIFIC_DRIVER_REVISION   /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 551)
#define IVI_ATTR_CLASS_DRIVER_REVISION      /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 552)
#define IVI_ATTR_ENGINE_REVISION            /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 553)

#define IVI_ATTR_OPC_CALLBACK               /* ViAddr,    hidden */     (IVI_ENGINE_PUBLIC_ATTR_BASE + 602)  /* see Ivi_OPCCallbackPtr  typedef */
#define IVI_ATTR_CHECK_STATUS_CALLBACK      /* ViAddr,    hidden */     (IVI_ENGINE_PUBLIC_ATTR_BASE + 603)  /* see Ivi_CheckStatusCallbackPtr  typedef */

#define IVI_ATTR_USER_INTERCHANGE_CHECK_CALLBACK /* ViAddr, hidden */   (IVI_ENGINE_PUBLIC_ATTR_BASE + 801)  /* see Ivi_InterchangeCheckCallbackPtr typedef */

/*****************************************************************************/
/*= Public IVI Engine Functions                                     ======== */
/*= These functions have a function panel                                    */
/*****************************************************************************/
/*****************************************************************************/
/*= Specific   Drivers                                              ======== */
/*****************************************************************************/
ViStatus IviDll _VI_FUNC    Ivi_SpecificDriverNew(ViConstString specificPrefix, ViConstString optionsString, ViSession *vi);
ViStatus IviDll _VI_FUNC    Ivi_ApplyDefaultSetup (ViSession vi);
ViStatus IviDll _VI_FUNC    Ivi_GetSpecificDriverStatusDesc (ViSession vi, ViStatus statusCode, ViChar messageBuf[IVI_MAX_MESSAGE_BUF_SIZE],
                                                             IviStringValueTable additionalTableToSearch);

    /*= Status Checking Control                                     ======== */
ViBoolean IviDll _VI_FUNC   Ivi_NeedToCheckStatus(ViSession vi);
ViStatus  IviDll _VI_FUNC   Ivi_SetNeedToCheckStatus(ViSession vi, ViBoolean needToCheckStatus);

    /*= Instrument Specific Error Queue                            ========= */
ViStatus IviDll _VI_FUNC    Ivi_QueueInstrSpecificError(ViSession vi, ViInt32 instrumentError, ViConstString message);
ViStatus IviDll _VI_FUNC    Ivi_DequeueInstrSpecificError(ViSession vi, ViInt32 *instrumentError, ViChar message[IVI_MAX_MESSAGE_BUF_SIZE]);
ViStatus IviDll _VI_FUNC    Ivi_ClearInstrSpecificErrorQueue (ViSession vi);
ViStatus IviDll _VI_FUNC    Ivi_InstrSpecificErrorQueueSize(ViSession vi, ViInt32 *numErrors);

    /*= Direct Instrument I/O                                      ========= */
ViStatus  IviDll _VI_FUNC   Ivi_WriteInstrData (ViSession vi, ViConstString writeBuffer);
ViStatus  IviDll _VI_FUNC   Ivi_ReadInstrData (ViSession vi, ViInt32 numBytes, ViChar rdBuf[], ViInt32 *bytesRead);
ViStatus  IviDll _VI_FUNC   Ivi_ReadToFile (ViSession vi, ViConstString filename, ViInt32 maxBytesToRead,
                                            ViInt32 fileAction, ViInt32 *totalBytesWritten);
ViStatus  IviDll _VI_FUNC   Ivi_WriteFromFile (ViSession vi, ViConstString filename, ViInt32 maxBytesToWrite,
                                               ViInt32 byteOffset, ViInt32 *totalBytesWritten);
ViStatus  IviDll _VI_FUNC   Ivi_viWrite (ViSession vi, ViByte buffer[], ViInt64 count, ViInt64 *returnCount);
ViStatus  IviDll _VI_FUNC   Ivi_viRead (ViSession vi, ViInt64 bufferSize, ViByte buffer[], ViInt64 *returnCount);

    /*= IVI Class Compliant Driver Helpers                                == */
ViStatus  IviDll _VI_FUNC   Ivi_PerformClassInterchangeCheck (ViSession vi, ViInt32 classAPI, ViConstString funcName);

/*****************************************************************************/
/*= Class Drivers                                                   ======== */
/*****************************************************************************/
ViStatus  IviDll _VI_FUNC   Ivi_ClassDriverNew(ViConstString logicalOrVInstrName, ViConstString classPrefix, ViString functionList[], ViSession *vi);
ViStatus  IviDll _VI_FUNC   Ivi_ClassFunctionCapabilities (ViSession vi, IviStringValueTable functionTable, ViChar capabilityString[], ViBoolean *allFound);
ViStatus  IviDll _VI_FUNC   Ivi_GetClassDriverStatusDesc(ViSession vi, ViStatus statusCode, ViChar messageBuf[IVI_MAX_MESSAGE_BUF_SIZE], IviStringValueTable additionalTableToSearch);

    /*= Specific Driver Session                                     ======== */
ViSession IviDll _VI_FUNC   Ivi_SpecificDriverSession(ViSession vi);
ViStatus  IviDll _VI_FUNC   Ivi_SetSpecificDriverSession(ViSession vi, ViSession specificDriver);

    /*= Simulation Driver Management                                ======== */
ViStatus  IviDll _VI_FUNC   Ivi_LoadSimulationDriver(ViSession vi, ViConstString defaultSwModule, ViString functionList[]);
ViStatus  IviDll _VI_FUNC   Ivi_GetSimulationSession (ViSession vi, ViSession* simVi);
ViStatus  IviDll _VI_FUNC   Ivi_CloseSimulationSession (ViSession vi);

    /*= Dynamic Load and Dispatch                                   ======== */
ViStatus  IviDll _VI_FUNC   Ivi_GetFunctionPtr(ViSession vi, ViInt32 functionId, ViAddr *functionPtr);
ViStatus  IviDll _VI_FUNC   Ivi_GetFunctionPtrByName(ViSession vi, ViConstString name, ViBoolean addPrefix, ViAddr *functionPtr);
ViStatus  IviDll _VI_FUNC   Ivi_GetSimulationDriverFunctionPtr(ViSession vi, ViConstString functionName, ViAddr* functionPtr);

/*****************************************************************************/
/*= Simulation Drivers                                              ======== */
/*****************************************************************************/
ViStatus  IviDll _VI_FUNC   Ivi_SimulationDriverNew(ViConstString logicalName, ViSession *vi);
ViStatus  IviDll _VI_FUNC   Ivi_ApplySimulationDriverDefaultSetup (ViSession vi, ViConstString name);

/*****************************************************************************/
/*= Sessions                                                 ======== */
/*****************************************************************************/
ViStatus IviDll _VI_FUNC    Ivi_ValidateSession (ViSession vi);
ViBoolean IviDll _VI_FUNC   Ivi_SessionIsAvailable (ViSession vi);
ViStatus IviDll _VI_FUNC    Ivi_Dispose(ViSession vi);

    /*= Locking                                                     ======== */
ViStatus  IviDll _VI_FUNC   Ivi_LockSession(ViSession vi, ViBoolean *callerHasLock);
ViStatus  IviDll _VI_FUNC   Ivi_UnlockSession(ViSession vi, ViBoolean *callerHasLock);

/*****************************************************************************/
/*= Channels                                                        ======== */
/*****************************************************************************/
ViStatus  IviDll _VI_FUNC   Ivi_BuildChannelTable(ViSession vi, ViConstString defaultChannelList, ViBoolean allowUnknownChannelStrings, Ivi_ValidateChannelStringFunc chanStrValidationFunc);
ViStatus  IviDll _VI_FUNC   Ivi_AddToChannelTable(ViSession vi, ViConstString channelStringsToAdd);
ViStatus  IviDll _VI_FUNC   Ivi_RestrictAttrToChannels(ViSession vi, ViAttr attributeId, ViConstString channelNameList);
ViStatus  IviDll _VI_FUNC   Ivi_ValidateAttrForChannel(ViSession vi, ViConstString channelName, ViAttr attributeId);

ViStatus  IviDll _VI_FUNC   Ivi_CoerceChannelName(ViSession vi, ViConstString channelName, ViConstString *channelString);
ViStatus  IviDll _VI_FUNC   Ivi_GetChannelIndex (ViSession vi, ViConstString channelName, ViInt32 *index);  /* 1-based index */
ViStatus  IviDll _VI_FUNC   Ivi_GetNthChannelString(ViSession vi, ViInt32 index, ViConstString *channelString);  /* 1-based index */
ViStatus  IviDll _VI_FUNC   Ivi_GetUserChannelName(ViSession vi, ViConstString channelString, ViConstString *userChannelName);

/*****************************************************************************/
/*= Repeated Capabilities                                           ======== */
/*****************************************************************************/
ViStatus IviDll _VI_FUNC    Ivi_BuildRepCapTable(ViSession vi, ViConstString repCapName, ViConstString names);
ViStatus IviDll _VI_FUNC    Ivi_AddToRepCapTable(ViSession vi, ViConstString repCapName, ViConstString namesToAdd);
ViStatus IviDll _VI_FUNC    Ivi_RestrictAttrToInstances(ViSession vi, ViAttr attributeId, ViConstString instances);
ViStatus IviDll _VI_FUNC    Ivi_ValidateAttrForRepCapName(ViSession vi, ViConstString repCapName, ViAttr attributeId);

ViStatus IviDll _VI_FUNC    Ivi_CoerceRepCapName(ViSession vi, ViConstString repCapName, ViConstString name, ViConstString *actualNameRef);
ViStatus IviDll _VI_FUNC    Ivi_GetRepCapIndex (ViSession vi, ViConstString repCapName, ViConstString name,  ViInt32 *indexRef);
ViStatus IviDll _VI_FUNC    Ivi_GetNthRepCapName(ViSession vi, ViConstString repCapName, ViInt32 index, ViConstString *nameRef);
ViStatus IviDll _VI_FUNC    Ivi_GetAttributeRepCapName(ViSession vi, ViAttr attributeId, ViConstString *repCapName);

/*****************************************************************************/
/*= Attributes                                                      ======== */
/*****************************************************************************/
ViStatus IviDll _VI_FUNC    Ivi_ValidateAttribute(ViSession vi, ViAttr attrId, IviValueType expectedType);
ViBoolean IviDll _VI_FUNC   Ivi_AttributeIsAvailable(ViSession vi, ViAttr attrId);
ViStatus IviDll _VI_FUNC    Ivi_ResetAttribute(ViSession vi, ViConstString repCapName, ViAttr attributeId);
ViStatus IviDll _VI_FUNC    Ivi_DeleteAttribute(ViSession vi, ViAttr attributeId);

    /*= Creation                                                    ======== */
ViStatus IviDll _VI_FUNC    Ivi_AddAttributeViInt32(ViSession                       vi,
                                                    ViAttr                          id,
                                                    ViConstString                   attrName,
                                                    ViInt32                         defaultValue,
                                                    IviAttrFlags                    attributeFlags,
                                                    ReadAttrViInt32_CallbackPtr     readCallback,
                                                    WriteAttrViInt32_CallbackPtr    writeCallback,
                                                    IviRangeTablePtr                rangeTable);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus IviDll _VI_FUNC    Ivi_AddAttributeViInt64(ViSession                       vi,
                                                    ViAttr                          id,
                                                    ViConstString                   attrName,
                                                    ViInt64                         defaultValue,
                                                    IviAttrFlags                    attributeFlags,
                                                    ReadAttrViInt64_CallbackPtr     readCallback,
                                                    WriteAttrViInt64_CallbackPtr    writeCallback,
                                                    IviRangeTablePtr                rangeTable);
#endif
ViStatus IviDll _VI_FUNC    Ivi_AddAttributeViReal64(ViSession                       vi,
                                                     ViAttr                          id,
                                                     ViConstString                   attrName,
                                                     ViReal64                        defaultValue,
                                                     IviAttrFlags                    attributeFlags,
                                                     ReadAttrViReal64_CallbackPtr    readCallback,
                                                     WriteAttrViReal64_CallbackPtr   writeCallback,
                                                     IviRangeTablePtr                rangeTable,
                                                     ViInt32                         comparePrecision);

ViStatus IviDll _VI_FUNC    Ivi_AddAttributeViString(ViSession                       vi,
                                                     ViAttr                          id,
                                                     ViConstString                   attrName,
                                                     ViConstString                   defaultValue,
                                                     IviAttrFlags                    attributeFlags,
                                                     ReadAttrViString_CallbackPtr    readCallback,
                                                     WriteAttrViString_CallbackPtr   writeCallback);

ViStatus IviDll _VI_FUNC    Ivi_AddAttributeViBoolean(  ViSession                       vi,
                                                        ViAttr                          id,
                                                        ViConstString                   attrName,
                                                        ViBoolean                       defaultValue,
                                                        IviAttrFlags                    attributeFlags,
                                                        ReadAttrViBoolean_CallbackPtr   readCallback,
                                                        WriteAttrViBoolean_CallbackPtr  writeCallback);

ViStatus IviDll _VI_FUNC    Ivi_AddAttributeViSession(  ViSession                       vi,
                                                        ViAttr                          id,
                                                        ViConstString                   attrName,
                                                        ViSession                       defaultValue,
                                                        IviAttrFlags                    attributeFlags,
                                                        ReadAttrViSession_CallbackPtr   readCallback,
                                                        WriteAttrViSession_CallbackPtr  writeCallback);

ViStatus IviDll _VI_FUNC    Ivi_AddAttributeViAddr( ViSession                       vi,
                                                    ViAttr                          id,
                                                    ViConstString                   attrName,
                                                    ViAddr                          defaultValue,
                                                    IviAttrFlags                    attributeFlags,
                                                    ReadAttrViAddr_CallbackPtr      readCallback,
                                                    WriteAttrViAddr_CallbackPtr     writeCallback);

ViStatus IviDll _VI_FUNC    Ivi_AddRepeatedAttributeViInt32(ViSession                       vi,
                                                            ViConstString                   repCapName,
                                                            ViAttr                          id,
                                                            ViConstString                   attrName,
                                                            ViInt32                         defaultValue,
                                                            IviAttrFlags                    attributeFlags,
                                                            ReadAttrViInt32_CallbackPtr     readCallback,
                                                            WriteAttrViInt32_CallbackPtr    writeCallback,
                                                            IviRangeTablePtr                rangeTable);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus IviDll _VI_FUNC    Ivi_AddRepeatedAttributeViInt64(   ViSession                       vi,
                                                            ViConstString                   repCapName,
                                                            ViAttr                          id,
                                                            ViConstString                   attrName,
                                                            ViInt64                         defaultValue,
                                                            IviAttrFlags                    attributeFlags,
                                                            ReadAttrViInt64_CallbackPtr     readCallback,
                                                            WriteAttrViInt64_CallbackPtr    writeCallback,
                                                            IviRangeTablePtr                rangeTable);
#endif
ViStatus IviDll _VI_FUNC    Ivi_AddRepeatedAttributeViReal64(  ViSession                       vi,
                                                                ViConstString                   repCapName,
                                                                ViAttr                          id,
                                                                ViConstString                   attrName,
                                                                ViReal64                        defaultValue,
                                                                IviAttrFlags                    attributeFlags,
                                                                ReadAttrViReal64_CallbackPtr    readCallback,
                                                                WriteAttrViReal64_CallbackPtr   writeCallback,
                                                                IviRangeTablePtr                rangeTable,
                                                                ViInt32                         comparePrecision);

ViStatus IviDll _VI_FUNC    Ivi_AddRepeatedAttributeViString(  ViSession                       vi,
                                                                ViConstString                   repCapName,
                                                                ViAttr                          id,
                                                                ViConstString                   attrName,
                                                                ViConstString                   defaultValue,
                                                                IviAttrFlags                    attributeFlags,
                                                                ReadAttrViString_CallbackPtr    readCallback,
                                                                WriteAttrViString_CallbackPtr   writeCallback);

ViStatus IviDll _VI_FUNC    Ivi_AddRepeatedAttributeViBoolean( ViSession                       vi,
                                                                ViConstString                   repCapName,
                                                                ViAttr                          id,
                                                                ViConstString                   attrName,
                                                                ViBoolean                       defaultValue,
                                                                IviAttrFlags                    attributeFlags,
                                                                ReadAttrViBoolean_CallbackPtr   readCallback,
                                                                WriteAttrViBoolean_CallbackPtr  writeCallback);

ViStatus IviDll _VI_FUNC    Ivi_AddRepeatedAttributeViSession( ViSession                       vi,
                                                                ViConstString                   repCapName,
                                                                ViAttr                          id,
                                                                ViConstString                   attrName,
                                                                ViSession                       defaultValue,
                                                                IviAttrFlags                    attributeFlags,
                                                                ReadAttrViSession_CallbackPtr   readCallback,
                                                                WriteAttrViSession_CallbackPtr  writeCallback);

ViStatus IviDll _VI_FUNC    Ivi_AddRepeatedAttributeViAddr(ViSession                       vi,
                                                            ViConstString                   repCapName,
                                                            ViAttr                          id,
                                                            ViConstString                   attrName,
                                                            ViAddr                          defaultValue,
                                                            IviAttrFlags                    attributeFlags,
                                                            ReadAttrViAddr_CallbackPtr      readCallback,
                                                            WriteAttrViAddr_CallbackPtr     writeCallback);


    /*= Set/Get/Check Attribute                                         ======== */
        /*= Typesafe Set Attribute functions for use in drivers         ======== */
ViStatus IviDll _VI_FUNC    Ivi_SetAttributeViInt32(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViInt32 value);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus IviDll _VI_FUNC    Ivi_SetAttributeViInt64(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViInt64 value);
#endif
ViStatus IviDll _VI_FUNC    Ivi_SetAttributeViReal64(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViReal64 value);
ViStatus IviDll _VI_FUNC    Ivi_SetAttributeViString(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViConstString value);
ViStatus IviDll _VI_FUNC    Ivi_SetAttributeViBoolean(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViBoolean value);
ViStatus IviDll _VI_FUNC    Ivi_SetAttributeViSession(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViSession value);
ViStatus IviDll _VI_FUNC    Ivi_SetAttributeViAddr(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViAddr value);

        /*= Typesafe Check Attribute functions for use in drivers       ======== */
ViStatus IviDll _VI_FUNC    Ivi_CheckAttributeViInt32(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViInt32 value);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus IviDll _VI_FUNC    Ivi_CheckAttributeViInt64(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViInt64 value);
#endif
ViStatus IviDll _VI_FUNC    Ivi_CheckAttributeViReal64(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViReal64 value);
ViStatus IviDll _VI_FUNC    Ivi_CheckAttributeViString(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViConstString value);
ViStatus IviDll _VI_FUNC    Ivi_CheckAttributeViBoolean(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViBoolean value);
ViStatus IviDll _VI_FUNC    Ivi_CheckAttributeViSession(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViSession value);
ViStatus IviDll _VI_FUNC    Ivi_CheckAttributeViAddr(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViAddr value);

        /*= Typesafe Get Attribute functions for use in drivers         ======== */
ViStatus IviDll _VI_FUNC    Ivi_GetAttributeViInt32(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViInt32 *value);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus IviDll _VI_FUNC    Ivi_GetAttributeViInt64(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViInt64 *value);
#endif
ViStatus IviDll _VI_FUNC    Ivi_GetAttributeViReal64(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViReal64 *value);
ViStatus IviDll _VI_FUNC    Ivi_GetAttributeViString(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViInt32 bufSize, ViChar value[]);
ViStatus IviDll _VI_FUNC    Ivi_GetAttributeViBoolean(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViBoolean *value);
ViStatus IviDll _VI_FUNC    Ivi_GetAttributeViSession(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViSession *value);
ViStatus IviDll _VI_FUNC    Ivi_GetAttributeViAddr(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 optionFlags, ViAddr *value);

        /*= State Caching/Invalidations                                 ======== */
ViStatus IviDll _VI_FUNC    Ivi_InvalidateAttribute(ViSession vi, ViConstString repCapName, ViAttr attributeId);
ViStatus IviDll _VI_FUNC    Ivi_InvalidateAllAttributes(ViSession vi);

ViStatus IviDll _VI_FUNC    Ivi_AddAttributeInvalidation(ViSession vi, ViAttr attributeId, ViAttr attributeToInval, ViBoolean allChannels);
ViStatus IviDll _VI_FUNC    Ivi_DeleteAttributeInvalidation(ViSession vi, ViAttr attributeId, ViAttr attributeToDelete);
ViStatus IviDll _VI_FUNC    Ivi_GetInvalidationList(ViSession vi, ViAttr attributeId, IviInvalEntry **invalList, ViInt32 *numInvalEntries);
void     IviDll _VI_FUNC    Ivi_DisposeInvalidationList(IviInvalEntry *invalList);

ViStatus IviDll _VI_FUNC    Ivi_AttributeIsCached(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViBoolean *instrStateIsCurrentlyCached);

    /*= Coercion                                                    ======== */
ViStatus IviDll _VI_FUNC    Ivi_GetCoercedValViInt32(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 value, ViInt32 *coercedValue);
ViStatus IviDll _VI_FUNC    Ivi_GetCoercedValViReal64(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViReal64 value, ViReal64 *coercedValue);
ViStatus IviDll _VI_FUNC    Ivi_GetNextCoercionInfo(ViSession vi, ViAttr *attributeId, ViConstString *attributeName, ViConstString *channelString,
                                                  IviValueType *attrType, ViReal64 *desiredValue, ViReal64 *coercedValue);
ViStatus IviDll _VI_FUNC    Ivi_GetNextCoercionString (ViSession vi, ViInt32 bufSize, ViChar coercion[]);

    /*= Callbacks                                                   ======== */
        /*= One function is needed because it is typesafe for all attribute types */
ViStatus IviDll _VI_FUNC    Ivi_SetAttrRangeTableCallback (ViSession vi, ViAttr attributeId, RangeTable_CallbackPtr rangeTableCallback);

        /*= Default callbacks                                              ========= */
        /*= Prototypes for functions supplied as default callbacks.        ========= */
        /*= These default callbacks are installed when an attribute is     ========= */
        /*= added by the class or specific driver using one of the         ========= */
        /*= AddAttribute functions.                                        ========= */
        /*= For ViInt32 and ViReal64, the Default Check callback is        ========= */
        /*= installed when the attribute is added with a range table.      ========= */
        /*= If the range table is of type IVI_VAL_COERCED,                 ========= */
        /*= the Default Coerce callback is also installed.                 ========= */
        /*= For ViReal64, the Default Compare callback is always installed.========= */
        /*= For ViBoolean, the Default Coerce callback is always installed.========= */
        /*= Do not call these functions directly unless you have already   ========= */
        /*= Ivi_LockSession().                                             ========= */
ViStatus IviDll _VI_FUNC    Ivi_DefaultCheckCallbackViInt32    (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 value);
ViStatus IviDll _VI_FUNC    Ivi_DefaultCoerceCallbackViInt32   (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt32 value, ViInt32 *coercedValue);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus IviDll _VI_FUNC    Ivi_DefaultCheckCallbackViInt64    (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt64 value);
ViStatus IviDll _VI_FUNC    Ivi_DefaultCoerceCallbackViInt64   (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViInt64 value, ViInt64 *coercedValue);
#endif
ViStatus IviDll _VI_FUNC    Ivi_DefaultCheckCallbackViReal64   (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViReal64 value);
ViStatus IviDll _VI_FUNC    Ivi_DefaultCoerceCallbackViReal64  (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViReal64 value, ViReal64 *coercedValue);
ViStatus IviDll _VI_FUNC    Ivi_DefaultCompareCallbackViReal64 (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViReal64 a, ViReal64 b, ViInt32 *result);
ViStatus IviDll _VI_FUNC    Ivi_DefaultCoerceCallbackViBoolean (ViSession vi, ViConstString repCapName, ViAttr attributeId, ViBoolean value, ViBoolean *coercedValue);

        /*= Set Attribute Read Callback functions                   ======== */
ViStatus IviDll _VI_FUNC    Ivi_SetAttrReadCallbackViInt32   (ViSession vi, ViAttr attributeId, ReadAttrViInt32_CallbackPtr readCallback);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus IviDll _VI_FUNC    Ivi_SetAttrReadCallbackViInt64   (ViSession vi, ViAttr attributeId, ReadAttrViInt64_CallbackPtr readCallback);
#endif
ViStatus IviDll _VI_FUNC    Ivi_SetAttrReadCallbackViReal64  (ViSession vi, ViAttr attributeId, ReadAttrViReal64_CallbackPtr readCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrReadCallbackViString  (ViSession vi, ViAttr attributeId, ReadAttrViString_CallbackPtr readCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrReadCallbackViBoolean (ViSession vi, ViAttr attributeId, ReadAttrViBoolean_CallbackPtr readCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrReadCallbackViSession (ViSession vi, ViAttr attributeId, ReadAttrViSession_CallbackPtr readCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrReadCallbackViAddr    (ViSession vi, ViAttr attributeId, ReadAttrViAddr_CallbackPtr readCallback);

        /*= Set Attribute Write Callback functions                  ======== */
ViStatus IviDll _VI_FUNC    Ivi_SetAttrWriteCallbackViInt32   (ViSession vi, ViAttr attributeId, WriteAttrViInt32_CallbackPtr writeCallback);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus IviDll _VI_FUNC    Ivi_SetAttrWriteCallbackViInt64   (ViSession vi, ViAttr attributeId, WriteAttrViInt64_CallbackPtr writeCallback);
#endif
ViStatus IviDll _VI_FUNC    Ivi_SetAttrWriteCallbackViReal64  (ViSession vi, ViAttr attributeId, WriteAttrViReal64_CallbackPtr writeCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrWriteCallbackViString  (ViSession vi, ViAttr attributeId, WriteAttrViString_CallbackPtr writeCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrWriteCallbackViBoolean (ViSession vi, ViAttr attributeId, WriteAttrViBoolean_CallbackPtr writeCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrWriteCallbackViSession (ViSession vi, ViAttr attributeId, WriteAttrViSession_CallbackPtr writeCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrWriteCallbackViAddr    (ViSession vi, ViAttr attributeId, WriteAttrViAddr_CallbackPtr writeCallback);

        /*= Set Attribute Check Callback functions                  ======== */
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCheckCallbackViInt32   (ViSession vi, ViAttr attributeId, CheckAttrViInt32_CallbackPtr checkCallback);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCheckCallbackViInt64   (ViSession vi, ViAttr attributeId, CheckAttrViInt64_CallbackPtr checkCallback);
#endif
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCheckCallbackViReal64  (ViSession vi, ViAttr attributeId, CheckAttrViReal64_CallbackPtr checkCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCheckCallbackViString  (ViSession vi, ViAttr attributeId, CheckAttrViString_CallbackPtr checkCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCheckCallbackViBoolean (ViSession vi, ViAttr attributeId, CheckAttrViBoolean_CallbackPtr checkCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCheckCallbackViSession (ViSession vi, ViAttr attributeId, CheckAttrViSession_CallbackPtr checkCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCheckCallbackViAddr    (ViSession vi, ViAttr attributeId, CheckAttrViAddr_CallbackPtr checkCallback);

        /*= Set Attribute Coerce Callback functions                 ======== */
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCoerceCallbackViInt32   (ViSession vi, ViAttr attributeId, CoerceAttrViInt32_CallbackPtr coerceCallback);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCoerceCallbackViInt64   (ViSession vi, ViAttr attributeId, CoerceAttrViInt64_CallbackPtr coerceCallback);
#endif
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCoerceCallbackViReal64  (ViSession vi, ViAttr attributeId, CoerceAttrViReal64_CallbackPtr coerceCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCoerceCallbackViString  (ViSession vi, ViAttr attributeId, CoerceAttrViString_CallbackPtr coerceCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCoerceCallbackViBoolean (ViSession vi, ViAttr attributeId, CoerceAttrViBoolean_CallbackPtr coerceCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCoerceCallbackViAddr    (ViSession vi, ViAttr attributeId, CoerceAttrViAddr_CallbackPtr coerceCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCoerceCallbackViSession (ViSession vi, ViAttr attributeId, CoerceAttrViSession_CallbackPtr coerceCallback);

        /*= Set Attribute Compare Callback functions                ======== */
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCompareCallbackViInt32   (ViSession vi, ViAttr attributeId, CompareAttrViInt32_CallbackPtr compareCallback);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCompareCallbackViInt64   (ViSession vi, ViAttr attributeId, CompareAttrViInt64_CallbackPtr compareCallback);
#endif
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCompareCallbackViReal64  (ViSession vi, ViAttr attributeId, CompareAttrViReal64_CallbackPtr compareCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCompareCallbackViString  (ViSession vi, ViAttr attributeId, CompareAttrViString_CallbackPtr compareCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCompareCallbackViBoolean (ViSession vi, ViAttr attributeId, CompareAttrViBoolean_CallbackPtr compareCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCompareCallbackViSession (ViSession vi, ViAttr attributeId, CompareAttrViSession_CallbackPtr compareCallback);
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCompareCallbackViAddr    (ViSession vi, ViAttr attributeId, CompareAttrViAddr_CallbackPtr compareCallback);

    /*= Inherent Attribute Accessors                                ======== */
ViSession IviDll _VI_FUNC   Ivi_IOSession (ViSession vi);
ViBoolean IviDll _VI_FUNC   Ivi_RangeChecking (ViSession vi);
ViBoolean IviDll _VI_FUNC   Ivi_QueryInstrStatus(ViSession vi);
ViBoolean IviDll _VI_FUNC   Ivi_Simulating(ViSession vi);
ViBoolean IviDll _VI_FUNC   Ivi_UseSpecificSimulation(ViSession vi);
ViBoolean IviDll _VI_FUNC   Ivi_Spying(ViSession vi);
ViBoolean IviDll _VI_FUNC   Ivi_InterchangeCheck(ViSession vi);

    /*= Comparison Precision                                        ======== */
ViStatus  IviDll _VI_FUNC   Ivi_SetAttrComparePrecision (ViSession vi, ViAttr attributeId, ViInt32 comparePrecision);
ViStatus  IviDll _VI_FUNC   Ivi_GetAttrComparePrecision (ViSession vi, ViAttr attributeId, ViInt32 *comparePrecision);

    /*= Information                                                 ======== */
ViStatus  IviDll _VI_FUNC   Ivi_GetNumAttributes(ViSession vi, ViInt32 *numAttributes);
ViStatus  IviDll _VI_FUNC   Ivi_GetNthAttribute(ViSession vi, ViInt32 index, ViAttr *attribute);
ViStatus  IviDll _VI_FUNC   Ivi_GetAttributeFlags(ViSession vi, ViAttr attributeId, IviAttrFlags *flags);
ViStatus  IviDll _VI_FUNC   Ivi_SetAttributeFlags(ViSession iviSession, ViAttr attributeId, IviAttrFlags flags);
ViStatus  IviDll _VI_FUNC   Ivi_GetAttributeType(ViSession vi, ViAttr attributeId, IviValueType *type);
ViStatus  IviDll _VI_FUNC   Ivi_GetAttributeName(ViSession vi, ViAttr attributeId, ViChar nameBuf[], ViInt32 bufSize);
ViStatus  IviDll _VI_FUNC   Ivi_GetAttrMinMaxViInt32(ViSession vi, ViConstString repCapName, ViAttr attr, ViInt32 *min, ViInt32 *max, ViBoolean *hasMin, ViBoolean *hasMax);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus  IviDll _VI_FUNC   Ivi_GetAttrMinMaxViInt64(ViSession vi, ViConstString repCapName, ViAttr attr, ViInt64 *min, ViInt64 *max, ViBoolean *hasMin, ViBoolean *hasMax);
#endif
ViStatus  IviDll _VI_FUNC   Ivi_GetAttrMinMaxViReal64(ViSession vi, ViConstString repCapName, ViAttr attr, ViReal64 *min, ViReal64 *max, ViBoolean *hasMin, ViBoolean *hasMax);
ViBoolean IviDll _VI_FUNC   Ivi_AttributeWasSetByUser (ViSession vi, ViConstString repCapName, ViAttr attributeId);
ViBoolean IviDll _VI_FUNC   Ivi_AttributeEverSetByUser (ViSession vi, ViConstString repCapName, ViAttr attributeId);

/*****************************************************************************/
/*= Error Information                                              ========= */
/*****************************************************************************/
ViStatus IviDll _VI_FUNC    Ivi_SetErrorInfo(ViSession vi, ViBoolean overWrite, ViStatus primaryError, ViStatus secondaryError, ViConstString errorElaboration);
ViStatus IviDll _VI_FUNC    Ivi_GetErrorInfo(ViSession vi, ViStatus *primaryError, ViStatus *secondaryError, ViChar errorElaboration[IVI_MAX_MESSAGE_BUF_SIZE]);
ViStatus IviDll _VI_FUNC    Ivi_ClearErrorInfo(ViSession vi);
ViStatus IviDll _VI_FUNC    Ivi_GetErrorMessage(ViStatus statusCode, ViChar messageBuf[IVI_MAX_MESSAGE_BUF_SIZE]);

/*****************************************************************************/
/*= Range Tables                                                    ======== */
/*****************************************************************************/
    /*  GetAttrRangeTable gets the range table that the engine uses for the  */
    /*  attribute. If there is a RangeTableCallback, GetAttrRangeTable       */
    /*  callback invokes it. Otherwise, it returns the stored range table    */
    /*  pointer.                                                             */
ViStatus  IviDll _VI_FUNC   Ivi_GetAttrRangeTable (ViSession vi, ViConstString repCapName, ViAttr attributeId, IviRangeTablePtr *rangeTable);
ViStatus  IviDll _VI_FUNC   Ivi_ValidateRangeTable (IviRangeTablePtr rangeTable);

    /*= Range Table Entries                                         ======== */
ViStatus  IviDll _VI_FUNC   Ivi_GetRangeTableNumEntries (IviRangeTablePtr table, ViInt32 *numEntries);

ViStatus  IviDll _VI_FUNC   Ivi_GetViInt32EntryFromValue (ViInt32 value, IviRangeTablePtr table, ViInt32 *discreteOrMin, ViInt32 *max,
                                                          ViInt32 *coercedValue, ViInt32 *tableIndex, ViString *cmdString, ViInt32 *cmdValue);
ViStatus  IviDll _VI_FUNC   Ivi_GetViInt32EntryFromString (ViConstString cmdString, IviRangeTablePtr table, ViInt32 *discreteOrMin, ViInt32 *max,
                                                           ViInt32 *coercedValue, ViInt32 *tableIndex, ViInt32 *cmdValue);
ViStatus  IviDll _VI_FUNC   Ivi_GetViInt32EntryFromIndex (ViInt32 tableIndex, IviRangeTablePtr table, ViInt32 *discreteOrMin, ViInt32 *max,
                                                          ViInt32 *coercedValue, ViString *cmdString, ViInt32 *cmdValue);
ViStatus  IviDll _VI_FUNC   Ivi_GetViInt32EntryFromCmdValue (ViInt32 cmdValue, IviRangeTablePtr table, ViInt32 *discreteOrMin, ViInt32 *max,
                                                             ViInt32 *coercedValue, ViInt32 *tableIndex, ViString *cmdString);
ViStatus  IviDll _VI_FUNC   Ivi_GetViInt32EntryFromCoercedVal (ViInt32 coercedValue, IviRangeTablePtr table, ViInt32 *discreteOrMin, ViInt32 *max,
                                                               ViInt32 *tableIndex, ViString *cmdString, ViInt32 *cmdValue);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus  IviDll _VI_FUNC   Ivi_GetViInt64EntryFromValue (ViInt64 value, IviRangeTablePtr table, ViInt64 *discreteOrMin, ViInt64 *max,
                                                          ViInt64 *coercedValue, ViInt32 *tableIndex, ViString *cmdString, ViInt32 *cmdValue);
ViStatus  IviDll _VI_FUNC   Ivi_GetViInt64EntryFromString (ViConstString cmdString, IviRangeTablePtr table, ViInt64 *discreteOrMin, ViInt64 *max,
                                                           ViInt64 *coercedValue, ViInt32 *tableIndex, ViInt32 *cmdValue);
ViStatus  IviDll _VI_FUNC   Ivi_GetViInt64EntryFromIndex (ViInt32 tableIndex, IviRangeTablePtr table, ViInt64 *discreteOrMin, ViInt64 *max,
                                                          ViInt64 *coercedValue, ViString *cmdString, ViInt32 *cmdValue);
ViStatus  IviDll _VI_FUNC   Ivi_GetViInt64EntryFromCmdValue (ViInt32 cmdValue, IviRangeTablePtr table, ViInt64 *discreteOrMin, ViInt64 *max,
                                                             ViInt64 *coercedValue, ViInt32 *tableIndex, ViString *cmdString);
ViStatus  IviDll _VI_FUNC   Ivi_GetViInt64EntryFromCoercedVal (ViInt64 coercedValue, IviRangeTablePtr table, ViInt64 *discreteOrMin, ViInt64 *max,
                                                              ViInt32 *tableIndex, ViString *cmdString, ViInt32 *cmdValue);
#endif

ViStatus  IviDll _VI_FUNC   Ivi_GetViReal64EntryFromValue (ViReal64 value, IviRangeTablePtr table, ViReal64 *discreteOrMin, ViReal64 *max,
                                                           ViReal64 *coercedValue, ViInt32 *tableIndex, ViString *cmdString, ViInt32 *cmdValue);
ViStatus  IviDll _VI_FUNC   Ivi_GetViReal64EntryFromString (ViConstString cmdString, IviRangeTablePtr table, ViReal64 *discreteOrMin,
                                                            ViReal64 *max, ViReal64 *coercedValue, ViInt32 *tableIndex, ViInt32 *cmdValue);
ViStatus  IviDll _VI_FUNC   Ivi_GetViReal64EntryFromIndex (ViInt32 tableIndex, IviRangeTablePtr table, ViReal64 *discreteOrMin,
                                                           ViReal64 *max, ViReal64 *coercedValue, ViString *cmdString, ViInt32 *cmdValue);
ViStatus  IviDll _VI_FUNC   Ivi_GetViReal64EntryFromCmdValue (ViInt32 cmdVal, IviRangeTablePtr table, ViReal64 *discreteOrMin, ViReal64 *max,
                                                              ViReal64 *coercedValue, ViInt32 *tableIndex, ViString *cmdString);
ViStatus  IviDll _VI_FUNC   Ivi_GetViReal64EntryFromCoercedVal (ViReal64 coercedValue, IviRangeTablePtr table, ViReal64 *discreteOrMin, ViReal64 *max,
                                                               ViInt32 *tableIndex, ViString *cmdString, ViInt32 *cmdValue);

    /*= Range Table Pointer                                         ======== */
ViStatus  IviDll _VI_FUNC   Ivi_GetStoredRangeTablePtr (ViSession vi, ViAttr attributeId, IviRangeTablePtr *rangeTable);  /* bypasses callback */
ViStatus  IviDll _VI_FUNC   Ivi_SetStoredRangeTablePtr (ViSession vi, ViAttr attributeId, IviRangeTablePtr  rangeTable);

    /*= Dynamic Range Tables                                        ======== */
ViStatus  IviDll _VI_FUNC   Ivi_RangeTableNew (ViSession vi, ViInt32 numRangeValueEntries, ViInt32 type, ViBoolean hasMin,
                                               ViBoolean hasMax, IviRangeTablePtr *rangeTable);
ViStatus  IviDll _VI_FUNC   Ivi_RangeTableFree (ViSession vi, IviRangeTablePtr rangeTable, ViBoolean freeCmdStrings);
ViStatus  IviDll _VI_FUNC   Ivi_SetRangeTableEntry (IviRangeTablePtr rangeTable, ViInt32 tableIndex, ViReal64 discreteOrMin,
                                                    ViReal64 max, ViReal64 coercedValue, ViConstString cmdString, ViInt32 cmdValue);
#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus  IviDll _VI_FUNC   Ivi_SetRangeTableEntryViInt64 (IviRangeTablePtr rangeTable, ViInt32 tableIndex, ViInt64 discreteOrMin,
                                                           ViInt64 max, ViInt64 coercedValue, ViConstString cmdString, ViInt32 cmdValue);
#endif
ViStatus  IviDll _VI_FUNC   Ivi_SetRangeTableEnd (IviRangeTablePtr rangeTable, ViInt32 endIndex);

/*****************************************************************************/
/*= Configuration Store                                             ======== */
/*****************************************************************************/
ViStatus  IviDll _VI_FUNC   Ivi_GetConfigStoreHandle(IviConfigStoreHandle* handle);
ViStatus  IviDll _VI_FUNC   Ivi_AttachToConfigStoreHandle (IviConfigStoreHandle handle, ViBoolean discardExistingHandle);
ViStatus  IviDll _VI_FUNC   Ivi_GetInfoFromResourceName(ViRsrc resourceName, ViString optionString,
                                                        ViChar newResourceName[IVI_MAX_MESSAGE_BUF_SIZE],
                                                        ViChar newOptionString[IVI_MAX_MESSAGE_BUF_SIZE],
                                                        ViBoolean *isLogicalName);
    /*= Logical Names                                               ======== */
ViStatus  IviDll _VI_FUNC   Ivi_GetLogicalNamesList(IviLogicalNameEntry **logicalNamesList, ViInt32 *numLogicalNames);
ViStatus  IviDll _VI_FUNC   Ivi_GetNthLogicalName(IviLogicalNameEntry *logicalNamesList, ViInt32 index, ViChar nameBuf[], ViInt32 bufSize, ViBoolean *fromFile);
void      IviDll _VI_FUNC   Ivi_DisposeLogicalNamesList(IviLogicalNameEntry *logicalNamesList);

/*****************************************************************************/
/*= Interchangeability Warnings                                     ======== */
/*****************************************************************************/
ViStatus  IviDll _VI_FUNC   Ivi_GetNextInterchangeCheckString (ViSession vi, ViInt32 bufSize, ViChar interchangeWarning[]);
ViStatus  IviDll _VI_FUNC   Ivi_ClearInterchangeWarnings (ViSession vi);
ViStatus  IviDll _VI_FUNC   Ivi_ResetInterchangeCheck (ViSession vi);
ViStatus  IviDll _VI_FUNC   Ivi_LogInterchangeWarning (ViSession vi, ViInt32 warningType, ViInt32 funcEnum, ViConstString repCapName, ViAttr attributeId, ViConstString elab);

/*****************************************************************************/
/*= Helper Functions                                                ======== */
/*****************************************************************************/
    /*= Memory Allocation                                               ======== */
    /*= Functions for allocating memory dynamically                     ======== */
    /*= and associating it with a session.                              ======== */
    /*= If you do not explicitly free all of the memory,                ======== */
    /*= Ivi_Dispose frees it.                                           ======== */
ViStatus  IviDll _VI_FUNC   Ivi_Alloc (ViSession vi, ViInt32 memBlockSize, ViAddr *memBlockPtr);
ViStatus  IviDll _VI_FUNC   Ivi_Free (ViSession vi, ViAddr memBlockPtr);
ViStatus  IviDll _VI_FUNC   Ivi_FreeAll (ViSession vi);

    /*= String Callbacks                                            ======== */
ViStatus  IviDll _VI_FUNC   Ivi_SetValInStringCallback (ViSession vi, ViAttr attributeId, ViConstString value);

    /*= String/Value Tables                                         ======== */
ViStatus  IviDll _VI_FUNC   Ivi_GetStringFromTable(IviStringValueTable table, ViInt32 value, ViString *string);
ViStatus  IviDll _VI_FUNC   Ivi_GetValueFromTable(IviStringValueTable table, ViConstString string, ViInt32 *value);

    /*= Value Manipulation                                         ======== */
ViStatus  IviDll _VI_FUNC   Ivi_CheckNumericRange (ViReal64 value, ViReal64 min, ViReal64 max, ViStatus errorCode);
ViStatus  IviDll _VI_FUNC   Ivi_CheckBooleanRange (ViBoolean value, ViStatus errorCode);
ViStatus  IviDll _VI_FUNC   Ivi_CoerceBoolean (ViBoolean  *value);
ViStatus  IviDll _VI_FUNC   Ivi_CompareWithPrecision (ViInt32 comparePrecision, ViReal64 a, ViReal64 b, ViInt32 *result);
ViStatus  IviDll _VI_FUNC   Ivi_GetViReal64Type (ViReal64 number, ViInt32 *typeOfDouble);
ViReal64* IviDll _VI_FUNC   Ivi_GetPtrToSpecialViReal64Value (ViInt32 typeOfDouble);

/*****************************************************************************/
/*= Functions that do not have a function panel                    ========= */
/*= These are internal, unsafe, functions                          ========= */
/*****************************************************************************/
    /*= Locking                                                     ======== */
ViStatus  IviDll _VI_FUNC   Ivi_LockSession_Class(ViSession vi, ViBoolean *callerHasLock);
ViStatus  IviDll _VI_FUNC   Ivi_UnlockSession_Class(ViSession vi, ViBoolean *callerHasLock);

    /*= Non-typesafe, generic Set/Get Attribute Callback functions ========= */
ViStatus IviDll _VI_FUNC    Ivi_SetAttrCallback (ViSession vi, ViAttr attributeId, IviValueType attrType, IviCallbackType callbackType, ViAddr callback);
ViStatus IviDll _VI_FUNC    Ivi_GetAttrCallback (ViSession vi, ViAttr attributeId, IviValueType attrType, IviCallbackType callbackType, ViAddr *callback);

    /*= Localized error messages                                   ========= */
    /* Constants for languages.                                              */
#define IVI_VAL_LANG_ENGLISH   				1L
#define IVI_VAL_LANG_FRENCH					2L
#define IVI_VAL_LANG_GERMAN					3L
#define IVI_VAL_LANG_JAPANESE				4L
#define IVI_VAL_LANG_KOREAN					5L
#define IVI_VAL_LANG_CHINESE_SIMPLIFIED		6L

ViStatus IviDll _VI_FUNC    Ivi_GetErrorMessageLocalized(ViStatus statusCode, ViUInt32 locale, ViInt32 bufSize, ViChar messageBuf[]);

    /*= NI-Spy support functions                                   ========= */
ViStatus  IviDll _VI_FUNC   Ivi_GetSpyingFromLogicalName (ViConstString logicalName, ViBoolean *isSpying);

    /*= Logging interchange check warnings                         ========= */
ViStatus  IviDll _VI_FUNC   Ivi_LogInterchangeWarning2 (ViSession vi, ViInt32 warningType, ViConstString funcName, ViConstString repCapName, ViAttr attributeId, ViConstString elab);

    /*= Parameter position                                         ========= */
ViStatus IviDll _VI_FUNC    Ivi_ParamPositionError(ViInt32 parameterPosition);  /* returns one of VI_ERROR_PARAMETER1, VI_ERROR_PARAMETER2, ..., VI_ERROR_PARAMETER8, IVI_ERROR_INVALID_PARAMETER */

/*****************************************************************************/
/*= Obsolete Functions and Defintions                              ========= */
/*****************************************************************************/
/* Function pointers */
typedef ViStatus (_VI_FUNC *Ivi_IviInitFuncPtr)     (   ViRsrc resourceName, ViBoolean IDQuery,
                                                        ViBoolean resetDevice,
                                                        ViSession vi);
typedef ViStatus (_VI_FUNC *Ivi_IviCloseFuncPtr)    (   ViSession vi);

/* Deferred I/O Updates */
#define IVI_ATTR_DEFER_UPDATE               /* ViBoolean, hidden */     (IVI_ENGINE_PUBLIC_ATTR_BASE + 51)
#define IVI_ATTR_RETURN_DEFERRED_VALUES     /* ViBoolean, hidden */     (IVI_ENGINE_PUBLIC_ATTR_BASE + 52)   /* if VI_TRUE, then when get an attribute value while a deferred update is pending, return the coerced deferred value */
#define IVI_ATTR_BUFFERED_IO_CALLBACK       /* ViAddr,    hidden */     (IVI_ENGINE_PUBLIC_ATTR_BASE + 601)  /* see Ivi_BufferedIOCallbackPtr typedef */
#define IVI_ATTR_SUPPORTS_WR_BUF_OPER_MODE  /* ViBoolean, hidden */     (IVI_ENGINE_PUBLIC_ATTR_BASE + 704)  /* indicates whether instrument supports VISA buffered writes (VISA's VI_ATTR_WR_BUF_OPER_MODE) */
#define IVI_ATTR_UPDATING_VALUES            /* ViBoolean, hidden */     (IVI_ENGINE_PUBLIC_ATTR_BASE + 708)  /* is VI_TRUE while in Ivi_Update() */

/*****************************************************************************/
/*= Typedefs and contants for the Buffered I/O callback.           ========= */
/*= The Buffered I/O callback is called when the I/O buffer needs  ========= */
/*= to be flushed and before/after processing deferred updates.    ========= */
/*= Different message parameters are passed to the callback to     ========= */
/*= indicate the context in which it was called.                   ========= */
/*= A Default Buffered I/O callback is installed automatically.    ========= */
/*= The default callback assumes VISA buffered I/O.                ========= */
/*= If a specific instrument does not used VISA message-based      ========= */
/*= I/O, use the IVI_ATTR_BUFFERED_IO_CALLBACK attribute to        ========= */
/*= to set the callback function pointer to VI_NULL.               ========= */
/*****************************************************************************/
typedef ViInt32 IviMessage;

typedef ViStatus (_VI_FUNC *Ivi_BufferedIOCallbackPtr)(ViSession vi, IviMessage message);

#define IVI_MSG_START_UPDATE    1  /*  sent by Ivi_Update before processing deferred updates; Ivi_DefaultBufferedIOCallback responds by disabling VISA flush-on-write option; */
                                   /*  note:  if the buffered I/O callback returns an error, the update is aborted */
#define IVI_MSG_END_UPDATE      2  /*  sent by Ivi_Update after processing deferred updates;  Ivi_DefaultBufferedIOCallback responds by restoring the original state of the VISA I/O session */
#define IVI_MSG_SUSPEND         3  /*  sent by Ivi_Update before invoking opc callback, check status callback, and read callbacks */
                                   /*  note:  nested suspend/resume pairs can occur */
#define IVI_MSG_RESUME          4  /*  sent by Ivi_Update after invoking opc callback, check status callback, and read callbacks */
#define IVI_MSG_FLUSH           5  /*  sent by Ivi_Update after invoking the write callback for an attribute that is marked with the IVI_VAL_FLUSH_ON_WRITE flag */


/* These functions are not supported on Linux and MacOSX */
#if !defined (_IVI_linux_) && !defined(_IVI_MacOSX_)

/* prototype for the default buffered I/O callback */
ViStatus  IviDll _VI_FUNC    Ivi_DefaultBufferedIOCallback(ViSession vi, IviMessage message);

ViStatus  IviDll _VI_FUNC   Ivi_AttributeUpdateIsPending(ViSession vi, ViConstString repCapName, ViAttr attributeId, ViBoolean *updatePending);
ViStatus  IviDll _VI_FUNC   Ivi_Update(ViSession vi);

    /*
        Define a buffered write call in IVI that will be used until it is implemented in VISA.
        Driver developers should not call the Ivi_BufWrite function directly and use the
        VISA named function (viBufWrite) instead.
        This function is obsolete and should not be used. Use viBufWrite instead
    */
#if (VI_SPEC_VERSION < 0x00200000L)
#define viBufWrite Ivi_BufWrite
#endif

ViStatus  IviDll _VI_FUNC   Ivi_BufWrite (ViSession vi, ViBuf buf, ViUInt32 count, ViUInt32 *rc);

#endif
/*= Interchangeability Checking                                     ======== */
/*****************************************************************************/
/*  Interchange Check Methods: The class drivers pass the following values   */
/*  to the Ivi_SetInterchangeCheckMethod function to identify the type of the*/
/*  interchange checking that the IVI Engine performs when the class driver  */
/*  calls the Ivi_PerformInterchangeCheck function.                          */
/*****************************************************************************/
#define IVI_VAL_CHECK_IN_USER_SPECIFIED_STATE   1
#define IVI_VAL_CHECK_READ_ONLY_ATTR_NEVER_SET  2
#define IVI_VAL_CHECK_CALL_CLASS_CALLBACK       3
#define IVI_VAL_CHECK_EXEMPT                    4

ViStatus  IviDll _VI_FUNC   Ivi_InterchangeCheckAttribute (ViSession vi, ViConstString repCapName,
                                                           ViAttr attrId, ViInt32 method, ViInt32 funcEnum);
ViStatus  IviDll _VI_FUNC   Ivi_PerformInterchangeCheck (ViSession vi, IviStringValueTable attributes, ViInt32 funcEnum);
ViStatus  IviDll _VI_FUNC   Ivi_SetInterchangeCheckMethod (ViSession vi, ViConstString repCapName, ViAttr attrId, ViInt32 method);

void IviDll _VI_FUNC IviDCPwr_InterchangeCheck (ViSession vi, ViConstString funcName);
void IviDll _VI_FUNC IviDmm_InterchangeCheck (ViSession vi, ViConstString funcName);
void IviDll _VI_FUNC IviFgen_InterchangeCheck (ViSession vi, ViConstString funcName);
void IviDll _VI_FUNC IviScope_InterchangeCheck (ViSession vi, ViConstString funcName);
void IviDll _VI_FUNC IviSwtch_InterchangeCheck (ViSession vi, ViConstString funcName);

void IviDll _VI_FUNC IviDmm_DisableUnusedExtensions (ViSession vi, ViConstString funcName);
void IviDll _VI_FUNC IviFgen_DisableUnusedExtensions (ViSession vi, ViConstString funcName);
void IviDll _VI_FUNC IviScope_DisableUnusedExtensions (ViSession vi, ViConstString funcName);

/*****************************************************************************/
/*= Shortcut macros for class and specific instrument drivers       ======== */
/*****************************************************************************/

#define Ivi_Decimalize(x)         (((x>>8)*100)+(((x >> 4) & 0xF)*10)+(x & 0xF))

#define Ivi_ConvertVISAVer(x)     ((((x>>20)*100)+(((x >> 8) & 0xFFF)*10)+(x & 0xFF))/100.0)

#if defined (_CVI_)
    #define IVI_COMPILER_NAME       "CVI"
    #define IVI_COMPILER_VER_NUM    ((_CVI_)/100.0)
#elif defined(__WATCOMC__)
    #define IVI_COMPILER_NAME       "Watcom"
    #define IVI_COMPILER_VER_NUM    ((__WATCOMC__)/100.0)
#elif defined(_MSC_VER)
    #define IVI_COMPILER_NAME       "MSVC"
    #define IVI_COMPILER_VER_NUM    (14.0)
#elif defined(__BORLANDC__)
    #define IVI_COMPILER_NAME       "Borland"
    #define IVI_COMPILER_VER_NUM    ((Ivi_Decimalize(__BORLANDC__))/100.0)
#elif defined(__SC__)
    #define IVI_COMPILER_NAME       "Symantec"
    #define IVI_COMPILER_VER_NUM    ((Ivi_Decimalize(__SC__))/100.0)
#elif defined(__SUNPRO_C)
    #define IVI_COMPILER_NAME       "Sun C"
    #define IVI_COMPILER_VER_NUM    ((Ivi_Decimalize(__SUNPRO_C))/100.0)
#else
    #define IVI_COMPILER_NAME       "Unknown"
    #define IVI_COMPILER_VER_NUM    1.0
#endif



/*  This section lists all attributes and values that became obsolete. Do not use   */
/*  those attributes and values in your drivers and applications.                   */
/*  IVI_ATTR_CLASS_PREFIX is obsolete. Use IVI_ATTR_CLASS_DRIVER_PREFIX instead     */
#define IVI_ATTR_CLASS_PREFIX           /* ViString, not writable*/     (IVI_ENGINE_PUBLIC_ATTR_BASE + 301)  /* instrument prefix for the class driver;  empty string if not using class driver */
/*  IVI_ATTR_SPECIFIC_PREFIX is obsolete. Use IVI_ATTR_SPECIFIC_DRIVER_PREFIX instead */
#define IVI_ATTR_SPECIFIC_PREFIX        /* ViString, not writable*/     (IVI_ENGINE_PUBLIC_ATTR_BASE + 302)  /* instrument prefix for the specific driver */
/*  IVI_ATTR_MODULE_PATHNAME is obsolete. Use IVI_ATTR_SPECIFIC_DRIVER_LOCATOR instead */
#define IVI_ATTR_MODULE_PATHNAME        /* ViString, not writable*/     (IVI_ENGINE_PUBLIC_ATTR_BASE + 303)  /* the pathnname of the specific driver code module; from the configuration file */
/*  IVI_ATTR_DRIVER_MAJOR_VERSION is obsolete. Use IVI_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION instead */
#define IVI_ATTR_DRIVER_MAJOR_VERSION       /* ViInt32,  not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 503)
/*  IVI_ATTR_DRIVER_MINOR_VERSION is obsolete. Use IVI_ATTR_SPECIFIC_DRIVER_MINOR_VERSION instead */
#define IVI_ATTR_DRIVER_MINOR_VERSION       /* ViInt32,  not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 504)
/*  IVI_ATTR_CLASS_MAJOR_VERSION is obsolete. Use IVI_ATTR_CLASS_DRIVER_MAJOR_VERSION instead */
#define IVI_ATTR_CLASS_MAJOR_VERSION        /* ViInt32,  not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 505)
/*  IVI_ATTR_CLASS_MINOR_VERSION is obsolete. Use IVI_ATTR_CLASS_DRIVER_MINOR_VERSION instead */
#define IVI_ATTR_CLASS_MINOR_VERSION        /* ViInt32,  not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 506)
/*  IVI_ATTR_DRIVER_REVISION is obsolete. Use IVI_ATTR_SPECIFIC_DRIVER_REVISION instead */
#define IVI_ATTR_DRIVER_REVISION            /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 551)
/*  IVI_ATTR_CLASS_REVISION is obsolete. Use IVI_ATTR_CLASS_DRIVER_REVISION instead */
#define IVI_ATTR_CLASS_REVISION             /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 552)
/*  IVI_ATTR_FIRMWARE_REVISION is obsolete. Use IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION instead */
#define IVI_ATTR_FIRMWARE_REVISION          /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 510)
/*  IVI_ATTR_SUPPORTED_CLASSES is obsolete. */
#define IVI_ATTR_SUPPORTED_CLASSES      /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 323)
/*  IVI_ATTR_NUM_CHANNELS is obsolete. Use IVI_ATTR_CHANNEL_COUNT instead */
#define IVI_ATTR_NUM_CHANNELS           /* ViInt32,  not writable*/     (IVI_ENGINE_PUBLIC_ATTR_BASE + 203)   /* set by the specific-driver;  default: 1 */

/*  IVI_ATTR_QUERY_INSTR_STATUS is obsolete. Use IVI_ATTR_QUERY_INSTRUMENT_STATUS instead */
#define IVI_ATTR_QUERY_INSTR_STATUS IVI_ATTR_QUERY_INSTRUMENT_STATUS
/*  IVI_ATTR_RESOURCE_DESCRIPTOR is obsolete. Use IVI_ATTR_IO_RESOURCE_DESCRIPTOR instead */
#define IVI_ATTR_RESOURCE_DESCRIPTOR IVI_ATTR_IO_RESOURCE_DESCRIPTOR
/*  IVI_ATTR_IO_SESSION is obsolete. Use IVI_ATTR_SYSTEM_IO_SESSION instead */
#define IVI_ATTR_IO_SESSION IVI_ATTR_SYSTEM_IO_SESSION
#define IVI_ATTR_ATTRIBUTE_CAPABILITIES /* ViString, not user-writable*/(IVI_ENGINE_PUBLIC_ATTR_BASE + 403)


#ifdef __cplusplus
    }
#endif

#endif /* IVI_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviACPwr_ni.h sha256=23c356261d33f54a645f2b41fad1091ee3f0f8c46ed2f097f6ef1ca7bd41c15a bytes=40041 -->
## FILE: imports/include/IviACPwr_ni.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviACPwr_ni.h`
- sha256: `23c356261d33f54a645f2b41fad1091ee3f0f8c46ed2f097f6ef1ca7bd41c15a`
- bytes: 40041

````c
/****************************************************************************
 *                           I V I - A C P W R
 *---------------------------------------------------------------------------
 *    Copyright (c) 2011-2020 National Instruments.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:       IviACPwr_ni.h
 * Purpose:     IviACPwr Class declarations for the Base and Extended
 *              IviACPwr Capabilities.
 ****************************************************************************/

#ifndef IVIACPWR_HEADER
#define IVIACPWR_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVIACPWR_MAJOR_VERSION                        (1L)
#define IVIACPWR_MINOR_VERSION                        (0L)

#define IVIACPWR_CLASS_SPEC_MAJOR_VERSION             (1L)
#define IVIACPWR_CLASS_SPEC_MINOR_VERSION             (2L)

#define IVIACPWR_DRIVER_VENDOR                        "National Instruments"
#ifdef _IVI_mswin64_
#define IVIACPWR_DRIVER_DESCRIPTION                   "IviACPwr Class Driver [Compiled for 64-bit.]"
#else
#define IVIACPWR_DRIVER_DESCRIPTION                   "IviACPwr Class Driver"
#endif

/****************************************************************************
 *------------------------------ Useful Macros -----------------------------*
 ****************************************************************************/


/****************************************************************************
 *------------------ IviACPwr Class Attribute Defines ----------------------*
 ****************************************************************************/

    /*- IVI Inherent Attributes -*/
        /*- User Options -*/
#define IVIACPWR_ATTR_CACHE                                         IVI_ATTR_CACHE                         /* ViBoolean */
#define IVIACPWR_ATTR_RANGE_CHECK                                   IVI_ATTR_RANGE_CHECK                   /* ViBoolean */
#define IVIACPWR_ATTR_QUERY_INSTRUMENT_STATUS                       IVI_ATTR_QUERY_INSTRUMENT_STATUS       /* ViBoolean */
#define IVIACPWR_ATTR_RECORD_COERCIONS                              IVI_ATTR_RECORD_COERCIONS              /* ViBoolean */
#define IVIACPWR_ATTR_SIMULATE                                      IVI_ATTR_SIMULATE                      /* ViBoolean */
#define IVIACPWR_ATTR_INTERCHANGE_CHECK                             IVI_ATTR_INTERCHANGE_CHECK             /* ViBoolean */
#define IVIACPWR_ATTR_SPY                                           IVI_ATTR_SPY                           /* ViBoolean */
#define IVIACPWR_ATTR_USE_SPECIFIC_SIMULATION                       IVI_ATTR_USE_SPECIFIC_SIMULATION       /* ViBoolean */

        /*- Instrument Capabilities -*/
#define IVIACPWR_ATTR_GROUP_CAPABILITIES                            IVI_ATTR_GROUP_CAPABILITIES            /* ViString, read-only */
#define IVIACPWR_ATTR_FUNCTION_CAPABILITIES                         IVI_ATTR_FUNCTION_CAPABILITIES         /* ViString, read-only */

        /*- Class Driver Information -*/
#define IVIACPWR_ATTR_CLASS_DRIVER_PREFIX                           IVI_ATTR_CLASS_DRIVER_PREFIX                       /* ViString, read-only */
#define IVIACPWR_ATTR_CLASS_DRIVER_VENDOR                           IVI_ATTR_CLASS_DRIVER_VENDOR                       /* ViString, read-only */
#define IVIACPWR_ATTR_CLASS_DRIVER_DESCRIPTION                      IVI_ATTR_CLASS_DRIVER_DESCRIPTION                  /* ViString, read-only */
#define IVIACPWR_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION         IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION     /* ViInt32,  read-only */
#define IVIACPWR_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION         IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION     /* ViInt32,  read-only */

        /*- Specific Driver Information -*/
#define IVIACPWR_ATTR_SPECIFIC_DRIVER_PREFIX                        IVI_ATTR_SPECIFIC_DRIVER_PREFIX                    /* ViString, read-only */
#define IVIACPWR_ATTR_SPECIFIC_DRIVER_LOCATOR                       IVI_ATTR_SPECIFIC_DRIVER_LOCATOR                   /* ViString, read-only */
#define IVIACPWR_ATTR_IO_RESOURCE_DESCRIPTOR                        IVI_ATTR_IO_RESOURCE_DESCRIPTOR                    /* ViString, read-only */
#define IVIACPWR_ATTR_LOGICAL_NAME                                  IVI_ATTR_LOGICAL_NAME                              /* ViString, read-only */
#define IVIACPWR_ATTR_SPECIFIC_DRIVER_VENDOR                        IVI_ATTR_SPECIFIC_DRIVER_VENDOR                    /* ViString, read-only */
#define IVIACPWR_ATTR_SPECIFIC_DRIVER_DESCRIPTION                   IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION               /* ViString, read-only */
#define IVIACPWR_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION      IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIACPWR_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION      IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/
#define IVIACPWR_ATTR_INSTRUMENT_FIRMWARE_REVISION                  IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION   /* ViString, read-only */
#define IVIACPWR_ATTR_INSTRUMENT_MANUFACTURER                       IVI_ATTR_INSTRUMENT_MANUFACTURER        /* ViString, read-only */
#define IVIACPWR_ATTR_INSTRUMENT_MODEL                              IVI_ATTR_INSTRUMENT_MODEL               /* ViString, read-only */
#define IVIACPWR_ATTR_SUPPORTED_INSTRUMENT_MODELS                   IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS    /* ViString, read-only */

        /*- Version Information -*/
#define IVIACPWR_ATTR_CLASS_DRIVER_REVISION                         IVI_ATTR_CLASS_DRIVER_REVISION          /* ViString, read-only */

#define IVIACPWR_ATTR_SPECIFIC_DRIVER_REVISION                      IVI_ATTR_SPECIFIC_DRIVER_REVISION       /* ViString, read-only */

        /*- Driver Setup information -*/
#define IVIACPWR_ATTR_DRIVER_SETUP                                  IVI_ATTR_DRIVER_SETUP                   /* ViString */

    /*- IviACPwr Fundamental Attributes -*/
#define IVIACPWR_ATTR_CURRENT_LIMIT                                 (IVI_CLASS_PUBLIC_ATTR_BASE+ 13L)  /* ViReal64, applies to OutputPhase           */
#define IVIACPWR_ATTR_FREQUENCY                                     (IVI_CLASS_PUBLIC_ATTR_BASE+ 1L)   /* ViReal64                                   */
#define IVIACPWR_ATTR_NUM_PHASES                                    (IVI_CLASS_PUBLIC_ATTR_BASE+ 2L)   /* ViInt32, read-only                         */
#define IVIACPWR_ATTR_OUTPUT_ENABLED                                (IVI_CLASS_PUBLIC_ATTR_BASE+ 14L)  /* ViBoolean, applies to OutputPhase          */
#define IVIACPWR_ATTR_VOLTAGE_LEVEL                                 (IVI_CLASS_PUBLIC_ATTR_BASE+ 16L)  /* ViReal64, applies to OutputPhase           */
#define IVIACPWR_ATTR_WAVEFORM                                      (IVI_CLASS_PUBLIC_ATTR_BASE+ 17L)  /* ViString, applies to OutputPhase           */
#define IVIACPWR_ATTR_OUTPUT_PHASE_COUNT                            (IVI_CLASS_PUBLIC_ATTR_BASE+ 36L)  /* ViInt32, read-only                         */
#define IVIACPWR_ATTR_NUM_VOLTAGE_RANGES                            (IVI_CLASS_PUBLIC_ATTR_BASE+ 15L)  /* ViInt32, read-only, applies to OutputPhase */
#define IVIACPWR_ATTR_VOLTAGE_RANGE                                 (IVI_CLASS_PUBLIC_ATTR_BASE+ 18L)  /* ViReal64, applies to OutputPhase           */
#define IVIACPWR_ATTR_NUM_FREQUENCY_RANGES                          (IVI_CLASS_PUBLIC_ATTR_BASE+ 3L)   /* ViInt32, read-only                         */
#define IVIACPWR_ATTR_FREQUENCY_RANGE                               (IVI_CLASS_PUBLIC_ATTR_BASE+ 4L)   /* ViReal64                                   */

    /* IviACPwrPhase Extended Attributes */
#define IVIACPWR_ATTR_PHASE_ANGLE                                   (IVI_CLASS_PUBLIC_ATTR_BASE+ 19L)  /* ViReal64, applies to OutputPhase */

    /* IviACPwrExternalSync Extended Attributes */
#define IVIACPWR_ATTR_EXTERNAL_SYNC_ENABLED                         (IVI_CLASS_PUBLIC_ATTR_BASE+ 10L)  /* ViBoolean            */
#define IVIACPWR_ATTR_EXTERNAL_SYNC_PHASE_OFFSET                    (IVI_CLASS_PUBLIC_ATTR_BASE+ 11L)  /* ViReal64             */
#define IVIACPWR_ATTR_EXTERNAL_SYNC_LOCKED                          (IVI_CLASS_PUBLIC_ATTR_BASE+ 12L)  /* ViBoolean, read-only */

    /* IviACPwrCurrentProtection Extended Attributes */
#define IVIACPWR_ATTR_CURRENT_PROTECTION_THRESHOLD                  (IVI_CLASS_PUBLIC_ATTR_BASE+ 25L)  /* ViReal64, applies to OutputPhase             */
#define IVIACPWR_ATTR_CURRENT_PROTECTION_DELAY                      (IVI_CLASS_PUBLIC_ATTR_BASE+ 23L)  /* ViReal64, applies to OutputPhase             */
#define IVIACPWR_ATTR_CURRENT_PROTECTION_ENABLED                    (IVI_CLASS_PUBLIC_ATTR_BASE+ 24L)  /* ViBoolean, applies to OutputPhase            */
#define IVIACPWR_ATTR_CURRENT_PROTECTION_TRIPPED                    (IVI_CLASS_PUBLIC_ATTR_BASE+ 26L)  /* ViBoolean, read-only, applies to OutputPhase */

    /* IviACPwrVoltageProtection Extended Attributes */
#define IVIACPWR_ATTR_UNDER_VOLTAGE_PROTECTION_LIMIT                (IVI_CLASS_PUBLIC_ATTR_BASE+ 30L)  /* ViReal64, applies to OutputPhase             */
#define IVIACPWR_ATTR_OVER_VOLTAGE_PROTECTION_LIMIT                 (IVI_CLASS_PUBLIC_ATTR_BASE+ 28L)  /* ViReal64, applies to OutputPhase             */
#define IVIACPWR_ATTR_OVER_VOLTAGE_PROTECTION_ENABLED               (IVI_CLASS_PUBLIC_ATTR_BASE+ 27L)  /* ViBoolean, applies to OutputPhase            */
#define IVIACPWR_ATTR_UNDER_VOLTAGE_PROTECTION_ENABLED              (IVI_CLASS_PUBLIC_ATTR_BASE+ 29L)  /* ViBoolean, applies to OutputPhase            */
#define IVIACPWR_ATTR_VOLTAGE_PROTECTION_TRIPPED                    (IVI_CLASS_PUBLIC_ATTR_BASE+ 31L)  /* ViBoolean, read-only, applies to OutputPhase */

    /* IviACPwrArbWaveform Extended Attributes */
#define IVIACPWR_ATTR_NUM_WAVEFORMS_MAX                             (IVI_CLASS_PUBLIC_ATTR_BASE+ 5L)   /* ViInt32, read-only */
#define IVIACPWR_ATTR_NUM_OPTIMAL_DATA_POINTS                       (IVI_CLASS_PUBLIC_ATTR_BASE+ 6L)   /* ViInt32, read-only */
#define IVIACPWR_ATTR_FIXED_WAVEFORM_COUNT                          (IVI_CLASS_PUBLIC_ATTR_BASE+ 7L)   /* ViInt32, read-only */
#define IVIACPWR_ATTR_USER_WAVEFORM_COUNT                           (IVI_CLASS_PUBLIC_ATTR_BASE+ 8L)   /* ViInt32, read-only */
#define IVIACPWR_ATTR_AVAILABLE_WAVEFORM_COUNT                      (IVI_CLASS_PUBLIC_ATTR_BASE+ 9L)   /* ViInt32, read-only */

    /* IviACPwrImpedance Extended Attributes */
#define IVIACPWR_ATTR_OUTPUT_IMPEDANCE_ENABLED                      (IVI_CLASS_PUBLIC_ATTR_BASE+ 21L)  /* ViBoolean, applies to OutputPhase */
#define IVIACPWR_ATTR_OUTPUT_IMPEDANCE_RESISTIVE                    (IVI_CLASS_PUBLIC_ATTR_BASE+ 22L)  /* ViReal64, applies to OutputPhase  */
#define IVIACPWR_ATTR_OUTPUT_IMPEDANCE_INDUCTIVE                    (IVI_CLASS_PUBLIC_ATTR_BASE+ 20L)  /* ViReal64, applies to OutputPhase  */

    /* IviACPwrDCGeneration Extended Attributes */
#define IVIACPWR_ATTR_DC_MODE                                       (IVI_CLASS_PUBLIC_ATTR_BASE+ 32L)  /* ViInt32, applies to OutputPhase             */
#define IVIACPWR_ATTR_DC_VOLTAGE_LEVEL                              (IVI_CLASS_PUBLIC_ATTR_BASE+ 33L)  /* ViReal64, applies to OutputPhase            */
#define IVIACPWR_ATTR_DC_RANGE_MIN                                  (IVI_CLASS_PUBLIC_ATTR_BASE+ 40L)  /* ViReal64, read-only, applies to OutputPhase */
#define IVIACPWR_ATTR_DC_RANGE_MAX                                  (IVI_CLASS_PUBLIC_ATTR_BASE+ 41L)  /* ViReal64, read-only, applies to OutputPhase */
#define IVIACPWR_ATTR_DC_NUM_RANGES                                 (IVI_CLASS_PUBLIC_ATTR_BASE+ 35L)  /* ViInt32, read-only, applies to OutputPhase  */

    /* IviACPwrVoltageRamp Extended Attributes */
#define IVIACPWR_ATTR_VOLTAGE_RAMP_BUSY                             (IVI_CLASS_PUBLIC_ATTR_BASE+ 37L)  /* ViBoolean, read-only, applies to OutputPhase */

    /* IviACPwrCurrentRamp Extended Attributes */
#define IVIACPWR_ATTR_CURRENT_RAMP_BUSY                             (IVI_CLASS_PUBLIC_ATTR_BASE+ 38L)  /* ViBoolean, read-only, applies to OutputPhase */

    /* IviACPwrFrequencyRamp Extended Attributes */
#define IVIACPWR_ATTR_FREQUENCY_RAMP_BUSY                           (IVI_CLASS_PUBLIC_ATTR_BASE+ 39L)  /* ViBoolean, read-only */

/****************************************************************************
 *----------------- IviACPwr Class Attribute Value Defines -----------------*
 ****************************************************************************/
    /*- Values Defines for IVIACPWR_ATTR_DC_MODE -*/
#define IVIACPWR_VAL_MODE_AC_ONLY                           (0L)
#define IVIACPWR_VAL_MODE_DC_ONLY                           (1L)
#define IVIACPWR_VAL_MODE_AC_DC                             (2L)

#define IVIACPWR_VAL_DC_MODE_CLASS_EXT_BASE                 (500L)
#define IVIACPWR_VAL_DC_MODE_SPECIFIC_EXT_BASE              (1000L)

/****************************************************************************
 *----------------- IviACPwr Function Parameter Value Definitions ----------*
 ****************************************************************************/

    /*- Fetch Measurement -*/
#define IVIACPWR_VAL_MEASURE_VOLTAGE_RMS_LN                 (0L)
#define IVIACPWR_VAL_MEASURE_CURRENT_RMS                    (1L)
#define IVIACPWR_VAL_MEASURE_FREQUENCY                      (2L)
#define IVIACPWR_VAL_MEASURE_VOLTAGE_DC                     (3L)
#define IVIACPWR_VAL_MEASURE_CURRENT_DC                     (4L)
#define IVIACPWR_VAL_MEASURE_POWER_FACTOR                   (5L)
#define IVIACPWR_VAL_MEASURE_CREST_FACTOR                   (6L)
#define IVIACPWR_VAL_MEASURE_CURRENT_PEAK                   (7L)
#define IVIACPWR_VAL_MEASURE_POWER_VA                       (8L)
#define IVIACPWR_VAL_MEASURE_POWER_REAL                     (9L)
#define IVIACPWR_VAL_MEASURE_POWER_DC                       (10L)
#define IVIACPWR_VAL_MEASURE_PHASE_ANGLE                    (11L)
#define IVIACPWR_VAL_MEASURE_VOLTAGE_RMS_LL                 (12L)
#define IVIACPWR_VAL_MEASURE_CURRENT_OHD                    (13L)
#define IVIACPWR_VAL_MEASURE_CURRENT_EHD                    (14L)
#define IVIACPWR_VAL_MEASURE_CURRENT_THD                    (15L)
#define IVIACPWR_VAL_MEASURE_VOLTAGE_OHD                    (16L)
#define IVIACPWR_VAL_MEASURE_VOLTAGE_EHD                    (17L)
#define IVIACPWR_VAL_MEASURE_VOLTAGE_THD                    (18L)

    /*- Fetch Measurement Array -*/
#define IVIACPWR_VAL_MEASURE_ARRAY_CURRENT_HARMONIC_PHASE   (0L)
#define IVIACPWR_VAL_MEASURE_ARRAY_CURRENT_HARMONIC_ABS     (1L)
#define IVIACPWR_VAL_MEASURE_ARRAY_CURRENT_HARMONIC_PCT     (2L)
#define IVIACPWR_VAL_MEASURE_ARRAY_VOLTAGE_HARMONIC_PHASE   (3L)
#define IVIACPWR_VAL_MEASURE_ARRAY_VOLTAGE_HARMONIC_ABS     (4L)
#define IVIACPWR_VAL_MEASURE_ARRAY_VOLTAGE_HARMONIC_PCT     (5L)
#define IVIACPWR_VAL_MEASURE_ARRAY_CURRENT_CYCLE            (6L)
#define IVIACPWR_VAL_MEASURE_ARRAY_VOLTAGE_CYCLE            (7L)

    /*- Initiate Measurement -*/
#define IVIACPWR_VAL_MEASUREMENT_GROUP_BASE                 (1L)
#define IVIACPWR_VAL_MEASUREMENT_GROUP_HARMONIC             (2L)
#define IVIACPWR_VAL_MEASUREMENT_GROUP_DISTORTION           (4L)
#define IVIACPWR_VAL_MEASUREMENT_GROUP_WAVEFORM             (8L)

    /*- Query Arbitrary Waveform Catalog -*/
#define IVIACPWR_VAL_WAVEFORM_CATALOG_FIXED                 (0L)
#define IVIACPWR_VAL_WAVEFORM_CATALOG_USER                  (1L)
#define IVIACPWR_VAL_WAVEFORM_CATALOG_ALL                   (2L)

/****************************************************************************
 *--------- IviACPwr Class Instrument Driver Function Declarations ---------*
 ****************************************************************************/
    /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviACPwr_init(ViRsrc logicalName,
                                ViBoolean idQuery,
                                ViBoolean resetDevice,
                                ViSession *vi);

ViStatus _VI_FUNC IviACPwr_close(ViSession vi);

ViStatus _VI_FUNC IviACPwr_reset(ViSession vi);

ViStatus _VI_FUNC IviACPwr_self_test(ViSession vi,
                                     ViInt16 *selfTestResult,
                                     ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviACPwr_error_query(ViSession vi,
                                       ViInt32 *errorCode,
                                       ViChar errorMessage[]);

ViStatus _VI_FUNC IviACPwr_error_message(ViSession vi,
                                         ViStatus statusCode,
                                         ViChar message[]);

ViStatus _VI_FUNC IviACPwr_revision_query(ViSession vi,
                                          ViChar driverRev[],
                                          ViChar instrRev[]);

    /*- Utility Functions -*/
ViStatus _VI_FUNC IviACPwr_InvalidateAllAttributes(ViSession vi);

ViStatus _VI_FUNC IviACPwr_ResetWithDefaults(ViSession vi);

ViStatus _VI_FUNC IviACPwr_Disable(ViSession vi);


    /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviACPwr_InitWithOptions(ViRsrc logicalName,
                                           ViBoolean IDQuery,
                                           ViBoolean resetDevice,
                                           ViConstString optionString,
                                           ViSession *vi);

    /*- Set, Get, and Check Attribute Functions -*/
ViStatus _VI_FUNC IviACPwr_GetAttributeViInt32(ViSession vi,
                                               ViConstString PhaseName,
                                               ViAttr attributeId,
                                               ViInt32 *value);

ViStatus _VI_FUNC IviACPwr_SetAttributeViInt32(ViSession vi,
                                               ViConstString PhaseName,
                                               ViAttr attributeId,
                                               ViInt32 value);

ViStatus _VI_FUNC IviACPwr_CheckAttributeViInt32(ViSession vi,
                                                 ViConstString PhaseName,
                                                 ViAttr attributeId,
                                                 ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviACPwr_GetAttributeViInt64(ViSession vi, 
                                               ViConstString PhaseName,
                                               ViAttr attributeId, 
                                               ViInt64 *value);

ViStatus _VI_FUNC IviACPwr_SetAttributeViInt64(ViSession vi, 
                                               ViConstString PhaseName,
                                               ViAttr attributeId,
                                               ViInt64 value);

ViStatus _VI_FUNC IviACPwr_CheckAttributeViInt64(ViSession vi,
                                                 ViConstString PhaseName,
                                                 ViAttr attributeId,
                                                 ViInt64 value);
#endif

ViStatus _VI_FUNC IviACPwr_GetAttributeViReal64(ViSession vi,
                                                ViConstString PhaseName,
                                                ViAttr attributeId,
                                                ViReal64 *value);

ViStatus _VI_FUNC IviACPwr_SetAttributeViReal64(ViSession vi,
                                                ViConstString PhaseName,
                                                ViAttr attributeId,
                                                ViReal64 value);

ViStatus _VI_FUNC IviACPwr_CheckAttributeViReal64(ViSession vi,
                                                  ViConstString PhaseName,
                                                  ViAttr attributeId,
                                                  ViReal64 value);

ViStatus _VI_FUNC IviACPwr_GetAttributeViString(ViSession vi,
                                                ViConstString PhaseName,
                                                ViAttr attributeId,
                                                ViInt32 bufferSize,
                                                ViChar value[]);

ViStatus _VI_FUNC IviACPwr_SetAttributeViString(ViSession vi,
                                                ViConstString PhaseName,
                                                ViAttr attributeId,
                                                ViConstString value);

ViStatus _VI_FUNC IviACPwr_CheckAttributeViString(ViSession vi,
                                                  ViConstString PhaseName,
                                                  ViAttr attributeId,
                                                  ViConstString value);

ViStatus _VI_FUNC IviACPwr_GetAttributeViBoolean(ViSession vi,
                                                 ViConstString PhaseName,
                                                 ViAttr attributeId,
                                                 ViBoolean *value);

ViStatus _VI_FUNC IviACPwr_SetAttributeViBoolean(ViSession vi,
                                                 ViConstString PhaseName,
                                                 ViAttr attributeId,
                                                 ViBoolean value);

ViStatus _VI_FUNC IviACPwr_CheckAttributeViBoolean(ViSession vi,
                                                   ViConstString PhaseName,
                                                   ViAttr attributeId,
                                                   ViBoolean value);

ViStatus _VI_FUNC IviACPwr_GetAttributeViSession(ViSession vi,
                                                 ViConstString PhaseName,
                                                 ViAttr attributeId,
                                                 ViSession *value);

ViStatus _VI_FUNC IviACPwr_SetAttributeViSession(ViSession vi,
                                                 ViConstString PhaseName,
                                                 ViAttr attributeId,
                                                 ViSession value);

ViStatus _VI_FUNC IviACPwr_CheckAttributeViSession(ViSession vi,
                                                   ViConstString PhaseName,
                                                   ViAttr attributeId,
                                                   ViSession value);

    /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviACPwr_LockSession(ViSession vi,
                                       ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviACPwr_UnlockSession(ViSession vi,
                                         ViBoolean *callerHasLock);

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviACPwr_GetError(ViSession vi,
                                    ViStatus *errorCode,
                                    ViInt32 bufferSize,
                                    ViChar description[]);

ViStatus _VI_FUNC IviACPwr_ClearError(ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviACPwr_GetNextInterchangeWarning(ViSession vi,
                                                     ViInt32 bufferSize,
                                                     ViChar warning[]);

ViStatus _VI_FUNC IviACPwr_ClearInterchangeWarnings(ViSession vi);
ViStatus _VI_FUNC IviACPwr_ResetInterchangeCheck(ViSession vi);

ViStatus _VI_FUNC IviACPwr_GetNextCoercionRecord(ViSession vi,
                                                 ViInt32 bufferSize,
                                                 ViChar record[]);

ViStatus _VI_FUNC IviACPwr_GetSpecificDriverCHandle(ViSession vi,
                                                    ViSession* specificDriverCHandle);

ViStatus _VI_FUNC IviACPwr_GetSpecificDriverIUnknownPtr(ViSession vi,
                                                        void* specificDriverIUnknownPtr);

    /*- IviACPwrBase Functions -*/
ViStatus _VI_FUNC IviACPwr_ConfigureCurrentLimit(ViSession vi,
                                                 ViConstString PhaseName,
                                                 ViReal64 Limit);
ViStatus _VI_FUNC IviACPwr_ConfigureOutputEnabled(ViSession vi,
                                                  ViConstString PhaseName,
                                                  ViBoolean Enabled);
ViStatus _VI_FUNC IviACPwr_ConfigureVoltageLevel(ViSession vi,
                                                 ViConstString PhaseName,
                                                 ViReal64 VoltageLevel);
ViStatus _VI_FUNC IviACPwr_ConfigureVoltageRange(ViSession vi,
                                                 ViConstString PhaseName,
                                                 ViReal64 Range);
ViStatus _VI_FUNC IviACPwr_ConfigureFrequency(ViSession vi,
                                              ViReal64 Frequency);
ViStatus _VI_FUNC IviACPwr_ConfigureFrequencyRange(ViSession vi,
                                                   ViReal64 Range);
ViStatus _VI_FUNC IviACPwr_ConfigureWaveform(ViSession vi,
                                             ViConstString PhaseName,
                                             ViConstString WaveformName);
ViStatus _VI_FUNC IviACPwr_QueryVoltageRangeCapabilities(ViSession vi,
                                                         ViConstString PhaseName,
                                                         ViInt32 Range,
                                                         ViConstString WaveformName,
                                                         ViReal64 * MinVoltage,
                                                         ViReal64 * MaxVoltage);
ViStatus _VI_FUNC IviACPwr_QueryFrequencyRangeCapabilities(ViSession vi,
                                                           ViInt32 Range,
                                                           ViReal64 * MinFrequency,
                                                           ViReal64 * MaxFrequency);
ViStatus _VI_FUNC IviACPwr_GetOutputPhaseName(ViSession vi,
                                              ViInt32 Index,
                                              ViInt32 NameBufferSize,
                                              ViChar  Name[]);

    /*- IviACPwrMeasurement Functions -*/
ViStatus _VI_FUNC IviACPwr_InitiateMeasurement(ViSession vi,
                                               ViInt32 Group);
ViStatus _VI_FUNC IviACPwr_FetchMeasurement(ViSession vi,
                                            ViConstString PhaseName,
                                            ViInt32 MeasurementType,
                                            ViReal64 * Measurement);
ViStatus _VI_FUNC IviACPwr_FetchMeasurementArray(ViSession vi,
                                                 ViConstString PhaseName,
                                                 ViInt32 MeasurementType,
                                                 ViInt32 MeasurementBufferSize,
                                                 ViReal64 Measurement[],
                                                 ViInt32 * MeasurementActualSize);

    /*- IviACPwrPhase Functions -*/
ViStatus _VI_FUNC IviACPwr_ConfigurePhaseAngle(ViSession vi,
                                               ViConstString PhaseName,
                                               ViReal64 PhaseAngle);

    /*- IviACPwrExternalSync Functions -*/
ViStatus _VI_FUNC IviACPwr_ConfigureExternalSync(ViSession vi,
                                                 ViBoolean Enabled,
                                                 ViReal64  PhaseOffset);
ViStatus _VI_FUNC IviACPwr_QueryExternalSyncLocked(ViSession vi,
                                                   ViBoolean * Locked);

    /*- IviACPwrCurrentProtection Functions -*/
ViStatus _VI_FUNC IviACPwr_QueryCurrentProtectionTripped(ViSession vi,
                                                         ViConstString PhaseName,
                                                         ViBoolean * Tripped);
ViStatus _VI_FUNC IviACPwr_ResetCurrentProtection(ViSession vi,
                                                  ViConstString PhaseName);
ViStatus _VI_FUNC IviACPwr_ConfigureCurrentProtection(ViSession vi,
                                                      ViConstString PhaseName,
                                                      ViBoolean Enabled,
                                                      ViReal64 Threshold,
                                                      ViReal64 Delay);

    /*- IviACPwrVoltageProtection Functions -*/
ViStatus _VI_FUNC IviACPwr_QueryVoltageProtectionTripped(ViSession vi,
                                                         ViConstString PhaseName,
                                                         ViBoolean * Tripped);
ViStatus _VI_FUNC IviACPwr_ResetVoltageProtection(ViSession vi,
                                                  ViConstString PhaseName);
ViStatus _VI_FUNC IviACPwr_ConfigureVoltageProtection(ViSession vi,
                                                      ViConstString PhaseName,
                                                      ViBoolean UnderEnabled,
                                                      ViBoolean OverEnabled,
                                                      ViReal64 UnderLimit,
                                                      ViReal64 OverLimit);

    /*- IviACPwrArbWaveform Functions -*/
ViStatus _VI_FUNC IviACPwr_ClearArbWaveform(ViSession vi,
                                            ViConstString WaveformName);

ViStatus _VI_FUNC IviACPwr_WriteArbWaveform(ViSession vi,
                                            ViConstString WaveformName,
                                            ViInt32 WaveformDataBufferSize,
                                            ViReal64 WaveformData[]);

ViStatus _VI_FUNC IviACPwr_QueryArbWaveformCatalog(ViSession vi,
                                                   ViInt32 CatalogType,
                                                   ViInt32 CatalogBufferSize,
                                                   ViChar Catalog[]);

    /*- IviACPwrImpedance Functions -*/
ViStatus _VI_FUNC IviACPwr_ConfigureOutputImpedance(ViSession vi,
                                                    ViConstString PhaseName,
                                                    ViBoolean Enabled,
                                                    ViReal64 ResistiveValue,
                                                    ViReal64 InductiveValue);

ViStatus _VI_FUNC IviACPwr_QueryOutputImpedanceCapabilities(ViSession vi,
                                                            ViConstString PhaseName,
                                                            ViReal64 * ResistiveMin,
                                                            ViReal64 * ResistiveMax,
                                                            ViReal64 * InductiveMin,
                                                            ViReal64 * InductiveMax);

    /*- IviACPwrDCGeneration Functions -*/
ViStatus _VI_FUNC IviACPwr_ConfigureDC(ViSession vi,
                                       ViConstString PhaseName,
                                       ViInt32 Mode,
                                       ViReal64 DCVoltageLevel);
ViStatus _VI_FUNC IviACPwr_ConfigureDCRange(ViSession vi,
                                            ViConstString PhaseName,
                                            ViReal64 Minimum,
                                            ViReal64 Maximum);
ViStatus _VI_FUNC IviACPwr_QueryDCCapabilities(ViSession vi,
                                               ViConstString PhaseName,
                                               ViInt32 Range,
                                               ViReal64 * Minimum,
                                               ViReal64 * Maximum);

    /*- IviACPwrVoltageRamp Functions -*/
ViStatus _VI_FUNC IviACPwr_RampVoltage(ViSession vi,
                                       ViConstString PhaseName,
                                       ViReal64 StartVoltage,
                                       ViReal64 EndVoltage,
                                       ViReal64 Duration);
ViStatus _VI_FUNC IviACPwr_QueryVoltageRampBusy(ViSession vi,
                                                ViConstString PhaseName,
                                                ViBoolean * Busy);
ViStatus _VI_FUNC IviACPwr_AbortVoltageRamp(ViSession vi,
                                            ViConstString PhaseName);

    /*- IviACPwrCurrentRamp Functions -*/
ViStatus _VI_FUNC IviACPwr_RampCurrent(ViSession vi,
                                       ViConstString PhaseName,
                                       ViReal64 StartCurrent,
                                       ViReal64 EndCurrent,
                                       ViReal64 Duration);
ViStatus _VI_FUNC IviACPwr_QueryCurrentRampBusy(ViSession vi,
                                                ViConstString PhaseName,
                                                ViBoolean * Busy);
ViStatus _VI_FUNC IviACPwr_AbortCurrentRamp(ViSession vi,
                                            ViConstString PhaseName);

    /*- IviACPwrFrequencyRamp Functions -*/
ViStatus _VI_FUNC IviACPwr_RampFrequency(ViSession vi,
                                         ViReal64 StartFrequency,
                                         ViReal64 EndFrequency,
                                         ViReal64 Duration);
ViStatus _VI_FUNC IviACPwr_QueryFrequencyRampBusy(ViSession vi,
                                                  ViBoolean * Busy);
ViStatus _VI_FUNC IviACPwr_AbortFrequencyRamp(ViSession vi);

/****************************************************************************
 *--------------- IviACPwr Class Error And Completion Codes ----------------*
 ****************************************************************************/
#define IVIACPWR_ERROR_ALL_PHASES_REQUIRED               (IVI_CLASS_ERROR_BASE + 0x0002L)
#define IVIACPWR_ERROR_CURRENT_PROTECTION                (IVI_CLASS_ERROR_BASE + 0x0003L)
#define IVIACPWR_ERROR_DUPLICATE_WAVEFORM_NAME           (IVI_CLASS_ERROR_BASE + 0x0004L)
#define IVIACPWR_ERROR_INVALID_WAVEFORM_NAME             (IVI_CLASS_ERROR_BASE + 0x0005L)
#define IVIACPWR_ERROR_MEASUREMENT_NOT_INITIATED         (IVI_CLASS_ERROR_BASE + 0x0006L)
#define IVIACPWR_ERROR_MEASUREMENT_NOT_SUPPORTED         (IVI_CLASS_ERROR_BASE + 0x0007L)
#define IVIACPWR_ERROR_NO_WAVEFORMS_AVAILABLE            (IVI_CLASS_ERROR_BASE + 0x0008L)
#define IVIACPWR_ERROR_PHASE_VALUES_DIFFERENT            (IVI_CLASS_ERROR_BASE + 0x000AL)
#define IVIACPWR_ERROR_UNSUPPORTED_MEASUREMENT_GROUP     (IVI_CLASS_ERROR_BASE + 0x000BL)
#define IVIACPWR_ERROR_VOLTAGE_PROTECTION                (IVI_CLASS_ERROR_BASE + 0x000CL)
#define IVIACPWR_ERROR_WAVEFORM_IN_USE                   (IVI_CLASS_ERROR_BASE + 0x000EL)
#define IVIACPWR_ERROR_WAVEFORM_NOT_FOUND                (IVI_CLASS_ERROR_BASE + 0x000FL)
#define IVIACPWR_ERROR_WAVEFORM_RESERVED                 (IVI_CLASS_ERROR_BASE + 0x0010L)
#define IVIACPWR_ERROR_WAVEFORM_DC_OFFSET                (IVI_CLASS_ERROR_BASE + 0x000DL)
#define IVIACPWR_ERROR_ALL_PHASES_NOT_SUPPORTED          (IVI_CLASS_ERROR_BASE + 0x0001L)
#define IVIACPWR_ERROR_OUTPUT_ENABLED                    (IVI_CLASS_ERROR_BASE + 0x0009L)

#define IVIACPWR_ERRMSG_ALL_PHASES_REQUIRED              "All phases required."
#define IVIACPWR_ERRMSG_CURRENT_PROTECTION               "Current protection tripped."
#define IVIACPWR_ERRMSG_DUPLICATE_WAVEFORM_NAME          "Duplicate waveform name."
#define IVIACPWR_ERRMSG_INVALID_WAVEFORM_NAME            "Invalid waveform name."
#define IVIACPWR_ERRMSG_MEASUREMENT_NOT_INITIATED        "Measurement not initiated."
#define IVIACPWR_ERRMSG_MEASUREMENT_NOT_SUPPORTED        "Measurement not supported."
#define IVIACPWR_ERRMSG_NO_WAVEFORMS_AVAILABLE           "No waveforms available."
#define IVIACPWR_ERRMSG_PHASE_VALUES_DIFFERENT           "Phase values different."
#define IVIACPWR_ERRMSG_UNSUPPORTED_MEASUREMENT_GROUP    "Unsupported measurement group."
#define IVIACPWR_ERRMSG_VOLTAGE_PROTECTION               "Voltage Protection tripped."
#define IVIACPWR_ERRMSG_WAVEFORM_IN_USE                  "Waveform in use."
#define IVIACPWR_ERRMSG_WAVEFORM_NOT_FOUND               "Waveform not found."
#define IVIACPWR_ERRMSG_WAVEFORM_RESERVED                "Waveform reserved."
#define IVIACPWR_ERRMSG_WAVEFORM_DC_OFFSET               "Waveform DC Offset."
#define IVIACPWR_ERRMSG_ALL_PHASES_NOT_SUPPORTED         "All phases not supported."
#define IVIACPWR_ERRMSG_OUTPUT_ENABLED                   "Output is enabled."

#define IVIACPWR_ERROR_CODES_AND_MSGS \
        { IVIACPWR_ERROR_ALL_PHASES_REQUIRED,            IVIACPWR_ERRMSG_ALL_PHASES_REQUIRED           }, \
        { IVIACPWR_ERROR_CURRENT_PROTECTION,             IVIACPWR_ERRMSG_CURRENT_PROTECTION            }, \
        { IVIACPWR_ERROR_DUPLICATE_WAVEFORM_NAME,        IVIACPWR_ERRMSG_DUPLICATE_WAVEFORM_NAME       }, \
        { IVIACPWR_ERROR_INVALID_WAVEFORM_NAME,          IVIACPWR_ERRMSG_INVALID_WAVEFORM_NAME         }, \
        { IVIACPWR_ERROR_MEASUREMENT_NOT_INITIATED,      IVIACPWR_ERRMSG_MEASUREMENT_NOT_INITIATED     }, \
        { IVIACPWR_ERROR_MEASUREMENT_NOT_SUPPORTED,      IVIACPWR_ERRMSG_MEASUREMENT_NOT_SUPPORTED     }, \
        { IVIACPWR_ERROR_NO_WAVEFORMS_AVAILABLE,         IVIACPWR_ERRMSG_NO_WAVEFORMS_AVAILABLE        }, \
        { IVIACPWR_ERROR_PHASE_VALUES_DIFFERENT,         IVIACPWR_ERRMSG_PHASE_VALUES_DIFFERENT        }, \
        { IVIACPWR_ERROR_UNSUPPORTED_MEASUREMENT_GROUP,  IVIACPWR_ERRMSG_UNSUPPORTED_MEASUREMENT_GROUP }, \
        { IVIACPWR_ERROR_VOLTAGE_PROTECTION,             IVIACPWR_ERRMSG_VOLTAGE_PROTECTION            }, \
        { IVIACPWR_ERROR_WAVEFORM_IN_USE,                IVIACPWR_ERRMSG_WAVEFORM_IN_USE               }, \
        { IVIACPWR_ERROR_WAVEFORM_NOT_FOUND,             IVIACPWR_ERRMSG_WAVEFORM_NOT_FOUND            }, \
        { IVIACPWR_ERROR_WAVEFORM_RESERVED,              IVIACPWR_ERRMSG_WAVEFORM_RESERVED             }, \
        { IVIACPWR_ERROR_WAVEFORM_DC_OFFSET,             IVIACPWR_ERRMSG_WAVEFORM_DC_OFFSET            }, \
        { IVIACPWR_ERROR_ALL_PHASES_NOT_SUPPORTED,       IVIACPWR_ERRMSG_ALL_PHASES_NOT_SUPPORTED      }, \
        { IVIACPWR_ERROR_OUTPUT_ENABLED,                 IVIACPWR_ERRMSG_OUTPUT_ENABLED                }

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

#endif /* IVIACPWR_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviCounter_ni.h sha256=66e49b6629f6d166ed9437645ed1d915411552a08328e0bf2b03b8f404b47793 bytes=33206 -->
## FILE: imports/include/IviCounter_ni.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviCounter_ni.h`
- sha256: `66e49b6629f6d166ed9437645ed1d915411552a08328e0bf2b03b8f404b47793`
- bytes: 33206

````c
/****************************************************************************
 *                           I V I - C O U N T E R                               
 *---------------------------------------------------------------------------
 *    Copyright (c) 2009-2020 National Instruments.  All Rights Reserved.        
 *---------------------------------------------------------------------------
 *                                                                          
 * Title:       ivicounter_ni.h                                                    
 * Purpose:     IviCounter Class declarations for the Base and Extended  
 *              IviCounter Capabilities.                                        
 ****************************************************************************/

#ifndef IVICOUNTER_HEADER
#define IVICOUNTER_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVICOUNTER_MAJOR_VERSION              (4L)
#define IVICOUNTER_MINOR_VERSION              (0L)

#define IVICOUNTER_CLASS_SPEC_MAJOR_VERSION   (2L)
#define IVICOUNTER_CLASS_SPEC_MINOR_VERSION   (0L)

#define IVICOUNTER_DRIVER_VENDOR              "National Instruments"
#ifdef	_IVI_mswin64_
#define IVICOUNTER_DRIVER_DESCRIPTION         "IviCounter Class Driver [Compiled for 64-bit.]"
#else
#define IVICOUNTER_DRIVER_DESCRIPTION			"IviCounter Class Driver"
#endif

/****************************************************************************
 *------------------------------ Useful Macros -----------------------------*
 ****************************************************************************/

/****************************************************************************
 *------------------ IviCounter Class Attribute Defines ----------------------*
 ****************************************************************************/

    /*- IVI Inherent Attributes -*/

        /*- User Options -*/
#define IVICOUNTER_ATTR_CACHE                     IVI_ATTR_CACHE                       /* ViBoolean */
#define IVICOUNTER_ATTR_RANGE_CHECK               IVI_ATTR_RANGE_CHECK                 /* ViBoolean */
#define IVICOUNTER_ATTR_QUERY_INSTRUMENT_STATUS   IVI_ATTR_QUERY_INSTRUMENT_STATUS     /* ViBoolean */
#define IVICOUNTER_ATTR_RECORD_COERCIONS          IVI_ATTR_RECORD_COERCIONS            /* ViBoolean */
#define IVICOUNTER_ATTR_SIMULATE                  IVI_ATTR_SIMULATE                    /* ViBoolean */
#define IVICOUNTER_ATTR_INTERCHANGE_CHECK         IVI_ATTR_INTERCHANGE_CHECK           /* ViBoolean */
#define IVICOUNTER_ATTR_SPY                       IVI_ATTR_SPY                         /* ViBoolean */
#define IVICOUNTER_ATTR_USE_SPECIFIC_SIMULATION   IVI_ATTR_USE_SPECIFIC_SIMULATION     /* ViBoolean */

        /*- Instrument Capabilities -*/
#define IVICOUNTER_ATTR_GROUP_CAPABILITIES        IVI_ATTR_GROUP_CAPABILITIES          /* ViString, read-only */
#define IVICOUNTER_ATTR_FUNCTION_CAPABILITIES     IVI_ATTR_FUNCTION_CAPABILITIES       /* ViString, read-only */

        /*- Class Driver Information -*/    
#define IVICOUNTER_ATTR_CLASS_DRIVER_PREFIX                     IVI_ATTR_CLASS_DRIVER_PREFIX         /* ViString, read-only */
#define IVICOUNTER_ATTR_CLASS_DRIVER_VENDOR                     IVI_ATTR_CLASS_DRIVER_VENDOR         /* ViString, read-only */
#define IVICOUNTER_ATTR_CLASS_DRIVER_DESCRIPTION                IVI_ATTR_CLASS_DRIVER_DESCRIPTION    /* ViString, read-only */
#define IVICOUNTER_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION   IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVICOUNTER_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION   IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Specific Driver Information -*/    
#define IVICOUNTER_ATTR_SPECIFIC_DRIVER_PREFIX                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX      /* ViString, read-only */
#define IVICOUNTER_ATTR_SPECIFIC_DRIVER_LOCATOR                     IVI_ATTR_SPECIFIC_DRIVER_LOCATOR     /* ViString, read-only */
#define IVICOUNTER_ATTR_IO_RESOURCE_DESCRIPTOR                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR      /* ViString, read-only */
#define IVICOUNTER_ATTR_LOGICAL_NAME                                IVI_ATTR_LOGICAL_NAME                /* ViString, read-only */
#define IVICOUNTER_ATTR_SPECIFIC_DRIVER_VENDOR                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR      /* ViString, read-only */
#define IVICOUNTER_ATTR_SPECIFIC_DRIVER_DESCRIPTION                 IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION /* ViString, read-only */
#define IVICOUNTER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVICOUNTER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/    
#define IVICOUNTER_ATTR_INSTRUMENT_FIRMWARE_REVISION     IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION /* ViString, read-only */
#define IVICOUNTER_ATTR_INSTRUMENT_MANUFACTURER          IVI_ATTR_INSTRUMENT_MANUFACTURER      /* ViString, read-only */
#define IVICOUNTER_ATTR_INSTRUMENT_MODEL                 IVI_ATTR_INSTRUMENT_MODEL             /* ViString, read-only */
#define IVICOUNTER_ATTR_SUPPORTED_INSTRUMENT_MODELS      IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS

        /*- Version Information -*/
#define IVICOUNTER_ATTR_CLASS_DRIVER_REVISION            IVI_ATTR_CLASS_DRIVER_REVISION              /* ViString, read-only */

#define IVICOUNTER_ATTR_SPECIFIC_DRIVER_REVISION         IVI_ATTR_SPECIFIC_DRIVER_REVISION             /* ViString, read-only */

        /*- Driver Setup Information -*/
#define IVICOUNTER_ATTR_DRIVER_SETUP              		 IVI_ATTR_DRIVER_SETUP                /* ViString */

    /*- IviCounter Fundamental Attributes -*/
#define IVICOUNTER_ATTR_CHANNEL_COUNT					IVI_ATTR_CHANNEL_COUNT				/* ViInt32,  read-only */	
#define IVICOUNTER_ATTR_MEASUREMENT_FUNCTION		    (IVI_CLASS_PUBLIC_ATTR_BASE + 3L)	/* ViInt32		*/
#define IVICOUNTER_ATTR_IMPEDANCE				        (IVI_CLASS_PUBLIC_ATTR_BASE + 4L)	/* ViInt32		*/
#define IVICOUNTER_ATTR_COUPLING			            (IVI_CLASS_PUBLIC_ATTR_BASE + 5L)	/* ViInt32		*/
#define IVICOUNTER_ATTR_ATTENUATION			            (IVI_CLASS_PUBLIC_ATTR_BASE + 6L)	/* ViReal64		*/        
#define IVICOUNTER_ATTR_CHANNEL_LEVEL				    (IVI_CLASS_PUBLIC_ATTR_BASE + 7L)	/* ViReal64		*/    
#define IVICOUNTER_ATTR_CHANNEL_HYSTERESIS			    (IVI_CLASS_PUBLIC_ATTR_BASE + 8L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_CHANNEL_SLOPE				    (IVI_CLASS_PUBLIC_ATTR_BASE + 9L)	/* ViInt32		*/    
#define IVICOUNTER_ATTR_FILTER_ENABLED				    (IVI_CLASS_PUBLIC_ATTR_BASE + 10L)	/* ViBoolean	*/
#define IVICOUNTER_ATTR_FREQUENCY_CHANNEL		        (IVI_CLASS_PUBLIC_ATTR_BASE + 11L)	/* ViString		*/
#define IVICOUNTER_ATTR_FREQUENCY_ESTIMATE			    (IVI_CLASS_PUBLIC_ATTR_BASE + 12L)	/* ViReal64		*/		 
#define IVICOUNTER_ATTR_FREQUENCY_RESOLUTION		    (IVI_CLASS_PUBLIC_ATTR_BASE + 13L)	/* ViReal64		*/   
#define IVICOUNTER_ATTR_FREQUENCY_APERTURE_TIME		    (IVI_CLASS_PUBLIC_ATTR_BASE + 14L)	/* ViReal64		*/ 	
#define IVICOUNTER_ATTR_FREQUENCY_ESTIMATE_AUTO		    (IVI_CLASS_PUBLIC_ATTR_BASE + 15L)	/* ViBoolean	*/
#define IVICOUNTER_ATTR_FREQUENCY_RESOLUTION_AUTO	    (IVI_CLASS_PUBLIC_ATTR_BASE + 16L)	/* ViBoolean	*/
#define IVICOUNTER_ATTR_PERIOD_CHANNEL	                (IVI_CLASS_PUBLIC_ATTR_BASE + 18L)  /* ViString		*/
#define IVICOUNTER_ATTR_PERIOD_ESTIMATE				    (IVI_CLASS_PUBLIC_ATTR_BASE + 19L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_PERIOD_RESOLUTION			    (IVI_CLASS_PUBLIC_ATTR_BASE + 20L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_PERIOD_APERTURE_TIME			(IVI_CLASS_PUBLIC_ATTR_BASE + 21L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_PULSE_WIDTH_CHANNEL             (IVI_CLASS_PUBLIC_ATTR_BASE + 22L)  /* ViString		*/
#define IVICOUNTER_ATTR_PULSE_WIDTH_ESTIMATE			(IVI_CLASS_PUBLIC_ATTR_BASE + 23L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_PULSE_WIDTH_RESOLUTION		    (IVI_CLASS_PUBLIC_ATTR_BASE + 24L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_DUTY_CYCLE_CHANNEL			    (IVI_CLASS_PUBLIC_ATTR_BASE + 25L)  /* ViString		*/
#define IVICOUNTER_ATTR_DUTY_CYCLE_FREQUENCY_ESTIMATE	(IVI_CLASS_PUBLIC_ATTR_BASE + 26L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_DUTY_CYCLE_RESOLUTION		    (IVI_CLASS_PUBLIC_ATTR_BASE + 27L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_EDGE_TIME_CHANNEL	            (IVI_CLASS_PUBLIC_ATTR_BASE + 28L)  /* ViString		*/
#define IVICOUNTER_ATTR_EDGE_TIME_REFERENCE_TYPE		(IVI_CLASS_PUBLIC_ATTR_BASE + 29L)  /* ViInt32		*/
#define IVICOUNTER_ATTR_EDGE_TIME_ESTIMATE		        (IVI_CLASS_PUBLIC_ATTR_BASE + 30L) 	/* ViReal64		*/
#define IVICOUNTER_ATTR_EDGE_TIME_RESOLUTION			(IVI_CLASS_PUBLIC_ATTR_BASE + 31L) 	/* ViReal64		*/
#define IVICOUNTER_ATTR_EDGE_TIME_HIGH_REFERENCE	    (IVI_CLASS_PUBLIC_ATTR_BASE + 32L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_EDGE_TIME_LOW_REFERENCE		    (IVI_CLASS_PUBLIC_ATTR_BASE + 33L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_FREQUENCY_RATIO_NUMERATOR_CHANNEL	(IVI_CLASS_PUBLIC_ATTR_BASE + 34L)   /*ViString   */
#define IVICOUNTER_ATTR_FREQUENCY_RATIO_DENOMINATOR_CHANNEL			    (IVI_CLASS_PUBLIC_ATTR_BASE + 35L)	/* ViString		*/
#define IVICOUNTER_ATTR_FREQUENCY_RATIO_NUMERATOR_FREQUENCY_ESTIMATE	(IVI_CLASS_PUBLIC_ATTR_BASE + 36L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_FREQUENCY_RATIO_ESTIMATE	    (IVI_CLASS_PUBLIC_ATTR_BASE + 37L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_FREQUENCY_RATIO_RESOLUTION	    (IVI_CLASS_PUBLIC_ATTR_BASE + 38L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_TIME_INTERVAL_START_CHANNEL	    (IVI_CLASS_PUBLIC_ATTR_BASE + 39L)  /* ViString		*/
#define IVICOUNTER_ATTR_TIME_INTERVAL_STOP_CHANNEL	    (IVI_CLASS_PUBLIC_ATTR_BASE + 40L)	/* ViString		*/
#define IVICOUNTER_ATTR_TIME_INTERVAL_ESTIMATE	        (IVI_CLASS_PUBLIC_ATTR_BASE + 41L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_TIME_INTERVAL_RESOLUTION	    (IVI_CLASS_PUBLIC_ATTR_BASE + 42L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_PHASE_INPUT_CHANNEL	            (IVI_CLASS_PUBLIC_ATTR_BASE + 43L)  /* ViString		*/
#define IVICOUNTER_ATTR_PHASE_REFERENCE_CHANNEL	        (IVI_CLASS_PUBLIC_ATTR_BASE + 44L)	/* ViString		*/
#define IVICOUNTER_ATTR_PHASE_FREQUENCY_ESTIMATE	    (IVI_CLASS_PUBLIC_ATTR_BASE + 45L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_PHASE_RESOLUTION		        (IVI_CLASS_PUBLIC_ATTR_BASE + 46L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_CONTINUOUS_TOTALIZE_CHANNEL	    (IVI_CLASS_PUBLIC_ATTR_BASE + 47L)  /* ViString		*/
#define IVICOUNTER_ATTR_GATED_TOTALIZE_CHANNEL	        (IVI_CLASS_PUBLIC_ATTR_BASE + 48L)  /* ViString		*/
#define IVICOUNTER_ATTR_GATED_TOTALIZE_GATE_SOURCE	    (IVI_CLASS_PUBLIC_ATTR_BASE + 49L)	/* ViString		*/
#define IVICOUNTER_ATTR_GATED_TOTALIZE_GATE_SLOPE		(IVI_CLASS_PUBLIC_ATTR_BASE + 50L)	/* ViInt32		*/
#define IVICOUNTER_ATTR_TIMED_TOTALIZE_CHANNEL	        (IVI_CLASS_PUBLIC_ATTR_BASE + 51L)  /* ViString		*/
#define IVICOUNTER_ATTR_TIMED_TOTALIZE_GATE_TIME		(IVI_CLASS_PUBLIC_ATTR_BASE + 52L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_START_ARM_TYPE				    (IVI_CLASS_PUBLIC_ATTR_BASE + 53L) 	/* ViInt32		*/
#define IVICOUNTER_ATTR_EXTERNAL_START_ARM_SOURCE		(IVI_CLASS_PUBLIC_ATTR_BASE + 54L)	/* ViString		*/
#define IVICOUNTER_ATTR_EXTERNAL_START_ARM_LEVEL		(IVI_CLASS_PUBLIC_ATTR_BASE + 55L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_EXTERNAL_START_ARM_SLOPE		(IVI_CLASS_PUBLIC_ATTR_BASE + 56L)	/* ViInt32		*/
#define IVICOUNTER_ATTR_EXTERNAL_START_ARM_DELAY	    (IVI_CLASS_PUBLIC_ATTR_BASE + 57L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_STOP_ARM_TYPE				    (IVI_CLASS_PUBLIC_ATTR_BASE + 58L)	/* ViInt32		*/
#define IVICOUNTER_ATTR_EXTERNAL_STOP_ARM_SOURCE		(IVI_CLASS_PUBLIC_ATTR_BASE + 59L)	/* ViString		*/
#define IVICOUNTER_ATTR_EXTERNAL_STOP_ARM_LEVEL			(IVI_CLASS_PUBLIC_ATTR_BASE + 60L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_EXTERNAL_STOP_ARM_SLOPE			(IVI_CLASS_PUBLIC_ATTR_BASE + 61L)	/* ViInt32		*/
#define IVICOUNTER_ATTR_EXTERNAL_STOP_ARM_DELAY			(IVI_CLASS_PUBLIC_ATTR_BASE + 62L)	/* ViReal64		*/

 /*- IviCounter Filter Group Attributes ---------------*/
#define IVICOUNTER_ATTR_FILTER_MINIMUM_FREQUENCY		(IVI_CLASS_PUBLIC_ATTR_BASE + 501L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_FILTER_MAXIMUM_FREQUENCY		(IVI_CLASS_PUBLIC_ATTR_BASE + 502L)	/* ViReal64		*/

 /*- IviCounter Time Interval Delay Group Attributes ---------------*/
#define IVICOUNTER_ATTR_TIME_INTERVAL_STOP_HOLDOFF		(IVI_CLASS_PUBLIC_ATTR_BASE + 601L)/* ViReal64		*/

 /*- IviCounter Voltage Measurement Group Attributes ---------------*/
#define IVICOUNTER_ATTR_VOLTAGE_CHANNEL	                (IVI_CLASS_PUBLIC_ATTR_BASE + 701L) /* ViString		*/
#define IVICOUNTER_ATTR_VOLTAGE_ESTIMATE			    (IVI_CLASS_PUBLIC_ATTR_BASE + 702L)	/* ViReal64		*/
#define IVICOUNTER_ATTR_VOLTAGE_RESOLUTION			    (IVI_CLASS_PUBLIC_ATTR_BASE + 703L)	/* ViReal64		*/

/****************************************************************************
 *----------------- IviCounter Class Attribute Value Defines -----------------*
 ****************************************************************************/

    /*- Defined values for attribute IVICOUNTER_ATTR_COUPLING -*/
#define IVICOUNTER_VAL_AC	 						      (1L)   
#define IVICOUNTER_VAL_DC							      (2L)   

#define IVICOUNTER_VAL_COUPLING_CLASS_EXT_BASE            (500L)
#define IVICOUNTER_VAL_COUPLING_SPECIFIC_EXT_BASE         (1000L) 
 
    /*- Defined values for attribute IVICOUNTER_ATTR_CHANNEL_SLOPE -*/
    /*- Defined values for attribute IVICOUNTER_ATTR_GATED_TOTALIZE_GATE_SLOPE -*/
    /*- Defined values for attribute IVICOUNTER_ATTR_EXTERNAL_START_ARM_SLOPE -*/
    /*- Defined values for attribute IVICOUNTER_ATTR_EXTERNAL_STOP_ARM_SLOPE -*/	
#define IVICOUNTER_VAL_NEGATIVE                           (0L)
#define IVICOUNTER_VAL_POSITIVE                           (1L)
	
#define IVICOUNTER_VAL_SLOPE_CLASS_EXT_BASE            	  (500L)
#define IVICOUNTER_VAL_SLOPE_SPECIFIC_EXT_BASE            (1000L)
	
    /*- Defined values for attribute IVICOUNTER_ATTR_MEASUREMENT_FUNCTION -*/
#define IVICOUNTER_VAL_FREQUENCY			              (1L)
#define IVICOUNTER_VAL_FREQUENCY_WITH_APERTURE			  (2L)
#define IVICOUNTER_VAL_PERIOD							  (3L)
#define IVICOUNTER_VAL_PERIOD_WITH_APERTURE				  (4L)
#define IVICOUNTER_VAL_PULSE_WIDTH						  (5L)
#define IVICOUNTER_VAL_DUTY_CYCLE						  (6L)
#define IVICOUNTER_VAL_EDGE_TIME						  (7L)
#define IVICOUNTER_VAL_FREQUENCY_RATIO					  (8L)
#define IVICOUNTER_VAL_TIME_INTERVAL					  (9L)
#define IVICOUNTER_VAL_PHASE							  (10L)
#define IVICOUNTER_VAL_CONTINUOUS_TOTALIZE				  (11L)
#define IVICOUNTER_VAL_GATED_TOTALIZE					  (12L)
#define IVICOUNTER_VAL_TIMED_TOTALIZE					  (13L)
#define IVICOUNTER_VAL_DC_VOLTAGE						  (14L)
#define IVICOUNTER_VAL_MAXIMUM_VOLTAGE					  (15L)
#define IVICOUNTER_VAL_MINIMUM_VOLTAGE					  (16L)
#define IVICOUNTER_VAL_RMS_VOLTAGE						  (17L)
#define IVICOUNTER_VAL_PEAK_TO_PEAK_VOLTAGE				  (18L)

#define IVICOUNTER_VAL_MEASUREMENT_FUNCTION_CLASS_EXT_BASE (500L)
#define IVICOUNTER_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE (1000L)
	
    /*- Defined values for attribute IVICOUNTER_ATTR_START_ARM_TYPE -*/
    /*- Defined values for attribute IVICOUNTER_ATTR_STOP_ARM_TYPE -*/
#define IVICOUNTER_VAL_IMMEDIATE_ARM_TYPE                 (1L)
#define IVICOUNTER_VAL_EXTERNAL_ARM_TYPE			      (2L)

#define IVICOUNTER_VAL_ARM_TYPE_CLASS_EXT_BASE            (500L)
#define IVICOUNTER_VAL_ARM_TYPE_SPECIFIC_EXT_BASE         (1000L)
	
    /*- Defined values for attribute IVICOUNTER_ATTR_EDGE_TIME_REFERENCE_TYPE -*/	
#define IVICOUNTER_VAL_VOLTAGE_REFERENCE_TYPE			  (1L)
#define IVICOUNTER_VAL_PERCENT_REFERENCE_TYPE			  (2L)

#define IVICOUNTER_VAL_REFERENCE_TYPE_CLASS_EXT_BASE	  (500L)
#define IVICOUNTER_VAL_REFERENCE_TYPE_SPECIFIC_EXT_BASE   (1000L)

    /*- Defined values for Function Parameters  -*/
#define IVICOUNTER_VAL_MAX_TIME_IMMEDIATE				  (0L)
#define IVICOUNTER_VAL_MAX_TIME_INFINITE				  (-1L)

#define IVICOUNTER_VAL_MEASUREMENT_COMPLETE        (1L)   
#define IVICOUNTER_VAL_MEASUREMENT_IN_PROGRESS     (0L)   
#define IVICOUNTER_VAL_MEASUREMENT_STATUS_UNKNOWN         (-1L) 

/****************************************************************************
 *--------- IviCounter Class Instrument Driver Function Declarations -----------*
 ****************************************************************************/
    /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviCounter_init (ViRsrc logicalName, 
                               ViBoolean idQuery, 
                               ViBoolean resetDevice, 
                               ViSession *vi);

ViStatus _VI_FUNC IviCounter_close (ViSession vi);

ViStatus _VI_FUNC IviCounter_reset (ViSession vi);

ViStatus _VI_FUNC IviCounter_self_test (ViSession vi, 
                                    ViInt16 *selfTestResult, 
                                    ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviCounter_error_query (ViSession vi, 
                                      ViInt32 *errorCode, 
                                      ViChar errorMessage[]);

ViStatus _VI_FUNC IviCounter_error_message (ViSession vi, 
                                        ViStatus statusCode, 
                                        ViChar message[]);

ViStatus _VI_FUNC IviCounter_revision_query (ViSession vi, 
                                         ViChar driverRev[], 
                                         ViChar instrRev[]);

    /*- Utility Functions -*/
ViStatus _VI_FUNC IviCounter_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviCounter_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviCounter_Disable (ViSession vi);

    /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviCounter_InitWithOptions (ViRsrc logicalName, 
                                          ViBoolean IDQuery,
                                          ViBoolean resetDevice, 
                                          ViConstString optionString, 
                                          ViSession *vi);

    /*- Set, Get, and Check Attribute Functions -*/
ViStatus _VI_FUNC IviCounter_GetAttributeViInt32 (ViSession vi, 
                                              ViConstString channelName,
                                              ViAttr attributeId,
                                              ViInt32 *value);

ViStatus _VI_FUNC IviCounter_SetAttributeViInt32 (ViSession vi, 
                                              ViConstString channelName,
                                              ViAttr attributeId,
                                              ViInt32 value);

ViStatus _VI_FUNC IviCounter_CheckAttributeViInt32 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviCounter_GetAttributeViInt64 (ViSession vi, 
                                              ViConstString channelName,
                                              ViAttr attributeId,
                                              ViInt64 *value);

ViStatus _VI_FUNC IviCounter_SetAttributeViInt64 (ViSession vi, 
                                              ViConstString channelName,
                                              ViAttr attributeId,
                                              ViInt64 value);

ViStatus _VI_FUNC IviCounter_CheckAttributeViInt64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt64 value);
#endif
												
ViStatus _VI_FUNC IviCounter_GetAttributeViReal64 (ViSession vi, 
                                               ViConstString channelName, 
                                               ViAttr attributeId, 
                                               ViReal64 *value);

ViStatus _VI_FUNC IviCounter_SetAttributeViReal64 (ViSession vi, 
                                               ViConstString channelName, 
                                               ViAttr attributeId, 
                                               ViReal64 value);

ViStatus _VI_FUNC IviCounter_CheckAttributeViReal64 (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 value);

ViStatus _VI_FUNC IviCounter_GetAttributeViString (ViSession vi, 
                                               ViConstString channelName, 
                                               ViAttr attributeId, 
                                               ViInt32 bufferSize, 
                                               ViChar value[]);

ViStatus _VI_FUNC IviCounter_SetAttributeViString (ViSession vi, 
                                               ViConstString channelName, 
                                               ViAttr attributeId, 
                                               ViConstString value);

ViStatus _VI_FUNC IviCounter_CheckAttributeViString (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViConstString value); 

ViStatus _VI_FUNC IviCounter_GetAttributeViBoolean (ViSession vi, 
                                                ViConstString channelName, 
                                                ViAttr attributeId, 
                                                ViBoolean *value);

ViStatus _VI_FUNC IviCounter_SetAttributeViBoolean (ViSession vi, 
                                                ViConstString channelName, 
                                                ViAttr attributeId, 
                                                ViBoolean value);

ViStatus _VI_FUNC IviCounter_CheckAttributeViBoolean (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean value);

ViStatus _VI_FUNC IviCounter_GetAttributeViSession (ViSession vi, 
                                                ViConstString channelName, 
                                                ViAttr attributeId, 
                                                ViSession *value);

ViStatus _VI_FUNC IviCounter_SetAttributeViSession (ViSession vi, 
                                                ViConstString channelName, 
                                                ViAttr attributeId, 
                                                ViSession value);

ViStatus _VI_FUNC IviCounter_CheckAttributeViSession (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViSession value);

    /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviCounter_LockSession (ViSession vi, 
                                      ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviCounter_UnlockSession (ViSession vi, 
                                        ViBoolean *callerHasLock);

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviCounter_GetError (ViSession vi, 
                                   ViStatus *errorCode, 
                                   ViInt32 bufferSize, 
                                   ViChar description[]);

ViStatus _VI_FUNC IviCounter_ClearError (ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviCounter_GetNextInterchangeWarning (ViSession vi, 
                                                    ViInt32 bufferSize,
                                                    ViChar warning[]);

ViStatus _VI_FUNC IviCounter_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviCounter_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviCounter_GetNextCoercionRecord (ViSession vi,
                                                ViInt32 bufferSize, 
                                                ViChar record[]);

ViStatus _VI_FUNC IviCounter_GetSpecificDriverCHandle (ViSession vi,
                                                   ViSession* specificDriverCHandle);

ViStatus _VI_FUNC IviCounter_GetSpecificDriverIUnknownPtr (ViSession vi,
                                                       void* specificDriverIUnknownPtr);
    /*- IviCounterBase Functions -*/
ViStatus _VI_FUNC IviCounter_GetChannelName (ViSession vi, 
                                      ViInt32 ChannelIndex,
                                      ViInt32 ChannelNameBufferSize,
                                      ViChar ChannelName[]);
	
ViStatus _VI_FUNC IviCounter_ConfigureChannel (ViSession vi, 
													  ViConstString Channel, 
													  ViReal64 Impedance, 
													  ViInt32 Coupling,
													  ViReal64 Attenuation);

ViStatus _VI_FUNC IviCounter_ConfigureChannelLevel (ViSession vi, 
														   ViConstString Channel, 
														   ViReal64 TriggerLevel, 
														   ViReal64 Hysteresis);													  
								
ViStatus _VI_FUNC IviCounter_ConfigureChannelSlope (ViSession vi, 
														   ViConstString Channel, 
														   ViInt32 Slope);
								
ViStatus _VI_FUNC IviCounter_ConfigureChannelFilterEnabled (ViSession vi, 
																   ViConstString Channel, 
																   ViBoolean FilterEnabled);

ViStatus _VI_FUNC IviCounter_ConfigureFrequency (ViSession vi, 
													    ViConstString Channel);

ViStatus _VI_FUNC IviCounter_ConfigureFrequencyManual (ViSession vi, 
															  ViConstString Channel, 
															  ViReal64 Estimate, 
															  ViReal64 Resolution);
													
ViStatus _VI_FUNC IviCounter_ConfigureFrequencyWithApertureTime (ViSession vi, 
																		ViConstString Channel, 
																		ViReal64 ApertureTime);	
													
ViStatus _VI_FUNC IviCounter_ConfigurePeriod (ViSession vi, 
													 ViConstString Channel, 
													 ViReal64 Estimate, 
													 ViReal64 Resolution);

ViStatus _VI_FUNC IviCounter_ConfigurePeriodWithApertureTime (ViSession vi, 
																	 ViConstString Channel, 
																	 ViReal64 ApertureTime);
											
ViStatus _VI_FUNC IviCounter_ConfigurePulseWidth (ViSession vi, 
														 ViConstString Channel, 
														 ViReal64 Estimate, 
														 ViReal64 Resolution);
				
ViStatus _VI_FUNC IviCounter_ConfigureDutyCycle (ViSession vi, 
														ViConstString Channel, 
														ViReal64 FrequencyEstimate, 
														ViReal64 Resolution);

ViStatus _VI_FUNC IviCounter_ConfigureEdgeTime (ViSession vi, 
													   ViConstString Channel, 
													   ViReal64 Estimate, 
													   ViReal64 Resolution);												 
	
ViStatus _VI_FUNC IviCounter_ConfigureEdgeTimeReferenceLevels (ViSession vi,
                                                      ViConstString Channel,
                                                      ViInt32 ReferenceType,
                                                      ViReal64 Estimate,
                                                      ViReal64 Resolution,
                                                      ViReal64 HighReference,
                                                      ViReal64 LowReference);
		
ViStatus _VI_FUNC IviCounter_ConfigureFrequencyRatio (ViSession vi, 
															 ViConstString NumeratorChannel,
															 ViConstString DenominatorChannel, 
															 ViReal64 NumeratorFrequencyEstimate,
															 ViReal64 Estimate,
															 ViReal64 Resolution);	
	
ViStatus _VI_FUNC IviCounter_ConfigureTimeInterval (ViSession vi, 
														   ViConstString StartChannel,
														   ViConstString StopChannel, 
														   ViReal64 Estimate, 
														   ViReal64 Resolution);	
	
ViStatus _VI_FUNC IviCounter_ConfigurePhase (ViSession vi, 
													ViConstString MeasurementChannel, 
													ViConstString ReferenceChannel, 
													ViReal64 FrequencyEstimate,
													ViReal64 Resolution);	
													
ViStatus _VI_FUNC IviCounter_ConfigureContinuousTotalize (ViSession vi, 
															     ViConstString Channel);	
	
ViStatus _VI_FUNC IviCounter_ConfigureGatedTotalize (ViSession vi, 
															ViConstString Channel,
															ViConstString GateSource, 
															ViInt32 GateSlope);
		
ViStatus _VI_FUNC IviCounter_ConfigureTimedTotalize (ViSession vi, 
															ViConstString Channel, 
															ViReal64 GateTime);		
		
ViStatus _VI_FUNC IviCounter_ConfigureStartArm (ViSession vi, 
													   ViInt32 Type);		
		
ViStatus _VI_FUNC IviCounter_ConfigureExternalStartArm (ViSession vi, 
															   ViConstString Source,
															   ViReal64 Level, 
															   ViInt32 Slope,
															   ViReal64 Delay);	

ViStatus _VI_FUNC IviCounter_ConfigureStopArm (ViSession vi, 
													  ViInt32 Type);															   
															   
ViStatus _VI_FUNC IviCounter_ConfigureExternalStopArm (ViSession vi, 
															  ViConstString Source,
															  ViReal64 Level, 
															  ViInt32 Slope,
															  ViReal64 Delay);

ViStatus _VI_FUNC IviCounter_ConfigureFilter (ViSession vi, 
													 ViConstString Channel, 
													 ViReal64 MinimumFrequency, 
													 ViReal64 MaximumFrequency);	

ViStatus _VI_FUNC IviCounter_ConfigureTimeIntervalStopHoldoff (ViSession vi, 
																ViReal64 Time);	

ViStatus _VI_FUNC IviCounter_ConfigureVoltage (ViSession vi, 
													  ViConstString Channel, 
													  ViInt32 Function, 
													  ViReal64 Estimate,
													  ViReal64 Resolution);																  
															  
ViStatus _VI_FUNC IviCounter_StartContinuousTotalize (ViSession vi);	

ViStatus _VI_FUNC IviCounter_StopContinuousTotalize (ViSession vi);																  
															  
ViStatus _VI_FUNC IviCounter_FetchContinuousTotalizeCount (ViSession vi, ViInt32* Measurement);
										
ViStatus _VI_FUNC IviCounter_Read (ViSession vi, 
                                 ViInt32 MaximumTime, 
                                 ViReal64 *Measurement);

ViStatus _VI_FUNC IviCounter_Initiate (ViSession vi);								 
								 
ViStatus _VI_FUNC IviCounter_Abort (ViSession vi);

ViStatus _VI_FUNC IviCounter_Fetch (ViSession vi, 
                                  ViReal64 *Measurement);
										
ViStatus _VI_FUNC IviCounter_IsMeasurementComplete (ViSession vi, ViInt32* MeasurementStatus);		
													  
/****************************************************************************
 *--------------- IviCounter Class Error And Completion Codes ----------------*
 ****************************************************************************/
#define IVICOUNTER_WARN_MEASURE_UNCALIBRATED    (IVI_CLASS_WARN_BASE + 0x0001L)

#define IVICOUNTER_ERRMSG_MEASURE_UNCALIBRATED  "The instrument was in an uncalibrated state when the measurement was taken."
	
#define IVICOUNTER_WARN_OVER_RANGE              (IVI_CLASS_WARN_BASE + 0x0002L)

#define IVICOUNTER_ERRMSG_OVER_RANGE            "The measurement taken was over the instrument's range."
	
#define IVICOUNTER_ERROR_MAX_TIME_EXCEEDED      (IVI_CLASS_ERROR_BASE + 0x0003L)

#define IVICOUNTER_ERRMSG_MAX_TIME_EXCEEDED     "The maximum waiting time for this operation was exceeded."	

#define IVICOUNTER_ERROR_CODES_AND_MSGS \
        {IVICOUNTER_WARN_MEASURE_UNCALIBRATED, IVICOUNTER_ERRMSG_MEASURE_UNCALIBRATED}, \
	   {IVICOUNTER_WARN_OVER_RANGE, IVICOUNTER_ERRMSG_OVER_RANGE}, \
	   {IVICOUNTER_ERROR_MAX_TIME_EXCEEDED, IVICOUNTER_ERRMSG_MAX_TIME_EXCEEDED}
	
/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

#endif /* IVICOUNTER_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviDCPwr.h sha256=40c57d200a621fa89ab0e0f33667a027411039695a728b5f03f51697e1360213 bytes=24609 -->
## FILE: imports/include/IviDCPwr.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviDCPwr.h`
- sha256: `40c57d200a621fa89ab0e0f33667a027411039695a728b5f03f51697e1360213`
- bytes: 24609

````c
/****************************************************************************
 *                           I V I - D C P W R                               
 *---------------------------------------------------------------------------
 *    Copyright (c) 2000-2020 National Instruments.  All Rights Reserved.        
 *---------------------------------------------------------------------------
 *                                                                          
 * Title:       ividcpwr.h                                                    
 * Purpose:     IviDCPwr Class declarations for the Base and Extended  
 *              IviDCPwr Capabilities.                                        
 ****************************************************************************/

#ifndef IVIDCPWR_HEADER
#define IVIDCPWR_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVIDCPWR_MAJOR_VERSION              (4L)
#define IVIDCPWR_MINOR_VERSION              (0L)

#define IVIDCPWR_CLASS_SPEC_MAJOR_VERSION   (3L)
#define IVIDCPWR_CLASS_SPEC_MINOR_VERSION   (0L)

#define IVIDCPWR_DRIVER_VENDOR              "National Instruments"
#ifdef	_IVI_mswin64_
#define IVIDCPWR_DRIVER_DESCRIPTION         "IviDCPwr Class Driver [Compiled for 64-bit.]"
#else
#define IVIDCPWR_DRIVER_DESCRIPTION         "IviDCPwr Class Driver"
#endif

/****************************************************************************
 *------------------------------ Useful Macros -----------------------------*
 ****************************************************************************/

    /*- Defined values for rangeType parameter of function -*/
    /*- IviDCPwr_ConfigureOutputRange -*/
#define IVIDCPWR_VAL_RANGE_CURRENT                  (0L)
#define IVIDCPWR_VAL_RANGE_VOLTAGE                  (1L)

#define IVIDCPWR_VAL_RANGE_TYPE_CLASS_EXT_BASE      (500L)
#define IVIDCPWR_VAL_RANGE_TYPE_SPECIFIC_EXT_BASE   (1000L)

    /*- Defined values for outputState parameter of function -*/
    /*- IviDCPwr_QueryOutputState -*/
#define IVIDCPWR_VAL_OUTPUT_CONSTANT_VOLTAGE        (0L)
#define IVIDCPWR_VAL_OUTPUT_CONSTANT_CURRENT        (1L)
#define IVIDCPWR_VAL_OUTPUT_OVER_VOLTAGE            (2L)
#define IVIDCPWR_VAL_OUTPUT_OVER_CURRENT            (3L)
#define IVIDCPWR_VAL_OUTPUT_UNREGULATED             (4L)

#define IVIDCPWR_VAL_OUTPUT_STATE_CLASS_EXT_BASE    (500L)
#define IVIDCPWR_VAL_OUTPUT_STATE_SPECIFIC_EXT_BASE (1000L)

    /*- Defined values for measurementType parameter of function -*/
    /*- IviDCPwr_Measure -*/
#define IVIDCPWR_VAL_MEASURE_CURRENT            (0L)
#define IVIDCPWR_VAL_MEASURE_VOLTAGE            (1L)

#define IVIDCPWR_VAL_MEASURE_CLASS_EXT_BASE     (500L)
#define IVIDCPWR_VAL_MEASURE_SPECIFIC_EXT_BASE  (1000L)

/****************************************************************************
 *------------------ IviDCPwr Class Attribute Defines ----------------------*
 ****************************************************************************/

    /*- IVI Inherent Attributes -*/
        /*- User Options -*/
#define IVIDCPWR_ATTR_CACHE                     IVI_ATTR_CACHE                         /* ViBoolean */
#define IVIDCPWR_ATTR_RANGE_CHECK               IVI_ATTR_RANGE_CHECK                   /* ViBoolean */
#define IVIDCPWR_ATTR_QUERY_INSTRUMENT_STATUS   IVI_ATTR_QUERY_INSTRUMENT_STATUS       /* ViBoolean */
#define IVIDCPWR_ATTR_RECORD_COERCIONS          IVI_ATTR_RECORD_COERCIONS              /* ViBoolean */
#define IVIDCPWR_ATTR_SIMULATE                  IVI_ATTR_SIMULATE                      /* ViBoolean */
#define IVIDCPWR_ATTR_INTERCHANGE_CHECK         IVI_ATTR_INTERCHANGE_CHECK             /* ViBoolean */
#define IVIDCPWR_ATTR_SPY                       IVI_ATTR_SPY                           /* ViBoolean */
#define IVIDCPWR_ATTR_USE_SPECIFIC_SIMULATION   IVI_ATTR_USE_SPECIFIC_SIMULATION       /* ViBoolean */

        /*- Instrument Capabilities -*/
#define IVIDCPWR_ATTR_GROUP_CAPABILITIES        IVI_ATTR_GROUP_CAPABILITIES            /* ViString, read-only */
#define IVIDCPWR_ATTR_FUNCTION_CAPABILITIES     IVI_ATTR_FUNCTION_CAPABILITIES         /* ViString, read-only */

        /*- Class Driver Information -*/    
#define IVIDCPWR_ATTR_CLASS_DRIVER_PREFIX                         IVI_ATTR_CLASS_DRIVER_PREFIX                       /* ViString, read-only */
#define IVIDCPWR_ATTR_CLASS_DRIVER_VENDOR                         IVI_ATTR_CLASS_DRIVER_VENDOR                       /* ViString, read-only */
#define IVIDCPWR_ATTR_CLASS_DRIVER_DESCRIPTION                    IVI_ATTR_CLASS_DRIVER_DESCRIPTION                  /* ViString, read-only */
#define IVIDCPWR_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION     /* ViInt32,  read-only */
#define IVIDCPWR_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION     /* ViInt32,  read-only */

        /*- Specific Driver Information -*/    
#define IVIDCPWR_ATTR_SPECIFIC_DRIVER_PREFIX                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX                    /* ViString, read-only */
#define IVIDCPWR_ATTR_SPECIFIC_DRIVER_LOCATOR                     IVI_ATTR_SPECIFIC_DRIVER_LOCATOR                   /* ViString, read-only */
#define IVIDCPWR_ATTR_IO_RESOURCE_DESCRIPTOR                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR                       /* ViString, read-only */
#define IVIDCPWR_ATTR_LOGICAL_NAME                                IVI_ATTR_LOGICAL_NAME                              /* ViString, read-only */
#define IVIDCPWR_ATTR_SPECIFIC_DRIVER_VENDOR                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR                    /* ViString, read-only */
#define IVIDCPWR_ATTR_SPECIFIC_DRIVER_DESCRIPTION                 IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION               /* ViString, read-only */
#define IVIDCPWR_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIDCPWR_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/    
#define IVIDCPWR_ATTR_INSTRUMENT_FIRMWARE_REVISION     IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION   /* ViString, read-only */
#define IVIDCPWR_ATTR_INSTRUMENT_MANUFACTURER          IVI_ATTR_INSTRUMENT_MANUFACTURER        /* ViString, read-only */
#define IVIDCPWR_ATTR_INSTRUMENT_MODEL                 IVI_ATTR_INSTRUMENT_MODEL               /* ViString, read-only */
#define IVIDCPWR_ATTR_SUPPORTED_INSTRUMENT_MODELS      IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS    /* ViString, read-only */
    
        /*- Version Information -*/
#define IVIDCPWR_ATTR_CLASS_DRIVER_REVISION            IVI_ATTR_CLASS_DRIVER_REVISION          /* ViString, read-only */

#define IVIDCPWR_ATTR_SPECIFIC_DRIVER_REVISION         IVI_ATTR_SPECIFIC_DRIVER_REVISION       /* ViString, read-only */

        /*- Driver Setup information -*/
#define IVIDCPWR_ATTR_DRIVER_SETUP                     IVI_ATTR_DRIVER_SETUP                   /* ViString */

    /*- IviDCPwr Fundamental Attributes -*/
#define IVIDCPWR_ATTR_CHANNEL_COUNT             IVI_ATTR_CHANNEL_COUNT                 /* ViInt32,  read-only */
#define IVIDCPWR_ATTR_VOLTAGE_LEVEL             (IVI_CLASS_PUBLIC_ATTR_BASE + 1L)      /* ViReal64,  multi-channel */
#define IVIDCPWR_ATTR_OVP_ENABLED               (IVI_CLASS_PUBLIC_ATTR_BASE + 2L)      /* ViBoolean, multi-channel */
#define IVIDCPWR_ATTR_OVP_LIMIT                 (IVI_CLASS_PUBLIC_ATTR_BASE + 3L)      /* ViReal64,  multi-channel */
#define IVIDCPWR_ATTR_CURRENT_LIMIT_BEHAVIOR    (IVI_CLASS_PUBLIC_ATTR_BASE + 4L)      /* ViInt32,   multi-channel */
#define IVIDCPWR_ATTR_CURRENT_LIMIT             (IVI_CLASS_PUBLIC_ATTR_BASE + 5L)      /* ViReal64,  multi-channel */
#define IVIDCPWR_ATTR_OUTPUT_ENABLED            (IVI_CLASS_PUBLIC_ATTR_BASE + 6L)      /* ViBoolean, multi-channel */

    /*- IviDCPwr Extended Attributes -*/
        /*- Trigger Attributes -*/
#define IVIDCPWR_ATTR_TRIGGER_SOURCE            (IVI_CLASS_PUBLIC_ATTR_BASE + 101L)    /* ViInt32,   multi-channel */
#define IVIDCPWR_ATTR_TRIGGERED_CURRENT_LIMIT   (IVI_CLASS_PUBLIC_ATTR_BASE + 102L)    /* ViReal64,  multi-channel */
#define IVIDCPWR_ATTR_TRIGGERED_VOLTAGE_LEVEL   (IVI_CLASS_PUBLIC_ATTR_BASE + 103L)    /* ViReal64,  multi-channel */

/****************************************************************************
 *----------------- IviDCPwr Class Attribute Value Defines -----------------*
 ****************************************************************************/

    /*- Defined values for attribute IVIDCPWR_ATTR_CURRENT_LIMIT_BEHAVIOR -*/
#define IVIDCPWR_VAL_CURRENT_REGULATE                           (0L)
#define IVIDCPWR_VAL_CURRENT_TRIP                               (1L)

#define IVIDCPWR_VAL_CURRENT_LIMIT_BEHAVIOR_CLASS_EXT_BASE      (500L)
#define IVIDCPWR_VAL_CURRENT_LIMIT_BEHAVIOR_SPECIFIC_EXT_BASE   (1000L)

    /*- Defined values for attribute IVIDCPWR_ATTR_TRIGGER_SOURCE -*/
#define IVIDCPWR_VAL_TRIG_IMMEDIATE                         (0L)
#define IVIDCPWR_VAL_TRIG_EXTERNAL                          (1L)
#define IVIDCPWR_VAL_SOFTWARE_TRIG                          (2L)
#define IVIDCPWR_VAL_TRIG_TTL0                              (3L)
#define IVIDCPWR_VAL_TRIG_TTL1                              (4L)
#define IVIDCPWR_VAL_TRIG_TTL2                              (5L)
#define IVIDCPWR_VAL_TRIG_TTL3                              (6L)
#define IVIDCPWR_VAL_TRIG_TTL4                              (7L)
#define IVIDCPWR_VAL_TRIG_TTL5                              (8L)
#define IVIDCPWR_VAL_TRIG_TTL6                              (9L)
#define IVIDCPWR_VAL_TRIG_TTL7                              (10L)
#define IVIDCPWR_VAL_TRIG_ECL0                              (11L)
#define IVIDCPWR_VAL_TRIG_ECL1                              (12L)
#define IVIDCPWR_VAL_TRIG_PXI_STAR                          (13L)
#define IVIDCPWR_VAL_TRIG_RTSI_0                            (14L)
#define IVIDCPWR_VAL_TRIG_RTSI_1                            (15L)
#define IVIDCPWR_VAL_TRIG_RTSI_2                            (16L)
#define IVIDCPWR_VAL_TRIG_RTSI_3                            (17L)
#define IVIDCPWR_VAL_TRIG_RTSI_4                            (18L)
#define IVIDCPWR_VAL_TRIG_RTSI_5                            (19L)
#define IVIDCPWR_VAL_TRIG_RTSI_6                            (20L)

#define IVIDCPWR_VAL_TRIG_SRC_CLASS_EXT_BASE                (500L)
#define IVIDCPWR_VAL_TRIG_SRC_SPECIFIC_EXT_BASE             (1000L)

/****************************************************************************
 *--------- IviDCPwr Class Instrument Driver Function Declarations ---------*
 ****************************************************************************/
    /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviDCPwr_init (ViRsrc logicalName, 
                                 ViBoolean idQuery, 
                                 ViBoolean resetDevice, 
                                 ViSession *vi);

ViStatus _VI_FUNC IviDCPwr_close (ViSession vi);

ViStatus _VI_FUNC IviDCPwr_reset (ViSession vi);

ViStatus _VI_FUNC IviDCPwr_self_test (ViSession vi, 
                                      ViInt16 *selfTestResult, 
                                      ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviDCPwr_error_query (ViSession vi, 
                                        ViInt32 *errorCode, 
                                        ViChar errorMessage[]);

ViStatus _VI_FUNC IviDCPwr_error_message (ViSession vi, 
                                          ViStatus statusCode, 
                                          ViChar message[]);

ViStatus _VI_FUNC IviDCPwr_revision_query (ViSession vi, 
                                           ViChar driverRev[], 
                                           ViChar instrRev[]);

    /*- Utility Functions -*/
ViStatus _VI_FUNC IviDCPwr_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviDCPwr_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviDCPwr_Disable (ViSession vi);


    /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviDCPwr_InitWithOptions (ViRsrc logicalName, 
                                            ViBoolean IDQuery,
                                            ViBoolean resetDevice, 
                                            ViConstString optionString, 
                                            ViSession *vi);

    /*- Set, Get, and Check Attribute Functions -*/

ViStatus _VI_FUNC IviDCPwr_GetAttributeViInt32 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt32 *value);

ViStatus _VI_FUNC IviDCPwr_SetAttributeViInt32 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt32 value);

ViStatus _VI_FUNC IviDCPwr_CheckAttributeViInt32 (ViSession vi, 
                                                  ViConstString channelName,
                                                  ViAttr attributeId,
                                                  ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviDCPwr_GetAttributeViInt64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt64 *value);

ViStatus _VI_FUNC IviDCPwr_SetAttributeViInt64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt64 value);

ViStatus _VI_FUNC IviDCPwr_CheckAttributeViInt64 (ViSession vi, 
                                                  ViConstString channelName,
                                                  ViAttr attributeId,
                                                  ViInt64 value);
#endif

ViStatus _VI_FUNC IviDCPwr_GetAttributeViReal64 (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 *value);

ViStatus _VI_FUNC IviDCPwr_SetAttributeViReal64 (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 value);

ViStatus _VI_FUNC IviDCPwr_CheckAttributeViReal64 (ViSession vi, 
                                                   ViConstString channelName, 
                                                   ViAttr attributeId, 
                                                   ViReal64 value);

ViStatus _VI_FUNC IviDCPwr_GetAttributeViString (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViInt32 bufferSize, 
                                                 ViChar value[]);

ViStatus _VI_FUNC IviDCPwr_SetAttributeViString (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViConstString value);

ViStatus _VI_FUNC IviDCPwr_CheckAttributeViString (ViSession vi, 
                                                   ViConstString channelName, 
                                                   ViAttr attributeId, 
                                                   ViConstString value); 

ViStatus _VI_FUNC IviDCPwr_GetAttributeViBoolean (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean *value);

ViStatus _VI_FUNC IviDCPwr_SetAttributeViBoolean (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean value);

ViStatus _VI_FUNC IviDCPwr_CheckAttributeViBoolean (ViSession vi, 
                                                    ViConstString channelName, 
                                                    ViAttr attributeId, 
                                                    ViBoolean value);

ViStatus _VI_FUNC IviDCPwr_GetAttributeViSession (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViSession *value);

ViStatus _VI_FUNC IviDCPwr_SetAttributeViSession (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViSession value);

ViStatus _VI_FUNC IviDCPwr_CheckAttributeViSession (ViSession vi, 
                                                    ViConstString channelName, 
                                                    ViAttr attributeId, 
                                                    ViSession value);

    /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviDCPwr_LockSession (ViSession vi, 
                                        ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviDCPwr_UnlockSession (ViSession vi, 
                                          ViBoolean *callerHasLock);

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviDCPwr_GetError (ViSession vi, 
                                     ViStatus *errorCode, 
                                     ViInt32 bufferSize, 
                                     ViChar description[]);

ViStatus _VI_FUNC IviDCPwr_ClearError (ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviDCPwr_GetNextInterchangeWarning (ViSession vi, 
                                                      ViInt32 bufferSize,
                                                      ViChar warning[]);

ViStatus _VI_FUNC IviDCPwr_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviDCPwr_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviDCPwr_GetNextCoercionRecord (ViSession vi,
                                                  ViInt32 bufferSize, 
                                                  ViChar record[]);

ViStatus _VI_FUNC IviDCPwr_GetSpecificDriverCHandle (ViSession vi,
                                                     ViSession* specificDriverCHandle);

ViStatus _VI_FUNC IviDCPwr_GetSpecificDriverIUnknownPtr (ViSession vi,
                                                       void* specificDriverIUnknownPtr);

    /*- IviDCPwrBase Functions -*/
ViStatus _VI_FUNC IviDCPwr_ConfigureOutputEnabled (ViSession vi,
                                                   ViConstString channelName,
                                                   ViBoolean enabled);

ViStatus _VI_FUNC IviDCPwr_ConfigureOutputRange (ViSession vi,
                                                 ViConstString channelName,
                                                 ViInt32 rangeType,
                                                 ViReal64 range);

ViStatus _VI_FUNC IviDCPwr_ConfigureCurrentLimit (ViSession vi,
                                                  ViConstString channelName,
                                                  ViInt32 behavior,
                                                  ViReal64 limit);

ViStatus _VI_FUNC IviDCPwr_ConfigureOVP (ViSession vi,
                                         ViConstString channelName,
                                         ViBoolean enabled,
                                         ViReal64 limit);

ViStatus _VI_FUNC IviDCPwr_ConfigureVoltageLevel (ViSession vi,
                                                  ViConstString channelName,
                                                  ViReal64 level);

ViStatus _VI_FUNC IviDCPwr_GetChannelName (ViSession vi,
                                           ViInt32 index,
                                           ViInt32 bufferSize,
                                           ViChar name[]);

ViStatus _VI_FUNC IviDCPwr_QueryOutputState (ViSession vi,
                                             ViConstString channelName,
                                             ViInt32 outputState,
                                             ViBoolean* inState);

ViStatus _VI_FUNC IviDCPwr_QueryMaxCurrentLimit (ViSession vi,
                                                 ViConstString channelName,
                                                 ViReal64 voltageLevel,
                                                 ViReal64* maxCurrentLimit);

ViStatus _VI_FUNC IviDCPwr_QueryMaxVoltageLevel (ViSession vi,
                                                 ViConstString channelName,
                                                 ViReal64 currentLimit,
                                                 ViReal64* maxVoltageLevel);

ViStatus _VI_FUNC IviDCPwr_ResetOutputProtection (ViSession vi,
                                                  ViConstString channelName);

    /*- IviDcPwrTrigger Functions -*/
ViStatus _VI_FUNC IviDCPwr_ConfigureTriggerSource (ViSession vi,
                                                   ViConstString channelName,
                                                   ViInt32 source);

ViStatus _VI_FUNC IviDCPwr_ConfigureTriggeredVoltageLevel (ViSession vi,
                                                           ViConstString channelName,
                                                           ViReal64 level);

ViStatus _VI_FUNC IviDCPwr_ConfigureTriggeredCurrentLimit (ViSession vi,
                                                           ViConstString channelName,
                                                           ViReal64 limit);

ViStatus _VI_FUNC IviDCPwr_Abort (ViSession vi);

ViStatus _VI_FUNC IviDCPwr_Initiate (ViSession vi);

    /*- IviDCPwrSoftwareTrigger Functions -*/
ViStatus _VI_FUNC IviDCPwr_SendSoftwareTrigger (ViSession vi);

    /*- IviDCPwrMeasure Functions -*/
ViStatus _VI_FUNC IviDCPwr_Measure (ViSession vi,
                                    ViConstString channelName,
                                    ViInt32 measurementType,
                                    ViReal64* measurement);

/****************************************************************************
 *--------------- IviDCPwr Class Error And Completion Codes ----------------*
 ****************************************************************************/
#define IVIDCPWR_ERROR_TRIGGER_NOT_SOFTWARE   (IVI_CROSS_CLASS_ERROR_BASE + 1L)

#define IVIDCPWR_ERRMSG_TRIGGER_NOT_SOFTWARE  "The trigger source is not set to software trigger."

#define IVIDCPWR_ERROR_CODES_AND_MSGS \
        {IVIDCPWR_ERROR_TRIGGER_NOT_SOFTWARE, IVIDCPWR_ERRMSG_TRIGGER_NOT_SOFTWARE}

/*- IviDCPwrObsolete.h included for backwards compatibility -*/
#include "IviDCPwrObsolete.h"

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

#endif /* IVIDCPWR_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviDCPwrObsolete.h sha256=f7c8d2173bad20ca9565293298bca2d89d5791cf08876ccb516125ebd524cb2e bytes=3462 -->
## FILE: imports/include/IviDCPwrObsolete.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviDCPwrObsolete.h`
- sha256: `f7c8d2173bad20ca9565293298bca2d89d5791cf08876ccb516125ebd524cb2e`
- bytes: 3462

````c
/*****************************************************************************
 *                          I V I - D C P W R  2.0                           
 *----------------------------------------------------------------------------
 *    Copyright (c) 2002-2020 National Instruments.  All Rights Reserved.         
 *----------------------------------------------------------------------------
 *                                                                           
 * Title:       IviDCPwrObsolete.h                                           
 * Purpose:     IviDCPwr Class value and attribute Id declarations for the   
 *              now obsolete IviDCPwr 2.0 specification.                      
 *              These macros are defined to keep backward compatibility with 
 *              previous versions of this file.  DC Power Supply specific       
 *              drivers should no longer use these macros. Instead, the      
 *              drivers must use definitions from the current IviDCPwr.h     
 *              header file.                                                 
 *****************************************************************************/

#ifndef IVIDCPWR_HEADER_OBSOLETE
#define IVIDCPWR_HEADER_OBSOLETE
#include <ivi.h>

    /*- Obsolete Inherent Attributes -*/
#define IVIDCPWR_ATTR_CLASS_DRIVER_MAJOR_VERSION        IVI_ATTR_CLASS_DRIVER_MAJOR_VERSION     /* ViInt32,  read-only */
#define IVIDCPWR_ATTR_CLASS_DRIVER_MINOR_VERSION        IVI_ATTR_CLASS_DRIVER_MINOR_VERSION     /* ViInt32,  read-only */

#define IVIDCPWR_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION     IVI_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIDCPWR_ATTR_SPECIFIC_DRIVER_MINOR_VERSION     IVI_ATTR_SPECIFIC_DRIVER_MINOR_VERSION  /* ViInt32,  read-only */
#define IVIDCPWR_ATTR_QUERY_INSTR_STATUS                IVI_ATTR_QUERY_INSTR_STATUS             /* ViBoolean */
#define IVIDCPWR_ATTR_RESOURCE_DESCRIPTOR               IVI_ATTR_RESOURCE_DESCRIPTOR            /* ViString, read-only */
#define IVIDCPWR_ATTR_NUM_CHANNELS                      IVI_ATTR_NUM_CHANNELS

#define IVIDCPWR_ATTR_IO_SESSION_TYPE                   IVI_ATTR_IO_SESSION_TYPE
#define IVIDCPWR_ATTR_IO_SESSION                        IVI_ATTR_IO_SESSION

#define IVIDCPWR_ATTR_ATTRIBUTE_CAPABILITIES            IVI_ATTR_ATTRIBUTE_CAPABILITIES        /* ViString, read-only */

    /*- Error Info -*/
#define IVIDCPWR_ATTR_PRIMARY_ERROR                     IVI_ATTR_PRIMARY_ERROR                  /* ViInt32  */
#define IVIDCPWR_ATTR_SECONDARY_ERROR                   IVI_ATTR_SECONDARY_ERROR                /* ViInt32  */
#define IVIDCPWR_ATTR_ERROR_ELABORATION                 IVI_ATTR_ERROR_ELABORATION              /* ViString */

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviDCPwr_GetErrorInfo (ViSession vi, 
                                         ViStatus *primaryError, 
                                         ViStatus *secondaryError, 
                                         ViChar errorElaboration[IVI_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC IviDCPwr_ClearErrorInfo (ViSession vi);

/*****************************************************************************
 *---------------------------- End Include File -----------------------------*
 *****************************************************************************/

#endif /* IVIDCPWR_HEADER_OBSOLETE */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviDigitizer_ni.h sha256=965b6933cdef5085a115905282bb6dc662bf3ecca016cba0daf64320cda67a42 bytes=49010 -->
## FILE: imports/include/IviDigitizer_ni.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviDigitizer_ni.h`
- sha256: `965b6933cdef5085a115905282bb6dc662bf3ecca016cba0daf64320cda67a42`
- bytes: 49010

````c
/****************************************************************************
*                         IVIDIGITIZER                              
*---------------------------------------------------------------------------
*    Copyright (c) 2009-2020 National Instruments.  All Rights Reserved.        
*---------------------------------------------------------------------------
*                                                                          
* Title:       IviDigitizer_ni.h                                                    
* Purpose:     IviDigitizer Class declarations for the Base and Extended  
*              IviDigitizer Capabilities.                                        
****************************************************************************/


#ifndef IVIDIGITIZER_HEADER
#define IVIDIGITIZER_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif


/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVIDIGITIZER_MAJOR_VERSION              (4L)
#define IVIDIGITIZER_MINOR_VERSION              (1L)

#define IVIDIGITIZER_CLASS_SPEC_MAJOR_VERSION   (2L)
#define IVIDIGITIZER_CLASS_SPEC_MINOR_VERSION   (3L)

#define IVIDIGITIZER_DRIVER_VENDOR              "National Instruments"
#ifdef	_IVI_mswin64_
#define IVIDIGITIZER_DRIVER_DESCRIPTION         "IviDigitizer Class Driver [Compiled for 64-bit.]"
#else
#define IVIDIGITIZER_DRIVER_DESCRIPTION			"IviDigitizer Class Driver"
#endif

/****************************************************************************
 *------------------------------ Useful Macros -----------------------------*
 ****************************************************************************/


/****************************************************************************
 *------------------ IviDigitizer Class Attribute Defines ------------------*
 ****************************************************************************/

/*- IVI Inherent Attributes -*/

	/*- User Options -*/
#define IVIDIGITIZER_ATTR_CACHE										IVI_ATTR_CACHE										/* ViBoolean */
#define IVIDIGITIZER_ATTR_RANGE_CHECK								IVI_ATTR_RANGE_CHECK								/* ViBoolean */
#define IVIDIGITIZER_ATTR_QUERY_INSTRUMENT_STATUS					IVI_ATTR_QUERY_INSTRUMENT_STATUS					/* ViBoolean */
#define IVIDIGITIZER_ATTR_RECORD_COERCIONS							IVI_ATTR_RECORD_COERCIONS							/* ViBoolean */
#define IVIDIGITIZER_ATTR_SIMULATE									IVI_ATTR_SIMULATE									/* ViBoolean */
#define IVIDIGITIZER_ATTR_INTERCHANGE_CHECK							IVI_ATTR_INTERCHANGE_CHECK							/* ViBoolean */
#define IVIDIGITIZER_ATTR_SPY										IVI_ATTR_SPY										/* ViBoolean */
#define IVIDIGITIZER_ATTR_USE_SPECIFIC_SIMULATION					IVI_ATTR_USE_SPECIFIC_SIMULATION					/* ViBoolean */

	/* Instrument Capabilities */
#define IVIDIGITIZER_ATTR_CHANNEL_COUNT								IVI_ATTR_CHANNEL_COUNT								/* ViInt32,  read-only  */

	/*- Instrument Capabilities -*/
#define IVIDIGITIZER_ATTR_GROUP_CAPABILITIES						IVI_ATTR_GROUP_CAPABILITIES							/* ViString, read-only */
#define IVIDIGITIZER_ATTR_FUNCTION_CAPABILITIES						IVI_ATTR_FUNCTION_CAPABILITIES						/* ViString, read-only */

	/*- Class Driver Information -*/    
#define IVIDIGITIZER_ATTR_CLASS_DRIVER_PREFIX						IVI_ATTR_CLASS_DRIVER_PREFIX						/* ViString, read-only */
#define IVIDIGITIZER_ATTR_CLASS_DRIVER_VENDOR						IVI_ATTR_CLASS_DRIVER_VENDOR						/* ViString, read-only */
#define IVIDIGITIZER_ATTR_CLASS_DRIVER_DESCRIPTION					IVI_ATTR_CLASS_DRIVER_DESCRIPTION					/* ViString, read-only */
#define IVIDIGITIZER_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION		IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION		/* ViInt32,  read-only */
#define IVIDIGITIZER_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION		IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION		/* ViInt32,  read-only */

	/*- Specific Driver Information -*/    
#define IVIDIGITIZER_ATTR_SPECIFIC_DRIVER_PREFIX					IVI_ATTR_SPECIFIC_DRIVER_PREFIX						/* ViString, read-only */
#define IVIDIGITIZER_ATTR_SPECIFIC_DRIVER_LOCATOR					IVI_ATTR_SPECIFIC_DRIVER_LOCATOR					/* ViString, read-only */
#define IVIDIGITIZER_ATTR_IO_RESOURCE_DESCRIPTOR					IVI_ATTR_IO_RESOURCE_DESCRIPTOR						/* ViString, read-only */
#define IVIDIGITIZER_ATTR_LOGICAL_NAME								IVI_ATTR_LOGICAL_NAME								/* ViString, read-only */
#define IVIDIGITIZER_ATTR_SPECIFIC_DRIVER_VENDOR					IVI_ATTR_SPECIFIC_DRIVER_VENDOR						/* ViString, read-only */
#define IVIDIGITIZER_ATTR_SPECIFIC_DRIVER_DESCRIPTION				IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION				/* ViString, read-only */
#define IVIDIGITIZER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION	IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION	/* ViInt32,  read-only */
#define IVIDIGITIZER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION	IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION	/* ViInt32,  read-only */

	/*- Instrument Information -*/    
#define IVIDIGITIZER_ATTR_INSTRUMENT_FIRMWARE_REVISION				IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION				/* ViString, read-only */
#define IVIDIGITIZER_ATTR_INSTRUMENT_MANUFACTURER					IVI_ATTR_INSTRUMENT_MANUFACTURER					/* ViString, read-only */
#define IVIDIGITIZER_ATTR_INSTRUMENT_MODEL							IVI_ATTR_INSTRUMENT_MODEL							/* ViString, read-only */
#define IVIDIGITIZER_ATTR_SUPPORTED_INSTRUMENT_MODELS				IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS				/* ViString, read-only */

	/*- Version Information -*/
#define IVIDIGITIZER_ATTR_CLASS_DRIVER_REVISION						IVI_ATTR_CLASS_DRIVER_REVISION						/* ViString, read-only */

#define IVIDIGITIZER_ATTR_SPECIFIC_DRIVER_REVISION					IVI_ATTR_SPECIFIC_DRIVER_REVISION					/* ViString, read-only */

	/*- Driver Setup information -*/
#define IVIDIGITIZER_ATTR_DRIVER_SETUP								IVI_ATTR_DRIVER_SETUP								/* ViString */

/*- IviDigitizer Fundamental Attributes -*/
#define IVIDIGITIZER_ATTR_ACTIVE_TRIGGER_SOURCE						(IVI_CLASS_PUBLIC_ATTR_BASE + 1L)		/* ViString */
#define IVIDIGITIZER_ATTR_CHANNEL_ENABLED							(IVI_CLASS_PUBLIC_ATTR_BASE + 2L)		/* ViBoolean */
#define IVIDIGITIZER_ATTR_INPUT_CONNECTOR_SELECTION					(IVI_CLASS_PUBLIC_ATTR_BASE + 3L)		/* ViInt32 */
#define IVIDIGITIZER_ATTR_INPUT_IMPEDANCE							(IVI_CLASS_PUBLIC_ATTR_BASE + 4L)		/* ViReal64 */
#define IVIDIGITIZER_ATTR_IS_IDLE									(IVI_CLASS_PUBLIC_ATTR_BASE + 5L)		/* ViInt32, read-only */
#define IVIDIGITIZER_ATTR_IS_MEASURING								(IVI_CLASS_PUBLIC_ATTR_BASE + 6L)		/* ViInt32, read-only */
#define IVIDIGITIZER_ATTR_IS_WAITING_FOR_ARM						(IVI_CLASS_PUBLIC_ATTR_BASE + 7L)		/* ViInt32, read-only */
#define IVIDIGITIZER_ATTR_IS_WAITING_FOR_TRIGGER					(IVI_CLASS_PUBLIC_ATTR_BASE + 8L)		/* ViInt32, read-only */
#define IVIDIGITIZER_ATTR_MAX_FIRST_VALID_POINT_VAL					(IVI_CLASS_PUBLIC_ATTR_BASE + 9L)		/* ViInt64, read-only */
#define IVIDIGITIZER_ATTR_MAX_SAMPLES_PER_CHANNEL					(IVI_CLASS_PUBLIC_ATTR_BASE + 10L)		/* ViInt64, read-only */
#define IVIDIGITIZER_ATTR_MIN_RECORD_SIZE							(IVI_CLASS_PUBLIC_ATTR_BASE + 11L)		/* ViInt64, read-only */
#define IVIDIGITIZER_ATTR_NUM_ACQUIRED_RECORDS						(IVI_CLASS_PUBLIC_ATTR_BASE + 12L)		/* ViInt64, read-only */
#define IVIDIGITIZER_ATTR_NUM_RECORDS_TO_ACQUIRE					(IVI_CLASS_PUBLIC_ATTR_BASE + 13L)		/* ViInt64 */
#define IVIDIGITIZER_ATTR_RECORD_SIZE								(IVI_CLASS_PUBLIC_ATTR_BASE + 14L)		/* ViInt64 */
#define IVIDIGITIZER_ATTR_SAMPLE_RATE								(IVI_CLASS_PUBLIC_ATTR_BASE + 15L)		/* ViReal64 */
#define IVIDIGITIZER_ATTR_TRIGGER_COUPLING							(IVI_CLASS_PUBLIC_ATTR_BASE + 16L)		/* ViInt32 */
#define IVIDIGITIZER_ATTR_TRIGGER_DELAY								(IVI_CLASS_PUBLIC_ATTR_BASE + 17L)		/* ViReal64 */
#define IVIDIGITIZER_ATTR_TRIGGER_HYSTERESIS						(IVI_CLASS_PUBLIC_ATTR_BASE + 18L)		/* ViReal64 */
#define IVIDIGITIZER_ATTR_TRIGGER_LEVEL								(IVI_CLASS_PUBLIC_ATTR_BASE + 19L)		/* ViReal64 */
#define IVIDIGITIZER_ATTR_TRIGGER_OUTPUT_ENABLED					(IVI_CLASS_PUBLIC_ATTR_BASE + 20L)		/* ViBoolean */
#define IVIDIGITIZER_ATTR_TRIGGER_SLOPE								(IVI_CLASS_PUBLIC_ATTR_BASE + 21L)		/* ViInt32 */
#define IVIDIGITIZER_ATTR_TRIGGER_SOURCE_COUNT						(IVI_CLASS_PUBLIC_ATTR_BASE + 22L)		/* ViInt32, read-only */
#define IVIDIGITIZER_ATTR_TRIGGER_TYPE								(IVI_CLASS_PUBLIC_ATTR_BASE + 23L)		/* ViInt32 */
#define IVIDIGITIZER_ATTR_VERTICAL_COUPLING							(IVI_CLASS_PUBLIC_ATTR_BASE + 24L)		/* ViInt32 */
#define IVIDIGITIZER_ATTR_VERTICAL_OFFSET							(IVI_CLASS_PUBLIC_ATTR_BASE + 25L)		/* ViReal64 */
#define IVIDIGITIZER_ATTR_VERTICAL_RANGE							(IVI_CLASS_PUBLIC_ATTR_BASE + 26L)		/* ViReal64 */

/*- IviDigitizerBoardTemperature Extension Group -*/
#define IVIDIGITIZER_ATTR_BOARD_TEMPERATURE							(IVI_CLASS_PUBLIC_ATTR_BASE + 100L)		/* ViReal64, read-only */
#define IVIDIGITIZER_ATTR_TEMPERATURE_UNITS							(IVI_CLASS_PUBLIC_ATTR_BASE + 101L)		/* ViInt32 */

/*- IviDigitizerChannelFilter Extension Group -*/
#define IVIDIGITIZER_ATTR_INPUT_FILTER_BYPASS						(IVI_CLASS_PUBLIC_ATTR_BASE + 200L)		/* ViBoolean */
#define IVIDIGITIZER_ATTR_INPUT_FILTER_MAX_FREQUENCY				(IVI_CLASS_PUBLIC_ATTR_BASE + 201L)		/* ViReal64 */
#define IVIDIGITIZER_ATTR_INPUT_FILTER_MIN_FREQUENCY				(IVI_CLASS_PUBLIC_ATTR_BASE + 202L)		/* ViReal64 */

/*- IviDigitizerChannelTemperature Extension Group -*/
#define IVIDIGITIZER_ATTR_CHANNEL_TEMPERATURE						(IVI_CLASS_PUBLIC_ATTR_BASE + 300L)		/* ViReal64, read-only */

/*- IviDigitizerTimeInterleavedChannels Extension Group -*/
#define IVIDIGITIZER_ATTR_TIME_INTERLEAVED_CHANNEL_LIST				(IVI_CLASS_PUBLIC_ATTR_BASE + 400L)		/* ViString */
#define IVIDIGITIZER_ATTR_TIME_INTERLEAVED_CHANNEL_LIST_AUTO		(IVI_CLASS_PUBLIC_ATTR_BASE + 401L)		/* ViBoolean */

/*- IviDigitizerDataInterleavedChannels Extension Group -*/
#define IVIDIGITIZER_ATTR_DATA_INTERLEAVED_CHANNEL_LIST				(IVI_CLASS_PUBLIC_ATTR_BASE + 500L)		/* ViString */

/*- IviDigitizerReferenceOscillator Extension Group -*/
#define IVIDIGITIZER_ATTR_REFERENCE_OSCILLATOR_EXTERNAL_FREQUENCY	(IVI_CLASS_PUBLIC_ATTR_BASE + 600L)		/* ViReal64 */
#define IVIDIGITIZER_ATTR_REFERENCE_OSCILLATOR_OUTPUT_ENABLED		(IVI_CLASS_PUBLIC_ATTR_BASE + 601L)		/* ViBoolean */
#define IVIDIGITIZER_ATTR_REFERENCE_OSCILLATOR_SOURCE				(IVI_CLASS_PUBLIC_ATTR_BASE + 602L)		/* ViInt32 */

/*- IviDigitizerSampleClock Extension Group -*/
#define IVIDIGITIZER_ATTR_SAMPLE_CLOCK_EXTERNAL_DIVIDER				(IVI_CLASS_PUBLIC_ATTR_BASE + 700L)		/* ViReal64 */
#define IVIDIGITIZER_ATTR_SAMPLE_CLOCK_EXTERNAL_FREQUENCY			(IVI_CLASS_PUBLIC_ATTR_BASE + 701L)		/* ViReal64 */
#define IVIDIGITIZER_ATTR_SAMPLE_CLOCK_OUTPUT_ENABLED				(IVI_CLASS_PUBLIC_ATTR_BASE + 702L)		/* ViBoolean */
#define IVIDIGITIZER_ATTR_SAMPLE_CLOCK_SOURCE						(IVI_CLASS_PUBLIC_ATTR_BASE + 703L)		/* ViInt32 */

/*- IviDigitizerSampleMode Extension Group -*/
#define IVIDIGITIZER_ATTR_SAMPLE_MODE								(IVI_CLASS_PUBLIC_ATTR_BASE + 800L)		/* ViInt32 */

/*- IviDigitizerDownconversion Extension Group -*/
#define IVIDIGITIZER_ATTR_DOWNCONVERSION_ENABLED					(IVI_CLASS_PUBLIC_ATTR_BASE + 900L)		/* ViBoolean */
#define IVIDIGITIZER_ATTR_DOWNCONVERSION_CENTER_FREQUENCY			(IVI_CLASS_PUBLIC_ATTR_BASE + 901L)		/* ViReal64 */
#define IVIDIGITIZER_ATTR_DOWNCONVERSION_IQ_INTERLEAVED				(IVI_CLASS_PUBLIC_ATTR_BASE + 902L)		/* ViBoolean */

/*- IviDigitizerArm Extension Group -*/
#define IVIDIGITIZER_ATTR_ACTIVE_ARM_SOURCE							(IVI_CLASS_PUBLIC_ATTR_BASE + 1000L)	/* ViString */
#define IVIDIGITIZER_ATTR_ARM_COUNT									(IVI_CLASS_PUBLIC_ATTR_BASE + 1001L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_ARM_COUPLING								(IVI_CLASS_PUBLIC_ATTR_BASE + 1002L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_ARM_DELAY									(IVI_CLASS_PUBLIC_ATTR_BASE + 1003L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_ARM_HYSTERESIS							(IVI_CLASS_PUBLIC_ATTR_BASE + 1004L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_ARM_LEVEL									(IVI_CLASS_PUBLIC_ATTR_BASE + 1005L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_ARM_OUTPUT_ENABLED						(IVI_CLASS_PUBLIC_ATTR_BASE + 1006L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_ARM_SLOPE									(IVI_CLASS_PUBLIC_ATTR_BASE + 1007L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_ARM_SOURCE_COUNT							(IVI_CLASS_PUBLIC_ATTR_BASE + 1008L)	/* ViInt32, read-only */
#define IVIDIGITIZER_ATTR_ARM_TYPE									(IVI_CLASS_PUBLIC_ATTR_BASE + 1009L)	/* ViInt32 */

/*- IviDigitizerMultiArm Extension Group -*/
#define IVIDIGITIZER_ATTR_ARM_SOURCE_LIST							(IVI_CLASS_PUBLIC_ATTR_BASE + 1100L)	/* ViString */
#define IVIDIGITIZER_ATTR_ARM_SOURCE_OPERATOR						(IVI_CLASS_PUBLIC_ATTR_BASE + 1101L)	/* ViInt32 */

/*- IviDigitizerGlitchArm Extension Group -*/
#define IVIDIGITIZER_ATTR_GLITCH_ARM_CONDITION						(IVI_CLASS_PUBLIC_ATTR_BASE + 1200L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_GLITCH_ARM_POLARITY						(IVI_CLASS_PUBLIC_ATTR_BASE + 1201L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_GLITCH_ARM_WIDTH							(IVI_CLASS_PUBLIC_ATTR_BASE + 1202L)	/* ViReal64 */

/*- IviDigitizerRuntArm Extension Group -*/
#define IVIDIGITIZER_ATTR_RUNT_ARM_HIGH_THRESHOLD					(IVI_CLASS_PUBLIC_ATTR_BASE + 1300L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_RUNT_ARM_LOW_THRESHOLD					(IVI_CLASS_PUBLIC_ATTR_BASE + 1301L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_RUNT_ARM_POLARITY							(IVI_CLASS_PUBLIC_ATTR_BASE + 1302L)	/* ViInt32 */

/*- IviDigitizerTVArm Extension -*/
#define IVIDIGITIZER_ATTR_TV_ARM_EVENT								(IVI_CLASS_PUBLIC_ATTR_BASE + 1400L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_TV_ARM_LINE_NUMBER						(IVI_CLASS_PUBLIC_ATTR_BASE + 1401L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_TV_ARM_POLARITY							(IVI_CLASS_PUBLIC_ATTR_BASE + 1402L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_TV_ARM_SIGNAL_FORMAT						(IVI_CLASS_PUBLIC_ATTR_BASE + 1403L)	/* ViInt32 */

/*- IviDigitizerWidthArm Extension Group -*/
#define IVIDIGITIZER_ATTR_WIDTH_ARM_CONDITION						(IVI_CLASS_PUBLIC_ATTR_BASE + 1500L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_WIDTH_ARM_HIGH_THRESHOLD					(IVI_CLASS_PUBLIC_ATTR_BASE + 1501L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_WIDTH_ARM_LOW_THRESHOLD					(IVI_CLASS_PUBLIC_ATTR_BASE + 1502L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_WIDTH_ARM_POLARITY						(IVI_CLASS_PUBLIC_ATTR_BASE + 1503L)	/* ViInt32 */

/*- IviDigitizerWindowArm Extension Group -*/
#define IVIDIGITIZER_ATTR_WINDOW_ARM_CONDITION						(IVI_CLASS_PUBLIC_ATTR_BASE + 1600L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_WINDOW_ARM_HIGH_THRESHOLD					(IVI_CLASS_PUBLIC_ATTR_BASE + 1601L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_WINDOW_ARM_LOW_THRESHOLD					(IVI_CLASS_PUBLIC_ATTR_BASE + 1602L)	/* ViReal64 */

/*- IviDigitizerTriggerModifier Extension Group -*/
#define IVIDIGITIZER_ATTR_TRIGGER_MODIFIER							(IVI_CLASS_PUBLIC_ATTR_BASE + 1700L)	/* ViInt32 */

/*- IviDigitizerMultiTrigger Extension Group -*/
#define IVIDIGITIZER_ATTR_TRIGGER_SOURCE_LIST						(IVI_CLASS_PUBLIC_ATTR_BASE + 1800L)	/* ViString */
#define IVIDIGITIZER_ATTR_TRIGGER_SOURCE_OPERATOR					(IVI_CLASS_PUBLIC_ATTR_BASE + 1801L)	/* ViInt32 */

/*- IviDigitizerPretriggerSamples Extension Group -*/
#define IVIDIGITIZER_ATTR_PRETRIGGER_SAMPLES						(IVI_CLASS_PUBLIC_ATTR_BASE + 1900L)	/* ViInt64 */

/*- IviDigitizerTriggerHoldoff Extension Group -*/
#define IVIDIGITIZER_ATTR_TRIGGER_HOLDOFF							(IVI_CLASS_PUBLIC_ATTR_BASE + 2000L)	/* ViReal64 */

/*- IIviDigitizerGlitchTrigger Extension Group -*/
#define IVIDIGITIZER_ATTR_GLITCH_TRIGGER_CONDITION					(IVI_CLASS_PUBLIC_ATTR_BASE + 2100L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_GLITCH_TRIGGER_POLARITY					(IVI_CLASS_PUBLIC_ATTR_BASE + 2101L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_GLITCH_TRIGGER_WIDTH						(IVI_CLASS_PUBLIC_ATTR_BASE + 2102L)	/* ViReal64 */

/*- IviDigitizerRuntTrigger Extension Group -*/
#define IVIDIGITIZER_ATTR_RUNT_TRIGGER_HIGH_THRESHOLD				(IVI_CLASS_PUBLIC_ATTR_BASE + 2200L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_RUNT_TRIGGER_LOW_THRESHOLD				(IVI_CLASS_PUBLIC_ATTR_BASE + 2201L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_RUNT_TRIGGER_POLARITY						(IVI_CLASS_PUBLIC_ATTR_BASE + 2202L)	/* ViInt32 */

/*- IviDigitizerTVTrigger Extension Group -*/
#define IVIDIGITIZER_ATTR_TV_TRIGGER_EVENT							(IVI_CLASS_PUBLIC_ATTR_BASE + 2300L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_TV_TRIGGER_LINE_NUMBER					(IVI_CLASS_PUBLIC_ATTR_BASE + 2301L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_TV_TRIGGER_POLARITY						(IVI_CLASS_PUBLIC_ATTR_BASE + 2302L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_TV_TRIGGER_SIGNAL_FORMAT					(IVI_CLASS_PUBLIC_ATTR_BASE + 2303L)	/* ViInt32 */

/*- IviDigitizerWidthTrigger Extension Group -*/
#define IVIDIGITIZER_ATTR_WIDTH_TRIGGER_CONDITION					(IVI_CLASS_PUBLIC_ATTR_BASE + 2400L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_WIDTH_TRIGGER_HIGH_THRESHOLD				(IVI_CLASS_PUBLIC_ATTR_BASE + 2401L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_WIDTH_TRIGGER_LOW_THRESHOLD				(IVI_CLASS_PUBLIC_ATTR_BASE + 2402L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_WIDTH_TRIGGER_POLARITY					(IVI_CLASS_PUBLIC_ATTR_BASE + 2403L)	/* ViInt32 */

/*- IviDigitizerWindowTrigger Extension Group -*/
#define IVIDIGITIZER_ATTR_WINDOW_TRIGGER_CONDITION					(IVI_CLASS_PUBLIC_ATTR_BASE + 2500L)	/* ViInt32 */
#define IVIDIGITIZER_ATTR_WINDOW_TRIGGER_HIGH_THRESHOLD				(IVI_CLASS_PUBLIC_ATTR_BASE + 2501L)	/* ViReal64 */
#define IVIDIGITIZER_ATTR_WINDOW_TRIGGER_LOW_THRESHOLD				(IVI_CLASS_PUBLIC_ATTR_BASE + 2502L)	/* ViReal64 */

/****************************************************************************
 *----------------- IviDigitizer Class Attribute Value Defines -------------*
 ****************************************************************************/
/*- Defined values for attribute IVIDIGITIZER_ATTR_IS_IDLE -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_IS_MEASURING -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_IS_WAITING_FOR_ARM -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_IS_WAITING_FOR_TRIGGER -*/
#define IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_TRUE				(1L)
#define IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_FALSE			(2L)
#define IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_UNKNOWN			(3L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_TRIGGER_COUPLING -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_ARM_COUPLING -*/
#define IVIDIGITIZER_VAL_TRIGGER_COUPLING_AC						(0L)
#define IVIDIGITIZER_VAL_TRIGGER_COUPLING_DC						(1L)
#define IVIDIGITIZER_VAL_TRIGGER_COUPLING_HF_REJECT					(2L)
#define IVIDIGITIZER_VAL_TRIGGER_COUPLING_LF_REJECT					(3L)
#define IVIDIGITIZER_VAL_TRIGGER_COUPLING_NOISE_REJECT				(4L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_TRIGGER_SLOPE -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_ARM_SLOPE -*/
#define IVIDIGITIZER_VAL_TRIGGER_SLOPE_NEGATIVE						(0L)
#define IVIDIGITIZER_VAL_TRIGGER_SLOPE_POSITIVE						(1L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_TRIGGER_TYPE -*/
#define IVIDIGITIZER_VAL_EDGE_TRIGGER								(1L)
#define IVIDIGITIZER_VAL_WIDTH_TRIGGER								(2L)
#define IVIDIGITIZER_VAL_RUNT_TRIGGER								(3L)
#define IVIDIGITIZER_VAL_GLITCH_TRIGGER								(4L)
#define IVIDIGITIZER_VAL_TV_TRIGGER									(5L)
#define IVIDIGITIZER_VAL_WINDOW_TRIGGER								(6L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_ARM_TYPE -*/
#define IVIDIGITIZER_VAL_EDGE_ARM									(1L)
#define IVIDIGITIZER_VAL_WIDTH_ARM									(2L)
#define IVIDIGITIZER_VAL_RUNT_ARM									(3L)
#define IVIDIGITIZER_VAL_GLITCH_ARM									(4L)
#define IVIDIGITIZER_VAL_TV_ARM										(5L)
#define IVIDIGITIZER_VAL_WINDOW_ARM									(6L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_VERTICAL_COUPLING -*/
#define IVIDIGITIZER_VAL_VERTICAL_COUPLING_AC						(0L)
#define IVIDIGITIZER_VAL_VERTICAL_COUPLING_DC						(1L)
#define IVIDIGITIZER_VAL_VERTICAL_COUPLING_GND						(2L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_TEMPERATURE_UNITS -*/
#define IVIDIGITIZER_VAL_CELSIUS									(0L)
#define IVIDIGITIZER_VAL_FAHRENHEIT									(1L)
#define IVIDIGITIZER_VAL_KELVIN										(2L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_REFERENCE_OSCILLATOR_SOURCE -*/
#define IVIDIGITIZER_VAL_REFERENCE_OSCILLATOR_SOURCE_INTERNAL		(0L)
#define IVIDIGITIZER_VAL_REFERENCE_OSCILLATOR_SOURCE_EXTERNAL		(1L)
#define IVIDIGITIZER_VAL_REFERENCE_OSCILLATOR_SOURCE_PXI_CLK10		(2L)
#define IVIDIGITIZER_VAL_REFERENCE_OSCILLATOR_SOURCE_PXIE_CLK100	(3L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_SAMPLE_CLOCK_SOURCE -*/
#define IVIDIGITIZER_VAL_SAMPLE_CLOCK_SOURCE_INTERNAL				(0L)
#define IVIDIGITIZER_VAL_SAMPLE_CLOCK_SOURCE_EXTERNAL				(1L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_SAMPLE_MODE -*/
#define IVIDIGITIZER_VAL_SAMPLE_MODE_REAL_TIME						(0L)
#define IVIDIGITIZER_VAL_SAMPLE_MODE_EQUIVALENT_TIME				(1L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_ARM_SOURCE_OPERATOR -*/
#define IVIDIGITIZER_VAL_ARM_SOURCE_OPERATOR_AND					(0L)
#define IVIDIGITIZER_VAL_ARM_SOURCE_OPERATOR_OR						(1L)
#define IVIDIGITIZER_VAL_ARM_SOURCE_OPERATOR_NONE					(2L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_GLITCH_ARM_CONDITION -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_GLITCH_TRIGGER_CONDITION -*/
#define IVIDIGITIZER_VAL_GLITCH_LESS_THAN							(1L)
#define IVIDIGITIZER_VAL_GLITCH_GREATER_THAN						(2L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_GLITCH_ARM_POLARITY -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_GLITCH_TRIGGER_POLARITY -*/
#define IVIDIGITIZER_VAL_GLITCH_POSITIVE							(1L)
#define IVIDIGITIZER_VAL_GLITCH_NEGATIVE							(2L)
#define IVIDIGITIZER_VAL_GLITCH_EITHER								(3L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_RUNT_ARM_POLARITY -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_RUNT_TRIGGER_POLARITY -*/
#define IVIDIGITIZER_VAL_RUNT_POSITIVE								(1L)
#define IVIDIGITIZER_VAL_RUNT_NEGATIVE								(2L)
#define IVIDIGITIZER_VAL_RUNT_EITHER								(3L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_TV_ARM_EVENT -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_TV_TRIGGER_EVENT -*/
#define IVIDIGITIZER_VAL_TV_EVENT_FIELD1							(1L)
#define IVIDIGITIZER_VAL_TV_EVENT_FIELD2							(2L)
#define IVIDIGITIZER_VAL_TV_EVENT_ANY_FIELD							(3L)
#define IVIDIGITIZER_VAL_TV_EVENT_ANY_LINE							(4L)
#define IVIDIGITIZER_VAL_TV_EVENT_LINE_NUMBER						(5L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_TV_ARM_POLARITY -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_TV_TRIGGER_POLARITY -*/
#define IVIDIGITIZER_VAL_TV_POSITIVE								(1L)
#define IVIDIGITIZER_VAL_TV_NEGATIVE								(2L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_TV_ARM_SIGNAL_FORMAT -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_TV_TRIGGER_SIGNAL_FORMAT -*/
#define IVIDIGITIZER_VAL_NTSC										(1L)
#define IVIDIGITIZER_VAL_PAL										(2L)
#define IVIDIGITIZER_VAL_SECAM										(3L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_WIDTH_ARM_CONDITION -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_WIDTH_TRIGGER_CONDITION -*/
#define IVIDIGITIZER_VAL_WIDTH_WITHIN								(1L)
#define IVIDIGITIZER_VAL_WIDTH_OUTSIDE								(2L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_WIDTH_ARM_POLARITY -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_WIDTH_TRIGGER_POLARITY -*/
#define IVIDIGITIZER_VAL_WIDTH_POSITIVE								(1L)
#define IVIDIGITIZER_VAL_WIDTH_NEGATIVE								(2L)
#define IVIDIGITIZER_VAL_WIDTH_EITHER								(3L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_WINDOW_ARM_CONDITION -*/
/*- Defined values for attribute IVIDIGITIZER_ATTR_WINDOW_TRIGGER_CONDITION -*/
#define IVIDIGITIZER_VAL_WINDOW_CONDITION_ENTERING					(1L)
#define IVIDIGITIZER_VAL_WINDOW_CONDITION_LEAVING					(2L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_TRIGGER_MODIFIER -*/
#define IVIDIGITIZER_VAL_TRIGGER_MODIFIER_NONE						(1L)
#define IVIDIGITIZER_VAL_TRIGGER_MODIFIER_AUTO						(2L)
#define IVIDIGITIZER_VAL_TRIGGER_MODIFIER_AUTO_LEVEL				(3L)

#define IVIDIGITIZER_VAL_TRIGGER_MOD_CLASS_EXT_BASE					(100L)
#define IVIDIGITIZER_VAL_TRIGGER_MOD_SPECIFIC_EXT_BASE				(1000L)

/*- Defined values for attribute IVIDIGITIZER_ATTR_TRIGGER_SOURCE_OPERATOR -*/
#define IVIDIGITIZER_VAL_TRIGGER_SOURCE_OPERATOR_AND				(0L)
#define IVIDIGITIZER_VAL_TRIGGER_SOURCE_OPERATOR_OR					(1L)
#define IVIDIGITIZER_VAL_TRIGGER_SOURCE_OPERATOR_NONE				(2L)

/****************************************************************************
*----------------- IviDigitizer Function Parameter Value Defines -------------*
****************************************************************************/
/*- Defined values for Read Waveform Int16, Read Waveform Int32, Read Waveform Int8, Read Waveform Real64 -*/
#define IVIDIGITIZER_VAL_TIMEOUT_IMMEDIATE                           (0L)
#define IVIDIGITIZER_VAL_TIMEOUT_INFINITE                            (-1L)

/****************************************************************************
 *--------- IviDigitizer Class Instrument Driver Function Declarations -----*
 ****************************************************************************/
/*- Required VXIplug&play Functions -*/
 ViStatus _VI_FUNC IviDigitizer_init (ViRsrc logicalName, 
									ViBoolean idQuery, 
									ViBoolean resetDevice, 
									ViSession *vi);

ViStatus _VI_FUNC IviDigitizer_close (ViSession vi);

ViStatus _VI_FUNC IviDigitizer_reset (ViSession vi);

ViStatus _VI_FUNC IviDigitizer_self_test (ViSession vi, 
									   ViInt16 *selfTestResult, 
									   ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviDigitizer_error_query (ViSession vi, 
										 ViInt32 *errorCode, 
										 ViChar errorMessage[]);

ViStatus _VI_FUNC IviDigitizer_error_message (ViSession vi, 
										   ViStatus statusCode, 
										   ViChar message[]);

ViStatus _VI_FUNC IviDigitizer_revision_query (ViSession vi, 
											ViChar driverRev[], 
											ViChar instrRev[]);

/*- Utility Functions -*/
ViStatus _VI_FUNC IviDigitizer_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviDigitizer_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviDigitizer_Disable (ViSession vi);

/*- Required IVI Functions -*/
ViStatus _VI_FUNC IviDigitizer_InitWithOptions (ViRsrc logicalName, 
											 ViBoolean IDQuery,
											 ViBoolean resetDevice, 
											 ViConstString optionString, 
											 ViSession *vi);

/*- Set, Get, and Check Attribute Functions -*/

ViStatus _VI_FUNC IviDigitizer_GetAttributeViInt32 (ViSession vi, 
												 ViConstString repeatedCapName,
												 ViAttr attributeId,
												 ViInt32 *value);

ViStatus _VI_FUNC IviDigitizer_SetAttributeViInt32 (ViSession vi, 
												 ViConstString repeatedCapName,
												 ViAttr attributeId,
												 ViInt32 value);

ViStatus _VI_FUNC IviDigitizer_CheckAttributeViInt32 (ViSession vi, 
												   ViConstString repeatedCapName,
												   ViAttr attributeId,
												   ViInt32 value);

ViStatus _VI_FUNC IviDigitizer_GetAttributeViInt64 (ViSession vi, 
													ViConstString repeatedCapName,
													ViAttr attributeId,
													ViInt64 *value);

ViStatus _VI_FUNC IviDigitizer_SetAttributeViInt64 (ViSession vi, 
													ViConstString repeatedCapName,
													ViAttr attributeId,
													ViInt64 value);

ViStatus _VI_FUNC IviDigitizer_CheckAttributeViInt64 (ViSession vi, 
													  ViConstString repeatedCapName,
													  ViAttr attributeId,
													  ViInt64 value);

ViStatus _VI_FUNC IviDigitizer_GetAttributeViReal64 (ViSession vi, 
												  ViConstString repeatedCapName, 
												  ViAttr attributeId, 
												  ViReal64 *value);

ViStatus _VI_FUNC IviDigitizer_SetAttributeViReal64 (ViSession vi, 
												  ViConstString repeatedCapName, 
												  ViAttr attributeId, 
												  ViReal64 value);

ViStatus _VI_FUNC IviDigitizer_CheckAttributeViReal64 (ViSession vi, 
													ViConstString repeatedCapName, 
													ViAttr attributeId, 
													ViReal64 value);

ViStatus _VI_FUNC IviDigitizer_GetAttributeViString (ViSession vi, 
												  ViConstString repeatedCapName, 
												  ViAttr attributeId, 
												  ViInt32 bufferSize, 
												  ViChar value[]);

ViStatus _VI_FUNC IviDigitizer_SetAttributeViString (ViSession vi, 
												  ViConstString repeatedCapName, 
												  ViAttr attributeId, 
												  ViConstString value);

ViStatus _VI_FUNC IviDigitizer_CheckAttributeViString (ViSession vi, 
													ViConstString repeatedCapName, 
													ViAttr attributeId, 
													ViConstString value); 

ViStatus _VI_FUNC IviDigitizer_GetAttributeViBoolean (ViSession vi, 
												   ViConstString repeatedCapName, 
												   ViAttr attributeId, 
												   ViBoolean *value);

ViStatus _VI_FUNC IviDigitizer_SetAttributeViBoolean (ViSession vi, 
												   ViConstString repeatedCapName, 
												   ViAttr attributeId, 
												   ViBoolean value);

ViStatus _VI_FUNC IviDigitizer_CheckAttributeViBoolean (ViSession vi, 
													 ViConstString repeatedCapName, 
													 ViAttr attributeId, 
													 ViBoolean value);

ViStatus _VI_FUNC IviDigitizer_GetAttributeViSession (ViSession vi, 
												   ViConstString repeatedCapName, 
												   ViAttr attributeId, 
												   ViSession *value);

ViStatus _VI_FUNC IviDigitizer_SetAttributeViSession (ViSession vi, 
												   ViConstString repeatedCapName, 
												   ViAttr attributeId, 
												   ViSession value);

ViStatus _VI_FUNC IviDigitizer_CheckAttributeViSession (ViSession vi, 
													 ViConstString repeatedCapName, 
													 ViAttr attributeId, 
													 ViSession value);

/*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviDigitizer_LockSession (ViSession vi, 
										 ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviDigitizer_UnlockSession (ViSession vi, 
										   ViBoolean *callerHasLock);

/*- Error Information Functions -*/
ViStatus _VI_FUNC IviDigitizer_GetError (ViSession vi, 
									  ViStatus *errorCode, 
									  ViInt32 bufferSize, 
									  ViChar description[]);

ViStatus _VI_FUNC IviDigitizer_ClearError (ViSession vi);

/*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviDigitizer_GetNextInterchangeWarning (ViSession vi, 
													   ViInt32 bufferSize,
													   ViChar warning[]);

ViStatus _VI_FUNC IviDigitizer_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviDigitizer_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviDigitizer_GetNextCoercionRecord (ViSession vi,
												   ViInt32 bufferSize, 
												   ViChar record[]);

ViStatus _VI_FUNC IviDigitizer_GetSpecificDriverCHandle (ViSession vi,
													  ViSession* specificDriverCHandle);

/*- IviDigitizer Fundamental Capabilities -*/
ViStatus _VI_FUNC IviDigitizer_Abort (ViSession vi);

ViStatus _VI_FUNC IviDigitizer_ConfigureAcquisition (ViSession vi,
												  ViInt64 NumRecords,
												  ViInt64 RecordSize,
												  ViReal64 SampleRate);

ViStatus _VI_FUNC IviDigitizer_ConfigureActiveTriggerSource (ViSession vi,
												  ViString TriggerSource);


ViStatus _VI_FUNC IviDigitizer_ConfigureChannel (ViSession vi,
											  ViConstString ChannelName,
											  ViReal64 Range,
											  ViReal64 Offset,
											  ViInt32 Coupling,
											  ViBoolean Enabled);

ViStatus _VI_FUNC IviDigitizer_ConfigureEdgeTriggerSource (ViSession vi,
														ViConstString Source,
														ViReal64 Level,
														ViInt32 Slope);

ViStatus _VI_FUNC IviDigitizer_FetchWaveformInt8 (ViSession vi,
												ViConstString ChannelName,
												ViInt64 WaveformArraySize,
												ViInt8 WaveformArray[],
												ViInt64* ActualPoints,
												ViInt64* FirstValidPoint,
												ViReal64* InitialXOffset,
												ViReal64* InitialXTimeSeconds,
												ViReal64* InitialXTimeFraction,
												ViReal64* XIncrement,
												ViReal64* ScaleFactor,
												ViReal64* ScaleOffset);

ViStatus _VI_FUNC IviDigitizer_FetchWaveformInt16 (ViSession vi,
												ViConstString ChannelName,
												ViInt64 WaveformArraySize,
												ViInt16 WaveformArray[],
												ViInt64* ActualPoints,
												ViInt64* FirstValidPoint,
												ViReal64* InitialXOffset,
												ViReal64* InitialXTimeSeconds,
												ViReal64* InitialXTimeFraction,
												ViReal64* XIncrement,
												ViReal64* ScaleFactor,
												ViReal64* ScaleOffset);

ViStatus _VI_FUNC IviDigitizer_FetchWaveformInt32 (ViSession vi,
												ViConstString ChannelName,
												ViInt64 WaveformArraySize,
												ViInt32 WaveformArray[],
												ViInt64* ActualPoints,
												ViInt64* FirstValidPoint,
												ViReal64* InitialXOffset,
												ViReal64* InitialXTimeSeconds,
												ViReal64* InitialXTimeFraction,
												ViReal64* XIncrement,
												ViReal64* ScaleFactor,
												ViReal64* ScaleOffset);

ViStatus _VI_FUNC IviDigitizer_FetchWaveformReal64 (ViSession vi,
												ViConstString ChannelName,
												ViInt64 WaveformArraySize,
												ViReal64 WaveformArray[],
												ViInt64* ActualPoints,
												ViInt64* FirstValidPoint,												 
												ViReal64* InitialXOffset,
												ViReal64* InitialXTimeSeconds,
												ViReal64* InitialXTimeFraction,
												ViReal64* XIncrement);

ViStatus _VI_FUNC IviDigitizer_GetChannelName (ViSession vi,
											ViInt32 ChannelIndex, 
											ViInt32 ChannelNameBufferSize,
											ViChar ChannelName[]);
									  
ViStatus _VI_FUNC IviDigitizer_GetTriggerSourceName (ViSession vi,
												  ViInt32 SourceIndex, 
												  ViInt32 SourceNameBufferSize,
												  ViChar SourceName[]);

ViStatus _VI_FUNC IviDigitizer_InitiateAcquisition (ViSession vi);

ViStatus _VI_FUNC IviDigitizer_IsIdle (ViSession vi,
											ViInt32* Status);

ViStatus _VI_FUNC IviDigitizer_IsMeasuring (ViSession vi,
										 ViInt32* Status);

ViStatus _VI_FUNC IviDigitizer_IsWaitingForArm (ViSession vi,
											 ViInt32* Status);

ViStatus _VI_FUNC IviDigitizer_IsWaitingForTrigger (ViSession vi,
												 ViInt32* Status);

ViStatus _VI_FUNC IviDigitizer_QueryMinWaveformMemory (ViSession vi,
													ViInt32 DataWidth, 
													ViInt64 NumRecords, 
													ViInt64 OffsetWithinRecord, 
													ViInt64 NumPointsPerRecord,
													ViInt64* NumSamples);												 
												 
ViStatus _VI_FUNC IviDigitizer_ReadWaveformInt8 (ViSession vi,
											ViConstString ChannelName,
											ViInt32 MaxTimeMilliseconds,
											ViInt64 WaveformArraySize,
											ViInt8 WaveformArray[],
											ViInt64* ActualPoints,
											ViInt64* FirstValidPoint,
											ViReal64* InitialXOffset,
											ViReal64* InitialXTimeSeconds,
											ViReal64* InitialXTimeFraction,
											ViReal64* XIncrement,
											ViReal64* ScaleFactor,
											ViReal64* ScaleOffset);

ViStatus _VI_FUNC IviDigitizer_ReadWaveformInt16 (ViSession vi,
											ViConstString ChannelName,
											ViInt32 MaxTimeMilliseconds,
											ViInt64 WaveformArraySize,
											ViInt16 WaveformArray[],
											ViInt64* ActualPoints,
											ViInt64* FirstValidPoint,
											ViReal64* InitialXOffset,
											ViReal64* InitialXTimeSeconds,
											ViReal64* InitialXTimeFraction,
											ViReal64* XIncrement,
											ViReal64* ScaleFactor,
											ViReal64* ScaleOffset);

ViStatus _VI_FUNC IviDigitizer_ReadWaveformInt32 (ViSession vi,
											ViConstString ChannelName,
											ViInt32 MaxTimeMilliseconds,
											ViInt64 WaveformArraySize,
											ViInt32 WaveformArray[],
											ViInt64* ActualPoints,
											ViInt64* FirstValidPoint,
											ViReal64* InitialXOffset,
											ViReal64* InitialXTimeSeconds,
											ViReal64* InitialXTimeFraction,
											ViReal64* XIncrement,
											ViReal64* ScaleFactor,
											ViReal64* ScaleOffset);

ViStatus _VI_FUNC IviDigitizer_ReadWaveformReal64 (ViSession vi,
											ViConstString ChannelName,
											ViInt32 MaxTimeMilliseconds,
											ViInt64 WaveformArraySize,
											ViReal64 WaveformArray[],
											ViInt64* ActualPoints,
											ViInt64* FirstValidPoint,
											ViReal64* InitialXOffset,
											ViReal64* InitialXTimeSeconds,
											ViReal64* InitialXTimeFraction,
											ViReal64* XIncrement);

ViStatus _VI_FUNC IviDigitizer_WaitForAcquisitionComplete (ViSession vi,
														ViInt32 MaxTimeMilliseconds);

/*- IviDigitizerMultiRecordAcquisition Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_FetchMultiRecordWaveformInt8 (ViSession vi,
														ViConstString ChannelName,
														ViInt64 FirstRecord,
														ViInt64 NumRecords,
														ViInt64 OffsetWithinRecord,
														ViInt64 NumPointsPerRecord,
														ViInt64 WaveformArraySize,
														ViInt8 WaveformArray[],
														ViInt64* ActualRecords,
														ViInt64 ActualPoints[],
														ViInt64 FirstValidPoint[],
														ViReal64 InitialXOffset[],
														ViReal64 InitialXTimeSeconds[],
														ViReal64 InitialXTimeFraction[],
														ViReal64* XIncrement,
														ViReal64* ScaleFactor,
														ViReal64* ScaleOffset);

ViStatus _VI_FUNC IviDigitizer_FetchMultiRecordWaveformInt16 (ViSession vi,
														ViConstString ChannelName,
														ViInt64 FirstRecord,
														ViInt64 NumRecords,
														ViInt64 OffsetWithinRecord,
														ViInt64 NumPointsPerRecord,
														ViInt64 WaveformArraySize,
														ViInt16 WaveformArray[],
														ViInt64* ActualRecords,
														ViInt64 ActualPoints[],
														ViInt64 FirstValidPoint[],
														ViReal64 InitialXOffset[],
														ViReal64 InitialXTimeSeconds[],
														ViReal64 InitialXTimeFraction[],
														ViReal64* XIncrement,
														ViReal64* ScaleFactor,
														ViReal64* ScaleOffset);
														
ViStatus _VI_FUNC IviDigitizer_FetchMultiRecordWaveformInt32 (ViSession vi,
														ViConstString ChannelName,
														ViInt64 FirstRecord,
														ViInt64 NumRecords,
														ViInt64 OffsetWithinRecord,
														ViInt64 NumPointsPerRecord,
														ViInt64 WaveformArraySize,
														ViInt32 WaveformArray[],
														ViInt64* ActualRecords,
														ViInt64 ActualPoints[],
														ViInt64 FirstValidPoint[],
														ViReal64 InitialXOffset[],
														ViReal64 InitialXTimeSeconds[],
														ViReal64 InitialXTimeFraction[],
														ViReal64* XIncrement,
														ViReal64* ScaleFactor,
														ViReal64* ScaleOffset);

ViStatus _VI_FUNC IviDigitizer_FetchMultiRecordWaveformReal64 (ViSession vi,
														ViConstString ChannelName,
														ViInt64 FirstRecord,
														ViInt64 NumRecords,
														ViInt64 OffsetWithinRecord,
														ViInt64 NumPointsPerRecord,
														ViInt64 WaveformArraySize,
														ViReal64 WaveformArray[],
														ViInt64* ActualRecords,
														ViInt64 ActualPoints[],
														ViInt64 FirstValidPoint[],
														ViReal64 InitialXOffset[],
														ViReal64 InitialXTimeSeconds[],
														ViReal64 InitialXTimeFraction[],
														ViReal64* XIncrement);
														
/*- IviDigitizerBoardTemperature Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureTemperatureUnits (ViSession vi,
													   ViInt32 Units);

ViStatus _VI_FUNC IviDigitizer_QueryBoardTemperature (ViSession vi,
												   ViReal64* Temperature);

/*- IviDigitizerChannelFilter Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureInputFilter (ViSession vi,
												  ViConstString ChannelName,
												  ViReal64 MinFrequency,
												  ViReal64 MaxFrequency);

/*- IviDigitizerChannelTemperature Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_QueryChannelTemperature (ViSession vi,
													 ViConstString ChannelName,
													 ViReal64* Temperature);

/*- IviDigitizerTimeInterleavedChannels Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureTimeInterleavedChannelList (ViSession vi,
																 ViConstString ChannelName,
																 ViConstString ChannelList);

/*- IviDigitizerDataInterleavedChannels Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureDataInterleavedChannelList (ViSession vi,
																 ViConstString ChannelName,
																 ViConstString ChannelList);

/*- IviDigitizerReferenceOscillator Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureReferenceOscillator (ViSession vi,
														  ViInt32 Source,
														  ViReal64 Frequency);

ViStatus _VI_FUNC IviDigitizer_ConfigureReferenceOscillatorOutputEnabled (ViSession vi,
																	   ViBoolean Enabled);

/*- IviDigitizerSampleClock Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureSampleClock (ViSession vi,
												  ViInt32 Source,
												  ViReal64 Frequency,
												  ViReal64 Divider);

ViStatus _VI_FUNC IviDigitizer_ConfigureSampleClockOutputEnabled (ViSession vi,
															   ViBoolean Enabled);

/*- IviDigitizerSampleMode Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureSampleMode (ViSession vi,
												 ViInt32 SampleMode);

/*- IviDigitizerSelfCalibration Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_SelfCalibrate (ViSession vi);

/*- IviDigitizerDownconversion Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureDownconversion (ViSession vi,
													 ViConstString ChannelName,
													 ViBoolean Enabled,
													 ViReal64 CenterFrequency);

/*- IviDigitizerArm Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureEdgeArmSource (ViSession vi,
													ViConstString Source,
													ViReal64 Level,
													ViInt32 Slope);

ViStatus _VI_FUNC IviDigitizer_GetArmSourceName (ViSession vi,
											  ViInt32 SourceIndex, 
											  ViInt32 SourceNameBufferSize,
											  ViChar SourceName[]);

/*- IviDigitizerMultiArm Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureMultiArm (ViSession vi,
											   ViConstString SourceList,
											   ViInt32 Operator);

/*- IviDigitizerGlitchArm Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureGlitchArmSource (ViSession vi,
													  ViConstString Source,
													  ViReal64 Level,
													  ViReal64 Width,
													  ViInt32 Polarity,
													  ViInt32 Condition);

/*- IviDigitizerRuntArm Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureRuntArmSource (ViSession vi,
													ViConstString Source,
													ViReal64 ThresholdLow,
													ViReal64 ThresholdHigh,
													ViInt32 Polarity);
													
/*- IviDigitizerSoftwareArm Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_SendSoftwareArm (ViSession vi);

/*- IviDigitizerTVArm Extension -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureTVArmSource (ViSession vi,
												  ViConstString Source,
												  ViInt32 SignalFormat,
												  ViInt32 Event,
												  ViInt32 Polarity);

/*- IviDigitizerWidthArm Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureWidthArmSource (ViSession vi,
													 ViConstString Source,
													 ViReal64 Level,
													 ViReal64 ThresholdLow,
													 ViReal64 ThresholdHigh,
													 ViInt32 Polarity,
													 ViInt32 Condition);

/*- IviDigitizerWindowArm Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureWindowArmSource (ViSession vi,
													  ViConstString Source,
													  ViReal64 ThresholdLow,
													  ViReal64 ThresholdHigh,
													  ViInt32 Condition);

/*- IviDigitizerTriggerModifier Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureTriggerModifier (ViSession vi, 
													  ViInt32 TriggerModifier);

/*- IviDigitizerMultiTrigger Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureMultiTrigger (ViSession vi,
												   ViConstString SourceList,
												   ViInt32 Operator);

/*- IviDigitizerPretriggerSamples Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigurePretriggerSamples (ViSession vi,
														ViInt64 PretriggerSamples);

/*- IviDigitizerTriggerHoldoff Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureTriggerHoldoff (ViSession vi,
													 ViReal64 TriggerHoldoff);

/*- IIviDigitizerGlitchTrigger Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureGlitchTriggerSource (ViSession vi,
														  ViConstString Source,
														  ViReal64 Level,
														  ViReal64 Width,
														  ViInt32 Polarity,
														  ViInt32 Condition);

/*- IviDigitizerRuntTrigger Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureRuntTriggerSource (ViSession vi,
														ViConstString Source,
														ViReal64 ThresholdLow,
														ViReal64 ThresholdHigh,
														ViInt32 Polarity);

/*- IviDigitizerSoftwareTrigger Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_SendSoftwareTrigger (ViSession vi);

/*- IviDigitizerTVTrigger Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureTVTriggerSource (ViSession vi,
													  ViConstString Source,
													  ViInt32 SignalFormat,
													  ViInt32 Event,
													  ViInt32 Polarity);

/*- IviDigitizerWidthTrigger Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureWidthTriggerSource (ViSession vi,
														 ViConstString Source,
														 ViReal64 Level,
														 ViReal64 ThresholdLow,
														 ViReal64 ThresholdHigh,
														 ViInt32 Polarity,
														 ViInt32 Condition);

/*- IviDigitizerWindowTrigger Extension Group -*/
ViStatus _VI_FUNC IviDigitizer_ConfigureWindowTriggerSource (ViSession vi,
														  ViConstString Source,
														  ViReal64 ThresholdLow,
														  ViReal64 ThresholdHigh,
														  ViInt32 Condition);

/****************************************************************************
*--------------- IviDigitizer Class Error And Completion Codes -------------*
****************************************************************************/
#define IVIDIGITIZER_ERROR_TRIGGER_NOT_SOFTWARE						(IVI_CROSS_CLASS_ERROR_BASE + 1L)
#define IVIDIGITIZER_ERROR_CHANNEL_NOT_ENABLED						(IVI_CLASS_ERROR_BASE + 1L)
#define IVIDIGITIZER_ERROR_MAX_TIME_EXCEEDED						(IVI_CLASS_ERROR_BASE + 2L)
#define IVIDIGITIZER_ERROR_ARM_NOT_SOFTWARE							(IVI_CLASS_ERROR_BASE + 3L)
#define IVIDIGITIZER_ERROR_INCOMPATIBLE_FETCH						(IVI_CLASS_ERROR_BASE + 4L)

#define IVIDIGITIZER_ERRMSG_TRIGGER_NOT_SOFTWARE					"Trigger source is not set to software trigger."
#define IVIDIGITIZER_ERRMSG_CHANNEL_NOT_ENABLED						"The specified channel is not enabled."
#define IVIDIGITIZER_ERRMSG_MAX_TIME_EXCEEDED						"Maximum time exceeded before the operation completed."
#define IVIDIGITIZER_ERRMSG_ARM_NOT_SOFTWARE						"Arm source is not set to software arm."
#define IVIDIGITIZER_ERRMSG_INCOMPATIBLE_FETCH						"The multi-record acquisition fetch functions must be used if the number of records to acquire is greater than 1."

#define IVIDIGITIZER_ERROR_CODES_AND_MSGS \
{IVIDIGITIZER_ERROR_TRIGGER_NOT_SOFTWARE,	IVIDIGITIZER_ERRMSG_TRIGGER_NOT_SOFTWARE},\
{IVIDIGITIZER_ERROR_CHANNEL_NOT_ENABLED,	IVIDIGITIZER_ERRMSG_CHANNEL_NOT_ENABLED},\
{IVIDIGITIZER_ERROR_MAX_TIME_EXCEEDED,		IVIDIGITIZER_ERRMSG_MAX_TIME_EXCEEDED},\
{IVIDIGITIZER_ERROR_ARM_NOT_SOFTWARE,		IVIDIGITIZER_ERRMSG_ARM_NOT_SOFTWARE},\
{IVIDIGITIZER_ERROR_INCOMPATIBLE_FETCH,		IVIDIGITIZER_ERRMSG_INCOMPATIBLE_FETCH}

/****************************************************************************
*---------------------------- End Include File ----------------------------*
****************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

#endif /* IVIDIGITIZER_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviDmm.h sha256=78c4747d93998d72abcf9892d804b8cbe4b7aa4841b6fe756da44ec8e4f85f2a bytes=33660 -->
## FILE: imports/include/IviDmm.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviDmm.h`
- sha256: `78c4747d93998d72abcf9892d804b8cbe4b7aa4841b6fe756da44ec8e4f85f2a`
- bytes: 33660

````c
/****************************************************************************
 *                              I V I - D M M                               
 *---------------------------------------------------------------------------
 *    Copyright (c) 1999-2020 National Instruments.  All Rights Reserved.        
 *---------------------------------------------------------------------------
 *                                                                          
 * Title:       ividmm.h                                                    
 * Purpose:     IviDmm Class declarations for the Base and Extended  
 *              IviDmm Capabilities.                                        
 ****************************************************************************/

#ifndef IVIDMM_HEADER
#define IVIDMM_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVIDMM_MAJOR_VERSION                (4L)
#define IVIDMM_MINOR_VERSION                (0L)

#define IVIDMM_CLASS_SPEC_MAJOR_VERSION     (4L)
#define IVIDMM_CLASS_SPEC_MINOR_VERSION     (1L)

#define IVIDMM_DRIVER_VENDOR                "National Instruments"
#ifdef	_IVI_mswin64_
#define IVIDMM_DRIVER_DESCRIPTION           "IviDmm Class Driver [Compiled for 64-bit.]"
#else
#define IVIDMM_DRIVER_DESCRIPTION           "IviDmm Class Driver"
#endif

/****************************************************************************
 *------------------------------ Useful Macros -----------------------------*
 ****************************************************************************/
    /*- Defined values for maxTime parameter to the Measure, Read -*/
    /*- and Fetch functions -*/
#define IVIDMM_VAL_MAX_TIME_INFINITE    IVI_VAL_MAX_TIME_INFINITE
#define IVIDMM_VAL_MAX_TIME_IMMEDIATE   IVI_VAL_MAX_TIME_IMMEDIATE

/****************************************************************************
 *--------------------- IviDmm Class Attribute Defines ---------------------*
 ****************************************************************************/

    /*- IVI Inherent Attributes -*/

        /*- User Options -*/
#define IVIDMM_ATTR_CACHE                     IVI_ATTR_CACHE                       /* ViBoolean */
#define IVIDMM_ATTR_RANGE_CHECK               IVI_ATTR_RANGE_CHECK                 /* ViBoolean */
#define IVIDMM_ATTR_QUERY_INSTRUMENT_STATUS   IVI_ATTR_QUERY_INSTRUMENT_STATUS     /* ViBoolean */
#define IVIDMM_ATTR_RECORD_COERCIONS          IVI_ATTR_RECORD_COERCIONS            /* ViBoolean */
#define IVIDMM_ATTR_SIMULATE                  IVI_ATTR_SIMULATE                    /* ViBoolean */
#define IVIDMM_ATTR_INTERCHANGE_CHECK         IVI_ATTR_INTERCHANGE_CHECK           /* ViBoolean */
#define IVIDMM_ATTR_SPY                       IVI_ATTR_SPY                         /* ViBoolean */
#define IVIDMM_ATTR_USE_SPECIFIC_SIMULATION   IVI_ATTR_USE_SPECIFIC_SIMULATION     /* ViBoolean */

        /*- Instrument Capabilities -*/
#define IVIDMM_ATTR_GROUP_CAPABILITIES        IVI_ATTR_GROUP_CAPABILITIES          /* ViString, read-only */
#define IVIDMM_ATTR_FUNCTION_CAPABILITIES     IVI_ATTR_FUNCTION_CAPABILITIES       /* ViString, read-only */

        /*- Class Driver Information -*/    
#define IVIDMM_ATTR_CLASS_DRIVER_PREFIX                     IVI_ATTR_CLASS_DRIVER_PREFIX         /* ViString, read-only */
#define IVIDMM_ATTR_CLASS_DRIVER_VENDOR                     IVI_ATTR_CLASS_DRIVER_VENDOR         /* ViString, read-only */
#define IVIDMM_ATTR_CLASS_DRIVER_DESCRIPTION                IVI_ATTR_CLASS_DRIVER_DESCRIPTION    /* ViString, read-only */
#define IVIDMM_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION   IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIDMM_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION   IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Specific Driver Information -*/    
#define IVIDMM_ATTR_SPECIFIC_DRIVER_PREFIX                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX      /* ViString, read-only */
#define IVIDMM_ATTR_SPECIFIC_DRIVER_LOCATOR                     IVI_ATTR_SPECIFIC_DRIVER_LOCATOR     /* ViString, read-only */
#define IVIDMM_ATTR_IO_RESOURCE_DESCRIPTOR                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR      /* ViString, read-only */
#define IVIDMM_ATTR_LOGICAL_NAME                                IVI_ATTR_LOGICAL_NAME                /* ViString, read-only */
#define IVIDMM_ATTR_SPECIFIC_DRIVER_VENDOR                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR      /* ViString, read-only */
#define IVIDMM_ATTR_SPECIFIC_DRIVER_DESCRIPTION                 IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION /* ViString, read-only */
#define IVIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/    
#define IVIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION     IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION /* ViString, read-only */
#define IVIDMM_ATTR_INSTRUMENT_MANUFACTURER          IVI_ATTR_INSTRUMENT_MANUFACTURER      /* ViString, read-only */
#define IVIDMM_ATTR_INSTRUMENT_MODEL                 IVI_ATTR_INSTRUMENT_MODEL             /* ViString, read-only */
#define IVIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS      IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS

        /*- Version Information -*/
#define IVIDMM_ATTR_CLASS_DRIVER_REVISION            IVI_ATTR_CLASS_DRIVER_REVISION              /* ViString, read-only */

#define IVIDMM_ATTR_SPECIFIC_DRIVER_REVISION         IVI_ATTR_SPECIFIC_DRIVER_REVISION             /* ViString, read-only */

        /*- Driver Setup Information -*/
#define IVIDMM_ATTR_DRIVER_SETUP              IVI_ATTR_DRIVER_SETUP                /* ViString */

    /*- IviDmm Fundamental Attributes -*/
#define IVIDMM_ATTR_FUNCTION                  (IVI_CLASS_PUBLIC_ATTR_BASE + 1L)    /* ViInt32  */
#define IVIDMM_ATTR_RANGE                     (IVI_CLASS_PUBLIC_ATTR_BASE + 2L)    /* ViReal64 */
#define IVIDMM_ATTR_RESOLUTION_ABSOLUTE       (IVI_CLASS_PUBLIC_ATTR_BASE + 8L)    /* ViReal64 */
#define IVIDMM_ATTR_TRIGGER_SOURCE            (IVI_CLASS_PUBLIC_ATTR_BASE + 4L)    /* ViInt32  */
#define IVIDMM_ATTR_TRIGGER_DELAY             (IVI_CLASS_PUBLIC_ATTR_BASE + 5L)    /* ViReal64 */

    /*- IviDmmAcMeasurement Attributes -*/
#define IVIDMM_ATTR_AC_MIN_FREQ               (IVI_CLASS_PUBLIC_ATTR_BASE + 6L)    /* ViReal64 */
#define IVIDMM_ATTR_AC_MAX_FREQ               (IVI_CLASS_PUBLIC_ATTR_BASE + 7L)    /* ViReal64 */

    /*- IviDmmFrequencyMeasurement Attributes -*/
#define IVIDMM_ATTR_FREQ_VOLTAGE_RANGE        (IVI_CLASS_PUBLIC_ATTR_BASE + 101L)  /* ViReal64 */

    /*- IviDmmTemperatureMeasurement Attributes -*/
#define IVIDMM_ATTR_TEMP_TRANSDUCER_TYPE      (IVI_CLASS_PUBLIC_ATTR_BASE + 201L)  /* ViInt32  */

    /*- IviDmmThermocouple Attributes -*/
#define IVIDMM_ATTR_TEMP_TC_TYPE              (IVI_CLASS_PUBLIC_ATTR_BASE + 231L)  /* ViInt32  */
#define IVIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE     (IVI_CLASS_PUBLIC_ATTR_BASE + 232L)  /* ViInt32  */
#define IVIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC    (IVI_CLASS_PUBLIC_ATTR_BASE + 233L)  /* ViReal64 */

    /*- IviDmmResistanceTemperatureDevice Attributes -*/
#define IVIDMM_ATTR_TEMP_RTD_ALPHA            (IVI_CLASS_PUBLIC_ATTR_BASE + 241L)  /* ViReal64 */
#define IVIDMM_ATTR_TEMP_RTD_RES              (IVI_CLASS_PUBLIC_ATTR_BASE + 242L)  /* ViReal64 */

    /*- IviDmmThermistor Attributes -*/
#define IVIDMM_ATTR_TEMP_THERMISTOR_RES       (IVI_CLASS_PUBLIC_ATTR_BASE + 251L)  /* ViReal64 */

    /*- IviDmmMultiPoint Attributes -*/
#define IVIDMM_ATTR_SAMPLE_COUNT              (IVI_CLASS_PUBLIC_ATTR_BASE + 301L)  /* ViInt32  */
#define IVIDMM_ATTR_SAMPLE_TRIGGER            (IVI_CLASS_PUBLIC_ATTR_BASE + 302L)  /* ViInt32  */
#define IVIDMM_ATTR_SAMPLE_INTERVAL           (IVI_CLASS_PUBLIC_ATTR_BASE + 303L)  /* ViReal64 */
#define IVIDMM_ATTR_TRIGGER_COUNT             (IVI_CLASS_PUBLIC_ATTR_BASE + 304L)  /* ViInt32  */
#define IVIDMM_ATTR_MEAS_COMPLETE_DEST        (IVI_CLASS_PUBLIC_ATTR_BASE + 305L)  /* ViInt32  */

    /*- IviDmmTriggerSlope Attributes -*/
#define IVIDMM_ATTR_TRIGGER_SLOPE             (IVI_CLASS_PUBLIC_ATTR_BASE + 334L)  /* ViInt32  */

    /*- IviDmmDeviceInfo Attributes -*/
#define IVIDMM_ATTR_APERTURE_TIME             (IVI_CLASS_PUBLIC_ATTR_BASE + 321L)  /* ViReal64, read-only */
#define IVIDMM_ATTR_APERTURE_TIME_UNITS       (IVI_CLASS_PUBLIC_ATTR_BASE + 322L)  /* ViInt32,  read-only */

    /*- IviDmmAutoRangeValue Attributes -*/
#define IVIDMM_ATTR_AUTO_RANGE_VALUE          (IVI_CLASS_PUBLIC_ATTR_BASE + 331L)  /* ViReal64, read-only */

    /*- IviDmmAutoZero Attributes -*/
#define IVIDMM_ATTR_AUTO_ZERO                 (IVI_CLASS_PUBLIC_ATTR_BASE + 332L)  /* ViInt32  */

    /*- IviDmmPowerLineFrequency Attributes -*/
#define IVIDMM_ATTR_POWERLINE_FREQ            (IVI_CLASS_PUBLIC_ATTR_BASE + 333L)  /* ViReal64 */


/****************************************************************************
 *----------------- IviDmm Class Attribute Value Defines -------------------*
 ****************************************************************************/

    /*- Defined values for attribute IVIDMM_ATTR_FUNCTION -*/
#define IVIDMM_VAL_DC_VOLTS                     (1L)
#define IVIDMM_VAL_AC_VOLTS                     (2L)
#define IVIDMM_VAL_DC_CURRENT                   (3L)
#define IVIDMM_VAL_AC_CURRENT                   (4L)
#define IVIDMM_VAL_2_WIRE_RES                   (5L)
#define IVIDMM_VAL_4_WIRE_RES                   (101L)
#define IVIDMM_VAL_AC_PLUS_DC_VOLTS             (106L)
#define IVIDMM_VAL_AC_PLUS_DC_CURRENT           (107L)
#define IVIDMM_VAL_FREQ                         (104L)
#define IVIDMM_VAL_PERIOD                       (105L)
#define IVIDMM_VAL_TEMPERATURE                  (108L)

#define IVIDMM_VAL_FUNC_CLASS_EXT_BASE          (500L)
#define IVIDMM_VAL_FUNC_SPECIFIC_EXT_BASE       (1000L)

    /*- Defined values for attribute IVIDMM_ATTR_RANGE -*/
#define IVIDMM_VAL_AUTO_RANGE_ON                (-1.0)
#define IVIDMM_VAL_AUTO_RANGE_OFF               (-2.0)
#define IVIDMM_VAL_AUTO_RANGE_ONCE              (-3.0)

#define IVIDMM_VAL_RANGE_CLASS_EXT_BASE         (-100.0)
#define IVIDMM_VAL_RANGE_SPECIFIC_EXT_BASE      (-1000.0)

    /*- Defined values for attribute IVIDMM_ATTR_FREQ_VOLTAGE_RANGE -*/
/* #define IVIDMM_VAL_AUTO_RANGE_ON                DEFINED ABOVE */
/* #define IVIDMM_VAL_AUTO_RANGE_OFF               DEFINED ABOVE */

#define IVIDMM_VAL_FREQ_VOLT_RANGE_CLASS_EXT_BASE    (-100.0L)
#define IVIDMM_VAL_FREQ_VOLT_RANGE_SPECIFIC_EXT_BASE (-1000.0L)

    /*- Defined values for attribute IVIDMM_ATTR_TRIGGER_DELAY -*/
#define IVIDMM_VAL_AUTO_DELAY_ON                    (-1.0L)
#define IVIDMM_VAL_AUTO_DELAY_OFF                   (-2.0L)

#define IVIDMM_VAL_TRIGGER_DELAY_CLASS_EXT_BASE     (-100.0L)
#define IVIDMM_VAL_TRIGGER_DELAY_SPECIFIC_EXT_BASE  (-1000.0L)

    /*- Defined values for attribute IVIDMM_ATTR_TRIGGER_SOURCE -*/
#define IVIDMM_VAL_IMMEDIATE                        (1L)
#define IVIDMM_VAL_EXTERNAL                         (2L)
#define IVIDMM_VAL_SOFTWARE_TRIG                    (3L)
#define IVIDMM_VAL_TTL0                             (111L)
#define IVIDMM_VAL_TTL1                             (112L)
#define IVIDMM_VAL_TTL2                             (113L)
#define IVIDMM_VAL_TTL3                             (114L)
#define IVIDMM_VAL_TTL4                             (115L)
#define IVIDMM_VAL_TTL5                             (116L)
#define IVIDMM_VAL_TTL6                             (117L)
#define IVIDMM_VAL_TTL7                             (118L)
#define IVIDMM_VAL_ECL0                             (119L)
#define IVIDMM_VAL_ECL1                             (120L)
#define IVIDMM_VAL_PXI_STAR                         (131L)
#define IVIDMM_VAL_RTSI_0                           (140L)
#define IVIDMM_VAL_RTSI_1                           (141L)
#define IVIDMM_VAL_RTSI_2                           (142L)
#define IVIDMM_VAL_RTSI_3                           (143L)
#define IVIDMM_VAL_RTSI_4                           (144L)
#define IVIDMM_VAL_RTSI_5                           (145L)
#define IVIDMM_VAL_RTSI_6                           (146L)

#define IVIDMM_VAL_TRIGGER_SOURCE_CLASS_EXT_BASE    (500L)
#define IVIDMM_VAL_TRIGGER_SOURCE_SPECIFIC_EXT_BASE (1000L)

    /*- Defined values for attribute IVIDMM_ATTR_TEMP_TRANSDUCER_TYPE -*/
#define IVIDMM_VAL_THERMOCOUPLE                     (1L)
#define IVIDMM_VAL_THERMISTOR                       (2L)
#define IVIDMM_VAL_2_WIRE_RTD                       (3L)
#define IVIDMM_VAL_4_WIRE_RTD                       (4L)

#define IVIDMM_VAL_TRANSDUCER_CLASS_EXT_BASE        (100L)
#define IVIDMM_VAL_TRANSDUCER_SPECIFIC_EXT_BASE     (1000L)

    /*- Defined values for attribute IVIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE -*/
#define IVIDMM_VAL_TEMP_REF_JUNC_INTERNAL           (1L)
#define IVIDMM_VAL_TEMP_REF_JUNC_FIXED              (2L)
#define IVIDMM_VAL_TEMP_REF_JUNC_CLASS_EXT_BASE     (100L)
#define IVIDMM_VAL_TEMP_REF_JUNC_SPECIFIC_EXT_BASE  (1000L)
    
    /*- Defined values for attribute IVIDMM_ATTR_TEMP_TC_TYPE -*/
#define IVIDMM_VAL_TEMP_TC_B                        (1L)
#define IVIDMM_VAL_TEMP_TC_C                        (2L)
#define IVIDMM_VAL_TEMP_TC_D                        (3L)
#define IVIDMM_VAL_TEMP_TC_E                        (4L)
#define IVIDMM_VAL_TEMP_TC_G                        (5L)
#define IVIDMM_VAL_TEMP_TC_J                        (6L)
#define IVIDMM_VAL_TEMP_TC_K                        (7L)
#define IVIDMM_VAL_TEMP_TC_N                        (8L)
#define IVIDMM_VAL_TEMP_TC_R                        (9L)
#define IVIDMM_VAL_TEMP_TC_S                        (10L)
#define IVIDMM_VAL_TEMP_TC_T                        (11L)
#define IVIDMM_VAL_TEMP_TC_U                        (12L)
#define IVIDMM_VAL_TEMP_TC_V                        (13L)
#define IVIDMM_VAL_TEMP_TC_TYPE_CLASS_EXT_BASE      (100L)
#define IVIDMM_VAL_TEMP_TC_TYPE_SPECIFIC_EXT_BASE   (1000L)
    
    /*- Defined values for attribute IVIDMM_ATTR_MEAS_COMPLETE_DEST -*/
#define IVIDMM_VAL_NONE                         (-1L)
/* #define IVIDMM_VAL_EXTERNAL                  DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL0                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL1                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL2                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL3                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL4                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL5                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL6                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL7                      DEFINED ABOVE */
/* #define IVIDMM_VAL_ECL0                      DEFINED ABOVE */
/* #define IVIDMM_VAL_ECL1                      DEFINED ABOVE */
/* #define IVIDMM_VAL_PXI_STAR                  DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_0                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_1                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_2                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_3                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_4                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_5                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_6                    DEFINED ABOVE */

    /* Defined values for attribute IVIDMM_ATTR_SAMPLE_TRIGGER -*/
/* #define IVIDMM_VAL_IMMEDIATE                 DEFINED ABOVE */
/* #define IVIDMM_VAL_EXTERNAL                  DEFINED ABOVE */
/* #define IVIDMM_VAL_SOFTWARE_TRIG             DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL0                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL1                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL2                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL3                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL4                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL5                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL6                      DEFINED ABOVE */
/* #define IVIDMM_VAL_TTL7                      DEFINED ABOVE */
/* #define IVIDMM_VAL_ECL0                      DEFINED ABOVE */
/* #define IVIDMM_VAL_ECL1                      DEFINED ABOVE */
/* #define IVIDMM_VAL_PXI_STAR                  DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_0                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_1                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_2                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_3                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_4                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_5                    DEFINED ABOVE */
/* #define IVIDMM_VAL_RTSI_6                    DEFINED ABOVE */
#define IVIDMM_VAL_INTERVAL                     (10L)

    /*- Defined values for attribute IVIDMM_ATTR_TRIGGER_SLOPE -*/
#define IVIDMM_VAL_POSITIVE                         (0L)
#define IVIDMM_VAL_NEGATIVE                         (1L)

#define IVIDMM_VAL_TRIGGER_SLOPE_CLASS_EXT_BASE     (100L)
#define IVIDMM_VAL_TRIGGER_SLOPE_SPECIFIC_EXT_BASE  (1000L)

    /*- Defined values for attribute IVIDMM_ATTR_APERTURE_TIME_UNITS -*/
#define IVIDMM_VAL_SECONDS                      (0L)
#define IVIDMM_VAL_POWER_LINE_CYCLES            (1L)

    /*- Defined values for extended attribute IVIDMM_ATTR_AUTO_ZER0 -*/
#define IVIDMM_VAL_AUTO_ZERO_OFF                (0L)
#define IVIDMM_VAL_AUTO_ZERO_ON                 (1L)
#define IVIDMM_VAL_AUTO_ZERO_ONCE               (2L)

#define IVIDMM_VAL_AUTO_ZERO_CLASS_EXT_BASE     (100L)
#define IVIDMM_VAL_AUTO_ZERO_SPECIFIC_EXT_BASE  (1000L)


/****************************************************************************
 *--------- IviDmm Class Instrument Driver Function Declarations -----------*
 ****************************************************************************/
    /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviDmm_init (ViRsrc logicalName, 
                               ViBoolean idQuery, 
                               ViBoolean resetDevice, 
                               ViSession *vi);

ViStatus _VI_FUNC IviDmm_close (ViSession vi);

ViStatus _VI_FUNC IviDmm_reset (ViSession vi);

ViStatus _VI_FUNC IviDmm_self_test (ViSession vi, 
                                    ViInt16 *selfTestResult, 
                                    ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviDmm_error_query (ViSession vi, 
                                      ViInt32 *errorCode, 
                                      ViChar errorMessage[]);

ViStatus _VI_FUNC IviDmm_error_message (ViSession vi, 
                                        ViStatus statusCode, 
                                        ViChar message[]);

ViStatus _VI_FUNC IviDmm_revision_query (ViSession vi, 
                                         ViChar driverRev[], 
                                         ViChar instrRev[]);

    /*- Utility Functions -*/
ViStatus _VI_FUNC IviDmm_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviDmm_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviDmm_Disable (ViSession vi);

    /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviDmm_InitWithOptions (ViRsrc logicalName, 
                                          ViBoolean IDQuery,
                                          ViBoolean resetDevice, 
                                          ViConstString optionString, 
                                          ViSession *vi);

    /*- Set, Get, and Check Attribute Functions -*/
ViStatus _VI_FUNC IviDmm_GetAttributeViInt32 (ViSession vi, 
                                              ViConstString channelName,
                                              ViAttr attributeId,
                                              ViInt32 *value);

ViStatus _VI_FUNC IviDmm_SetAttributeViInt32 (ViSession vi, 
                                              ViConstString channelName,
                                              ViAttr attributeId,
                                              ViInt32 value);

ViStatus _VI_FUNC IviDmm_CheckAttributeViInt32 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviDmm_GetAttributeViInt64 (ViSession vi, 
                                              ViConstString channelName,
                                              ViAttr attributeId,
                                              ViInt64 *value);

ViStatus _VI_FUNC IviDmm_SetAttributeViInt64 (ViSession vi, 
                                              ViConstString channelName,
                                              ViAttr attributeId,
                                              ViInt64 value);

ViStatus _VI_FUNC IviDmm_CheckAttributeViInt64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt64 value);
#endif

ViStatus _VI_FUNC IviDmm_GetAttributeViReal64 (ViSession vi, 
                                               ViConstString channelName, 
                                               ViAttr attributeId, 
                                               ViReal64 *value);

ViStatus _VI_FUNC IviDmm_SetAttributeViReal64 (ViSession vi, 
                                               ViConstString channelName, 
                                               ViAttr attributeId, 
                                               ViReal64 value);

ViStatus _VI_FUNC IviDmm_CheckAttributeViReal64 (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 value);

ViStatus _VI_FUNC IviDmm_GetAttributeViString (ViSession vi, 
                                               ViConstString channelName, 
                                               ViAttr attributeId, 
                                               ViInt32 bufferSize, 
                                               ViChar value[]);

ViStatus _VI_FUNC IviDmm_SetAttributeViString (ViSession vi, 
                                               ViConstString channelName, 
                                               ViAttr attributeId, 
                                               ViConstString value);

ViStatus _VI_FUNC IviDmm_CheckAttributeViString (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViConstString value); 

ViStatus _VI_FUNC IviDmm_GetAttributeViBoolean (ViSession vi, 
                                                ViConstString channelName, 
                                                ViAttr attributeId, 
                                                ViBoolean *value);

ViStatus _VI_FUNC IviDmm_SetAttributeViBoolean (ViSession vi, 
                                                ViConstString channelName, 
                                                ViAttr attributeId, 
                                                ViBoolean value);

ViStatus _VI_FUNC IviDmm_CheckAttributeViBoolean (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean value);

ViStatus _VI_FUNC IviDmm_GetAttributeViSession (ViSession vi, 
                                                ViConstString channelName, 
                                                ViAttr attributeId, 
                                                ViSession *value);

ViStatus _VI_FUNC IviDmm_SetAttributeViSession (ViSession vi, 
                                                ViConstString channelName, 
                                                ViAttr attributeId, 
                                                ViSession value);

ViStatus _VI_FUNC IviDmm_CheckAttributeViSession (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViSession value);

    /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviDmm_LockSession (ViSession vi, 
                                      ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviDmm_UnlockSession (ViSession vi, 
                                        ViBoolean *callerHasLock);

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviDmm_GetError (ViSession vi, 
                                   ViStatus *errorCode, 
                                   ViInt32 bufferSize, 
                                   ViChar description[]);

ViStatus _VI_FUNC IviDmm_ClearError (ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviDmm_GetNextInterchangeWarning (ViSession vi, 
                                                    ViInt32 bufferSize,
                                                    ViChar warning[]);

ViStatus _VI_FUNC IviDmm_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviDmm_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviDmm_GetNextCoercionRecord (ViSession vi,
                                                ViInt32 bufferSize, 
                                                ViChar record[]);

ViStatus _VI_FUNC IviDmm_GetSpecificDriverCHandle (ViSession vi,
                                                   ViSession* specificDriverCHandle);

ViStatus _VI_FUNC IviDmm_GetSpecificDriverIUnknownPtr (ViSession vi,
                                                       void* specificDriverIUnknownPtr);
    /*- IviDmmBase Functions -*/
ViStatus _VI_FUNC   IviDmm_ConfigureMeasurement (ViSession vi, 
                                                 ViInt32 function, 
                                                 ViReal64 range, 
                                                 ViReal64 resolution);

ViStatus _VI_FUNC   IviDmm_ConfigureTrigger (ViSession vi, 
                                             ViInt32 triggerSource, 
                                             ViReal64 triggerDelay);

ViStatus _VI_FUNC   IviDmm_Read (ViSession vi, 
                                 ViInt32 maxTime, 
                                 ViReal64 *reading);

ViStatus _VI_FUNC   IviDmm_Fetch (ViSession vi, 
                                  ViInt32 maxTime, 
                                  ViReal64 *reading);

ViStatus _VI_FUNC   IviDmm_Abort (ViSession vi);

ViStatus _VI_FUNC   IviDmm_Initiate (ViSession vi);

ViStatus _VI_FUNC   IviDmm_IsOverRange (ViSession vi, 
                                        ViReal64 measurementValue, 
                                        ViBoolean *isOverRange);

    /*- IviDmmAcMeasurement Functions -*/
ViStatus _VI_FUNC   IviDmm_ConfigureACBandwidth (ViSession vi, 
                                                 ViReal64 minFreq, 
                                                 ViReal64 maxFreq);
    
    /*- IviDmmFrequencyMeasurement Functions -*/
ViStatus _VI_FUNC   IviDmm_ConfigureFrequencyVoltageRange (ViSession vi, 
                                                           ViReal64 frequencyVoltageRange);

    /*- IviDmmTemperatureMeasurement Functions -*/
ViStatus _VI_FUNC   IviDmm_ConfigureTransducerType (ViSession vi, 
                                                    ViInt32 transducerType);

    /*- IviDmmThermocouple Functions -*/
ViStatus _VI_FUNC   IviDmm_ConfigureFixedRefJunction (ViSession vi, 
                                                      ViReal64 fixedRefJunction);
ViStatus _VI_FUNC   IviDmm_ConfigureThermocouple (ViSession vi, 
                                                  ViInt32 thermocoupleType, 
                                                  ViInt32 refJunctionType);

    /*- IviDmmRTD Functions -*/
ViStatus _VI_FUNC   IviDmm_ConfigureRTD (ViSession vi, 
                                         ViReal64 alpha, 
                                         ViReal64 resistance);

    /*- IviDmmThermistor Functions -*/
ViStatus _VI_FUNC   IviDmm_ConfigureThermistor (ViSession vi, 
                                                ViReal64 resistance);

    /*- IviDmmMultiPoint Functions -*/
ViStatus _VI_FUNC   IviDmm_ConfigureMeasCompleteDest (ViSession vi, 
                                                      ViInt32 measCompleteDest);
ViStatus _VI_FUNC   IviDmm_ConfigureMultiPoint (ViSession vi, 
                                                ViInt32 triggerCount, 
                                                ViInt32 sampleCount, 
                                                ViInt32 sampleTrigger, 
                                                ViReal64 sampleInterval);
ViStatus _VI_FUNC   IviDmm_ReadMultiPoint      (ViSession vi, 
                                                ViInt32 maxTime, 
                                                ViInt32 arraySize, 
                                                ViReal64 readingArray[], 
                                                ViInt32 *actualPts);
ViStatus _VI_FUNC   IviDmm_FetchMultiPoint     (ViSession vi, 
                                                ViInt32 maxTime, 
                                                ViInt32 arraySize, 
                                                ViReal64 readingArray[], 
                                                ViInt32 *actualPts);

    /*- IviDmmTriggerSlope Functions -*/
ViStatus _VI_FUNC   IviDmm_ConfigureTriggerSlope (ViSession vi, 
                                                  ViInt32 polarity);

    /*- IviDmmSoftwareTrigger Functions -*/
ViStatus _VI_FUNC   IviDmm_SendSoftwareTrigger (ViSession vi);

    /*- IviDmmDeviceInfo Functions -*/
ViStatus _VI_FUNC   IviDmm_GetApertureTimeInfo (ViSession vi, 
                                                ViReal64 *apertureTime, 
                                                ViInt32 *apertureTimeUnits);

    /*- IviDmmAutoRangeValue Functions -*/
ViStatus _VI_FUNC   IviDmm_GetAutoRangeValue (ViSession vi, 
                                              ViReal64 *autoRangeValue);

    /*- IviDmmAutoZero Functions -*/
ViStatus _VI_FUNC   IviDmm_ConfigureAutoZeroMode (ViSession vi, 
                                                  ViInt32 autoZeroMode);

    /*- IviDmmPowerLineFrequency Functions -*/
ViStatus _VI_FUNC   IviDmm_ConfigurePowerLineFrequency (ViSession vi, 
                                                        ViReal64 powerLineFreq);
                                                
/****************************************************************************
 *----------------- IviDmm Class Error And Completion Codes ----------------*
 ****************************************************************************/
#define IVIDMM_WARN_OVER_RANGE              (IVI_CLASS_WARN_BASE  + 1)

#define IVIDMM_ERROR_TRIGGER_NOT_SOFTWARE   (IVI_CROSS_CLASS_ERROR_BASE + 1)
#define IVIDMM_ERROR_MAX_TIME_EXCEEDED      (IVI_CLASS_ERROR_BASE + 3)

#define IVIDMM_WRNMSG_OVER_RANGE            "Over range."

#define IVIDMM_ERRMSG_MAX_TIME_EXCEEDED     "Max Time exceeded before "\
                                            "operation completed."
#define IVIDMM_ERRMSG_TRIGGER_NOT_SOFTWARE  "The trigger source is not set to "\
                                            "software trigger."
#define IVIDMM_ERROR_CODES_AND_MSGS                                         \
        {IVIDMM_WARN_OVER_RANGE,            IVIDMM_WRNMSG_OVER_RANGE},          \
        {IVIDMM_ERROR_MAX_TIME_EXCEEDED,    IVIDMM_ERRMSG_MAX_TIME_EXCEEDED},    \
        {IVIDMM_ERROR_TRIGGER_NOT_SOFTWARE, IVIDMM_ERRMSG_TRIGGER_NOT_SOFTWARE} 
        
/*- IviDmmObsolete.h included for backwards compatibility -*/
#include "IviDmmObsolete.h"

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/

#if defined(__cplusplus) || defined(__cplusplus__)
}                                                    
#endif

#endif /* IVIDMM_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviDmmObsolete.h sha256=1ff25f22a79b150b58145e3e6d07dc57d810a4c6e62de412ae4225ae680c5df2 bytes=7394 -->
## FILE: imports/include/IviDmmObsolete.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviDmmObsolete.h`
- sha256: `1ff25f22a79b150b58145e3e6d07dc57d810a4c6e62de412ae4225ae680c5df2`
- bytes: 7394

````c
/*****************************************************************************
 *                             I V I - DMM                                   
 *----------------------------------------------------------------------------
 *    Copyright (c) 1998-2020 National Instruments.  All Rights Reserved.         
 *----------------------------------------------------------------------------
 *                                                                           
 * Title:       IviDmmObsolete.h                                              
 * Purpose:     IviDmm Class value and attribute Id declarations for the     
 *              now obsolete IviDmm 1.0 specification.                        
 *              These macros are defined to keep backward compatibility with 
 *              previous versions of this file.  Dmm specific drivers        
 *              should no longer use these macros. Instead, the drivers must 
 *              use definitions from the current IviDmm.h header file.       
 *****************************************************************************/

#ifndef IVIDMM_HEADER_OBSOLETE
#define IVIDMM_HEADER_OBSOLETE

    /*- Obsolete Inherent Attributes -*/
#define IVIDMM_ATTR_CLASS_MAJOR_VERSION       IVI_ATTR_CLASS_MAJOR_VERSION         /* ViInt32,  read-only */
#define IVIDMM_ATTR_CLASS_MINOR_VERSION       IVI_ATTR_CLASS_MINOR_VERSION         /* ViInt32,  read-only */
#define IVIDMM_ATTR_CLASS_REVISION            IVI_ATTR_CLASS_REVISION              /* ViString, read-only */

#define IVIDMM_ATTR_CLASS_PREFIX              IVI_ATTR_CLASS_PREFIX                /* ViString, read-only */
#define IVIDMM_ATTR_SPECIFIC_PREFIX           IVI_ATTR_SPECIFIC_PREFIX             /* ViString, read-only */
#define IVIDMM_ATTR_MODULE_PATHNAME           IVI_ATTR_MODULE_PATHNAME             /* ViString, read-only */

#define IVIDMM_ATTR_DRIVER_MAJOR_VERSION      IVI_ATTR_DRIVER_MAJOR_VERSION        /* ViInt32,  read-only */
#define IVIDMM_ATTR_DRIVER_MINOR_VERSION      IVI_ATTR_DRIVER_MINOR_VERSION        /* ViInt32,  read-only */
#define IVIDMM_ATTR_DRIVER_REVISION           IVI_ATTR_DRIVER_REVISION             /* ViString, read-only */

#define IVIDMM_ATTR_ENGINE_MAJOR_VERSION      IVI_ATTR_ENGINE_MAJOR_VERSION        /* ViInt32,  read-only */
#define IVIDMM_ATTR_ENGINE_MINOR_VERSION      IVI_ATTR_ENGINE_MINOR_VERSION        /* ViInt32,  read-only */
#define IVIDMM_ATTR_ENGINE_REVISION           IVI_ATTR_ENGINE_REVISION             /* ViString, read-only */

#define IVIDMM_ATTR_NUM_CHANNELS              IVI_ATTR_NUM_CHANNELS                /* ViInt32,  read-only */
#define IVIDMM_ATTR_QUERY_INSTR_STATUS        IVI_ATTR_QUERY_INSTR_STATUS             /* ViBoolean */
#define IVIDMM_ATTR_RESOURCE_DESCRIPTOR       IVI_ATTR_RESOURCE_DESCRIPTOR            /* ViString, read-only */

#define IVIDMM_ATTR_IO_SESSION_TYPE                  IVI_ATTR_IO_SESSION_TYPE
#define IVIDMM_ATTR_IO_SESSION                       IVI_ATTR_IO_SESSION

#define IVIDMM_ATTR_CLASS_DRIVER_MAJOR_VERSION       IVI_ATTR_CLASS_DRIVER_MAJOR_VERSION         /* ViInt32,  read-only */
#define IVIDMM_ATTR_CLASS_DRIVER_MINOR_VERSION       IVI_ATTR_CLASS_DRIVER_MINOR_VERSION         /* ViInt32,  read-only */

#define IVIDMM_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION        /* ViInt32,  read-only */
#define IVIDMM_ATTR_SPECIFIC_DRIVER_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_MINOR_VERSION        /* ViInt32,  read-only */

#define IVIDMM_ATTR_ATTRIBUTE_CAPABILITIES    IVI_ATTR_ATTRIBUTE_CAPABILITIES      /* ViString, read-only */

        /*- Error Info -*/
#define IVIDMM_ATTR_PRIMARY_ERROR             IVI_ATTR_PRIMARY_ERROR               /* ViInt32  */
#define IVIDMM_ATTR_SECONDARY_ERROR           IVI_ATTR_SECONDARY_ERROR             /* ViInt32  */
#define IVIDMM_ATTR_ERROR_ELABORATION         IVI_ATTR_ERROR_ELABORATION           /* ViString */

    /*- Obsolete Macros -*/
#define IVIDMM_VAL_OVER_RANGE_READING         (1.0E+301)
#define IVIDMM_VAL_MAX_VALID_READING          (1.0E+300)

    /*- Obsolete Attributes -*/
#define IVIDMM_ATTR_RESOLUTION                (IVI_CLASS_PUBLIC_ATTR_BASE  + 3L)

    /*- Obsolete values for attributes -*/
        /*- IVIDMM_ATTR_FUNCTION values -*/
#define IVIDMM_VAL_DIODE                      (102)
#define IVIDMM_VAL_CONTINUITY                 (103)
#define IVIDMM_VAL_TEMP_F                     (109)
#define IVIDMM_VAL_TEMP_C                     (108)
#define IVIDMM_VAL_SIEMENS                    (110)
#define IVIDMM_VAL_COULOMBS                   (111)
    
        /*- IVIDMM_ATTR_RESOLUTION values -*/
#define IVIDMM_VAL_3_5_DIGITS                 (3.5)
#define IVIDMM_VAL_4_DIGITS                   (4.0)
#define IVIDMM_VAL_4_5_DIGITS                 (4.5)
#define IVIDMM_VAL_5_DIGITS                   (5.0)
#define IVIDMM_VAL_5_5_DIGITS                 (5.5)
#define IVIDMM_VAL_6_DIGITS                   (6.0)
#define IVIDMM_VAL_6_5_DIGITS                 (6.5)
#define IVIDMM_VAL_7_DIGITS                   (7.0)
#define IVIDMM_VAL_7_5_DIGITS                 (7.5)

        /*- IVIDMM_ATTR_TRIGGER_SOURCE values -*/
#define IVIDMM_VAL_GPIB_GET                   (101L)
#define IVIDMM_VAL_SW_TRIG_FUNC               (3L)

        /*- IVIDMM_ATTR_POWERLINE_FREQ values -*/
#define IVIDMM_VAL_50_HERTZ                   (50.0)
#define IVIDMM_VAL_60_HERTZ                   (60.0)
#define IVIDMM_VAL_400_HERTZ                  (400.0)

        /*- IVIDMM_ATTR_TRIGGER_POLARITY values -*/
#define IVIDMM_VAL_POS                        IVIDMM_VAL_POSITIVE
#define IVIDMM_VAL_NEG                        IVIDMM_VAL_NEGATIVE

    /*- Obsolete error and completion code values -*/
#define IVIDMM_ERROR_ACCURACY_UNKNOWN                       (IVI_CLASS_ERROR_BASE + 1)
#define IVIDMM_ERROR_ACCURACY_UNKNOWN_WHILE_AUTORANGING     (IVI_CLASS_ERROR_BASE + 2)

#define IVIDMM_ERRMSG_ACCURACY_UNKNOWN                      "The accuracy is unknown or not specified."
#define IVIDMM_ERRMSG_ACCURACY_UNKNOWN_WHILE_AUTORANGING    "The accuracy could not be determined while the DMM was autoranging." 

    /*- Obsolete Error Information Functions -*/
ViStatus _VI_FUNC IviDmm_GetErrorInfo (ViSession vi, 
                                       ViStatus *primaryError, 
                                       ViStatus *secondaryError, 
                                       ViChar errorElaboration[IVI_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC IviDmm_ClearErrorInfo (ViSession vi);

    /*- Obsolete functions -*/

ViStatus _VI_FUNC   IviDmm_Configure           (ViSession vi, ViInt32 measFunction, ViReal64 range, 
                                                ViReal64 resolution, ViReal64 acMinFreq, ViReal64 acMaxFreq);
ViStatus _VI_FUNC   IviDmm_SendSWTrigger       (ViSession vi);
ViStatus _VI_FUNC   IviDmm_CalculateAccuracy   (ViSession vi, ViReal64 freqOfInterest, 
                                                ViReal64 *readingMultiplier, ViReal64 *offset);


/*****************************************************************************
 *---------------------------- End Include File -----------------------------*
 *****************************************************************************/

#endif /* __IVIDMM_HEADER_OBSOLETE */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviDownconverter_ni.h sha256=81dec8b590bcab213a2c7ce36a935785f8ce8623316d8264f2967a30d94a4af4 bytes=33921 -->
## FILE: imports/include/IviDownconverter_ni.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviDownconverter_ni.h`
- sha256: `81dec8b590bcab213a2c7ce36a935785f8ce8623316d8264f2967a30d94a4af4`
- bytes: 33921

````c
/****************************************************************************
 *                              IVI - DOWNCONVERTER                               
 *---------------------------------------------------------------------------
 *    Copyright (c) 2009-2020 National Instruments.  All Rights Reserved.        
 *---------------------------------------------------------------------------
 *                                                                          
 * Title:       ividownconverter_ni.h                                                    
 * Purpose:     IviDownconverter Class declarations for the Base and Extended  
 *              IviDownconverter Capabilities.                                        
 ****************************************************************************/

#ifndef IVIDOWNCONVERTER_HEADER
#define IVIDOWNCONVERTER_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVIDOWNCONVERTER_MAJOR_VERSION                (4L)
#define IVIDOWNCONVERTER_MINOR_VERSION                (0L)

#define IVIDOWNCONVERTER_CLASS_SPEC_MAJOR_VERSION     (2L)
#define IVIDOWNCONVERTER_CLASS_SPEC_MINOR_VERSION     (0L)

#define IVIDOWNCONVERTER_DRIVER_VENDOR                "National Instruments"
#ifdef	_IVI_mswin64_
#define IVIDOWNCONVERTER_DRIVER_DESCRIPTION           "IviDownconverter Class Driver [Compiled for 64-bit.]"
#else
#define IVIDOWNCONVERTER_DRIVER_DESCRIPTION           "IviDownconverter Class Driver"
#endif

/****************************************************************************
 *------------------------------ Useful Macros -----------------------------*
 ****************************************************************************/

  
/****************************************************************************
 *---------------- IviDownconverter Class Attribute Defines ----------------*
 ****************************************************************************/

    /*- IVI Inherent Attributes -*/

        /*- User Options -*/
#define IVIDOWNCONVERTER_ATTR_CACHE                     IVI_ATTR_CACHE                       /* ViBoolean */
#define IVIDOWNCONVERTER_ATTR_RANGE_CHECK               IVI_ATTR_RANGE_CHECK                 /* ViBoolean */
#define IVIDOWNCONVERTER_ATTR_QUERY_INSTRUMENT_STATUS   IVI_ATTR_QUERY_INSTRUMENT_STATUS     /* ViBoolean */
#define IVIDOWNCONVERTER_ATTR_RECORD_COERCIONS          IVI_ATTR_RECORD_COERCIONS            /* ViBoolean */
#define IVIDOWNCONVERTER_ATTR_SIMULATE                  IVI_ATTR_SIMULATE                    /* ViBoolean */
#define IVIDOWNCONVERTER_ATTR_INTERCHANGE_CHECK         IVI_ATTR_INTERCHANGE_CHECK           /* ViBoolean */
#define IVIDOWNCONVERTER_ATTR_SPY                       IVI_ATTR_SPY                         /* ViBoolean */
#define IVIDOWNCONVERTER_ATTR_USE_SPECIFIC_SIMULATION   IVI_ATTR_USE_SPECIFIC_SIMULATION     /* ViBoolean */

        /*- Instrument Capabilities -*/
#define IVIDOWNCONVERTER_ATTR_GROUP_CAPABILITIES        IVI_ATTR_GROUP_CAPABILITIES          /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_FUNCTION_CAPABILITIES     IVI_ATTR_FUNCTION_CAPABILITIES       /* ViString, read-only */

        /*- Class Driver Information -*/    
#define IVIDOWNCONVERTER_ATTR_CLASS_DRIVER_PREFIX                     IVI_ATTR_CLASS_DRIVER_PREFIX         			  /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_CLASS_DRIVER_VENDOR                     IVI_ATTR_CLASS_DRIVER_VENDOR         			  /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_CLASS_DRIVER_DESCRIPTION                IVI_ATTR_CLASS_DRIVER_DESCRIPTION    			  /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION   IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIDOWNCONVERTER_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION   IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Specific Driver Information -*/    
#define IVIDOWNCONVERTER_ATTR_SPECIFIC_DRIVER_PREFIX                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX      				 /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_SPECIFIC_DRIVER_LOCATOR                     IVI_ATTR_SPECIFIC_DRIVER_LOCATOR     				 /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_IO_RESOURCE_DESCRIPTOR                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR      				 /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_LOGICAL_NAME                                IVI_ATTR_LOGICAL_NAME                				 /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_SPECIFIC_DRIVER_VENDOR                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR      				 /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_SPECIFIC_DRIVER_DESCRIPTION                 IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION 				 /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIDOWNCONVERTER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/    
#define IVIDOWNCONVERTER_ATTR_INSTRUMENT_FIRMWARE_REVISION     IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_INSTRUMENT_MANUFACTURER          IVI_ATTR_INSTRUMENT_MANUFACTURER      /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_INSTRUMENT_MODEL                 IVI_ATTR_INSTRUMENT_MODEL             /* ViString, read-only */
#define IVIDOWNCONVERTER_ATTR_SUPPORTED_INSTRUMENT_MODELS      IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS	 /* ViString, read-only */

        /*- Version Information -*/
#define IVIDOWNCONVERTER_ATTR_CLASS_DRIVER_REVISION            IVI_ATTR_CLASS_DRIVER_REVISION        /* ViString, read-only */

#define IVIDOWNCONVERTER_ATTR_SPECIFIC_DRIVER_REVISION         IVI_ATTR_SPECIFIC_DRIVER_REVISION     /* ViString, read-only */

        /*- Driver Setup Information -*/
#define IVIDOWNCONVERTER_ATTR_DRIVER_SETUP              	   IVI_ATTR_DRIVER_SETUP                 /* ViString */

    /*- IviDownconverter Fundamental Attributes -*/
#define IVIDOWNCONVERTER_ATTR_IF_OUTPUT_COUNT                  			(IVI_CLASS_PUBLIC_ATTR_BASE + 4L)    /* ViInt32,  read-only */
#define IVIDOWNCONVERTER_ATTR_RF_INPUT_FREQUENCY			            (IVI_CLASS_PUBLIC_ATTR_BASE + 12L)   /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_RF_INPUT_COUPLING							(IVI_CLASS_PUBLIC_ATTR_BASE + 10L)	 /* ViInt32  */	
#define IVIDOWNCONVERTER_ATTR_RF_INPUT_COUNT						    (IVI_CLASS_PUBLIC_ATTR_BASE + 11L)	 /* ViInt32,  read-only */
#define IVIDOWNCONVERTER_ATTR_ACTIVE_RF_INPUT							(IVI_CLASS_PUBLIC_ATTR_BASE + 1L)	 /* ViString */
#define IVIDOWNCONVERTER_ATTR_ACTIVE_IF_OUTPUT							(IVI_CLASS_PUBLIC_ATTR_BASE + 0L)	 /* ViString */	
#define IVIDOWNCONVERTER_ATTR_IF_OUTPUT_FREQUENCY						(IVI_CLASS_PUBLIC_ATTR_BASE + 6L)	 /* ViReal64, read-only */ 
#define IVIDOWNCONVERTER_ATTR_IF_OUTPUT_ENABLED							(IVI_CLASS_PUBLIC_ATTR_BASE + 5L)	 /* ViBoolean*/
#define IVIDOWNCONVERTER_ATTR_IF_OUTPUT_GAIN							(IVI_CLASS_PUBLIC_ATTR_BASE + 7L)	 /* ViReal64 */	 
#define IVIDOWNCONVERTER_ATTR_RF_INPUT_ATTENUATION						(IVI_CLASS_PUBLIC_ATTR_BASE + 9L)	 /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_RF_INPUT_CORRECTIONS_ENABLED				(IVI_CLASS_PUBLIC_ATTR_BASE + 340L)	 /* ViBoolean*/
#define IVIDOWNCONVERTER_ATTR_IS_SETTLED								(IVI_CLASS_PUBLIC_ATTR_BASE + 8L)	 /* ViBoolean,read-only */
#define IVIDOWNCONVERTER_ATTR_EXTERNAL_LO_ENABLED						(IVI_CLASS_PUBLIC_ATTR_BASE + 2L)	 /* ViBoolean*/
#define IVIDOWNCONVERTER_ATTR_EXTERNAL_LO_FREQUENCY						(IVI_CLASS_PUBLIC_ATTR_BASE + 3L)	 /* ViReal64 */	

    /*- IviDownconverterBypass Attributes -*/
#define IVIDOWNCONVERTER_ATTR_BYPASS									(IVI_CLASS_PUBLIC_ATTR_BASE + 100L)	 /* ViBoolean*/	

    /*- IviDownconverterExternalMixer Attributes -*/
#define IVIDOWNCONVERTER_ATTR_EXTERNAL_MIXER_ENABLED					(IVI_CLASS_PUBLIC_ATTR_BASE + 110L)	 /*	ViBoolean*/
#define IVIDOWNCONVERTER_ATTR_EXTERNAL_MIXER_BIAS_LEVEL					(IVI_CLASS_PUBLIC_ATTR_BASE + 111L)	 /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_EXTERNAL_MIXER_BIAS_LIMIT					(IVI_CLASS_PUBLIC_ATTR_BASE + 112L)	 /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_EXTERNAL_MIXER_BIAS_ENABLED				(IVI_CLASS_PUBLIC_ATTR_BASE + 113L)	 /* ViBoolean*/
#define IVIDOWNCONVERTER_ATTR_EXTERNAL_MIXER_HARMONIC					(IVI_CLASS_PUBLIC_ATTR_BASE + 114L)	 /* ViInt32  */
#define IVIDOWNCONVERTER_ATTR_EXTERNAL_MIXER_NUMBER_OF_PORTS			(IVI_CLASS_PUBLIC_ATTR_BASE + 115L)	 /* ViInt32  */

    /*- IviDownconverterFrequencyStep Attributes -*/
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_STEP_START						(IVI_CLASS_PUBLIC_ATTR_BASE + 204L)	 /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_STEP_STOP						(IVI_CLASS_PUBLIC_ATTR_BASE + 205L)	 /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_STEP_SIZE						(IVI_CLASS_PUBLIC_ATTR_BASE + 203L)	 /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_STEP_DWELL						(IVI_CLASS_PUBLIC_ATTR_BASE + 200L)	 /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_STEP_SINGLE_STEP_ENABLED		(IVI_CLASS_PUBLIC_ATTR_BASE + 202L)	 /* ViBoolean*/
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_STEP_SCALING					(IVI_CLASS_PUBLIC_ATTR_BASE + 201L)	 /* ViInt32  */

    /*- IviDownconverterFrequencySweep Attributes -*/
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_SWEEP_START				        (IVI_CLASS_PUBLIC_ATTR_BASE + 211L)  /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_SWEEP_STOP						(IVI_CLASS_PUBLIC_ATTR_BASE + 212L)	 /* ViReal64 */	
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_SWEEP_TIME						(IVI_CLASS_PUBLIC_ATTR_BASE + 213L)	 /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_SWEEP_TRIGGER_SOURCE			(IVI_CLASS_PUBLIC_ATTR_BASE + 214L)	 /* ViString */	
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_SWEEP_MODE						(IVI_CLASS_PUBLIC_ATTR_BASE + 210L)	 /* ViInt32  */
#define IVIDOWNCONVERTER_ATTR_IS_SWEEPING								(IVI_CLASS_PUBLIC_ATTR_BASE + 215L)	 /* ViBoolean,read-only */	

    /*- IviDownconverterFrequencySweepList Attributes -*/
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_SWEEP_LIST_SELECTED_NAME		(IVI_CLASS_PUBLIC_ATTR_BASE + 221L)	 /* ViString */
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_SWEEP_LIST_DWELL				(IVI_CLASS_PUBLIC_ATTR_BASE + 220L)	 /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_FREQUENCY_SWEEP_LIST_SINGLE_STEP_ENABLED	(IVI_CLASS_PUBLIC_ATTR_BASE + 222L)	 /* ViBoolean*/

    /*- IviDownconverterBandCrossingInformation Attributes -*/
#define IVIDOWNCONVERTER_ATTR_NUM_BANDS									(IVI_CLASS_PUBLIC_ATTR_BASE + 300L)	 /* ViInt32,  read-only */

    /*- IviDownconverterIFFilter Attributes -*/
#define IVIDOWNCONVERTER_ATTR_IF_OUTPUT_FILTER_BANDWIDTH				(IVI_CLASS_PUBLIC_ATTR_BASE + 310L)	 /* ViReal64 */

    /*- IviDownconverterPreselector Attributes -*/
#define IVIDOWNCONVERTER_ATTR_PRESELECTOR_ENABLED						(IVI_CLASS_PUBLIC_ATTR_BASE + 320L)	 /* ViBoolean*/

    /*- IviDownconverterVideoDetectorBandwidth Attributes -*/
#define IVIDOWNCONVERTER_ATTR_IF_OUTPUT_VIDEO_DETECTOR_BANDWIDTH		(IVI_CLASS_PUBLIC_ATTR_BASE + 330L)	 /* ViReal64 */	

    /*- IviDownconverterReferenceOscillator Attributes -*/
#define IVIDOWNCONVERTER_ATTR_REFERENCE_OSCILLATOR_EXTERNAL_FREQUENCY	(IVI_CLASS_PUBLIC_ATTR_BASE + 341L)  /* ViReal64 */
#define IVIDOWNCONVERTER_ATTR_REFERENCE_OSCILLATOR_SOURCE	            (IVI_CLASS_PUBLIC_ATTR_BASE + 342L)  /* ViInt32  */
#define IVIDOWNCONVERTER_ATTR_REFERENCE_OSCILLATOR_OUTPUT_ENABLED		(IVI_CLASS_PUBLIC_ATTR_BASE + 343L)	 /* ViBoolean*/

/****************************************************************************
 *--------------- IviDownconverter Class Attribute Value Defines -----------*
 ****************************************************************************/

    /*- Defined values for attribute IVIDOWNCONVERTER_ATTR_FREQUENCY_STEP_SCALING -*/
#define IVIDOWNCONVERTER_VAL_FREQUENCY_STEP_SCALING_LINEAR                     (0L)
#define IVIDOWNCONVERTER_VAL_FREQUENCY_STEP_SCALING_LOGARITHMIC                (1L)

#define IVIDOWNCONVERTER_VAL_FREQUENCY_STEP_SCALING_CLASS_EXT_BASE			   (100L)
#define IVIDOWNCONVERTER_VAL_FREQUENCY_STEP_SCALING_SPECIFIC_EXT_BASE		   (1000L)

    /*- Defined values for attribute IVIDOWNCONVERTER_ATTR_FREQUENCY_SWEEP_MODE -*/
#define IVIDOWNCONVERTER_VAL_FREQUENCY_SWEEP_MODE_NONE						   (0L)
#define IVIDOWNCONVERTER_VAL_FREQUENCY_SWEEP_MODE_SWEEP			               (1L)
#define IVIDOWNCONVERTER_VAL_FREQUENCY_SWEEP_MODE_STEP						   (2L)
#define IVIDOWNCONVERTER_VAL_FREQUENCY_SWEEP_MODE_LIST						   (3L)

#define IVIDOWNCONVERTER_VAL_FREQUENCY_SWEEP_MODE_CLASS_EXT_BASE			   (100L)
#define IVIDOWNCONVERTER_VAL_FREQUENCY_SWEEP_MODE_SPECIFIC_EXT_BASE			   (1000L)

    /*- Defined values for attribute IVIDOWNCONVERTER_ATTR_FREQUENCY_SWEEP_TRIGGER_SOURCE -*/
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_NONE							   ""
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_IMMEDIATE						   "Immediate"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_EXTERNAL						   "External"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_INTERNAL						   "Internal"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_SOFTWARE						   "Software"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LAN0							   "LAN0"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LAN1							   "LAN1"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LAN2							   "LAN2"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LAN3							   "LAN3"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LAN4							   "LAN4"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LAN5							   "LAN5"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LAN6							   "LAN6"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LAN7							   "LAN7"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LXI0							   "LXI0"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LXI1							   "LXI1"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LXI2							   "LXI2"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LXI3							   "LXI3"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LXI4							   "LXI4"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LXI5							   "LXI5"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LXI6							   "LXI6"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_LXI7							   "LXI7"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_TTL0							   "TTL0"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_TTL1							   "TTL1"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_TTL2							   "TTL2"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_TTL3							   "TTL3"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_TTL4							   "TTL4"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_TTL5							   "TTL5"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_TTL6							   "TTL6"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_TTL7							   "TTL7"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXI_STAR						   "PXI_STAR"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG0						   "PXI_TRIG0"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG1						   "PXI_TRIG1"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG2						   "PXI_TRIG2"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG3						   "PXI_TRIG3"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG4						   "PXI_TRIG4"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG5						   "PXI_TRIG5"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG6						   "PXI_TRIG6"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG7						   "PXI_TRIG7"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXIE_DSTARA						   "PXIe_DSTARA"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXIE_DSTARB						   "PXIe_DSTARB"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_PXIE_DSTARC						   "PXIe_DSTARC"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_RTSI0							   "RTSI0"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_RTSI1							   "RTSI1"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_RTSI2							   "RTSI2"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_RTSI3							   "RTSI3"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_RTSI4							   "RTSI4"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_RTSI5							   "RTSI5"
#define IVIDOWNCONVERTER_VAL_TRIGGER_SOURCE_RTSI6							   "RTSI6"

    /*- Defined values for attribute IVIDOWNCONVERTER_ATTR_REFERENCE_OSCILLATOR_SOURCE -*/
#define IVIDOWNCONVERTER_VAL_REFERENCE_OSCILLATOR_SOURCE_INTERNAL              (0L)
#define IVIDOWNCONVERTER_VAL_REFERENCE_OSCILLATOR_SOURCE_EXTERNAL              (1L)

#define IVIDOWNCONVERTER_VAL_REFERENCE_OSCILLATOR_SOURCE_CLASS_EXT_BASE		   (100L)
#define IVIDOWNCONVERTER_VAL_REFERENCE_OSCILLATOR_SOURCE_SPECIFIC_EXT_BASE	   (1000L)

    /*- Defined values for attribute IVIDOWNCONVERTER_ATTR_RF_INPUT_COUPLING -*/
#define IVIDOWNCONVERTER_VAL_INPUT_COUPLING_AC			                       (0L)
#define IVIDOWNCONVERTER_VAL_INPUT_COUPLING_DC                       		   (1L)

#define IVIDOWNCONVERTER_VAL_RF_INPUT_COUPLING_CLASS_EXT_BASE				   (100L)
#define IVIDOWNCONVERTER_VAL_RF_INPUT_COUPLING_SPECIFIC_EXT_BASE			   (1000L)

#define IVIDOWNCONVERTER_VAL_CALIBRATION_COMPLETE   						   (0L)
#define IVIDOWNCONVERTER_VAL_CALIBRATION_IN_PROGRESS						   (1L)
#define IVIDOWNCONVERTER_VAL_CALIBRATION_STATUS_UNKNOWN						   (2L)
#define IVIDOWNCONVERTER_VAL_CALIBRATION_FAILED         					   (3L)

#define IVIDOWNCONVERTER_VAL_CALIBRATED										   (0L)
#define IVIDOWNCONVERTER_VAL_UNCALIBRATED									   (1L)
#define IVIDOWNCONVERTER_VAL_CALIBRATED_STATUS_UNKNOWN						   (2L)

#define IVIDOWNCONVERTER_VAL_MAX_TIME_IMMEDIATE								   (IVI_VAL_MAX_TIME_IMMEDIATE)
#define IVIDOWNCONVERTER_VAL_MAX_TIME_INFINITE								   (IVI_VAL_MAX_TIME_INFINITE)

/****************************************************************************
 *------- IviDownconverter Class Instrument Driver Function Declarations ---*
 ****************************************************************************/
    /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviDownconverter_init (ViRsrc logicalName, 
                               			 ViBoolean idQuery, 
                               			 ViBoolean resetDevice, 
                               			 ViSession *vi);

ViStatus _VI_FUNC IviDownconverter_close (ViSession vi);

ViStatus _VI_FUNC IviDownconverter_reset (ViSession vi);

ViStatus _VI_FUNC IviDownconverter_self_test (ViSession vi, 
                                    		  ViInt16 *selfTestResult, 
                                    		  ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviDownconverter_error_query (ViSession vi, 
                                      			ViInt32 *errorCode, 
                                      			ViChar errorMessage[]);

ViStatus _VI_FUNC IviDownconverter_error_message (ViSession vi, 
                                        		  ViStatus statusCode, 
                                        		  ViChar message[]);

ViStatus _VI_FUNC IviDownconverter_revision_query (ViSession vi, 
                                         		   ViChar driverRev[], 
                                         		   ViChar instrRev[]);

    /*- Utility Functions -*/
ViStatus _VI_FUNC IviDownconverter_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviDownconverter_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviDownconverter_Disable (ViSession vi);

    /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviDownconverter_InitWithOptions (ViRsrc logicalName, 
                                          			ViBoolean IDQuery,
                                          			ViBoolean resetDevice, 
                                          			ViConstString optionString, 
                                          			ViSession *vi);

    /*- Set, Get, and Check Attribute Functions -*/
ViStatus _VI_FUNC IviDownconverter_GetAttributeViInt32 (ViSession vi, 
                                              			ViConstString channelName,
                                              			ViAttr attributeId,
                                              			ViInt32 *value);

ViStatus _VI_FUNC IviDownconverter_SetAttributeViInt32 (ViSession vi, 
                                              			ViConstString channelName,
                                              			ViAttr attributeId,
                                              			ViInt32 value);

ViStatus _VI_FUNC IviDownconverter_CheckAttributeViInt32 (ViSession vi, 
                                                		  ViConstString channelName,
                                                		  ViAttr attributeId,
                                                		  ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviDownconverter_GetAttributeViInt64 (ViSession vi, 
                                              			ViConstString channelName,
                                              			ViAttr attributeId,
                                              			ViInt64 *value);

ViStatus _VI_FUNC IviDownconverter_SetAttributeViInt64 (ViSession vi, 
                                              			ViConstString channelName,
                                              			ViAttr attributeId,
                                              			ViInt64 value);

ViStatus _VI_FUNC IviDownconverter_CheckAttributeViInt64 (ViSession vi, 
                                                		  ViConstString channelName,
                                                		  ViAttr attributeId,
                                                		  ViInt64 value);
#endif

ViStatus _VI_FUNC IviDownconverter_GetAttributeViReal64 (ViSession vi, 
                                               			 ViConstString channelName, 
                                               			 ViAttr attributeId, 
                                               			 ViReal64 *value);

ViStatus _VI_FUNC IviDownconverter_SetAttributeViReal64 (ViSession vi, 
                                               			 ViConstString channelName, 
                                               			 ViAttr attributeId, 
                                               			 ViReal64 value);

ViStatus _VI_FUNC IviDownconverter_CheckAttributeViReal64 (ViSession vi, 
                                                 		   ViConstString channelName, 
                                                 		   ViAttr attributeId, 
                                                 		   ViReal64 value);

ViStatus _VI_FUNC IviDownconverter_GetAttributeViString (ViSession vi, 
                                               			 ViConstString channelName, 
                                               			 ViAttr attributeId, 
                                               			 ViInt32 bufferSize, 
                                               			 ViChar value[]);

ViStatus _VI_FUNC IviDownconverter_SetAttributeViString (ViSession vi, 
                                               			 ViConstString channelName, 
                                               			 ViAttr attributeId, 
                                               			 ViConstString value);

ViStatus _VI_FUNC IviDownconverter_CheckAttributeViString (ViSession vi, 
                                                 		   ViConstString channelName, 
                                                 		   ViAttr attributeId, 
                                                 		   ViConstString value); 

ViStatus _VI_FUNC IviDownconverter_GetAttributeViBoolean (ViSession vi, 
                                                		  ViConstString channelName, 
                                                		  ViAttr attributeId, 
                                                		  ViBoolean *value);

ViStatus _VI_FUNC IviDownconverter_SetAttributeViBoolean (ViSession vi, 
                                                		  ViConstString channelName, 
                                                		  ViAttr attributeId, 
                                                		  ViBoolean value);

ViStatus _VI_FUNC IviDownconverter_CheckAttributeViBoolean (ViSession vi, 
                                                  			ViConstString channelName, 
                                                  			ViAttr attributeId, 
                                                  			ViBoolean value);

ViStatus _VI_FUNC IviDownconverter_GetAttributeViSession (ViSession vi, 
                                                		  ViConstString channelName, 
                                                		  ViAttr attributeId, 
                                                		  ViSession *value);

ViStatus _VI_FUNC IviDownconverter_SetAttributeViSession (ViSession vi, 
                                                		  ViConstString channelName, 
                                                		  ViAttr attributeId, 
                                                		  ViSession value);

ViStatus _VI_FUNC IviDownconverter_CheckAttributeViSession (ViSession vi, 
                                                  			ViConstString channelName, 
                                                  			ViAttr attributeId, 
                                                  			ViSession value);

    /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviDownconverter_LockSession (ViSession vi, 
                                      			ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviDownconverter_UnlockSession (ViSession vi, 
                                        		  ViBoolean *callerHasLock);

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviDownconverter_GetError (ViSession vi, 
                                   			 ViStatus *errorCode, 
                                   			 ViInt32 bufferSize, 
                                   			 ViChar description[]);

ViStatus _VI_FUNC IviDownconverter_ClearError (ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviDownconverter_GetNextInterchangeWarning (ViSession vi, 
                                                    		  ViInt32 bufferSize,
                                                    		  ViChar warning[]);

ViStatus _VI_FUNC IviDownconverter_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviDownconverter_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviDownconverter_GetNextCoercionRecord (ViSession vi,
                                                		  ViInt32 bufferSize, 
                                                		  ViChar record[]);

ViStatus _VI_FUNC IviDownconverter_GetSpecificDriverCHandle (ViSession vi,
                                                   			 ViSession* specificDriverCHandle);	

    /*- IviDownconverterBase Functions -*/
ViStatus _VI_FUNC   IviDownconverter_ConfigureIFOutputEnabled (ViSession vi, 
                                                 			   ViBoolean enabled);

ViStatus _VI_FUNC   IviDownconverter_ConfigureIFOutputGain (ViSession vi, 
															ViReal64 gain);

ViStatus _VI_FUNC   IviDownconverter_GetIFOutputName (ViSession vi, 
													  ViInt32 index,
													  ViInt32 nameBufferSize,
													  ViChar name[]);

ViStatus _VI_FUNC   IviDownconverter_SetActiveIFOutput (ViSession vi, 
														ViConstString name);

ViStatus _VI_FUNC   IviDownconverter_ConfigureRFInputAttenuation (ViSession vi, 
																  ViReal64 attenuation);

ViStatus _VI_FUNC   IviDownconverter_ConfigureRFInputFrequency (ViSession vi, 
																ViReal64 frequency);

ViStatus _VI_FUNC	IviDownconverter_GetRFInputName (ViSession vi, 
													 ViInt32 index,
												     ViInt32 nameBufferSize,
												     ViChar name[]);

ViStatus _VI_FUNC	IviDownconverter_SetActiveRFInput (ViSession vi,
													   ViConstString name);

ViStatus _VI_FUNC	IviDownconverter_WaitUntilSettled (ViSession vi,
													   ViInt32 maxTimeMilliseconds);

    /*- IviDownconverterBypass Functions -*/
ViStatus _VI_FUNC   IviDownconverter_ConfigureBypass (ViSession vi, 
													  ViBoolean bypass);
    
    /*- IviDownconverterExternalMixer Functions -*/
ViStatus _VI_FUNC   IviDownconverter_ConfigureExternalMixerBias (ViSession vi, 
																 ViReal64 bias, 
															     ViReal64 biasLimit);

    /*- IviDownconverterFrequencyStep Functions -*/
ViStatus _VI_FUNC   IviDownconverter_ConfigureFrequencyStepDwell (ViSession vi, 
																  ViBoolean singleStepEnabled, 
																  ViReal64 dwell);

ViStatus _VI_FUNC	IviDownconverter_ConfigureFrequencyStepStartStop (ViSession vi,
																	  ViReal64 start,
																	  ViReal64 stop,
																	  ViInt32 scaling,
																	  ViReal64 stepSize);

ViStatus _VI_FUNC	IviDownconverter_ResetFrequencyStep (ViSession vi);

    /*- IviDownconverterFrequencySweep Functions -*/
ViStatus _VI_FUNC   IviDownconverter_ConfigureFrequencySweep (ViSession vi, 
															  ViInt32 mode,
															  ViConstString triggerSource);

ViStatus _VI_FUNC   IviDownconverter_ConfigureFrequencySweepStartStop (ViSession vi, 
																	   ViReal64 start,
																	   ViReal64 stop);

ViStatus _VI_FUNC	IviDownconverter_ConfigureFrequencySweepTime (ViSession vi,
																  ViReal64 sweepTime);

ViStatus _VI_FUNC	IviDownconverter_WaitUntilFrequencySweepComplete (ViSession vi,
																	  ViInt32 maxTimeMilliseconds);

    /*- IviDownconverterFrequencySweepList Functions -*/
ViStatus _VI_FUNC   IviDownconverter_ClearAllFrequencySweepLists (ViSession vi);

ViStatus _VI_FUNC	IviDownconverter_ConfigureFrequencySweepListDwell (ViSession vi,
																	   ViBoolean singleStepEnabled,
																	   ViReal64 dwell);

ViStatus _VI_FUNC	IviDownconverter_CreateFrequencySweepList (ViSession vi,
															   ViConstString name,
															   ViInt32 frequencyListBufferSize,
															   ViReal64 frequencyList[]);

ViStatus _VI_FUNC	IviDownconverter_ResetFrequencySweepList (ViSession vi);

    /*- IviDownconverterBandCrossingInformation Functions -*/
ViStatus _VI_FUNC   IviDownconverter_GetBandCrossingInfo (ViSession vi, 
														  ViInt32 bufferSize,
														  ViReal64 startFrequencies[],
														  ViReal64 stopFrequencies[],
														  ViInt32* actualNumFrequencies);

    /*- IviDownconverterSoftwareTrigger Functions -*/
ViStatus _VI_FUNC   IviDownconverter_SendSoftwareTrigger (ViSession vi);

    /*- IviDownconverterIFFilter Functions -*/
ViStatus _VI_FUNC   IviDownconverter_ConfigureIFOutputFilterBandwidth (ViSession vi, 
																	   ViReal64 bandwidth);

    /*- IviDownconverterPreselector Functions -*/
ViStatus _VI_FUNC   IviDownconverter_ConfigurePreselectorEnabled (ViSession vi, 
																  ViBoolean enabled);

    /*- IviDownconverterVideoDetectorBandwidth Functions -*/
ViStatus _VI_FUNC   IviDownconverter_ConfigureIFOutputVideoDetectorBandwidth (ViSession vi, 
																			  ViReal64 bandwidth);

    /*- IviDownconverterCalibration Functions -*/
ViStatus _VI_FUNC   IviDownconverter_Calibrate (ViSession vi);

ViStatus _VI_FUNC	IviDownconverter_IsCalibrationComplete (ViSession vi,
															ViInt32* status);

ViStatus _VI_FUNC	IviDownconverter_IsCalibrated (ViSession vi,
												   ViInt32* status);

	/*- IviDownconverterReferenceOscillator Functions -*/
ViStatus _VI_FUNC   IviDownconverter_ConfigureReferenceOscillator (ViSession vi, 
																   ViInt32 source,
																   ViReal64 frequency);

ViStatus _VI_FUNC	IviDownconverter_ConfigureReferenceOscillatorOutputEnabled (ViSession vi,
																				ViBoolean enabled);
                                                
/****************************************************************************
 *------------- IviDownconverter Class Error And Completion Codes ----------*
 ****************************************************************************/
#define IVIDOWNCONVERTER_ERROR_FREQUENCY_LIST_UNKNOWN	(IVI_CLASS_ERROR_BASE + 1L) 
#define IVIDOWNCONVERTER_ERROR_MAX_TIME_EXCEEDED      	(IVI_CLASS_ERROR_BASE + 2L)
#define IVIDOWNCONVERTER_ERROR_TRIGGER_NOT_SOFTWARE   	(IVI_CROSS_CLASS_ERROR_BASE + 1L)

#define IVIDOWNCONVERTER_ERRMSG_FREQUENCY_LIST_UNKNOWN	"The selected frequency list is not defined."
#define IVIDOWNCONVERTER_ERRMSG_MAX_TIME_EXCEEDED     	"Maximum time exceeded before operation completed."	
#define IVIDOWNCONVERTER_ERRMSG_TRIGGER_NOT_SOFTWARE  	"The trigger source is not set to software trigger."

#define IVIDOWNCONVERTER_ERROR_CODES_AND_MSGS \
        {IVIDOWNCONVERTER_ERROR_FREQUENCY_LIST_UNKNOWN, IVIDOWNCONVERTER_ERRMSG_FREQUENCY_LIST_UNKNOWN}, \
        {IVIDOWNCONVERTER_ERROR_MAX_TIME_EXCEEDED,    	IVIDOWNCONVERTER_ERRMSG_MAX_TIME_EXCEEDED	  }, \
        {IVIDOWNCONVERTER_ERROR_TRIGGER_NOT_SOFTWARE, 	IVIDOWNCONVERTER_ERRMSG_TRIGGER_NOT_SOFTWARE  } 

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}                                                    
#endif

#endif /* IVIDOWNCONVERTER_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviFgen.h sha256=147eff96eef107ded4591cca686c1513e970776b94edfd18a509f33c4dd1e425 bytes=51320 -->
## FILE: imports/include/IviFgen.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviFgen.h`
- sha256: `147eff96eef107ded4591cca686c1513e970776b94edfd18a509f33c4dd1e425`
- bytes: 51320

````c
/******************************************************************************
 *                            I V I - F G E N
 *-----------------------------------------------------------------------------
 *    Copytight (c) 1998-2020 National Instruments.  All Rights Reserved.
 *-----------------------------------------------------------------------------
 *
 * Title:       ivifgen.h
 * Purpose:     IviFgen Class declarations for the Base and Extended
 *              IviFgen Capabilities.
 ******************************************************************************/
 
#ifndef IVIFGEN_HEADER
#define IVIFGEN_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cpluplus__)
extern "C" {
#endif

/******************************************************************************
 *------------------ Instrument Driver Revision Information ------------------*
 ******************************************************************************/

#define IVIFGEN_MAJOR_VERSION               (5L)
#define IVIFGEN_MINOR_VERSION               (0L)

#define IVIFGEN_CLASS_SPEC_MAJOR_VERSION    (5L)
#define IVIFGEN_CLASS_SPEC_MINOR_VERSION    (2L)

#define IVIFGEN_DRIVER_VENDOR               "National Instruments"
#ifdef	_IVI_mswin64_
#define IVIFGEN_DRIVER_DESCRIPTION          "IviFgen Class Driver [Compiled for 64-bit.]"
#else
#define IVIFGEN_DRIVER_DESCRIPTION          "IviFgen Class Driver"
#endif

/******************************************************************************
 *---------------------- IviFgen Class Attribute Defines ---------------------*
 ******************************************************************************/

    /*- IVI Inherent Attributes -*/
        /*- User Options -*/
#define IVIFGEN_ATTR_CACHE                     IVI_ATTR_CACHE                       /* ViBoolean */
#define IVIFGEN_ATTR_RANGE_CHECK               IVI_ATTR_RANGE_CHECK                 /* ViBoolean */
#define IVIFGEN_ATTR_QUERY_INSTRUMENT_STATUS   IVI_ATTR_QUERY_INSTRUMENT_STATUS     /* ViBoolean */
#define IVIFGEN_ATTR_RECORD_COERCIONS          IVI_ATTR_RECORD_COERCIONS            /* ViBoolean */
#define IVIFGEN_ATTR_SIMULATE                  IVI_ATTR_SIMULATE                    /* ViBoolean */
#define IVIFGEN_ATTR_INTERCHANGE_CHECK         IVI_ATTR_INTERCHANGE_CHECK           /* ViBoolean */
#define IVIFGEN_ATTR_SPY                       IVI_ATTR_SPY                         /* ViBoolean */
#define IVIFGEN_ATTR_USE_SPECIFIC_SIMULATION   IVI_ATTR_USE_SPECIFIC_SIMULATION     /* ViBoolean */

        /*- Instrument Capabilities -*/
#define IVIFGEN_ATTR_GROUP_CAPABILITIES        IVI_ATTR_GROUP_CAPABILITIES          /* ViString, read-only */
#define IVIFGEN_ATTR_FUNCTION_CAPABILITIES     IVI_ATTR_FUNCTION_CAPABILITIES       /* ViString, read-only */

        /*- Class Driver Information -*/
#define IVIFGEN_ATTR_CLASS_DRIVER_PREFIX                         IVI_ATTR_CLASS_DRIVER_PREFIX         /* ViString, read-only */
#define IVIFGEN_ATTR_CLASS_DRIVER_VENDOR                         IVI_ATTR_CLASS_DRIVER_VENDOR         /* ViString, read-only */
#define IVIFGEN_ATTR_CLASS_DRIVER_DESCRIPTION                    IVI_ATTR_CLASS_DRIVER_DESCRIPTION    /* ViString, read-only */
#define IVIFGEN_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIFGEN_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Specific Driver Information -*/
#define IVIFGEN_ATTR_SPECIFIC_DRIVER_PREFIX                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX      /* ViString, read-only */
#define IVIFGEN_ATTR_SPECIFIC_DRIVER_LOCATOR                     IVI_ATTR_SPECIFIC_DRIVER_LOCATOR     /* ViString, read-only */
#define IVIFGEN_ATTR_IO_RESOURCE_DESCRIPTOR                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR      /* ViString, read-only */
#define IVIFGEN_ATTR_LOGICAL_NAME                                IVI_ATTR_LOGICAL_NAME                /* ViString, read-only */
#define IVIFGEN_ATTR_SPECIFIC_DRIVER_VENDOR                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR      /* ViString, read-only */
#define IVIFGEN_ATTR_SPECIFIC_DRIVER_DESCRIPTION                 IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION /* ViString, read-only */
#define IVIFGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIFGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/    
#define IVIFGEN_ATTR_INSTRUMENT_FIRMWARE_REVISION     IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION /* ViString, read-only */
#define IVIFGEN_ATTR_INSTRUMENT_MANUFACTURER          IVI_ATTR_INSTRUMENT_MANUFACTURER      /* ViString, read-only */
#define IVIFGEN_ATTR_INSTRUMENT_MODEL                 IVI_ATTR_INSTRUMENT_MODEL             /* ViString, read-only */
#define IVIFGEN_ATTR_SUPPORTED_INSTRUMENT_MODELS      IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS

        /*- Version Information -*/
#define IVIFGEN_ATTR_CLASS_DRIVER_REVISION            IVI_ATTR_CLASS_DRIVER_REVISION              /* ViString, read-only */

#define IVIFGEN_ATTR_SPECIFIC_DRIVER_REVISION         IVI_ATTR_SPECIFIC_DRIVER_REVISION             /* ViString, read-only */

        /*- Driver Setup Information -*/
#define IVIFGEN_ATTR_DRIVER_SETUP                     IVI_ATTR_DRIVER_SETUP                /* ViString */

    /*- IviFgen Fundamental Attributes -*/
#define IVIFGEN_ATTR_CHANNEL_COUNT              IVI_ATTR_CHANNEL_COUNT              /* (ViInt32), read-only */
#define IVIFGEN_ATTR_OUTPUT_MODE                (IVI_CLASS_PUBLIC_ATTR_BASE + 1L)   /* (ViInt32) */
#define IVIFGEN_ATTR_REF_CLOCK_SOURCE           (IVI_CLASS_PUBLIC_ATTR_BASE + 2L)   /* (ViInt32) */
#define IVIFGEN_ATTR_OUTPUT_ENABLED             (IVI_CLASS_PUBLIC_ATTR_BASE + 3L)   /* (ViBoolean,  Multi-Channel) */
#define IVIFGEN_ATTR_OUTPUT_IMPEDANCE           (IVI_CLASS_PUBLIC_ATTR_BASE + 4L)   /* (ViReal64,   Multi-Channel) */
#define IVIFGEN_ATTR_OPERATION_MODE             (IVI_CLASS_PUBLIC_ATTR_BASE + 5L)   /* (ViInt32,    Multi-Channel) */

    /*- IviFgenSampleClock Extended Attributes -*/
#define IVIFGEN_ATTR_SAMPLE_CLOCK_SOURCE         (IVI_CLASS_PUBLIC_ATTR_BASE + 21L)  /* (ViInt32)   */
#define IVIFGEN_ATTR_SAMPLE_CLOCK_OUTPUT_ENABLED (IVI_CLASS_PUBLIC_ATTR_BASE + 22L) /* (ViBoolean) */

    /*- IviFgenTerminalConfiguration Extended Attributes -*/
#define IVIFGEN_ATTR_TERMINAL_CONFIGURATION      (IVI_CLASS_PUBLIC_ATTR_BASE + 31L)  /* (ViInt32,    Multi-Channel) */

    /*- IviFgenStdFunc Extended Attributes -*/
#define IVIFGEN_ATTR_FUNC_WAVEFORM              (IVI_CLASS_PUBLIC_ATTR_BASE + 101L)  /* (ViInt32,  Multi-Channel)   */
#define IVIFGEN_ATTR_FUNC_AMPLITUDE             (IVI_CLASS_PUBLIC_ATTR_BASE + 102L)  /* (ViReal64,  Multi-Channel)  */
#define IVIFGEN_ATTR_FUNC_DC_OFFSET             (IVI_CLASS_PUBLIC_ATTR_BASE + 103L)  /* (ViReal64,  Multi-Channel)  */
#define IVIFGEN_ATTR_FUNC_FREQUENCY             (IVI_CLASS_PUBLIC_ATTR_BASE + 104L)  /* (ViReal64,  Multi-Channel)  */
#define IVIFGEN_ATTR_FUNC_START_PHASE           (IVI_CLASS_PUBLIC_ATTR_BASE + 105L)  /* (ViReal64,  Multi-Channel)  */
#define IVIFGEN_ATTR_FUNC_DUTY_CYCLE_HIGH       (IVI_CLASS_PUBLIC_ATTR_BASE + 106L)  /* (ViReal64,  Multi-Channel)  */

    /*- IviFgenArbWfm Extended Attributes -*/
#define IVIFGEN_ATTR_ARB_WAVEFORM_HANDLE        (IVI_CLASS_PUBLIC_ATTR_BASE + 201L)  /* (ViInt32,  Multi-Channel)   */
#define IVIFGEN_ATTR_ARB_GAIN                   (IVI_CLASS_PUBLIC_ATTR_BASE + 202L)  /* (ViReal64, Multi-Channel)  */
#define IVIFGEN_ATTR_ARB_OFFSET                 (IVI_CLASS_PUBLIC_ATTR_BASE + 203L)  /* (ViReal64, Multi-Channel)  */
#define IVIFGEN_ATTR_ARB_SAMPLE_RATE            (IVI_CLASS_PUBLIC_ATTR_BASE + 204L)  /* (ViReal64)  */

#define IVIFGEN_ATTR_MAX_NUM_WAVEFORMS          (IVI_CLASS_PUBLIC_ATTR_BASE + 205L)  /* (ViInt32, Read-only)   */
#define IVIFGEN_ATTR_WAVEFORM_QUANTUM           (IVI_CLASS_PUBLIC_ATTR_BASE + 206L)  /* (ViInt32, Read-only)   */
#define IVIFGEN_ATTR_MIN_WAVEFORM_SIZE          (IVI_CLASS_PUBLIC_ATTR_BASE + 207L)  /* (ViInt32, Read-only)   */
#define IVIFGEN_ATTR_MAX_WAVEFORM_SIZE          (IVI_CLASS_PUBLIC_ATTR_BASE + 208L)  /* (ViInt32, Read-only)   */

    /*- IviFgenArbFrequency Extended Attributes -*/
#define IVIFGEN_ATTR_ARB_FREQUENCY              (IVI_CLASS_PUBLIC_ATTR_BASE + 209L)  /* (ViReal64, Multi-Channel)  */    

    /*- IviFgenArbSeq Extended Attributes -*/
#define IVIFGEN_ATTR_ARB_SEQUENCE_HANDLE        (IVI_CLASS_PUBLIC_ATTR_BASE + 211L)  /* (ViInt32, Multi-Channel)   */
#define IVIFGEN_ATTR_MAX_NUM_SEQUENCES          (IVI_CLASS_PUBLIC_ATTR_BASE + 212L)  /* (ViInt32, Read-only)   */
#define IVIFGEN_ATTR_MIN_SEQUENCE_LENGTH        (IVI_CLASS_PUBLIC_ATTR_BASE + 213L)  /* (ViInt32, Read-only)   */
#define IVIFGEN_ATTR_MAX_SEQUENCE_LENGTH        (IVI_CLASS_PUBLIC_ATTR_BASE + 214L)  /* (ViInt32, Read-only)   */
#define IVIFGEN_ATTR_MAX_LOOP_COUNT             (IVI_CLASS_PUBLIC_ATTR_BASE + 215L)  /* (ViInt32, Read-only)   */

    /*- IviFgenArbWfmSize64 Extended Attributes -*/
#define IVIFGEN_ATTR_MIN_WAVEFORM_SIZE64        (IVI_CLASS_PUBLIC_ATTR_BASE + 221L)  /* (ViInt64, Read-only)   */
#define IVIFGEN_ATTR_MAX_WAVEFORM_SIZE64        (IVI_CLASS_PUBLIC_ATTR_BASE + 222L)  /* (ViInt64, Read-only)   */

    /*- IviFgenArbWfmBinary Extended Attributes -*/
#define IVIFGEN_ATTR_BINARY_ALIGNMENT           (IVI_CLASS_PUBLIC_ATTR_BASE + 241L)  /* (ViInt32, Read-only)   */
#define	IVIFGEN_ATTR_SAMPLE_BIT_RESOLUTION      (IVI_CLASS_PUBLIC_ATTR_BASE + 242L)  /* (ViInt32, Read-only)   */

    /*- IviFgenArbDataMask Extended Attributes -*/
#define IVIFGEN_ATTR_OUTPUT_DATA_MASK           (IVI_CLASS_PUBLIC_ATTR_BASE + 261L)  /* (ViInt32) */

    /*- IviFgenArbSeqDepth Extended Attributes -*/
#define IVIFGEN_ATTR_SEQUENCE_DEPTH_MAX         (IVI_CLASS_PUBLIC_ATTR_BASE + 281L)  /* (ViInt32, Read-only)   */

    /*- IviFgenTrigger Extended Attributes -*/
#define IVIFGEN_ATTR_TRIGGER_SOURCE             (IVI_CLASS_PUBLIC_ATTR_BASE + 302L)  /* (ViInt32, Multi-Channel)   */

    /*- IviFgenInternalTrigger Extended Attributes -*/
#define IVIFGEN_ATTR_INTERNAL_TRIGGER_RATE      (IVI_CLASS_PUBLIC_ATTR_BASE + 310L)  /* (ViReal64)   */  

    /*- IviFgenStartTrigger Extended Attributes -*/
#define IVIFGEN_ATTR_START_TRIGGER_DELAY        (IVI_CLASS_PUBLIC_ATTR_BASE + 320L)  /* (ViReal64, Multi-Channel)  */
#define IVIFGEN_ATTR_START_TRIGGER_SLOPE        (IVI_CLASS_PUBLIC_ATTR_BASE + 321L)  /* (ViInt32,  Multi-Channel)  */
#define IVIFGEN_ATTR_START_TRIGGER_SOURCE       (IVI_CLASS_PUBLIC_ATTR_BASE + 322L)  /* (ViString, Multi-Channel)  */
#define IVIFGEN_ATTR_START_TRIGGER_THRESHOLD    (IVI_CLASS_PUBLIC_ATTR_BASE + 323L)  /* (ViReal64, Multi-Channel)  */

    /*- IviFgenStopTrigger Extended Attributes -*/
#define IVIFGEN_ATTR_STOP_TRIGGER_DELAY         (IVI_CLASS_PUBLIC_ATTR_BASE + 330L)  /* (ViReal64, Multi-Channel)  */
#define IVIFGEN_ATTR_STOP_TRIGGER_SLOPE         (IVI_CLASS_PUBLIC_ATTR_BASE + 331L)  /* (ViInt32,  Multi-Channel)  */
#define IVIFGEN_ATTR_STOP_TRIGGER_SOURCE        (IVI_CLASS_PUBLIC_ATTR_BASE + 332L)  /* (ViString, Multi-Channel)  */
#define IVIFGEN_ATTR_STOP_TRIGGER_THRESHOLD     (IVI_CLASS_PUBLIC_ATTR_BASE + 333L)  /* (ViReal64, Multi-Channel)  */

    /*- IviFgenHoldTrigger Extended Attributes -*/
#define IVIFGEN_ATTR_HOLD_TRIGGER_DELAY         (IVI_CLASS_PUBLIC_ATTR_BASE + 340L)  /* (ViReal64, Multi-Channel)  */
#define IVIFGEN_ATTR_HOLD_TRIGGER_SLOPE         (IVI_CLASS_PUBLIC_ATTR_BASE + 341L)  /* (ViInt32,  Multi-Channel)  */
#define IVIFGEN_ATTR_HOLD_TRIGGER_SOURCE        (IVI_CLASS_PUBLIC_ATTR_BASE + 342L)  /* (ViString, Multi-Channel)  */
#define IVIFGEN_ATTR_HOLD_TRIGGER_THRESHOLD      (IVI_CLASS_PUBLIC_ATTR_BASE + 343L)  /* (ViReal64, Multi-Channel)  */

    /*- IviFgenBurst Extended Attributes -*/
#define IVIFGEN_ATTR_BURST_COUNT                (IVI_CLASS_PUBLIC_ATTR_BASE + 350L)  /* (ViInt32, Multi-Channel)   */  

    /*- IviFgenResumeTrigger Extended Attributes -*/
#define IVIFGEN_ATTR_RESUME_TRIGGER_DELAY       (IVI_CLASS_PUBLIC_ATTR_BASE + 360L)  /* (ViReal64, Multi-Channel)  */
#define IVIFGEN_ATTR_RESUME_TRIGGER_SLOPE       (IVI_CLASS_PUBLIC_ATTR_BASE + 361L)  /* (ViInt32,  Multi-Channel)  */
#define IVIFGEN_ATTR_RESUME_TRIGGER_SOURCE      (IVI_CLASS_PUBLIC_ATTR_BASE + 362L)  /* (ViString, Multi-Channel)  */
#define IVIFGEN_ATTR_RESUME_TRIGGER_THRESHOLD   (IVI_CLASS_PUBLIC_ATTR_BASE + 363L)  /* (ViReal64, Multi-Channel)  */

    /*- IviFgenAdvanceTrigger Extended Attributes -*/
#define IVIFGEN_ATTR_ADVANCE_TRIGGER_DELAY      (IVI_CLASS_PUBLIC_ATTR_BASE + 370L)  /* (ViReal64, Multi-Channel)  */
#define IVIFGEN_ATTR_ADVANCE_TRIGGER_SLOPE      (IVI_CLASS_PUBLIC_ATTR_BASE + 371L)  /* (ViInt32,  Multi-Channel)  */
#define IVIFGEN_ATTR_ADVANCE_TRIGGER_SOURCE     (IVI_CLASS_PUBLIC_ATTR_BASE + 372L)  /* (ViString, Multi-Channel)  */
#define IVIFGEN_ATTR_ADVANCE_TRIGGER_THRESHOLD  (IVI_CLASS_PUBLIC_ATTR_BASE + 373L)  /* (ViReal64, Multi-Channel)  */

    /*- IviFgenModulateAM Extended Attributes -*/
#define IVIFGEN_ATTR_AM_ENABLED                 (IVI_CLASS_PUBLIC_ATTR_BASE + 401L)  /* (ViBoolean, Multi-Channel) */
#define IVIFGEN_ATTR_AM_SOURCE                  (IVI_CLASS_PUBLIC_ATTR_BASE + 402L)  /* (ViInt32, Multi-Channel)   */
#define IVIFGEN_ATTR_AM_INTERNAL_DEPTH          (IVI_CLASS_PUBLIC_ATTR_BASE + 403L)  /* (ViReal64)  */
#define IVIFGEN_ATTR_AM_INTERNAL_WAVEFORM       (IVI_CLASS_PUBLIC_ATTR_BASE + 404L)  /* (ViInt32)   */
#define IVIFGEN_ATTR_AM_INTERNAL_FREQUENCY      (IVI_CLASS_PUBLIC_ATTR_BASE + 405L)  /* (ViReal64)  */

    /*- IviFgenModulateFM Extended Attributes -*/
#define IVIFGEN_ATTR_FM_ENABLED                 (IVI_CLASS_PUBLIC_ATTR_BASE + 501L)  /* (ViBoolean, Multi-Channel) */
#define IVIFGEN_ATTR_FM_SOURCE                  (IVI_CLASS_PUBLIC_ATTR_BASE + 502L)  /* (ViInt32, Multi-Channel)   */
#define IVIFGEN_ATTR_FM_INTERNAL_DEVIATION      (IVI_CLASS_PUBLIC_ATTR_BASE + 503L)  /* (ViReal64)  */
#define IVIFGEN_ATTR_FM_INTERNAL_WAVEFORM       (IVI_CLASS_PUBLIC_ATTR_BASE + 504L)  /* (ViInt32)   */
#define IVIFGEN_ATTR_FM_INTERNAL_FREQUENCY      (IVI_CLASS_PUBLIC_ATTR_BASE + 505L)  /* (ViReal64)  */

    /*- IviFgenDataMarker Extended Attributes -*/
#define IVIFGEN_ATTR_DATAMARKER_AMPLITUDE       (IVI_CLASS_PUBLIC_ATTR_BASE + 601L)  /* (ViReal64) */
#define IVIFGEN_ATTR_DATAMARKER_BIT_POSITION    (IVI_CLASS_PUBLIC_ATTR_BASE + 602L)  /* (ViInt32)  */
#define IVIFGEN_ATTR_DATAMARKER_COUNT           (IVI_CLASS_PUBLIC_ATTR_BASE + 603L)  /* (ViInt32, Read-only )      */
#define IVIFGEN_ATTR_DATAMARKER_DELAY           (IVI_CLASS_PUBLIC_ATTR_BASE + 604L)  /* (ViReal64) */
#define IVIFGEN_ATTR_DATAMARKER_DESTINATION     (IVI_CLASS_PUBLIC_ATTR_BASE + 605L)  /* (ViString) */
#define IVIFGEN_ATTR_DATAMARKER_POLARITY        (IVI_CLASS_PUBLIC_ATTR_BASE + 606L)  /* (ViInt32)  */
#define IVIFGEN_ATTR_DATAMARKER_SOURCE_CHANNEL  (IVI_CLASS_PUBLIC_ATTR_BASE + 607L)  /* (ViString) */

    /*- IviFgenSparseMarker Extended Attributes -*/
#define IVIFGEN_ATTR_SPARSEMARKER_AMPLITUDE     (IVI_CLASS_PUBLIC_ATTR_BASE + 701L)  /* (ViReal64, Multi-Channel)  */
#define IVIFGEN_ATTR_SPARSEMARKER_COUNT         (IVI_CLASS_PUBLIC_ATTR_BASE + 702L)  /* (ViInt32,  Read-only)      */
#define IVIFGEN_ATTR_SPARSEMARKER_DELAY         (IVI_CLASS_PUBLIC_ATTR_BASE + 703L)  /* (ViReal64, Multi-Channel)  */
#define IVIFGEN_ATTR_SPARSEMARKER_DESTINATION   (IVI_CLASS_PUBLIC_ATTR_BASE + 704L)  /* (ViString, Multi-Channel)  */
#define IVIFGEN_ATTR_SPARSEMARKER_POLARITY      (IVI_CLASS_PUBLIC_ATTR_BASE + 705L)  /* (ViInt32,  Multi-Channel)  */
#define IVIFGEN_ATTR_SPARSEMARKER_WFMHANDLE     (IVI_CLASS_PUBLIC_ATTR_BASE + 706L)  /* (ViInt32,  Multi-Channel)  */

/******************************************************************************
 *------------------- IviFgen Class Attribute Value Defines ------------------*
 ******************************************************************************/

   /*- Defined valued for attribute IVIFGEN_ATTR_OUTPUT_MODE -*/
#define IVIFGEN_VAL_OUTPUT_FUNC                         (0L)
#define IVIFGEN_VAL_OUTPUT_ARB                          (1L)
#define IVIFGEN_VAL_OUTPUT_SEQ                          (2L)

#define IVIFGEN_VAL_OUT_MODE_CLASS_EXT_BASE             (500L)
#define IVIFGEN_VAL_OUT_MODE_SPECIFIC_EXT_BASE          (1000L)

   /*- Defined valued for attribute IVIFGEN_ATTR_OPERATION_MODE -*/
#define IVIFGEN_VAL_OPERATE_CONTINUOUS                  (0L)
#define IVIFGEN_VAL_OPERATE_BURST                       (1L)

#define IVIFGEN_VAL_OP_MODE_CLASS_EXT_BASE              (500L)
#define IVIFGEN_VAL_OP_MODE_SPECIFIC_EXT_BASE           (1000L)

   /*- Defined values for attribute IVIFGEN_ATTR_REF_CLOCK_SOURCE -*/
#define IVIFGEN_VAL_REF_CLOCK_INTERNAL                  (0L)
#define IVIFGEN_VAL_REF_CLOCK_EXTERNAL                  (1L)
#define IVIFGEN_VAL_REF_CLOCK_RTSI_CLOCK                (101L)

#define IVIFGEN_VAL_CLK_SRC_CLASS_EXT_BASE              (500L)
#define IVIFGEN_VAL_CLK_SRC_SPECIFIC_EXT_BASE           (1000L)

   /*- Defined values for attribute IVIFGEN_ATTR_FUNC_WAVEFORM -*/
#define IVIFGEN_VAL_WFM_SINE                            (1L)
#define IVIFGEN_VAL_WFM_SQUARE                          (2L)
#define IVIFGEN_VAL_WFM_TRIANGLE                        (3L)
#define IVIFGEN_VAL_WFM_RAMP_UP                         (4L)
#define IVIFGEN_VAL_WFM_RAMP_DOWN                       (5L)
#define IVIFGEN_VAL_WFM_DC                              (6L)

#define IVIFGEN_VAL_WFM_CLASS_EXT_BASE                  (500L)
#define IVIFGEN_VAL_WFM_SPECIFIC_EXT_BASE               (1000L)

    /*- Defined values for attribute IVIFGEN_ATTR_TRIGGER_SOURCE -*/
#define IVIFGEN_VAL_EXTERNAL                            (1L)
#define IVIFGEN_VAL_SOFTWARE_TRIG                       (2L)
#define IVIFGEN_VAL_INTERNAL_TRIGGER                    (3L) 
#define IVIFGEN_VAL_TTL0                                (111L)
#define IVIFGEN_VAL_TTL1                                (112L)
#define IVIFGEN_VAL_TTL2                                (113L)
#define IVIFGEN_VAL_TTL3                                (114L)
#define IVIFGEN_VAL_TTL4                                (115L)
#define IVIFGEN_VAL_TTL5                                (116L)
#define IVIFGEN_VAL_TTL6                                (117L)
#define IVIFGEN_VAL_TTL7                                (118L)
#define IVIFGEN_VAL_ECL0                                (119L)
#define IVIFGEN_VAL_ECL1                                (120L)
#define IVIFGEN_VAL_PXI_STAR                            (131L)
#define IVIFGEN_VAL_RTSI_0                              (141L)
#define IVIFGEN_VAL_RTSI_1                              (142L)
#define IVIFGEN_VAL_RTSI_2                              (143L)
#define IVIFGEN_VAL_RTSI_3                              (144L)
#define IVIFGEN_VAL_RTSI_4                              (145L)
#define IVIFGEN_VAL_RTSI_5                              (146L)
#define IVIFGEN_VAL_RTSI_6                              (147L)

#define IVIFGEN_VAL_TRIG_SRC_CLASS_EXT_BASE             (500L)
#define IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE          (1000L)

  /*- Defined values for attribute IVIFGEN_ATTR_START_TRIGGER_SOURCE -*/
  /*- Defined values for attribute IVIFGEN_ATTR_STOP_TRIGGER_SOURCE -*/
  /*- Defined values for attribute IVIFGEN_ATTR_HOLD_TRIGGER_SOURCE -*/
  /*- Defined values for attribute IVIFGEN_ATTR_RESUME_TRIGGER_SOURCE -*/
  /*- Defined values for attribute IVIFGEN_ATTR_ADVANCE_TRIGGER_SOURCE -*/
  /*- Defined values for attribute IVIFGEN_ATTR_RESUME_TRIGGER_SOURCE -*/
  /*- Defined values for attribute IVIFGEN_ATTR_DATA_MARKER_DESTINATION -*/
  /*- Defined values for attribute IVIFGEN_ATTR_SPARSE_MARKER_DESTINATION -*/
#define IVIFGEN_VAL_TRIGGER_SOURCE_NONE                 ""
#define IVIFGEN_VAL_TRIGGER_SOURCE_IMMEDIATE            "Immediate"
#define IVIFGEN_VAL_TRIGGER_SOURCE_EXTERNAL             "External"
#define IVIFGEN_VAL_TRIGGER_SOURCE_INTERNAL             "Internal"
#define IVIFGEN_VAL_TRIGGER_SOURCE_SOFTWARE             "Software"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LAN0                 "LAN0"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LAN1                 "LAN1"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LAN2                 "LAN2"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LAN3                 "LAN3"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LAN4                 "LAN4"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LAN5                 "LAN5"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LAN6                 "LAN6"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LAN7                 "LAN7"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LXI0                 "LXI0"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LXI1                 "LXI1"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LXI2                 "LXI2"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LXI3                 "LXI3"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LXI4                 "LXI4"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LXI5                 "LXI5"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LXI6                 "LXI6"
#define IVIFGEN_VAL_TRIGGER_SOURCE_LXI7                 "LXI7"
#define IVIFGEN_VAL_TRIGGER_SOURCE_TTL0                 "TTL0"
#define IVIFGEN_VAL_TRIGGER_SOURCE_TTL1                 "TTL1"
#define IVIFGEN_VAL_TRIGGER_SOURCE_TTL2                 "TTL2"
#define IVIFGEN_VAL_TRIGGER_SOURCE_TTL3                 "TTL3"
#define IVIFGEN_VAL_TRIGGER_SOURCE_TTL4                 "TTL4"
#define IVIFGEN_VAL_TRIGGER_SOURCE_TTL5                 "TTL5"
#define IVIFGEN_VAL_TRIGGER_SOURCE_TTL6                 "TTL6"
#define IVIFGEN_VAL_TRIGGER_SOURCE_TTL7                 "TTL7"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXI_STAR             "PXI_STAR"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG0            "PXI_TRIG0"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG1            "PXI_TRIG1"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG2            "PXI_TRIG2"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG3            "PXI_TRIG3"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG4            "PXI_TRIG4"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG5            "PXI_TRIG5"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG6            "PXI_TRIG6"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG7            "PXI_TRIG7"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXIE_DSTARA          "PXIe_DSTARA"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXIE_DSTARB          "PXIe_DSTARB"
#define IVIFGEN_VAL_TRIGGER_SOURCE_PXIE_DSTARC          "PXIe_DSTARC"
#define IVIFGEN_VAL_TRIGGER_SOURCE_RTSI0                "RTSI0"
#define IVIFGEN_VAL_TRIGGER_SOURCE_RTSI1                "RTSI1"
#define IVIFGEN_VAL_TRIGGER_SOURCE_RTSI2                "RTSI2"
#define IVIFGEN_VAL_TRIGGER_SOURCE_RTSI3                "RTSI3"
#define IVIFGEN_VAL_TRIGGER_SOURCE_RTSI4                "RTSI4"
#define IVIFGEN_VAL_TRIGGER_SOURCE_RTSI5                "RTSI5"
#define IVIFGEN_VAL_TRIGGER_SOURCE_RTSI6                "RTSI6"

  /*- Defined values for attribute IVIFGEN_ATTR_SAMPLE_CLOCK_SOURCE -*/
#define IVIFGEN_VAL_SAMPLE_CLOCK_SOURCE_INTERNAL        (0L)
#define IVIFGEN_VAL_SAMPLE_CLOCK_SOURCE_EXTERNAL        (1L)
	
  /*- Defined values for attribute IVIFGEN_ATTR_DATAMARKER_POLARITY -*/
#define IVIFGEN_VAL_MARKER_POLARITY_ACTIVE_HIGH         (0L)
#define IVIFGEN_VAL_MARKER_POLARITY_ACTIVE_LOW          (1L)

  /*- Defined values for attribute IVIFGEN_ATTR_AM_SOURCE -*/
#define IVIFGEN_VAL_AM_INTERNAL                         (0L)
#define IVIFGEN_VAL_AM_EXTERNAL                         (1L)

#define IVIFGEN_VAL_AM_SOURCE_CLASS_EXT_BASE            (500L)
#define IVIFGEN_VAL_AM_SOURCE_SPECIFIC_EXT_BASE         (1000L)

  /*- Defined values for attribute IVIFGEN_ATTR_AM_INTERNAL_WAVEFORM -*/
#define IVIFGEN_VAL_AM_INTERNAL_SINE                    (1L)
#define IVIFGEN_VAL_AM_INTERNAL_SQUARE                  (2L)
#define IVIFGEN_VAL_AM_INTERNAL_TRIANGLE                (3L)
#define IVIFGEN_VAL_AM_INTERNAL_RAMP_UP                 (4L)
#define IVIFGEN_VAL_AM_INTERNAL_RAMP_DOWN               (5L)

#define IVIFGEN_VAL_AM_INTERNAL_WFM_CLASS_EXT_BASE      (500L)
#define IVIFGEN_VAL_AM_INTERNAL_WFM_SPECIFIC_EXT_BASE   (1000L)

  /*- Defined values for attribute IVIFGEN_ATTR_FM_SOURCE -*/
#define IVIFGEN_VAL_FM_INTERNAL                         (0L)
#define IVIFGEN_VAL_FM_EXTERNAL                         (1L)

#define IVIFGEN_VAL_FM_SOURCE_CLASS_EXT_BASE            (500L)
#define IVIFGEN_VAL_FM_SOURCE_SPECIFIC_EXT_BASE         (1000L)

  /*- Defined values for attribute IVIFGEN_ATTR_FM_INTERNAL_WAVEFORM -*/
#define IVIFGEN_VAL_FM_INTERNAL_SINE                    (1L)
#define IVIFGEN_VAL_FM_INTERNAL_SQUARE                  (2L)
#define IVIFGEN_VAL_FM_INTERNAL_TRIANGLE                (3L)
#define IVIFGEN_VAL_FM_INTERNAL_RAMP_UP                 (4L)
#define IVIFGEN_VAL_FM_INTERNAL_RAMP_DOWN               (5L)

#define IVIFGEN_VAL_FM_INTERNAL_WFM_CLASS_EXT_BASE      (500L)
#define IVIFGEN_VAL_FM_INTERNAL_WFM_SPECIFIC_EXT_BASE   (1000L)

  /*- Defined values for attribute IVIFGEN_ATTR_BINARY_ALIGNMENT -*/
#define IVIFGEN_VAL_BINARY_ALIGNMENT_LEFT               (0L)
#define IVIFGEN_VAL_BINARY_ALIGNMENT_RIGHT              (1L)

#define IVIFGEN_VAL_BINARY_ALIGNMENT_CLASS_EXT_BASE     (500L)
#define IVIFGEN_VAL_BINARY_ALIGNMENT_SPECIFIC_EXT_BASE  (1000L)

  /*- Defined values for attribute IVIFGEN_ATTR_OUTPUT_TERMINAL_CONFIGURATION -*/
#define IVIFGEN_VAL_TERMINAL_CONFIGURATION_SINGLE_ENDED         (0L)
#define IVIFGEN_VAL_TERMINAL_CONFIGURATION_DIFFERENTIAL         (1L)

#define IVIFGEN_VAL_TERMINAL_CONFIGURATION_CLASS_EXT_BASE       (500L)
#define IVIFGEN_VAL_TERMINAL_CONFIGURATION_SPECIFIC_EXT_BASE    (1000L)

  /*- Defined values for attribute IVIFGEN_ATTR_START_TRIGGER_SLOPE -*/
  /*- Defined values for attribute IVIFGEN_ATTR_STOP_TRIGGER_SLOPE -*/
  /*- Defined values for attribute IVIFGEN_ATTR_HOLD_TRIGGER_SLOPE -*/
  /*- Defined values for attribute IVIFGEN_ATTR_RESUME_TRIGGER_SLOPE -*/
  /*- Defined values for attribute IVIFGEN_ATTR_ADVANCE_TRIGGER_SLOPE -*/
#define IVIFGEN_VAL_TRIGGER_POSITIVE                    (0L)
#define IVIFGEN_VAL_TRIGGER_NEGATIVE                    (1L)
#define IVIFGEN_VAL_TRIGGER_EITHER                      (2L)

#define IVIFGEN_VAL_TRIGGER_CLASS_EXT_BASE              (500L)
#define IVIFGEN_VAL_TRIGGER_SPECIFIC_EXT_BASE           (1000L)
	
   /*- Defined values for waveformHandle parameter for function IviFgen_ClearArbWaveform -*/
#define IVIFGEN_VAL_ALL_WAVEFORMS                       (-1L)

   /*- Defined values for sequenceHandle parameter for function IviFgen_ClearArbSequence -*/
#define IVIFGEN_VAL_ALL_SEQUENCES                       (-1L)

/******************************************************************************
 *----------- IviFgen Class Instrument Driver Function Declarations ----------*
 ******************************************************************************/
   /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviFgen_init (ViRsrc logicalName, 
                                ViBoolean IDQuery,
                                ViBoolean resetDevice, 
                                ViSession *vi);

ViStatus _VI_FUNC IviFgen_close (ViSession vi);

ViStatus _VI_FUNC IviFgen_reset (ViSession vi);

ViStatus _VI_FUNC IviFgen_self_test (ViSession vi, 
                                     ViInt16* selfTestResult,
                                     ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviFgen_error_query (ViSession vi, 
                                       ViInt32 *errorCode, 
                                       ViChar errorMessage[]);

ViStatus _VI_FUNC IviFgen_error_message (ViSession vi, 
                                         ViStatus statusCode,
                                         ViChar message[]);

ViStatus _VI_FUNC IviFgen_revision_query (ViSession vi, 
                                          ViChar driverRev[],
                                          ViChar instrRev[]);
                                           
    /*- Utility Functions -*/
ViStatus _VI_FUNC IviFgen_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviFgen_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviFgen_Disable (ViSession vi);

   /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviFgen_InitWithOptions (ViRsrc logicalName, 
                                           ViBoolean IDQuery,
                                           ViBoolean resetDevice, 
                                           ViConstString optionString, 
                                           ViSession *vi);

   /*- Set, Get, and Check Attribute Functions -*/
ViStatus _VI_FUNC IviFgen_GetAttributeViInt32 (ViSession vi, 
                                               ViConstString channelName,
                                               ViAttr attributeId, 
                                               ViInt32 *value);

ViStatus _VI_FUNC IviFgen_SetAttributeViInt32 (ViSession vi, 
                                               ViConstString channelName,
                                               ViAttr attributeId,
                                               ViInt32 value);

ViStatus _VI_FUNC IviFgen_CheckAttributeViInt32 (ViSession vi,
                                                 ViConstString channelName,
                                                 ViAttr attributeId,
                                                 ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviFgen_GetAttributeViInt64 (ViSession vi, 
                                               ViConstString channelName,
                                               ViAttr attributeId, 
                                               ViInt64 *value);

ViStatus _VI_FUNC IviFgen_SetAttributeViInt64 (ViSession vi, 
                                               ViConstString channelName,
                                               ViAttr attributeId,
                                               ViInt64 value);

ViStatus _VI_FUNC IviFgen_CheckAttributeViInt64 (ViSession vi,
                                                 ViConstString channelName,
                                                 ViAttr attributeId,
                                                 ViInt64 value);
#endif

ViStatus _VI_FUNC IviFgen_GetAttributeViReal64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId, 
                                                ViReal64 *value);

ViStatus _VI_FUNC IviFgen_SetAttributeViReal64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViReal64 value);

ViStatus _VI_FUNC IviFgen_CheckAttributeViReal64 (ViSession vi, 
                                                  ViConstString channelName,
                                                  ViAttr attributeId, 
                                                  ViReal64 value);

ViStatus _VI_FUNC IviFgen_GetAttributeViString (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId, 
                                                ViInt32 bufferSize,
                                                ViChar value[]);

ViStatus _VI_FUNC IviFgen_SetAttributeViString (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId, 
                                                ViConstString value);

ViStatus _VI_FUNC IviFgen_CheckAttributeViString (ViSession vi, 
                                                  ViConstString channelName,
                                                  ViAttr attributeId, 
                                                  ViConstString value);

ViStatus _VI_FUNC IviFgen_GetAttributeViBoolean (ViSession vi, 
                                                 ViConstString channelName,
                                                 ViAttr attributeId, 
                                                 ViBoolean *value);

ViStatus _VI_FUNC IviFgen_SetAttributeViBoolean (ViSession vi, 
                                                 ViConstString channelName,
                                                 ViAttr attributeId, 
                                                 ViBoolean value);

ViStatus _VI_FUNC IviFgen_CheckAttributeViBoolean (ViSession vi, 
                                                   ViConstString channelName,
                                                   ViAttr attributeId, 
                                                   ViBoolean value);

ViStatus _VI_FUNC IviFgen_GetAttributeViSession (ViSession vi, 
                                                 ViConstString channelName,
                                                 ViAttr attributeId, 
                                                 ViSession *value);

ViStatus _VI_FUNC IviFgen_SetAttributeViSession (ViSession vi, 
                                                 ViConstString channelName,
                                                 ViAttr attributeId, 
                                                 ViSession value);

ViStatus _VI_FUNC IviFgen_CheckAttributeViSession (ViSession vi, 
                                                   ViConstString channelName,
                                                   ViAttr attributeId, 
                                                   ViSession value);

   /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviFgen_LockSession (ViSession vi, 
                                       ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviFgen_UnlockSession (ViSession vi, 
                                         ViBoolean *callerHasLock);

   /*- Error Information Functions -*/
ViStatus _VI_FUNC IviFgen_GetError (ViSession vi, 
                                    ViStatus *errorCode,
                                    ViInt32 bufferSize,
                                    ViChar description[]);

ViStatus _VI_FUNC IviFgen_ClearError (ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviFgen_GetNextInterchangeWarning (ViSession vi, 
                                                     ViInt32 bufferSize, 
                                                     ViChar warning[]);

ViStatus _VI_FUNC IviFgen_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviFgen_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviFgen_GetNextCoercionRecord (ViSession vi, 
                                                 ViInt32 bufferSize, 
                                                 ViChar record[]);

ViStatus _VI_FUNC IviFgen_GetSpecificDriverCHandle (ViSession vi,
                                                    ViSession* specificDriverCHandle);
   
ViStatus _VI_FUNC IviFgen_GetSpecificDriverIUnknownPtr (ViSession vi,
                                                       void* specificDriverIUnknownPtr);
   /*- IviFgenBase Capability Group  -*/
ViStatus _VI_FUNC IviFgen_ConfigureOutputMode (ViSession vi, 
                                               ViInt32 outputMode);
ViStatus _VI_FUNC IviFgen_ConfigureOperationMode (ViSession vi,
                                                  ViConstString channelName,
                                                  ViInt32 operationMode);

ViStatus _VI_FUNC IviFgen_ConfigureRefClockSource (ViSession vi, 
                                                   ViInt32 refClockSource);

ViStatus _VI_FUNC IviFgen_ConfigureOutputImpedance (ViSession vi, 
                                                    ViConstString channelName,
                                                    ViReal64 outputImpedance);

ViStatus _VI_FUNC IviFgen_ConfigureOutputEnabled (ViSession vi, 
                                                  ViConstString channelName,
                                                  ViBoolean enabled);

ViStatus _VI_FUNC IviFgen_GetChannelName (ViSession vi,
                                          ViInt32 index,
                                          ViInt32 bufferSize,
                                          ViChar name[]);

ViStatus _VI_FUNC IviFgen_InitiateGeneration (ViSession vi);

ViStatus _VI_FUNC IviFgen_AbortGeneration    (ViSession vi);

   /*- IviFgenStdFunc Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureStandardWaveform (ViSession vi, 
                                                     ViConstString channelName,
                                                     ViInt32 waveform, 
                                                     ViReal64 amplitude,
                                                     ViReal64 dcOffset, 
                                                     ViReal64 frequency,
                                                     ViReal64 startPhase);

    /*- IviFgenArbWfm Extension Group -*/
ViStatus _VI_FUNC IviFgen_QueryArbWfmCapabilities (ViSession vi, 
                                                   ViInt32 *maxNumWfms,
                                                   ViInt32 *wfmQuantum,
                                                   ViInt32 *minWfmSize,
                                                   ViInt32 *maxWfmSize);

ViStatus _VI_FUNC IviFgen_CreateArbWaveform (ViSession vi,
                                             ViInt32 wfmSize,
                                             ViReal64 wfmData[], 
                                             ViInt32 *wfmHandle);

ViStatus _VI_FUNC IviFgen_ConfigureSampleRate (ViSession vi, 
                                               ViReal64 sampleRate);

ViStatus _VI_FUNC IviFgen_ConfigureArbWaveform (ViSession vi, 
                                                ViConstString channelName,
                                                ViInt32 wfmHandle,
                                                ViReal64 arbGain,
                                                ViReal64 arbOffset);

ViStatus _VI_FUNC IviFgen_ClearArbWaveform (ViSession vi, 
                                            ViInt32 wfmHandle);

    /*- IviFgenArbFrequency Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureArbFrequency (ViSession vi, 
                                                 ViConstString channelName,
                                                 ViReal64 frequency);

    /*- IviFgenArbSeq Extension Group -*/ 
ViStatus _VI_FUNC IviFgen_QueryArbSeqCapabilities (ViSession vi, 
                                                   ViInt32 *maxNumSeqs,
                                                   ViInt32 *minSeqLength, 
                                                   ViInt32 *maxSeqLength,
                                                   ViInt32 *maxLoopCount);

ViStatus _VI_FUNC IviFgen_CreateArbSequence (ViSession vi, 
                                             ViInt32 seqLength,
                                             ViInt32 wfmHandle[], 
                                             ViInt32 wfmLoopCount[],
                                             ViInt32 *seqHandle);

ViStatus _VI_FUNC IviFgen_ConfigureArbSequence (ViSession vi, 
                                                ViConstString channelName,
                                                ViInt32 seqHandle,
                                                ViReal64 arbGain,
                                                ViReal64 arbOffset);

ViStatus _VI_FUNC IviFgen_ClearArbSequence (ViSession vi, 
                                            ViInt32 seqHandle);

ViStatus _VI_FUNC IviFgen_ClearArbMemory (ViSession vi);

    /*- IviFgenTrigger Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureTriggerSource (ViSession vi,
                                                  ViConstString channelName,
                                                  ViInt32 trigSource);

    /*- IviFgenStartTrigger Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureStartTrigger (ViSession vi,
                                                 ViConstString channelName,
                                                 ViConstString source,
                                                 ViInt32 slope);

    /*- IviFgenStopTrigger Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureStopTrigger (ViSession vi,
                                                ViConstString channelName,
                                                ViConstString source,
                                                ViInt32 slope);

ViStatus _VI_FUNC IviFgen_SendSoftwareStopTrigger (ViSession vi);

    /*- IviFgenHoldTrigger Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureHoldTrigger (ViSession vi,
                                                ViConstString channelName,
                                                ViConstString source,
                                                ViInt32 slope);

ViStatus _VI_FUNC IviFgen_SendSoftwareHoldTrigger (ViSession vi);

    /*- IviFgenResumeTrigger Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureResumeTrigger (ViSession vi,
                                                  ViConstString channelName,
                                                  ViConstString source,
                                                  ViInt32 slope);

ViStatus _VI_FUNC IviFgen_SendSoftwareResumeTrigger (ViSession vi);

    /*- IviFgenAdvanceTrigger Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureAdvanceTrigger (ViSession vi,
                                                   ViConstString channelName,
                                                   ViConstString source,
                                                   ViInt32 slope);

ViStatus _VI_FUNC IviFgen_SendSoftwareAdvanceTrigger (ViSession vi);

    /*- IviFgenInternalTrigger Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureInternalTriggerRate (ViSession vi,
                                                        ViReal64 rate);

    /*- IviFgenSoftwareTrigger Extension Group -*/
ViStatus _VI_FUNC IviFgen_SendSoftwareTrigger (ViSession vi);

    /*- IviFgenBurst Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureBurstCount (ViSession vi,
                                               ViConstString channelName,
                                               ViInt32 count);

    /*- IviFgenModulateAM Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureAMEnabled (ViSession vi,
                                              ViConstString channelName,
                                              ViBoolean enabled);

ViStatus _VI_FUNC IviFgen_ConfigureAMSource (ViSession vi,
                                             ViConstString channelName,
                                             ViInt32 source);

ViStatus _VI_FUNC IviFgen_ConfigureAMInternal (ViSession vi, 
                                               ViReal64 amdepth,
                                               ViInt32 amWaveform,
                                               ViReal64 amFrequency);

    /*- IviFgenModulateFM Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureFMEnabled (ViSession vi,
                                              ViConstString channelName,
                                              ViBoolean enabled);

ViStatus _VI_FUNC IviFgen_ConfigureFMSource (ViSession vi,
                                             ViConstString channelName,
                                             ViInt32 source);

ViStatus _VI_FUNC IviFgen_ConfigureFMInternal (ViSession vi, 
                                               ViReal64 fmdeviation,
                                               ViInt32 fmWaveform,
                                               ViReal64 fmFrequency);

    /*- IviFgenSampleClock Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureSampleClock (ViSession vi, 
                                                ViInt32 source);

ViStatus _VI_FUNC IviFgen_ConfigureSampleClockOutputEnabled (ViSession vi,
                                                             ViBoolean enabled);

    /*- IviFgenArbWfmSize64 Extension Group -*/
ViStatus _VI_FUNC IviFgen_QueryArbWfmCapabilities64 (ViSession vi,
                                                     ViInt32 *maxNumWfms,
                                                     ViInt32 *wfmQuantum,
                                                     ViInt64 *minWfmSize,
                                                     ViInt64 *maxWfmSize);

    /*- IviFgenArbChannelWfm Extension Group -*/
ViStatus _VI_FUNC IviFgen_CreateChannelArbWaveform (ViSession vi,
                                                    ViConstString channelName,
                                                    ViInt64 wfmSize,
                                                    ViReal64 wfmData[],
                                                    ViInt32 *wfmHandle);

    /*- IviFgenArbWfmBinary Extension Group -*/
ViStatus _VI_FUNC IviFgen_CreateChannelArbWaveform16 (ViSession vi,
                                                      ViConstString channelName,
                                                      ViInt64 wfmSize,
                                                      ViInt16 wfmData[],
                                                      ViInt32 *wfmHandle);

ViStatus _VI_FUNC IviFgen_CreateChannelArbWaveform32 (ViSession vi,
                                                      ViConstString channelName,
                                                      ViInt64 wfmSize,
                                                      ViInt32 wfmData[],
                                                      ViInt32 *wfmHandle);

    /*- IviFgenDataMarker Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureDataMarker (ViSession vi,
                                               ViConstString name,
                                               ViConstString sourceChannel,
                                               ViInt32 bitPosition,
                                               ViConstString destination);

ViStatus _VI_FUNC IviFgen_GetDataMarkerName (ViSession vi,
                                             ViInt32 index, 
                                             ViInt32 nameBufferSize,
                                             ViChar name[]);

ViStatus _VI_FUNC IviFgen_DisableAllDataMarkers (ViSession vi);

    /*- IviFgenSparseMarker Extension Group -*/
ViStatus _VI_FUNC IviFgen_ConfigureSparseMarker (ViSession vi,
                                                 ViConstString name,
                                                 ViInt32 wfmHandle,
                                                 ViInt64 numIndexes, 
                                                 ViInt64 indexes[],
                                                 ViConstString destination);

ViStatus _VI_FUNC IviFgen_GetSparseMarkerName (ViSession vi,
                                               ViInt32 index, 
                                               ViInt32 nameBufferSize,
                                               ViChar name[]);

ViStatus _VI_FUNC IviFgen_GetSparseMarkerIndexes (ViSession vi,
                                                  ViConstString name,
                                                  ViInt64 indexesArraySize,
                                                  ViInt64 indexes[],
                                                  ViInt64 *indexesActualSize);

ViStatus _VI_FUNC IviFgen_SetSparseMarkerIndexes (ViSession vi,
                                                  ViConstString name,
                                                  ViInt64 indexesArraySize,
                                                  ViInt64 indexes[]);

ViStatus _VI_FUNC IviFgen_DisableAllSparseMarkers (ViSession vi);

/******************************************************************************
 *----------------- IviFgen Class Error And Completion Codes -----------------*
 ******************************************************************************/
#define IVIFGEN_ERROR_NO_WFMS_AVAILABLE       (IVI_CLASS_ERROR_BASE + 4L)
#define IVIFGEN_ERROR_WFM_IN_USE              (IVI_CLASS_ERROR_BASE + 8L)
#define IVIFGEN_ERROR_NO_SEQS_AVAILABLE       (IVI_CLASS_ERROR_BASE + 9L)
#define IVIFGEN_ERROR_SEQ_IN_USE              (IVI_CLASS_ERROR_BASE + 13L)
#define IVIFGEN_ERROR_INVALID_WFM_CHANNEL     (IVI_CLASS_ERROR_BASE + 14L)
#define IVIFGEN_ERROR_TRIGGER_NOT_SOFTWARE    (IVI_CROSS_CLASS_ERROR_BASE + 1L)

#define IVIFGEN_ERRMSG_NO_WFMS_AVAILABLE      "The function generator's waveform memory is full."
#define IVIFGEN_ERRMSG_WFM_IN_USE             "The waveform is currently in use."
#define IVIFGEN_ERRMSG_NO_SEQS_AVAILABLE      "The function generator's sequence memory is full."
#define IVIFGEN_ERRMSG_SEQ_IN_USE             "The sequence is currently in use."
#define IVIFGEN_ERRMSG_INVALID_WFM_CHANNEL    "The waveform was created on a different channel than the one for which it is being configured."
#define IVIFGEN_ERRMSG_TRIGGER_NOT_SOFTWARE   "The trigger source is not set to software trigger."

#define IVIFGEN_ERROR_CODES_AND_MSGS \
        { IVIFGEN_ERROR_NO_WFMS_AVAILABLE,    IVIFGEN_ERRMSG_NO_WFMS_AVAILABLE   }, \
        { IVIFGEN_ERROR_WFM_IN_USE,           IVIFGEN_ERRMSG_WFM_IN_USE          }, \
        { IVIFGEN_ERROR_NO_SEQS_AVAILABLE,    IVIFGEN_ERRMSG_NO_SEQS_AVAILABLE   }, \
        { IVIFGEN_ERROR_SEQ_IN_USE,           IVIFGEN_ERRMSG_SEQ_IN_USE          }, \
        { IVIFGEN_ERROR_INVALID_WFM_CHANNEL,  IVIFGEN_ERRMSG_INVALID_WFM_CHANNEL }, \
        { IVIFGEN_ERROR_TRIGGER_NOT_SOFTWARE, IVIFGEN_ERRMSG_TRIGGER_NOT_SOFTWARE}

/*- IviFgenObsolete.h included for backwards compatibility -*/
#include "IviFgenObsolete.h"

/******************************************************************************
 *----------------------------- End Include File -----------------------------*
 ******************************************************************************/
#if defined(__cplusplus) || defined(c__plusplus)
}
#endif

#endif /* IVIFGEN_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviFgenObsolete.h sha256=75ab99d5dd0cae39eb1890d93ed74973a84fe69c7cb6a16e55129473db761152 bytes=8754 -->
## FILE: imports/include/IviFgenObsolete.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviFgenObsolete.h`
- sha256: `75ab99d5dd0cae39eb1890d93ed74973a84fe69c7cb6a16e55129473db761152`
- bytes: 8754

````c
/*****************************************************************************
 *                              I V I - F G E N                              *
 *---------------------------------------------------------------------------*
 *    Copyright (c) 1999-2020 National Instruments.  All Rights Reserved.    *
 *---------------------------------------------------------------------------*
 *                                                                           *
 * Title:       IviFgenObsolete.h                                            * 
 * Purpose:     IviFgen Class value and attribute Id declarations for the    *
 *              now obsolete IviFgen 1.0 specification.                      * 
 *              These macros are defined to keep backward compatibility with *
 *              previous versions of this file.  Instrument specific         *
 *              drivers should no longer use these macros. Instead, the      *
 *              drivers must use definitions from the current IviFgen.h      *
 *              header file.                                                 *
 *****************************************************************************/

#ifndef __IVIFGEN_HEADER_OBSOLETE
#define __IVIFGEN_HEADER_OBSOLETE
#include <ivi.h>

    /*- Obsolete Inherent Attributes -*/
#define IVIFGEN_ATTR_CLASS_MAJOR_VERSION        IVI_ATTR_CLASS_MAJOR_VERSION
#define IVIFGEN_ATTR_CLASS_MINOR_VERSION        IVI_ATTR_CLASS_MINOR_VERSION
#define IVIFGEN_ATTR_CLASS_REVISION             IVI_ATTR_CLASS_REVISION

#define IVIFGEN_ATTR_CLASS_PREFIX               IVI_ATTR_CLASS_PREFIX
#define IVIFGEN_ATTR_SPECIFIC_PREFIX            IVI_ATTR_SPECIFIC_PREFIX
#define IVIFGEN_ATTR_MODULE_PATHNAME            IVI_ATTR_MODULE_PATHNAME

#define IVIFGEN_ATTR_DRIVER_MAJOR_VERSION       IVI_ATTR_DRIVER_MAJOR_VERSION
#define IVIFGEN_ATTR_DRIVER_MINOR_VERSION       IVI_ATTR_DRIVER_MINOR_VERSION
#define IVIFGEN_ATTR_DRIVER_REVISION            IVI_ATTR_DRIVER_REVISION

#define IVIFGEN_ATTR_ENGINE_MAJOR_VERSION       IVI_ATTR_ENGINE_MAJOR_VERSION        /* ViInt32,  read-only */
#define IVIFGEN_ATTR_ENGINE_MINOR_VERSION       IVI_ATTR_ENGINE_MINOR_VERSION        /* ViInt32,  read-only */
#define IVIFGEN_ATTR_ENGINE_REVISION            IVI_ATTR_ENGINE_REVISION             /* ViString, read-only */

#define IVIFGEN_ATTR_NUM_CHANNELS               IVI_ATTR_NUM_CHANNELS
#define IVIFGEN_ATTR_QUERY_INSTR_STATUS         IVI_ATTR_QUERY_INSTR_STATUS             /* ViBoolean */
#define IVIFGEN_ATTR_RESOURCE_DESCRIPTOR        IVI_ATTR_RESOURCE_DESCRIPTOR            /* ViString, read-only */

#define IVIFGEN_ATTR_IO_SESSION_TYPE                  IVI_ATTR_IO_SESSION_TYPE
#define IVIFGEN_ATTR_IO_SESSION                       IVI_ATTR_IO_SESSION

#define IVIFGEN_ATTR_CLASS_DRIVER_MAJOR_VERSION       IVI_ATTR_CLASS_DRIVER_MAJOR_VERSION         /* ViInt32,  read-only */
#define IVIFGEN_ATTR_CLASS_DRIVER_MINOR_VERSION       IVI_ATTR_CLASS_DRIVER_MINOR_VERSION         /* ViInt32,  read-only */

#define IVIFGEN_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION        /* ViInt32,  read-only */
#define IVIFGEN_ATTR_SPECIFIC_DRIVER_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_MINOR_VERSION        /* ViInt32,  read-only */

#define IVIFGEN_ATTR_ATTRIBUTE_CAPABILITIES    IVI_ATTR_ATTRIBUTE_CAPABILITIES      /* ViString, read-only */

        /*- Error Info -*/
#define IVIFGEN_ATTR_PRIMARY_ERROR                    IVI_ATTR_PRIMARY_ERROR               /* ViInt32  */
#define IVIFGEN_ATTR_SECONDARY_ERROR                  IVI_ATTR_SECONDARY_ERROR             /* ViInt32  */
#define IVIFGEN_ATTR_ERROR_ELABORATION                IVI_ATTR_ERROR_ELABORATION           /* ViString */

    /*- Obsolete Attributes -*/
#define IVIFGEN_ATTR_CYCLE_COUNT            (IVI_CLASS_PUBLIC_ATTR_BASE + 301L)

    /*- Obsolete values for function parameters -*/
#define IVIFGEN_VAL_FIRST_WAVEFORM_HANDLE   (10000L)
#define IVIFGEN_VAL_LAST_WAVEFORM_HANDLE    (IVIFGEN_VAL_FIRST_WAVEFORM_HANDLE + 9999L)

#define IVIFGEN_VAL_FIRST_SEQUENCE_HANDLE   (100000L)
#define IVIFGEN_VAL_LAST_SEQUENCE_HANDLE    (IVIFGEN_VAL_FIRST_SEQUENCE_HANDLE + 9999L)

    /*- Obsolete values for attributes -*/
        /*- IVIFGEN_ATTR_REF_CLOCK_SOURCE values -*/
#define IVIFGEN_VAL_INTERNAL                (0L)
#define IVIFGEN_VAL_RTSI_CLOCK              (101L)

        /*- IVIFGEN_ATTR_OUTPUT_IMPEDANCE values -*/
#define IVIFGEN_VAL_50_OHMS                 (50.0)
#define IVIFGEN_VAL_75_OHMS                 (75.0)
#define IVIFGEN_VAL_1_MEGA_OHM              (1.0e+6)

        /*- IVIFGEN_ATTR_FUNC_WAVEFORM values -*/
#define IVIFGEN_VAL_WFM_BASE                (0L)

        /*- IVIFGEN_ATTR_TRIGGER_SOURCE values -*/
#define IVIFGEN_VAL_IMMEDIATE               (0L)
#define IVIFGEN_VAL_SW_TRIG_FUNC            (2L)
#define IVIFGEN_VAL_GPIB_GET                (101L)

        /*- IVIFGEN_ATTR_CYCLE_COUNT values -*/
#define IVIFGEN_VAL_GENERATE_CONTINUOUS     (-1L)

        /*- IVIFGEN_ATTR_AM_INTERNAL_WAVEFORM -*/
#define IVIFGEN_VAL_AM_INTERNAL_DC          (6L)
    
        /*- IVIFGEN_ATTR_FM_INTERNAL_WAVEFORM -*/
#define IVIFGEN_VAL_FM_INTERNAL_DC          (6L)
    
    /*- Obsolete error and completion code values -*/
#define IVIFGEN_ERROR_NOT_CONFIGURABLE              (IVI_CLASS_ERROR_BASE+0x0001L) 
#define IVIFGEN_ERROR_NOT_GENERATING                (IVI_CLASS_ERROR_BASE+0x0002L)
#define IVIFGEN_ERROR_INVALID_MODE                  (IVI_CLASS_ERROR_BASE+0x0003L)        
#define IVIFGEN_ERROR_INVALID_WFM_LENGTH            (IVI_CLASS_ERROR_BASE+0x0005L)
#define IVIFGEN_ERROR_INVALID_WFM_ELEMENT           (IVI_CLASS_ERROR_BASE+0x0006L)
#define IVIFGEN_ERROR_INVALID_WAVEFORM              (IVI_CLASS_ERROR_BASE+0x0007L)        
#define IVIFGEN_ERROR_INVALID_SEQ_LENGTH            (IVI_CLASS_ERROR_BASE+0x000AL)
#define IVIFGEN_ERROR_INVALID_LOOP_COUNT            (IVI_CLASS_ERROR_BASE+0x000BL)
#define IVIFGEN_ERROR_INVALID_SEQUENCE              (IVI_CLASS_ERROR_BASE+0x000CL)

#define IVIFGEN_ERRMSG_NOT_CONFIGURABLE             "The operation cannot be completed because the function generator is not configurable" 
#define IVIFGEN_ERRMSG_NOT_GENERATING               "The operation cannot be completed because the function generator is not generating a signal" 
#define IVIFGEN_ERRMSG_INVALID_MODE                 "The operation cannot be completed in the current output mode."        
#define IVIFGEN_ERRMSG_INVALID_WFM_LENGTH           "The waveform length is invalid."
#define IVIFGEN_ERRMSG_INVALID_WFM_ELEMENT          "One of the elements in the waveform data array is invalid."
#define IVIFGEN_ERRMSG_INVALID_WAVEFORM             "The specified waveform is invalid."        
#define IVIFGEN_ERRMSG_INVALID_SEQ_LENGTH           "The sequence length is invalid."
#define IVIFGEN_ERRMSG_INVALID_LOOP_COUNT           "One of the the elements in the loop count array is invalid."
#define IVIFGEN_ERRMSG_INVALID_SEQUENCE             "The specified sequence is invalid."

    /*- Obsolete Error Information Functions -*/
ViStatus _VI_FUNC IviFgen_GetErrorInfo (ViSession vi, 
                                        ViStatus *primaryError,
                                        ViStatus *secondaryError,
                                        ViChar errorElaboration[IVI_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC IviFgen_ClearErrorInfo (ViSession vi);

    /*- Obsolete functions -*/
ViStatus _VI_FUNC IviFgen_EnableOutput       (ViSession vi, ViConstString channelName);
ViStatus _VI_FUNC IviFgen_DisableOutput      (ViSession vi, ViConstString channelName);
ViStatus _VI_FUNC IviFgen_ConfigureTrigger   (ViSession vi, ViConstString channelName,
                                              ViInt32 trigSource, ViInt32 cycleCount);
ViStatus _VI_FUNC IviFgen_SendSWTrigger      (ViSession vi);
ViStatus _VI_FUNC IviFgen_EnableAM           (ViSession vi, ViConstString channelName,
                                              ViInt32 amSource);
ViStatus _VI_FUNC IviFgen_DisableAM          (ViSession vi, ViConstString channelName);
ViStatus _VI_FUNC IviFgen_EnableFM                  (ViSession vi, ViConstString channelName,
                                                     ViInt32 fmSource);
ViStatus _VI_FUNC IviFgen_DisableFM                 (ViSession vi, ViConstString channelName);

/*****************************************************************************
 *---------------------------- End Include File -----------------------------*
 *****************************************************************************/

#endif /* __IVIFGEN_HEADER_OBSOLETE */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviPwrMeter.h sha256=93c215af7a94402c3dd86d42ce00827860d28d68b0c757f482d6c308f855d288 bytes=32102 -->
## FILE: imports/include/IviPwrMeter.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviPwrMeter.h`
- sha256: `93c215af7a94402c3dd86d42ce00827860d28d68b0c757f482d6c308f855d288`
- bytes: 32102

````c
/****************************************************************************
 *                         IVIPWRMETER                               
 *---------------------------------------------------------------------------
 *    Copyright (c) 2009-2020 National Instruments.  All Rights Reserved.        
 *---------------------------------------------------------------------------
 *                                                                          
 * Title:       IviPwrMeter.h                                                    
 * Purpose:     IviPwrMeter Class declarations for the Base and Extended  
 *              IviPwrMeter Capabilities.                                        
 ****************************************************************************/

#ifndef IVIPWRMETER_HEADER
#define IVIPWRMETER_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVIPWRMETER_MAJOR_VERSION              (4L)
#define IVIPWRMETER_MINOR_VERSION              (0L)

#define IVIPWRMETER_CLASS_SPEC_MAJOR_VERSION   (2L)
#define IVIPWRMETER_CLASS_SPEC_MINOR_VERSION   (0L)

#define IVIPWRMETER_DRIVER_VENDOR              "National Instruments"
#ifdef	_IVI_mswin64_
#define IVIPWRMETER_DRIVER_DESCRIPTION         "IviPwrMeter Class Driver [Compiled for 64-bit.]"
#else
#define IVIPWRMETER_DRIVER_DESCRIPTION         "IviPwrMeter Class Driver"
#endif

/****************************************************************************
 *------------------------------ Useful Macros -----------------------------*
 ****************************************************************************/
/*- Defined values for Operator parameter of function -*/
/*- IviPwrMeter_ConfigureMeasurement -*/
#define IVIPWRMETER_VAL_NONE                                                (0L)
#define IVIPWRMETER_VAL_DIFFERENCE                                          (1L)
#define IVIPWRMETER_VAL_SUM                                                 (2L)
#define IVIPWRMETER_VAL_QUOTIENT                                            (3L)

/*- Defined values for MeasurementStatus parameter of function -*/
/*- IviPwrMeter_IsMeasurementComplete -*/
#define IVIPWRMETER_VAL_MEAS_COMPLETE                                       (1L)
#define IVIPWRMETER_VAL_MEAS_IN_PROGRESS                                    (0L)
#define IVIPWRMETER_VAL_MEAS_STATUS_UNKNOWN                                 (-1L)

/*- Defined values for RangeType parameter of function -*/
/*- IviPwrMeter_QueryResultRangeType -*/
#define IVIPWRMETER_VAL_IN_RANGE                                            (0L)
#define IVIPWRMETER_VAL_UNDER_RANGE                                         (-1L)
#define IVIPWRMETER_VAL_OVER_RANGE                                          (1L)

/*- Defined values for MaxTime parameter of function -*/
/*- IviPwrMeter_Read -*/
/*- Defined values for MaxTime parameter of function -*/
/*- IviPwrMeter_ReadChannel -*/
#define IVIPWRMETER_VAL_MAX_TIME_IMMEDIATE                                  (0x0L)
#define IVIPWRMETER_VAL_MAX_TIME_INFINITE                                   (0xFFFFFFFFUL)

/*- Defined values for ZeroStatus parameter of function -*/
/*- IviPwrMeter_IsZeroComplete -*/
#define IVIPWRMETER_VAL_ZERO_COMPLETE                                       (1L)
#define IVIPWRMETER_VAL_ZERO_IN_PROGRESS                                    (0L)
#define IVIPWRMETER_VAL_ZERO_STATUS_UNKNOWN                                 (-1L)

/*- Defined values for CalibrationStatus parameter of function -*/
/*- IviPwrMeter_IsCalibrationComplete -*/
#define IVIPWRMETER_VAL_CALIBRATION_COMPLETE                                (1L)
#define IVIPWRMETER_VAL_CALIBRATION_IN_PROGRESS                             (0L)
#define IVIPWRMETER_VAL_CALIBRATION_STATUS_UNKNOWN                          (-1L)



/****************************************************************************
 *------------------ IviPwrMeter Class Attribute Defines ----------------------*
 ****************************************************************************/

    /*- IVI Inherent Attributes -*/

        /*- User Options -*/
#define IVIPWRMETER_ATTR_CACHE                     IVI_ATTR_CACHE                         /* ViBoolean */
#define IVIPWRMETER_ATTR_RANGE_CHECK               IVI_ATTR_RANGE_CHECK                   /* ViBoolean */
#define IVIPWRMETER_ATTR_QUERY_INSTRUMENT_STATUS   IVI_ATTR_QUERY_INSTRUMENT_STATUS       /* ViBoolean */
#define IVIPWRMETER_ATTR_RECORD_COERCIONS          IVI_ATTR_RECORD_COERCIONS              /* ViBoolean */
#define IVIPWRMETER_ATTR_SIMULATE                  IVI_ATTR_SIMULATE                      /* ViBoolean */
#define IVIPWRMETER_ATTR_INTERCHANGE_CHECK         IVI_ATTR_INTERCHANGE_CHECK             /* ViBoolean */
#define IVIPWRMETER_ATTR_SPY                       IVI_ATTR_SPY                           /* ViBoolean */
#define IVIPWRMETER_ATTR_USE_SPECIFIC_SIMULATION   IVI_ATTR_USE_SPECIFIC_SIMULATION       /* ViBoolean */

	/* Instrument Capabilities */
#define IVIPWRMETER_ATTR_CHANNEL_COUNT             IVI_ATTR_CHANNEL_COUNT                 /* ViInt32,  read-only  */

        /*- Instrument Capabilities -*/
#define IVIPWRMETER_ATTR_GROUP_CAPABILITIES        IVI_ATTR_GROUP_CAPABILITIES            /* ViString, read-only */
#define IVIPWRMETER_ATTR_FUNCTION_CAPABILITIES     IVI_ATTR_FUNCTION_CAPABILITIES         /* ViString, read-only */

        /*- Class Driver Information -*/    
#define IVIPWRMETER_ATTR_CLASS_DRIVER_PREFIX                         IVI_ATTR_CLASS_DRIVER_PREFIX                       /* ViString, read-only */
#define IVIPWRMETER_ATTR_CLASS_DRIVER_VENDOR                         IVI_ATTR_CLASS_DRIVER_VENDOR                       /* ViString, read-only */
#define IVIPWRMETER_ATTR_CLASS_DRIVER_DESCRIPTION                    IVI_ATTR_CLASS_DRIVER_DESCRIPTION                  /* ViString, read-only */
#define IVIPWRMETER_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION     /* ViInt32,  read-only */
#define IVIPWRMETER_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION     /* ViInt32,  read-only */

        /*- Specific Driver Information -*/    
#define IVIPWRMETER_ATTR_SPECIFIC_DRIVER_PREFIX                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX                    /* ViString, read-only */
#define IVIPWRMETER_ATTR_SPECIFIC_DRIVER_LOCATOR                     IVI_ATTR_SPECIFIC_DRIVER_LOCATOR                   /* ViString, read-only */
#define IVIPWRMETER_ATTR_IO_RESOURCE_DESCRIPTOR                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR                    /* ViString, read-only */
#define IVIPWRMETER_ATTR_LOGICAL_NAME                                IVI_ATTR_LOGICAL_NAME                              /* ViString, read-only */
#define IVIPWRMETER_ATTR_SPECIFIC_DRIVER_VENDOR                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR                    /* ViString, read-only */
#define IVIPWRMETER_ATTR_SPECIFIC_DRIVER_DESCRIPTION                 IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION               /* ViString, read-only */
#define IVIPWRMETER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIPWRMETER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/    
#define IVIPWRMETER_ATTR_INSTRUMENT_FIRMWARE_REVISION     IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION   /* ViString, read-only */
#define IVIPWRMETER_ATTR_INSTRUMENT_MANUFACTURER          IVI_ATTR_INSTRUMENT_MANUFACTURER        /* ViString, read-only */
#define IVIPWRMETER_ATTR_INSTRUMENT_MODEL                 IVI_ATTR_INSTRUMENT_MODEL               /* ViString, read-only */
#define IVIPWRMETER_ATTR_SUPPORTED_INSTRUMENT_MODELS      IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS    /* ViString, read-only */
  
        /*- Version Information -*/
#define IVIPWRMETER_ATTR_CLASS_DRIVER_REVISION            IVI_ATTR_CLASS_DRIVER_REVISION          /* ViString, read-only */

#define IVIPWRMETER_ATTR_SPECIFIC_DRIVER_REVISION         IVI_ATTR_SPECIFIC_DRIVER_REVISION       /* ViString, read-only */

        /*- Driver Setup information -*/
#define IVIPWRMETER_ATTR_DRIVER_SETUP                     IVI_ATTR_DRIVER_SETUP                   /* ViString */

    /*- IviPwrMeter Fundamental Attributes -*/
#define IVIPWRMETER_ATTR_AVERAGING_AUTO_ENABLED         (IVI_CLASS_PUBLIC_ATTR_BASE + 3L)    /* ViBoolean */
#define IVIPWRMETER_ATTR_CORRECTION_FREQUENCY           (IVI_CLASS_PUBLIC_ATTR_BASE + 4L)    /* ViReal64 */
#define IVIPWRMETER_ATTR_OFFSET                         (IVI_CLASS_PUBLIC_ATTR_BASE + 5L)    /* ViReal64 */
#define IVIPWRMETER_ATTR_RANGE_AUTO_ENABLED             (IVI_CLASS_PUBLIC_ATTR_BASE + 2L)    /* ViBoolean */
#define IVIPWRMETER_ATTR_UNITS                          (IVI_CLASS_PUBLIC_ATTR_BASE + 1L)    /* ViInt32 */

    /*- IviPwrMeter Extended Attributes -*/
        /*- IviPwrMeterChannelAcquisition Extension Group -*/
#define IVIPWRMETER_ATTR_CHANNEL_ENABLED                (IVI_CLASS_PUBLIC_ATTR_BASE + 51L)   /* ViBoolean */

        /*- IviPwrMeterManualRange Extension Group -*/
#define IVIPWRMETER_ATTR_RANGE_LOWER                    (IVI_CLASS_PUBLIC_ATTR_BASE + 101L)  /* ViReal64 */
#define IVIPWRMETER_ATTR_RANGE_UPPER                    (IVI_CLASS_PUBLIC_ATTR_BASE + 102L)  /* ViReal64 */

        /*- IviPwrMeterTriggerSource Extension Group -*/
#define IVIPWRMETER_ATTR_TRIGGER_SOURCE                 (IVI_CLASS_PUBLIC_ATTR_BASE + 201L)  /* ViInt32 */

        /*- IviPwrMeterInternalTrigger Extension Group -*/
#define IVIPWRMETER_ATTR_INTERNAL_TRIGGER_EVENT_SOURCE  (IVI_CLASS_PUBLIC_ATTR_BASE + 251L)  /* ViString */
#define IVIPWRMETER_ATTR_INTERNAL_TRIGGER_LEVEL         (IVI_CLASS_PUBLIC_ATTR_BASE + 252L)  /* ViReal64 */
#define IVIPWRMETER_ATTR_INTERNAL_TRIGGER_SLOPE         (IVI_CLASS_PUBLIC_ATTR_BASE + 253L)  /* ViInt32 */

        /*- IviPwrMeterAveragingCount Extension Group -*/
#define IVIPWRMETER_ATTR_AVERAGING_COUNT                (IVI_CLASS_PUBLIC_ATTR_BASE + 301L)  /* ViInt32 */

        /*- IviPwrMeterDutyCycleCorrection Extension Group -*/
#define IVIPWRMETER_ATTR_DUTY_CYCLE_CORRECTION          (IVI_CLASS_PUBLIC_ATTR_BASE + 402L)  /* ViReal64 */
#define IVIPWRMETER_ATTR_DUTY_CYCLE_CORRECTION_ENABLED  (IVI_CLASS_PUBLIC_ATTR_BASE + 401L)  /* ViBoolean */

        /*- IviPwrMeterReferenceOscillator Extension Group -*/
#define IVIPWRMETER_ATTR_REF_OSCILLATOR_ENABLED         (IVI_CLASS_PUBLIC_ATTR_BASE + 501L)  /* ViBoolean */
#define IVIPWRMETER_ATTR_REF_OSCILLATOR_FREQUENCY       (IVI_CLASS_PUBLIC_ATTR_BASE + 502L)  /* ViReal64 */
#define IVIPWRMETER_ATTR_REF_OSCILLATOR_LEVEL           (IVI_CLASS_PUBLIC_ATTR_BASE + 503L)  /* ViReal64 */


/****************************************************************************
 *----------------- IviPwrMeter Class Attribute Value Defines -----------------*
 ****************************************************************************/
/*- Defined values for attribute IVIPWRMETER_ATTR_UNITS -*/
#define IVIPWRMETER_VAL_DBM                                                 (1L)
#define IVIPWRMETER_VAL_DBMV                                                (2L)
#define IVIPWRMETER_VAL_DBUV                                                (3L)
#define IVIPWRMETER_VAL_WATTS                                               (4L)
#define IVIPWRMETER_VAL_UNITS_CLASS_EXT_BASE                                (500L)
#define IVIPWRMETER_VAL_UNITS_SPECIFIC_EXT_BASE                             (1000L)

/*- Defined values for attribute IVIPWRMETER_ATTR_TRIGGER_SOURCE -*/
#define IVIPWRMETER_VAL_IMMEDIATE                                           (1L)
#define IVIPWRMETER_VAL_EXTERNAL                                            (2L)
#define IVIPWRMETER_VAL_INTERNAL                                            (3L)
#define IVIPWRMETER_VAL_SOFTWARE_TRIG                                       (4L)
#define IVIPWRMETER_VAL_TTL0                                                (100L)
#define IVIPWRMETER_VAL_TTL1                                                (101L)
#define IVIPWRMETER_VAL_TTL2                                                (102L)
#define IVIPWRMETER_VAL_TTL3                                                (103L)
#define IVIPWRMETER_VAL_TTL4                                                (104L)
#define IVIPWRMETER_VAL_TTL5                                                (105L)
#define IVIPWRMETER_VAL_TTL6                                                (106L)
#define IVIPWRMETER_VAL_TTL7                                                (107L)
#define IVIPWRMETER_VAL_ECL0                                                (200L)
#define IVIPWRMETER_VAL_ECL1                                                (201L)
#define IVIPWRMETER_VAL_PXI_STAR                                            (300L)
#define IVIPWRMETER_VAL_RTSI_0                                              (400L)
#define IVIPWRMETER_VAL_RTSI_1                                              (401L)
#define IVIPWRMETER_VAL_RTSI_2                                              (402L)
#define IVIPWRMETER_VAL_RTSI_3                                              (403L)
#define IVIPWRMETER_VAL_RTSI_4                                              (404L)
#define IVIPWRMETER_VAL_RTSI_5                                              (405L)
#define IVIPWRMETER_VAL_RTSI_6                                              (406L)
#define IVIPWRMETER_VAL_TRIGGER_SOURCE_CLASS_EXT_BASE                       (500L)
#define IVIPWRMETER_VAL_TRIGGER_SOURCE_SPECIFIC_EXT_BASE                    (1000L)

/*- Defined values for attribute IVIPWRMETER_ATTR_INTERNAL_TRIGGER_SLOPE -*/
#define IVIPWRMETER_VAL_NEGATIVE                                            (0L)
#define IVIPWRMETER_VAL_POSITIVE                                            (1L)
#define IVIPWRMETER_VAL_TRIGGER_SLOPE_CLASS_EXT_BASE                        (500L)
#define IVIPWRMETER_VAL_TRIGGER_SLOPE_SPECIFIC_EXT_BASE                     (1000L)
#define IVIPWRMETER_VAL_INTERNAL_TRIGGER_SLOPE_CLASS_EXT_BASE               (500L)
#define IVIPWRMETER_VAL_INTERNAL_TRIGGER_SLOPE_SPECIFIC_EXT_BASE            (1000L)

/****************************************************************************
*----------------- IviPwrMeter Function Parameter Value Defines -----------------*
****************************************************************************/
/*- Defined values for Configure Measurement -*/
#define IVIPWRMETER_VAL_OPERATOR_CLASS_EXT_BASE                             (500L)
#define IVIPWRMETER_VAL_OPERATOR_SPECIFIC_EXT_BASE                          (1000L)

/****************************************************************************
 *--------- IviPwrMeter Class Instrument Driver Function Declarations ---------*
 ****************************************************************************/
    /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviPwrMeter_init (ViRsrc logicalName, 
                                 ViBoolean idQuery, 
                                 ViBoolean resetDevice, 
                                 ViSession *vi);

ViStatus _VI_FUNC IviPwrMeter_close (ViSession vi);

ViStatus _VI_FUNC IviPwrMeter_reset (ViSession vi);

ViStatus _VI_FUNC IviPwrMeter_self_test (ViSession vi, 
                                      ViInt16 *selfTestResult, 
                                      ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviPwrMeter_error_query (ViSession vi, 
                                        ViInt32 *errorCode, 
                                        ViChar errorMessage[]);

ViStatus _VI_FUNC IviPwrMeter_error_message (ViSession vi, 
                                          ViStatus statusCode, 
                                          ViChar message[]);

ViStatus _VI_FUNC IviPwrMeter_revision_query (ViSession vi, 
                                           ViChar driverRev[], 
                                           ViChar instrRev[]);
    /*- Utility Functions -*/
ViStatus _VI_FUNC IviPwrMeter_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviPwrMeter_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviPwrMeter_Disable (ViSession vi);

    /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviPwrMeter_InitWithOptions (ViRsrc logicalName, 
                                            ViBoolean IDQuery,
                                            ViBoolean resetDevice, 
                                            ViConstString optionString, 
                                            ViSession *vi);

    /*- Set, Get, and Check Attribute Functions -*/

ViStatus _VI_FUNC IviPwrMeter_GetAttributeViInt32 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt32 *value);

ViStatus _VI_FUNC IviPwrMeter_SetAttributeViInt32 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt32 value);

ViStatus _VI_FUNC IviPwrMeter_CheckAttributeViInt32 (ViSession vi, 
                                                  ViConstString channelName,
                                                  ViAttr attributeId,
                                                  ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviPwrMeter_GetAttributeViInt64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt64 *value);

ViStatus _VI_FUNC IviPwrMeter_SetAttributeViInt64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt64 value);

ViStatus _VI_FUNC IviPwrMeter_CheckAttributeViInt64 (ViSession vi, 
                                                  ViConstString channelName,
                                                  ViAttr attributeId,
                                                  ViInt64 value);
#endif

ViStatus _VI_FUNC IviPwrMeter_GetAttributeViReal64 (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 *value);

ViStatus _VI_FUNC IviPwrMeter_SetAttributeViReal64 (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 value);

ViStatus _VI_FUNC IviPwrMeter_CheckAttributeViReal64 (ViSession vi, 
                                                   ViConstString channelName, 
                                                   ViAttr attributeId, 
                                                   ViReal64 value);

ViStatus _VI_FUNC IviPwrMeter_GetAttributeViString (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViInt32 bufferSize, 
                                                 ViChar value[]);

ViStatus _VI_FUNC IviPwrMeter_SetAttributeViString (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViConstString value);

ViStatus _VI_FUNC IviPwrMeter_CheckAttributeViString (ViSession vi, 
                                                   ViConstString channelName, 
                                                   ViAttr attributeId, 
                                                   ViConstString value); 

ViStatus _VI_FUNC IviPwrMeter_GetAttributeViBoolean (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean *value);

ViStatus _VI_FUNC IviPwrMeter_SetAttributeViBoolean (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean value);

ViStatus _VI_FUNC IviPwrMeter_CheckAttributeViBoolean (ViSession vi, 
                                                    ViConstString channelName, 
                                                    ViAttr attributeId, 
                                                    ViBoolean value);

ViStatus _VI_FUNC IviPwrMeter_GetAttributeViSession (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViSession *value);

ViStatus _VI_FUNC IviPwrMeter_SetAttributeViSession (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViSession value);

ViStatus _VI_FUNC IviPwrMeter_CheckAttributeViSession (ViSession vi, 
                                                    ViConstString channelName, 
                                                    ViAttr attributeId, 
                                                    ViSession value);

    /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviPwrMeter_LockSession (ViSession vi, 
                                        ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviPwrMeter_UnlockSession (ViSession vi, 
                                          ViBoolean *callerHasLock);

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviPwrMeter_GetError (ViSession vi, 
                                   ViStatus *errorCode, 
                                   ViInt32 bufferSize, 
                                   ViChar description[]);

ViStatus _VI_FUNC IviPwrMeter_ClearError (ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviPwrMeter_GetNextInterchangeWarning (ViSession vi, 
                                                      ViInt32 bufferSize,
                                                      ViChar warning[]);

ViStatus _VI_FUNC IviPwrMeter_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviPwrMeter_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviPwrMeter_GetNextCoercionRecord (ViSession vi,
                                                  ViInt32 bufferSize, 
                                                  ViChar record[]);

ViStatus _VI_FUNC IviPwrMeter_GetSpecificDriverCHandle (ViSession vi,
                                                     ViSession* specificDriverCHandle);

    /*- IviPwrMeter Fundamental Capabilities -*/
ViStatus _VI_FUNC IviPwrMeter_Abort (ViSession vi);

ViStatus _VI_FUNC IviPwrMeter_ConfigureAveragingAutoEnabled (ViSession vi,
                                                             ViConstString Channel,
                                                             ViBoolean AveragingAutoEnabled);

ViStatus _VI_FUNC IviPwrMeter_ConfigureCorrectionFrequency (ViSession vi,
                                                            ViConstString Channel,
                                                            ViReal64 CorrectionFrequency);

ViStatus _VI_FUNC IviPwrMeter_ConfigureMeasurement (ViSession vi,
                                                    ViInt32 Operator,
                                                    ViConstString Operand1,
                                                    ViConstString Operand2);

ViStatus _VI_FUNC IviPwrMeter_ConfigureOffset (ViSession vi,
                                               ViConstString Channel,
                                               ViReal64 Offset);

ViStatus _VI_FUNC IviPwrMeter_ConfigureRangeAutoEnabled (ViSession vi,
                                                         ViConstString Channel,
                                                         ViBoolean RangeAutoEnabled);

ViStatus _VI_FUNC IviPwrMeter_ConfigureUnits (ViSession vi,
                                              ViInt32 Units);

ViStatus _VI_FUNC IviPwrMeter_Fetch (ViSession vi,
                                     ViReal64* Result);

ViStatus _VI_FUNC IviPwrMeter_GetChannelName (ViSession vi,
                                              ViInt32 ChannelIndex,
                                              ViInt32 ChannelNameBufferSize,
                                              ViChar ChannelName[]);

ViStatus _VI_FUNC IviPwrMeter_Initiate (ViSession vi);

ViStatus _VI_FUNC IviPwrMeter_IsMeasurementComplete (ViSession vi,
                                                     ViInt32* MeasurementStatus);

ViStatus _VI_FUNC IviPwrMeter_QueryResultRangeType (ViSession vi,
                                                    ViReal64 MeasurementValue,
                                                    ViInt32* RangeType);

ViStatus _VI_FUNC IviPwrMeter_Read (ViSession vi,
                                    ViInt32 MaxTime,
                                    ViReal64* Result);


    /*- IviPwrMeterChannelAcquisition Extension Group -*/
ViStatus _VI_FUNC IviPwrMeter_ConfigureChannelEnabled (ViSession vi,
                                                       ViConstString Channel,
                                                       ViBoolean ChannelEnabled);

ViStatus _VI_FUNC IviPwrMeter_FetchChannel (ViSession vi,
                                            ViConstString Channel,
                                            ViReal64* Result);

ViStatus _VI_FUNC IviPwrMeter_ReadChannel (ViSession vi,
                                           ViConstString Channel,
                                           ViInt32 MaxTime,
                                           ViReal64* Result);


    /*- IviPwrMeterManualRange Extension Group -*/
ViStatus _VI_FUNC IviPwrMeter_ConfigureRange (ViSession vi,
                                              ViConstString Channel,
                                              ViReal64 RangeLower,
                                              ViReal64 RangeUpper);


    /*- IviPwrMeterTriggerSource Extension Group -*/
ViStatus _VI_FUNC IviPwrMeter_ConfigureTriggerSource (ViSession vi,
                                                      ViInt32 TriggerSource);


    /*- IviPwrMeterInternalTrigger Extension Group -*/
ViStatus _VI_FUNC IviPwrMeter_ConfigureInternalTrigger (ViSession vi,
                                                        ViConstString EventSource,
                                                        ViInt32 Slope);

ViStatus _VI_FUNC IviPwrMeter_ConfigureInternalTriggerLevel (ViSession vi,
                                                             ViReal64 TriggerLevel);


    /*- IviPwrMeterSoftwareTrigger Extension Group -*/
ViStatus _VI_FUNC IviPwrMeter_SendSoftwareTrigger (ViSession vi);


    /*- IviPwrMeterAveragingCount Extension Group -*/
ViStatus _VI_FUNC IviPwrMeter_ConfigureAveragingCount (ViSession vi,
                                                       ViConstString Channel,
                                                       ViInt32 Count);


    /*- IviPwrMeterZeroCorrection Extension Group -*/
ViStatus _VI_FUNC IviPwrMeter_IsZeroComplete (ViSession vi,
                                              ViInt32* ZeroStatus);

ViStatus _VI_FUNC IviPwrMeter_Zero (ViSession vi,
                                    ViConstString Channel);

ViStatus _VI_FUNC IviPwrMeter_ZeroAllChannels (ViSession vi);


    /*- IviPwrMeterDutyCycleCorrection Extension Group -*/
ViStatus _VI_FUNC IviPwrMeter_ConfigureDutyCycleCorrection (ViSession vi,
                                                            ViConstString Channel,
                                                            ViBoolean CorrectionEnabled,
                                                            ViReal64 Correction);


    /*- IviPwrMeterCalibration Extension Group -*/
ViStatus _VI_FUNC IviPwrMeter_Calibrate (ViSession vi,
                                         ViConstString Channel);

ViStatus _VI_FUNC IviPwrMeter_IsCalibrationComplete (ViSession vi,
                                                     ViInt32* CalibrationStatus);


    /*- IviPwrMeterReferenceOscillator Extension Group -*/
ViStatus _VI_FUNC IviPwrMeter_ConfigureRefOscillator (ViSession vi,
                                                      ViReal64 Frequency,
                                                      ViReal64 Level);

ViStatus _VI_FUNC IviPwrMeter_ConfigureRefOscillatorEnabled (ViSession vi,
                                                             ViBoolean RefOscillatorEnabled);



/****************************************************************************
 *--------------- IviPwrMeter Class Error And Completion Codes ----------------*
 ****************************************************************************/
#define IVIPWRMETER_WARN_UNDER_RANGE             (IVI_CLASS_WARN_BASE + 0x0001L)
#define IVIPWRMETER_WARN_OVER_RANGE              (IVI_CLASS_WARN_BASE + 0x0002L)

#define IVIPWRMETER_ERROR_CHANNEL_NOT_ENABLED    (IVI_CLASS_ERROR_BASE + 0x0001L)
#define IVIPWRMETER_ERROR_MAX_TIME_EXCEEDED      (IVI_CLASS_ERROR_BASE + 0x0020L)
#define IVIPWRMETER_ERROR_TRIGGER_NOT_SOFTWARE   (IVI_CROSS_CLASS_ERROR_BASE + 0x0001L)



#define IVIPWRMETER_WARNMSG_UNDER_RANGE          "Measurement is under range."
#define IVIPWRMETER_WARNMSG_OVER_RANGE           "Measurement is over range."

#define IVIPWRMETER_ERRMSG_CHANNEL_NOT_ENABLED   "The specified channel is not enabled for measurement."
#define IVIPWRMETER_ERRMSG_MAX_TIME_EXCEEDED     "Maximum timeout exceeded before operation could complete."
#define IVIPWRMETER_ERRMSG_TRIGGER_NOT_SOFTWARE  "The trigger source is not set to software trigger."



#define IVIPWRMETER_ERROR_CODES_AND_MSGS \
    {IVIPWRMETER_WARN_UNDER_RANGE,           IVIPWRMETER_WARNMSG_UNDER_RANGE},\
    {IVIPWRMETER_WARN_OVER_RANGE,            IVIPWRMETER_WARNMSG_OVER_RANGE},\
    {IVIPWRMETER_ERROR_CHANNEL_NOT_ENABLED,  IVIPWRMETER_ERRMSG_CHANNEL_NOT_ENABLED},\
    {IVIPWRMETER_ERROR_MAX_TIME_EXCEEDED,    IVIPWRMETER_ERRMSG_MAX_TIME_EXCEEDED},\
    {IVIPWRMETER_ERROR_TRIGGER_NOT_SOFTWARE, IVIPWRMETER_ERRMSG_TRIGGER_NOT_SOFTWARE}


/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

#endif /* IVIPWRMETER_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviRFSigGen.h sha256=f5be32c3b799c07fbff128af37bb80d81bbfd5f9c630c34b5f1fdb117893d78c bytes=63760 -->
## FILE: imports/include/IviRFSigGen.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviRFSigGen.h`
- sha256: `f5be32c3b799c07fbff128af37bb80d81bbfd5f9c630c34b5f1fdb117893d78c`
- bytes: 63760

````c
/****************************************************************************
 *                         IVIRFSIGGEN                               
 *---------------------------------------------------------------------------
 *    Copyright (c) 2009-2020 National Instruments.  All Rights Reserved.        
 *---------------------------------------------------------------------------
 *                                                                          
 * Title:       IviRFSigGen.h                                                    
 * Purpose:     IviRFSigGen Class declarations for the Base and Extended  
 *              IviRFSigGen Capabilities.                                        
 ****************************************************************************/

#ifndef IVIRFSIGGEN_HEADER
#define IVIRFSIGGEN_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVIRFSIGGEN_MAJOR_VERSION              (4L)
#define IVIRFSIGGEN_MINOR_VERSION              (0L)

#define IVIRFSIGGEN_CLASS_SPEC_MAJOR_VERSION   (2L)
#define IVIRFSIGGEN_CLASS_SPEC_MINOR_VERSION   (0L)

#define IVIRFSIGGEN_DRIVER_VENDOR              "National Instruments"
#ifdef	_IVI_mswin64_
#define IVIRFSIGGEN_DRIVER_DESCRIPTION         "IviRFSigGen Class Driver [Compiled for 64-bit.]"
#else
#define IVIRFSIGGEN_DRIVER_DESCRIPTION         "IviRFSigGen Class Driver"
#endif

/****************************************************************************
 *------------------------------ Useful Macros -----------------------------*
 ****************************************************************************/
/*- Defined values for MaxTimeMilliseconds parameter of function -*/
/*- IviRFSigGen_WaitUntilSettled -*/
#define IVIRFSIGGEN_VAL_MAX_TIME_IMMEDIATE                                  (0L)
#define IVIRFSIGGEN_VAL_MAX_TIME_INFINITE                                  (0xFFFFFFFFUL)



/****************************************************************************
 *------------------ IviRFSigGen Class Attribute Defines ----------------------*
 ****************************************************************************/

    /*- IVI Inherent Attributes -*/

        /*- User Options -*/
#define IVIRFSIGGEN_ATTR_CACHE                     IVI_ATTR_CACHE                         /* ViBoolean */
#define IVIRFSIGGEN_ATTR_RANGE_CHECK               IVI_ATTR_RANGE_CHECK                   /* ViBoolean */
#define IVIRFSIGGEN_ATTR_QUERY_INSTRUMENT_STATUS   IVI_ATTR_QUERY_INSTRUMENT_STATUS       /* ViBoolean */
#define IVIRFSIGGEN_ATTR_RECORD_COERCIONS          IVI_ATTR_RECORD_COERCIONS              /* ViBoolean */
#define IVIRFSIGGEN_ATTR_SIMULATE                  IVI_ATTR_SIMULATE                      /* ViBoolean */
#define IVIRFSIGGEN_ATTR_INTERCHANGE_CHECK         IVI_ATTR_INTERCHANGE_CHECK             /* ViBoolean */
#define IVIRFSIGGEN_ATTR_SPY                       IVI_ATTR_SPY                           /* ViBoolean */
#define IVIRFSIGGEN_ATTR_USE_SPECIFIC_SIMULATION   IVI_ATTR_USE_SPECIFIC_SIMULATION       /* ViBoolean */

	/* Instrument Capabilities */
#define IVIRFSIGGEN_ATTR_CHANNEL_COUNT             IVI_ATTR_CHANNEL_COUNT                 /* ViInt32,  read-only  */

        /*- Instrument Capabilities -*/
#define IVIRFSIGGEN_ATTR_GROUP_CAPABILITIES        IVI_ATTR_GROUP_CAPABILITIES            /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_FUNCTION_CAPABILITIES     IVI_ATTR_FUNCTION_CAPABILITIES         /* ViString, read-only */

        /*- Class Driver Information -*/    
#define IVIRFSIGGEN_ATTR_CLASS_DRIVER_PREFIX                         IVI_ATTR_CLASS_DRIVER_PREFIX                       /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_CLASS_DRIVER_VENDOR                         IVI_ATTR_CLASS_DRIVER_VENDOR                       /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_CLASS_DRIVER_DESCRIPTION                    IVI_ATTR_CLASS_DRIVER_DESCRIPTION                  /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION     /* ViInt32,  read-only */
#define IVIRFSIGGEN_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION     /* ViInt32,  read-only */

        /*- Specific Driver Information -*/    
#define IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_PREFIX                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX                    /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_LOCATOR                     IVI_ATTR_SPECIFIC_DRIVER_LOCATOR                   /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_IO_RESOURCE_DESCRIPTOR                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR                    /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_LOGICAL_NAME                                IVI_ATTR_LOGICAL_NAME                              /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_VENDOR                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR                    /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_DESCRIPTION                 IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION               /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/    
#define IVIRFSIGGEN_ATTR_INSTRUMENT_FIRMWARE_REVISION     IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION   /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_INSTRUMENT_MANUFACTURER          IVI_ATTR_INSTRUMENT_MANUFACTURER        /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_INSTRUMENT_MODEL                 IVI_ATTR_INSTRUMENT_MODEL               /* ViString, read-only */
#define IVIRFSIGGEN_ATTR_SUPPORTED_INSTRUMENT_MODELS      IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS    /* ViString, read-only */
  
        /*- Version Information -*/
#define IVIRFSIGGEN_ATTR_CLASS_DRIVER_REVISION            IVI_ATTR_CLASS_DRIVER_REVISION          /* ViString, read-only */

#define IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_REVISION         IVI_ATTR_SPECIFIC_DRIVER_REVISION       /* ViString, read-only */

        /*- Driver Setup information -*/
#define IVIRFSIGGEN_ATTR_DRIVER_SETUP                     IVI_ATTR_DRIVER_SETUP                   /* ViString */

    /*- IviRFSigGen Fundamental Attributes -*/
#define IVIRFSIGGEN_ATTR_FREQUENCY                                      (IVI_CLASS_PUBLIC_ATTR_BASE + 1L)    /* ViReal64 */
#define IVIRFSIGGEN_ATTR_POWER_LEVEL                                    (IVI_CLASS_PUBLIC_ATTR_BASE + 2L)    /* ViReal64 */
#define IVIRFSIGGEN_ATTR_ALC_ENABLED                                    (IVI_CLASS_PUBLIC_ATTR_BASE + 3L)    /* ViBoolean */
#define IVIRFSIGGEN_ATTR_OUTPUT_ENABLED                                 (IVI_CLASS_PUBLIC_ATTR_BASE + 4L)    /* ViBoolean */

    /*- IviRFSigGen Extended Attributes -*/
        /*- IviRFSigGenModulateAM Extension Group -*/
#define IVIRFSIGGEN_ATTR_AM_ENABLED                                     (IVI_CLASS_PUBLIC_ATTR_BASE + 11L)   /* ViBoolean */
#define IVIRFSIGGEN_ATTR_AM_SOURCE                                      (IVI_CLASS_PUBLIC_ATTR_BASE + 12L)   /* ViString */
#define IVIRFSIGGEN_ATTR_AM_SCALING                                     (IVI_CLASS_PUBLIC_ATTR_BASE + 13L)   /* ViInt32 */
#define IVIRFSIGGEN_ATTR_AM_EXTERNAL_COUPLING                           (IVI_CLASS_PUBLIC_ATTR_BASE + 14L)   /* ViInt32 */
#define IVIRFSIGGEN_ATTR_AM_NOMINAL_VOLTAGE                             (IVI_CLASS_PUBLIC_ATTR_BASE + 15L)   /* ViReal64 */
#define IVIRFSIGGEN_ATTR_AM_DEPTH                                       (IVI_CLASS_PUBLIC_ATTR_BASE + 16L)   /* ViReal64 */

        /*- IviRFSigGenModulateFM Extension Group -*/
#define IVIRFSIGGEN_ATTR_FM_ENABLED                                     (IVI_CLASS_PUBLIC_ATTR_BASE + 21L)   /* ViBoolean */
#define IVIRFSIGGEN_ATTR_FM_SOURCE                                      (IVI_CLASS_PUBLIC_ATTR_BASE + 22L)   /* ViString */
#define IVIRFSIGGEN_ATTR_FM_EXTERNAL_COUPLING                           (IVI_CLASS_PUBLIC_ATTR_BASE + 23L)   /* ViInt32 */
#define IVIRFSIGGEN_ATTR_FM_NOMINAL_VOLTAGE                             (IVI_CLASS_PUBLIC_ATTR_BASE + 24L)   /* ViReal64 */
#define IVIRFSIGGEN_ATTR_FM_DEVIATION                                   (IVI_CLASS_PUBLIC_ATTR_BASE + 25L)   /* ViReal64 */

        /*- IviRFSigGenModulatePM Extension Group -*/
#define IVIRFSIGGEN_ATTR_PM_ENABLED                                     (IVI_CLASS_PUBLIC_ATTR_BASE + 31L)   /* ViBoolean */
#define IVIRFSIGGEN_ATTR_PM_SOURCE                                      (IVI_CLASS_PUBLIC_ATTR_BASE + 32L)   /* ViString */
#define IVIRFSIGGEN_ATTR_PM_EXTERNAL_COUPLING                           (IVI_CLASS_PUBLIC_ATTR_BASE + 33L)   /* ViInt32 */
#define IVIRFSIGGEN_ATTR_PM_NOMINAL_VOLTAGE                             (IVI_CLASS_PUBLIC_ATTR_BASE + 34L)   /* ViReal64 */
#define IVIRFSIGGEN_ATTR_PM_DEVIATION                                   (IVI_CLASS_PUBLIC_ATTR_BASE + 35L)   /* ViReal64 */

        /*- IviRFSigGenAnalogModulationSource Extension Group -*/
#define IVIRFSIGGEN_ATTR_ANALOG_MODULATION_SOURCE_COUNT                 (IVI_CLASS_PUBLIC_ATTR_BASE + 41L)   /* ViInt32 */

        /*- IviRFSigGenModulatePulse Extension Group -*/
#define IVIRFSIGGEN_ATTR_PULSE_MODULATION_ENABLED                       (IVI_CLASS_PUBLIC_ATTR_BASE + 51L)   /* ViBoolean */
#define IVIRFSIGGEN_ATTR_PULSE_MODULATION_SOURCE                        (IVI_CLASS_PUBLIC_ATTR_BASE + 52L)   /* ViInt32 */
#define IVIRFSIGGEN_ATTR_PULSE_MODULATION_EXTERNAL_POLARITY             (IVI_CLASS_PUBLIC_ATTR_BASE + 53L)   /* ViInt32 */

        /*- IviRFSigGenLFGenerator Extension Group -*/
#define IVIRFSIGGEN_ATTR_ACTIVE_LF_GENERATOR                            (IVI_CLASS_PUBLIC_ATTR_BASE + 101L)  /* ViString */
#define IVIRFSIGGEN_ATTR_LF_GENERATOR_COUNT                             (IVI_CLASS_PUBLIC_ATTR_BASE + 104L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_LF_GENERATOR_FREQUENCY                         (IVI_CLASS_PUBLIC_ATTR_BASE + 102L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_LF_GENERATOR_WAVEFORM                          (IVI_CLASS_PUBLIC_ATTR_BASE + 103L)  /* ViInt32 */

        /*- IviRFSigGenLFGeneratorOutput Extension Group -*/
#define IVIRFSIGGEN_ATTR_LF_GENERATOR_OUTPUT_AMPLITUDE                  (IVI_CLASS_PUBLIC_ATTR_BASE + 111L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_LF_GENERATOR_OUTPUT_ENABLED                    (IVI_CLASS_PUBLIC_ATTR_BASE + 112L)  /* ViBoolean */

        /*- IviRFSigGenPulseGenerator Extension Group -*/
#define IVIRFSIGGEN_ATTR_PULSE_INTERNAL_TRIGGER_PERIOD                  (IVI_CLASS_PUBLIC_ATTR_BASE + 121L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_PULSE_WIDTH                                    (IVI_CLASS_PUBLIC_ATTR_BASE + 122L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_PULSE_GATING_ENABLED                           (IVI_CLASS_PUBLIC_ATTR_BASE + 123L)  /* ViBoolean */
#define IVIRFSIGGEN_ATTR_PULSE_TRIGGER_SOURCE                           (IVI_CLASS_PUBLIC_ATTR_BASE + 124L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_PULSE_EXTERNAL_TRIGGER_SLOPE                   (IVI_CLASS_PUBLIC_ATTR_BASE + 125L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_PULSE_EXTERNAL_TRIGGER_DELAY                   (IVI_CLASS_PUBLIC_ATTR_BASE + 126L)  /* ViReal64 */

        /*- IviRFSigGenPulseDoubleGenerator Extension Group -*/
#define IVIRFSIGGEN_ATTR_PULSE_DOUBLE_ENABLED                           (IVI_CLASS_PUBLIC_ATTR_BASE + 131L)  /* ViBoolean */
#define IVIRFSIGGEN_ATTR_PULSE_DOUBLE_DELAY                             (IVI_CLASS_PUBLIC_ATTR_BASE + 132L)  /* ViReal64 */

        /*- IviRFSigGenPulseGeneratorOutput Extension Group -*/
#define IVIRFSIGGEN_ATTR_PULSE_OUTPUT_POLARITY                          (IVI_CLASS_PUBLIC_ATTR_BASE + 141L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_PULSE_OUTPUT_ENABLED                           (IVI_CLASS_PUBLIC_ATTR_BASE + 142L)  /* ViBoolean */

        /*- IviRFSigGenSweep Extension Group -*/
#define IVIRFSIGGEN_ATTR_SWEEP_MODE                                     (IVI_CLASS_PUBLIC_ATTR_BASE + 201L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_SWEEP_TRIGGER_SOURCE                           (IVI_CLASS_PUBLIC_ATTR_BASE + 202L)  /* ViInt32 */

        /*- IviRFSigGenFrequencySweep Extension Group -*/
#define IVIRFSIGGEN_ATTR_FREQUENCY_SWEEP_START                          (IVI_CLASS_PUBLIC_ATTR_BASE + 211L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_FREQUENCY_SWEEP_STOP                           (IVI_CLASS_PUBLIC_ATTR_BASE + 212L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_FREQUENCY_SWEEP_TIME                           (IVI_CLASS_PUBLIC_ATTR_BASE + 213L)  /* ViReal64 */

        /*- IviRFSigGenPowerSweep Extension Group -*/
#define IVIRFSIGGEN_ATTR_POWER_SWEEP_START                              (IVI_CLASS_PUBLIC_ATTR_BASE + 221L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_POWER_SWEEP_STOP                               (IVI_CLASS_PUBLIC_ATTR_BASE + 222L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_POWER_SWEEP_TIME                               (IVI_CLASS_PUBLIC_ATTR_BASE + 223L)  /* ViReal64 */

        /*- IviRFSigGenFrequencyStep Extension Group -*/
#define IVIRFSIGGEN_ATTR_FREQUENCY_STEP_START                           (IVI_CLASS_PUBLIC_ATTR_BASE + 241L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_FREQUENCY_STEP_STOP                            (IVI_CLASS_PUBLIC_ATTR_BASE + 242L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_FREQUENCY_STEP_SCALING                         (IVI_CLASS_PUBLIC_ATTR_BASE + 243L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_FREQUENCY_STEP_SIZE                            (IVI_CLASS_PUBLIC_ATTR_BASE + 244L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_FREQUENCY_STEP_SINGLE_STEP_ENABLED             (IVI_CLASS_PUBLIC_ATTR_BASE + 245L)  /* ViBoolean */
#define IVIRFSIGGEN_ATTR_FREQUENCY_STEP_DWELL                           (IVI_CLASS_PUBLIC_ATTR_BASE + 246L)  /* ViReal64 */

        /*- IviRFSigGenPowerStep Extension Group -*/
#define IVIRFSIGGEN_ATTR_POWER_STEP_START                               (IVI_CLASS_PUBLIC_ATTR_BASE + 261L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_POWER_STEP_STOP                                (IVI_CLASS_PUBLIC_ATTR_BASE + 262L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_POWER_STEP_SIZE                                (IVI_CLASS_PUBLIC_ATTR_BASE + 263L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_POWER_STEP_SINGLE_STEP_ENABLED                 (IVI_CLASS_PUBLIC_ATTR_BASE + 264L)  /* ViBoolean */
#define IVIRFSIGGEN_ATTR_POWER_STEP_DWELL                               (IVI_CLASS_PUBLIC_ATTR_BASE + 265L)  /* ViReal64 */

        /*- IviRFSigGenList Extension Group -*/
#define IVIRFSIGGEN_ATTR_LIST_SELECTED_NAME                             (IVI_CLASS_PUBLIC_ATTR_BASE + 281L)  /* ViString */
#define IVIRFSIGGEN_ATTR_LIST_SINGLE_STEP_ENABLED                       (IVI_CLASS_PUBLIC_ATTR_BASE + 282L)  /* ViBoolean */
#define IVIRFSIGGEN_ATTR_LIST_DWELL                                     (IVI_CLASS_PUBLIC_ATTR_BASE + 283L)  /* ViReal64 */

        /*- IviRFSigGenALC Extension Group -*/
#define IVIRFSIGGEN_ATTR_ALC_SOURCE                                     (IVI_CLASS_PUBLIC_ATTR_BASE + 301L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_ALC_BANDWIDTH                                  (IVI_CLASS_PUBLIC_ATTR_BASE + 302L)  /* ViReal64 */

        /*- IviRFSigGenReferenceOscillator Extension Group -*/
#define IVIRFSIGGEN_ATTR_REFERENCE_OSCILLATOR_SOURCE                    (IVI_CLASS_PUBLIC_ATTR_BASE + 321L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_REFERENCE_OSCILLATOR_EXTERNAL_FREQUENCY        (IVI_CLASS_PUBLIC_ATTR_BASE + 322L)  /* ViReal64 */

        /*- IviRFSigGenModulateIQ Extension Group -*/
#define IVIRFSIGGEN_ATTR_IQ_ENABLED                                     (IVI_CLASS_PUBLIC_ATTR_BASE + 401L)  /* ViBoolean */
#define IVIRFSIGGEN_ATTR_IQ_NOMINAL_VOLTAGE                             (IVI_CLASS_PUBLIC_ATTR_BASE + 402L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_IQ_SOURCE                                      (IVI_CLASS_PUBLIC_ATTR_BASE + 403L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_IQ_SWAP_ENABLED                                (IVI_CLASS_PUBLIC_ATTR_BASE + 404L)  /* ViBoolean */

        /*- IviRFSigGenIQImpairment Extension Group -*/
#define IVIRFSIGGEN_ATTR_IQ_IMPAIRMENT_ENABLED                          (IVI_CLASS_PUBLIC_ATTR_BASE + 421L)  /* ViBoolean */
#define IVIRFSIGGEN_ATTR_IQ_I_OFFSET                                    (IVI_CLASS_PUBLIC_ATTR_BASE + 422L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_IQ_Q_OFFSET                                    (IVI_CLASS_PUBLIC_ATTR_BASE + 423L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_IQ_RATIO                                       (IVI_CLASS_PUBLIC_ATTR_BASE + 424L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_IQ_SKEW                                        (IVI_CLASS_PUBLIC_ATTR_BASE + 425L)  /* ViReal64 */

        /*- IviRFSigGenArbGenerator Extension Group -*/
#define IVIRFSIGGEN_ATTR_ARB_SELECTED_WAVEFORM                          (IVI_CLASS_PUBLIC_ATTR_BASE + 451L)  /* ViString */
#define IVIRFSIGGEN_ATTR_ARB_CLOCK_FREQUENCY                            (IVI_CLASS_PUBLIC_ATTR_BASE + 452L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_ARB_FILTER_FREQUENCY                           (IVI_CLASS_PUBLIC_ATTR_BASE + 453L)  /* ViReal64 */
#define IVIRFSIGGEN_ATTR_ARB_MAX_NUMBER_WAVEFORMS                       (IVI_CLASS_PUBLIC_ATTR_BASE + 454L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_ARB_WAVEFORM_QUANTUM                           (IVI_CLASS_PUBLIC_ATTR_BASE + 455L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_ARB_WAVEFORM_SIZE_MIN                          (IVI_CLASS_PUBLIC_ATTR_BASE + 456L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_ARB_WAVEFORM_SIZE_MAX                          (IVI_CLASS_PUBLIC_ATTR_BASE + 457L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_ARB_TRIGGER_SOURCE                             (IVI_CLASS_PUBLIC_ATTR_BASE + 458L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_ARB_EXTERNAL_TRIGGER_SLOPE                     (IVI_CLASS_PUBLIC_ATTR_BASE + 459L)  /* ViInt32 */

        /*- IviRFSigGenDigitalModulationBase Extension Group -*/
#define IVIRFSIGGEN_ATTR_DIGITAL_MODULATION_BASE_STANDARD_COUNT         (IVI_CLASS_PUBLIC_ATTR_BASE + 501L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_DIGITAL_MODULATION_BASE_SELECTED_STANDARD      (IVI_CLASS_PUBLIC_ATTR_BASE + 502L)  /* ViString */
#define IVIRFSIGGEN_ATTR_DIGITAL_MODULATION_BASE_DATA_SOURCE            (IVI_CLASS_PUBLIC_ATTR_BASE + 503L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_DIGITAL_MODULATION_BASE_PRBS_TYPE              (IVI_CLASS_PUBLIC_ATTR_BASE + 504L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_DIGITAL_MODULATION_BASE_SELECTED_BIT_SEQUENCE  (IVI_CLASS_PUBLIC_ATTR_BASE + 505L)  /* ViString */
#define IVIRFSIGGEN_ATTR_DIGITAL_MODULATION_BASE_CLOCK_SOURCE           (IVI_CLASS_PUBLIC_ATTR_BASE + 506L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_DIGITAL_MODULATION_BASE_EXTERNAL_CLOCK_TYPE    (IVI_CLASS_PUBLIC_ATTR_BASE + 507L)  /* ViInt32 */

        /*- IviRFSigGenCDMABase Extension Group -*/
#define IVIRFSIGGEN_ATTR_CDMA_STANDARD_COUNT                            (IVI_CLASS_PUBLIC_ATTR_BASE + 601L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_CDMA_SELECTED_STANDARD                         (IVI_CLASS_PUBLIC_ATTR_BASE + 602L)  /* ViString */
#define IVIRFSIGGEN_ATTR_CDMA_TRIGGER_SOURCE                            (IVI_CLASS_PUBLIC_ATTR_BASE + 603L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_CDMA_EXTERNAL_TRIGGER_SLOPE                    (IVI_CLASS_PUBLIC_ATTR_BASE + 604L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_CDMA_TEST_MODEL_COUNT                          (IVI_CLASS_PUBLIC_ATTR_BASE + 605L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_CDMA_SELECTED_TEST_MODEL                       (IVI_CLASS_PUBLIC_ATTR_BASE + 606L)  /* ViString */
#define IVIRFSIGGEN_ATTR_CDMA_CLOCK_SOURCE                              (IVI_CLASS_PUBLIC_ATTR_BASE + 607L)  /* ViInt32 */

        /*- IviRFSigGenTDMABase Extension Group -*/
#define IVIRFSIGGEN_ATTR_TDMA_STANDARD_COUNT                            (IVI_CLASS_PUBLIC_ATTR_BASE + 701L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_TDMA_SELECTED_STANDARD                         (IVI_CLASS_PUBLIC_ATTR_BASE + 702L)  /* ViString */
#define IVIRFSIGGEN_ATTR_TDMA_TRIGGER_SOURCE                            (IVI_CLASS_PUBLIC_ATTR_BASE + 703L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_TDMA_EXTERNAL_TRIGGER_SLOPE                    (IVI_CLASS_PUBLIC_ATTR_BASE + 704L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_TDMA_FRAME_COUNT                               (IVI_CLASS_PUBLIC_ATTR_BASE + 705L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_TDMA_SELECTED_FRAME                            (IVI_CLASS_PUBLIC_ATTR_BASE + 706L)  /* ViString */
#define IVIRFSIGGEN_ATTR_TDMA_CLOCK_SOURCE                              (IVI_CLASS_PUBLIC_ATTR_BASE + 707L)  /* ViInt32 */
#define IVIRFSIGGEN_ATTR_TDMA_EXTERNAL_CLOCK_TYPE                       (IVI_CLASS_PUBLIC_ATTR_BASE + 708L)  /* ViInt32 */


/****************************************************************************
 *----------------- IviRFSigGen Class Attribute Value Defines -----------------*
 ****************************************************************************/
/*- Defined values for attribute IVIRFSIGGEN_ATTR_AM_SCALING -*/
#define IVIRFSIGGEN_VAL_AM_SCALING_LINEAR                                   (0L)
#define IVIRFSIGGEN_VAL_AM_SCALING_LOGARITHMIC                              (1L)
#define IVIRFSIGGEN_VAL_AM_SCALING_CLASS_EXT_BASE                           (500L)
#define IVIRFSIGGEN_VAL_AM_SCALING_SPECIFIC_EXT_BASE                        (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_AM_EXTERNAL_COUPLING -*/
#define IVIRFSIGGEN_VAL_AM_EXTERNAL_COUPLING_AC                             (0L)
#define IVIRFSIGGEN_VAL_AM_EXTERNAL_COUPLING_DC                             (1L)
#define IVIRFSIGGEN_VAL_AM_EXTERNAL_COUPLING_CLASS_EXT_BASE                 (500L)
#define IVIRFSIGGEN_VAL_AM_EXTERNAL_COUPLING_SPECIFIC_EXT_BASE              (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_FM_EXTERNAL_COUPLING -*/
#define IVIRFSIGGEN_VAL_FM_EXTERNAL_COUPLING_AC                             (0L)
#define IVIRFSIGGEN_VAL_FM_EXTERNAL_COUPLING_DC                             (1L)
#define IVIRFSIGGEN_VAL_FM_EXTERNAL_COUPLING_CLASS_EXT_BASE                 (500L)
#define IVIRFSIGGEN_VAL_FM_EXTERNAL_COUPLING_SPECIFIC_EXT_BASE              (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_PM_EXTERNAL_COUPLING -*/
#define IVIRFSIGGEN_VAL_PM_EXTERNAL_COUPLING_AC                             (0L)
#define IVIRFSIGGEN_VAL_PM_EXTERNAL_COUPLING_DC                             (1L)
#define IVIRFSIGGEN_VAL_PM_EXTERNAL_COUPLING_CLASS_EXT_BASE                 (500L)
#define IVIRFSIGGEN_VAL_PM_EXTERNAL_COUPLING_SPECIFIC_EXT_BASE              (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_PULSE_MODULATION_SOURCE -*/
#define IVIRFSIGGEN_VAL_PULSE_MODULATION_SOURCE_INTERNAL                    (0L)
#define IVIRFSIGGEN_VAL_PULSE_MODULATION_SOURCE_EXTERNAL                    (1L)
#define IVIRFSIGGEN_VAL_PULSE_MODULATION_SOURCE_CLASS_EXT_BASE              (500L)
#define IVIRFSIGGEN_VAL_PULSE_MODULATION_SOURCE_SPECIFIC_EXT_BASE           (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_PULSE_MODULATION_EXTERNAL_POLARITY -*/
#define IVIRFSIGGEN_VAL_PULSE_MODULATION_EXTERNAL_POLARITY_NORMAL           (0L)
#define IVIRFSIGGEN_VAL_PULSE_MODULATION_EXTERNAL_POLARITY_INVERSE          (1L)
#define IVIRFSIGGEN_VAL_PULSE_MODULATION_EXTERNAL_POLARITY_CLASS_EXT_BASE   (500L)
#define IVIRFSIGGEN_VAL_PULSE_MODULATION_EXTERNAL_POLARITY_SPECIFIC_EXT_BASE  (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_LF_GENERATOR_WAVEFORM -*/
#define IVIRFSIGGEN_VAL_LF_GENERATOR_WAVEFORM_SINE                          (0L)
#define IVIRFSIGGEN_VAL_LF_GENERATOR_WAVEFORM_SQUARE                        (1L)
#define IVIRFSIGGEN_VAL_LF_GENERATOR_WAVEFORM_TRIANGLE                      (2L)
#define IVIRFSIGGEN_VAL_LF_GENERATOR_WAVEFORM_RAMP_UP                       (3L)
#define IVIRFSIGGEN_VAL_LF_GENERATOR_WAVEFORM_RAMP_DOWN                     (4L)
#define IVIRFSIGGEN_VAL_LF_GENERATOR_WAVEFORM_CLASS_EXT_BASE       (500L)
#define IVIRFSIGGEN_VAL_LF_GENERATOR_WAVEFORM_SPECIFIC_EXT_BASE    (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_PULSE_TRIGGER_SOURCE -*/
#define IVIRFSIGGEN_VAL_PULSE_TRIGGER_SOURCE_INTERNAL                       (0L)
#define IVIRFSIGGEN_VAL_PULSE_TRIGGER_SOURCE_EXTERNAL                       (1L)
#define IVIRFSIGGEN_VAL_PULSE_TRIGGER_SOURCE_CLASS_EXT_BASE                 (500L)
#define IVIRFSIGGEN_VAL_PULSE_TRIGGER_SOURCE_SPECIFIC_EXT_BASE              (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_PULSE_EXTERNAL_TRIGGER_SLOPE -*/
#define IVIRFSIGGEN_VAL_PULSE_EXTERNAL_TRIGGER_SLOPE_POSITIVE               (0L)
#define IVIRFSIGGEN_VAL_PULSE_EXTERNAL_TRIGGER_SLOPE_NEGATIVE               (1L)
#define IVIRFSIGGEN_VAL_PULSE_EXTERNAL_TRIGGER_SLOPE_CLASS_EXT_BASE         (500L)
#define IVIRFSIGGEN_VAL_PULSE_EXTERNAL_TRIGGER_SLOPE_SPECIFIC_EXT_BASE      (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_PULSE_OUTPUT_POLARITY -*/
#define IVIRFSIGGEN_VAL_PULSE_OUTPUT_POLARITY_NORMAL                        (0L)
#define IVIRFSIGGEN_VAL_PULSE_OUTPUT_POLARITY_INVERSE                       (1L)
#define IVIRFSIGGEN_VAL_PULSE_OUTPUT_POLARITY_CLASS_EXT_BASE                (500L)
#define IVIRFSIGGEN_VAL_PULSE_OUTPUT_POLARITY_SPECIFIC_EXT_BASE             (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_SWEEP_MODE -*/
#define IVIRFSIGGEN_VAL_SWEEP_MODE_NONE                                     (0L)
#define IVIRFSIGGEN_VAL_SWEEP_MODE_FREQUENCY_SWEEP                          (1L)
#define IVIRFSIGGEN_VAL_SWEEP_MODE_POWER_SWEEP                              (2L)
#define IVIRFSIGGEN_VAL_SWEEP_MODE_FREQUENCY_STEP                           (3L)
#define IVIRFSIGGEN_VAL_SWEEP_MODE_POWER_STEP                               (4L)
#define IVIRFSIGGEN_VAL_SWEEP_MODE_LIST                                     (5L)
#define IVIRFSIGGEN_VAL_SWEEP_MODE_CLASS_EXT_BASE                           (500L)
#define IVIRFSIGGEN_VAL_SWEEP_MODE_SPECIFIC_EXT_BASE                        (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_SWEEP_TRIGGER_SOURCE -*/
#define IVIRFSIGGEN_VAL_SWEEP_TRIGGER_SOURCE_IMMEDIATE                      (0L)
#define IVIRFSIGGEN_VAL_SWEEP_TRIGGER_SOURCE_EXTERNAL                       (1L)
#define IVIRFSIGGEN_VAL_SWEEP_TRIGGER_SOURCE_SOFTWARE                       (2L)
#define IVIRFSIGGEN_VAL_SWEEP_TRIGGER_SOURCE_CLASS_EXT_BASE                 (500L)
#define IVIRFSIGGEN_VAL_SWEEP_TRIGGER_SOURCE_SPECIFIC_EXT_BASE              (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_FREQUENCY_STEP_SCALING -*/
#define IVIRFSIGGEN_VAL_FREQUENCY_STEP_SCALING_LINEAR                       (0L)
#define IVIRFSIGGEN_VAL_FREQUENCY_STEP_SCALING_LOGARITHMIC                  (1L)
#define IVIRFSIGGEN_VAL_FREQUENCY_STEP_SCALING_CLASS_EXT_BASE               (500L)
#define IVIRFSIGGEN_VAL_FREQUENCY_STEP_SCALING_SPECIFIC_EXT_BASE            (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_ALC_SOURCE -*/
#define IVIRFSIGGEN_VAL_ALC_SOURCE_INTERNAL                                 (0L)
#define IVIRFSIGGEN_VAL_ALC_SOURCE_EXTERNAL                                 (1L)
#define IVIRFSIGGEN_VAL_ALC_SOURCE_CLASS_EXT_BASE                           (500L)
#define IVIRFSIGGEN_VAL_ALC_SOURCE_SPECIFIC_EXT_BASE                        (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_REFERENCE_OSCILLATOR_SOURCE -*/
#define IVIRFSIGGEN_VAL_REFERENCE_OSCILLATOR_SOURCE_INTERNAL                (0L)
#define IVIRFSIGGEN_VAL_REFERENCE_OSCILLATOR_SOURCE_EXTERNAL                (1L)
#define IVIRFSIGGEN_VAL_REFERENCE_OSCILLATOR_SOURCE_CLASS_EXT_BASE          (500L)
#define IVIRFSIGGEN_VAL_REFERENCE_OSCILLATOR_SOURCE_SPECIFIC_EXT_BASE       (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_IQ_SOURCE -*/
#define IVIRFSIGGEN_VAL_IQ_SOURCE_DIGITAL_MODULATION_BASE                   (0L)
#define IVIRFSIGGEN_VAL_IQ_SOURCE_CDMA_BASE                                 (1L)
#define IVIRFSIGGEN_VAL_IQ_SOURCE_TDMA_BASE                                 (2L)
#define IVIRFSIGGEN_VAL_IQ_SOURCE_ARB_GENERATOR                             (3L)
#define IVIRFSIGGEN_VAL_IQ_SOURCE_EXTERNAL                                  (4L)
#define IVIRFSIGGEN_VAL_IQ_SOURCE_CLASS_EXT_BASE                            (500L)
#define IVIRFSIGGEN_VAL_IQ_SOURCE_SPECIFIC_EXT_BASE                         (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_ARB_TRIGGER_SOURCE -*/
#define IVIRFSIGGEN_VAL_ARB_TRIGGER_SOURCE_IMMEDIATE                        (0L)
#define IVIRFSIGGEN_VAL_ARB_TRIGGER_SOURCE_EXTERNAL                         (1L)
#define IVIRFSIGGEN_VAL_ARB_TRIGGER_SOURCE_SOFTWARE                         (2L)
#define IVIRFSIGGEN_VAL_ARB_TRIGGER_SOURCE_CLASS_EXT_BASE                   (500L)
#define IVIRFSIGGEN_VAL_ARB_TRIGGER_SOURCE_SPECIFIC_EXT_BASE                (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_ARB_EXTERNAL_TRIGGER_SLOPE -*/
#define IVIRFSIGGEN_VAL_ARB_EXTERNAL_TRIGGER_SLOPE_POSITIVE                 (0L)
#define IVIRFSIGGEN_VAL_ARB_EXTERNAL_TRIGGER_SLOPE_NEGATIVE                 (1L)
#define IVIRFSIGGEN_VAL_ARB_EXTERNAL_TRIGGER_SLOPE_CLASS_EXT_BASE           (500L)
#define IVIRFSIGGEN_VAL_ARB_EXTERNAL_TRIGGER_SLOPE_SPECIFIC_EXT_BASE        (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_DIGITAL_MODULATION_BASE_DATA_SOURCE -*/
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_DATA_SOURCE_EXTERNAL        (0L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_DATA_SOURCE_PRBS            (1L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_DATA_SOURCE_BIT_SEQUENCE    (2L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_DATA_SOURCE_CLASS_EXT_BASE  (500L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_DATA_SOURCE_SPECIFIC_EXT_BASE  (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_DIGITAL_MODULATION_BASE_PRBS_TYPE -*/
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_PRBS_TYPE_PRBS9             (0L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_PRBS_TYPE_PRBS11            (1L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_PRBS_TYPE_PRBS15            (2L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_PRBS_TYPE_PRBS16            (3L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_PRBS_TYPE_PRBS20            (4L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_PRBS_TYPE_PRBS21            (5L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_PRBS_TYPE_PRBS23            (6L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_PRBS_TYPE_CLASS_EXT_BASE    (500L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_PRBS_TYPE_SPECIFIC_EXT_BASE  (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_DIGITAL_MODULATION_BASE_CLOCK_SOURCE -*/
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_CLOCK_SOURCE_INTERNAL       (0L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_CLOCK_SOURCE_EXTERNAL       (1L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_CLOCK_SOURCE_CLASS_EXT_BASE  (500L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_CLOCK_SOURCE_SPECIFIC_EXT_BASE  (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_DIGITAL_MODULATION_BASE_EXTERNAL_CLOCK_TYPE -*/
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_EXTERNAL_CLOCK_TYPE_BIT     (0L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_EXTERNAL_CLOCK_TYPE_SYMBOL  (1L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_EXTERNAL_CLOCK_TYPE_CLASS_EXT_BASE  (500L)
#define IVIRFSIGGEN_VAL_DIGITAL_MODULATION_BASE_EXTERNAL_CLOCK_TYPE_SPECIFIC_EXT_BASE  (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_CDMA_TRIGGER_SOURCE -*/
#define IVIRFSIGGEN_VAL_CDMA_TRIGGER_SOURCE_IMMEDIATE                       (0L)
#define IVIRFSIGGEN_VAL_CDMA_TRIGGER_SOURCE_EXTERNAL                        (1L)
#define IVIRFSIGGEN_VAL_CDMA_TRIGGER_SOURCE_SOFTWARE                        (2L)
#define IVIRFSIGGEN_VAL_CDMA_TRIGGER_SOURCE_CLASS_EXT_BASE                  (500L)
#define IVIRFSIGGEN_VAL_CDMA_TRIGGER_SOURCE_SPECIFIC_EXT_BASE               (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_CDMA_EXTERNAL_TRIGGER_SLOPE -*/
#define IVIRFSIGGEN_VAL_CDMA_EXTERNAL_TRIGGER_SLOPE_POSITIVE                (0L)
#define IVIRFSIGGEN_VAL_CDMA_EXTERNAL_TRIGGER_SLOPE_NEGATIVE                (1L)
#define IVIRFSIGGEN_VAL_CDMA_EXTERNAL_TRIGGER_SLOPE_CLASS_EXT_BASE          (500L)
#define IVIRFSIGGEN_VAL_CDMA_EXTERNAL_TRIGGER_SLOPE_SPECIFIC_EXT_BASE       (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_CDMA_CLOCK_SOURCE -*/
#define IVIRFSIGGEN_VAL_CDMA_CLOCK_SOURCE_INTERNAL                          (0L)
#define IVIRFSIGGEN_VAL_CDMA_CLOCK_SOURCE_EXTERNAL                          (1L)
#define IVIRFSIGGEN_VAL_CDMA_CLOCK_SOURCE_CLASS_EXT_BASE                    (500L)
#define IVIRFSIGGEN_VAL_CDMA_CLOCK_SOURCE_SPECIFIC_EXT_BASE                 (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_TDMA_TRIGGER_SOURCE -*/
#define IVIRFSIGGEN_VAL_TDMA_TRIGGER_SOURCE_IMMEDIATE                       (0L)
#define IVIRFSIGGEN_VAL_TDMA_TRIGGER_SOURCE_EXTERNAL                        (1L)
#define IVIRFSIGGEN_VAL_TDMA_TRIGGER_SOURCE_SOFTWARE                        (2L)
#define IVIRFSIGGEN_VAL_TDMA_TRIGGER_SOURCE_CLASS_EXT_BASE                  (500L)
#define IVIRFSIGGEN_VAL_TDMA_TRIGGER_SOURCE_SPECIFIC_EXT_BASE               (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_TDMA_EXTERNAL_TRIGGER_SLOPE -*/
#define IVIRFSIGGEN_VAL_TDMA_EXTERNAL_TRIGGER_SLOPE_POSITIVE                (0L)
#define IVIRFSIGGEN_VAL_TDMA_EXTERNAL_TRIGGER_SLOPE_NEGATIVE                (1L)
#define IVIRFSIGGEN_VAL_TDMA_EXTERNAL_TRIGGER_SLOPE_CLASS_EXT_BASE          (500L)
#define IVIRFSIGGEN_VAL_TDMA_EXTERNAL_TRIGGER_SLOPE_SPECIFIC_EXT_BASE       (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_TDMA_CLOCK_SOURCE -*/
#define IVIRFSIGGEN_VAL_TDMA_CLOCK_SOURCE_INTERNAL                          (0L)
#define IVIRFSIGGEN_VAL_TDMA_CLOCK_SOURCE_EXTERNAL                          (1L)
#define IVIRFSIGGEN_VAL_TDMA_CLOCK_SOURCE_CLASS_EXT_BASE                    (500L)
#define IVIRFSIGGEN_VAL_TDMA_CLOCK_SOURCE_SPECIFIC_EXT_BASE                 (1000L)

/*- Defined values for attribute IVIRFSIGGEN_ATTR_TDMA_EXTERNAL_CLOCK_TYPE -*/
#define IVIRFSIGGEN_VAL_TDMA_EXTERNAL_CLOCK_TYPE_BIT                        (0L)
#define IVIRFSIGGEN_VAL_TDMA_EXTERNAL_CLOCK_TYPE_SYMBOL                     (1L)
#define IVIRFSIGGEN_VAL_TDMA_EXTERNAL_CLOCK_TYPE_CLASS_EXT_BASE             (500L)
#define IVIRFSIGGEN_VAL_TDMA_EXTERNAL_CLOCK_TYPE_SPECIFIC_EXT_BASE          (1000L)



/****************************************************************************
 *--------- IviRFSigGen Class Instrument Driver Function Declarations ---------*
 ****************************************************************************/
    /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviRFSigGen_init (ViRsrc logicalName, 
                                 ViBoolean idQuery, 
                                 ViBoolean resetDevice, 
                                 ViSession *vi);

ViStatus _VI_FUNC IviRFSigGen_close (ViSession vi);

ViStatus _VI_FUNC IviRFSigGen_reset (ViSession vi);

ViStatus _VI_FUNC IviRFSigGen_self_test (ViSession vi, 
                                      ViInt16 *selfTestResult, 
                                      ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviRFSigGen_error_query (ViSession vi, 
                                        ViInt32 *errorCode, 
                                        ViChar errorMessage[]);

ViStatus _VI_FUNC IviRFSigGen_error_message (ViSession vi, 
                                          ViStatus statusCode, 
                                          ViChar message[]);

ViStatus _VI_FUNC IviRFSigGen_revision_query (ViSession vi, 
                                           ViChar driverRev[], 
                                           ViChar instrRev[]);
    /*- Utility Functions -*/
ViStatus _VI_FUNC IviRFSigGen_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviRFSigGen_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviRFSigGen_Disable (ViSession vi);

    /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviRFSigGen_InitWithOptions (ViRsrc logicalName, 
                                            ViBoolean IDQuery,
                                            ViBoolean resetDevice, 
                                            ViConstString optionString, 
                                            ViSession *vi);

    /*- Set, Get, and Check Attribute Functions -*/

ViStatus _VI_FUNC IviRFSigGen_GetAttributeViInt32 (ViSession vi, 
                                                ViConstString repeatedCapName,
                                                ViAttr attributeId,
                                                ViInt32 *value);

ViStatus _VI_FUNC IviRFSigGen_SetAttributeViInt32 (ViSession vi, 
                                                ViConstString repeatedCapName,
                                                ViAttr attributeId,
                                                ViInt32 value);

ViStatus _VI_FUNC IviRFSigGen_CheckAttributeViInt32 (ViSession vi, 
                                                  ViConstString repeatedCapName,
                                                  ViAttr attributeId,
                                                  ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviRFSigGen_GetAttributeViInt64 (ViSession vi, 
                                                ViConstString repeatedCapName,
                                                ViAttr attributeId,
                                                ViInt64 *value);

ViStatus _VI_FUNC IviRFSigGen_SetAttributeViInt64 (ViSession vi, 
                                                ViConstString repeatedCapName,
                                                ViAttr attributeId,
                                                ViInt64 value);

ViStatus _VI_FUNC IviRFSigGen_CheckAttributeViInt64 (ViSession vi, 
                                                  ViConstString repeatedCapName,
                                                  ViAttr attributeId,
                                                  ViInt64 value);
#endif

ViStatus _VI_FUNC IviRFSigGen_GetAttributeViReal64 (ViSession vi, 
                                                 ViConstString repeatedCapName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 *value);

ViStatus _VI_FUNC IviRFSigGen_SetAttributeViReal64 (ViSession vi, 
                                                 ViConstString repeatedCapName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 value);

ViStatus _VI_FUNC IviRFSigGen_CheckAttributeViReal64 (ViSession vi, 
                                                   ViConstString repeatedCapName, 
                                                   ViAttr attributeId, 
                                                   ViReal64 value);

ViStatus _VI_FUNC IviRFSigGen_GetAttributeViString (ViSession vi, 
                                                 ViConstString repeatedCapName, 
                                                 ViAttr attributeId, 
                                                 ViInt32 bufferSize, 
                                                 ViChar value[]);

ViStatus _VI_FUNC IviRFSigGen_SetAttributeViString (ViSession vi, 
                                                 ViConstString repeatedCapName, 
                                                 ViAttr attributeId, 
                                                 ViConstString value);

ViStatus _VI_FUNC IviRFSigGen_CheckAttributeViString (ViSession vi, 
                                                   ViConstString repeatedCapName, 
                                                   ViAttr attributeId, 
                                                   ViConstString value); 

ViStatus _VI_FUNC IviRFSigGen_GetAttributeViBoolean (ViSession vi, 
                                                  ViConstString repeatedCapName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean *value);

ViStatus _VI_FUNC IviRFSigGen_SetAttributeViBoolean (ViSession vi, 
                                                  ViConstString repeatedCapName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean value);

ViStatus _VI_FUNC IviRFSigGen_CheckAttributeViBoolean (ViSession vi, 
                                                    ViConstString repeatedCapName, 
                                                    ViAttr attributeId, 
                                                    ViBoolean value);

ViStatus _VI_FUNC IviRFSigGen_GetAttributeViSession (ViSession vi, 
                                                  ViConstString repeatedCapName, 
                                                  ViAttr attributeId, 
                                                  ViSession *value);

ViStatus _VI_FUNC IviRFSigGen_SetAttributeViSession (ViSession vi, 
                                                  ViConstString repeatedCapName, 
                                                  ViAttr attributeId, 
                                                  ViSession value);

ViStatus _VI_FUNC IviRFSigGen_CheckAttributeViSession (ViSession vi, 
                                                    ViConstString repeatedCapName, 
                                                    ViAttr attributeId, 
                                                    ViSession value);

    /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviRFSigGen_LockSession (ViSession vi, 
                                        ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviRFSigGen_UnlockSession (ViSession vi, 
                                          ViBoolean *callerHasLock);

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviRFSigGen_GetError (ViSession vi, 
                                   ViStatus *errorCode, 
                                   ViInt32 bufferSize, 
                                   ViChar description[]);

ViStatus _VI_FUNC IviRFSigGen_ClearError (ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviRFSigGen_GetNextInterchangeWarning (ViSession vi, 
                                                      ViInt32 bufferSize,
                                                      ViChar warning[]);

ViStatus _VI_FUNC IviRFSigGen_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviRFSigGen_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviRFSigGen_GetNextCoercionRecord (ViSession vi,
                                                  ViInt32 bufferSize, 
                                                  ViChar record[]);

ViStatus _VI_FUNC IviRFSigGen_GetSpecificDriverCHandle (ViSession vi,
                                                     ViSession* specificDriverCHandle);

    /*- IviRFSigGen Fundamental Capabilities -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureRF (ViSession vi,
                                           ViReal64 Frequency,
                                           ViReal64 PowerLevel);

ViStatus _VI_FUNC IviRFSigGen_ConfigureALCEnabled (ViSession vi,
                                                   ViBoolean ALCEnabled);

ViStatus _VI_FUNC IviRFSigGen_ConfigureOutputEnabled (ViSession vi,
                                                      ViBoolean OutputEnabled);

ViStatus _VI_FUNC IviRFSigGen_DisableAllModulation (ViSession vi);

ViStatus _VI_FUNC IviRFSigGen_IsSettled (ViSession vi,
                                         ViBoolean* Done);

ViStatus _VI_FUNC IviRFSigGen_WaitUntilSettled (ViSession vi,
                                                ViInt32 MaxTimeMilliseconds);


    /*- IviRFSigGenModulateAM Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureAMEnabled (ViSession vi,
                                                  ViBoolean Enabled);

ViStatus _VI_FUNC IviRFSigGen_ConfigureAMExternalCoupling (ViSession vi,
                                                           ViInt32 Coupling);

ViStatus _VI_FUNC IviRFSigGen_ConfigureAM (ViSession vi,
                                           ViConstString Source,
                                           ViInt32 Scaling,
                                           ViReal64 Depth);


    /*- IviRFSigGenModulateFM Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureFMEnabled (ViSession vi,
                                                  ViBoolean Enabled);

ViStatus _VI_FUNC IviRFSigGen_ConfigureFMExternalCoupling (ViSession vi,
                                                           ViInt32 Coupling);

ViStatus _VI_FUNC IviRFSigGen_ConfigureFM (ViSession vi,
                                           ViConstString Source,
                                           ViReal64 Deviation);


    /*- IviRFSigGenModulatePM Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigurePMEnabled (ViSession vi,
                                                  ViBoolean Enabled);

ViStatus _VI_FUNC IviRFSigGen_ConfigurePMExternalCoupling (ViSession vi,
                                                           ViInt32 Coupling);

ViStatus _VI_FUNC IviRFSigGen_ConfigurePM (ViSession vi,
                                           ViConstString Source,
                                           ViReal64 Deviation);


    /*- IviRFSigGenAnalogModulationSource Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_GetAnalogModulationSourceName (ViSession vi,
                                                             ViInt32 Index,
                                                             ViInt32 NameBufferSize,
                                                             ViChar Name[]);


    /*- IviRFSigGenModulatePulse Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigurePulseModulationEnabled (ViSession vi,
                                                               ViBoolean Enabled);

ViStatus _VI_FUNC IviRFSigGen_ConfigurePulseModulationSource (ViSession vi,
                                                              ViInt32 Source);

ViStatus _VI_FUNC IviRFSigGen_ConfigurePulseModulationExternalPolarity (ViSession vi,
                                                                        ViInt32 Polarity);


    /*- IviRFSigGenLFGenerator Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_GetLFGeneratorName (ViSession vi,
                                                  ViInt32 Index,
                                                  ViInt32 NameBufferSize,
                                                  ViChar Name[]);

ViStatus _VI_FUNC IviRFSigGen_SetActiveLFGenerator (ViSession vi,
                                                    ViConstString ActiveLFGenerator);

ViStatus _VI_FUNC IviRFSigGen_ConfigureLFGenerator (ViSession vi,
                                                    ViReal64 Frequency,
                                                    ViInt32 Waveform);


    /*- IviRFSigGenLFGeneratorOutput Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureLFGeneratorOutput (ViSession vi,
                                                          ViReal64 Amplitude,
                                                          ViBoolean Enabled);


    /*- IviRFSigGenPulseGenerator Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigurePulseExternalTrigger (ViSession vi,
                                                             ViInt32 Slope,
                                                             ViReal64 Delay);

ViStatus _VI_FUNC IviRFSigGen_ConfigurePulseInternalTrigger (ViSession vi,
                                                             ViReal64 Period);

ViStatus _VI_FUNC IviRFSigGen_ConfigurePulse (ViSession vi,
                                              ViInt32 PulseTriggerSource,
                                              ViReal64 PulseWidth,
                                              ViBoolean GatingEnabled);


    /*- IviRFSigGenPulseDoubleGenerator Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigurePulseDouble (ViSession vi,
                                                    ViBoolean Enabled,
                                                    ViReal64 Delay);


    /*- IviRFSigGenPulseGeneratorOutput Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigurePulseOutput (ViSession vi,
                                                    ViInt32 Polarity,
                                                    ViBoolean Enabled);


    /*- IviRFSigGenSweep Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureSweep (ViSession vi,
                                              ViInt32 Mode,
                                              ViInt32 TriggerSource);


    /*- IviRFSigGenFrequencySweep Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureFrequencySweepStartStop (ViSession vi,
                                                                ViReal64 Start,
                                                                ViReal64 Stop);

ViStatus _VI_FUNC IviRFSigGen_ConfigureFrequencySweepCenterSpan (ViSession vi,
                                                                 ViReal64 Center,
                                                                 ViReal64 Span);

ViStatus _VI_FUNC IviRFSigGen_ConfigureFrequencySweepTime (ViSession vi,
                                                           ViReal64 Time);


    /*- IviRFSigGenPowerSweep Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigurePowerSweepStartStop (ViSession vi,
                                                            ViReal64 Start,
                                                            ViReal64 Stop);

ViStatus _VI_FUNC IviRFSigGen_ConfigurePowerSweepTime (ViSession vi,
                                                       ViReal64 Time);


    /*- IviRFSigGenFrequencyStep Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureFrequencyStepStartStop (ViSession vi,
                                                               ViReal64 Start,
                                                               ViReal64 Stop,
                                                               ViInt32 Scaling,
                                                               ViReal64 StepSize);

ViStatus _VI_FUNC IviRFSigGen_ConfigureFrequencyStepDwell (ViSession vi,
                                                           ViBoolean SingleStepEnabled,
                                                           ViReal64 Dwell);

ViStatus _VI_FUNC IviRFSigGen_ResetFrequencyStep (ViSession vi);


    /*- IviRFSigGenPowerStep Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigurePowerStepStartStop (ViSession vi,
                                                           ViReal64 Start,
                                                           ViReal64 Stop,
                                                           ViReal64 StepSize);

ViStatus _VI_FUNC IviRFSigGen_ConfigurePowerStepDwell (ViSession vi,
                                                       ViBoolean SingleStepEnabled,
                                                       ViReal64 Dwell);

ViStatus _VI_FUNC IviRFSigGen_ResetPowerStep (ViSession vi);


    /*- IviRFSigGenList Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_CreateFrequencyList (ViSession vi,
                                                   ViConstString Name,
                                                   ViInt32 Length,
                                                   ViReal64 Frequency[]);

ViStatus _VI_FUNC IviRFSigGen_CreatePowerList (ViSession vi,
                                               ViConstString Name,
                                               ViInt32 Length,
                                               ViReal64 Power[]);

ViStatus _VI_FUNC IviRFSigGen_CreateFrequencyPowerList (ViSession vi,
                                                        ViConstString Name,
                                                        ViInt32 Length,
                                                        ViReal64 Frequency[],
                                                        ViReal64 Power[]);

ViStatus _VI_FUNC IviRFSigGen_SelectList (ViSession vi,
                                          ViConstString Name);

ViStatus _VI_FUNC IviRFSigGen_ClearAllLists (ViSession vi);

ViStatus _VI_FUNC IviRFSigGen_ConfigureListDwell (ViSession vi,
                                                  ViBoolean SingleStepEnabled,
                                                  ViReal64 Dwell);

ViStatus _VI_FUNC IviRFSigGen_ResetList (ViSession vi);


    /*- IviRFSigGenALC Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureALC (ViSession vi,
                                            ViInt32 Source,
                                            ViReal64 Bandwidth);


    /*- IviRFSigGenReferenceOscillator Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureReferenceOscillator (ViSession vi,
                                                            ViInt32 Source,
                                                            ViReal64 Frequency);


    /*- IviRFSigGenSoftwareTrigger Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_SendSoftwareTrigger (ViSession vi);


    /*- IviRFSigGenModulateIQ Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureIQEnabled (ViSession vi,
                                                  ViBoolean Enabled);

ViStatus _VI_FUNC IviRFSigGen_ConfigureIQ (ViSession vi,
                                           ViInt32 Source,
                                           ViBoolean SwapEnabled);

ViStatus _VI_FUNC IviRFSigGen_CalibrateIQ (ViSession vi);


    /*- IviRFSigGenIQImpairment Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureIQImpairmentEnabled (ViSession vi,
                                                            ViBoolean Enabled);

ViStatus _VI_FUNC IviRFSigGen_ConfigureIQImpairment (ViSession vi,
                                                     ViReal64 IOffset,
                                                     ViReal64 QOffset,
                                                     ViReal64 Ratio,
                                                     ViReal64 Skew);


    /*- IviRFSigGenArbGenerator Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_ConfigureArb (ViSession vi,
                                            ViReal64 ClockFrequency,
                                            ViReal64 FilterFrequency);

ViStatus _VI_FUNC IviRFSigGen_WriteArbWaveform (ViSession vi,
                                                ViConstString Name,
                                                ViInt32 NumberOfSamples,
                                                ViReal64 IData[],
                                                ViReal64 QData[],
                                                ViBoolean MoreDataPending);

ViStatus _VI_FUNC IviRFSigGen_SelectArbWaveform (ViSession vi,
                                                 ViConstString Name);

ViStatus _VI_FUNC IviRFSigGen_ClearAllArbWaveforms (ViSession vi);

ViStatus _VI_FUNC IviRFSigGen_QueryArbWaveformCapabilities (ViSession vi,
                                                            ViInt32* MaxNumberWaveforms,
                                                            ViInt32* WaveformQuantum,
                                                            ViInt32* MinWaveformSize,
                                                            ViInt32* MaxWaveformSize);

ViStatus _VI_FUNC IviRFSigGen_ConfigureArbTriggerSource (ViSession vi,
                                                         ViInt32 Source);

ViStatus _VI_FUNC IviRFSigGen_ConfigureArbExternalTriggerSlope (ViSession vi,
                                                                ViInt32 Slope);


    /*- IviRFSigGenDigitalModulationBase Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_GetDigitalModulationBaseStandardName (ViSession vi,
                                                                    ViInt32 Index,
                                                                    ViInt32 NameBufferSize,
                                                                    ViChar Name[]);

ViStatus _VI_FUNC IviRFSigGen_SelectDigitalModulationBaseStandard (ViSession vi,
                                                                   ViConstString Name);

ViStatus _VI_FUNC IviRFSigGen_ConfigureDigitalModulationBaseClockSource (ViSession vi,
                                                                         ViInt32 Source,
                                                                         ViInt32 Type);

ViStatus _VI_FUNC IviRFSigGen_ConfigureDigitalModulationBaseDataSource (ViSession vi,
                                                                        ViInt32 Source);

ViStatus _VI_FUNC IviRFSigGen_ConfigureDigitalModulationBasePRBSType (ViSession vi,
                                                                      ViInt32 Type);

ViStatus _VI_FUNC IviRFSigGen_WriteDigitalModulationBaseBitSequence (ViSession vi,
                                                                     ViConstString Name,
                                                                     ViInt32 BitCount,
                                                                     ViChar Sequence[],
                                                                     ViBoolean MoreDataPending);

ViStatus _VI_FUNC IviRFSigGen_SelectDigitalModulationBaseBitSequence (ViSession vi,
                                                                      ViConstString Name);

ViStatus _VI_FUNC IviRFSigGen_ClearAllDigitalModulationBaseBitSequences (ViSession vi);


    /*- IviRFSigGenCDMABase Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_GetCDMAStandardName (ViSession vi,
                                                   ViInt32 Index,
                                                   ViInt32 NameBufferSize,
                                                   ViChar Name[]);

ViStatus _VI_FUNC IviRFSigGen_SelectCDMAStandard (ViSession vi,
                                                  ViConstString Name);

ViStatus _VI_FUNC IviRFSigGen_ConfigureCDMAClockSource (ViSession vi,
                                                        ViInt32 Source);

ViStatus _VI_FUNC IviRFSigGen_ConfigureCDMATriggerSource (ViSession vi,
                                                          ViInt32 Source);

ViStatus _VI_FUNC IviRFSigGen_ConfigureCDMAExternalTriggerSlope (ViSession vi,
                                                                 ViInt32 Slope);

ViStatus _VI_FUNC IviRFSigGen_GetCDMATestModelName (ViSession vi,
                                                    ViInt32 Index,
                                                    ViInt32 NameBufferSize,
                                                    ViChar Name[]);

ViStatus _VI_FUNC IviRFSigGen_SelectCDMATestModel (ViSession vi,
                                                   ViConstString Name);


    /*- IviRFSigGenTDMABase Extension Group -*/
ViStatus _VI_FUNC IviRFSigGen_GetTDMAStandardName (ViSession vi,
                                                   ViInt32 Index,
                                                   ViInt32 NameBufferSize,
                                                   ViChar Name[]);

ViStatus _VI_FUNC IviRFSigGen_SelectTDMAStandard (ViSession vi,
                                                  ViConstString Name);

ViStatus _VI_FUNC IviRFSigGen_ConfigureTDMAClockSource (ViSession vi,
                                                        ViInt32 Source,
                                                        ViInt32 Type);

ViStatus _VI_FUNC IviRFSigGen_ConfigureTDMATriggerSource (ViSession vi,
                                                               ViInt32 Source);

ViStatus _VI_FUNC IviRFSigGen_ConfigureTDMAExternalTriggerSlope (ViSession vi,
                                                                 ViInt32 Slope);

ViStatus _VI_FUNC IviRFSigGen_GetTDMAFrameName (ViSession vi,
                                                ViInt32 Index,
                                                ViInt32 NameBufferSize,
                                                ViChar Name[]);

ViStatus _VI_FUNC IviRFSigGen_SelectTDMAFrame (ViSession vi,
                                               ViConstString Name);



/****************************************************************************
 *--------------- IviRFSigGen Class Error And Completion Codes ----------------*
 ****************************************************************************/
#define IVIRFSIGGEN_ERROR_TRIGGER_NOT_SOFTWARE   (IVI_CROSS_CLASS_ERROR_BASE + 0x0001L)
#define IVIRFSIGGEN_ERROR_MAX_TIME_EXCEEDED      (IVI_CLASS_ERROR_BASE + 0x0003L)
#define IVIRFSIGGEN_ERROR_LIST_UNKNOWN            (IVI_CLASS_ERROR_BASE + 0x000AL)



#define IVIRFSIGGEN_ERRMSG_TRIGGER_NOT_SOFTWARE  "The trigger source is not set to software trigger."
#define IVIRFSIGGEN_ERRMSG_MAX_TIME_EXCEEDED     "Maximum time exceeded before the operation completed."
#define IVIRFSIGGEN_ERRMSG_LIST_UNKNOWN           "The selected list is not defined."



#define IVIRFSIGGEN_ERROR_CODES_AND_MSGS \
    {IVIRFSIGGEN_ERROR_TRIGGER_NOT_SOFTWARE, IVIRFSIGGEN_ERRMSG_TRIGGER_NOT_SOFTWARE},\
    {IVIRFSIGGEN_ERROR_MAX_TIME_EXCEEDED,    IVIRFSIGGEN_ERRMSG_MAX_TIME_EXCEEDED},\
    {IVIRFSIGGEN_ERROR_LIST_UNKNOWN,          IVIRFSIGGEN_ERRMSG_LIST_UNKNOWN}


/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

#endif /* IVIRFSIGGEN_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviScope.h sha256=5f02790e7bc21b2cba3db1b6cb17b435b8862afaed37e91fc473610a3b2799b3 bytes=43098 -->
## FILE: imports/include/IviScope.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviScope.h`
- sha256: `5f02790e7bc21b2cba3db1b6cb17b435b8862afaed37e91fc473610a3b2799b3`
- bytes: 43098

````c
/****************************************************************************
 *                             I V I - S C O P E                             
 *---------------------------------------------------------------------------
 *    Copyright (c) 1998-2020 National Instruments.  All Rights Reserved.         
 *---------------------------------------------------------------------------
 *                                                                           
 * Title:       iviscope.h                                                    
 * Purpose:     IviScope Class declarations for the Base and Extended         
 *              IviScope Capabilities.                                                 
 ****************************************************************************/

#ifndef IVISCOPE_HEADER
#define IVISCOPE_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVISCOPE_MAJOR_VERSION                  (4L)
#define IVISCOPE_MINOR_VERSION                  (0L)

#define IVISCOPE_SPECIFICATION_MAJOR_VERSION    (4L)
#define IVISCOPE_SPECIFICATION_MINOR_VERSION    (1L)

#define IVISCOPE_DRIVER_VENDOR                  "National Instruments"
#ifdef	_IVI_mswin64_
#define IVISCOPE_DRIVER_DESCRIPTION				"IviScope Class Driver [Compiled for 64-bit.]"
#else
#define IVISCOPE_DRIVER_DESCRIPTION				"IviScope Class Driver"
#endif

/****************************************************************************
 *-------------------- IviScope Class Attribute Defines --------------------*
 ****************************************************************************/

    /*- IVI Inherent Attributes -*/
        /*- User Options -*/
#define IVISCOPE_ATTR_CACHE                     IVI_ATTR_CACHE                         /* ViBoolean */
#define IVISCOPE_ATTR_RANGE_CHECK               IVI_ATTR_RANGE_CHECK                   /* ViBoolean */
#define IVISCOPE_ATTR_QUERY_INSTRUMENT_STATUS   IVI_ATTR_QUERY_INSTRUMENT_STATUS       /* ViBoolean */
#define IVISCOPE_ATTR_RECORD_COERCIONS          IVI_ATTR_RECORD_COERCIONS              /* ViBoolean */
#define IVISCOPE_ATTR_SIMULATE                  IVI_ATTR_SIMULATE                      /* ViBoolean */
#define IVISCOPE_ATTR_INTERCHANGE_CHECK         IVI_ATTR_INTERCHANGE_CHECK             /* ViBoolean */
#define IVISCOPE_ATTR_SPY                       IVI_ATTR_SPY                           /* ViBoolean */
#define IVISCOPE_ATTR_USE_SPECIFIC_SIMULATION   IVI_ATTR_USE_SPECIFIC_SIMULATION       /* ViBoolean */

        /*- Instrument Capabilities -*/
#define IVISCOPE_ATTR_GROUP_CAPABILITIES        IVI_ATTR_GROUP_CAPABILITIES            /* ViString, read-only */
#define IVISCOPE_ATTR_FUNCTION_CAPABILITIES     IVI_ATTR_FUNCTION_CAPABILITIES         /* ViString, read-only */

        /*- Class Driver Information -*/    
#define IVISCOPE_ATTR_CLASS_DRIVER_PREFIX                         IVI_ATTR_CLASS_DRIVER_PREFIX                       /* ViString, read-only */
#define IVISCOPE_ATTR_CLASS_DRIVER_VENDOR                         IVI_ATTR_CLASS_DRIVER_VENDOR                       /* ViString, read-only */
#define IVISCOPE_ATTR_CLASS_DRIVER_DESCRIPTION                    IVI_ATTR_CLASS_DRIVER_DESCRIPTION                  /* ViString, read-only */
#define IVISCOPE_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION     /* ViInt32,  read-only */
#define IVISCOPE_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION     /* ViInt32,  read-only */

        /*- Specific Driver Information -*/    
#define IVISCOPE_ATTR_SPECIFIC_DRIVER_PREFIX                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX                    /* ViString, read-only */
#define IVISCOPE_ATTR_SPECIFIC_DRIVER_LOCATOR                     IVI_ATTR_SPECIFIC_DRIVER_LOCATOR                   /* ViString, read-only */
#define IVISCOPE_ATTR_IO_RESOURCE_DESCRIPTOR                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR                       /* ViString, read-only */
#define IVISCOPE_ATTR_LOGICAL_NAME                                IVI_ATTR_LOGICAL_NAME                              /* ViString, read-only */
#define IVISCOPE_ATTR_SPECIFIC_DRIVER_VENDOR                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR                    /* ViString, read-only */
#define IVISCOPE_ATTR_SPECIFIC_DRIVER_DESCRIPTION                 IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION               /* ViString, read-only */
#define IVISCOPE_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVISCOPE_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/    
#define IVISCOPE_ATTR_INSTRUMENT_FIRMWARE_REVISION     IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION   /* ViString, read-only */
#define IVISCOPE_ATTR_INSTRUMENT_MANUFACTURER          IVI_ATTR_INSTRUMENT_MANUFACTURER        /* ViString, read-only */
#define IVISCOPE_ATTR_INSTRUMENT_MODEL                 IVI_ATTR_INSTRUMENT_MODEL               /* ViString, read-only */
#define IVISCOPE_ATTR_SUPPORTED_INSTRUMENT_MODELS      IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS

	/*- Version Information -*/
#define IVISCOPE_ATTR_CLASS_DRIVER_REVISION            IVI_ATTR_CLASS_DRIVER_REVISION          /* ViString, read-only */
#define IVISCOPE_ATTR_SPECIFIC_DRIVER_REVISION         IVI_ATTR_SPECIFIC_DRIVER_REVISION       /* ViString, read-only */

        /*- Driver Setup information -*/
#define IVISCOPE_ATTR_DRIVER_SETUP                     IVI_ATTR_DRIVER_SETUP                   /* ViString */

    /*- IviScope Fundamental Attributes -*/
        /*- Channel Subsystem -*/
#define IVISCOPE_ATTR_CHANNEL_COUNT             IVI_ATTR_CHANNEL_COUNT               /* ViInt32,  read-only */
#define IVISCOPE_ATTR_VERTICAL_RANGE            (IVI_CLASS_PUBLIC_ATTR_BASE  + 1L)   /* ViReal64,  Multi-Channel */
#define IVISCOPE_ATTR_VERTICAL_OFFSET           (IVI_CLASS_PUBLIC_ATTR_BASE  + 2L)   /* ViReal64,  Multi-Channel */
#define IVISCOPE_ATTR_VERTICAL_COUPLING         (IVI_CLASS_PUBLIC_ATTR_BASE  + 3L)   /* ViInt32,   Multi-Channel */
#define IVISCOPE_ATTR_PROBE_ATTENUATION         (IVI_CLASS_PUBLIC_ATTR_BASE  + 4L)   /* ViReal64,  Multi-Channel */
#define IVISCOPE_ATTR_CHANNEL_ENABLED           (IVI_CLASS_PUBLIC_ATTR_BASE  + 5L)   /* ViBoolean, Multi-Channel */
#define IVISCOPE_ATTR_MAX_INPUT_FREQUENCY       (IVI_CLASS_PUBLIC_ATTR_BASE  + 6L)   /* ViReal64,  Multi-Channel */
#define IVISCOPE_ATTR_INPUT_IMPEDANCE           (IVI_CLASS_PUBLIC_ATTR_BASE  + 103L) /* ViReal64,  Multi-Channel */
    
        /*- Acquisition Subsystem -*/
#define IVISCOPE_ATTR_ACQUISITION_TYPE          (IVI_CLASS_PUBLIC_ATTR_BASE  + 101L) /* ViInt32    */
#define IVISCOPE_ATTR_ACQUISITION_START_TIME    (IVI_CLASS_PUBLIC_ATTR_BASE  + 109L) /* ViReal64  */
#define IVISCOPE_ATTR_HORZ_TIME_PER_RECORD      (IVI_CLASS_PUBLIC_ATTR_BASE  + 7L)   /* ViReal64  */
#define IVISCOPE_ATTR_HORZ_RECORD_LENGTH        (IVI_CLASS_PUBLIC_ATTR_BASE  + 8L)   /* ViInt32, Read-only  */
#define IVISCOPE_ATTR_HORZ_MIN_NUM_PTS          (IVI_CLASS_PUBLIC_ATTR_BASE  + 9L)   /* ViInt32   */
#define IVISCOPE_ATTR_HORZ_SAMPLE_RATE          (IVI_CLASS_PUBLIC_ATTR_BASE  + 10L)  /* ViReal64, Read-only */

        /*- Triggering Subsystem -*/
#define IVISCOPE_ATTR_TRIGGER_TYPE              (IVI_CLASS_PUBLIC_ATTR_BASE  + 12L)  /* ViInt32   */
#define IVISCOPE_ATTR_TRIGGER_SOURCE            (IVI_CLASS_PUBLIC_ATTR_BASE  + 13L)  /* ViString  */
#define IVISCOPE_ATTR_TRIGGER_COUPLING          (IVI_CLASS_PUBLIC_ATTR_BASE  + 14L)  /* ViInt32   */
#define IVISCOPE_ATTR_TRIGGER_HOLDOFF           (IVI_CLASS_PUBLIC_ATTR_BASE  + 16L)  /* ViReal64  */

        /*- Edge Triggering Attributes -*/
#define IVISCOPE_ATTR_TRIGGER_LEVEL             (IVI_CLASS_PUBLIC_ATTR_BASE  + 17L)  /* ViReal64  */
#define IVISCOPE_ATTR_TRIGGER_SLOPE             (IVI_CLASS_PUBLIC_ATTR_BASE  + 18L)  /* ViInt32   */
    
    /*- IviScope Extended Attributes -*/
        /*- IviScopeTVTrigger Extension Group -*/
#define IVISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT  (IVI_CLASS_PUBLIC_ATTR_BASE + 201L) /* ViInt32   */
#define IVISCOPE_ATTR_TV_TRIGGER_EVENT          (IVI_CLASS_PUBLIC_ATTR_BASE + 205L) /* ViInt32   */
#define IVISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER    (IVI_CLASS_PUBLIC_ATTR_BASE + 206L) /* ViInt32   */
#define IVISCOPE_ATTR_TV_TRIGGER_POLARITY       (IVI_CLASS_PUBLIC_ATTR_BASE + 204L) /* ViInt32   */

        /*- IviScopeRuntTrigger Extension Group -*/
#define IVISCOPE_ATTR_RUNT_HIGH_THRESHOLD       (IVI_CLASS_PUBLIC_ATTR_BASE + 301L) /* ViReal64  */
#define IVISCOPE_ATTR_RUNT_LOW_THRESHOLD        (IVI_CLASS_PUBLIC_ATTR_BASE + 302L) /* ViReal64  */
#define IVISCOPE_ATTR_RUNT_POLARITY             (IVI_CLASS_PUBLIC_ATTR_BASE + 303L) /* ViInt32   */

        /*- IviScopeGlitchTrigger Extension Group -*/
#define IVISCOPE_ATTR_GLITCH_WIDTH              (IVI_CLASS_PUBLIC_ATTR_BASE + 401L) /* ViReal64  */
#define IVISCOPE_ATTR_GLITCH_POLARITY           (IVI_CLASS_PUBLIC_ATTR_BASE + 402L) /* ViInt32   */
#define IVISCOPE_ATTR_GLITCH_CONDITION          (IVI_CLASS_PUBLIC_ATTR_BASE + 403L) /* ViInt32   */

        /*- IviScopeWidthTrigger Extension Group -*/
#define IVISCOPE_ATTR_WIDTH_LOW_THRESHOLD       (IVI_CLASS_PUBLIC_ATTR_BASE + 501L) /* ViReal64  */
#define IVISCOPE_ATTR_WIDTH_HIGH_THRESHOLD      (IVI_CLASS_PUBLIC_ATTR_BASE + 502L) /* ViReal64  */
#define IVISCOPE_ATTR_WIDTH_POLARITY            (IVI_CLASS_PUBLIC_ATTR_BASE + 503L) /* ViInt32   */
#define IVISCOPE_ATTR_WIDTH_CONDITION           (IVI_CLASS_PUBLIC_ATTR_BASE + 504L) /* ViInt32   */

        /*- IviScopeAcLineTrigger Extension Group -*/
#define IVISCOPE_ATTR_AC_LINE_TRIGGER_SLOPE     (IVI_CLASS_PUBLIC_ATTR_BASE + 701L) /* ViInt32   */

        /*- IviScopeMinMaxWaveform Extension Group -*/
#define IVISCOPE_ATTR_NUM_ENVELOPES             (IVI_CLASS_PUBLIC_ATTR_BASE + 105L) /* ViInt32   */
    
        /*- IviScopeWaveformMeas Extension Group -*/
#define IVISCOPE_ATTR_MEAS_HIGH_REF             (IVI_CLASS_PUBLIC_ATTR_BASE + 607L) /* ViReal64, Percentage */
#define IVISCOPE_ATTR_MEAS_LOW_REF              (IVI_CLASS_PUBLIC_ATTR_BASE + 608L) /* ViReal64, Percentage */
#define IVISCOPE_ATTR_MEAS_MID_REF              (IVI_CLASS_PUBLIC_ATTR_BASE + 609L) /* ViReal64, Percentage */

        /*- IviScope Trigger Modifier Extension Group -*/
#define IVISCOPE_ATTR_TRIGGER_MODIFIER          (IVI_CLASS_PUBLIC_ATTR_BASE + 102L) /* ViInt32   */

        /*- IviScope Average Acquisition Extension Group -*/
#define IVISCOPE_ATTR_NUM_AVERAGES              (IVI_CLASS_PUBLIC_ATTR_BASE + 104L) /* ViInt32   */

        /*- IviScope Sample Mode Extension Group -*/
#define IVISCOPE_ATTR_SAMPLE_MODE               (IVI_CLASS_PUBLIC_ATTR_BASE + 106L) /* ViInt32, R/O  */

        /*- IviScope Continuous Acquisition Extension Group -*/
#define IVISCOPE_ATTR_INITIATE_CONTINUOUS       (IVI_CLASS_PUBLIC_ATTR_BASE + 107L) /* ViBoolean */

        /*- IviScope Probe Auto Sense Extension Group -*/
#define IVISCOPE_ATTR_PROBE_SENSE_VALUE         (IVI_CLASS_PUBLIC_ATTR_BASE + 108L) /* ViReal64, R/O */

        /*- IviScope Interpolation Extension Group -*/
#define IVISCOPE_ATTR_INTERPOLATION             (IVI_CLASS_PUBLIC_ATTR_BASE  + 19L) /* ViInt32   */

/*****************************************************************************
 *------ IviScope Class Function Parameter and Attribute Value Defines ------*
 *****************************************************************************/

    /*- Defined values for maxTime parameter to the waveform acquisition and measurement functions -*/
#define IVISCOPE_VAL_MAX_TIME_INFINITE          IVI_VAL_MAX_TIME_INFINITE
#define IVISCOPE_VAL_MAX_TIME_IMMEDIATE         IVI_VAL_MAX_TIME_IMMEDIATE

    /*- Defined values for the status parameter of the IviScope_AcquisitionStatus function -*/
#define IVISCOPE_VAL_ACQ_COMPLETE                               (1L)
#define IVISCOPE_VAL_ACQ_IN_PROGRESS                            (0L)
#define IVISCOPE_VAL_ACQ_STATUS_UNKNOWN                         (-1L)

    /*- Defined values for the measurementFunction parameter of the IviScope_ReadWaveformMeasurment function -*/
#define IVISCOPE_VAL_RISE_TIME                                  (0L)
#define IVISCOPE_VAL_FALL_TIME                                  (1L)
#define IVISCOPE_VAL_FREQUENCY                                  (2L)
#define IVISCOPE_VAL_PERIOD                                     (3L)
#define IVISCOPE_VAL_VOLTAGE_RMS                                (4L)
#define IVISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK                       (5L)
#define IVISCOPE_VAL_VOLTAGE_MAX                                (6L)
#define IVISCOPE_VAL_VOLTAGE_MIN                                (7L)
#define IVISCOPE_VAL_VOLTAGE_HIGH                               (8L)
#define IVISCOPE_VAL_VOLTAGE_LOW                                (9L)
#define IVISCOPE_VAL_VOLTAGE_AVERAGE                            (10L)
#define IVISCOPE_VAL_WIDTH_NEG                                  (11L)
#define IVISCOPE_VAL_WIDTH_POS                                  (12L)
#define IVISCOPE_VAL_DUTY_CYCLE_NEG                             (13L)
#define IVISCOPE_VAL_DUTY_CYCLE_POS                             (14L)
#define IVISCOPE_VAL_AMPLITUDE                                  (15L)
#define IVISCOPE_VAL_VOLTAGE_CYCLE_RMS                          (16L)
#define IVISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE                      (17L)
#define IVISCOPE_VAL_OVERSHOOT                                  (18L)
#define IVISCOPE_VAL_PRESHOOT                                   (19L)

#define IVISCOPE_VAL_MEASUREMENT_FUNCTION_CLASS_EXT_BASE        (100L)
#define IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE     (1000L)

    /*- Defined values for IVISCOPE_ATTR_VERTICAL_COUPLING -*/
#define IVISCOPE_VAL_AC                                         (0L)
#define IVISCOPE_VAL_DC                                         (1L)
#define IVISCOPE_VAL_GND                                        (2L)
#define IVISCOPE_VAL_VERTICAL_COUPLING_CLASS_EXT_BASE           (100L)
#define IVISCOPE_VAL_VERTICAL_COUPLING_SPECIFIC_EXT_BASE        (1000L)

    /*- Defined values for IVISCOPE_ATTR_TRIGGER_TYPE -*/
#define IVISCOPE_VAL_EDGE_TRIGGER                               (1L)
#define IVISCOPE_VAL_WIDTH_TRIGGER                              (2L)
#define IVISCOPE_VAL_RUNT_TRIGGER                               (3L)
#define IVISCOPE_VAL_GLITCH_TRIGGER                             (4L)
#define IVISCOPE_VAL_TV_TRIGGER                                 (5L)
#define IVISCOPE_VAL_IMMEDIATE_TRIGGER                          (6L)
#define IVISCOPE_VAL_AC_LINE_TRIGGER                            (7L)
#define IVISCOPE_VAL_TRIGGER_TYPE_CLASS_EXT_BASE                (200L)
#define IVISCOPE_VAL_TRIGGER_TYPE_SPECIFIC_EXT_BASE             (1000L)


    /*- Defined values for IVISCOPE_ATTR_TRIGGER_SLOPE -*/
#define IVISCOPE_VAL_POSITIVE                                   (1L)
#define IVISCOPE_VAL_NEGATIVE                                   (0L)

    /*- Defined values for IVISCOPE_ATTR_TRIGGER_SOURCE -*/
#define IVISCOPE_VAL_EXTERNAL                      "VAL_EXTERNAL"
#define IVISCOPE_VAL_TTL0                          "VAL_TTL0"
#define IVISCOPE_VAL_TTL1                          "VAL_TTL1"
#define IVISCOPE_VAL_TTL2                          "VAL_TTL2"
#define IVISCOPE_VAL_TTL3                          "VAL_TTL3"
#define IVISCOPE_VAL_TTL4                          "VAL_TTL4"
#define IVISCOPE_VAL_TTL5                          "VAL_TTL5"
#define IVISCOPE_VAL_TTL6                          "VAL_TTL6"
#define IVISCOPE_VAL_TTL7                          "VAL_TTL7"
#define IVISCOPE_VAL_ECL0                          "VAL_ECL0"
#define IVISCOPE_VAL_ECL1                          "VAL_ECL1"
#define IVISCOPE_VAL_PXI_STAR                      "VAL_PXI_STAR"
#define IVISCOPE_VAL_RTSI_0                        "VAL_RTSI_0"
#define IVISCOPE_VAL_RTSI_1                        "VAL_RTSI_1"
#define IVISCOPE_VAL_RTSI_2                        "VAL_RTSI_2"
#define IVISCOPE_VAL_RTSI_3                        "VAL_RTSI_3"
#define IVISCOPE_VAL_RTSI_4                        "VAL_RTSI_4"
#define IVISCOPE_VAL_RTSI_5                        "VAL_RTSI_5"
#define IVISCOPE_VAL_RTSI_6                        "VAL_RTSI_6"
    /*  
        In addition to the above defines, 
        IVISCOPE_ATTR_TRIGGER_SOURCE accpets any defined 
        channel name or string representation of a channel number
    */

    /*- Defined extended values for IVISCOPE_ATTR_PROBE_ATTENUATION -*/
#define IVISCOPE_VAL_PROBE_SENSE_ON                            (-1L)

#define IVISCOPE_VAL_PROBE_ATTENUATION_CLASS_EXT_BASE          (-100L)
#define IVISCOPE_VAL_PROBE_ATTENUATION_SPECIFIC_EXT_BASE       (-1000L)

    /*- Defined values for IVISCOPE_ATTR_TRIGGER_COUPLING -*/
/* #define IVISCOPE_VAL_AC                      DEFINED ABOVE */
/* #define IVISCOPE_VAL_DC                      DEFINED ABOVE */
#define IVISCOPE_VAL_HF_REJECT                                 (3L)
#define IVISCOPE_VAL_LF_REJECT                                 (4L)
#define IVISCOPE_VAL_NOISE_REJECT                              (5L)

#define IVISCOPE_VAL_TRIGGER_COUPLING_CLASS_EXT_BASE           (100L)
#define IVISCOPE_VAL_TRIGGER_COUPLING_SPECIFIC_EXT_BASE        (1000L)

    /*- Defined values for IVISCOPE_ATTR_INTERPOLATION -*/
#define IVISCOPE_VAL_NO_INTERPOLATION                          (1L)
#define IVISCOPE_VAL_SINE_X                                    (2L)
#define IVISCOPE_VAL_LINEAR                                    (3L)
#define IVISCOPE_VAL_INTERPOLATION_CLASS_EXT_BASE              (100L)
#define IVISCOPE_VAL_INTERPOLATION_SPECIFIC_EXT_BASE           (1000L)
    
    /*- Defined values for IVISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT -*/
#define IVISCOPE_VAL_NTSC                                      (1L)
#define IVISCOPE_VAL_PAL                                       (2L)
#define IVISCOPE_VAL_SECAM                                     (3L)
#define IVISCOPE_VAL_TV_SIGNAL_FORMAT_CLASS_EXT_BASE           (100L)
#define IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE        (1000L)

    /*- Defined values for IVISCOPE_ATTR_TV_TRIGGER_EVENT -*/
#define IVISCOPE_VAL_TV_EVENT_FIELD1                           (1L)
#define IVISCOPE_VAL_TV_EVENT_FIELD2                           (2L)
#define IVISCOPE_VAL_TV_EVENT_ANY_FIELD                        (3L)
#define IVISCOPE_VAL_TV_EVENT_ANY_LINE                         (4L)
#define IVISCOPE_VAL_TV_EVENT_LINE_NUMBER                      (5L)
#define IVISCOPE_VAL_TV_TRIGGER_EVENT_CLASS_EXT_BASE           (100L)
#define IVISCOPE_VAL_TV_TRIGGER_EVENT_SPECIFIC_EXT_BASE        (1000L)

    /*- Defined values for IVISCOPE_ATTR_TV_TRIGGER_POLARITY -*/
#define IVISCOPE_VAL_TV_POSITIVE                               (1L)
#define IVISCOPE_VAL_TV_NEGATIVE                               (2L)
#define IVISCOPE_VAL_TV_TRIGGER_POLARITY_CLASS_EXT_BASE        (100L)
#define IVISCOPE_VAL_TV_TRIGGER_POLARITY_SPECIFIC_EXT_BASE     (1000L)

    /*- Defined values for IVISCOPE_ATTR_RUNT_POLARITY -*/
#define IVISCOPE_VAL_RUNT_POSITIVE                             (1L)
#define IVISCOPE_VAL_RUNT_NEGATIVE                             (2L)
#define IVISCOPE_VAL_RUNT_EITHER                               (3L)

    /*- Defined values for IVISCOPE_ATTR_GLITCH_POLARITY -*/
#define IVISCOPE_VAL_GLITCH_POSITIVE                            (1L)
#define IVISCOPE_VAL_GLITCH_NEGATIVE                            (2L)
#define IVISCOPE_VAL_GLITCH_EITHER                              (3L)

    /*- Defined values for IVISCOPE_ATTR_GLITCH_CONDITION -*/
#define IVISCOPE_VAL_GLITCH_LESS_THAN                           (1L)
#define IVISCOPE_VAL_GLITCH_GREATER_THAN                        (2L)

    /*- Defined values for IVISCOPE_ATTR_WIDTH_POLARITY -*/
#define IVISCOPE_VAL_WIDTH_POSITIVE                             (1L)
#define IVISCOPE_VAL_WIDTH_NEGATIVE                             (2L)
#define IVISCOPE_VAL_WIDTH_EITHER                               (3L)
    
    /*- Defined values for IVISCOPE_ATTR_WIDTH_CONDITION -*/
#define IVISCOPE_VAL_WIDTH_WITHIN                               (1L)
#define IVISCOPE_VAL_WIDTH_OUTSIDE                              (2L)

    /*- Defined values for IVISCOPE_ATTR_AC_LINE_TRIGGER_SLOPE -*/
#define IVISCOPE_VAL_AC_LINE_POSITIVE                           (1L)
#define IVISCOPE_VAL_AC_LINE_NEGATIVE                           (2L)
#define IVISCOPE_VAL_AC_LINE_EITHER                             (3L)

    /*- Defined values for IVISCOPE_ATTR_ACQUISITION_TYPE -*/
#define IVISCOPE_VAL_NORMAL                                     (0L)
#define IVISCOPE_VAL_PEAK_DETECT                                (1L)
#define IVISCOPE_VAL_HI_RES                                     (2L)
#define IVISCOPE_VAL_ENVELOPE                                   (3L)
#define IVISCOPE_VAL_AVERAGE                                    (4L)

#define IVISCOPE_VAL_ACQUISITION_TYPE_CLASS_EXT_BASE            (100L)
#define IVISCOPE_VAL_ACQUISITION_TYPE_SPECIFIC_EXT_BASE         (1000L)

    /*- Defined values for IVISCOPE_ATTR_TRIGGER_MODIFIER -*/
#define IVISCOPE_VAL_NO_TRIGGER_MOD                             (1L)
#define IVISCOPE_VAL_AUTO                                       (2L)
#define IVISCOPE_VAL_AUTO_LEVEL                                 (3L)

#define IVISCOPE_VAL_TRIGGER_MOD_CLASS_EXT_BASE                 (100L)
#define IVISCOPE_VAL_TRIGGER_MOD_SPECIFIC_EXT_BASE              (1000L)

    /*- Defined values for IVISCOPE_ATTR_SAMPLE_MODE  */
#define IVISCOPE_VAL_REAL_TIME                                  (0L)
#define IVISCOPE_VAL_EQUIVALENT_TIME                            (1L)

/*****************************************************************************
 *-------- IviScope Class Instrument Driver Function Declarations -----------*
 *****************************************************************************/
    /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviScope_init (ViRsrc logicalName, 
                                 ViBoolean idQuery, 
                                 ViBoolean resetDevice, 
                                 ViSession *vi);

ViStatus _VI_FUNC IviScope_close (ViSession vi);

ViStatus _VI_FUNC IviScope_reset (ViSession vi);

ViStatus _VI_FUNC IviScope_self_test (ViSession vi, 
                                      ViInt16 *selfTestResult, 
                                      ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviScope_error_query (ViSession vi, 
                                        ViInt32 *errorCode, 
                                        ViChar errorMessage[]);

ViStatus _VI_FUNC IviScope_error_message (ViSession vi, 
                                          ViStatus statusCode, 
                                          ViChar message[]);

ViStatus _VI_FUNC IviScope_revision_query (ViSession vi, 
                                           ViChar driverRev[], 
                                           ViChar instrRev[]);

    /*- Utility Functions -*/
ViStatus _VI_FUNC IviScope_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviScope_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviScope_Disable (ViSession vi);

    /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviScope_InitWithOptions (ViRsrc logicalName, 
                                            ViBoolean IDQuery,
                                            ViBoolean resetDevice, 
                                            ViConstString optionString, 
                                            ViSession *vi);

    /*- Set, Get, and Check Attribute Functions -*/

ViStatus _VI_FUNC IviScope_GetAttributeViInt32 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt32 *value);

ViStatus _VI_FUNC IviScope_SetAttributeViInt32 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt32 value);

ViStatus _VI_FUNC IviScope_CheckAttributeViInt32 (ViSession vi, 
                                                  ViConstString channelName,
                                                  ViAttr attributeId,
                                                  ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviScope_GetAttributeViInt64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt64 *value);

ViStatus _VI_FUNC IviScope_SetAttributeViInt64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt64 value);

ViStatus _VI_FUNC IviScope_CheckAttributeViInt64 (ViSession vi, 
                                                  ViConstString channelName,
                                                  ViAttr attributeId,
                                                  ViInt64 value);
#endif

ViStatus _VI_FUNC IviScope_GetAttributeViReal64 (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 *value);

ViStatus _VI_FUNC IviScope_SetAttributeViReal64 (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 value);

ViStatus _VI_FUNC IviScope_CheckAttributeViReal64 (ViSession vi, 
                                                   ViConstString channelName, 
                                                   ViAttr attributeId, 
                                                   ViReal64 value);

ViStatus _VI_FUNC IviScope_GetAttributeViString (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViInt32 bufferSize, 
                                                 ViChar value[]);

ViStatus _VI_FUNC IviScope_SetAttributeViString (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViConstString value);

ViStatus _VI_FUNC IviScope_CheckAttributeViString (ViSession vi, 
                                                   ViConstString channelName, 
                                                   ViAttr attributeId, 
                                                   ViConstString value); 

ViStatus _VI_FUNC IviScope_GetAttributeViBoolean (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean *value);

ViStatus _VI_FUNC IviScope_SetAttributeViBoolean (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean value);

ViStatus _VI_FUNC IviScope_CheckAttributeViBoolean (ViSession vi, 
                                                    ViConstString channelName, 
                                                    ViAttr attributeId, 
                                                    ViBoolean value);

ViStatus _VI_FUNC IviScope_GetAttributeViSession (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViSession *value);

ViStatus _VI_FUNC IviScope_SetAttributeViSession (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViSession value);

ViStatus _VI_FUNC IviScope_CheckAttributeViSession (ViSession vi, 
                                                    ViConstString channelName, 
                                                    ViAttr attributeId, 
                                                    ViSession value);

    /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviScope_LockSession (ViSession vi, 
                                        ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviScope_UnlockSession (ViSession vi, 
                                          ViBoolean *callerHasLock);

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviScope_GetError (ViSession vi, 
                                     ViStatus *errorCode, 
                                     ViInt32 bufferSize, 
                                     ViChar description[]);

ViStatus _VI_FUNC IviScope_ClearError (ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviScope_GetNextInterchangeWarning (ViSession vi, 
                                                      ViInt32 bufferSize,
                                                      ViChar warning[]);

ViStatus _VI_FUNC IviScope_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviScope_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviScope_GetNextCoercionRecord (ViSession vi,
                                                  ViInt32 bufferSize, 
                                                  ViChar record[]);

ViStatus _VI_FUNC IviScope_GetSpecificDriverCHandle (ViSession vi,
                                                     ViSession* specificDriverCHandle);

ViStatus _VI_FUNC IviScope_GetSpecificDriverIUnknownPtr (ViSession vi,
                                                       void* specificDriverIUnknownPtr);
    /*- IviScope Fundamental Capabilities -*/
ViStatus _VI_FUNC IviScope_ConfigureChannel (ViSession vi, 
                                             ViConstString channel,
                                             ViReal64 range, 
                                             ViReal64 offset,
                                             ViInt32 coupling, 
                                             ViReal64 probeAttenuation,
                                             ViBoolean enabled);

ViStatus _VI_FUNC IviScope_ConfigureChanCharacteristics (ViSession vi,
                                                         ViConstString channel,
                                                         ViReal64 inputImpedance,
                                                         ViReal64 maxInputFrequency);

ViStatus _VI_FUNC IviScope_ConfigureAcquisitionType (ViSession vi, 
                                                     ViInt32 acquisitionType);

ViStatus _VI_FUNC IviScope_ConfigureAcquisitionRecord (ViSession vi, 
                                                       ViReal64 timePerRecord,
                                                       ViInt32 minimumRecordLength,
                                                       ViReal64 acqStartTime);

ViStatus _VI_FUNC IviScope_ActualRecordLength (ViSession vi, 
                                               ViInt32 *actualRecordLength);

ViStatus _VI_FUNC IviScope_SampleRate (ViSession vi, ViReal64 *sampleRate);

ViStatus _VI_FUNC IviScope_ConfigureTrigger (ViSession vi, 
                                             ViInt32 triggerType, 
                                             ViReal64 holdoff);

ViStatus _VI_FUNC IviScope_ConfigureTriggerCoupling (ViSession vi, 
                                                     ViInt32 coupling);

ViStatus _VI_FUNC IviScope_ConfigureEdgeTriggerSource (ViSession vi, 
                                                       ViConstString source,
                                                       ViReal64 level, 
                                                       ViInt32 slope);

ViStatus _VI_FUNC IviScope_ReadWaveform (ViSession vi, 
                                         ViConstString channel, 
                                         ViInt32 waveformSize,
                                         ViInt32 maxTime, 
                                         ViReal64 waveform[], 
                                         ViInt32 *actualPoints,
                                         ViReal64 *initialX, 
                                         ViReal64 *xIncrement);

ViStatus _VI_FUNC IviScope_Abort (ViSession vi);

ViStatus _VI_FUNC IviScope_InitiateAcquisition (ViSession vi);

ViStatus _VI_FUNC IviScope_AcquisitionStatus (ViSession vi, 
                                              ViInt32 *status);

ViStatus _VI_FUNC IviScope_FetchWaveform (ViSession vi, 
                                          ViConstString channel, 
                                          ViInt32 waveformSize,
                                          ViReal64 waveform[], 
                                          ViInt32 *actualPoints,
                                          ViReal64 *initialX, 
                                          ViReal64 *xIncrement);

ViStatus _VI_FUNC IviScope_IsInvalidWfmElement (ViSession vi, 
                                                ViReal64 elementValue,
                                                ViBoolean *isInvalid);

ViStatus _VI_FUNC IviScope_GetChannelName (ViSession vi, 
										   ViInt32 index,
                                           ViInt32 bufferSize,
                                           ViChar name[]);

    /*- IviScopeTVTrigger Extension Group -*/
ViStatus _VI_FUNC IviScope_ConfigureTVTriggerSource (ViSession vi, 
                                                     ViConstString source, 
                                                     ViInt32 TVSignalFormat, 
                                                     ViInt32 TVEvent, 
                                                     ViInt32 TVPolarity);
ViStatus _VI_FUNC IviScope_ConfigureTVTriggerLineNumber (ViSession vi, 
                                                         ViInt32 lineNumber);

    /*- IviScopeRuntTrigger Extension Group -*/
ViStatus _VI_FUNC IviScope_ConfigureRuntTriggerSource (ViSession vi, 
                                                       ViConstString source,
                                                       ViReal64 runtLowThreshold,
                                                       ViReal64 runtHighThreshold, 
                                                       ViInt32 runtPolarity);

    /*- IviScopeGlitchTrigger Extension Group -*/
ViStatus _VI_FUNC IviScope_ConfigureGlitchTriggerSource (ViSession vi, 
                                                         ViConstString source,
                                                         ViReal64 level, 
                                                         ViReal64 glitchWidth, 
                                                         ViInt32 glitchPolarity,
                                                         ViInt32 glitchCondition);

    /*- IviScopeWidthTrigger Extension Group -*/
ViStatus _VI_FUNC IviScope_ConfigureWidthTriggerSource (ViSession vi, 
                                                        ViConstString source,
                                                        ViReal64 level, 
                                                        ViReal64 widthLowThreshold, 
                                                        ViReal64 widthHighThreshold,
                                                        ViInt32 widthPolarity, 
                                                        ViInt32 widthCondition);

    /*- IviScopeAcLineTrigger Extension Group -*/
ViStatus _VI_FUNC IviScope_ConfigureAcLineTriggerSlope (ViSession vi, 
                                                        ViInt32 slope);

    /*- IviScopeTriggerModifier Extension Group -*/
ViStatus _VI_FUNC IviScope_ConfigureTriggerModifier (ViSession vi, 
                                                     ViInt32 triggerModifier);

    /*- IviScopeMinMaxWaveform Extension Group -*/
ViStatus _VI_FUNC IviScope_ConfigureNumEnvelopes (ViSession vi, 
                                                  ViInt32 numberOfEnvelopes);

ViStatus _VI_FUNC IviScope_ReadMinMaxWaveform (ViSession vi, 
                                               ViConstString channel, 
                                               ViInt32 waveformSize, 
                                               ViInt32 maxTime,
                                               ViReal64 minWaveform[], 
                                               ViReal64 maxWaveform[], 
                                               ViInt32 *actualPoints, 
                                               ViReal64 *initialX, 
                                               ViReal64 *xIncrement);

ViStatus _VI_FUNC IviScope_FetchMinMaxWaveform (ViSession vi, 
                                                ViConstString channel, 
                                                ViInt32 waveformSize, 
                                                ViReal64 minWaveform[], 
                                                ViReal64 maxWaveform[],
                                                ViInt32 *actualPoints, 
                                                ViReal64 *initialX,
                                                ViReal64 *xIncrement);
    
    /*- IviScopeWaveformMeas Extension Group -*/
ViStatus _VI_FUNC IviScope_ConfigureRefLevels (ViSession vi, ViReal64 lowRef, ViReal64 midRef, ViReal64 highRef);

ViStatus _VI_FUNC IviScope_ReadWaveformMeasurement (ViSession vi,
                                                    ViConstString channel, 
                                                    ViInt32 measurementFunction, 
                                                    ViInt32 maxTime, 
                                                    ViReal64 *measurement);

ViStatus _VI_FUNC IviScope_FetchWaveformMeasurement(ViSession vi,
                                                    ViConstString channel, 
                                                    ViInt32 measurementFunction, 
                                                    ViReal64 *measurement);

    /*- IviScope Average Acquisition Extension Group -*/
ViStatus _VI_FUNC IviScope_ConfigureNumAverages (ViSession vi, 
                                                 ViInt32 numberOfAverages);

    /*- IviScope Continuous Acquisition Extension Group -*/
ViStatus _VI_FUNC IviScope_ConfigureInitiateContinuous (ViSession vi, 
                                                        ViBoolean continuousAcquisition);

    /*- IviScope Interpolation Extension Group -*/
ViStatus _VI_FUNC IviScope_ConfigureInterpolation (ViSession vi, 
                                                   ViInt32 interpolation);

    /*- IviScope Sample Mode Extension Group -*/
ViStatus _VI_FUNC IviScope_SampleMode (ViSession vi, ViInt32 *sampleMode);

    /*- IviScope Probe Auto Sense Extension Group -*/
ViStatus _VI_FUNC IviScope_AutoProbeSenseValue (ViSession vi,
                                                ViConstString channel,
                                                ViReal64 *autoProbeSenseValue);
    /*- IviScope Auto Setup Extension Group -*/
ViStatus _VI_FUNC IviScope_AutoSetup (ViSession vi);
    
/*****************************************************************************
 *---------------- IviScope Class Error And Completion Codes ----------------*
 *****************************************************************************/
#define IVISCOPE_WARN_INVALID_WFM_ELEMENT              (IVI_CLASS_WARN_BASE+0x0001L)

#define IVISCOPE_ERROR_CHANNEL_NOT_ENABLED             (IVI_CLASS_ERROR_BASE+0x0001L)
#define IVISCOPE_ERROR_UNABLE_TO_PERFORM_MEASUREMENT   (IVI_CLASS_ERROR_BASE+0x0002L)
#define IVISCOPE_ERROR_MAX_TIME_EXCEEDED               (IVI_CLASS_ERROR_BASE+0x0003L)
#define IVISCOPE_ERROR_INVALID_ACQ_TYPE                (IVI_CLASS_ERROR_BASE+0x0004L)

#define IVISCOPE_WARNMSG_INVALID_WFM_ELEMENT           "One of the elements in the waveform array is invalid."

#define IVISCOPE_ERRMSG_CHANNEL_NOT_ENABLED            "Specified channel is not enabled."
#define IVISCOPE_ERRMSG_UNABLE_TO_PERFORM_MEASUREMENT  "Unable to perform desired measurement operation."
#define IVISCOPE_ERRMSG_MAX_TIME_EXCEEDED              "Maximum time exceeded before the operation completed."
#define IVISCOPE_ERRMSG_INVALID_ACQ_TYPE               "Invalid acquisition type."

#define IVISCOPE_ERROR_CODES_AND_MSGS \
        {IVISCOPE_ERROR_CHANNEL_NOT_ENABLED,           IVISCOPE_ERRMSG_CHANNEL_NOT_ENABLED}, \
        {IVISCOPE_ERROR_UNABLE_TO_PERFORM_MEASUREMENT, IVISCOPE_ERRMSG_UNABLE_TO_PERFORM_MEASUREMENT}, \
        {IVISCOPE_ERROR_MAX_TIME_EXCEEDED,             IVISCOPE_ERRMSG_MAX_TIME_EXCEEDED}, \
        {IVISCOPE_ERROR_INVALID_ACQ_TYPE,              IVISCOPE_ERRMSG_INVALID_ACQ_TYPE}, \
        {IVISCOPE_WARN_INVALID_WFM_ELEMENT,            IVISCOPE_WARNMSG_INVALID_WFM_ELEMENT}

/*- IviScopeObsolete.h included for backwards compatibility -*/
#include "IviScopeObsolete.h"

/*****************************************************************************
 *---------------------------- End Include File -----------------------------*
 *****************************************************************************/

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

#endif /* IVISCOPE_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviScopeObsolete.h sha256=1fbbc7246fba945b56d27e227c9315635f6a5bec6b4b04e3809a7c377399f634 bytes=9410 -->
## FILE: imports/include/IviScopeObsolete.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviScopeObsolete.h`
- sha256: `1fbbc7246fba945b56d27e227c9315635f6a5bec6b4b04e3809a7c377399f634`
- bytes: 9410

````c
/*****************************************************************************
 *                          I V I - S C O P E  1.0                           
 *----------------------------------------------------------------------------
 *    Copyright (c) 1999-2020 National Instruments.  All Rights Reserved.         
 *----------------------------------------------------------------------------
 *                                                                           
 * Title:       IviScopeObsolete.h                                           
 * Purpose:     IviScope Class value and attribute Id declarations for the   
 *              now obsolete IviScope 1.0 specification.                      
 *              These macros are defined to keep backward compatibility with 
 *              previous versions of this file.  Oscilloscope specific       
 *              drivers should no longer use these macros. Instead, the      
 *              drivers must use definitions from the current IviScope.h     
 *              header file.                                                 
 *****************************************************************************/

#ifndef IVISCOPE_HEADER_OBSOLETE
#define IVISCOPE_HEADER_OBSOLETE
#include <ivi.h>

    /*- Obsolete Inherent Attributes -*/
#define IVISCOPE_ATTR_CLASS_MAJOR_VERSION               IVI_ATTR_CLASS_MAJOR_VERSION
#define IVISCOPE_ATTR_CLASS_MINOR_VERSION               IVI_ATTR_CLASS_MINOR_VERSION
#define IVISCOPE_ATTR_CLASS_REVISION                    IVI_ATTR_CLASS_REVISION

#define IVISCOPE_ATTR_CLASS_PREFIX                      IVI_ATTR_CLASS_PREFIX
#define IVISCOPE_ATTR_SPECIFIC_PREFIX                   IVI_ATTR_SPECIFIC_PREFIX
#define IVISCOPE_ATTR_MODULE_PATHNAME                   IVI_ATTR_MODULE_PATHNAME

#define IVISCOPE_ATTR_DRIVER_MAJOR_VERSION              IVI_ATTR_DRIVER_MAJOR_VERSION
#define IVISCOPE_ATTR_DRIVER_MINOR_VERSION              IVI_ATTR_DRIVER_MINOR_VERSION
#define IVISCOPE_ATTR_DRIVER_REVISION                   IVI_ATTR_DRIVER_REVISION

#define IVISCOPE_ATTR_ENGINE_MAJOR_VERSION              IVI_ATTR_ENGINE_MAJOR_VERSION        /* ViInt32,  read-only */
#define IVISCOPE_ATTR_ENGINE_MINOR_VERSION              IVI_ATTR_ENGINE_MINOR_VERSION        /* ViInt32,  read-only */
#define IVISCOPE_ATTR_ENGINE_REVISION                   IVI_ATTR_ENGINE_REVISION             /* ViString, read-only */

#define IVISCOPE_ATTR_CLASS_DRIVER_MAJOR_VERSION        IVI_ATTR_CLASS_DRIVER_MAJOR_VERSION     /* ViInt32,  read-only */
#define IVISCOPE_ATTR_CLASS_DRIVER_MINOR_VERSION        IVI_ATTR_CLASS_DRIVER_MINOR_VERSION     /* ViInt32,  read-only */

#define IVISCOPE_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION     IVI_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVISCOPE_ATTR_SPECIFIC_DRIVER_MINOR_VERSION     IVI_ATTR_SPECIFIC_DRIVER_MINOR_VERSION  /* ViInt32,  read-only */

#define IVISCOPE_ATTR_NUM_CHANNELS                      IVI_ATTR_NUM_CHANNELS
#define IVISCOPE_ATTR_QUERY_INSTR_STATUS                IVI_ATTR_QUERY_INSTR_STATUS             /* ViBoolean */
#define IVISCOPE_ATTR_RESOURCE_DESCRIPTOR               IVI_ATTR_RESOURCE_DESCRIPTOR            /* ViString, read-only */

#define IVISCOPE_ATTR_IO_SESSION_TYPE                   IVI_ATTR_IO_SESSION_TYPE
#define IVISCOPE_ATTR_IO_SESSION                        IVI_ATTR_IO_SESSION

#define IVISCOPE_ATTR_ATTRIBUTE_CAPABILITIES    IVI_ATTR_ATTRIBUTE_CAPABILITIES        /* ViString, read-only */

    /*- Error Info -*/
#define IVISCOPE_ATTR_PRIMARY_ERROR                     IVI_ATTR_PRIMARY_ERROR                  /* ViInt32  */
#define IVISCOPE_ATTR_SECONDARY_ERROR                   IVI_ATTR_SECONDARY_ERROR                /* ViInt32  */
#define IVISCOPE_ATTR_ERROR_ELABORATION                 IVI_ATTR_ERROR_ELABORATION              /* ViString */

    /*- Obsolete Attributes -*/
#define IVISCOPE_ATTR_BANDWIDTH                         (IVI_CLASS_PUBLIC_ATTR_BASE  + 6L)
#define IVISCOPE_ATTR_HORZ_RECORD_REF_POSITION          (IVI_CLASS_PUBLIC_ATTR_BASE  + 11L)
#define IVISCOPE_ATTR_TRIGGER_DELAY_TIME                (IVI_CLASS_PUBLIC_ATTR_BASE  + 15L)
#define IVISCOPE_ATTR_TV_TRIGGER_SIGNAL_TYPE            (IVI_CLASS_PUBLIC_ATTR_BASE  + 201L)
#define IVISCOPE_ATTR_TV_TRIGGER_FIELD                  (IVI_CLASS_PUBLIC_ATTR_BASE  + 202L)
#define IVISCOPE_ATTR_TV_TRIGGER_LINE                   (IVI_CLASS_PUBLIC_ATTR_BASE  + 203L)         
        
    /*- Obsolete macros -*/
#define IVISCOPE_VAL_MAX_VALID_WFM_VOLTAGE          (1.0E+300)
#define IVISCOPE_VAL_INVALID_WFM_VOLTAGE            (1.0E+301)

    /*- Obsolete values for function parameters -*/
#define IVISCOPE_VAL_CALCULATION_SPECIFIC_DRIVER_BASE   (1000L)

    /*- Defined values for attributes -*/
        /*- IVISCOPE_ATTR_TRIGGER_TYPE values -*/
#define IVISCOPE_VAL_EDGE                       (1L)
#define IVISCOPE_VAL_WIDTH                      (101L)
#define IVISCOPE_VAL_RUNT                       (102L)
#define IVISCOPE_VAL_GLITCH                     (103L)
#define IVISCOPE_VAL_STATE                      (104L)
#define IVISCOPE_VAL_PATTERN                    (105L)
#define IVISCOPE_VAL_TV                         (106L)

    
        /*- IVISCOPE_ATTR_TRIGGER_SOURCE values -*/
#define IVISCOPE_VAL_IMMEDIATE                  "VAL_IMMEDIATE"
#define IVISCOPE_VAL_GPIB_GET                   "VAL_GPIB_GET"
#define IVISCOPE_VAL_SW_TRIG_FUNC               "VAL_SW_TRIG_FUNC"
#define IVISCOPE_VAL_AC_LINE                    "VAL_AC_LINE"

        /*- IVISCOPE_ATTR_TV_TRIGGER_SIGNAL_TYPE values -*/
#define IVISCOPE_VAL_TV_SIGNAL_TYPE_CLASS_EXT_BASE      (100L)
#define IVISCOPE_VAL_TV_SIGNAL_TYPE_SPECIFIC_EXT_BASE   (1000L)

        /*- IVISCOPE_ATTR_TV_TRIGGER_FIELD values -*/
#define IVISCOPE_VAL_TV_FIELD1                  (1L)
#define IVISCOPE_VAL_TV_FIELD2                  (2L)
#define IVISCOPE_VAL_TV_ANY_FIELD               (-1L)

#define IVISCOPE_VAL_TV_TRIGGER_FIELD_CLASS_EXT_BASE     (100L)
#define IVISCOPE_VAL_TV_TRIGGER_FIELD_SPECIFIC_EXT_BASE  (1000L)

        /*- IVISCOPE_ATTR_ACQUISITION_TYPE value -*/
#define IVISCOPE_VAL_ACQ_TYPE_CLASS_EXT_BASE    (100L)
#define IVISCOPE_VAL_ACQ_TYPE_SPECIFIC_EXT_BASE (1000L)

        /*- IVISCOPE_ATTR_NUM_ENVELOPES values -*/
        /*- IVISCOPE_ATTR_NUM_AVERAGES values -*/
#define IVISCOPE_VAL_INFINITE                   (-1L)

        /*- IVISCOPE_ATTR_INPUT_IMPEDANCE values -*/
#define IVISCOPE_VAL_50_OHMS                    (50.0)
#define IVISCOPE_VAL_75_OHMS                    (75.0)
#define IVISCOPE_VAL_1_MEG_OHM                  (1000000.0)

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviScope_GetErrorInfo (ViSession vi, 
                                         ViStatus *primaryError, 
                                         ViStatus *secondaryError, 
                                         ViChar errorElaboration[IVI_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC IviScope_ClearErrorInfo (ViSession vi);

    /*- IviScope Obsolete functions -*/
ViStatus _VI_FUNC IviScope_ConfigureVertical (ViSession vi, ViConstString channel,
                                              ViReal64 range, ViReal64 offset,
                                              ViInt32 coupling, ViReal64 probeAttenuation,
                                              ViBoolean enabled);
ViStatus _VI_FUNC IviScope_ConfigureHorizontal (ViSession vi, ViReal64 timePerRecord,
                                                ViInt32 minimumRecordLength,
                                                ViReal64 triggerPosition);
ViStatus _VI_FUNC IviScope_ConfigureTriggerSource (ViSession vi, ViConstString triggerSource,
                                                   ViInt32 triggerType, ViReal64 triggerDelay,
                                                   ViReal64 holdoff);
ViStatus _VI_FUNC IviScope_ConfigureEdgeTrigger (ViSession vi, ViReal64 level,
                                                 ViInt32 triggerCoupling, ViInt32 slope);
ViStatus _VI_FUNC IviScope_SendSWTrigger (ViSession vi);
ViStatus _VI_FUNC IviScope_ConfigureTVTrigger (ViSession vi, ViInt32 TVSignalType, 
                                               ViInt32 TVField, ViInt32 TVLine, ViInt32 TVPolarity);
ViStatus _VI_FUNC IviScope_ConfigureRuntTrigger (ViSession vi, ViReal64 runtLowThreshold,
                                                 ViReal64 runtHighThreshold, ViInt32 runtPolarity);
ViStatus _VI_FUNC IviScope_ConfigureGlitchTrigger (ViSession vi, ViReal64 level,
                                                   ViReal64 glitchWidth, ViInt32 glitchPolarity);
ViStatus _VI_FUNC IviScope_ConfigureWidthTrigger (ViSession vi, ViReal64 level,
                                                  ViReal64 widthLowThreshold, ViReal64 widthHighThreshold,
                                                  ViInt32 widthPolarity, ViInt32 widthCondition);
ViStatus _VI_FUNC IviScope_ConfigureAcquisition (ViSession vi, ViInt32 acquisitionType);

/*****************************************************************************
 *---------------------------- End Include File -----------------------------*
 *****************************************************************************/

#endif /* IVISCOPE_HEADER_OBSOLETE */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviSpecAn.h sha256=8b901706d16f768f778189c82125d22e438e6673d20f886ec8cbe26a06bc0474 bytes=41079 -->
## FILE: imports/include/IviSpecAn.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviSpecAn.h`
- sha256: `8b901706d16f768f778189c82125d22e438e6673d20f886ec8cbe26a06bc0474`
- bytes: 41079

````c
/****************************************************************************
 *                         IVISPECAN                               
 *---------------------------------------------------------------------------
 *    Copyright (c) 2009-2020 National Instruments.  All Rights Reserved.        
 *---------------------------------------------------------------------------
 *                                                                          
 * Title:       IviSpecAn.h                                                    
 * Purpose:     IviSpecAn Class declarations for the Base and Extended  
 *              IviSpecAn Capabilities.                                        
 ****************************************************************************/

#ifndef IVISPECAN_HEADER
#define IVISPECAN_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVISPECAN_MAJOR_VERSION              (4L)
#define IVISPECAN_MINOR_VERSION              (0L)

#define IVISPECAN_CLASS_SPEC_MAJOR_VERSION   (2L)
#define IVISPECAN_CLASS_SPEC_MINOR_VERSION   (0L)

#define IVISPECAN_DRIVER_VENDOR              "National Instruments"
#ifdef	_IVI_mswin64_
#define IVISPECAN_DRIVER_DESCRIPTION         "IviSpecAn Class Driver [Compiled for 64-bit.]"
#else
#define IVISPECAN_DRIVER_DESCRIPTION         "IviSpecAn Class Driver"
#endif

/****************************************************************************
 *------------------------------ Useful Macros -----------------------------*
 ****************************************************************************/


/****************************************************************************
 *------------------ IviSpecAn Class Attribute Defines ----------------------*
 ****************************************************************************/

    /*- IVI Inherent Attributes -*/

        /*- User Options -*/
#define IVISPECAN_ATTR_CACHE                     IVI_ATTR_CACHE                         /* ViBoolean */
#define IVISPECAN_ATTR_RANGE_CHECK               IVI_ATTR_RANGE_CHECK                   /* ViBoolean */
#define IVISPECAN_ATTR_QUERY_INSTRUMENT_STATUS   IVI_ATTR_QUERY_INSTRUMENT_STATUS       /* ViBoolean */
#define IVISPECAN_ATTR_RECORD_COERCIONS          IVI_ATTR_RECORD_COERCIONS              /* ViBoolean */
#define IVISPECAN_ATTR_SIMULATE                  IVI_ATTR_SIMULATE                      /* ViBoolean */
#define IVISPECAN_ATTR_INTERCHANGE_CHECK         IVI_ATTR_INTERCHANGE_CHECK             /* ViBoolean */
#define IVISPECAN_ATTR_SPY                       IVI_ATTR_SPY                           /* ViBoolean */
#define IVISPECAN_ATTR_USE_SPECIFIC_SIMULATION   IVI_ATTR_USE_SPECIFIC_SIMULATION       /* ViBoolean */

	/* Instrument Capabilities */
#define IVISPECAN_ATTR_CHANNEL_COUNT             IVI_ATTR_CHANNEL_COUNT                 /* ViInt32,  read-only  */

        /*- Instrument Capabilities -*/
#define IVISPECAN_ATTR_GROUP_CAPABILITIES        IVI_ATTR_GROUP_CAPABILITIES            /* ViString, read-only */
#define IVISPECAN_ATTR_FUNCTION_CAPABILITIES     IVI_ATTR_FUNCTION_CAPABILITIES         /* ViString, read-only */

        /*- Class Driver Information -*/    
#define IVISPECAN_ATTR_CLASS_DRIVER_PREFIX                         IVI_ATTR_CLASS_DRIVER_PREFIX                       /* ViString, read-only */
#define IVISPECAN_ATTR_CLASS_DRIVER_VENDOR                         IVI_ATTR_CLASS_DRIVER_VENDOR                       /* ViString, read-only */
#define IVISPECAN_ATTR_CLASS_DRIVER_DESCRIPTION                    IVI_ATTR_CLASS_DRIVER_DESCRIPTION                  /* ViString, read-only */
#define IVISPECAN_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION     /* ViInt32,  read-only */
#define IVISPECAN_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION     /* ViInt32,  read-only */

        /*- Specific Driver Information -*/    
#define IVISPECAN_ATTR_SPECIFIC_DRIVER_PREFIX                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX                    /* ViString, read-only */
#define IVISPECAN_ATTR_SPECIFIC_DRIVER_LOCATOR                     IVI_ATTR_SPECIFIC_DRIVER_LOCATOR                   /* ViString, read-only */
#define IVISPECAN_ATTR_IO_RESOURCE_DESCRIPTOR                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR                    /* ViString, read-only */
#define IVISPECAN_ATTR_LOGICAL_NAME                                IVI_ATTR_LOGICAL_NAME                              /* ViString, read-only */
#define IVISPECAN_ATTR_SPECIFIC_DRIVER_VENDOR                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR                    /* ViString, read-only */
#define IVISPECAN_ATTR_SPECIFIC_DRIVER_DESCRIPTION                 IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION               /* ViString, read-only */
#define IVISPECAN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVISPECAN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/    
#define IVISPECAN_ATTR_INSTRUMENT_FIRMWARE_REVISION     IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION   /* ViString, read-only */
#define IVISPECAN_ATTR_INSTRUMENT_MANUFACTURER          IVI_ATTR_INSTRUMENT_MANUFACTURER        /* ViString, read-only */
#define IVISPECAN_ATTR_INSTRUMENT_MODEL                 IVI_ATTR_INSTRUMENT_MODEL               /* ViString, read-only */
#define IVISPECAN_ATTR_SUPPORTED_INSTRUMENT_MODELS      IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS    /* ViString, read-only */
  
        /*- Version Information -*/
#define IVISPECAN_ATTR_CLASS_DRIVER_REVISION            IVI_ATTR_CLASS_DRIVER_REVISION          /* ViString, read-only */

#define IVISPECAN_ATTR_SPECIFIC_DRIVER_REVISION         IVI_ATTR_SPECIFIC_DRIVER_REVISION       /* ViString, read-only */

        /*- Driver Setup information -*/
#define IVISPECAN_ATTR_DRIVER_SETUP                     IVI_ATTR_DRIVER_SETUP                   /* ViString */

    /*- IviSpecAn Fundamental Attributes -*/
#define IVISPECAN_ATTR_AMPLITUDE_UNITS                               (IVI_CLASS_PUBLIC_ATTR_BASE + 1L)    /* ViInt32 */
#define IVISPECAN_ATTR_ATTENUATION                                   (IVI_CLASS_PUBLIC_ATTR_BASE + 2L)    /* ViReal64 */
#define IVISPECAN_ATTR_ATTENUATION_AUTO                              (IVI_CLASS_PUBLIC_ATTR_BASE + 3L)    /* ViBoolean */
#define IVISPECAN_ATTR_DETECTOR_TYPE                                 (IVI_CLASS_PUBLIC_ATTR_BASE + 4L)    /* ViInt32 */
#define IVISPECAN_ATTR_DETECTOR_TYPE_AUTO                            (IVI_CLASS_PUBLIC_ATTR_BASE + 5L)    /* ViBoolean */
#define IVISPECAN_ATTR_FREQUENCY_START                               (IVI_CLASS_PUBLIC_ATTR_BASE + 6L)    /* ViReal64 */
#define IVISPECAN_ATTR_FREQUENCY_STOP                                (IVI_CLASS_PUBLIC_ATTR_BASE + 7L)    /* ViReal64 */
#define IVISPECAN_ATTR_FREQUENCY_OFFSET                              (IVI_CLASS_PUBLIC_ATTR_BASE + 8L)    /* ViReal64 */
#define IVISPECAN_ATTR_INPUT_IMPEDANCE                               (IVI_CLASS_PUBLIC_ATTR_BASE + 9L)    /* ViReal64 */
#define IVISPECAN_ATTR_NUMBER_OF_SWEEPS                              (IVI_CLASS_PUBLIC_ATTR_BASE + 10L)   /* ViInt32 */
#define IVISPECAN_ATTR_REFERENCE_LEVEL                               (IVI_CLASS_PUBLIC_ATTR_BASE + 11L)   /* ViReal64 */
#define IVISPECAN_ATTR_REFERENCE_LEVEL_OFFSET                        (IVI_CLASS_PUBLIC_ATTR_BASE + 12L)   /* ViReal64 */
#define IVISPECAN_ATTR_RESOLUTION_BANDWIDTH                          (IVI_CLASS_PUBLIC_ATTR_BASE + 13L)   /* ViReal64 */
#define IVISPECAN_ATTR_RESOLUTION_BANDWIDTH_AUTO                     (IVI_CLASS_PUBLIC_ATTR_BASE + 14L)   /* ViBoolean */
#define IVISPECAN_ATTR_SWEEP_MODE_CONTINUOUS                         (IVI_CLASS_PUBLIC_ATTR_BASE + 15L)   /* ViBoolean */
#define IVISPECAN_ATTR_SWEEP_TIME                                    (IVI_CLASS_PUBLIC_ATTR_BASE + 16L)   /* ViReal64 */
#define IVISPECAN_ATTR_SWEEP_TIME_AUTO                               (IVI_CLASS_PUBLIC_ATTR_BASE + 17L)   /* ViBoolean */
#define IVISPECAN_ATTR_TRACE_COUNT                                   (IVI_CLASS_PUBLIC_ATTR_BASE + 18L)   /* ViInt32 */
#define IVISPECAN_ATTR_TRACE_SIZE                                    (IVI_CLASS_PUBLIC_ATTR_BASE + 19L)   /* ViInt32 */
#define IVISPECAN_ATTR_TRACE_TYPE                                    (IVI_CLASS_PUBLIC_ATTR_BASE + 20L)   /* ViInt32 */
#define IVISPECAN_ATTR_VERTICAL_SCALE                                (IVI_CLASS_PUBLIC_ATTR_BASE + 21L)   /* ViInt32 */
#define IVISPECAN_ATTR_VIDEO_BANDWIDTH                               (IVI_CLASS_PUBLIC_ATTR_BASE + 22L)   /* ViReal64 */
#define IVISPECAN_ATTR_VIDEO_BANDWIDTH_AUTO                          (IVI_CLASS_PUBLIC_ATTR_BASE + 23L)   /* ViBoolean */

    /*- IviSpecAn Extended Attributes -*/
        /*- IviSpecAnMarker Extension Group -*/
#define IVISPECAN_ATTR_ACTIVE_MARKER                                 (IVI_CLASS_PUBLIC_ATTR_BASE + 201L)  /* ViString */
#define IVISPECAN_ATTR_MARKER_AMPLITUDE                              (IVI_CLASS_PUBLIC_ATTR_BASE + 202L)  /* ViReal64 */
#define IVISPECAN_ATTR_MARKER_COUNT                                  (IVI_CLASS_PUBLIC_ATTR_BASE + 203L)  /* ViInt32 */
#define IVISPECAN_ATTR_MARKER_ENABLED                                (IVI_CLASS_PUBLIC_ATTR_BASE + 204L)  /* ViBoolean */
#define IVISPECAN_ATTR_MARKER_FREQUENCY_COUNTER_ENABLED              (IVI_CLASS_PUBLIC_ATTR_BASE + 205L)  /* ViBoolean */
#define IVISPECAN_ATTR_MARKER_FREQUENCY_COUNTER_RESOLUTION           (IVI_CLASS_PUBLIC_ATTR_BASE + 206L)  /* ViReal64 */
#define IVISPECAN_ATTR_MARKER_POSITION                               (IVI_CLASS_PUBLIC_ATTR_BASE + 207L)  /* ViReal64 */
#define IVISPECAN_ATTR_MARKER_THRESHOLD                              (IVI_CLASS_PUBLIC_ATTR_BASE + 208L)  /* ViReal64 */
#define IVISPECAN_ATTR_MARKER_TRACE                                  (IVI_CLASS_PUBLIC_ATTR_BASE + 209L)  /* ViString */
#define IVISPECAN_ATTR_PEAK_EXCURSION                                (IVI_CLASS_PUBLIC_ATTR_BASE + 210L)  /* ViReal64 */
#define IVISPECAN_ATTR_SIGNAL_TRACK_ENABLED                          (IVI_CLASS_PUBLIC_ATTR_BASE + 211L)  /* ViBoolean */

        /*- IviSpecAnTrigger Extension Group -*/
#define IVISPECAN_ATTR_TRIGGER_SOURCE                                (IVI_CLASS_PUBLIC_ATTR_BASE + 301L)  /* ViInt32 */

        /*- IviSpecAnExternalTrigger Extension Group -*/
#define IVISPECAN_ATTR_EXTERNAL_TRIGGER_LEVEL                        (IVI_CLASS_PUBLIC_ATTR_BASE + 401L)  /* ViReal64 */
#define IVISPECAN_ATTR_EXTERNAL_TRIGGER_SLOPE                        (IVI_CLASS_PUBLIC_ATTR_BASE + 402L)  /* ViInt32 */

        /*- IviSpecAnVideoTrigger Extension Group -*/
#define IVISPECAN_ATTR_VIDEO_TRIGGER_LEVEL                           (IVI_CLASS_PUBLIC_ATTR_BASE + 501L)  /* ViReal64 */
#define IVISPECAN_ATTR_VIDEO_TRIGGER_SLOPE                           (IVI_CLASS_PUBLIC_ATTR_BASE + 502L)  /* ViInt32 */

        /*- IviSpecAnDisplay Extension Group -*/
#define IVISPECAN_ATTR_NUMBER_OF_DIVISIONS                           (IVI_CLASS_PUBLIC_ATTR_BASE + 602L)  /* ViInt32 */
#define IVISPECAN_ATTR_UNITS_PER_DIVISION                            (IVI_CLASS_PUBLIC_ATTR_BASE + 601L)  /* ViReal64 */

        /*- IviSpecAnMarkerType Extension Group -*/
#define IVISPECAN_ATTR_MARKER_TYPE                                   (IVI_CLASS_PUBLIC_ATTR_BASE + 701L)  /* ViInt32 */

        /*- IviSpecAnDeltaMarker Extension Group -*/
#define IVISPECAN_ATTR_REFERENCE_MARKER_AMPLITUDE                    (IVI_CLASS_PUBLIC_ATTR_BASE + 801L)  /* ViReal64 */
#define IVISPECAN_ATTR_REFERENCE_MARKER_POSITION                     (IVI_CLASS_PUBLIC_ATTR_BASE + 802L)  /* ViReal64 */

        /*- IviSpecAnExternalMixer Extension Group -*/
#define IVISPECAN_ATTR_EXTERNAL_MIXER_AVERAGE_CONVERSION_LOSS        (IVI_CLASS_PUBLIC_ATTR_BASE + 901L)  /* ViReal64 */
#define IVISPECAN_ATTR_EXTERNAL_MIXER_BIAS                           (IVI_CLASS_PUBLIC_ATTR_BASE + 902L)  /* ViReal64 */
#define IVISPECAN_ATTR_EXTERNAL_MIXER_BIAS_ENABLED                   (IVI_CLASS_PUBLIC_ATTR_BASE + 903L)  /* ViBoolean */
#define IVISPECAN_ATTR_EXTERNAL_MIXER_BIAS_LIMIT                     (IVI_CLASS_PUBLIC_ATTR_BASE + 904L)  /* ViReal64 */
#define IVISPECAN_ATTR_EXTERNAL_MIXER_CONVERSION_LOSS_TABLE_ENABLED  (IVI_CLASS_PUBLIC_ATTR_BASE + 905L)  /* ViBoolean */
#define IVISPECAN_ATTR_EXTERNAL_MIXER_ENABLED                        (IVI_CLASS_PUBLIC_ATTR_BASE + 906L)  /* ViBoolean */
#define IVISPECAN_ATTR_EXTERNAL_MIXER_HARMONIC                       (IVI_CLASS_PUBLIC_ATTR_BASE + 907L)  /* ViInt32 */
#define IVISPECAN_ATTR_EXTERNAL_MIXER_NUMBER_OF_PORTS                (IVI_CLASS_PUBLIC_ATTR_BASE + 908L)  /* ViInt32 */

        /*- IviSpecAn Extension Bases -*/
#define IVISPECAN_VENDOR_CLASS_VAL_EXT_BASE                                (500L)
#define IVISPECAN_INSTR_SPECIFIC_VAL_EXT_BASE                              (1000L)
/****************************************************************************
 *----------------- IviSpecAn Class Attribute Value Defines -----------------*
 ****************************************************************************/
/*- Defined values for attribute IVISPECAN_ATTR_AMPLITUDE_UNITS -*/
#define IVISPECAN_VAL_AMPLITUDE_UNITS_DBM                                 (1L)
#define IVISPECAN_VAL_AMPLITUDE_UNITS_DBMV                                (2L)
#define IVISPECAN_VAL_AMPLITUDE_UNITS_DBUV                                (3L)
#define IVISPECAN_VAL_AMPLITUDE_UNITS_VOLT                                (4L)
#define IVISPECAN_VAL_AMPLITUDE_UNITS_WATT                                (5L)
#define IVISPECAN_VAL_AMPLITUDE_UNITS_CLASS_EXT_BASE                      (500L)
#define IVISPECAN_VAL_AMPLITUDE_UNITS_SPECIFIC_EXT_BASE                   (1000L)

/*- Defined values for attribute IVISPECAN_ATTR_DETECTOR_TYPE -*/
#define IVISPECAN_VAL_DETECTOR_TYPE_AUTO_PEAK                             (1L)
#define IVISPECAN_VAL_DETECTOR_TYPE_AVERAGE                               (2L)
#define IVISPECAN_VAL_DETECTOR_TYPE_MAX_PEAK                              (3L)
#define IVISPECAN_VAL_DETECTOR_TYPE_MIN_PEAK                              (4L)
#define IVISPECAN_VAL_DETECTOR_TYPE_SAMPLE                                (5L)
#define IVISPECAN_VAL_DETECTOR_TYPE_RMS                                   (6L)
#define IVISPECAN_VAL_DETECTOR_TYPE_CLASS_EXT_BASE                        (500L)
#define IVISPECAN_VAL_DETECTOR_TYPE_SPECIFIC_EXT_BASE                     (1000L)

/*- Defined values for attribute IVISPECAN_ATTR_TRACE_TYPE -*/
#define IVISPECAN_VAL_TRACE_TYPE_CLEAR_WRITE                              (1L)
#define IVISPECAN_VAL_TRACE_TYPE_MAX_HOLD                                 (2L)
#define IVISPECAN_VAL_TRACE_TYPE_MIN_HOLD                                 (3L)
#define IVISPECAN_VAL_TRACE_TYPE_VIDEO_AVERAGE                            (4L)
#define IVISPECAN_VAL_TRACE_TYPE_VIEW                                     (5L)
#define IVISPECAN_VAL_TRACE_TYPE_STORE                                    (6L)
#define IVISPECAN_VAL_TRACE_TYPE_CLASS_EXT_BASE                           (500L)
#define IVISPECAN_VAL_TRACE_TYPE_SPECIFIC_EXT_BASE                        (1000L)

/*- Defined values for attribute IVISPECAN_ATTR_VERTICAL_SCALE -*/
#define IVISPECAN_VAL_VERTICAL_SCALE_LINEAR                               (1L)
#define IVISPECAN_VAL_VERTICAL_SCALE_LOGARITHMIC                          (2L)
#define IVISPECAN_VAL_VERTICAL_SCALE_CLASS_EXT_BASE                       (500L)
#define IVISPECAN_VAL_VERTICAL_SCALE_SPECIFIC_EXT_BASE                    (1000L)

/*- Defined values for attribute IVISPECAN_ATTR_TRIGGER_SOURCE -*/
#define IVISPECAN_VAL_TRIGGER_SOURCE_EXTERNAL                             (1L)
#define IVISPECAN_VAL_TRIGGER_SOURCE_IMMEDIATE                            (2L)
#define IVISPECAN_VAL_TRIGGER_SOURCE_SOFTWARE                             (3L)
#define IVISPECAN_VAL_TRIGGER_SOURCE_AC_LINE                              (4L)
#define IVISPECAN_VAL_TRIGGER_SOURCE_VIDEO                                (5L)
#define IVISPECAN_VAL_TRIGGER_SOURCE_CLASS_EXT_BASE                       (500L)
#define IVISPECAN_VAL_TRIGGER_SOURCE_SPECIFIC_EXT_BASE                    (1000L)

/*- Defined values for attribute IVISPECAN_ATTR_EXTERNAL_TRIGGER_SLOPE -*/
#define IVISPECAN_VAL_EXTERNAL_TRIGGER_SLOPE_POSITIVE                     (1L)
#define IVISPECAN_VAL_EXTERNAL_TRIGGER_SLOPE_NEGATIVE                     (2L)
#define IVISPECAN_VAL_EXTERNAL_TRIGGER_SLOPE_CLASS_EXT_BASE               (500L)
#define IVISPECAN_VAL_EXTERNAL_TRIGGER_SLOPE_SPECIFIC_EXT_BASE            (1000L)

/*- Defined values for attribute IVISPECAN_ATTR_VIDEO_TRIGGER_SLOPE -*/
#define IVISPECAN_VAL_VIDEO_TRIGGER_SLOPE_POSITIVE                        (1L)
#define IVISPECAN_VAL_VIDEO_TRIGGER_SLOPE_NEGATIVE                        (2L)
#define IVISPECAN_VAL_VIDEO_TRIGGER_SLOPE_CLASS_EXT_BASE                  (500L)
#define IVISPECAN_VAL_VIDEO_TRIGGER_SLOPE_SPECIFIC_EXT_BASE               (1000L)

/*- Defined values for attribute IVISPECAN_ATTR_MARKER_TYPE -*/
#define IVISPECAN_VAL_MARKER_TYPE_NORMAL                                  (1L)
#define IVISPECAN_VAL_MARKER_TYPE_DELTA                                   (2L)
#define IVISPECAN_VAL_MARKER_TYPE_CLASS_EXT_BASE                          (500L)
#define IVISPECAN_VAL_MARKER_TYPE_SPECIFIC_EXT_BASE                       (1000L)



/****************************************************************************
 *------------- IviSpecAn Function Parameter Value Definitions -------------*
 ****************************************************************************/
/*- Defined values for status parameter of function -*/
/*- IviSpecAn_AcquisitionStatus -*/
#define IVISPECAN_VAL_ACQUISITION_STATUS_COMPLETE                         (1L)
#define IVISPECAN_VAL_ACQUISITION_STATUS_IN_PROGRESS                      (0L)
#define IVISPECAN_VAL_ACQUISITION_STATUS_UNKNOWN                          (-1L)

/*- Defined values for MaxTime parameter of function -*/
/*- IviSpecAn_ReadYTrace -*/
#define IVISPECAN_VAL_MAX_TIME_IMMEDIATE                                  (0x0L)
#define IVISPECAN_VAL_MAX_TIME_INFINITE                                   (0xFFFFFFFFUL)

/*- Defined values for SearchType parameter of function -*/
/*- IviSpecAn_MarkerSearch -*/
#define IVISPECAN_VAL_MARKER_SEARCH_HIGHEST                               (1L)
#define IVISPECAN_VAL_MARKER_SEARCH_MINIMUM                               (2L)
#define IVISPECAN_VAL_MARKER_SEARCH_NEXT_PEAK                             (3L)
#define IVISPECAN_VAL_MARKER_SEARCH_NEXT_PEAK_LEFT                        (4L)
#define IVISPECAN_VAL_MARKER_SEARCH_NEXT_PEAK_RIGHT                       (5L)
#define IVISPECAN_VAL_MARKER_SEARCH_CLASS_EXT_BASE                        (500L)
#define IVISPECAN_VAL_MARKER_SEARCH_SPECIFIC_EXT_BASE                     (1000L)

/*- Defined values for InstrumentSetting parameter of function -*/
/*- IviSpecAn_SetInstrumentFromMarker -*/
#define IVISPECAN_VAL_INSTRUMENT_SETTING_FREQUENCY_CENTER                 (1L)
#define IVISPECAN_VAL_INSTRUMENT_SETTING_FREQUENCY_SPAN                   (2L)
#define IVISPECAN_VAL_INSTRUMENT_SETTING_FREQUENCY_START                  (3L)
#define IVISPECAN_VAL_INSTRUMENT_SETTING_FREQUENCY_STOP                   (4L)
#define IVISPECAN_VAL_INSTRUMENT_SETTING_REFERENCE_LEVEL                  (5L)
#define IVISPECAN_VAL_INSTRUMENT_SETTING_CLASS_EXT_BASE                   (500L)
#define IVISPECAN_VAL_INSTRUMENT_SETTING_SPECIFIC_EXT_BASE                (1000L)


/****************************************************************************
 *--------- IviSpecAn Class Instrument Driver Function Declarations ---------*
 ****************************************************************************/
    /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviSpecAn_init (ViRsrc logicalName, 
                                 ViBoolean idQuery, 
                                 ViBoolean resetDevice, 
                                 ViSession *vi);

ViStatus _VI_FUNC IviSpecAn_close (ViSession vi);

ViStatus _VI_FUNC IviSpecAn_reset (ViSession vi);

ViStatus _VI_FUNC IviSpecAn_self_test (ViSession vi, 
                                      ViInt16 *selfTestResult, 
                                      ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviSpecAn_error_query (ViSession vi, 
                                        ViInt32 *errorCode, 
                                        ViChar errorMessage[]);

ViStatus _VI_FUNC IviSpecAn_error_message (ViSession vi, 
                                          ViStatus statusCode, 
                                          ViChar message[]);

ViStatus _VI_FUNC IviSpecAn_revision_query (ViSession vi, 
                                           ViChar driverRev[], 
                                           ViChar instrRev[]);
    /*- Utility Functions -*/
ViStatus _VI_FUNC IviSpecAn_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviSpecAn_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviSpecAn_Disable (ViSession vi);

    /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviSpecAn_InitWithOptions (ViRsrc logicalName, 
                                            ViBoolean IDQuery,
                                            ViBoolean resetDevice, 
                                            ViConstString optionString, 
                                            ViSession *vi);

    /*- Set, Get, and Check Attribute Functions -*/

ViStatus _VI_FUNC IviSpecAn_GetAttributeViInt32 (ViSession vi, 
                                                ViConstString repeatedCapName,
                                                ViAttr attributeId,
                                                ViInt32 *value);

ViStatus _VI_FUNC IviSpecAn_SetAttributeViInt32 (ViSession vi, 
                                                ViConstString repeatedCapName,
                                                ViAttr attributeId,
                                                ViInt32 value);

ViStatus _VI_FUNC IviSpecAn_CheckAttributeViInt32 (ViSession vi, 
                                                  ViConstString repeatedCapName,
                                                  ViAttr attributeId,
                                                  ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviSpecAn_GetAttributeViInt64 (ViSession vi, 
                                                ViConstString repeatedCapName,
                                                ViAttr attributeId,
                                                ViInt64 *value);

ViStatus _VI_FUNC IviSpecAn_SetAttributeViInt64 (ViSession vi, 
                                                ViConstString repeatedCapName,
                                                ViAttr attributeId,
                                                ViInt64 value);

ViStatus _VI_FUNC IviSpecAn_CheckAttributeViInt64 (ViSession vi, 
                                                  ViConstString repeatedCapName,
                                                  ViAttr attributeId,
                                                  ViInt64 value);
#endif

ViStatus _VI_FUNC IviSpecAn_GetAttributeViReal64 (ViSession vi, 
                                                 ViConstString repeatedCapName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 *value);

ViStatus _VI_FUNC IviSpecAn_SetAttributeViReal64 (ViSession vi, 
                                                 ViConstString repeatedCapName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 value);

ViStatus _VI_FUNC IviSpecAn_CheckAttributeViReal64 (ViSession vi, 
                                                   ViConstString repeatedCapName, 
                                                   ViAttr attributeId, 
                                                   ViReal64 value);

ViStatus _VI_FUNC IviSpecAn_GetAttributeViString (ViSession vi, 
                                                 ViConstString repeatedCapName, 
                                                 ViAttr attributeId, 
                                                 ViInt32 bufferSize, 
                                                 ViChar value[]);

ViStatus _VI_FUNC IviSpecAn_SetAttributeViString (ViSession vi, 
                                                 ViConstString repeatedCapName, 
                                                 ViAttr attributeId, 
                                                 ViConstString value);

ViStatus _VI_FUNC IviSpecAn_CheckAttributeViString (ViSession vi, 
                                                   ViConstString repeatedCapName, 
                                                   ViAttr attributeId, 
                                                   ViConstString value); 

ViStatus _VI_FUNC IviSpecAn_GetAttributeViBoolean (ViSession vi, 
                                                  ViConstString repeatedCapName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean *value);

ViStatus _VI_FUNC IviSpecAn_SetAttributeViBoolean (ViSession vi, 
                                                  ViConstString repeatedCapName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean value);

ViStatus _VI_FUNC IviSpecAn_CheckAttributeViBoolean (ViSession vi, 
                                                    ViConstString repeatedCapName, 
                                                    ViAttr attributeId, 
                                                    ViBoolean value);

ViStatus _VI_FUNC IviSpecAn_GetAttributeViSession (ViSession vi, 
                                                  ViConstString repeatedCapName, 
                                                  ViAttr attributeId, 
                                                  ViSession *value);

ViStatus _VI_FUNC IviSpecAn_SetAttributeViSession (ViSession vi, 
                                                  ViConstString repeatedCapName, 
                                                  ViAttr attributeId, 
                                                  ViSession value);

ViStatus _VI_FUNC IviSpecAn_CheckAttributeViSession (ViSession vi, 
                                                    ViConstString repeatedCapName, 
                                                    ViAttr attributeId, 
                                                    ViSession value);

    /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviSpecAn_LockSession (ViSession vi, 
                                        ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviSpecAn_UnlockSession (ViSession vi, 
                                          ViBoolean *callerHasLock);

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviSpecAn_GetError (ViSession vi, 
                                   ViStatus *errorCode, 
                                   ViInt32 bufferSize, 
                                   ViChar description[]);

ViStatus _VI_FUNC IviSpecAn_ClearError (ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviSpecAn_GetNextInterchangeWarning (ViSession vi, 
                                                      ViInt32 bufferSize,
                                                      ViChar warning[]);

ViStatus _VI_FUNC IviSpecAn_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviSpecAn_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviSpecAn_GetNextCoercionRecord (ViSession vi,
                                                  ViInt32 bufferSize, 
                                                  ViChar record[]);

ViStatus _VI_FUNC IviSpecAn_GetSpecificDriverCHandle (ViSession vi,
                                                     ViSession* specificDriverCHandle);

    /*- IviSpecAn Fundamental Capabilities -*/
ViStatus _VI_FUNC IviSpecAn_Abort (ViSession vi);

ViStatus _VI_FUNC IviSpecAn_AcquisitionStatus (ViSession vi,
                                               ViInt32* status);

ViStatus _VI_FUNC IviSpecAn_ConfigureAcquisition (ViSession vi,
                                                  ViBoolean sweepModeContinuous,
                                                  ViInt32 numberOfSweeps,
                                                  ViBoolean detectorTypeAuto,
                                                  ViInt32 detectorType,
                                                  ViInt32 verticalScale);

ViStatus _VI_FUNC IviSpecAn_ConfigureFrequencyCenterSpan (ViSession vi,
                                                          ViReal64 CenterFrequency,
                                                          ViReal64 Span);

ViStatus _VI_FUNC IviSpecAn_ConfigureFrequencyOffset (ViSession vi,
                                                      ViReal64 FrequencyOffset);

ViStatus _VI_FUNC IviSpecAn_ConfigureFrequencyStartStop (ViSession vi,
                                                         ViReal64 StartFrequency,
                                                         ViReal64 StopFrequency);

ViStatus _VI_FUNC IviSpecAn_ConfigureLevel (ViSession vi,
                                            ViInt32 AmplitudeUnits,
                                            ViReal64 InputImpedance,
                                            ViReal64 ReferenceLevel,
                                            ViReal64 ReferenceLevelOffset,
                                            ViBoolean AttenuationAuto,
                                            ViReal64 Attenuation);

ViStatus _VI_FUNC IviSpecAn_ConfigureSweepCoupling (ViSession vi,
                                                    ViBoolean ResolutionBandwidtAuto,
                                                    ViReal64 ResolutionBandwidth,
                                                    ViBoolean VideoBandwidthAuto,
                                                    ViReal64 VideoBandwidth,
                                                    ViBoolean SweepTimeAuto,
                                                    ViReal64 SweepTime);

ViStatus _VI_FUNC IviSpecAn_ConfigureTraceType (ViSession vi,
                                                ViConstString TraceName,
                                                ViInt32 TraceType);

ViStatus _VI_FUNC IviSpecAn_FetchYTrace (ViSession vi,
                                         ViConstString TraceName,
                                         ViInt32 ArrayLength,
                                         ViInt32* ActualPoints,
                                         ViReal64 Amplitude[]);

ViStatus _VI_FUNC IviSpecAn_GetTraceName (ViSession vi,
                                          ViInt32 Index,
                                          ViInt32 NameBufferSize,
                                          ViChar Name[]);

ViStatus _VI_FUNC IviSpecAn_Initiate (ViSession vi);

ViStatus _VI_FUNC IviSpecAn_QueryTraceSize (ViSession vi,
                                            ViConstString TraceName,
                                            ViInt32* TraceSize);

ViStatus _VI_FUNC IviSpecAn_ReadYTrace (ViSession vi,
                                        ViConstString TraceName,
                                        ViInt32 MaxTime,
                                        ViInt32 ArrayLength,
                                        ViInt32* ActualPoints,
                                        ViReal64 Amplitude[]);


    /*- IviSpecAnMultitrace Extension Group -*/
ViStatus _VI_FUNC IviSpecAn_AddTraces (ViSession vi,
                                       ViConstString DestinationTrace,
                                       ViConstString Trace1,
                                       ViConstString Trace2);

ViStatus _VI_FUNC IviSpecAn_CopyTrace (ViSession vi,
                                       ViConstString DestinationTrace,
                                       ViConstString SourceTrace);

ViStatus _VI_FUNC IviSpecAn_ExchangeTraces (ViSession vi,
                                            ViConstString Trace1,
                                            ViConstString Trace2);

ViStatus _VI_FUNC IviSpecAn_SubtractTraces (ViSession vi,
                                            ViConstString DestinationTrace,
                                            ViConstString Trace1,
                                            ViConstString Trace2);


    /*- IviSpecAnMarker Extension Group -*/
ViStatus _VI_FUNC IviSpecAn_ConfigureMarkerEnabled (ViSession vi,
                                                    ViBoolean MarkerEnabled,
                                                    ViConstString MarkerTraceName);

ViStatus _VI_FUNC IviSpecAn_ConfigureMarkerFrequencyCounter (ViSession vi,
                                                             ViBoolean Enabled,
                                                             ViReal64 Resolution);

ViStatus _VI_FUNC IviSpecAn_ConfigureMarkerSearch (ViSession vi,
                                                   ViReal64 PeakExcursion,
                                                   ViReal64 MarkerThreshold);

ViStatus _VI_FUNC IviSpecAn_ConfigureSignalTrackEnabled (ViSession vi,
                                                         ViBoolean SignalTrackEnabled);

ViStatus _VI_FUNC IviSpecAn_DisableAllMarkers (ViSession vi);

ViStatus _VI_FUNC IviSpecAn_GetMarkerName (ViSession vi,
                                           ViInt32 Index,
                                           ViInt32 NameBufferSize,
                                           ViChar Name[]);

ViStatus _VI_FUNC IviSpecAn_MarkerSearch (ViSession vi,
                                          ViInt32 SearchType);

ViStatus _VI_FUNC IviSpecAn_MoveMarker (ViSession vi,
                                        ViReal64 MarkerPosition);

ViStatus _VI_FUNC IviSpecAn_QueryMarker (ViSession vi,
                                         ViReal64* MarkerPosition,
                                         ViReal64* MarkerAmplitude);

ViStatus _VI_FUNC IviSpecAn_SetActiveMarker (ViSession vi,
                                             ViConstString ActiveMarker);

ViStatus _VI_FUNC IviSpecAn_SetInstrumentFromMarker (ViSession vi,
                                                     ViInt32 InstrumentSetting);


    /*- IviSpecAnTrigger Extension Group -*/
ViStatus _VI_FUNC IviSpecAn_ConfigureTriggerSource (ViSession vi,
                                                    ViInt32 TriggerSource);


    /*- IviSpecAnExternalTrigger Extension Group -*/
ViStatus _VI_FUNC IviSpecAn_ConfigureExternalTrigger (ViSession vi,
                                                      ViReal64 ExternalTriggerLevel,
                                                      ViInt32 ExternalTriggerSlope);


    /*- IviSpecAnSoftwareTrigger Extension Group -*/
ViStatus _VI_FUNC IviSpecAn_SendSoftwareTrigger (ViSession vi);


    /*- IviSpecAnVideoTrigger Extension Group -*/
ViStatus _VI_FUNC IviSpecAn_ConfigureVideoTrigger (ViSession vi,
                                                   ViReal64 VideoTriggerLevel,
                                                   ViInt32 VideoTriggerSlope);


    /*- IviSpecAnMarkerType Extension Group -*/
ViStatus _VI_FUNC IviSpecAn_QueryMarkerType (ViSession vi,
                                             ViInt32* MarkerType);


    /*- IviSpecAnDeltaMarker Extension Group -*/
ViStatus _VI_FUNC IviSpecAn_MakeMarkerDelta (ViSession vi,
                                             ViBoolean DeltaMarker);

ViStatus _VI_FUNC IviSpecAn_QueryReferenceMarker (ViSession vi,
                                                  ViReal64* ReferenceMarkerAmplitude,
                                                  ViReal64* ReferenceMarkerPosition);


    /*- IviSpecAnExternalMixer Extension Group -*/
ViStatus _VI_FUNC IviSpecAn_ConfigureConversionLossTable (ViSession vi,
                                                          ViInt32 Count,
                                                          ViReal64 Frequency[],
                                                          ViReal64 ConversionLoss[]);

ViStatus _VI_FUNC IviSpecAn_ConfigureConversionLossTableEnabled (ViSession vi,
                                                                 ViBoolean ConversionLossTableEnabled);

ViStatus _VI_FUNC IviSpecAn_ConfigureExternalMixer (ViSession vi,
                                                    ViInt32 Harmonic,
                                                    ViReal64 AverageConversionLoss);

ViStatus _VI_FUNC IviSpecAn_ConfigureExternalMixerBias (ViSession vi,
                                                        ViReal64 Bias,
                                                        ViReal64 BiasLimit);

ViStatus _VI_FUNC IviSpecAn_ConfigureExternalMixerBiasEnabled (ViSession vi,
                                                               ViBoolean BiasEnabled);

ViStatus _VI_FUNC IviSpecAn_ConfigureExternalMixerEnabled (ViSession vi,
                                                           ViBoolean ExternalMixerEnabled);

ViStatus _VI_FUNC IviSpecAn_ConfigureExternalMixerNumberOfPorts (ViSession vi,
                                                                 ViInt32 NumberOfPorts);


    /*- IviSpecAnPreselector Extension Group -*/
ViStatus _VI_FUNC IviSpecAn_PeakPreselector (ViSession vi);



/****************************************************************************
 *--------------- IviSpecAn Class Error And Completion Codes ----------------*
 ****************************************************************************/
#define IVISPECAN_WARN_MEASURE_UNCALIBRATED    (IVI_CLASS_WARN_BASE + 0x0001L)
#define IVISPECAN_WARN_OVER_RANGE              (IVI_CLASS_WARN_BASE + 0x0002L)

#define IVISPECAN_ERROR_MARKER_NOT_ENABLED     (IVI_CLASS_ERROR_BASE + 0x0003L)
#define IVISPECAN_ERROR_NOT_DELTA_MARKER       (IVI_CLASS_ERROR_BASE + 0x0002L)
#define IVISPECAN_ERROR_MAX_TIME_EXCEEDED      (IVI_CLASS_ERROR_BASE + 0x0001L)
#define IVISPECAN_ERROR_TRIGGER_NOT_SOFTWARE   (IVI_CROSS_CLASS_ERROR_BASE + 1L)



#define IVISPECAN_WARNMSG_MEASURE_UNCALIBRATED "The instrument was in an uncalibrated state when the measurement was taken."
#define IVISPECAN_WARNMSG_OVER_RANGE           "The measurement taken was over the instrument’s range."

#define IVISPECAN_ERRMSG_MARKER_NOT_ENABLED    "The Active Marker is not enabled."
#define IVISPECAN_ERRMSG_NOT_DELTA_MARKER      "The Active Marker is not a delta marker."
#define IVISPECAN_ERRMSG_MAX_TIME_EXCEEDED     "The maximum waiting time for this operation was exceeded."
#define IVISPECAN_ERRMSG_TRIGGER_NOT_SOFTWARE  "The trigger source is not set to software trigger."

#define IVISPECAN_ERROR_CODES_AND_MSGS \
    {IVISPECAN_WARN_MEASURE_UNCALIBRATED,  IVISPECAN_WARNMSG_MEASURE_UNCALIBRATED},\
    {IVISPECAN_WARN_OVER_RANGE,            IVISPECAN_WARNMSG_OVER_RANGE},\
    {IVISPECAN_ERROR_MARKER_NOT_ENABLED,   IVISPECAN_ERRMSG_MARKER_NOT_ENABLED},\
    {IVISPECAN_ERROR_NOT_DELTA_MARKER,     IVISPECAN_ERRMSG_NOT_DELTA_MARKER},\
    {IVISPECAN_ERROR_MAX_TIME_EXCEEDED,    IVISPECAN_ERRMSG_MAX_TIME_EXCEEDED},\
    {IVISPECAN_ERROR_TRIGGER_NOT_SOFTWARE, IVISPECAN_ERRMSG_TRIGGER_NOT_SOFTWARE}


/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

#endif /* IVISPECAN_HEADER */
````
