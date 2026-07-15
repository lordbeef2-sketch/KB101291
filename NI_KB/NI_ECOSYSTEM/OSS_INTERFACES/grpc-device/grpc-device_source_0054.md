# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/xnetsocket_converters.h sha256=505786f0760da20c2363031ef251b13f748f6444ebda2d609a7d95c385e7861b bytes=24710 -->
## FILE: source/custom/xnetsocket_converters.h

- repository: `ni/grpc-device`
- source_path: `source/custom/xnetsocket_converters.h`
- sha256: `505786f0760da20c2363031ef251b13f748f6444ebda2d609a7d95c385e7861b`
- bytes: 24710

````c
#ifndef NIDEVICE_GRPC_DEVICE_XNET_SOCKET_CONVERTERS_H
#define NIDEVICE_GRPC_DEVICE_XNET_SOCKET_CONVERTERS_H
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/util/time_util.h>
#include <nixnetsocket.pb.h>
#include <nixnetsocket/nixnetsocket_library_interface.h>
#include <nxsocket.h>
#include <server/converters.h>
#include <server/session_resource_repository.h>

#include <algorithm>
#include <cstring>
#include <memory>

// Helper classes and overrides of standard conversion routines go in nixnetsocket_grpc.
namespace nixnetsocket_grpc {

// Add underscore to usings so they don't conflict with including files in the same namespace.
namespace pb_ = ::google::protobuf;
using ResourceRepositorySharedPtr_ = std::shared_ptr<nidevice_grpc::SessionResourceRepository<nxSOCKET>>;

// This class allows us to have something allocated on the stack that can be used as an
// nxsockaddr* and initialized from a grpc SockAddr using standard codegen and copy convert routines.
struct SockAddrInputConverter {
  SockAddrInputConverter(const SockAddr& input)
  {
    switch (input.addr_case()) {
      case SockAddr::AddrCase::kIpv4:
        addr.ipv4.sin_family = nxAF_INET;
        addr.ipv4.sin_port = input.ipv4().port();
        addr.ipv4.sin_addr.addr = input.ipv4().addr().addr();
        break;
      case SockAddr::AddrCase::kIpv6:
        addr.ipv6.sin6_family = nxAF_INET6;
        addr.ipv6.sin6_port = input.ipv6().port();
        addr.ipv6.sin6_flowinfo = input.ipv6().flowinfo();
        std::memcpy(
            addr.ipv6.sin6_addr.addr,
            input.ipv6().addr().addr().data(),
            std::min(
                sizeof(addr.ipv6.sin6_addr.addr),
                static_cast<size_t>(input.ipv6().addr().addr().size())));
        addr.ipv6.sin6_scope_id = input.ipv6().scope_id();
        break;
      default:
        // pass. Use zero'd out SockAddrInputConverter.
        break;
    }
  }

  // Implicit conversion to nxsockaddr* simplifies codegen because these are passed by pointer to
  // the driver.
  operator nxsockaddr*()
  {
    return &(addr.ip_unknown);
  }

  operator const nxsockaddr*() const
  {
    return &(addr.ip_unknown);
  }

  // size() method is used to simplify codegen calculating the size of the
  // selected addr.
  nxsocklen_t size() const
  {
    switch (addr.ip_unknown.sa_family) {
      case nxAF_INET:
        return sizeof(nxsockaddr_in);
      case nxAF_INET6:
        return sizeof(nxsockaddr_in6);
      default:
        return 0;
    }
  }

  // Represent as a union: can be ipv4 or ipv6.
  union {
    nxsockaddr ip_unknown;
    nxsockaddr_in ipv4;
    nxsockaddr_in6 ipv6;
  } addr{};
};

void copy_ipv6_addr_to_output(const nxin6_addr& ipv6_input, In6Addr* ipv6_output)
{
  // Reinterpret unsigned char to char.
  auto addr_out = reinterpret_cast<const char*>(ipv6_input.addr);
  auto addr_size = sizeof(ipv6_input.addr);
  ipv6_output->set_addr(
      {&addr_out[0],
       &addr_out[addr_size]});
}

void convert_to_grpc(const nxsockaddr_storage* storage_ptr, SockAddr& output)
{
  switch (storage_ptr->ss_family) {
    case nxAF_INET: {
      auto ipv4_input = reinterpret_cast<const nxsockaddr_in*>(storage_ptr);
      auto ipv4_output = output.mutable_ipv4();
      ipv4_output->set_port(ipv4_input->sin_port);
      ipv4_output->mutable_addr()->set_addr(ipv4_input->sin_addr.addr);
    } break;
    case nxAF_INET6: {
      const auto ipv6_input = reinterpret_cast<const nxsockaddr_in6*>(storage_ptr);
      auto ipv6_output = output.mutable_ipv6();
      ipv6_output->set_port(ipv6_input->sin6_port);
      ipv6_output->set_flowinfo(ipv6_input->sin6_flowinfo);
      copy_ipv6_addr_to_output(ipv6_input->sin6_addr, ipv6_output->mutable_addr());
      ipv6_output->set_scope_id(ipv6_input->sin6_scope_id);
    } break;
    default:
      break;
  }
}

// This class allows us to have something allocated on the stack that provides backing
// storage for an nxsockaddr output param and converts it to the SockAddr grpc-type.
struct SockAddrOutputConverter {
  SockAddrOutputConverter()
  {
  }

  template <typename TAddr>
  const TAddr* storage_cast() const
  {
    return reinterpret_cast<const TAddr*>(&storage);
  }

  template <typename TAddr>
  TAddr* storage_cast()
  {
    return reinterpret_cast<TAddr*>(&storage);
  }

  // Overriding the address_of operator is like a implicit conversion for output
  // params. This works with our default output param passing codegen that passes
  // this as nxaccept(sock, &addr, &addrlen);
  nxsockaddr* operator&()
  {
    return storage_cast<nxsockaddr>();
  }

  void to_grpc(SockAddr& output) const
  {
    convert_to_grpc(&storage, output);
  }

  // nxsockaddr_storage is a type specifically designed to be large enough to hold
  // any of the nxsockaddr types.
  nxsockaddr_storage storage{};
};

struct IPv4AddrOutputConverter {
  IPv4AddrOutputConverter()
  {
  }

  nxin_addr* operator&()
  {
    return &addr;
  }

  void to_grpc(InAddr& output) const
  {
    output.set_addr(addr.addr);
  }

  nxin_addr addr{};
};

struct AddrInputConverter {
  AddrInputConverter(const Addr& input)
  {
    switch (input.addr_case()) {
      case Addr::AddrCase::kIpv4:
        addr.ipv4.addr = input.ipv4().addr();
        break;
      case Addr::AddrCase::kIpv6:
        std::memcpy(
            addr.ipv6.addr,
            input.ipv6().addr().data(),
            std::min(
                sizeof(addr.ipv6.addr),
                static_cast<size_t>(input.ipv6().addr().size())));
        break;
      default:
        // pass. Use zero'd out AddrInputConverter.
        break;
    }
  }

  operator void*()
  {
    return &addr;
  }

  operator const void*() const
  {
    return &addr;
  }

  // Represent as a union: can be ipv4 or ipv6.
  union {
    nxin_addr ipv4;
    nxin6_addr ipv6;
  } addr{};
};

struct AddrOutputConverter {
  AddrOutputConverter(int32_t address_family) : family(address_family)
  {
  }

  void* operator&()
  {
    return &addr;
  }

  void to_grpc(Addr& output) const
  {
    switch (family) {
      case nxAF_INET:
        output.mutable_ipv4()->set_addr(addr.ipv4.addr);
        break;
      case nxAF_INET6:
        copy_ipv6_addr_to_output(addr.ipv6, output.mutable_ipv6());
        break;
    }
  }

  union {
    nxin_addr ipv4;
    nxin6_addr ipv6;
  } addr{};
  int32_t family;
};

struct SetInputConverter {
  SetInputConverter(
      const pb_::RepeatedPtrField<nidevice_grpc::Session>& input,
      const ResourceRepositorySharedPtr_& resource_repository)
  {
    nxFD_ZERO(&set);
    for (const auto& session : input) {
      const auto socket = resource_repository->access_session(session.name());
      nxFD_SET(socket, &set);
    }
  }

  operator nxfd_set*()
  {
    return &set;
  }

  operator const nxfd_set*() const
  {
    return &set;
  }

  nxfd_set set;
};

struct TimeValInputConverter {
  TimeValInputConverter(const pb_::Duration& input)
  {
    time_val.tv_sec = input.seconds();
    time_val.tv_usec = input.nanos() / 1000;
  }

  operator nxtimeval*()
  {
    return &time_val;
  }

  operator const nxtimeval*() const
  {
    return &time_val;
  }

  nxtimeval time_val;
};

struct VirtualInterfaceOutputConverter {
  VirtualInterfaceOutputConverter(NiXnetSocketLibraryInterface* library) : virtual_interface_ptr(nullptr), library(library)
  {
  }

  VirtualInterfaceOutputConverter(const std::shared_ptr<NiXnetSocketLibraryInterface>& library) : VirtualInterfaceOutputConverter(library.get())
  {
  }

  nxVirtualInterface_t** operator&()
  {
    return &virtual_interface_ptr;
  }

  void to_grpc(pb_::RepeatedPtrField<VirtualInterface>& output)
  {
    auto curr_vi_ptr = virtual_interface_ptr;
    for (
        auto curr_vi_ptr = virtual_interface_ptr;
        curr_vi_ptr != nullptr;
        curr_vi_ptr = curr_vi_ptr->nextVirtualInterface) {
      auto curr_grpc_vi = output.Add();
      curr_grpc_vi->set_xnet_interface_name(curr_vi_ptr->xnetInterfaceName);
      curr_grpc_vi->set_vlan_name(curr_vi_ptr->vlanName);
      curr_grpc_vi->set_mac_address(curr_vi_ptr->macAddress);
      curr_grpc_vi->set_mac_mtu(curr_vi_ptr->macMTU);
      curr_grpc_vi->set_operational_status(static_cast<OperationalStatus>(curr_vi_ptr->operationalStatus));
      curr_grpc_vi->set_if_index(curr_vi_ptr->ifIndex);
      for (
          auto curr_ip_addr_ptr = curr_vi_ptr->firstIPAddress;
          curr_ip_addr_ptr != nullptr;
          curr_ip_addr_ptr = curr_ip_addr_ptr->nextIPAddress) {
        auto curr_grpc_ip_addr = curr_grpc_vi->add_ip_addresses();
        curr_grpc_ip_addr->set_family(static_cast<AddressFamily>(curr_ip_addr_ptr->family));
        curr_grpc_ip_addr->set_address(curr_ip_addr_ptr->address);
        curr_grpc_ip_addr->set_net_mask(curr_ip_addr_ptr->netmask);
        curr_grpc_ip_addr->set_prefix_length(curr_ip_addr_ptr->prefixLength);
      }
      for (
          auto curr_gateway_addr = curr_vi_ptr->firstGatewayAddress;
          curr_gateway_addr != nullptr;
          curr_gateway_addr = curr_gateway_addr->nextGatewayAddress) {
        auto curr_grpc_gateway_addr = curr_grpc_vi->add_gateway_addresses();
        curr_grpc_gateway_addr->set_family(static_cast<AddressFamily>(curr_gateway_addr->family));
        curr_grpc_gateway_addr->set_address(curr_gateway_addr->address);
      }
    }
    // Free the stack info after we've read it.
    library->IpStackFreeInfo(virtual_interface_ptr);
    virtual_interface_ptr = nullptr;
  }

  nxVirtualInterface_t* virtual_interface_ptr;
  NiXnetSocketLibraryInterface* library;
};

template <typename TSockAddr>
inline SockAddrInputConverter convert_from_grpc(const SockAddr& input)
{
  return SockAddrInputConverter(input);
}

inline void convert_to_grpc(const SockAddrOutputConverter& storage, SockAddr* output)
{
  storage.to_grpc(*output);
}

inline void convert_to_grpc(const IPv4AddrOutputConverter& storage, InAddr* output)
{
  storage.to_grpc(*output);
}

inline void convert_to_grpc(const AddrOutputConverter& storage, Addr* output)
{
  storage.to_grpc(*output);
}

template <typename TAddr>
inline AddrInputConverter convert_from_grpc(const Addr& input)
{
  return AddrInputConverter(input);
}

inline int32_t get_address_family(Addr::AddrCase selected_case)
{
  switch (selected_case) {
    case Addr::AddrCase::kIpv4:
      return nxAF_INET;
    case Addr::AddrCase::kIpv6:
      return nxAF_INET6;
    default:
      return nxAF_UNSPEC;
  }
}

template <typename TTimeVal>
inline SetInputConverter convert_from_grpc(
    const pb_::RepeatedPtrField<nidevice_grpc::Session>& input,
    const ResourceRepositorySharedPtr_& resource_repository)
{
  return SetInputConverter(input, resource_repository);
}

template <typename TTimeVal>
inline TimeValInputConverter convert_from_grpc(const pb_::Duration& input)
{
  return TimeValInputConverter(input);
}

inline void convert_to_grpc(VirtualInterfaceOutputConverter& storage, pb_::RepeatedPtrField<VirtualInterface>* output)
{
  storage.to_grpc(*output);
}

struct SockOptDataInputConverter {
  SockOptDataInputConverter(const SockOptData& input)
  {
    data_case = input.data_case();
    switch (data_case) {
      case SockOptData::DataCase::kDataInt32:
        data_int = input.data_int32();
        break;
      case SockOptData::DataCase::kDataBool:
        data_int = input.data_bool() ? 1 : 0;
        break;
      case SockOptData::DataCase::kDataString:
        data_string = std::string(input.data_string());
        break;
      case SockOptData::DataCase::kDataLinger:
        data_linger.l_linger = input.data_linger().linger();
        data_linger.l_onoff = input.data_linger().onoff();
        break;
      case SockOptData::DataCase::kDataIpMreq:
        data_ipmreq.imr_multiaddr.addr = input.data_ip_mreq().multiaddr().addr();
        data_ipmreq.imr_interface.addr = input.data_ip_mreq().imr_interface().addr();
        break;
      case SockOptData::DataCase::kDataIpv6Mreq:
        std::memcpy(
            data_ipv6mreq.ipv6mr_multiaddr.addr,
            input.data_ipv6_mreq().multiaddr().addr().data(),
            std::min(
                sizeof(data_ipv6mreq.ipv6mr_multiaddr.addr),
                static_cast<size_t>(input.data_ipv6_mreq().multiaddr().addr().size())));
        data_ipv6mreq.ipv6mr_interface = input.data_ipv6_mreq().ipv6mr_interface();
        break;
    }
  }

  void* data()
  {
    switch (data_case) {
      case SockOptData::DataCase::kDataInt32:
      case SockOptData::DataCase::kDataBool:
        return &data_int;
      case SockOptData::DataCase::kDataString:
        return &data_string[0];
      case SockOptData::DataCase::kDataLinger:
        return &data_linger;
        break;
      case SockOptData::DataCase::kDataIpMreq:
        return &data_ipmreq;
        break;
      case SockOptData::DataCase::kDataIpv6Mreq:
        return &data_ipv6mreq;
        break;
      default:
        return nullptr;
    }
  }

  // size() method is used to simplify codegen calculating the size of the
  // populated data.
  nxsocklen_t size() const
  {
    switch (data_case) {
      case SockOptData::DataCase::kDataInt32:
      case SockOptData::DataCase::kDataBool:
        return sizeof(data_int);
      case SockOptData::DataCase::kDataString:
        return static_cast<nxsocklen_t>(data_string.size());
      case SockOptData::DataCase::kDataLinger:
        return sizeof(data_linger);
      case SockOptData::DataCase::kDataIpMreq:
        return sizeof(data_ipmreq);
      case SockOptData::DataCase::kDataIpv6Mreq:
        return sizeof(data_ipv6mreq);
      default:
        return 0;
    }
  }

  SockOptData::DataCase data_case;
  int32_t data_int;
  std::string data_string;
  nxlinger data_linger;
  nxip_mreq data_ipmreq;
  nxipv6_mreq data_ipv6mreq;
};

template <typename TSockOptData>
inline SockOptDataInputConverter convert_from_grpc(const SockOptData& input)
{
  return SockOptDataInputConverter(input);
}

// This class allows us to have something allocated on the stack that provides backing
// storage for a void* opt_val output param and converts it to the SockOptData grpc-type.
struct SockOptDataOutputConverter {
  SockOptDataOutputConverter(NiXnetSocketLibraryInterface* library, int32_t opt_name) : opt_name(opt_name), library(library)
  {
  }

  SockOptDataOutputConverter(const std::shared_ptr<NiXnetSocketLibraryInterface>& library, int32_t opt_name) : SockOptDataOutputConverter(library.get(), opt_name)
  {
  }

  void* data()
  {
    switch (opt_name) {
      case OptName::OPT_NAME_IP_MULTICAST_TTL:
      case OptName::OPT_NAME_IPV6_MULTICAST_HOPS:
      case OptName::OPT_NAME_SO_RXDATA:
      case OptName::OPT_NAME_SO_RCVBUF:
      case OptName::OPT_NAME_SO_SNDBUF:
      case OptName::OPT_NAME_TCP_NODELAY:
      case OptName::OPT_NAME_IP_MULTICAST_IF:
      case OptName::OPT_NAME_IPV6_MULTICAST_IF:
      case OptName::OPT_NAME_SO_ERROR: {
        return &data_int;
      }
      case OptName::OPT_NAME_SO_NONBLOCK:
      case OptName::OPT_NAME_SO_REUSEADDR:
      case OptName::OPT_NAME_IPV6_V6ONLY: {
        return &data_int;
      }
      case OptName::OPT_NAME_SO_BINDTODEVICE: {
        data_string = std::string(string_length, '\0');
        return &data_string[0];
      }
      case OptName::OPT_NAME_SO_LINGER: {
        return &data_linger;
      }
      case OptName::OPT_NAME_IP_ADD_MEMBERSHIP:
      case OptName::OPT_NAME_IP_DROP_MEMBERSHIP: {
        return &data_ipmreq;
      }
      // IPV6 Add and Drop membership also cover Join Group and Leave Group OptName values
      case OptName::OPT_NAME_IPV6_ADD_MEMBERSHIP:
      case OptName::OPT_NAME_IPV6_DROP_MEMBERSHIP: {
        return &data_ipv6mreq;
      }
      default:
        return nullptr;
    }
  }

  void to_grpc(SockOptData& output) const
  {
    switch (opt_name) {
      case OptName::OPT_NAME_IP_MULTICAST_TTL:
      case OptName::OPT_NAME_IPV6_MULTICAST_HOPS:
      case OptName::OPT_NAME_SO_RXDATA:
      case OptName::OPT_NAME_SO_RCVBUF:
      case OptName::OPT_NAME_SO_SNDBUF:
      case OptName::OPT_NAME_TCP_NODELAY:
      case OptName::OPT_NAME_IP_MULTICAST_IF:
      case OptName::OPT_NAME_IPV6_MULTICAST_IF:
      case OptName::OPT_NAME_SO_ERROR: {
        output.set_data_int32(data_int);
        break;
      }
      case OptName::OPT_NAME_SO_NONBLOCK:
      case OptName::OPT_NAME_SO_REUSEADDR:
      case OptName::OPT_NAME_IPV6_V6ONLY: {
        output.set_data_bool(data_int == 0 ? false : true);
        break;
      }
      case OptName::OPT_NAME_SO_BINDTODEVICE: {
        output.set_data_string(data_string);
        nidevice_grpc::converters::trim_trailing_nulls(*(output.mutable_data_string()));
        break;
      }
      case OptName::OPT_NAME_SO_LINGER: {
        output.mutable_data_linger()->set_linger(data_linger.l_linger);
        output.mutable_data_linger()->set_onoff(data_linger.l_onoff);
        break;
      }
      case OptName::OPT_NAME_IP_ADD_MEMBERSHIP:
      case OptName::OPT_NAME_IP_DROP_MEMBERSHIP: {
        output.mutable_data_ip_mreq()->mutable_multiaddr()->set_addr(data_ipmreq.imr_multiaddr.addr);
        output.mutable_data_ip_mreq()->mutable_imr_interface()->set_addr(data_ipmreq.imr_interface.addr);
        break;
      }
      case OptName::OPT_NAME_IPV6_ADD_MEMBERSHIP:
      case OptName::OPT_NAME_IPV6_DROP_MEMBERSHIP: {
        copy_ipv6_addr_to_output(data_ipv6mreq.ipv6mr_multiaddr, output.mutable_data_ipv6_mreq()->mutable_multiaddr());
        output.mutable_data_ipv6_mreq()->set_ipv6mr_interface(data_ipv6mreq.ipv6mr_interface);
        break;
      }
      default:
        break;
    }
  }

  nxsocklen_t size(nxSOCKET& socket, int32_t level)
  {
    if (opt_name == OptName::OPT_NAME_SO_BINDTODEVICE) {
      int status = library->GetSockOpt(socket, level, opt_name, nullptr, &string_length);
      if (status < 0) {
        string_length = 255;
      }
    }
    return string_length;
  }

  int32_t opt_name;
  nxsocklen_t string_length = 255;
  int32_t data_int;
  std::string data_string;
  nxlinger data_linger;
  nxip_mreq data_ipmreq;
  nxipv6_mreq data_ipv6mreq;
  NiXnetSocketLibraryInterface* library;
};

inline void convert_to_grpc(const SockOptDataOutputConverter& storage, SockOptData* output)
{
  storage.to_grpc(*output);
}

struct AddrInfoHintInputConverter {
  AddrInfoHintInputConverter(const AddrInfoHint& input)
  {
    addr_info.ai_flags = nidevice_grpc::converters::convert_bitfield_as_enum_array_input(
        input.flags_array(),
        input.flags_raw());
    addr_info.ai_family = input.family();
    addr_info.ai_socktype = input.sock_type();
    addr_info.ai_protocol = input.protocol();

    // Other addr_info fields for the hint should be left unset (0 initialized).
  }

  operator nxaddrinfo*()
  {
    return &addr_info;
  }

  operator const nxaddrinfo*() const
  {
    return &addr_info;
  }

  nxaddrinfo addr_info{};
};

template <typename TAddrInfoHint>
inline AddrInfoHintInputConverter convert_from_grpc(const AddrInfoHint& input)
{
  return AddrInfoHintInputConverter(input);
}

inline void convert_to_addr_info_flags(int32_t flags, pb_::RepeatedField<int32_t>& get_addr_info_flags)
{
  for (auto flag_to_check = 1; flag_to_check <= GetAddrInfoFlags_MAX; flag_to_check <<= 1) {
    if (flags & flag_to_check) {
      if (GetAddrInfoFlags_IsValid(flag_to_check)) {
        get_addr_info_flags.Add(flag_to_check);
      }
    }
  }
}

struct AddrInfoOutputConverter {
  AddrInfoOutputConverter(NiXnetSocketLibraryInterface* library) : addr_info_ptr(nullptr), library(library)
  {
  }

  AddrInfoOutputConverter(const std::shared_ptr<NiXnetSocketLibraryInterface>& library) : AddrInfoOutputConverter(library.get())
  {
  }

  nxaddrinfo** operator&()
  {
    return &addr_info_ptr;
  }

  void to_grpc(pb_::RepeatedPtrField<AddrInfo>& output)
  {
    for (
        auto curr_addr_info_ptr = addr_info_ptr;
        curr_addr_info_ptr != nullptr;
        curr_addr_info_ptr = curr_addr_info_ptr->ai_next) {
      auto curr_grpc_addr_info = output.Add();
      curr_grpc_addr_info->set_flags_raw(curr_addr_info_ptr->ai_flags);
      convert_to_addr_info_flags(curr_addr_info_ptr->ai_flags, *(curr_grpc_addr_info->mutable_flags_array()));
      curr_grpc_addr_info->set_family((AddressFamily)curr_addr_info_ptr->ai_family);
      curr_grpc_addr_info->set_sock_type((SocketProtocolType)curr_addr_info_ptr->ai_socktype);
      curr_grpc_addr_info->set_protocol((IPProtocol)curr_addr_info_ptr->ai_protocol);
      curr_grpc_addr_info->set_canon_name(curr_addr_info_ptr->ai_canonname);

      convert_to_grpc(reinterpret_cast<const nxsockaddr_storage*>(curr_addr_info_ptr->ai_addr), *(curr_grpc_addr_info->mutable_addr()));
    }
    // Free the address info after we've read it.
    library->FreeAddrInfo(addr_info_ptr);
    addr_info_ptr = nullptr;
  }

  nxaddrinfo* addr_info_ptr;
  NiXnetSocketLibraryInterface* library;
};

inline void convert_to_grpc(AddrInfoOutputConverter& storage, pb_::RepeatedPtrField<AddrInfo>* output)
{
  storage.to_grpc(*output);
}

// Trivial converter implementation for strings that calls IpStackFreeAllStacksInfoStr after to_grpc.
struct IpStackInfoStringOutputConverter {
  IpStackInfoStringOutputConverter(NiXnetSocketLibraryInterface* library) : library(library)
  {
  }

  IpStackInfoStringOutputConverter(const std::shared_ptr<NiXnetSocketLibraryInterface>& library) : IpStackInfoStringOutputConverter(library.get())
  {
  }

  IpStackInfoString* operator&()
  {
    return &stack_info_string;
  }

  // Implementing data() allows this converter to work with standard codegen for strings
  // that assume that they have a data() member that can be passed to the driver.
  // This is required because the grpc_type is string.
  IpStackInfoString* data()
  {
    return &stack_info_string;
  }

  void to_grpc(std::string& output) const
  {
    output.assign(stack_info_string);
    library->IpStackFreeAllStacksInfoStr(stack_info_string);
  }

  IpStackInfoString stack_info_string{};
  NiXnetSocketLibraryInterface* library;
};

inline void convert_to_grpc(const IpStackInfoStringOutputConverter& storage, std::string* output)
{
  storage.to_grpc(*output);
}

}  // namespace nixnetsocket_grpc

// Template specializations go in nidevice_grpc::converters.
namespace nidevice_grpc {
namespace converters {

template <>
inline nxin_addr convert_from_grpc(const nixnetsocket_grpc::InAddr& input)
{
  return {input.addr()};
}

// Specialization of TypeToStorageType so that allocate_storage_type will
// allocate SockAddrOutputConverters for nxsockaddr output params.
template <>
struct TypeToStorageType<nxsockaddr, nixnetsocket_grpc::SockAddr> {
  using StorageType = nixnetsocket_grpc::SockAddrOutputConverter;
};

template <>
struct TypeToStorageType<nxVirtualInterface_t, google::protobuf::RepeatedPtrField<nixnetsocket_grpc::VirtualInterface>> {
  using StorageType = nixnetsocket_grpc::VirtualInterfaceOutputConverter;
};
// Specialization of TypeToStorageType so that allocate_storage_type will
// allocate SockOptDataOutputConverters for void* output params.
template <>
struct TypeToStorageType<void*, nixnetsocket_grpc::SockOptData> {
  using StorageType = nixnetsocket_grpc::SockOptDataOutputConverter;
};

template <>
struct TypeToStorageType<nxaddrinfo, google::protobuf::RepeatedPtrField<nixnetsocket_grpc::AddrInfo>> {
  using StorageType = nixnetsocket_grpc::AddrInfoOutputConverter;
};

template <>
struct TypeToStorageType<nxin_addr, nixnetsocket_grpc::InAddr> {
  using StorageType = nixnetsocket_grpc::IPv4AddrOutputConverter;
};

template <>
struct TypeToStorageType<void, nixnetsocket_grpc::Addr> {
  using StorageType = nixnetsocket_grpc::AddrOutputConverter;
};

template <>
struct TypeToStorageType<nixnetsocket_grpc::IpStackInfoString, std::string> {
  using StorageType = nixnetsocket_grpc::IpStackInfoStringOutputConverter;
};
}  // namespace converters
}  // namespace nidevice_grpc

#endif /* NIDEVICE_GRPC_DEVICE_XNET_SOCKET_CONVERTERS_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/xnetsocket_errors.h sha256=c3ad4cf63b72b436b02d6d2e132c8e1d98a22ee0cb3dc7ccbc8fbf83686e9753 bytes=807 -->
## FILE: source/custom/xnetsocket_errors.h

- repository: `ni/grpc-device`
- source_path: `source/custom/xnetsocket_errors.h`
- sha256: `c3ad4cf63b72b436b02d6d2e132c8e1d98a22ee0cb3dc7ccbc8fbf83686e9753`
- bytes: 807

````c
#ifndef NIDEVICE_GRPC_DEVICE_XNET_SOCKET_ERRORS_H
#define NIDEVICE_GRPC_DEVICE_XNET_SOCKET_ERRORS_H

#include <nixnetsocket.pb.h>
#include <nixnetsocket/nixnetsocket_library_interface.h>
#include <nxsocket.h>
#include <server/converters.h>

#include <algorithm>
#include <cstring>

namespace nixnetsocket_grpc {
constexpr auto ERROR_BUFFER_SIZE = 4096;
std::string get_last_error_message(NiXnetSocketLibraryInterface* library)
{
  auto buffer = std::vector<char>(ERROR_BUFFER_SIZE);
  library->GetLastErrorStr(buffer.data(), ERROR_BUFFER_SIZE);
  return std::string(buffer.data());
}

int32_t get_last_error_num(NiXnetSocketLibraryInterface* library)
{
  return library->GetLastErrorNum();
}
}  // namespace nixnetsocket_grpc
#endif /* NIDEVICE_GRPC_DEVICE_XNET_SOCKET_ERRORS_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/xnetsocket_winsock2_compatibility.h sha256=8c6472f6fa27e7f62605e0e61d558b531f4698c1bd513535991624d41d9ea80b bytes=757 -->
## FILE: source/custom/xnetsocket_winsock2_compatibility.h

- repository: `ni/grpc-device`
- source_path: `source/custom/xnetsocket_winsock2_compatibility.h`
- sha256: `8c6472f6fa27e7f62605e0e61d558b531f4698c1bd513535991624d41d9ea80b`
- bytes: 757

````c
#ifndef NIDEVICE_GRPC_DEVICE_XNET_SOCKET_WINSOCK2_COMPATIBILITY_H
#define NIDEVICE_GRPC_DEVICE_XNET_SOCKET_WINSOCK2_COMPATIBILITY_H

// Unfortunately XNET's Socket API conflicts with defines in the winsock2 API.
// We must undefine these to prevent winsock2 from replacing them.
#if defined(_WIN32) || defined(_WIN64)
// Ensure the problematic header is included before we undef.
#include <WS2tcpip.h>

// Undef problematic defines.
#ifdef FreeAddrInfo
#undef FreeAddrInfo
#endif
#ifdef GetAddrInfo
#undef GetAddrInfo
#endif
#ifdef GetNameInfo
#undef GetNameInfo
#endif
#ifdef InetNToP
#undef InetNToP
#endif
#ifdef InetPToN
#undef InetPToN
#endif

#endif

#endif /* NIDEVICE_GRPC_DEVICE_XNET_SOCKET_WINSOCK2_COMPATIBILITY_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/protobuf/session_utilities.proto sha256=25aece7f55cf995c7eb1f1b6bcc7f4feb72853d570ee5332a6bedeb57cb46577 bytes=2721 -->
## FILE: source/protobuf/session_utilities.proto

- repository: `ni/grpc-device`
- source_path: `source/protobuf/session_utilities.proto`
- sha256: `25aece7f55cf995c7eb1f1b6bcc7f4feb72853d570ee5332a6bedeb57cb46577`
- bytes: 2721

````protobuf
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.device";
option java_outer_classname = "NiDevice";
option csharp_namespace = "NationalInstruments.Grpc.Device";

package nidevice_grpc;

service SessionUtilities {
  // Provides a list of devices or chassis connected to server under localhost
  rpc EnumerateDevices(EnumerateDevicesRequest)
      returns (EnumerateDevicesResponse);

  // Provides a list of NI software installed on server under localhost
  rpc EnumerateInstalledSoftware(EnumerateInstalledSoftwareRequest)
      returns (EnumerateInstalledSoftwareResponse);

  // Reserve a set of client defined resources for exclusive use
  rpc Reserve(ReserveRequest) returns (ReserveResponse);

  // Determines if a set of client defined resources is currently reserved by a
  // specific client
  rpc IsReservedByClient(IsReservedByClientRequest)
      returns (IsReservedByClientResponse);

  // Unreserves a previously reserved resource
  rpc Unreserve(UnreserveRequest) returns (UnreserveResponse);

  // Resets the server to a default state with no open sessions
  rpc ResetServer(ResetServerRequest) returns (ResetServerResponse);
}

message DeviceProperties {
  string name = 1;
  string model = 2;
  string vendor = 3;
  string serial_number = 4;
  uint32 product_id = 5;
}

message EnumerateDevicesRequest {}

message EnumerateDevicesResponse {
  repeated DeviceProperties devices = 1;
}

message SoftwareProperties {
  string package_id = 1;
  string package_version = 2;
  string product_name = 3;
}

message EnumerateInstalledSoftwareRequest {
  bool include_hidden_packages = 1;
}

message EnumerateInstalledSoftwareResponse {
  repeated SoftwareProperties software = 1;
}

message ReserveRequest {
  // client defined string representing a set of reservable resources
  string reservation_id = 1;
  // client defined identifier for a specific client
  string client_id = 2;
}

message ReserveResponse {
  bool is_reserved = 1;
}

