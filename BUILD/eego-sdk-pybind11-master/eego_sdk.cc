// system
#include <ostream>
// pybind
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
// sdk
#include <eemagine/sdk/amplifier.h>
#include <eemagine/sdk/channel.h>
#include <eemagine/sdk/factory.h>
#include <eemagine/sdk/stream.h>
#include <eemagine/sdk/wrapper.cc>
///////////////////////////////////////////////////////////////////////////////
#if (EEGO_SDK_VERSION >= 46273)
#define HAVE_CASCADING
#endif
#if (EEGO_SDK_VERSION >= 57164)
#define HAVE_POWERSTATE
#define HAVE_TRIGGEROUT
#endif
///////////////////////////////////////////////////////////////////////////////
namespace {
//
std::ostream &operator<<(std::ostream &out,
                         const eemagine::sdk::channel::channel_type &t) {
  switch (t) {
  case eemagine::sdk::channel::channel_type::none:
    out << "none";
    break;
  case eemagine::sdk::channel::channel_type::reference:
    out << "ref";
    break;
  case eemagine::sdk::channel::channel_type::bipolar:
    out << "bip";
    break;
  case eemagine::sdk::channel::channel_type::trigger:
    out << "trg";
    break;
  case eemagine::sdk::channel::channel_type::sample_counter:
    out << "sc";
    break;
  case eemagine::sdk::channel::channel_type::impedance_reference:
    out << "ir";
    break;
  case eemagine::sdk::channel::channel_type::impedance_ground:
    out << "ig";
    break;
  case eemagine::sdk::channel::channel_type::accelerometer:
    out << "acc";
    break;
  case eemagine::sdk::channel::channel_type::gyroscope:
    out << "gyr";
    break;
  case eemagine::sdk::channel::channel_type::magnetometer:
    out << "mag";
    break;
  }
  return out;
}

//
// amplifier_wrapper
//
class amplifier_wrapper {
public:
  amplifier_wrapper(eemagine::sdk::amplifier *amp) : _amplifier(amp) {}

  eemagine::sdk::amplifier *detach() {
    auto rv(_amplifier.get());
    _amplifier.reset();
    return rv;
  }

  eemagine::sdk::stream *OpenEegStream_nomask(int rate, double ref_range,
                                              double bip_range) {
    return _amplifier->OpenEegStream(rate, ref_range, bip_range);
  }
  eemagine::sdk::stream *OpenEegStream_mask(int rate, double ref_range,
                                            double bip_range, uint64_t ref_mask,
                                            uint64_t bip_mask) {
    return _amplifier->OpenEegStream(rate, ref_range, bip_range, ref_mask,
                                     bip_mask);
  }
  eemagine::sdk::stream *OpenImpedanceStream_nomask() {
    return _amplifier->OpenImpedanceStream();
  }

  std::vector<eemagine::sdk::channel> getChannelList() const {
    return _amplifier->getChannelList();
  }
  std::string getSerialNumber() const { return _amplifier->getSerialNumber(); }
  int getFirmwareVersion() const { return _amplifier->getFirmwareVersion(); }
  std::string getType() const { return _amplifier->getType(); }
  std::vector<int> getSamplingRatesAvailable() const {
    return _amplifier->getSamplingRatesAvailable();
  }
  std::vector<double> getReferenceRangesAvailable() const {
    return _amplifier->getReferenceRangesAvailable();
  }
  std::vector<double> getBipolarRangesAvailable() const {
    return _amplifier->getBipolarRangesAvailable();
  }
#ifdef HAVE_POWERSTATE
  eemagine::sdk::amplifier::power_state getPowerState() const {
    return _amplifier->getPowerState();
  }
#endif
#ifdef HAVE_TRIGGEROUT
  void SetTriggerOutParameters(int channel, int duty_cycle,
                               float pulse_frequency, int pulse_count,
                               float burst_frequency, int burst_count) const {
    _amplifier->SetTriggerOutParameters(channel, duty_cycle, pulse_frequency,
                                        pulse_count, burst_frequency,
                                        burst_count);
  }
  void StartTriggerOut(const std::vector<int> &channel_list) const {
    _amplifier->StartTriggerOut(channel_list);
  }
  void StopTriggerOut(const std::vector<int> &channel_list) const {
    _amplifier->StopTriggerOut(channel_list);
  }
#endif

private:
  std::shared_ptr<eemagine::sdk::amplifier> _amplifier;
};

//
// factory_wrapper
//
class factory_wrapper {
public:
  eemagine::sdk::factory::version getVersion() const {
    return _factory.getVersion();
  }

  std::shared_ptr<amplifier_wrapper> getAmplifier() {
    return std::make_shared<amplifier_wrapper>(_factory.getAmplifier());
  }
  std::vector<std::shared_ptr<amplifier_wrapper>> getAmplifiers() {
    std::vector<std::shared_ptr<amplifier_wrapper>> rv;
    for (auto *a : _factory.getAmplifiers()) {
      rv.push_back(std::make_shared<amplifier_wrapper>(a));
    }
    return rv;
  }

#ifdef HAVE_CASCADING
  std::shared_ptr<amplifier_wrapper>
  createCascadedAmplifier(pybind11::list python_list) {
    std::vector<eemagine::sdk::amplifier *> amplifier_list;
    for (auto p : python_list) {
      auto a(p.cast<amplifier_wrapper>());
      amplifier_list.push_back(a.detach());
    }

    return std::make_shared<amplifier_wrapper>(
        _factory.createCascadedAmplifier(amplifier_list));
  }
#endif

private:
  eemagine::sdk::factory _factory;
};
} // namespace
///////////////////////////////////////////////////////////////////////////////
PYBIND11_MODULE(eego_sdk, m) {
  //
  // channel type
  //
  pybind11::enum_<eemagine::sdk::channel::channel_type>(m, "channel_type")
      .value("none", eemagine::sdk::channel::channel_type::none)
      .value("ref", eemagine::sdk::channel::channel_type::reference)
      .value("bip", eemagine::sdk::channel::channel_type::bipolar)
      .value("trg", eemagine::sdk::channel::channel_type::trigger)
      .value("sc", eemagine::sdk::channel::channel_type::sample_counter)
      .value("ir", eemagine::sdk::channel::channel_type::impedance_reference)
      .value("ig", eemagine::sdk::channel::channel_type::impedance_ground)
      .value("acc", eemagine::sdk::channel::channel_type::accelerometer)
      .value("gyr", eemagine::sdk::channel::channel_type::gyroscope)
      .value("mag", eemagine::sdk::channel::channel_type::magnetometer);

  //
  // channel
  //
  pybind11::class_<eemagine::sdk::channel>(m, "channel")
      .def("getIndex", &eemagine::sdk::channel::getIndex)
      .def("getType", &eemagine::sdk::channel::getType)
      .def("__repr__", [](const eemagine::sdk::channel &c) {
        std::ostringstream os;
        os << "channel(" << c.getIndex() << ", " << c.getType() << ")";
        return os.str();
      });

  //
  // buffer
  //
  pybind11::class_<eemagine::sdk::buffer>(m, "buffer",
                                          pybind11::buffer_protocol())
      .def("getChannelCount", &eemagine::sdk::buffer::getChannelCount)
      .def("getSampleCount", &eemagine::sdk::buffer::getSampleCount)
      .def("getSample", &eemagine::sdk::buffer::getSample)
      .def("__len__", [](const eemagine::sdk::buffer &b) { return b.size(); })
      .def(
          "__iter__",
          [](const eemagine::sdk::buffer &b) {
            auto base_address(&b.getSample(0, 0));
            return pybind11::make_iterator(base_address,
                                           base_address + b.size());
          },
          pybind11::keep_alive<0, 1>())
      .def_buffer([](eemagine::sdk::buffer &b) -> pybind11::buffer_info {
        const auto rows(b.getSampleCount());
        const auto cols(b.getChannelCount());
        return pybind11::buffer_info(
            b.data(),       // Pointer to buffer
            sizeof(double), // Size of one scalar
            pybind11::format_descriptor<
                double>::format(),  // Python struct-style format descriptor
            2,                      // Number of dimensions
            {rows, cols},           // Buffer dimensions
            {sizeof(double) * cols, // Strides (in bytes) for each index
             sizeof(double)});
      });

  ;

  //
  // stream
  //
  pybind11::class_<eemagine::sdk::stream,
                   std::shared_ptr<eemagine::sdk::stream>>(m, "stream")
      .def("getChannelList", &eemagine::sdk::stream::getChannelList)
      .def("getData", &eemagine::sdk::stream::getData);
  //
  // amplifier power state
  //
#ifdef HAVE_POWERSTATE
  pybind11::class_<eemagine::sdk::amplifier::power_state>(
      m, "amplifier.power_state")
      .def_readonly("is_powered",
                    &eemagine::sdk::amplifier::power_state::is_powered)
      .def_readonly("is_charging",
                    &eemagine::sdk::amplifier::power_state::is_charging)
      .def_readonly("charging_level",
                    &eemagine::sdk::amplifier::power_state::charging_level);
#endif
  //
  // amplifier
  //
  pybind11::class_<amplifier_wrapper, std::shared_ptr<amplifier_wrapper>>(
      m, "amplifier")
      .def("getType", &amplifier_wrapper::getType)
      .def("getFirmwareVersion", &amplifier_wrapper::getFirmwareVersion)
      .def("getSerialNumber", &amplifier_wrapper::getSerialNumber)
      .def("OpenEegStream", &amplifier_wrapper::OpenEegStream_nomask)
      .def("OpenEegStream", &amplifier_wrapper::OpenEegStream_mask)
      .def("OpenImpedanceStream",
           &amplifier_wrapper::OpenImpedanceStream_nomask)
      .def("getChannelList", &amplifier_wrapper::getChannelList)
      .def("getSamplingRatesAvailable",
           &amplifier_wrapper::getSamplingRatesAvailable)
      .def("getReferenceRangesAvailable",
           &amplifier_wrapper::getReferenceRangesAvailable)
      .def("getBipolarRangesAvailable",
           &amplifier_wrapper::getBipolarRangesAvailable)
#ifdef HAVE_POWERSTATE
      .def("getPowerState", &amplifier_wrapper::getPowerState)
#endif
#ifdef HAVE_TRIGGEROUT
      .def("SetTriggerOutParameters",
           &amplifier_wrapper::SetTriggerOutParameters)
      .def("StartTriggerOut", &amplifier_wrapper::StartTriggerOut)
      .def("StopTriggerOut", &amplifier_wrapper::StopTriggerOut)
#endif
      ;
  //
  // factory version
  //
  pybind11::class_<eemagine::sdk::factory::version>(m, "factory.version")
      .def_readonly("major", &eemagine::sdk::factory::version::major)
      .def_readonly("minor", &eemagine::sdk::factory::version::minor)
      .def_readonly("micro", &eemagine::sdk::factory::version::micro)
      .def_readonly("build", &eemagine::sdk::factory::version::build);

  //
  // factory
  //
  pybind11::class_<factory_wrapper>(m, "factory")
      .def(pybind11::init<>())
      .def("getVersion", &factory_wrapper::getVersion)
      .def("getAmplifier", &factory_wrapper::getAmplifier)
      .def("getAmplifiers", &factory_wrapper::getAmplifiers)
#ifdef HAVE_CASCADING
      .def("createCascadedAmplifier", &factory_wrapper::createCascadedAmplifier)
#endif
      ;
}