message IsReservedByClientRequest {
  // client defined string representing a set of reservable resources
  string reservation_id = 1;
  // client defined identifier for a specific client
  string client_id = 2;
}

message IsReservedByClientResponse {
  bool is_reserved = 1;
}

message UnreserveRequest {
  // client defined string representing a set of reservable resources
  string reservation_id = 1;
  // client defined identifier for a specific client
  string client_id = 2;
}

message UnreserveResponse {
  bool is_unreserved = 1;
}

message ResetServerRequest {}

message ResetServerResponse {
  bool is_server_reset = 1;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/protobuf_restricted/calibrationoperations_restricted.proto sha256=0b5aa7635d09c8934e5ebe4f28a280fee946527343fe06c2ec5efc500fcd50bd bytes=1194 -->
## FILE: source/protobuf_restricted/calibrationoperations_restricted.proto

- repository: `ni/grpc-device`
- source_path: `source/protobuf_restricted/calibrationoperations_restricted.proto`
- sha256: `0b5aa7635d09c8934e5ebe4f28a280fee946527343fe06c2ec5efc500fcd50bd`
- bytes: 1194

````protobuf
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.devicerestricted";
option java_outer_classname = "NiDeviceRestricted";
option csharp_namespace = "NationalInstruments.Grpc.DeviceRestricted";

package nidevice_restricted_grpc;

import "deviceid_restricted.proto";
import "google/protobuf/timestamp.proto";

service CalibrationOperationsRestricted {
  rpc GetCalibrationInformation(GetCalibrationInformationRequest) returns (GetCalibrationInformationResponse);
}

message GetCalibrationInformationRequest {
  DeviceId device_id = 1;
}

message GetCalibrationInformationResponse {
  optional bool supports_internal_calibration = 1;
  optional uint32 number_of_internal_calibration_details = 2;
  repeated string internal_calibration_names = 3;
  repeated double internal_calibration_last_temperatures = 4;
  repeated google.protobuf.Timestamp internal_calibration_last_times = 5;
  optional bool supports_external_calibration = 6;
  optional double external_calibration_last_temperature = 7;
  google.protobuf.Timestamp external_calibration_last_time = 8;
  google.protobuf.Timestamp recommended_next_calibration_time = 9;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/protobuf_restricted/debugsessionproperties_restricted.proto sha256=3858bc72f3e0cc9fad4f27835537b51705b0f2c118bee9df082aa74225a0adab bytes=1700 -->
## FILE: source/protobuf_restricted/debugsessionproperties_restricted.proto

- repository: `ni/grpc-device`
- source_path: `source/protobuf_restricted/debugsessionproperties_restricted.proto`
- sha256: `3858bc72f3e0cc9fad4f27835537b51705b0f2c118bee9df082aa74225a0adab`
- bytes: 1700

````protobuf
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.devicerestricted";
option java_outer_classname = "NiDeviceRestricted";
option csharp_namespace = "NationalInstruments.Grpc.DeviceRestricted";

package nidevice_restricted_grpc;

import "deviceid_restricted.proto";

service DebugSessionPropertiesRestricted {
  rpc IsDebugSessionEnabled(IsDebugSessionEnabledRequest) returns (IsDebugSessionEnabledResponse);
  rpc IsDebugSessionServerOutOfProcess(IsDebugSessionServerOutOfProcessRequest) returns (IsDebugSessionServerOutOfProcessResponse);
  rpc IsDebugSessionSupported(IsDebugSessionSupportedRequest) returns (IsDebugSessionSupportedResponse);
  rpc SetDebugSessionEnabled(SetDebugSessionEnabledRequest) returns (SetDebugSessionEnabledResponse);
  rpc SetDebugSessionServerOutOfProcess(SetDebugSessionServerOutOfProcessRequest) returns (SetDebugSessionServerOutOfProcessResponse);
}

message IsDebugSessionEnabledRequest {
  DeviceId device_id = 1;
}

message IsDebugSessionEnabledResponse {
  bool enabled = 1;
}

message IsDebugSessionServerOutOfProcessRequest {
  DeviceId device_id = 1;
}

message IsDebugSessionServerOutOfProcessResponse {
  bool out_of_process = 1;
}

message IsDebugSessionSupportedRequest {
  DeviceId device_id = 1;
}

message IsDebugSessionSupportedResponse {
  bool supported = 1;
}

message SetDebugSessionEnabledRequest {
  DeviceId device_id = 1;
  bool enabled = 2;
}

message SetDebugSessionEnabledResponse {}

message SetDebugSessionServerOutOfProcessRequest {
  DeviceId device_id = 1;
  bool out_of_process = 2;
}

message SetDebugSessionServerOutOfProcessResponse {}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/protobuf_restricted/deviceid_restricted.proto sha256=81746b5953914f3257cbdbaceb039f4552c024a31836aa2af04780500326202c bytes=375 -->
## FILE: source/protobuf_restricted/deviceid_restricted.proto

- repository: `ni/grpc-device`
- source_path: `source/protobuf_restricted/deviceid_restricted.proto`
- sha256: `81746b5953914f3257cbdbaceb039f4552c024a31836aa2af04780500326202c`
- bytes: 375

````protobuf
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.devicerestricted";
option java_outer_classname = "NiDeviceRestricted";
option csharp_namespace = "NationalInstruments.Grpc.DeviceRestricted";

package nidevice_restricted_grpc;

message DeviceId {
  string name = 1;
  string serial_number = 2;
  uint32 product_id = 3;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/calibration_operations_restricted_service.cpp sha256=440ae528afefdc9cd551b22d2838307566b637bae4211e75272b89eb7a58e683 bytes=10859 -->
## FILE: source/server/calibration_operations_restricted_service.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/calibration_operations_restricted_service.cpp`
- sha256: `440ae528afefdc9cd551b22d2838307566b637bae4211e75272b89eb7a58e683`
- bytes: 10859

````cpp
#include "calibration_operations_restricted_service.h"

#include "converters.h"
#include "nisyscfg.h"

namespace nidevice_restricted_grpc {

CalibrationOperationsRestrictedFeatureToggles::CalibrationOperationsRestrictedFeatureToggles(
  const nidevice_grpc::FeatureToggles& feature_toggles)
  : is_enabled(
      feature_toggles.is_feature_enabled("calibrationoperations_restricted", CodeReadiness::kRelease))
{
}

CalibrationOperationsRestrictedService::CalibrationOperationsRestrictedService(::nidevice_grpc::SysCfgLibraryInterface* library)
    : SysCfgResourceAccessor(library) {}

::grpc::Status CalibrationOperationsRestrictedService::GetCalibrationInformation(
  ::grpc::ServerContext* context,
  const GetCalibrationInformationRequest* request,
  GetCalibrationInformationResponse* response)
{
  bool supports_internal_calibration_available = false;
  bool supports_internal_calibration = false;
  bool number_of_internal_calibration_details_available = false;
  uint32_t number_of_internal_calibration_details = 0;
  bool supports_external_calibration_available = false;
  bool supports_external_calibration = false;
  bool external_calibration_last_temperature_available = false;
  double external_calibration_last_temperature = 0.0;
  bool external_calibration_last_time_available = false;
  google::protobuf::Timestamp external_calibration_last_time;
  bool recommended_next_calibration_time_available = false;
  google::protobuf::Timestamp recommended_next_calibration_time;

  auto status = get_calibration_info(
    context,
    request->device_id(),
    &supports_internal_calibration_available,
    &supports_internal_calibration,
    &number_of_internal_calibration_details_available,
    &number_of_internal_calibration_details,
    response->mutable_internal_calibration_names(),
    response->mutable_internal_calibration_last_temperatures(),
    response->mutable_internal_calibration_last_times(),
    &supports_external_calibration_available,
    &supports_external_calibration,
    &external_calibration_last_temperature_available,
    &external_calibration_last_temperature,
    &external_calibration_last_time_available,
    &external_calibration_last_time,
    &recommended_next_calibration_time_available,
    &recommended_next_calibration_time);

  if (supports_internal_calibration_available) {
    response->set_supports_internal_calibration(supports_internal_calibration);
  }
  if (number_of_internal_calibration_details_available) {
    response->set_number_of_internal_calibration_details(number_of_internal_calibration_details);
  }
  if (supports_external_calibration_available) {
    response->set_supports_external_calibration(supports_external_calibration);
  }
  if (external_calibration_last_temperature_available) {
    response->set_external_calibration_last_temperature(external_calibration_last_temperature);
  }
  if (external_calibration_last_time_available) {
    *response->mutable_external_calibration_last_time() = external_calibration_last_time;
  }
  if (recommended_next_calibration_time_available) {
    *response->mutable_recommended_next_calibration_time() = recommended_next_calibration_time;
  }

  return status;
}

static void AssignIfAvailable(bool* available, std::function<void()> set_value_func, NISysCfgStatus& status)
{
  if (NISysCfg_Failed(status)) {
    *available = false;
    if (status == NISysCfg_PropDoesNotExist) {
      status = NISysCfg_OK;
    }
  }
  else {
    *available = true;
    set_value_func();
  }
}

::grpc::Status CalibrationOperationsRestrictedService::get_calibration_info(
  ::grpc::ServerContext* context,
  const DeviceId& device_id,
  bool* supports_internal_calibration_available,
  bool* supports_internal_calibration,
  bool* number_of_internal_calibration_details_available,
  uint32_t* number_of_internal_calibration_details,
  google::protobuf::RepeatedPtrField<std::string>* internal_calibration_names,
  google::protobuf::RepeatedField<double>* internal_calibration_last_temperatures,
  google::protobuf::RepeatedPtrField<google::protobuf::Timestamp>* internal_calibration_last_times,
  bool* supports_external_calibration_available,
  bool* supports_external_calibration,
  bool* external_calibration_last_temperature_available,
  double* external_calibration_last_temperature,
  bool* external_calibration_last_time_available,
  google::protobuf::Timestamp* external_calibration_last_time,
  bool* recommended_next_calibration_time_available,
  google::protobuf::Timestamp* recommended_next_calibration_time)
{
  auto get_calibration_data = [&](nidevice_grpc::SysCfgLibraryInterface* library, NISysCfgResourceHandle resource, bool* save_changes) {
    NISysCfgBool syscfg_bool = NISysCfgBoolFalse;
    NISysCfgTimestampUTC syscfg_time = {{0}};
    char syscfg_string[NISYSCFG_SIMPLE_STRING_LENGTH] = {0};
    double syscfg_double = 0.0;
    int syscfg_int = 0;
    int local_number_of_internal_calibration_details = 0;

    // Supports Internal Calibration
    auto status = library->GetResourceProperty(resource, NISysCfgResourcePropertySupportsInternalCalibration, &syscfg_bool);
    auto set_supports_internal_calibration_func = [&] () {
      *supports_internal_calibration = syscfg_bool != NISysCfgBoolFalse;
    };
    AssignIfAvailable(supports_internal_calibration_available, set_supports_internal_calibration_func, status);
    if (NISysCfg_Failed(status)) {
      return status;
    }

    // Number of Internal Calibration Details
    status = library->GetResourceProperty(resource, NISysCfgResourcePropertyNumberOfInternalCalibrationDetails, &syscfg_int);
    auto set_number_of_internal_calibration_details_func = [&] () {
      local_number_of_internal_calibration_details = syscfg_int;
      *number_of_internal_calibration_details = static_cast<uint32_t>(syscfg_int);
    };
    AssignIfAvailable(number_of_internal_calibration_details_available, set_number_of_internal_calibration_details_func, status);
    if (NISysCfg_Failed(status)) {
      return status;
    }

    // Internal Calibration Names
    for (int i = 0; i < local_number_of_internal_calibration_details; ++i) {
      status = library->GetResourceIndexedProperty(resource, NISysCfgIndexedPropertyInternalCalibrationName, i, syscfg_string);
      auto set_internal_calibration_names_func = [&] () {
        internal_calibration_names->Add(syscfg_string);
      };
      bool internal_calibration_names_available = false;
      AssignIfAvailable(&internal_calibration_names_available, set_internal_calibration_names_func, status);
      if (NISysCfg_Failed(status)) {
        return status;
      }
      if (!internal_calibration_names_available) {
        break;
      }
    }

    // Internal Calibration Last Temperatures
    for (int i = 0; i < local_number_of_internal_calibration_details; ++i) {
      status = library->GetResourceIndexedProperty(resource, NISysCfgIndexedPropertyInternalCalibrationLastTemp, i, &syscfg_double);
      auto set_internal_calibration_last_temperatures_func = [&] () {
        internal_calibration_last_temperatures->Add(syscfg_double);
      };
      bool internal_calibration_last_temperatures_available = false;
      AssignIfAvailable(&internal_calibration_last_temperatures_available, set_internal_calibration_last_temperatures_func, status);
      if (NISysCfg_Failed(status)) {
        return status;
      }
      if (!internal_calibration_last_temperatures_available) {
        break;
      }
    }

    // Internal Calibration Last Times
    for (int i = 0; i < local_number_of_internal_calibration_details; ++i) {
      status = library->GetResourceIndexedProperty(resource, NISysCfgIndexedPropertyInternalCalibrationLastTime, i, &syscfg_time);
      auto set_internal_calibration_last_times_func = [&] () {
        CVIAbsoluteTime syscfg_time_convert = *reinterpret_cast<CVIAbsoluteTime*>(&syscfg_time);
        nidevice_grpc::converters::convert_to_grpc(syscfg_time_convert, internal_calibration_last_times->Add());
      };
      bool internal_calibration_last_times_available = false;
      AssignIfAvailable(&internal_calibration_last_times_available, set_internal_calibration_last_times_func, status);
      if (NISysCfg_Failed(status)) {
        return status;
      }
      if (!internal_calibration_last_times_available) {
        break;
      }
    }

    // Supports External Calibration
    status = library->GetResourceProperty(resource, NISysCfgResourcePropertySupportsExternalCalibration, &syscfg_bool);
    auto set_supports_external_calibration_func = [&] () {
      *supports_external_calibration = syscfg_bool != NISysCfgBoolFalse;
    };
    AssignIfAvailable(supports_external_calibration_available, set_supports_external_calibration_func, status);
    if (NISysCfg_Failed(status)) {
      return status;
    }

    // External Calibration Last Temperature
    status = library->GetResourceProperty(resource, NISysCfgResourcePropertyExternalCalibrationLastTemp, &syscfg_double);
    auto set_external_calibration_last_temperature_func = [&] () {
      *external_calibration_last_temperature = syscfg_double;
    };
    AssignIfAvailable(external_calibration_last_temperature_available, set_external_calibration_last_temperature_func, status);
    if (NISysCfg_Failed(status)) {
      return status;
    }

    // External Calibration Last Time
    status = library->GetResourceProperty(resource, NISysCfgResourcePropertyExternalCalibrationLastTime, &syscfg_time);
    auto set_external_calibration_last_time_func = [&] () {
      CVIAbsoluteTime syscfg_time_convert = *reinterpret_cast<CVIAbsoluteTime*>(&syscfg_time);
      nidevice_grpc::converters::convert_to_grpc(syscfg_time_convert, external_calibration_last_time);
    };
    AssignIfAvailable(external_calibration_last_time_available, set_external_calibration_last_time_func, status);
    if (NISysCfg_Failed(status)) {
      return status;
    }

    // Recommended Next Calibration Time
    status = library->GetResourceProperty(resource, NISysCfgResourcePropertyRecommendedNextCalibrationTime, &syscfg_time);
    auto set_recommended_next_calibration_time_func = [&] () {
      CVIAbsoluteTime syscfg_time_convert = *reinterpret_cast<CVIAbsoluteTime*>(&syscfg_time);
      nidevice_grpc::converters::convert_to_grpc(syscfg_time_convert, recommended_next_calibration_time);
    };
    AssignIfAvailable(recommended_next_calibration_time_available, set_recommended_next_calibration_time_func, status);

    return status;
  };

  return access_syscfg_resource_by_device_id_filter(context, device_id, kCalibrationPropertyAccessFailedMessage, get_calibration_data);
}

}  // namespace nidevice_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/calibration_operations_restricted_service.h sha256=9202b58a635b90e2adbdaf33b8a7feb4ebf2b65c34432abf7e3a749bec2d6219 bytes=2608 -->
## FILE: source/server/calibration_operations_restricted_service.h

- repository: `ni/grpc-device`
- source_path: `source/server/calibration_operations_restricted_service.h`
- sha256: `9202b58a635b90e2adbdaf33b8a7feb4ebf2b65c34432abf7e3a749bec2d6219`
- bytes: 2608

````c
#ifndef NIDEVICE_RESTRICTED_GRPC_CALIBRATION_OPERATIONS_RESTRICTED_SERVICE
#define NIDEVICE_RESTRICTED_GRPC_CALIBRATION_OPERATIONS_RESTRICTED_SERVICE

#include <calibrationoperations_restricted.grpc.pb.h>
#include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>

#include <string>

#include "feature_toggles.h"
#include "shared_library.h"
#include "syscfg_library_interface.h"
#include "syscfg_resource_accessor.h"

namespace nidevice_restricted_grpc {

static const char* kCalibrationPropertyAccessFailedMessage = "The NI System Configuration API was unable to access the calibration property.";

struct CalibrationOperationsRestrictedFeatureToggles {
  using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;
  CalibrationOperationsRestrictedFeatureToggles(const nidevice_grpc::FeatureToggles& feature_toggles = {});
  bool is_enabled;
};

class CalibrationOperationsRestrictedService final :
  public CalibrationOperationsRestricted::Service,
  public ::nidevice_restricted_grpc::SysCfgResourceAccessor {
 public:
  CalibrationOperationsRestrictedService(::nidevice_grpc::SysCfgLibraryInterface* library);

  ::grpc::Status GetCalibrationInformation(
    ::grpc::ServerContext* context,
    const GetCalibrationInformationRequest* request,
    GetCalibrationInformationResponse* response) override;

 private:
  ::grpc::Status get_calibration_info(
    ::grpc::ServerContext* context,
    const DeviceId& device_id,
    bool* supports_internal_calibration_available,
    bool* supports_internal_calibration,
    bool* number_of_internal_calibration_details_available,
    uint32_t* number_of_internal_calibration_details,
    google::protobuf::RepeatedPtrField<std::string>* internal_calibration_names,
    google::protobuf::RepeatedField<double>* internal_calibration_last_temperatures,
    google::protobuf::RepeatedPtrField<google::protobuf::Timestamp>* internal_calibration_last_times,
    bool* supports_external_calibration_available,
    bool* supports_external_calibration,
    bool* external_calibration_last_temperature_available,
    double* external_calibration_last_temperature,
    bool* external_calibration_last_time_available,
    google::protobuf::Timestamp* external_calibration_last_time,
    bool* recommended_next_calibration_time_available,
    google::protobuf::Timestamp* recommended_next_calibration_time);
};

}  // namespace nidevice_restricted_grpc

#endif  // NIDEVICE_RESTRICTED_GRPC_CALIBRATION_OPERATIONS_RESTRICTED_SERVICE
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/calibration_operations_restricted_service_registrar.cpp sha256=71933e1fae1cab3835cb01a9e6a6791304856a41a753451cc0bfa7b681d4a165 bytes=1760 -->
## FILE: source/server/calibration_operations_restricted_service_registrar.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/calibration_operations_restricted_service_registrar.cpp`
- sha256: `71933e1fae1cab3835cb01a9e6a6791304856a41a753451cc0bfa7b681d4a165`
- bytes: 1760

````cpp
#include "calibration_operations_restricted_service_registrar.h"

#include "calibration_operations_restricted_service.h"
#include "syscfg_library.h"

namespace nidevice_restricted_grpc {
namespace {
struct CalibrationOperationsRestrictedLibraryAndService {
  CalibrationOperationsRestrictedLibraryAndService(
    nidevice_grpc::ServerResetObserverRegistrarInterface& serverResetObserverRegistrar)
      : library(),
        service(&library),
        observerRegistrar(&serverResetObserverRegistrar)
  {
    observerRegistrar->register_observer(&service);
  }

  ~CalibrationOperationsRestrictedLibraryAndService()
  {
    // This code is currently unreachable, but if the call to wait exits, we need to clean up the service here.
    observerRegistrar->unregister_observer(&service);
    service.clear_syscfg_session();
  }

  ::nidevice_grpc::SysCfgLibrary library;
  CalibrationOperationsRestrictedService service;
  nidevice_grpc::ServerResetObserverRegistrarInterface* observerRegistrar;
};
}  // namespace

std::shared_ptr<void> register_calibration_operations_restricted_service(
  grpc::ServerBuilder& server_builder,
  const nidevice_grpc::FeatureToggles& feature_toggles,
  nidevice_grpc::ServerResetObserverRegistrarInterface& serverResetObserverRegistrar)
{
  auto toggles = CalibrationOperationsRestrictedFeatureToggles(feature_toggles);

  if (toggles.is_enabled)
  {
    auto library_and_service_ptr = std::make_shared<CalibrationOperationsRestrictedLibraryAndService>(serverResetObserverRegistrar);
    auto& service = library_and_service_ptr->service;
    server_builder.RegisterService(&service);
    return library_and_service_ptr;
  }

  return {};
}
}  // namespace nidevice_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/calibration_operations_restricted_service_registrar.h sha256=b054e1e52fbf261fea32b8f08abae29f31c1af5a53bc36b7ffcf93583f882c98 bytes=826 -->
## FILE: source/server/calibration_operations_restricted_service_registrar.h

- repository: `ni/grpc-device`
- source_path: `source/server/calibration_operations_restricted_service_registrar.h`
- sha256: `b054e1e52fbf261fea32b8f08abae29f31c1af5a53bc36b7ffcf93583f882c98`
- bytes: 826

````c
#ifndef NIDEVICE_GRPC_DEVICE_RESTRICTED_CALIBRATION_OPERATIONS_SERVICE_REGISTRAR_H
#define NIDEVICE_GRPC_DEVICE_RESTRICTED_CALIBRATION_OPERATIONS_SERVICE_REGISTRAR_H

#include <memory>

#include "feature_toggles.h"
#include "server_reset_observer_registrar_interface.h"

namespace grpc {
class ServerBuilder;
}

namespace nidevice_restricted_grpc {
using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;

std::shared_ptr<void> register_calibration_operations_restricted_service(
  grpc::ServerBuilder& server_builder,
  const nidevice_grpc::FeatureToggles& feature_toggles,
  nidevice_grpc::ServerResetObserverRegistrarInterface& serverResetObserverRegistrar);

}  // namespace nidevice_restricted_grpc

#endif  // NIDEVICE_GRPC_DEVICE_RESTRICTED_CALIBRATION_OPERATIONS_SERVICE_REGISTRAR_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/callback_router.h sha256=9989c8814ee7b0bd6ba28f0af27d837d344015ace4dd0882a9e8f3871d45fda7 bytes=3282 -->
## FILE: source/server/callback_router.h

- repository: `ni/grpc-device`
- source_path: `source/server/callback_router.h`
- sha256: `9989c8814ee7b0bd6ba28f0af27d837d344015ace4dd0882a9e8f3871d45fda7`
- bytes: 3282

````c
#ifndef NIDEVICE_GRPC_DEVICE_CALLBACK_ROUTER_H
#define NIDEVICE_GRPC_DEVICE_CALLBACK_ROUTER_H

#include <atomic>
#include <functional>
#include <mutex>
#include <unordered_map>

namespace nidevice_grpc {

struct CallbackRegistration {
  using Token = void*;

  virtual ~CallbackRegistration() {}
  virtual Token token() { return {}; }
};

// Allows registering Handlers taking TArgs... and exposes a static handle_callback
// method that can be passed as a function pointer to C APIs.
// This allows Handlers to be implemented with stateful lambdas, which are not convertible
// to function pointers.
template <typename TReturn, typename... TArgs>
class CallbackRouter {
 public:
  using Handler = std::function<TReturn(TArgs...)>;
  using Token = CallbackRegistration::Token;

  class CallbackRegistrationImpl : public CallbackRegistration {
    using LockGuard = std::lock_guard<std::mutex>;

   public:
    CallbackRegistrationImpl(Token token) : token_(token) {}
    CallbackRegistrationImpl(const CallbackRegistrationImpl&) = delete;
    CallbackRegistrationImpl& operator=(const CallbackRegistrationImpl&) = delete;
    CallbackRegistrationImpl(CallbackRegistrationImpl&& rhs) = delete;
    CallbackRegistrationImpl& operator=(CallbackRegistrationImpl&& rhs) = delete;
    ~CallbackRegistrationImpl()
    {
      instance().unregister_handler(token_);
    }

    Token token()
    {
      return token_;
    }

   private:
    Token token_;
  };

  static std::unique_ptr<CallbackRegistration> register_handler(const Handler& handler)
  {
    auto token = instance().allocate_token_for_handler(handler);
    return std::make_unique<CallbackRegistrationImpl>(token);
  }

  static TReturn handle_callback(TArgs... args, Token token)
  {
    return instance().route_callback_to_handler(args..., token);
  }

 private:
  CallbackRouter() {}
  CallbackRouter(const CallbackRouter&) = delete;
  CallbackRouter& operator=(const CallbackRouter&) = delete;
  CallbackRouter(CallbackRouter&&) = delete;
  CallbackRouter& operator=(CallbackRouter&&) = delete;

  static CallbackRouter& instance()
  {
    static CallbackRouter instance;
    return instance;
  }

  Token allocate_token_for_handler(const Handler& handler)
  {
    LockGuard guard(mutex_);
    auto token = reinterpret_cast<Token>(++callback_id_);
    handlers_[token] = handler;
    return token;
  }

  TReturn route_callback_to_handler(TArgs... args, Token token)
  {
    LockGuard guard(mutex_);
    auto handler_it = handlers_.find(token);
    if (handler_it != handlers_.end()) {
      auto& handler = handler_it->second;
      return (handler)(args...);
    }
    return 0;
  }

  void unregister_handler(Token token)
  {
    // Blocking unregister while callback is in progress ensures that the callback (and
    // its dependant state) remain valid during the call.
    LockGuard guard(mutex_);
    handlers_.erase(token);
  }

  using LockGuard = std::lock_guard<std::mutex>;
  using HandlerMap = std::unordered_map<Token, Handler>;
  std::atomic<size_t> callback_id_{0};
  std::mutex mutex_;
  HandlerMap handlers_;
};
}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_DEVICE_CALLBACK_ROUTER_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/common_types.h sha256=ba77857c602ebab13944ec82433de238a3deefd3cb3f5d61de12035d7e816852 bytes=3592 -->
## FILE: source/server/common_types.h

- repository: `ni/grpc-device`
- source_path: `source/server/common_types.h`
- sha256: `ba77857c602ebab13944ec82433de238a3deefd3cb3f5d61de12035d7e816852`
- bytes: 3592

````c
#ifndef NIDEVICE_GRPC_DEVICE_COMMON_TYPES_H
#define NIDEVICE_GRPC_DEVICE_COMMON_TYPES_H
#include <ivi.h>

// Note: these are defined with similar guards in several ivi-based driver
// headers that share these types.
#if !defined(_NIComplexNumber)
  #define _NIComplexNumber

  #pragma pack(push, 8)
typedef struct NIComplexNumber_struct {
  ViReal64 real;
  ViReal64 imaginary;
} NIComplexNumber;
  #pragma pack(pop)

#endif

#if !defined(_NIComplexNumberF32)
  #define _NIComplexNumberF32
typedef struct NIComplexNumberF32_struct {
  ViReal32 real;
  ViReal32 imaginary;
} NIComplexNumberF32;

#endif

#if !defined(_NIComplexI16)
  #define _NIComplexI16
typedef struct NIComplexI16_struct {
  ViInt16 real;
  ViInt16 imaginary;
} NIComplexI16;
#endif

// Structs from niRFmxInstr.h

#ifndef _NI_float64_DEFINED_
  #define _NI_float64_DEFINED_
typedef double float64;
#endif

#ifndef _NI_float32_DEFINED_
  #define _NI_float32_DEFINED_
typedef float float32;
#endif

#if !defined(_NIComplexSinglePrecision)
  #define _NIComplexSinglePrecision

  #ifndef _WIN64
    #pragma pack(push, 1)
  #endif

typedef struct NIComplexSingle_struct {
  float32 real;
  float32 imaginary;
} NIComplexSingle;

  #ifndef _WIN64
    #pragma pack(pop)
  #endif

#endif

#if !defined(_NIComplexDoublePrecision)
  #define _NIComplexDoublePrecision

  #ifndef _WIN64
    #pragma pack(push, 1)
  #endif

typedef struct NIComplexDouble_struct {
  float64 real;
  float64 imaginary;
} NIComplexDouble;

  #ifndef _WIN64
    #pragma pack(pop)
  #endif

#endif

#ifndef _NI_int8_DEFINED_
#define _NI_int8_DEFINED_
	typedef signed char        int8;
#endif
#ifndef _NI_uInt8_DEFINED_
#define _NI_uInt8_DEFINED_
	typedef unsigned char      uInt8;
#endif
#ifndef _NI_int16_DEFINED_
#define _NI_int16_DEFINED_
	typedef signed short       int16;
#endif
#ifndef _NI_uInt16_DEFINED_
#define _NI_uInt16_DEFINED_
	typedef unsigned short     uInt16;
#endif
#ifndef _NI_int32_DEFINED_
#define _NI_int32_DEFINED_
#if ((defined(__GNUG__) || defined(__GNUC__)) && defined(__x86_64__))
	typedef signed int         int32;
#else
	typedef signed long        int32;
#endif
#endif
#ifndef _NI_uInt32_DEFINED_
#define _NI_uInt32_DEFINED_
#if ((defined(__GNUG__) || defined(__GNUC__)) && defined(__x86_64__))
	typedef unsigned int       uInt32;
#else
	typedef unsigned long      uInt32;
#endif
#endif
#ifndef _NI_float32_DEFINED_
#define _NI_float32_DEFINED_
	typedef float              float32;
#endif
#ifndef _NI_float64_DEFINED_
#define _NI_float64_DEFINED_
	typedef double             float64;
#endif
#ifndef _NI_int64_DEFINED_
#define _NI_int64_DEFINED_
#if defined(__linux__) || defined(__APPLE__)
	typedef long long int      int64;
#else
	typedef __int64            int64;
#endif
#endif
#ifndef _NI_uInt64_DEFINED_
#define _NI_uInt64_DEFINED_
#if defined(__linux__) || defined(__APPLE__)
	typedef unsigned long long uInt64;
#else
	typedef unsigned __int64   uInt64;
#endif
#endif

/*- Time Structures and Helpers ----------------------------------*/

// Please visit ni.com/info and enter the Info Code NI_BTF for more information
#ifndef CVITime_DECLARED
  #define CVITime_DECLARED
typedef struct CVITime {
  uInt64 lsb;
  uInt64 msb;
} CVITime;
#endif
#ifndef CVIAbsoluteTime_DECLARED
  #define CVIAbsoluteTime_DECLARED
typedef union CVIAbsoluteTime {
  CVITime cviTime;
  unsigned int u32Data[4];
} CVIAbsoluteTime;
#endif

#endif /* NIDEVICE_GRPC_DEVICE_COMMON_TYPES_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/converters.h sha256=30a3eca7963a3d4f1d0940762083c58ba0c06349ff3e7b660d5ba976f7c9375e bytes=16026 -->
## FILE: source/server/converters.h

- repository: `ni/grpc-device`
- source_path: `source/server/converters.h`
- sha256: `30a3eca7963a3d4f1d0940762083c58ba0c06349ff3e7b660d5ba976f7c9375e`
- bytes: 16026

````c
#ifndef NIDEVICE_GRPC_DEVICE_CONVERTERS_H
#define NIDEVICE_GRPC_DEVICE_CONVERTERS_H

#include <google/protobuf/repeated_field.h>
#include <google/protobuf/util/time_util.h>
#include <grpcpp/grpcpp.h>
#include <nidevice.pb.h>          // For common grpc types.
#include <ni/protobuf/types/precision_timestamp.pb.h>
#include <server/common_types.h>  // For common C types.
#include <server/exceptions.h>
#include <utf8.h>

#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <sstream>
#include <string>
#include <typeinfo>
#include <vector>

namespace nidevice_grpc {
namespace converters {
inline void trim_trailing_nulls(std::string& s)
{
  // Erase from the first non-null character (going backwards) to the end.
  s.erase(
      std::find_if(
          s.rbegin(),
          s.rend(),
          [](unsigned char ch) { return ch != 0; })
          .base(),
      s.end());
}

enum MatchState {
  MISMATCH,
  MATCH,
  MATCH_OR_ZERO
};

struct LinkedArraySize {
  int size = 0;
  MatchState match_state = MatchState::MISMATCH;
};

template <size_t N>
inline LinkedArraySize calculate_linked_array_size(const std::array<int, N>& sizes, bool allow_optional)
{
  if (std::adjacent_find(sizes.begin(), sizes.end(), std::not_equal_to<>()) == sizes.end()) {
    return LinkedArraySize{sizes[0], MatchState::MATCH};
  }

  if (!allow_optional) {
    return LinkedArraySize{0, MatchState::MISMATCH};
  }

  int consensus_size = sizes[0];
  for (auto size_iter = sizes.begin() + 1; size_iter != sizes.end(); ++size_iter) {
    const auto size = *size_iter;
    if (size == consensus_size)
      ;  // pass
    else if (size == 0 || consensus_size == 0)
      consensus_size = std::max(size, consensus_size);
    else
      return LinkedArraySize{0, MatchState::MISMATCH};
  }

  return LinkedArraySize{consensus_size, MatchState::MATCH_OR_ZERO};
}

// Wrapper on std::vector that allows assigning or initializing from nullptr.
// When in an is_null_ state, data() will return nullptr.
// This class is intended to make it easier to write code that works with both
// vectors and pointers without complex, special-case codegen.
template <typename T>
class nullable_vector {
 public:
  nullable_vector(std::vector<T>&& vec) : vec_(std::move(vec)), is_null_(false)
  {
  }

  nullable_vector(std::nullptr_t) : vec_(), is_null_(true)
  {
  }

  nullable_vector<T>& operator=(std::nullptr_t)
  {
    vec_.clear();
    is_null_ = true;
    return *this;
  }

  T* data()
  {
    return is_null_ ? nullptr : vec_.data();
  }

  const T* data() const
  {
    return is_null_ ? nullptr : vec_.data();
  }

 private:
  bool is_null_;
  std::vector<T> vec_;
};

template <typename CType, typename GrpcType>
void convert_to_grpc(const CType& value, GrpcType* value_out)
{
  *value_out = static_cast<GrpcType>(value);
}

template <typename CType, typename GrpcType>
CType convert_from_grpc(const GrpcType& value)
{
  return static_cast<CType>(value);
}

template <typename T>
inline T convert_size(size_t value, const char* parameter_name)
{
  if (value > std::numeric_limits<T>::max()) {
    std::stringstream message_stream;
    message_stream << "Size exceeds " << typeid(T).name() << " range for parameter " << parameter_name;
    throw nidevice_grpc::NonDriverException(::grpc::StatusCode::INVALID_ARGUMENT, message_stream.str());
  }
  return static_cast<T>(value);
}

inline bool is_ascii(const char* str)
{
  for (; *str != '\0'; ++str) {
    if (static_cast<unsigned char>(*str) > 0x7f) {
      return false;
    }
  }
  return true;
}

template <>
inline std::string convert_from_grpc(const std::string& value)
{
  if (is_ascii(value.c_str())) {
    return value;
  }
#if WIN32
  std::wstring utf16value;
  utf16value.reserve(value.length());  // often too much, but that's okay
  utf8::utf8to16(value.begin(), value.end(), std::back_inserter(utf16value));
  int flags = GetACP() == 54936 ? 0 : 0x400;  // WC_NO_BEST_FIT_CHARS; not supported for GB18030
  int mbs_len = WideCharToMultiByte(CP_ACP, flags, utf16value.c_str(), -1, NULL, 0, NULL, NULL);
  if (mbs_len == 0) {
    throw new std::runtime_error("Unknown character in string");
  }
  --mbs_len;  // don't include trailing null
  std::string converted(mbs_len, '\0');
  WideCharToMultiByte(CP_ACP, flags, utf16value.c_str(), -1, &converted[0], mbs_len, NULL, NULL);
  return converted;
#else
  std::wstring utf32value;
  utf32value.reserve(utf8::distance(value.begin(), value.end()));
  utf8::utf8to32(value.begin(), value.end(), std::back_inserter(utf32value));
  size_t mbs_len = wcstombs(NULL, utf32value.c_str(), 0);
  if (mbs_len == (size_t)-1) {
    throw new std::runtime_error("Unknown character in string");
  }
  std::string converted(mbs_len, '\0');
  wcstombs(&converted[0], utf32value.c_str(), mbs_len);
  return converted;
#endif
}

template <>
inline void convert_to_grpc(const std::string& value, std::string* value_out)
{
  if (is_ascii(value.c_str())) {
    *value_out = value;
    return;
  }
#if WIN32
  int flags = MB_ERR_INVALID_CHARS | (GetACP() == 54936 ? 0 : MB_PRECOMPOSED);
  int wcs_len = MultiByteToWideChar(CP_ACP, flags, value.c_str(), -1, NULL, 0);
  if (wcs_len == 0) {
    throw new std::runtime_error("Unknown character in string");
  }
  --wcs_len;  // don't include trailing null
  std::wstring utf16value(wcs_len, '\0');
  MultiByteToWideChar(CP_ACP, flags, value.c_str(), -1, &utf16value[0], wcs_len);
  // Pre-reserve something close to the target byte count, for performance; doesn't have to be exact
  value_out->reserve(utf16value.length());
  utf8::utf16to8(utf16value.begin(), utf16value.end(), std::back_inserter(*value_out));
#else
  size_t wcs_len = mbstowcs(NULL, value.c_str(), 0);
  if (wcs_len == (size_t)-1) {
    throw new std::runtime_error("Unknown character in string");
  }
  std::wstring utf32value(wcs_len, '\0');
  mbstowcs(&utf32value[0], value.c_str(), wcs_len);
  // Pre-reserve something close to the target byte count, for performance; doesn't have to be exact
  value_out->reserve(utf32value.length());
  utf8::utf32to8(utf32value.begin(), utf32value.end(), std::back_inserter(*value_out));
#endif
}

template <typename CType, typename GrpcType>
inline nullable_vector<CType> convert_from_grpc(const google::protobuf::RepeatedPtrField<GrpcType>& input)
{
  auto output = std::vector<CType>();
  output.reserve(input.size());
  std::transform(
      input.begin(),
      input.end(),
      std::back_inserter(output),
      [&](GrpcType x) { return convert_from_grpc<CType>(x); });
  return nullable_vector<CType>(std::move(output));
}

template <typename CType, typename GrpcType>
inline std::vector<CType> convert_from_grpc(const google::protobuf::RepeatedField<GrpcType>& input)
{
  auto output = std::vector<CType>();
  output.reserve(input.size());
  std::transform(
      input.begin(),
      input.end(),
      std::back_inserter(output),
      [&](GrpcType x) { return convert_from_grpc<CType>(x); });
  return output;
}

template <typename GrpcType, typename CType>
inline void convert_to_grpc(const std::vector<CType>& input, google::protobuf::RepeatedPtrField<GrpcType>* output)
{
  output->Reserve(static_cast<int>(input.size()));
  for (auto item : input) {
    auto message = new GrpcType();
    convert_to_grpc(item, message);
    output->AddAllocated(message);
  }
}

template <typename BoolType>
inline void convert_to_grpc(const std::vector<BoolType>& input, google::protobuf::RepeatedField<bool>* output)
{
  output->Reserve(static_cast<int>(input.size()));
  for (auto item : input) {
    output->Add(item != BoolType(0));
  }
}

template <>
inline void convert_to_grpc(const NIComplexNumberF32_struct& input, nidevice_grpc::NIComplexNumberF32* output)
{
  output->set_real(input.real);
  output->set_imaginary(input.imaginary);
}

template <>
inline NIComplexNumberF32_struct convert_from_grpc(const nidevice_grpc::NIComplexNumberF32& input)
{
  auto output = NIComplexNumberF32_struct();
  output.real = input.real();
  output.imaginary = input.imaginary();
  return output;
}

template <>
inline void convert_to_grpc(const NIComplexSingle_struct& input, nidevice_grpc::NIComplexNumberF32* output)
{
  output->set_real(input.real);
  output->set_imaginary(input.imaginary);
}

template <>
inline NIComplexSingle_struct convert_from_grpc(const nidevice_grpc::NIComplexNumberF32& input)
{
  auto output = NIComplexSingle_struct();
  output.real = input.real();
  output.imaginary = input.imaginary();
  return output;
}

template <>
inline void convert_to_grpc(const NIComplexNumber_struct& input, nidevice_grpc::NIComplexNumber* output)
{
  output->set_real(input.real);
  output->set_imaginary(input.imaginary);
}

template <>
inline NIComplexNumber_struct convert_from_grpc(const nidevice_grpc::NIComplexNumber& input)
{
  auto output = NIComplexNumber_struct();
  output.real = input.real();
  output.imaginary = input.imaginary();
  return output;
}

template <>
inline void convert_to_grpc(const NIComplexDouble_struct& input, nidevice_grpc::NIComplexNumber* output)
{
  output->set_real(input.real);
  output->set_imaginary(input.imaginary);
}

template <>
inline NIComplexDouble_struct convert_from_grpc(const nidevice_grpc::NIComplexNumber& input)
{
  auto output = NIComplexDouble_struct();
  output.real = input.real();
  output.imaginary = input.imaginary();
  return output;
}

template <>
inline void convert_to_grpc(const NIComplexI16_struct& input, nidevice_grpc::NIComplexI16* output)
{
  output->set_real(input.real);
  output->set_imaginary(input.imaginary);
}

template <>
inline NIComplexI16_struct convert_from_grpc(const nidevice_grpc::NIComplexI16& input)
{
  auto output = NIComplexI16_struct();
  if (input.real() < (std::numeric_limits<ViInt16>::min)() || input.real() > (std::numeric_limits<ViInt16>::max)()) {
    std::string message("value ");
    message.append(std::to_string(input.real()));
    message.append(" doesn't fit in datatype ");
    message.append("ViInt16");
    throw nidevice_grpc::ValueOutOfRangeException(message);
  }
  output.real = static_cast<ViInt16>(input.real());
  if (input.imaginary() < (std::numeric_limits<ViInt16>::min)() || input.imaginary() > (std::numeric_limits<ViInt16>::max)()) {
    std::string message("value ");
    message.append(std::to_string(input.imaginary()));
    message.append(" doesn't fit in datatype ");
    message.append("ViInt16");
    throw nidevice_grpc::ValueOutOfRangeException(message);
  }
  output.imaginary = static_cast<ViInt16>(input.imaginary());
  return output;
}

template <typename SmtSpectrumInfoType>
inline void convert_to_grpc(const SmtSpectrumInfoType& input, nidevice_grpc::SmtSpectrumInfo* output)
{
  output->set_spectrum_type(input.spectrumType);
  output->set_linear_db(input.linearDB);
  output->set_window(input.window);
  output->set_window_size(input.windowSize);
  output->set_fft_size(input.FFTSize);
}

const int64 SecondsFromCVI1904EpochTo1970Epoch = 2082844800LL;
const int64 SecondsFromDotNet0001EpochToCVI1904Epoch = -((static_cast<int64>(0xfffffff2) << 32) | 0x0493b980); // extracted from NITYPES_ABSOLUTETIME_EPOCH_BIAS_FROM_0001 in ni-central/src/platform_services/abstractions/niatomicd/nitypes/source/nitypes/time/AbsoluteTime.h
const double TwoToSixtyFour = (double)(1 << 31) * (double)(1 << 31) * (double)(1 << 2);
const double NanosecondsPerSecond = 1000000000.0;
const int64 DotNetTicksPerSecond = 10000000; // each tick is 100ns

template <>
inline void convert_to_grpc(const CVIAbsoluteTime& value, google::protobuf::Timestamp* timestamp)
{
  // msb is whole seconds after 12:00 a.m., Friday, January 1, 1904, Universal Time
  time_t unixTime = static_cast<time_t>(value.cviTime.msb - SecondsFromCVI1904EpochTo1970Epoch);
  google::protobuf::Timestamp temp_timestamp = google::protobuf::util::TimeUtil::TimeTToTimestamp(unixTime);

  timestamp->set_seconds(temp_timestamp.seconds());
  // lsb is positive fractions (2^64) of a second
  // This is losing some precision since doubles have 52 bits of precision.
  // But there are only 10^9 nanoseconds in a second which is ~31 bits of precision,
  // so it's still good enough for our purposes.
  timestamp->set_nanos(static_cast<int32>((static_cast<double>(value.cviTime.lsb) * NanosecondsPerSecond) / TwoToSixtyFour));
}

template <>
inline CVIAbsoluteTime convert_from_grpc(const google::protobuf::Timestamp& value)
{
  time_t unixTime = google::protobuf::util::TimeUtil::TimestampToTimeT(value);
  CVIAbsoluteTime cviTime;
  cviTime.cviTime.msb = static_cast<int64>(unixTime + SecondsFromCVI1904EpochTo1970Epoch);
  cviTime.cviTime.lsb = static_cast<uInt64>((static_cast<double>(value.nanos()) / NanosecondsPerSecond) * TwoToSixtyFour);
  return cviTime;
}

// Convert .NET ticks (100ns since Jan 1, 0001) to PrecisionTimestamp (NI-BTF)
inline void convert_dot_net_ticks_to_precision_timestamp(int64 dot_net_ticks, ::ni::protobuf::types::PrecisionTimestamp* timestamp)
{
  const int64 dot_net_ticks_since_1904 = dot_net_ticks - SecondsFromDotNet0001EpochToCVI1904Epoch * DotNetTicksPerSecond;
  const double total_seconds = static_cast<double>(dot_net_ticks_since_1904) / DotNetTicksPerSecond;
  double integer_part;
  double fractional_part = std::modf(total_seconds, &integer_part);
  
  timestamp->set_seconds(static_cast<int64>(integer_part));
  timestamp->set_fractional_seconds(static_cast<uint64_t>(std::abs(fractional_part) * TwoToSixtyFour));
}

// Or together input_array and input_raw to implement the "bitfield_as_enum_array" feature for inputs.
// Note: TEnum is unused because protobuf C++ represents repeated enums as a int32 arrays.
template <typename TArray, typename TBitfield>
inline TBitfield convert_bitfield_as_enum_array_input(
    const TArray& input,
    TBitfield input_raw)
{
  const auto or_delegate = [](google::protobuf::int32 first, google::protobuf::int32 second) { return static_cast<TBitfield>(first | second); };
  return input_raw | std::accumulate(input.cbegin(), input.cend(), TBitfield{0}, or_delegate);
}

// TypeToStorageType should be specialized to define a (TDriverType, TGrpcType)->StorageType mapping, which
// will be used by allocate_output_storage.
template <typename TDriverType, typename TGrpcType>
struct TypeToStorageType {
  using StorageType = TDriverType;
};

// Constructs a default implementation of TypeToStorageType<TDriverType>::StorageType to use as an output_param.
// This should be customized by specializing the TypeToStorageType struct.
template <typename TDriverType, typename TGrpcType, typename... TArgs>
typename TypeToStorageType<TDriverType, TGrpcType>::StorageType allocate_output_storage(TArgs... args)
{
  using StorageType = typename TypeToStorageType<TDriverType, TGrpcType>::StorageType;
  return StorageType{args...};
}

}  // namespace converters

const int kMaxGrpcErrorDescriptionSize = 2048;

template <typename TServerContext>
inline ::grpc::Status ApiErrorAndDescriptionToStatus(TServerContext* context, int32_t status, std::string& description)
{
  context->AddTrailingMetadata("ni-error", std::to_string(status));
  converters::trim_trailing_nulls(description);
  std::string description_utf8;
  converters::convert_to_grpc(description, &description_utf8);
  return ::grpc::Status(grpc::StatusCode::UNKNOWN, description_utf8);
}

template <typename TServerContext>
inline ::grpc::Status ApiErrorToStatus(TServerContext* context, int32_t status)
{
  std::string description("Unknown");
  return ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nidevice_grpc

#endif /* NIDEVICE_GRPC_DEVICE_CONVERTERS_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/core_server.cpp sha256=8b2bc886cbaeef322c8e2838e038ae7af04199bfbda72ff2dd6a6c83b850ef2b bytes=11488 -->
## FILE: source/server/core_server.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/core_server.cpp`
- sha256: `8b2bc886cbaeef322c8e2838e038ae7af04199bfbda72ff2dd6a6c83b850ef2b`
- bytes: 11488

````cpp
#include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <grpcpp/grpcpp.h>
#include <register_all_services.h>
#include <sideband_data.h>

#include <mutex>
#include <thread>
#include <algorithm>

#include "feature_toggles.h"
#include "logging.h"
#include "tls_config_loader.h"
#include "server_configuration_parser.h"
#include "server_security_configuration.h"
#include "moniker_stream_processor.h"

#if defined(__GNUC__)
  #include <sys/mman.h>

  #include "linux/daemonize.h"
  #include "linux/syslog_logging.h"
#endif
#if defined(_WIN32)
  #include "windows/console_ctrl_handler.h"
#endif

#include "version.h"
#include "data_moniker_service.h"

using FeatureState = nidevice_grpc::FeatureToggles::FeatureState;
using FeatureToggles = nidevice_grpc::FeatureToggles;

struct ServerConfiguration {
  std::string config_file_path;
  std::string server_address;
  std::string sideband_address;
  std::string server_cert;
  std::string server_key;
  std::string root_cert;
  std::string security_mode;
  int max_message_size;
  int sideband_port;
  nidevice_grpc::FeatureToggles feature_toggles;
  MonikerStreamProcessor stream_processor;
};

static ServerConfiguration GetConfiguration(const std::string& config_file_path)
{
  ServerConfiguration config;
  try {
    nidevice_grpc::ServerConfigurationParser server_config_parser = config_file_path.empty()
        ? nidevice_grpc::ServerConfigurationParser()
        : nidevice_grpc::ServerConfigurationParser(config_file_path);

    config.config_file_path = server_config_parser.get_config_file_path();
    config.server_address = server_config_parser.parse_address();
    config.sideband_address = server_config_parser.parse_sideband_address();
    config.sideband_port = server_config_parser.parse_sideband_port();
    config.stream_processor = server_config_parser.parse_moniker_stream_processor();
    config.feature_toggles = server_config_parser.parse_feature_toggles();
    if (config.feature_toggles.is_feature_enabled("ni-tls-config", nidevice_grpc::FeatureToggles::CodeReadiness::kNextRelease)) {
      config.security_mode = server_config_parser.parse_security_mode();
    }
    if (config.security_mode != "ni-tls-config") {
      config.server_cert = server_config_parser.parse_server_cert();
      config.server_key = server_config_parser.parse_server_key();
      config.root_cert = server_config_parser.parse_root_cert();
    }
    config.max_message_size = server_config_parser.parse_max_message_size();
  }
  catch (const std::exception& ex) {
    nidevice_grpc::logging::log(
        nidevice_grpc::logging::Level_Error,
        "Failed to parse config: %s", ex.what());
    exit(EXIT_FAILURE);
  }
  return config;
}

static std::mutex server_mutex;
static std::unique_ptr<grpc::Server> server;
static bool shutdown_server = false;

static void StopServer()
{
  std::lock_guard<std::mutex> guard(server_mutex);
  shutdown_server = true;
  if (server) {
    server->Shutdown();
  }
}

static void RunServer(const ServerConfiguration& config)
{
  if (!config.config_file_path.empty()) {
    nidevice_grpc::logging::log(
        nidevice_grpc::logging::Level_Info,
        "Using server configuration from %s",
        config.config_file_path.c_str());
  }

  grpc::EnableDefaultHealthCheckService(true);
  grpc::reflection::InitProtoReflectionServerBuilderPlugin();

  grpc::ServerBuilder builder;
  nidevice_grpc::ServerSecurityConfiguration server_security_config;
  if (config.feature_toggles.is_feature_enabled("ni-tls-config", nidevice_grpc::FeatureToggles::CodeReadiness::kNextRelease) &&
      config.security_mode == "ni-tls-config") {
    nidevice_grpc::TlsConfigLoader loader;
    if (!loader.is_available()) {
      nidevice_grpc::logging::log(
          nidevice_grpc::logging::Level_Error,
          "ni-tls-config mode requested but nitlsconfig library could not be loaded"
          " - is ni-tls-config installed?");
      exit(EXIT_FAILURE);
    }
    try {
      server_security_config = loader.get_server_credentials("ni-grpc-device");
    }
    catch (const std::exception& ex) {
      nidevice_grpc::logging::log(
          nidevice_grpc::logging::Level_Error,
          "Failed to load TLS credentials from ni-tls-config: %s", ex.what());
      exit(EXIT_FAILURE);
    }
  }
  else {
    if (!config.security_mode.empty()) {
      nidevice_grpc::logging::log(
          nidevice_grpc::logging::Level_Error,
          "Unsupported security mode: \"%s\". The only supported security mode string is \"ni-tls-config\".",
          config.security_mode.c_str());
      exit(EXIT_FAILURE);
    }
    server_security_config = nidevice_grpc::ServerSecurityConfiguration(config.server_cert, config.server_key, config.root_cert);
  }
  int listeningPort = 0;
  builder.AddListeningPort(config.server_address, server_security_config.get_credentials(), &listeningPort);

  auto services = nidevice_grpc::register_all_services(builder, config.feature_toggles);

  builder.SetMaxSendMessageSize(config.max_message_size);
  builder.SetMaxReceiveMessageSize(config.max_message_size);

  // Assemble the server.
  {
    std::lock_guard<std::mutex> guard(server_mutex);
    if (shutdown_server) {
      nidevice_grpc::logging::log(
          nidevice_grpc::logging::Level_Info,
          "Asked to shutdown before creating the server");
      return;
    }
    server = builder.BuildAndStart();
    if (ni::data_monikers::is_moniker_streaming_enabled(config.feature_toggles)) {
      ni::data_monikers::configure_moniker_stream_processor(config.stream_processor);
      if (ni::data_monikers::is_moniker_streaming_sideband_support_enabled(config.feature_toggles)) {
      auto sideband_socket_thread = new std::thread(RunSidebandSocketsAccept, config.sideband_address.c_str(), config.sideband_port);
      // auto sideband_rdma_send_thread = new std::thread(AcceptSidebandRdmaSendRequests);
      // auto sideband_rdma_recv_thread = new std::thread(AcceptSidebandRdmaReceiveRequests);
      }
    }
  }

  if (!server) {
    nidevice_grpc::logging::log(
        nidevice_grpc::logging::Level_Error,
        "Server failed to start on %s", config.server_address.c_str());
    exit(EXIT_FAILURE);
  }

  nidevice_grpc::logging::log(nidevice_grpc::logging::Level_Info, "Server listening on port %d", listeningPort);

  if (server_security_config.is_insecure_credentials()) {
    auto address_lower = config.server_address;
    std::transform(address_lower.begin(), address_lower.end(), address_lower.begin(), ::tolower);
    bool is_loopback = address_lower.find("localhost") != std::string::npos ||
                       address_lower.find("127.0.0.1") != std::string::npos ||
                       address_lower.find("[::1]") != std::string::npos;
    if (!is_loopback) {
      nidevice_grpc::logging::log(
          nidevice_grpc::logging::Level_Warning,
          "WARNING: Server is using insecure credentials on a non-loopback address (%s). "
          "All RPCs are accessible without authentication. Consider configuring TLS or "
          "binding to a loopback address.",
          config.server_address.c_str());
    }
  }

  const char* security_description = server_security_config.is_insecure_credentials()
      ? "insecure credentials"
      : "secure credentials";
  const char* tls_description = "";
  auto credentials_options = server_security_config.try_get_options();
  if (credentials_options != nullptr) {
    tls_description = credentials_options->client_certificate_request == GRPC_SSL_DONT_REQUEST_CLIENT_CERTIFICATE
        ? " (Server-Side TLS)"
        : " (Mutual TLS)";
  }
  nidevice_grpc::logging::log(
      nidevice_grpc::logging::Level_Info,
      "Security is configured with %s%s.", security_description, tls_description);
  // This call will block until another thread shuts down the server.
  server->Wait();

  // destroy services in reverse order
  while (!services->empty()) {
    services->pop_back();
  }

  nidevice_grpc::logging::log(nidevice_grpc::logging::Level_Info, "Server stopped.");
}

struct Options {
  Options() :
#if defined(__GNUC__)
              daemonize(false),
              use_syslog(false),
              identity("ni_grpc_device_server"),
#endif
              config_file_path()
  {
  }

#if defined(__GNUC__)
  bool daemonize;
  bool use_syslog;
  std::string identity;
#endif
  std::string config_file_path;
};

#if defined(__GNUC__)
const char* usage = "Usage: ni_grpc_device_server [--help] [--daemonize] [--use-syslog] [--identity <foo>] [config-file-path]";
#else
const char* usage = "Usage: ni_grpc_device_server [--help] [config-file-path]";
#endif

Options parse_options(int argc, char** argv)
{
  Options options;
  for (int i = 1; i < argc; ++i) {
    bool known_option = true;
#if defined(__GNUC__)
    if (strcmp("--daemonize", argv[i]) == 0) {
      options.daemonize = true;
    }
    else if (strcmp("--use-syslog", argv[i]) == 0) {
      options.use_syslog = true;
    }
    else if (strcmp("--identity", argv[i]) == 0) {
      if (i + 1 < argc) {
        options.identity = argv[++i];
      }
      else {
        known_option = false;
      }
    }
    else
#endif
        if (strcmp("--help", argv[i]) == 0 || strcmp("-h", argv[i]) == 0) {
      nidevice_grpc::logging::log(nidevice_grpc::logging::Level_Info, usage);
      exit(EXIT_SUCCESS);
    }
    else if (strcmp("--version", argv[i]) == 0) {
      std::string string_kNiDeviceGrpcBranchName(nidevice_grpc::kNiDeviceGrpcBranchName);
      if (string_kNiDeviceGrpcBranchName.rfind("releases", 0) == 0) {
        nidevice_grpc::logging::log(nidevice_grpc::logging::Level_Info, nidevice_grpc::kNiDeviceGrpcFileVersion);
      }
      else {
        nidevice_grpc::logging::log(nidevice_grpc::logging::Level_Info, nidevice_grpc::kNiDeviceGrpcFileVersion);
        nidevice_grpc::logging::log(nidevice_grpc::logging::Level_Info, "dev");
      }
      exit(EXIT_SUCCESS);
    }
    else if (i == argc - 1) {
      options.config_file_path = argv[i];
    }
    else {
      known_option = false;
    }

    if (!known_option) {
      nidevice_grpc::logging::log(nidevice_grpc::logging::Level_Error, usage);
      exit(EXIT_FAILURE);
    }
  }

#if defined(__GNUC__)
  if (options.daemonize && !options.use_syslog) {
    nidevice_grpc::logging::log(nidevice_grpc::logging::Level_Error, "--daemonize requires --use-syslog");
    exit(EXIT_FAILURE);
  }
#endif

  return options;
}

static void SysFsWrite(const std::string& fileName, const std::string& value)
{
  std::ofstream fout;
  fout.open(fileName);
  fout << value;
  fout.close();
}

int main(int argc, char** argv)
{
  auto options = parse_options(argc, argv);
  auto config = GetConfiguration(options.config_file_path);
  setlocale(LC_ALL, "");
#if defined(__GNUC__)
  if (options.use_syslog) {
    nidevice_grpc::logging::setup_syslog(options.daemonize, options.identity);
    nidevice_grpc::logging::set_logger(&nidevice_grpc::logging::log_syslog);
  }

  if (options.daemonize) {
    nidevice_grpc::daemonize(&StopServer, options.identity);
  }
#endif
#if defined(_WIN32)
  nidevice_grpc::set_console_ctrl_handler(&StopServer);
#endif

  RunServer(config);
  return EXIT_SUCCESS;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/core_services_registrar.cpp sha256=cb264d7aadb86defb2cb4e019d45a17b0f1f747208d1ab972fdce6e7a0bad1f3 bytes=1564 -->
## FILE: source/server/core_services_registrar.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/core_services_registrar.cpp`
- sha256: `cb264d7aadb86defb2cb4e019d45a17b0f1f747208d1ab972fdce6e7a0bad1f3`
- bytes: 1564

````cpp
#include "core_services_registrar.h"

#include "calibration_operations_restricted_service_registrar.h"
#include "data_moniker_service.h"
#include "debug_session_properties_restricted_service_registrar.h"
#include "server_reset_observer_registrar_interface.h"
#include "session_utilities_service_registrar.h"

namespace nidevice_grpc {
void register_core_services(
  std::shared_ptr<std::vector<std::shared_ptr<void>>>& service_vector,
  grpc::ServerBuilder& server_builder,
  const std::shared_ptr<nidevice_grpc::SessionRepository>& session_repository,
  const nidevice_grpc::FeatureToggles& feature_toggles)
{
  ServerResetObserverRegistrarInterface* server_reset_observer_registrar;
  service_vector->push_back(nidevice_grpc::register_session_utilities_service(
    server_builder,
    session_repository,
    &server_reset_observer_registrar));
  service_vector->push_back(nidevice_restricted_grpc::register_calibration_operations_restricted_service(
    server_builder,
    feature_toggles,
    *server_reset_observer_registrar));
  service_vector->push_back(nidevice_restricted_grpc::register_debug_session_properties_restricted_service(
    server_builder,
    feature_toggles,
    *server_reset_observer_registrar));

  if (ni::data_monikers::is_moniker_streaming_enabled(feature_toggles)) {
    auto moniker_service = std::make_shared<ni::data_monikers::DataMonikerService>();
    server_builder.RegisterService(moniker_service.get());
    service_vector->push_back(moniker_service);
  }
}
}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/core_services_registrar.h sha256=924e9e9d726f6c45da37c20a1614d2d8561640c5656aa204020341ca78947105 bytes=614 -->
## FILE: source/server/core_services_registrar.h

- repository: `ni/grpc-device`
- source_path: `source/server/core_services_registrar.h`
- sha256: `924e9e9d726f6c45da37c20a1614d2d8561640c5656aa204020341ca78947105`
- bytes: 614

````c
#ifndef NIDEVICE_GRPC_DEVICE_CORE_SERVICES_REGISTRAR_H
#define NIDEVICE_GRPC_DEVICE_CORE_SERVICES_REGISTRAR_H

#include <memory>

#include "feature_toggles.h"
#include "session_repository.h"

namespace grpc {
class ServerBuilder;
}

namespace nidevice_grpc {
void register_core_services(
  std::shared_ptr<std::vector<std::shared_ptr<void>>>& service_vector,
  grpc::ServerBuilder& server_builder,
  const std::shared_ptr<nidevice_grpc::SessionRepository>& session_repository,
  const nidevice_grpc::FeatureToggles& feature_toggles);
}
#endif  // NIDEVICE_GRPC_DEVICE_CORE_SERVICES_REGISTRAR_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/data_moniker_service.cpp sha256=56a5d80c480824f2f9945902ff7b606e042ce5fdb66891186862b8297c02971e bytes=14042 -->
## FILE: source/server/data_moniker_service.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/data_moniker_service.cpp`
- sha256: `56a5d80c480824f2f9945902ff7b606e042ce5fdb66891186862b8297c02971e`
- bytes: 14042

````cpp
//---------------------------------------------------------------------
//---------------------------------------------------------------------
#include "data_moniker_service.h"
#include "exceptions.h"
#include "moniker_stream_processor.h"

#include <sideband_data.h>
#include <sideband_grpc.h>
#include <sideband_internal.h>

#include <thread>
#include <tuple>
#ifndef _WIN32
  #include <sys/syscall.h>
#endif

#include <fstream>
#include <sstream>

//---------------------------------------------------------------------
//---------------------------------------------------------------------
using google::protobuf::Arena;
using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::ServerReaderWriter;
using grpc::ServerWriter;
using grpc::Status;
using ni::data_monikers::BeginMonikerSidebandStreamRequest;
using ni::data_monikers::BeginMonikerSidebandStreamResponse;
using ni::data_monikers::DataMoniker;
using ni::data_monikers::MonikerList;
using ni::data_monikers::MonikerReadResponse;
using ni::data_monikers::MonikerWriteRequest;
using ni::data_monikers::SidebandReadResponse;
using ni::data_monikers::SidebandWriteRequest;
using ni::data_monikers::StreamWriteResponse;
using std::string;

static void SysFsWrite(const std::string& fileName, const std::string& value)
{
  std::ofstream fout;
  fout.open(fileName);
  fout << value;
  fout.close();
}

namespace ni::data_monikers {

static MonikerStreamProcessor s_StreamProcessor;

void configure_moniker_stream_processor(const MonikerStreamProcessor& stream_processor)
{
  s_StreamProcessor = stream_processor;
}

bool is_moniker_streaming_enabled(const nidevice_grpc::FeatureToggles& feature_toggles)
{
  return feature_toggles.is_feature_enabled("moniker_streaming", nidevice_grpc::FeatureToggles::CodeReadiness::kNextRelease);
}

bool is_moniker_streaming_sideband_support_enabled(const nidevice_grpc::FeatureToggles& feature_toggles)
{
  return feature_toggles.is_feature_enabled("moniker_streaming_sideband_support", nidevice_grpc::FeatureToggles::CodeReadiness::kNextRelease);
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
DataMonikerService* DataMonikerService::s_Server;

//---------------------------------------------------------------------
//---------------------------------------------------------------------
DataMonikerService::DataMonikerService()
{
  s_Server = this;
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
void DataMonikerService::RegisterMonikerEndpoint(string endpointName, MonikerEndpointPtr endpoint)
{
  s_Server->_endpoints.emplace(endpointName, endpoint);
}

//---------------------------------------------------------------------
// CWE-822: Register instance data behind an opaque handle instead of
// transmitting raw pointers over gRPC. The handle is a random 64-bit
// value that maps to the actual pointer in s_instance_registry.
// Randomized handles prevent attackers from guessing valid handles.
//---------------------------------------------------------------------
void DataMonikerService::RegisterMonikerInstance(string endpointName, void* instanceData, Moniker& moniker)
{
  int64_t handle;
  {
    std::lock_guard<std::mutex> lock(s_Server->instance_mutex_);
    do {
      handle = static_cast<int64_t>(s_Server->rng_());
    } while (handle == 0 || s_Server->instance_registry_.count(handle));
    s_Server->instance_registry_[handle] = instanceData;
  }
  moniker.set_data_instance(handle);
  moniker.set_service_location("local");
  moniker.set_data_source(endpointName);
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
void* DataMonikerService::LookupInstance(int64_t handle)
{
  std::lock_guard<std::mutex> lock(s_Server->instance_mutex_);
  auto it = s_Server->instance_registry_.find(handle);
  if (it != s_Server->instance_registry_.end()) {
    return it->second;
  }
  return nullptr;
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
void DataMonikerService::InitiateMonikerList(const MonikerList& monikers, EndpointList* readers, EndpointList* writers)
{
  for (auto readMoniker : monikers.read_monikers()) {
    auto instance = readMoniker.data_instance();
    auto source = readMoniker.data_source();
    auto it = _endpoints.find(source);
    if (it == _endpoints.end()) {
      throw nidevice_grpc::NonDriverException(grpc::INVALID_ARGUMENT, "Unknown moniker data_source: " + source);
    }
    void* instancePtr = LookupInstance(instance);
    if (!instancePtr) {
      throw nidevice_grpc::NonDriverException(grpc::INVALID_ARGUMENT, "Invalid moniker data_instance handle");
    }
    readers->push_back(EndpointInstance((*it).second, instancePtr));
  }
  for (auto writeMoniker : monikers.write_monikers()) {
    auto instance = writeMoniker.data_instance();
    auto source = writeMoniker.data_source();
    auto it = _endpoints.find(source);
    if (it == _endpoints.end()) {
      throw nidevice_grpc::NonDriverException(grpc::INVALID_ARGUMENT, "Unknown moniker data_source: " + source);
    }
    void* instancePtr = LookupInstance(instance);
    if (!instancePtr) {
      throw nidevice_grpc::NonDriverException(grpc::INVALID_ARGUMENT, "Invalid moniker data_instance handle");
    }
    writers->push_back(EndpointInstance((*it).second, instancePtr));
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
#ifndef _WIN32
void set_cpu_affinity(int cpu)
{
  if (cpu >= 0) {
    cpu_set_t cpuSet;
    CPU_ZERO(&cpuSet);
    CPU_SET(cpu, &cpuSet);
    sched_setaffinity(0, sizeof(cpu_set_t), &cpuSet);
  }
}
#endif

//---------------------------------------------------------------------
//---------------------------------------------------------------------
void DataMonikerService::RunSidebandReadWriteLoop(string sidebandIdentifier, ::SidebandStrategy strategy, EndpointList readers, EndpointList writers)
{
#ifndef _WIN32
  if (strategy == ::SidebandStrategy::RDMA_LOW_LATENCY ||
      strategy == ::SidebandStrategy::SOCKETS_LOW_LATENCY) {
    pid_t threadId = syscall(SYS_gettid);
    ::SysFsWrite("/dev/cgroup/cpuset/LabVIEW_tl_set/tasks", std::to_string(threadId));

    set_cpu_affinity(s_StreamProcessor.moniker_sideband_stream_read_write);
  }
#endif

  google::protobuf::Arena arena;
  int64_t sidebandToken;
  GetOwnerSidebandDataToken(sidebandIdentifier.c_str(), &sidebandToken);
  while (true) {
    auto writeRequest = google::protobuf::Arena::Create<SidebandWriteRequest>(&arena);
    if (!ReadSidebandMessage(sidebandToken, writeRequest)) {
      break;
    }
    if (writeRequest->cancel()) {
      break;
    }
    if (writers.size() > 0) {
      int x = 0;
      if (writers.size() != writeRequest->values().values_size()) {
        break;
      }
      for (auto writer : writers) {
        std::get<0>(writer)(std::get<1>(writer), arena, const_cast<google::protobuf::Any&>(writeRequest->values().values(x++)));
      }
    }
    auto readResult = Arena::Create<SidebandReadResponse>(&arena);
    if (readers.size() > 0) {
      int x = 0;
      for (auto reader : readers) {
        auto readValue = readResult->mutable_values()->add_values();
        std::get<0>(reader)(std::get<1>(reader), arena, *readValue);
      }
    }
    if (!WriteSidebandMessage(sidebandToken, *readResult)) {
      break;
    }
    arena.Reset();
    std::this_thread::sleep_for(std::chrono::microseconds(10));
  }
  CloseSidebandData(sidebandToken);
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
Status DataMonikerService::BeginSidebandStream(ServerContext* context, const BeginMonikerSidebandStreamRequest* request, BeginMonikerSidebandStreamResponse* response)
{
  try {
    // CWE-20: Validate the strategy enum before casting to the sideband library type.
    // Protobuf accepts any int32 on the wire, so an out-of-range value would be
    // passed through static_cast unchecked, causing undefined behavior.
    auto requested_strategy_enum = request->strategy();
    if (!ni::data_monikers::SidebandStrategy_IsValid(requested_strategy_enum) ||
        requested_strategy_enum == ni::data_monikers::UNKNOWN) {
      return Status(grpc::INVALID_ARGUMENT,
          "Invalid sideband strategy: " + std::to_string(static_cast<int>(requested_strategy_enum)));
    }
    auto sideband_strategy = static_cast<::SidebandStrategy>(requested_strategy_enum);

    auto bufferSize = 1024 * 1024;

    char identifier[32] = {};
    auto sideband_init_result = InitOwnerSidebandData(sideband_strategy, bufferSize, identifier);
    if (sideband_init_result == -1) {
      return Status(grpc::UNKNOWN,
        "Failed to initialize sideband stream for strategy: " + std::to_string(static_cast<int>(requested_strategy_enum)));
    }
    std::string identifierString(identifier);

    response->set_strategy(request->strategy());
    response->set_sideband_identifier(identifier);
    response->set_connection_url(GetConnectionAddress(sideband_strategy));
    response->set_buffer_size(bufferSize);
    QueueSidebandConnection(sideband_strategy, identifier, true, true, bufferSize);

    EndpointList writers;
    EndpointList readers;
    InitiateMonikerList(request->monikers(), &readers, &writers);
    std::thread(RunSidebandReadWriteLoop, identifierString, sideband_strategy, std::move(readers), std::move(writers)).detach();

    return Status::OK;
  } catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
Status DataMonikerService::StreamReadWrite(ServerContext* context, ServerReaderWriter<MonikerReadResponse, MonikerWriteRequest>* stream)
{
  try {
#ifndef _WIN32
    set_cpu_affinity(s_StreamProcessor.moniker_stream_read_write);
#endif

    EndpointList writers;
    EndpointList readers;
    MonikerWriteRequest writeRequest;
    stream->Read(&writeRequest);
    InitiateMonikerList(writeRequest.monikers(), &readers, &writers);

    google::protobuf::Arena arena;
    while (stream->Read(&writeRequest) && !context->IsCancelled()) {
      // CWE-125: Validate value count matches writer count before accessing by index.
      if (writers.size() != static_cast<size_t>(writeRequest.data().values_size())) {
        return Status(grpc::INVALID_ARGUMENT, "Value count does not match writer count");
      }
      int x = 0;
      for (auto writer : writers) {
        std::get<0>(writer)(std::get<1>(writer), arena, const_cast<google::protobuf::Any&>(writeRequest.data().values(x++)));
      }

      MonikerReadResponse readResult;
      for (auto reader : readers) {
        auto readValue = readResult.mutable_data()->add_values();
        std::get<0>(reader)(std::get<1>(reader), arena, *readValue);
      }
      stream->Write(readResult);
      arena.Reset();
    }
    return Status::OK;
  } catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
Status DataMonikerService::StreamRead(ServerContext* context, const MonikerList* request, ServerWriter<MonikerReadResponse>* writer)
{
  try {
#ifndef _WIN32
    set_cpu_affinity(s_StreamProcessor.moniker_stream_read);
#endif

    EndpointList writers;
    EndpointList readers;
    InitiateMonikerList(*request, &readers, &writers);

    google::protobuf::Arena arena;
    while (!context->IsCancelled()) {
      MonikerReadResponse readResult;
      for (auto reader : readers) {
        auto readValue = readResult.mutable_data()->add_values();
        std::get<0>(reader)(std::get<1>(reader), arena, *readValue);
      }
      writer->Write(readResult);
      arena.Reset();
    }
    return Status::OK;
  } catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
Status DataMonikerService::StreamWrite(ServerContext* context, ServerReaderWriter<StreamWriteResponse, MonikerWriteRequest>* stream)
{
  try {
#ifndef _WIN32
    set_cpu_affinity(s_StreamProcessor.moniker_stream_write);
#endif

    EndpointList writers;
    EndpointList readers;
    MonikerWriteRequest writeRequest;
    stream->Read(&writeRequest);
    InitiateMonikerList(writeRequest.monikers(), &readers, &writers);

    int x = 0;
    google::protobuf::Arena arena;
    while (stream->Read(&writeRequest) && !context->IsCancelled()) {
      // CWE-125: Validate value count matches writer count before accessing by index.
      if (writers.size() != static_cast<size_t>(writeRequest.data().values_size())) {
        return Status(grpc::INVALID_ARGUMENT, "Value count does not match writer count");
      }

      x = 0;
      for (auto writer : writers) {
        std::get<0>(writer)(std::get<1>(writer), arena, const_cast<google::protobuf::Any&>(writeRequest.data().values(x++)));
      }
      arena.Reset();
    }
    return Status::OK;
  } catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}
}  // namespace ni::data_monikers
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/data_moniker_service.h sha256=ddb4e917764264e88b8293b4565208873604dc464c9917b457abb44757632e07 bytes=3472 -->
## FILE: source/server/data_moniker_service.h

- repository: `ni/grpc-device`
- source_path: `source/server/data_moniker_service.h`
- sha256: `ddb4e917764264e88b8293b4565208873604dc464c9917b457abb44757632e07`
- bytes: 3472

````c
//---------------------------------------------------------------------
// Implementation of NI Data Moniker Service
//---------------------------------------------------------------------
#pragma once

//---------------------------------------------------------------------
//---------------------------------------------------------------------
#include <grpcpp/grpcpp.h>
#include <data_moniker.grpc.pb.h>
#include <type_traits>
#include <map>
#include <mutex>
#include <random>
#include <sideband_data.h>
#include "feature_toggles.h"
#include "moniker_stream_processor.h"

//---------------------------------------------------------------------
//---------------------------------------------------------------------
namespace ni::data_monikers
{
    void configure_moniker_stream_processor(const MonikerStreamProcessor& stream_processor);
    bool is_moniker_streaming_enabled(const nidevice_grpc::FeatureToggles& feature_toggles);
    bool is_moniker_streaming_sideband_support_enabled(const nidevice_grpc::FeatureToggles& feature_toggles);
    void set_cpu_affinity(int cpu);
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    using MonikerEndpointPtr = std::add_pointer<::grpc::Status(void*, google::protobuf::Arena& arena, google::protobuf::Any&)>::type;
    using EndpointInstance = std::tuple<MonikerEndpointPtr, void*>;
    using EndpointList = std::vector<EndpointInstance>;

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    class DataMonikerService final : public DataMoniker::Service
    {
    public:
        DataMonikerService();
        ::grpc::Status BeginSidebandStream(grpc::ServerContext* context, const ni::data_monikers::BeginMonikerSidebandStreamRequest* request, ni::data_monikers::BeginMonikerSidebandStreamResponse* response) override;
        ::grpc::Status StreamReadWrite(::grpc::ServerContext* context, ::grpc::ServerReaderWriter<MonikerReadResponse, MonikerWriteRequest>* stream) override;
        ::grpc::Status StreamRead(::grpc::ServerContext* context, const MonikerList* request, ::grpc::ServerWriter<MonikerReadResponse>* writer);
        ::grpc::Status StreamWrite(::grpc::ServerContext* context, ::grpc::ServerReaderWriter<StreamWriteResponse, MonikerWriteRequest>* stream);

    public:
        static void RegisterMonikerEndpoint(std::string endpointName, MonikerEndpointPtr endpoint);
        static void RegisterMonikerInstance(std::string endpointName, void* instanceData, Moniker& moniker);

        // CWE-822: Opaque handle registry — maps server-generated handles to instance
        // pointers so that raw pointers are never exposed over gRPC.
        static void* LookupInstance(int64_t handle);

    private:
        static DataMonikerService* s_Server;
        std::map<std::string, MonikerEndpointPtr> _endpoints;

        std::mutex instance_mutex_;
        std::mt19937_64 rng_{std::random_device{}()};
        std::map<int64_t, void*> instance_registry_;

    private:
        void InitiateMonikerList(const MonikerList& monikers, EndpointList* readers, EndpointList* writers);
        static void RunSidebandReadWriteLoop(std::string sidebandIdentifier, ::SidebandStrategy strategy, EndpointList readers, EndpointList writers);
    };
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/debug_session_properties_restricted_service.cpp sha256=18cbb3b795f29b0842ef9b095dbbbf58359ccdaeef51b4465329d839fb0d79e0 bytes=5275 -->
## FILE: source/server/debug_session_properties_restricted_service.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/debug_session_properties_restricted_service.cpp`
- sha256: `18cbb3b795f29b0842ef9b095dbbbf58359ccdaeef51b4465329d839fb0d79e0`
- bytes: 5275

````cpp
#include "debug_session_properties_restricted_service.h"

#include "converters.h"

namespace nidevice_restricted_grpc {

DebugSessionPropertiesRestrictedFeatureToggles::DebugSessionPropertiesRestrictedFeatureToggles(
  const nidevice_grpc::FeatureToggles& feature_toggles)
  : is_enabled(
      feature_toggles.is_feature_enabled("debugsessionproperties_restricted", CodeReadiness::kRelease))
{
}

DebugSessionPropertiesRestrictedService::DebugSessionPropertiesRestrictedService(::nidevice_grpc::SysCfgLibraryInterface* library)
    : SysCfgResourceAccessor(library)
{
}

::grpc::Status DebugSessionPropertiesRestrictedService::IsDebugSessionSupported(
  ::grpc::ServerContext* context,
  const IsDebugSessionSupportedRequest* request,
  IsDebugSessionSupportedResponse* response)
{
  bool supported = false;
  auto status = get_bool_property(context, kDebugSessionSupportedPropertyId, request->device_id(), &supported);
  response->set_supported(supported);
  return status;
}

::grpc::Status DebugSessionPropertiesRestrictedService::IsDebugSessionEnabled(
  ::grpc::ServerContext* context,
  const IsDebugSessionEnabledRequest* request,
  IsDebugSessionEnabledResponse* response)
{
  uint32_t enabled = false;
  auto status = get_uint_property(context, kDebugSessionEnabledPropertyId, request->device_id(), &enabled);
  response->set_enabled(enabled != 0);
  return status;
}

::grpc::Status DebugSessionPropertiesRestrictedService::IsDebugSessionServerOutOfProcess(
  ::grpc::ServerContext* context,
  const IsDebugSessionServerOutOfProcessRequest* request,
  IsDebugSessionServerOutOfProcessResponse* response)
{
  bool out_of_process = false;
  auto status = get_bool_property(context, kDebugSessionServerOutOfProcessPropertyId, request->device_id(), &out_of_process);
  response->set_out_of_process(out_of_process);
  return status;
}

::grpc::Status DebugSessionPropertiesRestrictedService::SetDebugSessionEnabled(
  ::grpc::ServerContext* context,
  const SetDebugSessionEnabledRequest* request,
  SetDebugSessionEnabledResponse* response)
{
  uint32_t enabled = request->enabled() ? 1 : 0;
  return set_uint_property(context, kDebugSessionEnabledPropertyId, request->device_id(), enabled);
}

::grpc::Status DebugSessionPropertiesRestrictedService::SetDebugSessionServerOutOfProcess(
  ::grpc::ServerContext* context,
  const SetDebugSessionServerOutOfProcessRequest* request,
  SetDebugSessionServerOutOfProcessResponse* response)
{
  return set_bool_property(context, kDebugSessionServerOutOfProcessPropertyId, request->device_id(), request->out_of_process());
}

::grpc::Status DebugSessionPropertiesRestrictedService::get_bool_property(
  ::grpc::ServerContext* context,
  NISysCfgResourceProperty property_id,
  const nidevice_restricted_grpc::DeviceId& device_id,
  bool* value)
{
  auto get_bool_lambda = [&] (nidevice_grpc::SysCfgLibraryInterface* library, NISysCfgResourceHandle resource, bool* save_changes) {
    NISysCfgBool syscfg_value = NISysCfgBoolFalse;
    auto status = library->GetResourceProperty(resource, property_id, &syscfg_value);
    *value = syscfg_value != NISysCfgBoolFalse;
    return status;
  };
  return access_syscfg_resource_by_device_id_filter(context, device_id, kDebugSessionPropertyAccessFailedMessage, get_bool_lambda);
}

::grpc::Status DebugSessionPropertiesRestrictedService::get_uint_property(
  ::grpc::ServerContext* context,
  NISysCfgResourceProperty property_id,
  const nidevice_restricted_grpc::DeviceId& device_id,
  uint32_t* value)
{
  auto get_uint_lambda = [&] (nidevice_grpc::SysCfgLibraryInterface* library, NISysCfgResourceHandle resource, bool* save_changes) {
      return library->GetResourceProperty(resource, property_id, value);
  };
  return access_syscfg_resource_by_device_id_filter(context, device_id, kDebugSessionPropertyAccessFailedMessage, get_uint_lambda);
}

::grpc::Status DebugSessionPropertiesRestrictedService::set_bool_property(
  ::grpc::ServerContext* context,
  NISysCfgResourceProperty property_id,
  const nidevice_restricted_grpc::DeviceId& device_id,
  bool value)
{
  NISysCfgBool syscfg_value = value ? NISysCfgBoolTrue : NISysCfgBoolFalse;
  auto set_bool_lambda = [&] (nidevice_grpc::SysCfgLibraryInterface* library, NISysCfgResourceHandle resource, bool* save_changes) {
    *save_changes = true;
    return library->SetResourceProperty(resource, property_id, syscfg_value);
  };
  return access_syscfg_resource_by_device_id_filter(context, device_id, kDebugSessionPropertyAccessFailedMessage, set_bool_lambda);
}

::grpc::Status DebugSessionPropertiesRestrictedService::set_uint_property(
  ::grpc::ServerContext* context,
  NISysCfgResourceProperty property_id,
  const nidevice_restricted_grpc::DeviceId& device_id,
  uint32_t value)
{
  auto set_uint_lambda = [&] (nidevice_grpc::SysCfgLibraryInterface* library, NISysCfgResourceHandle resource, bool* save_changes) {
    *save_changes = true;
    return library->SetResourceProperty(resource, property_id, value);
  };
  return access_syscfg_resource_by_device_id_filter(context, device_id, kDebugSessionPropertyAccessFailedMessage, set_uint_lambda);
}

}  // namespace nidevice_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/debug_session_properties_restricted_service.h sha256=e0c1928edc16c062c130cfa402eae237e6364830b6589cbac89189b9047d034e bytes=3431 -->
## FILE: source/server/debug_session_properties_restricted_service.h

- repository: `ni/grpc-device`
- source_path: `source/server/debug_session_properties_restricted_service.h`
- sha256: `e0c1928edc16c062c130cfa402eae237e6364830b6589cbac89189b9047d034e`
- bytes: 3431

````c
#ifndef NIDEVICE_RESTRICTED_GRPC_DEBUG_SESSION_PROPERTIES_RESTRICTED_SERVICE
#define NIDEVICE_RESTRICTED_GRPC_DEBUG_SESSION_PROPERTIES_RESTRICTED_SERVICE

#include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>
#include <debugsessionproperties_restricted.grpc.pb.h>

#include "feature_toggles.h"
#include "shared_library.h"
#include "syscfg_library_interface.h"
#include "syscfg_resource_accessor.h"

namespace nidevice_restricted_grpc {

static const char* kDebugSessionPropertyAccessFailedMessage = "The NI System Configuration API was unable to access the debug session property.";
static const auto kDebugSessionSupportedPropertyId = (NISysCfgResourceProperty)0x10001000;
static const auto kDebugSessionEnabledPropertyId = (NISysCfgResourceProperty)0x10002000;
static const auto kDebugSessionServerOutOfProcessPropertyId = (NISysCfgResourceProperty)0x10003000;

struct DebugSessionPropertiesRestrictedFeatureToggles
{
  using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;
  DebugSessionPropertiesRestrictedFeatureToggles(const nidevice_grpc::FeatureToggles& feature_toggles = {});

  bool is_enabled;
};

class DebugSessionPropertiesRestrictedService final :
  public DebugSessionPropertiesRestricted::Service,
  public ::nidevice_restricted_grpc::SysCfgResourceAccessor {
 public:
  DebugSessionPropertiesRestrictedService(::nidevice_grpc::SysCfgLibraryInterface* library);

  ::grpc::Status IsDebugSessionSupported(
    ::grpc::ServerContext* context,
    const IsDebugSessionSupportedRequest* request,
    IsDebugSessionSupportedResponse* response) override;
  ::grpc::Status IsDebugSessionEnabled(
    ::grpc::ServerContext* context,
    const IsDebugSessionEnabledRequest* request,
    IsDebugSessionEnabledResponse* response) override;
  ::grpc::Status IsDebugSessionServerOutOfProcess(
    ::grpc::ServerContext* context,
    const IsDebugSessionServerOutOfProcessRequest* request,
    IsDebugSessionServerOutOfProcessResponse* response) override;
  ::grpc::Status SetDebugSessionEnabled(
    ::grpc::ServerContext* context,
    const SetDebugSessionEnabledRequest* request,
    SetDebugSessionEnabledResponse* response) override;
  ::grpc::Status SetDebugSessionServerOutOfProcess(
    ::grpc::ServerContext* context,
    const SetDebugSessionServerOutOfProcessRequest* request,
    SetDebugSessionServerOutOfProcessResponse* response) override;

 private:
  ::grpc::Status get_bool_property(
    ::grpc::ServerContext* context,
    NISysCfgResourceProperty property_id,
    const nidevice_restricted_grpc::DeviceId& device_id,
    bool* value);
  ::grpc::Status get_uint_property(
    ::grpc::ServerContext* context,
    NISysCfgResourceProperty property_id,
    const nidevice_restricted_grpc::DeviceId& device_id,
    uint32_t* value);
  ::grpc::Status set_bool_property(
    ::grpc::ServerContext* context,
    NISysCfgResourceProperty property_id,
    const nidevice_restricted_grpc::DeviceId& device_id,
    bool value);
  ::grpc::Status set_uint_property(
    ::grpc::ServerContext* context,
    NISysCfgResourceProperty property_id,
    const nidevice_restricted_grpc::DeviceId& device_id,
    uint32_t value);
};

}  // namespace nidevice_restricted_grpc

#endif  // NIDEVICE_RESTRICTED_GRPC_DEBUG_SESSION_PROPERTIES_RESTRICTED_SERVICE
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/debug_session_properties_restricted_service_registrar.cpp sha256=8075a6940dfa4eff4928657a4b7ac543e95ff4454ac42843b7bbf7c2b637217c bytes=1772 -->
## FILE: source/server/debug_session_properties_restricted_service_registrar.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/debug_session_properties_restricted_service_registrar.cpp`
- sha256: `8075a6940dfa4eff4928657a4b7ac543e95ff4454ac42843b7bbf7c2b637217c`
- bytes: 1772

````cpp
#include "debug_session_properties_restricted_service_registrar.h"

#include "debug_session_properties_restricted_service.h"
#include "syscfg_library.h"

namespace nidevice_restricted_grpc {
namespace {
struct DebugSessionPropertiesRestrictedLibraryAndService {
  DebugSessionPropertiesRestrictedLibraryAndService(
    nidevice_grpc::ServerResetObserverRegistrarInterface& serverResetObserverRegistrar)
      : library(),
        service(&library),
        observerRegistrar(&serverResetObserverRegistrar)
  {
    observerRegistrar->register_observer(&service);
  }

  ~DebugSessionPropertiesRestrictedLibraryAndService()
  {
    // This code is currently unreachable, but if the call to wait exits, we need to clean up the service here.
    observerRegistrar->unregister_observer(&service);
    service.clear_syscfg_session();
  }

  ::nidevice_grpc::SysCfgLibrary library;
  DebugSessionPropertiesRestrictedService service;
  nidevice_grpc::ServerResetObserverRegistrarInterface* observerRegistrar;
};
}  // namespace

std::shared_ptr<void> register_debug_session_properties_restricted_service(
  grpc::ServerBuilder& server_builder,
  const nidevice_grpc::FeatureToggles& feature_toggles,
  nidevice_grpc::ServerResetObserverRegistrarInterface& serverResetObserverRegistrar)
{
  auto toggles = DebugSessionPropertiesRestrictedFeatureToggles(feature_toggles);

  if (toggles.is_enabled)
  {
    auto library_and_service_ptr = std::make_shared<DebugSessionPropertiesRestrictedLibraryAndService>(serverResetObserverRegistrar);
    auto& service = library_and_service_ptr->service;
    server_builder.RegisterService(&service);
    return library_and_service_ptr;
  }

  return {};
}
}  // namespace nidevice_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/debug_session_properties_restricted_service_registrar.h sha256=759415cb35c4e34d109a0b8580f0dce043595c4dc70475a2c82f654c3f8eb5ae bytes=823 -->
## FILE: source/server/debug_session_properties_restricted_service_registrar.h

- repository: `ni/grpc-device`
- source_path: `source/server/debug_session_properties_restricted_service_registrar.h`
- sha256: `759415cb35c4e34d109a0b8580f0dce043595c4dc70475a2c82f654c3f8eb5ae`
- bytes: 823

````c
#ifndef NIDEVICE_GRPC_DEVICE_RESTRICTED_DEBUG_SESSION_PROPERTIES_SERVICE_REGISTRAR_H
#define NIDEVICE_GRPC_DEVICE_RESTRICTED_DEBUG_SESSION_PROPERTIES_SERVICE_REGISTRAR_H

#include <memory>

#include "feature_toggles.h"
#include "server_reset_observer_registrar_interface.h"

namespace grpc {
class ServerBuilder;
}

namespace nidevice_restricted_grpc {
using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;

std::shared_ptr<void> register_debug_session_properties_restricted_service(
  grpc::ServerBuilder& server_builder,
  const nidevice_grpc::FeatureToggles& feature_toggles,
  nidevice_grpc::ServerResetObserverRegistrarInterface& serverResetObserverRegistrar);

} // nidevice_restricted_grpc

#endif  // NIDEVICE_GRPC_DEVICE_RESTRICTED_DEBUG_SESSION_PROPERTIES_SERVICE_REGISTRAR_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/device_enumerator.cpp sha256=da5f1be2c252d7908d9574c471518ef2f3b9be433f7a253474513901cf4e12f5 bytes=3753 -->
## FILE: source/server/device_enumerator.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/device_enumerator.cpp`
- sha256: `da5f1be2c252d7908d9574c471518ef2f3b9be433f7a253474513901cf4e12f5`
- bytes: 3753

````cpp
#include "device_enumerator.h"

namespace nidevice_grpc {

DeviceEnumerator::DeviceEnumerator(SysCfgLibraryInterface* library)
    : SysCfgSessionHandler(library)
{
}

DeviceEnumerator::~DeviceEnumerator()
{
}

// Provides a list of devices or chassis connected to server under localhost. This internally uses the
// "NI System Configuration API". If it is not currently installed, it can be downloaded from this page:
// https://www.ni.com/en-in/support/downloads/drivers/download.system-configuration.html.
::grpc::Status DeviceEnumerator::enumerate_devices(google::protobuf::RepeatedPtrField<DeviceProperties>* devices)
{
  NISysCfgStatus status = NISysCfg_OK;
  NISysCfgSessionHandle session = NULL;
  NISysCfgFilterHandle filter = NULL;
  NISysCfgEnumResourceHandle resources_handle = NULL;
  NISysCfgResourceHandle resource = NULL;
  char expert_name[NISYSCFG_SIMPLE_STRING_LENGTH] = "";
  char name[NISYSCFG_SIMPLE_STRING_LENGTH] = "";
  char model[NISYSCFG_SIMPLE_STRING_LENGTH] = "";
  char vendor[NISYSCFG_SIMPLE_STRING_LENGTH] = "";
  char serial_number[NISYSCFG_SIMPLE_STRING_LENGTH] = "";
  uint32_t product_id = 0;
  NISysCfgBool is_ni_product = NISysCfgBoolFalse;

  try {
    auto library = get_syscfg_library_interface();
    if (NISysCfg_Succeeded(status = open_or_get_localhost_syscfg_session(&session))) {
      if (NISysCfg_Succeeded(status = library->CreateFilter(session, &filter))) {
        library->SetFilterProperty(filter, NISysCfgFilterPropertyIsDevice, NISysCfgBoolTrue);
        library->SetFilterProperty(filter, NISysCfgFilterPropertyIsChassis, NISysCfgBoolTrue);
        if (NISysCfg_Succeeded(status = library->FindHardware(session, NISysCfgFilterModeMatchValuesAny, filter, NULL, &resources_handle))) {
          while (NISysCfg_Succeeded(status) && (status = library->NextResource(session, resources_handle, &resource)) == NISysCfg_OK) {
            library->GetResourceProperty(resource, NISysCfgResourcePropertyIsNIProduct, &is_ni_product);
            library->GetResourceIndexedProperty(resource, NISysCfgIndexedPropertyExpertName, 0, expert_name);
            if (is_ni_product && strcmp(expert_name, kNetworkExpertName) != 0) {
              DeviceProperties* properties = devices->Add();
              // Note that we don't check for status of GetResourceIndexedProperty and GetResourceProperty APIs because
              // we want to return empty string when any of the property does not exist for any resource.
              library->GetResourceIndexedProperty(resource, NISysCfgIndexedPropertyExpertUserAlias, 0, name);
              library->GetResourceProperty(resource, NISysCfgResourcePropertyProductName, model);
              library->GetResourceProperty(resource, NISysCfgResourcePropertyVendorName, vendor);
              library->GetResourceProperty(resource, NISysCfgResourcePropertySerialNumber, serial_number);
              library->GetResourceProperty(resource, NISysCfgResourcePropertyProductId, &product_id);
              properties->set_name(name);
              properties->set_model(model);
              properties->set_vendor(vendor);
              properties->set_serial_number(serial_number);
              properties->set_product_id(product_id);
            }
            library->CloseHandle(resource);
          }
          library->CloseHandle(resources_handle);
        }
        library->CloseHandle(filter);
      }
    }
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }

  if (NISysCfg_Failed(status)) {
    return ::grpc::Status(::grpc::StatusCode::INTERNAL, kDeviceEnumerationFailedMessage);
  }

  return ::grpc::Status::OK;
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/device_enumerator.h sha256=7273e96a3497b04d017620e494eccb20c369b3034c89fb776321ad7f0a852ec4 bytes=810 -->
## FILE: source/server/device_enumerator.h

- repository: `ni/grpc-device`
- source_path: `source/server/device_enumerator.h`
- sha256: `7273e96a3497b04d017620e494eccb20c369b3034c89fb776321ad7f0a852ec4`
- bytes: 810

````c
#ifndef NIDEVICE_GRPC_DEVICE_ENUMERATOR_H
#define NIDEVICE_GRPC_DEVICE_ENUMERATOR_H

#include <grpcpp/grpcpp.h>
#include <nisyscfg.h>
#include <session.grpc.pb.h>
#include <session_utilities.grpc.pb.h>
#include <shared_mutex>

#include "syscfg_library_interface.h"
#include "syscfg_session_handler.h"

namespace nidevice_grpc {

static const char* kDeviceEnumerationFailedMessage = "The NI System Configuration API was unable to enumerate the devices.";

class DeviceEnumerator : public SysCfgSessionHandler {
 public:
  DeviceEnumerator(SysCfgLibraryInterface* library);
  virtual ~DeviceEnumerator();

  ::grpc::Status enumerate_devices(google::protobuf::RepeatedPtrField<DeviceProperties>* devices);
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_DEVICE_ENUMERATOR_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/exceptions.h sha256=d225437e62f2ee54fbbb6ba80c7dc79ab3ab9cdb219381ba85a3010b331744ff bytes=1144 -->
## FILE: source/server/exceptions.h

- repository: `ni/grpc-device`
- source_path: `source/server/exceptions.h`
- sha256: `d225437e62f2ee54fbbb6ba80c7dc79ab3ab9cdb219381ba85a3010b331744ff`
- bytes: 1144

````c
#ifndef NIDEVICE_GRPC_EXCEPTIONS
#define NIDEVICE_GRPC_EXCEPTIONS

#include <grpcpp/grpcpp.h>

#include <stdexcept>

namespace nidevice_grpc {

class NonDriverException : public std::runtime_error {
 public:
  NonDriverException(::grpc::StatusCode code, const std::string& message) : std::runtime_error(message), code_(code) {}
  NonDriverException(::grpc::StatusCode code, const char* message) : std::runtime_error(message), code_(code) {}
  NonDriverException(const NonDriverException& other) : std::runtime_error(other), code_(other.code_) {}

  ::grpc::Status GetStatus() const { return ::grpc::Status(code_, what()); }

 private:
  ::grpc::StatusCode code_;
};

class ValueOutOfRangeException : public NonDriverException {
 public:
  ValueOutOfRangeException(const char* message) : NonDriverException(::grpc::StatusCode::OUT_OF_RANGE, message) {}
  ValueOutOfRangeException(const std::string& message) : NonDriverException(::grpc::StatusCode::OUT_OF_RANGE, message) {}
  ValueOutOfRangeException(const ValueOutOfRangeException& other) : NonDriverException(other) {}
};

}  // namespace nidevice_grpc

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/feature_toggles.cpp sha256=6ff48a401b52b06150eb49e712ba1c84f8c4a05307b712545a1698a73dcd587a bytes=761 -->
## FILE: source/server/feature_toggles.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/feature_toggles.cpp`
- sha256: `6ff48a401b52b06150eb49e712ba1c84f8c4a05307b712545a1698a73dcd587a`
- bytes: 761

````cpp
#include "feature_toggles.h"

namespace nidevice_grpc {
FeatureToggles::FeatureState FeatureToggles::get_feature_state(const std::string& feature_name) const
{
  auto found = map_.find(feature_name);
  if (found != map_.end()) {
    return found->second 
    ? FeatureState::kEnabled 
    : FeatureState::kDisabled;
  }
  return FeatureState::kUnspecified;
}

bool FeatureToggles::is_feature_enabled(
    const std::string& feature_name,
    FeatureToggles::CodeReadiness feature_readiness) const
{
  auto toggle_state = get_feature_state(feature_name);
  if (feature_readiness >= app_readiness_) {
    return toggle_state != FeatureState::kDisabled;
  }
  return toggle_state == FeatureState::kEnabled;
}
}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/feature_toggles.h sha256=b15adba0666281a23e4663f15c8a45f343aaafdb0983e62264d10ed1c295c35a bytes=1055 -->
## FILE: source/server/feature_toggles.h

- repository: `ni/grpc-device`
- source_path: `source/server/feature_toggles.h`
- sha256: `b15adba0666281a23e4663f15c8a45f343aaafdb0983e62264d10ed1c295c35a`
- bytes: 1055

````c
#ifndef NIDEVICE_GRPC_FEATURE_TOGGLES_H
#define NIDEVICE_GRPC_FEATURE_TOGGLES_H

#include <string>
#include <unordered_map>
namespace nidevice_grpc {

using FeatureToggleConfigurationMap = std::unordered_map<std::string, bool>;
class FeatureToggles {
 public:
  enum class FeatureState {
    kDisabled,
    kEnabled,
    kUnspecified
  };
  enum class CodeReadiness {
    kPrototype = 0,
    kIncomplete = 1,
    kNextRelease = 2,
    kRelease = 3,
  };

  FeatureToggles() {}
  FeatureToggles(FeatureToggleConfigurationMap&& map, CodeReadiness app_readiness = CodeReadiness::kRelease)
      : map_(map),
        app_readiness_(app_readiness) {}
  FeatureState get_feature_state(const std::string& feature_name) const;
  bool is_feature_enabled(
      const std::string& feature_name,
      CodeReadiness feature_readiness) const;

 private:
  FeatureToggleConfigurationMap map_;
  CodeReadiness app_readiness_ = CodeReadiness::kRelease;
};
}  // namespace nidevice_grpc

#endif /* NIDEVICE_GRPC_FEATURE_TOGGLES_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/linux/daemonize.cpp sha256=7b3aa6382f9552e70701d002ef4e7380401207b38cc43b8618518bd430946525 bytes=5234 -->
## FILE: source/server/linux/daemonize.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/linux/daemonize.cpp`
- sha256: `7b3aa6382f9552e70701d002ef4e7380401207b38cc43b8618518bd430946525`
- bytes: 5234

````cpp
#include "daemonize.h"

#include "../logging.h"

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <errno.h>
#include <fcntl.h>
#include <paths.h>
#include <signal.h>
#include <string>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

namespace nidevice_grpc {

static stop_callback signal_stop = NULL;
static std::string pid_path;
static int pid_fd = -1;

void catch_close(int sig) {
  const char* signal_description = "?";
  switch(sig)
  {
  case SIGINT:
    signal_description = "interrupt";
    break;
  case SIGTERM:
    signal_description = "terminate";
    break;
  case SIGHUP:
    signal_description = "hangup";
    break;
  default:
    break;
  }

  logging::log(logging::Level_Info, "handling signal: %d (%s)", sig, signal_description);
  if (signal_stop) {
    signal_stop();
  }

  if (close(pid_fd) < 0) {
    logging::log(logging::Level_Warning, "failed to close pid file: %d (%s)", errno, strerror(errno));
  }
  if (unlink(pid_path.c_str()) < 0) {
    logging::log(logging::Level_Warning, "failed to unlink pid file: %d (%s)", errno, strerror(errno));
  }
  exit(EXIT_SUCCESS);
}

int create_pidfile(const std::string& identity) {
  int size = snprintf(NULL, 0, _PATH_VARRUN "%s.pid", identity.c_str());
  pid_path.resize(size, ' ');
  if (snprintf(&pid_path[0], size + 1, _PATH_VARRUN "%s.pid", identity.c_str()) > size) {
    logging::log(logging::Level_Error, "creating pid path failed");
    exit(EXIT_FAILURE);
  }

  size = snprintf(NULL, 0, "%d\n", getpid());
  std::string pid_str(size, ' ');
  if (snprintf(&pid_str[0], size + 1, "%d\n", getpid()) > size) {
    logging::log(logging::Level_Error, "creating pid string failed");
    exit(EXIT_FAILURE);
  }

  int fd = open(pid_path.c_str(), O_RDWR|O_CREAT, 0644);
  if (fd < 0) {
    logging::log(logging::Level_Error, "creating pid file failed: %d (%s)", errno, strerror(errno));
    exit(EXIT_FAILURE);
  }
  if (lockf(fd, F_TLOCK, 0) < 0) {
    logging::log(logging::Level_Error, "locking pid file failed (likely already running): %d (%s)", errno, strerror(errno));
    close(fd);
    exit(EXIT_FAILURE);
  }
  if (write(fd, pid_str.c_str(), size) != static_cast<ssize_t>(pid_str.length())) {
    logging::log(logging::Level_Error, "writing pid file failed: %d (%s)", errno, strerror(errno));
    close(fd);
    exit(EXIT_FAILURE);
  }
  if (ftruncate(fd, size) < 0) {
    logging::log(logging::Level_Error, "truncating pid file failed: %d (%s)", errno, strerror(errno));
    close(fd);
    exit(EXIT_FAILURE);
  }
  return fd;
}

void daemonize(stop_callback signal_stop_, const std::string& identity) {
  // Fork off the parent process to get into the background
  pid_t pid = fork();
  if (pid < 0) {
    logging::log(logging::Level_Error, "initial fork failed: %d (%s)", errno, strerror(errno));
    exit(EXIT_FAILURE);
  }

  // Success: Let the parent terminate
  if (pid > 0) {
    exit(EXIT_SUCCESS);
  }

  // The child process becomes session leader to detach from the terminal
  if (setsid() < 0) {
    logging::log(logging::Level_Error, "setsid failed: %d (%s)", errno, strerror(errno));
    exit(EXIT_FAILURE);
  }

  // Fork off for the second time to get rid of the session leader
  pid = fork();
  if (pid < 0) {
    logging::log(logging::Level_Error, "second fork failed: %d (%s)", errno, strerror(errno));
    exit(EXIT_FAILURE);
  }

  // Success: Let the parent terminate
  if (pid > 0) {
    exit(EXIT_SUCCESS);
  }

  // Clear umask to give daemon complete control of file permissions
  umask(0);

  // Change the working directory to the root directory
  if (chdir("/") < 0) {
    logging::log(logging::Level_Error, "chdir failed: %d (%s)", errno, strerror(errno));
    exit(EXIT_FAILURE);
  }

  // Close all open file descriptors
  for (int x = sysconf(_SC_OPEN_MAX); x >= 0; x--) {
    close(x);
  }

  // Redirect standard files to /dev/null
  if (freopen("/dev/null", "r", stdin) == NULL) {
    logging::log(logging::Level_Error, "redirecting stdin to /dev/null: %d (%s)", errno, strerror(errno));
  }
  if (freopen("/dev/null", "w", stdout) == NULL) {
    logging::log(logging::Level_Error, "redirecting stdout to /dev/null: %d (%s)", errno, strerror(errno));
  }
  if (freopen("/dev/null", "w", stderr) == NULL) {
    logging::log(logging::Level_Error, "redirecting stderr to /dev/null: %d (%s)", errno, strerror(errno));
  }

  // We're fully operational, catch signals.
  signal_stop = signal_stop_;
  if (signal(SIGINT, catch_close) == SIG_ERR) {
    logging::log(logging::Level_Error, "failed to register SIGINT: %d (%s)", errno, strerror(errno));
  }
  if (signal(SIGTERM, catch_close) == SIG_ERR) {
    logging::log(logging::Level_Error, "failed to register SIGTERM: %d (%s)", errno, strerror(errno));
  }
  if (signal(SIGHUP, catch_close) == SIG_ERR) {
    logging::log(logging::Level_Error, "failed to register SIGHUP: %d (%s)", errno, strerror(errno));
  }

  // Now that we're fully daemonized, write our PID file and ensure we're the only daemon.
  pid_fd = create_pidfile(identity);
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/linux/daemonize.h sha256=0eb2bd157a49e1249940031793cdbd4d97411dea16f299af7512816007c73da1 bytes=317 -->
## FILE: source/server/linux/daemonize.h

- repository: `ni/grpc-device`
- source_path: `source/server/linux/daemonize.h`
- sha256: `0eb2bd157a49e1249940031793cdbd4d97411dea16f299af7512816007c73da1`
- bytes: 317

````c
#ifndef NIDEVICE_GRPC_LINUX_DAEMONIZE_H
#define NIDEVICE_GRPC_LINUX_DAEMONIZE_H

#include <string>

namespace nidevice_grpc {

typedef void (*stop_callback)();

void daemonize(stop_callback stop, const std::string& identity);

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_LINUX_DAEMONIZE_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/linux/syslog_logging.cpp sha256=9e62b678babab0bb18ccaf88a6b87f2ce2261875f42313274c1fe9a0791e6434 bytes=907 -->
## FILE: source/server/linux/syslog_logging.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/linux/syslog_logging.cpp`
- sha256: `9e62b678babab0bb18ccaf88a6b87f2ce2261875f42313274c1fe9a0791e6434`
- bytes: 907

````cpp
#include "syslog_logging.h"

#include <syslog.h>

namespace nidevice_grpc {
namespace logging {

void setup_syslog(bool is_daemon, const std::string& identity)
{
  int syslog_options = LOG_PID;
  int syslog_facility = 0;
  if (is_daemon) {
    syslog_facility = LOG_DAEMON;
  }
  else {
    // It's OK to fall back to the console if we're not a daemon.
    syslog_options |= LOG_CONS;
    syslog_facility |= LOG_USER;
  }
  openlog(identity.c_str(), syslog_options, syslog_facility);
}

void log_syslog(Level level, const char* fmt, va_list args)
{
  int priority;
  switch (level) {
    case Level_Info:
      priority = LOG_INFO;
      break;
    case Level_Warning:
      priority = LOG_WARNING;
      break;
    case Level_Error:
      priority = LOG_ERR;
      break;
  }
  vsyslog(priority, fmt, args);
}

}  // namespace logging
}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/linux/syslog_logging.h sha256=1712af3003f7a7dbb0bb5b083a1659a86440faae76112a2bb35c35397e8e9735 bytes=428 -->
## FILE: source/server/linux/syslog_logging.h

- repository: `ni/grpc-device`
- source_path: `source/server/linux/syslog_logging.h`
- sha256: `1712af3003f7a7dbb0bb5b083a1659a86440faae76112a2bb35c35397e8e9735`
- bytes: 428

````c
#ifndef NIDEVICE_GRPC_LINUX_SYSLOG_LOGGING_H
#define NIDEVICE_GRPC_LINUX_SYSLOG_LOGGING_H

#include <string>

#include "../logging.h"

namespace nidevice_grpc {
namespace logging {

void setup_syslog(bool is_daemon, const std::string& identity);
void log_syslog(Level level, const char* fmt, va_list args);

}  // namespace logging
}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_LINUX_SYSLOG_LOGGING_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/logging.cpp sha256=022d2068e9ad28aeb2afede0832b0491047cdaf2155e2d05bcd353b8693d67f4 bytes=777 -->
## FILE: source/server/logging.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/logging.cpp`
- sha256: `022d2068e9ad28aeb2afede0832b0491047cdaf2155e2d05bcd353b8693d67f4`
- bytes: 777

````cpp
#include "logging.h"

#include <cstdio>
#include <iostream>

namespace nidevice_grpc {
namespace logging {

void log_terminal(Level level, const char* fmt, va_list args)
{
  switch (level) {
    case Level_Info:
    // explicit fall-through
    case Level_Warning:
      vfprintf(stdout, fmt, args);
      std::cout << std::endl;
      break;
    case Level_Error:
      vfprintf(stderr, fmt, args);
      std::cerr << std::endl;
      break;
  }
}

static log_fn_impl logger = &log_terminal;

void set_logger(log_fn_impl impl)
{
  logger = impl;
}

void log(Level level, const char* fmt, ...)
{
  va_list args;
  va_start(args, fmt);
  logger(level, fmt, args);
  va_end(args);
}

}  // namespace logging
}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/logging.h sha256=de9ecd0437af24330137e0f6f3b17735bd0c8b6f759a332bfb13af4cc09eec80 bytes=527 -->
## FILE: source/server/logging.h

- repository: `ni/grpc-device`
- source_path: `source/server/logging.h`
- sha256: `de9ecd0437af24330137e0f6f3b17735bd0c8b6f759a332bfb13af4cc09eec80`
- bytes: 527

````c
#ifndef NIDEVICE_GRPC_LOGGING_H
#define NIDEVICE_GRPC_LOGGING_H

#include <cstdarg>

namespace nidevice_grpc {
namespace logging {

enum Level {
  Level_Info = 0,
  Level_Warning,
  Level_Error,
};

typedef void (*log_fn_impl)(Level level, const char* fmt, va_list args);

// The logger defaults to the terminal (stdout and stderr)
void set_logger(log_fn_impl impl);
void log(Level level, const char* fmt, ...);

}  // namespace logging
}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_LOGGING_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/mock_shared_library.h sha256=35e567ace1a15ce571ae6789bb8a7b7a934351b2617148652eb7d27e26796fd7 bytes=1266 -->
## FILE: source/server/mock_shared_library.h

- repository: `ni/grpc-device`
- source_path: `source/server/mock_shared_library.h`
- sha256: `35e567ace1a15ce571ae6789bb8a7b7a934351b2617148652eb7d27e26796fd7`
- bytes: 1266

````c
//---------------------------------------------------------------------
// Mock of SharedLibrary
//---------------------------------------------------------------------
#ifndef NIDEVICE_GRPC_MOCK_SHARED_LIBRARY_H
#define NIDEVICE_GRPC_MOCK_SHARED_LIBRARY_H

#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include <string>

#include "shared_library_interface.h"

namespace ni {
namespace tests {
namespace unit {

class MockSharedLibrary : public nidevice_grpc::SharedLibraryInterface {
 public:
  // MOCK_METHOD(void, swap, (nidevice_grpc::SharedLibraryInterface& other), ());
  MOCK_METHOD(bool, is_loaded, (), (const, override));
  MOCK_METHOD(nidevice_grpc::LibraryHandle, get_handle, (), (const, override));
  MOCK_METHOD(void, load, (), (override));
  MOCK_METHOD(void, unload, (), (override));
  MOCK_METHOD(const void*, get_function_pointer, (const char* name), (const, override));
  MOCK_METHOD(bool, function_exists, (const char* name), (const, override));
  MOCK_METHOD(void, set_library_name, (const char* library_name), (override));
  MOCK_METHOD(std::string, get_library_name, (), (const, override));
};

}  // namespace unit
}  // namespace tests
}  // namespace ni
#endif  // NIDEVICE_GRPC_MOCK_SHARED_LIBRARY_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/moniker_stream_processor.h sha256=d66c71ac09a580abe1992e2738adf13b2aa62cfc969cbee63c9a7f28392a20f2 bytes=313 -->
## FILE: source/server/moniker_stream_processor.h

- repository: `ni/grpc-device`
- source_path: `source/server/moniker_stream_processor.h`
- sha256: `d66c71ac09a580abe1992e2738adf13b2aa62cfc969cbee63c9a7f28392a20f2`
- bytes: 313

````c
#ifndef MONIKER_STREAM_PROCESSOR_H
#define MONIKER_STREAM_PROCESSOR_H

struct MonikerStreamProcessor {
    int moniker_sideband_stream_read_write = -1;
    int moniker_stream_write = -1;
    int moniker_stream_read = -1;
    int moniker_stream_read_write = -1;
};

#endif // Moniker_Stream_Processor_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/semaphore.cpp sha256=f84303caae245f40651c78a1ed2ecf08d0b5e8c45a0137c88cccc1a18160d8d6 bytes=594 -->
## FILE: source/server/semaphore.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/semaphore.cpp`
- sha256: `f84303caae245f40651c78a1ed2ecf08d0b5e8c45a0137c88cccc1a18160d8d6`
- bytes: 594

````cpp
#include "semaphore.h"

namespace nidevice_grpc {

Semaphore::Semaphore(int count)
    : count_(count), is_canceled_(false)
{
}

void Semaphore::notify()
{
  std::unique_lock<std::mutex> lock(mtx_);
  ++count_;
  cv_.notify_one();
}

void Semaphore::cancel()
{
  std::unique_lock<std::mutex> lock(mtx_);
  is_canceled_ = true;
  cv_.notify_all();
}

void Semaphore::wait()
{
  std::unique_lock<std::mutex> lock(mtx_);
  while (count_ == 0 && !is_canceled_) {
    cv_.wait(lock);
  }

  if (!is_canceled_) {
    count_--;
  }
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/semaphore.h sha256=a805d595acd8eee5eedb46f090a9e5b869dff66edc4201494636741436a988e8 bytes=448 -->
## FILE: source/server/semaphore.h

- repository: `ni/grpc-device`
- source_path: `source/server/semaphore.h`
- sha256: `a805d595acd8eee5eedb46f090a9e5b869dff66edc4201494636741436a988e8`
- bytes: 448

````c
#ifndef NIDEVICE_GRPC_SEMAPHORE_H
#define NIDEVICE_GRPC_SEMAPHORE_H

#include <shared_mutex>
#include <condition_variable>

namespace nidevice_grpc {

class Semaphore {
 public:
  Semaphore(int count = 1);
  void notify();
  void cancel();
  void wait();

 private:
  int count_;
  bool is_canceled_;
  std::mutex mtx_;
  std::condition_variable cv_;
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SEMAPHORE_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/server_configuration_parser.cpp sha256=70deee705c46b359b9c0f07a6d2151a342ca0fd241cf3d3cb52bdee98e2953c7 bytes=14249 -->
## FILE: source/server/server_configuration_parser.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/server_configuration_parser.cpp`
- sha256: `70deee705c46b359b9c0f07a6d2151a342ca0fd241cf3d3cb52bdee98e2953c7`
- bytes: 14249

````cpp
#include "server_configuration_parser.h"

#include <climits>
#include <iostream>
#include <sstream>

#include "feature_toggles.h"
#include "moniker_stream_processor.h"

#if defined(_MSC_VER)
  #include <windows.h>
#else
  #include <unistd.h>
#endif

namespace nidevice_grpc {

static const char* kDefaultFilename = "server_config.json";
static const char* kAddressJsonKey = "address";
static const char* kPortJsonKey = "port";
static const char* kSidebandAddressJsonKey = "sideband_address";
static const char* kSidebandPortJsonKey = "sideband_port";
static const char* kMonikerStreamProcessorKey = "moniker_stream_processor_configuration";
static const char* kMonikerSidebandStreamReadWriteKey = "moniker_sideband_stream_read_write";
static const char* kMonikerStreamWriteKey = "moniker_stream_write";
static const char* kMonikerStreamReadKey = "moniker_stream_read";
static const char* kMonikerStreamReadWriteKey = "moniker_stream_read_write";
static const char* kServerCertJsonKey = "server_cert";
static const char* kServerKeyJsonKey = "server_key";
static const char* kRootCertJsonKey = "root_cert";
static const char* kSecurityJsonKey = "security";
static const char* kCertsFolderName = "certs";
static const char* kMaxMessageSizeKey = "max_message_size";
static const char* kFeatureTogglesKey = "feature_toggles";
static const char* kCodeReadinessKey = "code_readiness";
#if defined(_MSC_VER)
static const char* kPathDelimiter = "\\";
#else
static const char* kPathDelimiter = "/";
#endif

ServerConfigurationParser::ServerConfigurationParser()
    : config_file_path_(get_exe_path() + kDefaultFilename),
      certs_directory_(get_exe_path() + kCertsFolderName)
{
   load_config_file();
}

ServerConfigurationParser::ServerConfigurationParser(const std::string& config_file_path)
    : config_file_path_(config_file_path),
      certs_directory_(get_certs_directory(config_file_path))
{
   load_config_file();
}

ServerConfigurationParser::ServerConfigurationParser(const nlohmann::json& config_file)
    : config_file_(config_file), certs_directory_(get_exe_path() + kCertsFolderName)
{
}

// Returns the absolute path to the folder that contains the running executable.
// The path includes the trailing platform-dependent delimiter (i.e. /path/to/exe/folder/
// or C:\path\to\exe\folder\) and does not contain the executable name. This function is
// public for test use.
std::string ServerConfigurationParser::get_exe_path()
{
#if defined(_MSC_VER)
  char filename[MAX_PATH];
  size_t path_length = GetModuleFileNameA(NULL, filename, MAX_PATH);
#else
  char filename[PATH_MAX];
  ssize_t path_length = readlink("/proc/self/exe", filename, PATH_MAX);
#endif
  if (path_length <= 0) {
    throw InvalidExePathException();
  }
  std::string exe_filename(filename, path_length);
  return exe_filename.erase(exe_filename.find_last_of(kPathDelimiter) + 1);
}

std::string ServerConfigurationParser::get_certs_directory(const std::string& config_file_path)
{
  std::string directory_path(config_file_path);
  size_t end_of_path_index = directory_path.find_last_of(kPathDelimiter);
  return end_of_path_index != std::string::npos
      ? directory_path.erase(end_of_path_index + 1) + kCertsFolderName
      : kCertsFolderName;
}

void ServerConfigurationParser::load_config_file()
{
  std::ifstream input_stream(config_file_path_);

  if (!input_stream) {
    throw ConfigFileNotFoundException(config_file_path_);
  }

  try {
    config_file_ = nlohmann::json::parse(input_stream);
  }
  catch (const nlohmann::json::parse_error& ex) {
    throw MalformedJsonException(ex.what());
  }
}

std::string ServerConfigurationParser::parse_address() const
{
  auto address = parse_bind_address() + ":" + std::to_string(parse_port());
  return address;
}

std::string ServerConfigurationParser::parse_sideband_address() const
{
  auto it = config_file_.find(kSidebandAddressJsonKey);
  return it != config_file_.end() ? it->get<std::string>() : "";
}

std::string ServerConfigurationParser::parse_server_cert() const
{
  auto file_name = parse_key_from_security_section(kServerCertJsonKey);
  return file_name.empty() ? "" : read_keycert(certs_directory_ + kPathDelimiter + file_name);
}

std::string ServerConfigurationParser::parse_server_key() const
{
  auto file_name = parse_key_from_security_section(kServerKeyJsonKey);
  return file_name.empty() ? "" : read_keycert(certs_directory_ + kPathDelimiter + file_name);
}

std::string ServerConfigurationParser::parse_root_cert() const
{
  auto file_name = parse_key_from_security_section(kRootCertJsonKey);
  return file_name.empty() ? "" : read_keycert(certs_directory_ + kPathDelimiter + file_name);
}

std::string ServerConfigurationParser::parse_security_mode() const
{
  auto it = config_file_.find(kSecurityJsonKey);
  if (it != config_file_.end() && it->is_string()) {
    return it->get<std::string>();
  }
  return "";
}

int ServerConfigurationParser::parse_max_message_size() const
{
  auto max_size_section_it = config_file_.find(kMaxMessageSizeKey);
  if (max_size_section_it != config_file_.end()) {
    try {
      return max_size_section_it->get<int>();
    }
    catch (const nlohmann::json::type_error& ex) {
      throw InvalidMaxMessageSizeException(ex.what());
    }
  }

  return UNLIMITED_MAX_MESSAGE_SIZE;
}

int ServerConfigurationParser::parse_sideband_port() const
{
  try {
    return parse_port_with_key(kSidebandPortJsonKey);
  }
  catch (const UnspecifiedPortException&) {
    return DEFAULT_SIDEBAND_PORT;
  }
}

FeatureToggles ServerConfigurationParser::parse_feature_toggles() const
{
  FeatureToggleConfigurationMap map;
  auto feature_toggle_section_it = config_file_.find(kFeatureTogglesKey);
  if (feature_toggle_section_it != config_file_.end()) {
    try {
      for (const auto& feature : feature_toggle_section_it->items()) {
        map[feature.key()] = feature.value();
      }
    }
    catch (const nlohmann::json::type_error& ex) {
      throw InvalidFeatureToggleException(ex.what());
    }
  }
  return FeatureToggles(std::move(map), parse_code_readiness());
}

FeatureToggles::CodeReadiness ServerConfigurationParser::parse_code_readiness() const
{
  auto code_readiness_it = config_file_.find(kCodeReadinessKey);
  if (code_readiness_it != config_file_.end()) {
    try {
      auto readiness_token_value = code_readiness_it->get<std::string>();
      std::transform(
          readiness_token_value.begin(),
          readiness_token_value.end(),
          readiness_token_value.begin(),
          [](unsigned char c) { return std::tolower(c); });

      using ReadinessMap = std::unordered_map<std::string, FeatureToggles::CodeReadiness>;
      const auto READINESS_MAP = ReadinessMap{
          {"release", FeatureToggles::CodeReadiness::kRelease},
          {"restrictedrelease", FeatureToggles::CodeReadiness::kRelease},
          {"restricted_release", FeatureToggles::CodeReadiness::kRelease},
          {"nextrelease", FeatureToggles::CodeReadiness::kNextRelease},
          {"next_release", FeatureToggles::CodeReadiness::kNextRelease},
          {"restrictednextrelease", FeatureToggles::CodeReadiness::kNextRelease},
          {"restricted_next_release", FeatureToggles::CodeReadiness::kNextRelease},
          {"incomplete", FeatureToggles::CodeReadiness::kIncomplete},
          {"prototype", FeatureToggles::CodeReadiness::kPrototype}};

      const auto readiness_map_iter = READINESS_MAP.find(readiness_token_value);
      if (readiness_map_iter != READINESS_MAP.end()) {
        return readiness_map_iter->second;
      }

      throw InvalidCodeReadinessException(readiness_token_value);
    }
    catch (const nlohmann::json::type_error& ex) {
      throw InvalidCodeReadinessException(ex.what());
    }
  }

  return FeatureToggles::CodeReadiness::kRelease;
}

std::string ServerConfigurationParser::parse_key_from_security_section(const char* key) const
{
  std::string parsed_value;

  auto security_section_it = config_file_.find(kSecurityJsonKey);
  if (security_section_it != config_file_.end()) {
    auto it = security_section_it->find(key);
    if (it != security_section_it->end()) {
      try {
        parsed_value = it->get<std::string>();
      }
      catch (const nlohmann::json::type_error&) {
        throw ValueTypeNotStringException(key);
      }
    }
  }
  return parsed_value;
}

std::string ServerConfigurationParser::read_keycert(const std::string& filename)
{
  std::string data;
  std::ifstream file(filename);
  if (!file) {
    throw FileNotFoundException(filename);
  }
  std::stringstream key_cert_contents;
  key_cert_contents << file.rdbuf();
  file.close();
  data = key_cert_contents.str();
  return data;
}

std::string ServerConfigurationParser::parse_bind_address() const
{
  // Use default address if none is specified
  std::string parsed_bind_address = kDefaultAddress;

  auto it = config_file_.find(kAddressJsonKey);
  if (it != config_file_.end()) {
    try {
      parsed_bind_address = it->get<std::string>();
    }
    catch (const nlohmann::json::type_error& ex) {
      throw WrongAddressTypeException(ex.what());
    }

    if (parsed_bind_address.empty()) {
      throw InvalidAddressException();
    }
  }

  return parsed_bind_address;
}

int ServerConfigurationParser::parse_port() const
{
  return parse_port_with_key(kPortJsonKey);
}

int ServerConfigurationParser::parse_port_with_key(const std::string& key) const
{
  int parsed_port = -1;

  auto it = config_file_.find(key);
  if (it != config_file_.end()) {
    try {
      parsed_port = it->get<int>();
    }
    catch (const nlohmann::json::type_error& ex) {
      throw WrongPortTypeException(ex.what());
    }
  }
  else {
    throw UnspecifiedPortException();
  }

  if (parsed_port < 0 || parsed_port > USHRT_MAX) {
    throw InvalidPortException();
  }

  return parsed_port;
}

MonikerStreamProcessor ServerConfigurationParser::parse_moniker_stream_processor() const
{
    MonikerStreamProcessor stream_processor;

    auto core_config_it = config_file_.find(kMonikerStreamProcessorKey);
    if (core_config_it != config_file_.end()) {
        stream_processor.moniker_sideband_stream_read_write = parse_moniker_stream_processor_with_key(kMonikerSidebandStreamReadWriteKey);
        stream_processor.moniker_stream_write = parse_moniker_stream_processor_with_key(kMonikerStreamWriteKey);
        stream_processor.moniker_stream_read = parse_moniker_stream_processor_with_key(kMonikerStreamReadKey);
        stream_processor.moniker_stream_read_write = parse_moniker_stream_processor_with_key(kMonikerStreamReadWriteKey);
    }
    return stream_processor;
}

int ServerConfigurationParser::parse_moniker_stream_processor_with_key(const std::string& key) const
{
    int parsed_core = -1;

    auto it = config_file_.find(key);
    if (it != config_file_.end()) {
        try {
            parsed_core = it->get<int>();
        }
        catch (const nlohmann::json::type_error& ex) {
            throw WrongMonikerStreamProcessorTypeException(ex.what());
        }
    }

    if (parsed_core < -1) {
        throw InvalidMonikerStreamProcessorException();
    }

    return parsed_core;
}

ServerConfigurationParser::ConfigFileNotFoundException::ConfigFileNotFoundException(const std::string& config_file_path)
    : std::runtime_error(kConfigFileNotFoundMessage + config_file_path)
{
}

ServerConfigurationParser::InvalidAddressException::InvalidAddressException()
    : std::runtime_error(kInvalidAddressMessage)
{
}

ServerConfigurationParser::WrongAddressTypeException::WrongAddressTypeException(const std::string& type_error_details)
    : std::runtime_error(kWrongAddressTypeMessage + type_error_details)
{
}

ServerConfigurationParser::InvalidPortException::InvalidPortException()
    : std::runtime_error(kInvalidPortMessage)
{
}

ServerConfigurationParser::InvalidMonikerStreamProcessorException::InvalidMonikerStreamProcessorException()
    : std::runtime_error(kInvalidMonikerStreamProcessorMessage)
{
}

ServerConfigurationParser::MalformedJsonException::MalformedJsonException(const std::string& parse_error_details)
    : std::runtime_error(kMalformedJsonMessage + parse_error_details)
{
}

ServerConfigurationParser::WrongPortTypeException::WrongPortTypeException(const std::string& type_error_details)
    : std::runtime_error(kWrongPortTypeMessage + type_error_details)
{
}

ServerConfigurationParser::WrongMonikerStreamProcessorTypeException::WrongMonikerStreamProcessorTypeException(const std::string& type_error_details)
    : std::runtime_error(kWrongMonikerStreamProcessorTypeMessage + type_error_details)
{
}

ServerConfigurationParser::UnspecifiedPortException::UnspecifiedPortException()
    : std::runtime_error(kUnspecifiedPortMessage)
{
}

ServerConfigurationParser::ValueTypeNotStringException::ValueTypeNotStringException(const std::string& key)
    : std::runtime_error(kValueTypeNotStringMessage + key)
{
}

ServerConfigurationParser::FileNotFoundException::FileNotFoundException(const std::string& filepath)
    : std::runtime_error(kFileNotFoundMessage + filepath)
{
}

ServerConfigurationParser::InvalidExePathException::InvalidExePathException()
    : std::runtime_error(kInvalidExePathMessage)
{
}

ServerConfigurationParser::InvalidFeatureToggleException::InvalidFeatureToggleException(const std::string& type_error_details)
    : std::runtime_error(kInvalidFeatureToggleMessage + type_error_details)
{
}

ServerConfigurationParser::InvalidCodeReadinessException::InvalidCodeReadinessException(const std::string& type_error_details)
    : std::runtime_error(kInvalidCodeReadinessMessage + type_error_details)
{
}

ServerConfigurationParser::InvalidMaxMessageSizeException::InvalidMaxMessageSizeException(const std::string& type_error_details)
    : std::runtime_error(kInvalidMaxMessageSizeMessage + type_error_details)
{
}
}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/server_configuration_parser.h sha256=98f42f468148da7147bb7f58f1759e45a35f19fe62dd61f404006d195ccdcb94 bytes=6406 -->
## FILE: source/server/server_configuration_parser.h

- repository: `ni/grpc-device`
- source_path: `source/server/server_configuration_parser.h`
- sha256: `98f42f468148da7147bb7f58f1759e45a35f19fe62dd61f404006d195ccdcb94`
- bytes: 6406

````c
#ifndef NIDEVICE_GRPC_SERVER_CONFIGURATION_PARSER_H
#define NIDEVICE_GRPC_SERVER_CONFIGURATION_PARSER_H

#include <fstream>
#include <nlohmann/json.hpp>

#include "feature_toggles.h"
#include "moniker_stream_processor.h"

namespace nidevice_grpc {

static const char* kConfigFileNotFoundMessage = "The server configuration file was not found at: ";
static const char* kInvalidAddressMessage = "The specified address is not valid.\n Use a valid IPv4 or IPv6 address. Valid values include localhost, 192.168.1.1, [::], [::1], etc.";
static const char* kWrongAddressTypeMessage = "The server address must be specified in the server's configuration file as a string: \n\n";
static const char* kInvalidPortMessage = "The specified port number must between 0 and 65535.";
static const char* kInvalidMonikerStreamProcessorMessage = "The specified moniker stream processor must be -1 or greater. -1 indicates that any available cpu core can be used.";
static const char* kMalformedJsonMessage = "The JSON in the server configuration file is malformed: \n\n";
static const char* kWrongPortTypeMessage = "The server port must be specified in the server's configuration file as an integer: \n\n";
static const char* kWrongMonikerStreamProcessorTypeMessage = "The moniker stream processor must be specified in the server's configuration file as an integer: \n\n";
static const char* kUnspecifiedPortMessage = "The server port must be specified in the server's configuration file.";
static const char* kValueTypeNotStringMessage = "The following key must be specified in the server's configuration file as a string enclosed with double quotes: ";
static const char* kFileNotFoundMessage = "The following certificate file was not found: ";
static const char* kInvalidExePathMessage = "The server was unable to resolve the current executable path.";
static const char* kInvalidMaxMessageSizeMessage = "The max message size must be an integer.";
static const char* kInvalidFeatureToggleMessage = "Feature Toggles must be specified as boolean fields in the form \"feature_toggles\": { \"feature1\": true, \"feature2\": false }. \n\n";
static const char* kInvalidCodeReadinessMessage = "code_readiness must be a string in [Release, RestrictedRelease, NextRelease, RestrictedNextRelease, Incomplete, Prototype].\n\n";
// CWE-306: Default to the IPv6 loopback address so the server is only reachable
// from the local machine when no address is specified in the configuration file.
// This prevents unintentional exposure on all network interfaces when insecure
// (non-TLS) credentials are used. Deployments that need to accept remote
// connections should set an explicit address (e.g. "[::]") in their config file.
static const char* kDefaultAddress = "[::1]";
constexpr int UNLIMITED_MAX_MESSAGE_SIZE = -1;
constexpr int DEFAULT_SIDEBAND_PORT = 50055;

class ServerConfigurationParser {
 public:
  ServerConfigurationParser();
  ServerConfigurationParser(const std::string& config_file_path);
  ServerConfigurationParser(const nlohmann::json& config_file);
  virtual ~ServerConfigurationParser() {}

  static std::string get_exe_path();

  const std::string& get_config_file_path() const { return config_file_path_; }

  std::string parse_address() const;
  std::string parse_sideband_address() const;
  std::string parse_server_cert() const;
  std::string parse_server_key() const;
  std::string parse_root_cert() const;
  std::string parse_security_mode() const;
  int parse_max_message_size() const;
  int parse_sideband_port() const;
  MonikerStreamProcessor parse_moniker_stream_processor() const;
  FeatureToggles parse_feature_toggles() const;
  FeatureToggles::CodeReadiness parse_code_readiness() const;

  struct ConfigFileNotFoundException : public std::runtime_error {
    ConfigFileNotFoundException(const std::string& config_file_path);
  };

  struct InvalidAddressException : public std::runtime_error {
    InvalidAddressException();
  };

  struct WrongAddressTypeException : public std::runtime_error {
    WrongAddressTypeException(const std::string& type_error_details);
  };

  struct InvalidPortException : public std::runtime_error {
    InvalidPortException();
  };

  struct InvalidMonikerStreamProcessorException : public std::runtime_error {
    InvalidMonikerStreamProcessorException();
  };

  struct MalformedJsonException : public std::runtime_error {
    MalformedJsonException(const std::string& parse_error_details);
  };

  struct WrongPortTypeException : public std::runtime_error {
    WrongPortTypeException(const std::string& type_error_details);
  };

  struct WrongMonikerStreamProcessorTypeException : public std::runtime_error {
    WrongMonikerStreamProcessorTypeException(const std::string& type_error_details);
  };

  struct UnspecifiedPortException : public std::runtime_error {
    UnspecifiedPortException();
  };

  struct ValueTypeNotStringException : public std::runtime_error {
    ValueTypeNotStringException(const std::string& key);
  };

  struct FileNotFoundException : public std::runtime_error {
    FileNotFoundException(const std::string& filepath);
  };

  struct InvalidExePathException : public std::runtime_error {
    InvalidExePathException();
  };

  struct InvalidFeatureToggleException : std::runtime_error {
    InvalidFeatureToggleException(const std::string& type_error_details);
  };

  struct InvalidCodeReadinessException : std::runtime_error {
    InvalidCodeReadinessException(const std::string& type_error_details);
  };

  struct InvalidMaxMessageSizeException : std::runtime_error {
    InvalidMaxMessageSizeException(const std::string& type_error_details);
  };

 private:
  void load_config_file();
  static std::string read_keycert(const std::string& filename);
  static std::string get_certs_directory(const std::string& config_file_path);
  std::string parse_key_from_security_section(const char* key) const;
  std::string parse_bind_address() const;
  int parse_port() const;
  int parse_port_with_key(const std::string& key) const;
  int parse_moniker_stream_processor_with_key(const std::string& key) const;

  std::string config_file_path_;
  nlohmann::json config_file_;
  std::string certs_directory_;
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SERVER_CONFIGURATION_PARSER_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/server_reactor.h sha256=7ee689b513203b7b6be8a35f945bd0a4a71453b4cf1a5b149b4199537186489e bytes=2139 -->
## FILE: source/server/server_reactor.h

- repository: `ni/grpc-device`
- source_path: `source/server/server_reactor.h`
- sha256: `7ee689b513203b7b6be8a35f945bd0a4a71453b4cf1a5b149b4199537186489e`
- bytes: 2139

````c
#ifndef NIDEVICE_GRPC_DEVICE_SERVER_REACTOR_H
#define NIDEVICE_GRPC_DEVICE_SERVER_REACTOR_H

#include <grpcpp/alarm.h>
#include <grpcpp/grpcpp.h>

#include <deque>
#include <memory>
#include <mutex>
#include <queue>

namespace nidevice_grpc {

// ServerWriteReactor implementation to support async response streaming.
template <typename TResponse, typename TProducer>
class ServerWriterReactor : public grpc::ServerWriteReactor<TResponse> {
  using LockGuard = std::lock_guard<std::recursive_mutex>;

 public:
  virtual ~ServerWriterReactor()
  {
  }

  void OnDone() override
  {
    delete this;
  }

  void OnWriteDone(bool write_succeeded) override
  {
    LockGuard lock(mutex_);
    write_ready_ = true;
    pending_send_.pop();
    if (write_succeeded) {
      next_write();
    }
  }

  void OnCancel() override
  {
    try_finish(::grpc::Status::OK);
  }

 protected:
  void queue_write(const TResponse& response)
  {
    LockGuard lock(mutex_);
    pending_send_.push(response);
    next_write();
  }

  void set_producer(std::unique_ptr<TProducer>&& producer)
  {
    producer_ = std::move(producer);
  }

  // Try to immediately finish the RPC. If called multiple times, the first call wins.
  // This method does not wait until the pending send queue is empty.
  bool try_finish(::grpc::Status status)
  {
    LockGuard lock(mutex_);
    if (!done_) {
      done_ = true;
      this->Finish(std::move(status));
      return true;
    }
    return false;
  }

 private:
  void next_write()
  {
    LockGuard lock(mutex_);

    if (!done_ && write_ready_ && !pending_send_.empty()) {
      write_ready_ = false;
      auto& response = pending_send_.front();
      this->StartWrite(&response);
    }
  }

  std::recursive_mutex mutex_;
  // This class relies on: std::deque does not invalidate on push/pop.
  std::queue<TResponse, std::deque<TResponse>> pending_send_;
  bool write_ready_{true};
  bool done_{false};
  std::unique_ptr<TProducer> producer_;
};
}  // namespace nidevice_grpc
#endif  // NIDEVICE_GRPC_DEVICE_SERVER_REACTOR_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/server_reset_observer_interface.h sha256=5de70c30a64352b0ef4043567b6f8ed6843018e662a7f6a11aa55837b7393cc6 bytes=379 -->
## FILE: source/server/server_reset_observer_interface.h

- repository: `ni/grpc-device`
- source_path: `source/server/server_reset_observer_interface.h`
- sha256: `5de70c30a64352b0ef4043567b6f8ed6843018e662a7f6a11aa55837b7393cc6`
- bytes: 379

````c
#ifndef NIDEVICE_GRPC_SERVER_RESET_OBSERVER_INTERFACE_H
#define NIDEVICE_GRPC_SERVER_RESET_OBSERVER_INTERFACE_H

namespace nidevice_grpc {

class ServerResetObserverInterface {
 public:
  virtual ~ServerResetObserverInterface() {}

  virtual void on_server_reset() = 0;
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SERVER_RESET_OBSERVER_INTERFACE_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/server_reset_observer_registrar_interface.h sha256=a4f6339cdd0fec034ded9debf1695c573672eaec47a6d4094be785d86a9ccbce bytes=596 -->
## FILE: source/server/server_reset_observer_registrar_interface.h

- repository: `ni/grpc-device`
- source_path: `source/server/server_reset_observer_registrar_interface.h`
- sha256: `a4f6339cdd0fec034ded9debf1695c573672eaec47a6d4094be785d86a9ccbce`
- bytes: 596

````c
#ifndef NIDEVICE_GRPC_SERVER_RESET_OBSERVER_REGISTRAR_INTERFACE_H
#define NIDEVICE_GRPC_SERVER_RESET_OBSERVER_REGISTRAR_INTERFACE_H

#include "server_reset_observer_interface.h"

namespace nidevice_grpc {

class ServerResetObserverRegistrarInterface {
 public:
  virtual ~ServerResetObserverRegistrarInterface() {}

  virtual void register_observer(ServerResetObserverInterface* observer) = 0;
  virtual void unregister_observer(ServerResetObserverInterface* observer) = 0;
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SERVER_RESET_OBSERVER_REGISTRAR_INTERFACE_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/server_security_configuration.cpp sha256=93b33aede07a4549fb09570303485b561a53ce292d7496a1461c8fe9911ce9d7 bytes=1529 -->
## FILE: source/server/server_security_configuration.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/server_security_configuration.cpp`
- sha256: `93b33aede07a4549fb09570303485b561a53ce292d7496a1461c8fe9911ce9d7`
- bytes: 1529

````cpp
#include "server_security_configuration.h"

#include <typeinfo>

namespace nidevice_grpc {

ServerSecurityConfiguration::ServerSecurityConfiguration()
    : ServerSecurityConfiguration("", "", "")
{
}

ServerSecurityConfiguration::ServerSecurityConfiguration(const std::string& server_cert, const std::string& server_key, const std::string& root_cert)
    : is_insecure_credentials_(server_cert.empty() || server_key.empty())
{
  if (is_insecure_credentials_) {
    server_credentials_ = ::grpc::InsecureServerCredentials();
    return;
  }

  ::grpc::SslServerCredentialsOptions::PemKeyCertPair key_cert_pair = {server_key, server_cert};
  credentials_options_.pem_key_cert_pairs.push_back(key_cert_pair);
  credentials_options_.client_certificate_request = root_cert.empty()
      ? GRPC_SSL_DONT_REQUEST_CLIENT_CERTIFICATE
      : GRPC_SSL_REQUEST_AND_REQUIRE_CLIENT_CERTIFICATE_AND_VERIFY;
  credentials_options_.pem_root_certs = root_cert;
  server_credentials_ = ::grpc::SslServerCredentials(credentials_options_);
}

std::shared_ptr<::grpc::ServerCredentials> ServerSecurityConfiguration::get_credentials() const
{
  return server_credentials_;
}

const ::grpc::SslServerCredentialsOptions* ServerSecurityConfiguration::try_get_options() const
{
  if (is_insecure_credentials_) {
    return nullptr;
  }
  return &credentials_options_;
}

bool ServerSecurityConfiguration::is_insecure_credentials() const
{
  return is_insecure_credentials_;
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/server_security_configuration.h sha256=b5cc14a404a8561ff14332cad8b3275ca650cd7d2b1d280b0835e24a73b512d1 bytes=855 -->
## FILE: source/server/server_security_configuration.h

- repository: `ni/grpc-device`
- source_path: `source/server/server_security_configuration.h`
- sha256: `b5cc14a404a8561ff14332cad8b3275ca650cd7d2b1d280b0835e24a73b512d1`
- bytes: 855

````c
#ifndef NIDEVICE_GRPC_SERVER_SECURITY_CONFIGURATION_H
#define NIDEVICE_GRPC_SERVER_SECURITY_CONFIGURATION_H

#include <grpcpp/grpcpp.h>

#include <string>

namespace nidevice_grpc {

class ServerSecurityConfiguration {
 public:
  ServerSecurityConfiguration();
  ServerSecurityConfiguration(const std::string& server_cert, const std::string& server_key, const std::string& root_cert);

  std::shared_ptr<::grpc::ServerCredentials> get_credentials() const;
  const ::grpc::SslServerCredentialsOptions* try_get_options() const;
  bool is_insecure_credentials() const;

 private:
  bool is_insecure_credentials_;
  ::grpc::SslServerCredentialsOptions credentials_options_;
  std::shared_ptr<::grpc::ServerCredentials> server_credentials_;
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SERVER_SECURITY_CONFIGURATION_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/session_repository.cpp sha256=cf61399964ca9c7d4d106f27ec501f88e400dd4d7af92489dd3804b980716c4d bytes=11366 -->
## FILE: source/server/session_repository.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/session_repository.cpp`
- sha256: `cf61399964ca9c7d4d106f27ec501f88e400dd4d7af92489dd3804b980716c4d`
- bytes: 11366

````cpp
#include "session_repository.h"

#include <grpcpp/grpcpp.h>

#include "shared_library.h"

namespace nidevice_grpc {

SessionRepository::SessionRepository()
{
}

SessionRepository::~SessionRepository()
{
  // Do not cleanup external resources during shutdown. At this stage, all of the
  // driver Library objects have been cleaned up so it's not safe to call them.
  // To fix that, we'd have to change up our resource management. But right now we
  // don't have a structured cleanup process and will let the driver figure out how
  // to handle ctrl+c shutdown.
  reset_server(/* cleanup_external_resources =*/false);
}

// Either returns (via session_name) an existing session with the specified name or initializes and
// adds a new session using the init_func provided. The init_func is only called when an existing
// session with session_name is not found. It is expected to return a tuple, where the first value
// is a status code, and the second value is the ID of a newly initialized session. The return
// value is the status returned from the init_func, or 0 if an existing named session is found.
int SessionRepository::add_session(
    std::string& session_name,
    InitFunc init_func,
    CleanupSessionFunc cleanup_func,
    SessionInitializationBehavior initialization_behavior,
    bool* initialized_new_session)
{
  if (initialized_new_session) {
    *initialized_new_session = false;
  }
  std::unique_lock<std::shared_mutex> lock(repository_lock_);
  auto now = std::chrono::steady_clock::now();
  auto it = named_sessions_.find(session_name);
  if (initialization_behavior == SESSION_INITIALIZATION_BEHAVIOR_INITIALIZE_NEW && it != named_sessions_.end()) {
    throw NonDriverException(::grpc::StatusCode::ALREADY_EXISTS, "Cannot initialize '" + session_name + "' when a session already exists.");
  }
  else if (initialization_behavior == SESSION_INITIALIZATION_BEHAVIOR_ATTACH_TO_EXISTING && it == named_sessions_.end()) {
    throw NonDriverException(::grpc::StatusCode::FAILED_PRECONDITION, "Cannot attach to '" + session_name + "' because a session has not been initialized.");
  }

  if (it != named_sessions_.end()) {
    it->second->last_access_time = now;
    return 0;
  }
  auto info = std::make_shared<SessionInfo>();
  auto status = init_func();
  if (status) {
    return status;
  }
  if (session_name.length() == 0) {
    session_name = next_id();
  }
  info->cleanup_func = cleanup_func;
  info->last_access_time = now;
  info->name = session_name;
  named_sessions_.emplace(session_name, info);
  if (initialized_new_session) {
    *initialized_new_session = true;
  }
  return 0;
}

// Updates the last_access_time of a session, if one is found with the given ID or name. Returns
// the ID of the session that matches the given ID or name, or 0 if such a session is not found.
// Only one of the two parameters needs to be specified.
// Passing only a name returns the corresponding ID.
std::string SessionRepository::access_session(const std::string& session_name)
{
  std::unique_lock<std::shared_mutex> lock(repository_lock_);
  auto now = std::chrono::steady_clock::now();
  auto it = named_sessions_.find(session_name);
  if (it != named_sessions_.end()) {
    it->second->last_access_time = now;
    return it->second->name;
  }
  return "";
}

// Removes a session by ID.
// To remove a session by name, use access_session to get the session ID.
void SessionRepository::remove_session(const std::string& name)
{
  std::unique_lock<std::shared_mutex> lock(repository_lock_);
  auto named_it = named_sessions_.find(name);
  if (named_it != named_sessions_.end()) {
    named_sessions_.erase(named_it);
  }
}

void SessionRepository::register_dependent_session(const std::string& name, const std::string& dependent_session_name, std::function<void()> cleanup)
{
  std::unique_lock<std::shared_mutex> lock(repository_lock_);
  auto it = named_sessions_.find(name);
  if (it != named_sessions_.end()) {
    auto remove_action = std::make_unique<RemoveAction>([dependent_session_name, cleanup, this]() {
      cleanup();
      named_sessions_.erase(dependent_session_name);
    });
    it->second->dependent_sessions.emplace_back(std::move(remove_action));
  }
}

// This method has three behaviors:
// 1) If no ReservationInfo exists with the given reservation_id, it creates a new ReservationInfo,
//    adds it to reservations_, and returns it.
// 2) If a ReservationInfo does exist with the given reservation_id
//    a) If the client_id on the existing reservation matches the given client_id given, returns a nullptr.
//    b) Otherwise, increments the client_count on the existing ReservationInfo and returns the info.
std::shared_ptr<SessionRepository::ReservationInfo> SessionRepository::find_or_create_reservation(const std::string& reservation_id, const std::string& client_id)
{
  std::unique_lock<std::shared_mutex> lock(repository_lock_);
  std::shared_ptr<ReservationInfo> info;
  auto it = reservations_.find(reservation_id);
  if (it != reservations_.end()) {
    info = it->second;
    if (info->client_id == client_id) {
      return nullptr;
    }
    ++info->client_count;
  }
  else {
    info = std::make_shared<SessionRepository::ReservationInfo>();
    info->creation_time = std::chrono::steady_clock::now();
    info->client_id = client_id;
    info->lock = std::make_unique<Semaphore>();
    info->client_count = 1;
    reservations_.emplace(reservation_id, info);
  }
  return info;
}

// Returns a boolean value indicating whether or not the client_id holds the reservation_id and it also sets the
// status to an appropriate grpc::Status providing more detail about the circumstances surrounding
// the returned reservation state. There are two states that are possible but multiple statuses in each state:
// 1. The provided client_id does not hold the reservation_id:
//   a. If the reservation_id or client_id are empty then the status is set to INVALID_ARGUMENT
//   b. If the reservation is not created because an external call like reset_server changed the server state while
//      waiting to acquire the reservation then the status is set to ABORTED.
//   c. If the reserve call is cancelled by a client call to cancel or by exceeding the client's deadline then
//      the status is set to CANCELLED.
// 2. The provided client_id does hold the reservation_id:
//   a. If the reservation requested is already reserved by client_id then status is set to FAILED_PRECONDITION. The
//      precondition in this case is that the client_id doesn't already hold the reservation_id.
//   b. If the reservation is created for client_id or if the reservation is changed from another client to client_id
//      then the status is set to OK.
bool SessionRepository::reserve(
    const ::grpc::ServerContext* context,
    const std::string& reservation_id,
    const std::string& client_id,
    ::grpc::Status& status)
{
  if (reservation_id.empty() || client_id.empty()) {
    status = ::grpc::Status(::grpc::INVALID_ARGUMENT, "You must specify a non-empty reservation_id and client_id.");
    return false;
  }
  std::shared_ptr<ReservationInfo> info = find_or_create_reservation(reservation_id, client_id);
  if (!info) {
    status = ::grpc::Status(::grpc::FAILED_PRECONDITION, "The provided reservation_id is already reserved by the provided client_id.");
    return true;
  }
  // If the info was newly created by find_or_create_reservation, this call
  // will not wait. On subsequent calls to reserve with the same reservation_id
  // and a different client_id, it will wait until the lock calls notify which
  // releases the lock one client at a time.
  info->lock->wait();
  {
    std::unique_lock<std::shared_mutex> lock(repository_lock_);
    info->client_count--;
    auto it = reservations_.find(reservation_id);
    if (context->IsCancelled()) {
      info->lock->notify();
      if (it != reservations_.end() && info->client_count <= 0) {
        reservations_.erase(it);
      }
      status = ::grpc::Status::CANCELLED;
      return false;
    }
    info->client_id = client_id;
    bool is_reserved = it != reservations_.end() && client_id == it->second->client_id;
    status = is_reserved
        ? ::grpc::Status::OK
        : ::grpc::Status(::grpc::ABORTED, "The reservation attempt was aborted by another server operation.");
    return is_reserved;
  }
}

bool SessionRepository::is_reserved_by_client(const std::string& reservation_id, const std::string& client_id)
{
  std::unique_lock<std::shared_mutex> lock(repository_lock_);
  auto it = reservations_.find(reservation_id);
  return it != reservations_.end() && client_id == it->second->client_id;
}

// Unreserving a reservation notifies the lock on the reservation, allowing the next client
// waiting to get the reservation.
// If there are no clients waiting on the lock, the reservation is removed from the reservations_ map.
bool SessionRepository::unreserve(const std::string& reservation_id, const std::string& client_id)
{
  std::unique_lock<std::shared_mutex> lock(repository_lock_);
  std::shared_ptr<SessionRepository::ReservationInfo> reservation_info;
  auto it = reservations_.find(reservation_id);
  if (it != reservations_.end() && client_id == it->second->client_id) {
    reservation_info = it->second;
    if (it->second->client_count <= 0) {
      reservations_.erase(it);
    }
  }
  return release_reservation(reservation_info.get());
}

bool SessionRepository::release_reservation(const ReservationInfo* reservation_info)
{
  if (reservation_info) {
    reservation_info->lock->notify();
    return true;
  }
  return false;
}

void SessionRepository::clear_reservations()
{
  for (auto it = reservations_.begin(); it != reservations_.end();) {
    std::shared_ptr<SessionRepository::ReservationInfo> reservation_info = it->second;
    it = reservations_.erase(it);
    reservation_info->lock->cancel();
  }
}

bool SessionRepository::reset_server(bool cleanup_external_resources)
{
  std::unique_lock<std::shared_mutex> lock(repository_lock_);
  clear_reservations();
  bool is_server_reset = close_sessions(cleanup_external_resources);
  return is_server_reset && reservations_.empty();
}

bool SessionRepository::close_sessions(bool cleanup_external_resources)
{
  // Copy sessions for cleanup to avoid invalidating iterators when dependent sessions
  // are removed.
  auto sessions_cleanup = std::vector<std::shared_ptr<SessionInfo>>();
  std::transform(
      named_sessions_.cbegin(),
      named_sessions_.cend(),
      std::back_inserter(sessions_cleanup),
      [](const NamedSessionMap::value_type& entry) { return entry.second; });

  named_sessions_.clear();
  if (cleanup_external_resources) {
    for (auto session_info : sessions_cleanup) {
      cleanup_session(session_info);
    }
  }
  sessions_cleanup.clear();
  return named_sessions_.empty();
}

void SessionRepository::cleanup_session(const std::shared_ptr<SessionInfo>& session_info)
{
  auto cleanup_process = session_info->cleanup_func;
  if (cleanup_process) {
    cleanup_process(session_info->name);
  }
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/session_repository.h sha256=4017ccce9c80e9e652e406fb34d4a968d5a846edd3fe5b57ef893734bf12134e bytes=3775 -->
## FILE: source/server/session_repository.h

- repository: `ni/grpc-device`
- source_path: `source/server/session_repository.h`
- sha256: `4017ccce9c80e9e652e406fb34d4a968d5a846edd3fe5b57ef893734bf12134e`
- bytes: 3775

````c
#ifndef NIDEVICE_GRPC_SESSION_REPOSITORY
#define NIDEVICE_GRPC_SESSION_REPOSITORY

#include <session.pb.h>

#include <atomic>
#include <functional>
#include <map>
#include <shared_mutex>
#include <vector>

#include "semaphore.h"

namespace grpc {
class ServerContext;
class Status;
}  // namespace grpc

namespace nidevice_grpc {

class SessionRepository {
 public:
  SessionRepository();
  ~SessionRepository();

  typedef std::function<int32_t()> InitFunc;
  typedef std::function<void(const std::string&)> CleanupSessionFunc;

  int add_session(
      std::string& session_name,
      InitFunc init_func,
      CleanupSessionFunc cleanup_func,
      SessionInitializationBehavior initialization_behavior = SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED,
      bool* initialized_new_session = nullptr);
  std::string access_session(const std::string& session_name);
  void remove_session(const std::string& name);

  void register_dependent_session(const std::string& name, const std::string& dependent_session_name, std::function<void()> cleanup);

  bool reserve(
      const ::grpc::ServerContext* context,
      const std::string& reservation_id,
      const std::string& client_id,
      ::grpc::Status& status);
  bool is_reserved_by_client(const std::string& reservation_id, const std::string& client_id);
  bool unreserve(const std::string& reservation_id, const std::string& client_id);
  bool reset_server(bool cleanup = true);

 private:
  struct ReservationInfo {
    std::string client_id;
    std::unique_ptr<Semaphore> lock;
    std::chrono::steady_clock::time_point creation_time;
    // The number of clients that have asked to reserve this reservation, but have not yet acquired the lock.
    int client_count;
  };

  // Action that is executed on remove from the map.
  // Unlike cleanup_action this is called for both explicit cleanup (close) and
  // implicit cleanup (reset_server).
  class RemoveAction {
   public:
    RemoveAction(std::function<void()> on_remove) : on_remove_(on_remove) {}
    ~RemoveAction()
    {
      on_remove_();
    }

   private:
    std::function<void()> on_remove_;
  };

  struct SessionInfo {
    std::string name;
    std::chrono::steady_clock::time_point last_access_time;
    SessionRepository::CleanupSessionFunc cleanup_func;
    std::vector<std::unique_ptr<RemoveAction>> dependent_sessions;
  };

  using NamedSessionMap = std::map<std::string, std::shared_ptr<SessionInfo>>;
  using ReservationMap = std::map<std::string, std::shared_ptr<ReservationInfo>>;

  std::shared_ptr<ReservationInfo> find_or_create_reservation(const std::string& reservation_id, const std::string& client_id);
  void clear_reservations();
  bool close_sessions(bool cleanup);
  void cleanup_session(const std::shared_ptr<SessionInfo>& session_info);
  bool release_reservation(const ReservationInfo* reservation_info);
  // CWE-330 note: Session IDs are intentionally sequential. grpc-device is not
  // a multi-tenant service and cross-client session access is by design.
  // These IDs are not security tokens and must not be relied upon for access
  // control or isolation. If tenant isolation is required in the future,
  // session ownership and access-control checks should be introduced rather
  // than merely randomizing identifiers.
  std::string next_id() { return "ni:generated:" + std::to_string(++_next_id); }

  std::shared_mutex repository_lock_;
  // These entries point at SessionInfo objects that are also contained in sessions_.
  NamedSessionMap named_sessions_;
  ReservationMap reservations_;
  std::atomic<uint32_t> _next_id{0};
};
}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SESSION_REPOSITORY
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/session_resource_repository.h sha256=4beeea9ad5f31daab0c731de71c6f8bdcb3a18cba4d5922df3523716d2c450d2 bytes=8576 -->
## FILE: source/server/session_resource_repository.h

- repository: `ni/grpc-device`
- source_path: `source/server/session_resource_repository.h`
- sha256: `4beeea9ad5f31daab0c731de71c6f8bdcb3a18cba4d5922df3523716d2c450d2`
- bytes: 8576

````c
#ifndef NIDEVICE_GRPC_SESSION_RESOURCE_REPOSITORY_H
#define NIDEVICE_GRPC_SESSION_RESOURCE_REPOSITORY_H

#include <memory>
#include <mutex>
#include <string>
#include <unordered_map>

#include "session_repository.h"
#include "shared_library.h"

namespace nidevice_grpc {

// Wraps SessionRepository to store a service-specific TResourceHandle associated with
// each session.
template <typename TResourceHandle>
class SessionResourceRepository {
 public:
  typedef std::function<std::tuple<int, TResourceHandle>()> InitFunc;
  typedef std::function<void(TResourceHandle)> CleanupSessionFunc;

  explicit SessionResourceRepository(const std::shared_ptr<SessionRepository>& session_repository)
      : session_repository_(session_repository),
        resource_map_(std::make_shared<ResourceMap>())
  {
  }

  int add_session(
      std::string& session_name,
      InitFunc init_func,
      CleanupSessionFunc cleanup_func,
      SessionInitializationBehavior initialization_behavior = SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED,
      bool* initialized_new_session = nullptr,
      bool include_in_reverse_lookup = true);

  TResourceHandle access_session(const std::string& session_name) const;
  std::string resolve_session_name(TResourceHandle handle) const;
  int add_dependent_session(std::string& session_name, InitFunc init_func, std::string& initiating_session);
  void remove_session(const std::string& session_name);

 private:
  // Wraps init_func_ and caches the result as handle_.
  // For passing into SessionRepository.add_session.
  struct SessionResourceCreator {
    const InitFunc& init_func_;
    TResourceHandle handle_;
    bool added_new_handle_;

    SessionResourceCreator(const InitFunc& init_func)
        : init_func_(init_func),
          added_new_handle_(false),
          handle_()
    {
    }

    uint32_t init_resource_handle();
  };

  // A thread-safe bi-directional map of session_id to TResourceHandle.
  class ResourceMap {
   public:
    void add(const std::string& session_name, TResourceHandle handle, bool include_in_reverse_lookup);

    bool contains(const std::string& session_name) const;
    TResourceHandle get_handle(const std::string& session_name) const;
    std::string get_session_name(TResourceHandle handle) const;

    TResourceHandle remove_session_name(const std::string& session_name);

   private:
    using SessionToResourceMap = std::map<std::string, TResourceHandle>;
    using ResourceToSessionMap = std::map<TResourceHandle, std::string>;
    using MapLock = std::lock_guard<std::recursive_mutex>;

    SessionToResourceMap map_;
    ResourceToSessionMap reverse_map_;
    mutable std::recursive_mutex map_mutex_;
  };

  // Services share ownership of session resource repositories, which share ownership of the session repository.
  std::shared_ptr<SessionRepository> session_repository_;

  // shared_ptr to allow sharing ownership with cleanup delegate in register_dependent_session.
  std::shared_ptr<ResourceMap> resource_map_;
};

template <typename TResourceHandle>
int SessionResourceRepository<TResourceHandle>::add_session(
    std::string& session_name,
    InitFunc init_func,
    CleanupSessionFunc cleanup_func,
    SessionInitializationBehavior initialization_behavior,
    bool* initialized_new_session,
    bool include_in_reverse_lookup)
{
  auto session_creator = SessionResourceCreator(init_func);
  auto resource_map = resource_map_;
  auto status = session_repository_->add_session(
      session_name,
      [&]() { return session_creator.init_resource_handle(); },
      // By val capture to keep cleanup_func in memory.
      [resource_map, cleanup_func](const std::string& name) {
        auto handle = resource_map->remove_session_name(name);
        return cleanup_func(handle);
      },
      initialization_behavior,
      initialized_new_session);

  if (status) {
    session_name = std::string();
    return status;
  }

  if (session_creator.added_new_handle_) {
    resource_map_->add(session_name, session_creator.handle_, include_in_reverse_lookup);
  }

  // session_name resolves to a session in a different resource repository.
  if (!resource_map_->contains(session_name)) {
    throw nidevice_grpc::SessionException("The session name \"" + session_name + "\" is being used by a different driver.");
  }

  return 0;
}

template <typename TResourceHandle>
int SessionResourceRepository<TResourceHandle>::add_dependent_session(
    std::string& session_name,
    InitFunc init_func,
    std::string& initiating_session)
{
  // Register with no cleanup function.
  // ASSUMPTION: dependent sessions are owned by the initiating driver session and appropriate
  // cleanup code will be executed when the initiating session is closed.
  // We're only responsible for cleaning up the map structures.
  auto status = add_session(
      session_name,
      init_func,
      [](TResourceHandle) {},
      /* initialization_behavior = */ SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED,
      /* initialized_new_session = */ nullptr,
      /* include_in_reverse_lookup = */ false);
  auto resource_map = resource_map_;
  session_repository_->register_dependent_session(
      initiating_session,
      session_name,
      [session_name, resource_map]() { resource_map->remove_session_name(session_name); });
  return status;
}

template <typename TResourceHandle>
TResourceHandle SessionResourceRepository<TResourceHandle>::access_session(const std::string& session_name) const
{
  auto name = session_repository_->access_session(session_name);
  return resource_map_->get_handle(name);
}

template <typename TResourceHandle>
std::string SessionResourceRepository<TResourceHandle>::resolve_session_name(TResourceHandle handle) const
{
  return resource_map_->get_session_name(handle);
}

template <typename TResourceHandle>
void SessionResourceRepository<TResourceHandle>::remove_session(const std::string& session_name)
{
  auto name = session_repository_->access_session(session_name);
  if (name.length()) {
    resource_map_->remove_session_name(name);
    session_repository_->remove_session(name);
  }
}

template <typename TResourceHandle>
uint32_t SessionResourceRepository<TResourceHandle>::SessionResourceCreator::init_resource_handle()
{
  auto init_result = init_func_();
  auto status = std::get<0>(init_result);
  if (status) {
    return status;
  }

  handle_ = std::get<1>(init_result);
  added_new_handle_ = true;

  return 0;
}

template <typename TResourceHandle>
void SessionResourceRepository<TResourceHandle>::ResourceMap::add(const std::string& session_name, TResourceHandle handle, bool include_in_reverse_lookup)
{
  MapLock lock(map_mutex_);
  map_[session_name] = handle;
  if (include_in_reverse_lookup) {
    reverse_map_[handle] = session_name;
  }
}

template <typename TResourceHandle>
bool SessionResourceRepository<TResourceHandle>::ResourceMap::contains(const std::string& session_name) const
{
  MapLock lock(map_mutex_);
  auto found = map_.find(session_name);
  return found != map_.end();
}

template <typename TResourceHandle>
TResourceHandle SessionResourceRepository<TResourceHandle>::ResourceMap::get_handle(const std::string& session_name) const
{
  MapLock lock(map_mutex_);
  auto resource_it = map_.find(session_name);
  if (resource_it != map_.end()) {
    return resource_it->second;
  }
  // Note: failed resolve will ultimately be reported as a bad resource by the driver
  // on use.
  return TResourceHandle();
}

template <typename TResourceHandle>
std::string SessionResourceRepository<TResourceHandle>::ResourceMap::get_session_name(TResourceHandle handle) const
{
  MapLock lock(map_mutex_);
  auto session_it = reverse_map_.find(handle);
  if (session_it != reverse_map_.end()) {
    return session_it->second;
  }
  // Note: failed resolve will ultimately be reported as a bad resource by the driver
  // on use.
  return "";
}

template <typename TResourceHandle>
TResourceHandle SessionResourceRepository<TResourceHandle>::ResourceMap::remove_session_name(const std::string& session_name)
{
  MapLock lock(map_mutex_);
  auto handle = get_handle(session_name);
  if (handle != TResourceHandle()) {
    map_.erase(session_name);
    reverse_map_.erase(handle);
  }
  return handle;
}

}  // namespace nidevice_grpc

#endif /* NIDEVICE_GRPC_SESSION_RESOURCE_REPOSITORY_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/session_utilities_service.cpp sha256=5ebcfe3304cbc68de6ba14ca36fab8ba6e9fb98496422f632972989c6fe274a7 bytes=3442 -->
## FILE: source/server/session_utilities_service.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/session_utilities_service.cpp`
- sha256: `5ebcfe3304cbc68de6ba14ca36fab8ba6e9fb98496422f632972989c6fe274a7`
- bytes: 3442

````cpp
#include "session_utilities_service.h"

#include <algorithm>

namespace nidevice_grpc {

SessionUtilitiesService::SessionUtilitiesService(SessionRepository* session_repository, DeviceEnumerator* device_enumerator, SoftwareEnumerator* software_enumerator)
    : session_repository_(session_repository), device_enumerator_(device_enumerator), software_enumerator_(software_enumerator)
{
}

::grpc::Status SessionUtilitiesService::EnumerateDevices(::grpc::ServerContext* context, const EnumerateDevicesRequest* request, EnumerateDevicesResponse* response)
{
  return device_enumerator_->enumerate_devices(response->mutable_devices());
}

::grpc::Status SessionUtilitiesService::EnumerateInstalledSoftware(::grpc::ServerContext* context, const EnumerateInstalledSoftwareRequest* request, EnumerateInstalledSoftwareResponse* response)
{
  return software_enumerator_->enumerate_installed_software(context, request->include_hidden_packages(), response->mutable_software());
}

::grpc::Status SessionUtilitiesService::Reserve(::grpc::ServerContext* context, const ReserveRequest* request, ReserveResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ::grpc::Status status;
  bool reserved = session_repository_->reserve(context, request->reservation_id(), request->client_id(), status);
  response->set_is_reserved(reserved);
  return status;
}

::grpc::Status SessionUtilitiesService::IsReservedByClient(::grpc::ServerContext* context, const IsReservedByClientRequest* request, IsReservedByClientResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  bool is_reserved = session_repository_->is_reserved_by_client(request->reservation_id(), request->client_id());
  response->set_is_reserved(is_reserved);
  return ::grpc::Status::OK;
}

::grpc::Status SessionUtilitiesService::Unreserve(::grpc::ServerContext* context, const UnreserveRequest* request, UnreserveResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  bool is_unreserved = session_repository_->unreserve(request->reservation_id(), request->client_id());
  response->set_is_unreserved(is_unreserved);
  return ::grpc::Status::OK;
}

::grpc::Status SessionUtilitiesService::ResetServer(::grpc::ServerContext* context, const ResetServerRequest* request, ResetServerResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  bool is_server_reset = session_repository_->reset_server();
  response->set_is_server_reset(is_server_reset);

  {
    std::unique_lock<std::shared_mutex> lock(observers_mutex_);
    for (auto observer : observers_)
    {
      observer->on_server_reset();
    }
  }

  return ::grpc::Status::OK;
}

void SessionUtilitiesService::register_observer(ServerResetObserverInterface* observer)
{
  std::unique_lock<std::shared_mutex> lock(observers_mutex_);
  if (std::find(observers_.begin(), observers_.end(), observer) == observers_.end())
  {
    observers_.push_back(observer);
  }
}

void SessionUtilitiesService::unregister_observer(ServerResetObserverInterface* observer)
{
  std::unique_lock<std::shared_mutex> lock(observers_mutex_);
  auto i = std::find(observers_.begin(), observers_.end(), observer);
  if (i != observers_.end())
  {
    observers_.erase(i);
  }
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/session_utilities_service.h sha256=804000a1121b47663f53135594735ccded4f3e71e9c8b78130eed8e76fd84327 bytes=2194 -->
## FILE: source/server/session_utilities_service.h

- repository: `ni/grpc-device`
- source_path: `source/server/session_utilities_service.h`
- sha256: `804000a1121b47663f53135594735ccded4f3e71e9c8b78130eed8e76fd84327`
- bytes: 2194

````c
#ifndef NIDEVICE_GRPC_SESSION_UTILITIES_SERVICE
#define NIDEVICE_GRPC_SESSION_UTILITIES_SERVICE

#include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>
#include <list>
#include <session.grpc.pb.h>
#include <shared_mutex>

#include "device_enumerator.h"
#include "server_reset_observer_interface.h"
#include "server_reset_observer_registrar_interface.h"
#include "session_repository.h"
#include "software_enumerator.h"

namespace nidevice_grpc {

class SessionUtilitiesService final : public SessionUtilities::Service, public ServerResetObserverRegistrarInterface {
 public:
  SessionUtilitiesService(SessionRepository* session_repository, DeviceEnumerator* device_enumerator, SoftwareEnumerator* software_enumerator);

  ::grpc::Status EnumerateDevices(::grpc::ServerContext* context, const EnumerateDevicesRequest* request, EnumerateDevicesResponse* response) override;
  ::grpc::Status EnumerateInstalledSoftware(::grpc::ServerContext* context, const EnumerateInstalledSoftwareRequest* request, EnumerateInstalledSoftwareResponse* response) override;
  ::grpc::Status Reserve(::grpc::ServerContext* context, const ReserveRequest* request, ReserveResponse* response) override;
  ::grpc::Status IsReservedByClient(::grpc::ServerContext* context, const IsReservedByClientRequest* request, IsReservedByClientResponse* response) override;
  ::grpc::Status Unreserve(::grpc::ServerContext* context, const UnreserveRequest* request, UnreserveResponse* response) override;
  ::grpc::Status ResetServer(::grpc::ServerContext* context, const ResetServerRequest* request, ResetServerResponse* response) override;

  void register_observer(ServerResetObserverInterface* observer) override;
  void unregister_observer(ServerResetObserverInterface* observer) override;

 private:
  SessionRepository* session_repository_;
  DeviceEnumerator* device_enumerator_;
  SoftwareEnumerator* software_enumerator_;
  std::list<ServerResetObserverInterface*> observers_;
  std::shared_mutex observers_mutex_;
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SESSION_UTILITIES_SERVICE
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/session_utilities_service_registrar.cpp sha256=597baeea97fd9054fe94a7724dfc6cc98833ca5f6982e135840fa216c91e4703 bytes=1938 -->
## FILE: source/server/session_utilities_service_registrar.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/session_utilities_service_registrar.cpp`
- sha256: `597baeea97fd9054fe94a7724dfc6cc98833ca5f6982e135840fa216c91e4703`
- bytes: 1938

````cpp
#include "session_utilities_service_registrar.h"

#include "device_enumerator.h"
#include "session_utilities_service.h"
#include "software_enumerator.h"
#include "syscfg_library.h"

namespace nidevice_grpc {
namespace {
struct SessionUtilitiesLibraryAndService {
  SessionUtilitiesLibraryAndService(
    const std::shared_ptr<SessionRepository>& session_repository,
    ServerResetObserverRegistrarInterface** serverResetObserverRegistrar)
      : session_repository(session_repository),
        library(),
        device_enumerator(&library),
        software_enumerator(&library),
        service(session_repository.get(), &device_enumerator, &software_enumerator)
  {
    service.register_observer(&device_enumerator);
    *serverResetObserverRegistrar = &service;
  }

  ~SessionUtilitiesLibraryAndService()
  {
    // This code is currently unreachable, but if the call to wait exits, we need to clean up the service here.
    session_repository->reset_server();
    service.unregister_observer(&device_enumerator);
    device_enumerator.clear_syscfg_session();
    software_enumerator.clear_syscfg_session();
  }

  std::shared_ptr<SessionRepository> session_repository;
  SysCfgLibrary library;
  DeviceEnumerator device_enumerator;
  SoftwareEnumerator software_enumerator;
  SessionUtilitiesService service;
};
}  // namespace

std::shared_ptr<void> register_session_utilities_service(
    grpc::ServerBuilder& server_builder,
    const std::shared_ptr<nidevice_grpc::SessionRepository>& session_repository,
    ServerResetObserverRegistrarInterface** serverResetObserverRegistrar)
{
  auto library_and_service = std::make_shared<SessionUtilitiesLibraryAndService>(session_repository, serverResetObserverRegistrar);
  auto& service_ref = library_and_service->service;
  server_builder.RegisterService(&service_ref);
  return library_and_service;
}
}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/session_utilities_service_registrar.h sha256=a68f1ff1fd8465a5aae1633fd2ff4404234c7b3e6b06b4aaf70338774ae647bd bytes=655 -->
## FILE: source/server/session_utilities_service_registrar.h

- repository: `ni/grpc-device`
- source_path: `source/server/session_utilities_service_registrar.h`
- sha256: `a68f1ff1fd8465a5aae1633fd2ff4404234c7b3e6b06b4aaf70338774ae647bd`
- bytes: 655

````c
#ifndef NIDEVICE_GRPC_DEVICE_SESSION_UTILITIES_SERVICE_REGISTRAR_H
#define NIDEVICE_GRPC_DEVICE_SESSION_UTILITIES_SERVICE_REGISTRAR_H

#include <memory>

#include "server_reset_observer_registrar_interface.h"
#include "session_repository.h"

namespace grpc {
class ServerBuilder;
}

namespace nidevice_grpc {
std::shared_ptr<void> register_session_utilities_service(
    grpc::ServerBuilder& server_builder,
    const std::shared_ptr<nidevice_grpc::SessionRepository>& session_repository,
    ServerResetObserverRegistrarInterface** serverResetObserverRegistrar);
}
#endif  // NIDEVICE_GRPC_DEVICE_SESSION_UTILITIES_SERVICE_REGISTRAR_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/shared_library.cpp sha256=b345cd90c898160e662a0c8aa06efde535e052c7b2d730abcbb0b858dcdc913d bytes=1864 -->
## FILE: source/server/shared_library.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/shared_library.cpp`
- sha256: `b345cd90c898160e662a0c8aa06efde535e052c7b2d730abcbb0b858dcdc913d`
- bytes: 1864

````cpp
#include "shared_library.h"

#if defined(__GNUC__)
  #include <dlfcn.h>
#endif

namespace nidevice_grpc {

SharedLibrary::SharedLibrary()
    : handle_(nullptr)
{
}

SharedLibrary::SharedLibrary(const char* library_name)
    : library_name_(library_name), handle_(nullptr)
{
}

SharedLibrary::SharedLibrary(const SharedLibrary& other)
    : library_name_(other.library_name_), handle_(nullptr)
{
  if (other.handle_) {
    load();
  }
}

SharedLibrary::~SharedLibrary()
{
  unload();
}

void SharedLibrary::swap(SharedLibrary& other)
{
  library_name_.swap(other.library_name_);
  std::swap(handle_, other.handle_);
}

bool SharedLibrary::is_loaded() const
{
  return handle_ != nullptr;
}

LibraryHandle SharedLibrary::get_handle() const
{
  return handle_;
}

void SharedLibrary::load()
{
  if (handle_) {
    return;
  }
  if (!library_name_.empty()) {
#if defined(_MSC_VER)
    handle_ = ::LoadLibraryA(library_name_.c_str());
#else
    handle_ = ::dlopen(library_name_.c_str(), RTLD_NOW | RTLD_GLOBAL);
#endif
  }
}

void SharedLibrary::unload()
{
  if (handle_) {
#if defined(_MSC_VER)
    ::FreeLibrary(handle_);
#else
    ::dlclose(handle_);
#endif
    handle_ = nullptr;
  }
}

const void* SharedLibrary::get_function_pointer(const char* name) const
{
  if (!handle_) {
    return nullptr;
  }
#if defined(_MSC_VER)
  return ::GetProcAddress(handle_, name);
#else
  return ::dlsym(handle_, name);
#endif
}

bool SharedLibrary::function_exists(const char* name) const
{
  return get_function_pointer(name) != nullptr;
}

void SharedLibrary::set_library_name(const char* library_name)
{
  if (!is_loaded())
    library_name_ = library_name;
}

std::string SharedLibrary::get_library_name() const
{
  return library_name_;
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/shared_library.h sha256=957a93461dd0e32306f01d4471a7bd55eedb6b113bff7380919d31660eef3a4e bytes=1905 -->
## FILE: source/server/shared_library.h

- repository: `ni/grpc-device`
- source_path: `source/server/shared_library.h`
- sha256: `957a93461dd0e32306f01d4471a7bd55eedb6b113bff7380919d31660eef3a4e`
- bytes: 1905

````c
#ifndef NIDEVICE_GRPC_SHARED_LIBRARY
#define NIDEVICE_GRPC_SHARED_LIBRARY

#include "shared_library_interface.h"
#include <stdexcept>
#include <string>

#include "exceptions.h"

#if defined(_MSC_VER)
  #include <Windows.h>
#endif

namespace nidevice_grpc {

#ifdef _MSC_VER
typedef HMODULE LibraryHandle;
#else
typedef void* LibraryHandle;
#endif

class LibraryLoadException : public NonDriverException {
 public:
  LibraryLoadException(const std::string& message) : NonDriverException(::grpc::StatusCode::NOT_FOUND, message) {}
  LibraryLoadException(const char* message) : NonDriverException(::grpc::StatusCode::NOT_FOUND, message) {}
  LibraryLoadException(const LibraryLoadException& other) : NonDriverException(other) {}
};

class SessionException : public NonDriverException {
 public:
  SessionException(const std::string& message) : NonDriverException(::grpc::StatusCode::INVALID_ARGUMENT, message) {}
  SessionException(const char* message) : NonDriverException(::grpc::StatusCode::INVALID_ARGUMENT, message) {}
  SessionException(const SessionException& other) : NonDriverException(other) {}
};

class SharedLibrary : public SharedLibraryInterface {
 public:
  SharedLibrary();
  SharedLibrary(const char* library_name);
  SharedLibrary(const SharedLibrary& other);
  virtual ~SharedLibrary();

  void swap(SharedLibrary& other);
  bool is_loaded() const override;
  LibraryHandle get_handle() const override;
  void load() override;
  void unload() override;
  const void* get_function_pointer(const char* name) const override;
  bool function_exists(const char* name) const override;
  void set_library_name(const char* library_name) override;
  std::string get_library_name() const override;

 private:
  std::string library_name_;
  LibraryHandle handle_;
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SHARED_LIBRARY
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/shared_library_interface.h sha256=48e6ed03affd326e23a2564ebce345866812d5a7bd2f3ca1ef71d5228ff8a6d1 bytes=1149 -->
## FILE: source/server/shared_library_interface.h

- repository: `ni/grpc-device`
- source_path: `source/server/shared_library_interface.h`
- sha256: `48e6ed03affd326e23a2564ebce345866812d5a7bd2f3ca1ef71d5228ff8a6d1`
- bytes: 1149

````c
#ifndef NIDEVICE_GRPC_SHARED_LIBRARY_INTERFACE
#define NIDEVICE_GRPC_SHARED_LIBRARY_INTERFACE

#include <stdexcept>
#include <string>

#include "exceptions.h"

namespace nidevice_grpc {

#ifdef _MSC_VER
typedef HMODULE LibraryHandle;
#else
typedef void* LibraryHandle;
#endif

class SharedLibraryInterface {
 public:
  virtual ~SharedLibraryInterface() = default;

  // not included because we have to templatize the class in order to make this virtual
  // and then can't specify a pointer to SharedLibraryInterface for our Library classes (because we would need a template specifier)
  // virtual void swap(SharedLibraryT& other) = 0;
  virtual bool is_loaded() const = 0;
  virtual LibraryHandle get_handle() const = 0;
  virtual void load() = 0;
  virtual void unload() = 0;
  virtual const void* get_function_pointer(const char* name) const = 0;
  virtual bool function_exists(const char* name) const = 0;
  virtual void set_library_name(const char* library_name) = 0;
  virtual std::string get_library_name() const = 0;

};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SHARED_LIBRARY_INTERFACE
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/software_enumerator.cpp sha256=3a0cfd0d40fa195ac4a072bb3fde32b5d63c476654f100f7a10b1ab5b15a101c bytes=2503 -->
## FILE: source/server/software_enumerator.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/software_enumerator.cpp`
- sha256: `3a0cfd0d40fa195ac4a072bb3fde32b5d63c476654f100f7a10b1ab5b15a101c`
- bytes: 2503

````cpp
#include "software_enumerator.h"

namespace nidevice_grpc {

SoftwareEnumerator::SoftwareEnumerator(SysCfgLibraryInterface* library)
    : SysCfgSessionHandler(library)
{
}

SoftwareEnumerator::~SoftwareEnumerator()
{
}

// Provides a list of installed software on a server under localhost. This internally uses the
// "NI System Configuration API". If it is not currently installed, it can be downloaded from this page:
// https://www.ni.com/en-in/support/downloads/drivers/download.system-configuration.html.
::grpc::Status SoftwareEnumerator::enumerate_installed_software(
    ::grpc::ServerContext* context,
    bool include_hidden_packages,
    google::protobuf::RepeatedPtrField<SoftwareProperties>* software)
{
  NISysCfgStatus status = NISysCfg_OK;
  NISysCfgSessionHandle session = NULL;
  NISysCfgEnumSoftwareComponentHandle installedComps = NULL;
  unsigned int numInstalledComps = 0;
  char package_id[NISYSCFG_SIMPLE_STRING_LENGTH] = "";
  char package_version[NISYSCFG_SIMPLE_STRING_LENGTH] = "";
  char product_name[NISYSCFG_SIMPLE_STRING_LENGTH] = "";

  try {
    auto library = get_syscfg_library_interface();
    if (NISysCfg_Succeeded(status = open_or_get_localhost_syscfg_session(&session))) {
      auto item_types = include_hidden_packages ? NISysCfgIncludeItemsAllVisibleAndHidden : NISysCfgIncludeItemsAllVisible;
      if (NISysCfg_Succeeded(status = library->GetInstalledSoftwareComponents(session, item_types, NISysCfgBoolFalse, &installedComps))) {
        if (NISysCfg_Succeeded(status = library->ResetEnumeratorGetCount(installedComps, &numInstalledComps)) && numInstalledComps > 0) {
          while (NISysCfg_Succeeded(status) && (status = library->NextComponentInfo(installedComps, package_id, package_version, product_name, NULL, NULL)) == NISysCfg_OK) {
            SoftwareProperties* properties = software->Add();
            properties->set_package_id(package_id);
            properties->set_package_version(package_version);
            properties->set_product_name(product_name);
          }
        }

        library->CloseHandle(installedComps);
      }
    }
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }

  if (NISysCfg_Failed(status)) {
    std::string description(kSoftwareEnumerationFailedMessage);
    return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
  }

  return ::grpc::Status::OK;
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/software_enumerator.h sha256=a35b6b3102e5bca3d5ab3bf6b0a8ed25ed4de150c2ea6b4fb0c58ca416e82a04 bytes=958 -->
## FILE: source/server/software_enumerator.h

- repository: `ni/grpc-device`
- source_path: `source/server/software_enumerator.h`
- sha256: `a35b6b3102e5bca3d5ab3bf6b0a8ed25ed4de150c2ea6b4fb0c58ca416e82a04`
- bytes: 958

````c
#ifndef NIDEVICE_GRPC_SOFTWARE_ENUMERATOR_H
#define NIDEVICE_GRPC_SOFTWARE_ENUMERATOR_H

#include <grpcpp/grpcpp.h>
#include <nisyscfg.h>
#include <session.grpc.pb.h>
#include <session_utilities.grpc.pb.h>

#include <shared_mutex>

#include "converters.h"
#include "syscfg_library_interface.h"
#include "syscfg_session_handler.h"

namespace nidevice_grpc {

static const char* kSoftwareEnumerationFailedMessage = "The NI System Configuration API was unable to enumerate the installed software.";

class SoftwareEnumerator : public SysCfgSessionHandler {
 public:
  SoftwareEnumerator(SysCfgLibraryInterface* library);
  virtual ~SoftwareEnumerator();

  ::grpc::Status enumerate_installed_software(
      ::grpc::ServerContext* context,
      bool includeHiddenPackages,
      google::protobuf::RepeatedPtrField<SoftwareProperties>* software);
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SOFTWARE_ENUMERATOR_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/syscfg_library.cpp sha256=b7c3fd83e955237ec1fc72498ed9efb4997a3d6ec0694e7c55d4ccac9f372787 bytes=7563 -->
## FILE: source/server/syscfg_library.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/syscfg_library.cpp`
- sha256: `b7c3fd83e955237ec1fc72498ed9efb4997a3d6ec0694e7c55d4ccac9f372787`
- bytes: 7563

````cpp
#include "syscfg_library.h"

#define GET_POINTER(ptrs, lib, name) \
  ptrs.name = reinterpret_cast<name##Ptr>(lib.get_function_pointer("NISysCfg" #name));

namespace nidevice_grpc {

SysCfgLibrary::SysCfgLibrary()
    : shared_library_(kSysCfgApiLibraryName)
{
  shared_library_.load();
  memset(&function_pointers_, 0, sizeof(function_pointers_));
  if (!shared_library_.is_loaded()) {
    return;
  }
  GET_POINTER(function_pointers_, shared_library_, InitializeSession);
  GET_POINTER(function_pointers_, shared_library_, CloseHandle);
  GET_POINTER(function_pointers_, shared_library_, CreateFilter);
  GET_POINTER(function_pointers_, shared_library_, SetFilterPropertyV);
  GET_POINTER(function_pointers_, shared_library_, FindHardware);
  GET_POINTER(function_pointers_, shared_library_, NextResource);
  GET_POINTER(function_pointers_, shared_library_, GetResourceIndexedProperty);
  GET_POINTER(function_pointers_, shared_library_, GetResourceProperty);
  GET_POINTER(function_pointers_, shared_library_, SetResourcePropertyV);
  GET_POINTER(function_pointers_, shared_library_, SaveResourceChanges);
  GET_POINTER(function_pointers_, shared_library_, FreeDetailedString);
  GET_POINTER(function_pointers_, shared_library_, GetInstalledSoftwareComponents);
  GET_POINTER(function_pointers_, shared_library_, ResetEnumeratorGetCount);
  GET_POINTER(function_pointers_, shared_library_, NextComponentInfo);
}

SysCfgLibrary::~SysCfgLibrary()
{
}

std::string SysCfgLibrary::get_library_name() const
{
  return shared_library_.get_library_name();
}

bool SysCfgLibrary::is_library_loaded() const
{
  return shared_library_.is_loaded();
}

NISysCfgStatus SysCfgLibrary::InitializeSession(
    const char* target_name,
    const char* username,
    const char* password,
    NISysCfgLocale language,
    NISysCfgBool force_property_refresh,
    unsigned int connect_timeout_msec,
    NISysCfgEnumExpertHandle* expert_enum_handle,
    NISysCfgSessionHandle* session_handle)
{
  if (!function_pointers_.InitializeSession) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.InitializeSession(
      target_name,
      username,
      password,
      language,
      force_property_refresh,
      connect_timeout_msec,
      expert_enum_handle,
      session_handle);
}

NISysCfgStatus SysCfgLibrary::CloseHandle(void* syscfg_handle)
{
  if (!function_pointers_.CloseHandle) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.CloseHandle(syscfg_handle);
}

NISysCfgStatus SysCfgLibrary::CreateFilter(
    NISysCfgSessionHandle session_handle,
    NISysCfgFilterHandle* filter_handle)
{
  if (!function_pointers_.CreateFilter) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.CreateFilter(session_handle, filter_handle);
}

NISysCfgStatus SysCfgLibrary::SetFilterProperty(
    NISysCfgFilterHandle filter_handle,
    NISysCfgFilterProperty property_ID,
    ...)
{
  if (!function_pointers_.SetFilterPropertyV) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  va_list args;
  NISysCfgStatus status;
  va_start(args, property_ID);
  status = function_pointers_.SetFilterPropertyV(filter_handle, property_ID, args);
  va_end(args);
  return status;
}

NISysCfgStatus SysCfgLibrary::FindHardware(
    NISysCfgSessionHandle session_handle,
    NISysCfgFilterMode filter_mode,
    NISysCfgFilterHandle filter_handle,
    const char* expert_names,
    NISysCfgEnumResourceHandle* resource_enum_handle)
{
  if (!function_pointers_.FindHardware) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.FindHardware(session_handle, filter_mode, filter_handle, expert_names, resource_enum_handle);
}

NISysCfgStatus SysCfgLibrary::NextResource(
    NISysCfgSessionHandle session_handle,
    NISysCfgEnumResourceHandle resource_enum_handle,
    NISysCfgResourceHandle* resource_handle)
{
  if (!function_pointers_.NextResource) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.NextResource(session_handle, resource_enum_handle, resource_handle);
}

NISysCfgStatus SysCfgLibrary::GetResourceIndexedProperty(
    NISysCfgResourceHandle resource_handle,
    NISysCfgIndexedProperty property_ID,
    unsigned int index,
    void* value)
{
  if (!function_pointers_.GetResourceIndexedProperty) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.GetResourceIndexedProperty(resource_handle, property_ID, index, value);
}

NISysCfgStatus SysCfgLibrary::GetResourceProperty(
    NISysCfgResourceHandle resource_handle,
    NISysCfgResourceProperty property_ID,
    void* value)
{
  if (!function_pointers_.GetResourceProperty) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.GetResourceProperty(resource_handle, property_ID, value);
}

NISysCfgStatus SysCfgLibrary::SetResourceProperty(
    NISysCfgResourceHandle resource_handle,
    NISysCfgResourceProperty property_ID,
    ...)
{
  if (!function_pointers_.SetResourcePropertyV) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  va_list args;
  NISysCfgStatus status;
  va_start(args, property_ID);
  status = function_pointers_.SetResourcePropertyV(resource_handle, property_ID, args);
  va_end(args);
  return status;
}

NISysCfgStatus SysCfgLibrary::SaveResourceChanges(
    NISysCfgResourceHandle resource_handle,
    NISysCfgBool* changes_require_restart,
    char** detailed_result)
{
  if (!function_pointers_.SaveResourceChanges) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.SaveResourceChanges(resource_handle, changes_require_restart, detailed_result);
}

NISysCfgStatus SysCfgLibrary::FreeDetailedString(char str[])
{
  if (!function_pointers_.FreeDetailedString) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.FreeDetailedString(str);
}

NISysCfgStatus SysCfgLibrary::GetInstalledSoftwareComponents(
    NISysCfgSessionHandle session_handle,
    NISysCfgIncludeComponentTypes item_types,
    NISysCfgBool cached,
    NISysCfgEnumSoftwareComponentHandle* component_enum_handle)
{
  if (!function_pointers_.GetInstalledSoftwareComponents) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.GetInstalledSoftwareComponents(session_handle, item_types, cached, component_enum_handle);
}

NISysCfgStatus SysCfgLibrary::ResetEnumeratorGetCount(
    void* enum_handle,
    unsigned int* count)
{
  if (!function_pointers_.ResetEnumeratorGetCount) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.ResetEnumeratorGetCount(enum_handle, count);
}

NISysCfgStatus SysCfgLibrary::NextComponentInfo(
    NISysCfgEnumSoftwareComponentHandle component_enum_handle,
    char* id,
    char* version,
    char* title,
    NISysCfgComponentType* itemType,
    char** detailedDescription)
{
  if (!function_pointers_.NextComponentInfo) {
    throw LibraryLoadException(kSysCfgApiNotInstalledMessage);
  }
  return function_pointers_.NextComponentInfo(component_enum_handle, id, version, title, itemType, detailedDescription);
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/syscfg_library.h sha256=fb29fcb98b4dd06e17449569fd8cdee6d2e311537b91e245c28f5c093f578b64 bytes=4991 -->
## FILE: source/server/syscfg_library.h

- repository: `ni/grpc-device`
- source_path: `source/server/syscfg_library.h`
- sha256: `fb29fcb98b4dd06e17449569fd8cdee6d2e311537b91e245c28f5c093f578b64`
- bytes: 4991

````c
#ifndef NIDEVICE_GRPC_SYSCFG_LIBRARY_H
#define NIDEVICE_GRPC_SYSCFG_LIBRARY_H

#include <grpcpp/grpcpp.h>
#include <nisyscfg.h>

#include "shared_library.h"
#include "syscfg_library_interface.h"

namespace nidevice_grpc {

#if defined(_MSC_VER)
static const char* kSysCfgApiLibraryName = "nisyscfg.dll";
#else
static const char* kSysCfgApiLibraryName = "libnisyscfg.so";
#endif

static const char* kSysCfgApiNotInstalledMessage = "The NI System Configuration API is not installed on the server.";

class SysCfgLibrary : public SysCfgLibraryInterface {
 public:
  SysCfgLibrary();
  virtual ~SysCfgLibrary();

  std::string get_library_name() const;
  bool is_library_loaded() const;
  NISysCfgStatus InitializeSession(
      const char* target_name,
      const char* username,
      const char* password,
      NISysCfgLocale language,
      NISysCfgBool force_property_refresh,
      unsigned int connect_timeout_msec,
      NISysCfgEnumExpertHandle* expert_enum_handle,
      NISysCfgSessionHandle* session_handle);
  NISysCfgStatus CloseHandle(
      void* syscfg_handle);
  NISysCfgStatus CreateFilter(
      NISysCfgSessionHandle session_handle,
      NISysCfgFilterHandle* filter_handle);
  NISysCfgStatus SetFilterProperty(
      NISysCfgFilterHandle filter_handle,
      NISysCfgFilterProperty property_ID,
      ...);
  NISysCfgStatus FindHardware(
      NISysCfgSessionHandle session_handle,
      NISysCfgFilterMode filter_mode,
      NISysCfgFilterHandle filter_handle,
      const char* expert_names,
      NISysCfgEnumResourceHandle* resource_enum_handle);
  NISysCfgStatus NextResource(
      NISysCfgSessionHandle session_handle,
      NISysCfgEnumResourceHandle resource_enum_handle,
      NISysCfgResourceHandle* resource_handle);
  NISysCfgStatus GetResourceIndexedProperty(
      NISysCfgResourceHandle resource_handle,
      NISysCfgIndexedProperty property_ID,
      unsigned int index,
      void* value);
  NISysCfgStatus GetResourceProperty(
      NISysCfgResourceHandle resource_handle,
      NISysCfgResourceProperty property_ID,
      void* value);
  NISysCfgStatus SetResourceProperty(
      NISysCfgResourceHandle resource_handle,
      NISysCfgResourceProperty property_ID,
      ...);
  NISysCfgStatus SaveResourceChanges(
      NISysCfgResourceHandle resource_handle,
      NISysCfgBool* changes_require_restart,
      char** detailed_result);
  NISysCfgStatus FreeDetailedString(
      char str[]);
  NISysCfgStatus GetInstalledSoftwareComponents(
      NISysCfgSessionHandle session_handle,
      NISysCfgIncludeComponentTypes item_types,
      NISysCfgBool cached,
      NISysCfgEnumSoftwareComponentHandle* component_enum_handle);
  NISysCfgStatus ResetEnumeratorGetCount(
      void* enumHandle,
      unsigned int* count);
  NISysCfgStatus NextComponentInfo(
      NISysCfgEnumSoftwareComponentHandle component_enum_handle,
      char* id,
      char* version,
      char* title,
      NISysCfgComponentType* itemType,
      char** detailedDescription);

 private:
  using InitializeSessionPtr = decltype(&NISysCfgInitializeSession);
  using CloseHandlePtr = decltype(&NISysCfgCloseHandle);
  using CreateFilterPtr = decltype(&NISysCfgCreateFilter);
  using SetFilterPropertyVPtr = decltype(&NISysCfgSetFilterPropertyV);
  using FindHardwarePtr = decltype(&NISysCfgFindHardware);
  using NextResourcePtr = decltype(&NISysCfgNextResource);
  using GetResourceIndexedPropertyPtr = decltype(&NISysCfgGetResourceIndexedProperty);
  using GetResourcePropertyPtr = decltype(&NISysCfgGetResourceProperty);
  using SetResourcePropertyVPtr = decltype(&NISysCfgSetResourcePropertyV);
  using SaveResourceChangesPtr = decltype(&NISysCfgSaveResourceChanges);
  using FreeDetailedStringPtr = decltype(&NISysCfgFreeDetailedString);
  using GetInstalledSoftwareComponentsPtr = decltype(&NISysCfgGetInstalledSoftwareComponents);
  using ResetEnumeratorGetCountPtr = decltype(&NISysCfgResetEnumeratorGetCount);
  using NextComponentInfoPtr = decltype(&NISysCfgNextComponentInfo);

  typedef struct FunctionPointers {
    InitializeSessionPtr InitializeSession;
    CloseHandlePtr CloseHandle;
    CreateFilterPtr CreateFilter;
    SetFilterPropertyVPtr SetFilterPropertyV;
    FindHardwarePtr FindHardware;
    NextResourcePtr NextResource;
    GetResourceIndexedPropertyPtr GetResourceIndexedProperty;
    GetResourcePropertyPtr GetResourceProperty;
    SetResourcePropertyVPtr SetResourcePropertyV;
    SaveResourceChangesPtr SaveResourceChanges;
    FreeDetailedStringPtr FreeDetailedString;
    GetInstalledSoftwareComponentsPtr GetInstalledSoftwareComponents;
    ResetEnumeratorGetCountPtr ResetEnumeratorGetCount;
    NextComponentInfoPtr NextComponentInfo;
  } FunctionLoadStatus;

  SharedLibrary shared_library_;
  FunctionPointers function_pointers_;
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SYSCFG_LIBRARY_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/syscfg_library_interface.h sha256=06f699b991a466b76db9d3935fcdeb7932f9b1572bd5649eaafe2bb28d9c3158 bytes=2901 -->
## FILE: source/server/syscfg_library_interface.h

- repository: `ni/grpc-device`
- source_path: `source/server/syscfg_library_interface.h`
- sha256: `06f699b991a466b76db9d3935fcdeb7932f9b1572bd5649eaafe2bb28d9c3158`
- bytes: 2901

````c
#ifndef NIDEVICE_GRPC_SYSCFG_LIBRARY_INTERFACE_H
#define NIDEVICE_GRPC_SYSCFG_LIBRARY_INTERFACE_H

#include <grpcpp/grpcpp.h>
#include <nisyscfg.h>

namespace nidevice_grpc {

class SysCfgLibraryInterface {
 public:
  virtual ~SysCfgLibraryInterface() {}

  virtual NISysCfgStatus InitializeSession(
      const char* target_name,
      const char* username,
      const char* password,
      NISysCfgLocale language,
      NISysCfgBool force_property_refresh,
      unsigned int connect_timeout_msec,
      NISysCfgEnumExpertHandle* expert_enum_handle,
      NISysCfgSessionHandle* session_handle) = 0;
  virtual NISysCfgStatus CloseHandle(
      void* syscfg_handle) = 0;
  virtual NISysCfgStatus CreateFilter(
      NISysCfgSessionHandle session_handle,
      NISysCfgFilterHandle* filter_handle) = 0;
  virtual NISysCfgStatus SetFilterProperty(
      NISysCfgFilterHandle filter_handle,
      NISysCfgFilterProperty property_ID,
      ...) = 0;
  virtual NISysCfgStatus FindHardware(
      NISysCfgSessionHandle session_handle,
      NISysCfgFilterMode filter_mode,
      NISysCfgFilterHandle filter_handle,
      const char* expert_names,
      NISysCfgEnumResourceHandle* resource_enum_handle) = 0;
  virtual NISysCfgStatus NextResource(
      NISysCfgSessionHandle session_handle,
      NISysCfgEnumResourceHandle resource_enum_handle,
      NISysCfgResourceHandle* resource_handle) = 0;
  virtual NISysCfgStatus GetResourceIndexedProperty(
      NISysCfgResourceHandle resource_handle,
      NISysCfgIndexedProperty property_ID,
      unsigned int index,
      void* value) = 0;
  virtual NISysCfgStatus GetResourceProperty(
      NISysCfgResourceHandle resource_handle,
      NISysCfgResourceProperty property_ID,
      void* value) = 0;
  virtual NISysCfgStatus SetResourceProperty(
      NISysCfgResourceHandle resource_handle,
      NISysCfgResourceProperty property_ID,
      ...) = 0;
  virtual NISysCfgStatus SaveResourceChanges(
      NISysCfgResourceHandle resource_handle,
      NISysCfgBool* changes_require_restart,
      char** detailed_result) = 0;
  virtual NISysCfgStatus FreeDetailedString(
      char str[]) = 0;
  virtual NISysCfgStatus GetInstalledSoftwareComponents(
      NISysCfgSessionHandle session_handle,
      NISysCfgIncludeComponentTypes item_types,
      NISysCfgBool cached,
      NISysCfgEnumSoftwareComponentHandle* component_enum_handle) = 0;
  virtual NISysCfgStatus ResetEnumeratorGetCount(
      void* enumHandle,
      unsigned int* count) = 0;
  virtual NISysCfgStatus NextComponentInfo(
      NISysCfgEnumSoftwareComponentHandle component_enum_handle,
      char* id,
      char* version,
      char* title,
      NISysCfgComponentType* itemType,
      char** detailedDescription) = 0;
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SYSCFG_LIBRARY_INTERFACE_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/syscfg_resource_accessor.cpp sha256=c91965d1ab228628f9e5fd4be0fd7a6b4699f2837b2122c2e4753cf00cf47d1e bytes=3017 -->
## FILE: source/server/syscfg_resource_accessor.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/syscfg_resource_accessor.cpp`
- sha256: `c91965d1ab228628f9e5fd4be0fd7a6b4699f2837b2122c2e4753cf00cf47d1e`
- bytes: 3017

````cpp
#include "syscfg_resource_accessor.h"

#include "converters.h"

namespace nidevice_restricted_grpc {

SysCfgResourceAccessor::SysCfgResourceAccessor(nidevice_grpc::SysCfgLibraryInterface* library)
    : SysCfgSessionHandler(library) {}

SysCfgResourceAccessor::~SysCfgResourceAccessor()
{
}

::grpc::Status SysCfgResourceAccessor::access_syscfg_resource_by_device_id_filter(
    ::grpc::ServerContext* context,
    const DeviceId& device_id,
    const char* access_failed_message,
    std::function<NISysCfgStatus(nidevice_grpc::SysCfgLibraryInterface*, NISysCfgResourceHandle, bool*)> syscfg_resource_action_func)
{
  NISysCfgStatus status = NISysCfg_OK;
  NISysCfgSessionHandle session = NULL;
  NISysCfgFilterHandle filter = NULL;
  NISysCfgEnumResourceHandle resources_handle = NULL;
  NISysCfgResourceHandle resource = NULL;
  bool no_hardware_found = false;

  try {
    auto library = get_syscfg_library_interface();
    if (NISysCfg_Succeeded(status = open_or_get_localhost_syscfg_session(&session))) {
      if (NISysCfg_Succeeded(status = library->CreateFilter(session, &filter))) {
        library->SetFilterProperty(filter, NISysCfgFilterPropertyIsDevice, NISysCfgBoolTrue);
        library->SetFilterProperty(filter, NISysCfgFilterPropertyUserAlias, device_id.name().c_str());
        library->SetFilterProperty(filter, NISysCfgFilterPropertySerialNumber, device_id.serial_number().c_str());
        library->SetFilterProperty(filter, NISysCfgFilterPropertyProductId, device_id.product_id());
        if (NISysCfg_Succeeded(status = library->FindHardware(session, NISysCfgFilterModeMatchValuesAll, filter, NULL, &resources_handle))) {
          if ((status = library->NextResource(session, resources_handle, &resource)) == NISysCfg_OK) {
            bool save_changes = false;
            if (NISysCfg_Succeeded(status = syscfg_resource_action_func(library, resource, &save_changes))) {
              if (save_changes) {
                NISysCfgBool changes_require_restart = NISysCfgBoolFalse;
                char* detailed_changes = nullptr;
                status = library->SaveResourceChanges(resource, &changes_require_restart, &detailed_changes);
                library->FreeDetailedString(detailed_changes);
              }
            }
            library->CloseHandle(resource);
          }
          else {
            no_hardware_found = true;
          }
          library->CloseHandle(resources_handle);
        }
        library->CloseHandle(filter);
      }
    }
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }

  if (NISysCfg_Failed(status)) {
    std::string description(access_failed_message);
    return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
  }

  if (no_hardware_found) {
    return ::grpc::Status(::grpc::StatusCode::NOT_FOUND, access_failed_message);
  }

  return ::grpc::Status::OK;
}
}  // namespace nidevice_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/syscfg_resource_accessor.h sha256=05f3140d30d168dfd3f7328ff61ca18126840de3bb7741ecd25f68259233ad46 bytes=1000 -->
## FILE: source/server/syscfg_resource_accessor.h

- repository: `ni/grpc-device`
- source_path: `source/server/syscfg_resource_accessor.h`
- sha256: `05f3140d30d168dfd3f7328ff61ca18126840de3bb7741ecd25f68259233ad46`
- bytes: 1000

````c
#ifndef NIDEVICE_GRPC_SYSCFG_RESOURCE_ACCESSOR_H
#define NIDEVICE_GRPC_SYSCFG_RESOURCE_ACCESSOR_H

#include <shared_mutex>

#include "deviceid_restricted.grpc.pb.h"
#include "server_reset_observer_interface.h"
#include "shared_library.h"
#include "syscfg_library_interface.h"
#include "syscfg_session_handler.h"

namespace nidevice_restricted_grpc {

class SysCfgResourceAccessor : public nidevice_grpc::SysCfgSessionHandler {
 public:
  SysCfgResourceAccessor(nidevice_grpc::SysCfgLibraryInterface* library);
  virtual ~SysCfgResourceAccessor();

 protected:
  ::grpc::Status access_syscfg_resource_by_device_id_filter(
      ::grpc::ServerContext* context,
      const DeviceId& device_id,
      const char* access_failed_message,
      std::function<NISysCfgStatus(nidevice_grpc::SysCfgLibraryInterface*, NISysCfgResourceHandle, bool*)> syscfg_resource_action_func);
};

};      // namespace nidevice_restricted_grpc
#endif  // NIDEVICE_GRPC_SYSCFG_RESOURCE_ACCESSOR_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/syscfg_session_handler.cpp sha256=a0a13a7912195fa57cb0e72b1fcaff0253b99627a83dd36ab7e0c26232b2f045 bytes=1742 -->
## FILE: source/server/syscfg_session_handler.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/syscfg_session_handler.cpp`
- sha256: `a0a13a7912195fa57cb0e72b1fcaff0253b99627a83dd36ab7e0c26232b2f045`
- bytes: 1742

````cpp
#include "syscfg_session_handler.h"

#include "converters.h"

namespace nidevice_grpc {

SysCfgSessionHandler::SysCfgSessionHandler(SysCfgLibraryInterface* library)
    : library_(library), syscfg_session_(nullptr)
{
}

SysCfgSessionHandler::~SysCfgSessionHandler()
{
  // Caller is expected to close the syscfg session before calling destructor.
}

// Sets cached NISysCfgSession to passed session handle.
// Sets null to cached session after failed initialization.
// Returns status of getting valid cached_syscfg_session is successful.
NISysCfgStatus SysCfgSessionHandler::open_or_get_localhost_syscfg_session(NISysCfgSessionHandle* session)
{
  std::unique_lock<std::shared_mutex> lock(session_mutex_);
  NISysCfgStatus status = NISysCfg_OK;
  if (!syscfg_session_) {
    if (NISysCfg_Failed(status = library_->InitializeSession(kLocalHostTargetName, NULL, NULL, NISysCfgLocaleDefault, NISysCfgBoolTrue, kConnectionTimeoutMilliSec, NULL, &syscfg_session_))) {
      return status;
    }
  }
  *session = syscfg_session_;
  return status;
}

// Calls Closehandle to clear sysconfig session and sets cached_syscfg_session to null.
void SysCfgSessionHandler::clear_syscfg_session()
{
  std::unique_lock<std::shared_mutex> lock(session_mutex_);
  if (syscfg_session_) {
    library_->CloseHandle(syscfg_session_);
    syscfg_session_ = nullptr;
  }
}

// Returns status of cached session.
bool SysCfgSessionHandler::is_session_open()
{
  return syscfg_session_ != nullptr;
}

void SysCfgSessionHandler::on_server_reset()
{
  clear_syscfg_session();
}

SysCfgLibraryInterface* SysCfgSessionHandler::get_syscfg_library_interface()
{
  return library_;
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/syscfg_session_handler.h sha256=637cd727ca4b4bdf2004d71267368b76f9d5df00fad43a2f05b1d854ee19aa13 bytes=1118 -->
## FILE: source/server/syscfg_session_handler.h

- repository: `ni/grpc-device`
- source_path: `source/server/syscfg_session_handler.h`
- sha256: `637cd727ca4b4bdf2004d71267368b76f9d5df00fad43a2f05b1d854ee19aa13`
- bytes: 1118

````c
#ifndef NIDEVICE_GRPC_SYSCFG_SESSION_HANDLER_H
#define NIDEVICE_GRPC_SYSCFG_SESSION_HANDLER_H

#include <shared_mutex>

#include "server_reset_observer_interface.h"
#include "shared_library.h"
#include "syscfg_library_interface.h"

namespace nidevice_grpc {

static const char* kLocalHostTargetName = "localhost";
static const char* kNetworkExpertName = "network";
static const int kConnectionTimeoutMilliSec = 10000;

class SysCfgSessionHandler : public ServerResetObserverInterface {
 public:
  SysCfgSessionHandler(SysCfgLibraryInterface* library);
  virtual ~SysCfgSessionHandler();

  virtual NISysCfgStatus open_or_get_localhost_syscfg_session(NISysCfgSessionHandle* session);
  virtual void clear_syscfg_session();
  virtual bool is_session_open();

  void on_server_reset() override;

 protected:
  virtual SysCfgLibraryInterface* get_syscfg_library_interface();

 private:
  SysCfgLibraryInterface* library_;
  std::shared_mutex session_mutex_;
  NISysCfgSessionHandle syscfg_session_;
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_SYSCFG_SESSION_HANDLER_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/tls_config_loader.cpp sha256=264bc5e69fff76d2796adbd11e7ee13d5007cae0b7ea1df1e751ffcc24930d4d bytes=6046 -->
## FILE: source/server/tls_config_loader.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/tls_config_loader.cpp`
- sha256: `264bc5e69fff76d2796adbd11e7ee13d5007cae0b7ea1df1e751ffcc24930d4d`
- bytes: 6046

````cpp
#include "tls_config_loader.h"

#include <stdexcept>
#include <string>

#include "nierr_Status.h"

namespace {
// RAII wrapper for nierr_Status. nierr_Status is a plain C struct with no
// destructor, so the json heap buffer must be freed explicitly. This wrapper
// does that automatically and provides helper methods matching the repo
// convention (see NIErrStatusOutputConverter in
// source/custom/nimxlcterminaladaptor_restricted_converters.h).
struct NiErrStatusGuard {
  nierr_Status status;
  NiErrStatusGuard() { nierr_Status_initialize(&status); }
  ~NiErrStatusGuard() { nierr_Status_jsonFree(&status); }
  NiErrStatusGuard(const NiErrStatusGuard&) = delete;
  NiErrStatusGuard& operator=(const NiErrStatusGuard&) = delete;
  bool is_fatal() const { return nierr_Status_isFatal(&status); }
  // Returns the json detail string, or empty string if none.
  std::string detail() const { return status.json ? status.json : ""; }
  // Allows passing &guard directly to C functions expecting nierr_Status*.
  nierr_Status* operator&() { return &status; }
};
}  // namespace

namespace nidevice_grpc {

#if defined(_MSC_VER)
static const char* kNiTlsConfigLibraryName = "nitlsconfig.dll";
#else
static const char* kNiTlsConfigLibraryName = "libnitlsconfig.so";
#endif

TlsConfigLoader::TlsConfigLoader()
    : library_(kNiTlsConfigLibraryName),
      is_available_(false),
      read_certificate_mode_(nullptr),
      read_client_mode_(nullptr),
      read_certificate_chain_contents_(nullptr),
      read_certificate_key_contents_(nullptr),
      read_trusted_certificates_contents_(nullptr)
{
  library_.load();
  if (!library_.is_loaded()) {
    return;
  }

  read_certificate_mode_ = reinterpret_cast<ReadCertificateModeFunc>(
      library_.get_function_pointer("nitlsconfig_server_readCertificateMode"));
  read_client_mode_ = reinterpret_cast<ReadClientModeFunc>(
      library_.get_function_pointer("nitlsconfig_server_readClientMode"));
  read_certificate_chain_contents_ = reinterpret_cast<ReadContentsFunc>(
      library_.get_function_pointer("nitlsconfig_server_readCertificateChainContents"));
  read_certificate_key_contents_ = reinterpret_cast<ReadContentsFunc>(
      library_.get_function_pointer("nitlsconfig_server_readCertificateKeyContents"));
  read_trusted_certificates_contents_ = reinterpret_cast<ReadContentsFunc>(
      library_.get_function_pointer("nitlsconfig_server_readTrustedCertificatesContents"));

  is_available_ = read_certificate_mode_ != nullptr &&
      read_client_mode_ != nullptr &&
      read_certificate_chain_contents_ != nullptr &&
      read_certificate_key_contents_ != nullptr &&
      read_trusted_certificates_contents_ != nullptr;
}

bool TlsConfigLoader::is_available() const
{
  return is_available_;
}

ServerSecurityConfiguration TlsConfigLoader::get_server_credentials(
    const std::string& service_name) const
{
  if (!is_available_) {
    throw std::runtime_error("ni-tls-config: library is not available");
  }

  uint32_t mode = CertificateMode_Unknown;
  NiErrStatusGuard s;
  // The int32_t return value mirrors nierr_Status.code; checking is_fatal() on
  // the status struct is sufficient and also captures the JSON detail string.
  (void)read_certificate_mode_(service_name.c_str(), &mode, &s);
  if (s.is_fatal()) {
    throw std::runtime_error(
        "ni-tls-config: failed to read certificate mode for service: " +
        service_name + (s.detail().empty() ? "" : (" (" + s.detail() + ")")));
  }

  switch (static_cast<CertificateMode>(mode)) {
    case CertificateMode_Disabled:
      return ServerSecurityConfiguration();
    case CertificateMode_Unmanaged:
    case CertificateMode_ManagedSelfSigned:
      break;
    case CertificateMode_Unknown:
    default:
      throw std::runtime_error(
          "ni-tls-config: unsupported certificate mode " +
          std::to_string(mode) + " for service: " + service_name);
  }

  auto cert_chain = read_contents(
      service_name, read_certificate_chain_contents_, "certificate chain");
  auto cert_key = read_contents(
      service_name, read_certificate_key_contents_, "certificate key");

  uint32_t client_mode = ClientMode_Unknown;
  NiErrStatusGuard sc;
  (void)read_client_mode_(service_name.c_str(), &client_mode, &sc);
  if (sc.is_fatal()) {
    throw std::runtime_error(
        "ni-tls-config: failed to read client mode for service: " +
        service_name + (sc.detail().empty() ? "" : (" (" + sc.detail() + ")")));
  }

  std::string root_cert;
  if (client_mode != ClientMode_Disabled) {
    root_cert = read_contents(
        service_name, read_trusted_certificates_contents_, "trusted certificates");
  }

  return ServerSecurityConfiguration(cert_chain, cert_key, root_cert);
}

std::string TlsConfigLoader::read_contents(
    const std::string& service_name,
    ReadContentsFunc func,
    const char* description) const
{
  constexpr size_t kBufferSize = 4096;
  std::string contents(kBufferSize, '\0');
  size_t actual_size = 0;

  NiErrStatusGuard s;
  (void)func(service_name.c_str(), contents.data(), kBufferSize, &actual_size, &s);
  if (s.is_fatal()) {
    throw std::runtime_error(
        std::string("ni-tls-config: failed to read ") + description +
        " contents for service: " + service_name +
        (s.detail().empty() ? "" : (" (" + s.detail() + ")")));
  }

  if (actual_size > kBufferSize) {
    contents.resize(actual_size, '\0');
    NiErrStatusGuard s2;
    (void)func(service_name.c_str(), contents.data(), actual_size, &actual_size, &s2);
    if (s2.is_fatal()) {
      throw std::runtime_error(
          std::string("ni-tls-config: failed to read ") + description +
          " contents for service: " + service_name +
          (s2.detail().empty() ? "" : (" (" + s2.detail() + ")")));
    }
  }

  contents.resize(std::strlen(contents.c_str()));
  return contents;
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/tls_config_loader.h sha256=c6eabeda6f95eb975ee33928ded36a4cbc8a9eb2a3893e2fa65ee3cf601da580 bytes=2362 -->
## FILE: source/server/tls_config_loader.h

- repository: `ni/grpc-device`
- source_path: `source/server/tls_config_loader.h`
- sha256: `c6eabeda6f95eb975ee33928ded36a4cbc8a9eb2a3893e2fa65ee3cf601da580`
- bytes: 2362

````c
#ifndef NIDEVICE_GRPC_TLS_CONFIG_LOADER_H
#define NIDEVICE_GRPC_TLS_CONFIG_LOADER_H

#include <string>

#include "nierr_Status.h"
#include "server_security_configuration.h"
#include "shared_library.h"

namespace nidevice_grpc {

// Dynamically loads the nitlsconfig library (if installed) and reads per-service
// TLS configuration from it.  The library is never a link-time dependency.
class TlsConfigLoader {
 public:
  TlsConfigLoader();
  ~TlsConfigLoader() = default;

  TlsConfigLoader(const TlsConfigLoader&) = delete;
  TlsConfigLoader& operator=(const TlsConfigLoader&) = delete;

  // Returns true only when the library was found and all function pointers resolved.
  bool is_available() const;

  // Reads TLS configuration for the given service and returns the corresponding
  // server credentials.  When certificate_mode is Disabled, returns insecure
  // credentials.  Throws std::runtime_error on any other failure.
  ServerSecurityConfiguration get_server_credentials(const std::string& service_name) const;

 private:
  // C enum values that mirror the nitlsconfig ABI (do not rename/reorder).
  enum CertificateMode {
    CertificateMode_Disabled = 0,
    CertificateMode_Unmanaged = 1,
    CertificateMode_ManagedSelfSigned = 2,
    CertificateMode_Unknown = 255,
  };

  // C enum values that mirror the nitlsconfig ABI (do not rename/reorder).
  enum ClientMode {
    ClientMode_Disabled = 0,
    ClientMode_Unmanaged = 1,
    ClientMode_ManagedSelfSigned = 2,
    ClientMode_Unknown = 255,
  };

  using ReadCertificateModeFunc = int32_t (*)(const char*, uint32_t*, nierr_Status*);
  using ReadClientModeFunc = int32_t (*)(const char*, uint32_t*, nierr_Status*);
  using ReadContentsFunc = int32_t (*)(const char*, char*, size_t, size_t*, nierr_Status*);

  std::string read_contents(
      const std::string& service_name,
      ReadContentsFunc func,
      const char* description) const;

  SharedLibrary library_;
  bool is_available_;

  ReadCertificateModeFunc read_certificate_mode_;
  ReadClientModeFunc read_client_mode_;
  ReadContentsFunc read_certificate_chain_contents_;
  ReadContentsFunc read_certificate_key_contents_;
  ReadContentsFunc read_trusted_certificates_contents_;
};

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_TLS_CONFIG_LOADER_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/version.h.in sha256=57d99825d5610674315fe70c09ab95fe75e0cfab084528f17eef7adecbf1f6c6 bytes=436 -->
## FILE: source/server/version.h.in

- repository: `ni/grpc-device`
- source_path: `source/server/version.h.in`
- sha256: `57d99825d5610674315fe70c09ab95fe75e0cfab084528f17eef7adecbf1f6c6`
- bytes: 436

````text
#ifndef NIDEVICE_GRPC_VERSION_H
#define NIDEVICE_GRPC_VERSION_H

namespace nidevice_grpc {

static constexpr const char* kNiDeviceGrpcFileVersion = "@PROJECT_VERSION_MAJOR@.@PROJECT_VERSION_MINOR@.@PROJECT_VERSION_PATCH@.0";
static constexpr const char* kNiDeviceGrpcOriginalFileName = "ni_grpc_device_server.exe";
static constexpr const char* kNiDeviceGrpcBranchName = "@GIT_BRANCH@";

}

#endif // NIDEVICE_GRPC_VERSION_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/version.rc.in sha256=3d34a5fd794468a55a43ddcb5f11b3800a52aa88b47fe236a501fc7577d3f450 bytes=1439 -->
## FILE: source/server/version.rc.in

- repository: `ni/grpc-device`
- source_path: `source/server/version.rc.in`
- sha256: `3d34a5fd794468a55a43ddcb5f11b3800a52aa88b47fe236a501fc7577d3f450`
- bytes: 1439

````text
#if defined(__MINGW64__) || defined(__MINGW32__)
    // MinGW-w64, MinGW
    #if defined(__has_include) && __has_include(<winres.h>)
        #include <winres.h>
    #else
        #include <afxres.h>
        #include <winresrc.h>
    #endif
#else
    // MSVC, Windows SDK
    #include <winres.h>
#endif

LANGUAGE LANG_ENGLISH, SUBLANG_ENGLISH_US
#pragma code_page(1252)

VS_VERSION_INFO VERSIONINFO
    FILEVERSION @PROJECT_VERSION_MAJOR@,@PROJECT_VERSION_MINOR@,@PROJECT_VERSION_PATCH@,0
    PRODUCTVERSION @PROJECT_VERSION_MAJOR@,@PROJECT_VERSION_MINOR@,0,0
    FILEFLAGSMASK 0x3fL
#ifdef _DEBUG
    FILEFLAGS 0x1L
#else
    FILEFLAGS 0x0L
#endif
    FILEOS 0x40004L
    FILETYPE 0x1L
    FILESUBTYPE 0x0L
BEGIN
    BLOCK "StringFileInfo"
    BEGIN
        BLOCK "040904b0"
        BEGIN
            VALUE "CompanyName", "NI"
            VALUE "FileDescription", ""
            VALUE "FileVersion", "@PROJECT_VERSION_MAJOR@.@PROJECT_VERSION_MINOR@.@PROJECT_VERSION_PATCH@.0"
            VALUE "InternalName", ""
            VALUE "LegalCopyright", "Copyright (C) 2021 - 2022"
            VALUE "OriginalFilename", "ni_grpc_device_server.exe"
            VALUE "ProductName", "NI gRPC Device Server"
            VALUE "ProductVersion", "@PROJECT_VERSION_MAJOR@.@PROJECT_VERSION_MINOR@"
        END
    END
    BLOCK "VarFileInfo"
    BEGIN
        VALUE "Translation", 0x409, 1200
    END
END
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/windows/console_ctrl_handler.cpp sha256=14e9fc2eef69ac98d057db3448e069173d32390dcd4e1197aba67b52cc69c334 bytes=1714 -->
## FILE: source/server/windows/console_ctrl_handler.cpp

- repository: `ni/grpc-device`
- source_path: `source/server/windows/console_ctrl_handler.cpp`
- sha256: `14e9fc2eef69ac98d057db3448e069173d32390dcd4e1197aba67b52cc69c334`
- bytes: 1714

````cpp
#include "console_ctrl_handler.h"

#include "../logging.h"

#include <string>
#include <Windows.h>

namespace nidevice_grpc {

static stop_callback signal_stop = nullptr;

static BOOL WINAPI console_ctrl_handler(DWORD dwCtrlType)
{
  const char* signal_description = "?";
  switch (dwCtrlType)
  {
  case CTRL_C_EVENT:
    signal_description = "ctrl-c";
    break;
  case CTRL_BREAK_EVENT:
    signal_description = "ctrl-break";
    break;
  case CTRL_CLOSE_EVENT:
    signal_description = "close";
    break;
  case CTRL_LOGOFF_EVENT:
    signal_description = "logoff";
    break;
  case CTRL_SHUTDOWN_EVENT:
    signal_description = "shutdown";
    break;
  default:
    break;
  }

  logging::log(logging::Level_Info, "Received %s signal, stopping server.", signal_description);
  if (signal_stop) {
    signal_stop();

    // Wait up to 10 seconds for the server to stop. When either main() or this handler returns,
    // the process will exit.
    Sleep(10000);
  }
  return TRUE;
}

static std::string get_error_message(DWORD error)
{
  char buffer[1024] = "";
  if (!FormatMessageA(FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS, nullptr, error, 0, buffer, sizeof(buffer), nullptr)) {
    return "unknown Win32 error " + std::to_string(error);
  }
  return buffer;
}

void set_console_ctrl_handler(stop_callback signal_stop_)
{
  signal_stop = signal_stop_;
  if (!SetConsoleCtrlHandler(&console_ctrl_handler, TRUE /*Add*/)) {
    DWORD error = GetLastError();
    logging::log(logging::Level_Error, "Failed to register console control handler: %s",
      get_error_message(error).c_str());
  }
}

}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/server/windows/console_ctrl_handler.h sha256=de41cb52fb2da778a6427dcf313aba046a8ef97047ee20b298d6599bd90faaf3 bytes=333 -->
## FILE: source/server/windows/console_ctrl_handler.h

- repository: `ni/grpc-device`
- source_path: `source/server/windows/console_ctrl_handler.h`
- sha256: `de41cb52fb2da778a6427dcf313aba046a8ef97047ee20b298d6599bd90faaf3`
- bytes: 333

````c
#ifndef NIDEVICE_GRPC_WINDOWS_SET_CONSOLE_CTRL_HANDLER_H
#define NIDEVICE_GRPC_WINDOWS_SET_CONSOLE_CTRL_HANDLER_H

namespace nidevice_grpc {

typedef void (*stop_callback)();

void set_console_ctrl_handler(stop_callback stop);

}  // namespace nidevice_grpc

#endif  // NIDEVICE_GRPC_WINDOWS_SET_CONSOLE_CTRL_HANDLER_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/assets/certs/test_client_self_signed_crt.pem sha256=48797c73f072e73ba275ef5853b1963f11afd4ae902a9e17b488e93104edc605 bytes=118 -->
## FILE: source/tests/assets/certs/test_client_self_signed_crt.pem

- repository: `ni/grpc-device`
- source_path: `source/tests/assets/certs/test_client_self_signed_crt.pem`
- sha256: `48797c73f072e73ba275ef5853b1963f11afd4ae902a9e17b488e93104edc605`
- bytes: 118

````text
-----BEGIN CERTIFICATE-----
This is not a real certificate and is only used for testing.
-----END CERTIFICATE-----
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/assets/certs/test_server_privatekey.pem sha256=c2054d8f6ec957742f108ae8082103a928a31a11025c0a8e5a28ec74307ae512 bytes=115 -->
## FILE: source/tests/assets/certs/test_server_privatekey.pem

- repository: `ni/grpc-device`
- source_path: `source/tests/assets/certs/test_server_privatekey.pem`
- sha256: `c2054d8f6ec957742f108ae8082103a928a31a11025c0a8e5a28ec74307ae512`
- bytes: 115

````text
-----BEGIN CERTIFICATE-----
This is not a real certificate and is only used for testing
-----END CERTIFICATE-----
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/assets/certs/test_server_self_signed_crt.pem sha256=9ed4533094af76c64ff033d87229069b4b7c2dc3728d0be301184a1d502a671e bytes=117 -->
## FILE: source/tests/assets/certs/test_server_self_signed_crt.pem

- repository: `ni/grpc-device`
- source_path: `source/tests/assets/certs/test_server_self_signed_crt.pem`
- sha256: `9ed4533094af76c64ff033d87229069b4b7c2dc3728d0be301184a1d502a671e`
- bytes: 117

````text
-----BEGIN CERTIFICATE-----
This is not a real certificate and is only used for testing
-----END CERTIFICATE-----
````
